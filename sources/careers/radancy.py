"""Server-rendered Radancy career-site search adapter."""

from __future__ import annotations

import json
import time
from typing import Any, Dict, List, Optional, Tuple

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

PAGE_SIZE = 30
MAX_DETAILS = 100


def _soup(html: str):
    from bs4 import BeautifulSoup

    return BeautifulSoup(html, "html.parser")


def _cards(html: str) -> List[Tuple[str, str, str, str]]:
    soup = _soup(html)
    cards: List[Tuple[str, str, str, str]] = []
    for row in soup.select("table[data-controller*='table-results'] tbody tr[data-job-url]"):
        link = row.select_one(".job-search-results-title a")
        req = row.select_one(".job-search-results-requisition-identifiers")
        loc = row.select_one(".job-search-results-location")
        url = normalize_space(row.get("data-job-url") or (link.get("href") if link else ""))
        jid = normalize_space(req.get_text(" ", strip=True) if req else "")
        title = normalize_space(link.get_text(" ", strip=True) if link else "")
        location = normalize_space(loc.get_text("; ", strip=True) if loc else "")
        if url and jid and title:
            cards.append((jid, url, title, location))
    return cards


def _job_posting(html: str) -> Dict[str, Any]:
    soup = _soup(html)
    for node in soup.select("script[type='application/ld+json']"):
        try:
            value = json.loads(node.string or node.get_text() or "{}")
        except (TypeError, ValueError):
            continue
        values = value if isinstance(value, list) else [value]
        for item in values:
            if isinstance(item, dict) and item.get("@type") == "JobPosting":
                return item
    return {}


def scrape_radancy(
    session: requests.Session,
    *,
    company: str,
    search_url: str,
    max_pages: int = 3,
    queries: Optional[List[str]] = None,
    fetch_details: bool = True,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = pages = detail_fetches = 0
    errors: List[str] = []

    for query in queries or ROLE_SEARCH_QUERIES:
        query_ids: set[str] = set()
        for page in range(1, max_pages + 1):
            result = http_get(
                session,
                search_url,
                label=f"{company} career search",
                params={"query": query, "page": page, "country_codes[]": "US"},
            )
            pages += 1
            cards = _cards(result.text)
            if not cards:
                break
            page_ids = [card[0] for card in cards]
            if query_ids and all(jid in query_ids for jid in page_ids):
                break
            query_ids.update(page_ids)
            for jid, official, title, location in cards:
                raw_count += 1
                if jid in seen:
                    continue
                seen.add(jid)
                if location and not keep_us_or_unknown(location):
                    continue
                description = posted = ""
                if fetch_details and detail_fetches < MAX_DETAILS:
                    try:
                        detail = http_get(session, official, label=f"{company} career detail")
                        posting = _job_posting(detail.text)
                        title = normalize_space(posting.get("title") or title)
                        description = html_to_text(posting.get("description") or "")
                        posted = normalize_space(posting.get("datePosted") or "")
                        detail_fetches += 1
                        time.sleep(0.1)
                    except Exception as exc:  # noqa: BLE001
                        errors.append(f"detail {jid}: {exc}")
                jobs.append(make_job(
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
                ))
            if len(cards) < PAGE_SIZE:
                break
            time.sleep(0.2)

    return {
        "company": company,
        "source": source,
        "method": "HTTP GET server-rendered Radancy search + JobPosting JSON-LD",
        "search_url": search_url,
        "search_urls": [search_url],
        "pagination": "page=1,2,...; country_codes[]=US; stop on empty/repeat/short page",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "detail_fetches": detail_fetches,
    }
