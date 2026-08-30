"""Disney Careers server-rendered US search adapter."""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional
from urllib.parse import quote, urljoin

import requests
from bs4 import BeautifulSoup

from ..schema import make_job, normalize_space
from .http import http_get, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

BASE = "https://www.disneycareers.com"
PATH = "/en/search-jobs/{query}/United%20States/391/1/2/6252001/39x76/-98x5/100/2"


def scrape_disney(
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
        base_url = BASE + PATH.format(query=quote(query, safe=""))
        for page in range(1, min(max_pages, 3) + 1):
            html = http_get(
                session,
                base_url,
                label="Disney careers search",
                params={"p": page},
            ).text
            soup = BeautifulSoup(html, "html.parser")
            cards = soup.select("#search-results-jobs a[data-job-id]")
            pages += 1
            if not cards:
                break
            for card in cards:
                raw_count += 1
                jid = str(card.get("data-job-secondary-id") or card.get("data-job-id") or "")
                if not jid or jid in seen:
                    continue
                seen.add(jid)
                location_node = card.select_one(".job-location")
                location = normalize_space(location_node.get_text(" ", strip=True) if location_node else "")
                if location and not keep_us_or_unknown(location):
                    continue
                official = urljoin(BASE, card.get("href") or "")
                title_node = card.select_one("h2")
                date_node = card.select_one(".job-date-posted")
                jobs.append(make_job(
                    source="disney_official_careers",
                    company="Disney",
                    title=normalize_space(title_node.get_text(" ", strip=True) if title_node else ""),
                    location=location,
                    job_id=jid,
                    posted_date=normalize_space(date_node.get_text(" ", strip=True) if date_node else ""),
                    date_confidence="high" if date_node else "unknown",
                    source_url=official,
                    official_url=official,
                    description="",
                    fetched_at=fetched_at,
                ))
            next_link = soup.select_one("nav#pagination-bottom a.next")
            if not next_link or "disabled" in (next_link.get("class") or []):
                break
            time.sleep(0.15)
    return {
        "company": "Disney",
        "source": "disney_official_careers",
        "method": "HTTP GET Disney server-rendered US search results",
        "search_url": BASE + PATH.format(query="software%20engineer"),
        "search_urls": [BASE + PATH.format(query="software%20engineer")],
        "pagination": "?p=1,2,3 per role query (intentional request cap)",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }
