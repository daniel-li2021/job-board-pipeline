"""Shared, conservative company-alias matching.

``source/target_companies.json`` is the single canonical referral list.  The
same matcher is used by Syncareer, ATS/LinkedIn, official careers, and the
cross-pipeline reconciler so referral/coverage decisions cannot drift.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .schema import normalize_company_key


def prepare_alias_entries(entries: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    prepared: List[Dict[str, Any]] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        name = str(entry.get("name") or "").strip()
        if not name:
            continue
        aliases = list(entry.get("aliases") or []) + [name]
        normalized = sorted(
            {normalize_company_key(str(alias)) for alias in aliases if alias},
            key=len,
            reverse=True,
        )
        prepared.append({**entry, "name": name, "norm_aliases": [a for a in normalized if a]})
    return prepared


def load_alias_file(path: Path, key: str = "companies") -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    entries = payload.get(key, []) if isinstance(payload, dict) else []
    return prepare_alias_entries(entries)


def match_company_alias(company_name: str, entries: Iterable[Dict[str, Any]]) -> Optional[str]:
    """Return the canonical name using safe exact/token/long-alias matching.

    Short aliases such as ``sap`` or ``meta`` only match an exact normalized
    company name or a whole token; long aliases (>=6 chars) may match inside a
    legal company suffix.  Bidirectional substring matching is deliberately
    avoided (it previously matched ``Sapios`` as ``SAP``).
    """

    key = normalize_company_key(company_name)
    if not key:
        return None
    tokens = {t for t in re.split(r"[^a-z0-9]+", (company_name or "").lower()) if t}
    for entry in entries:
        aliases = entry.get("norm_aliases") or []
        for alias in aliases:
            if key == alias or alias in tokens:
                return str(entry.get("name") or "") or None
            if len(alias) >= 6 and alias in key:
                return str(entry.get("name") or "") or None
    return None
