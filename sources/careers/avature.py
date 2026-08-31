"""Bloomberg Avature career-site adapter.

Method: GET ``https://bloomberg.avature.net/careers/SearchJobs`` with
``jobOffset`` pagination, then job-detail HTML for JD / posted date / location.
US-only at discovery. Keyword query is applied when the form honors ``q``.
"""

from __future__ import annotations

import re
import time
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso
from .incremental import DetailCache, annotate_detail

SEARCH = "https://bloomberg.avature.net/careers/SearchJobs"
SLEEP_S = 0.3
DETAIL_SLEEP_S = 0.12
MAX_DETAILS = 200
PAGE_SIZE = 12
DEFAULT_QUERIES = ["software engineer", "machine learning engineer"]
JOB_RE = re.compile(r"/careers/JobDetail/([^\"/?#]+)/(\d+)")


def _soup(html: str):
    from bs4 import BeautifulSoup

    return BeautifulSoup(html, "html.parser")


def _cards(html: str) -> List[Tuple[str, str, str, str]]:
    soup = _soup(html)
    out: List[Tuple[str, str, str, str]] = []
    seen: set[str] = set()
    for link in soup.select("a[href*='/careers/JobDetail/']"):
        href = link.get("href") or ""
        match = JOB_RE.search(href)
        if not match:
            continue
        slug, jid = match.group(1), match.group(2)
        if jid in seen:
            continue
        seen.add(jid)
        title = normalize_space(link.get_text(" ", strip=True)) or slug.replace("-", " ")
        location = ""
        parent = link.find_parent("article") or link.find_parent("li") or link.find_parent("div")
        if parent:
            loc_el = parent.select_one(".list__item__subtitle, .job-location, .location, span")
            if loc_el:
                location = normalize_space(loc_el.get_text(" ", strip=True))
        out.append((jid, href, title, location))
    return out


def scrape_avature(
    session: requests.Session,
    *,
    company: str,
    search_url: str = SEARCH,
    max_pages: int = 50,
    queries: Optional[List[str]] = None,
    fetch_details: bool = True,
    detail_cache: Optional[DetailCache] = None,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = queries or DEFAULT_QUERIES
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    pages = 0
    errors: List[str] = []
    detail_fetches = 0
    detail_reused = 0
    detail_cache = detail_cache or DetailCache([])

    for query in queries:
        query_ids: set[str] = set()
        for page in range(max_pages):
            offset = page * PAGE_SIZE
            payload = http_get(
                session,
                search_url,
                label=f"{company} avature",
                params={
                    "q": query,
                    "jobRecordsPerPage": PAGE_SIZE,
                    "jobOffset": offset,
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
                official = urljoin("https://bloomberg.avature.net", href)
                listing_title = title
                decision = detail_cache.decide(
                    company=company, job_id=jid, url=official, title=listing_title,
                )
                description = str((decision.cached or {}).get("description") or "")
                posted = str((decision.cached or {}).get("posted_date") or "")
                if decision.cached and not decision.should_fetch:
                    location = str(decision.cached.get("location") or location)
                    detail_reused += 1
                detail_fetched = False
                if fetch_details and decision.should_fetch and detail_fetches < MAX_DETAILS:
                    try:
                        det = http_get(session, official, label=f"{company} avature detail")
                        soup = _soup(det.text)
                        desc_el = (
                            soup.select_one(".job-description, #job-description, [itemprop='description'], article")
                            or soup.select_one(".cms-content, .jobdetail")
                        )
                        description = html_to_text(str(desc_el) if desc_el else det.text)
                        date_el = soup.select_one("[itemprop='datePosted'], time")
                        if date_el:
                            posted = date_el.get("datetime") or date_el.get_text(" ", strip=True)
                        loc_el = soup.select_one("[itemprop='jobLocation'], .job-location, .location")
                        if loc_el:
                            loc2 = normalize_space(loc_el.get_text(" ", strip=True))
                            if loc2:
                                location = loc2
                        h1 = soup.select_one("h1")
                        if h1 and not title:
                            title = normalize_space(h1.get_text(" ", strip=True))
                        detail_fetches += 1
                        detail_fetched = True
                        time.sleep(DETAIL_SLEEP_S)
                    except Exception as exc:  # noqa: BLE001
                        errors.append(f"detail {jid}: {exc}")
                if location and not keep_us_or_unknown(location):
                    continue
                job = make_job(
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
                annotate_detail(job, decision, detail_fetched=detail_fetched, listing_title=listing_title)
                jobs.append(job)
            if len(cards) < PAGE_SIZE:
                break
            time.sleep(SLEEP_S)

    return {
        "company": company,
        "source": source,
        "method": "HTTP GET Avature SearchJobs HTML + JobDetail HTML",
        "search_url": f"{search_url}?q=software+engineer&jobRecordsPerPage={PAGE_SIZE}&jobOffset=0",
        "search_urls": [search_url],
        "pagination": f"jobOffset=0,{PAGE_SIZE},... ; stop on empty/repeat or short page",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "detail_fetches": detail_fetches,
        "detail_cache_reused": detail_reused,
    }
