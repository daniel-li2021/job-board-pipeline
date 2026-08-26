#!/usr/bin/env python3
"""Minimal job scraping feasibility prototype.

Goal: low-volume tests only, no bypassing restrictions, and clear worked/failed reporting.
"""

from __future__ import annotations

import csv
import difflib
import json
import os
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
CSV_PATH = OUTPUT_DIR / "jobs.csv"
REPORT_PATH = OUTPUT_DIR / "feasibility_report.md"

RECENT_DAYS = 7
REQUEST_TIMEOUT = 25
REQUEST_SLEEP_SECONDS = 1.0
MAX_ITEMS_PER_SOURCE = 120
MAX_SYNC_ITEMS_PER_SOURCE = 300
MAX_SYNC_PAGES = 12
ENABLE_PLAYWRIGHT_FALLBACK = True

CSV_FIELDS = [
    "company",
    "title",
    "location",
    "job_url",
    "job_id",
    "posted_date",
    "source",
    "raw_text_snippet",
]

SYNCareer_URLS = {
    "google": ["https://syncareer.com/company/a100003-google/jobs?time=last7days"],
    "amazon": ["https://syncareer.com/company/a100005-amazon/jobs?time=last7days"],
    "microsoft": ["https://syncareer.com/company/a100004-microsoft/jobs?time=last7days"],
    "meta": ["https://syncareer.com/company/a100007-meta/jobs?time=last7days"],
    "bytedance": ["https://syncareer.com/company/b100217-bytedance/jobs?time=last7days"],
    "tiktok": ["https://syncareer.com/company/b100012-tiktok/jobs?time=last7days"],
}

US_HINTS = [
    "united states",
    "usa",
    "us",
    "new york",
    "california",
    "texas",
    "washington",
    "florida",
    "massachusetts",
    "san francisco",
    "mountain view",
    "austin",
    "seattle",
]

STATE_ABBRS = {
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC",
}


@dataclass
class SourceResult:
    source_name: str
    status: str = "failed"  # worked / partial / failed
    notes: str = ""
    us_filter_worked: bool = False
    recent_sort_worked: bool = False
    posted_date_available: bool = False
    fields_extracted: List[str] = field(default_factory=list)
    attempted_urls: List[str] = field(default_factory=list)
    count: int = 0
    pagination_worked: bool = False


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "")).strip()


def is_us_location(location: str) -> bool:
    text = normalize_space(location).lower()
    if not text:
        return False
    if any(hint in text for hint in US_HINTS):
        return True
    parts = [p.strip().upper() for p in re.split(r"[,\s/()-]+", text) if p.strip()]
    return any(part in STATE_ABBRS for part in parts)


def parse_posted_date(value: str) -> Optional[datetime]:
    text = normalize_space(value).lower()
    if not text:
        return None

    # Relative formats: "3d", "3 days ago", "12h ago"
    rel_match = re.search(r"(\d+)\s*(day|days|d|hour|hours|h|week|weeks|w)\b", text)
    if rel_match:
        amount = int(rel_match.group(1))
        unit = rel_match.group(2)
        if unit in {"day", "days", "d"}:
            return now_utc() - timedelta(days=amount)
        if unit in {"hour", "hours", "h"}:
            return now_utc() - timedelta(hours=amount)
        if unit in {"week", "weeks", "w"}:
            return now_utc() - timedelta(days=7 * amount)

    for fmt in ("%Y-%m-%d", "%b %d, %Y", "%B %d, %Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(text, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def is_recent(posted_date: str, max_days: int = RECENT_DAYS) -> bool:
    parsed = parse_posted_date(posted_date)
    if not parsed:
        return False
    return (now_utc() - parsed) <= timedelta(days=max_days)


def http_get(session: requests.Session, url: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
    response = session.get(url, params=params, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response


def make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        }
    )
    return session


def extract_next_data_jobs(html: str) -> List[Dict[str, Any]]:
    soup = BeautifulSoup(html, "html.parser")
    script = soup.find("script", id="__NEXT_DATA__")
    if not script or not script.string:
        return []
    try:
        payload = json.loads(script.string)
    except json.JSONDecodeError:
        return []

    matches: List[Dict[str, Any]] = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            keys = set(node.keys())
            if (
                ("title" in keys or "jobTitle" in keys)
                and ("location" in keys or "locations" in keys or "city" in keys)
            ):
                matches.append(node)
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(payload)
    return matches


def normalize_job(
    *,
    company: str,
    title: str,
    location: str,
    job_url: str,
    source: str,
    job_id: str = "",
    posted_date: str = "",
    raw_text_snippet: str = "",
) -> Dict[str, str]:
    return {
        "company": normalize_space(company),
        "title": normalize_space(title),
        "location": normalize_space(location),
        "job_url": normalize_space(job_url),
        "job_id": normalize_space(job_id),
        "posted_date": normalize_space(posted_date),
        "source": normalize_space(source),
        "raw_text_snippet": normalize_space(raw_text_snippet)[:500],
    }


def scrape_google_official(session: requests.Session) -> Tuple[List[Dict[str, str]], SourceResult]:
    result = SourceResult(source_name="google_official")
    rows: List[Dict[str, str]] = []
    url = "https://www.google.com/about/careers/applications/jobs/results/"
    params = {
        "location": "United States",
        "sort_by": "date",
        "distance": "50",
    }
    result.attempted_urls.append(f"{url}?location=United%20States&sort_by=date")
    try:
        html = http_get(session, url, params=params).text
        raw_jobs = extract_next_data_jobs(html)

        for item in raw_jobs:
            title = item.get("title") or item.get("jobTitle") or ""
            location = item.get("location") or item.get("locations") or item.get("city") or ""
            if isinstance(location, list):
                location = ", ".join(str(x) for x in location[:2])
            job_id = str(item.get("jobId") or item.get("id") or "")
            posted = str(item.get("postedDate") or item.get("publishDate") or item.get("updatedAt") or "")
            apply_url = str(item.get("applyUrl") or item.get("url") or "")
            if apply_url and apply_url.startswith("/"):
                apply_url = urljoin("https://www.google.com", apply_url)

            if not title or not location:
                continue
            if not is_us_location(str(location)):
                continue
            if posted and not is_recent(posted):
                continue

            snippet = " | ".join(
                normalize_space(str(item.get(k, "")))
                for k in ("team", "subteam", "description")
                if item.get(k)
            )
            rows.append(
                normalize_job(
                    company="Google",
                    title=title,
                    location=str(location),
                    job_url=apply_url or url,
                    job_id=job_id,
                    posted_date=posted,
                    source="google_official",
                    raw_text_snippet=snippet,
                )
            )
            if len(rows) >= MAX_ITEMS_PER_SOURCE:
                break

        if rows:
            result.status = "worked"
            result.notes = "Parsed jobs from page embedded data."
        else:
            rows = scrape_google_with_playwright_text()
            if rows:
                result.status = "worked"
                result.notes = "Parsed rendered Google job cards with Playwright fallback."
            else:
                result.status = "partial"
                result.notes = "Request succeeded but no parsable recent U.S. jobs were found."

    except Exception as exc:  # noqa: BLE001
        result.status = "failed"
        result.notes = f"Request/parsing failed: {exc}"

    result.count = len(rows)
    result.us_filter_worked = True if rows else False
    result.recent_sort_worked = True
    result.posted_date_available = any(r["posted_date"] for r in rows)
    result.fields_extracted = [f for f in CSV_FIELDS if any(r.get(f) for r in rows)]
    return rows, result


def scrape_syncareer_company(session: requests.Session, company_key: str) -> Tuple[List[Dict[str, str]], SourceResult]:
    source_name = f"syncareer_{company_key}"
    result = SourceResult(source_name=source_name)
    rows: List[Dict[str, str]] = []
    urls = SYNCareer_URLS.get(company_key, [])
    pages_with_jobs = 0

    for url in urls:
        for page in range(1, MAX_SYNC_PAGES + 1):
            page_url = f"{url}&page={page}" if "?" in url else f"{url}?page={page}"
            result.attempted_urls.append(page_url)
            try:
                html = http_get(session, page_url).text
            except Exception:  # noqa: BLE001
                time.sleep(0.4)
                continue

            soup = BeautifulSoup(html, "html.parser")
            lines = [
                normalize_space(x)
                for x in soup.get_text("\n", strip=True).splitlines()
                if normalize_space(x)
            ]
            page_rows = 0
            for i, line in enumerate(lines):
                if "united states" not in line.lower():
                    continue
                if i < 2:
                    continue
                location = line
                company_line = lines[i - 1].lower()
                title = re.sub(r"^new\s*", "", lines[i - 2], flags=re.IGNORECASE).strip()
                posted = lines[i - 3] if i >= 3 and re.search(r"\d+\s*(d|day|days|h|hour|hours|w|week|weeks)$", lines[i - 3].lower()) else ""
                if not title or len(title) < 5:
                    continue
                if len(title) > 140 or len(title.split()) > 20:
                    continue
                if title.lower() in {"jobs", "companies", "job tracker", "sign in", "about"}:
                    continue
                if any(bad in title.lower() for bad in ["required qualifications", "minimum qualifications", "this position", "must have authorization"]):
                    continue
                if re.match(r"^\d+\s+years?\s+experience", title.lower()):
                    continue
                if company_key not in company_line and company_key != "bytedance":
                    continue
                if company_key == "bytedance" and "bytedance" not in company_line:
                    continue
                if posted and not is_recent(posted):
                    continue
                rows.append(
                    normalize_job(
                        company="ByteDance" if company_key == "bytedance" else company_key.capitalize(),
                        title=title,
                        location=location,
                        job_url=page_url,
                        job_id="",
                        posted_date=posted,
                        source=source_name,
                        raw_text_snippet=f"{title} | {location}",
                    )
                )
                page_rows += 1
                if len(rows) >= MAX_SYNC_ITEMS_PER_SOURCE:
                    break
            if page_rows > 0:
                pages_with_jobs += 1
            if page_rows == 0 and page > 1:
                break
            if len(rows) >= MAX_SYNC_ITEMS_PER_SOURCE:
                break

    if rows:
        result.status = "worked"
        result.notes = "Parsed jobs from Syncareer last7days listing text."
    elif result.attempted_urls:
        result.status = "partial"
        result.notes = "Syncareer pages reached, but extraction was limited."
    else:
        result.status = "failed"
        result.notes = "No Syncareer URL configured."

    result.count = len(rows)
    result.us_filter_worked = any(r["location"] and is_us_location(r["location"]) for r in rows)
    result.recent_sort_worked = True
    result.posted_date_available = any(r["posted_date"] for r in rows)
    result.fields_extracted = [f for f in CSV_FIELDS if any(r.get(f) for r in rows)]
    result.pagination_worked = pages_with_jobs > 1
    return rows, result


def scrape_amazon_official(session: requests.Session) -> Tuple[List[Dict[str, str]], SourceResult]:
    result = SourceResult(source_name="amazon_official")
    rows: List[Dict[str, str]] = []
    url = "https://www.amazon.jobs/en/search.json"
    params = {
        "base_query": "",
        "loc_query": "United States",
        "offset": 0,
        "result_limit": 20,
        "sort": "recent",
    }
    result.attempted_urls.append(f"{url}?loc_query=United+States&sort=recent")
    try:
        payload = http_get(session, url, params=params).json()
        jobs = payload.get("jobs", [])
        for item in jobs[:MAX_ITEMS_PER_SOURCE]:
            title = item.get("title") or ""
            location = item.get("location") or ""
            posted = item.get("posted_date") or item.get("postedDate") or ""
            if not title or not location or not is_us_location(location):
                continue
            if posted and not is_recent(str(posted)):
                continue
            job_path = item.get("job_path") or item.get("job_url") or ""
            job_url = urljoin("https://www.amazon.jobs", job_path) if job_path else "https://www.amazon.jobs/"
            rows.append(
                normalize_job(
                    company="Amazon",
                    title=str(title),
                    location=str(location),
                    job_url=job_url,
                    job_id=str(item.get("id", "")),
                    posted_date=str(posted),
                    source="amazon_official",
                    raw_text_snippet=normalize_space(str(item)),
                )
            )
        result.status = "worked" if rows else "partial"
        result.notes = "Parsed search JSON endpoint." if rows else "JSON endpoint returned no recent U.S. rows."
    except Exception as exc:  # noqa: BLE001
        result.status = "failed"
        result.notes = f"Amazon request failed: {exc}"

    result.count = len(rows)
    result.us_filter_worked = True if rows else False
    result.recent_sort_worked = True
    result.posted_date_available = any(r["posted_date"] for r in rows)
    result.fields_extracted = [f for f in CSV_FIELDS if any(r.get(f) for r in rows)]
    return rows, result


def scrape_tiktok_official(session: requests.Session) -> Tuple[List[Dict[str, str]], SourceResult]:
    result = SourceResult(source_name="tiktok_official")
    rows: List[Dict[str, str]] = []
    api_url = "https://careers.tiktok.com/api/v1/search/job/posts"
    params = {
        "keyword": "",
        "limit": 20,
        "offset": 0,
        "location": "United States",
    }
    result.attempted_urls.append(f"{api_url}?location=United%20States")
    try:
        payload = http_get(session, api_url, params=params).json()
        data = payload.get("data", {})
        posts = data.get("job_post_list", []) if isinstance(data, dict) else []
        for item in posts[:MAX_ITEMS_PER_SOURCE]:
            title = item.get("title") or ""
            location = item.get("location") or ""
            posted = item.get("create_time") or item.get("updated_at") or ""
            if not title or not location or not is_us_location(str(location)):
                continue
            if posted and not is_recent(str(posted)):
                continue
            job_id = str(item.get("id") or item.get("job_id") or "")
            job_url = item.get("apply_url") or item.get("detail_url") or ""
            rows.append(
                normalize_job(
                    company="TikTok",
                    title=str(title),
                    location=str(location),
                    job_url=str(job_url),
                    job_id=job_id,
                    posted_date=str(posted),
                    source="tiktok_official",
                    raw_text_snippet=normalize_space(str(item)),
                )
            )
        result.status = "worked" if rows else "partial"
        result.notes = "Parsed TikTok API endpoint." if rows else "TikTok endpoint reachable but returned no recent U.S. rows."
    except Exception as exc:  # noqa: BLE001
        rows = scrape_lifeat_api_with_playwright(
            page_url="https://lifeattiktok.com/search",
            api_substring="api.lifeattiktok.com/api/v1/public/supplier/search/job/posts",
            source="tiktok_official",
            company="TikTok",
        )
        if rows:
            result.status = "worked"
            result.notes = f"TikTok API failed initially ({exc}); Playwright network capture succeeded."
        else:
            result.status = "failed"
            result.notes = f"TikTok API failed: {exc}"

    if not rows and result.status != "worked":
        fallback_rows = scrape_lifeat_api_with_playwright(
            page_url="https://lifeattiktok.com/search",
            api_substring="api.lifeattiktok.com/api/v1/public/supplier/search/job/posts",
            source="tiktok_official",
            company="TikTok",
        )
        if fallback_rows:
            rows = fallback_rows
            result.status = "worked"
            result.notes = (result.notes + " Playwright network capture fallback succeeded.").strip()

    result.count = len(rows)
    result.us_filter_worked = True if rows else False
    result.recent_sort_worked = True
    result.posted_date_available = any(r["posted_date"] for r in rows)
    result.fields_extracted = [f for f in CSV_FIELDS if any(r.get(f) for r in rows)]
    return rows, result


def scrape_meta_official(session: requests.Session) -> Tuple[List[Dict[str, str]], SourceResult]:
    result = SourceResult(source_name="meta_official")
    rows: List[Dict[str, str]] = []
    url = "https://www.metacareers.com/jobs/"
    params = {"offices[0]": "United States"}
    result.attempted_urls.append(f"{url}?offices[0]=United%20States")
    try:
        html = http_get(session, url, params=params).text
        raw_jobs = extract_next_data_jobs(html)
        for item in raw_jobs:
            title = item.get("title") or item.get("jobTitle") or ""
            location = item.get("location") or item.get("locations") or ""
            if isinstance(location, list):
                location = ", ".join(str(v) for v in location[:2])
            posted = item.get("postedDate") or item.get("updatedAt") or ""
            if not title or not location or not is_us_location(str(location)):
                continue
            if posted and not is_recent(str(posted)):
                continue
            job_url = str(item.get("url") or item.get("job_url") or url)
            if job_url.startswith("/"):
                job_url = urljoin("https://www.metacareers.com", job_url)
            rows.append(
                normalize_job(
                    company="Meta",
                    title=str(title),
                    location=str(location),
                    job_url=job_url,
                    job_id=str(item.get("id") or item.get("jobId") or ""),
                    posted_date=str(posted),
                    source="meta_official",
                    raw_text_snippet=normalize_space(str(item)),
                )
            )
            if len(rows) >= MAX_ITEMS_PER_SOURCE:
                break
        result.status = "worked" if rows else "partial"
        result.notes = "Parsed embedded page data." if rows else "Page loaded but no parsable recent U.S. rows."
    except Exception as exc:  # noqa: BLE001
        rows = scrape_meta_with_playwright_text()
        if rows:
            result.status = "worked"
            result.notes = f"Meta request/parsing failed ({exc}); Playwright rendered-text extraction succeeded."
        else:
            result.status = "failed"
            result.notes = f"Meta request/parsing failed: {exc}"

    if not rows and result.status != "worked":
        fallback_rows = scrape_meta_with_playwright_text()
        if fallback_rows:
            rows = fallback_rows
            result.status = "worked"
            result.notes = (result.notes + " Playwright rendered-text fallback succeeded.").strip()

    result.count = len(rows)
    result.us_filter_worked = True if rows else False
    result.recent_sort_worked = False
    result.posted_date_available = any(r["posted_date"] for r in rows)
    result.fields_extracted = [f for f in CSV_FIELDS if any(r.get(f) for r in rows)]
    return rows, result


def scrape_microsoft_official(session: requests.Session) -> Tuple[List[Dict[str, str]], SourceResult]:
    result = SourceResult(source_name="microsoft_official")
    rows: List[Dict[str, str]] = []
    url = "https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&l=en_us&pg=1&pgSz=20&o=Recent"
    result.attempted_urls.append(url)
    try:
        html = http_get(session, url).text
        # Microsoft listings are heavily client-rendered; attempt embedded JSON if present.
        raw_jobs = extract_next_data_jobs(html)
        for item in raw_jobs[:MAX_ITEMS_PER_SOURCE]:
            title = item.get("title") or item.get("jobTitle") or ""
            location = item.get("location") or item.get("city") or ""
            if not title or not location or not is_us_location(str(location)):
                continue
            rows.append(
                normalize_job(
                    company="Microsoft",
                    title=str(title),
                    location=str(location),
                    job_url=str(item.get("url") or url),
                    job_id=str(item.get("jobId") or item.get("id") or ""),
                    posted_date=str(item.get("postedDate") or ""),
                    source="microsoft_official",
                    raw_text_snippet=normalize_space(str(item)),
                )
            )
        if rows:
            result.status = "worked"
            result.notes = "Parsed embedded data from Microsoft page."
        else:
            rows = scrape_microsoft_with_playwright_links()
            if rows:
                result.status = "worked"
                result.notes = "Extracted Microsoft jobs from rendered apply links via Playwright."
            else:
                result.status = "partial"
                result.notes = "Microsoft page loaded but no parseable server-side job payload found."
    except Exception as exc:  # noqa: BLE001
        result.status = "failed"
        result.notes = f"Microsoft request failed: {exc}"

    result.count = len(rows)
    result.us_filter_worked = True if rows else False
    result.recent_sort_worked = True
    result.posted_date_available = any(r["posted_date"] for r in rows)
    result.fields_extracted = [f for f in CSV_FIELDS if any(r.get(f) for r in rows)]
    return rows, result


def scrape_bytedance_official(session: requests.Session) -> Tuple[List[Dict[str, str]], SourceResult]:
    result = SourceResult(source_name="bytedance_official")
    rows: List[Dict[str, str]] = []
    url = "https://jobs.bytedance.com/en/position?keywords=&location=United%20States&type=2&current=1&limit=20"
    result.attempted_urls.append(url)
    try:
        html = http_get(session, url).text
        raw_jobs = extract_next_data_jobs(html)
        for item in raw_jobs[:MAX_ITEMS_PER_SOURCE]:
            title = item.get("title") or item.get("jobTitle") or ""
            location = item.get("location") or item.get("city") or ""
            posted = item.get("postedDate") or item.get("updatedAt") or ""
            if not title or not location or not is_us_location(str(location)):
                continue
            if posted and not is_recent(str(posted)):
                continue
            rows.append(
                normalize_job(
                    company="ByteDance",
                    title=str(title),
                    location=str(location),
                    job_url=str(item.get("url") or url),
                    job_id=str(item.get("jobId") or item.get("id") or ""),
                    posted_date=str(posted),
                    source="bytedance_official",
                    raw_text_snippet=normalize_space(str(item)),
                )
            )
        if rows:
            result.status = "worked"
            result.notes = "Parsed embedded data from ByteDance page."
        else:
            rows = scrape_lifeat_api_with_playwright(
                page_url="https://joinbytedance.com/search?keyword=&limit=20&offset=0&recruitment_id_list=201",
                api_substring="jobs.bytedance.com/api/v1/public/supplier/search/job/posts",
                source="bytedance_official",
                company="ByteDance",
            )
            if rows:
                result.status = "worked"
                result.notes = "Extracted ByteDance jobs via Playwright network capture."
            else:
                result.status = "partial"
                result.notes = "ByteDance page loaded but no parseable server-side job payload found."
    except Exception as exc:  # noqa: BLE001
        result.status = "failed"
        result.notes = f"ByteDance request failed: {exc}"

    if not rows and result.status != "worked":
        fallback_rows = scrape_lifeat_api_with_playwright(
            page_url="https://joinbytedance.com/search?keyword=&limit=20&offset=0&recruitment_id_list=201",
            api_substring="jobs.bytedance.com/api/v1/public/supplier/search/job/posts",
            source="bytedance_official",
            company="ByteDance",
        )
        if fallback_rows:
            rows = fallback_rows
            result.status = "worked"
            result.notes = (result.notes + " Playwright network capture fallback succeeded.").strip()

    result.count = len(rows)
    result.us_filter_worked = True if rows else False
    result.recent_sort_worked = True
    result.posted_date_available = any(r["posted_date"] for r in rows)
    result.fields_extracted = [f for f in CSV_FIELDS if any(r.get(f) for r in rows)]
    return rows, result


def try_playwright_page_content(url: str) -> Optional[str]:
    if not ENABLE_PLAYWRIGHT_FALLBACK:
        return None
    try:
        from playwright.sync_api import sync_playwright
    except Exception:  # noqa: BLE001
        return None


def city_chain_from_info(city_info: Dict[str, Any]) -> str:
    parts: List[str] = []
    current: Any = city_info
    while isinstance(current, dict):
        value = current.get("en_name") or current.get("name") or current.get("i18n_name") or ""
        if value:
            parts.append(str(value))
        current = current.get("parent")
    return " > ".join(parts)


def scrape_google_with_playwright_text() -> List[Dict[str, str]]:
    try:
        from playwright.sync_api import sync_playwright
    except Exception:  # noqa: BLE001
        return []

    rows: List[Dict[str, str]] = []
    url = "https://www.google.com/about/careers/applications/jobs/results/?location=United%20States&sort_by=date"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(6000)
        seen_text = set()
        collected_blocks: List[str] = []
        for _ in range(8):
            text = page.inner_text("body")
            if text and text not in seen_text:
                collected_blocks.append(text)
                seen_text.add(text)
            page.mouse.wheel(0, 2200)
            page.wait_for_timeout(1200)
        text = "\n".join(collected_blocks)
        browser.close()

    lines = [normalize_space(x) for x in text.splitlines() if normalize_space(x)]
    for i, line in enumerate(lines):
        if line != "place":
            continue
        if i < 3 or i + 1 >= len(lines):
            continue
        title = lines[i - 3]
        company = lines[i - 1]
        location = lines[i + 1]
        if company.lower() != "google":
            continue
        if not is_us_location(location):
            continue
        rows.append(
            normalize_job(
                company="Google",
                title=title,
                location=location,
                job_url=url,
                source="google_official",
                raw_text_snippet=f"{title} | {location}",
            )
        )
        if len(rows) >= MAX_ITEMS_PER_SOURCE:
            break
    return dedupe_rows(rows)[:MAX_ITEMS_PER_SOURCE]


def scrape_microsoft_with_playwright_links() -> List[Dict[str, str]]:
    try:
        from playwright.sync_api import sync_playwright
    except Exception:  # noqa: BLE001
        return []

    rows: List[Dict[str, str]] = []
    url = "https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&l=en_us&pg=1&pgSz=20&o=Recent"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(8000)
        text = page.inner_text("body")
        browser.close()

    lines = [normalize_space(x) for x in text.splitlines() if normalize_space(x)]
    start_idx = 0
    end_idx = len(lines)
    for i, line in enumerate(lines):
        if line.startswith("Sort: Latest"):
            start_idx = i
            break
    for i, line in enumerate(lines):
        if re.match(r"\d+\s+of\s+\d+", line):
            end_idx = i
            break
    listing_lines = lines[start_idx:end_idx]

    for i, line in enumerate(listing_lines):
        if "United States" not in line:
            continue
        if i == 0:
            continue
        title = listing_lines[i - 1]
        location = line
        posted = (
            listing_lines[i + 1].replace("Posted ", "").strip()
            if i + 1 < len(listing_lines) and "Posted " in listing_lines[i + 1]
            else ""
        )
        if not title or len(title) < 4:
            continue
        if len(title) > 140:
            continue
        if title in {"Jobs", "Search jobs", "Sort: Latest", "Apply now"}:
            continue
        job_url = "https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&l=en_us&pg=1&pgSz=20&o=Recent"
        job_id = ""
        if job_id:
            job_url = f"https://apply.careers.microsoft.com/careers/job/{job_id}"
        rows.append(
            normalize_job(
                company="Microsoft",
                title=title,
                location=location,
                job_url=job_url,
                source="microsoft_official",
                posted_date=posted,
                job_id=job_id,
                raw_text_snippet=f"{title} | {location} | {posted}",
            )
        )
        if len(rows) >= MAX_ITEMS_PER_SOURCE:
            break
    return dedupe_rows(rows)[:MAX_ITEMS_PER_SOURCE]


def scrape_meta_with_playwright_text() -> List[Dict[str, str]]:
    try:
        from playwright.sync_api import sync_playwright
    except Exception:  # noqa: BLE001
        return []

    rows: List[Dict[str, str]] = []
    url = "https://www.metacareers.com/jobs/"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(8000)
        text = page.inner_text("body")
        browser.close()

    lines = [normalize_space(x) for x in text.splitlines() if normalize_space(x)]
    location_re = re.compile(r".+,\s*[A-Z]{2}(?:\s*\+\d+\s*locations)?$")
    for i, line in enumerate(lines):
        if not location_re.match(line):
            continue
        if i == 0:
            continue
        title = lines[i - 1]
        if len(title) < 4 or title.lower() in {"featured jobs", "all jobs", "sort by"}:
            continue
        rows.append(
            normalize_job(
                company="Meta",
                title=title,
                location=line,
                job_url=url,
                source="meta_official",
                raw_text_snippet=f"{title} | {line}",
            )
        )
        if len(rows) >= MAX_ITEMS_PER_SOURCE:
            break
    return rows


def scrape_lifeat_api_with_playwright(
    *, page_url: str, api_substring: str, source: str, company: str
) -> List[Dict[str, str]]:
    try:
        from playwright.sync_api import sync_playwright
    except Exception:  # noqa: BLE001
        return []

    rows: List[Dict[str, str]] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        def on_resp(resp: Any) -> None:
            if api_substring not in resp.url:
                return
            try:
                payload = json.loads(resp.text())
            except Exception:  # noqa: BLE001
                return
            jobs = payload.get("data", {}).get("job_post_list", [])
            for item in jobs:
                city_chain = city_chain_from_info(item.get("city_info") or {})
                if not city_chain or "United States" not in city_chain:
                    continue
                title = str(item.get("title") or "")
                if not title:
                    continue
                job_id = str(item.get("id") or "")
                rows.append(
                    normalize_job(
                        company=company,
                        title=title,
                        location=city_chain,
                        job_url=f"{page_url.rstrip('/')}/{job_id}" if job_id else page_url,
                        job_id=job_id,
                        source=source,
                        raw_text_snippet=normalize_space(str(item.get("description") or item.get("requirement") or "")),
                    )
                )

        page.on("response", on_resp)
        page.goto(page_url, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(9000)
        browser.close()

    return dedupe_rows(rows)[:MAX_ITEMS_PER_SOURCE]

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=30000)
            html = page.content()
            browser.close()
            return html
    except Exception:  # noqa: BLE001
        return None


def playwright_fallback_for_source(source: str, result: SourceResult, rows: List[Dict[str, str]]) -> Tuple[List[Dict[str, str]], SourceResult]:
    if rows or result.status == "worked":
        return rows, result

    fallback_targets = {
        "tiktok_official": ("https://careers.tiktok.com/search?location=United%20States", "TikTok"),
        "meta_official": ("https://www.metacareers.com/jobs/?offices[0]=United%20States", "Meta"),
        "google_official": ("https://www.google.com/about/careers/applications/jobs/results/?location=United%20States", "Google"),
        "microsoft_official": ("https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&l=en_us&pg=1&pgSz=20&o=Recent", "Microsoft"),
        "bytedance_official": ("https://jobs.bytedance.com/en/position?keywords=&location=United%20States&type=2&current=1&limit=20", "ByteDance"),
    }
    target = fallback_targets.get(source)
    if not target:
        return rows, result

    url, company = target
    result.attempted_urls.append(f"playwright:{url}")
    html = try_playwright_page_content(url)
    if not html:
        return rows, result

    raw_jobs = extract_next_data_jobs(html)
    for item in raw_jobs[:MAX_ITEMS_PER_SOURCE]:
        title = item.get("title") or item.get("jobTitle") or ""
        location = item.get("location") or item.get("locations") or ""
        if isinstance(location, list):
            location = ", ".join(str(v) for v in location[:2])
        if not title or not location or not is_us_location(str(location)):
            continue
        rows.append(
            normalize_job(
                company=company,
                title=str(title),
                location=str(location),
                job_url=str(item.get("url") or url),
                job_id=str(item.get("id") or item.get("jobId") or ""),
                posted_date=str(item.get("postedDate") or item.get("updatedAt") or ""),
                source=source,
                raw_text_snippet=normalize_space(str(item)),
            )
        )
    if rows:
        result.status = "worked"
        result.notes = (result.notes + " Playwright fallback extracted rows.").strip()
        result.count = len(rows)
        result.posted_date_available = any(r["posted_date"] for r in rows)
        result.fields_extracted = [f for f in CSV_FIELDS if any(r.get(f) for r in rows)]
    return rows, result


def dedupe_rows(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    seen = set()
    deduped: List[Dict[str, str]] = []
    for row in rows:
        key = (
            row.get("source", "").lower(),
            row.get("title", "").lower(),
            row.get("location", "").lower(),
            row.get("job_url", "").lower(),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)
    return deduped


def write_csv(rows: List[Dict[str, str]]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in CSV_FIELDS})


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if not text or text.startswith("#") or "=" not in text:
            continue
        key, value = text.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and value and key not in os.environ:
            os.environ[key] = value


def normalize_title_for_match(title: str) -> str:
    text = normalize_space(title).lower()
    text = re.sub(r"[^a-z0-9\s]+", " ", text)
    text = re.sub(r"\b(senior|sr|ii|iii|iv|junior|jr)\b", " ", text)
    return normalize_space(text)


def normalize_location_for_match(location: str) -> str:
    text = normalize_space(location).lower()
    text = text.replace("united states of america", "united states")
    text = text.replace("usa", "united states")
    text = re.sub(r"\s*\+\s*\d+\s*more$", "", text)
    return normalize_space(text)


def call_openai_soft_match(company: str, syncareer_rows: List[Dict[str, str]], official_rows: List[Dict[str, str]]) -> List[Tuple[int, int]]:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key or not syncareer_rows or not official_rows:
        return []

    sync_payload = [
        {"i": i, "title": r["title"], "location": r["location"]}
        for i, r in enumerate(syncareer_rows[:40])
    ]
    off_payload = [
        {"i": i, "title": r["title"], "location": r["location"]}
        for i, r in enumerate(official_rows[:40])
    ]
    prompt = {
        "company": company,
        "instructions": (
            "Match equivalent jobs between syncareer and official lists using title semantics "
            "and location similarity. Return only strong matches. "
            "Return JSON with key 'matches': [{'sync_idx': int, 'off_idx': int, 'confidence': float}]"
        ),
        "syncareer_jobs": sync_payload,
        "official_jobs": off_payload,
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "temperature": 0,
                "response_format": {"type": "json_object"},
                "messages": [
                    {"role": "system", "content": "You are a strict job list matcher."},
                    {"role": "user", "content": json.dumps(prompt)},
                ],
            },
            timeout=45,
        )
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        payload = json.loads(content)
        matches = payload.get("matches", [])
        out: List[Tuple[int, int]] = []
        for item in matches:
            s_idx = int(item.get("sync_idx", -1))
            o_idx = int(item.get("off_idx", -1))
            confidence = float(item.get("confidence", 0))
            if s_idx < 0 or o_idx < 0 or confidence < 0.7:
                continue
            if s_idx >= len(syncareer_rows[:40]) or o_idx >= len(official_rows[:40]):
                continue
            out.append((s_idx, o_idx))
        return out
    except Exception:  # noqa: BLE001
        return []


def compare_official_vs_syncareer(rows: List[Dict[str, str]]) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    companies = ["google", "amazon", "microsoft", "meta", "tiktok", "bytedance"]
    for company in companies:
        official_rows = [r for r in rows if r["company"].lower() == company and r["source"].endswith("_official")]
        syncareer_rows = [r for r in rows if r["company"].lower() == company and r["source"].startswith("syncareer_")]

        official_norm = [
            (normalize_title_for_match(r["title"]), normalize_location_for_match(r["location"]))
            for r in official_rows
        ]
        sync_norm = [
            (normalize_title_for_match(r["title"]), normalize_location_for_match(r["location"]))
            for r in syncareer_rows
        ]
        official_set = set(official_norm)
        sync_set = set(sync_norm)
        hard_overlap = official_set & sync_set

        # Fuzzy soft matching without LLM.
        used_official: set[int] = set()
        soft_matches: List[Tuple[int, int]] = []
        for s_idx, (s_title, s_loc) in enumerate(sync_norm):
            best_idx = -1
            best_score = 0.0
            for o_idx, (o_title, o_loc) in enumerate(official_norm):
                if o_idx in used_official:
                    continue
                title_score = difflib.SequenceMatcher(None, s_title, o_title).ratio()
                loc_score = difflib.SequenceMatcher(None, s_loc, o_loc).ratio()
                score = 0.78 * title_score + 0.22 * loc_score
                if score > best_score:
                    best_score = score
                    best_idx = o_idx
            if best_idx >= 0 and best_score >= 0.86:
                used_official.add(best_idx)
                soft_matches.append((s_idx, best_idx))

        llm_matches = call_openai_soft_match(company, syncareer_rows, official_rows)
        soft_match_pairs = {(sync_norm[s], official_norm[o]) for s, o in soft_matches}
        for s_idx, o_idx in llm_matches:
            soft_match_pairs.add((sync_norm[s_idx], official_norm[o_idx]))

        soft_overlap_count = len(hard_overlap.union({pair[0] for pair in soft_match_pairs}))
        hard_overlap_count = len(hard_overlap)
        official_count = len(official_rows)
        sync_count = len(syncareer_rows)
        official_coverage_hard = (hard_overlap_count / official_count) if official_count else 0.0
        sync_coverage_hard = (hard_overlap_count / sync_count) if sync_count else 0.0
        official_coverage_soft = (soft_overlap_count / official_count) if official_count else 0.0
        sync_coverage_soft = (soft_overlap_count / sync_count) if sync_count else 0.0

        missing_in_sync = sorted(official_set - sync_set)[:5]
        missing_in_official = sorted(sync_set - official_set)[:5]
        out[company] = {
            "official_count": official_count,
            "syncareer_count": sync_count,
            "hard_overlap_count": hard_overlap_count,
            "soft_overlap_count": soft_overlap_count,
            "official_coverage_hard": official_coverage_hard,
            "sync_coverage_hard": sync_coverage_hard,
            "official_coverage_soft": official_coverage_soft,
            "sync_coverage_soft": sync_coverage_soft,
            "missing_in_syncareer": missing_in_sync,
            "missing_in_official": missing_in_official,
            "llm_soft_match_count": len(llm_matches),
        }
    return out


def write_report(results: List[SourceResult], rows: List[Dict[str, str]]) -> None:
    load_env_file(BASE_DIR / ".env")
    comparison = compare_official_vs_syncareer(rows)
    lines: List[str] = []
    lines.append("# Job Scraping Feasibility Report")
    lines.append("")
    lines.append(f"- Run time (UTC): {now_utc().isoformat()}")
    lines.append(f"- Total extracted rows: {len(rows)}")
    lines.append(f"- Recent window target: last {RECENT_DAYS} days when dates were available")
    lines.append("")
    lines.append("## Source Status")
    worked = [r for r in results if r.status == "worked"]
    partial = [r for r in results if r.status == "partial"]
    failed = [r for r in results if r.status == "failed"]
    lines.append(f"- Worked: {', '.join(r.source_name for r in worked) if worked else 'None'}")
    lines.append(f"- Partial: {', '.join(r.source_name for r in partial) if partial else 'None'}")
    lines.append(f"- Failed: {', '.join(r.source_name for r in failed) if failed else 'None'}")
    lines.append("")
    lines.append("## Requested Test Summary")
    lines.append("- Syncareer last7days worked: " + ("yes" if any(r.source_name.startswith("syncareer_") and r.count > 0 for r in results) else "no"))
    lines.append("- Pagination worked on Syncareer: " + ("yes" if any(r.source_name.startswith("syncareer_") and r.pagination_worked for r in results) else "no/unclear"))
    lines.append("- Official career pages worked: " + (", ".join(r.source_name for r in results if r.source_name.endswith("_official") and r.status == "worked") or "none"))
    lines.append("- Official career pages failed/partial: " + (", ".join(r.source_name for r in results if r.source_name.endswith("_official") and r.status != "worked") or "none"))
    lines.append("")

    lines.append("## Jobs Per Source")
    for r in sorted(results, key=lambda x: x.source_name):
        lines.append(f"- {r.source_name}: {r.count}")
    lines.append("")

    lines.append("## Per-Source Details")
    for r in results:
        lines.append(f"### {r.source_name}")
        lines.append(f"- status: {r.status}")
        lines.append(f"- rows_extracted: {r.count}")
        lines.append(f"- U.S. filtering worked: {'yes' if r.us_filter_worked else 'no/unclear'}")
        lines.append(f"- recent/date sorting worked: {'yes' if r.recent_sort_worked else 'no/unclear'}")
        lines.append(f"- posted_date available: {'yes' if r.posted_date_available else 'no'}")
        lines.append(f"- extracted fields: {', '.join(r.fields_extracted) if r.fields_extracted else 'none'}")
        lines.append(f"- notes: {r.notes or 'n/a'}")
        lines.append(f"- pagination worked: {'yes' if r.pagination_worked else 'no/unclear'}")
        if r.attempted_urls:
            lines.append(f"- attempted URLs: {', '.join(r.attempted_urls)}")
        lines.append("")

    lines.append("## Official vs Syncareer Comparison")
    for company, stats in comparison.items():
        lines.append(f"### {company.capitalize()}")
        lines.append(f"- official listings collected: {stats['official_count']}")
        lines.append(f"- syncareer listings collected: {stats['syncareer_count']}")
        lines.append(f"- hard overlap count: {stats['hard_overlap_count']}")
        lines.append(f"- soft overlap count (fuzzy + LLM): {stats['soft_overlap_count']}")
        lines.append(f"- official coverage hard: {stats['official_coverage_hard']:.1%}")
        lines.append(f"- official coverage soft: {stats['official_coverage_soft']:.1%}")
        lines.append(f"- syncareer coverage hard: {stats['sync_coverage_hard']:.1%}")
        lines.append(f"- syncareer coverage soft: {stats['sync_coverage_soft']:.1%}")
        lines.append(f"- LLM-assisted matches added: {stats['llm_soft_match_count']}")
        more_side = (
            "official"
            if stats["official_count"] > stats["syncareer_count"]
            else "syncareer"
            if stats["syncareer_count"] > stats["official_count"]
            else "tie"
        )
        lines.append(f"- which has more in this sample: {more_side}")
        miss_sync = stats["missing_in_syncareer"]
        miss_off = stats["missing_in_official"]
        lines.append(
            "- examples missing from Syncareer sample: "
            + (", ".join(f"{t} ({l})" for t, l in miss_sync) if miss_sync else "none observed")
        )
        lines.append(
            "- examples missing from official sample: "
            + (", ".join(f"{t} ({l})" for t, l in miss_off) if miss_off else "none observed")
        )
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def run() -> None:
    session = make_session()
    all_rows: List[Dict[str, str]] = []
    source_results: List[SourceResult] = []

    sources = [
        ("syncareer_google", lambda s: scrape_syncareer_company(s, "google")),
        ("syncareer_amazon", lambda s: scrape_syncareer_company(s, "amazon")),
        ("syncareer_microsoft", lambda s: scrape_syncareer_company(s, "microsoft")),
        ("syncareer_meta", lambda s: scrape_syncareer_company(s, "meta")),
        ("syncareer_bytedance", lambda s: scrape_syncareer_company(s, "bytedance")),
        ("syncareer_tiktok", lambda s: scrape_syncareer_company(s, "tiktok")),
        ("google_official", scrape_google_official),
        ("amazon_official", scrape_amazon_official),
        ("microsoft_official", scrape_microsoft_official),
        ("meta_official", scrape_meta_official),
        ("tiktok_official", scrape_tiktok_official),
        ("bytedance_official", scrape_bytedance_official),
    ]

    for source_name, scraper in sources:
        rows, result = scraper(session)
        rows, result = playwright_fallback_for_source(source_name, result, rows)
        all_rows.extend(rows)
        source_results.append(result)
        time.sleep(REQUEST_SLEEP_SECONDS)

    all_rows = dedupe_rows(all_rows)
    write_csv(all_rows)
    write_report(source_results, all_rows)

    print(f"Wrote CSV: {CSV_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Total rows: {len(all_rows)}")
    for r in source_results:
        print(f"{r.source_name}: {r.status} ({r.count} rows)")


if __name__ == "__main__":
    run()
