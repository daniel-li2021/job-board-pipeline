"""Shared, conservative company-alias matching.

``config/target_companies.json`` is the single canonical referral list.  The
same matcher is used by Syncareer, ATS/LinkedIn, official careers, and the
cross-pipeline reconciler so referral/coverage decisions cannot drift.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional
from urllib.parse import urlsplit

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
        excluded = {
            form
            for alias in entry.get("exclude_aliases") or []
            for form in _company_forms(str(alias))
        }
        prepared.append({
            **entry,
            "name": name,
            "norm_aliases": [a for a in normalized if a],
            "norm_exclude_aliases": sorted(excluded),
        })
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


def match_company_entry(
    company_name: str, entries: Iterable[Dict[str, Any]]
) -> Optional[Dict[str, Any]]:
    """Return the matching canonical entry using declared aliases only.

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
    fallback = None
    for entry in entries:
        if forms.intersection(entry.get("norm_exclude_aliases") or []):
            continue
        aliases = entry.get("norm_aliases") or []
        if key in aliases:
            return entry
        for alias in aliases:
            if fallback is None and (alias in forms or alias in tokens):
                fallback = entry
    return fallback


def match_company_alias(company_name: str, entries: Iterable[Dict[str, Any]]) -> Optional[str]:
    """Return the canonical name using exact, token, and declared aliases only."""
    entry = match_company_entry(company_name, entries)
    return (str(entry.get("name") or "") or None) if entry else None


def company_risk_rank(entry: Dict[str, Any]) -> int:
    """Rank employer exposure: defense/government above cybersecurity."""
    tags = set(entry.get("tags") or [])
    if entry.get("type") == "government" or tags & {
        "clearance_heavy", "clearance_risk", "defense", "government", "government_contracting",
    }:
        return 2
    return int("cybersecurity" in tags)


def recover_missing_company(job: Dict[str, Any], profiles: Iterable[Dict[str, Any]]) -> bool:
    """Name an anonymous source-ID card from a curated, exact Ashby tenant.

    Tenant identity does not verify the posting, its JD, or role sponsorship.
    """
    if job.get("company") or not job.get("job_id") or job.get("source") not in {"indeed", "linkedin", "glassdoor"}:
        return False
    tenants: Dict[str, set[str]] = {}
    for profile in profiles:
        board = urlsplit(str(profile.get("career_board_url") or ""))
        if board.scheme == "https" and board.netloc == "jobs.ashbyhq.com" and re.fullmatch(r"/[A-Za-z0-9_-]+/?", board.path):
            tenants.setdefault(board.path.strip("/").casefold(), set()).add(profile["name"])
    matches = {}
    for field in ("official_url", "application_url"):
        url = urlsplit(str(job.get(field) or ""))
        path = re.fullmatch(r"/([A-Za-z0-9_-]+)/([a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12})/?", url.path)
        if url.scheme != "https" or url.netloc != "jobs.ashbyhq.com" or not path:
            continue
        names = tenants.get(path[1].casefold(), set())
        if len(names) != 1:
            return False
        matches[next(iter(names))] = f"https://jobs.ashbyhq.com/{path[1]}"
    if len(matches) != 1:
        return False
    name, evidence = next(iter(matches.items()))
    job.update(company=name, company_identity_method="curated_ats_tenant", company_identity_url=evidence)
    return True


def preserve_source_company(job: Dict[str, Any], previous: Dict[str, Any]) -> None:
    """A temporarily missing employer must not erase a name on the same source ID."""
    if (not str(job.get("company") or "").strip() and previous.get("company")
            and job.get("job_id") and job.get("job_id") == previous.get("job_id")
            and job.get("source") == previous.get("source")):
        job["company"] = previous["company"]
        job["company_identity_method"] = previous.get("company_identity_method") or "previous_source_id"
        if previous.get("company_identity_url"):
            job["company_identity_url"] = previous["company_identity_url"]
