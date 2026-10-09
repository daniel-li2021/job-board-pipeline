"""Build dashboard health from the run/state artifacts each pipeline already owns."""

from __future__ import annotations

import html
import recovery_policy
import json
import os
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import median
from typing import Any
from zoneinfo import ZoneInfo

from scripts.macos.local_source_gate import decision as local_schedule_decision
from state_io import decode_json_bytes

PIPELINES = {
    "board": ("ATS / Board (GitHub)", "board", "jobs.json"),
    "official": ("Big Company Official (GitHub)", "official_careers", "jobs.json"),
    "syncareer": ("Syncareer (GitHub)", "syncareer", "jobs.json"),
}
SEVERITY = {"Healthy": 0, "Partial": 1, "Warning": 1, "Stale": 2, "Problem": 3}


def _read(path: Path, default: Any) -> Any:
    try:
        return decode_json_bytes(path.read_bytes())
    except (OSError, ValueError, UnicodeDecodeError):
        return default


def _age_hours(value: str, now: datetime) -> float | None:
    try:
        stamp = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            stamp = stamp.replace(tzinfo=timezone.utc)
        return max(0.0, (now - stamp.astimezone(timezone.utc)).total_seconds() / 3600)
    except (TypeError, ValueError):
        return None


def _display_time(value: object) -> str:
    """Render report timestamps in Pacific time without changing JSON data."""
    try:
        stamp = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            stamp = stamp.replace(tzinfo=timezone.utc)
        pacific = stamp.astimezone(ZoneInfo("America/Los_Angeles"))
        return f"{int(pacific.strftime('%I'))}:{pacific:%M %p} PT, {pacific.day} {pacific:%B}"
    except (TypeError, ValueError):
        return str(value or "unknown")


def _pacific_day(value: object) -> object:
    stamp = recovery_policy.stamp(value)
    return stamp.astimezone(ZoneInfo("America/Los_Angeles")).date() if stamp else None


def _normalize_run_telemetry(run: dict[str, Any]) -> dict[str, Any]:
    """Mark legacy placeholder zeroes as unavailable without hiding measured zeroes."""
    normalized = dict(run)
    measured = float(run.get("latency_seconds", 0) or 0) > 0 or bool(run.get("batches"))
    normalized.setdefault("latency_measured", measured)
    normalized.setdefault("json_reliability_measured", measured)
    normalized.setdefault("batch_outcomes_measured", measured)
    return normalized


def _run_history(base: Path) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    latest: dict[str, dict[str, Any]] = {}
    history: list[dict[str, Any]] = []
    for key, (_label, folder, _store) in PIPELINES.items():
        records = [
            _normalize_run_telemetry(record)
            for record in list((_read(base / "output" / folder / "run_history.json", {}) or {}).get("runs") or [])
        ]
        if not records:
            for path in sorted((base / "output" / folder / "runs").glob("*_stats.json"))[-20:]:
                record = _read(path, {})
                if record:
                    records.append(_normalize_run_telemetry(record))
        records.sort(key=lambda item: str(item.get("run_at") or ""), reverse=True)
        history.extend({"pipeline": key, **record} for record in records)
        current = _read(base / "output" / folder / "latest_stats.json", {})
        if current:
            latest[key] = current
            if not any(current.get("run_at") == record.get("run_at") for record in records):
                llm = current.get("llm", {})
                history.append(_normalize_run_telemetry({
                    "pipeline": key, "run_at": current.get("run_at", ""),
                    "health": "degraded" if _failure_items(current.get("failures")) else "success",
                    "model": llm.get("model", ""), "reasoning_effort": llm.get("reasoning_effort", ""),
                    "scoring_version": llm.get("scoring_version", ""),
                    "jobs_scored": llm.get("scored", llm.get("llm", 0)),
                    "cache_reused": llm.get("reused", 0), "fallback_count": llm.get("retryable_fallbacks", 0),
                    "peer_reused": llm.get("peer_reused", 0),
                    "same_content_reused": llm.get("same_content_reused", 0),
                    "non_material_change_reused": llm.get("non_material_change_reused", 0),
                    "new_or_changed": llm.get("new_or_changed", 0),
                    "new_or_changed_reasons": llm.get("new_or_changed_reasons", {}),
                    "rescored_within_24h": llm.get("rescored_within_24h", 0),
                    "requests": llm.get("api_requests", 0), "input_tokens": llm.get("input_tokens", 0),
                    "output_tokens": llm.get("output_tokens", 0), "reasoning_tokens": llm.get("reasoning_tokens", 0),
                    "estimated_usd": llm.get("estimated_usd", 0), "output": current.get("output", {}),
                    "scrape_failure_sources": [
                        source for source, errors in ((current.get("failures") or {}).get("scrape") or {}).items()
                        if _failure_items(errors)
                    ] if key == "official" else [],
                    "funnel": current.get("funnel", {}), "enrichment": current.get("enrichment", {}),
                    "batches_total": llm.get("batches_total", 0), "batches_failed": llm.get("batches_failed", 0),
                    "primary_batches_total": llm.get("primary_batches_total", llm.get("batches_total", 0)),
                    "retry_splits": llm.get("retry_splits", 0), "retry_batches": llm.get("retry_batches", 0),
                    "retry_batches_succeeded": llm.get("retry_batches_succeeded", 0),
                    "retry_batches_failed": llm.get("retry_batches_failed", 0),
                    "latency_measured": "latency_seconds" in llm,
                    "json_reliability_measured": "json_results" in llm,
                    "batch_outcomes_measured": "batches_succeeded" in llm,
                }))
        elif records:
            latest[key] = records[0]
        if records:
            shown = [int(item.get("output", {}).get("shown", 0) or 0) for item in records[1:7]]
            if shown:
                latest[key]["recent_shown_median"] = median(shown)
        if key == "official":
            current_sources = [
                source for source, errors in ((current.get("failures") or {}).get("scrape") or {}).items()
                if _failure_items(errors)
            ] if current else None
            for item in (entry for entry in history if entry.get("pipeline") == "official"):
                if current_sources is not None and item.get("run_at") == current.get("run_at"):
                    item["scrape_failure_sources"] = current_sources
                sources = item.get("scrape_failure_sources")
                if sources is None and "failures" in item:
                    sources = [
                        source for source, errors in ((item.get("failures") or {}).get("scrape") or {}).items()
                        if _failure_items(errors)
                    ]
                    item["scrape_failure_sources"] = sources
                if sources is None:
                    item["health"] = "unknown"
                elif _official_scraper_count(base, sources) >= 5:
                    item["health"] = "degraded"
                else:
                    item["health"] = (
                        "limited" if sources or item.get("health") in {"degraded", "limited"} else "success"
                    )
    history.sort(key=lambda item: str(item.get("run_at") or ""), reverse=True)
    return latest, history[:40]


def _consecutive_degraded(history: list[dict[str, Any]], pipeline: str) -> int:
    count = 0
    for run in (item for item in history if item.get("pipeline") == pipeline):
        failed = run.get("health") == "degraded" or int(run.get("batches_failed", 0) or 0) > 0
        if not failed:
            break
        count += 1
    return count


def _consecutive_official_degraded(
    base: Path, history: list[dict[str, Any]], run: dict[str, Any], current_count: int
) -> int:
    if current_count < 5:
        return 0
    count = 1
    for previous in (item for item in history if item.get("pipeline") == "official"):
        if previous.get("run_at") == run.get("run_at"):
            continue
        sources = previous.get("scrape_failure_sources")
        if sources is None or _official_scraper_count(base, sources) < 5:
            break
        count += 1
    return count


def _official_scraper_streak(history: list[dict[str, Any]], source: str, cause: str,
                             current_stamp: str) -> int:
    count = 1
    for previous in (item for item in history if item.get("pipeline") == "official"):
        if previous.get("run_at") == current_stamp:
            continue
        if source not in (previous.get("scrape_failure_sources") or []):
            break
        prior_cause = (previous.get("scrape_failure_causes") or {}).get(source)
        if prior_cause != cause:
            break
        count += 1
    return count


def _consecutive_low_volume(history: list[dict[str, Any]], pipeline: str, baseline: float) -> int:
    count = 0
    for run in (
        item for item in history
        if item.get("pipeline") == pipeline and item.get("mode") != "matching_retry"
    ):
        if int((run.get("output") or {}).get("shown", 0) or 0) >= baseline * 0.3:
            break
        count += 1
    return count


def _llm_impact(run: dict[str, Any]) -> str:
    llm = run.get("llm") or {}
    total = int(llm.get("batches_total", 0) or 0)
    failed = int(llm.get("batches_failed", 0) or 0)
    attempted = int(llm.get("batches_attempted", total) or 0)
    skipped = int(llm.get("batches_skipped", 0) or 0)
    fallback = int(llm.get("retryable_fallbacks", 0) or 0)
    errors = _failure_items((run.get("failures") or {}).get("llm"))
    rate_limited = sum("429" in item for item in errors)
    if total and failed:
        reason = " with HTTP 429" if rate_limited == failed else ""
        reasons = list(dict.fromkeys(
            item.split(": ", 1)[1] if item.startswith("batch_") and ": " in item else item
            for item in errors
        ))
        reason_detail = (
            f" ({'; '.join(reasons[:2])}{'; more' if len(reasons) > 2 else ''})"
            if reasons else ""
        )
        scope = f"{failed}/{attempted} attempted" if skipped else f"{failed}/{total}"
        skipped_note = f"; {skipped} later batches skipped" if skipped else ""
        return f"{scope} LLM batches failed{reason}{reason_detail}{skipped_note}; {fallback} jobs used retryable rule fallback"
    return ""


def _failure_items(value: Any, prefix: str = "") -> list[str]:
    if isinstance(value, dict):
        return [
            item
            for key, child in value.items()
            for item in _failure_items(child, f"{prefix}{key}: ")
        ]
    if isinstance(value, (list, tuple, set)):
        return [item for child in value for item in _failure_items(child, prefix)]
    text = str(value or "").strip()
    return [f"{prefix}{text}"] if text else []


def _failure_summary(failures: Any) -> tuple[int, str]:
    items = _failure_items(failures)
    if not items:
        return 0, ""
    shown = "; ".join(items[:3])
    if len(items) > 3:
        shown += f"; +{len(items) - 3} more"
    return len(items), shown


def _short_cause(message: str) -> str:
    lowered = message.lower()
    for token, label in (("429", "429"), ("403", "403"), ("timed out", "timeout"),
                         ("timeout", "timeout"), ("404", "404")):
        if token in lowered:
            return label
    return "error"


def _official_failure_partition(base: Path, failures: Any) -> tuple[Any, list[str]]:
    """Remove configured limitations and the LinkedIn-company adapter from active failures."""
    if not isinstance(failures, dict):
        return failures, []
    registry = _read(base / "config" / "official_careers.json", {})
    link_only = {
        str(company.get("id") or "")
        for company in registry.get("companies", [])
        if isinstance(company, dict) and company.get("adapter") == "skip"
    }
    actionable = dict(failures)
    scrape = dict(actionable.get("scrape") or {})
    limited = sorted(key for key in scrape if key in link_only)
    for key in limited:
        scrape.pop(key, None)
    linkedin = scrape.pop("linkedin", None)
    if scrape:
        actionable["scrape"] = scrape
    else:
        actionable.pop("scrape", None)
    limitations = [
        f"Big Company Official: {len(limited)} configured link-only source(s) omitted from active failures ({', '.join(limited)})"
    ] if limited else []
    if linkedin:
        limitations.append(
            "Big Company Official: linkedin_company_official_adapter failures are ignored for overall health "
            f"({'; '.join(_failure_items(linkedin))})"
        )
    return actionable, limitations


def _official_scraper_count(base: Path, sources: list[str]) -> int:
    actionable, _limitations = _official_failure_partition(
        base, {"scrape": {source: ["failed"] for source in sources}}
    )
    return len(actionable.get("scrape", {}))


def _main_state(item: dict[str, Any]) -> str:
    """Three user-facing run states; retain the detailed status in JSON."""
    if not item.get("data_usable"):
        return "Failed"
    if (item.get("latest_attempt_status") in {"partial", "skipped_unavailable", "skipped_error", "blocked"}
            and "focused_coverage" not in (item.get("degradation_kinds") or [])):
        return "Partial"
    if (item.get("status") != "Healthy" or item.get("failure_count")
            or item.get("latest_attempt_status") in {"failed", "degraded", "limited"}):
        return "Partial"
    return "Healthy"


def _latest_run_panels(base: Path, latest: dict[str, dict[str, Any]],
                       components: dict[str, dict[str, Any]], local: dict[str, Any],
                       recovery: dict[str, Any]) -> dict[str, dict[str, str]]:
    """Build comparable summaries only from counters belonging to the latest attempts."""
    board = latest.get("board") or {}
    official = latest.get("official") or {}
    linkedin_state = local.get("linkedin") or {}
    indeed_state = local.get("indeed") or {}
    linkedin_snapshot = _read(base / "output" / "sources" / "linkedin.json", {}) or {}
    indeed_snapshot = _read(base / "output" / "sources" / "indeed.json", {}) or {}

    def observed(snapshot: dict[str, Any], state: dict[str, Any]) -> list[dict[str, Any]]:
        attempt = str(state.get("last_attempt_at") or "")
        if not attempt or attempt != str((snapshot.get("meta") or {}).get("scraped_at") or ""):
            return []
        rows = list(snapshot.get("jobs") or [])
        if state.get("status") == "partial":
            return [row for row in rows if row.get("verified_this_run")
                    and row.get("source_verified_at") == attempt]
        return rows

    linkedin_rows = observed(linkedin_snapshot, linkedin_state)
    linkedin_attempt = recovery_policy.stamp(linkedin_state.get("last_attempt_at"))
    recovery_at = recovery_policy.stamp(recovery.get("run_at"))
    linked_recovery_run = (recovery if linkedin_attempt and recovery_at
                           and timedelta(0) <= recovery_at - linkedin_attempt <= timedelta(hours=1) else {})
    new_now = earlier_today = 0
    for row in linkedin_rows:
        seen = recovery_policy.stamp(row.get("first_seen"))
        if seen and linkedin_attempt and seen >= linkedin_attempt:
            new_now += 1
        elif seen and linkedin_attempt and seen.astimezone(ZoneInfo("America/Los_Angeles")).date() == (
                linkedin_attempt.astimezone(ZoneInfo("America/Los_Angeles")).date()):
            earlier_today += 1
    older = len(linkedin_rows) - new_now - earlier_today
    # Follow-up recovery can replace Health detail stats; the snapshot retains initial stats.
    snapshot_meta = linkedin_snapshot.get("meta") or {}
    detail = (snapshot_meta.get("detail_enrichment", linkedin_state.get("detail_enrichment")) or {}
              if linkedin_state.get("last_attempt_at") == snapshot_meta.get("scraped_at") else {})
    recovery_detail = linked_recovery_run.get("linkedin_detail") or {}
    http_state = components["linkedin"].get("latest_run") or {}
    search = linkedin_state.get("search_collection") or {}
    linked_recovery = int(linked_recovery_run.get("linkedin_detail_recoveries", 0) or 0)
    other_recovery = int(linked_recovery_run.get("official_jds_recovered", 0) or 0) + int(
        linked_recovery_run.get("targeted_linkedin_detail_jds", 0) or 0)
    eligible = int(detail.get("eligible", 0) or 0)
    resolved = min(eligible, int(detail.get("jds_resolved", 0) or 0) + linked_recovery + other_recovery)
    remaining = max(0, eligible - resolved)
    deferred = min(remaining, sum(int(detail.get(key, 0) or 0) for key in
                                  ("official_deferred", "budget_deferred", "retry_deferred")))
    failed = min(remaining - deferred, int(detail.get("failed", 0) or 0))
    linkedin_same_attempt = bool(linkedin_state.get("last_attempt_at") and
                                 linkedin_state.get("last_attempt_at") ==
                                 (linkedin_snapshot.get("meta") or {}).get("scraped_at"))
    linkedin_jobs = (
        f"{int(linkedin_state.get('partial_collected_count', 0) or 0) if linkedin_state.get('status') == 'partial' else int(linkedin_state.get('last_attempt_count', 0) or 0):,} found · "
        f"{len(linkedin_rows):,} kept · {new_now:,} new this run · {earlier_today:,} seen earlier today · {older:,} already known"
        if linkedin_same_attempt else "Latest attempt and snapshot do not match; counts unavailable"
    )
    linkedin_panel = {
        "title": "LinkedIn Local", "status": components["linkedin"]["run_state"],
        "jobs": linkedin_jobs,
        "jd": (f"{eligible:,} fresh jobs needed JD · {resolved:,} resolved · {deferred:,} deferred · {failed:,} failed; "
               f"{int(detail.get('cache_reused', 0) or 0):,} cache reused · "
               f"{int(detail.get('detail_jds_fetched', 0) or 0):,} fetched from LinkedIn · "
               f"{linked_recovery + other_recovery:,} recovered later") if "eligible" in detail else
              f"Fresh JD need counts unavailable · {linked_recovery + other_recovery:,} recovered later",
        "requests": (f"Search {int(search.get('responses', 0) or 0)}/{int(search.get('requests', 0) or 0)} · "
                     f"LinkedIn detail {int(detail.get('responses', 0) or 0) + int(recovery_detail.get('responses', 0) or 0)}/"
                     f"{int(detail.get('requests', 0) or 0) + int(recovery_detail.get('requests', 0) or 0)} · "
                     f"Web recovery {int(linked_recovery_run.get('generic_jobs_processed', 0) or 0)} jobs / "
                     f"{int(linked_recovery_run.get('search_requests', 0) or 0)} searches / "
                     f"{int(linked_recovery_run.get('official_page_requests', 0) or 0)} pages"),
        "sources": (f"LinkedIn search {'cooldown/deferred' if http_state.get('search_cooldown_active') else 'rate limited' if http_state.get('search_429') else 'failed' if linkedin_state.get('status') in {'skipped_unavailable', 'skipped_error'} else 'healthy'}"
                    f"{' · focused coverage' if search.get('coverage_limited') else ''}"),
        "issue": (str(components["linkedin"].get("issue") or linkedin_state.get("reason") or "")
                  if components["linkedin"]["run_state"] != "Healthy" else ""),
        "note": ("Search 429 this run · " if http_state.get("search_429") else "No Search 429 this run · ")
                + ("Detail 429 this run · " if http_state.get("detail_429") else "No Detail 429 this run · ")
                + (f"search deferred until {_display_time(http_state.get('search_cooldown_until'))} · "
                   if http_state.get("search_cooldown_active") else "")
                + (f"detail cooldown until {_display_time(http_state.get('detail_cooldown_until'))} · "
                   if http_state.get("detail_cooldown_active") else "")
                + ("budget/deadline hit" if detail.get("budget_exhausted") or linked_recovery_run.get("deadline_reached")
                   else "no budget/deadline hit"),
    }

    online = board.get("online_recovery") or {}
    direct = (board.get("enrichment") or {}).get("direct") or {}
    attempted = int(online.get("jobs_processed", 0) or 0)
    direct_jds = int(direct.get("jds_resolved", 0) or 0)
    later_jds = int(online.get("jds_recovered", 0) or 0)
    ats_errors = [error for error in _failure_items((board.get("failures") or {}).get("discovery"))
                  if "Indeed discovery partial:" not in error]
    board_panel = {
        "title": "Online Board", "status": components["board"]["run_state"],
        "jobs": (f"{int((board.get('funnel') or {}).get('after_dedup', 0) or 0):,} current source jobs · "
                 f"{int((board.get('output') or {}).get('new_jobs', 0) or 0):,} new to Board · "
                 f"{int((board.get('output') or {}).get('shown', 0) or 0):,} A/B shown · "
                 f"{int((board.get('output') or {}).get('new_jobs_added', 0) or 0):,} newly added to A/B"),
        "jd": (f"{attempted:,} fresh jobs attempted · {direct_jds + later_jds:,} JDs resolved · "
               f"{max(0, attempted - direct_jds - later_jds):,} still missing; "
               f"{direct_jds:,} direct · {later_jds:,} follow-up recovery"),
        "requests": (f"{int(direct.get('http_requests', 0) or 0) + int(direct.get('scrapling_requests', 0) or 0):,} "
                     f"direct attempts · {int(online.get('search_requests', 0) or 0):,} searches · "
                     f"{int(online.get('page_requests', 0) or 0):,} official pages"),
        "sources": (f"ATS {'limited' if ats_errors else 'healthy'} · "
                    f"Indeed {components['indeed']['run_state'].lower()} · LinkedIn Local snapshot · "
                    f"Glassdoor {'cached' if components['glassdoor']['run_state'] != 'Healthy' else 'available'}; "
                    "current / new: " + " · ".join(
                        f"{name} {int((board.get('source_raw') or {}).get(key, 0) or 0):,} / "
                        f"{int((((board.get('output') or {}).get('new_jobs_by_source') or {}).get(key) or {}).get('found', 0) or 0):,}"
                        for name, key in (("ATS", "ats"), ("LinkedIn", "linkedin"), ("Indeed", "indeed"), ("Glassdoor", "glassdoor"))
                    )),
        "issue": (f"Indeed {indeed_state.get('reason')}" if indeed_state.get("status") == "partial" else
                  str(components["board"].get("issue") or "")) if components["board"]["run_state"] != "Healthy" else "",
        "note": ("Request budget or deadline hit" if online.get("deadline_reached") or
                 attempted >= recovery_policy.RecoveryBudget().max_jobs else "No request-budget or deadline hit"),
    }

    jd = official.get("jd_recovery") or {}
    eligible_official = int(jd.get("eligible", 0) or 0)
    usable_official = int(jd.get("usable_jd", 0) or 0)
    gaps = sorted(((name, max(0, int(row.get("eligible", 0) or 0) - int(row.get("usable_jd", 0) or 0)))
                   for name, row in (jd.get("per_company") or {}).items()), key=lambda pair: pair[1], reverse=True)
    gaps = [(name, count) for name, count in gaps if count][:4]
    queries = [stat for values in (official.get("query_diagnostics") or {}).values()
               for stat in values if isinstance(stat, dict)]
    official_panel = {
        "title": "Big Company Official", "status": components["official"]["run_state"],
        "jobs": (f"{int((official.get('enrichment') or {}).get('discovered', 0) or 0):,} raw listings scanned · "
                 f"{int((official.get('funnel') or {}).get('after_prefilter', 0) or 0):,} relevant after filters · "
                 f"{int((official.get('output') or {}).get('new_jobs', 0) or 0):,} new · "
                 f"{int((official.get('output') or {}).get('shown', 0) or 0):,} passed · "
                 f"{int((official.get('output') or {}).get('new_jobs_added', 0) or 0):,} newly added to A/B"),
        "jd": (f"JD recovery pool: {eligible_official:,} candidates · {usable_official:,} have JD "
               f"({usable_official / eligible_official:.1%}) · {max(0, eligible_official - usable_official):,} unresolved; "
               f"{int(jd.get('cache_reused', 0) or 0):,} reused from cache · "
               f"{int(jd.get('detail_requests', 0) or 0):,} detail requests") if eligible_official else "JD recovery pool unavailable",
        "requests": (f"{len(queries):,} searches · {sum(int(stat.get('pages_fetched', 0) or 0) for stat in queries):,} "
                     f"search pages · {int(jd.get('detail_requests', 0) or 0):,} detail requests"),
        "sources": "Official company career sites",
        "issue": str(components["official"].get("issue") or "") if components["official"]["run_state"] != "Healthy" else "",
        "note": ("Remaining gaps: " + " · ".join(f"{name} {count}" for name, count in gaps) if gaps else "No remaining JD gaps")
                + (" · request budget hit" if int(jd.get("budget_deferred", 0) or 0) else ""),
    }

    indeed_rows = list(indeed_snapshot.get("jobs") or [])
    indeed_observed = observed(indeed_snapshot, indeed_state)
    indeed_attempt = str(indeed_state.get("last_attempt_at") or "")
    indeed_same_attempt = bool(indeed_attempt and indeed_attempt ==
                               str((indeed_snapshot.get("meta") or {}).get("scraped_at") or ""))
    indeed_new = sum(str(row.get("first_seen") or "") == indeed_attempt for row in indeed_observed)
    indeed_with_jd = sum(len(str(row.get("description") or "").strip()) >= 200 for row in indeed_observed)
    succeeded = int(indeed_state.get("queries_succeeded", 0) or 0)
    failed_queries = int(indeed_state.get("queries_failed", 0) or 0)
    not_run = int(indeed_state.get("queries_not_run", 0) or 0)
    if not (succeeded or failed_queries or not_run):
        succeeded = len(indeed_state.get("query_stats") or []) if indeed_state.get("status") == "ok" else 0
    indeed_panel = {
        "title": "Indeed", "status": components["indeed"]["run_state"],
        "jobs": (f"{len(indeed_rows):,} current · {indeed_new:,} new this run" if indeed_state.get("status") == "ok" and indeed_observed else
                 f"{len(indeed_rows):,} current · new-this-run count unavailable" if indeed_state.get("status") == "ok" else
                 f"{int(indeed_state.get('partial_fresh_kept', 0) or 0):,} fresh jobs preserved · "
                 f"{int(indeed_state.get('partial_carried_count', 0) or 0):,} previous jobs retained"
                 if indeed_state.get("status") == "partial" else f"{len(indeed_rows):,} cached jobs remain"),
        "jd": (f"{indeed_with_jd:,}/{len(indeed_observed):,} "
               f"{'fresh jobs kept' if indeed_state.get('status') == 'partial' else 'jobs collected'} have JD · "
               f"{len(indeed_observed) - indeed_with_jd:,} missing; Board handles missing JDs"
               if indeed_same_attempt else "Latest attempt JD counts unavailable"),
        "requests": f"{succeeded:,} searches completed · {failed_queries:,} failed · {not_run:,} not run",
        "sources": ("Partial fresh results + last-good snapshot" if indeed_state.get("status") == "partial"
                    else "Fresh Indeed collection" if indeed_state.get("status") == "ok"
                    else "Last-good Indeed snapshot"),
        "issue": str(indeed_state.get("reason") or components["indeed"].get("issue") or "")
                 if components["indeed"]["run_state"] != "Healthy" else "",
        "note": "",
    }
    return {"board": board_panel, "linkedin": linkedin_panel,
            "official": official_panel, "indeed": indeed_panel}


def _today_summary(base: Path, now: datetime, latest: dict[str, dict[str, Any]],
                   history: list[dict[str, Any]], local: dict[str, Any],
                   components: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Sum Pacific-day run outcomes; leave unmeasured results unavailable."""
    today = now.astimezone(ZoneInfo("America/Los_Angeles")).date()
    rows: dict[str, dict[str, Any]] = {}
    board_source_added: Counter[str] = Counter()
    board_attribution_complete = False
    for key in PIPELINES:
        runs = [item for item in history if item.get("pipeline") == key
                and _pacific_day(item.get("run_at")) == today]
        current = latest.get(key) or {}
        if _pacific_day(current.get("run_at")) == today and not any(
                item.get("run_at") == current.get("run_at") for item in runs):
            runs.append({"pipeline": key, **current})
        # A retained A/B list appears in every run. Only new additions may be summed.
        if key == "board":
            board_attribution_complete = bool(runs) and all(
                "new_jobs_by_source" in (run.get("output") or {}) for run in runs)
        for run in runs if key == "board" else []:
            for source, counts in ((run.get("output") or {}).get("new_jobs_by_source") or {}).items():
                board_source_added[source] += int((counts or {}).get("added", 0) or 0)
        latest_run = max(runs, key=lambda item: str(item.get("run_at") or ""), default={})
        outputs = [item.get("output") or {} for item in runs]
        rows[key] = {
            "status": components[key]["run_state"] if runs else "No run today",
            "new": (sum(int(output.get("new_jobs", 0) or 0) for output in outputs)
                    if runs and all("new_jobs" in output for output in outputs) else None),
            "new_added": (sum(int(output.get("new_jobs_added", 0) or 0) for output in outputs)
                          if runs and all("new_jobs_added" in output for output in outputs) else None),
            "shown_latest": (latest_run.get("output") or {}).get("shown") if runs else None,
            "runs": len(runs),
            "failed_runs": sum(item.get("health") in {"degraded", "failed", "error"}
                               for item in runs),
            "consecutive_failures": components[key].get("consecutive_failures", 0),
            "latest_run": max((str(item.get("run_at") or "") for item in runs), default=""),
            "issue": components[key].get("issue") or "",
        }
    source_history = (_read(base / "output" / "sources" / "health.json", {}) or {}).get("run_history") or []
    for key in ("linkedin", "indeed", "glassdoor"):
        state = local.get(key) or {}
        attempted_today = _pacific_day(state.get("last_attempt_at")) == today
        runs = [item for item in source_history if item.get("source") == key
                and _pacific_day(item.get("run_at")) == today]
        latest_run = max(runs, key=lambda item: str(item.get("run_at") or ""), default={})
        rows[key] = {
            "status": components[key]["run_state"] if runs or attempted_today else "No run today",
            "new": (sum(int(item["new"] or 0) for item in runs)
                    if runs and all("new" in item and item["new"] is not None for item in runs) else None),
            "pass": (sum(int(item["pass"] or 0) for item in runs)
                     if runs and all(item.get("pass") is not None for item in runs) else None),
            "new_added": board_source_added[key] if runs and board_attribution_complete else None,
            "shown_latest": None,
            "runs": len(runs) if runs or not attempted_today else "—",
            "failed_runs": (sum(bool(item.get("failure")) for item in runs)
                            if runs and all("failure" in item for item in runs) else
                            "—" if attempted_today else 0),
            "consecutive_failures": components[key].get("consecutive_failures", 0),
            "latest_run": latest_run.get("run_at") or state.get("last_attempt_at") if attempted_today else "",
            "issue": components[key].get("issue") or "",
        }
    return rows


def build(base: Path, now: datetime | None = None) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    now = now or datetime.now(timezone.utc)
    latest, history = _run_history(base)
    components: dict[str, dict[str, Any]] = {}
    problems: list[str] = []
    degradations: list[str] = []
    limitations: list[str] = []
    unresolved: list[dict[str, str]] = []
    failure_reasons: Counter[str] = Counter()

    workflow_name = os.getenv("PIPELINE_WORKFLOW_NAME", "")
    workflow_conclusion = os.getenv("PIPELINE_WORKFLOW_CONCLUSION", "")
    workflow_url = os.getenv("PIPELINE_WORKFLOW_URL", "")

    for key, (label, folder, store_name) in PIPELINES.items():
        store = _read(base / "output" / folder / store_name, {})
        entries = list(store.get("entries") or []) if isinstance(store, dict) else []
        run = latest.get(key, {})
        run_stamp = str(run.get("run_at") or "")
        store_stamp = str(store.get("updated_at") or store.get("scraped_at") or "") if entries else ""
        data_age = _age_hours(store_stamp, now)
        attempt_age = _age_hours(run_stamp, now)
        data_usable = bool(entries) and data_age is not None
        if data_usable:
            status = "Healthy" if data_age <= 36 else "Stale"
            details = [f"Usable snapshot: {len(entries)} jobs, updated {data_age:.1f}h ago"]
        elif entries:
            status = "Stale"
            details = [f"Snapshot has {len(entries)} jobs but no usable update timestamp"]
        else:
            status = "Problem"
            details = ["No usable job snapshot"]
        keywords: list[str] = []
        shown = int(run.get("output", {}).get("shown", 0) or 0)
        baseline = float(run.get("recent_shown_median", 0) or 0)
        low_volume_runs = (
            _consecutive_low_volume(history, key, baseline)
            if key == "syncareer" and baseline >= 10 else 0
        )
        if status == "Healthy" and low_volume_runs >= 2:
            status = "Warning"
            keywords.append("low-volume")
            details.append(
                f"output stayed low for {low_volume_runs} runs; latest {shown} vs recent median {baseline:g}"
            )
        failures = run.get("failures") or {}
        ignored_linkedin = (
            _failure_items((failures.get("scrape") or {}).get("linkedin"))
            if key == "official" and isinstance(failures, dict) else []
        )
        known_limitations: list[str] = []
        if key == "official":
            failures, known_limitations = _official_failure_partition(base, failures)
            limitations.extend(known_limitations)
        failure_count, failure_detail = _failure_summary(failures)
        indeed_partial = key == "board" and any(
            "Indeed discovery partial:" in str(item)
            for item in _failure_items((failures.get("discovery") or []) if isinstance(failures, dict) else [])
        )
        failed_scrapers = (
            {name: _failure_items(errors) for name, errors in (failures.get("scrape") or {}).items()}
            if key == "official" else {}
        )
        failed_scrapers = {name: errors for name, errors in failed_scrapers.items() if errors}
        scraper_error_count = len(failed_scrapers)
        scraper_streaks = {
            f"{name} {_short_cause(' '.join(errors))}": _official_scraper_streak(
                history, name, _short_cause(" ".join(errors)), run_stamp)
            for name, errors in failed_scrapers.items()
        }
        consecutive_failures = (
            _consecutive_official_degraded(base, history, run, scraper_error_count)
            if key == "official" else _consecutive_degraded(history, key)
        )
        if ignored_linkedin:
            details.append(
                "LinkedIn company adapter excluded from status: " + "; ".join(ignored_linkedin)
            )
            keywords.append("LinkedIn adapter blocked")
        if scraper_error_count:
            scraper_summary = f"{scraper_error_count} scraper failure{'s' if scraper_error_count != 1 else ''}"
            keywords.append(scraper_summary)
            details.append(
                scraper_summary + ": " + "; ".join(
                    f"{name} ({'; '.join(errors)})" for name, errors in failed_scrapers.items()
                )
            )
        if failure_count:
            llm_impact = _llm_impact(run)
            if key == "official":
                if scraper_error_count >= 10:
                    status = "Problem"
                elif status == "Healthy" and (scraper_error_count >= 5 or llm_impact):
                    status = "Warning"
            elif status == "Healthy" and (llm_impact or consecutive_failures >= 2):
                status = "Warning"
            if "429" in (llm_impact or failure_detail) or "rate" in failure_detail.lower():
                keywords.append("rate-limited")
            if data_usable:
                keywords.append("cached")
            qualifier = "degraded" if status != "Healthy" else "had recoverable issues"
            details.append(f"latest run {qualifier}: {llm_impact or f'{failure_count} failure(s): {failure_detail}'}")
        if indeed_partial and status in {"Healthy", "Warning"}:
            status = "Partial"
        workflow_token = {"board": "board", "official": "official", "syncareer": "syncareer"}[key]
        if workflow_conclusion and workflow_conclusion != "success" and workflow_token in workflow_name.lower():
            status = "Warning" if data_usable and data_age is not None and data_age <= 36 else "Problem"
            if data_usable:
                keywords.append("cached")
            details.append(f"latest workflow attempt concluded {workflow_conclusion}; last-good data remains {'usable' if data_usable else 'unusable'}")
        if workflow_conclusion and workflow_conclusion != "success" and workflow_token in workflow_name.lower():
            latest_attempt_status = "failed"
        elif not run_stamp:
            latest_attempt_status = "unknown"
        elif key == "official":
            latest_attempt_status = (
                "degraded" if scraper_error_count >= 5
                else "limited" if _failure_items(run.get("failures")) else "success"
            )
        else:
            latest_attempt_status = "degraded" if failure_count else "success"
        detail = "; ".join(details)
        issue = ""
        if key == "official" and scraper_error_count:
            named = []
            for name, errors in failed_scrapers.items():
                cause = _short_cause(" ".join(errors))
                named.append(f"{name.title()} {cause} ×{scraper_streaks[f'{name} {cause}']}")
            issue = (f"{scraper_error_count} scraper{'s' if scraper_error_count != 1 else ''} failed: "
                     + ", ".join(named[:2]) + (f", +{len(named) - 2} more" if len(named) > 2 else ""))
        elif failure_count:
            issue = f"{label} {_short_cause(failure_detail)} ×{max(1, consecutive_failures)}"
        components[key] = {
            "label": label,
            "status": status,
            "detail": detail,
            "issue": issue,
            "updated_at": store_stamp,
            "data_usable": data_usable,
            "last_good_count": len(entries),
            "last_good_at": store_stamp,
            "latest_attempt_at": run_stamp,
            "latest_attempt_age_hours": round(attempt_age, 1) if attempt_age is not None else None,
            "latest_attempt_status": latest_attempt_status,
            "failure_count": failure_count,
            "scraper_error_count": scraper_error_count,
            "consecutive_failures": consecutive_failures,
            "failure_streaks": scraper_streaks if key == "official" else {},
            "low_volume_runs": low_volume_runs,
            "keywords": list(dict.fromkeys(keywords)),
            "impact": _llm_impact(run) or (
                f"latest attempt {'degraded' if status != 'Healthy' else 'had recoverable issues'}; fresh last-good snapshot remains usable"
                if failure_count and data_usable else ""
            ),
            "known_limitations": known_limitations,
        }

        for entry in entries:
            description_available = bool(entry.get("description_available")) or len(
                str(entry.get("description") or "").strip()
            ) >= 200
            if description_available or str(entry.get("filter_status") or "kept") not in {"kept", ""}:
                continue
            reason = str(entry.get("enrichment_failure_reason") or "no_recorded_failure")
            failure_reasons[reason] += 1
            if len(unresolved) < 50:
                unresolved.append({
                    "pipeline": key,
                    "company": str(entry.get("company") or ""),
                    "title": str(entry.get("title") or ""),
                    "url": str(entry.get("official_url") or entry.get("source_url") or entry.get("job_url") or entry.get("url") or ""),
                    "reason": reason,
                })

    local_payload = _read(base / "output" / "sources" / "health.json", {})
    local = local_payload.get("sources", {})
    mac_completed_at = str(local_payload.get("mac_last_completed_at") or "")
    _, _, mac_schedule = local_schedule_decision(now, {"last_success_at": mac_completed_at})
    local_scheduler = {
        "last_successful_local_run_at": mac_completed_at,
        "last_scheduled_slot_at": mac_schedule["last_scheduled_slot_at"],
        "scheduled_slot_missed": mac_schedule["scheduled_slot_missed"] if mac_completed_at else None,
        "catch_up_status": mac_schedule["catch_up_status"] if mac_completed_at else "unknown",
        "catch_up_pending": mac_schedule["catch_up_pending"] if mac_completed_at else None,
        "reason": mac_schedule["catch_up_reason"] if mac_completed_at else "No published Local round timestamp yet",
        "next_scheduled_run_at": mac_schedule["next_scheduled_run_at"],
        "basis": "last published Local round; Mac availability is not reported",
    }
    for source in ("linkedin", "indeed", "glassdoor"):
        state = local.get(source, {})
        snapshot = _read(base / "output" / "sources" / f"{source}.json", {})
        snapshot_jobs = list(snapshot.get("jobs") or []) if isinstance(snapshot, dict) else []
        # ``age`` is the freshness of the last complete collection, which is
        # the only verification the whole snapshot ever received. A recent
        # partial attempt is tracked separately and never resets that clock.
        age = _age_hours(str(state.get("last_success_at") or ""), now)
        attempt_age = _age_hours(str(state.get("last_attempt_at") or ""), now)
        partial_age = _age_hours(str(state.get("last_partial_at") or ""), now)
        is_partial = str(state.get("status") or "") == "partial"
        search = state.get("search_collection") or {}
        partial_reason = str(state.get("reason") or "")
        rate_limited_partial = bool(is_partial and (search.get("rate_limited") or "429" in partial_reason
                                                    or "rate" in partial_reason.lower()))
        focused_partial = bool(source == "linkedin" and is_partial and not rate_limited_partial)
        last_good_count = len(snapshot_jobs)
        data_usable = last_good_count > 0 and (age is not None or partial_age is not None)
        cooling = source == "linkedin" and bool(search.get("cooldown_active"))
        attempt_failed = not state.get("healthy") and not focused_partial and not cooling
        if not data_usable:
            status = "Problem" if state.get("required", source != "glassdoor") else "Warning"
        elif focused_partial and partial_age is not None and partial_age <= 12:
            status = "Healthy"
        elif age is None:
            status = "Healthy" if source == "linkedin" and partial_age is not None else "Warning"
        elif age > (36 if source == "indeed" else 12):
            status = "Stale"
        elif age > (18 if source == "indeed" else 6) and source != "linkedin":
            status = "Warning"
        else:
            status = "Healthy"
        consecutive_failures = (
            int((state.get("runner_states") or {}).get("mac", {}).get("search_429_streak", 0) or 0)
            if source == "linkedin" and focused_partial else
            int(state.get("consecutive_failures", 1 if attempt_failed else 0) or 0)
        )
        if focused_partial:
            consecutive_failures = 0
        runtime = ((state.get("runner_states") or {}).get("mac") or state) if source == "linkedin" else {}
        search_streak = int(runtime.get("search_429_streak", consecutive_failures if rate_limited_partial or search.get("rate_limited") else 0) or 0)
        search_cooldown_until = str(runtime.get("search_cooldown_until") or "")
        search_until = recovery_policy.stamp(search_cooldown_until)
        search_cooldown_active = bool(source == "linkedin" and (cooling or (search_until and search_until > now)))
        targeted_streak = int((local_payload.get("local_recovery") or {}).get("targeted_429_streak", 0) or 0)
        detail_streak = int(runtime.get("detail_429_streak", state.get("detail_429_streak", 0)) or 0)
        failure_threshold = 3 if source == "linkedin" else 2
        if source == "linkedin":
            consecutive_failures = max(search_streak, targeted_streak, detail_streak)
            if status == "Healthy" and search_cooldown_active:
                status = "Warning"
            if status == "Healthy" and consecutive_failures >= failure_threshold and (targeted_streak or detail_streak):
                status = "Warning"
        if status == "Healthy" and attempt_failed and consecutive_failures >= failure_threshold:
            status = "Warning"
        if source == "indeed" and is_partial and status in {"Healthy", "Warning"}:
            status = "Partial"
        verified_age = f"{age:.1f}h old" if age is not None else "never fully verified"
        details = [
            f"Usable last-good snapshot: {last_good_count} jobs, {verified_age}"
            if data_usable else "No usable last-good snapshot"
        ]
        attempt_kind = "search/discovery" if source == "linkedin" else "collection"
        attempt_when = f" {attempt_age:.1f}h ago" if attempt_age is not None else ""
        if is_partial:
            collected = int(state.get("partial_collected_count", 0) or 0)
            fresh_kept = int(state.get("partial_fresh_kept", 0) or 0)
            carried = int(state.get("partial_carried_count", 0) or 0)
            if source == "indeed":
                details.append(
                    f"{int(state.get('queries_succeeded', 0) or 0)} queries succeeded · "
                    f"{int(state.get('queries_failed', 0) or 0)} failed / "
                    f"{int(state.get('queries_not_run', 0) or 0)} not run · "
                    f"{fresh_kept} fresh jobs kept · {carried} cached jobs reused; "
                    f"latest attempt{attempt_when}: {state.get('reason') or 'partial collection'}"
                )
            else:
                details.append(
                    f"latest {attempt_kind} attempt{attempt_when} had "
                    f"{'rate-limited' if rate_limited_partial else 'focused'} coverage "
                    f"({state.get('reason') or 'partial coverage'}): collected {collected} rows, kept {fresh_kept}; "
                    f"merged snapshot serves {last_good_count} ({carried} carried, last full collection {verified_age})"
                )
        elif cooling:
            details.append("Search deferred during cooldown; no search HTTP request was made")
        elif attempt_failed:
            details.append(
                f"latest {attempt_kind} attempt{attempt_when} failed ({state.get('status', 'unknown')}): "
                f"{state.get('reason') or 'unknown reason'}"
            )
            if status == "Healthy":
                limitations.append(
                    f"{'LinkedIn (local/general)' if source == 'linkedin' else source.title()}: one recoverable "
                    f"{attempt_kind} failure; fresh last-good data remains usable"
                )
        enrichment = state.get("detail_enrichment") or (
            snapshot.get("meta", {}).get("detail_enrichment", {})
            if source != "linkedin" or state.get("last_attempt_at") == (snapshot.get("meta") or {}).get("scraped_at") else {}
        )
        degradation_kinds: list[str] = []
        keywords = []
        if is_partial:
            degradation_kinds.append("rate_limited_partial_collection" if rate_limited_partial else
                                     "partial_collection" if source == "indeed" else "focused_coverage")
            keywords.extend(("partial", "rate-limited" if rate_limited_partial else
                             "partial collection" if source == "indeed" else "focused coverage", "cached"))
            limitations.append(
                f"{'LinkedIn (local/general)' if source == 'linkedin' else source.title()}: "
                f"{'rate-limited' if rate_limited_partial else 'focused' if source == 'linkedin' else 'failed'} partial "
                f"collection; {last_good_count} jobs usable "
                f"({int(state.get('partial_carried_count', 0) or 0)} carried from the last complete run)"
            )
        if source == "linkedin":
            cooldown_until = str(state.get("detail_cooldown_until") or "")
            last_detail_attempt = recovery_policy.stamp(state.get("detail_last_attempt_at"))
            recorded_cooldown = recovery_policy.stamp(cooldown_until)
            if last_detail_attempt and recorded_cooldown:
                cooldown_until = min(
                    recorded_cooldown,
                    last_detail_attempt + timedelta(hours=recovery_policy.LINKEDIN_DETAIL_COOLDOWN_HOURS),
                ).isoformat()
            intentional_pause = state.get("detail_cooldown_reason") == "intentional pause"
            blocked = str(enrichment.get("blocked") or "")
            detail_rate_limited = bool(enrichment.get("rate_limited") or ("HTTP 429" in blocked and not intentional_pause))
            detail_until = recovery_policy.stamp(cooldown_until)
            detail_cooldown_active = bool(detail_until and detail_until > now)
            if status == "Healthy" and detail_rate_limited:
                status = "Warning"
            scrapling_requests = int(enrichment.get("scrapling_requests", 0) or 0)
            scrapling_resolved = int(enrichment.get("scrapling_jds_resolved", 0) or 0)
            remaining = int(enrichment.get("remaining_no_jd", 0) or 0)
            if blocked and not intentional_pause:
                degradation_kinds.append("detail_enrichment_blocked")
                details.append(f"primary detail enrichment blocked: {blocked}")
                if "429" in blocked or "rate" in blocked.lower():
                    keywords.append("rate-limited")
            if scrapling_requests and not intentional_pause:
                details.append(f"Scrapling fallback recovered {scrapling_resolved}/{scrapling_requests} attempted JDs")
            if enrichment.get("scrapling_error") and not intentional_pause:
                degradation_kinds.append("scrapling_limited")
                details.append(f"Scrapling fallback unavailable: {enrichment['scrapling_error']}")
            if remaining:
                degradation_kinds.append("missing_descriptions")
                details.append(f"{remaining} discovered records remain without a JD")
            if (blocked and not intentional_pause) or remaining:
                limitations.append(
                    f"LinkedIn (local/general): {remaining} JD(s) remain without enrichment"
                    if intentional_pause else
                    f"LinkedIn (local/general): recovered detail limitation; Scrapling resolved "
                    f"{scrapling_resolved}/{scrapling_requests}, {remaining} JD(s) remain"
                )
            if cooldown_until:
                degradation_kinds.append("detail_enrichment_cooldown")
                if intentional_pause:
                    details.append(
                        f"LinkedIn detail intentionally paused/cooldown until {_display_time(cooldown_until)}; "
                        "search/discovery continues; next eligible detail request is a one-job probe"
                    )
                else:
                    details.append(
                        f"LinkedIn detail cooldown ({state.get('detail_cooldown_reason') or 'repeated 429'}); "
                        f"next probe after {_display_time(cooldown_until)}"
                    )
                    keywords.append("rate-limited")
        if attempt_failed and data_usable:
            keywords.extend(("cached", "scraper errors"))
            reason = str(state.get("reason") or "")
            if "429" in reason or "rate" in reason.lower():
                keywords.append("rate-limited")
        query_stats = list(state.get("query_stats") or [])
        static_fallbacks = sum(str(item.get("stop_reason") or "") == "static_html_fallback" for item in query_stats)
        if static_fallbacks:
            degradation_kinds.append("static_html_fallback")
            details.append(
                f"{static_fallbacks}/{len(query_stats)} queries used static HTML fallback; cards remain usable but coverage is a repeatable known limitation"
            )
            limitations.append(
                f"Glassdoor: {static_fallbacks}/{len(query_stats)} queries used the expected static HTML fallback"
            )
        detail = "; ".join(details)
        cause = str(state.get("failure_cause") or "")
        if source == "linkedin":
            endpoint_issues = []
            if search.get("rate_limited"):
                endpoint_issues.append(f"Search 429 ×{max(1, search_streak)}")
            if search_cooldown_active:
                endpoint_issues.append(f"Search cooldown/deferred until {_display_time(search_cooldown_until)}")
            if detail_rate_limited:
                endpoint_issues.append(f"Detail 429 ×{max(1, detail_streak)}")
            elif detail_cooldown_active:
                endpoint_issues.append(f"Detail cooldown until {_display_time(cooldown_until)}")
            elif detail_streak:
                endpoint_issues.append("Detail probe pending")
            if targeted_streak:
                endpoint_issues.append(f"Targeted Search 429 ×{targeted_streak}")
            issue = "; ".join(endpoint_issues)
            if not issue and attempt_failed:
                issue = str(state.get("reason") or "Search failed")
        elif focused_partial:
            issue = ""
        elif cause and attempt_failed:
            issue = (
                f"{int(state.get('queries_succeeded', 0) or 0)} queries succeeded · "
                f"{int(state.get('queries_failed', 0) or 0)} failed / "
                f"{int(state.get('queries_not_run', 0) or 0)} not run · "
                f"{int(state.get('partial_fresh_kept', 0) or 0)} fresh jobs kept · "
                f"{int(state.get('partial_carried_count', 0) or 0)} cached jobs reused · "
                f"{state.get('reason') or cause}"
                if source == "indeed" and is_partial else
                f"{source.title()} {cause} ×{consecutive_failures}"
            )
        elif attempt_failed:
            issue = f"{source.title()} {_short_cause(str(state.get('reason') or ''))} ×{consecutive_failures}"
        else:
            issue = ""
        components[source] = {
            "label": {"linkedin": "LinkedIn (Mac)", "indeed": "Indeed (GitHub)", "glassdoor": "Glassdoor (Mac)"}[source],
            "status": status,
            "detail_status": state.get("detail_status", "") if source == "linkedin" else "",
            "detail": detail,
            "issue": issue,
            "recent_history": state.get("previous_failure") or {},
            "updated_at": state.get("last_success_at", ""),
            "data_usable": data_usable,
            "last_good_count": last_good_count,
            "last_good_at": state.get("last_success_at", ""),
            "latest_attempt_at": state.get("last_attempt_at", ""),
            "latest_attempt_age_hours": round(attempt_age, 1) if attempt_age is not None else None,
            "latest_attempt_status": state.get("status", "unknown"),
            "latest_partial_at": state.get("last_partial_at", ""),
            "latest_partial_age_hours": round(partial_age, 1) if partial_age is not None else None,
            "partial_collected_count": int(state.get("partial_collected_count", 0) or 0),
            "partial_fresh_kept": int(state.get("partial_fresh_kept", 0) or 0),
            "partial_carried_count": int(state.get("partial_carried_count", 0) or 0),
            "degradation_kinds": degradation_kinds,
            "consecutive_failures": consecutive_failures,
            "failure_streaks": ({"search_429": search_streak,
                                 "targeted_429": targeted_streak, "detail_429": detail_streak}
                                if source == "linkedin" else
                                {str(state.get("failure_cause") or _short_cause(str(state.get("reason") or ""))): consecutive_failures}
                                if consecutive_failures else {}),
            "keywords": list(dict.fromkeys(keywords)),
            "impact": (
                f"partial collection ({state.get('reason') or 'HTTP 429'}); {last_good_count} jobs usable, "
                f"last full collection {verified_age}"
                if is_partial and data_usable else
                f"collection failed; {last_good_count} last-good jobs remain usable"
                if attempt_failed and data_usable else
                ("required source has no usable data" if not data_usable and state.get("required", source != "glassdoor") else "")
            ),
        }
        if source == "linkedin":
            attempt_at = str(state.get("last_attempt_at") or "")
            snapshot_at = str((snapshot.get("meta") or {}).get("scraped_at") or "")
            same_snapshot = bool(attempt_at and attempt_at == snapshot_at)
            retained = ([job for job in snapshot_jobs
                         if job.get("verified_this_run") and job.get("source_verified_at") == attempt_at]
                        if is_partial else snapshot_jobs) if same_snapshot else []
            recovery = local_payload.get("local_recovery") or {}
            recovery_at = str(recovery.get("run_at") or "")
            try:
                recovery_delay = (datetime.fromisoformat(recovery_at.replace("Z", "+00:00"))
                                  - datetime.fromisoformat(attempt_at.replace("Z", "+00:00")))
                same_recovery = timedelta(0) <= recovery_delay <= timedelta(hours=1)
            except ValueError:
                same_recovery = False
            components[source]["latest_run"] = {
                "attempt_at": attempt_at,
                "titles_found": (int(state.get("partial_collected_count", 0) or 0) if is_partial
                                 else int(state.get("last_attempt_count", 0) or 0)) if same_snapshot else None,
                "titles_kept": len(retained) if same_snapshot else None,
                "jds_on_kept_titles": (sum(len(str(job.get("description") or "").strip()) >= 200
                                           for job in retained) if same_snapshot else None),
                "search_jds_resolved": (int(((snapshot.get("meta") or {}).get("detail_enrichment") or {})
                                            .get("jds_resolved", 0) or 0) if same_snapshot else None),
                "recovery_linkedin_jds": int(recovery.get("linkedin_detail_recoveries", 0) or 0) if same_recovery else None,
                "recovery_other_jds": int(recovery.get("official_jds_recovered", 0) or 0) if same_recovery else None,
                "search_429": bool(search.get("rate_limited")),
                "search_cooldown_active": search_cooldown_active,
                "search_cooldown_until": search_cooldown_until,
                "detail_cooldown_active": detail_cooldown_active,
                "detail_429": detail_rate_limited or bool(same_recovery and (recovery.get("linkedin_detail") or {}).get("rate_limited")),
                "search_http_status": search.get("http_status"),
                "detail_http_status_counts": enrichment.get("http_status_counts", {}),
                "stored_unresolved_job_reasons": enrichment.get("failure_reasons", {}),
                "post_429_jds_recovered": (recovery.get("post_429_jds_recovered")
                                           if same_recovery and recovery.get("post_429_jds_recovered") is not None
                                           else 0 if same_recovery and recovery.get("linkedin_rate_limited")
                                           and not recovery.get("official_jds_recovered") else None),
                "detail_cooldown_until": cooldown_until,
            }

    components["board"]["keywords"] = list(dict.fromkeys([
        *components["board"]["keywords"],
        *(keyword for name in ("linkedin", "indeed", "glassdoor") for keyword in components[name]["keywords"]),
    ]))

    board_entries = list((_read(base / "output" / "board" / "jobs.json", {}) or {}).get("entries") or [])
    for key, item in components.items():
        if key in PIPELINES:
            entries = list((_read(base / "output" / PIPELINES[key][1] / "jobs.json", {}) or {}).get("entries") or [])
            jd_count = sum(bool(entry.get("description_available")) for entry in entries)
            pass_count = sum(entry.get("tier") in {"A", "B"} for entry in entries)
        else:
            entries = list((_read(base / "output" / "sources" / f"{key}.json", {}) or {}).get("jobs") or [])
            jd_count = sum(len(str(entry.get("description") or "").strip()) >= 200 for entry in entries)
            pass_count = sum(entry.get("tier") in {"A", "B"} for entry in board_entries
                             if str(entry.get("source") or "").lower() == key)
        item["volumes"] = {"jobs": item.get("last_good_count", 0), "jd": jd_count, "pass": pass_count}
        summary = f"{item['label']}: {item.get('issue') or item['detail']}"
        if item["status"] in {"Problem", "Stale"}:
            problems.append(summary)
        elif item["status"] in {"Warning", "Partial"}:
            degradations.append(summary)

    local_state = local_payload
    recovery = local_state.get("local_recovery") or {}
    local_sources = local_state.get("sources") or {}

    def _group(statuses: list[str], jobs: int, jds: int, elapsed: float | None,
               children: dict[str, Any]) -> dict[str, Any]:
        return {"jobs_processed": jobs, "jds_recovered": jds, "elapsed_seconds": elapsed,
                "status": max(statuses, key=SEVERITY.get), "subcomponents": children}

    remote_children = {
        "ATS": {"jobs_processed": int((latest.get("board", {}).get("source_raw") or {}).get("ats", 0) or 0),
                "status": components["board"]["status"],
                "elapsed_seconds": latest.get("board", {}).get("remote_elapsed_seconds")},
        "Official": {"jobs_processed": int((latest.get("official", {}).get("enrichment") or {}).get("discovered", 0) or 0),
                     "status": components["official"]["status"],
                     "elapsed_seconds": latest.get("official", {}).get("scrape_elapsed_seconds")},
        "Syncareer": {"jobs_processed": int((latest.get("syncareer", {}).get("output") or {}).get("new_jobs", 0) or 0),
                      "status": components["syncareer"]["status"],
                      "elapsed_seconds": latest.get("syncareer", {}).get("remote_elapsed_seconds")},
        "Indeed": {"jobs_processed": int((local.get("indeed") or {}).get("last_attempt_count", 0) or 0),
                   "status": components["indeed"]["status"],
                   "elapsed_seconds": (local.get("indeed") or {}).get("last_attempt_elapsed_seconds")},
        "other remote sources": {"jobs_processed": 0, "status": "unmeasured"},
    }
    remote_jobs = sum(int(child.get("jobs_processed", 0) or 0) for child in remote_children.values())
    remote_jds = (
        int((latest.get("official", {}).get("enrichment") or {}).get("source_jds_available", 0) or 0)
        + int(((latest.get("board", {}).get("enrichment") or {}).get("direct") or {}).get("jds_resolved", 0) or 0)
        + int((latest.get("syncareer", {}).get("enrichment") or {}).get("detail_api_resolved", 0) or 0)
        + sum(len(str(job.get("description") or "").strip()) >= 200
              for job in (_read(base / "output" / "sources" / "indeed.json", {}) or {}).get("jobs", []))
        + sum(int((latest.get(key, {}).get("enrichment") or {}).get("exact_peer_resolved", 0) or 0)
              for key in PIPELINES)
    )
    action_jds = int((latest.get("board", {}).get("online_recovery") or {}).get("jds_recovered", 0) or 0)
    remote_elapsed_values = [remote_children[key].get("elapsed_seconds") for key in ("ATS", "Official", "Syncareer", "Indeed")]
    remote_elapsed = (round(sum(float(value or 0) for value in remote_elapsed_values), 3)
                      if any(value is not None for value in remote_elapsed_values) else None)
    action_jobs = sum(int((latest.get(key, {}).get("funnel") or {}).get("after_dedup", 0) or 0)
                      for key in PIPELINES)
    action_elapsed_values = [
        max(0, float(latest.get(key, {}).get("elapsed_seconds") or 0)
            - float(latest.get(key, {}).get("remote_elapsed_seconds") or 0))
        for key in ("board", "syncareer")
    ] + [float(latest.get("official", {}).get("elapsed_seconds") or 0)]
    action_children = {
        "ingest": {"jobs_processed": remote_jobs},
        "dedup": {"jobs_processed": action_jobs},
        "enrichment": {"jds_recovered": action_jds,
                       "needed": sum(int((latest.get(key, {}).get("enrichment") or {}).get("needed", 0) or 0)
                                     for key in PIPELINES),
                       "online_company_title": latest.get("board", {}).get("online_recovery", {})},
        "LLM": {"jobs_processed": sum(int((latest.get(key, {}).get("llm") or {}).get("scored", 0) or 0)
                                      for key in PIPELINES),
                "requests": sum(int((latest.get(key, {}).get("llm") or {}).get("api_requests", 0) or 0)
                                for key in PIPELINES)},
        "publish": {"jobs_processed": sum(int((latest.get(key, {}).get("output") or {}).get("shown", 0) or 0)
                                          for key in PIPELINES),
                    "status": "measured in latest run outputs"},
    }
    local_elapsed_values = [(local_sources.get(key) or {}).get("last_attempt_elapsed_seconds")
                            for key in ("linkedin", "glassdoor")]
    groups = {
        "Remote": _group([components[key]["status"] for key in (*PIPELINES, "indeed")], remote_jobs, remote_jds,
                         remote_elapsed, remote_children),
        "GitHub Actions": _group([components[key]["status"] for key in PIPELINES], action_jobs,
                                 action_jds, sum(float(value or 0) for value in action_elapsed_values)
                                 if any(latest.get(key, {}).get("elapsed_seconds") is not None
                                        for key in PIPELINES) else None,
                                 action_children),
        "Local Mac": _group([components[key]["status"] for key in ("linkedin", "glassdoor")],
                            sum(int((local_sources.get(key) or {}).get("last_attempt_count", 0) or 0)
                                for key in ("linkedin", "glassdoor")),
                            int(recovery.get("official_jds_recovered", 0) or 0)
                            + int(recovery.get("linkedin_detail_recoveries", 0) or 0)
                            + int(recovery.get("targeted_linkedin_detail_jds", 0) or 0),
                            sum(float(value or 0) for value in local_elapsed_values)
                            + float(recovery.get("elapsed_seconds") or 0)
                            if any(value is not None for value in local_elapsed_values)
                            or recovery.get("elapsed_seconds") is not None else None,
                            {"LinkedIn discovery": {**local_sources.get("linkedin", {}).get("search_collection", {}),
                                                    "jobs_processed": local_sources.get("linkedin", {}).get("last_attempt_count", 0),
                                                    "elapsed_seconds": local_sources.get("linkedin", {}).get("last_attempt_elapsed_seconds")},
                             "official-web recovery": {"jds_recovered": recovery.get("official_jds_recovered", 0),
                                                         "requests": recovery.get("search_requests", 0),
                                                         "elapsed_seconds": recovery.get("elapsed_seconds")},
                             "targeted LinkedIn recovery": {"requests": recovery.get("targeted_linkedin_search_requests", 0),
                                                            "jds_recovered": recovery.get("targeted_linkedin_detail_jds", 0)},
                             "LinkedIn detail": {"jds_recovered": recovery.get("linkedin_detail_recoveries", 0),
                                                 **local_sources.get("linkedin", {}).get("detail_enrichment", {})}}),
    }

    current_rows: dict[str, dict[str, Any]] = {}
    stored_rows: dict[str, dict[str, Any]] = {}
    for key, (_label, folder, store_name) in PIPELINES.items():
        payload = _read(base / "output" / folder / store_name, {}) or {}
        for entry in payload.get("entries", []):
            identity = str(entry.get("canonical_job_key") or recovery_policy.identity(entry))
            stored_rows.setdefault(identity, entry)
            seen = recovery_policy.stamp(entry.get("first_seen"))
            if not seen or not timedelta(0) <= now - seen <= timedelta(hours=72):
                continue
            current_rows.setdefault(identity, entry)
    no_jd = [entry for entry in current_rows.values()
             if not entry.get("description_available")
             and len(str(entry.get("description") or "").strip()) < 200]
    older_no_jd = sum(not entry.get("description_available")
                      and len(str(entry.get("description") or "").strip()) < 200
                      and not recovery_policy.fresh(entry, now)
                      for entry in stored_rows.values())
    recovery_summary = {
        "discovered_this_run": sum(int((latest.get(key, {}).get("output") or {}).get("new_jobs", 0) or 0)
                                   for key in PIPELINES),
        "verified_this_run": sum(int((local_sources.get(key) or {}).get(
                                     "partial_fresh_kept" if (local_sources.get(key) or {}).get("status") == "partial"
                                     else "last_attempt_count", 0) or 0)
                                 for key in ("linkedin", "indeed", "glassdoor")
                                 if (local_sources.get(key) or {}).get("status") in {"ok", "partial"}),
        "fallback_current": sum(str(entry.get("score_source") or "") in {"rule_fallback", "metadata_ai_fallback"}
                                for entry in current_rows.values()),
        "no_jd_current": len(no_jd),
        "pending_fresh": sum(recovery_policy.fresh(entry, now)
                             and not entry.get("recovery_methods")
                             and not entry.get("official_search_attempted_at")
                             and not entry.get("linkedin_detail_attempted_at")
                             and (entry.get("recovery_triage") or {}).get("action") != "skip"
                             for entry in no_jd),
        "attempted_unresolved": sum(bool(entry.get("recovery_methods") or entry.get("official_search_attempted_at")
                                         or entry.get("linkedin_detail_attempted_at")) for entry in no_jd),
        "older_no_jd": older_no_jd,
    }
    if recovery_summary["pending_fresh"] >= 20:
        limitations.append(f"Fresh JD recovery backlog: {recovery_summary['pending_fresh']} pending")
    if (recovery.get("linkedin_rate_limited") or
            (local_sources.get("linkedin", {}).get("search_collection") or {}).get("rate_limited")):
        limitations.append("LinkedIn HTTP 429 stopped further LinkedIn requests")
    for item in components.values():
        item["run_state"] = _main_state(item)
    online_status = (latest.get("board") or {}).get("online_recovery") or {}
    if (online_status.get("deadline_reached") or
            int(online_status.get("jobs_processed", 0) or 0) >= recovery_policy.RecoveryBudget().max_jobs):
        if components["board"]["run_state"] == "Healthy":
            components["board"]["run_state"] = "Partial"
            components["board"]["issue"] = "Online JD recovery budget or deadline reached"
    official_jd_status = (latest.get("official") or {}).get("jd_recovery") or {}
    if official_jd_status.get("errors") or int(official_jd_status.get("budget_deferred", 0) or 0):
        if components["official"]["run_state"] == "Healthy":
            components["official"]["run_state"] = "Partial"
            components["official"]["issue"] = (
                str((official_jd_status.get("errors") or [""])[0]) or
                f"{int(official_jd_status.get('budget_deferred', 0) or 0)} detail jobs deferred by budget"
            )
    linkedin_jd_status = (local_sources.get("linkedin") or {}).get("detail_enrichment") or {}
    if (linkedin_jd_status.get("rate_limited") or linkedin_jd_status.get("budget_exhausted")
            or int(linkedin_jd_status.get("failed", 0) or 0)):
        if components["linkedin"]["run_state"] == "Healthy":
            components["linkedin"]["run_state"] = "Partial"
            components["linkedin"]["issue"] = (
                str(linkedin_jd_status.get("blocked") or "") or
                ("LinkedIn JD request budget reached" if linkedin_jd_status.get("budget_exhausted") else
                 "LinkedIn JD rate limited" if linkedin_jd_status.get("rate_limited") else
                 f"{int(linkedin_jd_status.get('failed', 0) or 0)} LinkedIn JD requests failed")
            )
    required = ("board", "official", "syncareer", "linkedin", "indeed")
    overall_detail_status = max((components[name]["status"] for name in PIPELINES), key=SEVERITY.get)
    overall = ("Failed" if any(components[name]["run_state"] == "Failed" for name in required)
               else "Partial" if any(components[name]["run_state"] == "Partial" for name in required)
               else "Healthy")
    for group_name, names in (("Remote", ("board", "official", "syncareer", "indeed")),
                              ("GitHub Actions", tuple(PIPELINES)), ("Local Mac", ("linkedin",))):
        groups[group_name]["run_state"] = (
            "Failed" if any(components[name]["run_state"] == "Failed" for name in names) else
            "Partial" if any(components[name]["run_state"] == "Partial" for name in names) else "Healthy"
        )
    # Remote collectors report current JD inventory, not a complete count of
    # JDs newly fetched in that run. Do not relabel that inventory as new work.
    board_direct = int((((latest.get("board") or {}).get("enrichment") or {}).get("direct") or {}).get("jds_resolved", 0) or 0)
    board_followup = int(((latest.get("board") or {}).get("online_recovery") or {}).get("jds_recovered", 0) or 0)
    official_detail = sum(int(row.get("detail_success", 0) or 0) for row in
                          (((latest.get("official") or {}).get("jd_recovery") or {}).get("per_company") or {}).values())
    syncareer_detail = int(((latest.get("syncareer") or {}).get("enrichment") or {}).get("detail_api_resolved", 0) or 0)
    github_measured = board_direct + board_followup + official_detail + syncareer_detail
    local_detail = int(((local_sources.get("linkedin") or {}).get("detail_enrichment") or {}).get("detail_jds_fetched", 0) or 0)
    local_followup = (int(recovery.get("official_jds_recovered", 0) or 0)
                      + int(recovery.get("linkedin_detail_recoveries", 0) or 0)
                      + int(recovery.get("targeted_linkedin_detail_jds", 0) or 0))
    groups["Remote"].update(new_jds_this_run=None, new_jds_note="Not measured across remote collectors")
    groups["GitHub Actions"].update(new_jds_this_run=github_measured,
                                    new_jds_note="Measured direct and follow-up JDs; source-supplied JDs are not counted")
    groups["Local Mac"].update(new_jds_this_run=local_detail + local_followup,
                               new_jds_note=f"{local_detail} fetched directly · {local_followup} recovered later")
    latest_runs = _latest_run_panels(base, latest, components, local_sources, recovery)
    board_recovery = (latest.get("board") or {}).get("online_recovery") or {}
    board_direct = (((latest.get("board") or {}).get("enrichment") or {}).get("direct") or {})
    board_attempted = int(board_recovery.get("jobs_processed", 0) or 0)
    board_missing = max(0, board_attempted - int(board_direct.get("jds_resolved", 0) or 0)
                        - int(board_recovery.get("jds_recovered", 0) or 0))
    linkedin_detail = (local_sources.get("linkedin") or {}).get("detail_enrichment") or {}
    coverage = {
        "board_attempted": board_attempted,
        "board_still_missing": board_missing,
        "linkedin_fresh_needed": int(linkedin_detail.get("eligible", 0) or 0),
        "linkedin_still_missing": int(linkedin_detail.get("remaining_no_jd", 0) or 0),
        "using_fallback": recovery_summary["fallback_current"],
        "older_no_jd": older_no_jd,
    }
    today = _today_summary(base, now, latest, history, local_sources, components)
    attention = []
    for name in ("board", "official", "syncareer", "linkedin", "indeed", "glassdoor"):
        item = components[name]
        if item["run_state"] != "Healthy":
            attention.append(f"{item['label']}: {item.get('issue') or item.get('detail') or item['run_state']}")
    if recovery_summary["pending_fresh"] >= 20:
        attention.append(f"Fresh JD backlog: {recovery_summary['pending_fresh']:,} pending")
    report = {
        "generated_at": now.isoformat(),
        "overall": overall,
        "overall_detail_status": overall_detail_status,
        "components": components,
        "latest_runs": latest_runs,
        "today": today,
        "source_run_history": local_payload.get("run_history") or [],
        "latest_funnels": {key: latest.get(key, {}).get("funnel", {}) for key in PIPELINES},
        "coverage": coverage,
        "attention": attention,
        "local_scheduler": local_scheduler,
        "groups": groups,
        "problems": problems,
        "degradations": degradations,
        "limitations": limitations,
        "workflow_failure": {"name": workflow_name, "conclusion": workflow_conclusion, "url": workflow_url} if workflow_conclusion and workflow_conclusion != "success" else {},
        "enrichment": {
            "pipelines": {key: latest.get(key, {}).get("enrichment", {}) for key in PIPELINES},
            "linkedin": _read(base / "output" / "sources" / "linkedin.json", {}).get("meta", {}).get("detail_enrichment", {}),
            "unresolved_thin_or_no_jd": sum(failure_reasons.values()),
            "failure_reasons": dict(failure_reasons.most_common()),
        },
        "recovery_summary": recovery_summary,
        "unresolved_examples": unresolved,
    }
    return report, history


def write(public: Path, report: dict[str, Any], history: list[dict[str, Any]]) -> None:
    public.mkdir(parents=True, exist_ok=True)
    (public / "health.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (public / "health-history.json").write_text(json.dumps(history, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def esc(value: object) -> str:
        return html.escape(str(value or ""))

    def number(value: object) -> str:
        return f"{int(value or 0):,}"

    def duration(value: object) -> str:
        if value is None:
            return "—"
        seconds = round(float(value))
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes}m {seconds:02d}s" if minutes else f"{seconds}s"

    panels = []
    for name in ("board", "linkedin", "official", "indeed"):
        item = report["latest_runs"][name]
        lines = [
            ("Jobs", item["jobs"]), ("JD & recovery", item["jd"]),
            ("Requests", item["requests"]), ("Sources", item["sources"]),
        ]
        rows = ""
        for label, value in lines:
            note_here = (label == "Requests" and name != "official") or (label == "Sources" and name == "official")
            note = f'<br><small class="run-note">{esc(item["note"])}</small>' if note_here and item.get("note") else ""
            rows += f'<div class="run-line"><dt>{esc(label)}</dt><dd><span>{esc(value)}</span>{note}</dd></div>'
        if item.get("issue"):
            rows += f'<div class="run-line issue"><dt>Issue</dt><dd>{esc(item["issue"])}</dd></div>'
        panels.append(
            f'<article class="run-card"><h3><span>{esc(item["title"])}</span><span aria-hidden="true">·</span><span class="state state-{esc(item["status"]).lower()}">{esc(item["status"])}</span></h3>'
            f'<dl>{rows}</dl></article>'
        )

    today_rows = []
    for name in ("board", "official", "syncareer", "linkedin", "indeed", "glassdoor"):
        item = report["today"][name]
        status = str(item["status"])
        status_html = (f'<span class="state state-{esc(status).lower()}">{esc(status)}</span>'
                       if status != "No run today" else "No run today")
        shown = item.get("shown_latest")
        new_text = "—" if item["new"] is None else number(item["new"])
        result_parts = ([f"{number(shown)} shown latest"] if shown is not None else [])
        if item.get("pass") is not None:
            result_parts.append(f"{number(item['pass'])} passed today")
        if item.get("new_added") is not None:
            result_parts.append(f"{number(item['new_added'])} new A/B today")
        result = " · ".join(result_parts) or "—"
        today_rows.append(
            f'<tr><th scope="row">{esc(report["components"][name]["label"])}</th>'
            f'<td>{status_html}</td>'
            f'<td class="num">{new_text}</td>'
            f'<td>{esc(result)}</td>'
            f'<td class="num">{esc(str(item["runs"]))}</td>'
            f'<td class="num">{esc(str(item["failed_runs"]))}</td>'
            f'<td class="num">{number(item["consecutive_failures"])}</td>'
            f'<td>{esc(_display_time(item["latest_run"])) if item["latest_run"] else "—"}</td>'
            f'<td>{esc(item.get("issue")) if item.get("issue") else "—"}</td></tr>'
        )

    execution_rows = []
    for name, group in report["groups"].items():
        new = group.get("new_jds_this_run")
        new_text = "—" if new is None else number(new)
        note = str(group.get("new_jds_note") or "")
        note_html = f'<br><small class="execution-note">Breakdown: {esc(note)}</small>' if note else ""
        execution_rows.append(
            f'<tr><th scope="row">{esc(name)}</th>'
            f'<td><span class="state state-{esc(group["run_state"]).lower()}">{esc(group["run_state"])}</span></td>'
            f'<td class="num">{number(group.get("jobs_processed"))}</td>'
            f'<td class="num">{new_text}{note_html}</td>'
            f'<td>{esc(duration(group.get("elapsed_seconds")))}</td></tr>'
        )

    recovery = report["recovery_summary"]
    coverage = report.get("coverage") or {}
    attention = report.get("attention") or []
    attention_html = "".join(f"<li>{esc(item)}</li>" for item in attention) or "<li>None</li>"
    headline_attention = " · ".join(attention[:2]) if attention else "None"
    scheduler = report["local_scheduler"]
    schedule_text = " · ".join((
        f"Last run {_display_time(scheduler['last_successful_local_run_at'])}",
        f"Latest slot {_display_time(scheduler['last_scheduled_slot_at'])}",
        f"Next scheduled run {_display_time(scheduler['next_scheduled_run_at'])}",
        f"Catch-up {str(scheduler['catch_up_status']).replace('_', ' ')}",
        str(scheduler["reason"]),
    ))
    diagnostics = {
        "components": {key: {"status": item.get("status"), "detail": item.get("detail"),
                             "consecutive_failures": item.get("consecutive_failures"),
                             "degradation_kinds": item.get("degradation_kinds"),
                             "retained_inventory": item.get("volumes"),
                             "recent_history": item.get("recent_history"),
                             "latest_http_and_stored_job_reasons": {key: value for key, value in (item.get("latest_run") or {}).items()
                                                                   if key not in {"attempt_at", "search_cooldown_until", "detail_cooldown_until"}}}
                       for key, item in report["components"].items()},
        "groups": report["groups"], "enrichment": report["enrichment"],
        "recovery_summary": recovery, "coverage": coverage,
        "source_run_history": report.get("source_run_history", []),
        "latest_funnels": report.get("latest_funnels", {}),
        "problems": report.get("problems", []), "degradations": report.get("degradations", []),
        "limitations": report.get("limitations", []),
        "unresolved_examples": report.get("unresolved_examples", []),
    }
    style = """
    :root{color-scheme:light}*{box-sizing:border-box}body{font:15px/1.5 system-ui,-apple-system,sans-serif;color:#1b2c25;background:#f8faf8;margin:0}
    main{max-width:1200px;margin:auto;padding:32px 20px 64px}h1{font-size:29px;margin:0}h2{font-size:21px;margin:34px 0 14px}h3{font-size:18px;margin:0 0 12px}
    p{margin:8px 0}a{color:#17654c}.muted,small{color:#607268}small{display:block;font-size:12px;margin-top:2px}
    .top{display:flex;align-items:center;gap:12px;flex-wrap:wrap}.state{display:inline-block;font-size:12px;font-weight:750;padding:3px 8px;border-radius:999px;background:#e7f4ed;color:#176341;white-space:nowrap}
    .state-partial{background:#fff0ce;color:#795309}.state-failed{background:#fae2df;color:#a22f2b}.strip{padding:11px 15px;background:white;border:1px solid #dbe6dd;border-radius:9px;margin-top:10px}
    .run-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.run-card{background:white;border:1px solid #dbe6dd;border-radius:12px;padding:18px 20px;box-shadow:0 3px 10px #1c3c2508}
    .run-card h3{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.run-card dl{margin:0}.run-line{display:grid;grid-template-columns:110px minmax(0,1fr);gap:10px;padding:8px 0;border-top:1px solid #eef2ee}.run-note{margin-top:5px}.execution-note{white-space:normal;text-align:right;margin-top:5px}
    dt{font-weight:700;color:#415d4d}dd{margin:0}.issue dd{color:#9d3b25}.metric-row{display:flex;gap:12px;flex-wrap:wrap}.metric{flex:1;min-width:230px;background:white;border:1px solid #dbe6dd;border-radius:9px;padding:13px 16px}
    .metric strong{display:block;font-size:19px}table{border-collapse:collapse;width:100%;background:white}th,td{padding:9px 11px;text-align:left;border-bottom:1px solid #e4ebe5;vertical-align:top}thead th{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:#61746a}
    .table-wrap{overflow-x:auto;border:1px solid #dbe6dd;border-radius:9px}.num{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}ul{padding-left:22px}li{margin:6px 0}details{border:1px solid #dbe6dd;background:white;border-radius:9px;padding:13px 16px;margin-top:24px}summary{cursor:pointer;font-weight:700}
    pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px;background:#f4f7f4;padding:12px;border-radius:6px}
    @media(max-width:780px){.run-grid{grid-template-columns:1fr}.run-line{grid-template-columns:90px minmax(0,1fr)}main{padding:22px 14px}}
    """
    page = (
        '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>Pipeline Health · {esc(report["overall"])}</title><style>{style}</style><body data-generated-at="{esc(report["generated_at"])}"><main>'
        f'<div class="top"><h1>Pipeline Health</h1><span class="state state-{esc(report["overall"]).lower()}">{esc(report["overall"])}</span></div>'
        '<p id="publicationFreshness" class="strip" role="status" hidden></p>'
        f'<p class="muted">Generated {esc(_display_time(report["generated_at"]))} · '
        '<a href="index.html">Dashboard</a> · <a href="health.json">JSON</a> · '
        '<a href="health-history.json">History</a></p>'
        f'<p class="strip"><strong>Needs attention:</strong> {esc(headline_attention)}</p>'
        '<h2>Latest runs</h2><div class="run-grid">' + "".join(panels) + '</div>'
        '<h2>Today</h2><div class="table-wrap"><table><thead><tr><th>Source</th><th>Status today</th><th class="num">New today</th><th>A/B/pass today</th><th class="num">Runs today</th><th class="num">Failed runs</th><th class="num">Consecutive failures</th><th>Latest run</th><th>Current issue</th></tr></thead><tbody>'
        + "".join(today_rows) + '</tbody></table></div>'
        '<p class="muted">Shown is the latest run result; new A/B is summed across today. A dash means no run or measured result is available for today. Source history begins with the first run after this update.</p>'
        '<h2>Needs attention</h2><ul>' + attention_html + '</ul>'
        '<h2>Execution</h2><div class="table-wrap"><table><thead><tr><th>Runner</th><th>Status</th><th>Jobs processed</th><th>New JDs this run</th><th>Time</th></tr></thead><tbody>'
        + "".join(execution_rows) + '</tbody></table></div>'
        '<details><summary>Technical details</summary>'
        f'<p><strong>Local Mac schedule:</strong> {esc(schedule_text)}</p>'
        '<p><strong>Raw diagnostics</strong> · Subcomponents, request limits, enrichment, retry state, and recovery methods remain in the JSON report. Stored unresolved-job reasons are historical job outcomes, not HTTP failures in the current run.</p>'
        f'<pre>{esc(json.dumps(diagnostics, indent=2, ensure_ascii=False))}</pre>'
        '</details></main><script>'
        + Path(__file__).with_name("dashboard_freshness.js").read_text(encoding="utf-8")
        + '</script></body></html>'
    )
    (public / "health.html").write_text(page, encoding="utf-8")
