"""Shared freshness and outbound recovery limits."""

from __future__ import annotations

import hashlib
import json
import time
from datetime import datetime, timedelta, timezone


def stamp(value: object) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value or "").replace("Z", "+00:00"))
        return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def fresh(row: dict, now: datetime) -> bool:
    seen = stamp(row.get("first_seen"))
    return seen is not None and timedelta(0) <= now - seen <= timedelta(hours=24)


def identity(row: dict) -> str:
    source = str(row.get("source") or "").casefold()
    job_id = str(row.get("job_id") or "").casefold()
    if job_id:
        return f"{source}|id|{job_id}"
    url = str(row.get("source_url") or row.get("official_url") or row.get("application_url") or "").casefold()
    if url:
        return f"{source}|url|{url}"
    return "|".join(str(row.get(key) or "").casefold() for key in ("source", "company", "title", "location"))


def evidence_hash(row: dict, *extra: object) -> str:
    fields = ("company", "title", "location", "source_url", "official_url", "application_url", "job_id", "requisition_id")
    payload = [str(row.get(field) or "") for field in fields] + [str(item or "") for item in extra]
    return hashlib.sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()[:20]


class RecoveryBudget:
    def __init__(self, max_jobs: int = 100, seconds: int = 20 * 60):
        self.max_jobs = max_jobs
        self.seconds = seconds
        self.deadline: float | None = None
        self.attempted: set[str] = set()

    def available(self, row: dict | None = None) -> bool:
        if self.deadline is not None and time.monotonic() >= self.deadline:
            return False
        return row is None or identity(row) in self.attempted or len(self.attempted) < self.max_jobs

    def claim(self, row: dict) -> bool:
        if not self.available(row):
            return False
        if self.deadline is None:
            self.deadline = time.monotonic() + self.seconds
        self.attempted.add(identity(row))
        return True

    @property
    def deadline_reached(self) -> bool:
        return self.deadline is not None and time.monotonic() >= self.deadline
