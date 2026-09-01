"""Company registry + dispatcher for official-careers discovery."""

from __future__ import annotations

import json
import os
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set

import requests

from ..schema import BASE_DIR, SourceUnavailable
from .amazon import scrape_amazon
from .apple import scrape_apple
from .ashby import scrape_ashby
from .avature import scrape_avature
from .eightfold_html import scrape_eightfold_html
from .google import scrape_google
from .greenhouse import scrape_greenhouse
from .happydance import scrape_happydance
from .jibe import scrape_jibe
from .disney import scrape_disney
from .lever import scrape_lever
from .linkedin_company import scrape_linkedin_company
from .meta import scrape_meta
from .mathworks import scrape_mathworks
from .microsoft import scrape_microsoft
from .microsoft import scrape_pcsx
from .oracle_hcm import scrape_oracle_hcm
from .radancy import scrape_radancy
from .sap import scrape_sap
from .smartrecruiters import scrape_smartrecruiters
from .uber import scrape_uber
from .tiktok import scrape_bytedance, scrape_tiktok
from .walmart import scrape_walmart
from .workday import scrape_workday
from .incremental import DetailCache
from .http import make_session

REGISTRY_PATH = BASE_DIR / "source" / "official_careers.json"
ATS_BOARDS_PATH = BASE_DIR / "source" / "ats_boards.json"
COMPANY_WORKERS = 5


def load_companies(path: Optional[Path] = None) -> Dict[str, Any]:
    target = path or REGISTRY_PATH
    data = json.loads(target.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {"companies": []}


def enabled_companies(data: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    payload = data or load_companies()
    return [c for c in payload.get("companies") or [] if c.get("enabled")]


def _ats_board(company_id: str) -> Dict[str, str]:
    payload = json.loads(ATS_BOARDS_PATH.read_text(encoding="utf-8"))
    for board in payload.get("boards") or []:
        if str(board.get("token") or "").lower() == company_id.lower():
            return board
    raise SourceUnavailable(f"no ATS board configured for {company_id}")


def _only_ids(only: Optional[str]) -> Optional[Set[str]]:
    if not only:
        return None
    return {part.strip().lower() for part in only.split(",") if part.strip()}


def scrape_company(
    session: requests.Session,
    company: Dict[str, Any],
    *,
    max_pages: int,
    detail_cache: Optional[DetailCache] = None,
    detail_title_filter: Optional[Callable[[str], bool]] = None,
) -> Dict[str, Any]:
    adapter = (company.get("adapter") or "").strip().lower()
    name = company.get("name") or company.get("id") or adapter
    max_pages = min(max_pages, int(company.get("max_pages") or max_pages))
    if adapter == "skip":
        raise SourceUnavailable(company.get("skip_reason") or f"{name} skipped")
    if adapter == "ats":
        board = _ats_board(str(company.get("id") or ""))
        ats = str(board.get("ats") or "").lower()
        token = str(board.get("token") or "")
        if ats == "greenhouse":
            return scrape_greenhouse(session, company=name, token=token)
        if ats == "ashby":
            return scrape_ashby(session, company=name, token=token)
        if ats == "lever":
            return scrape_lever(session, company=name, token=token)
        raise SourceUnavailable(f"unsupported ATS adapter {ats!r} for {name}")
    if adapter == "google":
        return scrape_google(session, max_pages=max_pages, seen_job_ids=(detail_cache or DetailCache([])).seen_ids(name))
    if adapter == "amazon":
        return scrape_amazon(session, max_pages=max_pages, seen_job_ids=(detail_cache or DetailCache([])).seen_ids(name))
    if adapter == "apple":
        return scrape_apple(session, max_pages=max_pages, seen_job_ids=(detail_cache or DetailCache([])).seen_ids(name))
    if adapter == "microsoft":
        return scrape_microsoft(session, max_pages=max_pages, detail_cache=detail_cache)
    if adapter == "pcsx":
        pc = company.get("pcsx") or {}
        return scrape_pcsx(
            session,
            company=name,
            portal=pc["portal"],
            domain=pc["domain"],
            max_pages=max_pages,
            detail_cache=detail_cache,
        )
    if adapter == "eightfold_html":
        ef = company.get("eightfold_html") or {}
        return scrape_eightfold_html(
            session,
            company=name,
            portal=ef["portal"],
            domain=ef["domain"],
            queries=ef.get("queries"),
        )
    if adapter == "disney":
        return scrape_disney(session, max_pages=max_pages)
    if adapter == "linkedin_company":
        return scrape_linkedin_company(session, max_pages=max_pages)
    if adapter == "meta":
        return scrape_meta(session, max_pages=max_pages)
    if adapter == "tiktok":
        return scrape_tiktok(session, max_pages=max_pages)
    if adapter == "bytedance":
        return scrape_bytedance(session, max_pages=max_pages)
    if adapter == "walmart":
        return scrape_walmart(session, max_pages=max_pages)
    if adapter == "workday":
        wd = company.get("workday") or {}
        return scrape_workday(
            session,
            company=name,
            host=wd["host"],
            tenant=wd["tenant"],
            site=wd["site"],
            max_pages=max_pages,
            public_prefix=wd.get("public_prefix"),
            extra_queries=wd.get("extra_queries"),
            apply_us_facet=bool(wd.get("apply_us_facet", True)),
            detail_cache=detail_cache,
            detail_title_filter=detail_title_filter,
        )
    if adapter == "greenhouse":
        gh = company.get("greenhouse") or {}
        return scrape_greenhouse(session, company=name, token=gh["token"])
    if adapter == "ashby":
        ash = company.get("ashby") or {}
        return scrape_ashby(session, company=name, token=ash["token"])
    if adapter == "lever":
        lever = company.get("lever") or {}
        return scrape_lever(session, company=name, token=lever["token"])
    if adapter == "smartrecruiters":
        sr = company.get("smartrecruiters") or {}
        return scrape_smartrecruiters(
            session,
            company=name,
            slug=sr["slug"],
            max_pages=max_pages,
            detail_cache=detail_cache,
        )
    if adapter == "radancy":
        rd = company.get("radancy") or {}
        return scrape_radancy(
            session,
            company=name,
            search_url=rd["search_url"],
            max_pages=max_pages,
            queries=rd.get("queries"),
            query_param=rd.get("query_param", "query"),
            page_param=rd.get("page_param", "page"),
            country_param=rd.get("country_param", "country_codes[]"),
            country_value=rd.get("country_value", "US"),
            page_size=int(rd.get("page_size") or 30),
        )
    if adapter == "mathworks":
        return scrape_mathworks(session, max_pages=max_pages)
    if adapter == "happydance":
        hd = company.get("happydance") or {}
        return scrape_happydance(
            session,
            company=name,
            base_url=hd["base_url"],
            max_pages=max_pages,
            queries=hd.get("queries"),
            searches=hd.get("searches"),
        )
    if adapter == "jibe":
        jb = company.get("jibe") or {}
        return scrape_jibe(
            session,
            company=name,
            api_url=jb["api_url"],
            max_pages=max_pages,
            queries=jb.get("queries"),
            country=jb.get("country", "United States"),
        )
    if adapter == "oracle_hcm":
        oc = company.get("oracle_hcm") or {}
        return scrape_oracle_hcm(
            session,
            company=name,
            host=oc["host"],
            site_number=oc["site_number"],
            public_job_base=oc["public_job_base"],
            max_pages=max_pages,
            extra_queries=oc.get("extra_queries"),
            detail_cache=detail_cache,
        )
    if adapter == "sap":
        return scrape_sap(session, max_pages=max_pages, detail_cache=detail_cache)
    if adapter == "avature":
        av = company.get("avature") or {}
        return scrape_avature(
            session,
            company=name,
            search_url=av.get("search_url") or "https://bloomberg.avature.net/careers/SearchJobs",
            max_pages=max_pages,
            queries=av.get("queries"),
            query_param=av.get("query_param", "q"),
            page_size=int(av.get("page_size") or 12),
            base_url=av.get("base_url") or "https://bloomberg.avature.net",
            detail_cache=detail_cache,
        )
    if adapter == "uber":
        return scrape_uber(session, max_pages=max_pages, detail_cache=detail_cache)
    raise SourceUnavailable(f"unknown adapter {adapter!r} for {name}")


def _blocked_result(company: Dict[str, Any], cid: str, exc: Exception, status: str) -> Dict[str, Any]:
    return {
        "company_id": cid,
        "company": company.get("name") or cid,
        "source": cid,
        "method": company.get("adapter"),
        "search_url": "",
        "pagination": "",
        "pages_fetched": 0,
        "raw_jobs": 0,
        "jobs": [],
        "errors": [str(exc)],
        "status": status,
    }


def scrape_enabled(
    session: Optional[requests.Session] = None,
    *,
    only: Optional[str] = None,
    max_pages: int = 50,
    previous_jobs: Optional[List[Dict[str, Any]]] = None,
    full_sweep: Optional[bool] = None,
    detail_title_filter: Optional[Callable[[str], bool]] = None,
    max_workers: int = COMPANY_WORKERS,
) -> List[Dict[str, Any]]:
    detail_cache = DetailCache(previous_jobs or [])
    if full_sweep is None:
        full_sweep = (os.getenv("OFFICIAL_FULL_SWEEP") or "").strip() == "1" or datetime.now(timezone.utc).weekday() == 6
    wanted = _only_ids(only)
    companies = []
    for company in enabled_companies():
        cid = (company.get("id") or "").lower()
        if wanted and cid not in wanted:
            continue
        companies.append(company)

    def scrape_one(company: Dict[str, Any]) -> Dict[str, Any]:
        cid = (company.get("id") or "").lower()
        company_session = make_session()
        if isinstance(session, requests.Session):
            company_session.headers.update(dict(session.headers.items()))
            company_session.cookies.update(session.cookies)
        started = time.monotonic()
        try:
            adapter = (company.get("adapter") or "").strip().lower()
            # Newest-sorted sources use adaptive overlap stopping. Full-board
            # ATS APIs remain complete. Unsorted sources are shallow daily and
            # automatically receive a deeper weekly Sunday sweep.
            bounded_pages = max_pages
            if not full_sweep and adapter not in {"ats", "greenhouse", "lever", "ashby", "google", "amazon", "apple", "microsoft"}:
                bounded_pages = min(max_pages, 4)
            result = scrape_company(
                company_session,
                company,
                max_pages=bounded_pages,
                detail_cache=detail_cache,
                detail_title_filter=detail_title_filter,
            )
            result["company_id"] = cid
            result["incremental_mode"] = "full_sweep" if full_sweep else "incremental"
            result["page_cap_applied"] = bounded_pages
            result["full_listing_coverage"] = adapter in {"ats", "greenhouse", "lever", "ashby"}
        except SourceUnavailable as exc:
            result = _blocked_result(company, cid, exc, "blocked")
        except Exception as exc:  # noqa: BLE001
            result = _blocked_result(company, cid, exc, "error")
            result["errors"] = [f"{type(exc).__name__}: {exc}"]
        finally:
            elapsed_seconds = time.monotonic() - started

        request_count = getattr(company_session, "request_count", 0)
        request_seconds = getattr(company_session, "request_seconds", 0.0)
        result["http_requests"] = request_count if isinstance(request_count, int) else 0
        result["http_request_seconds"] = round(
            float(request_seconds) if isinstance(request_seconds, (int, float)) else 0.0, 3
        )
        result["elapsed_seconds"] = round(elapsed_seconds, 3)
        result["detail_cache_status_counts"] = dict(sorted(Counter(
            str(job.get("detail_cache_status") or "")
            for job in result.get("jobs") or []
            if isinstance(job, dict) and job.get("detail_cache_status")
        ).items()))
        company_session.close()
        return result

    # DetailCache is immutable after construction; workers only read it. All
    # output merging and persistence remain ordered on the caller thread.
    workers = max(1, min(max_workers, COMPANY_WORKERS, len(companies) or 1))
    with ThreadPoolExecutor(max_workers=workers) as executor:
        return list(executor.map(scrape_one, companies))
