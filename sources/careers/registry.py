"""Company registry + dispatcher for official-careers discovery."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import requests

from ..schema import BASE_DIR, SourceUnavailable
from .amazon import scrape_amazon
from .apple import scrape_apple
from .ashby import scrape_ashby
from .avature import scrape_avature
from .google import scrape_google
from .greenhouse import scrape_greenhouse
from .disney import scrape_disney
from .lever import scrape_lever
from .linkedin_company import scrape_linkedin_company
from .meta import scrape_meta
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

REGISTRY_PATH = BASE_DIR / "source" / "official_careers.json"
ATS_BOARDS_PATH = BASE_DIR / "source" / "ats_boards.json"


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
        return scrape_google(session, max_pages=max_pages)
    if adapter == "amazon":
        return scrape_amazon(session, max_pages=max_pages)
    if adapter == "apple":
        return scrape_apple(session, max_pages=max_pages)
    if adapter == "microsoft":
        return scrape_microsoft(session, max_pages=max_pages)
    if adapter == "pcsx":
        pc = company.get("pcsx") or {}
        return scrape_pcsx(
            session,
            company=name,
            portal=pc["portal"],
            domain=pc["domain"],
            max_pages=max_pages,
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
        )
    if adapter == "radancy":
        rd = company.get("radancy") or {}
        return scrape_radancy(
            session,
            company=name,
            search_url=rd["search_url"],
            max_pages=max_pages,
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
        )
    if adapter == "sap":
        return scrape_sap(session, max_pages=max_pages)
    if adapter == "avature":
        av = company.get("avature") or {}
        return scrape_avature(
            session,
            company=name,
            search_url=av.get("search_url") or "https://bloomberg.avature.net/careers/SearchJobs",
            max_pages=max_pages,
        )
    if adapter == "uber":
        return scrape_uber(session, max_pages=max_pages)
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
    session: requests.Session,
    *,
    only: Optional[str] = None,
    max_pages: int = 50,
) -> List[Dict[str, Any]]:
    wanted = _only_ids(only)
    results: List[Dict[str, Any]] = []
    for company in enabled_companies():
        cid = (company.get("id") or "").lower()
        if wanted and cid not in wanted:
            continue
        try:
            result = scrape_company(session, company, max_pages=max_pages)
            result["company_id"] = cid
            results.append(result)
        except SourceUnavailable as exc:
            results.append(_blocked_result(company, cid, exc, "blocked"))
        except Exception as exc:  # noqa: BLE001
            results.append(_blocked_result(company, cid, exc, "error"))
            results[-1]["errors"] = [f"{type(exc).__name__}: {exc}"]
    return results
