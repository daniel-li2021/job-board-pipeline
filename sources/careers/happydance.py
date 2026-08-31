"""Happydance public jobs-search API adapter."""

from __future__ import annotations

import json
import re
import time
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

PAGE_SIZE = 100


def _rsc_detail(page: str) -> Tuple[str, str]:
    """Return (description, posted) from public Next.js flight-data chunks."""
    from bs4 import BeautifulSoup

    description = posted = ""
    for node in BeautifulSoup(page, "html.parser").select("script"):
        text = node.string or node.get_text()
        if not text.startswith("self.__next_f.push("):
            continue
        try:
            value = json.loads(text[len("self.__next_f.push("):-1])
            decoded = value[1] if isinstance(value, list) and len(value) > 1 and isinstance(value[1], str) else ""
        except (TypeError, ValueError):
            continue
        if not posted:
            match = re.search(r'"DisplayDate":"([^"]+)"', decoded)
            if match:
                posted = match.group(1)
        if decoded.lstrip().startswith("<") and "<p" in decoded and len(decoded) > len(description):
            description = decoded
    return html_to_text(description), posted


def scrape_happydance(
    session: requests.Session,
    *,
    company: str,
    base_url: str,
    max_pages: int = 3,
    queries: Optional[List[str]] = None,
    searches: Optional[List[Dict[str, str]]] = None,
    fetch_details: bool = True,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    endpoint = f"{base_url.rstrip('/')}/api/jobs/search/"
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = pages = details = 0
    errors: List[str] = []

    request_filters = searches or [{"search": query} for query in (queries or ROLE_SEARCH_QUERIES)]
    for request_filter in request_filters:
        query_ids: set[str] = set()
        for page in range(1, max_pages + 1):
            payload = http_get(
                session,
                endpoint,
                label=f"{company} jobs API",
                params={**request_filter, "page": page, "pagesize": PAGE_SIZE},
                headers={"Accept": "application/json"},
            ).json()
            pages += 1
            rows = payload.get("jobs") or []
            if not rows:
                break
            page_ids = [normalize_space(row.get("Id")) for row in rows]
            if query_ids and all(jid in query_ids for jid in page_ids):
                break
            query_ids.update(jid for jid in page_ids if jid)
            for row in rows:
                raw_count += 1
                jid = normalize_space(row.get("OriginalId") or row.get("Reference") or row.get("Id"))
                dedup_id = normalize_space(row.get("Id") or jid)
                if not jid or dedup_id in seen:
                    continue
                seen.add(dedup_id)
                locations = row.get("Locations") or []
                location = "; ".join(
                    normalize_space(loc.get("Identifier") or loc.get("City"))
                    for loc in locations if isinstance(loc, dict) and normalize_space(loc.get("Identifier") or loc.get("City"))
                )
                if location and not keep_us_or_unknown(location):
                    continue
                urls = row.get("Urls") or []
                path = next((item.get("Url") for item in urls if isinstance(item, dict) and item.get("IsDefault")), "")
                path = path or next((item.get("Url") for item in urls if isinstance(item, dict)), "")
                official = urljoin(base_url.rstrip("/") + "/", path or f"jobs/{dedup_id}/")
                description = posted = ""
                if fetch_details and details < 100:
                    try:
                        detail = http_get(session, official, label=f"{company} career detail")
                        description, posted = _rsc_detail(detail.text)
                        details += 1
                    except Exception as exc:  # noqa: BLE001
                        errors.append(f"detail {jid}: {exc}")
                jobs.append(make_job(
                    source=source,
                    company=company,
                    title=normalize_space(row.get("Title")),
                    location=location,
                    job_id=jid,
                    posted_date=posted,
                    date_confidence="high" if posted else "unknown",
                    source_url=official,
                    official_url=official,
                    description=description,
                    fetched_at=fetched_at,
                ))
            if page >= int(payload.get("totalPages") or 1):
                break
            time.sleep(0.1)

    return {
        "company": company,
        "source": source,
        "method": "HTTP GET public Happydance jobs JSON + server-rendered detail flight data",
        "search_url": endpoint,
        "search_urls": [endpoint],
        "pagination": f"page=1,2,... with pagesize={PAGE_SIZE}; stop on total/empty/repeat",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "detail_fetches": details,
    }
