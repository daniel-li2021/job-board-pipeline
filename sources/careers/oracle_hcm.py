"""Oracle Cloud HCM Candidate Experience adapter (JPMC, Oracle careers).

GET ``{host}/hcmRestApi/resources/latest/recruitingCEJobRequisitions`` with
finder ``findReqs;siteNumber=...``. Details from ``recruitingCEJobRequisitionDetails``.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import requests

from ..schema import make_job, normalize_space
from .http import html_to_text, http_get, keep_us_or_unknown, now_iso
from .incremental import DetailCache, annotate_detail
from .query_terms import ROLE_SEARCH_QUERIES

PAGE_SIZE = 20
SLEEP_S = 0.25
DETAIL_SLEEP_S = 0.12
MAX_DETAILS = 200
DEFAULT_QUERIES = ROLE_SEARCH_QUERIES
EXTRA_QUERY_MAX_PAGES = 3


def _location(item: Dict[str, Any]) -> str:
    parts: List[str] = []
    primary = normalize_space(item.get("PrimaryLocation") or "")
    country = normalize_space(item.get("PrimaryLocationCountry") or "")
    if primary:
        parts.append(primary)
    elif country:
        parts.append(country)
    for extra in item.get("secondaryLocations") or []:
        if isinstance(extra, dict):
            label = extra.get("Name") or extra.get("PrimaryLocation") or extra.get("Location") or ""
        else:
            label = extra
        label = normalize_space(label)
        if label and label not in parts:
            parts.append(label)
    return "; ".join(parts)


def _is_us_row(item: Dict[str, Any], location: str) -> bool:
    country = normalize_space(item.get("PrimaryLocationCountry") or "").upper()
    if country in {"US", "USA", "UNITED STATES"}:
        return True
    if country and country not in {"US", "USA"} and not keep_us_or_unknown(location):
        return False
    return keep_us_or_unknown(location) if location else True


def scrape_oracle_hcm(
    session: requests.Session,
    *,
    company: str,
    host: str,
    site_number: str,
    public_job_base: str,
    max_pages: int = 50,
    queries: Optional[List[str]] = None,
    extra_queries: Optional[List[str]] = None,
    fetch_details: bool = True,
    detail_cache: Optional[DetailCache] = None,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = list(queries or DEFAULT_QUERIES)
    extras = [q for q in (extra_queries or []) if q and q not in queries]
    queries.extend(extras)
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    host = host.rstrip("/")
    list_url = f"{host}/hcmRestApi/resources/latest/recruitingCEJobRequisitions"
    detail_url = f"{host}/hcmRestApi/resources/latest/recruitingCEJobRequisitionDetails"
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    pages = 0
    errors: List[str] = []
    detail_fetches = 0
    detail_reused = 0
    detail_cache = detail_cache or DetailCache([])

    for query in queries:
        offset = 0
        query_ids: set[str] = set()
        query_max_pages = min(max_pages, EXTRA_QUERY_MAX_PAGES if query in extras else max_pages)
        for _page in range(query_max_pages):
            finder = (
                f"findReqs;siteNumber={site_number},limit={PAGE_SIZE},offset={offset},"
                f"keyword={query}"
            )
            payload = http_get(
                session,
                list_url,
                label=f"{company} oracle hcm",
                params={
                    "onlyData": "true",
                    "expand": "requisitionList.secondaryLocations",
                    "finder": finder,
                },
            ).json()
            pages += 1
            wrapper = (payload.get("items") or [{}])[0]
            rows = wrapper.get("requisitionList") or []
            total = int(wrapper.get("TotalJobsCount") or 0)
            if not rows:
                break
            page_ids = [str(item.get("Id") or "") for item in rows if isinstance(item, dict)]
            page_ids = [jid for jid in page_ids if jid]
            if page_ids and query_ids and all(jid in query_ids for jid in page_ids):
                break
            for item in rows:
                if not isinstance(item, dict):
                    continue
                raw_count += 1
                jid = str(item.get("Id") or "")
                if not jid:
                    continue
                query_ids.add(jid)
                if jid in seen:
                    continue
                seen.add(jid)
                location = _location(item)
                if not _is_us_row(item, location):
                    continue
                official = urljoin(public_job_base.rstrip("/") + "/", jid)
                posted = item.get("PostedDate") or ""
                listing_title = item.get("Title") or ""
                decision = detail_cache.decide(
                    company=company, job_id=jid, url=official, title=listing_title,
                    posted_date=posted,
                )
                description = str((decision.cached or {}).get("description") or "") or html_to_text(item.get("ShortDescriptionStr") or "")
                if decision.cached and not decision.should_fetch:
                    location = str(decision.cached.get("location") or location)
                    posted = str(decision.cached.get("posted_date") or posted)
                    detail_reused += 1
                detail_fetched = False
                if fetch_details and decision.should_fetch and detail_fetches < MAX_DETAILS:
                    try:
                        det_payload = http_get(
                            session,
                            detail_url,
                            label=f"{company} oracle hcm detail",
                            params={
                                "onlyData": "true",
                                "finder": f"ById;Id={jid},siteNumber={site_number}",
                            },
                        ).json()
                        det = (det_payload.get("items") or [{}])[0]
                        chunks = [
                            det.get("ExternalDescriptionStr") or "",
                            det.get("ExternalResponsibilitiesStr") or "",
                            det.get("ExternalQualificationsStr") or "",
                        ]
                        description = html_to_text(" ".join(chunks)) or description
                        loc2 = _location(det)
                        if loc2:
                            location = loc2
                            if not _is_us_row(det, location):
                                detail_fetches += 1
                                time.sleep(DETAIL_SLEEP_S)
                                continue
                        posted = det.get("ExternalPostedStartDate") or posted
                        detail_fetches += 1
                        detail_fetched = True
                        time.sleep(DETAIL_SLEEP_S)
                    except Exception as exc:  # noqa: BLE001
                        errors.append(f"detail {jid}: {exc}")
                job = make_job(
                        source=source,
                        company=company,
                        title=listing_title,
                        location=location,
                        job_id=jid,
                        posted_date=posted,
                        date_confidence="high" if posted else "unknown",
                        source_url=official,
                        official_url=official,
                        description=description,
                        fetched_at=fetched_at,
                    )
                annotate_detail(
                    job, decision, detail_fetched=detail_fetched,
                    listing_title=listing_title,
                    listing_posted_date=item.get("PostedDate") or "",
                )
                jobs.append(job)
            offset += PAGE_SIZE
            if total and offset >= total:
                break
            time.sleep(SLEEP_S)

    return {
        "company": company,
        "source": source,
        "method": "HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)",
        "search_url": f"{host}/hcmUI/CandidateExperience/en/sites/{site_number}/requisitions?keyword=software+engineer",
        "search_urls": [list_url],
        "pagination": f"finder offset=0,{PAGE_SIZE},... ; limit={PAGE_SIZE}; stop on empty/repeat or TotalJobsCount",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "detail_fetches": detail_fetches,
        "detail_cache_reused": detail_reused,
    }
