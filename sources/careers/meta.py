"""Meta Careers Relay adapter with dynamic token and persisted-query discovery."""

from __future__ import annotations

import json
import re
import time
from typing import Any, Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup

from ..schema import SourceUnavailable, make_job
from .http import http_get, keep_us_or_unknown, now_iso, raise_for_status
from .query_terms import ROLE_SEARCH_QUERIES

PORTAL = "https://www.metacareers.com/jobsearch/"
GRAPHQL = "https://www.metacareers.com/graphql"
FRIENDLY_NAME = "CareersJobSearchResultsV2DataQuery"
META_HEADERS = {"User-Agent": "Mozilla/5.0"}


def _relay_credentials(session: requests.Session) -> Tuple[str, str]:
    html = http_get(
        session,
        PORTAL,
        label="Meta careers portal",
        params={"q": "software engineer", "sort_by_new": "true"},
        headers=META_HEADERS,
    ).text
    token = re.search(r'"LSD",\[\],\{"token":"([^"]+)', html)
    if not token:
        raise SourceUnavailable("Meta careers page did not expose an LSD token")
    operation = re.compile(
        r'CareersJobSearchResultsV2DataQuery_candidate_portalRelayOperation"[^\n]{0,180}?exports="(\d+)"'
    )
    for tag in BeautifulSoup(html, "html.parser").find_all("script"):
        url = tag.get("src") or ""
        if not url.startswith("http"):
            continue
        script = http_get(session, url, label="Meta careers Relay bundle", headers=META_HEADERS).text
        match = operation.search(script)
        if match:
            return token.group(1), match.group(1)
    raise SourceUnavailable("Meta careers Relay bundle did not expose the current job-search doc_id")


def scrape_meta(
    session: requests.Session,
    *,
    max_pages: int = 12,
    queries: Optional[List[str]] = None,
) -> Dict[str, Any]:
    del max_pages  # the Relay result is one complete payload per query
    fetched_at = now_iso()
    queries = queries or ROLE_SEARCH_QUERIES
    lsd, doc_id = _relay_credentials(session)
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = pages = 0
    for query in queries:
        search_input = {
            "q": query,
            "divisions": [],
            "offices": [],
            "roles": [],
            "leadership_levels": [],
            "saved_jobs": [],
            "saved_searches": [],
            "sub_teams": [],
            "teams": [],
            "is_leadership": False,
            "is_remote_only": False,
            "sort_by_new": True,
            "results_per_page": None,
        }
        variables = {"search_input": search_input, "viewasUserID": None, "isLoggedIn": False}
        data = {
            "av": "0",
            "__user": "0",
            "__a": "1",
            "lsd": lsd,
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": FRIENDLY_NAME,
            "server_timestamps": "true",
            "variables": json.dumps(variables, separators=(",", ":")),
            "doc_id": doc_id,
        }
        try:
            response = session.post(
                GRAPHQL,
                data=data,
                headers={**META_HEADERS, "Accept": "application/json", "Referer": PORTAL, "X-FB-LSD": lsd},
                timeout=30,
            )
        except requests.RequestException as exc:
            raise SourceUnavailable(f"Meta careers GraphQL network error: {exc}") from exc
        raise_for_status(response, "Meta careers GraphQL")
        payload = response.json()
        if payload.get("errors"):
            raise SourceUnavailable(f"Meta careers GraphQL error: {payload['errors'][0].get('message', 'unknown')}")
        result = ((payload.get("data") or {}).get("job_search_with_featured_jobs_v2") or {})
        rows = result.get("all_jobs") or []
        pages += 1
        for item in rows:
            if not isinstance(item, dict):
                continue
            raw_count += 1
            jid = str(item.get("id") or "")
            if not jid or jid in seen:
                continue
            seen.add(jid)
            location = "; ".join(item.get("locations") or [])
            if location and not keep_us_or_unknown(location):
                continue
            official = f"https://www.metacareers.com/jobs/{jid}"
            jobs.append(make_job(
                source="meta_official_careers",
                company="Meta",
                title=item.get("title") or "",
                location=location,
                job_id=jid,
                posted_date="",
                date_confidence="unknown",
                source_url=official,
                official_url=official,
                description="",
                fetched_at=fetched_at,
            ))
        time.sleep(0.1)
    return {
        "company": "Meta",
        "source": "meta_official_careers",
        "method": "HTTP POST Meta Relay GraphQL; dynamic LSD and doc_id discovery",
        "search_url": PORTAL,
        "search_urls": [PORTAL, GRAPHQL],
        "pagination": "one complete Relay payload per role query",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }
