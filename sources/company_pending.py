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
    if not isinstance(aliases, list) or not isinstance(tags, list):
        return None
    entry = {"name": name, "aliases": [str(a).strip() for a in aliases if str(a).strip()]}
    entry.update({field: str(value.get(field) or "unknown") for field in SCREENING_FIELDS})
    entry["tags"] = [str(tag).strip() for tag in tags if str(tag).strip()]
    return entry
