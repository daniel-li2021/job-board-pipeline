#!/usr/bin/env python3
"""Strict cross-pipeline coverage reconciliation.

Coverage is evaluated before LLM/ranking.  Only URL, requisition-id, or exact
company+title+location matches count as covered.  Fuzzy matches are audit hints
only.  Every exact Official match is suppressed from external pipelines;
manual company state remains an audit signal and never hides an entire company.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import re
import requests
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlsplit

import compact_ai

from sources.company_aliases import load_alias_file, match_company_alias, prepare_alias_entries
from state_io import decode_json_bytes
from sources.schema import (
    adopt_better_posted_date,
    dedup_key,
    is_aggregator_url,
    is_outbound_tracker_url,
    parse_datetime,
    make_job,
    normalize_job_url,
    normalize_location_key,
    normalize_title_key,
    read_source_snapshot_payload,
)

BASE_DIR = Path(__file__).resolve().parent
OFFICIAL_RAW_PATH = BASE_DIR / "output" / "cache" / "official_careers" / "raw.json.gz"
LEGACY_OFFICIAL_RAW_PATH = BASE_DIR / "output" / "official_careers" / "raw.json.gz"
OFFICIAL_STORE_PATH = BASE_DIR / "output" / "official_careers" / "jobs.json"
BOARD_STORE_PATH = BASE_DIR / "output" / "board" / "jobs.json"
SYNCAREER_STORE_PATH = BASE_DIR / "output" / "syncareer" / "jobs.json"
REGISTRY_PATH = BASE_DIR / "config" / "official_careers.json"
REFERRAL_PATH = BASE_DIR / "config" / "target_companies.json"
COVERAGE_CONFIG_PATH = BASE_DIR / "profile" / "official_coverage.json"
REVIEW_STATE_PATH = BASE_DIR / "profile" / "review_state.json"
OUTPUT_DIR = BASE_DIR / "output" / "cross_pipeline"
COVERAGE_JSON_PATH = OUTPUT_DIR / "coverage.json"
COVERAGE_MD_PATH = OUTPUT_DIR / "coverage.md"
IDENTITY_AI_CACHE_PATH = OUTPUT_DIR / "identity_ai_cache.json"

def snapshot_timestamp(payload: Dict[str, Any]) -> Optional[datetime]:
    for field in ("scraped_at", "updated_at", "generated_at"):
        parsed = parse_datetime(payload.get(field))
        if parsed:
            return parsed
    return None


def normalize_url(value: str) -> str:
    """Backward-compatible public alias for the shared URL normalizer."""
    return normalize_job_url(value)


def job_urls(job: Dict[str, Any]) -> set[str]:
    return {
        normalized
        for field in ("official_url", "application_url", "source_url", "job_url", "url")
        if (normalized := normalize_url(str(job.get(field) or "")))
    }


def job_ids(job: Dict[str, Any]) -> set[str]:
    values: set[str] = set()
    source = str(job.get("source") or job.get("source_pipeline") or "").lower()
    aggregator_record = any(name in source for name in ("linkedin", "indeed", "glassdoor", "syncareer"))
    for field in ("requisition_id", "req_id"):
        explicit = str(job.get(field) or "").strip().lower()
        if explicit:
            values.add(explicit)
    if not aggregator_record:
        explicit = str(job.get("job_id") or "").strip().lower()
        if explicit:
            values.add(explicit)
    for url in job_urls(job):
        host = (urlsplit(url).hostname or "").lower()
        if is_aggregator_url(url) or is_outbound_tracker_url(url) or (
            host == "syncareer.com" or host.endswith(".syncareer.com")
        ):
            continue
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
    candidates: List[Tuple[Dict[str, Any], List[Dict[str, Any]], str]] = []
    for path, source in ((OFFICIAL_RAW_PATH, "local_raw_cache"), (LEGACY_OFFICIAL_RAW_PATH, "legacy_raw")):
        try:
            raw_payload = json.loads(gzip.decompress(path.read_bytes()))
        except (OSError, json.JSONDecodeError, UnicodeDecodeError):
            continue
        if isinstance(raw_payload, dict):
            candidates.append((raw_payload, list(raw_payload.get("jobs") or []), source))
    store_payload, store_jobs = _load_store_entries(OFFICIAL_STORE_PATH)
    if store_payload:
        fields = store_payload.get("coverage_fields") or []
        rows = store_payload.get("coverage_entries") or []
        coverage_jobs = [dict(zip(fields, row)) for row in rows if isinstance(row, list)] if fields else store_jobs
        candidates.append((store_payload, coverage_jobs, "published_store"))
    payload, jobs, coverage_source = max(
        candidates or [({}, [], "missing")],
        key=lambda item: snapshot_timestamp(item[0]) or datetime.min.replace(tzinfo=timezone.utc),
    )
    scraped_company_ids = set(payload.get("scraped_company_ids") or []) if isinstance(payload, dict) else set()
    registry_entries, registry_by_id = load_registry_entries()
    by_company: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for job in jobs:
        cid = company_id_for(str(job.get("company") or ""), registry_entries)
        if cid:
            by_company[cid].append(job)
    return {
        "payload": payload,
        "jobs": jobs,
        "coverage_source": coverage_source,
        "snapshot_at": snapshot_timestamp(payload),
        "registry_entries": registry_entries,
        "registry_by_id": registry_by_id,
        "by_company": by_company,
        "scraped_company_ids": scraped_company_ids,
        "config": load_coverage_config(),
        "company_runs": payload.get("coverage_company_runs") or {},
    }


def exact_match(external: Dict[str, Any], official_jobs: Iterable[Dict[str, Any]]) -> Tuple[str, Optional[Dict[str, Any]]]:
    ext_urls = job_urls(external)
    ext_ids = job_ids(external)
    for official in official_jobs:
        if ext_urls.intersection(job_urls(official)):
            return "url", official
        if ext_ids and ext_ids.intersection(job_ids(official)):
            return "job_id", official
    # A stable employer-side ID that disagrees with the Official snapshot is
    # stronger evidence than title/location similarity.
    if ext_ids:
        return "", None
    title_location_candidates = title_location_matches(external, official_jobs)
    # Title/location is safe only when it identifies one official requisition.
    # Multiple same-title jobs in one city remain reviewable rather than being
    # silently attached to an arbitrary requisition.
    if len(title_location_candidates) == 1:
        return "title_location", title_location_candidates[0]
    return "", None


def title_location_matches(external: Dict[str, Any], official_jobs: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    ext_title = normalize_title_key(str(external.get("title") or ""))
    ext_location = normalize_location_key(str(external.get("location") or ""))
    if not ext_title or not ext_location:
        return []
    remote_title = bool(re.search(r"\bremote\b\s*\)?\s*$", str(external.get("title") or ""), re.I))
    return [
        official for official in official_jobs
        if ext_title == normalize_title_key(str(official.get("title") or ""))
        and (
            remote_title
            or locations_compatible(ext_location, normalize_location_key(str(official.get("location") or "")))
        )
    ]


def hydrate_from_original(external: Dict[str, Any], original: Dict[str, Any]) -> None:
    """Copy authoritative employer fields while preserving discovery provenance."""
    provenance = (str(external.get("source") or "") + str(external.get("discovered_via") or "")).lower()
    if not external.get("aggregator_posted_date") and any(name in provenance for name in ("linkedin", "indeed", "glassdoor")):
        external["aggregator_posted_date"] = external.get("posted_date", "")
    for field in ("official_url", "description", "title", "location"):
        if original.get(field):
            external[field] = original[field]
    adopt_better_posted_date(external, original)
    if original.get("updated_date"):
        external["updated_date"] = original["updated_date"]
    external["original_resolved"] = bool(external.get("official_url"))


def locations_compatible(left_key: str, right_key: str) -> bool:
    """Return true for the same city with compatible state information.

    Handles single-location external rows against multi-location official rows
    and Workday's ``State - City`` format. Generic remote/state-only tokens do
    not establish a match by themselves.
    """
    if not left_key or not right_key:
        return False
    if left_key == right_key:
        return True
    left = set(left_key.split("|"))
    right = set(right_key.split("|"))
    state_tokens = {
        "al", "ak", "az", "ar", "ca", "co", "ct", "de", "fl", "ga", "hi", "id",
        "il", "in", "ia", "ks", "ky", "la", "me", "md", "ma", "mi", "mn", "ms",
        "mo", "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc", "nd", "oh", "ok",
        "or", "pa", "ri", "sc", "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv",
        "wi", "wy", "dc",
    }
    generic = state_tokens | {"remote", "us"}
    # Multi-location feeds sometimes omit a state for one city while including
    # states for other cities. A shared city is stronger evidence than the
    # aggregate state-set conflict; exact_match still requires one requisition.
    if (left - generic) & (right - generic):
        return True
    left_states = left & state_tokens
    right_states = right & state_tokens
    if left_states and right_states and left_states.isdisjoint(right_states):
        return False
    # Exact-title matching remains safe when one source exposes only a US-wide
    # location and the other provides a US city/state. Uniqueness is enforced
    # by exact_match before a record can be suppressed.
    left_us = "us" in left or bool(left_states)
    right_us = "us" in right or bool(right_states)
    broad_regions = {"canada", "europe", "european union", "north america", "worldwide"}
    broad_generic = generic | broad_regions
    return left_us and right_us and (left <= broad_generic or right <= broad_generic)


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
    scraped_company_ids = context.get("scraped_company_ids", set())
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
            elif not by_company.get(cid) and cid not in scraped_company_ids:
                # A configured adapter with no company records in the merged
                # official snapshot has not established a comparable baseline
                # yet. Treat it as awaiting its first refresh, not as a miss.
                job["coverage_status"] = "pending_official_refresh"
            else:
                method, official = exact_match(job, by_company.get(cid, []))
                if official:
                    hydrate_from_original(job, official)
                    job["coverage_match_method"] = method
                    job["duplicate_of"] = canonical_job_key(official)
                    job["canonical_source"] = "official"
                    job["coverage_status"] = "official_duplicate"
                    job["suppress_alert"] = True
                else:
                    ambiguous = title_location_matches(job, by_company.get(cid, []))
                    stable_ids = sorted(job_ids(job))
                    if stable_ids:
                        job["coverage_status"] = "official_identity_unmatched"
                        job["coverage_stable_ids"] = stable_ids[:10]
                        job["coverage_candidate_count"] = len(ambiguous)
                        job["coverage_candidate_ids"] = [str(item.get("job_id") or "") for item in ambiguous[:10]]
                    elif len(ambiguous) > 1:
                        job["coverage_status"] = "official_ambiguous"
                        job["coverage_candidate_count"] = len(ambiguous)
                        job["coverage_candidate_ids"] = [str(item.get("job_id") or "") for item in ambiguous[:10]]
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
        payload = decode_json_bytes(path.read_bytes())
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return {}, []
    if not isinstance(payload, dict):
        return {}, []
    return payload, list(payload.get("entries", []))


def board_scope(now: datetime) -> List[Dict[str, Any]]:
    _, entries = _load_store_entries(BOARD_STORE_PATH)
    current: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for source in ("linkedin", "indeed", "glassdoor"):
        for job in read_source_snapshot_payload(source).get("jobs", []):
            key = (source, str(job.get("job_id") or ""))
            if key[1]:
                current[key] = job
    scoped: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for entry in entries:
        if entry.get("filter_status") != "kept" or not within_days(entry, now, 3):
            continue
        job = dict(entry)
        latest = current.get((str(job.get("source") or "").lower(), str(job.get("job_id") or "")), {})
        for field in ("application_url", "official_url"):
            if latest.get(field):
                job[field] = latest[field]
        if latest.get("application_url") and job.get("official_url"):
            application_ids = job_ids({"source": job.get("source"), "application_url": latest["application_url"]})
            stored_ids = job_ids({"official_url": job["official_url"]})
            if application_ids and stored_ids and application_ids.isdisjoint(stored_ids):
                job["official_url"] = ""
        key = (
            str(job.get("source") or "").lower(),
            str(job.get("job_id") or canonical_job_key(job)),
            str(job.get("company") or "").lower(),
        )
        if key not in scoped or str(job.get("last_seen") or "") > str(scoped[key].get("last_seen") or ""):
            scoped[key] = job
    return list(scoped.values())


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
        scoped.append(job)
    return scoped


def load_review_state() -> Dict[str, Any]:
    try:
        payload = json.loads(REVIEW_STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload.get("jobs", {}) if isinstance(payload, dict) else {}


def _loss_reason(record: Dict[str, Any], context: Dict[str, Any], now: datetime) -> str:
    status = str(record.get("coverage_status") or "")
    if not str(record.get("company") or "").strip():
        return "unclassifiable"
    if status in {"not_dedicated", "official_unsupported"}:
        return "unsupported_company"
    if status == "official_duplicate":
        return "exact_match"
    cid = str(record.get("official_company_id") or "")
    run = context.get("company_runs", {}).get(cid, {})
    last_success = parse_datetime(run.get("last_success_at"))
    last_comparable = parse_datetime(run.get("last_comparable_at"))
    source_first = parse_datetime(record.get("first_seen") or record.get("fetched_at"))
    if source_first and last_success and source_first > last_success:
        return "source_timing"
    if status == "pending_official_refresh" and source_first and context.get("snapshot_at") and source_first > context["snapshot_at"]:
        return "source_timing"
    if status in {"official_ambiguous", "official_identity_unmatched"} and record.get("coverage_candidate_count", 0):
        return "identity_mismatch"
    if not last_comparable or now - last_comparable > timedelta(days=3):
        return "unverified_snapshot"
    return "discovery_miss"


def _identity_cases(record: Dict[str, Any], context: Dict[str, Any]) -> List[Tuple[Dict[str, Any], Dict[str, Any]]]:
    cid = str(record.get("official_company_id") or "")
    candidates = title_location_matches(record, context.get("by_company", {}).get(cid, []))
    suggestion = record.get("coverage_suggestion") or {}
    if not candidates and suggestion:
        candidates = [job for job in context.get("by_company", {}).get(cid, [])
                      if canonical_job_key(job) == suggestion.get("official_key")][:1]
    if not candidates:
        return []
    def compact(job: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "company": str(job.get("company") or "")[:80],
            "title": str(job.get("title") or "")[:120],
            "location": str(job.get("location") or "")[:100],
            "date": str(job.get("posted_date") or job.get("first_seen") or "")[:30],
            "ids": sorted(job_ids(job))[:3],
            "url": str(job.get("official_url") or job.get("application_url") or job.get("source_url") or "")[:250],
        }
    cases = []
    for candidate in candidates[:5]:
        evidence = {"external": compact(record), "candidate": compact(candidate)}
        digest = hashlib.sha256(json.dumps(evidence, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        cases.append(({"case_id": digest, **evidence}, candidate))
    return cases


def _verify_employer_redirect(record: Dict[str, Any], candidate: Dict[str, Any]) -> Tuple[bool, bool]:
    """Resolve one direct employer link; never contact aggregators from GitHub."""
    target = normalize_url(str(candidate.get("official_url") or ""))
    if not target:
        return False, False
    target_host = (urlsplit(target).hostname or "").lower()
    for field in ("application_url", "official_url", "source_url"):
        source = str(record.get(field) or "")
        host = (urlsplit(source).hostname or "").lower()
        if (not source.startswith("https://") or host != target_host
                or is_aggregator_url(source) or is_outbound_tracker_url(source)
                or normalize_url(source) == target):
            continue
        response = requests.get(source, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        return response.status_code < 400 and normalize_url(response.url) == target, True
    return False, False


def _identity_ai(records: List[Dict[str, Any]], context: Dict[str, Any], *, use_ai: bool) -> Dict[str, Any]:
    try:
        cache = json.loads(IDENTITY_AI_CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        cache = {}
    if not isinstance(cache, dict):
        cache = {}
    entries = cache.get("entries", {}) if isinstance(cache.get("entries"), dict) else {}
    new_cases: Dict[str, Dict[str, Any]] = {}
    pairs: Dict[str, Tuple[Dict[str, Any], Dict[str, Any]]] = {}
    for record in records:
        if record.get("coverage_status") not in {"official_ambiguous", "official_identity_unmatched"}:
            continue
        for case, candidate in _identity_cases(record, context):
            case_id = case["case_id"]
            record.setdefault("identity_case_ids", []).append(case_id)
            pairs[case_id] = (record, candidate)
            if case_id not in entries:
                new_cases[case_id] = case
    errors: List[str] = []
    verification_requests = 0
    key = os.getenv("OPENAI_API_KEY", "")
    if use_ai and key and new_cases:
        try:
            answered = compact_ai.decide(
                task="identity_evidence: Are these postings the same employer requisition? Be conservative when IDs disagree or candidates are multiple.",
                cases=new_cases.values(), choices=("likely_same", "ambiguous", "different"), api_key=key,
            )
            entries.update(answered)
        except Exception as exc:
            errors.append(f"{type(exc).__name__}: {exc}")
    for record in records:
        judgments = []
        for case_id in record.get("identity_case_ids") or []:
            decision = entries.get(case_id)
            if isinstance(decision, dict):
                judgments.append((case_id, decision))
        likely = [(cid, d) for cid, d in judgments if d.get("decision") == "likely_same" and float(d.get("confidence") or 0) >= 0.9]
        if len(likely) == 1:
            case_id, decision = likely[0]
            candidate = pairs[case_id][1]
            if not decision.get("verified_url") and use_ai and verification_requests < 10:
                try:
                    verified, attempted = _verify_employer_redirect(record, candidate)
                    if attempted:
                        verification_requests += 1
                    if verified:
                        decision["verified_url"] = str(candidate.get("official_url") or "")
                except requests.RequestException as exc:
                    errors.append(f"redirect verification: {type(exc).__name__}")
            if decision.get("verified_url") == candidate.get("official_url"):
                hydrate_from_original(record, candidate)
                record["coverage_match_method"] = "verified_redirect"
                record["duplicate_of"] = canonical_job_key(candidate)
                record["canonical_source"] = "official"
                record["coverage_status"] = "official_duplicate"
                record["suppress_alert"] = True
                record["coverage_loss"] = "exact_match"
        if judgments:
            case_id, decision = max(judgments, key=lambda pair: (pair[1].get("decision") == "likely_same", float(pair[1].get("confidence") or 0)))
            record["identity_ai"] = {
                "decision": decision.get("decision"), "confidence": decision.get("confidence"),
                "candidate_id": str(pairs[case_id][1].get("job_id") or ""),
                "verification": "verified_redirect" if decision.get("verified_url") else "needs_independent_employer_url_or_id",
            }
    if use_ai and key and (new_cases or verification_requests):
        try:
            IDENTITY_AI_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
            IDENTITY_AI_CACHE_PATH.write_text(
                json.dumps({"version": 1, "entries": entries}, sort_keys=True, separators=(",", ":")) + "\n",
                encoding="utf-8",
            )
        except OSError as exc:
            errors.append(f"cache write: {type(exc).__name__}: {exc}")
    return {"cases": len(pairs),
            "new_cases": len(new_cases), "api_requests": (len(new_cases) + compact_ai.BATCH_SIZE - 1) // compact_ai.BATCH_SIZE if use_ai and key and not errors else 0,
            "verification_requests": verification_requests, "errors": errors}


def build_coverage_payload(now: Optional[datetime] = None, *, use_ai: bool = False) -> Dict[str, Any]:
    now = now or datetime.now(timezone.utc)
    context = load_official_context()
    board_jobs = annotate_jobs(board_scope(now), "board", context)
    syncareer_jobs = annotate_jobs(syncareer_scope(now), "syncareer", context)
    records = board_jobs + syncareer_jobs
    for record in records:
        record["coverage_loss"] = _loss_reason(record, context, now)
    identity_ai = _identity_ai(records, context, use_ai=use_ai)
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
        if record.get("coverage_match_method"):
            company_stats[cid][f"method_{record['coverage_match_method']}"] += 1

    companies: List[Dict[str, Any]] = []
    config = context.get("config", {})
    for cid, registry in context.get("registry_by_id", {}).items():
        counts = company_stats.get(cid, Counter())
        exact = counts["official_duplicate"] + counts["covered_unvalidated"]
        comparable = (
            exact + counts["official_ambiguous"] + counts["official_identity_unmatched"]
            + counts["official_gap"]
        )
        present = exact + counts["official_ambiguous"]
        manual = config.get(cid, {}) if isinstance(config.get(cid, {}), dict) else {}
        companies.append({
            "id": cid,
            "name": registry.get("name", cid),
            "adapter": registry.get("adapter", ""),
            "manual_status": manual.get("status", "unvalidated"),
            "in_scope": counts["in_scope"],
            "exact_covered": exact,
            "official_gaps": counts["official_gap"],
            "ambiguous_covered": counts["official_ambiguous"],
            "identity_unmatched": counts["official_identity_unmatched"],
            "pending_refresh": counts["pending_official_refresh"],
            "unsupported": counts["official_unsupported"],
            "coverage_ratio": round(exact / comparable, 4) if comparable else None,
            "official_presence_ratio": round(present / comparable, 4) if comparable else None,
            "identity_resolution_ratio": round(exact / present, 4) if present else None,
            "board_jobs": counts["source_board"],
            "syncareer_jobs": counts["source_syncareer"],
            "exact_methods": {
                method: counts[f"method_{method}"]
                for method in ("url", "job_id", "title_location", "verified_redirect")
                if counts[f"method_{method}"]
            },
        })
    companies.sort(key=lambda c: (c["manual_status"] != "validated", -(c["in_scope"] or 0), c["name"]))
    adapter_counts = Counter(str(company.get("adapter") or "skip") for company in companies)
    configured_total = len(companies)
    link_only = adapter_counts.get("skip", 0)
    status_counts = Counter(r.get("coverage_status", "unknown") for r in records)
    exact_methods = Counter(
        r.get("coverage_match_method") for r in records if r.get("coverage_match_method")
    )
    comparable = (
        status_counts["official_duplicate"]
        + status_counts["official_ambiguous"]
        + status_counts["official_identity_unmatched"]
        + status_counts["official_gap"]
    )
    present = status_counts["official_duplicate"] + status_counts["official_ambiguous"]
    losses = Counter(r["coverage_loss"] for r in records)
    def loss_company(record: Dict[str, Any]) -> str:
        cid = str(record.get("official_company_id") or "")
        registry = context.get("registry_by_id", {}).get(cid, {})
        return str(registry.get("name") or record.get("company") or "(missing company)")
    top_loss_companies = {
        reason: [
            {"company": name, "count": count}
            for name, count in Counter(
                loss_company(r) for r in records if r["coverage_loss"] == reason
            ).most_common(10)
        ]
        for reason in ("unsupported_company", "discovery_miss", "identity_mismatch", "source_timing", "unverified_snapshot", "unclassifiable")
    }
    board_payload, _ = _load_store_entries(BOARD_STORE_PATH)
    sync_payload, _ = _load_store_entries(SYNCAREER_STORE_PATH)
    return {
        "generated_at": now.isoformat(),
        "window_days": 3,
        "official_snapshot_at": context.get("snapshot_at").isoformat() if context.get("snapshot_at") else "",
        "official_coverage_source": context.get("coverage_source", ""),
        "board_snapshot_at": str(board_payload.get("updated_at") or board_payload.get("scraped_at") or ""),
        "syncareer_snapshot_at": str(sync_payload.get("updated_at") or sync_payload.get("scraped_at") or ""),
        "manual_validation_target": "100% exact observed in-scope coverage; user makes final validation decision",
        "counts": dict(status_counts),
        "loss_funnel": {
            "external_in_scope": len(records),
            "supported_company": len(records) - losses["unsupported_company"] - losses["unclassifiable"],
            "comparable_official": losses["exact_match"] + losses["identity_mismatch"] + losses["discovery_miss"],
            "official_candidate_found": losses["exact_match"] + losses["identity_mismatch"],
            "exact_identity_matched": losses["exact_match"],
            "losses": dict(losses),
        },
        "top_loss_companies": top_loss_companies,
        "identity_ai": identity_ai,
        "coverage_ratio": round(status_counts["official_duplicate"] / comparable, 4) if comparable else None,
        "observed_coverage_ratio": round(present / comparable, 4) if comparable else None,
        "identity_resolution_ratio": round(status_counts["official_duplicate"] / present, 4) if present else None,
        "exact_match_methods": dict(exact_methods),
        "registry_counts": {
            "companies": configured_total,
            "implemented": configured_total - link_only,
            "link_only": link_only,
            "adapters": dict(sorted(adapter_counts.items())),
        },
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
        f"- Board snapshot: {payload.get('board_snapshot_at') or 'missing'}",
        f"- Syncareer snapshot: {payload.get('syncareer_snapshot_at') or 'missing'}",
        f"- Official coverage source: {payload.get('official_coverage_source') or 'unknown'}",
        "- Coverage scope: jobs from the last 3 days that pass shared hard + role/seniority prefilters; LLM score is not used.",
        "- Validation: 100% exact observed coverage is the current review target; final validation is manual.",
        f"- Registry adapters: {payload.get('registry_counts', {}).get('implemented', 0)} implemented / "
        f"{payload.get('registry_counts', {}).get('companies', 0)} companies; "
        f"{payload.get('registry_counts', {}).get('link_only', 0)} remain link-only.",
        f"- Exact reconciliation rate: "
        f"{payload.get('counts', {}).get('official_duplicate', 0)} exact / "
        f"{payload.get('counts', {}).get('official_duplicate', 0) + payload.get('counts', {}).get('official_ambiguous', 0) + payload.get('counts', {}).get('official_identity_unmatched', 0) + payload.get('counts', {}).get('official_gap', 0)} comparable "
        f"({payload.get('coverage_ratio', 0):.1%})." if payload.get("coverage_ratio") is not None else "- Exact reconciliation rate: not available.",
        f"- Official presence rate: {payload.get('observed_coverage_ratio', 0):.1%}; this includes ambiguous candidates."
        if payload.get("observed_coverage_ratio") is not None else "- Official presence coverage: not available.",
        f"- Identity resolution within observed Official matches: {payload.get('identity_resolution_ratio', 0):.1%}."
        if payload.get("identity_resolution_ratio") is not None else "- Identity resolution: not available.",
        f"- Identity evidence requiring review: {payload.get('counts', {}).get('official_ambiguous', 0)} ambiguous title/location record(s) and "
        f"{payload.get('counts', {}).get('official_identity_unmatched', 0)} stable-ID record(s) absent from the snapshot; all remain unsuppressed.",
        f"- Exact match methods: {payload.get('exact_match_methods') or 'none'}",
        "",
        "## Loss funnel",
        "",
        "Counts use the same three-day external records as the existing rate. Official candidate presence is evidence, not a verified duplicate.",
        "",
        "| Stage or loss | Records |",
        "|---|---:|",
        f"| External in scope | {payload.get('loss_funnel', {}).get('external_in_scope', 0)} |",
        f"| Supported company | {payload.get('loss_funnel', {}).get('supported_company', 0)} |",
        f"| Comparable Official snapshot | {payload.get('loss_funnel', {}).get('comparable_official', 0)} |",
        f"| Official candidate found | {payload.get('loss_funnel', {}).get('official_candidate_found', 0)} |",
        f"| Exact identity matched | {payload.get('loss_funnel', {}).get('exact_identity_matched', 0)} |",
    ]
    loss_labels = {
        "unsupported_company": "Unsupported company (add company)",
        "discovery_miss": "Official discovery miss (improve scraper)",
        "identity_mismatch": "Identity or alias mismatch (verify identifiers)",
        "source_timing": "Source newer than Official run (refresh)",
        "unverified_snapshot": "Official run absent, stale, failed, or partial (verify run)",
        "unclassifiable": "Missing company (repair source metadata)",
    }
    for reason, label in loss_labels.items():
        lines.append(f"| {label} | {payload.get('loss_funnel', {}).get('losses', {}).get(reason, 0)} |")
    lines.extend(["", "### Largest contributors by loss", "",
                  "| Loss | Companies (records) |", "|---|---|"])
    for reason, label in loss_labels.items():
        leaders = payload.get("top_loss_companies", {}).get(reason, [])[:5]
        text = ", ".join(f"{str(item['company']).replace('|', '/')} ({item['count']})" for item in leaders) or "-"
        lines.append(f"| {label} | {text} |")
    lines.extend([
        "", f"- AI identity evidence: {payload.get('identity_ai', {}).get('cases', 0)} candidate cases; "
        f"{payload.get('identity_ai', {}).get('api_requests', 0)} batched request(s). "
        "AI alone never suppresses a posting.",
        "- AI errors: " + ("; ".join(payload.get("identity_ai", {}).get("errors", [])) or "none"),
        "",
        "## Company coverage",
        "",
        "| Company | Manual state | Adapter | Board / Sync | In scope | Exact | Ambiguous | ID absent | No candidate | Pending | Unsupported | Exact rate | Presence |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for company in payload.get("companies", []):
        exact_ratio = company.get("coverage_ratio")
        presence_ratio = company.get("official_presence_ratio")
        lines.append(
            f"| {company['name']} | {company['manual_status']} | {company['adapter']} | "
            f"{company['board_jobs']} / {company['syncareer_jobs']} | "
            f"{company['in_scope']} | {company['exact_covered']} | {company['ambiguous_covered']} | "
            f"{company['identity_unmatched']} | {company['official_gaps']} | {company['pending_refresh']} | {company['unsupported']} | "
            f"{'-' if exact_ratio is None else f'{exact_ratio:.0%}'} | "
            f"{'-' if presence_ratio is None else f'{presence_ratio:.0%}'} |"
        )
    unsupported = [company for company in payload.get("companies", []) if company.get("adapter") == "skip"]
    lines.extend(["", f"## Expected unsupported / link-only sources ({len(unsupported)})", ""])
    lines.extend(f"- {company['name']}" for company in unsupported)
    unresolved = [r for r in payload.get("records", []) if r.get("coverage_status") in {"official_ambiguous", "official_identity_unmatched"}]
    lines.extend([
        "", f"## Identity evidence requiring review ({len(unresolved)})", "",
        f"- `official_ambiguous` ({payload.get('counts', {}).get('official_ambiguous', 0)}): Official candidates exist, but title/location does not identify one requisition.",
        f"- `official_identity_unmatched` ({payload.get('counts', {}).get('official_identity_unmatched', 0)}): a stable employer-side ID is absent from the Official snapshot; this is stronger adapter/snapshot-gap evidence.",
        "", "| Status | Pipeline | Company | Title | Location | Stable IDs | Candidate IDs | AI evidence | Link |",
        "|---|---|---|---|---|---|---|---|---|",
    ])
    for row in unresolved:
        link_url = row.get("application_url") or row.get("official_url") or row.get("source_url") or row.get("job_url") or ""
        link = f"[open]({link_url})" if link_url else "-"
        lines.append(
            f"| {row.get('coverage_status')} | {row.get('source_pipeline')} | "
            f"{str(row.get('company') or '').replace('|','/')} | {str(row.get('title') or '').replace('|','/')[:90]} | "
            f"{str(row.get('location') or '').replace('|','/')} | {', '.join(row.get('coverage_stable_ids') or []) or '-'} | "
            f"{', '.join(row.get('coverage_candidate_ids') or []) or '-'} | "
            f"{(row.get('identity_ai') or {}).get('decision') or '-'} "
            f"{(row.get('identity_ai') or {}).get('confidence') if (row.get('identity_ai') or {}).get('confidence') is not None else ''} | {link} |"
        )
    gaps = [r for r in payload.get("records", []) if r.get("coverage_status") in {"official_gap", "pending_official_refresh"}]
    lines.extend([
        "",
        f"## Official snapshot misses ({payload.get('counts', {}).get('official_gap', 0)}) and timing-pending records "
        f"({payload.get('counts', {}).get('pending_official_refresh', 0)})",
        "", "| Status | Pipeline | Company | Title | Location | Link |", "|---|---|---|---|---|---|",
    ])
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
    import board_pipeline as board
    board.load_env_file(BASE_DIR / ".env")
    payload = build_coverage_payload(use_ai=True)
    write_coverage_outputs(payload)
    if args.json:
        print(json.dumps({"counts": payload["counts"], "companies": payload["companies"]}, indent=2))
    else:
        print(f"Wrote {COVERAGE_JSON_PATH} and {COVERAGE_MD_PATH}")


if __name__ == "__main__":
    main()
