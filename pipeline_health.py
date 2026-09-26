"""Build dashboard health from the run/state artifacts each pipeline already owns."""

from __future__ import annotations

import html
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from typing import Any

from state_io import decode_json_bytes

PIPELINES = {
    "board": ("ATS / Board (GitHub)", "board", "jobs.json"),
    "official": ("Big Company Official (GitHub)", "official_careers", "jobs.json"),
    "syncareer": ("Syncareer (GitHub)", "syncareer", "jobs.json"),
}
SEVERITY = {"Healthy": 0, "Warning": 1, "Stale": 2, "Problem": 3}


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
        attempt_failed = not state.get("healthy") and not focused_partial
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
        runtime = (state.get("runner_states") or {}).get("mac", {}) if source == "linkedin" else {}
        targeted_streak = int((local_payload.get("local_recovery") or {}).get("targeted_429_streak", 0) or 0)
        detail_streak = int(runtime.get("detail_429_streak", state.get("detail_429_streak", 0)) or 0)
        failure_threshold = 3 if source == "linkedin" else 2
        if source == "linkedin":
            consecutive_failures = max(consecutive_failures, targeted_streak, detail_streak)
            if status == "Healthy" and consecutive_failures >= failure_threshold and (targeted_streak or detail_streak):
                status = "Warning"
        if status == "Healthy" and attempt_failed and consecutive_failures >= failure_threshold:
            status = "Warning"
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
            details.append(
                f"latest {attempt_kind} attempt{attempt_when} had "
                f"{'rate-limited' if rate_limited_partial else 'focused'} coverage "
                f"({state.get('reason') or 'partial coverage'}): collected {collected} rows, kept {fresh_kept}; "
                f"merged snapshot serves {last_good_count} ({carried} carried, last full collection {verified_age})"
            )
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
            snapshot.get("meta", {}).get("detail_enrichment", {}) if isinstance(snapshot, dict) else {}
        )
        degradation_kinds: list[str] = []
        keywords = []
        if is_partial:
            degradation_kinds.append("rate_limited_partial_collection" if rate_limited_partial else "focused_coverage")
            keywords.extend(("partial", "rate-limited" if rate_limited_partial else "focused coverage", "cached"))
            limitations.append(
                f"{'LinkedIn (local/general)' if source == 'linkedin' else source.title()}: "
                f"{'rate-limited' if rate_limited_partial else 'focused'} partial "
                f"collection; {last_good_count} jobs usable "
                f"({int(state.get('partial_carried_count', 0) or 0)} carried from the last complete run)"
            )
        if source == "linkedin":
            cooldown_until = str(state.get("detail_cooldown_until") or "")
            intentional_pause = state.get("detail_cooldown_reason") == "intentional pause"
            blocked = str(enrichment.get("blocked") or "")
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
                        f"LinkedIn detail intentionally paused/cooldown until {cooldown_until}; "
                        "search/discovery continues; next eligible detail request is a one-job probe"
                    )
                else:
                    details.append(
                        f"LinkedIn detail cooldown ({state.get('detail_cooldown_reason') or 'repeated 429'}); "
                        f"next probe after {cooldown_until}"
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
        if source == "linkedin" and targeted_streak:
            issue = f"LinkedIn targeted 429 ×{targeted_streak}"
        elif source == "linkedin" and detail_streak:
            issue = f"LinkedIn detail 429 ×{detail_streak}"
        elif focused_partial:
            recovered = state.get("previous_failure") or {}
            issue = (f"focused coverage · Recovered, previous {recovered.get('cause')} ×{recovered.get('count')}"
                     if recovered.get("cause") and recovered.get("count") else "focused coverage")
        elif cause:
            issue = f"{source.title()} {cause} ×{consecutive_failures}"
        elif attempt_failed:
            issue = f"{source.title()} {_short_cause(str(state.get('reason') or ''))} ×{consecutive_failures}"
        else:
            recovered = state.get("previous_failure") or {}
            issue = (f"Recovered · previous {recovered.get('cause')} ×{recovered.get('count')}"
                     if recovered.get("cause") and recovered.get("count") else "")
        components[source] = {
            "label": {"linkedin": "LinkedIn (Mac)", "indeed": "Indeed (GitHub)", "glassdoor": "Glassdoor (Mac)"}[source],
            "status": status,
            "detail_status": state.get("detail_status", "") if source == "linkedin" else "",
            "detail": detail,
            "issue": issue,
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
            "failure_streaks": ({"search_429": int(runtime.get("search_429_streak", 0) or 0),
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
        elif item["status"] == "Warning":
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

    overall = max((components[name]["status"] for name in PIPELINES), key=SEVERITY.get)
    report = {
        "generated_at": now.isoformat(),
        "overall": overall,
        "components": components,
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
        "unresolved_examples": unresolved,
    }
    return report, history


def write(public: Path, report: dict[str, Any], history: list[dict[str, Any]]) -> None:
    public.mkdir(parents=True, exist_ok=True)
    (public / "health.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (public / "health-history.json").write_text(json.dumps(history, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    rows = "".join(
        f"<tr><td>{html.escape(item['label'])}</td><td>{html.escape(item['status'])}</td>"
        f"<td>{int(item.get('volumes', {}).get('jobs', 0))} / {int(item.get('volumes', {}).get('jd', 0))} / "
        f"{int(item.get('volumes', {}).get('pass', 0))}</td>"
        f"<td>{html.escape(str(item.get('last_good_at') or 'unknown'))}</td>"
        f"<td>{html.escape(item.get('issue') or '—')}</td>"
        f"<td>{html.escape(str(item.get('consecutive_failures', 0)))}</td></tr>"
        for item in report["components"].values()
    )
    groups = "".join(
        f"<tr><td>{html.escape(name)}</td><td>{html.escape(str(group['status']))}</td>"
        f"<td>{group['jobs_processed']}</td><td>{group['jds_recovered']}</td>"
        f"<td>{html.escape(str(group.get('elapsed_seconds') if group.get('elapsed_seconds') is not None else '—'))}</td></tr>"
        for name, group in report.get("groups", {}).items()
    )
    issues = "".join(f"<li>{html.escape(issue)}</li>" for issue in report["problems"]) or "<li>None</li>"
    degradations = "".join(f"<li>{html.escape(issue)}</li>" for issue in report.get("degradations", [])) or "<li>None</li>"
    limitations = "".join(f"<li>{html.escape(issue)}</li>" for issue in report.get("limitations", [])) or "<li>None</li>"
    examples = "".join(
        f"<li>{html.escape(item['pipeline'])}: <a href=\"{html.escape(item['url'])}\">{html.escape(item['company'])} — {html.escape(item['title'])}</a> — {html.escape(item['reason'])}</li>"
        for item in report["unresolved_examples"]
    ) or "<li>None</li>"
    page = f"""<!doctype html><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>Pipeline health</title><style>body{{font:15px/1.45 system-ui;max-width:1250px;margin:40px auto;padding:0 20px;color:#172019}}table{{border-collapse:collapse;width:100%}}td,th{{padding:8px;border-bottom:1px solid #ddd;text-align:left;vertical-align:top}}code{{background:#eee;padding:2px 4px}}li{{margin:5px 0}}</style><h1>Pipeline health: {report['overall']}</h1><p>Generated {html.escape(report['generated_at'])}. <a href=\"index.html\">Dashboard</a> · <a href=\"health.json\">current JSON</a> · <a href=\"health-history.json\">recent run and batch history</a></p><h2>Components</h2><table><tr><th>Source</th><th>Status</th><th>Jobs / JD / Pass</th><th>Updated</th><th>Issue</th><th>Consecutive failures</th></tr>{rows}</table><h2>Execution</h2><table><tr><th>Component</th><th>Status</th><th>Jobs processed</th><th>JDs recovered</th><th>Elapsed seconds</th></tr>{groups}</table><details><summary>Subcomponents and diagnostics</summary><pre>{html.escape(json.dumps(report.get('groups', {}), indent=2))}</pre><pre>{html.escape(json.dumps({key: item.get('detail') for key, item in report['components'].items()}, indent=2))}</pre></details><h2>Actionable problems</h2><ul>{issues}</ul><h2>Active warnings</h2><ul>{degradations}</ul><h2>Recovered behavior / known limitations</h2><ul>{limitations}</ul><h2>Enrichment funnel</h2><pre>{html.escape(json.dumps(report['enrichment'], indent=2))}</pre><h2>Unresolved JD examples</h2><ul>{examples}</ul>"""
    (public / "health.html").write_text(page, encoding="utf-8")
