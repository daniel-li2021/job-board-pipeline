#!/usr/bin/env python3
"""Big Tech Official Careers pipeline (component 3).

Discovery only lives here. After scrape, jobs are normalized to the shared
schema and handed to the EXISTING board_pipeline matching stack:

    hard filter -> role/seniority prefilter -> score_survivors (LLM/cache)
    -> assign_tier / rank

This file does not reimplement scoring. It does not write output/board/ or
touch the Syncareer watchlist.

Usage:
    python3 official_careers.py scrape --only google
    python3 official_careers.py match --no-llm
    python3 official_careers.py run            # scrape + match; digest at most once/day
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import alert_history
from sources.careers.http import (
    is_placeholder_location,
    keep_us_or_unknown,
    make_session,
)
from sources.careers.registry import load_companies, scrape_enabled
from sources.schema import (
    OUTPUT_DIR,
    RECENCY_BUCKETS,
    dedup_key,
    recency_bucket,
)

import board_pipeline as board
import coverage_reconcile
import llm_config

BASE_DIR = Path(__file__).resolve().parent
CAREERS_DIR = OUTPUT_DIR / "official_careers"
RAW_PATH = CAREERS_DIR / "raw.json"
STORE_PATH = CAREERS_DIR / "jobs.json"
LATEST_MD_PATH = CAREERS_DIR / "latest.md"
INBOX_MD_PATH = CAREERS_DIR / "inbox.md"
INBOX_CSV_PATH = CAREERS_DIR / "inbox.csv"
REPORT_PATH = CAREERS_DIR / "scrape_report.md"
DIGEST_STATE_PATH = CAREERS_DIR / "digest_state.json"
ALERT_HISTORY_PATH = CAREERS_DIR / "alert_history.json"
RUNS_DIR = CAREERS_DIR / "runs"
ALERTS_DIR = OUTPUT_DIR / "alerts"
RETENTION_DAYS = 7
INBOX_DAYS = 3

# Official-careers discovery extras. Matching/scoring stay in board_pipeline.
PHD_TITLE_RE = re.compile(r"\bph\.?d\.?\b", re.IGNORECASE)


def official_discovery_filter(job: Dict[str, str]) -> Tuple[bool, str]:
    """US-only + PhD-track drops applied before shared matching."""
    title = job.get("title") or ""
    if PHD_TITLE_RE.search(title):
        return False, "phd_only"
    location = job.get("location") or ""
    if is_placeholder_location(location):
        job["location"] = "United States"
        location = "United States"
    if location and not keep_us_or_unknown(location, path_hint=job.get("official_url") or job.get("source_url") or ""):
        return False, "non_us_location"
    return True, "keep"


def _sample_record(job: Dict[str, str]) -> Dict[str, str]:
    return {
        "company": job.get("company", ""),
        "source": job.get("source", ""),
        "job_id": job.get("job_id", ""),
        "title": job.get("title", ""),
        "location": job.get("location", ""),
        "official_url": job.get("official_url", ""),
        "posted_date": job.get("posted_date", ""),
        "updated_date": job.get("updated_date", ""),
        "fetched_at": job.get("fetched_at", ""),
        "date_confidence": job.get("date_confidence", ""),
        "description": (job.get("description") or "")[:180],
    }


def write_scrape_outputs(
    results: List[Dict[str, Any]],
    stamp: str,
    *,
    merge_previous: bool = True,
) -> List[Dict[str, str]]:
    CAREERS_DIR.mkdir(parents=True, exist_ok=True)
    scraped_companies = {(r.get("company") or "") for r in results}
    current_jobs = [j for r in results for j in (r.get("jobs") or []) if isinstance(j, dict)]
    current_keys = {dedup_key(j) for j in current_jobs}
    result_by_company = {(r.get("company") or ""): r for r in results}
    all_jobs: List[Dict[str, str]] = []
    if merge_previous:
        for job in load_raw_jobs():
            company = job.get("company") or ""
            result = result_by_company.get(company)
            if company not in scraped_companies:
                all_jobs.append(job)
                continue
            successful_full_sweep = bool(
                result
                and (
                    result.get("incremental_mode") == "full_sweep"
                    or result.get("full_listing_coverage")
                )
                and not result.get("errors")
            )
            # Incremental newest-first/limited-depth runs intentionally do not
            # revisit the tail. Carry unseen prior live records until the
            # periodic successful full sweep can remove closed postings.
            if dedup_key(job) not in current_keys and not successful_full_sweep:
                carried = dict(job)
                carried["listing_cache_status"] = "carried_until_full_sweep"
                all_jobs.append(carried)
    lines = [
        f"# Official careers scrape report — {stamp}",
        "",
        "Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.",
        "",
    ]
    for result in results:
        jobs = [j for j in result.get("jobs") or [] if isinstance(j, dict)]
        all_jobs.extend(jobs)
        trustworthy = sum(
            1
            for j in jobs
            if j.get("posted_date") and (j.get("date_confidence") or "").lower() in ("high", "medium")
        )
        status = result.get("status") or ("ok" if jobs else ("blocked" if result.get("errors") else "empty"))
        lines.extend(
            [
                f"## {result.get('company') or result.get('source')}",
                "",
                f"- Status: {status}",
                f"- Scraping method: {result.get('method') or '-'}",
                f"- Search URL/API: `{result.get('search_url') or '-'}`",
                f"- Pagination: {result.get('pagination') or '-'}",
                f"- Pages/requests fetched: {result.get('pages_fetched', 0)}",
                f"- Incremental mode/page cap: {result.get('incremental_mode', '-')} / {result.get('page_cap_applied', '-')}",
                f"- Detail pages fetched/cache reused: {result.get('detail_fetches', 0)} / {result.get('detail_cache_reused', 0)}",
                f"- Raw jobs found: {result.get('raw_jobs', 0)}",
                f"- After US/location filtering: {len(jobs)}",
                f"- With trustworthy posted_date: {trustworthy}",
                f"- Errors/403s: {result.get('errors') or 'none'}",
                "",
            ]
        )
        samples = [_sample_record(j) for j in jobs[:5]]
        if samples:
            lines.append("Sample normalized records:")
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(samples, indent=2, ensure_ascii=False))
            lines.append("```")
            lines.append("")
        result_for_disk = dict(result)
        result_for_disk["jobs_kept"] = len(jobs)
        result_for_disk["trustworthy_posted_date"] = trustworthy
        result_for_disk["samples"] = samples
        # Do not duplicate the full job list inside the markdown-oriented summary blob.
        result_for_disk.pop("jobs", None)
        result["summary"] = result_for_disk

    payload = {
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "stamp": stamp,
        "count": len(all_jobs),
        "scraped_company_ids": sorted(
            str(r.get("company_id") or "") for r in results if r.get("company_id")
        ),
        "per_company": [r.get("summary") for r in results],
        "jobs": all_jobs,
    }
    RAW_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    return all_jobs


def load_raw_jobs() -> List[Dict[str, str]]:
    if not RAW_PATH.exists():
        return []
    try:
        data = json.loads(RAW_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    jobs = data.get("jobs") if isinstance(data, dict) else data
    return [j for j in jobs if isinstance(j, dict)] if isinstance(jobs, list) else []


def load_careers_store() -> Dict[str, Dict[str, Any]]:
    if not STORE_PATH.exists():
        return {}
    try:
        data = json.loads(STORE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    entries = data.get("entries", []) if isinstance(data, dict) else data
    out: Dict[str, Dict[str, Any]] = {}
    if isinstance(entries, list):
        for entry in entries:
            key = entry.get("key")
            if key:
                out[key] = entry
    return out


def save_careers_store(store: Dict[str, Dict[str, Any]]) -> None:
    CAREERS_DIR.mkdir(parents=True, exist_ok=True)
    entries = sorted(store.values(), key=lambda e: (e.get("first_seen", ""), e.get("key", "")), reverse=True)
    payload = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "retention_days": RETENTION_DAYS,
        "count": len(entries),
        "entries": entries,
    }
    STORE_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_latest_md(visible: List[Dict[str, str]], stats: Dict[str, Any], stamp: str) -> None:
    CAREERS_DIR.mkdir(parents=True, exist_ok=True)
    report_now = datetime.now(timezone.utc)
    lines = [
        f"# Big Tech official careers — 7-day view — {stamp}",
        "",
        f"- Updated (PT): {report_now.astimezone(board.PACIFIC).strftime('%Y-%m-%d %H:%M %Z')}",
        f"- Snapshot (UTC): {report_now.isoformat()}",
        f"- Last 24 hours: {sum(1 for job in visible if (board._job_inbox_ref(job) or report_now) >= report_now - timedelta(hours=24))}",
        f"- Last 3 days: {sum(1 for job in visible if (board._job_inbox_ref(job) or report_now) >= report_now - timedelta(days=3))}",
        "",
        "Discovery: `official_careers.py scrape`. Matching: shared `board_pipeline` scoring/ranking.",
        "",
        "## Run stats",
        "",
        f"- Scraped companies: {stats['source_raw']}",
        f"- Funnel: after dedup {stats['funnel']['after_dedup']} -> after company filter {stats['funnel']['after_company']} "
        f"-> after hard filter {stats['funnel']['after_hard_filter']} "
        f"-> after role+seniority prefilter {stats['funnel']['after_prefilter']} | dropped {stats['funnel']['dropped']}",
        f"- LLM usage: scored {stats['llm']['scored']} / API requests {stats['llm']['api_requests']} / "
        f"cache reused {stats['llm']['reused']} (cross-pipeline {stats['llm'].get('peer_reused', 0)}) / "
        f"rule fallback {stats['llm']['rule']}",
        f"- LLM cost: {llm_config.format_usage(stats['llm'])}",
        f"- Output: Tier A {stats['output']['tier_a']} / Tier B {stats['output']['tier_b']} / shown {stats['output']['shown']}",
        "",
    ]
    by_tier = {
        "A": [j for j in visible if j.get("tier") == "A"],
        "B": [j for j in visible if j.get("tier") == "B"],
    }
    titles = {"A": "Tier A - apply now / referral", "B": "Tier B - worth applying"}
    for tier in ("A", "B"):
        rows = by_tier[tier]
        lines.append(f"## {titles[tier]} ({len(rows)})")
        lines.append("")
        if not rows:
            lines.append("_none_")
            lines.append("")
            continue
        lines.append("| Score | Src | Source | Company | Title | Location | Posted | Recency | Conf | Resume | Referral | Review | Coverage | Link |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for row in rows:
            link_url = row.get("official_url") or row.get("source_url") or ""
            link = f"[open]({link_url})" if link_url else "-"
            title = (row.get("title") or "").replace("|", "/")[:70]
            company = (row.get("company") or "").replace("|", "/")
            loc = (row.get("location") or "").replace("|", "/")
            resume = (row.get("resume_profile_used") or "").replace("resume_", "")
            src = row.get("score_source") or "-"
            referral = row.get("referral_name") or "-"
            lines.append(
                f"| {float(row.get('match_score', 0)):.0f} | {src} | official | {company} | {title} | {loc} | "
                f"{row.get('posted_date', '') or '-'} | {row.get('recency_bucket', '')} | "
                f"{row.get('date_confidence', '')} | {resume} | {referral} | {row.get('review_status') or 'unreviewed'} | official_canonical | {link} |"
            )
        lines.append("")
    LATEST_MD_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_inbox(visible: List[Dict[str, str]], stamp: str, now: datetime) -> None:
    cutoff = now - timedelta(days=INBOX_DAYS)
    inbox: List[Dict[str, str]] = []
    for job in visible:
        ref = None
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
            ref = parsed
            break
        if ref is None or ref >= cutoff:
            inbox.append(job)
    CAREERS_DIR.mkdir(parents=True, exist_ok=True)
    with INBOX_CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=board.ALERT_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in inbox:
            writer.writerow({k: row.get(k, "") for k in board.ALERT_FIELDS})
    lines = [
        f"# Big Tech official careers inbox (last {INBOX_DAYS} days)",
        "",
        f"- Updated (PT): {now.astimezone(board.PACIFIC).strftime('%Y-%m-%d %H:%M %Z')}",
        f"- Snapshot (UTC): {now.isoformat()}",
        f"- Jobs: {len(inbox)} (Tier A/B only)",
        f"- Last 24 hours: {sum(1 for job in inbox if (board._job_inbox_ref(job) or now) >= now - timedelta(hours=24))}",
        f"- Last 3 days: {len(inbox)}",
        "",
        "Coverage gaps from ATS/Syncareer are reviewed in `../cross_pipeline/coverage.md`.",
        "",
        "| Tier | Score | Source | Company | Title | Location | Posted | Recency | Referral | Review | Coverage | Link |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in inbox:
        link_url = row.get("official_url") or row.get("source_url") or ""
        link = f"[open]({link_url})" if link_url else "-"
        title = (row.get("title") or "").replace("|", "/")[:70]
        referral = row.get("referral_name") or "-"
        lines.append(
            f"| {row.get('tier')} | {float(row.get('match_score', 0)):.0f} | official | "
            f"{(row.get('company') or '').replace('|', '/')} | {title} | "
            f"{(row.get('location') or '').replace('|', '/')} | {row.get('posted_date', '') or '-'} | "
            f"{row.get('recency_bucket', '')} | {referral} | {row.get('review_status') or 'unreviewed'} | official_canonical | {link} |"
        )
    INBOX_MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_digest(jobs: List[Dict[str, str]], stamp: str) -> Dict[str, Path]:
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    ALERTS_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = ALERTS_DIR / f"official_{stamp}.csv"
    body_path = ALERTS_DIR / "official_issue_body.md"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=board.ALERT_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in jobs:
            writer.writerow({k: row.get(k, "") for k in board.ALERT_FIELDS})
    lines = [
        f"Big Tech official careers digest - {stamp}",
        "",
        f"Updated (PT): {datetime.now(board.PACIFIC).strftime('%Y-%m-%d %H:%M %Z')}",
        f"Snapshot (UTC): {datetime.now(timezone.utc).isoformat()}",
        "",
        f"{len(jobs)} new or promoted (B→A) Tier A/B job(s).",
        "",
        "At most one digest is sent per Pacific day. Score/JD-only changes are not re-alerted.",
        "",
        "| Tier | Score | Source | Company | Title | Location | Posted | Recency | Referral | Review | Coverage | Link |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in jobs:
        link_url = row.get("official_url") or row.get("source_url") or ""
        link = f"[open]({link_url})" if link_url else "-"
        title = (row.get("title") or "").replace("|", "/")[:70]
        referral = row.get("referral_name") or "-"
        lines.append(
            f"| {row.get('tier')} | {float(row.get('match_score', 0)):.0f} | official | "
            f"{(row.get('company') or '').replace('|', '/')} | {title} | "
            f"{(row.get('location') or '').replace('|', '/')} | {row.get('posted_date', '') or '-'} | "
            f"{row.get('recency_bucket', '')} | {referral} | {row.get('review_status') or 'unreviewed'} | official_canonical | {link} |"
        )
    body_path.write_text("\n".join(lines), encoding="utf-8")
    return {"csv": csv_path, "issue_body": body_path}


def cmd_scrape(args: argparse.Namespace) -> List[Dict[str, str]]:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M")
    registry = load_companies()
    max_pages = int(args.max_pages or registry.get("max_pages_default") or 50)
    session = make_session()
    print(f"Scraping official careers (only={args.only or 'all'}, max_pages={max_pages})...")
    results = scrape_enabled(
        session,
        only=args.only,
        max_pages=max_pages,
        previous_jobs=load_raw_jobs(),
        full_sweep=True if getattr(args, "full_sweep", False) else None,
    )
    jobs = write_scrape_outputs(results, stamp)
    for result in results:
        jobs_n = len(result.get("jobs") or [])
        print(
            f"  {result.get('company')}: raw={result.get('raw_jobs', 0)} "
            f"kept={jobs_n} pages={result.get('pages_fetched', 0)} "
            f"errors={len(result.get('errors') or [])}"
        )
    print(f"Wrote {len(jobs)} jobs -> {RAW_PATH}")
    print(f"Report -> {REPORT_PATH}")
    return jobs


def cmd_match(args: argparse.Namespace, jobs: Optional[List[Dict[str, str]]] = None) -> None:
    board.load_env_file(BASE_DIR / ".env")
    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    stamp = now.strftime("%Y-%m-%d_%H%M")
    raw_jobs = jobs if jobs is not None else load_raw_jobs()
    if not raw_jobs:
        print("No official-careers jobs to match. Run scrape first.")
        board.emit_github_output(
            {
                "new_count": "0",
                "stamp": stamp,
                "digest_emitted": "0",
                "issue_title": "",
                "issue_body_path": "",
            }
        )
        return

    profiles = board.load_profiles()
    targets = board.load_target_companies()
    company_filters = board.load_company_filters()
    review_state = coverage_reconcile.load_review_state()

    deduped = board.merge_by_key(raw_jobs)
    store = board.prune_store(load_careers_store(), now)
    new_keys: set[str] = set()
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
        job["source_pipeline"] = "official"
        job["canonical_job_key"] = coverage_reconcile.canonical_job_key(job)
        job["canonical_source"] = "official"
        job["coverage_status"] = "official_canonical"
        job["duplicate_of"] = ""
        job["official_snapshot_at"] = now_iso
        job["source_snapshot_at"] = now_iso
        job["suppress_alert"] = False
        review_entry = review_state.get(job["canonical_job_key"], {})
        job["review_status"] = review_entry.get("status", "unreviewed") if isinstance(review_entry, dict) else "unreviewed"

    drops: Counter = Counter()
    after_company: List[Dict[str, str]] = []
    for job in deduped:
        action, _matched = board.classify_company(job.get("company", ""), company_filters, job.get("title", ""))
        # Official-careers IS the coverage for Big Tech, so skip covered_elsewhere drops.
        if action == "covered_elsewhere":
            action = "keep"
        job["company_flag"] = "" if action == "keep" else action
        job["deprioritized"] = action == "deprioritize"
        job["preferred"] = action == "prefer"
        job["clearance_risk_company"] = action == "clearance_risk"
        if action in board.CATEGORY_DROP_REASON and action != "covered_elsewhere":
            reason = board.CATEGORY_DROP_REASON[action]
            job["filter_status"] = "dropped"
            job["drop_reason"] = reason
            drops[reason] += 1
        else:
            after_company.append(job)

    after_discovery: List[Dict[str, str]] = []
    for job in after_company:
        keep, reason = official_discovery_filter(job)
        if keep:
            after_discovery.append(job)
        else:
            job["filter_status"] = "dropped"
            job["drop_reason"] = reason
            drops[reason] += 1

    after_hard: List[Dict[str, str]] = []
    for job in after_discovery:
        keep, reason = board.hard_filter(job)
        if keep:
            job["filter_status"] = "kept"
            job["drop_reason"] = ""
            after_hard.append(job)
        else:
            job["filter_status"] = "dropped"
            job["drop_reason"] = reason
            drops[reason] += 1

    candidates: List[Dict[str, str]] = []
    for job in after_hard:
        keep, reason = board.role_seniority_prefilter(job)
        if keep:
            candidates.append(job)
        else:
            job["filter_status"] = "dropped"
            job["drop_reason"] = reason
            drops[reason] += 1

    referrals: Dict[str, bool] = {}
    for job in candidates:
        name = board.match_target_company(job.get("company", ""), targets)
        referrals[dedup_key(job)] = bool(name)
        job["referral_name"] = name or ""

    screen_method, llm_errors, score_counts = board.score_survivors(
        candidates,
        referrals,
        profiles,
        store,
        use_llm=not args.no_llm,
    )
    for job in candidates:
        job["tier"] = board.assign_tier(job, referrals.get(dedup_key(job), False))
        board.apply_referral_action(job)
    candidates.sort(key=board.user_facing_sort_key)

    tier_a = [j for j in candidates if j["tier"] == "A"]
    tier_b = [j for j in candidates if j["tier"] == "B"]
    visible = tier_a + tier_b

    new_store = dict(store)
    for job in deduped:
        key = dedup_key(job)
        new_store[key] = board.build_store_entry(job, key)
    for entry in new_store.values():
        board.ensure_entry_defaults(entry)
    new_store = board.prune_store(new_store, now)
    save_careers_store(new_store)

    recency_dist = {b: 0 for b in RECENCY_BUCKETS}
    for job in candidates:
        recency_dist[job.get("recency_bucket", "gt7d")] += 1

    per_company = Counter(j.get("company", "") for j in raw_jobs)
    stats = {
        "source_raw": dict(per_company),
        "funnel": {
            "after_dedup": len(deduped),
            "after_company": len(after_company),
            "after_hard_filter": len(after_hard),
            "after_prefilter": len(candidates),
            "dropped": sum(drops.values()),
        },
        "llm": {
            **score_counts,
            "scored": score_counts["llm"],
            "api_requests": score_counts.get("api_requests", 0),
            "reused": score_counts["reused"],
            "peer_reused": score_counts.get("peer_reused", 0),
            "rule": score_counts["rule"],
        },
        "output": {
            "tier_a": len(tier_a),
            "tier_b": len(tier_b),
            "shown": len(visible),
        },
        "recency": recency_dist,
        "screen_method": screen_method,
    }
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    (RUNS_DIR / f"{stamp}_stats.json").write_text(
        json.dumps({"run_at": now_iso, **stats}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_latest_md(visible, stats, stamp)
    write_inbox(visible, stamp, now)

    digest_state = board.load_digest_state(DIGEST_STATE_PATH)
    digest_jobs, emit_digest, digest_day = board.decide_digest(
        visible, digest_state, force=args.force_digest, no_digest=args.no_digest
    )
    alert_paths: Dict[str, Path] = {}
    digest_count = 0
    if emit_digest:
        alert_paths = write_digest(digest_jobs, stamp)
        alert_history.append_event(
            ALERT_HISTORY_PATH,
            pipeline="official",
            stamp=stamp,
            jobs=digest_jobs,
            event_kind="new_or_promoted_ab",
        )
        board.apply_digest_state(digest_state, digest_jobs, digest_day)
        digest_count = len(digest_jobs)
    board.save_digest_state(DIGEST_STATE_PATH, digest_state)

    board.emit_github_output(
        {
            "new_count": str(digest_count),
            "stamp": stamp,
            "tier_a": str(len(tier_a)),
            "tier_b": str(len(tier_b)),
            "shown": str(len(visible)),
            "digest_emitted": "1" if emit_digest else "0",
            "issue_title": f"Official careers digest {stamp} ({digest_count} new/promoted A/B)",
            "issue_body_path": str(alert_paths.get("issue_body", "")),
        }
    )

    print(
        f"Funnel: dedup {len(deduped)} -> company {len(after_company)} -> hard {len(after_hard)} "
        f"-> prefilter {len(candidates)} | dropped {sum(drops.values())}"
    )
    print(
        f"LLM: scored {score_counts['llm']} / reused {score_counts['reused']} / "
        f"rule {score_counts['rule']} ({screen_method}"
        + (f", {len(llm_errors)} llm errors" if llm_errors else "")
        + ")"
    )
    print(f"LLM cost: {llm_config.format_usage(score_counts)}")
    print(f"Output: Tier A {len(tier_a)} / Tier B {len(tier_b)} / shown {len(visible)}")
    if emit_digest:
        print(f"Digest emitted: {digest_count} new/promoted A/B -> {alert_paths.get('issue_body')}")
    else:
        digest_today = digest_state.get("last_digest_date") == digest_day
        reason = (
            "--no-digest" if args.no_digest
            else "already sent today" if digest_today
            else "no new or promoted A/B"
        )
        print(f"Digest skipped ({reason}). Store updated silently.")
    print(f"Wrote {LATEST_MD_PATH} and {STORE_PATH} ({len(new_store)} entries)")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Big Tech official careers discovery + shared matching")
    sub = parser.add_subparsers(dest="cmd", required=True)

    scrape = sub.add_parser("scrape", help="Discover jobs from official career sites")
    scrape.add_argument("--only", help="Company id(s) from source/official_careers.json, comma-separated")
    scrape.add_argument("--max-pages", type=int, default=0, help="Safety cap per query (default from registry)")
    scrape.add_argument("--full-sweep", action="store_true", help="Force deep/full pagination instead of the daily incremental depth")

    match = sub.add_parser("match", help="Run shared board_pipeline matching on the last scrape")
    match.add_argument("--no-llm", action="store_true")
    match.add_argument("--no-digest", action="store_true", help="Update store/latest.md without a user-facing digest")
    match.add_argument("--force-digest", action="store_true", help="Emit a digest even if one already went out today")

    run = sub.add_parser("run", help="Scrape then match (default scheduled entry point)")
    run.add_argument("--only", help="Company id(s) from source/official_careers.json, comma-separated")
    run.add_argument("--max-pages", type=int, default=0)
    run.add_argument("--full-sweep", action="store_true", help="Force deep/full pagination instead of the daily incremental depth")
    run.add_argument("--no-llm", action="store_true")
    run.add_argument("--no-digest", action="store_true")
    run.add_argument("--force-digest", action="store_true")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.cmd == "scrape":
        cmd_scrape(args)
        return
    if args.cmd == "match":
        cmd_match(args)
        return
    jobs = cmd_scrape(args)
    cmd_match(args, jobs=jobs)


if __name__ == "__main__":
    main()
