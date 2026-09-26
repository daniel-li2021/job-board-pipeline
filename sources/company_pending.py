"""Small, backward-compatible shape for unprofiled employers."""

from __future__ import annotations

import re
from typing import Any


SCREENING_FIELDS = ("size", "maturity", "sponsor", "type")
LEGAL_ENDINGS = {"inc", "incorporated", "corp", "corporation", "llc", "llp", "ltd", "limited", "plc", "co", "company"}


def company_key(name: str) -> str:
    """Exact name, allowing only uninformative trailing legal endings."""
    words = re.findall(r"[a-z0-9]+", name.casefold())
    while len(words) > 1 and words[-1] in LEGAL_ENDINGS:
        words.pop()
    return "".join(words)


def pending_entry(value: Any) -> dict[str, Any] | None:
    if isinstance(value, str):
        value = {"name": value}
    if not isinstance(value, dict):
        return None
    name = str(value.get("name") or "").strip()
    if not name:
        return None
    aliases = value.get("aliases") or []
    tags = value.get("tags") or []
    keys = value.get("seen_job_keys") or []
    if not isinstance(aliases, list) or not isinstance(tags, list):
        return None
    if not isinstance(keys, list) or any(not isinstance(key, str) or not re.fullmatch(r"[0-9a-f]{24}", key) for key in keys):
        raise ValueError(f"invalid pending job keys for {name}")
    distinct_jobs = len(set(keys))
    if "seen_count" in value and value["seen_count"] not in {distinct_jobs, max(1, distinct_jobs)}:
        raise ValueError(f"pending seen_count disagrees with job keys for {name}")
    entry = {"name": name, "aliases": [str(a).strip() for a in aliases if str(a).strip()]}
    entry.update({field: str(value.get(field) or "unknown") for field in SCREENING_FIELDS})
    entry["tags"] = [str(tag).strip() for tag in tags if str(tag).strip()]
    entry["seen_job_keys"] = sorted(set(keys))
    entry["seen_count"] = max(1, distinct_jobs)
    return entry
