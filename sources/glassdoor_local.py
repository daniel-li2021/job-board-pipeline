#!/usr/bin/env python3
"""Glassdoor job-search adapter. LOCAL USE ONLY.

Parses Glassdoor's public search results HTML (job cards + JSON-LD). This is
best-effort: on captcha / security check / 403 / 429 it raises
``SourceUnavailable`` so the caller keeps the last good snapshot.

Do NOT run from GitHub Actions. Driven locally by launchd via
``local_sources.py``. Glassdoor's default result set is already recency-biased;
the pipeline re-sorts by first_seen / posted_date, so a wide window is fine.
"""

from __future__ import annotations

import re
import time
from typing import Any, Dict, List
from urllib.parse import urlencode, urlsplit

import requests
from bs4 import BeautifulSoup

from .schema import (
    SourceUnavailable,
    is_us_location,
    make_job,
    normalize_space,
)
from .local_search import source_queries, query_stat

REQUEST_TIMEOUT = 25
POLITE_SLEEP_SECONDS = 2.0
SEARCH_BASE_URL = "https://www.glassdoor.com/Job/jobs.htm"


def build_search_url(keyword: str, page: int) -> str:
    return SEARCH_BASE_URL + "?" + urlencode({
        "sc.keyword": keyword, "locT": "N", "locId": "1", "fromAge": "1", "p": page,
    })


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
    if resp.status_code >= 400:
        raise SourceUnavailable(f"HTTP {resp.status_code}")
    low = resp.text[:5000].lower()
    if "please verify you are a human" in low or "security check" in low or "px-captcha" in low:
        raise SourceUnavailable("captcha / security check")


def _parse_cards(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select('[data-test="jobListing"]')
    rows: List[Dict[str, str]] = []
    for card in cards:
        title_el = card.select_one('[data-test="job-title"]')
        loc_el = card.select_one('[data-test="emp-location"]')
        age_el = card.select_one('[data-test="job-age"]')
        emp_el = card.select_one('[class*="EmployerProfile_compactEmployerName"]')
        snip_el = card.select_one('[data-test="descSnippet"]')
        href = title_el.get("href", "") if title_el else ""
        clean_url = href.split("?")[0]
        m = re.search(r"jl=(\d+)", href)
        job_id = m.group(1) if m else ""
        row = make_job(
                source="glassdoor",
                company=normalize_space(emp_el.get_text() if emp_el else ""),
                title=normalize_space(title_el.get_text() if title_el else ""),
                location=normalize_space(loc_el.get_text() if loc_el else ""),
                job_id=job_id,
                posted_date=normalize_space(age_el.get_text() if age_el else ""),
                aggregator_posted_date=normalize_space(age_el.get_text() if age_el else ""),
                date_confidence="low",
                source_url=clean_url,
                official_url="",
                description=normalize_space(snip_el.get_text() if snip_el else ""),
            )
        if href and urlsplit(href).netloc and "glassdoor." not in urlsplit(href).netloc.lower():
            row["application_url"] = href
        rows.append(row)
    return rows


def scrape(
    session: requests.Session | None = None, keywords: List[str] | None = None,
) -> Dict[str, Any]:
    """Return Glassdoor job rows. Raises SourceUnavailable on captcha/network."""
    session = session or _make_session()
    seen: set[str] = set()
    by_key: Dict[str, Dict[str, str]] = {}
    rows: List[Dict[str, str]] = []
    stats: List[Dict[str, object]] = []
    specs = list(source_queries("glassdoor"))
    if keywords:
        wanted = set(keywords)
        specs = [spec for spec in specs if spec[1] in wanted]
    for index, (group, keyword, page_budget) in enumerate(specs):
        stat = query_stat(keyword, group, page_budget)
        started = time.monotonic()
        query_seen: set[str] = set()
        first_page_ids: set[str] = set()
        for page in range(1, page_budget + 1):
            try:
                resp = session.get(build_search_url(keyword, page), timeout=REQUEST_TIMEOUT)
            except requests.RequestException as exc:
                stat["stop_reason"] = "network_error"
                stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
                stats.append(stat)
                stats.extend(_unattempted(specs[index + 1:], "source_unavailable"))
                return {"status": "blocked", "reason": f"network error: {exc}", "jobs": rows, "query_stats": stats}
            try:
                _check_blocked(resp)
            except SourceUnavailable as exc:
                stat["stop_reason"] = f"blocked_http_{resp.status_code}"
                stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
                stats.append(stat)
                stats.extend(_unattempted(specs[index + 1:], "source_unavailable"))
                return {"status": "blocked", "reason": str(exc), "jobs": rows, "query_stats": stats}
            stat["pages_fetched"] = int(stat["pages_fetched"]) + 1
            page_rows = _parse_cards(resp.text)
            stat["raw_jobs"] = int(stat["raw_jobs"]) + len(page_rows)
            page_ids = {row.get("job_id") or row.get("source_url") for row in page_rows}
            page_ids.discard("")
            if not page_rows:
                stat["stop_reason"] = "empty_page"
                break
            if page == 2 and (not page_ids or page_ids == first_page_ids):
                stat["stop_reason"] = "pagination_unverified"
                break
            if page_ids and page_ids.issubset(query_seen):
                stat["stop_reason"] = "repeated_page"
                break
            if page == 1:
                first_page_ids = set(page_ids)
            query_seen.update(page_ids)
            added = 0
            for row in page_rows:
                key = row.get("job_id") or row.get("source_url")
                if key and key in seen:
                    prior = by_key.get(key)
                    if prior:
                        prior["discovery_queries"]["glassdoor"] = list(dict.fromkeys([
                            *prior["discovery_queries"]["glassdoor"], keyword,
                        ]))
                    continue
                if key:
                    seen.add(key)
                if row["location"] and not is_us_location(row["location"]):
                    continue
                row["discovery_queries"] = {"glassdoor": [keyword]}
                rows.append(row)
                if key:
                    by_key[key] = row
                added += 1
            if added == 0:
                stat["stop_reason"] = "no_new_jobs"
                break
            time.sleep(POLITE_SLEEP_SECONDS)
        stat["unique_jobs"] = len(query_seen)
        stat["unique_contribution"] = sum(
            1 for row in rows if (row.get("discovery_queries") or {}).get("glassdoor", [None])[0] == keyword
        )
        stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
        stats.append(stat)
        if stat["stop_reason"] == "pagination_unverified":
            stats.extend(_unattempted(specs[index + 1:], "source_unavailable"))
            return {
                "status": "pagination_unverified", "reason": "page 2 did not return distinct job IDs",
                "jobs": rows, "query_stats": stats,
            }
    return {"status": "ok", "jobs": rows, "query_stats": stats}


def _unattempted(specs: List[tuple[str, str, int]], reason: str) -> List[Dict[str, object]]:
    out = []
    for group, query, budget in specs:
        stat = query_stat(query, group, budget)
        stat["stop_reason"] = reason
        out.append(stat)
    return out
