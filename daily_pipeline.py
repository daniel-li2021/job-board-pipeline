#!/usr/bin/env python3
"""Daily Syncareer job pipeline.

Runs once per day:
  1. Keyword search (no company filter) over a recent time window.
  2. Deduplicate against a persistent seen-jobs store.
  3. Fetch full detail for each new job.
  4. Hard-filter (senior/lead titles, US-citizen-only, non-US locations).
  5. Enrich (sponsorship / target-company / graduation flags).
  6. LLM match against both resumes -> Tier 1 (must-apply) / Tier 2 (backup).
  7. Write dated CSVs + markdown report; update the seen store.

Usage:
    python3 daily_pipeline.py                # default: last3days window
    python3 daily_pipeline.py --time 24hours # only last 24 hours
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import time
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlencode
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

import alert_history
import board_pipeline as board
import coverage_reconcile
import board_pipeline as board
import llm_config
from sources.company_aliases import load_alias_file, match_company_alias
from sources.schema import normalize_sponsorship


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
DAILY_DIR = OUTPUT_DIR / "daily"
# Syncareer pipeline owns this folder. The ATS/LinkedIn board pipeline
# writes only under output/board/ — never mix the two.
SYNCAREER_DIR = OUTPUT_DIR / "syncareer"
RUNS_DIR = SYNCAREER_DIR / "runs"
SEEN_IDS_PATH = OUTPUT_DIR / "seen_job_ids.json"
WATCHLIST_PATH = SYNCAREER_DIR / "watchlist.json"
ALERT_HISTORY_PATH = SYNCAREER_DIR / "alert_history.json"
LEGACY_WATCHLIST_PATH = OUTPUT_DIR / "watchlist.json"
WATCHLIST_RETENTION_DAYS = 7
# Canonical "I skipped a day" view: kept jobs first_seen/posted in this window.
INBOX_DAYS = 3
COMPANY_LINKS_JSON = BASE_DIR / "source" / "company_links.json"
TARGET_COMPANIES_JSON = BASE_DIR / "source" / "target_companies.json"
SWE_RESUME_PATH = BASE_DIR / "profile" / "resume_swe.md"
AI_RESUME_PATH = BASE_DIR / "profile" / "resume_ai.md"
PACIFIC = ZoneInfo("America/Los_Angeles")

SEARCH_BASE_URL = "https://syncareer.com/"
DETAIL_API_URL = "https://syncareer.com/api/job/detail"
REQUEST_TIMEOUT = 30
PAGE_SLEEP_SECONDS = 0.35
DETAIL_SLEEP_SECONDS = 0.15
MAX_PAGES_PER_KEYWORD = 6
DEFAULT_TIME_WINDOW = "last3days"
EXPERIENCE_FILTER = "intern|new_grad|junior|mid"

# Keywords validated against Syncareer's search (see analysis in chat).
# "Software" and "Full Stack" cover core SWE; the AI/ML/Infra terms add
# largely non-overlapping roles. Data Engineer and Site Reliability were
# retained after bounded tests; broader Data Scientist searches were noisy.
SEARCH_KEYWORDS = [
    "Software",
    "Full Stack",
    "AI",
    "Machine Learning",
    "Infrastructure",
    "Forward Deployed",
    "DevOps",
    # Broader coverage added for the automated alert (largely non-overlapping,
    # dedup handles any repeats across keywords).
    "Backend",
    "Platform",
    "New Grad",
    "LLM",
    "Applied Scientist",
    "Data Engineer",
    "Site Reliability",
]

RAW_FIELDS = [
    "job_id",
    "title",
    "company",
    "location",
    "posting_date",
    "job_url",
    "experience",
    "degree",
    "remote_type",
    "salary",
    "sponsorship",
    "target_company",
    "target_company_match",
    "has_grad_req",
    "matched_keywords",
    "first_seen",
    "coverage_status",
    "canonical_source",
    "canonical_job_key",
    "duplicate_of",
    "official_snapshot_at",
    "source_snapshot_at",
    "description",
    "requirements",
    "snippet",
    "match_score",
    "tier",
    "score_source",
    "screen_method",
    "resume_profile_used",
    "role_family",
    "seniority_fit",
    "main_gaps",
    "recommended_action",
    "cache_key",
    "jd_hash",
]

TIER_FIELDS = [
    "tier",
    "match_score",
    "fit_score",
    "score_source",
    "recommended_resume",
    "company",
    "title",
    "location",
    "posting_date",
    "sponsorship",
    "target_company",
    "target_company_match",
    "job_url",
    "fit_category",
    "reason",
    "risk",
    "main_gaps",
    "sponsorship_concern",
    "screen_method",
    "job_id",
]


# --------------------------------------------------------------------------
# Shared utilities (self-contained; mirrors syncareer_deep_scrape.py)
# --------------------------------------------------------------------------
def load_env_file(path: Path) -> None:
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
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        }
    )
    return session


class NuxtPayloadDecoder:
    def __init__(self, array_payload: List[Any]) -> None:
        self.arr = array_payload
        self._cache: Dict[int, Any] = {}
        self._visiting: set[int] = set()

    def decode_ref(self, idx: int) -> Any:
        if idx in self._cache:
            return self._cache[idx]
        if idx in self._visiting:
            return None
        self._visiting.add(idx)
        value = self._decode_value(self.arr[idx])
        self._cache[idx] = value
        self._visiting.remove(idx)
        return value

    def _decode_value(self, value: Any) -> Any:
        if isinstance(value, int) and 0 <= value < len(self.arr):
            return self.decode_ref(value)
        if isinstance(value, list):
            if value and isinstance(value[0], str):
                tag = value[0]
                if tag in {"ShallowReactive", "Reactive"} and len(value) > 1:
                    return self._decode_value(value[1])
                if tag == "EmptyRef":
                    return None
                if tag == "Set":
                    return [self._decode_value(v) for v in value[1:]]
            return [self._decode_value(v) for v in value]
        if isinstance(value, dict):
            return {k: self._decode_value(v) for k, v in value.items()}
        return value


def extract_payload_array(html: str) -> Optional[List[Any]]:
    soup = BeautifulSoup(html, "html.parser")
    script_tags = soup.find_all("script", {"type": "application/json"})
    if not script_tags:
        return None
    payload_tag = max(script_tags, key=lambda x: len(x.string or x.text or ""))
    text = payload_tag.string or payload_tag.text or ""
    if not text:
        return None
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return None
    return payload if isinstance(payload, list) else None


def extract_search_result_global(html: str) -> Optional[Dict[str, Any]]:
    """Search page uses the 'index-search-result-' Nuxt key prefix."""
    payload_arr = extract_payload_array(html)
    if not payload_arr:
        return None
    root = NuxtPayloadDecoder(payload_arr).decode_ref(0)
    if not isinstance(root, dict):
        return None
    data_block = root.get("data") or {}
    if not isinstance(data_block, dict):
        return None
    for key, value in data_block.items():
        if "index-search-result-" in str(key) and isinstance(value, dict):
            return value
    return None


def parse_location(loc: Dict[str, Any]) -> str:
    city = ((loc.get("city") or {}).get("eng") or "").strip()
    province = ((loc.get("province") or {}).get("eng") or "").strip()
    country = ((loc.get("country") or {}).get("eng") or "").strip()
    parts = [p for p in [city, province, country] if p]
    return ", ".join(parts)


def classify_location_bucket(location: str) -> str:
    loc = (location or "").strip().lower()
    if not loc:
        return "unknown"
    if any(t in loc for t in ["united states", ", usa", ", us", "u.s."]):
        return "us"
    non_us_tokens = [
        "canada", "india", "china", "japan", "singapore", "ireland", "uk",
        "united kingdom", "germany", "france", "spain", "italy", "netherlands",
        "sweden", "switzerland", "australia", "new zealand", "mexico",
        "brazil", "argentina", "poland", "korea", "taiwan", "israel",
    ]
    if any(t in loc for t in non_us_tokens):
        return "non_us"
    return "unknown"


def epoch_to_date(value: Any) -> str:
    if not isinstance(value, (int, float)) or value <= 0:
        return ""
    return datetime.fromtimestamp(value, tz=timezone.utc).strftime("%Y-%m-%d")


def html_to_text(value: str) -> str:
    if not value:
        return ""
    soup = BeautifulSoup(value, "html.parser")
    text = soup.get_text("\n", strip=True)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()


def split_requirements(description_text: str) -> Tuple[str, str]:
    if not description_text:
        return "", ""
    lower = description_text.lower()
    anchors = [
        "minimum qualifications",
        "basic qualifications",
        "required qualifications",
        "preferred qualifications",
        "requirements",
        "qualifications",
    ]
    split_pos = -1
    for anchor in anchors:
        pos = lower.find(anchor)
        if pos >= 0 and (split_pos < 0 or pos < split_pos):
            split_pos = pos
    if split_pos < 0:
        return description_text, ""
    return description_text[:split_pos].strip(), description_text[split_pos:].strip()


def fetch_job_detail(session: requests.Session, job_id: str, referer_url: str) -> Optional[Dict[str, Any]]:
    try:
        resp = session.post(
            DETAIL_API_URL,
            json={"id": job_id},
            headers={"Referer": referer_url, "Content-Type": "application/json"},
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
        body = resp.json()
    except Exception:  # noqa: BLE001
        return None
    if not isinstance(body, dict) or body.get("code") != 0:
        return None
    data = body.get("data")
    return data if isinstance(data, dict) else None


# --------------------------------------------------------------------------
# Phase 1: keyword search
# --------------------------------------------------------------------------
def build_search_url(keyword: str, time_window: str, page: int) -> str:
    params = {
        "q": keyword,
        "loc": "United States",
        "time": time_window,
        "exps": EXPERIENCE_FILTER,
        "page": str(page),
    }
    return SEARCH_BASE_URL + "?" + urlencode(params)


def search_keyword(session: requests.Session, keyword: str, time_window: str) -> Dict[str, Dict[str, Any]]:
    """Return {job_id: summary_dict} for one keyword across pages."""
    found: Dict[str, Dict[str, Any]] = {}
    seen_signatures: set[Tuple[str, ...]] = set()
    for page in range(1, MAX_PAGES_PER_KEYWORD + 1):
        url = build_search_url(keyword, time_window, page)
        try:
            resp = session.get(url, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
        except Exception:  # noqa: BLE001
            break
        sr = extract_search_result_global(resp.text)
        if not sr:
            break
        page_list = sr.get("list") or []
        if not isinstance(page_list, list) or not page_list:
            break
        signature = tuple(sorted(str(i.get("id", "")) for i in page_list if i.get("id")))
        if signature in seen_signatures:
            break
        seen_signatures.add(signature)
        before = len(found)
        for item in page_list:
            jid = str(item.get("id", "")).strip()
            if jid and jid not in found:
                found[jid] = item
        if len(found) == before:
            break
        time.sleep(PAGE_SLEEP_SECONDS)
    return found


def run_search(session: requests.Session, time_window: str) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, List[str]], Dict[str, int]]:
    """Aggregate all keywords. Returns (id->summary, id->keywords, per-keyword counts)."""
    id_to_summary: Dict[str, Dict[str, Any]] = {}
    id_to_keywords: Dict[str, List[str]] = defaultdict(list)
    per_keyword_counts: Dict[str, int] = {}
    for keyword in SEARCH_KEYWORDS:
        found = search_keyword(session, keyword, time_window)
        per_keyword_counts[keyword] = len(found)
        for jid, summary in found.items():
            if jid not in id_to_summary:
                id_to_summary[jid] = summary
            id_to_keywords[jid].append(keyword)
        time.sleep(0.4)
    return id_to_summary, id_to_keywords, per_keyword_counts


# --------------------------------------------------------------------------
# Phase 2: incremental dedup
# --------------------------------------------------------------------------
def load_seen_ids() -> set[str]:
    if not SEEN_IDS_PATH.exists():
        return set()
    try:
        data = json.loads(SEEN_IDS_PATH.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return set()
    if isinstance(data, dict):
        return set(str(x) for x in data.get("seen_ids", []))
    if isinstance(data, list):
        return set(str(x) for x in data)
    return set()


def save_seen_ids(seen_ids: set[str]) -> None:
    SEEN_IDS_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(seen_ids),
        "seen_ids": sorted(seen_ids),
    }
    SEEN_IDS_PATH.write_text(json.dumps(payload, indent=0), encoding="utf-8")


# --------------------------------------------------------------------------
# Rolling 7-day watchlist (used by the automated alert flow)
# --------------------------------------------------------------------------
def _parse_iso_date(value: str) -> Optional[datetime]:
    value = (value or "").strip()
    if not value:
        return None
    parsed: Optional[datetime] = None
    try:
        # Accept both "YYYY-MM-DD" and full ISO timestamps.
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        try:
            parsed = datetime.strptime(value[:10], "%Y-%m-%d")
        except ValueError:
            return None
    # Normalize to UTC-aware so comparisons never mix naive/aware.
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def load_watchlist() -> Dict[str, Dict[str, Any]]:
    """Return {job_id: entry}. Entry keeps title/company/posted/url/first_seen."""
    path = WATCHLIST_PATH if WATCHLIST_PATH.exists() else LEGACY_WATCHLIST_PATH
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {}
    entries = data.get("entries") if isinstance(data, dict) else data
    out: Dict[str, Dict[str, Any]] = {}
    if isinstance(entries, list):
        for e in entries:
            jid = str(e.get("job_id", "")).strip()
            if jid:
                out[jid] = e
    elif isinstance(entries, dict):
        for jid, e in entries.items():
            out[str(jid)] = e
    return out


def prune_watchlist(
    watchlist: Dict[str, Dict[str, Any]],
    now: Optional[datetime] = None,
    retention_days: int = WATCHLIST_RETENTION_DAYS,
) -> Dict[str, Dict[str, Any]]:
    """Drop entries whose posted_date/first_seen are older than retention_days."""
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=retention_days)
    kept: Dict[str, Dict[str, Any]] = {}
    for jid, e in watchlist.items():
        ref = _parse_iso_date(e.get("first_seen", "")) or _parse_iso_date(e.get("posted_date", ""))
        # Missing/unparseable dates: keep (they will age out once first_seen set).
        if ref is None or ref >= cutoff:
            kept[jid] = e
    return kept


def save_watchlist(watchlist: Dict[str, Dict[str, Any]]) -> None:
    WATCHLIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    entries = sorted(
        watchlist.values(),
        key=lambda e: (e.get("first_seen", ""), e.get("job_id", "")),
        reverse=True,
    )
    payload = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "retention_days": WATCHLIST_RETENTION_DAYS,
        "count": len(entries),
        "entries": entries,
    }
    WATCHLIST_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _entry_age_ref(entry: Dict[str, Any]) -> Optional[datetime]:
    """Discovery activity for inbox/rolling views; posting date is fallback."""
    return (
        _parse_iso_date(entry.get("first_seen", ""))
        or _parse_iso_date(entry.get("posting_date", ""))
        or _parse_iso_date(entry.get("posted_date", ""))
    )


def inbox_entries(
    watchlist: Dict[str, Dict[str, Any]],
    now: Optional[datetime] = None,
    inbox_days: int = INBOX_DAYS,
) -> List[Dict[str, Any]]:
    """Kept jobs from the last inbox_days (posted_date, else first_seen)."""
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=inbox_days)
    kept: List[Dict[str, Any]] = []
    for e in watchlist.values():
        if str(e.get("kept", "")).lower() not in {"yes", "true", "1"}:
            continue
        ref = _entry_age_ref(e)
        if ref is None or ref >= cutoff:
            kept.append(e)
    kept.sort(
        key=lambda e: (
            0 if e.get("target_company") == "yes" else 1,
            e.get("posted_date") or e.get("first_seen") or "",
        ),
        reverse=True,
    )
    return kept


def _watchlist_to_alert_row(e: Dict[str, Any]) -> Dict[str, str]:
    return {
        "title": e.get("title", ""),
        "company": e.get("company", ""),
        "location": e.get("location", ""),
        "posting_date": e.get("posting_date") or e.get("posted_date") or "",
        "sponsorship": e.get("sponsorship", ""),
        "target_company": e.get("target_company", ""),
        "target_company_match": e.get("target_company_match", ""),
        "has_grad_req": e.get("has_grad_req", ""),
        "matched_keywords": e.get("matched_keywords", ""),
        "salary": e.get("salary", ""),
        "job_url": e.get("job_url") or e.get("url") or "",
        "first_seen": e.get("first_seen", ""),
        "tier": e.get("tier", ""),
        "match_score": e.get("match_score", e.get("fit_score", "")),
        "fit_score": e.get("fit_score", ""),
        "score_source": e.get("score_source", ""),
        "screen_method": e.get("screen_method", ""),
        "resume_profile_used": e.get("resume_profile_used", ""),
        "role_family": e.get("role_family", ""),
        "seniority_fit": e.get("seniority_fit", ""),
        "main_gaps": e.get("main_gaps", []),
        "recommended_action": e.get("recommended_action", ""),
        "recommended_resume": e.get("recommended_resume", ""),
        "review_status": e.get("review_status", "unreviewed"),
        "coverage_status": e.get("coverage_status", ""),
        "canonical_source": e.get("canonical_source", ""),
        "canonical_job_key": e.get("canonical_job_key", ""),
        "duplicate_of": e.get("duplicate_of", ""),
        "official_snapshot_at": e.get("official_snapshot_at", ""),
        "source_snapshot_at": e.get("source_snapshot_at", ""),
        "source_pipeline": e.get("source_pipeline", "syncareer"),
    }


def write_syncareer_inbox(rows: List[Dict[str, Any]], stamp: str, with_tiers: bool) -> None:
    SYNCAREER_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(SYNCAREER_DIR / "inbox.csv", rows, ALERT_FIELDS)
    (SYNCAREER_DIR / "inbox.txt").write_text(
        build_alert_txt(rows, f"inbox last {INBOX_DAYS}d @ {stamp}", with_tiers),
        encoding="utf-8",
    )
    md_table = _jobs_markdown_table(rows, with_tiers)
    (SYNCAREER_DIR / "inbox.md").write_text(
        "\n".join(
            [
                f"# Syncareer inbox (last {INBOX_DAYS} days)",
                "",
                f"- Updated (PT): {datetime.now(PACIFIC).strftime('%Y-%m-%d %H:%M %Z')}",
                f"- Snapshot (UTC): {datetime.now(timezone.utc).isoformat()}",
                f"- Jobs: {len(rows)}",
                f"- Last 24 hours: {sum(1 for r in rows if (_entry_age_ref(r) or datetime.now(timezone.utc)) >= datetime.now(timezone.utc) - timedelta(hours=24))}",
                f"- Last 3 days: {len(rows)}",
                "",
                "If you check every 1–2 days, **only open this file**. Dated run files are in `runs/`.",
                "",
                md_table,
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def _jobs_markdown_table(rows: List[Dict[str, Any]], with_tiers: bool) -> str:
    lines: List[str] = []
    if with_tiers:
        lines.append("| Tier | Score | Source | Company | Title | Location | Posted | Sponsorship | Referral | Review | Coverage | Link |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    else:
        lines.append("| Source | Company | Title | Location | Posted | Sponsorship | Referral | Review | Coverage | Link |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        title = (r.get("title") or "").replace("|", "/")[:70]
        company = (r.get("company") or "").replace("|", "/")
        loc = (r.get("location") or "").replace("|", "/")
        referral = f"YES ({r['target_company_match']})" if r.get("target_company") == "yes" else "-"
        url = r.get("job_url") or r.get("url") or ""
        link = f"[open]({url})" if url else "-"
        posted = r.get("posting_date") or r.get("posted_date") or ""
        if with_tiers:
            lines.append(
                f"| {r.get('tier','-')} | {r.get('match_score', r.get('fit_score','-'))} | Syncareer | {company} | {title} | "
                f"{loc} | {posted} | {r.get('sponsorship','')} | {referral} | {r.get('review_status') or 'unreviewed'} | {r.get('coverage_status') or '-'} | {link} |"
            )
        else:
            lines.append(
                f"| Syncareer | {company} | {title} | {loc} | {posted} | "
                f"{r.get('sponsorship','')} | {referral} | {r.get('review_status') or 'unreviewed'} | {r.get('coverage_status') or '-'} | {link} |"
            )
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Phase 3 + 5: normalize + enrich
# --------------------------------------------------------------------------
def normalize_company_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


def load_target_companies() -> List[Dict[str, Any]]:
    return load_alias_file(TARGET_COMPANIES_JSON)


def match_target_company(company_name: str, targets: List[Dict[str, Any]]) -> Optional[str]:
    return match_company_alias(company_name, targets)


def apply_external_company_policy(
    row: Dict[str, Any], company_filters: Dict[str, List[Dict[str, Any]]]
) -> bool:
    """Apply shared company flags; return True when externally hidden."""
    action, _matched = board.classify_company(
        str(row.get("company") or ""), company_filters, str(row.get("title") or "")
    )
    row["company_flag"] = "" if action == "keep" else action
    row["deprioritized"] = action == "deprioritize"
    row["preferred"] = action == "prefer"
    row["staffing_firm"] = action == "staffing"
    row["clearance_risk_company"] = action == "clearance_risk"
    hidden = board.hidden_external_company(str(row.get("company") or ""), company_filters)
    if hidden:
        row["company_flag"] = "hidden_external"
        row["filter_status"] = "hidden"
        row["drop_reason"] = "company_hidden_external"
        row["suppress_alert"] = True
        return True
    return False


def sponsorship_from_supports(supports: Any) -> str:
    if not isinstance(supports, list) or not supports:
        return "Unknown"
    joined = " ".join(str(s).lower() for s in supports)
    if "h1b" in joined or "h-1b" in joined:
        return "Sponsor"
    # Field present but no H1B token -> employer indicated no sponsorship.
    return "No sponsor"


GRAD_YEAR_RE = re.compile(r"\b(graduat\w*|class of|degree)\b[^\n]{0,60}\b(202[4-9])\b", re.IGNORECASE)
GRAD_YEAR_RE2 = re.compile(r"\b(202[4-9])\b[^\n]{0,40}\bgraduat", re.IGNORECASE)


def detect_grad_requirement(text: str) -> str:
    if not text:
        return "no"
    if GRAD_YEAR_RE.search(text) or GRAD_YEAR_RE2.search(text):
        return "yes"
    return "no"


def format_salary(salary: Any) -> str:
    if not isinstance(salary, dict):
        return ""
    smin = salary.get("min")
    smax = salary.get("max")
    currency = salary.get("currency") or ""
    stype = salary.get("type") or ""
    if smin and smax:
        return f"{smin:,}-{smax:,} {currency}/{stype}".strip()
    return ""


def normalize_job_row(
    summary: Dict[str, Any],
    detail: Dict[str, Any],
    matched_keywords: List[str],
    targets: List[Dict[str, Any]],
) -> Dict[str, str]:
    location_info = detail.get("location") or summary.get("location") or {}
    location = parse_location(location_info) if isinstance(location_info, dict) else ""
    title = str(detail.get("title") or summary.get("title") or "").strip()
    company = str(
        detail.get("companyNameEng")
        or summary.get("companyNameEng")
        or detail.get("companyNameChn")
        or ""
    ).strip()
    posting_date = epoch_to_date(detail.get("publishAt") or summary.get("publishAt"))
    job_url = str(detail.get("url") or summary.get("url") or "").strip()
    desc_text = html_to_text(str(detail.get("desc") or ""))
    desc_main, requirements = split_requirements(desc_text)
    supports = detail.get("supports")
    if supports is None:
        supports = summary.get("supports")
    sponsorship = normalize_sponsorship(
        {"sponsorship": sponsorship_from_supports(supports), "description": desc_text}
    )
    target_match = match_target_company(company, targets)

    return {
        "job_id": str(detail.get("id") or summary.get("id") or ""),
        "title": title,
        "company": company,
        "location": location,
        "posting_date": posting_date,
        "job_url": job_url,
        "experience": str(detail.get("experience") or summary.get("experience") or ""),
        "degree": str(detail.get("degree") or summary.get("degree") or ""),
        "remote_type": str(detail.get("remoteType") or summary.get("remoteType") or ""),
        "salary": format_salary(detail.get("salary") or summary.get("salary")),
        "sponsorship": sponsorship,
        "target_company": "yes" if target_match else "no",
        "target_company_match": target_match or "",
        "has_grad_req": detect_grad_requirement(desc_text),
        "matched_keywords": ", ".join(matched_keywords),
        "description": desc_main,
        "requirements": requirements,
        "snippet": (desc_main or requirements or title)[:400],
    }


# --------------------------------------------------------------------------
# Phase 4: hard filters
# --------------------------------------------------------------------------
SENIOR_TITLE_RE = re.compile(
    r"\b(senior|sr\.?|lead|staff|principal|director|manager|head of|vp|vice president|architect)\b",
    re.IGNORECASE,
)
CITIZEN_ONLY_PHRASES = [
    "us citizen",
    "u.s. citizen",
    "united states citizen",
    "us citizenship",
    "u.s. citizenship",
    "must be a citizen",
    "us person",
    "u.s. person",
    "security clearance",
]
# Word-boundary regexes so e.g. "campus personnel" does not match "us person".
CITIZEN_ONLY_RES = [
    (phrase, re.compile(r"\b" + re.escape(phrase).replace(r"\ ", r"\s+") + r"\b", re.IGNORECASE))
    for phrase in CITIZEN_ONLY_PHRASES
]


def hard_filter(
    row: Dict[str, str],
    company_filters: Optional[Dict[str, List[Dict[str, Any]]]] = None,
) -> Tuple[bool, str]:
    """Use the Board's shared hard constraints; seniority is the next gate."""
    if company_filters is not None:
        action, _matched = board.classify_company(
            row.get("company", ""), company_filters, row.get("title", "")
        )
        if action == "exclude":
            return False, "company_excluded"
        row["clearance_risk_company"] = action == "clearance_risk"
    job = coverage_reconcile.normalize_syncareer_job(row)
    job["clearance_risk_company"] = bool(row.get("clearance_risk_company"))
    keep, reason = board.hard_filter(job)
    return (keep, "keep" if keep else f"exclude_{reason}")


# --------------------------------------------------------------------------
# Phase 6: LLM tier assignment
# --------------------------------------------------------------------------
SHARED_SCORE_FIELDS = (
    "match_score", "tier", "score_source", "screen_method",
    "resume_profile_used", "role_family", "role_relevance",
    "seniority_fit", "hard_constraint_status", "top_match_reasons",
    "main_gaps", "recommended_action", "cache_key", "jd_hash",
    "match_canonical_key", "match_source_pipeline", "match_jd_hash",
    "recency_bucket",
)


def to_shared_job(row: Dict[str, Any], now_iso: str = "") -> Dict[str, Any]:
    """Map one Syncareer record into the Board's canonical matching schema."""
    job = coverage_reconcile.normalize_syncareer_job(row)
    job["first_seen"] = str(row.get("first_seen") or now_iso)
    job["last_seen"] = now_iso or str(row.get("last_seen") or "")
    job["source_pipeline"] = "syncareer"
    job["referral_name"] = str(
        row.get("referral_name") or row.get("target_company_match") or ""
    )
    for field in (
        "canonical_job_key", "duplicate_of", "coverage_status",
        "official_snapshot_at", "source_snapshot_at", "deprioritized",
        "preferred", "staffing_firm", "company_flag", "referral_name",
    ):
        if row.get(field) not in (None, ""):
            job[field] = row.get(field)
    keep, _reason = board.role_seniority_prefilter(job)
    if not keep:
        # Callers only pass shared-prefilter survivors. Retain the detected
        # family/seniority fields if a legacy row slips through.
        job.setdefault("role_family", board.detect_role_family(job))
    job["recency_bucket"] = board.recency_bucket(job)
    return job


def shared_score_store(watchlist: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Index persisted Syncareer scoring/cache fields by shared dedup key."""
    store: Dict[str, Dict[str, Any]] = {}
    for entry in watchlist.values():
        job = to_shared_job(entry)
        key = board.dedup_key(job)
        cached = dict(entry)
        cached["key"] = key
        cached.setdefault("canonical_job_key", job.get("canonical_job_key") or key)
        store[key] = cached
    return store


def assign_shared_scores(
    rows: List[Dict[str, Any]],
    watchlist: Dict[str, Dict[str, Any]],
    use_llm: bool,
) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, int], List[str], str]:
    """Use the shared 0-100 matcher and deterministic A/B/C tier policy."""
    if not rows:
        return {}, {"llm": 0, "reused": 0, "rule": 0, "api_requests": 0}, [], "none"
    now_iso = datetime.now(timezone.utc).isoformat()
    jobs = [to_shared_job(row, now_iso) for row in rows]
    referrals: Dict[str, bool] = {}
    for job in jobs:
        referrals[board.dedup_key(job)] = bool(job.get("referral_name"))
    method, errors, counts = board.score_survivors(
        jobs,
        referrals,
        board.load_profiles(),
        shared_score_store(watchlist),
        use_llm=use_llm,
        peer_stores=[
            ("official", board.load_store_path(OUTPUT_DIR / "official_careers" / "jobs.json"))
        ],
        prefer_peer=True,
    )
    decisions: Dict[str, Dict[str, Any]] = {}
    for job in jobs:
        job["tier"] = board.assign_tier(job, referrals.get(board.dedup_key(job), False))
        board.apply_referral_action(job)
        result = {field: job.get(field) for field in SHARED_SCORE_FIELDS}
        # fit_score remains a compatibility alias, now on the shared 0-100 scale.
        result["fit_score"] = job.get("match_score", "")
        result["recommended_resume"] = (
            "AI-FDE" if job.get("resume_profile_used") == "resume_ai" else "SWE"
        )
        result["fit_category"] = job.get("role_family", "")
        result["reason"] = "; ".join(job.get("top_match_reasons") or [])
        result["risk"] = "; ".join(job.get("main_gaps") or [])
        result["sponsorship_concern"] = "yes" if str(
            next((r.get("sponsorship") for r in rows if str(r.get("job_id")) == str(job.get("job_id"))), "")
        ) in {"No sponsor", "Unknown"} else "no"
        decisions[str(job.get("job_id") or "")] = result
    return decisions, counts, errors, method


def build_providers() -> List[Dict[str, str]]:
    providers: List[Dict[str, str]] = []
    openai_key = (os.environ.get("OPENAI_API_KEY") or "").strip()
    groq_key = (os.environ.get("GROQ_API_KEY") or "").strip()
    if openai_key:
        providers.append(
            {"name": "openai", "endpoint": llm_config.OPENAI_CHAT_COMPLETIONS_ENDPOINT, "api_key": openai_key, "model": llm_config.configured_model()}
        )
    if groq_key:
        providers.append(
            {"name": "groq", "endpoint": llm_config.GROQ_CHAT_COMPLETIONS_ENDPOINT, "api_key": groq_key, "model": llm_config.GROQ_FALLBACK_MODEL}
        )
    return providers


def parse_json_object(text: str) -> Optional[Dict[str, Any]]:
    text = (text or "").strip()
    try:
        data = json.loads(text)
        return data if isinstance(data, dict) else None
    except Exception:  # noqa: BLE001
        pass
    match = re.search(r"\{.*\}", text, flags=re.S)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
        return data if isinstance(data, dict) else None
    except Exception:  # noqa: BLE001
        return None


def full_text_of(row: Dict[str, str]) -> str:
    description = (row.get("description") or "").strip()
    requirements = (row.get("requirements") or "").strip()
    if description and requirements:
        return f"{description}\n{requirements}"
    return description or requirements


def llm_tier_batch(
    batch: List[Dict[str, str]],
    swe_resume: str,
    ai_resume: str,
    provider: Dict[str, str],
    resume_route: str,
) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Any]]:
    jobs_payload = [
        {
            "job_id": r["job_id"],
            "title": r["title"],
            "company": r["company"],
            "location": r["location"],
            "sponsorship": r["sponsorship"],
            "job_description": llm_config.select_jd_context(full_text_of(r)),
        }
        for r in batch
    ]
    prompt = {
        "task": "Match early-career SWE / AI-engineer jobs to the candidate using responsibilities and core required qualifications.",
        "candidate_target": "New-grad / early-career Software Engineer or AI/ML Engineer. Master's CS (grad 2026).",
        "tier_rules": [
            "tier 1 = strong or exceptional match (fit_score >= 80)",
            "tier 2 = reasonable or weak/stretch match (fit_score 60-79)",
            "skip = generally skip (fit_score < 60)",
        ],
        "resume_route": resume_route,
        "instructions": [
            "Score 0-100 with broad spread: 90+ exceptional/direct, 80s strong, 70s reasonable, 60s weak/stretch, below 60 generally skip.",
            "Use responsibilities and required/minimum qualifications, not keyword overlap.",
            "Do not automatically reject strong 3-5 years-of-experience fits; judge demonstrated scope and core skills.",
            "main_gaps contains only meaningful missing core requirements; preferred/nice-to-have gaps are minor.",
            "Flag sponsorship_concern=yes when sponsorship is 'No sponsor' or 'Unknown'.",
        ],
        "return_schema": {
            "results": [
                {
                    "job_id": "string",
                    "fit_score": "0-100 int",
                    "recommended_resume": "SWE|AI-FDE",
                    "tier": "1|2|skip",
                    "fit_category": "short string",
                    "reason": "short string",
                    "risk": "short string",
                    "main_gaps": ["0-3 missing core requirements"],
                    "sponsorship_concern": "yes|no",
                }
            ]
        },
        "jobs": jobs_payload,
    }
    if resume_route in {"SWE", "BOTH"}:
        prompt["swe_resume"] = swe_resume
    if resume_route in {"AI-FDE", "BOTH"}:
        prompt["ai_fde_resume"] = ai_resume
    request_json: Dict[str, Any] = {
        "model": provider["model"],
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": "You are a precise early-career tech recruiting screener. Return JSON only."},
            {"role": "user", "content": json.dumps(prompt)},
        ],
    }
    if provider["name"] == "openai":
        request_json["reasoning_effort"] = llm_config.configured_reasoning_effort()
    resp = requests.post(
        provider["endpoint"],
        headers={"Authorization": f"Bearer {provider['api_key']}", "Content-Type": "application/json"},
        json=request_json,
        timeout=90,
    )
    resp.raise_for_status()
    response_payload = resp.json()
    usage = llm_config.usage_from_response(response_payload, provider["model"])
    parsed = parse_json_object(response_payload["choices"][0]["message"]["content"])
    if not parsed:
        return {}, usage
    out: Dict[str, Dict[str, Any]] = {}
    for item in parsed.get("results", []):
        job_id = str(item.get("job_id", "")).strip()
        if not job_id:
            continue
        tier = str(item.get("tier", "skip")).lower().strip()
        if tier not in {"1", "2", "skip"}:
            tier = "skip"
        out[job_id] = {
            "fit_score": float(item.get("fit_score", 0) or 0),
            "recommended_resume": str(item.get("recommended_resume", "SWE")),
            "tier": tier,
            "fit_category": str(item.get("fit_category", "")),
            "reason": str(item.get("reason", "")),
            "risk": str(item.get("risk", "")),
            "main_gaps": (
                [str(x) for x in item.get("main_gaps", [])][:3]
                if isinstance(item.get("main_gaps"), list)
                else ([str(item.get("main_gaps"))] if item.get("main_gaps") else [])
            ),
            "sponsorship_concern": str(item.get("sponsorship_concern", "no")).lower(),
        }
    usage["jobs_scored"] = len(out)
    usage["estimated_usd"] = llm_config.estimate_cost_usd(usage)
    return out, usage


def fallback_tier(row: Dict[str, str]) -> Dict[str, Any]:
    title = (row.get("title") or "").lower()
    text = f"{title} {full_text_of(row)[:1200]}".lower()
    ai_signals = ["machine learning", " ml", " ai ", "llm", "rag", "agent", "applied ai", "model", "forward deployed"]
    eng_signals = [
        "software engineer", "backend", "full stack", "full-stack", "platform",
        "infrastructure", "cloud", "devops", "data engineer", "distributed",
    ]
    score = 4.5
    if any(x in text for x in eng_signals):
        score += 2.2
    if any(x in text for x in ai_signals):
        score += 1.6
    score = max(1.0, min(10.0, score))
    tier = "skip"
    score *= 10
    if score >= 80:
        tier = "1"
    elif score >= 60:
        tier = "2"
    rec = "AI-FDE" if any(x in text for x in ai_signals) else "SWE"
    concern = "yes" if row.get("sponsorship") in {"No sponsor", "Unknown"} else "no"
    return {
        "fit_score": round(score, 1),
        "recommended_resume": rec,
        "tier": tier,
        "fit_category": "keyword_match",
        "reason": "Keyword-based technical relevance (LLM unavailable)",
        "risk": "No LLM judgment; verify manually",
        "main_gaps": [],
        "sponsorship_concern": concern,
    }


def assign_tiers(
    rows: List[Dict[str, str]],
    swe_resume: str,
    ai_resume: str,
) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, str], List[str], Dict[str, Any]]:
    """Return decisions, methods, errors, and per-run LLM usage."""
    decisions: Dict[str, Dict[str, Any]] = {}
    methods: Dict[str, str] = {}
    errors: List[str] = []
    providers = build_providers()
    usage_total = llm_config.empty_usage(providers[0]["model"] if providers else None)
    if not providers:
        errors.append("no_api_key_configured")
        for row in rows:
            decisions[row["job_id"]] = fallback_tier(row)
            methods[row["job_id"]] = "fallback"
        return decisions, methods, errors, usage_total

    chunk_size = 12
    routed_batches: List[Tuple[str, List[Dict[str, str]]]] = []
    def family_of(row: Dict[str, str]) -> str:
        routed_row = dict(row)
        routed_row["description"] = full_text_of(row)
        return board.detect_role_family(routed_row)

    for route, family in (("SWE", "swe"), ("AI-FDE", "ai"), ("BOTH", "ambiguous")):
        routed = [r for r in rows if family_of(r) == family]
        routed_batches.extend((route, routed[i : i + chunk_size]) for i in range(0, len(routed), chunk_size))
    for chunk_idx, (route, batch) in enumerate(routed_batches):
        batch_done = False
        chunk_errors: List[str] = []
        for provider in providers:
            try:
                result, usage = llm_tier_batch(batch, swe_resume, ai_resume, provider, route)
                llm_config.merge_usage(usage_total, [usage])
                if result:
                    for row in batch:
                        d = result.get(row["job_id"])
                        if d is not None:
                            decisions[row["job_id"]] = d
                            methods[row["job_id"]] = "llm_decision"
                    batch_done = True
                    break
            except Exception as exc:  # noqa: BLE001
                usage_total["api_requests"] += 1
                chunk_errors.append(f"{provider['name']}:{type(exc).__name__}:{str(exc)[:120]}")
                continue
        # Fill any rows the LLM omitted, or the whole batch on failure.
        for row in batch:
            if row["job_id"] not in decisions:
                decisions[row["job_id"]] = fallback_tier(row)
                methods[row["job_id"]] = "fallback"
        if batch_done:
            time.sleep(0.25)
        else:
            errors.append(f"chunk_{chunk_idx}_failed[{len(batch)} jobs]: " + " | ".join(chunk_errors))
    usage_total["jobs_scored"] = sum(1 for method in methods.values() if method == "llm_decision")
    return decisions, methods, errors, usage_total


# --------------------------------------------------------------------------
# Phase 7: outputs
# --------------------------------------------------------------------------
def write_csv(path: Path, rows: List[Dict[str, Any]], fields: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


# Compact schema for the downloadable alert CSV/TXT.
ALERT_FIELDS = [
    "title",
    "company",
    "location",
    "posting_date",
    "sponsorship",
    "target_company_match",
    "has_grad_req",
    "matched_keywords",
    "salary",
    "tier",
    "match_score",
    "fit_score",
    "score_source",
    "screen_method",
    "resume_profile_used",
    "role_family",
    "seniority_fit",
    "main_gaps",
    "recommended_action",
    "recommended_resume",
    "first_seen",
    "review_status",
    "coverage_status",
    "canonical_source",
    "canonical_job_key",
    "duplicate_of",
    "official_snapshot_at",
    "source_snapshot_at",
    "source_pipeline",
    "job_url",
]


def emit_github_output(values: Dict[str, str]) -> None:
    """Expose key=value pairs to GitHub Actions steps via $GITHUB_OUTPUT."""
    out_path = os.environ.get("GITHUB_OUTPUT")
    if not out_path:
        return
    try:
        with open(out_path, "a", encoding="utf-8") as f:
            for key, value in values.items():
                f.write(f"{key}={value}\n")
    except Exception:  # noqa: BLE001
        pass


def build_issue_body(new_rows: List[Dict[str, Any]], stamp: str, with_tiers: bool) -> str:
    lines: List[str] = []
    lines.append(f"Syncareer alert — {stamp}")
    lines.append("")
    lines.append(f"Updated (PT): {datetime.now(PACIFIC).strftime('%Y-%m-%d %H:%M %Z')}")
    lines.append(f"Snapshot (UTC): {datetime.now(timezone.utc).isoformat()}")
    lines.append("")
    lines.append(f"{len(new_rows)} new matching job(s) this run (hard-filtered).")
    lines.append("")
    lines.append(
        f"If you skipped a day, **do not read every Issue**. Open "
        f"`output/syncareer/inbox.md` in the repo (last {INBOX_DAYS} days, one file)."
    )
    lines.append("")
    referral_rows = [r for r in new_rows if r.get("target_company") == "yes"]
    if referral_rows:
        lines.append(f"Referral companies in this batch: {len(referral_rows)}")
        lines.append("")
    if with_tiers:
        header = "| Tier | Score | Source | Company | Title | Location | Posted | Sponsorship | Referral | Review | Coverage | Link |"
        sep = "|---|---|---|---|---|---|---|---|---|---|---|---|"
    else:
        header = "| Source | Company | Title | Location | Posted | Sponsorship | Referral | Review | Coverage | Link |"
        sep = "|---|---|---|---|---|---|---|---|---|---|"
    lines.append(header)
    lines.append(sep)
    for r in new_rows:
        title = (r.get("title") or "").replace("|", "/")[:70]
        company = (r.get("company") or "").replace("|", "/")
        loc = (r.get("location") or "").replace("|", "/")
        referral = f"YES ({r['target_company_match']})" if r.get("target_company") == "yes" else "-"
        link = f"[open]({r.get('job_url','')})" if r.get("job_url") else "-"
        if with_tiers:
            lines.append(
                f"| {r.get('tier','-')} | {r.get('match_score', r.get('fit_score','-'))} | Syncareer | {company} | {title} | "
                f"{loc} | {r.get('posting_date','')} | {r.get('sponsorship','')} | {referral} | {r.get('review_status') or 'unreviewed'} | {r.get('coverage_status') or '-'} | {link} |"
            )
        else:
            lines.append(
                f"| Syncareer | {company} | {title} | {loc} | {r.get('posting_date','')} | "
                f"{r.get('sponsorship','')} | {referral} | {r.get('review_status') or 'unreviewed'} | {r.get('coverage_status') or '-'} | {link} |"
            )
    lines.append("")
    lines.append(
        f"Inbox CSV: `output/syncareer/inbox.csv`. This-run snapshot: `output/syncareer/runs/{stamp}.csv`."
    )
    return "\n".join(lines)


def build_alert_txt(new_rows: List[Dict[str, Any]], stamp: str, with_tiers: bool) -> str:
    lines: List[str] = [f"Syncareer job alert - {stamp}", f"{len(new_rows)} new job(s)", ""]
    for i, r in enumerate(new_rows, 1):
        head = f"[{i}] {r.get('company','')} - {r.get('title','')}"
        if with_tiers and r.get("tier"):
            head += f"  (Tier {r.get('tier')}, score {r.get('match_score', r.get('fit_score'))})"
        lines.append(head)
        referral = f" | Referral: {r['target_company_match']}" if r.get("target_company") == "yes" else ""
        lines.append(
            f"    {r.get('location','')} | Posted: {r.get('posting_date','')} | "
            f"{r.get('sponsorship','')}{referral}"
        )
        if r.get("matched_keywords"):
            lines.append(f"    Keywords: {r.get('matched_keywords')}")
        if r.get("job_url"):
            lines.append(f"    {r.get('job_url')}")
        lines.append("")
    return "\n".join(lines)


def write_alert_outputs(new_rows: List[Dict[str, Any]], stamp: str, with_tiers: bool) -> Dict[str, Path]:
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    SYNCAREER_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = RUNS_DIR / f"{stamp}.csv"
    txt_path = RUNS_DIR / f"{stamp}.txt"
    issue_body_path = SYNCAREER_DIR / "issue_body.md"

    write_csv(csv_path, new_rows, ALERT_FIELDS)
    txt_path.write_text(build_alert_txt(new_rows, stamp, with_tiers), encoding="utf-8")
    issue_body_path.write_text(build_issue_body(new_rows, stamp, with_tiers), encoding="utf-8")
    return {
        "csv": csv_path,
        "txt": txt_path,
        "issue_body": issue_body_path,
    }


def run() -> None:
    parser = argparse.ArgumentParser(description="Daily Syncareer job pipeline")
    parser.add_argument("--time", default=DEFAULT_TIME_WINDOW, choices=["24hours", "last3days", "last7days"], help="Time window")
    parser.add_argument("--no-llm", action="store_true", help="Skip LLM tiering; use hard filter + keyword fallback only")
    parser.add_argument(
        "--alert",
        action="store_true",
        help="Automation mode: 7-day watchlist + write output/syncareer/ inbox and run snapshots",
    )
    args = parser.parse_args()
    time_window = args.time
    use_llm = not args.no_llm
    alert_mode = args.alert

    load_env_file(BASE_DIR / ".env")
    session = make_session()
    targets = load_target_companies()
    company_filters = board.load_company_filters()

    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    stamp = now.strftime("%Y-%m-%d_%H%M")

    # Phase 1: search
    id_to_summary, id_to_keywords, per_keyword_counts = run_search(session, time_window)
    total_found = len(id_to_summary)

    # Phase 2: dedup against the chosen store.
    if alert_mode:
        watchlist = prune_watchlist(load_watchlist(), now=now.astimezone(timezone.utc))
        known_ids = set(watchlist.keys())
    else:
        watchlist = {}
        seen_ids = load_seen_ids()
        known_ids = seen_ids
    new_ids = [jid for jid in id_to_summary if jid not in known_ids]

    # Phase 3 + 5: fetch details + enrich for new jobs only.
    raw_rows: List[Dict[str, str]] = []
    for jid in new_ids:
        detail = fetch_job_detail(session, jid, referer_url=SEARCH_BASE_URL)
        summary = id_to_summary[jid]
        if not detail:
            detail = summary
        row = normalize_job_row(summary, detail, id_to_keywords.get(jid, []), targets)
        raw_rows.append(row)
        time.sleep(DETAIL_SLEEP_SECONDS)

    # Phase 4: hard filters (always applied).
    kept_rows: List[Dict[str, str]] = []
    drop_reasons: Counter = Counter()
    for row in raw_rows:
        keep, reason = hard_filter(row, company_filters)
        if keep:
            kept_rows.append(row)
        else:
            drop_reasons[reason.split(":")[0]] += 1

    # Shared role/seniority scope and strict official reconciliation happen
    # before LLM calls. Suppressed official duplicates remain in kept_rows and
    # the watchlist, but do not consume scoring calls or appear in alerts.
    first_seen_iso = now.astimezone(timezone.utc).isoformat()
    scoped_rows: List[Dict[str, str]] = []
    for row in kept_rows:
        row["first_seen"] = first_seen_iso
        if coverage_reconcile.syncareer_job_in_scope(row):
            scoped_rows.append(row)
        else:
            drop_reasons["exclude_role_seniority_prefilter"] += 1
    kept_rows = scoped_rows
    coverage_reconcile.annotate_jobs(kept_rows, "syncareer")
    hidden_external_count = 0
    for row in kept_rows:
        if apply_external_company_policy(row, company_filters):
            hidden_external_count += 1
    scoring_rows = [row for row in kept_rows if not row.get("suppress_alert")]

    # Phase 6: shared 0-100 scoring always runs. --no-llm selects the Board's
    # conservative rule fallback rather than leaving Score/Tier blank.
    historical_to_score: List[Dict[str, Any]] = []
    if alert_mode:
        cutoff = now.astimezone(timezone.utc) - timedelta(days=INBOX_DAYS)
        for entry in watchlist.values():
            if str(entry.get("kept") or "").lower() not in {"yes", "true", "1"}:
                continue
            if entry.get("match_score") not in (None, "") and entry.get("tier") in {"A", "B", "C"}:
                continue
            ref = _entry_age_ref(entry)
            if ref is not None and ref < cutoff:
                continue
            if not coverage_reconcile.syncareer_job_in_scope(entry):
                entry["kept"] = "no"
                entry["filter_status"] = "dropped"
                entry["drop_reason"] = "exclude_role_seniority_prefilter"
                entry["suppress_alert"] = True
                continue
            if apply_external_company_policy(entry, company_filters):
                continue
            historical = dict(entry)
            historical.setdefault("posting_date", historical.get("posted_date", ""))
            historical.setdefault("job_url", historical.get("url", ""))
            historical_to_score.append(historical)

    score_input = scoring_rows + historical_to_score
    decisions, score_counts, llm_errors, shared_screen_method = assign_shared_scores(
        score_input, watchlist, use_llm=use_llm
    )
    enriched_rows: List[Dict[str, Any]] = []
    for row in scoring_rows:
        enriched = dict(row)
        enriched.update(decisions.get(str(row.get("job_id")), {}))
        enriched_rows.append(enriched)
    tier_a_rows = [row for row in enriched_rows if row.get("tier") == "A"]
    tier_b_rows = [row for row in enriched_rows if row.get("tier") == "B"]
    tier_c_rows = [row for row in enriched_rows if row.get("tier") == "C"]
    for group in (tier_a_rows, tier_b_rows, tier_c_rows):
        group.sort(
            key=lambda row: (
                -float(row.get("match_score") or 0),
                0 if row.get("target_company") == "yes" else 1,
            )
        )

    # Persist scores on the daily rows as well as the rolling watchlist.
    by_job_id = {str(row.get("job_id")): row for row in enriched_rows}
    kept_rows = [by_job_id.get(str(row.get("job_id")), row) for row in kept_rows]

    # Phase 7: write daily outputs.
    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    jobs_csv = DAILY_DIR / f"{today}_jobs.csv"
    write_csv(jobs_csv, kept_rows, RAW_FIELDS)
    write_csv(DAILY_DIR / f"{today}_tier_a.csv", tier_a_rows, TIER_FIELDS)
    write_csv(DAILY_DIR / f"{today}_tier_b.csv", tier_b_rows, TIER_FIELDS)

    # Only actionable A/B jobs appear in alerts; C remains in the internal store.
    alert_rows = tier_a_rows + tier_b_rows

    # Report
    lines: List[str] = []
    lines.append(f"# Daily Job Report - {today}")
    lines.append("")
    lines.append(f"- Run time (UTC): {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"- Mode: {'alert (rolling 7d watchlist)' if alert_mode else 'standard (seen_ids)'}")
    lines.append(f"- Time window: {time_window}")
    lines.append(f"- Shared 0-100 matching: {'LLM + cache/rule fallback' if use_llm else 'rule fallback'}")
    lines.append(f"- Keywords: {', '.join(SEARCH_KEYWORDS)}")
    lines.append(f"- Total jobs found (deduped across keywords): {total_found}")
    lines.append(f"- Already-known (skipped): {total_found - len(new_ids)}")
    lines.append(f"- New jobs this run: {len(new_ids)}")
    lines.append(f"- Passed shared hard + role/seniority filter: {len(kept_rows)}")
    lines.append(f"- Amazon/Apple hidden externally: {hidden_external_count}")
    lines.append(f"- Coverage duplicates/hidden suppressed: {len(kept_rows) - len(scoring_rows)}")
    lines.append(f"- New alert candidates before tiering: {len(scoring_rows)}")
    lines.append(f"- Historical rows backfilled: {len(historical_to_score)}")
    lines.append(f"- Tier A (new): {len(tier_a_rows)}")
    lines.append(f"- Tier B (new): {len(tier_b_rows)}")
    lines.append(f"- Tier C/store-only (new): {len(tier_c_rows)}")
    lines.append(
        f"- Screening: {shared_screen_method}; LLM={score_counts.get('llm', 0)}, "
        f"cache={score_counts.get('reused', 0)}, rules={score_counts.get('rule', 0)}, "
        f"API requests={score_counts.get('api_requests', 0)}"
    )
    lines.append("")
    lines.append("## Per-keyword counts (this run, pre-dedup)")
    for kw in SEARCH_KEYWORDS:
        lines.append(f"- {kw}: {per_keyword_counts.get(kw, 0)}")
    lines.append("")
    lines.append("## Hard-filter drops")
    if drop_reasons:
        for reason, count in drop_reasons.most_common():
            lines.append(f"- {reason}: {count}")
    else:
        lines.append("- none")
    lines.append("")
    if llm_errors:
        lines.append("## LLM errors (not silently swallowed)")
        for err in llm_errors[:30]:
            lines.append(f"- {err}")
        lines.append("")
    (DAILY_DIR / f"{today}_report.md").write_text("\n".join(lines), encoding="utf-8")
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    (RUNS_DIR / f"{stamp}_stats.json").write_text(
        json.dumps(
            {
                "run_at": datetime.now(timezone.utc).isoformat(),
                "llm": llm_usage,
                "screening": dict(method_counts),
                "jobs_scored": len(scoring_rows),
                "tier_1": len(tier1_rows),
                "tier_2": len(tier2_rows),
            },
            indent=2,
            ensure_ascii=False,
        ) + "\n",
        encoding="utf-8",
    )

    # Alert-mode outputs + rolling watchlist update.
    alert_paths: Dict[str, Path] = {}
    if alert_mode:
        kept_ids = {row["job_id"] for row in kept_rows}
        for row in kept_rows:
            watchlist[row["job_id"]] = {
                "job_id": row["job_id"],
                "title": row.get("title", ""),
                "company": row.get("company", ""),
                "location": row.get("location", ""),
                "posted_date": row.get("posting_date", ""),
                "posting_date": row.get("posting_date", ""),
                "url": row.get("job_url", ""),
                "job_url": row.get("job_url", ""),
                "sponsorship": row.get("sponsorship", ""),
                "target_company": row.get("target_company", ""),
                "target_company_match": row.get("target_company_match", ""),
                "has_grad_req": row.get("has_grad_req", ""),
                "matched_keywords": row.get("matched_keywords", ""),
                "salary": row.get("salary", ""),
                "description": row.get("description", ""),
                "requirements": row.get("requirements", ""),
                "snippet": row.get("snippet", ""),
                "kept": "yes",
                "first_seen": first_seen_iso,
                "coverage_status": row.get("coverage_status", ""),
                "canonical_source": row.get("canonical_source", ""),
                "canonical_job_key": row.get("canonical_job_key", ""),
                "duplicate_of": row.get("duplicate_of", ""),
                "official_snapshot_at": row.get("official_snapshot_at", ""),
                "source_snapshot_at": row.get("source_snapshot_at", ""),
                "suppress_alert": bool(row.get("suppress_alert")),
                "filter_status": row.get("filter_status", "kept"),
                "drop_reason": row.get("drop_reason", ""),
                "company_flag": row.get("company_flag", ""),
                "deprioritized": bool(row.get("deprioritized")),
                "preferred": bool(row.get("preferred")),
                "staffing_firm": bool(row.get("staffing_firm")),
            }
        for job_id, decision in decisions.items():
            if job_id in watchlist:
                watchlist[job_id].update(decision)
        for row in raw_rows:
            if row["job_id"] in kept_ids:
                continue
            canonical_key = coverage_reconcile.canonical_job_key(
                coverage_reconcile.normalize_syncareer_job(row)
            )
            watchlist[row["job_id"]] = {
                "job_id": row["job_id"],
                "title": row.get("title", ""),
                "company": row.get("company", ""),
                "location": row.get("location", ""),
                "posted_date": row.get("posting_date", ""),
                "url": row.get("job_url", ""),
                "kept": "no",
                "first_seen": first_seen_iso,
                "coverage_status": "out_of_scope",
                "canonical_source": "syncareer",
                "canonical_job_key": canonical_key,
                "duplicate_of": "",
                "source_snapshot_at": first_seen_iso,
                "review_status": "unreviewed",
                "source_pipeline": "syncareer",
            }
        watchlist = prune_watchlist(watchlist, now=now.astimezone(timezone.utc))

        # Reconcile historical in-scope entries too, so validation changes take
        # effect without waiting for a job to be rediscovered.
        historical_rows: List[Dict[str, Any]] = []
        for entry in watchlist.values():
            if str(entry.get("kept") or "").lower() in {"yes", "true", "1"} and coverage_reconcile.syncareer_job_in_scope(entry):
                historical_rows.append(entry)
        coverage_reconcile.annotate_jobs(historical_rows, "syncareer")
        for entry in historical_rows:
            apply_external_company_policy(entry, company_filters)
        save_watchlist(watchlist)

        inbox_rows = [
            _watchlist_to_alert_row(e)
            for e in inbox_entries(watchlist, now=now.astimezone(timezone.utc))
            if not e.get("suppress_alert") and e.get("tier") in {"A", "B"}
        ]
        write_syncareer_inbox(inbox_rows, stamp, with_tiers=True)
        if alert_rows:
            alert_paths = write_alert_outputs(alert_rows, stamp, with_tiers=True)
            alert_history.append_event(
                ALERT_HISTORY_PATH,
                pipeline="syncareer",
                stamp=stamp,
                jobs=alert_rows,
                event_kind="new_matching",
            )
        else:
            # Still refresh issue_body so GHA has a path even when 0 new.
            SYNCAREER_DIR.mkdir(parents=True, exist_ok=True)
            body = SYNCAREER_DIR / "issue_body.md"
            body.write_text(
                f"Syncareer alert — {stamp}\n\n0 new jobs this run.\n\n"
                f"Open `output/syncareer/inbox.md` for the last {INBOX_DAYS} days.\n",
                encoding="utf-8",
            )
            alert_paths["issue_body"] = body
        emit_github_output(
            {
                "new_count": str(len(alert_rows)),
                "inbox_count": str(len(inbox_rows)),
                "stamp": stamp,
                "issue_title": f"Syncareer alert {stamp} ({len(alert_rows)} new A/B)",
                "issue_body_path": str(alert_paths.get("issue_body", "")),
            }
        )
    else:
        seen_ids.update(id_to_summary.keys())
        save_seen_ids(seen_ids)

    # Console summary.
    print(f"Mode: {'alert' if alert_mode else 'standard'} | window: {time_window} | LLM: {'on' if use_llm else 'off'}")
    print(f"Total found: {total_found} | new: {len(new_ids)} | kept (store): {len(kept_rows)} | new score candidates: {len(scoring_rows)}")
    print(f"Tier A: {len(tier_a_rows)} | Tier B: {len(tier_b_rows)} | Tier C: {len(tier_c_rows)}")
    print(f"Screening: {shared_screen_method}; LLM={score_counts.get('llm', 0)}, cache={score_counts.get('reused', 0)}, rules={score_counts.get('rule', 0)}")
    print(f"Hidden external companies: {hidden_external_count} new; historical policy refreshed")
    if llm_errors:
        print(f"LLM errors: {len(llm_errors)} (see report)")
    print(f"Wrote: {jobs_csv}")
    if alert_mode:
        print(f"Inbox: {SYNCAREER_DIR / 'inbox.csv'} ({len(inbox_rows)} jobs, last {INBOX_DAYS}d)")
        if alert_paths.get("csv"):
            print(f"This-run CSV: {alert_paths['csv']}")
            print(f"Issue body: {alert_paths['issue_body']}")
        else:
            print("No new jobs this run; inbox refreshed.")


if __name__ == "__main__":
    run()
