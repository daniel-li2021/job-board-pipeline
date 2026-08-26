#!/usr/bin/env python3
"""Deep Syncareer scrape with incremental crawl + full re-screen."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlencode, urlparse, parse_qsl

import requests
from bs4 import BeautifulSoup


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
RAW_CSV = OUTPUT_DIR / "syncareer_raw_jobs.csv"
SCREENED_CSV = OUTPUT_DIR / "syncareer_screened_jobs.csv"
REPORT_MD = OUTPUT_DIR / "syncareer_report.md"
DROPPED_SAMPLE_CSV = OUTPUT_DIR / "stage1_dropped_sample.csv"
COMPANY_LINKS_JSON = BASE_DIR / "source" / "company_links.json"
SWE_RESUME_PATH = BASE_DIR / "source" / "swe-resume.txt"
AI_RESUME_PATH = BASE_DIR / "source" / "aie-resume.txt"

DETAIL_API_URL = "https://syncareer.com/api/job/detail"
REQUEST_TIMEOUT = 30
PAGE_SLEEP_SECONDS = 0.3
DETAIL_SLEEP_SECONDS = 0.15
MAX_PAGE_GUARD = 220

RAW_FIELDS = [
    "job_id",
    "title",
    "company",
    "location",
    "posting_date",
    "job_url",
    "description",
    "requirements",
    "tags",
    "category",
    "snippet",
    "source",
]
SCREEN_FIELDS = RAW_FIELDS + ["screen_keep", "screen_reason", "screen_confidence", "screen_method"]


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


def build_jobs_url(base_url: str, loc: str, time_window: str, page_num: int = 1) -> str:
    parsed = urlparse(base_url)
    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    query["loc"] = loc
    query["time"] = time_window
    query["page"] = str(page_num)
    return parsed._replace(query=urlencode(query)).geturl()


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


def extract_search_result(html: str) -> Optional[Dict[str, Any]]:
    payload_arr = extract_payload_array(html)
    if not payload_arr:
        return None
    root = NuxtPayloadDecoder(payload_arr).decode_ref(0)
    if not isinstance(root, dict):
        return None
    data_block = root.get("data") or {}
    if not isinstance(data_block, dict):
        return None
    for key in data_block.keys():
        if str(key).endswith("-search-result"):
            result = data_block.get(key)
            if isinstance(result, dict):
                return result
    return None


def probe_window_count(
    session: requests.Session,
    base_url: str,
    loc: str,
    time_window: str,
    threshold: int = 100,
    max_probe_pages: int = 6,
) -> Optional[int]:
    """Count unique jobs quickly to decide whether 7d is under threshold."""
    seen_ids: set[str] = set()
    for page in range(1, max_probe_pages + 1):
        page_url = build_jobs_url(base_url, loc, time_window, page_num=page)
        try:
            resp = session.get(page_url, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
        except Exception:  # noqa: BLE001
            return None
        sr = extract_search_result(resp.text)
        if not sr:
            return None
        page_list = sr.get("list") or []
        if not isinstance(page_list, list) or not page_list:
            break
        before = len(seen_ids)
        for item in page_list:
            jid = str(item.get("id", "")).strip()
            if jid:
                seen_ids.add(jid)
        if len(seen_ids) >= threshold:
            return len(seen_ids)
        if len(seen_ids) == before:
            break
    return len(seen_ids)


def parse_location(loc: Dict[str, Any]) -> str:
    city = ((loc.get("city") or {}).get("eng") or "").strip()
    province = ((loc.get("province") or {}).get("eng") or "").strip()
    country = ((loc.get("country") or {}).get("eng") or "").strip()
    parts = [p for p in [city, province, country] if p]
    return ", ".join(parts)


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


def scrape_company_pages(session: requests.Session, jobs_url: str) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    all_summaries: List[Dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_page_signatures: set[Tuple[str, ...]] = set()
    attempted_pages: List[str] = []
    stop_reason = "unknown"
    page = 1

    while page <= MAX_PAGE_GUARD:
        page_url = build_jobs_url(jobs_url, "", "", page_num=page)
        # build_jobs_url expects params; reuse by directly setting page on existing query.
        parsed = urlparse(jobs_url)
        query = dict(parse_qsl(parsed.query, keep_blank_values=True))
        query["page"] = str(page)
        page_url = parsed._replace(query=urlencode(query)).geturl()
        attempted_pages.append(page_url)
        try:
            resp = session.get(page_url, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            stop_reason = f"request_failed_page_{page}: {exc}"
            break

        search_result = extract_search_result(resp.text)
        if not search_result:
            stop_reason = f"search_result_missing_page_{page}"
            break
        page_list = search_result.get("list") or []
        if not isinstance(page_list, list):
            stop_reason = f"search_list_invalid_page_{page}"
            break
        if not page_list:
            stop_reason = f"no_jobs_page_{page}"
            break

        page_ids = [str(item.get("id", "")) for item in page_list if item.get("id")]
        signature = tuple(sorted(page_ids))
        if signature in seen_page_signatures:
            stop_reason = f"repeated_page_signature_page_{page}"
            break
        seen_page_signatures.add(signature)

        new_count = 0
        for item in page_list:
            jid = str(item.get("id", ""))
            if not jid or jid in seen_ids:
                continue
            seen_ids.add(jid)
            all_summaries.append(item)
            new_count += 1
        if new_count == 0:
            stop_reason = f"no_new_jobs_page_{page}"
            break

        page += 1
        time.sleep(PAGE_SLEEP_SECONDS)
    else:
        stop_reason = f"max_page_guard_{MAX_PAGE_GUARD}"

    return all_summaries, {
        "attempted_pages": attempted_pages,
        "stop_reason": stop_reason,
        "pagination_complete": stop_reason.startswith(
            ("no_jobs_page_", "repeated_page_signature_page_", "no_new_jobs_page_")
        ),
        "summary_count": len(all_summaries),
    }


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


def normalize_raw_row(
    summary: Dict[str, Any],
    detail: Dict[str, Any],
    company_name: str,
    source_tag: str,
) -> Dict[str, str]:
    location_info = detail.get("location") or summary.get("location") or {}
    location = parse_location(location_info) if isinstance(location_info, dict) else ""
    title = str(detail.get("title") or summary.get("title") or "").strip()
    posting_date = epoch_to_date(detail.get("publishAt") or summary.get("publishAt"))
    job_url = str(detail.get("url") or summary.get("url") or "").strip()
    desc_text = html_to_text(str(detail.get("desc") or ""))
    desc_main, requirements = split_requirements(desc_text)
    supports = detail.get("supports") if isinstance(detail.get("supports"), list) else []
    industries = detail.get("industries") if isinstance(detail.get("industries"), list) else []
    tags = [x for x in [detail.get("jobType"), detail.get("degree"), detail.get("experience"), detail.get("remoteType")] if x]
    tags.extend([str(s) for s in supports if s])
    tags.extend([str(i) for i in industries if i])
    return {
        "job_id": str(detail.get("id") or summary.get("id") or ""),
        "title": title,
        "company": company_name,
        "location": location,
        "posting_date": posting_date,
        "job_url": job_url,
        "description": desc_main,
        "requirements": requirements,
        "tags": ", ".join(dict.fromkeys(tags)),
        "category": str(detail.get("jobType") or "").strip(),
        "snippet": (desc_main or requirements or title)[:400],
        "source": source_tag,
    }


def has_word(text: str, phrase: str) -> bool:
    """Word-boundary match so 'sales' does not match 'Salesforce'."""
    return re.search(r"\b" + re.escape(phrase) + r"\b", text) is not None


# Business / non-technical role exclusions. Applied to title + category only,
# never to company name or free-form description text.
BUSINESS_ROLE_EXCLUSIONS = [
    "director",
    "recruiter",
    "marketing",
    "legal",
    "finance",
    "account executive",
    "customer success",
    "warehouse",
    "human resources",
    "sales",
    "operations",
]

RESTRICTION_PHRASES = ["security clearance", "u.s. person", "us person"]


def role_text(row: Dict[str, str]) -> str:
    return f"{row.get('title', '')} {row.get('category', '')}".lower()


def conservative_filter(row: Dict[str, str]) -> Tuple[bool, str]:
    rtext = role_text(row)
    content = f"{row.get('snippet', '')} {row.get('description', '')[:800]} {row.get('requirements', '')[:800]}".lower()

    bucket = classify_location_bucket(row.get("location", ""))
    if bucket == "non_us":
        return False, "conservative_exclude_non_us_location"

    # Role exclusions only on title/category, using word boundaries.
    for kw in BUSINESS_ROLE_EXCLUSIONS:
        if has_word(rtext, kw):
            return False, f"conservative_exclude_role:{kw}"

    # Hard restrictions may appear in content.
    for phrase in RESTRICTION_PHRASES:
        if has_word(content, phrase):
            return False, "conservative_exclude_restriction"

    # Unknown locations are kept for manual review, never silently dropped.
    if bucket == "unknown":
        return True, "conservative_keep_unknown_location_review"
    return True, "conservative_keep"


def drop_list_logic(row: Dict[str, str]) -> Tuple[bool, str]:
    rtext = role_text(row)
    include_text = (
        f"{row.get('title', '')} {row.get('snippet', '')} "
        f"{row.get('description', '')[:900]} {row.get('requirements', '')[:900]}"
    ).lower()
    include_hits = [
        "software engineer",
        "swe",
        "sde",
        "backend",
        "full stack",
        "platform",
        "infrastructure",
        "cloud",
        "data engineer",
        "machine learning",
        "ml engineer",
        "ai engineer",
        "llm",
        "applied ai",
        "research engineer",
        "new grad",
        "early career",
        "systems engineer",
        "solutions engineer",
        "customer engineer",
    ]
    # Seniority/role exclusions only on title/category with word boundaries.
    exclude_roles = [
        "senior manager",
        "director",
        "principal",
        "staff",
        "recruiter",
        "marketing",
        "legal",
        "finance",
        "sales",
        "warehouse",
    ]
    for kw in exclude_roles:
        if has_word(rtext, kw):
            return False, f"drop_list_exclude:{kw}"
    for phrase in RESTRICTION_PHRASES:
        if has_word(include_text, phrase):
            return False, "drop_list_exclude_restriction"
    if any(x in include_text for x in include_hits):
        return True, "drop_list_include"
    return False, "drop_list_no_signal"


def llm_screen_rows(
    rows: List[Dict[str, str]],
    swe_resume: str,
    ai_resume: str,
) -> Tuple[Dict[str, Dict[str, Any]], List[str]]:
    """Return (decisions, errors). Errors are surfaced instead of swallowed."""
    decisions: Dict[str, Dict[str, Any]] = {}
    errors: List[str] = []
    openai_key = (os.environ.get("OPENAI_API_KEY") or "").strip()
    groq_key = (os.environ.get("GROQ_API_KEY") or "").strip()
    if not openai_key and not groq_key:
        errors.append("no_api_key_configured")
        return decisions, errors

    providers: List[Dict[str, str]] = []
    if openai_key:
        providers.append({"name": "openai", "endpoint": "https://api.openai.com/v1/chat/completions", "api_key": openai_key, "model": "gpt-4o-mini"})
    if groq_key:
        providers.append({"name": "groq", "endpoint": "https://api.groq.com/openai/v1/chat/completions", "api_key": groq_key, "model": "llama-3.1-8b-instant"})

    # Keep per-request payloads small enough to avoid provider 413 / timeout.
    chunk_size = 12
    for start in range(0, len(rows), chunk_size):
        chunk = rows[start : start + chunk_size]
        chunk_idx = start // chunk_size
        payload_jobs = [
            {
                "job_id": r["job_id"],
                "title": r["title"],
                "company": r["company"],
                "location": r["location"],
                "snippet": r["snippet"][:400],
                "description_preview": r["description"][:700],
                "requirements_preview": (r.get("requirements") or "")[:700],
                "full_text_preview": full_text_for_stats(r)[:1600],
            }
            for r in chunk
        ]
        prompt_obj = {
            "task": "Classify job relevance for SWE/AI-engineer target using resume context.",
            "include_guidance": "SWE/SDE/backend/full-stack/platform/infrastructure/data engineer/ML/AI/LLM/applied AI/new grad/early career are relevant.",
            "exclude_guidance": "Exclude obvious non-technical roles and leadership-heavy roles where irrelevant.",
            "resume_guidance": "Use SWE resume for SWE/backend/full-stack/platform/infrastructure/cloud/data/general engineering. Use AI/FDE resume for AI/ML/LLM/Applied AI/Agent/RAG.",
            "swe_resume": swe_resume[:3500],
            "ai_fde_resume": ai_resume[:3500],
            "return_schema": {"decisions": [{"job_id": "string", "keep": "boolean", "reason": "short string", "confidence": "0-1 float"}]},
            "jobs": payload_jobs,
        }
        provider_success = False
        chunk_errors: List[str] = []
        for provider in providers:
            try:
                resp = requests.post(
                    provider["endpoint"],
                    headers={"Authorization": f"Bearer {provider['api_key']}", "Content-Type": "application/json"},
                    json={
                        "model": provider["model"],
                        "temperature": 0,
                        "response_format": {"type": "json_object"},
                        "messages": [
                            {"role": "system", "content": "You are a careful recruiting screener."},
                            {"role": "user", "content": json.dumps(prompt_obj)},
                        ],
                    },
                    timeout=90,
                )
                resp.raise_for_status()
                parsed = json.loads(resp.json()["choices"][0]["message"]["content"])
                for item in parsed.get("decisions", []):
                    job_id = str(item.get("job_id", "")).strip()
                    if not job_id:
                        continue
                    decisions[job_id] = {
                        "keep": bool(item.get("keep", False)),
                        "reason": str(item.get("reason", f"{provider['name']}_llm"))[:180],
                        "confidence": float(item.get("confidence", 0.0)),
                    }
                provider_success = True
                break
            except Exception as exc:  # noqa: BLE001
                chunk_errors.append(f"{provider['name']}:{type(exc).__name__}:{str(exc)[:120]}")
                continue
        if provider_success:
            time.sleep(0.25)
        else:
            errors.append(f"chunk_{chunk_idx}_failed[{len(chunk)} jobs]: " + " | ".join(chunk_errors))
    return decisions, errors


def write_csv(path: Path, rows: List[Dict[str, Any]], fields: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def load_company_registry(path: Path) -> Tuple[List[Dict[str, Any]], str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    companies = payload.get("companies", [])
    default_loc = payload.get("default_loc", "United States")
    return companies, default_loc


def load_existing_raw() -> List[Dict[str, str]]:
    if not RAW_CSV.exists():
        return []
    with RAW_CSV.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def dedupe_rows(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    seen: set[Tuple[str, str, str, str]] = set()
    out: List[Dict[str, str]] = []
    for row in rows:
        key = (
            row.get("job_id", "").strip(),
            row.get("company", "").strip().lower(),
            row.get("title", "").strip().lower(),
            row.get("location", "").strip().lower(),
        )
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def infer_window_from_rows(rows: List[Dict[str, str]]) -> str:
    sources = " ".join((r.get("source", "") or "").lower() for r in rows)
    if "last30days" in sources:
        return "last30days"
    if "last7days" in sources:
        return "last7days"
    return "unknown"


def normalize_location_key(location: str) -> str:
    value = re.sub(r"\s+", " ", (location or "").strip())
    return value if value else "(empty)"


def classify_location_bucket(location: str) -> str:
    loc = (location or "").strip().lower()
    if not loc:
        return "unknown"
    us_tokens = [
        "united states",
        ", usa",
        ", us",
        "u.s.",
    ]
    if any(token in loc for token in us_tokens):
        return "us"
    # Common non-US markers seen in Syncareer locations.
    non_us_tokens = [
        "canada",
        "india",
        "china",
        "japan",
        "singapore",
        "ireland",
        "uk",
        "united kingdom",
        "germany",
        "france",
        "spain",
        "italy",
        "netherlands",
        "sweden",
        "switzerland",
        "australia",
        "new zealand",
        "mexico",
        "brazil",
        "argentina",
        "poland",
    ]
    if any(token in loc for token in non_us_tokens):
        return "non_us"
    # If a location has commas but no country token, treat as unknown instead of assuming US.
    return "unknown"


def full_text_for_stats(row: Dict[str, str]) -> str:
    description = (row.get("description") or "").strip()
    requirements = (row.get("requirements") or "").strip()
    if description and requirements:
        return f"{description}\n{requirements}"
    return description or requirements


def calc_detail_quality_stats(rows: List[Dict[str, str]]) -> Dict[str, Any]:
    desc_nonempty = 0
    req_nonempty = 0
    full_nonempty = 0
    full_total_len = 0
    for row in rows:
        description = (row.get("description") or "").strip()
        requirements = (row.get("requirements") or "").strip()
        full_text = full_text_for_stats(row)
        if description:
            desc_nonempty += 1
        if requirements:
            req_nonempty += 1
        if full_text:
            full_nonempty += 1
            full_total_len += len(full_text)
    avg_full_len = (full_total_len / full_nonempty) if full_nonempty else 0.0
    return {
        "description_nonempty_count": desc_nonempty,
        "requirements_nonempty_count": req_nonempty,
        "full_text_nonempty_count": full_nonempty,
        "avg_full_text_length": avg_full_len,
    }


def calc_location_stats(rows: List[Dict[str, str]]) -> Dict[str, Any]:
    us_count = 0
    non_us_count = 0
    unknown_count = 0
    dist: Dict[str, int] = defaultdict(int)
    for row in rows:
        loc = normalize_location_key(row.get("location", ""))
        dist[loc] += 1
        bucket = classify_location_bucket(row.get("location", ""))
        if bucket == "us":
            us_count += 1
        elif bucket == "non_us":
            non_us_count += 1
        else:
            unknown_count += 1
    top_locations = sorted(dist.items(), key=lambda x: (-x[1], x[0]))[:12]
    top_locations_text = "; ".join([f"{name} ({count})" for name, count in top_locations])
    return {
        "us_count": us_count,
        "non_us_count": non_us_count,
        "unknown_count": unknown_count,
        "top_locations_text": top_locations_text,
    }


def run() -> None:
    load_env_file(BASE_DIR / ".env")
    session = make_session()
    swe_resume = SWE_RESUME_PATH.read_text(encoding="utf-8") if SWE_RESUME_PATH.exists() else ""
    ai_resume = AI_RESUME_PATH.read_text(encoding="utf-8") if AI_RESUME_PATH.exists() else ""
    companies, default_loc = load_company_registry(COMPANY_LINKS_JSON)
    existing_rows = dedupe_rows(load_existing_raw())
    existing_by_company: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in existing_rows:
        existing_by_company[row.get("company", "").strip().lower()].append(row)

    all_raw_rows: List[Dict[str, str]] = list(existing_rows)
    company_stats: Dict[str, Dict[str, Any]] = {}

    # If raw already exists, rerun screening/report only (no recrawl).
    if not existing_rows:
        for cfg in companies:
            company_name = str(cfg.get("name", "")).strip()
            company_key = str(cfg.get("key", company_name.lower())).strip()
            base_url = str(cfg.get("base_url", "")).strip()
            if not company_name or not base_url:
                continue
            expected = cfg.get("expected_rough_count", 0) or 0

            total_7d = probe_window_count(session, base_url, default_loc, "last7days", threshold=100)
            window_used = "last7days"
            window_reason = "default_7d"
            if isinstance(total_7d, int) and total_7d < 100:
                window_used = "last30days"
                window_reason = f"7d_total_{total_7d}_lt_100"
            jobs_url = build_jobs_url(base_url, default_loc, window_used, page_num=1)
            summaries, meta = scrape_company_pages(session, jobs_url)

            raw_rows_company: List[Dict[str, str]] = []
            detail_success = 0
            for summary in summaries:
                job_id = str(summary.get("id", "")).strip()
                if not job_id:
                    continue
                detail = fetch_job_detail(session, job_id, referer_url=jobs_url)
                if not detail:
                    detail = summary
                else:
                    detail_success += 1
                source_tag = f"syncareer_{window_used}"
                row = normalize_raw_row(summary, detail, company_name, source_tag=source_tag)
                raw_rows_company.append(row)
                time.sleep(DETAIL_SLEEP_SECONDS)

            all_raw_rows.extend(raw_rows_company)
            company_stats[company_name] = {
                "expected_rough_count": expected,
                "raw_count": len(raw_rows_company),
                "detail_success_count": detail_success,
                "pagination_complete": meta["pagination_complete"],
                "attempted_pages": len(meta["attempted_pages"]),
                "stop_reason": meta["stop_reason"],
                "window_used": window_used,
                "window_reason": window_reason,
                "data_source": "new_crawl",
                "key": company_key,
                "7d_total_probe": total_7d,
            }
    else:
        for cfg in companies:
            company_name = str(cfg.get("name", "")).strip()
            company_key = str(cfg.get("key", company_name.lower())).strip()
            expected = cfg.get("expected_rough_count", 0) or 0
            rows = existing_by_company.get(company_name.lower(), [])
            inferred_window = infer_window_from_rows(rows) if rows else "unknown"
            company_stats[company_name] = {
                "expected_rough_count": expected,
                "raw_count": len(rows),
                "detail_success_count": "reused_previous_metadata",
                "pagination_complete": "reused_previous_metadata",
                "attempted_pages": "reused_previous_metadata",
                "stop_reason": "reused_existing_raw_screening_only",
                "window_used": inferred_window,
                "window_reason": "inferred_from_existing_raw",
                "data_source": "reused_existing",
                "key": company_key,
            }

    all_raw_rows = dedupe_rows(all_raw_rows)
    write_csv(RAW_CSV, all_raw_rows, RAW_FIELDS)

    # Full re-screen on merged raw.
    rows_by_company: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in all_raw_rows:
        rows_by_company[row.get("company", "")].append(row)

    screened_rows: List[Dict[str, str]] = []
    dropped_stage1_rows: List[Dict[str, str]] = []
    screened_count_by_company: Dict[str, int] = defaultdict(int)
    llm_used_by_company: Dict[str, bool] = {}
    post_heuristic_count_by_company: Dict[str, int] = {}
    detail_quality_by_company: Dict[str, Dict[str, Any]] = {}
    location_stats_by_company: Dict[str, Dict[str, Any]] = {}
    llm_decision_count_by_company: Dict[str, int] = defaultdict(int)
    fallback_count_by_company: Dict[str, int] = defaultdict(int)
    llm_errors_by_company: Dict[str, List[str]] = defaultdict(list)

    for company, rows in rows_by_company.items():
        detail_quality_by_company[company] = calc_detail_quality_stats(rows)
        location_stats_by_company[company] = calc_location_stats(rows)
        stage1_rows: List[Dict[str, str]] = []
        for row in rows:
            keep1, reason1 = conservative_filter(row)
            if not keep1:
                dropped_stage1_rows.append(
                    {
                        "company": row.get("company", ""),
                        "job_id": row.get("job_id", ""),
                        "title": row.get("title", ""),
                        "location": row.get("location", ""),
                        "posting_date": row.get("posting_date", ""),
                        "job_url": row.get("job_url", ""),
                        "category": row.get("category", ""),
                        "drop_reason": reason1,
                    }
                )
                continue
            r = dict(row)
            r["_stage1_reason"] = reason1
            stage1_rows.append(r)
        post_heuristic_count_by_company[company] = len(stage1_rows)

        if len(stage1_rows) > 50:
            llm_decisions, llm_errors = llm_screen_rows(stage1_rows, swe_resume=swe_resume, ai_resume=ai_resume)
            llm_used_by_company[company] = True
            if llm_errors:
                llm_errors_by_company[company].extend(llm_errors)
            for row in stage1_rows:
                d = llm_decisions.get(row["job_id"])
                if d is None:
                    keep2, reason2 = drop_list_logic(row)
                    d = {"keep": keep2, "reason": f"fallback_drop_list:{reason2}", "confidence": 0.55}
                    method = "fallback_drop_list"
                    fallback_count_by_company[company] += 1
                else:
                    method = "llm_decision"
                    llm_decision_count_by_company[company] += 1
                out = dict(row)
                out["screen_keep"] = "yes" if d["keep"] else "no"
                out["screen_reason"] = str(d["reason"])
                out["screen_confidence"] = f"{float(d['confidence']):.2f}"
                out["screen_method"] = method
                if d["keep"]:
                    screened_rows.append(out)
                    screened_count_by_company[company] += 1
        else:
            llm_used_by_company[company] = False
            for row in stage1_rows:
                keep2, reason2 = drop_list_logic(row)
                out = dict(row)
                out["screen_keep"] = "yes" if keep2 else "no"
                out["screen_reason"] = f"drop_list:{reason2}"
                out["screen_confidence"] = "0.60"
                out["screen_method"] = "drop_list_logic"
                if keep2:
                    screened_rows.append(out)
                    screened_count_by_company[company] += 1

    write_csv(SCREENED_CSV, screened_rows, SCREEN_FIELDS)
    # Keep an auditable sample of stage1 drops (20 per company).
    dropped_by_company: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in dropped_stage1_rows:
        dropped_by_company[row.get("company", "")].append(row)
    dropped_sample_rows: List[Dict[str, str]] = []
    for company_name in sorted(dropped_by_company.keys()):
        dropped_sample_rows.extend(dropped_by_company[company_name][:20])
    write_csv(
        DROPPED_SAMPLE_CSV,
        dropped_sample_rows,
        ["company", "job_id", "title", "location", "posting_date", "job_url", "category", "drop_reason"],
    )

    lines: List[str] = []
    total_llm = sum(llm_decision_count_by_company.values())
    total_fallback = sum(fallback_count_by_company.values())
    companies_with_errors = sorted([c for c, e in llm_errors_by_company.items() if e])

    lines.append("# Syncareer Deep Scrape Report")
    lines.append("")
    lines.append(f"- Run time (UTC): {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"- Raw rows total: {len(all_raw_rows)}")
    lines.append(f"- Screened rows total: {len(screened_rows)}")
    lines.append(f"- LLM decision count (total): {total_llm}")
    lines.append(f"- Fallback (drop_list) count within LLM path (total): {total_fallback}")
    lines.append(f"- Companies with LLM errors: {', '.join(companies_with_errors) if companies_with_errors else 'none'}")
    lines.append("")
    if companies_with_errors:
        lines.append("## LLM Errors (not silently swallowed)")
        for company_name in companies_with_errors:
            lines.append(f"### {company_name}")
            for err in llm_errors_by_company[company_name][:20]:
                lines.append(f"- {err}")
            lines.append("")
    lines.append("## Company Counts")
    for cfg in companies:
        name = cfg["name"]
        stats = company_stats.get(name, {})
        raw_count = stats.get("raw_count", 0)
        expected = stats.get("expected_rough_count", 0)
        screened_count = screened_count_by_company.get(name, 0)
        ratio = (raw_count / expected) if expected else 0.0
        lines.append(f"### {name}")
        lines.append(f"- data_source: {stats.get('data_source', 'unknown')}")
        lines.append(f"- window_used: {stats.get('window_used', 'unknown')}")
        lines.append(f"- window_reason: {stats.get('window_reason', 'n/a')}")
        if "7d_total_probe" in stats:
            lines.append(f"- window_probe_7d_count: {stats.get('7d_total_probe')}")
        lines.append(f"- raw_count: {raw_count}")
        loc_stats = location_stats_by_company.get(name, {"us_count": 0, "non_us_count": 0, "unknown_count": 0, "top_locations_text": ""})
        lines.append(f"- us_count: {loc_stats.get('us_count', 0)}")
        lines.append(f"- non_us_count: {loc_stats.get('non_us_count', 0)}")
        lines.append(f"- unknown_location_count: {loc_stats.get('unknown_count', 0)}")
        lines.append(f"- location_distribution_top: {loc_stats.get('top_locations_text', '')}")
        quality_stats = detail_quality_by_company.get(
            name,
            {
                "description_nonempty_count": 0,
                "requirements_nonempty_count": 0,
                "full_text_nonempty_count": 0,
                "avg_full_text_length": 0.0,
            },
        )
        lines.append(f"- description_nonempty_count: {quality_stats.get('description_nonempty_count', 0)}")
        lines.append(f"- requirements_nonempty_count: {quality_stats.get('requirements_nonempty_count', 0)}")
        lines.append(f"- full_text_nonempty_count: {quality_stats.get('full_text_nonempty_count', 0)}")
        lines.append(f"- avg_full_text_length: {quality_stats.get('avg_full_text_length', 0.0):.1f}")
        lines.append(f"- stage1_count_after_conservative: {post_heuristic_count_by_company.get(name, 0)}")
        lines.append(f"- screened_count: {screened_count}")
        lines.append(f"- screening_path: {'llm_decision' if llm_used_by_company.get(name) else 'drop_list_logic'}")
        if llm_used_by_company.get(name):
            lines.append(f"- llm_decision_count: {llm_decision_count_by_company.get(name, 0)}")
            lines.append(f"- fallback_drop_list_count: {fallback_count_by_company.get(name, 0)}")
            lines.append(f"- llm_error_count: {len(llm_errors_by_company.get(name, []))}")
        lines.append(f"- expected_rough_count: {expected}")
        lines.append(f"- scraped_vs_expected_ratio: {ratio:.1%}")
        lines.append(f"- detail_success_count: {stats.get('detail_success_count', 'n/a')}")
        pagination_complete = stats.get("pagination_complete")
        if isinstance(pagination_complete, str):
            pagination_display = pagination_complete
        else:
            pagination_display = "yes" if pagination_complete else "no/unclear"
        lines.append(f"- pagination_complete: {pagination_display}")
        lines.append(f"- pagination_attempted_pages: {stats.get('attempted_pages', 0)}")
        lines.append(f"- pagination_stop_reason: {stats.get('stop_reason', 'n/a')}")
        if expected and raw_count < expected * 0.7:
            lines.append("- below_expected_flag: YES")
        else:
            lines.append("- below_expected_flag: no")
        lines.append("")

    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote raw CSV: {RAW_CSV}")
    print(f"Wrote screened CSV: {SCREENED_CSV}")
    print(f"Wrote stage1 dropped sample: {DROPPED_SAMPLE_CSV}")
    print(f"Wrote report: {REPORT_MD}")
    for cfg in companies:
        name = cfg["name"]
        stats = company_stats.get(name, {})
        print(
            f"{name}: source={stats.get('data_source', 'unknown')} "
            f"window={stats.get('window_used', 'unknown')} "
            f"raw={stats.get('raw_count', 0)} "
            f"screened={screened_count_by_company.get(name, 0)}"
        )


# ==========================================================================
# Snapshot mode: crawl a chosen subset of companies for a fresh time window
# into a dated folder, without touching the canonical syncareer_raw_jobs.csv.
# ==========================================================================
SNAPSHOT_SENIOR_RE = re.compile(
    r"\b(senior|sr\.?|lead|staff|principal|director|manager|vp|vice president|head of|distinguished|architect|fellow)\b",
    re.IGNORECASE,
)
SNAPSHOT_SENIOR_TAGS = ["senior", "principal", "staff", "director", "lead", "executive"]
SNAPSHOT_INCLUDE = [
    "software engineer", "software developer", "software development engineer",
    "swe", "sde", "backend", "back end", "back-end", "full stack", "full-stack",
    "frontend", "front end", "front-end", "platform engineer", "platform software",
    "infrastructure", "cloud engineer", "distributed systems", "systems engineer",
    "data engineer", "machine learning", "ml engineer", "ai engineer",
    "applied ai", "applied scientist", "applied science", "llm", "deep learning",
    "research engineer", "forward deployed", "devops", "site reliability", "sre",
    "new grad", "early career", "university graduate", "computer vision", "nlp",
    "generative ai", "gen ai", "genai", "agent", "rag", "developer productivity",
]


def posting_within_days(row: Dict[str, str], max_age_days: int, now: Optional[datetime] = None) -> bool:
    """Keep jobs whose posting_date is within max_age_days. Missing/unparseable dates are kept."""
    raw = (row.get("posting_date") or "").strip()
    if not raw:
        return True
    try:
        posted = datetime.strptime(raw[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        return True
    ref = now or datetime.now(timezone.utc)
    cutoff = (ref - timedelta(days=max_age_days)).date()
    return posted.date() >= cutoff


def snapshot_screen(row: Dict[str, str]) -> Tuple[bool, str]:
    """Two rules: (1) keep only SWE/AI-related roles, (2) drop Senior-level.

    Relevance is checked first so that non-technical roles (e.g. "Category
    Manager") are counted as drop_irrelevant, and drop_senior only reflects
    genuinely technical-but-too-senior roles (e.g. "Staff SWE").
    """
    title = row.get("title", "")
    text = (
        f"{title} {row.get('snippet', '')} "
        f"{row.get('description', '')[:900]} {row.get('requirements', '')[:900]}"
    ).lower()
    if not any(k in text for k in SNAPSHOT_INCLUDE):
        return False, "drop_irrelevant"
    if classify_location_bucket(row.get("location", "")) == "non_us":
        return False, "drop_non_us"
    tags = (row.get("tags", "") or "").lower()
    if SNAPSHOT_SENIOR_RE.search(title) or any(t in tags for t in SNAPSHOT_SENIOR_TAGS):
        return False, "drop_senior"
    return True, "keep_relevant"


def _read_company_csvs(folder: Path) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for path in sorted(folder.glob("*.csv")):
        if path.name.upper() == "ALL.CSV":
            continue
        with path.open("r", encoding="utf-8", newline="") as f:
            rows.extend(list(csv.DictReader(f)))
    return rows


def _merge_snapshot_stats(report_path: Path, new_stats: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    merged: Dict[str, Dict[str, Any]] = {}
    if report_path.exists():
        for line in report_path.read_text(encoding="utf-8").splitlines():
            if not line.startswith("| ") or line.startswith("| Company") or line.startswith("|---"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 9:
                continue
            merged[cells[0].lower()] = {
                "name": cells[0],
                "raw": cells[1],
                "screened": cells[2],
                "drop_senior": cells[3],
                "drop_irrelevant": cells[4],
                "drop_non_us": cells[5],
                "detail_success": cells[6],
                "pages": cells[7],
                "stop_reason": cells[8],
            }
    for s in new_stats:
        merged[str(s["name"]).lower()] = s
    return list(merged.values())


def run_snapshot(company_keys: List[str], window: str, max_age_days: Optional[int] = None) -> None:
    load_env_file(BASE_DIR / ".env")
    session = make_session()
    companies, default_loc = load_company_registry(COMPANY_LINKS_JSON)
    by_key = {str(c.get("key", "")).lower(): c for c in companies}
    by_name = {str(c.get("name", "")).lower(): c for c in companies}

    selected: List[Dict[str, Any]] = []
    missing: List[str] = []
    for key in company_keys:
        k = key.strip().lower()
        cfg = by_key.get(k) or by_name.get(k)
        if cfg:
            selected.append(cfg)
        else:
            missing.append(key)
    if missing:
        print(f"WARNING: not found in company_links.json: {missing}")
    if not selected:
        print("No valid companies selected; aborting.")
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    out_root = OUTPUT_DIR / "by_company" / date_str
    raw_dir = out_root / "raw"
    screened_dir = out_root / "screened"
    raw_dir.mkdir(parents=True, exist_ok=True)
    screened_dir.mkdir(parents=True, exist_ok=True)

    all_raw: List[Dict[str, str]] = []
    all_screened: List[Dict[str, str]] = []
    stats: List[Dict[str, Any]] = []

    for cfg in selected:
        name = cfg["name"]
        base_url = cfg["base_url"]
        jobs_url = build_jobs_url(base_url, default_loc, window, page_num=1)
        print(f"[{name}] crawling {window} ...")
        summaries, meta = scrape_company_pages(session, jobs_url)

        raw_rows: List[Dict[str, str]] = []
        detail_success = 0
        for summary in summaries:
            job_id = str(summary.get("id", "")).strip()
            if not job_id:
                continue
            detail = fetch_job_detail(session, job_id, referer_url=jobs_url)
            if detail:
                detail_success += 1
            else:
                detail = summary
            row = normalize_raw_row(summary, detail, name, source_tag=f"syncareer_{window}")
            raw_rows.append(row)
            time.sleep(DETAIL_SLEEP_SECONDS)

        crawled_count = len(raw_rows)
        date_filtered_out = 0
        date_unknown_kept = 0
        if max_age_days is not None:
            now = datetime.now(timezone.utc)
            filtered: List[Dict[str, str]] = []
            for row in raw_rows:
                if posting_within_days(row, max_age_days, now=now):
                    filtered.append(row)
                    if not (row.get("posting_date") or "").strip():
                        date_unknown_kept += 1
                else:
                    date_filtered_out += 1
            raw_rows = filtered
            print(
                f"[{name}] date filter last {max_age_days}d: "
                f"kept {len(raw_rows)}/{crawled_count} "
                f"(dropped {date_filtered_out} older; {date_unknown_kept} missing dates kept)"
            )

        # Screen with the two lightweight rules.
        kept_rows: List[Dict[str, str]] = []
        drop_counts: Dict[str, int] = defaultdict(int)
        for row in raw_rows:
            keep, reason = snapshot_screen(row)
            out = dict(row)
            out["screen_keep"] = "yes" if keep else "no"
            out["screen_reason"] = reason
            if keep:
                kept_rows.append(out)
            else:
                drop_counts[reason] += 1

        company_slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
        write_csv(raw_dir / f"{company_slug}.csv", raw_rows, RAW_FIELDS)
        write_csv(
            screened_dir / f"{company_slug}.csv",
            kept_rows,
            RAW_FIELDS + ["screen_keep", "screen_reason"],
        )

        all_raw.extend(raw_rows)
        all_screened.extend(kept_rows)
        stats.append(
            {
                "name": name,
                "raw": len(raw_rows),
                "screened": len(kept_rows),
                "detail_success": detail_success,
                "drop_senior": drop_counts.get("drop_senior", 0),
                "drop_irrelevant": drop_counts.get("drop_irrelevant", 0),
                "drop_non_us": drop_counts.get("drop_non_us", 0),
                "stop_reason": (
                    f"{meta.get('stop_reason', '')}"
                    + (
                        f"; filtered_to_{max_age_days}d (dropped {date_filtered_out} of {crawled_count})"
                        if max_age_days is not None
                        else ""
                    )
                ),
                "pages": len(meta.get("attempted_pages", [])),
            }
        )
        print(f"[{name}] raw={len(raw_rows)} screened={len(kept_rows)} stop={meta.get('stop_reason','')}")

    # Rebuild combined files from every company CSV in the dated folder so a
    # later add-on crawl (e.g. Google) does not wipe earlier companies.
    all_raw = _read_company_csvs(raw_dir)
    all_screened = _read_company_csvs(screened_dir)
    write_csv(raw_dir / "ALL.csv", all_raw, RAW_FIELDS)
    write_csv(screened_dir / "ALL.csv", all_screened, RAW_FIELDS + ["screen_keep", "screen_reason"])

    this_run_names = [s["name"] for s in stats]
    stats = _merge_snapshot_stats(out_root / "report.md", stats)
    lines: List[str] = []
    lines.append(f"# By-Company Snapshot - {date_str}")
    lines.append("")
    lines.append(f"- Run time (UTC): {datetime.now(timezone.utc).isoformat()}")
    window_note = window
    if max_age_days is not None:
        window_note = (
            f"mixed; this run crawled {window} then kept posting_date within last "
            f"{max_age_days} days for {', '.join(this_run_names)}"
        )
    lines.append(f"- Time window: {window_note}")
    lines.append(f"- Companies: {', '.join(s['name'] for s in stats)}")
    lines.append(f"- Total raw: {len(all_raw)}")
    lines.append(f"- Total screened (kept): {len(all_screened)}")
    lines.append("- Screening rules: drop Senior-level; keep only SWE/AI-related roles")
    lines.append("")
    lines.append("## Per company")
    lines.append("")
    lines.append("| Company | Raw | Kept | Drop(senior) | Drop(irrelevant) | Drop(non-US) | Detail OK | Pages | Stop reason |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for s in stats:
        lines.append(
            f"| {s['name']} | {s['raw']} | {s['screened']} | {s['drop_senior']} | "
            f"{s['drop_irrelevant']} | {s['drop_non_us']} | {s['detail_success']} | {s['pages']} | {s['stop_reason']} |"
        )
    lines.append("")
    (out_root / "report.md").write_text("\n".join(lines), encoding="utf-8")

    print("")
    print(f"Snapshot written to: {out_root}")
    print(f"Total raw={len(all_raw)} screened={len(all_screened)}")
    print(f"Report: {out_root / 'report.md'}")


DEFAULT_SNAPSHOT_COMPANIES = [
    "google", "meta", "tiktok", "microsoft", "apple", "nvidia",
    "openai", "anthropic", "databricks",
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Syncareer by-company scraper")
    parser.add_argument(
        "--snapshot",
        action="store_true",
        help="Snapshot mode: crawl selected companies fresh into output/by_company/<date>/",
    )
    parser.add_argument(
        "--companies",
        default=",".join(DEFAULT_SNAPSHOT_COMPANIES),
        help="Comma-separated company keys (snapshot mode). Default: big cos + AI unicorns (no Amazon).",
    )
    parser.add_argument(
        "--window",
        default="last7days",
        choices=["24hours", "last3days", "last7days", "last30days"],
        help="Time window for snapshot mode (default last7days).",
    )
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=None,
        help="After crawl, keep only jobs with posting_date within this many days (e.g. 14).",
    )
    args = parser.parse_args()

    if args.snapshot:
        keys = [k for k in args.companies.split(",") if k.strip()]
        run_snapshot(keys, args.window, max_age_days=args.max_age_days)
    else:
        run()
