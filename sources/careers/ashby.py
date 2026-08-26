"""Official-careers Ashby job-board adapter.

GET ``https://api.ashbyhq.com/posting-api/job-board/{token}`` returns listed
jobs with HTML descriptions. US-only via location + secondaryLocations.
"""

from __future__ import annotations

from typing import Any, Dict, List

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso

JSON_URL = "https://api.ashbyhq.com/posting-api/job-board/{token}"


def _loc_text(item: Dict[str, Any]) -> str:
    parts: List[str] = []
    loc = item.get("location") or ""
    if isinstance(loc, dict):
        loc = loc.get("name") or loc.get("location") or ""
    if loc:
        parts.append(normalize_space(loc))
    addr = item.get("address") or {}
    postal = addr.get("postalAddress") if isinstance(addr, dict) else {}
    if isinstance(postal, dict):
        bits = [
            postal.get("addressLocality") or "",
            postal.get("addressRegion") or "",
            postal.get("addressCountry") or "",
        ]
        label = ", ".join(normalize_space(b) for b in bits if b)
        if label and label not in parts:
            parts.append(label)
    for extra in item.get("secondaryLocations") or []:
        if isinstance(extra, dict):
            extra = extra.get("location") or extra.get("name") or ""
        extra = normalize_space(extra)
        if extra and extra not in parts:
            parts.append(extra)
    if item.get("isRemote") and not any("remote" in p.lower() for p in parts):
        country = ""
        if isinstance(postal, dict):
            country = normalize_space(postal.get("addressCountry") or "")
        if country:
            parts.append(f"Remote, {country}")
        else:
            parts.append("Remote")
    return "; ".join(parts)


def scrape_ashby(
    session: requests.Session,
    *,
    company: str,
    token: str,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    url = JSON_URL.format(token=token)
    payload = http_get(session, url, label=f"{company} ashby").json()
    rows = payload.get("jobs") or []
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    for item in rows:
        if not isinstance(item, dict):
            continue
        if item.get("isListed") is False:
            continue
        raw_count += 1
        location = _loc_text(item)
        if location and not keep_us_or_unknown(location):
            continue
        official = item.get("jobUrl") or item.get("applyUrl") or ""
        desc = item.get("descriptionPlain") or html_to_text(item.get("descriptionHtml") or "")
        jobs.append(
            make_job(
                source=source,
                company=company,
                title=item.get("title") or "",
                location=location,
                job_id=str(item.get("id") or ""),
                posted_date=item.get("publishedAt") or "",
                date_confidence="high" if item.get("publishedAt") else "unknown",
                source_url=official,
                official_url=official,
                description=desc,
                fetched_at=fetched_at,
            )
        )
    return {
        "company": company,
        "source": source,
        "method": "HTTP GET Ashby posting-api/job-board/{token}",
        "search_url": url,
        "search_urls": [url],
        "pagination": "single JSON payload (no paging)",
        "pages_fetched": 1,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }
