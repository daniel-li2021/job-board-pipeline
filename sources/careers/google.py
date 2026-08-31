"""Google Careers search-results scraper.

Method: plain HTTP GET of the public results page, then parse the embedded
``AF_initDataCallback({key: 'ds:1', ...})`` JSON. Pagination is ``&page=N``
(1-based, 20 jobs/page). Confirmed 2026-08-26 against:

https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Software%20Engineer%22&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE&location=United%20States&page=1
"""

from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlencode

import requests

from ..schema import SourceUnavailable, make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso, slugify

SOURCE = "google_official_careers"
COMPANY = "Google"
BASE = "https://www.google.com/about/careers/applications/jobs/results"
RESULTS_BASE = BASE + "/"
SLEEP_S = 0.35

# User-provided search: quoted SWE + early/mid/intern levels, US, newest first.
DEFAULT_QUERIES: List[Dict[str, Any]] = [
    {
        "q": '"Software Engineer"',
        "target_levels": ["MID", "EARLY", "INTERN_AND_APPRENTICE"],
        "location": "United States",
        "sort_by": "date",
    },
    {
        "q": '"Machine Learning Engineer"',
        "target_levels": ["MID", "EARLY", "INTERN_AND_APPRENTICE"],
        "location": "United States",
        "sort_by": "date",
    },
    {
        "q": '"Data Engineer"',
        "target_levels": ["MID", "EARLY", "INTERN_AND_APPRENTICE"],
        "location": "United States",
        "sort_by": "date",
        "max_pages": 3,
    },
    {
        "q": '"Infrastructure Engineer"',
        "target_levels": ["MID", "EARLY", "INTERN_AND_APPRENTICE"],
        "location": "United States",
        "sort_by": "date",
        "max_pages": 3,
    },
    {
        "q": '"DeepMind"',
        "target_levels": ["MID", "EARLY", "INTERN_AND_APPRENTICE"],
        "location": "United States",
        "sort_by": "date",
        "max_pages": 2,
    },
]


def _params(query: Dict[str, Any], page: int) -> List[Tuple[str, str]]:
    items: List[Tuple[str, str]] = [
        ("sort_by", query.get("sort_by") or "date"),
        ("q", query["q"]),
        ("location", query.get("location") or "United States"),
        ("page", str(page)),
    ]
    for level in query.get("target_levels") or []:
        items.append(("target_level", str(level)))
    return items


def search_url(query: Dict[str, Any], page: int = 1) -> str:
    return BASE + "?" + urlencode(_params(query, page), doseq=True)


def _extract_ds1(html: str) -> Any:
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, flags=re.S)
    blob = next((s for s in scripts if "AF_initDataCallback({key: 'ds:1'" in s), "")
    if not blob:
        raise SourceUnavailable("Google results page missing AF_initDataCallback ds:1")
    match = re.search(
        r"AF_initDataCallback\(\{key: 'ds:1', hash: '[^']*', data:(.*), sideChannel:",
        blob,
        flags=re.S,
    )
    if not match:
        raise SourceUnavailable("Google ds:1 payload could not be sliced")
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise SourceUnavailable(f"Google ds:1 JSON: {exc}") from exc


def _unix_to_iso(value: Any) -> str:
    if isinstance(value, list) and value:
        value = value[0]
    if not isinstance(value, (int, float)) or value <= 0:
        return ""
    try:
        return datetime.fromtimestamp(float(value), tz=timezone.utc).strftime("%Y-%m-%d")
    except (OverflowError, OSError, ValueError):
        return ""


def _locations(raw: Any) -> str:
    if not isinstance(raw, list):
        return ""
    seen: List[str] = []
    for loc in raw:
        label = ""
        if isinstance(loc, list) and loc:
            label = normalize_space(loc[0])
        elif isinstance(loc, str):
            label = normalize_space(loc)
        if label and label not in seen:
            seen.append(label)
    return "; ".join(seen)


def _parse_jobs(data: Any, fetched_at: str) -> Tuple[List[Dict[str, str]], int, int]:
    if not isinstance(data, list) or not data:
        return [], 0, 20
    rows = data[0] if isinstance(data[0], list) else []
    total = int(data[2]) if len(data) > 2 and isinstance(data[2], int) else 0
    page_size = int(data[3]) if len(data) > 3 and isinstance(data[3], int) else 20
    jobs: List[Dict[str, str]] = []
    for item in rows:
        if not isinstance(item, list) or len(item) < 2:
            continue
        jid = str(item[0] or "")
        title = normalize_space(item[1] if len(item) > 1 else "")
        if not jid or not title:
            continue
        location = _locations(item[9] if len(item) > 9 else None)
        responsibilities = html_to_text(item[3][1] if len(item) > 3 and isinstance(item[3], list) and len(item[3]) > 1 else "")
        qualifications = html_to_text(item[4][1] if len(item) > 4 and isinstance(item[4], list) and len(item[4]) > 1 else "")
        overview = html_to_text(item[10][1] if len(item) > 10 and isinstance(item[10], list) and len(item[10]) > 1 else "")
        description = normalize_space(" ".join(p for p in (overview, responsibilities, qualifications) if p))
        posted = _unix_to_iso(item[12] if len(item) > 12 else None)
        updated = _unix_to_iso(item[13] if len(item) > 13 else None)
        slug = slugify(title)
        official = f"{RESULTS_BASE}{jid}-{slug}"
        jobs.append(
            make_job(
                source=SOURCE,
                company=COMPANY,
                title=title,
                location=location or "United States",
                job_id=jid,
                posted_date=posted,
                updated_date=updated,
                date_confidence="high" if posted else "unknown",
                source_url=official,
                official_url=official,
                description=description,
                fetched_at=fetched_at,
            )
        )
    return jobs, total, page_size


def scrape_google(
    session: requests.Session,
    *,
    max_pages: int = 50,
    queries: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = queries or DEFAULT_QUERIES
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    pages = 0
    errors: List[str] = []
    search_urls = [search_url(q, 1) for q in queries]

    for query in queries:
        query_ids: set[str] = set()
        query_max_pages = min(max_pages, int(query.get("max_pages") or max_pages))
        for page in range(1, query_max_pages + 1):
            html = http_get(
                session,
                BASE,
                label="google",
                params=_params(query, page),
            ).text
            pages += 1
            try:
                data = _extract_ds1(html)
                page_jobs, total, page_size = _parse_jobs(data, fetched_at)
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
            if total and page * max(page_size, 1) >= total:
                break
            time.sleep(SLEEP_S)

    return {
        "company": COMPANY,
        "source": SOURCE,
        "method": "HTTP GET HTML + AF_initDataCallback ds:1 JSON",
        "search_url": search_urls[0] if search_urls else BASE,
        "search_urls": search_urls,
        "pagination": "page=1,2,... (20 jobs/page); stop on empty/repeat or advertised total",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
    }
