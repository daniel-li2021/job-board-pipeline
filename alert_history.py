#!/usr/bin/env python3
"""Persist the exact jobs emitted by automation digests.

Dashboard Fresh is an activity feed: it should mirror jobs placed in recent
GitHub alert Issues, including B->A promotions whose original first_seen is
older. Each pipeline owns its history file under its own output directory.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from sources.schema import dedup_key

RETENTION_DAYS = 14
SNAPSHOT_FIELDS = (
    "canonical_job_key", "job_id", "tier", "match_score", "fit_score",
    "company", "title", "location", "posted_date", "posting_date",
    "date_confidence", "first_seen", "referral_name", "target_company_match",
    "review_status", "official_url", "source_url", "job_url", "url", "source",
)


def parse_stamp(stamp: str) -> Optional[datetime]:
    try:
        return datetime.strptime(stamp, "%Y-%m-%d_%H%M").replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


def _read(path: Path) -> Dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"events": []}
    return payload if isinstance(payload, dict) else {"events": []}


def job_snapshot(job: Dict[str, Any]) -> Dict[str, Any]:
    row = {field: job.get(field, "") for field in SNAPSHOT_FIELDS if job.get(field) not in (None, "")}
    row["canonical_job_key"] = job.get("canonical_job_key") or dedup_key(job)
    row["url"] = (
        job.get("official_url") or job.get("source_url") or job.get("job_url")
        or job.get("url") or ""
    )
    return row


def append_event(
    path: Path,
    *,
    pipeline: str,
    stamp: str,
    jobs: Iterable[Dict[str, Any]],
    event_kind: str,
    emitted_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Append or replace one idempotent pipeline+stamp alert event."""
    now = emitted_at or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    payload = _read(path)
    events = [event for event in payload.get("events", []) if isinstance(event, dict)]
    cutoff = now.astimezone(timezone.utc) - timedelta(days=RETENTION_DAYS)
    kept: List[Dict[str, Any]] = []
    for event in events:
        when = parse_stamp(str(event.get("stamp") or ""))
        if when and when >= cutoff and not (
            event.get("pipeline") == pipeline and event.get("stamp") == stamp
        ):
            kept.append(event)
    kept.append({
        "pipeline": pipeline,
        "stamp": stamp,
        "emitted_at": now.astimezone(timezone.utc).isoformat(),
        "event_kind": event_kind,
        "count": 0,
        "jobs": [job_snapshot(job) for job in jobs],
    })
    kept[-1]["count"] = len(kept[-1]["jobs"])
    kept.sort(key=lambda event: str(event.get("emitted_at") or event.get("stamp") or ""))
    result = {"retention_days": RETENTION_DAYS, "events": kept}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def recent_events(path: Path, now: datetime, hours: int = 24) -> List[Dict[str, Any]]:
    cutoff = now.astimezone(timezone.utc) - timedelta(hours=hours)
    events: List[Dict[str, Any]] = []
    for event in _read(path).get("events", []):
        if not isinstance(event, dict):
            continue
        when_raw = event.get("emitted_at")
        try:
            when = datetime.fromisoformat(str(when_raw).replace("Z", "+00:00"))
        except ValueError:
            when = parse_stamp(str(event.get("stamp") or ""))
        if when and when.astimezone(timezone.utc) >= cutoff:
            events.append(event)
    return events
