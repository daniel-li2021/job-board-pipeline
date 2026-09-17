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
    "board": ("ATS / LinkedIn", "board", "jobs.json"),
    "official": ("Big Company Official", "official_careers", "jobs.json"),
    "syncareer": ("Syncareer", "syncareer", "jobs.json"),
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
                    "funnel": current.get("funnel", {}), "enrichment": current.get("enrichment", {}),
                    "batches_total": llm.get("batches_total", 0), "batches_failed": llm.get("batches_failed", 0),
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
        scope = f"{failed}/{attempted} attempted" if skipped else f"{failed}/{total}"
        skipped_note = f"; {skipped} later batches skipped" if skipped else ""
        return f"{scope} LLM batches failed{reason}{skipped_note}; {fallback} jobs used retryable rule fallback"
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


def _official_failure_partition(base: Path, failures: Any) -> tuple[Any, list[str]]:
    """Remove configured link-only sources from active failures and clarify LinkedIn ownership."""
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
    if "linkedin" in scrape:
        scrape["linkedin_company_official_adapter"] = scrape.pop("linkedin")
    if scrape:
        actionable["scrape"] = scrape
    else:
        actionable.pop("scrape", None)
    limitations = [
        f"Big Company Official: {len(limited)} configured link-only source(s) omitted from active failures ({', '.join(limited)})"
    ] if limited else []
    return actionable, limitations


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
        store_stamp = str(store.get("updated_at") or store.get("scraped_at") or (run_stamp if entries else ""))
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
        shown = int(run.get("output", {}).get("shown", 0) or 0)
        baseline = float(run.get("recent_shown_median", 0) or 0)
        if status == "Healthy" and run.get("mode") != "matching_retry" and baseline >= 10 and shown < baseline * 0.3:
            status = "Warning"
            details.append(f"latest output fell to {shown} vs recent median {baseline:g}")
        failures = run.get("failures") or {}
        known_limitations: list[str] = []
        if key == "official":
            failures, known_limitations = _official_failure_partition(base, failures)
            limitations.extend(known_limitations)
        failure_count, failure_detail = _failure_summary(failures)
        consecutive_failures = _consecutive_degraded(history, key)
        if failure_count:
            llm_impact = _llm_impact(run)
            if status == "Healthy" and (llm_impact or consecutive_failures >= 2):
                status = "Warning"
            qualifier = "degraded" if status == "Warning" else "had recoverable issues"
            details.append(f"latest run {qualifier}: {llm_impact or f'{failure_count} failure(s): {failure_detail}'}")
        workflow_token = {"board": "board", "official": "official", "syncareer": "syncareer"}[key]
        if workflow_conclusion and workflow_conclusion != "success" and workflow_token in workflow_name.lower():
            status = "Warning" if data_usable and data_age is not None and data_age <= 36 else "Problem"
            details.append(f"latest workflow attempt concluded {workflow_conclusion}; last-good data remains {'usable' if data_usable else 'unusable'}")
        detail = "; ".join(details)
        components[key] = {
            "label": label,
            "status": status,
            "detail": detail,
            "updated_at": store_stamp or run_stamp,
            "data_usable": data_usable,
            "last_good_count": len(entries),
            "last_good_at": store_stamp,
            "latest_attempt_at": run_stamp,
            "latest_attempt_age_hours": round(attempt_age, 1) if attempt_age is not None else None,
            "latest_attempt_status": "failed" if workflow_conclusion and workflow_conclusion != "success" and workflow_token in workflow_name.lower() else ("degraded" if failure_count else ("success" if run_stamp else "unknown")),
            "failure_count": failure_count,
            "consecutive_failures": consecutive_failures,
            "impact": _llm_impact(run) or (
                f"latest attempt {'degraded' if status == 'Warning' else 'had recoverable issues'}; fresh last-good snapshot remains usable"
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

    local = _read(base / "output" / "sources" / "health.json", {}).get("sources", {})
    for source in ("linkedin", "indeed", "glassdoor"):
        state = local.get(source, {})
        snapshot = _read(base / "output" / "sources" / f"{source}.json", {})
        snapshot_jobs = list(snapshot.get("jobs") or []) if isinstance(snapshot, dict) else []
        age = _age_hours(str(state.get("last_success_at") or ""), now)
        attempt_age = _age_hours(str(state.get("last_attempt_at") or ""), now)
        last_good_count = len(snapshot_jobs)
        data_usable = last_good_count > 0 and age is not None
        attempt_failed = not state.get("healthy")
        if not data_usable:
            status = "Problem" if state.get("required", source != "glassdoor") else "Warning"
        elif age > 12:
            status = "Stale"
        elif age > 6:
            status = "Warning"
        else:
            status = "Healthy"
        consecutive_failures = int(state.get("consecutive_failures", 1 if attempt_failed else 0) or 0)
        if attempt_failed and consecutive_failures >= 2:
            status = "Warning"
        details = [
            f"Usable last-good snapshot: {last_good_count} jobs, {age:.1f}h old"
            if data_usable else "No usable last-good snapshot"
        ]
        if attempt_failed:
            attempt_kind = "search/discovery" if source == "linkedin" else "collection"
            attempt_when = f" {attempt_age:.1f}h ago" if attempt_age is not None else ""
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
        if source == "linkedin" and enrichment:
            blocked = str(enrichment.get("blocked") or "")
            scrapling_requests = int(enrichment.get("scrapling_requests", 0) or 0)
            scrapling_resolved = int(enrichment.get("scrapling_jds_resolved", 0) or 0)
            remaining = int(enrichment.get("remaining_no_jd", 0) or 0)
            if blocked:
                degradation_kinds.append("detail_enrichment_blocked")
                details.append(f"primary detail enrichment blocked: {blocked}")
            if scrapling_requests:
                details.append(f"Scrapling fallback recovered {scrapling_resolved}/{scrapling_requests} attempted JDs")
            if enrichment.get("scrapling_error"):
                degradation_kinds.append("scrapling_limited")
                details.append(f"Scrapling fallback unavailable: {enrichment['scrapling_error']}")
            if remaining:
                degradation_kinds.append("missing_descriptions")
                details.append(f"{remaining} discovered records remain without a JD")
            recovery_ratio = scrapling_resolved / scrapling_requests if scrapling_requests else 0.0
            material_missing = remaining >= max(10, round(last_good_count * 0.05))
            poor_recovery = bool(blocked) and (not scrapling_requests or recovery_ratio < 0.9)
            if (enrichment.get("scrapling_error") or poor_recovery or material_missing) and status == "Healthy":
                status = "Warning"
            elif blocked or remaining:
                limitations.append(
                    f"LinkedIn (local/general): recovered detail limitation; Scrapling resolved "
                    f"{scrapling_resolved}/{scrapling_requests}, {remaining} JD(s) remain"
                )
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
        components[source] = {
            "label": {"linkedin": "LinkedIn (local/general)", "indeed": "Indeed", "glassdoor": "Glassdoor"}[source],
            "status": status,
            "detail": detail,
            "updated_at": state.get("last_success_at", ""),
            "data_usable": data_usable,
            "last_good_count": last_good_count,
            "last_good_at": state.get("last_success_at", ""),
            "latest_attempt_at": state.get("last_attempt_at", ""),
            "latest_attempt_age_hours": round(attempt_age, 1) if attempt_age is not None else None,
            "latest_attempt_status": state.get("status", "unknown"),
            "degradation_kinds": degradation_kinds,
            "consecutive_failures": consecutive_failures,
            "impact": (
                f"collection failed; {last_good_count} last-good jobs remain usable"
                if attempt_failed and data_usable else
                ("required source has no usable data" if not data_usable and state.get("required", source != "glassdoor") else "")
            ),
        }

    board_statuses = [components[name]["status"] for name in ("linkedin", "indeed", "glassdoor")]
    if components["board"]["status"] == "Healthy" and any(status != "Healthy" for status in board_statuses):
        components["board"]["status"] = "Warning"
        affected = [
            f"{name}={components[name]['status']} ({components[name]['detail']})"
            for name in ("linkedin", "indeed", "glassdoor")
            if components[name]["status"] != "Healthy"
        ]
        components["board"]["detail"] += "; local inputs: " + "; ".join(affected)

    for item in components.values():
        summary = f"{item['label']}: {item['detail']}"
        if item["status"] in {"Problem", "Stale"}:
            problems.append(summary)
        elif item["status"] == "Warning":
            degradations.append(summary)

    overall = max((item["status"] for item in components.values()), key=SEVERITY.get)
    report = {
        "generated_at": now.isoformat(),
        "overall": overall,
        "components": components,
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
        f"<tr><td>{html.escape(item['label'])}</td><td>{item['status']}</td>"
        f"<td>{html.escape(str(item.get('last_good_count', 0)))} at {html.escape(str(item.get('last_good_at') or 'unknown'))}</td>"
        f"<td>{html.escape(str(item.get('latest_attempt_status') or 'unknown'))} at {html.escape(str(item.get('latest_attempt_at') or 'unknown'))}</td>"
        f"<td>{html.escape(str(item.get('consecutive_failures', 0)))}</td><td>{html.escape(item['detail'])}</td></tr>"
        for item in report["components"].values()
    )
    issues = "".join(f"<li>{html.escape(issue)}</li>" for issue in report["problems"]) or "<li>None</li>"
    degradations = "".join(f"<li>{html.escape(issue)}</li>" for issue in report.get("degradations", [])) or "<li>None</li>"
    limitations = "".join(f"<li>{html.escape(issue)}</li>" for issue in report.get("limitations", [])) or "<li>None</li>"
    examples = "".join(
        f"<li>{html.escape(item['pipeline'])}: <a href=\"{html.escape(item['url'])}\">{html.escape(item['company'])} — {html.escape(item['title'])}</a> — {html.escape(item['reason'])}</li>"
        for item in report["unresolved_examples"]
    ) or "<li>None</li>"
    page = f"""<!doctype html><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>Pipeline health</title><style>body{{font:15px/1.45 system-ui;max-width:1250px;margin:40px auto;padding:0 20px;color:#172019}}table{{border-collapse:collapse;width:100%}}td,th{{padding:8px;border-bottom:1px solid #ddd;text-align:left;vertical-align:top}}code{{background:#eee;padding:2px 4px}}li{{margin:5px 0}}</style><h1>Pipeline health: {report['overall']}</h1><p>Generated {html.escape(report['generated_at'])}. <a href=\"index.html\">Dashboard</a> · <a href=\"health.json\">current JSON</a> · <a href=\"health-history.json\">recent run and batch history</a></p><h2>Components</h2><table><tr><th>Pipeline/source</th><th>Status</th><th>Last good</th><th>Latest attempt</th><th>Consecutive failures</th><th>Impact / detail</th></tr>{rows}</table><h2>Actionable problems</h2><ul>{issues}</ul><h2>Active warnings</h2><ul>{degradations}</ul><h2>Recovered behavior / known limitations</h2><ul>{limitations}</ul><h2>Enrichment funnel</h2><pre>{html.escape(json.dumps(report['enrichment'], indent=2))}</pre><h2>Unresolved JD examples</h2><ul>{examples}</ul>"""
    (public / "health.html").write_text(page, encoding="utf-8")
