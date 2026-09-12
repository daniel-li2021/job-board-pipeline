#!/usr/bin/env python3
"""Local JobSpy adapter for Indeed and Glassdoor."""

from __future__ import annotations

import time
import logging
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from typing import Any, Callable, Dict, List
from urllib.parse import parse_qs, quote, urljoin, urlsplit

from bs4 import BeautifulSoup

from .local_search import query_stat, source_queries
from .schema import is_aggregator_url, is_us_location, make_job, normalize_space

JOBSPY_SITE = {
    "indeed": "indeed",
    "glassdoor": "glassdoor",
}
RESULTS_PER_PAGE = {"indeed": 100, "glassdoor": 30}


def provenance() -> Dict[str, str]:
    try:
        release = version("python-jobspy")
    except PackageNotFoundError:
        release = "not-installed"
    return {"implementation": "python-jobspy", "version": release}


def _patch_glassdoor_transport() -> None:
    """Backport JobSpy PRs #347/#350 until they reach a PyPI release."""
    from jobspy.exception import GlassdoorException
    from jobspy.glassdoor import Glassdoor
    from jobspy.glassdoor.util import get_cursor_for_page
    from jobspy.model import DescriptionFormat
    from jobspy.util import markdown_converter

    if getattr(Glassdoor, "_jobboard_compat", False):
        return

    def csrf_token(self: Any) -> str | None:
        response = self.session.get(f"{self.base_url.rstrip('/')}/")
        matches = re.findall(r'"token":\s*"([^"]+)"', response.text)
        return matches[0] if matches else None

    def location(self: Any, value: str, is_remote: bool) -> tuple[int | str, str]:
        if not value or is_remote:
            return "11047", "STATE"
        url = (
            f"{self.base_url.rstrip('/')}/findPopularLocationAjax.htm?maxLocationsToReturn=10"
            f"&term={quote(value, safe='')}"
        )
        response = self.session.get(url)
        if response.status_code != 200:
            raise GlassdoorException(f"location lookup HTTP {response.status_code}")
        items = response.json()
        if not items:
            raise GlassdoorException(f"location not found: {value}")
        location_type = {"C": "CITY", "S": "STATE", "N": "COUNTRY"}.get(
            items[0]["locationType"], items[0]["locationType"]
        )
        return int(items[0]["locationId"]), location_type

    def fetch_page(
        self: Any, scraper_input: Any, location_id: int, location_type: str,
        page_num: int, cursor: str | None,
    ) -> tuple[list[Any], str | None]:
        response = self.session.post(
            f"{self.base_url.rstrip('/')}/graph",
            timeout_seconds=15,
            data=self._add_payload(location_id, location_type, page_num, cursor),
        )
        if response.status_code != 200:
            raise GlassdoorException(f"search GraphQL HTTP {response.status_code}")
        payload = response.json()[0]
        listings = (payload.get("data") or {}).get("jobListings")
        if not listings:
            raise GlassdoorException("search GraphQL response missing jobListings")
        jobs: List[Any] = []
        with ThreadPoolExecutor(max_workers=self.jobs_per_page) as executor:
            for result in executor.map(self._process_job, listings.get("jobListings") or []):
                if result:
                    jobs.append(result)
        return jobs, get_cursor_for_page(listings.get("paginationCursors") or [], page_num + 1)

    def fetch_description(self: Any, job_id: int) -> str | None:
        response = self.session.post(
            f"{self.base_url.rstrip('/')}/graph",
            timeout_seconds=15,
            json=[{
                "operationName": "JobDetailQuery",
                "variables": {"jl": job_id, "queryString": "q", "pageTypeEnum": "SERP"},
                "query": """
                    query JobDetailQuery($jl: Long!, $queryString: String, $pageTypeEnum: PageTypeEnum) {
                        jobview: jobView(
                            listingId: $jl
                            contextHolder: {queryString: $queryString, pageTypeEnum: $pageTypeEnum}
                        ) { job { description } }
                    }
                """,
            }],
        )
        if response.status_code != 200:
            return None
        description = response.json()[0]["data"]["jobview"]["job"]["description"]
        return markdown_converter(description) if self.scraper_input.description_format == DescriptionFormat.MARKDOWN else description

    Glassdoor._get_csrf_token = csrf_token
    Glassdoor._get_location = location
    Glassdoor._fetch_jobs_page = fetch_page
    Glassdoor._fetch_job_description = fetch_description
    Glassdoor._jobboard_compat = True


def _fetch_records(source: str, keyword: str, budget: int, hours: int, stat: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Use separate JobSpy transports with a measured, hard page ceiling."""
    from jobspy.indeed import Indeed
    from jobspy.glassdoor import Glassdoor
    from jobspy.model import ScraperInput, Site

    scraper = (Indeed if source == "indeed" else Glassdoor)()
    method = "_scrape_page" if source == "indeed" else "_fetch_jobs_page"
    fetch = getattr(scraper, method)
    exhausted = False

    def page(*args: Any, **kwargs: Any) -> Any:
        nonlocal exhausted
        if exhausted or stat["pages_fetched"] >= budget:
            return [], None
        # Indeed otherwise silently turns HTTP failures into an empty page.
        post = scraper.session.post
        def checked_post(*a: Any, **kw: Any) -> Any:
            response = post(*a, **kw)
            if response.status_code != 200:
                raise RuntimeError(f"{source} HTTP {response.status_code}")
            return response
        scraper.session.post = checked_post
        try:
            jobs, cursor = fetch(*args, **kwargs)
        finally:
            scraper.session.post = post
        stat["pages_fetched"] += 1
        exhausted = not cursor or not jobs
        if exhausted:
            stat["stop_reason"] = "exhausted"
        return jobs, cursor

    setattr(scraper, method, page)
    response = scraper.scrape(ScraperInput(
        site_type=[Site.INDEED if source == "indeed" else Site.GLASSDOOR],
        search_term=keyword, location="United States", distance=50,
        hours_old=hours, results_wanted=budget * RESULTS_PER_PAGE[source],
    ))
    records = []
    for job in response.jobs:
        record = job.model_dump()
        record["company"] = job.company_name
        record["location"] = job.location.display_location() if job.location else ("Remote" if job.is_remote else "")
        records.append(record)
    return records


def _scrapling_glassdoor_records(keyword: str, hours: int) -> List[Dict[str, Any]]:
    """Recover the static Glassdoor result cards after its old location API fails."""
    try:
        from scrapling.fetchers import Fetcher
    except ImportError as exc:
        raise RuntimeError("Scrapling is not installed") from exc
    url = (
        "https://www.glassdoor.com/Job/jobs.htm?"
        f"sc.keyword={quote(keyword, safe='')}&locT=N&locId=1&fromAge={max(1, hours // 24)}"
    )
    response = Fetcher.get(
        url, impersonate="chrome", stealthy_headers=True, retries=0, timeout=25,
    )
    status = int(getattr(response, "status", 0) or 0)
    if status != 200:
        raise RuntimeError(f"Glassdoor static search HTTP {status}")
    return _parse_glassdoor_cards(getattr(response, "body", b""))


def _parse_glassdoor_cards(body: str | bytes) -> List[Dict[str, Any]]:
    soup = BeautifulSoup(body, "html.parser")
    records: List[Dict[str, Any]] = []
    for card in soup.select('[data-test="job-card-wrapper"]'):
        anchor = card.select_one('a[data-test="job-title"]')
        href = urljoin("https://www.glassdoor.com", str(anchor.get("href") or "")) if anchor else ""
        job_id = (parse_qs(urlsplit(href).query).get("jl") or [""])[0]
        company = card.select_one('[class*="compactEmployerName"]')
        location = card.select_one('[data-test="emp-location"]')
        snippet = card.select_one('[data-test="descSnippet"]')
        if not anchor or not href:
            continue
        records.append({
            "id": job_id,
            "title": anchor.get_text(" ", strip=True),
            "company": company.get_text(" ", strip=True) if company else "",
            "location": location.get_text(" ", strip=True) if location else "",
            "job_url": href,
            "description": "",
            "source_snippet": snippet.get_text(" ", strip=True) if snippet else "",
            "enrichment_failure_reason": "glassdoor_detail_http_403_static_card_only",
        })
    return records


def _value(value: Any) -> str:
    if value is None:
        return ""
    try:
        if value != value:  # NaN/NaT
            return ""
    except (TypeError, ValueError):
        pass
    text = normalize_space(value)
    return "" if text.lower() in {"nan", "nat", "<na>", "none"} else text


def _normalize(source: str, record: Dict[str, Any], fetched_at: str) -> Dict[str, str]:
    posted = _value(record.get("date_posted"))
    row = make_job(
        source=source,
        company=_value(record.get("company")),
        title=_value(record.get("title")),
        location=_value(record.get("location")),
        job_id=_value(record.get("id")),
        posted_date=posted,
        aggregator_posted_date=posted,
        date_confidence="low",
        source_url=_value(record.get("job_url")),
        description=_value(record.get("description")),
        fetched_at=fetched_at,
    )
    direct = _value(record.get("job_url_direct"))
    if urlsplit(direct).scheme in {"http", "https"} and not is_aggregator_url(direct):
        row["application_url"] = direct
    if record.get("enrichment_failure_reason"):
        row["enrichment_status"] = "unresolved"
        row["enrichment_failure_reason"] = _value(record["enrichment_failure_reason"])
    if record.get("source_snippet"):
        row["source_snippet"] = _value(record["source_snippet"])
    return row


def scrape(
    source: str,
    keywords: List[str] | None = None,
    *,
    scrape_jobs_func: Callable[..., Any] | None = None,
) -> Dict[str, Any]:
    """Fetch one JobSpy source and normalize it to the shared job schema."""
    source_provenance = provenance()
    if scrape_jobs_func is None:
        try:
            import jobspy  # noqa: F401
        except ImportError:
            return {
                "status": "missing_dependency",
                "reason": "python-jobspy is not installed; install requirements-local.txt",
                "jobs": [],
                "query_stats": [],
                "provenance": source_provenance,
            }
        if source == "glassdoor":
            _patch_glassdoor_transport()
            source_provenance["compat"] = "JobSpy PRs #347/#350"
            source_provenance["reliability"] = "best_effort_optional"

    specs = list(source_queries(source))
    if keywords:
        wanted = set(keywords)
        specs = [spec for spec in specs if spec[1] in wanted]
    seen: set[str] = set()
    by_key: Dict[str, Dict[str, str]] = {}
    rows: List[Dict[str, str]] = []
    stats: List[Dict[str, object]] = []
    fetched_at = datetime.now(timezone.utc).isoformat()
    errors: List[str] = []
    handler = logging.Handler(level=logging.ERROR)
    handler.emit = lambda record: errors.append(record.getMessage())  # type: ignore[method-assign]
    logger = logging.getLogger(f"JobSpy:{JOBSPY_SITE[source].replace('_', '').title()}")
    logger.addHandler(handler)

    try:
        for index, (group, keyword, page_budget) in enumerate(specs):
            stat = query_stat(keyword, group, page_budget)
            started = time.monotonic()
            errors.clear()
            hours = 48 if source == "indeed" and group == "primary" else 24
            stat["hours_old"] = hours
            try:
                if scrape_jobs_func is None:
                    records = _fetch_records(source, keyword, page_budget, hours, stat)
                else:
                    frame = scrape_jobs_func(
                        site_name=JOBSPY_SITE[source], search_term=keyword,
                        location="United States", results_wanted=page_budget * RESULTS_PER_PAGE[source],
                        hours_old=hours, country_indeed="USA", description_format="markdown", verbose=0,
                    )
                    records = frame.to_dict(orient="records")
                if errors and (records or index > 0):
                    raise RuntimeError("; ".join(errors[-2:]))
            except Exception as exc:  # JobSpy wraps board-specific transport errors.
                if source == "glassdoor" and scrape_jobs_func is None:
                    try:
                        records = _scrapling_glassdoor_records(keyword, hours)
                    except Exception as fallback_exc:  # noqa: BLE001 - preserve last-good snapshot
                        records = []
                        exc = fallback_exc
                    if records:
                        stat["pages_fetched"] = 1
                        stat["stop_reason"] = "static_html_fallback"
                        stat["fallback_reason"] = f"JobSpy failed before results: {type(exc).__name__}: {exc}"
                        source_provenance["implementation"] = "python-jobspy+scrapling-static"
                    else:
                        stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
                        stats.append(stat)
                        return {
                            "status": "blocked",
                            "reason": f"{type(exc).__name__}: {exc}",
                            "jobs": rows,
                            "query_stats": stats,
                            "provenance": source_provenance,
                        }
                else:
                    stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
                    stats.append(stat)
                    return {
                        "status": "blocked",
                        "reason": f"{type(exc).__name__}: {exc}",
                        "jobs": rows,
                        "query_stats": stats,
                        "provenance": source_provenance,
                    }

            stat["raw_jobs"] = len(records)
            if not records:
                stat["stop_reason"] = "empty_unverified"
                stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
                stats.append(stat)
                if index == 0:
                    return {
                        "status": "empty_unverified",
                        "reason": "; ".join(errors[-2:]) if errors else "JobSpy returned no rows for the broad primary query; access may be blocked",
                        "jobs": [],
                        "query_stats": stats,
                        "provenance": source_provenance,
                    }
                continue

            query_seen: set[str] = set()
            added = 0
            for record in records:
                row = _normalize(source, record, fetched_at)
                key = row.get("job_id") or row.get("source_url")
                if key:
                    query_seen.add(key)
                if key and key in seen:
                    prior = by_key.get(key)
                    if prior:
                        prior["discovery_queries"][source] = list(dict.fromkeys([
                            *prior["discovery_queries"][source], keyword,
                        ]))
                    continue
                if row["location"] and not is_us_location(row["location"]):
                    continue
                if key:
                    seen.add(key)
                row["discovery_queries"] = {source: [keyword]}
                rows.append(row)
                if key:
                    by_key[key] = row
                added += 1
            stat["unique_jobs"] = len(query_seen)
            stat["unique_contribution"] = added
            stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
            stats.append(stat)
    finally:
        logger.removeHandler(handler)

    return {"status": "ok", "jobs": rows, "query_stats": stats, "provenance": source_provenance}
