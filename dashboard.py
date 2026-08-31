#!/usr/bin/env python3
"""Generate the read-only GitHub Pages job dashboard."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from zoneinfo import ZoneInfo

import coverage_reconcile
import alert_history
from sources.company_aliases import load_alias_file, match_company_alias
from sources.schema import classify_location_bucket

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"
DASHBOARD_JSON = PUBLIC_DIR / "dashboard.json"
DASHBOARD_HTML = PUBLIC_DIR / "index.html"
REPO_URL = "https://github.com/daniel-li2021/job-board-pipeline"
PAGES_URL = "https://daniel-li2021.github.io/job-board-pipeline/"
PACIFIC = ZoneInfo("America/Los_Angeles")
REFERRAL_PATH = BASE_DIR / "source" / "target_companies.json"
COMPANY_FILTERS_PATH = BASE_DIR / "profile" / "company_filters.json"
OFFICIAL_REGISTRY_PATH = BASE_DIR / "source" / "official_careers.json"
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://wzriavtjqfpkeafeisfv.supabase.co")
SUPABASE_PUBLISHABLE_KEY = os.getenv(
    "SUPABASE_PUBLISHABLE_KEY", "sb_publishable_uYhplHl4QV7h5sKcItb4vg_UP9uiAQF"
)
ALERT_HISTORY_PATHS = {
    "board": BASE_DIR / "output" / "board" / "alert_history.json",
    "official": BASE_DIR / "output" / "official_careers" / "alert_history.json",
    "syncareer": BASE_DIR / "output" / "syncareer" / "alert_history.json",
}
ISSUE_BODY_PATHS = {
    "board": BASE_DIR / "output" / "board" / "issue_body.md",
    "official": BASE_DIR / "output" / "alerts" / "official_issue_body.md",
    "syncareer": BASE_DIR / "output" / "syncareer" / "issue_body.md",
}

STORE_PATHS = {
    "board": BASE_DIR / "output" / "board" / "jobs.json",
    "official": BASE_DIR / "output" / "official_careers" / "jobs.json",
    "syncareer": BASE_DIR / "output" / "syncareer" / "watchlist.json",
}
REPORT_PATHS = {
    "board": "output/board/inbox.md",
    "official": "output/official_careers/inbox.md",
    "syncareer": "output/syncareer/inbox.md",
}


def read_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def parse_dt(value: Any) -> Optional[datetime]:
    return coverage_reconcile.parse_datetime(value)


def _load_entries(path: Path) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    payload = read_json(path, {})
    if not isinstance(payload, dict):
        return {}, []
    entries = payload.get("entries", [])
    return payload, [dict(entry) for entry in entries if isinstance(entry, dict)]


def parse_issue_event(path: Path, pipeline: str) -> Optional[Dict[str, Any]]:
    """Parse the latest tracked Issue body as a migration fallback."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    stamp_match = re.search(r"(\d{4}-\d{2}-\d{2}_\d{4})", "\n".join(lines[:8]))
    if not stamp_match:
        return None
    stamp = stamp_match.group(1)
    emitted = alert_history.parse_stamp(stamp)
    if not emitted:
        return None
    header_index = next((i for i, line in enumerate(lines) if line.strip().startswith("|") and "Company" in line), -1)
    if header_index < 0:
        return None
    headers = [cell.strip().lower() for cell in lines[header_index].strip().strip("|").split("|")]
    jobs: List[Dict[str, Any]] = []
    for line in lines[header_index + 2:]:
        if not line.strip().startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != len(headers):
            continue
        values = dict(zip(headers, cells))
        link_cell = values.get("link", "")
        link_match = re.search(r"\[[^]]*\]\(([^)]+)\)", link_cell)
        jobs.append({
            "tier": values.get("tier") or "-",
            "match_score": values.get("score") or values.get("fit") or "",
            "company": values.get("company", ""),
            "title": values.get("title", ""),
            "location": values.get("location", ""),
            "posted_date": values.get("posted", ""),
            "referral_name": "" if values.get("referral", "-") == "-" else values.get("referral", ""),
            "url": link_match.group(1) if link_match else "",
            "source": pipeline,
        })
    return {
        "pipeline": pipeline,
        "stamp": stamp,
        "emitted_at": emitted.isoformat(),
        "event_kind": "issue_body_fallback",
        "count": len(jobs),
        "jobs": jobs,
    }


def _age_bucket(age_hours: Optional[float]) -> str:
    if age_hours is None:
        return "unknown"
    if age_hours < 3:
        return "lt3h"
    if age_hours < 24:
        return "3to24h"
    if age_hours <= 72:
        return "1to3d"
    if age_hours <= 168:
        return "3to7d"
    return "gt7d"


def _age_hours(value: Optional[datetime], now: datetime) -> Optional[float]:
    return round(max(0.0, (now - value).total_seconds() / 3600), 2) if value else None


def recency(job: Dict[str, Any], now: datetime) -> Dict[str, Any]:
    """Expose posting recency and discovery activity as separate signals."""
    confidence = str(job.get("date_confidence") or "unknown").lower()
    posted_raw = str(job.get("posted_date") or job.get("posting_date") or "").strip()
    posted = parse_dt(posted_raw)
    first_seen = parse_dt(job.get("first_seen"))
    trusted = confidence in {"high", "medium"} and posted is not None
    date_only = bool(posted_raw) and len(posted_raw) == 10
    posted_age = _age_hours(posted, now) if trusted else None
    discovered_age = _age_hours(first_seen, now)
    posted_bucket = _age_bucket(posted_age)
    discovered_bucket = _age_bucket(discovered_age)

    if trusted:
        bucket = posted_bucket
        kind = "confirmed_posted_date_only" if date_only else "confirmed_posted"
        reference_at = posted.isoformat() if posted else ""
        age_hours = posted_age
    elif first_seen:
        bucket = "newly_discovered" if (discovered_age or 0) <= 72 else discovered_bucket
        kind = "newly_discovered"
        reference_at = first_seen.isoformat()
        age_hours = discovered_age
    else:
        bucket, kind, reference_at, age_hours = "unknown", "unknown", "", None
    return {
        "bucket": bucket,
        "kind": kind,
        "age_hours": age_hours,
        "reference_at": reference_at,
        "posted": {"bucket": posted_bucket, "age_hours": posted_age, "at": posted.isoformat() if posted and trusted else "", "date_only": date_only, "trusted": trusted},
        "discovered": {"bucket": discovered_bucket, "age_hours": discovered_age, "at": first_seen.isoformat() if first_seen else ""},
        # Dashboard windows intentionally follow discovery/Issue activity, not
        # the employer's posting date. posted_date remains reference metadata.
        "fresh_activity": discovered_age is not None and discovered_age <= 24,
        "rolling_activity": discovered_age is not None and discovered_age <= 72,
    }


def sponsorship_label(entry: Dict[str, Any]) -> str:
    """Map existing source sponsorship data to the dashboard's small vocabulary."""
    raw = str(
        entry.get("sponsorship")
        or entry.get("sponsorship_status")
        or entry.get("visa_sponsorship")
        or ""
    ).strip().lower()
    if not raw or raw == "unknown":
        return "Unknown"
    if re.search(r"\b(?:no|not|without|ineligible)\b.*\bsponsor", raw):
        return "No sponsor"
    if "sponsor" in raw:
        return "Sponsor"
    return "Unknown"


def normalize_row(
    entry: Dict[str, Any],
    pipeline: str,
    now: datetime,
    referrals: List[Dict[str, Any]],
    coverage_by_key: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    if pipeline == "syncareer":
        entry.setdefault("source_url", entry.get("job_url") or entry.get("url") or "")
        entry.setdefault("official_url", entry.get("job_url") or entry.get("url") or "")
        entry.setdefault("posted_date", entry.get("posting_date") or "")
        entry.setdefault("date_confidence", "medium")
        entry.setdefault("filter_status", "kept" if str(entry.get("kept", "")).lower() in {"yes", "true", "1"} else "dropped")
        entry.setdefault("tier", entry.get("tier") or "-")
    key = entry.get("canonical_job_key") or coverage_reconcile.canonical_job_key(entry)
    audit = coverage_by_key.get(key, {})
    referral = entry.get("referral_name") or entry.get("target_company_match") or match_company_alias(str(entry.get("company") or ""), referrals) or ""
    freshness = recency(entry, now)
    return {
        "canonical_job_key": key,
        "pipeline": pipeline,
        "source": entry.get("source") or pipeline,
        "company": entry.get("company", ""),
        "title": entry.get("title", ""),
        "location": entry.get("location", ""),
        "posted_date": entry.get("posted_date") or entry.get("posting_date") or "",
        "first_seen": entry.get("first_seen", ""),
        "date_confidence": entry.get("date_confidence", "unknown"),
        "freshness": freshness,
        "tier": entry.get("tier") or "-",
        "score": entry.get("match_score") if entry.get("match_score") is not None else entry.get("fit_score", ""),
        "sponsorship": sponsorship_label(entry),
        "referral": referral,
        "review_status": "unreviewed",
        "review_updated_at": "",
        "coverage_status": audit.get("coverage_status") or entry.get("coverage_status") or ("official_canonical" if pipeline == "official" else "not_reconciled"),
        "canonical_source": audit.get("canonical_source") or entry.get("canonical_source") or pipeline,
        "duplicate_of": audit.get("duplicate_of") or entry.get("duplicate_of") or "",
        "url": entry.get("official_url") or entry.get("source_url") or entry.get("job_url") or entry.get("url") or "",
        "filter_status": entry.get("filter_status", "kept"),
        "suppress_alert": bool(audit.get("suppress_alert") or entry.get("suppress_alert")),
    }


def visible_candidate(
    row: Dict[str, Any], hard_excludes: Optional[List[Dict[str, Any]]] = None
) -> bool:
    if match_company_alias(str(row.get("company") or ""), hard_excludes or []):
        return False
    if row.get("filter_status") not in {"kept", ""}:
        return False
    if row.get("suppress_alert"):
        return False
    if classify_location_bucket(str(row.get("location") or "")) == "non_us":
        return False
    tier = str(row.get("tier") or "-")
    return tier in {"A", "B", "1", "2", "-"}


def fallback_c_candidate(row: Dict[str, Any]) -> bool:
    """Presentation-only eligibility for stored Board Tier C fallback rows."""
    if row.get("pipeline") != "board" or str(row.get("tier") or "") != "C":
        return False
    if row.get("filter_status") not in {"kept", ""} or row.get("suppress_alert"):
        return False
    if classify_location_bucket(str(row.get("location") or "")) == "non_us":
        return False
    try:
        return float(row.get("score")) >= 60
    except (TypeError, ValueError):
        return False


def append_board_c_fallback(
    rows: Iterable[Dict[str, Any]],
    all_rows: Iterable[Dict[str, Any]],
    *,
    minimum_ab: int,
    target: int,
    window: str,
) -> List[Dict[str, Any]]:
    """Append stored Board C rows only when that Board view has too few A/B jobs."""
    result = list(rows)
    board_ab = sum(
        row.get("pipeline") == "board" and str(row.get("tier") or "") in {"A", "B", "1", "2"}
        for row in result
    )
    if board_ab >= minimum_ab:
        return result

    existing = {
        str(row.get("canonical_job_key") or coverage_reconcile.normalize_url(str(row.get("url") or "")))
        for row in result
    }
    activity_flag = "fresh_activity" if window == "fresh" else "rolling_activity"
    candidates = []
    for row in all_rows:
        stable = str(row.get("canonical_job_key") or coverage_reconcile.normalize_url(str(row.get("url") or "")))
        if stable in existing:
            continue
        if fallback_c_candidate(row) and row.get("freshness", {}).get(activity_flag):
            candidates.append(dict(row, dashboard_fallback=True))

    candidates.sort(key=lambda row: (
        -float(row.get("score") or 0),
        row.get("freshness", {}).get("discovered", {}).get("age_hours")
        if row.get("freshness", {}).get("discovered", {}).get("age_hours") is not None else 999999,
        str(row.get("company") or "").lower(),
    ))
    needed = max(0, target - board_ab)
    strong = [row for row in candidates if float(row.get("score") or 0) >= 65]
    secondary = [row for row in candidates if 60 <= float(row.get("score") or 0) < 65]
    result.extend((strong + secondary)[:needed])
    return result


def config_company_match(company: str, title: str, entries: List[Dict[str, Any]]) -> Optional[str]:
    title_key = str(title or "").lower()
    eligible = [
        entry for entry in entries
        if not entry.get("title_terms")
        or any(str(term).lower() in title_key for term in entry["title_terms"])
    ]
    return match_company_alias(company, eligible)


def _sort_rows(rows: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    bucket_rank = {"lt3h": 0, "3to24h": 1, "1to3d": 2, "newly_discovered": 3, "3to7d": 4, "gt7d": 5, "unknown": 6}
    tier_rank = {"A": 0, "1": 0, "B": 1, "2": 1, "-": 2}
    return sorted(
        rows,
        key=lambda row: (
            tier_rank.get(str(row.get("tier") or "-"), 3),
            row.get("activity_age_hours") if row.get("activity_age_hours") is not None else (
                row["freshness"]["discovered"]["age_hours"]
                if row["freshness"]["discovered"]["age_hours"] is not None else 999999
            ),
            -float(row.get("score") or 0),
            bucket_rank.get(row["freshness"]["posted"]["bucket"], 9),
            str(row.get("company") or "").lower(),
        ),
    )


def alert_fresh_rows(
    all_rows: List[Dict[str, Any]], now: datetime,
    hard_excludes: Optional[List[Dict[str, Any]]] = None,
) -> Tuple[List[Dict[str, Any]], Dict[str, str]]:
    """Build Fresh from exact alert events, not inferred first_seen values."""
    by_key = {str(row.get("canonical_job_key") or ""): row for row in all_rows if row.get("canonical_job_key")}
    by_key_pipeline = {
        (str(row.get("pipeline") or ""), str(row.get("canonical_job_key") or "")): row
        for row in all_rows if row.get("canonical_job_key")
    }
    by_url = {
        coverage_reconcile.normalize_url(str(row.get("url") or "")): row
        for row in all_rows if row.get("url")
    }
    by_url_pipeline = {
        (str(row.get("pipeline") or ""), coverage_reconcile.normalize_url(str(row.get("url") or ""))): row
        for row in all_rows if row.get("url")
    }
    chosen: Dict[str, Dict[str, Any]] = {}
    basis: Dict[str, str] = {}
    for pipeline in STORE_PATHS:
        events = alert_history.recent_events(ALERT_HISTORY_PATHS[pipeline], now, hours=24)
        fallback = parse_issue_event(ISSUE_BODY_PATHS[pipeline], pipeline)
        if fallback:
            fallback_at = parse_dt(fallback.get("emitted_at"))
            known_stamps = {str(event.get("stamp") or "") for event in events}
            if fallback_at and (now - fallback_at).total_seconds() <= 24 * 3600 and fallback.get("stamp") not in known_stamps:
                events.append(fallback)
        if events:
            basis[pipeline] = "alert_history_or_issue"
        else:
            # One-release migration guard for official, whose prior Issue body
            # was ignored by git. New runs immediately create alert_history.
            basis[pipeline] = "first_seen_migration_fallback"
            for row in all_rows:
                if row.get("pipeline") == pipeline and row["freshness"]["fresh_activity"]:
                    event_at = row.get("first_seen")
                    events.append({
                        "pipeline": pipeline,
                        "stamp": "",
                        "emitted_at": event_at,
                        "event_kind": "first_seen_migration_fallback",
                        "jobs": [{"canonical_job_key": row.get("canonical_job_key"), "url": row.get("url")}],
                    })

        for event in events:
            emitted_at = parse_dt(event.get("emitted_at")) or alert_history.parse_stamp(str(event.get("stamp") or ""))
            if not emitted_at:
                continue
            activity_age = _age_hours(emitted_at, now)
            if activity_age is None or activity_age > 24:
                continue
            for snapshot in event.get("jobs", []):
                if not isinstance(snapshot, dict):
                    continue
                key = str(snapshot.get("canonical_job_key") or "")
                url_key = coverage_reconcile.normalize_url(str(snapshot.get("url") or snapshot.get("official_url") or snapshot.get("source_url") or snapshot.get("job_url") or ""))
                source_row = (
                    by_key_pipeline.get((pipeline, key))
                    or by_url_pipeline.get((pipeline, url_key))
                    or by_key.get(key)
                    or by_url.get(url_key)
                )
                if not source_row:
                    continue
                row = dict(source_row)
                if not visible_candidate(row, hard_excludes):
                    continue
                row["alerted_at"] = emitted_at.isoformat()
                row["alert_stamp"] = event.get("stamp", "")
                row["alert_kind"] = event.get("event_kind", "")
                row["activity_age_hours"] = activity_age
                # Fresh mirrors alert activity. The same canonical job may
                # legitimately appear in both an ATS Issue and an Official
                # Issue, so deduplicate within a pipeline, not across them.
                stable = f"{pipeline}::{row.get('canonical_job_key') or url_key}"
                previous = chosen.get(stable)
                if previous is None or float(previous.get("activity_age_hours") or 999999) > activity_age:
                    chosen[stable] = row
    return _sort_rows(chosen.values()), basis


def official_search_catalog() -> List[Dict[str, Any]]:
    registry = read_json(OFFICIAL_REGISTRY_PATH, {})
    companies: List[Dict[str, Any]] = []
    for company in registry.get("companies", []) if isinstance(registry, dict) else []:
        if not isinstance(company, dict) or not company.get("enabled"):
            continue
        links = company.get("search_links") or []
        if isinstance(links, str):
            links = [{"label": "Official search", "url": links}]
        companies.append({
            "id": company.get("id", ""),
            "name": company.get("name", ""),
            "priority_tier": company.get("priority_tier", ""),
            "adapter": company.get("adapter", ""),
            "automation": "active" if company.get("adapter") != "skip" else "search_link_only",
            "search_links": [link for link in links if isinstance(link, dict) and link.get("url")],
            "note": company.get("skip_reason", "") if company.get("adapter") == "skip" else "",
        })
    return sorted(companies, key=lambda item: (
        {"A": 0, "B": 1, "C": 2}.get(str(item["priority_tier"]), 3),
        item["automation"] != "active",
        str(item["name"]).lower(),
    ))


def build_payload(now: Optional[datetime] = None) -> Dict[str, Any]:
    now = now or datetime.now(timezone.utc)
    referrals = load_alias_file(REFERRAL_PATH)
    hard_excludes = load_alias_file(COMPANY_FILTERS_PATH, key="exclude")
    practical_skips = load_alias_file(COMPANY_FILTERS_PATH, key="clearance_risk")
    coverage = coverage_reconcile.build_coverage_payload(now)
    coverage_by_key = {record.get("canonical_job_key", ""): record for record in coverage.get("records", [])}

    snapshots: Dict[str, str] = {}
    all_rows: List[Dict[str, Any]] = []
    for pipeline, path in STORE_PATHS.items():
        store, entries = _load_entries(path)
        snapshots[pipeline] = str(store.get("updated_at") or store.get("scraped_at") or "")
        for entry in entries:
            practical = config_company_match(
                str(entry.get("company") or ""), str(entry.get("title") or ""), practical_skips
            )
            if practical and not entry.get("clearance_risk_company"):
                continue
            all_rows.append(normalize_row(entry, pipeline, now, referrals, coverage_by_key))

    eligible_rows = [
        row for row in all_rows
        if not match_company_alias(str(row.get("company") or ""), hard_excludes)
    ]
    candidates = [row for row in eligible_rows if visible_candidate(row, hard_excludes)]
    current = candidates
    fresh, fresh_basis = alert_fresh_rows(eligible_rows, now, hard_excludes)
    fresh = append_board_c_fallback(fresh, eligible_rows, minimum_ab=10, target=20, window="fresh")
    rolling = _sort_rows(row for row in current if row["freshness"]["rolling_activity"])
    rolling = append_board_c_fallback(rolling, eligible_rows, minimum_ab=30, target=50, window="rolling")
    older = _sort_rows(
        row for row in current
        if row["freshness"]["discovered"]["age_hours"] is not None
        and 72 < row["freshness"]["discovered"]["age_hours"] <= 168
    )
    referral_rows = _sort_rows(
        row for row in current
        if row.get("referral")
        and row["freshness"]["discovered"]["age_hours"] is not None
        and row["freshness"]["discovered"]["age_hours"] <= 168
    )

    def counts(rows: Iterable[Dict[str, Any]]) -> Dict[str, int]:
        result = Counter(row["pipeline"] for row in rows)
        return {pipeline: result.get(pipeline, 0) for pipeline in STORE_PATHS}

    return {
        "generated_at": now.isoformat(),
        "updated_pt": now.astimezone(PACIFIC).strftime("%b %-d, %Y · %-I:%M %p"),
        "pages_url": PAGES_URL,
        "repository": REPO_URL,
        "snapshots": snapshots,
        "report_links": {key: f"{REPO_URL}/blob/main/{path}" for key, path in REPORT_PATHS.items()},
        "referral_file": f"{REPO_URL}/blob/main/source/target_companies.json",
        "coverage_report": f"{REPO_URL}/blob/main/output/cross_pipeline/coverage.md",
        "supabase": {"url": SUPABASE_URL, "publishable_key": SUPABASE_PUBLISHABLE_KEY},
        "counts_24h": counts(fresh),
        "counts_3d": counts(rolling),
        "fresh_24h": fresh[:500],
        "fresh_basis": fresh_basis,
        "rolling_3d": rolling[:1000],
        "referrals": referral_rows[:500],
        "older_review": older[:500],
        # Shared status changes need a complete row pool so a job can move
        # between sections immediately without regenerating static job data.
        "workflow_rows": _sort_rows(candidates)[:2000],
        "coverage": coverage,
        "official_searches": official_search_catalog(),
    }


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Daniel's Job Board</title>
<style>
:root{--bg:#f4f6f1;--card:#fff;--ink:#152018;--muted:#687269;--line:#dce2da;--green:#176b45;--gold:#ad6c00;--blue:#275fa8;--red:#9d3b31}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.wrap{max-width:1440px;margin:auto;padding:28px}header{display:flex;justify-content:space-between;gap:20px;align-items:flex-end;margin-bottom:14px}.header-actions{display:flex;gap:12px;align-items:center;flex-wrap:wrap;justify-content:flex-end}h1{font-size:30px;letter-spacing:-.03em;margin:0}h2{font-size:20px;margin:0 0 12px}p{margin:5px 0;color:var(--muted)}a{color:var(--blue)}button,select{font:inherit}
.section-nav{position:sticky;top:0;z-index:30;display:flex;gap:4px;width:max-content;max-width:100%;margin:0 0 14px;padding:5px;background:#fffffff2;border:1px solid var(--line);border-radius:999px;box-shadow:0 5px 18px #1b2a1d18;backdrop-filter:blur(10px)}.section-nav a{padding:6px 11px;border-radius:999px;color:var(--muted);font-size:12px;font-weight:700;text-decoration:none;white-space:nowrap}.section-nav a.active{background:var(--ink);color:#fff}.panel[data-nav-section]{scroll-margin-top:58px}
.sync-indicator{font-size:12px;font-weight:700;white-space:nowrap}.sync-ok{color:var(--green)}.sync-expanded{padding:6px 9px;background:var(--card);border:1px solid var(--line);border-radius:9px;box-shadow:0 2px 8px #1b2a1d0d}.sync-error{color:var(--red);border-color:#e7bbb5;background:#fff7f5}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0}.card,.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:0 2px 10px #1b2a1d0a}.card{padding:13px 14px}.card>span{font-weight:650}.countline{display:flex;align-items:baseline;gap:5px;margin:5px 0 3px;color:var(--muted);font-size:12px}.countline b{font-size:20px;line-height:1;color:var(--ink)}.countline i{font-style:normal;color:#a6ada7;margin:0 2px}.card>a{font-size:12px}.panel{padding:18px;margin:16px 0;overflow:hidden}.tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}.tab{border:1px solid var(--line);background:#fff;border-radius:999px;padding:7px 12px;cursor:pointer}.tab.on{background:var(--ink);color:#fff}.company-tabs{display:none;margin:-3px 0 14px;padding-left:8px;gap:6px}.company-tabs .tab{border-color:#b9cbe3;background:#f3f7fc;color:#234f86;border-radius:8px;padding:5px 10px;font-size:12px}.company-tabs .tab.on{background:#dce9f7;border-color:#7da2cf;color:#173f70}.tablewrap{overflow:auto;max-height:620px}table{border-collapse:collapse;width:100%;min-width:880px}th,td{text-align:left;padding:9px 10px;border-bottom:1px solid #edf0ec;vertical-align:top}th{position:sticky;top:0;background:#fafbf9;color:#59645c;font-size:12px;text-transform:uppercase;letter-spacing:.04em}.pill{display:inline-block;padding:2px 7px;border-radius:999px;background:#edf2ee;font-size:12px;white-space:nowrap}.confirmed{color:var(--green);background:#e8f4ed}.discovered{color:var(--gold);background:#fff3d8}.referral{color:#744a00;background:#fff0c8}.empty{padding:24px;color:var(--muted);text-align:center}.small{font-size:12px;color:var(--muted)}.links,.workflow{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.active{color:var(--green)}.manual{color:var(--gold)}select{max-width:155px;padding:5px 7px;border:1px solid var(--line);border-radius:8px;background:white;color:var(--ink)}button.delete,button.restore{border:1px solid var(--line);border-radius:8px;padding:5px 8px;background:#fff;cursor:pointer}button.delete{color:var(--red)}button.restore{color:var(--green)}button:disabled,select:disabled{cursor:not-allowed;opacity:.5}details.panel>summary{font-size:20px;font-weight:700;cursor:pointer}.timestamp{font-weight:600;color:var(--ink)}@media(max-width:760px){.wrap{padding:16px}header{display:block}.header-actions{margin-top:10px;justify-content:flex-start}.section-nav{width:100%;overflow:auto}.cards{grid-template-columns:1fr}}
</style></head><body><div class="wrap">
<header><div><h1>Job visibility dashboard</h1><p id="updated" class="timestamp"></p><p id="sourceSnapshots" class="small"></p></div><div class="header-actions"><span id="reviewMessage" class="sync-indicator sync-expanded" aria-live="polite">● Syncing…</span><a id="repo">Repository</a></div></header>
<nav id="sectionNav" class="section-nav" aria-label="Job sections"><a href="#section-fresh" data-section="fresh" class="active">Fresh</a><a href="#section-rolling" data-section="rolling">Rolling</a><a href="#section-in-progress" data-section="in-progress">In Progress</a><a href="#section-applied" data-section="applied">Applied</a></nav>
<div class="cards" id="summary"></div>
<section id="section-fresh" data-nav-section="fresh" class="panel"><h2>Fresh — alerted in the last 24 hours</h2><p>Jobs emitted by the latest GitHub alert Issues, including newly found A/B jobs and B→A promotions. This mirrors automation activity rather than posted_date or original first_seen.</p><p id="freshBasis" class="small"></p><div class="tabs" data-target="fresh"></div><div class="tabs company-tabs" data-company-target="fresh"></div><div id="fresh"></div></section>
<section id="section-rolling" data-nav-section="rolling" class="panel"><h2>Rolling — newly found in the last 3 days</h2><p>Current A/B (or Syncareer kept) candidates, ranked Tier A first, then discovery time and score.</p><div class="tabs" data-target="rolling"></div><div class="tabs company-tabs" data-company-target="rolling"></div><div id="rolling"></div></section>
<section id="section-in-progress" data-nav-section="in-progress" class="panel"><h2>In Progress</h2><p>Jobs you are actively preparing or following up on.</p><div id="inProgress"></div></section>
<section id="section-applied" data-nav-section="applied" class="panel"><h2>Applied / Completed</h2><p>Applied jobs leave the active Fresh and Rolling lists.</p><div id="applied"></div></section>
<section class="panel"><h2>Deleted</h2><p>Deleted jobs stay recoverable with Restore while they remain in the rolling job data.</p><div id="deleted"></div></section>
<details class="panel"><summary>Referral opportunities</summary><p>Optional view. Aliases come only from <a id="referralFile">source/target_companies.json</a>.</p><div id="referrals"></div></details>
<section class="panel"><h2>Official company search links</h2><p>Quick official searches for manual checks and future adapters. “Automated” entries already have a scraper; “link only” entries are intentionally not reverse-engineered yet.</p><div id="officialSearches"></div></section>
</div><script id="payload" type="application/json">__PAYLOAD__</script><script>
const D=JSON.parse(document.getElementById('payload').textContent); document.getElementById('updated').textContent=D.updated_pt; document.getElementById('repo').href=D.repository;document.getElementById('referralFile').href=D.referral_file;
const names={official:'Big Company Official',board:'ATS / LinkedIn',syncareer:'Syncareer'};
document.getElementById('sourceSnapshots').textContent='Source snapshots: '+Object.keys(names).map(k=>`${names[k]} ${D.snapshots[k]||'unknown'}`).join(' · ');
document.getElementById('freshBasis').textContent='Fresh source: '+Object.keys(names).map(k=>`${names[k]} ${(D.fresh_basis||{})[k]==='first_seen_migration_fallback'?'temporary migration fallback':'alert history / latest Issue'}`).join(' · ');
document.getElementById('summary').innerHTML=Object.keys(names).map(k=>`<div class="card"><span>${names[k]}</span><div class="countline"><b>${D.counts_24h[k]}</b><span>last 24h</span><i>·</i><b>${D.counts_3d[k]}</b><span>in 3 days</span></div><a href="${D.report_links[k]}">open report</a></div>`).join('');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const bucketNames={lt3h:'<3h', '3to24h':'3–24h', '1to3d':'1–3d', '3to7d':'3–7d', gt7d:'>7d', unknown:'unknown'};
const statusChoices=['unreviewed','in_progress','applied_complete'];const statusLabels={unreviewed:'Unreviewed',in_progress:'In Progress',applied_complete:'Applied/Complete'};const statusCacheKey='jobReviewSharedCacheV1';const statusAliases={applied:'applied_complete',completed:'applied_complete',replied:'in_progress'};
const normalizeStatus=s=>statusAliases[s]||(statusChoices.includes(s)?s:'unreviewed');
let reviewStates={};try{reviewStates=JSON.parse(localStorage.getItem(statusCacheKey)||'{}')}catch(e){reviewStates={}}
let supabase=null,sharedLoaded=false,sharedError='';const pendingKeys=new Set();
function reviewState(key){const state=reviewStates[key];return state&&typeof state==='object'?state:null}
function statusOf(r){return normalizeStatus(reviewState(r.canonical_job_key)?.status||'unreviewed')}
function isDeleted(r){return Boolean(reviewState(r.canonical_job_key)?.deleted)}
function stateTime(state){const value=Date.parse(state?.updated_at||'');return Number.isFinite(value)?value:0}
function normalizedState(state,pending=false){return {canonical_job_key:String(state.canonical_job_key),status:normalizeStatus(state.status),deleted:Boolean(state.deleted),updated_at:state.updated_at||new Date(0).toISOString(),pending:Boolean(pending)}}
function pendingCount(){return Object.values(reviewStates).filter(state=>state?.pending).length}
function persist(){try{localStorage.setItem(statusCacheKey,JSON.stringify(reviewStates))}catch(e){}}
function renderReviewMessage(){const box=document.getElementById('reviewMessage'),pending=pendingCount(),loading=!sharedLoaded&&!sharedError;box.className='sync-indicator';if(sharedError){box.classList.add('sync-expanded','sync-error');box.textContent=`Sync error · ${sharedError}`}else if(pending){box.classList.add('sync-expanded');box.textContent=`● Syncing · ${pending} pending change${pending===1?'':'s'}`}else if(loading){box.classList.add('sync-expanded');box.textContent=Object.keys(reviewStates).length?'● Syncing · showing cached status…':'● Syncing…'}else{box.classList.add('sync-ok');box.textContent='● Synced'}}
async function pushState(snapshot){const key=snapshot.canonical_job_key;if(!supabase||pendingKeys.has(key))return;pendingKeys.add(key);renderAll();const payload={canonical_job_key:key,status:snapshot.status,deleted:snapshot.deleted,updated_at:snapshot.updated_at};const {data,error}=await supabase.from('job_review_status').upsert(payload,{onConflict:'canonical_job_key'}).select('canonical_job_key,status,deleted,updated_at').single();pendingKeys.delete(key);const current=reviewState(key);if(error){sharedError=`Could not sync review status: ${error.message}`}else if(current){const remote=normalizedState(data,false);sharedError='';if(stateTime(remote)>=stateTime(current)){reviewStates[key]=remote}else if(current.pending){setTimeout(()=>pushState(current),0)}}persist();renderReviewMessage();renderAll()}
function saveState(key,changes){const previous=reviewState(key);const next={canonical_job_key:key,status:normalizeStatus(previous?.status||'unreviewed'),deleted:Boolean(previous?.deleted),...changes,updated_at:new Date().toISOString(),pending:true};reviewStates[key]=next;persist();renderReviewMessage();renderAll();pushState(next)}
function setStatus(key,value){if(statusChoices.includes(value))saveState(key,{status:value,deleted:false})}
function deleteJob(key){saveState(key,{deleted:true})}
function restoreJob(key){saveState(key,{deleted:false})}
function activityText(r){if(r.alerted_at){const h=r.activity_age_hours;const b=h<3?'lt3h':h<24?'3to24h':'1to3d';return `Alerted ${bucketNames[b]} ago`}const d=r.freshness.discovered||{};return d.age_hours===null||d.age_hours===undefined?'Discovery unknown':`Found ${bucketNames[d.bucket]||d.bucket} ago`}
function postingText(r){const p=r.freshness.posted||{};if(!p.trusted)return r.posted_date?`Posted ${esc(r.posted_date)} · low confidence`:'Posting date unknown';return p.date_only?`Posted ${esc(r.posted_date)} · day precision`:`Posted ${bucketNames[p.bucket]||p.bucket} ago`}
function jobs(rows,deleted=false){if(!rows.length)return '<div class="empty">No qualifying jobs in this view.</div>';return `<div class="tablewrap"><table><thead><tr><th>Tier</th><th>Company / Title</th><th>Location</th><th>Alert / Posted</th><th>Sponsorship</th><th>Referral</th><th>Status</th><th>Source</th></tr></thead><tbody>${rows.map(r=>{const state=reviewState(r.canonical_job_key),disabled=pendingKeys.has(r.canonical_job_key)?'disabled':'',pending=state?.pending?'<span class="small">Pending sync</span>':'';return `<tr><td><b>${esc(r.tier)}</b>${r.score!==''?`<div class="small">${esc(r.score)}</div>`:''}</td><td><b>${esc(r.company)}</b><br><a href="${esc(r.url)}">${esc(r.title)}</a></td><td>${esc(r.location)}</td><td><span class="pill discovered">${activityText(r)}</span><div class="small">${postingText(r)}</div></td><td>${esc(r.sponsorship||'Unknown')}</td><td>${r.referral?`<span class="pill referral">${esc(r.referral)}</span>`:'-'}</td><td><div class="workflow">${deleted?`<span class="pill">Deleted</span><button class="restore" data-key="${esc(r.canonical_job_key)}" ${disabled}>Restore</button>`:`<select class="status-select" data-key="${esc(r.canonical_job_key)}" ${disabled}>${statusChoices.map(s=>`<option value="${s}" ${statusOf(r)===s?'selected':''}>${statusLabels[s]}</option>`).join('')}</select><button class="delete" data-key="${esc(r.canonical_job_key)}" ${disabled}>Delete</button>`}${pending}</div></td><td>${esc(names[r.pipeline]||r.pipeline)}</td></tr>`}).join('')}</tbody></table></div>`}
function bindStatus(box){box.querySelectorAll('.status-select').forEach(s=>s.onchange=()=>setStatus(s.dataset.key,s.value));box.querySelectorAll('.delete').forEach(b=>b.onclick=()=>deleteJob(b.dataset.key));box.querySelectorAll('.restore').forEach(b=>b.onclick=()=>restoreJob(b.dataset.key))}
function renderBox(id,rows){const box=document.getElementById(id);box.innerHTML=jobs(rows);bindStatus(box)}
function tabs(elId,rows){const filtered=rows.filter(r=>statusOf(r)==='unreviewed'&&!isDeleted(r)),tab=document.querySelector(`[data-target="${elId}"]`),companyTab=document.querySelector(`[data-company-target="${elId}"]`),box=document.getElementById(elId);let active='all',company='all';const companyNames=['all','Google','Microsoft','Apple','Amazon'];const companyRows=k=>filtered.filter(r=>r.pipeline==='official'&&(k==='all'||r.company.toLowerCase().includes(k.toLowerCase())));const draw=()=>{tab.innerHTML=['all',...Object.keys(names)].map(k=>`<button class="tab ${k===active?'on':''}" data-k="${k}">${k==='all'?'All':names[k]} (${k==='all'?filtered.length:filtered.filter(r=>r.pipeline===k).length})</button>`).join('');companyTab.style.display=active==='official'?'flex':'none';companyTab.innerHTML=active==='official'?companyNames.map(k=>`<button class="tab ${k===company?'on':''}" data-company="${k}">${k} (${companyRows(k).length})</button>`).join(''):'';let shown=active==='all'?filtered:filtered.filter(r=>r.pipeline===active);if(active==='official'&&company!=='all')shown=companyRows(company);box.innerHTML=jobs(shown);bindStatus(box);tab.querySelectorAll('button').forEach(b=>b.onclick=()=>{active=b.dataset.k;if(active!=='official')company='all';draw()});companyTab.querySelectorAll('button').forEach(b=>b.onclick=()=>{company=b.dataset.company;draw()})};draw()}
const allRows=[...(D.workflow_rows||[]),...D.fresh_24h,...D.rolling_3d,...D.referrals];const uniqueRows=()=>[...new Map(allRows.map(r=>[r.canonical_job_key,r])).values()];
function renderAll(){const rows=uniqueRows();tabs('fresh',D.fresh_24h);tabs('rolling',D.rolling_3d);renderBox('referrals',D.referrals.filter(r=>statusOf(r)==='unreviewed'&&!isDeleted(r)));renderBox('inProgress',rows.filter(r=>statusOf(r)==='in_progress'&&!isDeleted(r)));renderBox('applied',rows.filter(r=>statusOf(r)==='applied_complete'&&!isDeleted(r)));const box=document.getElementById('deleted');box.innerHTML=jobs(rows.filter(isDeleted),true);bindStatus(box)}
async function syncPending(){await Promise.all(Object.values(reviewStates).filter(state=>state?.pending).map(state=>pushState(state)))}
async function loadSharedStates(){const {data,error}=await supabase.from('job_review_status').select('canonical_job_key,status,deleted,updated_at');if(error)throw error;const merged={};(data||[]).forEach(row=>{if(row.canonical_job_key&&statusChoices.includes(row.status))merged[row.canonical_job_key]=normalizedState(row,false)});Object.values(reviewStates).filter(state=>state?.pending).forEach(local=>{const remote=merged[local.canonical_job_key];if(!remote||stateTime(local)>stateTime(remote))merged[local.canonical_job_key]=normalizedState(local,true)});reviewStates=merged;persist();sharedLoaded=true;sharedError='';renderReviewMessage();renderAll();await syncPending()}
async function refreshSharedStates(){try{await loadSharedStates()}catch(error){sharedError=`Shared review unavailable: ${error.message}`;renderReviewMessage();renderAll()}}
async function initializeSupabase(){try{const {createClient}=await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm');supabase=createClient(D.supabase.url,D.supabase.publishable_key);await refreshSharedStates()}catch(error){sharedError=`Shared review unavailable: ${error.message}`;renderReviewMessage();renderAll()}}
function initializeSectionNav(){const nav=document.getElementById('sectionNav'),links=[...nav.querySelectorAll('a[data-section]')],sections=links.map(link=>document.querySelector(`[data-nav-section="${link.dataset.section}"]`)).filter(Boolean);let queued=false;const update=()=>{queued=false;const threshold=nav.getBoundingClientRect().height+20;let current=sections[0];for(const section of sections){if(section.getBoundingClientRect().top<=threshold)current=section}const active=current?.dataset.navSection||'fresh';links.forEach(link=>{const on=link.dataset.section===active;link.classList.toggle('active',on);if(on)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current')})};window.addEventListener('scroll',()=>{if(!queued){queued=true;requestAnimationFrame(update)}},{passive:true});window.addEventListener('resize',update);links.forEach(link=>link.addEventListener('click',()=>setTimeout(update,0)));update()}
window.addEventListener('online',refreshSharedStates);initializeSectionNav();renderReviewMessage();renderAll();initializeSupabase();
document.getElementById('officialSearches').innerHTML=`<div class="tablewrap"><table><thead><tr><th>Tier</th><th>Company</th><th>Automation</th><th>Official searches</th><th>Note</th></tr></thead><tbody>${(D.official_searches||[]).map(c=>`<tr><td><b>${esc(c.priority_tier||'-')}</b></td><td><b>${esc(c.name)}</b></td><td class="${c.automation==='active'?'active':'manual'}">${c.automation==='active'?'Automated':'Link only'}</td><td><div class="links">${c.search_links.length?c.search_links.map(l=>`<a href="${esc(l.url)}">${esc(l.label||'Search')}</a>`).join(''):'-'}</div></td><td class="small">${esc(c.note)}</td></tr>`).join('')}</tbody></table></div>`;
</script></body></html>'''


def write_dashboard(payload: Dict[str, Any]) -> None:
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    DASHBOARD_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    DASHBOARD_HTML.write_text(HTML_TEMPLATE.replace("__PAYLOAD__", serialized), encoding="utf-8")
    (PUBLIC_DIR / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate GitHub Pages job dashboard")
    parser.add_argument("--json", action="store_true", help="Print compact counts")
    args = parser.parse_args()
    payload = build_payload()
    coverage_reconcile.write_coverage_outputs(payload["coverage"])
    write_dashboard(payload)
    if args.json:
        print(json.dumps({"counts_24h": payload["counts_24h"], "counts_3d": payload["counts_3d"]}, indent=2))
    else:
        print(f"Wrote {DASHBOARD_HTML} and {DASHBOARD_JSON}")


if __name__ == "__main__":
    main()
