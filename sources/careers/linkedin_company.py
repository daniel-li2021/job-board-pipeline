"""LinkedIn-the-company jobs via LinkedIn's logged-out guest search."""

from __future__ import annotations

import re
import time
from typing import Any, Dict, List, Optional
from urllib.parse import urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup

from ..schema import make_job, normalize_space
from .http import http_get, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

SEARCH = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
COMPANY_ID = "1337"
PAGE_SIZE = 10


def _clean_url(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def scrape_linkedin_company(
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
        query_ids: set[str] = set()
        for page in range(max_pages):
            params = {
                "keywords": query,
                "location": "United States",
                "f_C": COMPANY_ID,
                "sortBy": "DD",
                "start": page * PAGE_SIZE,
            }
            html = http_get(session, SEARCH, label="LinkedIn company guest search", params=params).text
            cards = BeautifulSoup(html, "html.parser").select("div.job-search-card")
            pages += 1
            if not cards:
                break
            page_ids: set[str] = set()
            for card in cards:
                company = normalize_space(card.select_one(".base-search-card__subtitle").get_text(" ", strip=True) if card.select_one(".base-search-card__subtitle") else "")
                if company.lower() != "linkedin":
                    continue
                urn = card.get("data-entity-urn") or ""
                match = re.search(r"jobPosting:(\d+)", urn)
                link = card.select_one("a.base-card__full-link")
                jid = match.group(1) if match else ""
                if not jid or not link:
                    continue
                page_ids.add(jid)
                raw_count += 1
                if jid in seen:
                    continue
                seen.add(jid)
                title_node = card.select_one(".base-search-card__title")
                location_node = card.select_one(".job-search-card__location")
                date_node = card.select_one("time")
                location = normalize_space(location_node.get_text(" ", strip=True) if location_node else "")
                if location and not keep_us_or_unknown(location):
                    continue
                official = _clean_url(link.get("href") or "")
                jobs.append(make_job(
                    source="linkedin_company_official_careers",
                    company="LinkedIn",
                    title=normalize_space(title_node.get_text(" ", strip=True) if title_node else ""),
                    location=location,
                    job_id=jid,
                    posted_date=date_node.get("datetime") if date_node else "",
                    date_confidence="high" if date_node and date_node.get("datetime") else "unknown",
                    source_url=official,
                    official_url=official,
                    description="",
                    fetched_at=fetched_at,
                ))
            if query_ids and page_ids and page_ids <= query_ids:
                break
            query_ids.update(page_ids)
            if len(cards) < PAGE_SIZE:
                break
            time.sleep(0.2)
    return {
        "company": "LinkedIn",
        "source": "linkedin_company_official_careers",
        "method": "HTTP GET LinkedIn logged-out guest job search, company id 1337",
        "search_url": SEARCH,
        "search_urls": ["https://www.linkedin.com/company/linkedin/jobs/", SEARCH],
        "pagination": f"start=0,{PAGE_SIZE},...; company filter f_C={COMPANY_ID}",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }
