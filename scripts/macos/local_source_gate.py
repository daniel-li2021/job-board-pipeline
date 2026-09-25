#!/usr/bin/env python3
"""Gate the Mac collector's calendar and post-wake launches.

launchd supplies a ten-minute heartbeat and fixed calendar events. A gap in
heartbeats identifies a wake/agent reload without depending on pmset log text.
"""

from __future__ import annotations

import fcntl
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

PACIFIC = ZoneInfo("America/Los_Angeles")
REPO = Path(__file__).resolve().parents[2]
STATE = REPO / "output/logs/local_source_mac_gate.json"
LOCK = REPO / "output/logs/local_source_mac_gate.lock"
RESULT = REPO / "output/logs/local_sources_mac_latest.json"


def _stamp(value: object) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value or ""))
        return parsed.astimezone(PACIFIC) if parsed.tzinfo else parsed.replace(tzinfo=PACIFIC)
    except (TypeError, ValueError):
        return None


def decision(now: datetime, state: dict) -> tuple[bool, str, dict]:
    """Pure scheduling decision; state updates on every heartbeat."""
    now = now.astimezone(PACIFIC)
    result = dict(state)
    last_check = _stamp(state.get("last_check_at"))
    last_success = _stamp(state.get("last_success_at"))
    wake = last_check is None or now - last_check > timedelta(minutes=17)
    fixed = now.hour in {12, 15, 21} and now.minute < 10
    result["last_check_at"] = now.isoformat()
    if now.hour == 17:
        if wake:
            result["deferred_evening"] = True
        return False, "5-6 PM Mac quiet hour", result
    if now.hour >= 18:
        if state.get("evening_success_date") == now.date().isoformat():
            return False, "evening LinkedIn already published", result
        if fixed or wake or state.get("deferred_evening"):
            return True, "evening fixed/wake catch-up", result
        return False, "not due", result
    if not (fixed or wake):
        return False, "not due", result
    if last_success and now - last_success < timedelta(hours=3):
        return False, "three-hour minimum spacing", result
    return True, "fixed/wake catch-up", result


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
            _write(state)
            return completed.returncode
        finished = datetime.now(PACIFIC)
        state["last_success_at"] = finished.isoformat()
        state["deferred_evening"] = False
        try:
            receipt = json.loads(RESULT.read_text(encoding="utf-8"))
            linkedin_usable = any(item.get("source") == "linkedin" and item.get("status") in {"ok", "partial"}
                                  for item in receipt.get("sources", []))
        except (OSError, ValueError):
            linkedin_usable = False
        if finished.hour >= 18 and linkedin_usable:
            state["evening_success_date"] = finished.date().isoformat()
        _write(state)
        return 0


if __name__ == "__main__":
    sys.exit(main())
