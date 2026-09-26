#!/usr/bin/env python3
"""Generate the read-only GitHub Pages job dashboard."""

from __future__ import annotations

import argparse
import hashlib
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
import pipeline_health
from sources.company_aliases import company_risk_rank, load_alias_file, match_company_alias, match_company_entry
from sources.schema import classify_location_bucket, normalize_company_key, normalize_sponsorship, normalize_title_key
from sources.company_pending import company_key, pending_entry
from state_io import decode_json_bytes

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"
DASHBOARD_JSON = PUBLIC_DIR / "dashboard.json"
DASHBOARD_HTML = PUBLIC_DIR / "index.html"
PENDING_COMPANY_PROFILES_JSON = PUBLIC_DIR / "company_profiles_pending.json"
LOCAL_PENDING_COMPANY_PROFILES_JSON = BASE_DIR / "profile" / "company_profiles_pending.json"
REPO_URL = "https://github.com/daniel-li2021/job-board-pipeline"
PAGES_URL = "https://daniel-li2021.github.io/job-board-pipeline/"
PACIFIC = ZoneInfo("America/Los_Angeles")
REFERRAL_PATH = BASE_DIR / "config" / "target_companies.json"
COMPANY_FILTERS_PATH = BASE_DIR / "profile" / "company_filters.json"
COMPANY_PROFILES_PATH = BASE_DIR / "profile" / "company_profiles.json"
OFFICIAL_REGISTRY_PATH = BASE_DIR / "config" / "official_careers.json"
INTERNSHIP_TITLE_RE = re.compile(r"\b(intern|internship|co-op|coop)\b", re.IGNORECASE)
FRESH_INELIGIBLE_2027_TITLE_RE = re.compile(
    r"\b2027\b.*\b(?:intern(?:ship)?|co-op|coop|graduate|new grad)\b|"
    r"\b(?:intern(?:ship)?|co-op|coop|graduate|new grad)\b.*\b2027\b",
    re.IGNORECASE,
)
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
    "syncareer": BASE_DIR / "output" / "syncareer" / "jobs.json",
}
REPORT_PATHS = {
    "board": "output/board/inbox.md",
    "official": "output/official_careers/inbox.md",
    "syncareer": "output/syncareer/inbox.md",
}


def read_json(path: Path, default: Any) -> Any:
    try:
        return decode_json_bytes(path.read_bytes())
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
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
    row = {
        "pipeline": pipeline,
        "stamp": stamp,
        "emitted_at": emitted.isoformat(),
        "event_kind": "issue_body_fallback",
        "count": len(jobs),
        "jobs": jobs,
    }
    return row


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
        "fresh_activity": first_seen is not None and now - first_seen <= timedelta(hours=24),
        "rolling_activity": first_seen is not None and now - first_seen <= timedelta(hours=72),
    }


def sponsorship_label(entry: Dict[str, Any], company_profile: Optional[Dict[str, Any]] = None) -> str:
    """Prefer source/JD evidence, then fall back to company-level likelihood."""
    label = normalize_sponsorship(entry)
    if label != "Unknown":
        return label
    return {"likely": "Likely", "unlikely": "Unlikely"}.get(
        str((company_profile or {}).get("sponsor") or "").lower(), "Unknown"
    )


def pending_company_profiles(
    seen_jobs: Iterable[Dict[str, Any] | str], company_profiles: Iterable[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Accumulate distinct raw jobs for unprofiled companies across runs."""
    stored = read_json(LOCAL_PENDING_COMPANY_PROFILES_JSON, {})
    existing = stored.get("companies", []) if isinstance(stored, dict) else []
    pending: Dict[str, Dict[str, Any]] = {}
    job_keys: Dict[str, set[str]] = {}
    for raw in (existing if isinstance(existing, list) else []):
        if entry := pending_entry(raw):
            key = company_key(entry["name"])
            if key in pending:
                old = pending[key]
                for field in ("size", "maturity", "sponsor", "type"):
                    if old[field] == "unknown":
                        old[field] = entry[field]
                old["aliases"] = sorted(set(old["aliases"] + entry["aliases"] + [entry["name"]]) - {old["name"]})
                job_keys[key].update(entry["seen_job_keys"])
            else:
                pending[key] = entry
                job_keys[key] = set(entry["seen_job_keys"])
    for job in seen_jobs:
        company = job if isinstance(job, str) else job.get("company")
        if entry := pending_entry(company):
            key = company_key(entry["name"])
            if not key:
                continue
            if key not in pending:
                pending[key] = entry
                job_keys[key] = set()
            elif entry["name"] != pending[key]["name"]:
                pending[key]["aliases"] = sorted(set(pending[key]["aliases"] + [entry["name"]]))
            if isinstance(job, dict):
                identity = str(job.get("duplicate_of") or job.get("canonical_job_key") or "")
                if not identity and (job.get("official_url") or job.get("job_id") or job.get("title")):
                    identity = coverage_reconcile.canonical_job_key(job)
                if identity:
                    job_keys[key].add(hashlib.sha256(identity.encode("utf-8")).hexdigest()[:24])
    for key, entry in pending.items():
        entry["seen_job_keys"] = sorted(job_keys[key])
        entry["seen_count"] = max(1, len(job_keys[key]))
    profiled = {
        company_key(alias)
        for profile in company_profiles
        for alias in [profile["name"], *profile.get("aliases", [])]
    }
    return sorted(
        (entry for entry in pending.values() if not any(
            company_key(alias) in profiled for alias in [entry["name"], *entry["aliases"]]
        )),
        key=lambda entry: entry["name"].casefold(),
    )


def why_match_reasons(entry: Dict[str, Any]) -> List[str]:
    reasons = [str(value).strip() for value in entry.get("top_match_reasons") or [] if str(value).strip()]
    fallback = []
    family = str(entry.get("role_family") or "").lower()
    if family == "ai":
        fallback.append("AI/ML fit")
    elif family == "swe":
        fallback.append("SWE fit")
    elif family == "ambiguous":
        fallback.append("Engineering fit")
    if str(entry.get("seniority_fit") or "").lower() in {"good", "strong", "realistic"}:
        fallback.append("Experience fit")
    if not fallback and float(entry.get("match_score") or entry.get("fit_score") or 0) >= 85:
        fallback.append("Strong fit")
    if not fallback:
        fallback = [" ".join(reason.split()[:4]) for reason in reasons]
    return fallback[:2]


def why_company_signals(
    profile: Dict[str, Any], *, profiled: bool, staffing: bool, tech_service: bool, risk_rank: int = 0,
) -> List[str]:
    if not profiled:
        return ["Profile pending", "Neutral priority"]
    signals = [f"{str(profile.get('priority') or 'normal').title()} priority"]
    sponsor = str(profile.get("sponsor") or "unknown")
    if sponsor != "unknown":
        signals.append(f"Sponsor {sponsor}")
    company_type = str(profile.get("type") or "unknown")
    maturity = str(profile.get("maturity") or "unknown")
    if company_type != "unknown" or maturity != "unknown":
        signals.append(" / ".join(value.title() for value in (company_type, maturity) if value != "unknown"))
    if risk_rank:
        signals.append("Government/defense penalty" if risk_rank == 2 else "Cybersecurity penalty")
    if staffing:
        signals.append("Staffing penalty")
    elif tech_service:
        signals.append("Tech-service penalty")
    return signals[:4]


def why_evidence(entry: Dict[str, Any]) -> List[str]:
    source = str(entry.get("score_source") or "")
    evidence = []
    if source in {"llm", "cached_llm"}:
        evidence.append("LLM")
    elif source == "rule_fallback":
        evidence.append("Rule fallback")
    elif source.startswith("rule"):
        evidence.append("Rules")
    if not entry.get("description_available"):
        evidence.append("Title only")
    elif entry.get("jd_tentative"):
        evidence.append("Tentative JD")
    if entry.get("llm_retryable"):
        evidence.append("LLM retry")
    return evidence[:2]


def why_gap(entry: Dict[str, Any]) -> str:
    for gap in entry.get("main_gaps") or []:
        years = re.search(r"\b([3-9]|\d{2,})\s*\+?\s*(?:years?|yrs?)\b", str(gap), re.IGNORECASE)
        if years:
            return f"{years.group(1)}+ yrs required"
    return ""


def normalize_row(
    entry: Dict[str, Any],
    pipeline: str,
    now: datetime,
    referrals: List[Dict[str, Any]],
    coverage_by_key: Dict[str, Dict[str, Any]],
    company_profiles: Iterable[Dict[str, Any]] = (),
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
    company = str(entry.get("company") or "")
    matched_company_profile = match_company_entry(company, company_profiles)
    company_profile = matched_company_profile or {}
    risk_rank = company_risk_rank(company_profile)
    referral = entry.get("referral_name") or entry.get("target_company_match") or match_company_alias(company, referrals) or ""
    company_key = normalize_company_key(str(referral or company))
    freshness = recency(entry, now)
    staffing = bool(entry.get("staffing_firm") or "staffing" in (company_profile.get("tags") or []))
    internship = bool(INTERNSHIP_TITLE_RE.search(str(entry.get("title") or "")))
    application_priority = "low" if (
        internship
        or staffing
        or company_profile.get("priority") == "low"
        or company_profile.get("sponsor") == "unlikely"
    ) else str(company_profile.get("priority") or "normal")
    tech_service = "tech_service" in (company_profile.get("tags") or [])
    return {
        "canonical_job_key": key,
        "pipeline": pipeline,
        "source": entry.get("source") or pipeline,
        "company": company,
        "company_key": company_key,
        "display_group_key": f"{company_key}::{normalize_title_key(str(entry.get('title') or ''))}",
        "title": entry.get("title", ""),
        "location": entry.get("location", ""),
        "posted_date": entry.get("posted_date") or entry.get("posting_date") or "",
        "first_seen": entry.get("first_seen", ""),
        "date_confidence": entry.get("date_confidence", "unknown"),
        "freshness": freshness,
        "tier": entry.get("tier") or "-",
        "score": entry.get("match_score") if entry.get("match_score") is not None else entry.get("fit_score", ""),
        "sponsorship": sponsorship_label(entry, company_profile),
        "company_priority": company_profile.get("priority", "normal"),
        "company_sponsor": company_profile.get("sponsor", "unknown"),
        "company_size": company_profile.get("size", "unknown"),
        "company_type": company_profile.get("type", "unknown"),
        "company_maturity": company_profile.get("maturity", "unknown"),
        "company_tags": list(company_profile.get("tags") or []),
        "company_risk_rank": risk_rank,
        "company_profile_status": "curated" if matched_company_profile else "pending",
        "application_priority": application_priority,
        "application_reason": "internship/co-op" if internship else ("staffing" if staffing else ("tech service" if tech_service else "")),
        "tech_service": tech_service,
        "internship": internship,
        "staffing_firm": staffing,
        "referral": referral,
        "review_status": "unreviewed",
        "review_updated_at": "",
        "coverage_status": audit.get("coverage_status") or entry.get("coverage_status") or ("official_canonical" if pipeline == "official" else "not_reconciled"),
        "canonical_source": audit.get("canonical_source") or entry.get("canonical_source") or pipeline,
        "duplicate_of": audit.get("duplicate_of") or entry.get("duplicate_of") or "",
        "url": entry.get("official_url") or entry.get("source_url") or entry.get("job_url") or entry.get("url") or "",
        "filter_status": entry.get("filter_status", "kept"),
        "suppress_alert": bool(audit.get("suppress_alert") or entry.get("suppress_alert")),
        "score_source": entry.get("score_source", ""),
        "score_model": entry.get("score_model", ""),
        "scoring_version": entry.get("scoring_version", ""),
        "reasoning_effort": entry.get("reasoning_effort", ""),
        "top_match_reasons": list(entry.get("top_match_reasons") or [])[:2],
        "main_gaps": list(entry.get("main_gaps") or [])[:2],
        "main_gaps_count": int(entry.get("main_gaps_count", len(entry.get("main_gaps") or [])) or 0),
        "role_family": entry.get("role_family", ""),
        "seniority_fit": entry.get("seniority_fit", ""),
        "description_available": bool(entry.get("description_available")),
        "jd_tentative": bool(entry.get("jd_tentative")),
        "why_match": why_match_reasons(entry),
        "why_company": why_company_signals(
            company_profile, profiled=bool(matched_company_profile), staffing=staffing,
            tech_service=tech_service, risk_rank=risk_rank,
        ),
        "why_gap": why_gap(entry),
        "why_evidence": why_evidence(entry),
        "llm_retryable": bool(entry.get("llm_retryable")),
        "llm_last_error": entry.get("llm_last_error", ""),
    }
    optional = {
        "application_reason", "tech_service", "score_model", "scoring_version",
        "reasoning_effort", "top_match_reasons", "main_gaps", "llm_retryable",
        "llm_last_error",
    }
    return {key: value for key, value in row.items() if key not in optional or value not in (None, "", False, [], {})}


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


def fresh_title_eligible(row: Dict[str, Any]) -> bool:
    """Hide explicit 2027 student-cohort roles from Fresh without mutating stores."""
    return not FRESH_INELIGIBLE_2027_TITLE_RE.search(str(row.get("title") or ""))


def dedup_canonical_rows(rows: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Show an exact canonical job once across pipeline stores."""
    rank = {"official": 0, "board": 1, "syncareer": 2}
    chosen: Dict[str, Dict[str, Any]] = {}
    for row in rows:
        key = str(row.get("canonical_job_key") or "")
        previous = chosen.get(key)
        if not previous or rank.get(str(row.get("pipeline")), 99) < rank.get(str(previous.get("pipeline")), 99):
            chosen[key] = row
    return list(chosen.values())


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
        if (
            fallback_c_candidate(row)
            and row.get("freshness", {}).get(activity_flag)
            and (window != "fresh" or fresh_title_eligible(row))
        ):
            candidates.append(dict(row, dashboard_fallback=True))

    needed = max(0, target - board_ab)
    strong = _sort_rows(row for row in candidates if float(row.get("score") or 0) >= 65)
    secondary = _sort_rows(row for row in candidates if 60 <= float(row.get("score") or 0) < 65)
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
    tier_rank = {"A": 0, "1": 0, "B": 1, "2": 1, "-": 2}

    def key(row: Dict[str, Any]) -> Tuple[Any, ...]:
        freshness = row.get("freshness") or {}
        posted = freshness.get("posted") or {}
        discovered = freshness.get("discovered") or {}
        posted_age = posted.get("age_hours")
        discovered_age = discovered.get("age_hours")
        if posted.get("trusted") and posted_age is not None and posted_age < 72:
            day_rank = int(posted_age // 24)
            exact_age = posted_age
        else:
            day_rank = {
                "newly_discovered": 3, "1to3d": 3, "3to7d": 4, "gt7d": 5,
            }.get(str(freshness.get("bucket") or "unknown"), 6)
            exact_age = discovered_age if discovered_age is not None else 999999
        score = float(row.get("score") or 0)
        gaps = min(2, int(row.get("main_gaps_count", len(row.get("main_gaps") or [])) or 0))
        seniority_rank = {
            "good": 0, "strong": 0, "realistic": 0, "stretch": 1, "mismatch": 2,
        }.get(str(row.get("seniority_fit") or "").lower(), 1)
        evidence_rank = 0 if row.get("description_available") else 1
        application_low = bool(
            row.get("application_priority") == "low"
            or row.get("internship")
            or row.get("staffing_firm")
            or INTERNSHIP_TITLE_RE.search(str(row.get("title") or ""))
        )
        return (
            tier_rank.get(str(row.get("tier") or "-"), 3),
            day_rank,
            -int(score // 5),
            gaps,
            seniority_rank,
            evidence_rank,
            int(application_low),
            int(row.get("company_risk_rank") or 0),
            int(bool(row.get("tech_service"))),
            {"high": 0, "normal": 1, "low": 2}.get(str(row.get("company_priority") or "normal"), 1),
            {"likely": 0, "unknown": 1, "unlikely": 2}.get(str(row.get("company_sponsor") or "unknown"), 1),
            0 if row.get("company_type") == "tech" else 1,
            0 if row.get("company_maturity") in {"growth", "established"} else 1,
            {"20k+": 0, "5k-20k": 1, "1k-5k": 2, "200-1k": 3, "50-200": 4}.get(str(row.get("company_size") or ""), 5),
            -score,
            0 if row.get("referral") else 1,
            exact_age,
            str(row.get("company") or "").lower(),
        )

    return sorted(
        rows,
        key=key,
    )


def alert_fresh_rows(
    all_rows: List[Dict[str, Any]], now: datetime,
    hard_excludes: Optional[List[Dict[str, Any]]] = None,
) -> Tuple[List[Dict[str, Any]], Dict[str, str]]:
    """Include alert activity and every newly discovered qualifying job."""
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
        basis[pipeline] = "alerts_and_new_discoveries"

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
                if not visible_candidate(row, hard_excludes) or not fresh_title_eligible(row):
                    continue
                row["alerted_at"] = emitted_at.isoformat()
                row["alert_stamp"] = event.get("stamp", "")
                row["alert_kind"] = event.get("event_kind", "")
                row["activity_age_hours"] = activity_age
                stable = str(row.get("canonical_job_key") or url_key)
                previous = chosen.get(stable)
                if previous is None or float(previous.get("activity_age_hours") or 999999) > activity_age:
                    chosen[stable] = row
    for row in all_rows:
        if (
            row["freshness"]["fresh_activity"]
            and visible_candidate(row, hard_excludes)
            and fresh_title_eligible(row)
        ):
            stable = str(row.get("canonical_job_key") or coverage_reconcile.normalize_url(str(row.get("url") or "")))
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
    company_profiles = load_alias_file(COMPANY_PROFILES_PATH)
    coverage = coverage_reconcile.build_coverage_payload(now)
    health, health_history = pipeline_health.build(BASE_DIR, now)
    coverage_by_key = {record.get("canonical_job_key", ""): record for record in coverage.get("records", [])}
    snapshots: Dict[str, str] = {}
    all_rows: List[Dict[str, Any]] = []
    seen_jobs: List[Dict[str, Any]] = []
    for pipeline, path in STORE_PATHS.items():
        store, entries = _load_entries(path)
        snapshots[pipeline] = str(store.get("updated_at") or store.get("scraped_at") or "")
        for entry in entries:
            seen_jobs.append(entry)
            practical = config_company_match(
                str(entry.get("company") or ""), str(entry.get("title") or ""), practical_skips
            )
            if practical and not entry.get("clearance_risk_company"):
                continue
            all_rows.append(normalize_row(entry, pipeline, now, referrals, coverage_by_key, company_profiles))

    # History is recovery-only: expired or newly filtered jobs must not re-enter discovery.
    history_details: Dict[str, List[Any]] = {}
    for row in all_rows:
        key = str(row.get("canonical_job_key") or "")
        if key and (row.get("tier") not in (None, "", "-") or row.get("score") not in (None, "")):
            history_details[key] = [
                row.get("pipeline", ""), row.get("company", ""), row.get("title", ""),
                row.get("location", ""), row.get("url", ""), row.get("tier") or "-", row.get("score", ""),
            ]
    for pipeline, path in ALERT_HISTORY_PATHS.items():
        for event in read_json(path, {}).get("events", []):
            for entry in event.get("jobs", []):
                if isinstance(entry, dict):
                    key = str(entry.get("canonical_job_key") or coverage_reconcile.canonical_job_key(entry))
                    tier = entry.get("tier") or "-"
                    score = entry.get("match_score") if entry.get("match_score") is not None else entry.get("fit_score", "")
                    previous = history_details.get(key, ["", "", "", "", "", "-", ""])
                    values = [
                        pipeline, entry.get("company") or "", entry.get("title") or "",
                        entry.get("location") or "",
                        entry.get("official_url") or entry.get("source_url") or entry.get("job_url") or entry.get("url") or "",
                    ]
                    history_details[key] = [value or previous[index] for index, value in enumerate(values)] + [
                        tier if tier != "-" else previous[5], score if score not in (None, "") else previous[6],
                    ]

    eligible_rows = [
        row for row in all_rows
        if not match_company_alias(str(row.get("company") or ""), hard_excludes)
    ]
    candidates = dedup_canonical_rows(
        row for row in eligible_rows if visible_candidate(row, hard_excludes)
    )
    company_profiles_pending = pending_company_profiles(seen_jobs, company_profiles)
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

    today = now.astimezone(PACIFIC).date()
    today_runs = [
        run for run in health_history
        if (parse_dt(run.get("run_at")) or datetime.min.replace(tzinfo=timezone.utc)).astimezone(PACIFIC).date() == today
    ]
    llm_observability = {
        "today_estimated_usd": round(sum(float(run.get("estimated_usd", 0) or 0) for run in today_runs), 6),
        "today_runs": len(today_runs),
        "recent_runs": health_history[:20],
        "details_url": f"{PAGES_URL}health-history.json",
    }
    matching_summary = {
        "tiers": dict(Counter(str(row.get("tier") or "-") for row in candidates)),
        "score_sources": dict(Counter(str(row.get("score_source") or "unknown") for row in candidates)),
        "retryable": max(
            sum(bool(row.get("llm_retryable")) for row in all_rows),
            int(read_json(BASE_DIR / "output" / "board" / "matching_retry.json.gz", {}).get("count", 0) or 0),
        ),
        "explainable": sum(bool(row.get("why_match")) for row in candidates),
        "company_profiles_pending": len(company_profiles_pending),
        "total_visible": len(candidates),
    }

    return {
        "generated_at": now.isoformat(),
        "updated_pt": now.astimezone(PACIFIC).strftime("%b %-d, %Y · %-I:%M %p"),
        "pages_url": PAGES_URL,
        "repository": REPO_URL,
        "snapshots": snapshots,
        "report_links": {key: f"{REPO_URL}/blob/main/{path}" for key, path in REPORT_PATHS.items()},
        "referral_file": f"{REPO_URL}/blob/main/config/target_companies.json",
        "coverage_report": f"{PAGES_URL}coverage.md",
        "coverage_summary": {
            "counts": coverage.get("counts", {}),
            "registry_counts": coverage.get("registry_counts", {}),
            "coverage_ratio": coverage.get("coverage_ratio"),
            "observed_coverage_ratio": coverage.get("observed_coverage_ratio"),
            "exact_match_methods": coverage.get("exact_match_methods", {}),
            "generated_at": coverage.get("generated_at", ""),
        },
        "supabase": {"url": SUPABASE_URL, "publishable_key": SUPABASE_PUBLISHABLE_KEY},
        "counts_24h": counts(fresh),
        "counts_3d": counts(rolling),
        "fresh_24h": fresh,
        "fresh_basis": fresh_basis,
        "rolling_3d": rolling,
        "referrals": referral_rows[:500],
        "older_review": older[:500],
        # Shared status changes need a complete row pool so a job can move
        # between sections immediately without regenerating static job data.
        "workflow_rows": _sort_rows(candidates),
        "history_details": history_details,
        "coverage": coverage,
        "health": health,
        "health_history": health_history,
        "llm_observability": llm_observability,
        "matching_summary": matching_summary,
        "company_profiles_pending": company_profiles_pending,
        "health_report": f"{PAGES_URL}health.html",
        "official_searches": official_search_catalog(),
    }


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Daniel's Job Board</title>
<style>
:root{--bg:#f4f6f1;--card:#fff;--ink:#152018;--muted:#687269;--line:#dce2da;--green:#176b45;--gold:#ad6c00;--blue:#275fa8;--red:#9d3b31}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.wrap{max-width:1440px;margin:auto;padding:28px}header{display:flex;justify-content:space-between;gap:20px;align-items:flex-end;margin-bottom:14px}.header-actions{display:flex;gap:12px;align-items:center;flex-wrap:wrap;justify-content:flex-end}h1{font-size:30px;letter-spacing:-.03em;margin:0}h2{font-size:20px;margin:0 0 12px}p{margin:5px 0;color:var(--muted)}a{color:var(--blue)}button,select,input{font:inherit}
.main-tabs{display:flex;gap:4px;width:max-content;max-width:100%;margin:0 0 12px;padding:5px;background:#f3f5f1;border:1px solid var(--line);border-radius:999px;overflow:auto}.main-tab{border:0;background:transparent;border-radius:999px;padding:7px 12px;color:var(--muted);font-size:12px;font-weight:700;cursor:pointer;white-space:nowrap}.main-tab.on{background:var(--ink);color:#fff}.main-tab:focus-visible{outline:2px solid var(--blue);outline-offset:2px}.main-view[hidden]{display:none}.main-view>h2{margin-top:0}
.job-search{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:0 0 18px}.job-search>input[type=search]{width:min(420px,100%);min-width:240px;padding:9px 11px;border:1px solid var(--line);border-radius:10px;background:#fff;color:var(--ink)}.job-search>input:focus,.header-filter input:focus,.filter-menu summary:focus{outline:2px solid #b9cbe3;outline-offset:1px}.job-search button{border:1px solid var(--line);border-radius:8px;padding:7px 10px;background:#fff;color:var(--ink);cursor:pointer}.export-actions{display:flex;gap:8px;margin-left:auto}
.tier-header{width:76px;min-width:76px}.sponsorship-header{width:148px;min-width:148px}.header-filter{margin-top:5px;text-transform:none;letter-spacing:0}.min-score-filter{width:54px;height:27px;min-width:0;padding:3px 6px;border:1px solid var(--line);border-radius:7px;background:#fff;color:var(--ink);font-size:12px;font-weight:700;-moz-appearance:textfield}.min-score-filter::-webkit-outer-spin-button,.min-score-filter::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}.filter-menu{position:relative;text-transform:none;letter-spacing:0}.filter-menu summary{height:27px;display:flex;align-items:center;gap:5px;padding:3px 7px;border:1px solid var(--line);border-radius:7px;background:#fff;color:var(--ink);font-size:11px;font-weight:700;cursor:pointer;list-style:none;white-space:nowrap}.filter-menu summary::-webkit-details-marker{display:none}.filter-menu summary::after{content:'▾';color:var(--muted);font-size:9px}.filter-menu[open] summary::after{content:'▴'}.filter-options{position:absolute;z-index:6;top:31px;left:0;min-width:148px;padding:6px;background:#fff;border:1px solid var(--line);border-radius:9px;box-shadow:0 8px 24px #1520181c}.filter-options label{display:flex;align-items:center;gap:7px;padding:6px;border-radius:6px;color:var(--ink);font-size:12px;font-weight:500;white-space:nowrap;text-transform:none;letter-spacing:0}.filter-options label:hover{background:#f3f5f1}
.sync-indicator,.health-indicator{font-size:12px;font-weight:700;white-space:nowrap}.sync-ok,.health-healthy{color:var(--green)}.sync-expanded,.health-indicator{padding:6px 9px;background:var(--card);border:1px solid var(--line);border-radius:9px;box-shadow:0 2px 8px #1b2a1d0d}.sync-error,.health-problem{color:var(--red);border-color:#e7bbb5;background:#fff7f5}.health-warning,.health-stale{color:var(--gold)}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0}.card,.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:0 2px 10px #1b2a1d0a}.card{padding:13px 14px}.card>span{font-weight:650}.countline{display:flex;align-items:baseline;gap:5px;margin:5px 0 3px;color:var(--muted);font-size:12px}.countline b{font-size:20px;line-height:1;color:var(--ink)}.countline i{font-style:normal;color:#a6ada7;margin:0 2px}.card>a{font-size:12px}.panel{padding:18px;margin:16px 0;overflow:hidden}.tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}.tab{border:1px solid var(--line);background:#fff;border-radius:999px;padding:7px 12px;cursor:pointer}.tab.on{background:var(--ink);color:#fff}.company-tabs{display:none;margin:-3px 0 14px;padding-left:8px;gap:6px}.company-tabs .tab{border-color:#b9cbe3;background:#f3f7fc;color:#234f86;border-radius:8px;padding:5px 10px;font-size:12px}.company-tabs .tab.on{background:#dce9f7;border-color:#7da2cf;color:#173f70}.tablewrap{overflow:auto;max-height:620px}table{border-collapse:collapse;width:100%;min-width:880px}th,td{text-align:left;padding:9px 10px;border-bottom:1px solid #edf0ec;vertical-align:top}th{position:sticky;z-index:2;top:0;background:#fafbf9;color:#59645c;font-size:12px;text-transform:uppercase;letter-spacing:.04em}tbody tr:hover{background:#fafcf9}.pill{display:inline-block;padding:2px 7px;border-radius:999px;background:#edf2ee;font-size:12px;white-space:nowrap}.confirmed{color:var(--green);background:#e8f4ed}.discovered{color:var(--gold);background:#fff3d8}.referral{color:#744a00;background:#fff0c8}.application-badges{display:inline-flex;gap:4px;margin-left:6px;vertical-align:middle}.empty{padding:24px;color:var(--muted);text-align:center}.small{font-size:12px;color:var(--muted)}.links,.workflow{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.active{color:var(--green)}.manual{color:var(--gold)}select{max-width:155px;padding:5px 7px;border:1px solid var(--line);border-radius:8px;background:white;color:var(--ink)}button.delete,button.restore{border:1px solid var(--line);border-radius:8px;padding:5px 8px;background:#fff;cursor:pointer}button.delete{color:var(--red)}button.restore{color:var(--green)}button:disabled,select:disabled{cursor:not-allowed;opacity:.5}details.panel>summary{font-size:20px;font-weight:700;cursor:pointer}.timestamp{font-weight:600;color:var(--ink)}@media(max-width:760px){.wrap{padding:16px}header{display:block}.header-actions{margin-top:10px;justify-content:flex-start}.main-tabs{width:100%}.job-search>input[type=search]{width:100%;min-width:0}.export-actions{margin-left:0}.cards{grid-template-columns:1fr}}
button.hide-company,button.show-company{border:1px solid var(--line);border-radius:8px;padding:5px 8px;background:#fff;cursor:pointer}button.hide-company{color:var(--red)}button.show-company{color:var(--green)}
</style></head><body><div class="wrap">
<header><div><h1>Job visibility dashboard</h1><p id="updated" class="timestamp"></p><p id="sourceSnapshots" class="small"></p></div><div class="header-actions"><a id="healthIndicator" class="health-indicator" target="_blank" rel="noopener noreferrer">Health</a><span id="reviewMessage" class="sync-indicator sync-expanded" aria-live="polite">● Syncing…</span><a target="_blank" rel="noopener noreferrer" id="repo">Repository</a></div></header>
<div class="cards" id="summary"></div>
<section class="panel"><div class="cards"><div class="card"><span>LLM Matching Today</span><div class="countline"><b id="llmToday"></b></div><p id="llmTodayDetail"></p><a href="#llmRunDetails">Recent runs and batches</a></div><div class="card"><span>Coverage</span><p id="coverageSummary"></p><a id="coverageReport" target="_blank" rel="noopener noreferrer">Open full coverage report</a></div><div class="card"><span>Matching</span><p id="matchingSummary"></p><a id="matchingDetails" target="_blank" rel="noopener noreferrer">Open run details</a></div></div><details id="llmRunDetails"><summary>Recent matching runs and batch details</summary><div id="llmRuns"></div></details></section>
<section class="panel main-jobs"><div id="mainViewTabs" class="main-tabs" role="tablist" aria-label="Job views"><button id="main-tab-fresh" class="main-tab on" type="button" role="tab" aria-selected="true" aria-controls="main-view-fresh" data-main-view="fresh">Fresh</button><button id="main-tab-rolling" class="main-tab" type="button" role="tab" aria-selected="false" aria-controls="main-view-rolling" data-main-view="rolling">Rolling</button><button id="main-tab-in-progress" class="main-tab" type="button" role="tab" aria-selected="false" aria-controls="main-view-in-progress" data-main-view="in-progress">In Progress</button><button id="main-tab-applied" class="main-tab" type="button" role="tab" aria-selected="false" aria-controls="main-view-applied" data-main-view="applied">Applied</button></div>
<div class="job-search"><input id="jobSearch" type="search" autocomplete="off" placeholder="Search title or company" aria-label="Search jobs by title or company"><button id="clearJobSearch" type="button" hidden>Clear</button><span id="jobSearchCount" class="small" aria-live="polite"></span><div class="export-actions"><button id="copyMarkdown" type="button">Copy MD</button><button id="downloadMarkdown" type="button">Download MD</button></div></div>
<div id="main-view-fresh" class="main-view" role="tabpanel" aria-labelledby="main-tab-fresh" data-main-panel="fresh"><h2>Fresh — alerts and discoveries in the last 24 hours</h2><p>Jobs from recent alerts, including B→A promotions, plus all qualifying Official jobs first discovered in the last 24 hours.</p><p id="freshBasis" class="small"></p><div class="tabs" data-target="fresh"></div><div class="tabs company-tabs" data-company-target="fresh"></div><div id="fresh"></div></div>
<div id="main-view-rolling" class="main-view" role="tabpanel" aria-labelledby="main-tab-rolling" data-main-panel="rolling" hidden><h2>Rolling — newly found in the last 3 days</h2><p>Current A/B (or Syncareer kept) candidates, ranked by tier, posting day, fit, and application quality.</p><div class="tabs" data-target="rolling"></div><div class="tabs company-tabs" data-company-target="rolling"></div><div id="rolling"></div></div>
<div id="main-view-in-progress" class="main-view" role="tabpanel" aria-labelledby="main-tab-in-progress" data-main-panel="in-progress" hidden><h2>In Progress</h2><p>Jobs you are actively preparing or following up on.</p><div id="inProgress"></div></div>
<div id="main-view-applied" class="main-view" role="tabpanel" aria-labelledby="main-tab-applied" data-main-panel="applied" hidden><h2>Applied / Completed</h2><p>Applied jobs leave the active Fresh and Rolling lists.</p><div id="applied"></div></div></section>
<details class="panel"><summary>Hidden companies <span id="hiddenCompanyCount"></span></summary><p>Hidden companies stay out of discovery views. Show one again at any time.</p><div id="hiddenCompanies"></div></details>
<section class="panel"><h2>Deleted</h2><p>Deleted jobs stay recoverable with Restore while they remain in the rolling job data.</p><div id="deleted"></div></section>
<details class="panel"><summary>Referral opportunities</summary><p>Optional view. Aliases come only from <a target="_blank" rel="noopener noreferrer" id="referralFile">config/target_companies.json</a>.</p><div id="referrals"></div></details>
<section class="panel"><h2>Official company search links</h2><p>Quick official searches for manual checks and future adapters. “Automated” entries already have a scraper; “link only” entries are intentionally not reverse-engineered yet.</p><div id="officialSearches"></div></section>
</div><script id="payload" type="application/json">__PAYLOAD__</script><script>
const D=JSON.parse(document.getElementById('payload').textContent); document.getElementById('updated').textContent=D.updated_pt; document.getElementById('repo').href=D.repository;document.getElementById('referralFile').href=D.referral_file;
const names={official:'Big Company Official',board:'ATS / LinkedIn',syncareer:'Syncareer'};
const health=document.getElementById('healthIndicator'),overall=D.health?.overall||'Warning';health.href=D.health_report;health.textContent=`Health: ${overall}`;health.classList.add(`health-${overall.toLowerCase()}`);
const snapshotTime=v=>{const d=new Date(v);return Number.isNaN(d.getTime())?'unknown':new Intl.DateTimeFormat('en-US',{timeZone:'America/Los_Angeles',month:'short',day:'numeric',hour:'numeric',minute:'2-digit',hour12:true}).format(d).replace(',','')+' PT'};
document.getElementById('sourceSnapshots').textContent='Source snapshots: '+Object.keys(names).map(k=>`${names[k]} · ${snapshotTime(D.snapshots[k])}`).join('   ');
document.getElementById('freshBasis').textContent='Fresh source: '+Object.keys(names).map(k=>`${names[k]} ${(D.fresh_basis||{})[k]==='alerts_and_new_discoveries'?'alerts + all new discoveries':(D.fresh_basis||{})[k]==='first_seen_migration_fallback'?'temporary migration fallback':'alert history / latest Issue'}`).join(' · ');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const compactJson=value=>esc(JSON.stringify(value||{},null,2));
function renderObservability(){const o=D.llm_observability||{},runs=o.recent_runs||[];document.getElementById('llmToday').textContent=`$${Number(o.today_estimated_usd||0).toFixed(4)}`;document.getElementById('llmTodayDetail').textContent=`${o.today_runs||0} runs today · production and retry attempts combined`;document.getElementById('llmRuns').innerHTML=runs.length?`<div class="tablewrap"><table><thead><tr><th>Run</th><th>Model</th><th>Jobs / cache / fallback</th><th>Requests / tokens</th><th>Cost / latency</th><th>Health / detail</th></tr></thead><tbody>${runs.map(r=>{const latency=r.latency_measured?`${r.latency_seconds}s`:'Unknown',json=r.json_reliability_measured&&r.json_reliability!=null?Math.round(r.json_reliability*100)+'%':'—',batches=r.batch_outcomes_measured?`${r.batches_succeeded||0}/${r.batches_total||0} succeeded`:'—';return `<tr><td>${esc(names[r.pipeline]||r.pipeline)}<div class="small">${esc(snapshotTime(r.run_at))}</div></td><td>${esc(r.model||'-')}<div class="small">${esc(r.reasoning_effort||'-')} · ${esc(r.scoring_version||'-')}</div></td><td>${esc(r.jobs_scored||0)} / ${esc(r.cache_reused||0)} / ${esc(r.fallback_count||0)}</td><td>${esc(r.requests||0)} · in ${esc(r.input_tokens||0)} / out ${esc(r.output_tokens||0)} / reasoning ${esc(r.reasoning_tokens||0)}<div class="small">RPM ${esc(r.effective_rpm??'—')} · TPM ${esc(r.effective_tpm??'—')} · JSON ${json} · batches ${batches}</div></td><td>$${Number(r.estimated_usd||0).toFixed(4)} · ${esc(latency)}</td><td><span class="pill">${esc(r.health||'unknown')}</span><details><summary>data</summary><pre>${compactJson({funnel:r.funnel,output:r.output,batches:r.batches})}</pre></details></td></tr>`}).join('')}</tbody></table></div>`:'<div class="empty">No persistent run history yet.</div>';const coverage=D.coverage_summary||{},matching=D.matching_summary||{};const ratio=coverage.coverage_ratio==null?'—':Math.round(coverage.coverage_ratio*100)+'%',presence=coverage.observed_coverage_ratio==null?'—':Math.round(coverage.observed_coverage_ratio*100)+'%';document.getElementById('coverageSummary').textContent=`Exact ${ratio} · official presence ${presence} · ${Object.entries(coverage.counts||{}).map(([k,v])=>`${k}: ${v}`).join(' · ')||'No coverage summary'}`;document.getElementById('coverageReport').href=D.coverage_report;document.getElementById('matchingSummary').textContent=`Visible ${matching.total_visible||0} · explainable ${matching.explainable||0} · retryable ${matching.retryable||0} · company profiles pending ${matching.company_profiles_pending||0} · tiers ${Object.entries(matching.tiers||{}).map(([k,v])=>`${k}:${v}`).join(' ')}`;document.getElementById('matchingDetails').href=o.details_url||D.health_report}
renderObservability();
const bucketNames={lt3h:'<3h', '3to24h':'3–24h', '1to3d':'1–3d', '3to7d':'3–7d', gt7d:'>7d', unknown:'unknown'};
const statusChoices=['unreviewed','in_progress','applied_complete'];const statusLabels={unreviewed:'Unreviewed',in_progress:'In Progress',applied_complete:'Applied/Complete'};const statusCacheKey='jobReviewSharedCacheV1';const statusAliases={applied:'applied_complete',completed:'applied_complete',replied:'in_progress'};
const companyStatePrefix='company::';
const normalizeStatus=s=>statusAliases[s]||(statusChoices.includes(s)?s:'unreviewed');
let reviewStates={};try{reviewStates=JSON.parse(localStorage.getItem(statusCacheKey)||'{}')}catch(e){reviewStates={}}
let supabase=null,sharedLoaded=false,sharedError='';const pendingKeys=new Set();
function reviewState(key){const state=reviewStates[key];return state&&typeof state==='object'?state:null}
function statusOf(r){return normalizeStatus(reviewState(r.canonical_job_key)?.status||'unreviewed')}
function isDeleted(r){return Boolean(reviewState(r.canonical_job_key)?.deleted)}
const companyStateKey=r=>r?.company_key?companyStatePrefix+r.company_key:'';
const isPreferenceKey=key=>String(key||'').startsWith(companyStatePrefix);
function isCompanyHidden(r){const key=companyStateKey(r);return Boolean(key&&reviewState(key)?.deleted)}
function stateTime(state){const value=Date.parse(state?.updated_at||'');return Number.isFinite(value)?value:0}
function normalizedState(state,pending=false){return {canonical_job_key:String(state.canonical_job_key),status:normalizeStatus(state.status),deleted:Boolean(state.deleted),updated_at:state.updated_at||new Date(0).toISOString(),pending:Boolean(pending)}}
function pendingCount(){return Object.values(reviewStates).filter(state=>state?.pending).length}
function persist(){try{localStorage.setItem(statusCacheKey,JSON.stringify(reviewStates))}catch(e){}}
function renderReviewMessage(){const box=document.getElementById('reviewMessage'),pending=pendingCount(),loading=!sharedLoaded&&!sharedError;box.className='sync-indicator';if(sharedError){box.classList.add('sync-expanded','sync-error');box.textContent=`Sync error · ${sharedError}`}else if(pending){box.classList.add('sync-expanded');box.textContent=`● Syncing · ${pending} pending change${pending===1?'':'s'}`}else if(loading){box.classList.add('sync-expanded');box.textContent=Object.keys(reviewStates).length?'● Syncing · showing cached status…':'● Syncing…'}else{box.classList.add('sync-ok');box.textContent='● Synced'}}
async function pushState(snapshot){
  const key=snapshot.canonical_job_key;if(!supabase||pendingKeys.has(key))return;
  pendingKeys.add(key);renderAll();
  try {
    const payload={canonical_job_key:key,status:snapshot.status,deleted:snapshot.deleted,updated_at:snapshot.updated_at};
    const {data,error}=await supabase.from('job_review_status').upsert(payload,{onConflict:'canonical_job_key'}).select('canonical_job_key,status,deleted,updated_at').single();
    if(error)throw error;
    const current=reviewState(key),remote=normalizedState(data,false);sharedError='';
    if(current&&stateTime(remote)>=stateTime(current))reviewStates[key]=remote;
    else if(current?.pending)setTimeout(()=>pushState(reviewState(key)),0);
  } catch(error) {sharedError=`Could not sync review status: ${error.message}`}
  finally {pendingKeys.delete(key);persist();renderReviewMessage();renderAll()}
}
function saveStates(keys,changes){const updated_at=new Date(Math.max(Date.now(),...keys.map(key=>stateTime(reviewState(key))+1))).toISOString();keys.forEach(key=>{const previous=reviewState(key);reviewStates[key]={canonical_job_key:key,status:normalizeStatus(previous?.status||'unreviewed'),deleted:Boolean(previous?.deleted),...changes,updated_at,pending:true}});persist();renderReviewMessage();renderAll();keys.forEach(key=>pushState(reviewStates[key]))}
function saveState(key,changes){saveStates([key],changes)}
function setStatus(keys,value){if(statusChoices.includes(value))saveStates(keys,{status:value,deleted:false})}
function deleteJob(keys){saveStates(keys,{deleted:true})}
function restoreJob(keys){saveStates(keys,{deleted:false})}
function setCompanyHidden(key,hidden){if(!key)return;const password=window.prompt(`Enter password to ${hidden?'hide':'show again'} this company:`);if(password!=='300701'){if(password!==null)window.alert('Incorrect password.');return}saveState(companyStatePrefix+key,{deleted:hidden})}
function activityText(r){if(r.alerted_at){const h=r.activity_age_hours;const b=h<3?'lt3h':h<24?'3to24h':'1to3d';return `Alerted ${bucketNames[b]} ago`}const d=r.freshness.discovered||{};return d.age_hours===null||d.age_hours===undefined?'Discovery unknown':`Found ${bucketNames[d.bucket]||d.bucket} ago`}
function postingText(r){const p=r.freshness.posted||{};if(!p.trusted)return r.posted_date?`Posted ${esc(r.posted_date)} · low confidence`:'Posting date unknown';return p.date_only?`Posted ${esc(r.posted_date)} · day precision`:`Posted ${bucketNames[p.bucket]||p.bucket} ago`}
const displayGroupKey=r=>r.display_group_key||`${r.company||''}|${r.title||''}`.toLowerCase().replace(/[^a-z0-9|]+/g,' ');
let applicationHistoryBadges=()=>'';
function displayRows(rows){const groups=new Map();rows.forEach(r=>{const key=displayGroupKey(r);if(!groups.has(key))groups.set(key,[]);groups.get(key).push(r)});return [...groups.values()].flatMap(group=>{const variants=[...new Map(group.map(r=>[r.canonical_job_key,r])).values()],locations=new Set(variants.map(r=>String(r.location||'').trim().toLowerCase()).filter(Boolean));return locations.size>1?[{...variants[0],_variants:variants}]:variants})}
const actionKeys=element=>{try{return JSON.parse(element.dataset.keys||'[]')}catch(error){return element.dataset.key?[element.dataset.key]:[]}};
function whyMatch(r){const reasons=(r.why_match||[]).map(esc).join(' · ')||'Unknown',company=(r.why_company||[]).map(esc).join(' · ')||'Neutral priority',gap=esc(r.why_gap||'None'),evidence=(r.why_evidence||[]).map(esc).join(' · ');return `<details class="small"><summary>Why</summary><div><b>Match:</b> ${reasons}</div><div><b>Company:</b> ${company}</div><div><b>Gap:</b> ${gap}${evidence?` · <b>Evidence:</b> ${evidence}`:''}</div></details>`}
function jobRows(rows,deleted=false){return rows.length?displayRows(rows).map(r=>{const variants=r._variants||[r],keys=variants.map(v=>v.canonical_job_key),keyData=esc(JSON.stringify(keys)),states=keys.map(reviewState),statuses=variants.map(statusOf),status=statuses.every(value=>value===statuses[0])?statuses[0]:'mixed',disabled=keys.some(key=>pendingKeys.has(key))?'disabled':'',companyDisabled=pendingKeys.has(companyStateKey(r))?'disabled':'',pending=states.some(state=>state?.pending)?'<span class="small">Pending sync</span>':'',companyAction=r.company_key?` <button class="${isCompanyHidden(r)?'show-company':'hide-company'}" data-company-key="${esc(r.company_key)}" ${companyDisabled}>${isCompanyHidden(r)?'Show again':'Hide company'}</button>`:'',location=variants.length>1?`<details><summary>${variants.length} locations</summary>${variants.map(v=>`<div><a target="_blank" rel="noopener noreferrer" href="${esc(v.url)}">${esc(v.location||'Open location')}</a></div>`).join('')}</details>`:esc(r.location),sources=[...new Set(variants.map(v=>names[v.pipeline]||v.pipeline))].join(' / ');return `<tr><td><b>${esc(r.tier)}</b>${r.score!==''?`<div class="small">${esc(r.score)}</div>`:''}${whyMatch(r)}</td><td><b>${esc(r.company)}</b>${applicationHistoryBadges(r)}${companyAction}<br><a target="_blank" rel="noopener noreferrer" href="${esc(r.url)}">${esc(r.title)}</a>${variants.length>1?`<div class="small">Collapsed same role · individual location links preserved</div>`:''}</td><td>${location}</td><td><span class="pill discovered">${activityText(r)}</span><div class="small">${postingText(r)}</div></td><td>${esc(r.sponsorship||'Unknown')}</td><td>${r.referral?`<span class="pill referral">${esc(r.referral)}</span>`:'-'}</td><td><div class="workflow">${deleted?`<span class="pill">Deleted</span><button class="restore" data-keys="${keyData}" ${disabled}>Restore</button>`:`<select class="status-select" data-keys="${keyData}" ${disabled}>${status==='mixed'?'<option value="mixed" selected disabled>Mixed</option>':''}${statusChoices.map(s=>`<option value="${s}" ${status===s?'selected':''}>${statusLabels[s]}</option>`).join('')}</select><button class="delete" data-keys="${keyData}" ${disabled}>Delete</button>`}${pending}</div></td><td>${esc(sources)}</td></tr>`}).join(''):'<tr><td colspan="8"><div class="empty">No qualifying jobs in this view.</div></td></tr>'}
function sponsorshipSummary(){const selected=sponsorshipChoices.filter(value=>sponsorshipFilters.has(value));return selected.length===sponsorshipChoices.length?'All':selected.length===1?selected[0]:selected.length+' selected'}
function discoveryHeader(){const option=value=>`<label><input type="checkbox" value="${value}" ${sponsorshipFilters.has(value)?'checked':''}> ${value}</label>`;return `<th class="tier-header">Tier<div class="header-filter"><input class="min-score-filter" type="number" min="0" max="100" step="1" inputmode="numeric" value="${esc(minScore)}" placeholder="Min" aria-label="Minimum score"></div></th><th>Company / Title</th><th>Location</th><th>Alert / Posted</th><th class="sponsorship-header">Sponsorship<details class="filter-menu sponsorship-filter"><summary>${sponsorshipSummary()}</summary><div class="filter-options" role="group" aria-label="Sponsorship options">${sponsorshipChoices.map(option).join('')}</div></details></th>`}
function jobs(rows,deleted=false,discovery=false){if(!rows.length&&!discovery)return '<div class="empty">No qualifying jobs in this view.</div>';const header=discovery?discoveryHeader():'<th>Tier</th><th>Company / Title</th><th>Location</th><th>Alert / Posted</th><th>Sponsorship</th>';return `<div class="tablewrap"><table><thead><tr>${header}<th>Referral</th><th>Status</th><th>Source</th></tr></thead><tbody>${jobRows(rows,deleted)}</tbody></table></div>`}
function bindStatus(box){box.querySelectorAll('.status-select').forEach(s=>s.onchange=()=>setStatus(actionKeys(s),s.value));box.querySelectorAll('.delete').forEach(b=>b.onclick=()=>deleteJob(actionKeys(b)));box.querySelectorAll('.restore').forEach(b=>b.onclick=()=>restoreJob(actionKeys(b)));box.querySelectorAll('.hide-company').forEach(b=>b.onclick=()=>setCompanyHidden(b.dataset.companyKey,true));box.querySelectorAll('.show-company').forEach(b=>b.onclick=()=>setCompanyHidden(b.dataset.companyKey,false))}
const exportViewRows={fresh:[],rolling:[]},exportViewLabels={'in-progress':'In Progress',applied:'Applied'};
function renderBox(id,rows){if(id==='inProgress')exportViewRows['in-progress']=displayRows(rows);if(id==='applied')exportViewRows.applied=displayRows(rows);const box=document.getElementById(id);box.innerHTML=jobs(rows);bindStatus(box)}
const normalRows=rows=>rows.filter(r=>statusOf(r)==='unreviewed'&&!isDeleted(r)&&!isCompanyHidden(r));
let searchQuery='';
const searchTerms=()=>searchQuery.trim().toLowerCase().split(/\s+/).filter(Boolean);
function matchesSearch(r){const terms=searchTerms();if(!terms.length)return true;const haystack=`${r.title||''} ${r.company||''}`.toLowerCase();return terms.every(term=>haystack.includes(term))}
const searchedRows=rows=>rows.filter(matchesSearch);
let minScore='';
const sponsorshipChoices=['Sponsor','Likely','Unknown','Unlikely','No sponsor'];
let sponsorshipFilters=new Set(sponsorshipChoices);
function jobScore(r){const raw=r?.score;if(raw===''||raw==null)return null;const n=Number(raw);return Number.isFinite(n)?n:null}
function matchesMinScore(r){if(minScore==='')return true;const n=Number(minScore);if(!Number.isFinite(n))return true;const score=jobScore(r);return score!==null&&score>=n}
function matchesSponsorship(r){if(sponsorshipFilters.size===sponsorshipChoices.length)return true;return sponsorshipFilters.has(r.sponsorship||'Unknown')}
function matchesDiscoveryFilters(r){return matchesMinScore(r)&&matchesSponsorship(r)}
const discoveryRows=rows=>searchedRows(rows).filter(matchesDiscoveryFilters);
const discoveryFilterActive=()=>minScore!==''||sponsorshipFilters.size!==sponsorshipChoices.length;
function tabs(elId,rows){const tab=document.querySelector(`[data-target="${elId}"]`),companyTab=document.querySelector(`[data-company-target="${elId}"]`),box=document.getElementById(elId);let active=tab.querySelector('[data-k].on')?.dataset.k||'all',company=companyTab.querySelector('[data-company].on')?.dataset.company||'all';const companyNames=['all','Google','Microsoft','Apple','Amazon','Meta','TikTok'];const draw=()=>{const filtered=discoveryRows(normalRows(rows)),companyRows=k=>filtered.filter(r=>r.pipeline==='official'&&(k==='all'||r.company.toLowerCase().includes(k.toLowerCase())));tab.innerHTML=['all',...Object.keys(names)].map(k=>`<button class="tab ${k===active?'on':''}" data-k="${k}">${k==='all'?'All':names[k]} (${k==='all'?filtered.length:filtered.filter(r=>r.pipeline===k).length})</button>`).join('');companyTab.style.display=active==='official'?'flex':'none';companyTab.innerHTML=active==='official'?companyNames.map(k=>`<button class="tab ${k===company?'on':''}" data-company="${k}">${k} (${companyRows(k).length})</button>`).join(''):'';let shown=active==='all'?filtered:filtered.filter(r=>r.pipeline===active);if(active==='official'&&company!=='all')shown=companyRows(company);exportViewRows[elId]=displayRows(shown);exportViewLabels[elId]=[elId==='fresh'?'Fresh':'Rolling',active==='all'?'All':names[active],...(active==='official'&&company!=='all'?[company]:[])].join(' → ');const body=box.querySelector('tbody');if(body)body.innerHTML=jobRows(shown);else box.innerHTML=jobs(shown,false,true);bindStatus(box);bindDiscoveryFilters(box,draw);tab.querySelectorAll('button').forEach(b=>b.onclick=()=>{active=b.dataset.k;if(active!=='official')company='all';draw()});companyTab.querySelectorAll('button').forEach(b=>b.onclick=()=>{company=b.dataset.company;draw()})};draw()}
function renderDiscoveryViews(){const rolling=activeMainView==='rolling';tabs(rolling?'rolling':'fresh',rolling?D.rolling_3d:D.fresh_24h);renderMainViewTabs();renderSearchState()}
const allRows=[...(D.workflow_rows||[]),...D.fresh_24h,...D.rolling_3d,...D.referrals];const uniqueRows=()=>[...new Map(allRows.filter(r=>!isPreferenceKey(r.canonical_job_key)).map(r=>[r.canonical_job_key,r])).values()];let activeMainView='fresh';
const pipelineRuns=k=>(D.health_history||[]).filter(run=>run.pipeline===k&&(!run.mode||run.mode==='pipeline')).sort((a,b)=>String(b.run_at||'').localeCompare(String(a.run_at||''))).slice(0,k==='board'?4:2);
const runMetric=(run,key)=>run.output&&Object.prototype.hasOwnProperty.call(run.output,key)?esc(run.output[key]):'—';
const runYield=run=>`${esc(snapshotTime(run.run_at))} · ${runMetric(run,'new_jobs')} found · ${runMetric(run,'new_jobs_added')} added`;
function renderSummary(){document.getElementById('summary').innerHTML=Object.keys(names).map(k=>{const h=D.health?.components?.[k]||{status:'Warning'},keywords=(h.keywords||[]).map(value=>`<span class="pill">${esc(value)}</span>`).join(''),runs=pipelineRuns(k),runDetails=`<div class="small">Recent runs${runs.length?runs.map(run=>`<div>${runYield(run)}</div>`).join(''):' · unavailable'}</div>`;return `<div class="card"><span>${names[k]}</span> <a class="pill health-${h.status.toLowerCase()}" target="_blank" rel="noopener noreferrer" href="${D.health_report}">${h.status}</a><div class="countline"><b>${esc(h.last_good_count??0)}</b><span>usable · updated ${esc(snapshotTime(h.last_good_at))}</span></div>${keywords?`<div class="links">${keywords}</div>`:''}${runDetails}<a target="_blank" rel="noopener noreferrer" href="${D.report_links[k]}">open report</a> · <a target="_blank" rel="noopener noreferrer" href="${D.health_report}">health details</a></div>`}).join('')}
function renderHiddenCompanies(rows){const labels=new Map(rows.filter(r=>r.company_key).map(r=>[r.company_key,r.referral||r.company||r.company_key])),hidden=Object.entries(reviewStates).filter(([key,state])=>isPreferenceKey(key)&&state?.deleted).map(([key])=>{const company_key=key.slice(companyStatePrefix.length);return {company_key,company:labels.get(company_key)||company_key}}).sort((a,b)=>a.company.localeCompare(b.company));document.getElementById('hiddenCompanyCount').textContent=`(${hidden.length})`;const box=document.getElementById('hiddenCompanies');box.innerHTML=hidden.length?`<div class="links">${hidden.map(r=>`<span class="pill"><b>${esc(r.company)}</b> <button class="show-company" data-company-key="${esc(r.company_key)}" ${pendingKeys.has(companyStatePrefix+r.company_key)?'disabled':''}>Show again</button></span>`).join('')}</div>`:'<div class="empty">No hidden companies.</div>';bindStatus(box)}
function mainViewCounts(rows=uniqueRows()){return {fresh:discoveryRows(normalRows(D.fresh_24h)).length,rolling:discoveryRows(normalRows(D.rolling_3d)).length,'in-progress':searchedRows(rows.filter(r=>statusOf(r)==='in_progress'&&!isDeleted(r))).length,applied:searchedRows(rows.filter(r=>statusOf(r)==='applied_complete'&&!isDeleted(r))).length}}
function renderMainViewTabs(rows=uniqueRows()){const counts=mainViewCounts(rows);const labels={fresh:'Fresh',rolling:'Rolling','in-progress':'In Progress',applied:'Applied'};document.querySelectorAll('#mainViewTabs [data-main-view]').forEach(button=>{const on=button.dataset.mainView===activeMainView;button.classList.toggle('on',on);button.setAttribute('aria-selected',String(on));button.tabIndex=on?0:-1;button.textContent=`${labels[button.dataset.mainView]} ${counts[button.dataset.mainView]}`});document.querySelectorAll('[data-main-panel]').forEach(panel=>{panel.hidden=panel.dataset.mainPanel!==activeMainView})}
function renderSearchState(rows=uniqueRows()){const clear=document.getElementById('clearJobSearch'),count=document.getElementById('jobSearchCount'),query=searchQuery.trim(),discovery=activeMainView==='fresh'||activeMainView==='rolling',filtering=Boolean(query)||(discovery&&discoveryFilterActive());clear.hidden=!query;if(!filtering){count.textContent='';return}const matches=mainViewCounts(rows)[activeMainView];count.textContent=`${matches} match${matches===1?'':'es'} in this view`}
function initializeMainViewTabs(){const buttons=[...document.querySelectorAll('#mainViewTabs [data-main-view]')];buttons.forEach((button,index)=>{button.onclick=()=>{activeMainView=button.dataset.mainView;if(activeMainView==='fresh'||activeMainView==='rolling')renderDiscoveryViews();else{renderMainViewTabs();renderSearchState()}button.focus({preventScroll:true})};button.onkeydown=event=>{let target;if(event.key==='ArrowRight')target=buttons[(index+1)%buttons.length];else if(event.key==='ArrowLeft')target=buttons[(index-1+buttons.length)%buttons.length];else if(event.key==='Home')target=buttons[0];else if(event.key==='End')target=buttons[buttons.length-1];if(target){event.preventDefault();target.click()}}});renderMainViewTabs();renderSearchState()}
function initializeJobSearch(){const input=document.getElementById('jobSearch'),clear=document.getElementById('clearJobSearch');input.oninput=()=>{searchQuery=input.value;renderAll()};input.onkeydown=event=>{if(event.key==='Escape'&&input.value){event.preventDefault();input.value='';searchQuery='';renderAll()}};clear.onclick=()=>{input.value='';searchQuery='';renderAll();input.focus({preventScroll:true})}}
function bindDiscoveryFilters(box,draw){const score=box.querySelector('.min-score-filter'),options=box.querySelector('.filter-options'),summary=box.querySelector('.sponsorship-filter summary');if(!score||!options||!summary)return;score.value=minScore;options.querySelectorAll('input').forEach(input=>input.checked=sponsorshipFilters.has(input.value));summary.textContent=sponsorshipSummary();score.oninput=()=>{minScore=score.value.trim();draw();renderMainViewTabs();renderSearchState()};options.onchange=event=>{if(!event.target.matches('input[type=checkbox]'))return;if(event.target.checked)sponsorshipFilters.add(event.target.value);else sponsorshipFilters.delete(event.target.value);draw();renderMainViewTabs();renderSearchState()}}
const markdownCell=value=>String(value??'').replace(/\s+/g,' ').trim().replace(/\|/g,'\\|');
function markdownExport(){const rows=(exportViewRows[activeMainView]||[]).flatMap(r=>r._variants||[r]);return `## ${exportViewLabels[activeMainView]}\n\n| Company | Title | Score | Location | Link |\n|---|---|---:|---|---|${rows.length?'\n'+rows.map(r=>`| ${markdownCell(r.company)} | ${markdownCell(r.title)} | ${markdownCell(r.score)} | ${markdownCell(r.location)} | ${markdownCell(r.url)} |`).join('\n'):''}\n`}
async function copyMarkdown(){const button=document.getElementById('copyMarkdown');try{await navigator.clipboard.writeText(markdownExport());button.textContent='Copied';setTimeout(()=>button.textContent='Copy MD',1200)}catch(error){window.alert(`Could not copy Markdown: ${error.message}`)}}
function downloadMarkdown(){const blob=new Blob([markdownExport()],{type:'text/markdown;charset=utf-8'}),url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download=(exportViewLabels[activeMainView]||'jobs').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')+'.md';link.click();URL.revokeObjectURL(url)}
function initializeMarkdownExport(){document.getElementById('copyMarkdown').onclick=copyMarkdown;document.getElementById('downloadMarkdown').onclick=downloadMarkdown}
function renderAll(){const rows=uniqueRows();renderSummary();tabs('fresh',D.fresh_24h);tabs('rolling',D.rolling_3d);renderBox('referrals',normalRows(D.referrals));renderBox('inProgress',searchedRows(rows.filter(r=>statusOf(r)==='in_progress'&&!isDeleted(r))));renderBox('applied',searchedRows(rows.filter(r=>statusOf(r)==='applied_complete'&&!isDeleted(r))));const box=document.getElementById('deleted');box.innerHTML=jobs(rows.filter(isDeleted),true);bindStatus(box);renderHiddenCompanies(rows);renderMainViewTabs(rows);renderSearchState(rows)}
async function syncPending(){await Promise.all(Object.values(reviewStates).filter(state=>state?.pending).map(state=>pushState(state)))}
async function loadSharedStates(){const {data,error}=await supabase.from('job_review_status').select('canonical_job_key,status,deleted,updated_at');if(error)throw error;const merged={};(data||[]).forEach(row=>{if(row.canonical_job_key&&statusChoices.includes(row.status))merged[row.canonical_job_key]=normalizedState(row,false)});Object.values(reviewStates).filter(state=>state?.pending).forEach(local=>{const remote=merged[local.canonical_job_key];if(!remote||stateTime(local)>stateTime(remote))merged[local.canonical_job_key]=normalizedState(local,true)});reviewStates=merged;persist();sharedLoaded=true;sharedError='';renderReviewMessage();renderAll();await syncPending()}
async function refreshSharedStates(){try{await loadSharedStates()}catch(error){sharedError=`Shared review unavailable: ${error.message}`;renderReviewMessage();renderAll()}}
async function initializeSupabase(){try{const {createClient}=await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm');supabase=createClient(D.supabase.url,D.supabase.publishable_key);await refreshSharedStates()}catch(error){sharedError=`Shared review unavailable: ${error.message}`;renderReviewMessage();renderAll()}}
let updateCheckPending=false;
async function checkForDashboardUpdate(){if(updateCheckPending)return;updateCheckPending=true;try{const checkUrl=new URL(location.href);checkUrl.searchParams.set('_check',Date.now());const response=await fetch(checkUrl,{method:'HEAD',cache:'no-store'}),remote=Date.parse(response.headers.get('Last-Modified')||''),loaded=Date.parse(document.lastModified);if(response.ok&&Number.isFinite(remote)&&Number.isFinite(loaded)&&remote>loaded){checkUrl.search='';checkUrl.searchParams.set('v',String(remote));location.replace(checkUrl.href)}}catch(error){}finally{updateCheckPending=false}}
window.addEventListener('focus',checkForDashboardUpdate);document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')checkForDashboardUpdate()});
window.addEventListener('online',refreshSharedStates);renderReviewMessage();initializeJobSearch();initializeMarkdownExport();renderAll();initializeMainViewTabs();initializeSupabase();
document.getElementById('officialSearches').innerHTML=`<div class="tablewrap"><table><thead><tr><th>Tier</th><th>Company</th><th>Automation</th><th>Official searches</th><th>Note</th></tr></thead><tbody>${(D.official_searches||[]).map(c=>`<tr><td><b>${esc(c.priority_tier||'-')}</b></td><td><b>${esc(c.name)}</b></td><td class="${c.automation==='active'?'active':'manual'}">${c.automation==='active'?'Automated':'Link only'}</td><td><div class="links">${c.search_links.length?c.search_links.map(l=>`<a target="_blank" rel="noopener noreferrer" href="${esc(l.url)}">${esc(l.label||'Search')}</a>`).join(''):'-'}</div></td><td class="small">${esc(c.note)}</td></tr>`).join('')}</tbody></table></div>`;
</script></body></html>'''


def write_dashboard(payload: Dict[str, Any]) -> None:
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    dashboard_payload = {key: value for key, value in payload.items() if key != "company_profiles_pending"}
    if DASHBOARD_JSON.exists():
        previous_history = read_json(DASHBOARD_JSON, {}).get("history_details", {})
        current_history = dashboard_payload.setdefault("history_details", {})
        for key, old_values in previous_history.items():
            new_values = current_history.get(key)
            if not new_values:
                current_history[key] = old_values
            else:
                current_history[key] = [
                    old if new in (None, "", "-") else new
                    for old, new in zip(old_values, new_values)
                ]
    pending = [entry for raw in payload.get("company_profiles_pending") or [] if (entry := pending_entry(raw))]
    pending_payload = json.dumps({
        "generated_at": payload.get("generated_at", ""), "count": len(pending), "companies": pending,
    }, indent=2, ensure_ascii=False) + "\n"
    PENDING_COMPANY_PROFILES_JSON.write_text(pending_payload, encoding="utf-8")
    LOCAL_PENDING_COMPANY_PROFILES_JSON.write_text(pending_payload, encoding="utf-8")
    serialized = json.dumps(dashboard_payload, ensure_ascii=False).replace("</", "<\\/")
    DASHBOARD_JSON.write_text(json.dumps(dashboard_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    DASHBOARD_HTML.write_text(HTML_TEMPLATE.replace("__PAYLOAD__", serialized), encoding="utf-8")
    pipeline_health.write(PUBLIC_DIR, payload["health"], payload["health_history"])
    (PUBLIC_DIR / "coverage.md").write_text(coverage_reconcile.COVERAGE_MD_PATH.read_text(encoding="utf-8"), encoding="utf-8")
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
