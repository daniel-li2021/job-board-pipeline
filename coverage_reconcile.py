#!/usr/bin/env python3
"""Strict cross-pipeline coverage reconciliation.

Coverage is evaluated before LLM/ranking.  Only URL, requisition-id, or exact
company+title+location matches count as covered.  Fuzzy matches are audit hints
only.  Manual company state in ``profile/official_coverage.json`` controls
whether an exact match is suppressed from ATS/Syncareer alerts.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from sources.company_aliases import load_alias_file, match_company_alias, prepare_alias_entries
from sources.schema import (
    dedup_key,
    make_job,
    normalize_company_key,
    normalize_location_key,
    normalize_title_key,
)

BASE_DIR = Path(__file__).resolve().parent
OFFICIAL_RAW_PATH = BASE_DIR / "output" / "official_careers" / "raw.json"
OFFICIAL_STORE_PATH = BASE_DIR / "output" / "official_careers" / "jobs.json"
BOARD_STORE_PATH = BASE_DIR / "output" / "board" / "jobs.json"
SYNCAREER_STORE_PATH = BASE_DIR / "output" / "syncareer" / "watchlist.json"
REGISTRY_PATH = BASE_DIR / "source" / "official_careers.json"
REFERRAL_PATH = BASE_DIR / "source" / "target_companies.json"
COVERAGE_CONFIG_PATH = BASE_DIR / "profile" / "official_coverage.json"
REVIEW_STATE_PATH = BASE_DIR / "profile" / "review_state.json"
OUTPUT_DIR = BASE_DIR / "output" / "cross_pipeline"
COVERAGE_JSON_PATH = OUTPUT_DIR / "coverage.json"
COVERAGE_MD_PATH = OUTPUT_DIR / "coverage.md"

TRACKING_QUERY_KEYS = {
    "ref", "refid", "trackingid", "trk", "source", "utm_campaign",
    "utm_content", "utm_medium", "utm_source", "utm_term",
}


def parse_datetime(value: Any) -> Optional[datetime]:
    raw = str(value or "").strip()
    if not raw:
        return None
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        try:
            parsed = datetime.strptime(raw[:10], "%Y-%m-%d")
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def snapshot_timestamp(payload: Dict[str, Any]) -> Optional[datetime]:
    for field in ("scraped_at", "updated_at", "generated_at"):
        parsed = parse_datetime(payload.get(field))
        if parsed:
            return parsed
    return None


def normalize_url(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    try:
        parts = urlsplit(raw)
    except ValueError:
        return raw.lower().rstrip("/")
    query = [
        (k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if k.lower() not in TRACKING_QUERY_KEYS and not k.lower().startswith("utm_")
    ]
    path = re.sub(r"/+$", "", parts.path or "") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, urlencode(query), ""))


def job_ids(job: Dict[str, Any]) -> set[str]:
    values: set[str] = set()
    explicit = str(job.get("job_id") or "").strip().lower()
    if explicit:
        values.add(explicit)
    url = str(job.get("official_url") or job.get("source_url") or job.get("job_url") or "")
    values.update(re.findall(r"(?<!\d)(\d{5,})(?!\d)", url))
    values.update(re.findall(r"[0-9a-f]{8}-[0-9a-f-]{27,}", url.lower()))
    return values


def canonical_job_key(job: Dict[str, Any]) -> str:
    normalized = {
        "source": job.get("source") or job.get("source_pipeline") or "external",
        "job_id": job.get("job_id") or "",
        "company": job.get("company") or "",
        "title": job.get("title") or "",
        "location": job.get("location") or "",
        "official_url": job.get("official_url") or "",
        "source_url": job.get("source_url") or job.get("job_url") or "",
    }
    return dedup_key(normalized)


def load_registry_entries() -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    payload = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    referrals = load_alias_file(REFERRAL_PATH)
    entries: List[Dict[str, Any]] = []
    by_id: Dict[str, Dict[str, Any]] = {}
    for company in payload.get("companies", []):
        item = dict(company)
        aliases = [item.get("id", ""), item.get("name", "")]
        referral_name = match_company_alias(item.get("name", ""), referrals)
        if referral_name:
            for ref in referrals:
                if ref.get("name") == referral_name:
                    aliases.extend(ref.get("aliases") or [])
                    aliases.append(referral_name)
                    break
        item["aliases"] = aliases
        prepared = prepare_alias_entries([item])[0]
        entries.append(prepared)
        by_id[str(item.get("id"))] = prepared
    return entries, by_id


def company_id_for(name: str, registry_entries: Iterable[Dict[str, Any]]) -> Optional[str]:
    matched = match_company_alias(name, registry_entries)
    if not matched:
        return None
    for entry in registry_entries:
        if entry.get("name") == matched:
            return str(entry.get("id") or "") or None
    return None


def load_coverage_config() -> Dict[str, Dict[str, Any]]:
    try:
        payload = json.loads(COVERAGE_CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    companies = payload.get("companies", {}) if isinstance(payload, dict) else {}
    return companies if isinstance(companies, dict) else {}


def load_official_context() -> Dict[str, Any]:
    try:
        payload = json.loads(OFFICIAL_RAW_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        payload = {}
    jobs = payload.get("jobs", []) if isinstance(payload, dict) else []
    registry_entries, registry_by_id = load_registry_entries()
    by_company: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for job in jobs:
        cid = company_id_for(str(job.get("company") or ""), registry_entries)
        if cid:
            by_company[cid].append(job)
    return {
        "payload": payload,
        "jobs": jobs,
        "snapshot_at": snapshot_timestamp(payload),
        "registry_entries": registry_entries,
        "registry_by_id": registry_by_id,
        "by_company": by_company,
        "config": load_coverage_config(),
    }


def exact_match(external: Dict[str, Any], official_jobs: Iterable[Dict[str, Any]]) -> Tuple[str, Optional[Dict[str, Any]]]:
    ext_url = normalize_url(str(external.get("official_url") or external.get("source_url") or external.get("job_url") or ""))
    ext_ids = job_ids(external)
    ext_title = normalize_title_key(str(external.get("title") or ""))
    ext_location = normalize_location_key(str(external.get("location") or ""))
    for official in official_jobs:
        off_url = normalize_url(str(official.get("official_url") or official.get("source_url") or ""))
        if ext_url and off_url and ext_url == off_url:
            return "url", official
        if ext_ids and ext_ids.intersection(job_ids(official)):
            return "job_id", official
        if ext_title and ext_location:
            if ext_title == normalize_title_key(str(official.get("title") or "")) and ext_location == normalize_location_key(str(official.get("location") or "")):
                return "title_location", official
    return "", None


def fuzzy_suggestion(external: Dict[str, Any], official_jobs: Iterable[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    ext_title = normalize_title_key(str(external.get("title") or ""))
    ext_location = normalize_location_key(str(external.get("location") or ""))
    if not ext_title:
        return None
    best: Tuple[float, Optional[Dict[str, Any]]] = (0.0, None)
    for official in official_jobs:
        title = normalize_title_key(str(official.get("title") or ""))
        if not title:
            continue
        location = normalize_location_key(str(official.get("location") or ""))
        location_ok = not ext_location or not location or ext_location == location
        if not location_ok:
            continue
        ratio = SequenceMatcher(None, ext_title, title).ratio()
        if ratio > best[0]:
            best = (ratio, official)
    if best[0] < 0.84 or best[1] is None:
        return None
    return {
        "score": round(best[0], 3),
        "official_key": canonical_job_key(best[1]),
        "official_title": best[1].get("title", ""),
        "official_location": best[1].get("location", ""),
    }


def annotate_jobs(jobs: Iterable[Dict[str, Any]], source_pipeline: str, context: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    context = context or load_official_context()
    snapshot_at: Optional[datetime] = context.get("snapshot_at")
    config = context.get("config", {})
    registry_entries = context.get("registry_entries", [])
    by_company = context.get("by_company", {})
    annotations: List[Dict[str, Any]] = []
    snapshot_iso = snapshot_at.isoformat() if snapshot_at else ""
    review = load_review_state()

    for job in jobs:
        cid = company_id_for(str(job.get("company") or ""), registry_entries)
        job["source_pipeline"] = source_pipeline
        job["canonical_job_key"] = canonical_job_key(job)
        job["official_snapshot_at"] = snapshot_iso
        job["source_snapshot_at"] = str(job.get("last_seen") or job.get("first_seen") or job.get("fetched_at") or "")
        job["canonical_source"] = source_pipeline
        job["duplicate_of"] = ""
        job["suppress_alert"] = False
        job["coverage_match_method"] = ""

        if not cid:
            job["coverage_status"] = "not_dedicated"
        else:
            job["official_company_id"] = cid
            manual = config.get(cid, {}) if isinstance(config.get(cid, {}), dict) else {}
            manual_status = str(manual.get("status") or "unvalidated")
            registry = context.get("registry_by_id", {}).get(cid, {})
            if manual_status == "unsupported" or registry.get("adapter") == "skip":
                job["coverage_status"] = "official_unsupported"
            else:
                method, official = exact_match(job, by_company.get(cid, []))
                if official:
                    job["coverage_match_method"] = method
                    job["duplicate_of"] = canonical_job_key(official)
                    job["canonical_source"] = "official"
                    if manual_status == "validated":
                        job["coverage_status"] = "official_duplicate"
                        job["suppress_alert"] = True
                    else:
                        job["coverage_status"] = "covered_unvalidated"
                else:
                    source_at = parse_datetime(job.get("first_seen") or job.get("fetched_at") or job.get("last_seen"))
                    if source_at and snapshot_at and source_at > snapshot_at:
                        job["coverage_status"] = "pending_official_refresh"
                    else:
                        job["coverage_status"] = "official_gap"
                    suggestion = fuzzy_suggestion(job, by_company.get(cid, []))
                    if suggestion:
                        job["coverage_suggestion"] = suggestion
        review_entry = review.get(job["canonical_job_key"], {})
        job["review_status"] = review_entry.get("status", "unreviewed") if isinstance(review_entry, dict) else "unreviewed"
        annotations.append(job)
    return annotations


def within_days(job: Dict[str, Any], now: datetime, days: int) -> bool:
    confidence = str(job.get("date_confidence") or "unknown").lower()
    fields = ("posted_date", "posting_date", "first_seen") if confidence in {"high", "medium"} else ("first_seen", "posted_date", "posting_date")
    for field in fields:
        parsed = parse_datetime(job.get(field))
        if parsed:
            return parsed >= now - timedelta(days=days)
    return True


def _load_store_entries(path: Path) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}, []
    return payload, list(payload.get("entries", []))


def board_scope(now: datetime) -> List[Dict[str, Any]]:
    _, entries = _load_store_entries(BOARD_STORE_PATH)
    return [dict(e) for e in entries if e.get("filter_status") == "kept" and within_days(e, now, 3)]


def normalize_syncareer_job(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Map a Syncareer row/watchlist entry to the shared filtering schema."""
    job = make_job(
        source="syncareer",
        company=str(entry.get("company") or ""),
        title=str(entry.get("title") or ""),
        location=str(entry.get("location") or ""),
        job_id=str(entry.get("job_id") or ""),
        posted_date=entry.get("posting_date") or entry.get("posted_date") or "",
        date_confidence="medium",
        source_url=str(entry.get("job_url") or entry.get("url") or ""),
        official_url=str(entry.get("job_url") or entry.get("url") or ""),
        description="\n".join(
            str(entry.get(field) or "") for field in ("description", "requirements", "snippet")
        ),
    )
    job["first_seen"] = str(entry.get("first_seen") or "")
    return job


def syncareer_job_in_scope(entry: Dict[str, Any]) -> bool:
    """Apply the ATS hard + role-family gates before coverage or LLM work."""
    import board_pipeline as board  # Lazy import avoids a board->coverage cycle.

    job = normalize_syncareer_job(entry)
    keep, _ = board.hard_filter(job)
    if not keep:
        return False
    keep, _ = board.role_seniority_prefilter(job)
    return keep


def syncareer_scope(now: datetime) -> List[Dict[str, Any]]:
    _, entries = _load_store_entries(SYNCAREER_STORE_PATH)
    scoped: List[Dict[str, Any]] = []
    for entry in entries:
        if str(entry.get("kept") or "").lower() not in {"yes", "true", "1"}:
            continue
        job = normalize_syncareer_job(entry)
        if not within_days(job, now, 3):
            continue
        if syncareer_job_in_scope(entry):
            scoped.append(job)
    return scoped


def load_review_state() -> Dict[str, Any]:
    try:
        payload = json.loads(REVIEW_STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload.get("jobs", {}) if isinstance(payload, dict) else {}


def build_coverage_payload(now: Optional[datetime] = None) -> Dict[str, Any]:
    now = now or datetime.now(timezone.utc)
    context = load_official_context()
    board_jobs = annotate_jobs(board_scope(now), "board", context)
    syncareer_jobs = annotate_jobs(syncareer_scope(now), "syncareer", context)
    records = board_jobs + syncareer_jobs
    review = load_review_state()
    for record in records:
        state = review.get(record.get("canonical_job_key"), {})
        record["review_status"] = state.get("status", "unreviewed") if isinstance(state, dict) else "unreviewed"

    company_stats: Dict[str, Counter] = defaultdict(Counter)
    for record in records:
        cid = record.get("official_company_id")
        if not cid:
            continue
        company_stats[cid]["in_scope"] += 1
        company_stats[cid][record.get("coverage_status", "unknown")] += 1
        company_stats[cid][f"source_{record.get('source_pipeline')}"] += 1

    companies: List[Dict[str, Any]] = []
    config = context.get("config", {})
    for cid, registry in context.get("registry_by_id", {}).items():
        counts = company_stats.get(cid, Counter())
        exact = counts["official_duplicate"] + counts["covered_unvalidated"]
        observed = counts["in_scope"] - counts["pending_official_refresh"] - counts["official_unsupported"]
        ratio = (exact / observed) if observed > 0 else None
        manual = config.get(cid, {}) if isinstance(config.get(cid, {}), dict) else {}
        companies.append({
            "id": cid,
            "name": registry.get("name", cid),
            "adapter": registry.get("adapter", ""),
            "manual_status": manual.get("status", "unvalidated"),
            "in_scope": counts["in_scope"],
            "exact_covered": exact,
            "official_gaps": counts["official_gap"],
            "pending_refresh": counts["pending_official_refresh"],
            "unsupported": counts["official_unsupported"],
            "coverage_ratio": round(ratio, 4) if ratio is not None else None,
            "board_jobs": counts["source_board"],
            "syncareer_jobs": counts["source_syncareer"],
        })
    companies.sort(key=lambda c: (c["manual_status"] != "validated", -(c["in_scope"] or 0), c["name"]))
    return {
        "generated_at": now.isoformat(),
        "window_days": 3,
        "official_snapshot_at": context.get("snapshot_at").isoformat() if context.get("snapshot_at") else "",
        "manual_validation_target": "100% exact observed in-scope coverage; user makes final validation decision",
        "counts": dict(Counter(r.get("coverage_status", "unknown") for r in records)),
        "companies": companies,
        "records": records,
    }


def write_coverage_outputs(payload: Dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    COVERAGE_JSON_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Cross-pipeline official coverage audit",
        "",
        f"- Generated: {payload.get('generated_at', '')}",
        f"- Official snapshot: {payload.get('official_snapshot_at') or 'missing'}",
        "- Coverage scope: jobs from the last 3 days that pass shared hard + role/seniority prefilters; LLM score is not used.",
        "- Validation: 100% exact observed coverage is the current review target; final validation is manual.",
        "",
        "## Company coverage",
        "",
        "| Company | Manual state | Adapter | In scope | Exact | Gaps | Pending refresh | Coverage |",
        "|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for company in payload.get("companies", []):
        ratio = company.get("coverage_ratio")
        ratio_text = "-" if ratio is None else f"{ratio:.0%}"
        lines.append(
            f"| {company['name']} | {company['manual_status']} | {company['adapter']} | "
            f"{company['in_scope']} | {company['exact_covered']} | {company['official_gaps']} | "
            f"{company['pending_refresh']} | {ratio_text} |"
        )
    gaps = [r for r in payload.get("records", []) if r.get("coverage_status") in {"official_gap", "pending_official_refresh"}]
    lines.extend(["", f"## Gaps / pending review ({len(gaps)})", "", "| Status | Pipeline | Company | Title | Location | Link |", "|---|---|---|---|---|---|"])
    for row in gaps:
        link_url = row.get("official_url") or row.get("source_url") or row.get("job_url") or ""
        link = f"[open]({link_url})" if link_url else "-"
        lines.append(
            f"| {row.get('coverage_status')} | {row.get('source_pipeline')} | "
            f"{str(row.get('company') or '').replace('|','/')} | {str(row.get('title') or '').replace('|','/')[:90]} | "
            f"{str(row.get('location') or '').replace('|','/')} | {link} |"
        )
    COVERAGE_MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Reconcile Official vs ATS/Syncareer coverage")
    parser.add_argument("--json", action="store_true", help="Print summary JSON")
    args = parser.parse_args()
    payload = build_coverage_payload()
    write_coverage_outputs(payload)
    if args.json:
        print(json.dumps({"counts": payload["counts"], "companies": payload["companies"]}, indent=2))
    else:
        print(f"Wrote {COVERAGE_JSON_PATH} and {COVERAGE_MD_PATH}")


if __name__ == "__main__":
    main()
