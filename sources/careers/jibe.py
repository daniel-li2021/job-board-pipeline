"""Public Jibe/iCIMS career-search JSON adapter."""

from __future__ import annotations

import math
import time
from typing import Any, Dict, List, Optional

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

PAGE_SIZE = 100


def scrape_jibe(
    session: requests.Session,
    *,
    company: str,
    api_url: str,
    max_pages: int = 12,
    queries: Optional[List[str]] = None,
    country: str = "United States",
) -> Dict[str, Any]:
    fetched_at = now_iso()
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = pages = 0

    for query in queries or ROLE_SEARCH_QUERIES:
        query_ids: set[str] = set()
        for page in range(1, max_pages + 1):
            payload = http_get(
                session,
                api_url,
                label=f"{company} Jibe jobs API",
                params={"keywords": query, "country": country, "page": page, "limit": PAGE_SIZE},
                headers={"Accept": "application/json"},
            ).json()
            pages += 1
            rows = payload.get("jobs") or []
            if not rows:
                break
            page_ids = [normalize_space((row.get("data") or {}).get("req_id") or (row.get("data") or {}).get("slug")) for row in rows]
            if query_ids and page_ids and all(jid in query_ids for jid in page_ids):
                break
            query_ids.update(jid for jid in page_ids if jid)
            for wrapper in rows:
                row = wrapper.get("data") or {}
                raw_count += 1
                jid = normalize_space(row.get("req_id") or row.get("slug"))
                if not jid or jid in seen:
                    continue
                seen.add(jid)
                location = normalize_space(row.get("full_location") or row.get("short_location"))
                if location and not keep_us_or_unknown(location):
                    continue
                official = normalize_space(row.get("canonical_url") or "")
                jobs.append(make_job(
                    source=source,
                    company=company,
                    title=normalize_space(row.get("title")),
                    location=location,
                    job_id=jid,
                    posted_date=row.get("create_date") or "",
                    updated_date=row.get("update_date") or "",
                    date_confidence="high" if row.get("create_date") else "unknown",
                    source_url=official or api_url,
                    official_url=official,
                    description=html_to_text(row.get("description") or ""),
                    fetched_at=fetched_at,
                ))
            total = int(payload.get("totalCount") or payload.get("count") or 0)
            if page >= math.ceil(total / PAGE_SIZE) or len(rows) < PAGE_SIZE:
                break
            time.sleep(0.1)

    return {
        "company": company,
        "source": source,
        "method": "HTTP GET public Jibe/iCIMS jobs JSON",
        "search_url": api_url,
        "search_urls": [api_url],
        "pagination": "page=1,2,... per role query; stop on total/empty/repeat/short page",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }
