#!/usr/bin/env python3
"""Official company career-page adapters that work over plain HTTP (CI-safe).

Only endpoints that respond to anonymous HTTP JSON/HTML are included here so
this can run in GitHub Actions without a headless browser. Each company is an
independent best-effort source: if one fails it is skipped, not fatal.

Currently: Amazon (search JSON) and Google (results page links). Others
(Microsoft/Apple/Uber/TikTok/ByteDance) are gated behind anti-bot/JS rendering
and are intentionally left to the local adapters / ATS coverage for v1.
"""

from __future__ import annotations

import re
import time
from typing import Any, Callable, Dict, List
from urllib.parse import urljoin

import requests

from .schema import (
    SourceUnavailable,
    is_us_location,
    make_job,
    normalize_space,
)

REQUEST_TIMEOUT = 25
KEYWORDS = [
    "software engineer",
    "backend engineer",
    "full stack engineer",
    "machine learning engineer",
    "ai engineer",
    "data engineer",
]
MAX_PER_KEYWORD = 100


def _get(session: requests.Session, url: str, **kwargs: Any) -> requests.Response:
    try:
        resp = session.get(url, timeout=REQUEST_TIMEOUT, **kwargs)
    except requests.RequestException as exc:
        raise SourceUnavailable(f"network error: {exc}") from exc
    if resp.status_code in (401, 403, 429):
        raise SourceUnavailable(f"blocked with HTTP {resp.status_code}")
    if resp.status_code >= 400:
        raise SourceUnavailable(f"HTTP {resp.status_code}")
    return resp


def fetch_amazon(session: requests.Session) -> List[Dict[str, str]]:
    url = "https://www.amazon.jobs/en/search.json"
    seen: set[str] = set()
    rows: List[Dict[str, str]] = []
    for keyword in KEYWORDS:
        offset = 0
        while offset < MAX_PER_KEYWORD:
            params = {
                "base_query": keyword,
                "loc_query": "United States",
                "country": "USA",
                "result_limit": 20,
                "offset": offset,
                "sort": "recent",
            }
            payload = _get(session, url, params=params).json()
            jobs = payload.get("jobs", [])
            if not jobs:
                break
            for item in jobs:
                jid = str(item.get("id_icims") or item.get("id") or "")
                if jid and jid in seen:
                    continue
                seen.add(jid)
                location = item.get("normalized_location") or item.get("location") or ""
                if location and not is_us_location(location):
                    continue
                job_path = item.get("job_path") or ""
                job_url = urljoin("https://www.amazon.jobs", job_path) if job_path else "https://www.amazon.jobs/"
                rows.append(
                    make_job(
                        source="amazon_official",
                        company="Amazon",
                        title=item.get("title", ""),
                        location=location,
                        job_id=jid,
                        posted_date=item.get("posted_date") or "",
                        date_confidence="high",
                        source_url=job_url,
                        official_url=job_url,
                        description=normalize_space(item.get("description_short") or item.get("basic_qualifications") or ""),
                    )
                )
            offset += 20
            time.sleep(0.25)
    return rows


def fetch_google(session: requests.Session) -> List[Dict[str, str]]:
    base = "https://www.google.com/about/careers/applications/jobs/results/"
    link_re = re.compile(r"jobs/results/(\d+)-([a-z0-9\-]+)")
    seen: set[str] = set()
    rows: List[Dict[str, str]] = []
    for keyword in KEYWORDS:
        params = {"q": keyword, "location": "United States", "sort_by": "date"}
        html = _get(session, base, params=params).text
        for jid, slug in link_re.findall(html):
            if jid in seen:
                continue
            seen.add(jid)
            title = normalize_space(slug.replace("-", " ")).title()
            job_url = urljoin(base, f"{jid}-{slug}")
            rows.append(
                make_job(
                    source="google_official",
                    company="Google",
                    title=title,
                    location="United States",
                    job_id=jid,
                    posted_date="",
                    date_confidence="unknown",
                    source_url=job_url,
                    official_url=job_url,
                )
            )
        time.sleep(0.4)
    return rows


_SOURCES: Dict[str, Callable[[requests.Session], List[Dict[str, str]]]] = {
    "amazon_official": fetch_amazon,
    "google_official": fetch_google,
}


def fetch_all_official(session: requests.Session) -> Dict[str, Any]:
    """Run every official source. One failing skips only that source."""
    jobs: List[Dict[str, str]] = []
    per_source: Dict[str, int] = {}
    errors: List[str] = []
    for name, fetcher in _SOURCES.items():
        try:
            src_rows = fetcher(session)
            jobs.extend(src_rows)
            per_source[name] = len(src_rows)
        except SourceUnavailable as exc:
            errors.append(f"{name}: {exc}")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{name}: unexpected {type(exc).__name__}: {exc}")
    return {"jobs": jobs, "per_source": per_source, "errors": errors}
