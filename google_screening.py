#!/usr/bin/env python3
"""Google-only two-step screening from existing Syncareer raw CSV."""

from __future__ import annotations

import csv
import json
import os
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
SOURCE_CSV = OUTPUT_DIR / "syncareer_raw_jobs.csv"
HEURISTIC_CSV = OUTPUT_DIR / "google_heuristic_candidates.csv"
SHORTLIST_CSV = OUTPUT_DIR / "google_llm_shortlist.csv"
REPORT_MD = OUTPUT_DIR / "google_screening_report.md"
ENV_PATH = BASE_DIR / ".env"
SWE_RESUME_PATH = BASE_DIR / "source" / "swe-resume.txt"
AI_RESUME_PATH = BASE_DIR / "source" / "aie-resume.txt"

SHORTLIST_COLUMNS = [
    "company",
    "title",
    "location",
    "posting_date",
    "job_url",
    "fit_score",
    "recommended_resume",
    "fit_category",
    "reason",
    "risk",
    "decision",
    "confidence",
]


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


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "")).strip()


def get_full_text(row: Dict[str, str]) -> str:
    description = (row.get("description") or "").strip()
    requirements = (row.get("requirements") or "").strip()
    text = description if description else requirements
    return normalize_space(text)


def conservative_heuristic_filter(row: Dict[str, str]) -> Tuple[bool, str]:
    title = normalize_space(row.get("title", "")).lower()
    full_text = get_full_text(row).lower()
    mix = f"{title} {full_text[:1200]}"

    # Hard excludes by role family (conservative but clear).
    hard_exclude_patterns = [
        r"\bmanager\b",
        r"\bdirector\b",
        r"\brecruiter\b",
        r"\baccount executive\b",
        r"\bcustomer success\b",
        r"\bmarketing\b",
        r"\blegal\b",
        r"\bhuman resources\b",
        r"\bfinance\b",
        r"\bwarehouse\b",
        r"\boperations\b",
        r"\bprogram manager\b",
        r"\bproduct manager\b",
        r"\bsales\b",
    ]
    for pat in hard_exclude_patterns:
        if re.search(pat, title):
            return False, f"exclude_title:{pat}"

    # Security-clearance / US-person restriction if visible.
    clearance_patterns = [
        "security clearance",
        "u.s. person",
        "us person",
        "must be a u.s. person",
        "requires us person",
    ]
    if any(x in mix for x in clearance_patterns):
        return False, "exclude_restriction"

    # Hardware-only signals.
    if "hardware" in title and not any(x in title for x in ["software", "firmware", "platform", "systems"]):
        return False, "exclude_hardware_only"

    return True, "keep_conservative"


def keyword_pre_score(row: Dict[str, str]) -> float:
    title = normalize_space(row.get("title", "")).lower()
    full_text = get_full_text(row).lower()
    mix = f"{title} {full_text[:1400]}"
    score = 0.0

    strong_hits = [
        "software engineer",
        "software development engineer",
        "sde",
        "backend engineer",
        "full stack",
        "platform engineer",
        "infrastructure engineer",
        "cloud engineer",
        "machine learning engineer",
        "ai engineer",
        "applied ai",
        "llm",
        "agent",
        "rag",
        "research engineer",
        "new grad",
        "early career",
    ]
    medium_hits = [
        "systems engineer",
        "solutions engineer",
        "technical solutions engineer",
        "customer engineer",
        "business systems analyst",
        "data engineer",
        "applied scientist",
    ]
    for w in strong_hits:
        if w in mix:
            score += 2.0
    for w in medium_hits:
        if w in mix:
            score += 1.0
    if "senior" in title or "staff" in title or "principal" in title:
        score -= 1.8
    return score


def parse_json_object(text: str) -> Optional[Dict[str, Any]]:
    text = text.strip()
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


def llm_batch_screen(
    batch_rows: List[Dict[str, str]],
    swe_resume: str,
    ai_resume: str,
    provider: Dict[str, str],
) -> Dict[str, Dict[str, Any]]:
    endpoint = provider["endpoint"]
    api_key = provider["api_key"]
    model = provider["model"]

    jobs_payload: List[Dict[str, Any]] = []
    for row in batch_rows:
        full_text = get_full_text(row)
        jobs_payload.append(
            {
                "job_id": row["job_id"],
                "title": row["title"],
                "company": row["company"],
                "location": row["location"],
                "posting_date": row["posting_date"],
                "job_url": row["job_url"],
                "full_text": full_text[:3200],
            }
        )

    prompt = {
        "task": "Screen Google jobs for application shortlist",
        "instructions": [
            "Be broad: keep maybe-relevant technical roles rather than over-filtering.",
            "Target: Software Engineer, SDE, Backend, Full-stack, Platform, Infrastructure, Cloud, Data Engineer (engineering-heavy), ML/AI/LLM/Applied AI/Agent/RAG, Research Engineer, New Grad/Early Career.",
            "Use SWE resume for SWE/backend/full-stack/platform/infrastructure/cloud/data/general engineering.",
            "Use AI/FDE resume for AI/ML/LLM/Applied AI/Agent/RAG/AI platform/forward deployed style roles.",
            "Output per job: keep/maybe/skip, fit_score 1-10, recommended_resume SWE or AI/FDE, fit_category, reason, risk, seniority risk yes/no, confidence 0-1.",
            "Do not over-penalize if role is not explicitly junior; mark risk but keep maybe when uncertain.",
        ],
        "swe_resume": swe_resume[:7000],
        "ai_fde_resume": ai_resume[:7000],
        "jobs": jobs_payload,
        "return_json_schema": {
            "results": [
                {
                    "job_id": "string",
                    "fit_score": 1,
                    "recommended_resume": "SWE|AI/FDE",
                    "fit_category": "string",
                    "reason": "string",
                    "risk": "string",
                    "too_senior_risk": "yes|no",
                    "decision": "keep|maybe|skip",
                    "confidence": 0.5,
                }
            ]
        },
    }

    body = {
        "model": model,
        "temperature": 0,
        "messages": [
            {"role": "system", "content": "You are an accurate job-screening assistant. Return JSON only."},
            {"role": "user", "content": json.dumps(prompt)},
        ],
    }
    if "openai.com" in endpoint:
        body["response_format"] = {"type": "json_object"}

    response = requests.post(
        endpoint,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=body,
        timeout=80,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"]
    parsed = parse_json_object(content)
    if not parsed:
        return {}

    out: Dict[str, Dict[str, Any]] = {}
    for item in parsed.get("results", []):
        job_id = str(item.get("job_id", "")).strip()
        if not job_id:
            continue
        out[job_id] = {
            "fit_score": float(item.get("fit_score", 0)),
            "recommended_resume": str(item.get("recommended_resume", "SWE")),
            "fit_category": str(item.get("fit_category", "")),
            "reason": str(item.get("reason", "")),
            "risk": str(item.get("risk", "")),
            "decision": str(item.get("decision", "maybe")).lower(),
            "confidence": float(item.get("confidence", 0.5)),
            "too_senior_risk": str(item.get("too_senior_risk", "no")),
        }
    return out


def fallback_llm_like_decision(row: Dict[str, str]) -> Dict[str, Any]:
    title = normalize_space(row["title"]).lower()
    full_text = get_full_text(row).lower()
    mix = f"{title} {full_text[:1400]}"

    ai_signals = ["machine learning", "ml ", " ai ", "llm", "rag", "agent", "applied ai", "model"]
    core_eng_signals = [
        "software engineer",
        "software development engineer",
        "backend",
        "full-stack",
        "platform",
        "infrastructure",
        "cloud",
        "data engineer",
        "research engineer",
        "systems engineer",
        "solutions engineer",
    ]
    score = 4.5
    if any(x in mix for x in core_eng_signals):
        score += 2.2
    if any(x in mix for x in ai_signals):
        score += 1.8
    if any(x in title for x in ["senior", "staff", "principal"]):
        score -= 1.6
    score = max(1.0, min(10.0, score))

    decision = "skip"
    if score >= 7.2:
        decision = "keep"
    elif score >= 5.7:
        decision = "maybe"
    rec = "AI/FDE" if any(x in mix for x in ai_signals) else "SWE"
    return {
        "fit_score": score,
        "recommended_resume": rec,
        "fit_category": "engineering_match" if decision != "skip" else "weak_match",
        "reason": "Keyword-based technical relevance",
        "risk": "Potential seniority/domain mismatch",
        "decision": decision,
        "confidence": 0.58,
        "too_senior_risk": "yes" if any(x in title for x in ["senior", "staff", "principal"]) else "no",
    }


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def run() -> None:
    load_env_file(ENV_PATH)
    swe_resume = SWE_RESUME_PATH.read_text(encoding="utf-8") if SWE_RESUME_PATH.exists() else ""
    ai_resume = AI_RESUME_PATH.read_text(encoding="utf-8") if AI_RESUME_PATH.exists() else ""

    raw_google: List[Dict[str, str]] = []
    with SOURCE_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if normalize_space(row.get("company", "")).lower() == "google":
                raw_google.append(row)

    heuristic_candidates: List[Dict[str, str]] = []
    removed_count = 0
    for row in raw_google:
        keep, reason = conservative_heuristic_filter(row)
        if keep:
            out = dict(row)
            out["heuristic_reason"] = reason
            heuristic_candidates.append(out)
        else:
            removed_count += 1

    # Save heuristic candidates.
    heuristic_fields = list(heuristic_candidates[0].keys()) if heuristic_candidates else []
    if heuristic_fields:
        write_csv(HEURISTIC_CSV, heuristic_candidates, heuristic_fields)
    else:
        write_csv(HEURISTIC_CSV, [], ["job_id", "title", "company"])

    # LLM screening on top-N pre-ranked candidates.
    ranked = sorted(heuristic_candidates, key=keyword_pre_score, reverse=True)
    llm_pool = ranked[:220]  # broad enough, avoids token explosion

    providers: List[Dict[str, str]] = []
    openai_key = (os.environ.get("OPENAI_API_KEY") or "").strip()
    groq_key = (os.environ.get("GROQ_API_KEY") or "").strip()
    if openai_key:
        providers.append(
            {
                "name": "openai",
                "endpoint": "https://api.openai.com/v1/chat/completions",
                "api_key": openai_key,
                "model": "gpt-4o-mini",
            }
        )
    if groq_key:
        providers.append(
            {
                "name": "groq",
                "endpoint": "https://api.groq.com/openai/v1/chat/completions",
                "api_key": groq_key,
                "model": "llama-3.1-8b-instant",
            }
        )

    decisions: Dict[str, Dict[str, Any]] = {}
    llm_success = False
    batch_size = 14
    if providers and llm_pool:
        for i in range(0, len(llm_pool), batch_size):
            batch = llm_pool[i : i + batch_size]
            batch_done = False
            for provider in providers:
                try:
                    result = llm_batch_screen(batch, swe_resume, ai_resume, provider)
                    if result:
                        decisions.update(result)
                        llm_success = True
                        batch_done = True
                        break
                except Exception:  # noqa: BLE001
                    continue
            if not batch_done:
                # fallback per row
                for row in batch:
                    decisions[row["job_id"]] = fallback_llm_like_decision(row)
    else:
        for row in llm_pool:
            decisions[row["job_id"]] = fallback_llm_like_decision(row)

    # Ensure every pooled row gets a decision.
    for row in llm_pool:
        if row["job_id"] not in decisions:
            decisions[row["job_id"]] = fallback_llm_like_decision(row)

    shortlisted_rows: List[Dict[str, Any]] = []
    decision_counts = Counter()
    resume_counts = Counter()
    for row in llm_pool:
        d = decisions[row["job_id"]]
        decision = str(d.get("decision", "maybe")).lower()
        if decision not in {"keep", "maybe", "skip"}:
            decision = "maybe"
        decision_counts[decision] += 1
        resume_counts[str(d.get("recommended_resume", "SWE"))] += 1
        if decision == "skip":
            continue
        shortlisted_rows.append(
            {
                "company": row["company"],
                "title": row["title"],
                "location": row["location"],
                "posting_date": row["posting_date"],
                "job_url": row["job_url"],
                "fit_score": f"{float(d.get('fit_score', 0.0)):.1f}",
                "recommended_resume": d.get("recommended_resume", "SWE"),
                "fit_category": d.get("fit_category", ""),
                "reason": d.get("reason", ""),
                "risk": d.get("risk", ""),
                "decision": decision,
                "confidence": f"{float(d.get('confidence', 0.5)):.2f}",
            }
        )

    # Broad shortlist target 20-30.
    shortlisted_rows.sort(
        key=lambda x: (
            0 if x["decision"] == "keep" else 1,
            -float(x["fit_score"]),
            -float(x["confidence"]),
        )
    )
    target_n = 25
    if len(shortlisted_rows) > target_n:
        shortlisted_rows = shortlisted_rows[:target_n]

    write_csv(SHORTLIST_CSV, shortlisted_rows, SHORTLIST_COLUMNS)

    lines: List[str] = []
    lines.append("# Google Screening Report")
    lines.append("")
    lines.append(f"- Run time (UTC): {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"- Source file: `{SOURCE_CSV}`")
    lines.append(f"- Google raw rows: {len(raw_google)}")
    lines.append(f"- Step 1 heuristic candidates: {len(heuristic_candidates)}")
    lines.append(f"- Step 1 removed (clear mismatch): {removed_count}")
    lines.append(f"- Step 2 LLM pool size: {len(llm_pool)}")
    lines.append(f"- Step 2 LLM mode: {'LLM API' if llm_success else 'fallback scoring'}")
    lines.append(f"- Final shortlist size: {len(shortlisted_rows)}")
    lines.append("")
    lines.append("## Step 2 Decision Mix (pool)")
    lines.append(f"- keep: {decision_counts.get('keep', 0)}")
    lines.append(f"- maybe: {decision_counts.get('maybe', 0)}")
    lines.append(f"- skip: {decision_counts.get('skip', 0)}")
    lines.append("")
    lines.append("## Resume Recommendation Mix (pool)")
    lines.append(f"- SWE: {resume_counts.get('SWE', 0)}")
    lines.append(f"- AI/FDE: {resume_counts.get('AI/FDE', 0)}")
    lines.append("")
    lines.append("## Outputs")
    lines.append(f"- Heuristic candidates: `{HEURISTIC_CSV}`")
    lines.append(f"- LLM shortlist: `{SHORTLIST_CSV}`")
    lines.append(f"- This report: `{REPORT_MD}`")

    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote: {HEURISTIC_CSV}")
    print(f"Wrote: {SHORTLIST_CSV}")
    print(f"Wrote: {REPORT_MD}")
    print(f"raw_google={len(raw_google)} heuristic_candidates={len(heuristic_candidates)} shortlist={len(shortlisted_rows)} llm_success={llm_success}")


if __name__ == "__main__":
    run()
