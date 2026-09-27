"""Bounded, post-discovery detail retrieval for metadata-only Official jobs."""

from __future__ import annotations

import hashlib
import json
import time
from collections import Counter, defaultdict, deque
from typing import Any, Callable, Dict, List, Optional, Tuple
from urllib.parse import urlsplit

from bs4 import BeautifulSoup

import compact_ai
from ..schema import adopt_better_posted_date, normalize_job_url, normalize_title_key, parse_datetime
from .http import html_to_text, http_get, make_session
from .incremental import DetailCache, annotate_detail


THIN_JD_CHARS = 200
DETAIL_REQUEST_CAP = 150
PRIORITY_COMPANIES = ("Meta", "Disney", "Netflix", "Equinix")


def _posting(html: str) -> Dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")
    for node in soup.select('script[type="application/ld+json"]'):
        try:
            value = json.loads(node.string or node.get_text() or "{}")
        except (TypeError, ValueError):
            continue
        values = value if isinstance(value, list) else [value]
        for item in values:
            if not isinstance(item, dict):
                continue
            candidates = [item, *(item.get("@graph") or [])]
            for candidate in candidates:
                if isinstance(candidate, dict) and "JobPosting" in str(candidate.get("@type") or ""):
                    return candidate
    return {}


def extract_detail(html: str, company: str) -> Tuple[str, str, str, str]:
    """Return JD, title, posted date, and employer-side identifier."""
    posting = _posting(html)
    description = html_to_text(str(posting.get("description") or ""))
    if len(description) < THIN_JD_CHARS:
        soup = BeautifulSoup(html, "html.parser")
        selectors = (
            ".job-description", "[itemprop='description']", "#job-description",
            ".job-details", ".job-posting",
        )
        for selector in selectors:
            node = soup.select_one(selector)
            if node:
                text = html_to_text(str(node))
                if len(text) > len(description):
                    description = text
    identifier = posting.get("identifier") or ""
    if isinstance(identifier, dict):
        identifier = identifier.get("value") or identifier.get("name") or ""
    return (description, str(posting.get("title") or ""),
            str(posting.get("datePosted") or ""), str(identifier))


def _same_job(job: Dict[str, Any], response_url: str, title: str, identifier: str) -> bool:
    expected_url = str(job.get("official_url") or "")
    expected_id = str(job.get("job_id") or "")
    if not expected_url or urlsplit(response_url).hostname != urlsplit(expected_url).hostname:
        return False
    if identifier and expected_id and identifier.lower() != expected_id.lower():
        # Some portals expose a second display ID; the canonical URL can still
        # establish identity if its employer-side path has not changed.
        if normalize_job_url(response_url) != normalize_job_url(expected_url):
            return False
    if title and normalize_title_key(title) != normalize_title_key(str(job.get("title") or "")):
        return False
    if normalize_job_url(response_url) == normalize_job_url(expected_url):
        return True
    return bool(expected_id and expected_id.lower() in urlsplit(response_url).path.lower())


def _triage_hash(job: Dict[str, Any]) -> str:
    fields = [str(job.get(key) or "") for key in ("company", "job_id", "title", "location")]
    return hashlib.sha256(json.dumps(fields, separators=(",", ":")).encode()).hexdigest()


def recover(
    results: List[Dict[str, Any]], previous_jobs: List[Dict[str, Any]],
    candidate_kind: Callable[[Dict[str, Any]], str], *, api_key: str = "",
    request_cap: int = DETAIL_REQUEST_CAP,
) -> Dict[str, Any]:
    """Enrich eligible jobs in place; no model decision changes scoring."""
    started = time.monotonic()
    cache = DetailCache(previous_jobs)
    pending: List[Tuple[Dict[str, Any], Dict[str, Any], str, Any]] = []
    ai_cases: Dict[str, Dict[str, Any]] = {}
    metrics: Counter = Counter()
    per_company: Dict[str, Counter] = defaultdict(Counter)
    for result in results:
        for job in result.get("jobs") or []:
            kind = candidate_kind(job)
            if kind == "skip":
                if len(str(job.get("description") or "").strip()) < THIN_JD_CHARS:
                    per_company[str(job.get("company") or "")]["deterministic_skip"] += 1
                continue
            company = str(job.get("company") or "")
            if len(str(job.get("description") or "").strip()) >= THIN_JD_CHARS:
                job["jd_recovery_eligible"] = True
                per_company[company]["eligible"] += 1
                continue
            decision = cache.decide(
                company=company, job_id=str(job.get("job_id") or ""),
                url=str(job.get("official_url") or ""), title=str(job.get("title") or ""),
                posted_date=job.get("posted_date"), updated_date=job.get("updated_date"),
            )
            cached = decision.cached or {}
            if len(str(cached.get("description") or "").strip()) >= THIN_JD_CHARS:
                job["description"] = cached["description"]
                job["jd_recovery_source"] = "cache"
                annotate_detail(job, decision, detail_fetched=False, listing_title=str(job.get("title") or ""),
                                listing_posted_date=str(job.get("posted_date") or ""),
                                listing_updated_date=str(job.get("updated_date") or ""))
                per_company[company]["cache_reused"] += 1
                metrics["cache_reused"] += 1
                if not decision.should_fetch:
                    job["jd_recovery_eligible"] = True
                    per_company[company]["eligible"] += 1
                    continue
            if kind == "borderline":
                digest = _triage_hash(job)
                job["detail_triage_hash"] = digest
                if cached.get("detail_triage_hash") == digest and cached.get("detail_triage_decision") in {"recover", "skip"}:
                    job["detail_triage_decision"] = cached["detail_triage_decision"]
                    job["detail_triage_priority"] = cached.get("detail_triage_priority") or "medium"
                elif digest not in ai_cases:
                    ai_cases[digest] = {
                        "case_id": digest, "company": company[:80],
                        "job_id": str(job.get("job_id") or "")[:80],
                        "title": str(job.get("title") or "")[:120],
                        "location": str(job.get("location") or "")[:100],
                        "date": str(job.get("posted_date") or "")[:30],
                    }
            pending.append((result, job, kind, decision))
    answers: Dict[str, Dict[str, Any]] = {}
    errors: List[str] = []
    if api_key and ai_cases:
        try:
            answers = compact_ai.decide(
                task="detail_retrieval", cases=ai_cases.values(), choices=("recover", "skip"), api_key=api_key,
            )
            metrics["ai_requests"] = (len(ai_cases) + compact_ai.BATCH_SIZE - 1) // compact_ai.BATCH_SIZE
        except Exception as exc:  # network or malformed model output must not block discovery
            errors.append(f"AI triage: {type(exc).__name__}: {exc}")
    queues: Dict[str, List[Tuple[Dict[str, Any], Dict[str, Any], Any]]] = defaultdict(list)
    for result, job, kind, decision in pending:
        company = str(job.get("company") or "")
        if kind == "borderline":
            answer = answers.get(str(job.get("detail_triage_hash") or ""), {})
            if answer:
                job["detail_triage_decision"] = answer["decision"]
                job["detail_triage_priority"] = answer.get("priority") or "medium"
                job["detail_triage_confidence"] = answer.get("confidence")
            confidence = job.get("detail_triage_confidence")
            if job.get("detail_triage_decision") == "skip" and float(1 if confidence is None else confidence) >= 0.8:
                per_company[company]["ai_skip"] += 1
                continue
            per_company[company]["ai_recover"] += 1
        job["jd_recovery_eligible"] = True
        per_company[company]["eligible"] += 1
        queues[company].append((result, job, decision))
    priority = {"high": 0, "medium": 1, "low": 2}
    def sort_date(job: Dict[str, Any]) -> float:
        value = parse_datetime(job.get("posted_date") or job.get("first_seen"))
        return -(value.timestamp() if value else 0)
    for company, rows in queues.items():
        rows.sort(key=lambda item: (
            bool(item[1].get("description")),
            priority.get(str(item[1].get("detail_triage_priority") or "high"), 1),
            sort_date(item[1]),
        ))
    order = [company for company in PRIORITY_COMPANIES if company in queues]
    order.extend(sorted(company for company in queues if company not in order))
    active = deque(order)
    sessions = {company: make_session() for company in order}
    try:
        while active and metrics["detail_requests"] < request_cap:
            company = active.popleft()
            result, job, decision = queues[company].pop(0)
            if queues[company]:
                active.append(company)
            url = str(job.get("official_url") or "")
            if not url.startswith("https://"):
                per_company[company]["invalid_url"] += 1
                continue
            begun = time.monotonic()
            metrics["detail_requests"] += 1
            per_company[company]["detail_requests"] += 1
            result["detail_fetches"] = int(result.get("detail_fetches") or 0) + 1
            try:
                response = http_get(sessions[company], url, label=f"{company} career detail")
                description, title, posted, identifier = extract_detail(response.text, company)
                if len(description.strip()) < THIN_JD_CHARS:
                    raise ValueError("thin_detail")
                if not _same_job(job, response.url, title, identifier):
                    raise ValueError("identity_mismatch")
                job["description"] = description
                job["jd_recovery_source"] = "detail"
                if posted:
                    adopt_better_posted_date(job, {"posted_date": posted, "date_confidence": "high"})
                annotate_detail(job, decision, detail_fetched=True, listing_title=str(job.get("title") or ""),
                                listing_posted_date=str(job.get("posted_date") or ""),
                                listing_updated_date=str(job.get("updated_date") or ""))
                per_company[company]["detail_success"] += 1
                metrics["detail_success"] += 1
            except Exception as exc:  # keep cached description if a detail fetch fails
                reason = f"{type(exc).__name__}: {exc}"
                job["detail_failure_reason"] = reason[:160]
                per_company[company]["detail_failure"] += 1
                if len(str((decision.cached or {}).get("description") or "").strip()) >= THIN_JD_CHARS:
                    job["description"] = decision.cached["description"]
                    job["jd_recovery_source"] = "cache"
                    per_company[company]["last_good_reused"] += 1
            result["http_requests"] = int(result.get("http_requests") or 0) + 1
            result["http_request_seconds"] = round(float(result.get("http_request_seconds") or 0) + time.monotonic() - begun, 3)
            result["elapsed_seconds"] = round(float(result.get("elapsed_seconds") or 0) + time.monotonic() - begun, 3)
    finally:
        for session in sessions.values():
            session.close()
    for company, rows in queues.items():
        per_company[company]["budget_deferred"] += len(rows)
    for result in results:
        company = str(result.get("company") or "")
        counts = per_company[company]
        counts["usable_jd"] = sum(
            len(str(job.get("description") or "").strip()) >= THIN_JD_CHARS
            for job in result.get("jobs") or [] if job.get("jd_recovery_eligible")
        )
        result["jd_recovery"] = dict(counts)
        result["detail_cache_reused"] = int(result.get("detail_cache_reused") or 0) + counts["cache_reused"]
        result["detail_prefilter_skipped"] = int(result.get("detail_prefilter_skipped") or 0) + counts["deterministic_skip"] + counts["ai_skip"]
        result["detail_cache_status_counts"] = dict(Counter(
            str(job.get("detail_cache_status") or "") for job in result.get("jobs") or [] if job.get("detail_cache_status")
        ))
    return {
        **dict(metrics), "eligible": sum(c["eligible"] for c in per_company.values()),
        "usable_jd": sum(c["usable_jd"] for c in per_company.values()),
        "budget_deferred": sum(c["budget_deferred"] for c in per_company.values()),
        "ai_skip": sum(c["ai_skip"] for c in per_company.values()),
        "deterministic_skip": sum(c["deterministic_skip"] for c in per_company.values()),
        "elapsed_seconds": round(time.monotonic() - started, 3), "errors": errors,
        "per_company": {company: dict(counts) for company, counts in per_company.items()},
    }
