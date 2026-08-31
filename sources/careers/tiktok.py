"""TikTok/ByteDance public supplier job-search API adapters."""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

import requests

from ..schema import SourceUnavailable, make_job, normalize_space
from .http import http_post, keep_us_or_unknown, now_iso
from .query_terms import ROLE_SEARCH_QUERIES

SEARCH = "https://api.lifeattiktok.com/api/v1/public/supplier/search/job/posts"
BYTEDANCE_SEARCH = "https://jobs.bytedance.com/api/v1/public/supplier/search/job/posts"
PAGE_SIZE = 50
US_LOCATION_CODES = [
    "CT_100762", "CT_247", "CT_1103554", "CT_94", "CT_103", "CT_223",
    "CT_243", "CT_114", "CT_203", "CT_75", "CT_1103355", "CT_130",
    "CT_157", "CT_233",
]
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "accept-language": "en-US",
    "Origin": "https://lifeattiktok.com",
    "website-path": "tiktok",
}
BYTEDANCE_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "accept-language": "en-US",
    "Origin": "https://joinbytedance.com",
    "website-path": "en",
    "x-tt-env": "boe_epam_api",
}


def _location(item: Dict[str, Any]) -> str:
    node = item.get("city_info") or {}
    parts: List[str] = []
    while isinstance(node, dict) and node:
        name = normalize_space(node.get("i18n_name") or node.get("en_name") or node.get("name") or "")
        if name and name not in parts:
            parts.append(name)
        node = node.get("parent") or {}
    return ", ".join(parts)


def _scrape_supplier(
    session: requests.Session,
    *,
    company: str,
    search_url: str,
    headers: Dict[str, str],
    recruitment_ids: List[str],
    public_base: str,
    max_pages: int = 12,
    queries: Optional[List[str]] = None,
) -> Dict[str, Any]:
    fetched_at = now_iso()
    queries = queries or ROLE_SEARCH_QUERIES
    seen: set[str] = set()
    jobs: List[Dict[str, str]] = []
    raw_count = pages = 0
    for query in queries:
        offset = 0
        for _page in range(max_pages):
            body = {
                "keyword": query,
                "limit": PAGE_SIZE,
                "offset": offset,
                "recruitment_id_list": recruitment_ids,
                "location_code_list": US_LOCATION_CODES,
                "job_category_id_list": [],
                "subject_id_list": [],
                "tag_id_list": [],
            }
            payload = http_post(
                session,
                search_url,
                label=f"{company} job search",
                json_body=body,
                headers=headers,
            ).json()
            if int(payload.get("code") or 0) != 0:
                raise SourceUnavailable(payload.get("message") or f"{company} API error")
            data = payload.get("data") or {}
            rows = data.get("job_post_list") or []
            pages += 1
            if not rows:
                break
            for item in rows:
                if not isinstance(item, dict):
                    continue
                raw_count += 1
                jid = str(item.get("id") or "")
                if not jid or jid in seen:
                    continue
                seen.add(jid)
                location = _location(item)
                if location and not keep_us_or_unknown(location):
                    continue
                official = f"{public_base.rstrip('/')}/{jid}"
                jobs.append(make_job(
                    source=f"{company.lower()}_official_careers",
                    company=company,
                    title=item.get("title") or "",
                    location=location,
                    job_id=jid,
                    posted_date="",
                    date_confidence="unknown",
                    source_url=official,
                    official_url=official,
                    description="\n\n".join(filter(None, [item.get("description"), item.get("requirement")])),
                    fetched_at=fetched_at,
                ))
            offset += len(rows)
            if offset >= int(data.get("count") or 0):
                break
            time.sleep(0.15)
    return {
        "company": company,
        "source": f"{company.lower()}_official_careers",
        "method": "HTTP POST public supplier /search/job/posts",
        "search_url": search_url,
        "search_urls": [search_url],
        "pagination": f"offset=0,{PAGE_SIZE},...; limit={PAGE_SIZE}; US city filter",
        "pages_fetched": pages,
        "raw_jobs": raw_count,
        "jobs": jobs,
        "errors": [],
    }


def scrape_tiktok(
    session: requests.Session,
    *,
    max_pages: int = 12,
    queries: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return _scrape_supplier(
        session,
        company="TikTok",
        search_url=SEARCH,
        headers=HEADERS,
        recruitment_ids=["1", "201"],
        public_base="https://lifeattiktok.com/search",
        max_pages=max_pages,
        queries=queries,
    )


def scrape_bytedance(
    session: requests.Session,
    *,
    max_pages: int = 12,
    queries: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return _scrape_supplier(
        session,
        company="ByteDance",
        search_url=BYTEDANCE_SEARCH,
        headers=BYTEDANCE_HEADERS,
        recruitment_ids=[],
        public_base="https://joinbytedance.com/search",
        max_pages=max_pages,
        queries=queries,
    )
