#!/usr/bin/env python3
"""Unified job schema and shared helpers for the board pipeline.

All source adapters normalize to :func:`make_job`. The orchestrator
(``board_pipeline.py``) consumes only these fields, so adding a new source
is just a matter of emitting the same dict shape.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
SOURCES_DIR = OUTPUT_DIR / "sources"

# Unified record fields. Adapters must fill these (missing -> "").
JOB_FIELDS = [
    "job_id",
    "source",
    "company",
    "title",
    "location",
    "posted_date",       # ISO date "YYYY-MM-DD" when known, else ""
    "updated_date",      # ISO date when the source exposes a last-updated time
    "date_confidence",   # high | medium | low | unknown
    "source_url",        # where we found it
    "official_url",      # canonical company/ATS URL when verified, else ""
    "description",
    "fetched_at",        # ISO timestamp when this adapter fetched the record
    "first_seen",        # ISO timestamp, set by the orchestrator on first sight
]


class SourceUnavailable(Exception):
    """Raised by an adapter when it hits login/captcha/403/429/network errors.

    The orchestrator catches this and skips only the failing source.
    """


# --------------------------------------------------------------------------
# Text / location / date helpers
# --------------------------------------------------------------------------
def normalize_space(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


US_HINTS = [
    "united states",
    ", usa",
    ", us",
    "u.s.",
    "remote, us",
    "remote - us",
    "remote (us",
    "remote, usa",
    "remote - usa",
    "remote (usa",
    "remote, united states",
    "united states, remote",
    "usa, remote",
    "us, remote",
    "us remote",
    "usa remote",
    "remote us",
    "san francisco bay area",
]

STATE_ABBRS = {
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC",
}

NON_US_TOKENS = [
    "canada", "india", "china", "japan", "singapore", "ireland",
    "united kingdom", "germany", "france", "spain", "italy",
    "netherlands", "sweden", "switzerland", "australia",
    "new zealand", "mexico", "brazil", "argentina", "poland",
    "korea", "taiwan", "israel", "portugal", "romania", "hungary",
    "philippines", "vietnam", "indonesia", "malaysia", "uae",
    "dubai", "london", "toronto", "vancouver", "bangalore",
    "hyderabad", "beijing", "shanghai", "tokyo", "berlin", "paris",
    "amsterdam", "dublin", "sydney", "norway", "denmark", "finland",
    "belgium", "austria", "oslo", "copenhagen", "helsinki",
]


def classify_location_bucket(location: str) -> str:
    """Return 'us', 'non_us', or 'unknown'."""
    loc = normalize_space(location).lower()
    if not loc:
        return "unknown"
    if any(t in loc for t in US_HINTS):
        return "us"
    if any(t in loc for t in NON_US_TOKENS):
        return "non_us"
    # State-abbreviation match (e.g. "Seattle, WA").
    parts = [p.strip().upper() for p in re.split(r"[,\s/()\-]+", loc) if p.strip()]
    if any(p in STATE_ABBRS for p in parts):
        return "us"
    return "unknown"


def is_us_location(location: str) -> bool:
    return classify_location_bucket(location) == "us"


def to_iso_date(value: Any) -> str:
    """Best-effort convert epoch/relative/ISO strings to 'YYYY-MM-DD'."""
    if value is None or value == "":
        return ""
    # Epoch (seconds or milliseconds).
    if isinstance(value, (int, float)):
        epoch = float(value)
        if epoch > 1e12:  # milliseconds
            epoch /= 1000.0
        if epoch <= 0:
            return ""
        try:
            return datetime.fromtimestamp(epoch, tz=timezone.utc).strftime("%Y-%m-%d")
        except (OverflowError, OSError, ValueError):
            return ""
    text = normalize_space(value)
    if not text:
        return ""
    # "30+ days ago" -> "30 days ago" so the relative parser can match.
    text = re.sub(r"(\d+)\+", r"\1 ", text)
    # Numeric-looking epoch in a string.
    if re.fullmatch(r"\d{10,13}", text):
        return to_iso_date(int(text))
    # Relative: "3 days ago", "12h", "2 weeks ago", "yesterday", "today".
    low = text.lower()
    if "today" in low or "just posted" in low or "hour" in low or re.search(r"\b\d+\s*h\b", low):
        return datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if "yesterday" in low:
        return (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    rel = re.search(r"(\d+)\s*(day|days|d|week|weeks|w|month|months)\b", low)
    if rel:
        amount = int(rel.group(1))
        unit = rel.group(2)
        if unit.startswith("d"):
            delta = timedelta(days=amount)
        elif unit.startswith("w"):
            delta = timedelta(days=7 * amount)
        else:
            delta = timedelta(days=30 * amount)
        return (datetime.now(timezone.utc) - delta).strftime("%Y-%m-%d")
    # Absolute formats.
    cleaned = text.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(cleaned).strftime("%Y-%m-%d")
    except ValueError:
        pass
    for fmt in ("%Y-%m-%d", "%b %d, %Y", "%B %d, %Y", "%m/%d/%Y", "%d %b %Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(text[:len(datetime.now().strftime(fmt)) + 5], fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    # Last resort: leading YYYY-MM-DD.
    m = re.match(r"(\d{4}-\d{2}-\d{2})", text)
    return m.group(1) if m else ""


def days_since(iso_date: str) -> Optional[int]:
    if not iso_date:
        return None
    try:
        d = datetime.strptime(iso_date[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return (datetime.now(timezone.utc) - d).days


def _parse_iso_timestamp(value: str) -> Optional[datetime]:
    value = (value or "").strip()
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        try:
            dt = datetime.strptime(value[:10], "%Y-%m-%d")
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


# Recency bucket ordering (lower rank = fresher = higher priority).
# Trusted official/ATS posted_date buckets (lt3h / 3to24h / 1to3d) outrank
# `newly_discovered` (low-confidence first_seen) so a LinkedIn card found
# today cannot outrank a verified job posted 1–3 days ago.
RECENCY_BUCKETS = ["lt3h", "3to24h", "1to3d", "newly_discovered", "3to7d", "gt7d"]
RECENCY_BUCKET_RANK = {b: i for i, b in enumerate(RECENCY_BUCKETS)}

# Buckets treated as "recent enough" for normal Tier A/B consideration (<=3d).
NORMAL_RECENCY_BUCKETS = {"lt3h", "3to24h", "newly_discovered", "1to3d"}


def _trusted_posted_hours(job: Dict[str, str], now: datetime) -> Optional[float]:
    """Hours since posted_date, only when confidence is high/medium."""
    confidence = (job.get("date_confidence") or "unknown").lower()
    posted = (job.get("posted_date") or "").strip()
    if posted and confidence in ("high", "medium"):
        dt = _parse_iso_timestamp(posted)
        if dt is not None:
            return max(0.0, (now - dt).total_seconds() / 3600.0)
    return None


def recency_hours(job: Dict[str, str], now: Optional[datetime] = None) -> Optional[float]:
    """Best-effort hours since the job became relevant (for diagnostics).

    Trusted posted_date wins; otherwise falls back to discovery time.
    Note: bucketing uses ``recency_bucket`` which keeps posted vs first_seen
    conceptually separate — this helper only exists for coarse reporting.
    """
    now = now or datetime.now(timezone.utc)
    trusted = _trusted_posted_hours(job, now)
    if trusted is not None:
        return trusted
    fs = _parse_iso_timestamp(job.get("first_seen", ""))
    if fs is not None:
        return max(0.0, (now - fs).total_seconds() / 3600.0)
    return None


def recency_bucket(job: Dict[str, str], now: Optional[datetime] = None) -> str:
    """Confidence-aware recency bucket.

    - High/medium-confidence posted_date (official/ATS): use the true
      ``lt3h / 3to24h / 1to3d / 3to7d / gt7d`` buckets.
    - Low/unknown confidence (e.g. LinkedIn reposts): NEVER claim sub-day
      freshness from a posted_date. Use our own discovery time (first_seen):
      found <24h ago -> ``newly_discovered``; else age it into 1to3d/3to7d/gt7d.
    """
    now = now or datetime.now(timezone.utc)
    trusted = _trusted_posted_hours(job, now)
    if trusted is not None:
        if trusted < 3:
            return "lt3h"
        if trusted < 24:
            return "3to24h"
        if trusted < 72:
            return "1to3d"
        if trusted < 168:
            return "3to7d"
        return "gt7d"
    # Low/unknown confidence: rely on discovery time only.
    fs = _parse_iso_timestamp(job.get("first_seen", ""))
    if fs is None:
        return "gt7d"  # unknown recency -> stale (store-only)
    hours = max(0.0, (now - fs).total_seconds() / 3600.0)
    if hours < 24:
        return "newly_discovered"
    if hours < 72:
        return "1to3d"
    if hours < 168:
        return "3to7d"
    return "gt7d"


# --------------------------------------------------------------------------
# Official / ATS URL detection
# --------------------------------------------------------------------------
ATS_URL_MARKERS = [
    "boards.greenhouse.io",
    "job-boards.greenhouse.io",
    "greenhouse.io",
    "jobs.lever.co",
    "lever.co",
    "jobs.ashbyhq.com",
    "ashbyhq.com",
    "myworkdayjobs.com",
    "myworkdaysite.com",
    "avature.net",
    "jobs.sap.com",
    "careers.cisco.com",
    "job-boards.greenhouse.io",
    "amazon.jobs",
    "google.com/about/careers",
    "careers.google.com",
    "metacareers.com",
    "jobs.careers.microsoft.com",
    "careers.microsoft.com",
    "apply.careers.microsoft.com",
    "jobs.apple.com",
    "jobs.bytedance.com",
    "joinbytedance.com",
    "lifeattiktok.com",
    "careers.tiktok.com",
    "jobs.uber.com",
    "eightfold.ai",
    "oraclecloud.com",
    "icims.com",
    "smartrecruiters.com",
    "workable.com",
]


def looks_official(url: str) -> bool:
    u = (url or "").lower()
    return any(marker in u for marker in ATS_URL_MARKERS)


# --------------------------------------------------------------------------
# Normalization + dedup
# --------------------------------------------------------------------------
def normalize_company_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


def normalize_title_key(title: str) -> str:
    t = (title or "").lower()
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# Common US state names -> abbreviations, so "Seattle, Washington" and
# "Seattle, WA" collapse to the same location key.
_STATE_NAME_TO_ABBR = {
    "alabama": "al", "alaska": "ak", "arizona": "az", "arkansas": "ar",
    "california": "ca", "colorado": "co", "connecticut": "ct", "delaware": "de",
    "florida": "fl", "georgia": "ga", "hawaii": "hi", "idaho": "id",
    "illinois": "il", "indiana": "in", "iowa": "ia", "kansas": "ks",
    "kentucky": "ky", "louisiana": "la", "maine": "me", "maryland": "md",
    "massachusetts": "ma", "michigan": "mi", "minnesota": "mn", "mississippi": "ms",
    "missouri": "mo", "montana": "mt", "nebraska": "ne", "nevada": "nv",
    "new hampshire": "nh", "new jersey": "nj", "new mexico": "nm", "new york": "ny",
    "north carolina": "nc", "north dakota": "nd", "ohio": "oh", "oklahoma": "ok",
    "oregon": "or", "pennsylvania": "pa", "rhode island": "ri", "south carolina": "sc",
    "south dakota": "sd", "tennessee": "tn", "texas": "tx", "utah": "ut",
    "vermont": "vt", "virginia": "va", "washington": "wa", "west virginia": "wv",
    "wisconsin": "wi", "wyoming": "wy", "district of columbia": "dc",
}


def normalize_location_key(location: str) -> str:
    """Normalize a location for dedup: city + state abbr, order-independent.

    Returns "" when location is blank. Callers must treat "" as NOT matching
    any other location (blank is never a wildcard).
    """
    loc = (location or "").lower().strip()
    if not loc:
        return ""
    loc = loc.replace("united states", "").replace("u.s.", "").replace("usa", "")
    tokens = [t.strip() for t in re.split(r"[,/;|]+", loc) if t.strip()]
    norm: List[str] = []
    for tok in tokens:
        tok = re.sub(r"[^a-z0-9 ]", " ", tok).strip()
        tok = re.sub(r"\s+", " ", tok)
        if not tok:
            continue
        norm.append(_STATE_NAME_TO_ABBR.get(tok, tok))
    # Order-independent so "CA, San Francisco" == "San Francisco, CA".
    return "|".join(sorted(set(norm)))


# Keep opening (role) + closing (requirements/eligibility). Hard-filter
# citizenship/clearance checks need the end of long JDs; a 4k cap was
# dropping Palantir/Lever "What We Require" sections.
JD_HEAD_CHARS = 5000
JD_TAIL_CHARS = 4000


def retain_description(description: str) -> str:
    text = normalize_space(description)
    if len(text) <= JD_HEAD_CHARS + JD_TAIL_CHARS:
        return text
    return f"{text[:JD_HEAD_CHARS]} {text[-JD_TAIL_CHARS:]}"


def make_job(
    *,
    source: str,
    company: str,
    title: str,
    location: str = "",
    job_id: str = "",
    posted_date: Any = "",
    updated_date: Any = "",
    date_confidence: str = "unknown",
    source_url: str = "",
    official_url: str = "",
    description: str = "",
    fetched_at: str = "",
) -> Dict[str, str]:
    iso = to_iso_date(posted_date)
    if iso and date_confidence == "unknown":
        date_confidence = "medium"
    return {
        "job_id": normalize_space(job_id),
        "source": normalize_space(source),
        "company": normalize_space(company),
        "title": normalize_space(title),
        "location": normalize_space(location),
        "posted_date": iso,
        "updated_date": to_iso_date(updated_date),
        "date_confidence": date_confidence,
        "source_url": normalize_space(source_url),
        "official_url": normalize_space(official_url),
        "description": retain_description(description),
        "fetched_at": normalize_space(fetched_at),
        "first_seen": "",
    }


def dedup_key(job: Dict[str, str]) -> str:
    """Priority: official_url -> source+job_id -> company+title+location.

    Location is REQUIRED in the fallback key so two different-city or
    different-requisition openings with the same title are NOT merged. When
    location is blank we include the source_url so blank never acts as a
    wildcard that collapses distinct postings.
    """
    official = (job.get("official_url") or "").strip().lower().rstrip("/")
    if official:
        return f"url::{official}"
    jid = (job.get("job_id") or "").strip()
    src = (job.get("source") or "").strip().lower()
    if jid:
        return f"id::{src}::{jid}"
    ckey = normalize_company_key(job.get("company", ""))
    tkey = normalize_title_key(job.get("title", ""))
    lkey = normalize_location_key(job.get("location", ""))
    if not lkey:
        # No location: fall back to the source URL so we don't over-merge.
        surl = (job.get("source_url") or "").strip().lower().rstrip("/")
        return f"ctl::{ckey}::{tkey}::url::{surl}"
    return f"ctl::{ckey}::{tkey}::{lkey}"


# --------------------------------------------------------------------------
# Content hashing for the incremental LLM cache
# --------------------------------------------------------------------------
def _sha1(text: str) -> str:
    return hashlib.sha1((text or "").encode("utf-8")).hexdigest()


def jd_hash(job: Dict[str, str]) -> str:
    """Hash of the fields that define a job's content for LLM scoring."""
    basis = "\n".join([
        normalize_company_key(job.get("company", "")),
        normalize_title_key(job.get("title", "")),
        normalize_space(job.get("description", "")),
    ])
    return _sha1(basis)


def combined_cache_key(job: Dict[str, str], profile_fingerprint: str) -> str:
    """Cache key = JD content + resume/profile/prompt fingerprint.

    Changing any resume, the candidate profile, or the prompt version changes
    ``profile_fingerprint`` and thus invalidates all cached scores.
    """
    return _sha1(f"{jd_hash(job)}::{profile_fingerprint}")


# --------------------------------------------------------------------------
# Local source snapshot IO (used by local adapters + orchestrator ingest)
# --------------------------------------------------------------------------
def write_source_snapshot(name: str, jobs: List[Dict[str, str]], meta: Optional[Dict[str, Any]] = None) -> Path:
    """Write output/sources/<name>.json. Sorted for stable git diffs."""
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    path = SOURCES_DIR / f"{name}.json"
    ordered = sorted(jobs, key=lambda j: (j.get("company", ""), j.get("title", ""), j.get("job_id", "")))
    payload = {
        "source": name,
        "count": len(ordered),
        "meta": meta or {},
        "jobs": ordered,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def read_source_snapshot(name: str) -> List[Dict[str, str]]:
    path = SOURCES_DIR / f"{name}.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    jobs = data.get("jobs") if isinstance(data, dict) else data
    return [j for j in jobs if isinstance(j, dict)] if isinstance(jobs, list) else []
