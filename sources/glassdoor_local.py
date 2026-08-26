#!/usr/bin/env python3
"""Glassdoor job-search adapter. LOCAL USE ONLY.

Parses Glassdoor's public search results HTML (job cards + JSON-LD). This is
best-effort: on captcha / security check / 403 / 429 it raises
``SourceUnavailable`` so the caller keeps the last good snapshot.

Do NOT run from GitHub Actions. Driven locally by launchd via
``local_sources.py``. Glassdoor's default result set is already recency-biased;
the pipeline re-sorts by first_seen / posted_date, so a wide window is fine.
"""

from __future__ import annotations

import re
import time
from typing import Dict, List
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

from .schema import (
    SourceUnavailable,
    is_us_location,
    make_job,
    normalize_space,
)

REQUEST_TIMEOUT = 25
POLITE_SLEEP_SECONDS = 2.0
# Glassdoor SRCH URLs are keyword-specific; keep a small, high-signal set.
# Each entry: (keyword label, search URL). fromAge=1 -> last day when honored.
SEARCH_URLS = {
    "software engineer": "https://www.glassdoor.com/Job/united-states-software-engineer-jobs-SRCH_IL.0,13_IN1_KO14,31.htm",
    "ai engineer": "https://www.glassdoor.com/Job/united-states-ai-engineer-jobs-SRCH_IL.0,13_IN1_KO14,25.htm",
    "machine learning engineer": "https://www.glassdoor.com/Job/united-states-machine-learning-engineer-jobs-SRCH_IL.0,13_IN1_KO14,39.htm",
    "data engineer": "https://www.glassdoor.com/Job/united-states-data-engineer-jobs-SRCH_IL.0,13_IN1_KO14,27.htm",
}


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
    if resp.status_code >= 400:
        raise SourceUnavailable(f"HTTP {resp.status_code}")
    low = resp.text[:5000].lower()
    if "please verify you are a human" in low or "security check" in low or "px-captcha" in low:
        raise SourceUnavailable("captcha / security check")


def _parse_cards(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select('[data-test="jobListing"]')
    rows: List[Dict[str, str]] = []
    for card in cards:
        title_el = card.select_one('[data-test="job-title"]')
        loc_el = card.select_one('[data-test="emp-location"]')
        age_el = card.select_one('[data-test="job-age"]')
        emp_el = card.select_one('[class*="EmployerProfile_compactEmployerName"]')
        snip_el = card.select_one('[data-test="descSnippet"]')
        href = title_el.get("href", "") if title_el else ""
        clean_url = href.split("?")[0]
        m = re.search(r"jl=(\d+)", href)
        job_id = m.group(1) if m else ""
        rows.append(
            make_job(
                source="glassdoor",
                company=normalize_space(emp_el.get_text() if emp_el else ""),
                title=normalize_space(title_el.get_text() if title_el else ""),
                location=normalize_space(loc_el.get_text() if loc_el else ""),
                job_id=job_id,
                posted_date=normalize_space(age_el.get_text() if age_el else ""),
                date_confidence="low",
                source_url=clean_url,
                official_url="",
                description=normalize_space(snip_el.get_text() if snip_el else ""),
            )
        )
    return rows


def scrape(session: requests.Session | None = None) -> List[Dict[str, str]]:
    """Return Glassdoor job rows. Raises SourceUnavailable on captcha/network."""
    session = session or _make_session()
    seen: set[str] = set()
    rows: List[Dict[str, str]] = []
    for _keyword, url in SEARCH_URLS.items():
        try:
            resp = session.get(url, timeout=REQUEST_TIMEOUT)
        except requests.RequestException as exc:
            raise SourceUnavailable(f"network error: {exc}") from exc
        _check_blocked(resp)
        for row in _parse_cards(resp.text):
            key = row.get("job_id") or row.get("source_url")
            if key and key in seen:
                continue
            if key:
                seen.add(key)
            if row["location"] and not is_us_location(row["location"]):
                continue
            rows.append(row)
        time.sleep(POLITE_SLEEP_SECONDS)
    return rows
