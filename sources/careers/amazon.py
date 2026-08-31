"""Amazon.jobs JSON search scraper.

Method: anonymous ``/en/search.json`` (same filters as the public HTML search).
Pagination is ``offset`` + ``result_limit``. Confirmed 2026-08-26 against:

https://www.amazon.jobs/en/search?base_query=software+engineer&country=USA&offset=0&result_limit=10&sort=recent
https://www.amazon.jobs/en/search.json?base_query=software+engineer&country=USA&offset=0&result_limit=10&sort=recent
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso
from .incremental import NewestFirstPager
from .query_terms import ROLE_SEARCH_QUERIES

SOURCE = "amazon_official_careers"
COMPANY = "Amazon"
JSON_URL = "https://www.amazon.jobs/en/search.json"
HTML_SEARCH = "https://www.amazon.jobs/en/search"
SLEEP_S = 0.25
RESULT_LIMIT = 20

DEFAULT_QUERIES = ROLE_SEARCH_QUERIES + [
    "software development engineer",
    "systems development engineer",
    "site reliability engineer",
    "applied scientist",
]
# Broader role-family variants are useful but lower-volume. Bound them so the
# scheduled run does not double the worst-case request count.
QUERY_PAGE_CAPS = {
    "data engineer": 3,
    "systems development engineer": 3,
    "site reliability engineer": 3,
    "applied scientist": 2,
}


def scrape_amazon(
    session: requests.Session,
    *,
    max_pages: int = 50,
    queries: Optional[List[str]] = None,
    seen_job_ids: Optional[set[str]] = None,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = queries or DEFAULT_QUERIES
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    pages = 0
    errors: List[str] = []

    for keyword in queries:
        pager = NewestFirstPager(seen_job_ids or set())
        offset = 0
        query_ids: set[str] = set()
        query_max_pages = min(max_pages, QUERY_PAGE_CAPS.get(keyword, max_pages))
        for _page in range(query_max_pages):
            params = {
                "base_query": keyword,
                "country": "USA",
                "offset": offset,
                "result_limit": RESULT_LIMIT,
                "sort": "recent",
            }
            payload = http_get(session, JSON_URL, label="amazon", params=params).json()
            pages += 1
            rows = payload.get("jobs") or []
            hits = int(payload.get("hits") or 0)
            if not rows:
                break
            page_ids = [str(item.get("id_icims") or item.get("id") or "") for item in rows]
            page_ids = [jid for jid in page_ids if jid]
            if page_ids and query_ids and all(jid in query_ids for jid in page_ids):
                break
            for item in rows:
                raw_count += 1
                jid = str(item.get("id_icims") or item.get("id") or "")
                if not jid:
                    continue
                query_ids.add(jid)
                if jid in seen:
                    continue
                seen.add(jid)
                location = item.get("normalized_location") or item.get("location") or ""
                if location and not keep_us_or_unknown(location):
                    continue
                job_path = item.get("job_path") or ""
                official = urljoin("https://www.amazon.jobs", job_path) if job_path else "https://www.amazon.jobs/"
                quals = html_to_text(item.get("basic_qualifications") or "")
                preferred = html_to_text(item.get("preferred_qualifications") or "")
                desc = html_to_text(item.get("description") or item.get("description_short") or "")
                description = normalize_space(" ".join(p for p in (desc, quals, preferred) if p))
                jobs.append(
                    make_job(
                        source=SOURCE,
                        company=COMPANY,
                        title=item.get("title", ""),
                        location=location,
                        job_id=jid,
                        posted_date=item.get("posted_date") or "",
                        updated_date=item.get("updated_time") or "",
                        date_confidence="high" if item.get("posted_date") else "unknown",
                        source_url=official,
                        official_url=official,
                        description=description,
                        fetched_at=fetched_at,
                    )
                )
            if pager.should_stop_after(
                (_page + 1), page_ids, [str(item.get("posted_date") or "") for item in rows if isinstance(item, dict)]
            ):
                break
            offset += RESULT_LIMIT
            if hits and offset >= hits:
                break
            time.sleep(SLEEP_S)

    return {
        "company": COMPANY,
        "source": SOURCE,
        "method": "HTTP GET search.json",
        "search_url": f"{HTML_SEARCH}?base_query=software+engineer&country=USA&offset=0&result_limit=10&sort=recent",
        "search_urls": [JSON_URL],
        "pagination": f"newest-first offset by {RESULT_LIMIT}; minimum 2 pages, then two seen pages + one overlap page; otherwise hits/cap",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
    }
