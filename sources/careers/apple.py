"""Apple Jobs search scraper.

Method: HTTP GET of the server-rendered search page and parse
``window.__staticRouterHydrationData``. Pagination is ``&page=N`` (20/page).
The POST ``/api/v1/search`` endpoint exists but returned empty results without
the exact browser payload; HTML hydration is sufficient. Confirmed 2026-08-26:

https://jobs.apple.com/en-us/search?location=united-states-USA&page=1
https://jobs.apple.com/en-us/search?location=united-states-USA&team=apps-and-frameworks-SFTWR-AF&page=1
https://jobs.apple.com/en-us/search?search=software%20engineer&location=united-states-USA&sort=newest&page=1
"""

from __future__ import annotations

import json
import re
import time
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlencode

import requests

from ..schema import SourceUnavailable, make_job, normalize_space
from .http import keep_us_or_unknown, now_iso

SOURCE = "apple_official_careers"
COMPANY = "Apple"
SEARCH = "https://jobs.apple.com/en-us/search"
SLEEP_S = 0.35

DEFAULT_SEARCHES: List[Dict[str, str]] = [
    {"search": "software engineer", "location": "united-states-USA", "sort": "newest"},
    {"search": "machine learning engineer", "location": "united-states-USA", "sort": "newest"},
    {"location": "united-states-USA", "team": "apps-and-frameworks-SFTWR-AF"},
]


def search_url(filters: Dict[str, str], page: int = 1) -> str:
    params = dict(filters)
    params["page"] = str(page)
    return SEARCH + "?" + urlencode(params)


def _parse_hydration(html: str) -> Dict[str, Any]:
    match = re.search(
        r"window\.__staticRouterHydrationData = JSON\.parse\(\"(.+)\"\);\s*</script>",
        html,
        flags=re.S,
    )
    if not match:
        raise SourceUnavailable("Apple search page missing __staticRouterHydrationData")
    try:
        text = json.loads('"' + match.group(1) + '"')
        data = json.loads(text) if isinstance(text, str) else text
    except json.JSONDecodeError as exc:
        raise SourceUnavailable(f"Apple hydration JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise SourceUnavailable("Apple hydration payload is not an object")
    return data


def _location(job: Dict[str, Any]) -> str:
    parts: List[str] = []
    for loc in job.get("locations") or []:
        if not isinstance(loc, dict):
            continue
        city = normalize_space(loc.get("city") or "")
        if city.lower() == "new city":
            city = ""
        bits = [
            city,
            loc.get("stateProvince") or "",
            loc.get("metro") or "",
            loc.get("name") or "",
            loc.get("countryName") or "",
        ]
        cleaned: List[str] = []
        for bit in bits:
            label = normalize_space(bit)
            if not label or label.lower() == "new city":
                continue
            if label not in cleaned:
                cleaned.append(label)
        text = ", ".join(cleaned)
        if text and text not in parts:
            parts.append(text)
    return "; ".join(parts)


def _parse_page(html: str, fetched_at: str) -> Tuple[List[Dict[str, str]], int]:
    data = _parse_hydration(html)
    search = ((data.get("loaderData") or {}).get("search") or {})
    total = int(search.get("totalRecords") or 0)
    jobs: List[Dict[str, str]] = []
    for item in search.get("searchResults") or []:
        if not isinstance(item, dict):
            continue
        position_id = str(item.get("positionId") or item.get("id") or "")
        title = normalize_space(item.get("postingTitle") or "")
        if not position_id or not title:
            continue
        slug = item.get("transformedPostingTitle") or ""
        official = f"https://jobs.apple.com/en-us/details/{position_id}"
        if slug:
            official = f"{official}/{slug}"
        posted = item.get("postDateInGMT") or item.get("postingDate") or ""
        jobs.append(
            make_job(
                source=SOURCE,
                company=COMPANY,
                title=title,
        location=_location(item) or "United States",
                job_id=str(item.get("reqId") or position_id),
                posted_date=posted,
                date_confidence="high" if item.get("postDateInGMT") else ("medium" if posted else "unknown"),
                source_url=official,
                official_url=official,
                description=normalize_space(item.get("jobSummary") or ""),
                fetched_at=fetched_at,
            )
        )
    return jobs, total


def scrape_apple(
    session: requests.Session,
    *,
    max_pages: int = 50,
    searches: Optional[List[Dict[str, str]]] = None,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    searches = searches or DEFAULT_SEARCHES
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    pages = 0
    errors: List[str] = []
    search_urls = [search_url(s, 1) for s in searches]

    for filters in searches:
        query_ids: set[str] = set()
        for page in range(1, max_pages + 1):
            html = http_get_apple(session, search_url(filters, page))
            pages += 1
            try:
                page_jobs, total = _parse_page(html, fetched_at)
            except SourceUnavailable as exc:
                errors.append(f"page {page}: {exc}")
                break
            if not page_jobs:
                break
            page_ids = [job["job_id"] for job in page_jobs]
            if page_ids and query_ids and all(jid in query_ids for jid in page_ids):
                break
            for job in page_jobs:
                raw_count += 1
                jid = job["job_id"]
                query_ids.add(jid)
                if jid in seen:
                    continue
                seen.add(jid)
                if not keep_us_or_unknown(job.get("location", "")):
                    continue
                jobs.append(job)
            if total and page * 20 >= total:
                break
            time.sleep(SLEEP_S)

    return {
        "company": COMPANY,
        "source": SOURCE,
        "method": "HTTP GET HTML + __staticRouterHydrationData JSON",
        "search_url": search_urls[0] if search_urls else SEARCH,
        "search_urls": search_urls,
        "pagination": "page=1,2,... (20 jobs/page); stop on empty/repeat or totalRecords",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
    }


def http_get_apple(session: requests.Session, url: str) -> str:
    from .http import http_get

    return http_get(session, url, label="apple").text
