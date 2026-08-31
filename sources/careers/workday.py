"""Generic Workday CXS adapter.

Method: POST ``{host}/wday/cxs/{tenant}/{site}/jobs`` with ``limit`` 20 and
``offset`` pagination. US filtering uses the ``locationHierarchy1`` (or similar)
facet whose descriptor is "United States". Job details (description + startDate)
come from GET ``.../job/{externalPath}``.

One adapter covers NVIDIA, Salesforce, Adobe, and later Workday tenants.

NVIDIA: https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite
Salesforce: https://salesforce.wd12.myworkdayjobs.com/External_Career_Site
Adobe: https://adobe.wd5.myworkdayjobs.com/external_experienced
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import requests

from ..schema import SourceUnavailable, make_job, normalize_space
from .http import (
    html_to_text,
    http_get,
    http_post,
    is_placeholder_location,
    keep_us_or_unknown,
    location_from_workday_path,
    now_iso,
)
from .query_terms import ROLE_SEARCH_QUERIES

PAGE_SIZE = 20
SLEEP_S = 0.25
DETAIL_SLEEP_S = 0.12
MAX_DETAILS = 200
DEFAULT_QUERIES = ROLE_SEARCH_QUERIES
QUERY_PAGE_CAPS = {"platform engineer": 3}
JSON_HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}


def _jobs_url(host: str, tenant: str, site: str) -> str:
    return f"{host.rstrip('/')}/wday/cxs/{tenant}/{site}/jobs"


def _detail_url(host: str, tenant: str, site: str, external_path: str) -> str:
    path = external_path if external_path.startswith("/") else f"/{external_path}"
    return f"{host.rstrip('/')}/wday/cxs/{tenant}/{site}{path}"


def _public_prefix(host: str, tenant: str, site: str, public_prefix: Optional[str] = None) -> str:
    if public_prefix:
        return public_prefix.strip("/")
    if "myworkdaysite.com" in (host or "").lower():
        return f"recruiting/{tenant}/{site}"
    return site


def _official_url(host: str, public_prefix: str, external_path: str) -> str:
    path = external_path if external_path.startswith("/") else f"/{external_path}"
    return urljoin(host.rstrip("/") + "/", f"{public_prefix}{path}")


def _detail_location(info: Dict[str, Any], fallback: str = "") -> str:
    parts: List[str] = []
    values = [info.get("location") or fallback]
    values.extend(info.get("additionalLocations") or [])
    for value in values:
        if isinstance(value, dict):
            value = value.get("descriptor") or value.get("location") or value.get("name") or ""
        label = normalize_space(value)
        if label and not is_placeholder_location(label) and label not in parts:
            parts.append(label)
    return "; ".join(parts)


def _us_facet(facets: Any) -> Optional[Dict[str, str]]:
    """Return {facetParameter: [id]} for the United States country facet."""
    if not isinstance(facets, list):
        return None

    def search(nodes: List[Any], parent_param: str = "") -> Optional[Dict[str, str]]:
        for node in nodes:
            if not isinstance(node, dict):
                continue
            param = str(node.get("facetParameter") or parent_param)
            descriptor = normalize_space(node.get("descriptor") or "")
            node_id = str(node.get("id") or "")
            if descriptor.lower() == "united states" and node_id and param:
                return {param: node_id}
            nested = node.get("values") or []
            if nested:
                hit = search(nested if isinstance(nested, list) else [], param)
                if hit:
                    return hit
        return None

    return search(facets)


def _posted_recent_enough(posted_on: str) -> bool:
    text = (posted_on or "").lower()
    if not text:
        return True
    if "30+" in text or "30 +" in text:
        return False
    return True


def scrape_workday(
    session: requests.Session,
    *,
    company: str,
    host: str,
    tenant: str,
    site: str,
    max_pages: int = 50,
    queries: Optional[List[str]] = None,
    extra_queries: Optional[List[str]] = None,
    fetch_details: bool = True,
    public_prefix: Optional[str] = None,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = list(queries or DEFAULT_QUERIES)
    extras = [q for q in (extra_queries or []) if q and q not in queries]
    queries.extend(extras)
    source = f"{normalize_space(company).lower().replace(' ', '_')}_official_careers"
    jobs_endpoint = _jobs_url(host, tenant, site)
    public_prefix = _public_prefix(host, tenant, site, public_prefix)
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = 0
    pages = 0
    errors: List[str] = []
    detail_fetches = 0
    us_applied: Dict[str, List[str]] = {}

    # Resolve the United States facet id from an unfiltered first page.
    probe = http_post(
        session,
        jobs_endpoint,
        label=f"{company} workday probe",
        json_body={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": queries[0]},
        headers=JSON_HEADERS,
    ).json()
    us = _us_facet(probe.get("facets"))
    if us:
        param, facet_id = next(iter(us.items()))
        us_applied = {param: [facet_id]}

    for query in queries:
        offset = 0
        query_ids: set[str] = set()
        query_max_pages = min(max_pages, QUERY_PAGE_CAPS.get(query, 3 if query in extras else max_pages))
        for _page in range(query_max_pages):
            body = {
                "appliedFacets": us_applied,
                "limit": PAGE_SIZE,
                "offset": offset,
                "searchText": query,
            }
            payload = http_post(
                session,
                jobs_endpoint,
                label=f"{company} workday",
                json_body=body,
                headers=JSON_HEADERS,
            ).json()
            pages += 1
            rows = payload.get("jobPostings") or []
            total = int(payload.get("total") or 0)
            if not rows:
                break
            page_ids = []
            for item in rows:
                if not isinstance(item, dict):
                    continue
                bullets = item.get("bulletFields") or []
                page_ids.append(str(bullets[0] if bullets else "") or str(item.get("externalPath") or ""))
            page_ids = [jid for jid in page_ids if jid]
            if page_ids and query_ids and all(jid in query_ids for jid in page_ids):
                break
            for item in rows:
                if not isinstance(item, dict):
                    continue
                raw_count += 1
                bullets = item.get("bulletFields") or []
                jid = str(bullets[0] if bullets else "") or str(item.get("externalPath") or "")
                if not jid:
                    continue
                query_ids.add(jid)
                if jid in seen:
                    continue
                seen.add(jid)
                location = item.get("locationsText") or ""
                external_path = item.get("externalPath") or ""
                path_loc = location_from_workday_path(external_path)
                if is_placeholder_location(location) and path_loc:
                    location = path_loc
                if location and not keep_us_or_unknown(location, path_hint=external_path):
                    continue
                official = _official_url(host, public_prefix, external_path)
                posted_on = item.get("postedOn") or ""
                description = ""
                start_date = ""
                need_detail = bool(
                    fetch_details
                    and external_path
                    and detail_fetches < MAX_DETAILS
                    and (
                        _posted_recent_enough(posted_on)
                        or is_placeholder_location(item.get("locationsText") or "")
                    )
                )
                if need_detail:
                    try:
                        det = http_get(
                            session,
                            _detail_url(host, tenant, site, external_path),
                            label=f"{company} workday detail",
                            headers={"Accept": "application/json"},
                        ).json()
                        info = det.get("jobPostingInfo") or {}
                        description = html_to_text(info.get("jobDescription") or "")
                        start_date = info.get("startDate") or ""
                        detail_loc = _detail_location(info, location)
                        if detail_loc:
                            location = detail_loc
                        elif path_loc:
                            location = path_loc
                        jid = str(info.get("jobReqId") or jid)
                        detail_fetches += 1
                        time.sleep(DETAIL_SLEEP_S)
                    except SourceUnavailable as exc:
                        errors.append(f"detail {jid}: {exc}")
                if is_placeholder_location(location) and path_loc:
                    location = path_loc
                if location and not keep_us_or_unknown(location, path_hint=external_path):
                    continue
                posted = start_date or posted_on
                confidence = "high" if start_date else ("medium" if posted_on else "unknown")
                jobs.append(
                    make_job(
                        source=source,
                        company=company,
                        title=item.get("title") or "",
                        location=location,
                        job_id=jid,
                        posted_date=posted,
                        date_confidence=confidence,
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
        "method": "HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)",
        "search_url": f"{host.rstrip('/')}/{public_prefix}",
        "search_urls": [jobs_endpoint],
        "pagination": "offset=0,20,40,... ; limit=20; stop on empty/repeat or total",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": errors,
        "us_facet": us_applied,
        "detail_fetches": detail_fetches,
    }
