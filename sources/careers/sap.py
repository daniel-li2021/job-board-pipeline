"""SAP SuccessFactors RMK HTML search adapter.

Method: GET ``https://jobs.sap.com/search/`` with ``locationsearch=United+States``
and ``startrow`` pagination (25/page). Job details from the public job HTML.
"""

from __future__ import annotations

import re
import time
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso

SEARCH = "https://jobs.sap.com/search/"
SLEEP_S = 0.3
DETAIL_SLEEP_S = 0.12
MAX_DETAILS = 200
PAGE_SIZE = 25
DEFAULT_QUERIES = ["software engineer", "machine learning engineer"]
JOB_HREF_RE = re.compile(r'href="(/job/[^"]+/(\d+)/?)"')


def _soup(html: str):
    from bs4 import BeautifulSoup

    return BeautifulSoup(html, "html.parser")


def _cards(html: str) -> List[Tuple[str, str, str, str]]:
    """Return (job_id, path, title, location) from a search page."""
    soup = _soup(html)
    out: List[Tuple[str, str, str, str]] = []
    seen: set[str] = set()
    for link in soup.select("a.jobTitle-link, a[href*='/job/']"):
        href = link.get("href") or ""
        match = re.search(r"/job/[^\"']+/(\d+)/?", href)
        if not match:
            continue
        jid = match.group(1)
        if jid in seen:
            continue
        seen.add(jid)
        title = normalize_space(link.get_text(" ", strip=True))
        location = ""
        parent = link.find_parent("tr") or link.find_parent("div")
        if parent:
            loc_el = parent.select_one(".jobLocation, .job-location, span.location")
            if loc_el:
                location = normalize_space(loc_el.get_text(" ", strip=True))
        if not location:
            # URL slug often contains City-...-ST-zip
            slug = href.split("/job/")[-1].rsplit("/", 2)[0]
            location = normalize_space(slug.replace("-", " "))
        out.append((jid, href, title, location))
    return out


def scrape_sap(
    session: requests.Session,
    *,
    max_pages: int = 50,
    queries: Optional[List[str]] = None,
    fetch_details: bool = True,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = queries or DEFAULT_QUERIES
    company = "SAP"
    source = "sap_official_careers"
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    pages = 0
    errors: List[str] = []
    detail_fetches = 0

    for query in queries:
        query_ids: set[str] = set()
        for page in range(max_pages):
            startrow = page * PAGE_SIZE
            payload = http_get(
                session,
                SEARCH,
                label="sap search",
                params={
                    "q": query,
                    "locationsearch": "United States",
                    "startrow": startrow,
                },
            )
            pages += 1
            cards = _cards(payload.text)
            if not cards:
                break
            page_ids = [c[0] for c in cards]
            if page_ids and query_ids and all(jid in query_ids for jid in page_ids):
                break
            for jid, href, title, location in cards:
                raw_count += 1
                query_ids.add(jid)
                if jid in seen:
                    continue
                seen.add(jid)
                if location and not keep_us_or_unknown(location):
                    continue
                official = urljoin("https://jobs.sap.com", href)
                description = ""
                posted = ""
                if fetch_details and detail_fetches < MAX_DETAILS:
                    try:
                        det = http_get(session, official, label="sap detail")
                        soup = _soup(det.text)
                        desc_el = (
                            soup.select_one(".jobdescription, #job-details, .job-description, article")
                            or soup.select_one("[itemprop='description']")
                        )
                        if desc_el:
                            description = html_to_text(str(desc_el))
                        else:
                            description = html_to_text(det.text)
                        date_el = soup.select_one("[itemprop='datePosted'], time")
                        if date_el:
                            posted = date_el.get("datetime") or date_el.get_text(" ", strip=True)
                        loc_el = soup.select_one(".jobLocation, [itemprop='address'], .location")
                        if loc_el:
                            loc2 = normalize_space(loc_el.get_text(" ", strip=True))
                            if loc2:
                                location = loc2
                        detail_fetches += 1
                        time.sleep(DETAIL_SLEEP_S)
                    except Exception as exc:  # noqa: BLE001
                        errors.append(f"detail {jid}: {exc}")
                if location and not keep_us_or_unknown(location):
                    continue
                jobs.append(
                    make_job(
                        source=source,
                        company=company,
                        title=title,
                        location=location,
                        job_id=jid,
                        posted_date=posted,
                        date_confidence="high" if posted else "unknown",
                        source_url=official,
                        official_url=official,
                        description=description,
                        fetched_at=fetched_at,
                    )
                )
            if len(cards) < PAGE_SIZE:
                break
            time.sleep(SLEEP_S)

    return {
        "company": company,
        "source": source,
        "method": "HTTP GET jobs.sap.com/search HTML + job detail HTML",
        "search_url": "https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States",
        "search_urls": [SEARCH],
        "pagination": f"startrow=0,{PAGE_SIZE},... ; stop on empty/repeat or short page",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "detail_fetches": detail_fetches,
    }
