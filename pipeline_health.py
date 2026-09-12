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

PIPELINES = {
    "board": ("ATS / LinkedIn", "board", "jobs.json"),
    "official": ("Big Company Official", "official_careers", "jobs.json"),
    "syncareer": ("Syncareer", "syncareer", "watchlist.json"),
}
SEVERITY = {"Healthy": 0, "Warning": 1, "Stale": 2, "Problem": 3}


def _read(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def _age_hours(value: str, now: datetime) -> float | None:
    try:
        stamp = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            stamp = stamp.replace(tzinfo=timezone.utc)
        return max(0.0, (now - stamp.astimezone(timezone.utc)).total_seconds() / 3600)
    except (TypeError, ValueError):
        return None


def _run_history(base: Path) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    latest: dict[str, dict[str, Any]] = {}
    history: list[dict[str, Any]] = []
    for key, (_label, folder, _store) in PIPELINES.items():
        records = []
        for path in sorted((base / "output" / folder / "runs").glob("*_stats.json"))[-20:]:
            record = _read(path, {})
            if record:
                records.append(record)
                history.append({
                    "pipeline": key,
                    "run_at": record.get("run_at", ""),
                    "output": record.get("output", {}),
                    "enrichment": record.get("enrichment", {}),
                })
        if records:
            latest[key] = records[-1]
            shown = [int(item.get("output", {}).get("shown", 0) or 0) for item in records[-7:-1]]
            if shown:
                latest[key]["recent_shown_median"] = median(shown)
    history.sort(key=lambda item: str(item.get("run_at") or ""), reverse=True)
    return latest, history[:40]


def build(base: Path, now: datetime | None = None) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    now = now or datetime.now(timezone.utc)
    latest, history = _run_history(base)
    components: dict[str, dict[str, Any]] = {}
    problems: list[str] = []
    unresolved: list[dict[str, str]] = []
    failure_reasons: Counter[str] = Counter()

    workflow_name = os.getenv("PIPELINE_WORKFLOW_NAME", "")
    workflow_conclusion = os.getenv("PIPELINE_WORKFLOW_CONCLUSION", "")
    workflow_url = os.getenv("PIPELINE_WORKFLOW_URL", "")

    for key, (label, folder, store_name) in PIPELINES.items():
        store = _read(base / "output" / folder / store_name, {})
        entries = list(store.get("entries") or []) if isinstance(store, dict) else []
        run = latest.get(key, {})
        stamp = str(run.get("run_at") or store.get("updated_at") or store.get("scraped_at") or "")
        age = _age_hours(stamp, now)
        status = "Healthy"
        detail = f"Last run {age:.1f}h ago" if age is not None else "No usable run timestamp"
        if age is None or age > 36:
            status = "Stale"
        shown = int(run.get("output", {}).get("shown", 0) or 0)
        baseline = float(run.get("recent_shown_median", 0) or 0)
        if status == "Healthy" and baseline >= 10 and shown < baseline * 0.3:
            status = "Warning"
            detail += f"; output {shown} vs recent median {baseline:g}"
        failures = run.get("failures") or {}
        if status == "Healthy" and any(bool(value) for value in failures.values()):
            status = "Warning"
            detail += "; run recorded scrape/auth/LLM failures"
        workflow_token = {"board": "board", "official": "official", "syncareer": "syncareer"}[key]
        if workflow_conclusion and workflow_conclusion != "success" and workflow_token in workflow_name.lower():
            status = "Problem"
            detail = f"Latest workflow concluded {workflow_conclusion}"
        components[key] = {"label": label, "status": status, "detail": detail, "updated_at": stamp}
        if status != "Healthy":
            problems.append(f"{label}: {detail}")

        for entry in entries:
            description = str(entry.get("description") or "").strip()
            if len(description) >= 200 or str(entry.get("filter_status") or "kept") not in {"kept", ""}:
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
        age = _age_hours(str(state.get("last_success_at") or ""), now)
        if not state.get("healthy"):
            status = "Problem" if state.get("required", source != "glassdoor") else "Warning"
        elif age is None or age > 12:
            status = "Stale"
        elif age > 6:
            status = "Warning"
        else:
            status = "Healthy"
        detail = str(state.get("reason") or (f"Last success {age:.1f}h ago" if age is not None else "No successful snapshot"))
        components[source] = {"label": source.title(), "status": status, "detail": detail, "updated_at": state.get("last_success_at", "")}
        if status != "Healthy":
            problems.append(f"{source.title()}: {detail}")

    board_statuses = [components[name]["status"] for name in ("linkedin", "indeed", "glassdoor")]
    if components["board"]["status"] == "Healthy" and any(status != "Healthy" for status in board_statuses):
        components["board"]["status"] = "Warning"
        components["board"]["detail"] += "; one or more local sources degraded"

    overall = max((item["status"] for item in components.values()), key=SEVERITY.get)
    report = {
        "generated_at": now.isoformat(),
        "overall": overall,
        "components": components,
        "problems": problems,
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
        f"<tr><td>{html.escape(item['label'])}</td><td>{item['status']}</td><td>{html.escape(item['detail'])}</td></tr>"
        for item in report["components"].values()
    )
    issues = "".join(f"<li>{html.escape(issue)}</li>" for issue in report["problems"]) or "<li>None</li>"
    examples = "".join(
        f"<li>{html.escape(item['pipeline'])}: <a href=\"{html.escape(item['url'])}\">{html.escape(item['company'])} — {html.escape(item['title'])}</a> — {html.escape(item['reason'])}</li>"
        for item in report["unresolved_examples"]
    ) or "<li>None</li>"
    page = f"""<!doctype html><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>Pipeline health</title><style>body{{font:15px/1.45 system-ui;max-width:1050px;margin:40px auto;padding:0 20px;color:#172019}}table{{border-collapse:collapse;width:100%}}td,th{{padding:8px;border-bottom:1px solid #ddd;text-align:left}}code{{background:#eee;padding:2px 4px}}li{{margin:5px 0}}</style><h1>Pipeline health: {report['overall']}</h1><p>Generated {html.escape(report['generated_at'])}. <a href=\"index.html\">Dashboard</a> · <a href=\"health.json\">current JSON</a> · <a href=\"health-history.json\">recent run history</a></p><h2>Components</h2><table><tr><th>Pipeline/source</th><th>Status</th><th>Detail</th></tr>{rows}</table><h2>Actionable problems</h2><ul>{issues}</ul><h2>Enrichment funnel</h2><pre>{html.escape(json.dumps(report['enrichment'], indent=2))}</pre><h2>Unresolved JD examples</h2><ul>{examples}</ul>"""
    (public / "health.html").write_text(page, encoding="utf-8")
