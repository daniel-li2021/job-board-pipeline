#!/usr/bin/env python3
"""Local JobSpy adapter for Indeed and Glassdoor."""

from __future__ import annotations

import time
import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from typing import Any, Callable, Dict, List
from urllib.parse import quote

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
            futures = [executor.submit(self._process_job, item) for item in listings.get("jobListings") or []]
            for future in as_completed(futures):
                result = future.result()
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
    if direct and not is_aggregator_url(direct):
        row["application_url"] = direct
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
            from jobspy import scrape_jobs as scrape_jobs_func
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
    handler = logging.Handler()
    handler.emit = lambda record: errors.append(record.getMessage())  # type: ignore[method-assign]
    logger = logging.getLogger(f"JobSpy:{JOBSPY_SITE[source].replace('_', '').title()}")
    logger.addHandler(handler)

    try:
        for index, (group, keyword, page_budget) in enumerate(specs):
            stat = query_stat(keyword, group, page_budget)
            started = time.monotonic()
            try:
                frame = scrape_jobs_func(
                    site_name=JOBSPY_SITE[source],
                    search_term=keyword,
                    location="United States",
                    results_wanted=page_budget * RESULTS_PER_PAGE[source],
                    hours_old=24,
                    country_indeed="USA",
                    description_format="markdown",
                    verbose=0,
                )
                records = frame.to_dict(orient="records")
            except Exception as exc:  # JobSpy wraps board-specific transport errors.
                stat["stop_reason"] = "source_error"
                stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
                stats.append(stat)
                return {
                    "status": "blocked",
                    "reason": f"{type(exc).__name__}: {exc}",
                    "jobs": rows,
                    "query_stats": stats,
                    "provenance": source_provenance,
                }

            stat["pages_fetched"] = page_budget if records else 0
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
            stat["stop_reason"] = "page_budget"
            stat["elapsed_seconds"] = round(time.monotonic() - started, 3)
            stats.append(stat)
    finally:
        logger.removeHandler(handler)

    return {"status": "ok", "jobs": rows, "query_stats": stats, "provenance": source_provenance}
