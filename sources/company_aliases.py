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


LEGAL_SUFFIXES = {
    "co", "company", "corp", "corporation", "inc", "incorporated", "llc",
    "limited", "ltd", "plc", "group", "holdings", "services", "usa", "us",
}


def _company_forms(company_name: str) -> set[str]:
    """Return exact normalized forms, optionally without legal suffix tokens."""
    tokens = [t for t in re.split(r"[^a-z0-9]+", (company_name or "").lower()) if t]
    forms = {normalize_company_key(company_name)}
    stripped = list(tokens)
    while stripped and stripped[-1] in LEGAL_SUFFIXES:
        stripped.pop()
    if stripped:
        forms.add("".join(stripped))
    return {form for form in forms if form}


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
    """Return the canonical name using exact, token, and declared aliases only.

    Arbitrary substrings are deliberately forbidden: besides short-alias errors
    such as SAP/Sapios, they can make eHealth match GE HealthCare. Legal suffixes
    are handled by comparing a second normalized form with trailing suffix tokens
    removed.
    """

    key = normalize_company_key(company_name)
    if not key:
        return None
    forms = _company_forms(company_name)
    tokens = {t for t in re.split(r"[^a-z0-9]+", (company_name or "").lower()) if t}
    for entry in entries:
        aliases = entry.get("norm_aliases") or []
        for alias in aliases:
            if alias in forms or alias in tokens:
                return str(entry.get("name") or "") or None
    return None
