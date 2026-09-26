#!/usr/bin/env python3
"""Run local best-effort job-board sources and snapshot them.

Each source is independent: if one hits a login wall / captcha / 403 / 429 /
network error, or returns zero rows, it is skipped and its previous
``output/sources/<name>.json`` snapshot is left untouched (never overwritten
with nothing). The other source and the downstream git sync proceed normally.

LinkedIn search remains card-first. Indeed/Glassdoor arrive through JobSpy;
all three then share hard filtering, JD persistence, diagnostics, snapshots,
and downstream Board processing. LinkedIn alone needs a separate bounded,
cache-aware logged-out detail fetch.

This is invoked by launchd every 2-3 hours (see scripts/). It does NOT run the
full board pipeline and does NOT touch jobs.json / latest.md — those are
GitHub-Actions-owned to avoid local/CI git conflicts.

Usage:
    python3 local_sources.py                 # all sources
    python3 local_sources.py --only linkedin
    python3 local_sources.py --only indeed
    python3 local_sources.py --only glassdoor
    python3 local_sources.py --recover-jds         # current LinkedIn + Indeed only
"""

from __future__ import annotations

import argparse
import copy
import json

from state_io import atomic_write
import os
import subprocess
import time
from datetime import datetime, timedelta, timezone
from typing import Callable, Dict

import board_pipeline as board
import coverage_reconcile
import remote_recovery
from sources import jobspy_local, linkedin_local, official_jd_recovery
from sources.schema import (
    OUTPUT_DIR,
    SNAPSHOT_SCHEMA_VERSION,
    SourceUnavailable,
    read_source_snapshot_payload,
    write_source_snapshot,
)

SOURCES: Dict[str, Callable[[], Dict[str, object]]] = {
    "linkedin": linkedin_local.scrape,
    "indeed": lambda: jobspy_local.scrape("indeed"),
    "glassdoor": lambda: jobspy_local.scrape("glassdoor"),
}
OPTIONAL_SOURCES = {"glassdoor"}
HEALTH_PATH = OUTPUT_DIR / "sources" / "health.json"
HEALTH_SCHEMA_VERSION = 1
LINKEDIN_DETAIL_LIMIT = 8
MAC_SEARCH_PAGE_LIMIT = 14
LINKEDIN_DETAIL_COOLDOWN_HOURS = 24
GLASSDOOR_RECOVERY_HOURS = 24
LINKEDIN_SEARCH_COOLDOWN_HOURS = 24
RECOVERY_SEARCH_LIMIT = float("inf")
RECOVERY_PAGE_LIMIT = float("inf")


def _health_source(name: str) -> Dict[str, object]:
    try:
        payload = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}
    source = payload.get("sources", {}).get(name, {}) if isinstance(payload, dict) else {}
    return dict(source) if isinstance(source, dict) else {}


def _linkedin_runner_state() -> Dict[str, object]:
    state = _health_source("linkedin")
    if os.environ.get("LOCAL_SOURCE_PROFILE") != "mac":
        return state
    runners = state.get("runner_states", {})
    runner = runners.get("mac", {}) if isinstance(runners, dict) else {}
    return dict(runner) if isinstance(runner, dict) else {}


def _linkedin_detail_control(now: datetime) -> tuple[int, bool, bool]:
    state = _linkedin_runner_state()
    streak = int(state.get("detail_429_streak", 0) or 0)
    try:
        cooldown_until = datetime.fromisoformat(
            str(state.get("detail_cooldown_until") or "").replace("Z", "+00:00")
        )
        if cooldown_until.tzinfo is None:
            cooldown_until = cooldown_until.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        cooldown_until = datetime.min.replace(tzinfo=timezone.utc)
    if cooldown_until > now:
        return 0, True, False
    probe = bool(state.get("detail_cooldown_until")) or streak >= 2
    return (1 if probe else LINKEDIN_DETAIL_LIMIT), False, probe


def _update_linkedin_detail_health(state: Dict[str, object], detail: Dict[str, object], attempted_at: datetime) -> None:
    """Advance detail failure state only when a detail request occurred."""
    requests_made = int(detail.get("requests", 0) or 0)
    if not requests_made:
        return
    state["detail_last_attempt_at"] = attempted_at.isoformat()
    if detail.get("probe"):
        if int(detail.get("detail_jds_fetched", 0) or 0):
            state["detail_429_streak"] = 0
            state["detail_cooldown_until"] = ""
            state["detail_cooldown_reason"] = ""
            state["detail_status"] = "active"
        else:
            state["detail_cooldown_until"] = (attempted_at + timedelta(hours=LINKEDIN_DETAIL_COOLDOWN_HOURS)).isoformat()
            state["detail_cooldown_reason"] = str(detail.get("blocked") or "detail probe returned no JD")
            state["detail_status"] = "cooldown"
            if detail.get("rate_limited"):
                state["detail_429_streak"] = int(state.get("detail_429_streak", 0) or 0) + 1
    elif detail.get("rate_limited"):
        streak = int(state.get("detail_429_streak", 0) or 0) + 1
        state["detail_429_streak"] = streak
        if streak >= 2:
            state["detail_cooldown_until"] = (attempted_at + timedelta(hours=LINKEDIN_DETAIL_COOLDOWN_HOURS)).isoformat()
            state["detail_cooldown_reason"] = "repeated HTTP 429"
            state["detail_status"] = "cooldown"
    elif int(detail.get("responses", 0) or 0):
        state["detail_429_streak"] = 0
        state["detail_cooldown_until"] = ""
        state["detail_cooldown_reason"] = ""


def _linkedin_search_control(now: datetime) -> tuple[int, bool, bool]:
    state = _linkedin_runner_state()
    streak = int(state.get("search_429_streak", 0) or 0)
    try:
        until = datetime.fromisoformat(str(state.get("search_cooldown_until") or "").replace("Z", "+00:00"))
        if until.tzinfo is None:
            until = until.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        until = datetime.min.replace(tzinfo=timezone.utc)
    active = until > now
    probe = not active and streak >= 2
    normal_limit = MAC_SEARCH_PAGE_LIMIT if os.environ.get("LOCAL_SOURCE_PROFILE") == "mac" else linkedin_local.SEARCH_PAGE_LIMIT
    return (0 if active else 1 if probe else normal_limit), active, probe


def _mark_linkedin_official_matches(
    rows: list[dict], previous_jobs: list[dict], context: Dict[str, object], store: Dict[str, dict],
) -> int:
    """Mark exact official matches without changing local snapshot identities."""
    previous_by_id = {str(job.get("job_id") or ""): job for job in previous_jobs if job.get("job_id")}
    stored_by_id = {
        (str(entry.get("source") or ""), str(entry.get("job_id") or "")): entry
        for entry in store.values()
    }
    matched = 0
    for row in rows:
        company_id = coverage_reconcile.company_id_for(
            str(row.get("company") or ""), context.get("registry_entries", []),
        )
        if not company_id:
            continue
        probe = dict(row)
        prior = previous_by_id.get(str(row.get("job_id") or ""), {})
        for field in ("official_url", "application_url", "requisition_id", "req_id"):
            if not probe.get(field) and prior.get(field):
                probe[field] = prior[field]
        method, official = coverage_reconcile.exact_match(
            probe, context.get("by_company", {}).get(company_id, []),
        )
        if not method or not official:
            continue
        official_url = str(official.get("official_url") or official.get("application_url") or "")
        if not official_url:
            continue
        board_prior = stored_by_id.get((str(row.get("source") or ""), str(row.get("job_id") or "")), {})
        same_prior_match = coverage_reconcile.normalize_url(str(board_prior.get("official_url") or "")) == coverage_reconcile.normalize_url(official_url)
        row["_linkedin_official_url"] = official_url
        row["_linkedin_official_defer"] = not (same_prior_match and not board_prior.get("description_available"))
        matched += 1
    return matched


def _remote_handoff_rows() -> list[dict]:
    return [
        {**row, "remote_recovery": True}
        for pipeline in ("official", "board", "syncareer")
        for row in remote_recovery.read_snapshot(OUTPUT_DIR / "recovery" / f"{pipeline}.json.gz")
    ]


def collector_provenance() -> Dict[str, object]:
    commit = os.environ.get("COLLECTOR_COMMIT", "").strip()
    dirty_env = os.environ.get("COLLECTOR_DIRTY")
    try:
        if not commit:
            commit = subprocess.run(
                ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True,
            ).stdout.strip()
        dirty = dirty_env != "0" if dirty_env is not None else bool(subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=no"],
            capture_output=True, text=True, check=True,
        ).stdout.strip())
    except (OSError, subprocess.CalledProcessError):
        dirty = dirty_env != "0" if dirty_env is not None else None
    return {"commit": commit or "unknown", "dirty": dirty}


def run_one(name: str, collector: Dict[str, object] | None = None, *, force: bool = False) -> Dict[str, object]:
    scraper = SOURCES[name]
    now = datetime.now(timezone.utc)
    stamp = now.isoformat()
    collector = collector or collector_provenance()
    source_provenance: Dict[str, object] = {
        "implementation": "sources.linkedin_local" if name == "linkedin" else "sources.jobspy_local",
    }
    if name == "glassdoor" and not force:
        state = _health_source(name)
        try:
            last_attempt = datetime.fromisoformat(
                str(state.get("last_attempt_at") or "").replace("Z", "+00:00")
            )
            if last_attempt.tzinfo is None:
                last_attempt = last_attempt.replace(tzinfo=timezone.utc)
        except (TypeError, ValueError):
            last_attempt = datetime.min.replace(tzinfo=timezone.utc)
        if state.get("healthy") is False and now - last_attempt < timedelta(hours=GLASSDOOR_RECOVERY_HOURS):
            return {
                "source": name, "status": "deferred", "source_healthy": False,
                "reason": "Glassdoor recovery probe deferred until 24 hours after the last attempt",
                "count": 0, "collector": collector, "source_provenance": source_provenance,
            }
    started = time.monotonic()
    search_control: Dict[str, object] = {}
    if name == "linkedin" and scraper is linkedin_local.scrape:
        limit, cooldown, probe = _linkedin_search_control(datetime.fromisoformat(stamp))
        search_control = {"cooldown_active": cooldown, "probe": probe}
    try:
        if name == "linkedin" and scraper is linkedin_local.scrape:
            result = (
                {"status": "blocked", "reason": "search cooldown", "jobs": [], "query_stats": [],
                 "requests": 0, "responses": 0, "http_status": 0}
                if search_control["cooldown_active"] else
                scraper(page_limit=limit, profile=os.environ.get("LOCAL_SOURCE_PROFILE", "github"))
            )
        else:
            result = scraper()
    except SourceUnavailable as exc:
        print(f"[{name}] SKIP (blocked/unavailable): {exc} -> keeping last good snapshot")
        return {"source": name, "status": "skipped_unavailable", "source_healthy": False, "reason": str(exc), "count": 0, "attempted_at": stamp, "collector": collector, "source_provenance": source_provenance}
    except Exception as exc:  # noqa: BLE001
        print(f"[{name}] SKIP (unexpected {type(exc).__name__}): {exc} -> keeping last good snapshot")
        return {"source": name, "status": "skipped_error", "source_healthy": False, "reason": str(exc), "count": 0, "attempted_at": stamp, "collector": collector, "source_provenance": source_provenance}

    rows = list(result.get("jobs") or [])
    query_stats = list(result.get("query_stats") or [])
    source_provenance = dict(result.get("provenance") or source_provenance)
    search_collection = {
        **search_control,
        "requests": int(result.get("requests", 0) or 0),
        "responses": int(result.get("responses", 0) or 0),
        "pages_fetched": int(result.get("pages_fetched", 0) or 0),
        "rate_limited": int(result.get("http_status") or 0) == 429,
        "budget_exhausted": any(stat.get("stop_reason") == "global_page_budget" for stat in query_stats),
        "coverage_limited": bool(result.get("coverage_limited")),
    } if name == "linkedin" else {}
    # A bounded search cannot verify queries it never reached. Merge its
    # coverage just like a 429-limited run, without treating absence as removal.
    search_rate_limited = bool(name == "linkedin" and int(result.get("http_status") or 0) == 429)
    budget_partial = bool(name == "linkedin" and result.get("status") == "ok"
                          and search_collection["budget_exhausted"])
    focused_partial = bool(name == "linkedin" and result.get("status") == "ok"
                           and search_collection["coverage_limited"])
    partial = bool(rows and (search_rate_limited or budget_partial or focused_partial))
    partial_reason = (str(result.get("reason") or "rate limited") if search_rate_limited else
                      "search page budget exhausted" if budget_partial else "focused query coverage")
    if result.get("status") != "ok" and not partial:
        reason = str(result.get("reason") or result.get("status"))
        print(f"[{name}] SKIP ({reason}) -> keeping last good snapshot")
        return {
            "source": name, "status": "skipped_unavailable", "source_healthy": False, "reason": reason,
            "count": 0, "query_stats": query_stats, "search_collection": search_collection,
            "elapsed_seconds": round(time.monotonic() - started, 3),
            "attempted_at": stamp, "collector": collector, "source_provenance": source_provenance,
        }

    detail_enrichment: Dict[str, object] = {}
    official_enrichment: Dict[str, object] = {}
    official_context: Dict[str, object] = {}
    board_store: Dict[str, dict] = {}
    previous = read_source_snapshot_payload(name) if name in {"linkedin", "indeed"} else {}
    if name in {"linkedin", "indeed"} and rows and (name != "linkedin" or scraper is linkedin_local.scrape):
        try:
            official_context = coverage_reconcile.load_official_context()
        except (OSError, ValueError, json.JSONDecodeError):
            official_context = {}
        try:
            board_store = board.load_store()
        except (OSError, ValueError, json.JSONDecodeError):
            board_store = {}
        previous_jobs = list(previous.get("jobs") or [])
        previous_by_id = {str(job.get("job_id") or ""): job for job in previous_jobs if job.get("job_id")}
        board_store = {
            **{f"source-cache::{index}": job for index, job in enumerate(previous_jobs) if job.get("official_search_verified")},
            **({f"indeed-peer::{index}": job for index, job in enumerate(read_source_snapshot_payload("indeed").get("jobs") or [])}
               if name == "linkedin" else {}),
            **{f"remote-peer::{index}": job for index, job in enumerate(_remote_handoff_rows())
               if len(str(job.get("description") or "").strip()) >= board.THIN_JD_CHARS},
            **board_store,
        }
        resolver = official_jd_recovery.Resolver(
            search_limit=RECOVERY_SEARCH_LIMIT, page_limit=RECOVERY_PAGE_LIMIT,
        ) if os.environ.get("LOCAL_SOURCE_PROFILE") == "mac" else official_jd_recovery.Resolver()
        now = datetime.fromisoformat(stamp)
        pending = []
        for row in rows:
            if len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS:
                continue
            prior = previous_by_id.get(str(row.get("job_id") or ""), {})
            if resolver.recover(row, previous=prior, context=official_context, store=board_store,
                                now=now, cheap_only=True) == "pending":
                pending.append(row)
        pending.sort(key=lambda row: (
            bool(resolver.pattern_cache.get(official_jd_recovery.normalize_company_key(str(row.get("company") or "")))),
            official_jd_recovery._stamp(row.get("first_seen")) or datetime.min.replace(tzinfo=timezone.utc),
        ), reverse=True)
        for row in pending:
            prior = previous_by_id.get(str(row.get("job_id") or ""), {})
            resolver.recover(row, previous=prior, context=official_context, store=board_store, now=now)
        official_enrichment = {
            **dict(resolver.stats), "search_requests": resolver.search_requests,
            "search_provider": resolver.search_provider,
            "official_page_requests": resolver.page_requests,
            "remaining_no_jd": sum(len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS for row in rows),
        }
    if name != "linkedin":
        for row in rows:
            if len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS and not row.get("enrichment_failure_reason"):
                row["enrichment_status"] = "unresolved"
                row["enrichment_failure_reason"] = f"{name}_detail_missing_or_thin"
    if name == "linkedin" and rows:
        detail_candidates = [row for row in rows if row.get("jd_tentative") or len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS]
        if official_context:
            _mark_linkedin_official_matches(
                detail_candidates, list(previous.get("jobs") or []), official_context, board_store,
            )
        detail_limit, cooldown_active, probe = _linkedin_detail_control(
            datetime.fromisoformat(stamp)
        )
        detail_enrichment = linkedin_local.enrich_details(
            detail_candidates,
            previous_jobs=list(previous.get("jobs") or []),
            allow_requests=not search_rate_limited and not cooldown_active,
            request_limit=detail_limit,
            min_description_chars=board.THIN_JD_CHARS,
            cooldown=cooldown_active,
            probe=probe,
        )
        detail_enrichment["cooldown_active"] = cooldown_active
        detail_enrichment["probe"] = probe
        detail_enrichment["status"] = "cooldown" if cooldown_active else "probe" if probe else "active"
        if cooldown_active:
            detail_enrichment["cooldown_until"] = str(_linkedin_runner_state().get("detail_cooldown_until") or "")

    # Every discovered record reaches enrichment before filtering.
    stage1_survivors = []
    for row in rows:
        keep, _reason = board.hard_filter(row)
        if keep:
            stage1_survivors.append(row)
    for stat in query_stats:
        matches = [
            row for row in stage1_survivors
            if stat["query"] in (row.get("discovery_queries") or {}).get(name, [])
        ]
        stat["first_pass_survivors"] = len(matches)
        stat["jds_resolved"] = sum(bool(row.get("description")) for row in matches)

    # Keep full aggregator JDs in the Board store. Original-employer resolution
    # remains independent and may still replace them with verified employer data.
    for row in stage1_survivors:
        if row.get("description") and not row.get("jd_tentative"):
            row["direct_original_fetched"] = True

    survivors = stage1_survivors

    if not survivors and not partial:
        print(f"[{name}] SKIP (0 first-pass survivors) -> keeping last good snapshot")
        return {
            "source": name, "status": "skipped_empty", "source_healthy": False, "reason": "0 first-pass survivors", "count": 0,
            "query_stats": query_stats, "detail_enrichment": detail_enrichment, "official_enrichment": official_enrichment, "search_collection": search_collection,
            "elapsed_seconds": round(time.monotonic() - started, 3),
            "attempted_at": stamp, "collector": collector, "source_provenance": source_provenance,
        }

    elapsed = round(time.monotonic() - started, 3)
    meta = {
        "snapshot_schema_version": SNAPSHOT_SCHEMA_VERSION,
        "scraped_at": stamp,
        "collector": collector,
        "source_provenance": source_provenance,
        "elapsed_seconds": elapsed,
        "query_stats": query_stats,
    }
    if detail_enrichment:
        meta["detail_enrichment"] = detail_enrichment
    if official_enrichment:
        meta["official_enrichment"] = official_enrichment
    carried_count = 0
    if partial:
        fresh_keys = {board.dedup_key(job) for job in survivors}
        carried_count = sum(
            1 for job in read_source_snapshot_payload(name).get("jobs") or []
            if board.dedup_key(job) not in fresh_keys
        )
        meta.update({
            "partial": True,
            "blocked_reason": partial_reason,
            "collected_count": len(rows),
            "carried_count": carried_count,
        })
    path = write_source_snapshot(name, survivors, meta=meta, merge_previous=partial)
    if partial:
        merged_count = len(survivors) + carried_count
        print(
            f"[{name}] PARTIAL {len(survivors)} fresh + {carried_count} carried = {merged_count} rows "
            f"({elapsed:.1f}s; {partial_reason}) -> {path}"
        )
        return {
            "source": name, "status": "partial", "source_healthy": False, "data_usable": True,
            "reason": partial_reason,
            "count": len(survivors), "collected_count": len(rows), "fresh_kept": len(survivors),
            "carried_count": carried_count, "merged_count": merged_count, "path": str(path),
            "query_stats": query_stats, "detail_enrichment": detail_enrichment, "official_enrichment": official_enrichment, "search_collection": search_collection,
            "elapsed_seconds": elapsed,
            "attempted_at": stamp, "partial_at": stamp, "collector": collector,
            "source_provenance": source_provenance,
        }
    detail_note = ""
    if detail_enrichment:
        detail_note = (
            f"; detail requests {detail_enrichment.get('requests', 0)}, "
            f"cache {detail_enrichment.get('cache_reused', 0)}, "
            f"JDs {detail_enrichment.get('jds_resolved', 0)}"
        )
    print(f"[{name}] OK {len(survivors)} rows ({elapsed:.1f}s{detail_note}) -> {path}")
    return {
        "source": name, "status": "ok", "source_healthy": True, "count": len(survivors), "path": str(path),
        "query_stats": query_stats, "detail_enrichment": detail_enrichment, "official_enrichment": official_enrichment, "search_collection": search_collection,
        "elapsed_seconds": elapsed,
        "attempted_at": stamp, "succeeded_at": stamp, "collector": collector,
        "source_provenance": source_provenance,
    }


def write_health(results: list[Dict[str, object]], collector: Dict[str, object]) -> None:
    if not any(result.get("status") != "deferred" for result in results):
        return
    try:
        previous = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        previous = {}
    previous_sources = previous.get("sources", {}) if isinstance(previous, dict) else {}
    sources = dict(previous_sources) if isinstance(previous_sources, dict) else {}
    for result in results:
        if result.get("status") == "deferred":
            continue
        name = str(result["source"])
        prior = sources.get(name, {}) if isinstance(sources.get(name), dict) else {}
        snapshot = read_source_snapshot_payload(name)
        snapshot_meta = snapshot.get("meta", {})
        healthy = bool(result.get("source_healthy", result.get("status") == "ok"))
        partial = result.get("status") == "partial"
        reason = str(result.get("reason") or "")
        search = result.get("search_collection") or {}
        if name == "linkedin" and partial and not search.get("rate_limited"):
            failure_cause = ""
        elif "429" in reason or search.get("rate_limited"):
            failure_cause = "429"
        elif "403" in reason:
            failure_cause = "403"
        elif "timeout" in reason.lower() or "timed out" in reason.lower():
            failure_cause = "timeout"
        elif healthy:
            failure_cause = ""
        else:
            failure_cause = "collection"
        prior_reason = str(prior.get("reason") or "")
        prior_cause = str(prior.get("failure_cause") or (
            "429" if "429" in prior_reason else "403" if "403" in prior_reason else
            "timeout" if "timeout" in prior_reason.lower() or "timed out" in prior_reason.lower() else ""
        ))
        prior_streak = int(prior.get("consecutive_failures", 0) or 0)
        if name == "linkedin" and not prior.get("failure_cause"):
            prior_streak = int((prior.get("runner_states") or {}).get("mac", {}).get("search_429_streak", 0) or 0)
            if prior_cause != "429":
                prior_streak = 0  # Legacy generic streak includes focused coverage.
        failure_streak = (prior_streak + 1 if prior_cause == failure_cause else 1) if failure_cause else 0
        # ``last_success_at`` means a complete collection that verified the
        # whole snapshot. A partial run rewrites the snapshot, so its
        # ``scraped_at`` must never be adopted as a full success.
        snapshot_full_success = "" if snapshot_meta.get("partial") else str(snapshot_meta.get("scraped_at", ""))
        state = dict(prior)
        state.update({
            "required": name not in OPTIONAL_SOURCES,
            "healthy": healthy,
            "status": result.get("status", "unknown"),
            "reason": reason if partial or failure_cause else "",
            "last_attempt_at": result.get("attempted_at", ""),
            "last_success_at": result.get("succeeded_at") or prior.get("last_success_at") or snapshot_full_success,
            "last_partial_at": result.get("partial_at") or prior.get("last_partial_at") or "",
            "partial_collected_count": int(
                (result.get("collected_count") if partial else prior.get("partial_collected_count")) or 0
            ),
            "partial_fresh_kept": int(
                (result.get("fresh_kept") if partial else prior.get("partial_fresh_kept")) or 0
            ),
            "partial_carried_count": int(
                (result.get("carried_count") if partial else prior.get("partial_carried_count")) or 0
            ),
            "last_attempt_collector": collector,
            "last_success_collector": collector if healthy else prior.get("last_success_collector") or snapshot_meta.get("collector", {}),
            "last_attempt_source_provenance": result.get("source_provenance", {}),
            "last_success_source_provenance": result.get("source_provenance", {}) if healthy else prior.get("last_success_source_provenance") or snapshot_meta.get("source_provenance", {}),
            "last_attempt_count": int(result.get("count", 0) or 0),
            "last_attempt_elapsed_seconds": result.get("elapsed_seconds"),
            "consecutive_failures": failure_streak,
            "failure_cause": failure_cause,
            "previous_failure": (
                {"cause": prior_cause, "count": prior_streak}
                if not failure_cause and prior_cause and prior_streak else {}
            ),
            "query_stats": list(result.get("query_stats") or []),
            "detail_enrichment": dict(result.get("detail_enrichment") or {}),
            "official_enrichment": dict(result.get("official_enrichment") or {}),
            "search_collection": dict(result.get("search_collection") or {}),
            "last_good_count": len(snapshot.get("jobs", [])),
        })
        if name == "linkedin":
            mac = os.environ.get("LOCAL_SOURCE_PROFILE") == "mac"
            prior_runtime = (prior.get("runner_states", {}).get("mac", {}) if mac else prior)
            if not isinstance(prior_runtime, dict):
                prior_runtime = {}
            runtime = dict(prior_runtime) if mac else state
            search = state["search_collection"]
            search_requests = int(search.get("requests", 0) or 0)
            if search_requests:
                runtime["search_last_attempt_at"] = result.get("attempted_at", "")
                if search.get("rate_limited"):
                    streak = int(prior_runtime.get("search_429_streak", 0) or 0) + 1
                    runtime["search_429_streak"] = streak
                    if streak >= 2:
                        attempted_at = datetime.fromisoformat(str(result.get("attempted_at") or "").replace("Z", "+00:00"))
                        runtime["search_cooldown_until"] = (attempted_at + timedelta(hours=LINKEDIN_SEARCH_COOLDOWN_HOURS)).isoformat()
                elif int(search.get("responses", 0) or 0):
                    runtime["search_429_streak"] = 0
                    runtime["search_cooldown_until"] = ""
            detail = state["detail_enrichment"]
            runtime["detail_status"] = str(detail.get("status") or prior_runtime.get("detail_status") or "active")
            if detail.get("cooldown_active"):
                runtime["detail_cooldown_reason"] = str(prior_runtime.get("detail_cooldown_reason") or "intentional pause")
            _update_linkedin_detail_health(
                runtime, detail,
                datetime.fromisoformat(str(result.get("attempted_at") or datetime.now(timezone.utc).isoformat()).replace("Z", "+00:00")),
            )
            if mac:
                runners = dict(state.get("runner_states") or {})
                runners["mac"] = runtime
                state["runner_states"] = runners
        sources[name] = state
    HEALTH_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": HEALTH_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "collector": collector,
        "sources": sources,
    }
    atomic_write(HEALTH_PATH, (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


def recover_jds() -> Dict[str, object]:
    """One bounded enrichment pass over current snapshots, without rediscovery."""
    started = time.monotonic()
    names = ("linkedin", "indeed", "remote_recovery")
    snapshots = {name: read_source_snapshot_payload(name) for name in names}
    remote_rows = _remote_handoff_rows()
    previous_remote = list(snapshots["remote_recovery"]["jobs"])
    if not remote_rows:
        remote_rows = [{**row, "remote_recovery": True} for row in previous_remote]
    previous_remote_by_key = {
        (str(row.get("source") or ""), str(row.get("job_id") or "")): row
        for row in previous_remote
    }
    for row in remote_rows:
        prior = previous_remote_by_key.get((str(row.get("source") or ""), str(row.get("job_id") or "")), {})
        if len(str(prior.get("description") or "").strip()) >= board.THIN_JD_CHARS and len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS:
            row["description"] = prior["description"]
            row["enrichment_method"] = prior.get("enrichment_method", "local_cache")
    snapshots["remote_recovery"]["jobs"] = remote_rows
    originals = {name: copy.deepcopy(snapshots[name]["jobs"]) for name in names}
    counts_before = {
        name: sum(len(str(job.get("description") or "").strip()) < board.THIN_JD_CHARS for job in originals[name])
        for name in names
    }
    now = datetime.now(timezone.utc)
    deadline = float("inf")
    context = coverage_reconcile.load_official_context()
    store = board.load_store()
    store = {
        **{f"source-cache::{name}::{index}": job
           for name in names for index, job in enumerate(originals[name]) if job.get("official_search_verified")},
        **{f"remote::{index}": job for index, job in enumerate(remote_rows)
           if len(str(job.get("description") or "").strip()) >= board.THIN_JD_CHARS},
        **store,
    }
    resolver = official_jd_recovery.Resolver(
        search_limit=RECOVERY_SEARCH_LIMIT,
        page_limit=RECOVERY_PAGE_LIMIT, deadline=deadline,
    )
    prior_by_id = {
        name: {str(job.get("job_id") or ""): job for job in originals[name] if job.get("job_id")}
        for name in names
    }
    pending = []
    cheap_counts: Dict[str, int] = {}
    for name in names:
        for row in snapshots[name]["jobs"]:
            if len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS:
                continue
            prior = prior_by_id[name].get(str(row.get("job_id") or ""), {})
            method = resolver.recover(row, previous=prior, context=context, store=store,
                                      now=now, cheap_only=True)
            if method == "pending":
                pending.append((name, row, prior))
            else:
                cheap_counts[method] = cheap_counts.get(method, 0) + 1
    pending.sort(key=lambda item: (
        bool(resolver.pattern_cache.get(official_jd_recovery.normalize_company_key(str(item[1].get("company") or "")))),
        official_jd_recovery._stamp(item[1].get("first_seen")) or datetime.min.replace(tzinfo=timezone.utc),
    ), reverse=True)
    methods: Dict[str, int] = {}
    processed = 0
    web_attempted_rows: set[int] = set()
    for name, row, prior in pending:
        if (time.monotonic() >= deadline or resolver.search_requests >= resolver.search_limit
                or resolver.page_requests >= resolver.page_limit):
            break
        method = resolver.recover(row, previous=prior, context=context, store=store, now=now)
        web_attempted_rows.add(id(row))
        methods[method] = methods.get(method, 0) + 1
        processed += 1
    linkedin_rows = [row for row in snapshots["linkedin"]["jobs"]
                     if len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS]
    if linkedin_rows:
        _mark_linkedin_official_matches(linkedin_rows, originals["linkedin"], context, store)
    detail_limit, cooldown, probe = _linkedin_detail_control(now)
    detail = linkedin_local.enrich_details(
        linkedin_rows, previous_jobs=originals["linkedin"],
        allow_requests=not cooldown and time.monotonic() < deadline,
        request_limit=min(detail_limit, LINKEDIN_DETAIL_LIMIT),
        min_description_chars=board.THIN_JD_CHARS,
        cooldown=cooldown,
        probe=probe,
    ) if linkedin_rows else {"requests": 0, "responses": 0, "rate_limited": False, "jds_resolved": 0}
    detail.update(cooldown_active=cooldown, probe=probe,
                  status="cooldown" if cooldown else "probe" if probe else "active")
    targeted_requests = 0
    targeted_matches = 0
    targeted_detail_jds = 0
    targeted_rate_limited = False
    if not cooldown and not detail.get("rate_limited") and time.monotonic() < deadline:
        remaining_detail = max(0, min(detail_limit, LINKEDIN_DETAIL_LIMIT) - int(detail.get("requests", 0) or 0))
        for name, row, _prior in pending:
            if (name != "remote_recovery" or id(row) not in web_attempted_rows
                    or targeted_requests >= 3 or not remaining_detail or time.monotonic() >= deadline):
                continue
            if len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS:
                continue
            card, rate_limited = linkedin_local.targeted_search(
                str(row.get("company") or ""), str(row.get("title") or ""), str(row.get("location") or ""),
            )
            targeted_requests += 1
            if rate_limited:
                targeted_rate_limited = True
                break
            if not card:
                continue
            targeted_matches += 1
            result = linkedin_local.enrich_details(
                [card], allow_requests=True, request_limit=1,
                min_description_chars=board.THIN_JD_CHARS,
            )
            remaining_detail -= int(result.get("requests", 0) or 0)
            if len(str(card.get("description") or "").strip()) >= board.THIN_JD_CHARS:
                row.update(description=card["description"], enrichment_method="targeted_linkedin_detail",
                           enrichment_status="resolved", linkedin_source_url=card.get("source_url", ""))
                targeted_detail_jds += 1
            if result.get("rate_limited"):
                targeted_rate_limited = True
                break
    after = {
        name: sum(len(str(job.get("description") or "").strip()) < board.THIN_JD_CHARS for job in snapshots[name]["jobs"])
        for name in names
    }
    changed = []
    for name in names:
        for row in snapshots[name]["jobs"]:
            row.pop("_linkedin_official_url", None)
            row.pop("_linkedin_official_defer", None)
        if name == "remote_recovery":
            recovered = [row for row in snapshots[name]["jobs"]
                         if row.get("enrichment_method") and len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS]
            snapshots[name]["jobs"] = recovered
            originals[name] = previous_remote
        if snapshots[name]["jobs"] == originals[name]:
            continue
        path = OUTPUT_DIR / "sources" / f"{name}.json"
        try:
            # Keep the persisted snapshot layout; the loader returns a reduced,
            # differently ordered view intended for consumers, not serialization.
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            payload = dict(snapshots[name])
        payload["jobs"] = snapshots[name]["jobs"]
        payload["source"] = name
        payload["count"] = len(payload["jobs"])
        payload["meta"] = {**payload.get("meta", {}), "jd_recovery_at": now.isoformat()}
        atomic_write(path, (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
        changed.append(name)
    if int(detail.get("requests", 0) or 0):
        # Keep collection freshness and other health fields unchanged.
        try:
            health = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            health = {"schema_version": HEALTH_SCHEMA_VERSION, "sources": {}}
        state = health.setdefault("sources", {}).setdefault("linkedin", {})
        state["detail_enrichment"] = detail
        _update_linkedin_detail_health(state, detail, now)
        state["detail_status"] = state.get("detail_status") or detail["status"]
        atomic_write(HEALTH_PATH, (json.dumps(health, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    report: Dict[str, object] = {
        "run_at": now.isoformat(), "before_no_jd": counts_before, "after_no_jd": after,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "before_total": sum(counts_before.values()), "after_total": sum(after.values()),
        "cheap_matches": cheap_counts, "methods": methods, "official_matches": dict(resolver.stats),
        "official_jds_recovered": sum(counts_before.values()) - sum(after.values()) - int(detail.get("jds_resolved", 0) or 0),
        "linkedin_detail_recoveries": int(detail.get("jds_resolved", 0) or 0),
        "linkedin_detail": detail, "search_requests": resolver.search_requests,
        "targeted_linkedin_search_requests": targeted_requests,
        "targeted_linkedin_matches": targeted_matches,
        "targeted_linkedin_detail_jds": targeted_detail_jds,
        "targeted_linkedin_rate_limited": targeted_rate_limited,
        "official_page_requests": resolver.page_requests, "generic_jobs_processed": processed,
        "search_provider": resolver.search_provider,
        "generic_jobs_deferred": len(pending) - processed, "changed_sources": changed,
        "glassdoor": "excluded",
    }
    log_path = OUTPUT_DIR / "logs" / "linkedin_jd_recovery_latest.json"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(log_path, (json.dumps(report, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    try:
        health = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        health = {"schema_version": HEALTH_SCHEMA_VERSION, "sources": {}}
    previous_targeted = int((health.get("local_recovery") or {}).get("targeted_429_streak", 0) or 0)
    targeted_streak = (previous_targeted + 1 if targeted_rate_limited else 0
                       if targeted_requests else previous_targeted)
    health["local_recovery"] = {key: report[key] for key in (
        "run_at", "elapsed_seconds", "official_jds_recovered", "linkedin_detail_recoveries",
        "targeted_linkedin_search_requests", "targeted_linkedin_detail_jds",
        "targeted_linkedin_rate_limited", "generic_jobs_processed",
        "search_requests", "official_page_requests",
    )}
    health["local_recovery"]["targeted_429_streak"] = targeted_streak
    atomic_write(HEALTH_PATH, (json.dumps(health, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local best-effort job sources")
    parser.add_argument("--only", choices=sorted(SOURCES.keys()), help="Run a single source")
    parser.add_argument("--recover-jds", action="store_true", help="Bounded JD recovery for current LinkedIn and Indeed snapshots")
    args = parser.parse_args()

    if args.recover_jds:
        recover_jds()
        return

    names = [args.only] if args.only else list(SOURCES.keys())
    collector = collector_provenance()
    results = [run_one(name, collector, force=args.only == "glassdoor") for name in names]
    write_health(results, collector)
    if not args.only and os.environ.get("LOCAL_SOURCE_PROFILE") == "mac":
        recover_jds()

    diagnostics_path = OUTPUT_DIR / "logs" / "local_sources_latest.json"
    diagnostics_path.parent.mkdir(parents=True, exist_ok=True)
    diagnostics_path.write_text(
        json.dumps({"run_at": datetime.now(timezone.utc).isoformat(), "sources": results}, indent=2) + "\n",
        encoding="utf-8",
    )

    ok = [r for r in results if r["status"] == "ok"]
    print(f"\nDone. {len(ok)}/{len(results)} source(s) updated: "
          + ", ".join(f"{r['source']}={r['status']}" for r in results))
    if names != ["glassdoor"] and not any(
        r["status"] in ("ok", "partial") and r["source"] not in OPTIONAL_SOURCES for r in results
    ):
        raise SystemExit("No required local source succeeded; last-good snapshots were preserved.")


if __name__ == "__main__":
    main()
