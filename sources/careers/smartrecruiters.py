"""Official-careers SmartRecruiters Posting API adapter.

GET ``/v1/companies/{slug}/postings`` with ``country=us`` and keyword queries.
Details (full JD) come from GET ``.../postings/{id}``.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

LIST_URL = "https://api.smartrecruiters.com/v1/companies/{slug}/postings"
DETAIL_URL = "https://api.smartrecruiters.com/v1/companies/{slug}/postings/{pid}"
PAGE_SIZE = 100
SLEEP_S = 0.2
DETAIL_SLEEP_S = 0.12
MAX_DETAILS = 200
DEFAULT_QUERIES = ROLE_SEARCH_QUERIES


def _location(item: Dict[str, Any]) -> str:
    loc = item.get("location") or {}
    if not isinstance(loc, dict):
        return normalize_space(loc)
    if loc.get("fullLocation"):
        return normalize_space(loc.get("fullLocation"))
    bits = [loc.get("city") or "", loc.get("region") or "", loc.get("country") or ""]
    label = ", ".join(normalize_space(b) for b in bits if b)
    if loc.get("remote"):
        label = f"{label}; Remote" if label else "Remote"
    return label


def _jobad_text(detail: Dict[str, Any]) -> str:
    job_ad = detail.get("jobAd") or {}
    sections = job_ad.get("sections") if isinstance(job_ad, dict) else {}
    parts: List[str] = []
    if isinstance(sections, dict):
        for section in sections.values():
            if isinstance(section, dict):
                parts.append(html_to_text(section.get("text") or ""))
            elif isinstance(section, str):
                parts.append(html_to_text(section))
    return normalize_space(" ".join(p for p in parts if p))


def scrape_smartrecruiters(
    session: requests.Session,
    *,
    company: str,
    slug: str,
    max_pages: int = 50,
    queries: Optional[List[str]] = None,
    fetch_details: bool = True,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = queries or DEFAULT_QUERIES
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    list_url = LIST_URL.format(slug=slug)
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    pages = 0
    errors: List[str] = []
    detail_fetches = 0

    for query in queries:
        offset = 0
        query_ids: set[str] = set()
        for _page in range(max_pages):
            payload = http_get(
                session,
                list_url,
                label=f"{company} smartrecruiters",
                params={"q": query, "country": "us", "limit": PAGE_SIZE, "offset": offset},
            ).json()
            pages += 1
            rows = payload.get("content") or []
            total = int(payload.get("totalFound") or 0)
            if not rows:
                break
            page_ids = [str(item.get("id") or "") for item in rows if isinstance(item, dict)]
            page_ids = [jid for jid in page_ids if jid]
            if page_ids and query_ids and all(jid in query_ids for jid in page_ids):
                break
            for item in rows:
                if not isinstance(item, dict):
                    continue
                raw_count += 1
                jid = str(item.get("id") or "")
                if not jid:
                    continue
                query_ids.add(jid)
                if jid in seen:
                    continue
                seen.add(jid)
                location = _location(item)
                if location and not keep_us_or_unknown(location):
                    continue
                official = item.get("postingUrl") or f"https://jobs.smartrecruiters.com/{slug}/{jid}"
                description = ""
                if fetch_details and detail_fetches < MAX_DETAILS:
                    try:
                        det = http_get(
                            session,
                            DETAIL_URL.format(slug=slug, pid=jid),
                            label=f"{company} smartrecruiters detail",
                        ).json()
                        description = _jobad_text(det)
                        official = det.get("postingUrl") or official
                        loc2 = _location(det)
                        if loc2:
                            location = loc2
                        detail_fetches += 1
                        time.sleep(DETAIL_SLEEP_S)
                    except Exception as exc:  # noqa: BLE001
                        errors.append(f"detail {jid}: {exc}")
                if location and not keep_us_or_unknown(location):
                    continue
                jobs.append(
                    make_job(
                        source=source,
                        company=company,
                        title=item.get("name") or "",
                        location=location,
                        job_id=item.get("refNumber") or jid,
                        posted_date=item.get("releasedDate") or "",
                        date_confidence="high" if item.get("releasedDate") else "unknown",
                        source_url=official,
                        official_url=official,
                        description=description,
                        fetched_at=fetched_at,
                    )
                )
            offset += PAGE_SIZE
            if total and offset >= total:
                break
            time.sleep(SLEEP_S)

    return {
        "company": company,
        "source": source,
        "method": "HTTP GET SmartRecruiters /v1/companies/{slug}/postings (+ posting detail)",
        "search_url": f"https://careers.smartrecruiters.com/{slug}",
        "search_urls": [list_url],
        "pagination": f"offset=0,{PAGE_SIZE},... ; country=us; stop on empty/repeat or totalFound",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "detail_fetches": detail_fetches,
    }
