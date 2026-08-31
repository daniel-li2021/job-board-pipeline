"""Eightfold server-rendered embedded-position fallback."""

from __future__ import annotations

import html
import json
import time
from typing import Any, Dict, List, Optional

import requests

from ..schema import make_job, normalize_space
from .http import http_get, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES


def _payload(page: str) -> Dict[str, Any]:
    from bs4 import BeautifulSoup

    node = BeautifulSoup(page, "html.parser").select_one("#smartApplyData")
    if not node:
        return {}
    try:
        value = json.loads(html.unescape(node.get_text()))
    except (TypeError, ValueError):
        return {}
    return value if isinstance(value, dict) else {}


def scrape_eightfold_html(
    session: requests.Session,
    *,
    company: str,
    portal: str,
    domain: str,
    queries: Optional[List[str]] = None,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = pages = 0
    search_urls: List[str] = []

    for query in queries or ROLE_SEARCH_QUERIES:
        response = http_get(
            session,
            portal,
            label=f"{company} Eightfold public HTML",
            params={"query": query, "domain": domain},
        )
        pages += 1
        search_urls.append(getattr(response, "url", "") or portal)
        for row in _payload(response.text).get("positions") or []:
            if not isinstance(row, dict):
                continue
            raw_count += 1
            jid = normalize_space(row.get("ats_job_id") or row.get("display_job_id") or row.get("id"))
            if not jid or jid in seen:
                continue
            seen.add(jid)
            locations = row.get("locations") or [row.get("location") or ""]
            location = "; ".join(normalize_space(value) for value in locations if normalize_space(value))
            if location and not keep_us_or_unknown(location):
                continue
            official = normalize_space(row.get("canonicalPositionUrl") or f"{portal.rstrip('/')}/job/{row.get('id')}")
            jobs.append(make_job(
                source=source,
                company=company,
                title=normalize_space(row.get("posting_name") or row.get("name")),
                location=location,
                job_id=jid,
                posted_date=row.get("t_create") or "",
                updated_date=row.get("t_update") or "",
                date_confidence="high" if row.get("t_create") else "unknown",
                source_url=official,
                official_url=official,
                description=normalize_space(row.get("job_description") or ""),
                fetched_at=fetched_at,
            ))
        time.sleep(0.1)

    return {
        "company": company,
        "source": source,
        "method": "HTTP GET Eightfold server HTML + embedded smartApplyData positions",
        "search_url": portal,
        "search_urls": search_urls,
        "pagination": "first 10 embedded positions per focused role query; PCSX remains disabled",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }
