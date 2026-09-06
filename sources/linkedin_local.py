#!/usr/bin/env python3
"""LinkedIn guest job-search adapter. LOCAL USE ONLY.

Uses the public, unauthenticated guest endpoint
``/jobs-guest/jobs/api/seeMoreJobPostings/search`` which returns HTML job
cards. This is best-effort: on login wall / captcha / 403 / 429 it raises
``SourceUnavailable`` so the caller keeps the last good snapshot instead of
overwriting it with nothing.

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
from typing import Any, Dict, List

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
US_GEO_ID = "103644278"
DEFAULT_KEYWORDS = [query for _group, query, _budget in source_queries("linkedin")]
EXPERIENCE_LEVEL_FILTER = "2,3"
PAGE_SIZE = 10
REQUEST_TIMEOUT = 25
POLITE_SLEEP_SECONDS = 1.2


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


def scrape(
    keywords: List[str] | None = None,
    session: requests.Session | None = None,
) -> Dict[str, Any]:
    """Return LinkedIn job rows. Raises SourceUnavailable on anti-bot/network."""
    session = session or _make_session()
    specs = list(source_queries("linkedin"))
    if keywords:
        wanted = set(keywords)
        specs = [spec for spec in specs if spec[1] in wanted]
    seen: set[str] = set()
    by_key: Dict[str, Dict[str, str]] = {}
    rows: List[Dict[str, str]] = []
    stats: List[Dict[str, object]] = []
    for index, (group, keyword, page_budget) in enumerate(specs):
        stat = query_stat(keyword, group, page_budget)
        started = time.monotonic()
        query_seen: set[str] = set()
        for page in range(page_budget):
            params = {
                "keywords": keyword,
                "location": "United States",
                "geoId": US_GEO_ID,
                "f_TPR": "r86400",
                "f_E": EXPERIENCE_LEVEL_FILTER,
                "start": page * PAGE_SIZE,
            }
            try:
                resp = session.get(GUEST_SEARCH_URL, params=params, timeout=REQUEST_TIMEOUT)
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
            if added == 0:
                stat["stop_reason"] = "no_new_jobs"
                break
            time.sleep(POLITE_SLEEP_SECONDS)
        stat["unique_jobs"] = len(query_seen)
        stat["unique_contribution"] = sum(
            1 for row in rows if (row.get("discovery_queries") or {}).get("linkedin", [None])[0] == keyword
        )
        stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
        stats.append(stat)
    return {"status": "ok", "jobs": rows, "query_stats": stats}


def _unattempted(specs: List[tuple[str, str, int]], reason: str) -> List[Dict[str, object]]:
    out = []
    for group, query, budget in specs:
        stat = query_stat(query, group, budget)
        stat["stop_reason"] = reason
        out.append(stat)
    return out
