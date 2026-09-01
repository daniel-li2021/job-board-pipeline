"""Incremental detail-cache and newest-first pagination policies."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Iterable, Optional, Set


DETAIL_STALE_DAYS = 14
MIN_NEWEST_PAGES = 2
CONSISTENT_OVERLAP_PAGES = 2
RELATIVE_POSTING_RE = re.compile(
    r"^(?:posted\s+)?(?:today|yesterday|\d+\+?\s+days?\s+ago)$",
    re.IGNORECASE,
)


def _identity(company: str, job_id: str, url: str) -> tuple[str, str]:
    company_key = " ".join((company or "").lower().split())
    return company_key, (job_id or url or "").strip().lower()


def _stable_listing_date(value: str) -> str:
    normalized = " ".join((value or "").split())
    return "" if RELATIVE_POSTING_RE.fullmatch(normalized) else normalized


def listing_signature(title: str = "", posted_date: str = "", updated_date: str = "") -> str:
    payload = [
        " ".join((title or "").lower().split()),
        _stable_listing_date(posted_date),
        _stable_listing_date(updated_date),
    ]
    return hashlib.sha1(json.dumps(payload, separators=(",", ":")).encode("utf-8")).hexdigest()


def _parse_time(value: str) -> Optional[datetime]:
    try:
        parsed = datetime.fromisoformat((value or "").replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


@dataclass
class DetailDecision:
    cached: Optional[Dict[str, Any]]
    should_fetch: bool
    reason: str


class DetailCache:
    def __init__(
        self,
        jobs: Iterable[Dict[str, Any]],
        *,
        now: Optional[datetime] = None,
        stale_days: int = DETAIL_STALE_DAYS,
    ) -> None:
        self.now = now or datetime.now(timezone.utc)
        self.stale_after = timedelta(days=stale_days)
        self._jobs: Dict[tuple[str, str], Dict[str, Any]] = {}
        for job in jobs:
            company = str(job.get("company") or "")
            for identity in (str(job.get("job_id") or ""), str(job.get("official_url") or "")):
                key = _identity(company, identity, "")
                if all(key):
                    self._jobs[key] = job

    def seen_ids(self, company: str) -> Set[str]:
        company_key = " ".join((company or "").lower().split())
        return {identity for ckey, identity in self._jobs if ckey == company_key and not identity.startswith("http")}

    def decide(
        self,
        *,
        company: str,
        job_id: str,
        url: str,
        title: str = "",
        posted_date: str = "",
        updated_date: str = "",
    ) -> DetailDecision:
        cached = self._jobs.get(_identity(company, job_id, "")) or self._jobs.get(_identity(company, "", url))
        if not cached:
            return DetailDecision(None, True, "new")
        if not (cached.get("description") or "").strip():
            return DetailDecision(cached, True, "missing_detail")
        current_sig = listing_signature(title, posted_date, updated_date)
        previous_sig = cached.get("listing_signature") or listing_signature(
            str(cached.get("title") or ""),
            str(cached.get("posted_date") or ""),
            str(cached.get("updated_date") or ""),
        )
        # Old Workday signatures contain rolling text such as "Posted Today".
        # Compare the stable parts directly so deployment does not force one
        # final detail refresh before the normalized signature is persisted.
        posted_relative = RELATIVE_POSTING_RE.fullmatch(" ".join((posted_date or "").split()))
        updated_relative = RELATIVE_POSTING_RE.fullmatch(" ".join((updated_date or "").split()))
        if posted_relative or updated_relative:
            previous_sig = listing_signature(
                str(cached.get("title") or ""),
                "" if posted_relative else str(cached.get("posted_date") or ""),
                "" if updated_relative else str(cached.get("updated_date") or ""),
            )
        if current_sig != previous_sig:
            return DetailDecision(cached, True, "changed")
        detail_time = _parse_time(str(cached.get("detail_fetched_at") or cached.get("fetched_at") or ""))
        if not detail_time or self.now - detail_time > self.stale_after:
            return DetailDecision(cached, True, "stale")
        return DetailDecision(cached, False, "reused")


def annotate_detail(
    job: Dict[str, Any],
    decision: DetailDecision,
    *,
    detail_fetched: bool,
    listing_title: str,
    listing_posted_date: str = "",
    listing_updated_date: str = "",
) -> None:
    job["listing_signature"] = listing_signature(listing_title, listing_posted_date, listing_updated_date)
    if detail_fetched:
        job["detail_fetched_at"] = job.get("fetched_at") or datetime.now(timezone.utc).isoformat()
        job["detail_cache_status"] = f"fetched:{decision.reason}"
    elif decision.cached:
        job["detail_fetched_at"] = decision.cached.get("detail_fetched_at") or decision.cached.get("fetched_at") or ""
        job["detail_cache_status"] = "reused" if not decision.should_fetch else f"reuse_after_error:{decision.reason}"
    else:
        job["detail_fetched_at"] = ""
        job["detail_cache_status"] = f"missing:{decision.reason}"


class NewestFirstPager:
    """Stop after two seen/old pages plus one additional overlap page."""

    def __init__(
        self,
        seen_ids: Set[str],
        *,
        min_pages: int = MIN_NEWEST_PAGES,
        now: Optional[datetime] = None,
        old_days: int = DETAIL_STALE_DAYS,
    ) -> None:
        self.seen_ids = {str(x).lower() for x in seen_ids}
        self.min_pages = min_pages
        self.old_cutoff = (now or datetime.now(timezone.utc)) - timedelta(days=old_days)
        self._consistent_pages = 0
        self._overlap_due = False

    def should_stop_after(
        self,
        page_number: int,
        page_ids: Iterable[str],
        page_dates: Optional[Iterable[str]] = None,
    ) -> bool:
        ids = [str(x).lower() for x in page_ids if x]
        dates = list(page_dates or [])
        if self._overlap_due:
            return True
        if page_number < self.min_pages or not ids:
            return False
        resolved_dates = [_parse_time(str(value)) for value in dates]
        all_old = bool(resolved_dates) and all(
            value is not None and value < self.old_cutoff for value in resolved_dates
        )
        all_seen_or_old = len(resolved_dates) == len(ids) and all(
            identity in self.seen_ids
            or (resolved_dates[index] is not None and resolved_dates[index] < self.old_cutoff)
            for index, identity in enumerate(ids)
        )
        if all(identity in self.seen_ids for identity in ids) or all_old or all_seen_or_old:
            self._consistent_pages += 1
        else:
            self._consistent_pages = 0
        if self._consistent_pages >= CONSISTENT_OVERLAP_PAGES:
            self._overlap_due = True
        return False
