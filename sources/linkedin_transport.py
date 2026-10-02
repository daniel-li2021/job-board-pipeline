"""Local LinkedIn traffic allowance, shared by discovery and recovery."""

import json
import random
import time
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

from recovery_policy import stamp
from state_io import atomic_write

ROUND_LIMIT = 18
DETAIL_LIMIT = 8
DAY_LIMIT = 54
DAY_DETAIL_LIMIT = 24
SPACING_SECONDS = 2.5


class RequestDeferred(Exception):
    """An intentional transport pause, with no HTTP attempt."""


class LinkedInTransport:
    def __init__(self, health_path=None, local_path=None):
        self.health_path = health_path
        self.local_path = Path(local_path) if local_path else None
        self.events = []
        self.rate_limits = []
        self.blocked_until = None
        self.counts = {"search": 0, "detail": 0}
        self.closed = False
        self.detail_probe_used = False
        self.stop_reason = ""
        for path in (self.health_path, self.local_path):
            data = self._read(path)
            state = data.get("linkedin_transport", {}) if path == self.health_path else data
            for event in state.get("events", []):
                at = stamp(event.get("at"))
                if at and datetime.now(timezone.utc) - timedelta(hours=24) < at:
                    if event not in self.events:
                        self.events.append(event)
            until = stamp(state.get("blocked_until"))
            if until and (self.blocked_until is None or until > self.blocked_until):
                self.blocked_until = until
            for event in state.get("rate_limits", []):
                if event not in self.rate_limits:
                    self.rate_limits.append(event)

    @staticmethod
    def _read(path):
        if path is None:
            return {}
        try:
            data = json.loads(Path(path).read_text())
            return data if isinstance(data, dict) else {}
        except (OSError, ValueError):
            return {}

    def rolling_counts(self, now):
        return {str(seconds): {
            endpoint: sum(event.get("endpoint") == endpoint and
                          now - timedelta(seconds=seconds) < stamp(event.get("at")) <= now
                          for event in self.events)
            for endpoint in ("search", "detail")
        } for seconds in (60, 3600, 86400)}

    def available(self, endpoint, *, probe=False):
        now = datetime.now(timezone.utc)
        self.events = [event for event in self.events
                       if stamp(event.get("at")) > now - timedelta(hours=24)]
        rolling = self.rolling_counts(now)
        hourly = sum(rolling["3600"].values())
        reason = ("global_429_pause" if self.closed or (self.blocked_until and now < self.blocked_until) else
                  "global_round_budget" if sum(self.counts.values()) >= ROUND_LIMIT else
                  "global_hour_budget" if hourly >= ROUND_LIMIT else
                  "global_day_budget" if len(self.events) >= DAY_LIMIT else
                  "shared_detail_budget" if endpoint == "detail" and self.counts[endpoint] >= DETAIL_LIMIT else
                  "shared_detail_hour_budget" if endpoint == "detail" and rolling["3600"]["detail"] >= DETAIL_LIMIT else
                  "shared_detail_day_budget" if endpoint == "detail" and rolling["86400"]["detail"] >= DAY_DETAIL_LIMIT else
                  "single_detail_probe" if endpoint == "detail" and self.detail_probe_used else "")
        self.stop_reason = reason
        return not reason

    def get(self, session, url, *, endpoint, query="", page=None, probe=False, **kwargs):
        if not self.available(endpoint, probe=probe):
            raise RequestDeferred(self.stop_reason)
        if self.events:
            latest = max(stamp(event["at"]) for event in self.events)
            elapsed = (datetime.now(timezone.utc) - latest).total_seconds()
            delay = SPACING_SECONDS + random.uniform(0, 0.75) - elapsed
            if delay > 0:
                time.sleep(delay)
        now = datetime.now(timezone.utc)
        self.events.append({"at": now.isoformat(), "endpoint": endpoint})
        self.counts[endpoint] += 1
        if endpoint == "detail" and probe:
            self.detail_probe_used = True
        self._save()  # Count attempts even if the network call or collector fails.
        response = session.get(url, allow_redirects=False, **kwargs)
        if response.status_code == 429:
            now = datetime.now(timezone.utc)
            raw = getattr(response, "headers", {}).get("Retry-After", "")
            raw = raw if isinstance(raw, str) else ""
            try:
                retry_at = now + timedelta(seconds=max(0, int(raw)))
            except (ValueError, OverflowError):
                try:
                    retry_at = parsedate_to_datetime(raw).astimezone(timezone.utc)
                except (TypeError, ValueError, OverflowError):
                    retry_at = now
            self.closed = True
            self.blocked_until = max(now + timedelta(hours=1), retry_at)
            self.rate_limits.append({
                "at": now.isoformat(), "endpoint": endpoint, "url": url,
                "query": query, "page": page, "retry_after": raw,
                "retry_after_until": retry_at.isoformat(),
                "request_ordinal": sum(self.counts.values()),
                "endpoint_ordinal": self.counts[endpoint],
                "round_counts": dict(self.counts), "rolling_counts": self.rolling_counts(now),
            })
            self._save()
        return response

    def summary(self):
        return {"requests": sum(self.counts.values()), "endpoint_counts": dict(self.counts),
                "round_limit": ROUND_LIMIT, "detail_limit": DETAIL_LIMIT, "day_limit": DAY_LIMIT,
                "day_detail_limit": DAY_DETAIL_LIMIT,
                "rolling_counts": self.rolling_counts(datetime.now(timezone.utc)),
                "stop_reason": self.stop_reason,
                "blocked_until": self.blocked_until.isoformat() if self.blocked_until else "",
                "rate_limits": self.rate_limits[-20:]}

    def _save(self):
        state = {**self.summary(), "events": self.events}
        for path in (self.health_path, self.local_path):
            if path is None:
                continue
            data = {**self._read(path), "linkedin_transport": state} if path == self.health_path else {**self._read(path), **state}
            atomic_write(Path(path), (json.dumps(data, indent=2) + "\n").encode())
