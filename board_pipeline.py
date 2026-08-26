#!/usr/bin/env python3
"""Multi-source job board pipeline (GitHub-Actions-owned writer).

Flow:
    Sources -> Normalize -> Dedup(first_seen) -> Official Verify ->
    Hard Filter -> Match Score (LLM if OPENAI_API_KEY else rules) ->
    Rank (Tier A/B/C) -> jobs.json + latest.md + alert

Sources:
  - ATS (Greenhouse/Lever/Ashby)         -> sources.ats
  - Official career pages (Amazon/Google) -> sources.official
  - Local snapshots (LinkedIn/Glassdoor)  -> output/sources/*.json (ingested)

This is the ONLY writer of output/board/ (jobs.json, inbox.md, latest.md, runs/).
The Syncareer pipeline writes only under output/syncareer/. Do not mix folders.
The local launchd job never writes those, avoiding git conflicts.

LLM policy (per plan):
  - Default ON. Runs only on rule-filter survivors to control cost.
  - Key read from os.getenv("OPENAI_API_KEY") (local .env or GHA secret).
  - No key / API error -> fallback to rule-based scoring; never fail the run.
  - --no-llm forces rule-based (local debug only).
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import time
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests

from sources import ats, official
from sources.schema import (
    OUTPUT_DIR,
    RECENCY_BUCKET_RANK,
    RECENCY_BUCKETS,
    classify_location_bucket,
    combined_cache_key,
    dedup_key,
    jd_hash,
    looks_official,
    normalize_company_key,
    normalize_location_key,
    normalize_space,
    normalize_title_key,
    read_source_snapshot,
    recency_bucket,
    NORMAL_RECENCY_BUCKETS,
)

BASE_DIR = Path(__file__).resolve().parent
BOARD_DIR = OUTPUT_DIR / "board"
JOBS_STORE_PATH = BOARD_DIR / "jobs.json"
LATEST_MD_PATH = BOARD_DIR / "latest.md"
INBOX_MD_PATH = BOARD_DIR / "inbox.md"
INBOX_CSV_PATH = BOARD_DIR / "inbox.csv"
RUNS_DIR = BOARD_DIR / "runs"
RETENTION_DAYS = 7
INBOX_DAYS = 3
TARGET_COMPANIES_JSON = BASE_DIR / "source" / "target_companies.json"

# Profile inputs drive matching. Fallback to legacy source/*.txt if missing.
PROFILE_DIR = BASE_DIR / "profile"
CANDIDATE_PROFILE_PATH = PROFILE_DIR / "candidate_profile.md"
RESUME_SWE_PATH = PROFILE_DIR / "resume_swe.md"
RESUME_AI_PATH = PROFILE_DIR / "resume_ai.md"
COMPANY_FILTERS_PATH = PROFILE_DIR / "company_filters.json"
LEGACY_SWE_RESUME_PATH = BASE_DIR / "source" / "swe-resume.txt"
LEGACY_AI_RESUME_PATH = BASE_DIR / "source" / "aie-resume.txt"

# Bump whenever the LLM prompt schema/policy changes; invalidates cached scores.
PROMPT_VERSION = "v3-strict-seniority-gaps"

# score_source values. Only llm / cached_llm are reusable cache hits.
# rule_overflow MUST remain eligible for LLM on a later run.
SCORE_LLM = "llm"
SCORE_CACHED_LLM = "cached_llm"
SCORE_OVERFLOW = "rule_overflow"
SCORE_FALLBACK = "rule_fallback"
SCORE_RECENCY = "rule_recency"
SCORE_RULE = "rule"
LLM_SCORE_SOURCES = {SCORE_LLM, SCORE_CACHED_LLM}

# Upper bound (NOT a target) for Tier A+B rows shown in latest.md / alerts.
MAX_VISIBLE = 200

# Strict Tier A / Tier B / exceptional-A thresholds on the 0-100 match scale.
TIER_A_MIN = 85.0          # <=3d, strong-fit floor for immediate-apply Tier A
TIER_B_MIN = 55.0
EXCEPTIONAL_A_MIN = 90.0   # 3to7d may only reach Tier A when truly exceptional
MAX_A_GAPS = 1             # Tier A tolerates at most this many core gaps
# 3to7d jobs only hit the LLM when their rule fit is already exceptionally strong.
RULE_EXCEPTIONAL_FOR_LLM = 72.0
# Seniority-fit labels that count as realistic for an early-career candidate.
STRONG_SENIORITY_FITS = {"good", "strong", "realistic", "early_career"}

LOCAL_SOURCES = ["linkedin", "glassdoor"]

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


# --------------------------------------------------------------------------
# Env / IO helpers
# --------------------------------------------------------------------------
def load_env_file(path: Path) -> None:
    """Populate os.environ from a .env file (local only). Tolerates spaces."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if not text or text.startswith("#") or "=" not in text:
            continue
        key, value = text.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and value and key not in os.environ:
            os.environ[key] = value


def make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"})
    return session


def emit_github_output(values: Dict[str, str]) -> None:
    out_path = os.environ.get("GITHUB_OUTPUT")
    if not out_path:
        return
    try:
        with open(out_path, "a", encoding="utf-8") as f:
            for key, value in values.items():
                f.write(f"{key}={value}\n")
    except OSError:
        pass


# --------------------------------------------------------------------------
# Target-company (referral) matching
# --------------------------------------------------------------------------
def load_target_companies() -> List[Dict[str, Any]]:
    if not TARGET_COMPANIES_JSON.exists():
        return []
    data = json.loads(TARGET_COMPANIES_JSON.read_text(encoding="utf-8"))
    companies = data.get("companies", []) if isinstance(data, dict) else []
    out = []
    for entry in companies:
        name = entry.get("name", "")
        aliases = entry.get("aliases", []) or [name]
        norm = sorted({normalize_company_key(a) for a in aliases if a}, key=len, reverse=True)
        out.append({"name": name, "norm_aliases": [a for a in norm if len(a) >= 3]})
    return out


def match_target_company(company_name: str, targets: List[Dict[str, Any]]) -> Optional[str]:
    """Referral flag: same safe exact/token/alias rules as company_filters.

    Short aliases (sap, meta, apple) only match as a whole token or exact key.
    Never bidirectional substring — that flagged Sapios as SAP.
    """
    return _company_alias_hit(company_name, targets)


# --------------------------------------------------------------------------
# Company filtering (config-driven; no hardcoded names in Python)
# --------------------------------------------------------------------------
CATEGORY_DROP_REASON = {
    "exclude": "company_excluded",
    "covered_elsewhere": "company_covered_elsewhere",
}


def load_company_filters() -> Dict[str, List[Dict[str, Any]]]:
    """Load profile/company_filters.json into normalized alias lists."""
    out: Dict[str, List[Dict[str, Any]]] = {
        "exclude": [], "covered_elsewhere": [], "deprioritize": [],
        "staffing": [], "prefer": [], "clearance_risk": [],
    }
    if not COMPANY_FILTERS_PATH.exists():
        return out
    try:
        data = json.loads(COMPANY_FILTERS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return out
    for category in out:
        for entry in data.get(category, []) or []:
            if not isinstance(entry, dict):
                continue
            name = entry.get("name", "")
            aliases = entry.get("aliases", []) or [name]
            norm = sorted({normalize_company_key(a) for a in aliases if a}, key=len, reverse=True)
            out[category].append({"name": name, "norm_aliases": [a for a in norm if a]})
    return out


def _company_alias_hit(company_name: str, entries: List[Dict[str, Any]]) -> Optional[str]:
    """Match a company against normalized aliases.

    Whole-token match always counts; substring match only for aliases >= 6 chars
    (so short aliases like "meta"/"apple" don't false-match "metadata" etc.).
    """
    key = normalize_company_key(company_name)
    if not key:
        return None
    tokens = {t for t in re.split(r"[^a-z0-9]+", (company_name or "").lower()) if t}
    for entry in entries:
        for alias in entry["norm_aliases"]:
            if alias in tokens or key == alias:
                return entry["name"]
            if len(alias) >= 6 and alias in key:
                return entry["name"]
    return None


def classify_company(company_name: str, filters: Dict[str, List[Dict[str, Any]]]) -> Tuple[str, str]:
    """Return (action, matched_name). action in
    {exclude, covered_elsewhere, deprioritize, prefer, keep}. Priority order
    ensures a drop beats a soft flag."""
    for category in ("exclude", "covered_elsewhere", "deprioritize", "staffing", "prefer", "clearance_risk"):
        name = _company_alias_hit(company_name, filters.get(category, []))
        if name:
            return category, name
    return "keep", ""


# --------------------------------------------------------------------------
# Collect + normalize + dedup
# --------------------------------------------------------------------------
def collect_sources(session: requests.Session, skip_network: bool = False) -> Tuple[List[Dict[str, str]], Dict[str, Any]]:
    """Gather all sources. Each source failing skips only itself."""
    jobs: List[Dict[str, str]] = []
    meta: Dict[str, Any] = {"per_source": {}, "errors": []}

    if not skip_network:
        ats_res = ats.fetch_all_ats(session)
        jobs.extend(ats_res["jobs"])
        meta["per_source"].update(ats_res["per_board"])
        meta["errors"].extend(ats_res["errors"])

        off_res = official.fetch_all_official(session)
        jobs.extend(off_res["jobs"])
        meta["per_source"].update(off_res["per_source"])
        meta["errors"].extend(off_res["errors"])

    # Ingest local snapshots committed by the launchd job.
    for name in LOCAL_SOURCES:
        rows = read_source_snapshot(name)
        if rows:
            jobs.extend(rows)
            meta["per_source"][f"local:{name}"] = len(rows)

    return jobs, meta


def canonical_rank(job: Dict[str, str]) -> Tuple[int, int, int, int]:
    """Lower is more canonical. Encodes source positioning from the plan:

    official career page > greenhouse|lever|ashby > linkedin > glassdoor,
    preferring records that already carry an official_url. Ties broken by
    date confidence then description richness.
    """
    src = (job.get("source") or "").lower()
    if "official" in src:
        base = 0
    elif any(a in src for a in ("greenhouse", "lever", "ashby")):
        base = 1
    elif "linkedin" in src:
        base = 3
    elif "glassdoor" in src:
        base = 4
    else:
        base = 2
    has_official = 0 if job.get("official_url") else 1
    conf = {"high": 3, "medium": 2, "low": 1, "unknown": 0}.get(job.get("date_confidence", "unknown"), 0)
    return (has_official, base, -conf, -len(job.get("description") or ""))


def _merge_pair(canonical: Dict[str, str], other: Dict[str, str]) -> Dict[str, str]:
    """Fill blanks on the canonical record from a less-canonical duplicate."""
    merged = dict(canonical)
    if not merged.get("official_url") and other.get("official_url"):
        merged["official_url"] = other["official_url"]
    if not merged.get("description") and other.get("description"):
        merged["description"] = other["description"]
    if not merged.get("posted_date") and other.get("posted_date"):
        merged["posted_date"] = other["posted_date"]
        merged["date_confidence"] = other.get("date_confidence", merged.get("date_confidence"))
    if not merged.get("location") and other.get("location"):
        merged["location"] = other["location"]
    # Union of provenance (which sources surfaced this job).
    via = list(merged.get("discovered_via") or [])
    for name in (other.get("discovered_via") or [other.get("source", "")]):
        if name and name not in via:
            via.append(name)
    merged["discovered_via"] = via
    return merged


def merge_by_key(jobs: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Collapse duplicates by dedup_key, keeping the most canonical record.

    Never merges distinct requisitions/locations: dedup_key requires
    official_url, or source+job_id, or company+title+LOCATION.
    """
    best: Dict[str, Dict[str, str]] = {}
    for job in jobs:
        rec = dict(job)
        rec.setdefault("discovered_via", [rec.get("source", "")] if rec.get("source") else [])
        key = dedup_key(rec)
        if key not in best:
            best[key] = rec
            continue
        prev = best[key]
        if canonical_rank(rec) < canonical_rank(prev):
            best[key] = _merge_pair(rec, prev)
        else:
            best[key] = _merge_pair(prev, rec)
    return list(best.values())


# Backwards-compatible alias.
dedup_merge = merge_by_key


def collapse_cross_source(jobs: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Second dedup pass after official_url is filled by verify_official().

    Newly-discovered official URLs can reveal cross-source duplicates that the
    first pass (keyed on company+title+location) could not see.
    """
    return merge_by_key(jobs)


# --------------------------------------------------------------------------
# Official verification
# --------------------------------------------------------------------------
def verify_official(jobs: List[Dict[str, str]]) -> None:
    """Fill official_url in place (best-effort). Mutates job dicts.

    Never match on company+title alone — that would attach one city's
    requisition URL to a same-title opening in a different city.
    """
    by_id: Dict[Tuple[str, str], str] = {}
    by_ctl: Dict[Tuple[str, str, str], str] = {}
    for job in jobs:
        url = job.get("official_url") or ""
        if not url:
            continue
        ckey = normalize_company_key(job.get("company", ""))
        tkey = normalize_title_key(job.get("title", ""))
        lkey = normalize_location_key(job.get("location", ""))
        jid = (job.get("job_id") or "").strip()
        if ckey and jid:
            by_id.setdefault((ckey, jid), url)
        if ckey and tkey and lkey:
            by_ctl.setdefault((ckey, tkey, lkey), url)

    for job in jobs:
        if job.get("official_url"):
            continue
        # 1) The source URL is already an official/ATS domain.
        if looks_official(job.get("source_url", "")):
            job["official_url"] = job["source_url"]
            continue
        ckey = normalize_company_key(job.get("company", ""))
        tkey = normalize_title_key(job.get("title", ""))
        lkey = normalize_location_key(job.get("location", ""))
        jid = (job.get("job_id") or "").strip()
        # 2) Same company + job_id (cross-source same requisition).
        if ckey and jid:
            hit = by_id.get((ckey, jid))
            if hit:
                job["official_url"] = hit
                continue
        # 3) Same company + title + location (never title-only).
        if ckey and tkey and lkey:
            hit = by_ctl.get((ckey, tkey, lkey))
            if hit:
                job["official_url"] = hit


# --------------------------------------------------------------------------
# Hard filter
# --------------------------------------------------------------------------
SENIOR_TITLE_RE = re.compile(
    r"\b(senior|sr\.?|lead|staff|principal|director|manager|head of|vp|vice president|distinguished|fellow)\b",
    re.IGNORECASE,
)
HARDWARE_TITLE_RE = re.compile(
    r"\b(asic|rtl|fpga|verilog|vhdl|analog|rf|pcb|soc design|silicon|hardware|embedded|firmware|mechanical|electrical engineer)\b",
    re.IGNORECASE,
)
CITIZEN_PHRASES = [
    "us citizen", "u.s. citizen", "united states citizen", "us citizenship",
    "u.s. citizenship", "must be a citizen", "us person", "u.s. person",
    "security clearance", "active clearance", "ts/sci", "ts sci", "polygraph",
    "top secret", "secret clearance", "clearance required", "active secret",
    "must be able to obtain", "ability to obtain a clearance",
    "eligible for a security clearance", "eligible to obtain",
    "requires a clearance", "requires security clearance",
    "us persons only", "u.s. persons only", "citizens only",
    "itar", "export control", "export-controlled",
]
CITIZEN_RES = [
    re.compile(r"\b" + re.escape(p).replace(r"\ ", r"\s+") + r"\b", re.IGNORECASE)
    for p in CITIZEN_PHRASES
]
# Extra patterns that are not clean phrases (slashes, optional words).
CLEARANCE_EXTRA_RES = [
    re.compile(r"\bts\s*/\s*sci\b", re.IGNORECASE),
    re.compile(r"\b(secret|top[- ]secret)\s+(clearance|eligible)\b", re.IGNORECASE),
    re.compile(r"\b(obtain|obtainable|eligible for)\b.{0,40}\bclearance\b", re.IGNORECASE),
    re.compile(r"\bclearance\b.{0,40}\b(required|needed|must)\b", re.IGNORECASE),
]
# Title-only gov/defense signal when the JD is too thin to verify constraints.
GOV_DEFENSE_TITLE_RE = re.compile(
    r"\b(us government|u\.s\. government|u\.s\. gov|us gov|"
    r"department of defense|\bdod\b|defense contractor|"
    r"intelligence community|\bts/?sci\b|clearance|"
    r"federal government|national security)\b",
    re.IGNORECASE,
)
THIN_JD_CHARS = 200  # LinkedIn guest cards often have empty descriptions
YOE_RE = re.compile(r"\b(\d{1,2})\+?\s*(?:years|yrs)\b", re.IGNORECASE)


def _full_constraint_text(job: Dict[str, str]) -> str:
    """Full title + JD for citizenship/clearance checks (no truncation)."""
    return f"{job.get('title') or ''} {job.get('description') or ''}"


def hard_filter(job: Dict[str, str]) -> Tuple[bool, str]:
    if classify_location_bucket(job.get("location", "")) == "non_us":
        return False, "non_us_location"
    content = _full_constraint_text(job)
    for pattern in CITIZEN_RES:
        if pattern.search(content):
            return False, "citizen_or_clearance"
    for pattern in CLEARANCE_EXTRA_RES:
        if pattern.search(content):
            return False, "citizen_or_clearance"
    # LinkedIn guest cards have no JD. Do not promote gov/defense roles to
    # A/B when we cannot read citizenship/clearance requirements.
    desc = (job.get("description") or "").strip()
    src = (job.get("source") or "").lower()
    thin = len(desc) < THIN_JD_CHARS
    low_conf_source = "linkedin" in src or "glassdoor" in src
    if thin and low_conf_source:
        title = job.get("title") or ""
        if GOV_DEFENSE_TITLE_RE.search(title) or job.get("clearance_risk_company"):
            return False, "incomplete_jd_clearance_risk"
    return True, "keep"


# --------------------------------------------------------------------------
# Profiles (candidate policy + routed resumes) + role-family detection
# --------------------------------------------------------------------------
def _read_first(*paths: Path) -> str:
    for p in paths:
        if p.exists():
            try:
                return p.read_text(encoding="utf-8")
            except OSError:
                continue
    return ""


def load_profiles() -> Dict[str, Any]:
    """Load candidate profile + routed resumes and a fingerprint for caching."""
    candidate = _read_first(CANDIDATE_PROFILE_PATH)
    swe = _read_first(RESUME_SWE_PATH, LEGACY_SWE_RESUME_PATH)
    ai = _read_first(RESUME_AI_PATH, LEGACY_AI_RESUME_PATH)
    import hashlib

    def h(text: str) -> str:
        return hashlib.sha1((text or "").encode("utf-8")).hexdigest()

    fingerprint = h("::".join([h(swe), h(ai), h(candidate), PROMPT_VERSION]))
    return {
        "candidate": candidate,
        "resume_swe": swe,
        "resume_ai": ai,
        "fingerprint": fingerprint,
    }


AI_FAMILY_RE = re.compile(
    r"\b(ai|a\.i\.|artificial intelligence|ml|machine learning|deep learning|"
    r"llm|genai|generative ai|applied ai|applied scientist|nlp|computer vision|"
    r"cv engineer|rag|retrieval|search engineer|agent|agentic|mlops|ml ?ops|"
    r"model|inference)\b",
    re.IGNORECASE,
)
SWE_FAMILY_RE = re.compile(
    r"\b(software|swe|sde|backend|back[- ]?end|full[- ]?stack|front[- ]?end|"
    r"platform|infrastructure|infra|cloud|distributed systems|devops|"
    r"site reliability|sre|data platform|data engineer|systems engineer|"
    r"developer|programmer|forward[- ]?deployed|\bfde\b|implementation engineer|"
    r"solutions architect|solution architect|ai solutions architect)\b",
    re.IGNORECASE,
)
# Title must look like an engineering role. Stops JD keywords from rescuing
# Content Designer / BizOps / asset-management titles.
TITLE_TECH_RE = re.compile(
    r"\b(software|swe|sde|backend|full[- ]?stack|frontend|front[- ]?end|"
    r"platform|infrastructure|data engineer|data platform|machine learning|"
    r"ml engineer|ai engineer|artificial intelligence|applied ai|llm|genai|"
    r"developer|programmer|architect|forward[- ]?deployed|\bfde\b|scientist|"
    r"sre|site reliability|devops|research engineer|systems engineer|agentic)\b",
    re.IGNORECASE,
)
NEGATIVE_FAMILY_RE = re.compile(
    r"\b(product manager|program manager|project manager|sales|account executive|"
    r"business development|marketing|growth|finance|accountant|legal|counsel|"
    r"recruit(er|ing)|talent acquisition|human resources|\bhr\b|"
    r"ux designer|ui designer|graphic designer|product designer|content designer|"
    r"business operations|asset management|"
    r"mechanical engineer|electrical engineer|civil engineer|hardware engineer|"
    r"customer success|support engineer|technical writer|"
    r"nurse|teacher|driver|warehouse|barista|clinical)\b",
    re.IGNORECASE,
)
# Sales/presales/quota — used to drop SA/FDE only when clearly commercial.
SALES_HEAVY_RE = re.compile(
    r"\b(presales|pre-sales|pre sales|\bquota\b|commission|account executive|"
    r"go-to-market|\bgtm\b|revenue target)\b",
    re.IGNORECASE,
)
INTERNSHIP_TITLE_RE = re.compile(
    r"\b(intern|internship|co-op|coop)\b",
    re.IGNORECASE,
)
EARLY_CAREER_TITLE_RE = re.compile(
    r"\b(new grad|new-grad|early career|early-career|university grad|"
    r"university graduate|university hire|college grad|recent graduate|"
    r"entry[- ]?level|engineer i\b|swe i\b|sde i\b|"
    r"associate software|associate engineer)\b",
    re.IGNORECASE,
)


def detect_role_family(job: Dict[str, str]) -> str:
    """Return 'ai', 'swe', 'ambiguous', 'negative', or 'none'."""
    title = (job.get("title") or "")
    text = f"{title} {(job.get('description') or '')[:1200]}"
    # Title dominates for negatives so a passing JD keyword doesn't rescue a PM role.
    if NEGATIVE_FAMILY_RE.search(title) and not SWE_FAMILY_RE.search(title) and not AI_FAMILY_RE.search(title):
        return "negative"
    is_ai = bool(AI_FAMILY_RE.search(text))
    is_swe = bool(SWE_FAMILY_RE.search(text))
    if is_ai and is_swe:
        return "ambiguous"
    if is_ai:
        return "ai"
    if is_swe:
        return "swe"
    if NEGATIVE_FAMILY_RE.search(text):
        return "negative"
    return "none"


def role_relevance_score(family: str) -> int:
    return {"ai": 2, "swe": 2, "ambiguous": 1}.get(family, 0)


def is_sales_heavy(job: Dict[str, str]) -> bool:
    """True when the TITLE is clearly commercial (presales/quota), not merely customer-facing."""
    title = job.get("title") or ""
    return bool(SALES_HEAVY_RE.search(title))


def role_seniority_prefilter(job: Dict[str, str]) -> Tuple[bool, str]:
    """Tighten the LLM candidate pool after the hard filter.

    Drops negative families, senior/staff/principal/lead titles, explicit high
    YOE, hardware-first, sales/presales-heavy titles, and titles that are not
    recognizably technical. Keeps hands-on SA / FDE / implementation roles.
    """
    title = (job.get("title") or "")
    text = f"{title} {(job.get('description') or '')[:1500]}"
    family = job.get("role_family") or detect_role_family(job)
    job["role_family"] = family
    job["role_relevance"] = role_relevance_score(family)

    if family == "negative":
        return False, "prefilter:negative_family"
    if is_sales_heavy(job):
        return False, "prefilter:sales_heavy"
    # Hardware-first title that isn't clearly software/ML.
    if HARDWARE_TITLE_RE.search(title) and not any(
        w in title.lower() for w in ("software", "platform", "systems", "ml", "ai", "backend")
    ):
        return False, "prefilter:hardware"
    if SENIOR_TITLE_RE.search(title):
        return False, "prefilter:senior"
    m = YOE_RE.search(text)
    if m and int(m.group(1)) >= 5:
        return False, "prefilter:high_yoe"
    # Title must look like an engineering role. JD keywords cannot rescue
    # Content Designer / BizOps / asset-management titles.
    if not TITLE_TECH_RE.search(title):
        return False, "prefilter:no_positive_family"
    if family == "none":
        return False, "prefilter:no_positive_family"
    return True, "keep"


def seniority_fit_ok(job: Dict[str, str]) -> bool:
    """Rule-derived seniority realism used when the LLM doesn't provide it."""
    fit = (job.get("seniority_fit") or "").lower()
    if fit in ("mismatch", "senior", "over"):
        return False
    if fit in ("good", "strong", "realistic", "early_career", "stretch"):
        return fit != "mismatch"
    title = (job.get("title") or "")
    if SENIOR_TITLE_RE.search(title):
        return False
    m = YOE_RE.search(f"{title} {(job.get('description') or '')[:1200]}")
    if m and int(m.group(1)) >= 5:
        return False
    return True


# --------------------------------------------------------------------------
# Rule scoring (fallback + pre-rank before LLM)
# --------------------------------------------------------------------------
STRONG_HITS = [
    "software engineer", "software development engineer", "sde", "backend",
    "full stack", "full-stack", "platform engineer", "infrastructure engineer",
    "cloud engineer", "machine learning engineer", "ml engineer", "ai engineer",
    "applied ai", "applied scientist", "llm", "new grad", "early career",
]
MEDIUM_HITS = [
    "systems engineer", "solutions engineer", "solutions architect",
    "solution architect", "forward deployed", "data engineer",
    "research engineer", "developer", "programmer",
]


def rule_match_score(job: Dict[str, str]) -> float:
    """Resume/JD keyword fit only (0-100). No referral / recency / official boosts."""
    title = normalize_space(job.get("title", "")).lower()
    text = f"{title} {normalize_space(job.get('description',''))[:1500].lower()}"
    score = 40.0
    if any(w in text for w in STRONG_HITS):
        score += 25.0
    if any(w in text for w in MEDIUM_HITS):
        score += 10.0
    if SENIOR_TITLE_RE.search(title):
        score -= 25.0
    m = YOE_RE.search(text)
    if m and int(m.group(1)) >= 5:
        score -= 15.0
    if HARDWARE_TITLE_RE.search(title) and not any(w in title for w in ["software", "platform", "systems", "ml", "ai"]):
        score -= 20.0
    if is_sales_heavy(job):
        score -= 20.0
    if job.get("deprioritized"):
        score -= 10.0
    return max(1.0, min(100.0, score))


def llm_dispatch_priority(job: Dict[str, str]) -> float:
    """Who gets the LLM first this run. Ranking only — not stored as match_score."""
    s = float(job.get("rule_score", 0) or 0)
    if job.get("official_url"):
        s += 5.0
    if job.get("referral_name"):
        s += 4.0
    if job.get("preferred"):
        s += 6.0
    s -= RECENCY_BUCKET_RANK.get(job.get("recency_bucket", "gt7d"), 5) * 2
    return s


# --------------------------------------------------------------------------
# LLM matching (OpenAI), survivors only
# --------------------------------------------------------------------------
def parse_json_object(text: str) -> Optional[Dict[str, Any]]:
    text = (text or "").strip()
    try:
        data = json.loads(text)
        return data if isinstance(data, dict) else None
    except json.JSONDecodeError:
        pass
    m = re.search(r"\{.*\}", text, flags=re.S)
    if not m:
        return None
    try:
        data = json.loads(m.group(0))
        return data if isinstance(data, dict) else None
    except json.JSONDecodeError:
        return None


LLM_MAX_CANDIDATES = 400  # safety cap on new/changed jobs sent to the LLM per run


def llm_match_batch(
    batch: List[Dict[str, str]],
    profiles: Dict[str, Any],
    api_key: str,
    model: str,
) -> Dict[str, Dict[str, Any]]:
    """Evidence-based match against JD + routed resume. Keyed by canonical key."""
    jobs_payload = [
        {
            "key": dedup_key(j),
            "title": j["title"],
            "company": j["company"],
            "location": j["location"],
            "posted_date": j.get("posted_date", ""),
            "detected_family": j.get("role_family", "none"),
            "text": (j.get("description") or j["title"])[:1600],
        }
        for j in batch
    ]
    prompt = {
        "task": (
            "Score how well each job fits the candidate using evidence from the "
            "job description AND the resume(s). Do not score on keyword overlap alone."
        ),
        "candidate_profile": profiles.get("candidate", "")[:4000],
        "resume_swe": profiles.get("resume_swe", "")[:3500],
        "resume_ai": profiles.get("resume_ai", "")[:3500],
        "instructions": [
            "match_score is 0-100 (higher = stronger evidence-based fit).",
            "Be strict: reserve 85-100 for genuinely strong, immediate-apply fits.",
            "Seniority mismatch is heavily penalizing: a Senior/Staff/Principal/Lead "
            "role, or one requiring 5+ years, for an early-career candidate should "
            "score well below 60 and seniority_fit=mismatch.",
            "If the job's core required qualifications are NOT clearly evidenced in "
            "the resume, cap match_score below 80 and list them in main_gaps.",
            "Directional relevance alone (right domain, wrong depth/seniority) is NOT "
            "a high score.",
            "role_family in {swe, ai, ambiguous}.",
            "resume_profile_used in {resume_swe, resume_ai}; pick the stronger match.",
            "seniority_fit in {good, stretch, mismatch} for an early-career candidate.",
            "hard_constraint_status in {ok, citizen_or_clearance, non_us, other}.",
            "recommended_action in {referral_now, apply_now, apply_if_time, skip}.",
            "top_match_reasons: 2-4 short strings. main_gaps: 0-3 short strings "
            "naming missing core requirements.",
            "Penalize hardware-first roles.",
            "Keep hands-on Solutions Architect, AI Solutions Architect, Forward Deployed, "
            "and implementation-engineering roles when the work is technical. "
            "Score sales/presales/quota-oriented architect roles well below 60.",
        ],
        "return_schema": {
            "results": [
                {
                    "key": "string",
                    "role_family": "swe|ai|ambiguous",
                    "resume_profile_used": "resume_swe|resume_ai",
                    "match_score": "0-100 int",
                    "seniority_fit": "good|stretch|mismatch",
                    "hard_constraint_status": "ok|citizen_or_clearance|non_us|other",
                    "top_match_reasons": ["string"],
                    "main_gaps": ["string"],
                    "recommended_action": "referral_now|apply_now|apply_if_time|skip",
                }
            ]
        },
        "jobs": jobs_payload,
    }
    resp = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": model,
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": "You are a precise early-career tech recruiting screener. Return JSON only."},
                {"role": "user", "content": json.dumps(prompt)},
            ],
        },
        timeout=90,
    )
    resp.raise_for_status()
    parsed = parse_json_object(resp.json()["choices"][0]["message"]["content"])
    if not parsed:
        return {}
    out: Dict[str, Dict[str, Any]] = {}
    for item in parsed.get("results", []):
        key = str(item.get("key", "")).strip()
        if not key:
            continue
        try:
            score = float(item.get("match_score", 0) or 0)
        except (TypeError, ValueError):
            score = 0.0

        def _as_list(v: Any) -> List[str]:
            if isinstance(v, list):
                return [str(x) for x in v][:4]
            if v:
                return [str(v)]
            return []

        out[key] = {
            "match_score": max(0.0, min(100.0, score)),
            "role_family": str(item.get("role_family", "")) or "",
            "resume_profile_used": str(item.get("resume_profile_used", "resume_swe")),
            "seniority_fit": str(item.get("seniority_fit", "")) or "",
            "hard_constraint_status": str(item.get("hard_constraint_status", "ok")),
            "top_match_reasons": _as_list(item.get("top_match_reasons")),
            "main_gaps": _as_list(item.get("main_gaps")),
            "recommended_action": str(item.get("recommended_action", "apply_if_time")),
        }
    return out


def _apply_rule_result(job: Dict[str, str], score_source: str, note: str) -> None:
    job["match_score"] = float(job.get("rule_score", 0.0))
    fam = job.get("role_family") or detect_role_family(job)
    job["role_family"] = fam
    job["resume_profile_used"] = "resume_ai" if fam == "ai" else "resume_swe"
    job["seniority_fit"] = "good" if seniority_fit_ok(job) else "stretch"
    job["hard_constraint_status"] = "ok"
    job["top_match_reasons"] = [note]
    job["main_gaps"] = []
    job["recommended_action"] = "apply_if_time"
    job["score_source"] = score_source
    job["screen_method"] = score_source


def _apply_cached_result(job: Dict[str, str], entry: Dict[str, Any]) -> None:
    job["match_score"] = float(entry.get("match_score", 0.0) or 0.0)
    job["role_family"] = entry.get("role_family") or job.get("role_family", "")
    job["resume_profile_used"] = entry.get("resume_profile_used", "resume_swe")
    job["seniority_fit"] = entry.get("seniority_fit", "")
    job["hard_constraint_status"] = entry.get("hard_constraint_status", "ok")
    job["top_match_reasons"] = list(entry.get("top_match_reasons") or [])
    job["main_gaps"] = list(entry.get("main_gaps") or [])
    job["recommended_action"] = entry.get("recommended_action", "apply_if_time")
    job["score_source"] = SCORE_CACHED_LLM
    job["screen_method"] = SCORE_CACHED_LLM


def _is_reusable_llm_cache(prev: Dict[str, Any], job: Dict[str, str]) -> bool:
    """Only a completed LLM (or cached-LLM) score may be reused.

    rule_overflow / rule_fallback / rule_recency stay eligible for a later LLM call.
    """
    if not prev:
        return False
    if prev.get("cache_key") != job.get("cache_key"):
        return False
    if prev.get("match_score") is None:
        return False
    src = (prev.get("score_source") or "").strip()
    if src in LLM_SCORE_SOURCES:
        return True
    # Legacy store: real LLM results used screen_method=llm and no score_source.
    if not src and prev.get("screen_method") == "llm":
        return True
    return False


def score_survivors(
    candidates: List[Dict[str, str]],
    referrals: Dict[str, bool],
    profiles: Dict[str, Any],
    store: Dict[str, Dict[str, Any]],
    use_llm: bool,
) -> Tuple[str, List[str], Dict[str, int]]:
    """Attach match_score + LLM fields to each candidate in place.

    Incremental: reuse cached LLM scores only. Rule-overflow jobs are NOT
    treated as a completed cache hit. Returns (method, errors, counts).
    """
    errors: List[str] = []
    counts = {
        "reused": 0, "llm": 0, "new_or_changed": 0, "rule": 0, "sent": 0,
        "api_requests": 0, "recency_skipped": 0, "overflow": 0,
    }
    fp = profiles["fingerprint"]

    for job in candidates:
        job["rule_score"] = rule_match_score(job)
        job["cache_key"] = combined_cache_key(job, fp)
        job["jd_hash"] = jd_hash(job)

    to_llm: List[Dict[str, str]] = []
    for job in candidates:
        key = dedup_key(job)
        prev = store.get(key)
        if _is_reusable_llm_cache(prev or {}, job):
            _apply_cached_result(job, prev)
            counts["reused"] += 1
        else:
            to_llm.append(job)
    counts["new_or_changed"] = len(to_llm)

    if not to_llm:
        return ("cache", errors, counts)

    def llm_recency_eligible(job: Dict[str, str]) -> bool:
        title = job.get("title") or ""
        # Explicit early-career titles may enter the LLM gate at any age,
        # including >7d, so we don't miss New Grad / Engineer I postings.
        if EARLY_CAREER_TITLE_RE.search(title):
            return True
        bucket = job.get("recency_bucket") or recency_bucket(job)
        if bucket == "gt7d":
            return False
        if bucket == "3to7d":
            return float(job.get("rule_score", 0)) >= RULE_EXCEPTIONAL_FOR_LLM
        return bucket in NORMAL_RECENCY_BUCKETS

    eligible: List[Dict[str, str]] = []
    for job in to_llm:
        if llm_recency_eligible(job):
            eligible.append(job)
        else:
            _apply_rule_result(job, SCORE_RECENCY, "Rule-based (recency-gated from LLM)")
            counts["rule"] += 1
            counts["recency_skipped"] += 1

    api_key = (os.getenv("OPENAI_API_KEY") or "").strip()
    if not use_llm or not api_key:
        note = "Rule-based (LLM disabled)" if not use_llm else "Rule-based (no OPENAI_API_KEY)"
        for job in eligible:
            _apply_rule_result(job, SCORE_RULE, note)
            counts["rule"] += 1
        method = "cache+rule" if counts["reused"] else "rule"
        if use_llm and not api_key:
            errors.append("no_openai_key")
        return (method, errors, counts)

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    eligible_sorted = sorted(eligible, key=llm_dispatch_priority, reverse=True)
    llm_pool = eligible_sorted[:LLM_MAX_CANDIDATES]
    overflow = eligible_sorted[LLM_MAX_CANDIDATES:]
    counts["sent"] = len(llm_pool)
    counts["overflow"] = len(overflow)

    decisions: Dict[str, Dict[str, Any]] = {}
    llm_ok = False
    chunk = 15
    for i in range(0, len(llm_pool), chunk):
        batch = llm_pool[i : i + chunk]
        counts["api_requests"] += 1
        try:
            result = llm_match_batch(batch, profiles, api_key, model)
            if result:
                decisions.update(result)
                llm_ok = True
            time.sleep(0.2)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"chunk_{i // chunk}: {type(exc).__name__}: {str(exc)[:120]}")

    if not llm_ok:
        for job in eligible:
            _apply_rule_result(job, SCORE_FALLBACK, "Rule-based fallback (LLM error)")
            counts["rule"] += 1
        method = "cache+rule_fallback" if counts["reused"] else "rule_fallback"
        return (method, errors, counts)

    for job in llm_pool:
        d = decisions.get(dedup_key(job))
        if d:
            job["match_score"] = d["match_score"]
            job["role_family"] = d["role_family"] or job.get("role_family", "")
            job["resume_profile_used"] = d["resume_profile_used"]
            job["seniority_fit"] = d["seniority_fit"]
            job["hard_constraint_status"] = d["hard_constraint_status"]
            job["top_match_reasons"] = d["top_match_reasons"]
            job["main_gaps"] = d["main_gaps"]
            job["recommended_action"] = d["recommended_action"]
            job["score_source"] = SCORE_LLM
            job["screen_method"] = SCORE_LLM
            counts["llm"] += 1
        else:
            _apply_rule_result(job, SCORE_FALLBACK, "Rule-based (missing from LLM response)")
            counts["rule"] += 1
    for job in overflow:
        # Deliberately NOT a cacheable LLM score — next run will retry.
        _apply_rule_result(job, SCORE_OVERFLOW, "Rule-based (over LLM cap; retry next run)")
        counts["rule"] += 1

    method = "cache+llm" if counts["reused"] else "llm"
    return (method, errors, counts)


# --------------------------------------------------------------------------
# Tiering
# --------------------------------------------------------------------------
def _strong_seniority(job: Dict[str, str]) -> bool:
    """Stricter than seniority_fit_ok: 'stretch' does NOT qualify for Tier A."""
    fit = (job.get("seniority_fit") or "").lower()
    if fit:
        return fit in STRONG_SENIORITY_FITS
    # No explicit label (rule path fallback): derive conservatively.
    return seniority_fit_ok(job)


def assign_tier(job: Dict[str, str], is_referral: bool) -> str:
    """Recency-gated, quality-gated tiering on the 0-100 match scale.

    LLM / cached-LLM strong matches may enter Tier A normally.
    Rule-only scores (overflow / fallback / recency / rule) generally max at
    Tier B, except explicit New Grad / Early Career / Engineer I with a
    clearly strong family match.
    """
    del is_referral  # ranking/action only; never a match_score or A-gate.
    score = float(job.get("match_score", 0) or 0)
    bucket = job.get("recency_bucket") or recency_bucket(job)
    strong_sen = _strong_seniority(job)
    few_gaps = len(job.get("main_gaps") or []) <= MAX_A_GAPS
    deprioritized = bool(job.get("deprioritized"))
    src = (job.get("score_source") or "").strip()
    llm_scored = src in LLM_SCORE_SOURCES
    rule_only = src in {SCORE_OVERFLOW, SCORE_FALLBACK, SCORE_RECENCY, SCORE_RULE, ""}
    early = bool(EARLY_CAREER_TITLE_RE.search(job.get("title") or ""))
    family = (job.get("role_family") or "").lower()
    strong_family = family in ("swe", "ai", "ambiguous")

    intern = bool(INTERNSHIP_TITLE_RE.search(job.get("title") or ""))
    staffing = bool(job.get("staffing_firm"))
    a_quality = strong_sen and few_gaps and not deprioritized and not intern and not staffing

    # Non-early-career: >7d store-only; 3-7d only exceptional LLM Tier A.
    # Early-career: recency does not auto-assign A, but A/B are allowed at any
    # age if match_score says so (LLM still decides).
    if bucket == "gt7d" and not early:
        return "C"
    if bucket == "3to7d" and not early:
        if score >= EXCEPTIONAL_A_MIN and a_quality and llm_scored:
            return "A"
        return "C"
    # <=3d normal window
    if score >= TIER_A_MIN and a_quality:
        if llm_scored:
            return "A"
        if rule_only and early and strong_family:
            return "A"
        # rule-only otherwise caps at B
    if score >= TIER_B_MIN:
        return "B"
    return "C"


def apply_referral_action(job: Dict[str, str]) -> None:
    """Referral is a ranking/action flag, not a match_score bonus."""
    if not job.get("referral_name"):
        return
    score = float(job.get("match_score", 0) or 0)
    action = job.get("recommended_action") or "apply_if_time"
    if job.get("tier") == "A" or score >= TIER_A_MIN:
        job["recommended_action"] = "referral_now"
    elif action == "apply_if_time":
        job["recommended_action"] = "apply_now"


def user_facing_sort_key(job: Dict[str, str]) -> Tuple:
    """Recency dominates, then quality, then referral, then verification.

    (bucket_rank, tier_rank, -match_score, 0 if referral else 1,
     seniority_fit_rank, 0 if official_verified else 1, -role_relevance)
    """
    bucket = job.get("recency_bucket") or recency_bucket(job)
    tier_rank = {"A": 0, "B": 1, "C": 2}.get(job.get("tier", "C"), 2)
    sfit = (job.get("seniority_fit") or "").lower()
    sfit_rank = {"good": 0, "strong": 0, "realistic": 0, "stretch": 1}.get(sfit, 2 if sfit == "mismatch" else 1)
    verified = 0 if job.get("official_url") else 1
    referral = 0 if job.get("referral_name") else 1
    conf = {"high": 0, "medium": 1, "low": 2, "unknown": 3}.get(
        (job.get("date_confidence") or "unknown").lower(), 3
    )
    return (
        RECENCY_BUCKET_RANK.get(bucket, len(RECENCY_BUCKETS)),
        conf,
        tier_rank,
        -float(job.get("match_score", 0) or 0),
        referral,
        sfit_rank,
        verified,
        -int(job.get("role_relevance", 0) or 0),
    )


# --------------------------------------------------------------------------
# jobs.json store (dedup + first_seen, 7-day rolling)
# --------------------------------------------------------------------------
def load_store() -> Dict[str, Dict[str, Any]]:
    if not JOBS_STORE_PATH.exists():
        return {}
    try:
        data = json.loads(JOBS_STORE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    entries = data.get("entries", []) if isinstance(data, dict) else data
    out: Dict[str, Dict[str, Any]] = {}
    if isinstance(entries, list):
        for e in entries:
            key = e.get("key")
            if key:
                out[key] = e
    return out


def save_store(store: Dict[str, Dict[str, Any]]) -> None:
    BOARD_DIR.mkdir(parents=True, exist_ok=True)
    entries = sorted(store.values(), key=lambda e: (e.get("first_seen", ""), e.get("key", "")), reverse=True)
    payload = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "retention_days": RETENTION_DAYS,
        "count": len(entries),
        "entries": entries,
    }
    JOBS_STORE_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def prune_store(store: Dict[str, Dict[str, Any]], now: datetime) -> Dict[str, Dict[str, Any]]:
    kept: Dict[str, Dict[str, Any]] = {}
    for key, e in store.items():
        fs = e.get("first_seen", "")
        try:
            seen = datetime.fromisoformat(fs.replace("Z", "+00:00")) if fs else now
        except ValueError:
            seen = now
        if (now - seen).days <= RETENTION_DAYS:
            kept[key] = e
    return kept


# --------------------------------------------------------------------------
# Outputs
# --------------------------------------------------------------------------
def _stats_lines(stats: Dict[str, Any]) -> List[str]:
    src = stats["source_raw"]
    fn = stats["funnel"]
    out = stats["output"]
    rec = stats["recency"]
    llm = stats["llm"]
    lines = [
        "## Run stats",
        "",
        f"- Source raw: ATS {src['ats']} / Official {src['official']} / "
        f"LinkedIn {src['linkedin']} / Glassdoor {src['glassdoor']} / Syncareer {src['syncareer']}",
        f"- Funnel: after dedup {fn['after_dedup']} -> after company filter {fn['after_company']} "
        f"-> after hard filter {fn['after_hard_filter']} "
        f"-> after role+seniority prefilter {fn['after_prefilter']} | dropped {fn['dropped']}",
        f"- LLM usage: jobs scored {llm['scored']} / API requests {llm['api_requests']} / "
        f"cache reused {llm['reused']} / rule fallback+overflow {llm['rule']} "
        f"(recency-gated {llm['recency_skipped']}, overflow {llm.get('overflow', 0)}, "
        f"new/changed {llm['new_or_changed']})",
        f"- Output sizing: Tier A {out['tier_a']} / Tier B {out['tier_b']} / "
        f"A+B before cap {out['ab_before_cap']} / Shown in latest.md {out['shown']} (cap {MAX_VISIBLE})",
        f"- Recency (kept): <3h {rec['lt3h']} / 3-24h {rec['3to24h']} / "
        f"newly-disc {rec['newly_discovered']} / 1-3d {rec['1to3d']} / "
        f"3-7d {rec['3to7d']} / >7d {rec['gt7d']}",
    ]
    return lines


def write_latest_md(visible: List[Dict[str, str]], stats: Dict[str, Any], stamp: str) -> None:
    """7-day Tier A/B view (capped). Prefer inbox.md if you skipped a day."""
    BOARD_DIR.mkdir(parents=True, exist_ok=True)
    lines: List[str] = [
        f"# ATS / LinkedIn board — 7-day view — {stamp}",
        "",
        f"If you check every 1–2 days, open **`output/board/inbox.md`** (last {INBOX_DAYS} days) instead of this file.",
        "",
    ]
    lines.extend(_stats_lines(stats))
    lines.append("")

    by_tier = {"A": [j for j in visible if j.get("tier") == "A"],
               "B": [j for j in visible if j.get("tier") == "B"]}
    titles = {"A": "Tier A - apply now / referral", "B": "Tier B - worth applying"}
    for tier in ["A", "B"]:
        rows = by_tier[tier]
        lines.append(f"## {titles[tier]} ({len(rows)})")
        lines.append("")
        if not rows:
            lines.append("_none_")
            lines.append("")
            continue
        lines.append("| Score | Src | Company | Title | Location | Posted | Recency | Conf | Resume | Referral | Verified | Link |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in rows:
            link_url = r.get("official_url") or r.get("source_url") or ""
            link = f"[open]({link_url})" if link_url else "-"
            referral = r.get("referral_name") or "-"
            verified = "yes" if r.get("official_url") else "-"
            title = (r.get("title") or "").replace("|", "/")[:70]
            company = (r.get("company") or "").replace("|", "/")
            loc = (r.get("location") or "").replace("|", "/")
            resume = (r.get("resume_profile_used") or "").replace("resume_", "")
            src = r.get("score_source") or "-"
            lines.append(
                f"| {float(r.get('match_score') or 0):.0f} | {src} | {company} | {title} | {loc} | "
                f"{r.get('posted_date','') or '-'} | {r.get('recency_bucket','')} | "
                f"{r.get('date_confidence','')} | {resume} | {referral} | {verified} | {link} |"
            )
        lines.append("")
    LATEST_MD_PATH.write_text("\n".join(lines), encoding="utf-8")


def _job_inbox_ref(job: Dict[str, Any]) -> Optional[datetime]:
    for field in ("posted_date", "first_seen"):
        raw = (job.get(field) or "").strip()
        if not raw:
            continue
        try:
            parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            try:
                parsed = datetime.strptime(raw[:10], "%Y-%m-%d")
            except ValueError:
                continue
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed
    return None


def write_board_inbox(visible: List[Dict[str, str]], stamp: str, now: datetime) -> List[Dict[str, str]]:
    """Last INBOX_DAYS of Tier A/B — the file to open if you skipped a day."""
    cutoff = now - timedelta(days=INBOX_DAYS)
    inbox = []
    for job in visible:
        ref = _job_inbox_ref(job)
        if ref is None or ref >= cutoff:
            inbox.append(job)
    BOARD_DIR.mkdir(parents=True, exist_ok=True)
    with INBOX_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ALERT_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for r in inbox:
            writer.writerow({k: r.get(k, "") for k in ALERT_FIELDS})

    lines = [
        f"# ATS / LinkedIn inbox (last {INBOX_DAYS} days)",
        "",
        f"- Updated: {stamp}",
        f"- Jobs: {len(inbox)} (Tier A/B only)",
        "",
        "If you check every 1–2 days, **only open this file**. This-run snapshots are in `runs/`.",
        "The 7-day dump is `latest.md`.",
        "",
        "| Tier | Score | Company | Title | Location | Posted | Recency | Referral | Link |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in inbox:
        link_url = r.get("official_url") or r.get("source_url") or ""
        link = f"[open]({link_url})" if link_url else "-"
        referral = r.get("referral_name") or "-"
        title = (r.get("title") or "").replace("|", "/")[:70]
        lines.append(
            f"| {r.get('tier')} | {float(r.get('match_score') or 0):.0f} | "
            f"{(r.get('company') or '').replace('|','/')} | {title} | "
            f"{(r.get('location') or '').replace('|','/')} | {r.get('posted_date','') or '-'} | "
            f"{r.get('recency_bucket','')} | {referral} | {link} |"
        )
    INBOX_MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return inbox


ALERT_FIELDS = ["tier", "match_score", "score_source", "company", "title", "location",
                "posted_date", "recency_bucket", "date_confidence", "resume_profile_used",
                "referral_name", "recommended_action", "official_url", "source", "source_url"]


def write_alert(new_ab: List[Dict[str, str]], stamp: str) -> Dict[str, Path]:
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    BOARD_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = RUNS_DIR / f"{stamp}.csv"
    body_path = BOARD_DIR / "issue_body.md"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ALERT_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for r in new_ab:
            writer.writerow({k: r.get(k, "") for k in ALERT_FIELDS})

    # Mention the repo owner for a "mentioned you" ping. Prefer Participating-only
    # watching if Issue-opened emails already work, otherwise Watch + @ will duplicate.
    lines = [
        f"ATS / LinkedIn alert - {stamp}",
        "",
        "cc @daniel-li2021",
        "",
        f"{len(new_ab)} new Tier A/B job(s) this run.",
        "",
        f"If you skipped a day, open `output/board/inbox.md` (last {INBOX_DAYS} days). Do not read every Issue.",
        "",
    ]
    lines.append("| Tier | Score | Company | Title | Location | Posted | Recency | Referral | Link |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for r in new_ab:
        link_url = r.get("official_url") or r.get("source_url") or ""
        link = f"[open]({link_url})" if link_url else "-"
        referral = r.get("referral_name") or "-"
        title = (r.get("title") or "").replace("|", "/")[:70]
        lines.append(
            f"| {r.get('tier')} | {float(r.get('match_score') or 0):.0f} | "
            f"{(r.get('company') or '').replace('|','/')} | {title} | "
            f"{(r.get('location') or '').replace('|','/')} | {r.get('posted_date','') or '-'} | "
            f"{r.get('recency_bucket','')} | {referral} | {link} |"
        )
    body_path.write_text("\n".join(lines), encoding="utf-8")
    return {"csv": csv_path, "issue_body": body_path}


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def _raw_source_counts(raw_jobs: List[Dict[str, str]]) -> Dict[str, int]:
    counts = {"ats": 0, "official": 0, "linkedin": 0, "glassdoor": 0, "syncareer": "N/A"}
    for job in raw_jobs:
        src = (job.get("source") or "").lower()
        if "linkedin" in src:
            counts["linkedin"] += 1
        elif "glassdoor" in src:
            counts["glassdoor"] += 1
        elif "official" in src:
            counts["official"] += 1
        elif any(a in src for a in ("greenhouse", "lever", "ashby")):
            counts["ats"] += 1
        else:
            counts["ats"] += 1
    return counts


ENTRY_DEFAULTS: Dict[str, Any] = {
    "company": "", "title": "", "location": "", "posted_date": "",
    "date_confidence": "unknown", "official_url": "", "source": "", "source_url": "",
    "discovered_via": [], "filter_status": "kept", "drop_reason": "",
    "company_flag": "",
    "role_family": "", "role_relevance": 0, "tier": "", "recency_bucket": "",
    "cache_key": "", "jd_hash": "", "match_score": None, "resume_profile_used": "",
    "seniority_fit": "", "hard_constraint_status": "", "top_match_reasons": [],
    "main_gaps": [], "recommended_action": "", "screen_method": "", "score_source": "",
    "first_seen": "", "last_seen": "",
}


def ensure_entry_defaults(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize a (possibly legacy) store entry to the current schema."""
    for k, default in ENTRY_DEFAULTS.items():
        if k not in entry:
            entry[k] = default() if callable(default) else default
    return entry


def build_store_entry(job: Dict[str, str], key: str) -> Dict[str, Any]:
    """One canonical entry for jobs.json (kept OR dropped)."""
    return {
        # identity + display
        "key": key,
        "company": job.get("company", ""),
        "title": job.get("title", ""),
        "location": job.get("location", ""),
        "posted_date": job.get("posted_date", ""),
        "date_confidence": job.get("date_confidence", "unknown"),
        "official_url": job.get("official_url", ""),
        "source": job.get("source", ""),
        "source_url": job.get("source_url", ""),
        # provenance
        "discovered_via": list(job.get("discovered_via") or ([job.get("source", "")] if job.get("source") else [])),
        # pipeline status
        "filter_status": job.get("filter_status", "kept"),
        "drop_reason": job.get("drop_reason", ""),
        "company_flag": job.get("company_flag", ""),
        "role_family": job.get("role_family", ""),
        "role_relevance": int(job.get("role_relevance", 0) or 0),
        "tier": job.get("tier", ""),
        "recency_bucket": job.get("recency_bucket", ""),
        # LLM cache
        "cache_key": job.get("cache_key", ""),
        "jd_hash": job.get("jd_hash", ""),
        "match_score": job.get("match_score", None),
        "resume_profile_used": job.get("resume_profile_used", ""),
        "seniority_fit": job.get("seniority_fit", ""),
        "hard_constraint_status": job.get("hard_constraint_status", ""),
        "top_match_reasons": list(job.get("top_match_reasons") or []),
        "main_gaps": list(job.get("main_gaps") or []),
        "recommended_action": job.get("recommended_action", ""),
        "screen_method": job.get("screen_method", ""),
        "score_source": job.get("score_source", ""),
        # lifecycle
        "first_seen": job.get("first_seen", ""),
        "last_seen": job.get("last_seen", ""),
    }


def run() -> None:
    parser = argparse.ArgumentParser(description="Multi-source job board pipeline")
    parser.add_argument("--no-llm", action="store_true", help="Force rule-based scoring (local debug)")
    parser.add_argument("--skip-network", action="store_true", help="Ingest local snapshots only (no ATS/official fetch)")
    parser.add_argument("--local-out", action="store_true", help="Write to output/board-local/ (gitignored) for local testing")
    args = parser.parse_args()

    global BOARD_DIR, JOBS_STORE_PATH, LATEST_MD_PATH, INBOX_MD_PATH, INBOX_CSV_PATH, RUNS_DIR
    if args.local_out:
        BOARD_DIR = OUTPUT_DIR / "board-local"
        JOBS_STORE_PATH = BOARD_DIR / "jobs.json"
        LATEST_MD_PATH = BOARD_DIR / "latest.md"
        INBOX_MD_PATH = BOARD_DIR / "inbox.md"
        INBOX_CSV_PATH = BOARD_DIR / "inbox.csv"
        RUNS_DIR = BOARD_DIR / "runs"

    load_env_file(BASE_DIR / ".env")
    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    stamp = now.strftime("%Y-%m-%d_%H%M")
    session = make_session()
    targets = load_target_companies()
    profiles = load_profiles()
    company_filters = load_company_filters()

    # 1) Collect (raw)
    raw_jobs, meta = collect_sources(session, skip_network=args.skip_network)
    source_raw = _raw_source_counts(raw_jobs)

    # 2) Dedup + merge (carry discovered_via, prefer canonical source)
    deduped = merge_by_key(raw_jobs)
    # 3) Official verify then a second cross-source collapse
    verify_official(deduped)
    deduped = collapse_cross_source(deduped)

    # 4) Store lifecycle: assign first_seen/last_seen BEFORE recency so
    #    first_seen can back low-confidence sources.
    store = prune_store(load_store(), now)
    new_keys: set = set()
    for job in deduped:
        key = dedup_key(job)
        prev = store.get(key)
        if prev and prev.get("first_seen"):
            job["first_seen"] = prev["first_seen"]
        else:
            job["first_seen"] = now_iso
            new_keys.add(key)
        job["last_seen"] = now_iso
        job["recency_bucket"] = recency_bucket(job, now=now)

    # 5) Company filter (config-driven; applied before hard filter so excluded
    #    / covered-elsewhere companies never reach the LLM).
    drops: Counter = Counter()
    after_company: List[Dict[str, str]] = []
    for job in deduped:
        action, matched = classify_company(job.get("company", ""), company_filters)
        job["company_flag"] = "" if action == "keep" else action
        job["deprioritized"] = action == "deprioritize"
        job["preferred"] = action == "prefer"
        job["staffing_firm"] = action == "staffing"
        job["clearance_risk_company"] = bool(
            action == "clearance_risk"
            or _company_alias_hit(job.get("company", ""), company_filters.get("clearance_risk", []))
        )
        if action in CATEGORY_DROP_REASON:
            reason = CATEGORY_DROP_REASON[action]
            job["filter_status"] = "dropped"
            job["drop_reason"] = reason
            drops[reason] += 1
        else:
            after_company.append(job)

    # 6) Hard filter (records dropped too, for the store/funnel)
    after_hard: List[Dict[str, str]] = []
    for job in after_company:
        keep, reason = hard_filter(job)
        if keep:
            job["filter_status"] = "kept"
            job["drop_reason"] = ""
            after_hard.append(job)
        else:
            job["filter_status"] = "dropped"
            job["drop_reason"] = reason
            drops[reason] += 1

    # 6) Role-family + seniority prefilter (tighten LLM candidate pool)
    candidates: List[Dict[str, str]] = []
    for job in after_hard:
        keep, reason = role_seniority_prefilter(job)
        if keep:
            candidates.append(job)
        else:
            job["filter_status"] = "dropped"
            job["drop_reason"] = reason
            drops[reason] += 1

    # Referral flags on the candidate pool
    referrals: Dict[str, bool] = {}
    for job in candidates:
        name = match_target_company(job.get("company", ""), targets)
        referrals[dedup_key(job)] = bool(name)
        job["referral_name"] = name or ""

    # 7) Score: reuse cache, LLM only on new/changed, rule fallback
    screen_method, llm_errors, score_counts = score_survivors(
        candidates, referrals, profiles, store, use_llm=not args.no_llm
    )

    # 8) Tier + user-facing rank
    for job in candidates:
        job["tier"] = assign_tier(job, referrals.get(dedup_key(job), False))
        apply_referral_action(job)
    candidates.sort(key=user_facing_sort_key)

    tier_a = [j for j in candidates if j["tier"] == "A"]
    tier_b = [j for j in candidates if j["tier"] == "B"]
    ab_before_cap = len(tier_a) + len(tier_b)
    visible = (tier_a + tier_b)[:MAX_VISIBLE]  # already sorted by priority

    # 9) Rebuild store with deduped canonical jobs only (kept + dropped)
    new_store: Dict[str, Dict[str, Any]] = dict(store)
    for job in deduped:
        key = dedup_key(job)
        new_store[key] = build_store_entry(job, key)
    # Normalize carried-forward (legacy) entries to the current schema.
    for entry in new_store.values():
        ensure_entry_defaults(entry)
    new_store = prune_store(new_store, now)
    save_store(new_store)

    # 10) Recency distribution over kept (candidate) jobs
    recency_dist = {b: 0 for b in RECENCY_BUCKETS}
    for job in candidates:
        recency_dist[job.get("recency_bucket", "gt7d")] += 1

    stats = {
        "source_raw": source_raw,
        "funnel": {
            "after_dedup": len(deduped),
            "after_company": len(after_company),
            "after_hard_filter": len(after_hard),
            "after_prefilter": len(candidates),
            "dropped": sum(drops.values()),
        },
        "llm": {
            "scored": score_counts["llm"],
            "api_requests": score_counts.get("api_requests", 0),
            "reused": score_counts["reused"],
            "rule": score_counts["rule"],
            "recency_skipped": score_counts.get("recency_skipped", 0),
            "overflow": score_counts.get("overflow", 0),
            "new_or_changed": score_counts["new_or_changed"],
            "sent": score_counts.get("sent", 0),
        },
        "output": {
            "tier_a": len(tier_a),
            "tier_b": len(tier_b),
            "ab_before_cap": ab_before_cap,
            "shown": len(visible),
        },
        "recency": recency_dist,
        "screen_method": screen_method,
        "drops": dict(drops),
    }

    # 11) Outputs (Tier A/B only)
    write_latest_md(visible, stats, stamp)
    write_board_inbox(visible, stamp, now)
    new_ab = [j for j in visible if dedup_key(j) in new_keys]
    new_ab.sort(key=user_facing_sort_key)
    alert_paths: Dict[str, Path] = {}
    if new_ab:
        alert_paths = write_alert(new_ab, stamp)

    emit_github_output({
        "new_count": str(len(new_ab)),
        "stamp": stamp,
        "tier_a": str(len(tier_a)),
        "tier_b": str(len(tier_b)),
        "ab_before_cap": str(ab_before_cap),
        "shown": str(len(visible)),
        "llm_scored": str(score_counts["llm"]),
        "llm_api_requests": str(score_counts.get("api_requests", 0)),
        "llm_reused": str(score_counts["reused"]),
        "llm_rule_fallback": str(score_counts["rule"]),
        "issue_title": f"ATS/LinkedIn alert {stamp} ({len(new_ab)} new A/B)",
        "issue_body_path": str(alert_paths.get("issue_body", "")),
    })

    # Console summary
    print(f"Source raw: ATS {source_raw['ats']} / Official {source_raw['official']} / "
          f"LinkedIn {source_raw['linkedin']} / Glassdoor {source_raw['glassdoor']} / "
          f"Syncareer {source_raw['syncareer']}")
    print(f"Funnel: dedup {len(deduped)} -> company {len(after_company)} -> hard {len(after_hard)} "
          f"-> prefilter {len(candidates)} | dropped {sum(drops.values())}")
    print(f"LLM usage: scored {score_counts['llm']} / API requests {score_counts.get('api_requests', 0)} "
          f"/ cache reused {score_counts['reused']} / rule fallback+overflow {score_counts['rule']} "
          f"(recency-gated {score_counts.get('recency_skipped', 0)}, "
          f"overflow {score_counts.get('overflow', 0)}, new/changed {score_counts['new_or_changed']})")
    print(f"Screening: {screen_method}" + (f" ({len(llm_errors)} llm errors)" if llm_errors else ""))
    print(f"Output: Tier A {len(tier_a)} / Tier B {len(tier_b)} / A+B before cap {ab_before_cap} "
          f"/ shown {len(visible)} (cap {MAX_VISIBLE}) | new A/B {len(new_ab)}")
    print("Recency (kept): " + " / ".join(f"{b}={recency_dist[b]}" for b in RECENCY_BUCKETS))
    if drops:
        print("Drops: " + ", ".join(f"{k}={v}" for k, v in sorted(drops.items())))
    print(f"Wrote inbox {INBOX_MD_PATH} and {LATEST_MD_PATH}")
    print(f"Store: {JOBS_STORE_PATH} ({len(new_store)} entries)")


if __name__ == "__main__":
    run()
