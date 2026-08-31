"""Official-careers wrapper around the shared public Lever adapter."""

from __future__ import annotations

from typing import Any, Dict

import requests

from ..ats import fetch_lever
from ..schema import normalize_space


def scrape_lever(session: requests.Session, *, company: str, token: str) -> Dict[str, Any]:
    jobs = fetch_lever(session, company, token)
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    for job in jobs:
        job["source"] = source
        job["discovered_via"] = [source]
    url = f"https://api.lever.co/v0/postings/{token}"
    return {
        "company": company,
        "source": source,
        "method": "HTTP GET shared Lever postings API /v0/postings/{token}",
        "search_url": f"https://jobs.lever.co/{token}",
        "search_urls": [url],
        "pagination": "single JSON payload (no paging)",
        "pages_fetched": 1,
        "raw_jobs": len(jobs),
        "jobs": jobs,
        "errors": [],
    }
