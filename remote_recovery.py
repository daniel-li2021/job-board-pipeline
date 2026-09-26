"""Small, durable handoff of remote discovery to the Mac JD resolver."""

from __future__ import annotations

import gzip
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

from state_io import atomic_write

FIELDS = ("company", "title", "location", "source", "official_url", "source_url",
          "job_id", "requisition_id", "description", "first_seen")


def _record(row: dict, pipeline: str) -> dict | None:
    company = str(row.get("company") or "").strip()
    title = str(row.get("title") or "").strip()
    if not company or not title:
        return None
    record = {field: row.get(field) or "" for field in FIELDS}
    record["company"] = company
    record["title"] = title
    record["source"] = str(row.get("source") or pipeline)
    record["official_url"] = str(row.get("official_url") or row.get("application_url") or "")
    record["source_url"] = str(row.get("source_url") or row.get("job_url") or row.get("url") or "")
    record["description"] = str(row.get("description") or row.get("requirements") or row.get("snippet") or "")
    record["requisition_id"] = str(row.get("requisition_id") or row.get("req_id") or "")
    record["recovery_status"] = "jd_available" if len(record["description"].strip()) >= 200 else "candidate"
    return record


def write_snapshot(path: Path, pipeline: str, rows: Iterable[dict]) -> None:
    """Persist discovered records before filtering or matching can discard them."""
    now = datetime.now(timezone.utc)
    def identity(record: dict) -> str:
        prefix = "|".join(str(record[field]).casefold() for field in ("source", "company"))
        if record.get("job_id"):
            return prefix + "|id|" + str(record["job_id"]).casefold()
        url = record.get("official_url") or record.get("source_url")
        if url:
            return prefix + "|url|" + str(url).casefold()
        return prefix + "|title|" + str(record.get("title") or "").casefold() + "|" + str(record.get("location") or "").casefold()

    records: dict[str, dict] = {}
    for prior in read_snapshot(path):
        try:
            seen = datetime.fromisoformat(str(prior.get("first_seen") or "").replace("Z", "+00:00"))
            if seen.tzinfo is None:
                seen = seen.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        if seen >= now - timedelta(days=30):
            records[identity(prior)] = prior
    for row in rows:
        record = _record(row, pipeline)
        if record is None:
            continue
        record["first_seen"] = str(record.get("first_seen") or now.isoformat())
        key = identity(record)
        prior = records.get(key)
        if prior and len(record["description"].strip()) < 200 and len(str(prior.get("description") or "").strip()) >= 200:
            record["description"] = prior["description"]
            record["recovery_status"] = "jd_available"
        records[key] = record
    payload = {"schema_version": 1, "pipeline": pipeline,
               "updated_at": datetime.now(timezone.utc).isoformat(),
               "count": len(records), "jobs": list(records.values())}
    atomic_write(path, gzip.compress(json.dumps(payload, ensure_ascii=False,
                                                separators=(",", ":")).encode(), mtime=0))


def read_snapshot(path: Path) -> list[dict]:
    try:
        payload = json.loads(gzip.decompress(path.read_bytes()))
    except (OSError, ValueError, EOFError):
        return []
    return [row for row in payload.get("jobs", []) if isinstance(row, dict)]
