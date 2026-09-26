#!/usr/bin/env python3
"""Gate fixed Mac collection slots and missed-slot catch-up checks."""

from __future__ import annotations

import fcntl
import json
import os
import subprocess
import sys
from datetime import datetime, time, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

PACIFIC = ZoneInfo("America/Los_Angeles")
REPO = Path(__file__).resolve().parents[2]
STATE = REPO / "output/logs/local_source_mac_gate.json"
LOCK = REPO / "output/logs/local_source_mac_gate.lock"
SCHEDULE_HOURS = (12, 15, 21)


def _stamp(value: object) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value or ""))
        return parsed.astimezone(PACIFIC) if parsed.tzinfo else parsed.replace(tzinfo=PACIFIC)
    except (TypeError, ValueError):
        return None


def _slots(now: datetime) -> tuple[datetime, datetime]:
    today = [datetime.combine(now.date(), time(hour), PACIFIC) for hour in SCHEDULE_HOURS]
    previous = [slot for slot in today if slot <= now]
    latest = previous[-1] if previous else datetime.combine(
        now.date() - timedelta(days=1), time(SCHEDULE_HOURS[-1]), PACIFIC
    )
    upcoming = [slot for slot in today if slot > now]
    following = upcoming[0] if upcoming else datetime.combine(
        now.date() + timedelta(days=1), time(SCHEDULE_HOURS[0]), PACIFIC
    )
    return latest, following


def decision(now: datetime, state: dict) -> tuple[bool, str, dict]:
    """Run fixed slots; reconsider any missed slot on every ten-minute check."""
    now = now.astimezone(PACIFIC)
    result = dict(state)
    result.pop("deferred_evening", None)
    result.pop("evening_success_date", None)
    last_success = _stamp(state.get("last_success_at"))
    latest, following = _slots(now)
    missed = last_success is None or last_success.astimezone(timezone.utc) < latest.astimezone(timezone.utc)
    fixed = now.hour in SCHEDULE_HOURS and now.minute < 10
    result["last_check_at"] = now.isoformat()
    result["last_scheduled_slot_at"] = latest.isoformat()
    result["next_scheduled_run_at"] = following.isoformat()
    result["scheduled_slot_missed"] = missed
    if not missed:
        status, reason, run = "not_needed", "latest slot completed", False
    elif fixed:
        status, reason, run = "scheduled", "fixed slot", True
    elif now.hour == 17:
        status, reason, run = "pending", "5-6 PM Pacific quiet hour", False
    elif last_success and (now.astimezone(timezone.utc) - last_success.astimezone(timezone.utc)) < timedelta(hours=3):
        status, reason, run = "skipped", "successful Local round within three hours", False
    else:
        status, reason, run = "due", "missed scheduled slot", True
    result["catch_up_status"] = status
    result["catch_up_pending"] = missed and not run
    result["catch_up_reason"] = reason
    return run, reason, result


def _write(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    temp = STATE.with_suffix(".tmp")
    temp.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, STATE)


def main() -> int:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    with LOCK.open("a+") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Mac local-source round already running; coalescing trigger")
            return 0
        try:
            state = json.loads(STATE.read_text(encoding="utf-8"))
        except (FileNotFoundError, OSError, ValueError):
            state = {}
        now = datetime.now(PACIFIC)
        run, reason, state = decision(now, state)
        _write(state)
        print(f"Mac local-source gate: {reason}", flush=True)
        if not run:
            return 0
        env = dict(os.environ, LOCAL_SOURCE_PROFILE="mac",
                   LOCAL_SOURCE_RESULT_PATH=str(RESULT))
        completed = subprocess.run(["/bin/bash", str(REPO / "scripts/local_source_sync.sh")], cwd=REPO, env=env)
        if completed.returncode:
            state["last_failure_at"] = datetime.now(PACIFIC).isoformat()
            state["last_run_status"] = "failed"
            _, _, state = decision(datetime.now(PACIFIC), state)
            _write(state)
            return completed.returncode
        finished = datetime.now(PACIFIC)
        state["last_success_at"] = finished.isoformat()
        state["last_run_status"] = "success"
        _, _, state = decision(finished, state)
        _write(state)
        return 0


if __name__ == "__main__":
    sys.exit(main())
