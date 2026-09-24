#!/usr/bin/env python3
"""LinkedIn guest job-search adapter. LOCAL USE ONLY.

Uses the public, unauthenticated guest endpoints for search cards and bounded
job-detail enrichment. This is best-effort: on login wall / captcha / 403 /
429 it preserves the card results so the caller can keep the last good
snapshot behavior without turning a detail-block into a source outage.

Do NOT run this from GitHub Actions (datacenter IPs get blocked fast). It is
driven locally by launchd via ``local_sources.py``.

Filters (per plan):
  - f_TPR=r86400  : posted in the last 24h (wide window; pipeline re-sorts)
  - f_E=2,3       : entry + associate (captures realistic ~0-3 YOE / I-II)
  - geoId=103644278 + location=United States
  - keywords      : rotated across several engineering titles
"""

from __future__ import annotations

import time
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List
from urllib.parse import parse_qs, unquote, urljoin, urlsplit

import requests
from bs4 import BeautifulSoup

from .schema import (
    SourceUnavailable,
    is_us_location,
    make_job,
    normalize_space,
)
from .local_search import source_queries, query_stat

GUEST_SEARCH_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
GUEST_DETAIL_URL = "https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
US_GEO_ID = "103644278"
DEFAULT_KEYWORDS = [query for _group, query, _budget in source_queries("linkedin")]
EXPERIENCE_LEVEL_FILTER = "2,3"
PAGE_SIZE = 10
REQUEST_TIMEOUT = 25
POLITE_SLEEP_SECONDS = 1.2
DETAIL_CACHE_DAYS = 14
DETAIL_SLEEP_SECONDS = 0.4
DETAIL_RETRY_HOURS = 24
SEARCH_PAGE_LIMIT = 12
SEARCH_QUERY_PAGE_LIMIT = 2


def _make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml",
        }
    )
    return session


def _check_blocked(resp: requests.Response) -> None:
    if resp.status_code in (401, 403, 429):
        raise SourceUnavailable(f"blocked with HTTP {resp.status_code}")
    if resp.status_code == 999:  # LinkedIn's anti-bot status
        raise SourceUnavailable("blocked with HTTP 999 (LinkedIn anti-bot)")
    if resp.status_code >= 400:
        raise SourceUnavailable(f"HTTP {resp.status_code}")
    lowered = resp.text[:2000].lower()
    if "authwall" in lowered or "sign in to continue" in lowered or "captcha" in lowered:
        raise SourceUnavailable("login/captcha wall detected")


def _parse_cards(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("div", class_="base-card")
    rows: List[Dict[str, str]] = []
    for card in cards:
        title_tag = card.find("h3")
        company_tag = card.find("h4")
        loc_tag = card.find("span", class_="job-search-card__location")
        link_tag = card.find("a", class_="base-card__full-link") or card.find("a")
        time_tag = card.find("time")
        urn = card.get("data-entity-urn") or ""
        job_id = urn.split(":")[-1] if urn else ""
        location = normalize_space(loc_tag.get_text() if loc_tag else "")
        href = (link_tag.get("href") if link_tag else "") or ""
        # Strip tracking query string.
        clean_url = href.split("?")[0]
        rows.append(
            make_job(
                source="linkedin",
                company=normalize_space(company_tag.get_text() if company_tag else ""),
                title=normalize_space(title_tag.get_text() if title_tag else ""),
                location=location,
                job_id=normalize_space(job_id),
                posted_date=(time_tag.get("datetime") if time_tag else "") or "",
                aggregator_posted_date=(time_tag.get("datetime") if time_tag else "") or "",
                date_confidence="low",  # LinkedIn shows reposts as fresh
                source_url=clean_url,
                official_url="",
            )
        )
    return rows


def _external_apply_url(soup: BeautifulSoup) -> str:
    """Return an off-site Apply URL only when the guest detail actually exposes one.

    LinkedIn commonly withholds off-site apply destinations when logged out, so
    absence is expected. Restrict extraction to apply-labelled anchors to avoid
    accidentally treating the employer's LinkedIn company page as canonical.
    """
    for anchor in soup.find_all("a", href=True):
        label = normalize_space(anchor.get_text(" ")).lower()
        classes = " ".join(anchor.get("class") or []).lower()
        if "apply" not in label and "apply" not in classes:
            continue
        href = urljoin("https://www.linkedin.com", str(anchor.get("href") or ""))
        parsed = urlsplit(href)
        candidate = href
        if "linkedin." in parsed.netloc.lower():
            query = parse_qs(parsed.query)
            redirected = ""
            for key in ("url", "target", "redirect", "dest"):
                for value in query.get(key, []):
                    decoded = unquote(value)
                    if urlsplit(decoded).scheme in {"http", "https"}:
                        redirected = decoded
                        break
                if redirected:
                    break
            candidate = redirected
        host = urlsplit(candidate).netloc.lower() if candidate else ""
        if host and "linkedin." not in host:
            return candidate
    return ""


def _parse_detail(html: str) -> Dict[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    description_node = (
        soup.select_one(".show-more-less-html__markup")
        or soup.select_one(".description__text")
        or soup.select_one(".show-more-less-html")
    )
    description = normalize_space(description_node.get_text(" ") if description_node else "")
    return {
        "description": description,
        "application_url": _external_apply_url(soup),
    }


def _scrapling_fetch_html(url: str) -> tuple[str, int | None, str]:
    """Return body, status, and error; a missing status means no request occurred."""
    try:
        from scrapling.fetchers import Fetcher
    except ImportError:
        return "", None, "Scrapling is not installed"
    try:
        response = Fetcher.get(
            url,
            impersonate="chrome",
            stealthy_headers=True,
            retries=0,
            timeout=REQUEST_TIMEOUT,
        )
    except Exception:  # noqa: BLE001 - optional fallback must not fail collection
        return "", 0, "scrapling_fetch_failed"
    status = int(getattr(response, "status", 0) or 0)
    if status != 200:
        return "", status, f"scrapling_http_{status}"
    body = getattr(response, "body", b"")
    html = body.decode("utf-8", errors="replace") if isinstance(body, bytes) else str(body or "")
    return html, status, ""


def _fresh_cached_detail(previous: Dict[str, Any], row: Dict[str, Any], now: datetime, min_description_chars: int = 1) -> bool:
    if len(str(previous.get("description") or "").strip()) < min_description_chars:
        return False
    if normalize_space(previous.get("title")) != normalize_space(row.get("title")):
        return False
    try:
        fetched = datetime.fromisoformat(
            str(previous.get("linkedin_detail_fetched_at") or "").replace("Z", "+00:00")
        )
        if fetched.tzinfo is None:
            fetched = fetched.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return False
    return now - fetched.astimezone(timezone.utc) <= timedelta(days=DETAIL_CACHE_DAYS)


def enrich_details(
    rows: List[Dict[str, Any]],
    *,
    previous_jobs: List[Dict[str, Any]] | None = None,
    session: requests.Session | None = None,
    allow_requests: bool = True,
    request_limit: int | None = None,
    min_description_chars: int = 1,
    cooldown: bool = False,
    probe: bool = False,
) -> Dict[str, Any]:
    """Hydrate every unresolved LinkedIn row with the logged-out full JD.

    Previous snapshot details are reused for 14 days when title/job_id are
    unchanged. A detail-endpoint block stops only enrichment; it does not
    invalidate already-collected search cards.

    ``allow_requests=False`` serves a rate-limited run: cached details only.
    Each eligible job gets one transport attempt; a later retry may use
    Scrapling after an ordinary non-429 HTTP failure. During ``cooldown``,
    unresolved cards are intentionally deferred; ``probe`` permits one fresh
    HTTP attempt after the pause even if that job's retry timer is still active.
    """
    session = session or _make_session()
    now = datetime.now(timezone.utc)
    previous_by_id = {
        str(job.get("job_id") or ""): job
        for job in (previous_jobs or [])
        if job.get("job_id")
    }
    stats: Dict[str, Any] = {
        "eligible": len(rows),
        "cache_reused": 0,
        "requests": 0,
        "responses": 0,
        "request_limit": request_limit,
        "budget_deferred": 0,
        "budget_exhausted": False,
        "retry_deferred": 0,
        "retry_attempts": 0,
        "exact_official": 0,
        "official_deferred": 0,
        "rate_limited": False,
        "jds_resolved": 0,
        "external_apply_urls": 0,
        "failed": 0,
        "detail_jds_fetched": 0,
        "intentional_skips": 0,
        "blocked": "",
        "scrapling_requests": 0,
        "scrapling_jds_resolved": 0,
        "scrapling_error": "",
        "remaining_no_jd": 0,
        "failure_reasons": {},
    }
    pending: List[Dict[str, Any]] = []

    for row in rows:
        if len(str(row.get("description") or "").strip()) >= min_description_chars:
            stats["jds_resolved"] += 1
            if row.get("application_url"):
                stats["external_apply_urls"] += 1
            continue
        prior = previous_by_id.get(str(row.get("job_id") or ""))
        if prior and _fresh_cached_detail(prior, row, now, min_description_chars):
            row["description"] = prior.get("description", "")
            if prior.get("application_url"):
                row["application_url"] = prior["application_url"]
            row["linkedin_detail_fetched_at"] = prior.get("linkedin_detail_fetched_at", "")
            row["linkedin_detail_resolved"] = True
            row["enrichment_method"] = "linkedin_cache"
            row["enrichment_status"] = "resolved"
            stats["cache_reused"] += 1
            stats["jds_resolved"] += 1
            if row.get("application_url"):
                stats["external_apply_urls"] += 1
            continue
        if row.pop("_linkedin_official_defer", False):
            stats["exact_official"] += 1
            stats["official_deferred"] += 1
            row.pop("_linkedin_official_url", None)
            row["enrichment_status"] = "unresolved"
            row["enrichment_failure_reason"] = "official_detail_deferred"
            continue
        if row.pop("_linkedin_official_url", None):
            stats["exact_official"] += 1
        if row.get("job_id"):
            if cooldown:
                pending.append(row)
                continue
            attempted_at = str((prior or {}).get("linkedin_detail_attempted_at") or "")
            try:
                attempted = datetime.fromisoformat(attempted_at.replace("Z", "+00:00"))
                if attempted.tzinfo is None:
                    attempted = attempted.replace(tzinfo=timezone.utc)
                deferred = now - attempted.astimezone(timezone.utc) < timedelta(hours=DETAIL_RETRY_HOURS)
            except (TypeError, ValueError):
                deferred = False
            if deferred and not probe:
                row["linkedin_detail_attempted_at"] = attempted_at
                row["enrichment_status"] = "unresolved"
                row["enrichment_failure_reason"] = str(
                    (prior or {}).get("enrichment_failure_reason") or "linkedin_detail_deferred"
                )
                stats["retry_deferred"] += 1
            else:
                pending.append(row)
        else:
            row["enrichment_status"] = "unresolved"
            row["enrichment_failure_reason"] = "missing_job_id"

    if not allow_requests:
        stats["blocked"] = "" if cooldown else "rate_limited_no_further_requests"
        stats["intentional_skips"] = len(pending) if cooldown else 0
        for row in pending:
            row["enrichment_status"] = "deferred" if cooldown else "unresolved"
            if cooldown:
                row["enrichment_deferred_reason"] = "linkedin_detail_cooldown"
                row.pop("enrichment_failure_reason", None)
            else:
                row["enrichment_failure_reason"] = "linkedin_rate_limited"
        pending = []

    for index, row in enumerate(pending):
        if request_limit is not None and stats["requests"] >= request_limit:
            stats["budget_exhausted"] = True
            stats["budget_deferred"] = len(pending) - index
            break
        prior = previous_by_id.get(str(row.get("job_id") or "")) or {}
        prior_reason = str(prior.get("enrichment_failure_reason") or "")
        use_scrapling = not probe and prior_reason.startswith("linkedin_http_") and prior_reason not in {
            "linkedin_http_429", "linkedin_http_network_error",
        }
        url = GUEST_DETAIL_URL.format(job_id=row["job_id"])
        if use_scrapling:
            html, status, error = _scrapling_fetch_html(url)
            if status is None:
                stats["scrapling_error"] = error
                row["enrichment_status"] = "unresolved"
                row["enrichment_failure_reason"] = "scrapling_unavailable"
                break
            stats["requests"] += 1
            stats["scrapling_requests"] += 1
            stats["retry_attempts"] += 1
            row["linkedin_detail_attempted_at"] = now.isoformat()
            if status:
                stats["responses"] += 1
            if status == 429:
                stats["blocked"] = "blocked with HTTP 429"
                stats["rate_limited"] = True
                row["enrichment_status"] = "unresolved"
                row["enrichment_failure_reason"] = "scrapling_http_429"
                break
            if not html:
                stats["failed"] += 1
                row["enrichment_status"] = "unresolved"
                row["enrichment_failure_reason"] = error or "scrapling_fetch_failed"
                time.sleep(DETAIL_SLEEP_SECONDS)
                continue
            detail = _parse_detail(html)
            method = "scrapling_fetcher"
        else:
            stats["requests"] += 1
            row["linkedin_detail_attempted_at"] = now.isoformat()
            try:
                response = session.get(url, timeout=REQUEST_TIMEOUT)
            except requests.RequestException:
                stats["failed"] += 1
                row["enrichment_status"] = "unresolved"
                row["enrichment_failure_reason"] = "linkedin_http_network_error"
                time.sleep(DETAIL_SLEEP_SECONDS)
                continue
            stats["responses"] += 1
            try:
                _check_blocked(response)
            except SourceUnavailable as exc:
                row["enrichment_status"] = "unresolved"
                row["enrichment_failure_reason"] = f"linkedin_http_{response.status_code}"
                if response.status_code == 429:
                    stats["rate_limited"] = True
                if response.status_code in (401, 403, 429, 999) or response.status_code < 400:
                    stats["blocked"] = str(exc)
                    break
                stats["failed"] += 1
                time.sleep(DETAIL_SLEEP_SECONDS)
                continue
            detail = _parse_detail(response.text)
            method = "linkedin_http"

        row["linkedin_detail_fetched_at"] = now.isoformat()
        if len(str(detail["description"] or "").strip()) >= min_description_chars:
            row["description"] = detail["description"]
            row["linkedin_detail_resolved"] = True
            row["enrichment_method"] = method
            row["enrichment_status"] = "resolved"
            row.pop("enrichment_failure_reason", None)
            stats["jds_resolved"] += 1
            stats["detail_jds_fetched"] += 1
            if use_scrapling:
                stats["scrapling_jds_resolved"] += 1
        else:
            row["enrichment_status"] = "unresolved"
            row["enrichment_failure_reason"] = f"{method}_no_jd"
        if detail["application_url"]:
            row["application_url"] = detail["application_url"]
            stats["external_apply_urls"] += 1
        time.sleep(DETAIL_SLEEP_SECONDS)

    for row in rows:
        row.pop("_linkedin_official_defer", None)
        row.pop("_linkedin_official_url", None)

    unresolved = [row for row in rows if not row.get("description")]
    reasons: Dict[str, int] = {}
    for row in unresolved:
        if row.get("enrichment_deferred_reason") == "linkedin_detail_cooldown":
            continue
        reason = str(row.get("enrichment_failure_reason") or "no_description")
        reasons[reason] = reasons.get(reason, 0) + 1
    stats["remaining_no_jd"] = len(unresolved)
    stats["failure_reasons"] = reasons
    return stats


def scrape(
    keywords: List[str] | None = None,
    session: requests.Session | None = None,
    *,
    query_cursor: int = 0,
    page_limit: int = SEARCH_PAGE_LIMIT,
) -> Dict[str, Any]:
    """Return LinkedIn job rows. Raises SourceUnavailable on anti-bot/network."""
    session = session or _make_session()
    specs = list(source_queries("linkedin"))
    if keywords:
        wanted = set(keywords)
        specs = [spec for spec in specs if spec[1] in wanted]
    if specs:
        offset = query_cursor % len(specs)
        specs = specs[offset:] + specs[:offset]
    seen: set[str] = set()
    by_key: Dict[str, Dict[str, str]] = {}
    rows: List[Dict[str, str]] = []
    stats: List[Dict[str, object]] = []
    requests_made = 0
    responses = 0
    pages_fetched = 0
    for index, (group, keyword, page_budget) in enumerate(specs):
        stat = query_stat(keyword, group, min(page_budget, SEARCH_QUERY_PAGE_LIMIT))
        started = time.monotonic()
        query_seen: set[str] = set()
        for page in range(min(page_budget, SEARCH_QUERY_PAGE_LIMIT)):
            if requests_made >= page_limit:
                stat["stop_reason"] = "global_page_budget"
                break
            params = {
                "keywords": keyword,
                "location": "United States",
                "geoId": US_GEO_ID,
                "f_TPR": "r86400",
                "f_E": EXPERIENCE_LEVEL_FILTER,
                "start": page * PAGE_SIZE,
            }
            try:
                requests_made += 1
                resp = session.get(GUEST_SEARCH_URL, params=params, timeout=REQUEST_TIMEOUT)
            except requests.RequestException as exc:
                stat["stop_reason"] = "network_error"
                stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
                stats.append(stat)
                stats.extend(_unattempted(specs[index + 1:], "source_unavailable"))
                return {
                    "status": "blocked", "reason": f"network error: {exc}", "jobs": rows,
                    "query_stats": stats, "http_status": 0,
                    "queries_completed": index, "queries_total": len(specs),
                    "requests": requests_made, "responses": responses, "pages_fetched": pages_fetched,
                }
            try:
                responses += 1
                _check_blocked(resp)
            except SourceUnavailable as exc:
                stat["stop_reason"] = f"blocked_http_{resp.status_code}"
                stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
                stats.append(stat)
                stats.extend(_unattempted(specs[index + 1:], "source_unavailable"))
                return {
                    "status": "blocked", "reason": str(exc), "jobs": rows,
                    "query_stats": stats, "http_status": resp.status_code,
                    "queries_completed": index, "queries_total": len(specs),
                    "requests": requests_made, "responses": responses, "pages_fetched": pages_fetched,
                }
            stat["pages_fetched"] = int(stat["pages_fetched"]) + 1
            pages_fetched += 1
            page_rows = _parse_cards(resp.text)
            stat["raw_jobs"] = int(stat["raw_jobs"]) + len(page_rows)
            if not page_rows:
                stat["stop_reason"] = "empty_page"
                break
            added = 0
            for row in page_rows:
                key = row.get("job_id") or row.get("source_url")
                if key:
                    query_seen.add(key)
                if key and key in seen:
                    prior = by_key.get(key)
                    if prior:
                        prior["discovery_queries"]["linkedin"] = list(dict.fromkeys([
                            *prior["discovery_queries"]["linkedin"], keyword,
                        ]))
                    continue
                if key:
                    seen.add(key)
                # US filter; keep unknown locations (LinkedIn sometimes omits).
                if row["location"] and not is_us_location(row["location"]):
                    continue
                row["discovery_queries"] = {"linkedin": [keyword]}
                rows.append(row)
                if key:
                    by_key[key] = row
                added += 1
            if added <= 1:
                stat["stop_reason"] = "low_unique_yield"
                break
            time.sleep(POLITE_SLEEP_SECONDS)
        stat["unique_jobs"] = len(query_seen)
        stat["unique_contribution"] = sum(
            1 for row in rows if (row.get("discovery_queries") or {}).get("linkedin", [None])[0] == keyword
        )
        stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
        stats.append(stat)
        if requests_made >= page_limit:
            stats.extend(_unattempted(specs[index + 1:], "global_page_budget"))
            break
    return {
        "status": "ok", "jobs": rows, "query_stats": stats,
        "queries_completed": sum(bool(stat["pages_fetched"]) for stat in stats),
        "queries_total": len(specs), "requests": requests_made,
        "responses": responses, "pages_fetched": pages_fetched,
    }


def _unattempted(specs: List[tuple[str, str, int]], reason: str) -> List[Dict[str, object]]:
    out = []
    for group, query, budget in specs:
        stat = query_stat(query, group, budget)
        stat["stop_reason"] = reason
        out.append(stat)
    return out
