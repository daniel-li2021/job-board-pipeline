#!/usr/bin/env python3
"""Update the optional committed pipeline review-state overlay."""

from __future__ import annotations

import argparse
import json

from state_io import atomic_write, decode_json_bytes, read_json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import coverage_reconcile

BASE_DIR = Path(__file__).resolve().parent
STATE_PATH = BASE_DIR / "profile" / "review_state.json"
STORE_PATHS = (
    BASE_DIR / "output" / "board" / "jobs.json",
    BASE_DIR / "output" / "official_careers" / "jobs.json",
    BASE_DIR / "output" / "syncareer" / "watchlist.json",
)
STATUSES = {"unreviewed", "in_progress", "applied"}


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
    record = {**(jobs.get(key) or {}), "status": status, "updated_at": datetime.now(timezone.utc).isoformat()}
    if notes:
        record["notes"] = notes
    jobs[key] = record
    atomic_write(STATE_PATH, (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    return key


def main() -> None:
    parser = argparse.ArgumentParser(description="Set a dashboard job status")
    parser.add_argument("selector", help="canonical_job_key, exact URL, or unique job ID")
    parser.add_argument("status", choices=sorted(STATUSES))
    parser.add_argument("--notes", default="")
    args = parser.parse_args()
    key = set_status(args.selector, args.status, args.notes)
    print(f"Updated {key} -> {args.status}")
    print("Commit profile/review_state.json to retain the pipeline overlay; live dashboard status is stored separately in Supabase.")


if __name__ == "__main__":
    main()
