"""Generic Lever postings API adapter."""

from __future__ import annotations

from typing import Any, Dict, List

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso

API = "https://api.lever.co/v0/postings/{token}"


def _location(item: Dict[str, Any]) -> str:
    categories = item.get("categories") or {}
    parts = categories.get("allLocations") or []
    if not parts and categories.get("location"):
        parts = [categories["location"]]
    return "; ".join(normalize_space(value) for value in parts if value)


def scrape_lever(session: requests.Session, *, company: str, token: str) -> Dict[str, Any]:
    fetched_at = now_iso()
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    url = API.format(token=token)
    rows = http_get(session, url, label=f"{company} lever", params={"mode": "json"}).json()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    for item in rows if isinstance(rows, list) else []:
        if not isinstance(item, dict):
            continue
        raw_count += 1
        location = _location(item)
        if location and not keep_us_or_unknown(location):
            continue
        description = " ".join(
            html_to_text(section.get("content") or "")
            for section in item.get("lists") or []
            if isinstance(section, dict)
        )
        official = item.get("hostedUrl") or item.get("applyUrl") or ""
        jobs.append(make_job(
            source=source,
            company=company,
            title=item.get("text") or "",
            location=location,
            job_id=str(item.get("id") or ""),
            posted_date=item.get("createdAt") or "",
            date_confidence="high" if item.get("createdAt") else "unknown",
            source_url=official,
            official_url=official,
            description=description,
            fetched_at=fetched_at,
        ))
    return {
        "company": company,
        "source": source,
        "method": "HTTP GET Lever /v0/postings/{token}?mode=json",
        "search_url": url,
        "search_urls": [url],
        "pagination": "single JSON payload",
        "pages_fetched": 1,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }
