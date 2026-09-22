"""Bounded, conservative official JD recovery for local source cards."""

from __future__ import annotations

import base64
import json
import re
import time
from collections import Counter
from datetime import datetime, timedelta, timezone
from urllib.parse import parse_qs, urljoin, urlsplit

import requests
from bs4 import BeautifulSoup

import board_pipeline as board
import coverage_reconcile
from .schema import (
    is_aggregator_url, is_outbound_tracker_url, looks_official,
    normalize_company_key, normalize_location_key, normalize_space,
    normalize_title_key, unwrap_redirect_url,
)

SEARCH_URL = "https://html.duckduckgo.com/html/"
BING_SEARCH_URL = "https://www.bing.com/search"
CACHE_DAYS = 14
NO_MATCH_HOURS = 24
NORMAL_SEARCH_LIMIT = 12
NORMAL_PAGE_LIMIT = 12
ATS_HOSTS = (
    "ashbyhq.com", "greenhouse.io", "lever.co", "myworkdayjobs.com",
    "smartrecruiters.com", "workable.com", "icims.com", "teamtailor.com",
    "bamboohr.com", "oraclecloud.com", "eightfold.ai",
)


def _stamp(value: object) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value or "").replace("Z", "+00:00"))
        return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def _host(url: str) -> str:
    try:
        return (urlsplit(url).hostname or "").lower()
    except ValueError:
        return ""


def _bing_target(url: str) -> str:
    if _host(url) != "www.bing.com":
        return url
    encoded = parse_qs(urlsplit(url).query).get("u", [""])[0]
    if not encoded.startswith("a1"):
        return ""
    try:
        return base64.urlsafe_b64decode(encoded[2:] + "===").decode("utf-8")
    except (ValueError, UnicodeDecodeError):
        return ""


def _credible(url: str, company: str, patterns: set[str]) -> bool:
    host = _host(url)
    if not host or is_aggregator_url(url) or is_outbound_tracker_url(url):
        return False
    if any(host == pattern or host.endswith("." + pattern) for pattern in patterns):
        return True
    if looks_official(url) and any(host == ats or host.endswith("." + ats) for ats in ATS_HOSTS):
        return True
    slug = re.sub(r"[^a-z0-9]", "", normalize_company_key(company))
    return len(slug) >= 4 and slug in host.replace("-", "")


def _posting_location(posting: dict) -> str:
    places = posting.get("jobLocation") or []
    places = places if isinstance(places, list) else [places]
    bits = []
    for place in places:
        address = place.get("address") if isinstance(place, dict) else {}
        if isinstance(address, dict):
            bits.append(", ".join(str(address.get(key) or "") for key in ("addressLocality", "addressRegion", "addressCountry") if address.get(key)))
    return " | ".join(bit for bit in bits if bit)


def _title_key(value: str, *, variant: bool = False) -> str:
    title = normalize_title_key(value)
    if variant:
        title = re.sub(r"\b(remote|hybrid|onsite|on site)\b", "", title)
        title = re.sub(r"\s+", " ", title).strip()
    return title


def _verified_posting(row: dict, html: str, *, variant: bool = False) -> str:
    def postings(value: object) -> list[dict]:
        if isinstance(value, list):
            return [job for item in value for job in postings(item)]
        if not isinstance(value, dict):
            return []
        kinds = value.get("@type") or []
        if "JobPosting" in (kinds if isinstance(kinds, list) else [kinds]):
            return [value]
        return [job for item in value.values() for job in postings(item)]

    found = []
    for node in BeautifulSoup(html, "html.parser").select('script[type="application/ld+json"]'):
        try:
            found.extend(postings(json.loads(node.get_text())))
        except json.JSONDecodeError:
            continue
    if len(found) != 1:
        return ""
    posting = found[0]
    org = posting.get("hiringOrganization") or {}
    org = org.get("name") if isinstance(org, dict) else ""
    if normalize_company_key(str(org or "")) != normalize_company_key(str(row.get("company") or "")):
        return ""
    if _title_key(str(posting.get("title") or ""), variant=variant) != _title_key(str(row.get("title") or ""), variant=variant):
        return ""
    source_loc = normalize_location_key(str(row.get("location") or ""))
    posting_loc = normalize_location_key(_posting_location(posting))
    remote = str(posting.get("jobLocationType") or "").upper() == "TELECOMMUTE"
    if not source_loc or not (coverage_reconcile.locations_compatible(source_loc, posting_loc) or (remote and "remote" in source_loc)):
        return ""
    description = normalize_space(BeautifulSoup(str(posting.get("description") or ""), "html.parser").get_text(" "))
    return description if len(description) >= board.THIN_JD_CHARS else ""


def _patterns(company: str, context: dict, store: dict) -> set[str]:
    key = normalize_company_key(company)
    hosts: set[str] = set()
    cid = coverage_reconcile.company_id_for(company, context.get("registry_entries", []))
    registry = context.get("registry_by_id", {}).get(cid, {}) if cid else {}
    for link in registry.get("search_links") or []:
        host = _host(str(link.get("url") or ""))
        if host:
            hosts.add(host)
    for entry in store.values():
        if normalize_company_key(str(entry.get("company") or "")) != key:
            continue
        for field in ("official_url", "application_url"):
            url = str(entry.get(field) or "")
            if entry.get("original_resolved") or entry.get("official_search_verified") or field == "official_url":
                host = _host(url)
                if host and not is_aggregator_url(url) and not is_outbound_tracker_url(url):
                    hosts.add(host)
    return hosts


def _listing_urls(company: str, context: dict, store: dict) -> list[str]:
    """Reuse verified company board paths without guessing a new ATS tenant."""
    key = normalize_company_key(company)
    cid = coverage_reconcile.company_id_for(company, context.get("registry_entries", []))
    registry = context.get("registry_by_id", {}).get(cid, {}) if cid else {}
    urls = [str(link.get("url") or "") for link in registry.get("search_links") or []]
    for entry in store.values():
        if normalize_company_key(str(entry.get("company") or "")) != key:
            continue
        if not (entry.get("official_search_verified") or entry.get("original_resolved") or entry.get("official_url")):
            continue
        url = str(entry.get("official_url") or entry.get("application_url") or "")
        parts = urlsplit(url)
        first = next((segment for segment in parts.path.split("/") if segment), "")
        host = (parts.hostname or "").lower()
        if first and (first.lower() in {"jobs", "careers", "positions", "job"}
                      or any(host.endswith(ats) for ats in ATS_HOSTS)):
            urls.append(f"{parts.scheme}://{parts.netloc}/{first}")
    return list(dict.fromkeys(url for url in urls if urlsplit(url).scheme in {"http", "https"}))[:2]


class Resolver:
    def __init__(self, *, session: requests.Session | None = None, search_limit: int = NORMAL_SEARCH_LIMIT,
                 page_limit: int = NORMAL_PAGE_LIMIT, deadline: float | None = None):
        self.session = session or board.make_session()
        self.search_limit = search_limit
        self.page_limit = page_limit
        self.deadline = deadline
        self.search_requests = 0
        self.page_requests = 0
        self.last_search = 0.0
        self.search_provider = "duckduckgo"
        self.stats: Counter = Counter()
        self.pattern_cache: dict[str, set[str]] = {}
        self.listing_cache: dict[str, list[str]] = {}
        self.store_by_id: dict[tuple[str, str], dict] = {}
        self.dedicated_seen: set[tuple[str, str]] = set()

    def _available(self) -> bool:
        return self.deadline is None or time.monotonic() < self.deadline

    def search(self, query: str) -> tuple[list[str], str]:
        if self.search_requests >= self.search_limit or not self._available():
            return [], "budget"
        if self.search_provider == "disabled":
            return [], "network"
        delay = 1.0 - (time.monotonic() - self.last_search)
        if delay > 0:
            time.sleep(delay)
        self.search_requests += 1
        self.last_search = time.monotonic()
        provider = self.search_provider
        url = SEARCH_URL if provider == "duckduckgo" else BING_SEARCH_URL
        try:
            response = self.session.get(url, params={"q": query}, timeout=10)
        except requests.RequestException:
            self.search_provider = "bing" if provider == "duckduckgo" else "disabled"
            self.stats["search_provider_failures"] += 1
            return [], "network"
        if response.status_code != 200:
            self.search_provider = "disabled" if response.status_code == 429 or provider == "bing" else "bing"
            self.stats["search_provider_failures"] += 1
            return [], "http"
        soup = BeautifulSoup(response.text, "html.parser")
        urls = []
        selector = "a.result__a" if provider == "duckduckgo" else "li.b_algo h2 a"
        for link in soup.select(selector):
            target = unwrap_redirect_url(str(link.get("href") or ""))
            if provider == "bing":
                target = _bing_target(target)
            if urlsplit(target).scheme in {"http", "https"}:
                urls.append(target)
        return list(dict.fromkeys(urls[:8])), "ok"

    def page(self, url: str, local: Counter) -> tuple[str, str, str]:
        if self.page_requests >= self.page_limit or local["pages"] >= 4 or not self._available():
            return "", url, "budget"
        self.page_requests += 1
        local["pages"] += 1
        try:
            response = self.session.get(url, timeout=15, allow_redirects=True)
        except requests.RequestException:
            return "", url, "network"
        if response.status_code == 200:
            return response.text, unwrap_redirect_url(response.url), "ok"
        if response.status_code == 429:
            return "", url, "http_429"
        # Reuse the Board transport for official sites that require a browser.
        if response.status_code in {401, 403} and self.page_requests < self.page_limit and local["pages"] < 4:
            self.page_requests += 1
            local["pages"] += 1
            html, final_url, failure = board._scrapling_fetch(url)
            return html, final_url, failure or "ok"
        return "", url, f"http_{response.status_code}"

    def recover(self, row: dict, *, previous: dict, context: dict, store: dict, now: datetime,
                cheap_only: bool = False) -> str:
        """Return resolution method or a deferred/no-match reason."""
        if len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS:
            return "already_resolved"
        if normalize_title_key(str(previous.get("title") or "")) == normalize_title_key(str(row.get("title") or "")):
            cached_at = _stamp(previous.get("official_jd_fetched_at"))
            if cached_at and now - cached_at <= timedelta(days=CACHE_DAYS) and len(str(previous.get("description") or "").strip()) >= board.THIN_JD_CHARS:
                for field in ("description", "application_url", "official_jd_fetched_at", "official_search_verified"):
                    if previous.get(field):
                        row[field] = previous[field]
                row["enrichment_method"] = "official_cache"
                row["enrichment_status"] = "resolved"
                row["official_search_status"] = "resolved"
                self.stats["cache"] += 1
                return "cache"
        key = (str(row.get("source") or ""), str(row.get("job_id") or ""))
        if not self.store_by_id:
            self.store_by_id = {
                (str(entry.get("source") or ""), str(entry.get("job_id") or "")): entry
                for entry in store.values() if entry.get("job_id")
            }
        for entry in [self.store_by_id.get(key, {})]:
            if normalize_title_key(str(entry.get("title") or "")) == normalize_title_key(str(row.get("title") or "")) and len(str(entry.get("description") or "").strip()) >= board.THIN_JD_CHARS:
                row["description"] = entry["description"]
                if entry.get("official_url"):
                    row["application_url"] = entry["official_url"]
                    row["official_search_verified"] = True
                    row["official_jd_fetched_at"] = now.isoformat()
                row["enrichment_method"] = "board_cache"
                row["enrichment_status"] = "resolved"
                row["official_search_status"] = "resolved" if row.get("official_search_verified") else ""
                self.stats["cache"] += 1
                return "cache"
        company = str(row.get("company") or "")
        cid = coverage_reconcile.company_id_for(company, context.get("registry_entries", []))
        official = None
        if cid:
            probe = dict(row)
            for field in ("application_url", "requisition_id", "req_id"):
                if not probe.get(field) and previous.get(field):
                    probe[field] = previous[field]
            _method, official = coverage_reconcile.exact_match(probe, context.get("by_company", {}).get(cid, []))
        company_key = normalize_company_key(company)
        if company_key not in self.pattern_cache:
            self.pattern_cache[company_key] = _patterns(company, context, store)
            self.listing_cache[company_key] = _listing_urls(company, context, store)
        patterns = self.pattern_cache[company_key]
        local = Counter()
        variant_candidates: list[tuple[str, str]] = []

        def accept(url: str, method: str, *, variant: bool = False) -> bool:
            if not _credible(url, company, patterns) or local["candidates"] >= 2:
                return False
            local["candidates"] += 1
            html, final_url, status = self.page(url, local)
            if status != "ok":
                if status == "budget":
                    local["deferred"] += 1
                else:
                    local["errors"] += 1
                return False
            if not _credible(final_url, company, patterns):
                return False
            description = _verified_posting(row, html, variant=variant)
            if not description:
                if method == "site_exact":
                    variant_description = _verified_posting(row, html, variant=True)
                    if variant_description:
                        variant_candidates.append((final_url, variant_description))
                return False
            row.update(description=description, application_url=final_url,
                       official_search_verified=True, official_jd_fetched_at=now.isoformat(),
                       jd_recovery_at=now.isoformat(), enrichment_method=method,
                       enrichment_status="resolved", official_search_status="resolved", direct_original_fetched=True,
                       direct_original_fetched_at=now.isoformat())
            row.pop("enrichment_failure_reason", None)
            patterns.add(_host(final_url))
            self.stats[method] += 1
            return True

        if official:
            if key not in self.dedicated_seen:
                self.dedicated_seen.add(key)
                self.stats["dedicated_matches"] += 1
            official_url = str(official.get("official_url") or official.get("application_url") or "")
            if len(str(official.get("description") or "").strip()) >= board.THIN_JD_CHARS and official_url:
                row.update(description=official["description"], application_url=official_url,
                           official_search_verified=True, official_jd_fetched_at=now.isoformat(),
                           jd_recovery_at=now.isoformat(), enrichment_method="dedicated_official",
                           enrichment_status="resolved", official_search_status="resolved", direct_original_fetched=True,
                           direct_original_fetched_at=now.isoformat())
                self.stats["dedicated_official"] += 1
                return "dedicated_official"
            if official_url and not cheap_only and accept(official_url, "dedicated_official"):
                return "dedicated_official"
            if official_url:
                row["_linkedin_official_url"] = official_url
                row["_linkedin_official_defer"] = True

        if cheap_only:
            return "pending"

        prior_no_match = _stamp(previous.get("official_search_attempted_at"))
        if previous.get("official_search_status") == "no_match" and prior_no_match and now - prior_no_match < timedelta(hours=NO_MATCH_HOURS):
            row["official_search_status"] = "no_match"
            row["official_search_attempted_at"] = previous["official_search_attempted_at"]
            return "no_match_cached"

        title = str(row.get("title") or "").strip()
        location = str(row.get("location") or "").strip()
        queries = [f'"{title}" "{company}"', f'"{title}" "{company}" "{location}"',
                   f'{company} {title} careers jobs']
        discovered: list[str] = []
        for index, query in enumerate(queries, 1):
            urls, status = self.search(query)
            if status != "ok":
                local["deferred" if status == "budget" else "errors"] += 1
                if status == "budget":
                    break
                continue
            for url in urls:
                if not _credible(url, company, patterns):
                    continue
                host = _host(url)
                if host and host not in discovered:
                    discovered.append(host)
                if accept(url, f"generic_{index}"):
                    return f"generic_{index}"
                if local["candidates"] >= 2:
                    break
            if local["candidates"] >= 2:
                local["deferred"] += 1

        hosts = list(dict.fromkeys([*sorted(patterns), *discovered]))[:2]
        # Inspect verified ATS board paths and employer career homepages.
        for host in hosts:
            if local["pages"] >= 2 or local["candidates"] >= 2:
                break
            starts = [url for url in self.listing_cache[company_key] if _host(url) == host]
            start_url = starts[0] if starts else f"https://{host}/"
            html, final_url, status = self.page(start_url, local)
            if status != "ok":
                local["deferred" if status == "budget" else "errors"] += 1
                continue
            links = []
            for link in BeautifulSoup(html, "html.parser").select("a[href]"):
                label = normalize_space(link.get_text(" ")).lower()
                target = urljoin(final_url, str(link.get("href") or ""))
                if normalize_title_key(title) in normalize_title_key(label) and _credible(target, company, patterns):
                    if accept(target, "direct_careers"):
                        return "direct_careers"
                if re.search(r"\b(careers|jobs|open positions)\b", label) and _credible(target, company, patterns):
                    links.append(target)
            for target in list(dict.fromkeys(links))[:1]:
                careers_html, careers_url, careers_status = self.page(target, local)
                if careers_status != "ok":
                    local["deferred" if careers_status == "budget" else "errors"] += 1
                    continue
                for link in BeautifulSoup(careers_html, "html.parser").select("a[href]"):
                    if normalize_title_key(title) not in normalize_title_key(link.get_text(" ")):
                        continue
                    candidate = urljoin(careers_url, str(link.get("href") or ""))
                    if accept(candidate, "direct_careers"):
                        return "direct_careers"

        for host in hosts:
            urls, status = self.search(f'site:{host} "{title}" "{company}"')
            if status != "ok":
                local["deferred" if status == "budget" else "errors"] += 1
                continue
            for url in urls:
                if _host(url) != host or not _credible(url, company, patterns):
                    continue
                if accept(url, "site_exact"):
                    return "site_exact"
        # The already-fetched candidate may use a deterministic title variant.
        # Do not choose one if the bounded evidence contains a second match.
        unique = {url: description for url, description in variant_candidates}
        if len(unique) == 1 and not local["deferred"] and not local["errors"]:
            url, description = next(iter(unique.items()))
            row.update(description=description, application_url=url,
                       official_search_verified=True, official_jd_fetched_at=now.isoformat(),
                       jd_recovery_at=now.isoformat(), enrichment_method="title_fallback",
                       enrichment_status="resolved", official_search_status="resolved", direct_original_fetched=True,
                       direct_original_fetched_at=now.isoformat())
            row.pop("enrichment_failure_reason", None)
            self.stats["title_fallback"] += 1
            return "title_fallback"

        row["official_search_attempted_at"] = now.isoformat()
        if local["deferred"] or local["errors"] or local["candidates"] >= 2 or not self._available():
            row["official_search_status"] = "deferred"
            self.stats["deferred"] += 1
            return "deferred"
        row["official_search_status"] = "no_match"
        self.stats["no_match"] += 1
        return "no_match"
