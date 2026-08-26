"""Microsoft Careers (Eightfold PCSX) scraper.

Method: GET ``/api/pcsx/search`` on apply.careers.microsoft.com after loading
the public careers portal for CSRF + session cookies. Pagination is
``start`` + ``num`` (API caps ``num`` at 10). ``sort_by=timestamp`` is newest
first. ``location=United States`` is a real API filter. Confirmed 2026-08-26.

Portal: https://apply.careers.microsoft.com/careers
Search: GET /api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10
Details: GET /api/pcsx/position_details?domain=microsoft.com&position_id=...
"""

from __future__ import annotations

import re
import time
from typing import Any, Dict, List, Optional

import requests

from ..schema import SourceUnavailable, make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso

SOURCE = "microsoft_official_careers"
COMPANY = "Microsoft"
PORTAL = "https://apply.careers.microsoft.com/careers"
SEARCH = "https://apply.careers.microsoft.com/api/pcsx/search"
DETAILS = "https://apply.careers.microsoft.com/api/pcsx/position_details"
DOMAIN = "microsoft.com"
PAGE_SIZE = 10
SLEEP_S = 0.25
DETAIL_SLEEP_S = 0.12
MAX_DETAILS = 200

DEFAULT_QUERIES = [
    "software engineer",
    "machine learning engineer",
]


def _csrf_headers(session: requests.Session) -> Dict[str, str]:
    html = http_get(session, PORTAL, label="microsoft portal").text
    match = re.search(r'name="_csrf" content="([^"]+)"', html)
    if not match:
        raise SourceUnavailable("Microsoft careers portal missing CSRF token")
    return {
        "Accept": "application/json",
        "X-CSRFToken": match.group(1),
        "Referer": PORTAL,
    }


def _unwrap(payload: Any) -> Dict[str, Any]:
    if not isinstance(payload, dict):
        return {}
    data = payload.get("data")
    return data if isinstance(data, dict) else payload


def _location(item: Dict[str, Any]) -> str:
    locs = item.get("locations") or item.get("standardizedLocations") or []
    if isinstance(locs, list):
        return "; ".join(normalize_space(x) for x in locs if x)
    return normalize_space(locs)


def scrape_microsoft(
    session: requests.Session,
    *,
    max_pages: int = 50,
    queries: Optional[List[str]] = None,
    fetch_details: bool = True,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = queries or DEFAULT_QUERIES
    headers = _csrf_headers(session)
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    pages = 0
    errors: List[str] = []
    detail_fetches = 0

    for query in queries:
        start = 0
        query_ids: set[str] = set()
        for _page in range(max_pages):
            params = {
                "domain": DOMAIN,
                "query": query,
                "location": "United States",
                "sort_by": "timestamp",
                "start": start,
                "num": PAGE_SIZE,
            }
            payload = http_get(session, SEARCH, label="microsoft search", params=params, headers=headers).json()
            pages += 1
            data = _unwrap(payload)
            rows = data.get("positions") or []
            total = int(data.get("count") or 0)
            if not rows:
                break
            page_ids = [
                str(item.get("displayJobId") or item.get("atsJobId") or item.get("id") or "")
                for item in rows
                if isinstance(item, dict)
            ]
            page_ids = [jid for jid in page_ids if jid]
            if page_ids and query_ids and all(jid in query_ids for jid in page_ids):
                break
            for item in rows:
                if not isinstance(item, dict):
                    continue
                raw_count += 1
                jid = str(item.get("displayJobId") or item.get("atsJobId") or item.get("id") or "")
                pid = str(item.get("id") or "")
                if not jid:
                    continue
                query_ids.add(jid)
                if jid in seen:
                    continue
                seen.add(jid)
                location = _location(item)
                if location and not keep_us_or_unknown(location):
                    continue
                path = item.get("positionUrl") or f"/careers/job/{pid}"
                official = "https://apply.careers.microsoft.com" + path
                description = ""
                if fetch_details and pid and detail_fetches < MAX_DETAILS:
                    try:
                        det = http_get(
                            session,
                            DETAILS,
                            label="microsoft details",
                            params={"domain": DOMAIN, "position_id": pid},
                            headers=headers,
                        ).json()
                        info = _unwrap(det)
                        description = html_to_text(info.get("jobDescription") or "")
                        location = _location(info) or location
                        detail_fetches += 1
                        time.sleep(DETAIL_SLEEP_S)
                    except SourceUnavailable as exc:
                        errors.append(f"details {pid}: {exc}")
                jobs.append(
                    make_job(
                        source=SOURCE,
                        company=COMPANY,
                        title=item.get("name") or "",
                        location=location,
                        job_id=jid,
                        posted_date=item.get("postedTs") or item.get("creationTs") or "",
                        updated_date="",
                        date_confidence="high" if item.get("postedTs") else "unknown",
                        source_url=official,
                        official_url=official,
                        description=description,
                        fetched_at=fetched_at,
                    )
                )
            start += PAGE_SIZE
            if total and start >= total:
                break
            time.sleep(SLEEP_S)

    return {
        "company": COMPANY,
        "source": SOURCE,
        "method": "HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)",
        "search_url": (
            f"{SEARCH}?domain={DOMAIN}&query=software+engineer"
            "&location=United+States&sort_by=timestamp&start=0&num=10"
        ),
        "search_urls": [PORTAL, SEARCH],
        "pagination": "start=0,10,20,... ; num=10 (API cap); stop on empty/repeat or count",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "detail_fetches": detail_fetches,
    }
