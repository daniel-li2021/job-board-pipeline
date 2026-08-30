"""Walmart Careers hybrid-search adapter."""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

import requests

from ..schema import make_job, normalize_space
from .http import http_post, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

SEARCH = "https://careers.walmart.com/api/ai/search-ai/api/v1/combined/hybrid-search"
PAGE_SIZE = 25


def _location(meta: Dict[str, Any]) -> str:
    city = normalize_space(meta.get("primaryLocationCity") or "")
    state = normalize_space(meta.get("primaryLocationState") or "")
    country = normalize_space(meta.get("primaryLocationCountry") or "")
    return ", ".join(value for value in (city, state, country) if value)


def scrape_walmart(
    session: requests.Session,
    *,
    max_pages: int = 12,
    queries: Optional[List[str]] = None,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = queries or ROLE_SEARCH_QUERIES
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = pages = 0
    for query in queries:
        for page in range(max_pages):
            params = {"page": page, "size": PAGE_SIZE, "locale": "en_US"}
            payload = http_post(
                session,
                SEARCH,
                label="Walmart hybrid search",
                params=params,
                json_body={"query": query, "basicSearch": False, "filter": "", "locale": "en_US"},
                headers={"Accept": "application/json", "Content-Type": "application/json"},
            ).json()
            pages += 1
            rows = payload.get("jobs") or []
            if not rows:
                break
            for item in rows:
                if not isinstance(item, dict):
                    continue
                raw_count += 1
                meta = item.get("metadata") or {}
                jid = str(meta.get("jobId") or item.get("id") or "").removesuffix("-External")
                if not jid or jid in seen:
                    continue
                seen.add(jid)
                location = _location(meta)
                if location and not keep_us_or_unknown(location):
                    continue
                official = f"https://careers.walmart.com/job/{jid}"
                jobs.append(make_job(
                    source="walmart_official_careers",
                    company="Walmart Global Tech",
                    title=meta.get("jobPostingTitle") or meta.get("title") or "",
                    location=location,
                    job_id=jid,
                    posted_date=meta.get("jobPostingStartDate") or "",
                    date_confidence="high" if meta.get("jobPostingStartDate") else "unknown",
                    source_url=official,
                    official_url=official,
                    description=item.get("text") or "",
                    fetched_at=fetched_at,
                ))
            if (page + 1) * PAGE_SIZE >= int(payload.get("totalJobs") or 0):
                break
            time.sleep(0.15)
    return {
        "company": "Walmart Global Tech",
        "source": "walmart_official_careers",
        "method": "HTTP POST Walmart combined hybrid-search",
        "search_url": SEARCH,
        "search_urls": [SEARCH],
        "pagination": f"page=0,1,...; size={PAGE_SIZE}; bounded per query",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }
