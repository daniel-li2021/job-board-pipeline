"""MathWorks server-rendered official opportunity-search adapter."""

from __future__ import annotations

import json
import time
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

SEARCH = "https://www.mathworks.com/company/jobs/opportunities/search/"
PAGE_SIZE = 20
HONEST_CLIENT_HEADERS = {"User-Agent": "python-requests/official-careers"}


def _posting(page: str) -> Dict[str, Any]:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(page, "html.parser")
    for node in soup.select("script[type='application/ld+json']"):
        try:
            value = json.loads(node.string or node.get_text() or "{}")
        except (TypeError, ValueError):
            continue
        for item in value if isinstance(value, list) else [value]:
            if isinstance(item, dict) and item.get("@type") == "JobPosting":
                return item
    return {}


def scrape_mathworks(
    session: requests.Session,
    *,
    max_pages: int = 3,
    queries: Optional[List[str]] = None,
    fetch_details: bool = True,
) -> Dict[str, Any]:
    from bs4 import BeautifulSoup

    fetched_at = now_iso()
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = pages = details = 0
    errors: List[str] = []

    for query in queries or ROLE_SEARCH_QUERIES:
        query_ids: set[str] = set()
        for page in range(1, max_pages + 1):
            params: Dict[str, Any] = {"keywords": query}
            if page > 1:
                params["page"] = page
            text = http_get(
                session,
                SEARCH,
                label="MathWorks career search",
                params=params,
                headers=HONEST_CLIENT_HEADERS,
            ).text
            pages += 1
            soup = BeautifulSoup(text, "html.parser")
            rows = soup.select("tr:has(input.job_posting_checkbox)")
            if not rows:
                break
            page_ids = []
            for row in rows:
                checkbox = row.select_one("input.job_posting_checkbox")
                page_ids.append(normalize_space(checkbox.get("value") if checkbox else ""))
            if query_ids and all(jid in query_ids for jid in page_ids):
                break
            query_ids.update(jid for jid in page_ids if jid)
            for row in rows:
                raw_count += 1
                checkbox = row.select_one("input.job_posting_checkbox")
                link = row.select_one(".search_title a")
                jid = normalize_space(checkbox.get("value") if checkbox else "")
                if not jid or not link or jid in seen:
                    continue
                seen.add(jid)
                loc = row.select_one(".add_font_color_green, .job-location")
                location = normalize_space(loc.get_text(" ", strip=True) if loc else "")
                if location and not keep_us_or_unknown(location):
                    continue
                official = urljoin(SEARCH, link.get("href") or "")
                title = normalize_space(link.get_text(" ", strip=True))
                description = posted = ""
                if fetch_details and details < 100:
                    try:
                        detail = http_get(
                            session,
                            official,
                            label="MathWorks career detail",
                            headers=HONEST_CLIENT_HEADERS,
                        )
                        posting = _posting(detail.text)
                        title = normalize_space(posting.get("title") or title)
                        description = html_to_text(posting.get("description") or "")
                        posted = normalize_space(posting.get("datePosted") or "")
                        details += 1
                    except Exception as exc:  # noqa: BLE001
                        errors.append(f"detail {jid}: {exc}")
                jobs.append(make_job(
                    source="mathworks_official_careers",
                    company="MathWorks",
                    title=title,
                    location=location,
                    job_id=jid,
                    posted_date=posted,
                    date_confidence="high" if posted else "unknown",
                    source_url=official,
                    official_url=official,
                    description=description,
                    fetched_at=fetched_at,
                ))
            if len(rows) < PAGE_SIZE:
                break
            time.sleep(0.1)

    return {
        "company": "MathWorks",
        "source": "mathworks_official_careers",
        "method": "HTTP GET server-rendered MathWorks search + JobPosting JSON-LD",
        "search_url": SEARCH,
        "search_urls": [SEARCH],
        "pagination": "page=2,3,... after the unnumbered first page; stop on empty/repeat/short page",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "detail_fetches": details,
    }
