#!/usr/bin/env python3
"""Update the committed lightweight tracked-job store."""

from __future__ import annotations

import argparse
import json

from state_io import atomic_write, decode_json_bytes, read_json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import coverage_reconcile

BASE_DIR = Path(__file__).resolve().parent
STATE_PATH = BASE_DIR / "output" / "tracked_jobs.json"
STORE_PATHS = (
    BASE_DIR / "output" / "board" / "jobs.json",
    BASE_DIR / "output" / "official_careers" / "jobs.json",
    BASE_DIR / "output" / "syncareer" / "jobs.json",
)
STATUSES = {"unreviewed", "in_progress", "applied"}
TRACKED_FIELDS = (
    "company", "title", "location", "posted_date", "first_seen", "tier",
    "sponsorship", "canonical_source",
)
ARCHIVE_PREFIX = "applied-archive::"


def _read(path: Path, default: Any) -> Any:
    try:
        return decode_json_bytes(path.read_bytes())
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return default


def _entries() -> Iterable[Dict[str, Any]]:
    for path in STORE_PATHS:
        payload = _read(path, {})
        for entry in payload.get("entries", []) if isinstance(payload, dict) else []:
            if isinstance(entry, dict):
                yield entry


def _current_snapshots() -> Dict[str, Dict[str, Any]]:
    snapshots: Dict[str, Dict[str, Any]] = {}
    for path in STORE_PATHS:
        payload = _read(path, {})
        for entry in payload.get("entries", []) if isinstance(payload, dict) else []:
            if not isinstance(entry, dict):
                continue
            entry_key = str(entry.get("canonical_job_key") or coverage_reconcile.canonical_job_key(entry))
            pipeline = {"official_careers": "official", "syncareer": "syncareer"}.get(path.parent.name, "board")
            snapshot = {field: entry.get(field, "") for field in TRACKED_FIELDS}
            snapshot.update({
                "canonical_job_key": entry_key,
                "pipeline": pipeline,
                "url": entry.get("official_url") or entry.get("source_url") or entry.get("job_url") or entry.get("url") or "",
                "score": entry.get("match_score") if entry.get("match_score") is not None else entry.get("fit_score", ""),
            })
            snapshots[entry_key] = snapshot
    return snapshots


def _job_snapshot(key: str) -> Dict[str, Any]:
    return _current_snapshots().get(key, {"canonical_job_key": key})


def _archive_snapshots(states: Iterable[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    snapshots: Dict[str, Dict[str, Any]] = {}
    for state in states:
        storage_key = str(state.get("canonical_job_key") or "")
        if not storage_key.startswith(ARCHIVE_PREFIX):
            continue
        try:
            compact = json.loads(storage_key[len(ARCHIVE_PREFIX):])
        except (json.JSONDecodeError, TypeError):
            continue
        key = str(compact.get("k") or "") if isinstance(compact, dict) else ""
        if not key:
            continue
        snapshot = {
            "canonical_job_key": key, "pipeline": compact.get("p", ""),
            "company": compact.get("c", ""), "title": compact.get("t", ""),
            "location": compact.get("l", ""), "url": compact.get("u", ""),
            "posted_date": compact.get("d", ""), "tier": compact.get("tier", "-"),
            "score": compact.get("score", ""), "applied_at": compact.get("applied", ""),
            "archive_updated_at": state.get("updated_at", ""),
        }
        previous = snapshots.get(key, {})
        if str(snapshot["archive_updated_at"]) >= str(previous.get("archive_updated_at", "")):
            snapshots[key] = snapshot
    return snapshots


def sync_remote_states(states: Iterable[Dict[str, Any]]) -> int:
    """Replace tracked jobs from live statuses while retaining lightweight metadata."""
    rows = [row for row in states if isinstance(row, dict)]
    archives, current = _archive_snapshots(rows), _current_snapshots()
    existing = read_json(STATE_PATH, {"jobs": {}})
    if not isinstance(existing, dict) or not isinstance(existing.get("jobs", {}), dict):
        raise ValueError(f"Invalid review state: {STATE_PATH}")
    jobs: Dict[str, Dict[str, Any]] = {}
    for state in rows:
        key, status = str(state.get("canonical_job_key") or ""), str(state.get("status") or "")
        if not key or key.startswith(("company::", ARCHIVE_PREFIX)) or state.get("deleted"):
            continue
        if status not in {"in_progress", "applied", "applied_complete"}:
            continue
        record: Dict[str, Any] = {"canonical_job_key": key}
        for source in (existing["jobs"].get(key, {}), archives.get(key, {}), current.get(key, {})):
            record.update({field: value for field, value in source.items() if value not in (None, "")})
        record["status"] = "applied" if status in {"applied", "applied_complete"} else status
        record["updated_at"] = str(state.get("updated_at") or "")
        if record["status"] == "applied" and not record.get("applied_at"):
            record["applied_at"] = record["updated_at"]
        record.pop("archive_updated_at", None)
        jobs[key] = record
    updated_at = max((str(job.get("updated_at") or "") for job in jobs.values()), default="")
    payload = {"updated_at": updated_at, "count": len(jobs), "jobs": dict(sorted(jobs.items()))}
    atomic_write(STATE_PATH, (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    return len(jobs)


def fetch_supabase_states(url: str, key: str) -> list[Dict[str, Any]]:
    import requests

    rows: list[Dict[str, Any]] = []
    for offset in range(0, 100_000, 1000):
        response = requests.get(
            f"{url}/rest/v1/job_review_status",
            params={"select": "canonical_job_key,status,deleted,updated_at"},
            headers={"apikey": key, "Authorization": f"Bearer {key}", "Range": f"{offset}-{offset + 999}"},
            timeout=30,
        )
        response.raise_for_status()
        page = response.json()
        if not isinstance(page, list):
            raise ValueError("Supabase review-state response must be a list")
        rows.extend(item for item in page if isinstance(item, dict))
        if len(page) < 1000:
            return rows
    raise ValueError("Supabase review-state pagination exceeded 100,000 rows")


def resolve_selector(selector: str) -> Optional[str]:
    """Resolve a canonical key, exact URL, or unique job ID selector."""
    selector = selector.strip()
    matches: list[str] = []
    for entry in _entries():
        key = str(entry.get("canonical_job_key") or coverage_reconcile.canonical_job_key(entry))
        values = {
            key,
            str(entry.get("job_id") or ""),
            str(entry.get("official_url") or ""),
            str(entry.get("source_url") or entry.get("job_url") or entry.get("url") or ""),
        }
        if selector in values:
            matches.append(key)
    unique = sorted(set(matches))
    if selector.startswith(("url::", "id::", "composite::")):
        return selector
    if len(unique) == 1:
        return unique[0]
    if len(unique) > 1:
        raise SystemExit(f"Selector matched {len(unique)} jobs; use the canonical_job_key instead.")
    return None


def set_status(selector: str, status: str, notes: str = "") -> str:
    if status not in STATUSES:
        raise SystemExit(f"Invalid status {status!r}. Choose: {', '.join(sorted(STATUSES))}")
    key = resolve_selector(selector)
    if not key:
        raise SystemExit("Job not found. Use its canonical_job_key, exact URL, or unique job ID.")
    payload = read_json(STATE_PATH, {"jobs": {}})
    if not isinstance(payload, dict):
        raise ValueError(f"Invalid review state: {STATE_PATH}")
    jobs = payload.setdefault("jobs", {})
    if not isinstance(jobs, dict):
        raise ValueError(f"Invalid review state: {STATE_PATH}")
    if status == "unreviewed":
        jobs.pop(key, None)
        payload["updated_at"] = datetime.now(timezone.utc).isoformat()
        payload["count"] = len(jobs)
        atomic_write(STATE_PATH, (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
        return key
    record = {
        **_job_snapshot(key), **(jobs.get(key) or {}),
        "status": status, "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    if notes:
        record["notes"] = notes
    jobs[key] = record
    payload["updated_at"] = record["updated_at"]
    payload["count"] = len(jobs)
    atomic_write(STATE_PATH, (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    return key


def main() -> None:
    parser = argparse.ArgumentParser(description="Set a dashboard job status")
    parser.add_argument("selector", nargs="?", help="canonical_job_key, exact URL, or unique job ID")
    parser.add_argument("status", nargs="?", choices=sorted(STATUSES))
    parser.add_argument("--notes", default="")
    parser.add_argument("--sync-supabase", action="store_true", help="Refresh tracked_jobs.json from live review state")
    args = parser.parse_args()
    if args.sync_supabase:
        import dashboard
        count = sync_remote_states(fetch_supabase_states(dashboard.SUPABASE_URL, dashboard.SUPABASE_PUBLISHABLE_KEY))
        print(f"Synced {count} tracked jobs")
        return
    if not args.selector or not args.status:
        parser.error("selector and status are required unless --sync-supabase is used")
    key = set_status(args.selector, args.status, args.notes)
    print(f"Updated {key} -> {args.status}")
    print("Commit output/tracked_jobs.json to retain this tracked-job snapshot; live dashboard changes also use Supabase.")


if __name__ == "__main__":
    main()
