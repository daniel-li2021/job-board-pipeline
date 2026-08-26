"""Official-careers Greenhouse job-board adapter.

Uses the public boards API (same JSON the career site uses). US-only via
``keep_us_or_unknown`` so multi-office US+abroad rows are kept. Matching does
the role/seniority filtering — we do not keyword-drop at scrape time.
"""

from __future__ import annotations

from typing import Any, Dict, List
from urllib.parse import urljoin

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso

JSON_URL = "https://boards-api.greenhouse.io/v1/boards/{token}/jobs"


def _location(item: Dict[str, Any]) -> str:
    parts: List[str] = []
    primary = (item.get("location") or {}).get("name") if isinstance(item.get("location"), dict) else item.get("location")
    if primary:
        parts.append(normalize_space(primary))
    for office in item.get("offices") or []:
        if not isinstance(office, dict):
            continue
        loc = office.get("location") or office.get("name") or ""
        if isinstance(loc, dict):
            loc = loc.get("name") or ""
        loc = normalize_space(loc)
        if loc and loc not in parts:
            parts.append(loc)
    return "; ".join(parts)


def scrape_greenhouse(
    session: requests.Session,
    *,
    company: str,
    token: str,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    url = JSON_URL.format(token=token)
    payload = http_get(session, url, label=f"{company} greenhouse", params={"content": "true"}).json()
    rows = payload.get("jobs") or []
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    for item in rows:
        if not isinstance(item, dict):
            continue
        raw_count += 1
        location = _location(item)
        if location and not keep_us_or_unknown(location):
            continue
        official = item.get("absolute_url") or ""
        if official and not official.startswith("http"):
            official = urljoin("https://job-boards.greenhouse.io/", official)
        jobs.append(
            make_job(
                source=source,
                company=company,
                title=item.get("title") or "",
                location=location,
                job_id=str(item.get("id") or ""),
                posted_date=item.get("first_published") or item.get("updated_at") or "",
                updated_date=item.get("updated_at") or "",
                date_confidence="high" if item.get("first_published") else "medium",
                source_url=official,
                official_url=official,
                description=html_to_text(item.get("content") or ""),
                fetched_at=fetched_at,
            )
        )
    return {
        "company": company,
        "source": source,
        "method": "HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true",
        "search_url": url,
        "search_urls": [url],
        "pagination": "single JSON payload (no paging)",
        "pages_fetched": 1,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }
