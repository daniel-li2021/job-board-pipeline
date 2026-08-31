"""Server-rendered Radancy career-site search adapter."""

from __future__ import annotations

import json
import time
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

PAGE_SIZE = 30
MAX_DETAILS = 100


def _soup(html: str):
    from bs4 import BeautifulSoup

    return BeautifulSoup(html, "html.parser")


def _cards(html: str, base_url: str = "") -> List[Tuple[str, str, str, str]]:
    soup = _soup(html)
    cards: List[Tuple[str, str, str, str]] = []
    for row in soup.select("table[data-controller*='table-results'] tbody tr[data-job-url]"):
        link = row.select_one(".job-search-results-title a")
        req = row.select_one(".job-search-results-requisition-identifiers")
        loc = row.select_one(".job-search-results-location")
        url = urljoin(base_url, normalize_space(row.get("data-job-url") or (link.get("href") if link else "")))
        jid = normalize_space(req.get_text(" ", strip=True) if req else "")
        title = normalize_space(link.get_text(" ", strip=True) if link else "")
        location = normalize_space(loc.get_text("; ", strip=True) if loc else "")
        if url and jid and title:
            cards.append((jid, url, title, location))
    for row in soup.select("li.search-results-list__list-item, #search-results-list li"):
        link = row.select_one("a.sr-job-link, a[data-job-id], a[href*='/job/']")
        if not link:
            continue
        href = normalize_space(link.get("href") or "")
        title_node = row.select_one("h2, h3")
        loc = row.select_one(".job-location")
        req = row.select_one(".jobId, .job-id")
        jid = normalize_space(link.get("data-job-id") or (req.get_text(" ", strip=True) if req else ""))
        jid = jid.removeprefix("Job ID:").strip()
        if not jid:
            jid = href.rstrip("/").split("/")[-1]
        title = normalize_space(title_node.get_text(" ", strip=True) if title_node else link.get_text(" ", strip=True))
        location = normalize_space(loc.get_text("; ", strip=True) if loc else "")
        url = urljoin(base_url, href)
        if url and jid and title and not any(card[0] == jid for card in cards):
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
    query_param: str = "query",
    page_param: str = "page",
    country_param: Optional[str] = "country_codes[]",
    country_value: str = "US",
    page_size: int = PAGE_SIZE,
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
            params = {query_param: query, page_param: page}
            if country_param:
                params[country_param] = country_value
            result = http_get(
                session,
                search_url,
                label=f"{company} career search",
                params=params,
            )
            pages += 1
            cards = _cards(result.text, search_url)
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
            if len(cards) < page_size:
                break
            time.sleep(0.2)

    return {
        "company": company,
        "source": source,
        "method": "HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD",
        "search_url": search_url,
        "search_urls": [search_url],
        "pagination": f"{page_param}=1,2,...; stop on empty/repeat/short page",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "detail_fetches": detail_fetches,
    }
