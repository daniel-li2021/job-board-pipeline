#!/usr/bin/env python3
"""LinkedIn guest job-search adapter. LOCAL USE ONLY.

Uses the public, unauthenticated guest endpoint
``/jobs-guest/jobs/api/seeMoreJobPostings/search`` which returns HTML job
cards. This is best-effort: on login wall / captcha / 403 / 429 it raises
``SourceUnavailable`` so the caller keeps the last good snapshot instead of
overwriting it with nothing.

Do NOT run this from GitHub Actions (datacenter IPs get blocked fast). It is
driven locally by launchd via ``local_sources.py``.

Filters (per plan):
  - f_TPR=r86400  : posted in the last 24h (wide window; pipeline re-sorts)
  - f_E=2,3       : entry + associate (captures realistic ~0-3 YOE / I-II)
  - geoId=103644278 + location=United States
  - keywords      : rotated across several engineering titles
"""

from __future__ import annotations

import time
from typing import Dict, List

import requests
from bs4 import BeautifulSoup

from .schema import (
    SourceUnavailable,
    is_us_location,
    make_job,
    normalize_space,
)

GUEST_SEARCH_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
US_GEO_ID = "103644278"
DEFAULT_KEYWORDS = [
    "software engineer",
    "software engineer i",
    "software engineer ii",
    "associate software engineer",
    "backend engineer",
    "full stack engineer",
    "platform engineer",
    "ai engineer",
    "applied ai engineer",
    "machine learning engineer",
    "data engineer",
    "forward deployed engineer",
]
EXPERIENCE_LEVEL_FILTER = "2,3"
PAGE_SIZE = 10
MAX_PAGES_PER_KEYWORD = 10
REQUEST_TIMEOUT = 25
POLITE_SLEEP_SECONDS = 1.2


def _make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml",
        }
    )
    return session


def _check_blocked(resp: requests.Response) -> None:
    if resp.status_code in (401, 403, 429):
        raise SourceUnavailable(f"blocked with HTTP {resp.status_code}")
    if resp.status_code == 999:  # LinkedIn's anti-bot status
        raise SourceUnavailable("blocked with HTTP 999 (LinkedIn anti-bot)")
    if resp.status_code >= 400:
        raise SourceUnavailable(f"HTTP {resp.status_code}")
    lowered = resp.text[:2000].lower()
    if "authwall" in lowered or "sign in to continue" in lowered or "captcha" in lowered:
        raise SourceUnavailable("login/captcha wall detected")


def _parse_cards(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("div", class_="base-card")
    rows: List[Dict[str, str]] = []
    for card in cards:
        title_tag = card.find("h3")
        company_tag = card.find("h4")
        loc_tag = card.find("span", class_="job-search-card__location")
        link_tag = card.find("a", class_="base-card__full-link") or card.find("a")
        time_tag = card.find("time")
        urn = card.get("data-entity-urn") or ""
        job_id = urn.split(":")[-1] if urn else ""
        location = normalize_space(loc_tag.get_text() if loc_tag else "")
        href = (link_tag.get("href") if link_tag else "") or ""
        # Strip tracking query string.
        clean_url = href.split("?")[0]
        rows.append(
            make_job(
                source="linkedin",
                company=normalize_space(company_tag.get_text() if company_tag else ""),
                title=normalize_space(title_tag.get_text() if title_tag else ""),
                location=location,
                job_id=normalize_space(job_id),
                posted_date=(time_tag.get("datetime") if time_tag else "") or "",
                date_confidence="low",  # LinkedIn shows reposts as fresh
                source_url=clean_url,
                official_url="",
            )
        )
    return rows


def scrape(
    keywords: List[str] | None = None,
    session: requests.Session | None = None,
) -> List[Dict[str, str]]:
    """Return LinkedIn job rows. Raises SourceUnavailable on anti-bot/network."""
    session = session or _make_session()
    keywords = keywords or DEFAULT_KEYWORDS
    seen: set[str] = set()
    rows: List[Dict[str, str]] = []
    for keyword in keywords:
        for page in range(MAX_PAGES_PER_KEYWORD):
            params = {
                "keywords": keyword,
                "location": "United States",
                "geoId": US_GEO_ID,
                "f_TPR": "r86400",
                "f_E": EXPERIENCE_LEVEL_FILTER,
                "start": page * PAGE_SIZE,
            }
            try:
                resp = session.get(GUEST_SEARCH_URL, params=params, timeout=REQUEST_TIMEOUT)
            except requests.RequestException as exc:
                raise SourceUnavailable(f"network error: {exc}") from exc
            _check_blocked(resp)
            page_rows = _parse_cards(resp.text)
            if not page_rows:
                break
            added = 0
            for row in page_rows:
                key = row.get("job_id") or row.get("source_url")
                if key and key in seen:
                    continue
                if key:
                    seen.add(key)
                # US filter; keep unknown locations (LinkedIn sometimes omits).
                if row["location"] and not is_us_location(row["location"]):
                    continue
                rows.append(row)
                added += 1
            if added == 0:
                break
            time.sleep(POLITE_SLEEP_SECONDS)
    return rows
