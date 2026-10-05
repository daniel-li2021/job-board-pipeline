#!/usr/bin/env python3
"""Run local best-effort job-board sources and snapshot them.

Each source is independent: if one hits a login wall / captcha / 403 / 429 /
network error, or returns zero rows, it is skipped and its previous
``output/sources/<name>.json`` snapshot is left untouched (never overwritten
with nothing). The other source and the downstream git sync proceed normally.

LinkedIn search remains card-first. Glassdoor arrives through JobSpy. Indeed
is collected on GitHub; its persisted snapshot is an exact JD peer here.

This is invoked by the Mac's fixed slots and missed-slot catch-up (see scripts/). It does NOT run the
full board pipeline and does NOT touch jobs.json / latest.md — those are
GitHub-Actions-owned to avoid local/CI git conflicts.

Usage:
    python3 local_sources.py                 # all sources
    python3 local_sources.py --only linkedin
    python3 local_sources.py --only glassdoor
    python3 local_sources.py --recover-jds
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
from pathlib import Path
from typing import Callable, Dict

import board_pipeline as board
import coverage_reconcile
import remote_recovery
import recovery_policy
import recovery_ai
from sources import jobspy_local, linkedin_local, official_jd_recovery
from sources.linkedin_transport import DETAIL_LIMIT
from sources.schema import (
    OUTPUT_DIR,
    SNAPSHOT_SCHEMA_VERSION,
    SourceUnavailable,
    read_source_snapshot_payload,
    assign_source_first_seen,
    record_source_first_seen,
    write_source_snapshot,
)

SOURCES: Dict[str, Callable[[], Dict[str, object]]] = {
    "linkedin": linkedin_local.scrape,
    "glassdoor": lambda: jobspy_local.scrape("glassdoor"),
}
OPTIONAL_SOURCES = {"glassdoor"}
HEALTH_PATH = OUTPUT_DIR / "sources" / "health.json"
HEALTH_SCHEMA_VERSION = 1
SOURCE_HISTORY_LIMIT = 120

LINKEDIN_DETAIL_LIMIT = DETAIL_LIMIT
MAC_SEARCH_PAGE_LIMIT = 10
LINKEDIN_DETAIL_COOLDOWN_HOURS = recovery_policy.LINKEDIN_DETAIL_COOLDOWN_HOURS
GLASSDOOR_RECOVERY_HOURS = 24
LINKEDIN_SEARCH_COOLDOWN_HOURS = 24
RECOVERY_SEARCH_LIMIT = 100
RECOVERY_PAGE_LIMIT = 150


def _linkedin_transport():
    return linkedin_local.LinkedInTransport(
        HEALTH_PATH, os.environ.get("LINKEDIN_TRANSPORT_STATE_PATH"))


def _persist_linkedin_runner_state(state):
    path = os.environ.get("LINKEDIN_TRANSPORT_STATE_PATH")
    if path:
        data = linkedin_local.LinkedInTransport._read(path)
        atomic_write(Path(path), (json.dumps({**data, "runner_state": state}, indent=2) + "\n").encode())


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
    runner = dict(runner) if isinstance(runner, dict) else {}
    # A failed push can discard the collector's Health update, but not local cooldowns.
    local = linkedin_local.LinkedInTransport._read(os.environ.get("LINKEDIN_TRANSPORT_STATE_PATH")).get("runner_state", {})
    for endpoint, keys in (
        ("search", ("search_last_attempt_at", "search_query_cursor", "search_429_streak", "search_cooldown_until")),
        ("detail", ("detail_last_attempt_at", "detail_429_streak", "detail_cooldown_until",
                    "detail_cooldown_reason", "detail_status", "detail_retry_after_until")),
    ):
        local_at = recovery_policy.stamp(local.get(f"{endpoint}_last_attempt_at"))
        saved_at = recovery_policy.stamp(runner.get(f"{endpoint}_last_attempt_at"))
        if local_at and (not saved_at or local_at > saved_at):
            runner.update({key: local[key] for key in keys if key in local})
    # Older follow-up recovery runs wrote detail state only at the top level.
    # Prefer the newer attempt so a Mac run cannot bypass that cooldown.
    detail_keys = ("detail_last_attempt_at", "detail_429_streak", "detail_cooldown_until",
                   "detail_cooldown_reason", "detail_status", "detail_retry_after_until")
    top_attempt = recovery_policy.stamp(state.get("detail_last_attempt_at"))
    mac_attempt = recovery_policy.stamp(runner.get("detail_last_attempt_at"))
    if top_attempt and (not mac_attempt or top_attempt > mac_attempt):
        runner.update({key: state[key] for key in detail_keys if key in state})
    attempt = recovery_policy.stamp(runner.get("detail_last_attempt_at"))
    until = recovery_policy.stamp(runner.get("detail_cooldown_until"))
    if attempt and until:
        runner["detail_cooldown_until"] = min(
            until, attempt + timedelta(hours=LINKEDIN_DETAIL_COOLDOWN_HOURS)
        ).isoformat()
        retry_until = recovery_policy.stamp(runner.get("detail_retry_after_until"))
        if retry_until:
            runner["detail_cooldown_until"] = max(retry_until, recovery_policy.stamp(runner["detail_cooldown_until"])).isoformat()
    return runner


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
    if detail.get("rate_limited"):
        state["detail_429_streak"] = int(state.get("detail_429_streak", 0) or 0) + 1
        state["detail_cooldown_until"] = (attempted_at + timedelta(hours=LINKEDIN_DETAIL_COOLDOWN_HOURS)).isoformat()
        retry_until = recovery_policy.stamp((detail.get("rate_limit_event") or {}).get("retry_after_until"))
        if retry_until:
            state["detail_retry_after_until"] = retry_until.isoformat()
            state["detail_cooldown_until"] = max(retry_until, recovery_policy.stamp(state["detail_cooldown_until"])).isoformat()
        state["detail_cooldown_reason"] = "HTTP 429"
        state["detail_status"] = "cooldown"
    elif int(detail.get("successful_responses", 0) or 0):
        state["detail_429_streak"] = 0
        state["detail_cooldown_until"] = ""
        state["detail_retry_after_until"] = ""
        state["detail_cooldown_reason"] = ""
        state["detail_status"] = "active"


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


def _linkedin_metadata_skip(row: dict, filters: dict) -> str:
    """Admission only: JD-dependent rejection and matching remain downstream."""
    if board.classify_company(str(row.get("company") or ""), filters, str(row.get("title") or ""))[0] == "exclude":
        return "company_excluded"
    if board.classify_location_bucket(str(row.get("location") or "")) == "non_us":
        return "non_us_location"
    metadata = {"title": row.get("title", ""), "description": ""}
    keep, reason = board.hard_filter(metadata)
    if not keep:
        return reason
    keep, reason = board.role_seniority_prefilter(metadata)
    if keep:
        return ""
    # Generic technical titles need JD evidence; lack of a software keyword is
    # insufficient proof of irrelevance (e.g. Engineer II / Research Engineer).
    title = str(row.get("title") or "")
    if reason == "prefilter:no_positive_family" and (
            board.TITLE_TECH_RE.search(title) or board.EARLY_CAREER_TITLE_RE.search(title)
            or "engineer" in title.casefold()):
        return ""
    return reason


def _linkedin_detail_waiting(row: dict) -> bool:
    return ((row.get("linkedin_detail_triage") or {}).get("needs_jd") is True
            and not row.get("linkedin_detail_attempted_at")
            and bool(row.get("linkedin_detail_deferred_at") or
                     row.get("enrichment_deferred_reason") == "linkedin_detail_round_budget"))


def _linkedin_detail_eligible(row: dict, now: datetime) -> bool:
    # A budget-deferred, already admitted card retains one opportunity through
    # Rolling. This does not refresh first_seen or broaden generic recovery.
    seen = recovery_policy.stamp(row.get("first_seen"))
    return recovery_policy.fresh(row, now) or bool(
        _linkedin_detail_waiting(row) and seen and timedelta(0) <= now - seen <= timedelta(hours=72))


def _linkedin_detail_sort_key(row: dict):
    return (
        -{"high": 2, "normal": 1, "low": 0}.get((row.get("linkedin_detail_triage") or {}).get("priority"), 1),
        not _linkedin_detail_waiting(row),
        recovery_policy.stamp(row.get("first_seen")) or datetime.max.replace(tzinfo=timezone.utc),
        recovery_policy.identity(row),
    )


def _prepare_linkedin_detail(rows: list[dict], previous: list[dict], now: datetime) -> tuple[list[dict], dict]:
    prior_by_id = {str(row.get("job_id") or ""): row for row in previous}
    for row in rows:
        prior = prior_by_id.get(str(row.get("job_id") or ""), {})
        if recovery_policy.evidence_hash(row) == recovery_policy.evidence_hash(prior):
            for field in ("linkedin_detail_triage", "linkedin_detail_triage_hash",
                          "linkedin_detail_deferred_at", "linkedin_detail_attempted_at",
                          "enrichment_deferred_reason"):
                if field not in row and field in prior:
                    row[field] = copy.deepcopy(prior[field])
    candidates = [row for row in rows if _linkedin_detail_eligible(row, now)
                  and (row.get("jd_tentative") or len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS)]
    filters = board.load_company_filters()
    eligible = []
    reasons: Dict[str, int] = {}
    for row in candidates:
        reason = _linkedin_metadata_skip(row, filters)
        if reason:
            reasons[reason] = reasons.get(reason, 0) + 1
            row["enrichment_deferred_reason"] = f"linkedin_detail_rules:{reason}"
        else:
            eligible.append(row)
    cached = linkedin_local.enrich_details(eligible, previous_jobs=previous,
                                           min_description_chars=board.THIN_JD_CHARS, cache_only=True)
    return eligible, {"candidates": len(candidates), "rules_skipped": sum(reasons.values()),
                      "rule_reasons": reasons, "cache_reused": cached.get("cache_reused", 0)}


def _finish_linkedin_detail(rows: list[dict], previous: list[dict], admission: dict,
                            budget: recovery_policy.RecoveryBudget, now: datetime,
                            *, blocked: bool = False,
                            transport: linkedin_local.LinkedInTransport | None = None) -> dict:
    """Last-resort admission and one Detail allowance for the whole Local round."""
    unresolved = [row for row in rows if row.get("jd_tentative")
                  or len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS]
    for row in unresolved:
        row.pop("_linkedin_official_defer", None)
        row.pop("_linkedin_official_url", None)
    admission["non_linkedin_resolved"] = len(rows) - len(unresolved) - admission["cache_reused"]
    limit, cooldown, probe = _linkedin_detail_control(now)
    if budget.linkedin_detail_limit is None:
        budget.linkedin_detail_limit = limit
    remaining = max(0, min(limit, budget.linkedin_detail_limit - budget.linkedin_detail_requests))
    allowed = (not blocked and not cooldown and budget.available() and remaining > 0
               and (transport is None or transport.available("detail", probe=probe)))
    admitted = []
    if allowed and unresolved:
        try:
            profile = board.load_profiles()
        except (OSError, ValueError, KeyError):
            profile = {}
        prior_by_id = {str(row.get("job_id") or ""): row for row in previous}
        to_triage = []
        for row in unresolved:
            fingerprint = recovery_policy.evidence_hash(
                row, "linkedin-detail-v1", profile.get("candidate_fingerprint", ""),
                json.dumps(row.get("recovery_methods") or {}, sort_keys=True),
                json.dumps(row.get("recovery_candidates") or []), bool(row.get("jd_tentative")),
            )
            prior = prior_by_id.get(str(row.get("job_id") or ""), {})
            if row.get("linkedin_detail_triage_hash") != fingerprint:
                row["linkedin_detail_triage"] = (prior.get("linkedin_detail_triage") or {}
                    if prior.get("linkedin_detail_triage_hash") == fingerprint else {})
                row["linkedin_detail_triage_hash"] = fingerprint
            if not row.get("linkedin_detail_triage"):
                to_triage.append(row)
        decisions = (recovery_ai.triage_linkedin_detail(to_triage, profile.get("candidate", ""))
                     if to_triage else {})
        for row in to_triage:
            row["linkedin_detail_triage"] = decisions.get(recovery_policy.identity(row), {})
        for row in unresolved:
            decision = row.get("linkedin_detail_triage") or {}
            if decision.get("needs_jd") is True:
                admitted.append(row)
                row.pop("enrichment_deferred_reason", None)
            else:
                row["enrichment_status"] = "tentative" if row.get("jd_tentative") else "deferred"
                row["enrichment_deferred_reason"] = (
                    "linkedin_detail_not_worthwhile" if decision.get("needs_jd") is False
                    else "linkedin_detail_triage_unavailable")
        admission["triage_evaluated"] = len(to_triage)
        admission["triage_deferred"] = len(unresolved) - len(admitted)
    if not allowed:
        admitted = [row for row in unresolved if (row.get("linkedin_detail_triage") or {}).get("needs_jd") is True]
    admission["worth_detail"] = len(admitted)
    admitted.sort(key=_linkedin_detail_sort_key)
    queue = [row for row in admitted if recovery_policy.identity(row) not in budget.linkedin_detail_attempted]
    # Existing cooldown/429 diagnostics still annotate unresolved cards without
    # spending requests or LLM calls while LinkedIn traffic is paused.
    if not blocked and not cooldown and not allowed:
        for row in unresolved:
            row["enrichment_deferred_reason"] = "linkedin_detail_round_budget"
    detail = linkedin_local.enrich_details(
        queue if allowed else unresolved if blocked or cooldown else [], previous_jobs=previous,
        allow_requests=allowed, request_limit=remaining, min_description_chars=board.THIN_JD_CHARS,
        cooldown=cooldown, probe=probe, budget=budget, transport=transport,
    )
    budget.linkedin_detail_requests += int(detail.get("requests", 0) or 0)
    attempted_ids = set(detail.get("attempted_ids") or [])
    budget.linkedin_detail_attempted.update(recovery_policy.identity(row) for row in queue
                                           if str(row.get("job_id")) in attempted_ids)
    deferred_reason = (detail.get("transport_stop_reason") or
                       (transport.stop_reason if transport is not None else "") or
                       ("recovery_job_budget" if not budget.available() else "linkedin_detail_round_budget"))
    waiting = []
    for row in admitted:
        if (str(row.get("job_id")) not in attempted_ids and not row.get("linkedin_detail_attempted_at")
                and not blocked and not cooldown and not detail.get("rate_limited")
                and (detail.get("budget_exhausted") or not allowed)):
            row.setdefault("linkedin_detail_deferred_at", now.isoformat())
            row["enrichment_status"] = "deferred"
            row["enrichment_deferred_reason"] = deferred_reason
            waiting.append(row)
    if not allowed and waiting:
        detail["budget_deferred"] = len(waiting)
        detail["budget_exhausted"] = True
        detail["transport_stop_reason"] = deferred_reason
    detail["queue"] = [{
        "job_id": str(row.get("job_id") or ""), "first_seen": row.get("first_seen"),
        "priority": (row.get("linkedin_detail_triage") or {}).get("priority", "normal"),
        "needs_jd": (row.get("linkedin_detail_triage") or {}).get("needs_jd"),
        "deferred_at": row.get("linkedin_detail_deferred_at"),
        "attempted_at": row.get("linkedin_detail_attempted_at"),
        "attempted_this_phase": str(row.get("job_id")) in attempted_ids,
        "resolved": not row.get("jd_tentative") and len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS,
        "method": row.get("enrichment_method"), "deferred_reason": row.get("enrichment_deferred_reason"),
        "past_fresh": not recovery_policy.fresh(row, now),
    } for row in rows]
    detail.update(admission=admission, cooldown_active=cooldown, probe=probe,
                  round_request_limit=budget.linkedin_detail_limit,
                  round_requests=budget.linkedin_detail_requests,
                  status="cooldown" if cooldown or detail.get("rate_limited") else "probe" if probe else "active")
    detail["cache_reused"] = admission["cache_reused"]
    if cooldown:
        detail["cooldown_until"] = str(_linkedin_runner_state().get("detail_cooldown_until") or "")
    return detail


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


def run_one(name: str, collector: Dict[str, object] | None = None, *, force: bool = False,
            scraper: Callable[[], Dict[str, object]] | None = None,
            recover_missing: bool = True,
            budget: recovery_policy.RecoveryBudget | None = None,
            transport: linkedin_local.LinkedInTransport | None = None) -> Dict[str, object]:
    scraper = scraper or SOURCES[name]
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
    budget = budget or recovery_policy.RecoveryBudget()
    search_control: Dict[str, object] = {}
    if name == "linkedin" and scraper is linkedin_local.scrape:
        transport = transport or _linkedin_transport()
        previous_search = read_source_snapshot_payload(name)
        known_identities = set(previous_search.get("first_seen_ledger") or {})
        known_identities.update(recovery_policy.identity(row) for row in previous_search.get("jobs") or [])
        limit, cooldown, probe = _linkedin_search_control(datetime.fromisoformat(stamp))
        transport_paused = not transport.available("search")
        cooldown = cooldown or transport_paused
        search_control = {"cooldown_active": cooldown, "probe": probe,
                          "query_cursor": int(_linkedin_runner_state().get("search_query_cursor", 0) or 0)}
    try:
        if name == "linkedin" and scraper is linkedin_local.scrape:
            result = (
                {"status": "blocked", "reason": transport.stop_reason if transport_paused else "search cooldown",
                 "jobs": [], "query_stats": [],
                 "requests": 0, "responses": 0, "http_status": 0,
                 "transport_stop_reason": transport.stop_reason if transport_paused else ""}
                if search_control["cooldown_active"] else
                scraper(page_limit=limit, profile=os.environ.get("LOCAL_SOURCE_PROFILE", "github"),
                        query_cursor=search_control["query_cursor"], known_identities=known_identities,
                        transport=transport)
            )
        else:
            result = scraper()
    except SourceUnavailable as exc:
        print(f"[{name}] SKIP (blocked/unavailable): {exc} -> keeping last good snapshot")
        return {"source": name, "status": "skipped_unavailable", "source_healthy": False, "reason": str(exc), "count": 0, "elapsed_seconds": round(time.monotonic() - started, 3), "attempted_at": stamp, "collector": collector, "source_provenance": source_provenance}
    except Exception as exc:  # noqa: BLE001
        print(f"[{name}] SKIP (unexpected {type(exc).__name__}): {exc} -> keeping last good snapshot")
        return {"source": name, "status": "skipped_error", "source_healthy": False, "reason": str(exc), "count": 0, "elapsed_seconds": round(time.monotonic() - started, 3), "attempted_at": stamp, "collector": collector, "source_provenance": source_provenance}

    rows = list(result.get("jobs") or [])
    if rows:
        previous_snapshot = read_source_snapshot_payload(name)
        assign_source_first_seen(rows, previous_snapshot.get("jobs", []), stamp,
                                 previous_snapshot.get("first_seen_ledger", {}))
    query_stats = list(result.get("query_stats") or [])
    source_provenance = dict(result.get("provenance") or source_provenance)
    search_collection = {
        **search_control,
        "requests": int(result.get("requests", 0) or 0),
        "responses": int(result.get("responses", 0) or 0),
        "pages_fetched": int(result.get("pages_fetched", 0) or 0),
        "http_status": int(result.get("http_status") or 0),
        "rate_limited": int(result.get("http_status") or 0) == 429,
        "budget_exhausted": any(stat.get("stop_reason") in {
            "global_page_budget", "global_round_budget", "global_hour_budget", "global_day_budget",
        } for stat in query_stats),
        "rate_limit_event": result.get("rate_limit_event") or {},
        "transport_stop_reason": result.get("transport_stop_reason") or "",
        "new_to_ledger": sum(stat.get("new_to_ledger", 0) for stat in query_stats),
        "rediscovered": sum(stat.get("rediscovered", 0) for stat in query_stats),
        "coverage_limited": bool(result.get("coverage_limited")),
    } if name == "linkedin" else {}
    # A bounded search cannot verify queries it never reached. Merge its
    # coverage just like a 429-limited run, without treating absence as removal.
    search_rate_limited = bool(name == "linkedin" and int(result.get("http_status") or 0) == 429)
    budget_partial = bool(name == "linkedin" and result.get("status") == "ok"
                          and search_collection["budget_exhausted"])
    focused_partial = bool(name == "linkedin" and result.get("status") == "ok"
                           and search_collection["coverage_limited"])
    indeed_partial = name == "indeed" and result.get("status") != "ok" and bool(rows)
    partial = bool(rows and (search_rate_limited or budget_partial or focused_partial or indeed_partial))
    partial_reason = (str(result.get("reason") or "collection failed") if indeed_partial else
                      str(result.get("reason") or "rate limited") if search_rate_limited else
                      "search page budget exhausted" if budget_partial else "focused query coverage")
    if result.get("status") != "ok" and not partial:
        reason = str(result.get("reason") or result.get("status"))
        print(f"[{name}] SKIP ({reason}) -> keeping last good snapshot")
        return {
            "source": name, "status": "cooldown" if search_control.get("cooldown_active") else "skipped_unavailable",
            "source_healthy": False, "reason": reason,
            "data_usable": bool(read_source_snapshot_payload(name).get("jobs")),
            "count": 0, "query_stats": query_stats, "search_collection": search_collection,
            "elapsed_seconds": round(time.monotonic() - started, 3),
            "attempted_at": stamp, "collector": collector, "source_provenance": source_provenance,
        }

    detail_enrichment: Dict[str, object] = {}
    official_enrichment: Dict[str, object] = {}
    official_context: Dict[str, object] = {}
    board_store: Dict[str, dict] = {}
    previous = read_source_snapshot_payload(name) if name in {"linkedin", "indeed"} else {}
    carried_queue = []
    if name == "linkedin":
        discovered_ids = {recovery_policy.identity(row) for row in rows}
        carried_queue = [copy.deepcopy(row) for row in previous.get("jobs") or []
                         if recovery_policy.identity(row) not in discovered_ids
                         and _linkedin_detail_eligible(row, now)
                         and (row.get("linkedin_detail_triage") or {}).get("needs_jd") is True
                         and (row.get("jd_tentative") or len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS)]
        old_cards = [row for row in rows if not recovery_policy.fresh(row, now)
                     and len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS]
        if old_cards:
            linkedin_local.enrich_details(old_cards, previous_jobs=list(previous.get("jobs") or []),
                                          min_description_chars=board.THIN_JD_CHARS, cache_only=True)
    linkedin_candidates, detail_admission = (_prepare_linkedin_detail(rows + carried_queue, list(previous.get("jobs") or []), now)
                                             if name == "linkedin" else ([], {}))
    if indeed_partial:
        previous_by_key = {board.dedup_key(job): job for job in previous.get("jobs") or []}
        for row in rows:
            prior = previous_by_key.get(board.dedup_key(row), {})
            if len(str(prior.get("description") or "")) > len(str(row.get("description") or "")):
                row["description"] = prior["description"]
    if recover_missing and name in {"linkedin", "indeed"} and rows and (name != "linkedin" or scraper is linkedin_local.scrape):
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
            budget=budget if name == "linkedin" else None,
        ) if os.environ.get("LOCAL_SOURCE_PROFILE") == "mac" else official_jd_recovery.Resolver(
            budget=budget if name == "linkedin" else None,
        )
        now = datetime.fromisoformat(stamp)
        pending = []
        linkedin_eligible = {id(row) for row in linkedin_candidates}
        for row in rows + carried_queue:
            if len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS:
                continue
            prior = previous_by_id.get(str(row.get("job_id") or ""), {})
            if (resolver.recover(row, previous=prior, context=official_context, store=board_store,
                                 now=now, cheap_only=True) == "pending"
                    and (name != "linkedin" or recovery_policy.fresh(row, now))
                    and (name != "linkedin" or id(row) in linkedin_eligible)):
                pending.append(row)
        pending.sort(key=lambda row: (
            bool(resolver.pattern_cache.get(official_jd_recovery.normalize_company_key(str(row.get("company") or "")))),
            official_jd_recovery._stamp(row.get("first_seen")) or datetime.min.replace(tzinfo=timezone.utc),
        ), reverse=True)
        if name == "linkedin":
            official_jd_recovery.recover_pending(
                resolver, [(row, previous_by_id.get(str(row.get("job_id") or ""), {})) for row in pending],
                context=official_context, store=board_store, now=now,
            )
        else:
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
        detail_enrichment = _finish_linkedin_detail(
            linkedin_candidates, list(previous.get("jobs") or []), detail_admission,
            budget, now, blocked=search_rate_limited, transport=transport,
        )

    # Admission skips retain cards for the existing downstream filters.
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
        record_source_first_seen(name, rows)
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
    if name == "linkedin":
        meta["search_collection"] = search_collection
    if detail_enrichment:
        meta["detail_enrichment"] = detail_enrichment
    if official_enrichment:
        meta["official_enrichment"] = official_enrichment
    carried_count = 0
    if partial:
        fresh_keys = {board.dedup_key(job) for job in survivors}
        prior_meta = previous.get("meta") or {}
        carried_count = sum(
            1 for job in read_source_snapshot_payload(name).get("jobs") or []
            if board.dedup_key(job) not in fresh_keys
        )
        meta.update({
            "partial": True,
            "blocked_reason": partial_reason,
            "collected_count": len(rows),
            "carried_count": carried_count,
            "last_full_snapshot_at": (prior_meta.get("last_full_snapshot_at") if prior_meta.get("partial")
                                      else prior_meta.get("scraped_at")) or "",
            "last_full_collector": (prior_meta.get("last_full_collector") if prior_meta.get("partial")
                                    else prior_meta.get("collector")) or {},
            "last_full_source_provenance": (prior_meta.get("last_full_source_provenance") if prior_meta.get("partial")
                                            else prior_meta.get("source_provenance")) or {},
        })
    if name == "indeed":
        meta.update({key: int(result.get(key, 0) or 0) for key in
                     ("queries_total", "queries_succeeded", "queries_failed", "queries_not_run")})
    path = write_source_snapshot(name, survivors, meta=meta, merge_previous=partial,
                                 observed_jobs=rows, carried_updates=carried_queue)
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
            "queries_total": meta.get("queries_total", 0), "queries_succeeded": meta.get("queries_succeeded", 0),
            "queries_failed": meta.get("queries_failed", 0), "queries_not_run": meta.get("queries_not_run", 0),
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
        "queries_total": meta.get("queries_total", 0), "queries_succeeded": meta.get("queries_succeeded", 0),
        "queries_failed": meta.get("queries_failed", 0), "queries_not_run": meta.get("queries_not_run", 0),
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
    history = list(previous.get("run_history") or []) if isinstance(previous, dict) else []
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
        cooling = name == "linkedin" and result.get("status") == "cooldown"
        if cooling or (name == "linkedin" and partial and not search.get("rate_limited")):
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
            "reason": reason if partial or failure_cause or cooling else "",
            "last_attempt_at": result.get("attempted_at", ""),
            "last_success_at": (result.get("succeeded_at") or prior.get("last_success_at")
                                or snapshot_meta.get("last_full_snapshot_at") or snapshot_full_success),
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
            "queries_total": int(result.get("queries_total", 0) or 0),
            "queries_succeeded": int(result.get("queries_succeeded", 0) or 0),
            "queries_failed": int(result.get("queries_failed", 0) or 0),
            "queries_not_run": int(result.get("queries_not_run", 0) or 0),
            "last_attempt_collector": collector,
            "last_success_collector": collector if healthy else prior.get("last_success_collector") or snapshot_meta.get("last_full_collector", {}) or snapshot_meta.get("collector", {}),
            "last_attempt_source_provenance": result.get("source_provenance", {}),
            "last_success_source_provenance": result.get("source_provenance", {}) if healthy else prior.get("last_success_source_provenance") or snapshot_meta.get("last_full_source_provenance", {}) or snapshot_meta.get("source_provenance", {}),
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
            prior_runtime = _linkedin_runner_state() if mac else prior
            if not isinstance(prior_runtime, dict):
                prior_runtime = {}
            runtime = dict(prior_runtime) if mac else state
            search = state["search_collection"]
            search_requests = int(search.get("requests", 0) or 0)
            if search_requests:
                runtime["search_last_attempt_at"] = result.get("attempted_at", "")
                runtime["search_query_cursor"] = int(search.get("query_cursor", 0) or 0) + 1
                if search.get("rate_limited"):
                    streak = int(prior_runtime.get("search_429_streak", 0) or 0) + 1
                    runtime["search_429_streak"] = streak
                    if streak >= 2:
                        attempted_at = datetime.fromisoformat(str(result.get("attempted_at") or "").replace("Z", "+00:00"))
                        runtime["search_cooldown_until"] = (attempted_at + timedelta(hours=LINKEDIN_SEARCH_COOLDOWN_HOURS)).isoformat()
                    retry_until = recovery_policy.stamp((search.get("rate_limit_event") or {}).get("retry_after_until"))
                    if retry_until:
                        runtime["search_cooldown_until"] = max(retry_until, recovery_policy.stamp(runtime.get("search_cooldown_until")) or retry_until).isoformat()
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
                _persist_linkedin_runner_state(runtime)
                runners["mac"] = runtime
                state["runner_states"] = runners
                for key in ("detail_last_attempt_at", "detail_429_streak", "detail_cooldown_until",
                            "detail_cooldown_reason", "detail_status", "detail_retry_after_until"):
                    if key in runtime:
                        state[key] = runtime[key]
        sources[name] = state
        attempt_at = str(result.get("attempted_at") or "")
        if attempt_at:
            snapshot_at = str(snapshot_meta.get("scraped_at") or "")
            new_jobs = (sum(str(job.get("first_seen") or "") == attempt_at
                            for job in snapshot.get("jobs") or [])
                        if snapshot_at == attempt_at else
                        None if result.get("status") in {"ok", "partial"} else 0)
            detail = result.get("detail_enrichment") or {}
            failure = bool(failure_cause or detail.get("rate_limited") or detail.get("failed"))
            record = {
                "source": name, "run_at": attempt_at, "status": result.get("status", "unknown"),
                "new": new_jobs, "pass": result.get("pass"), "new_ab": result.get("new_ab"),
                "failure": failure, "reason": (reason or str(detail.get("blocked") or "JD detail failed")) if failure or cooling else "",
                "search_429": bool(search.get("rate_limited")), "detail_429": bool(detail.get("rate_limited")),
                "elapsed_seconds": result.get("elapsed_seconds"),
                "search_requests": int(search.get("requests", 0) or 0) if name == "linkedin" else None,
                "initial_detail_requests": int(detail.get("requests", 0) or 0) if name == "linkedin" else None,
                "new_to_ledger": search.get("new_to_ledger") if name == "linkedin" else None,
                "rediscovered": search.get("rediscovered") if name == "linkedin" else None,
            }
            history = [item for item in history if not (
                item.get("source") == name and item.get("run_at") == attempt_at)]
            history.append(record)
    history.sort(key=lambda item: str(item.get("run_at") or ""), reverse=True)
    HEALTH_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        **previous,
        "schema_version": HEALTH_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "collector": collector,
        "sources": sources,
        "run_history": history[:SOURCE_HISTORY_LIMIT],
    }
    atomic_write(HEALTH_PATH, (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


def recover_jds(*, budget: recovery_policy.RecoveryBudget | None = None,
                linkedin_blocked: bool = False,
                transport: linkedin_local.LinkedInTransport | None = None,
                initial_detail: dict | None = None) -> Dict[str, object]:
    """Recover only Fresh unresolved cards, sharing the Mac outbound budget."""
    started = time.monotonic()
    transport = transport or _linkedin_transport()
    budget = budget or recovery_policy.RecoveryBudget()
    now = datetime.now(timezone.utc)
    names = ("linkedin", "remote_recovery")
    snapshots = {name: read_source_snapshot_payload(name) for name in names}
    remote_path = OUTPUT_DIR / "sources" / "remote_recovery.json"
    try:
        remote_payload = json.loads(remote_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError, OSError):
        remote_payload = {}
    previous_attempts = remote_payload.get("attempts") or {}
    previous_remote = list(snapshots["remote_recovery"]["jobs"])
    remote_rows = _remote_handoff_rows()
    if not remote_rows:
        remote_rows = [{**row, "remote_recovery": True} for row in previous_remote]
    previous_remote_by_key = {recovery_policy.identity(row): row for row in previous_remote}
    for row in remote_rows:
        key = recovery_policy.identity(row)
        prior = previous_remote_by_key.get(key) or previous_attempts.get(key) or {}
        if not row.get("first_seen") and prior.get("first_seen"):
            row["first_seen"] = prior["first_seen"]
        for field in ("recovery_methods", "recovery_candidates", "recovery_triage", "recovery_input_hash"):
            if not row.get(field) and prior.get(field):
                row[field] = prior[field]
        if (len(str(prior.get("description") or "").strip()) >= board.THIN_JD_CHARS
                and len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS):
            row["description"] = prior["description"]
            row["enrichment_method"] = prior.get("enrichment_method", "local_cache")
    snapshots["remote_recovery"]["jobs"] = remote_rows
    originals = {name: copy.deepcopy(snapshots[name]["jobs"]) for name in names}
    before = {name: sum(len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS
                        for row in originals[name]) for name in names}
    blocked_before_recovery = linkedin_blocked
    context = coverage_reconcile.load_official_context()
    store = board.load_store()
    store = {
        **{f"source-cache::{name}::{i}": row for name in names for i, row in enumerate(originals[name])
           if row.get("official_search_verified")},
        **{f"remote::{i}": row for i, row in enumerate(remote_rows)
           if len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS},
        **{f"indeed-peer::{i}": row for i, row in enumerate(read_source_snapshot_payload("indeed").get("jobs") or [])
           if len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS},
        **store,
    }
    resolver = official_jd_recovery.Resolver(search_limit=RECOVERY_SEARCH_LIMIT,
                                             page_limit=RECOVERY_PAGE_LIMIT, budget=budget)
    prior_by_id = {
        name: {str(row.get("job_id") or ""): row for row in originals[name] if row.get("job_id")}
        for name in names
    }
    linkedin_candidates, detail_admission = _prepare_linkedin_detail(
        snapshots["linkedin"]["jobs"], originals["linkedin"], now,
    )
    linkedin_eligible = {id(row) for row in linkedin_candidates}
    cheap_counts: Dict[str, int] = {}
    for name in names:
        for row in snapshots[name]["jobs"]:
            if name == "linkedin" and id(row) not in linkedin_eligible:
                continue
            if ((name != "linkedin" and not recovery_policy.fresh(row, now))
                    or len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS):
                continue
            prior = prior_by_id[name].get(str(row.get("job_id") or ""), {})
            method = resolver.recover(row, previous=prior, context=context, store=store,
                                      now=now, cheap_only=True)
            if method != "pending":
                cheap_counts[method] = cheap_counts.get(method, 0) + 1

    pending: list[tuple[dict, dict]] = []
    for name in names:
        for row in snapshots[name]["jobs"]:
            if name == "linkedin" and id(row) not in linkedin_eligible:
                continue
            if (not recovery_policy.fresh(row, now)
                    or len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS):
                continue
            prior = prior_by_id[name].get(str(row.get("job_id") or ""), {})
            if resolver.recover(row, previous=prior, context=context, store=store,
                                now=now, cheap_only=True) != "pending":
                continue
            probe_row = dict(row)
            if name != "linkedin" and (not board.hard_filter(probe_row)[0] or not board.role_seniority_prefilter(probe_row)[0]):
                row["recovery_status"] = "filtered"
                continue
            pending.append((row, prior))
    try:
        profile = board.load_profiles()
        candidate_fp = profile.get("candidate_fingerprint", "")
        candidate_text = profile.get("candidate", "")
    except (OSError, ValueError, KeyError):
        candidate_fp = candidate_text = ""
    to_triage = []
    for row, prior in pending:
        if id(row) in linkedin_eligible:
            continue
        fingerprint = recovery_policy.evidence_hash(row, candidate_fp)
        if row.get("recovery_input_hash") != fingerprint:
            row["recovery_triage"] = {}
            row["recovery_input_hash"] = fingerprint
        if not row.get("recovery_triage"):
            to_triage.append(row)
    decisions = recovery_ai.triage(to_triage, candidate_text)
    for row in to_triage:
        row["recovery_triage"] = decisions.get(recovery_policy.identity(row), {})
    pending = [(row, prior) for row, prior in pending
               if id(row) in linkedin_eligible or (row.get("recovery_triage") or {}).get("action") != "skip"]
    pending.sort(key=lambda item: (
        {"high": 2, "normal": 1, "low": 0}.get((item[0].get("recovery_triage") or {}).get("priority"), 1),
        official_jd_recovery._stamp(item[0].get("first_seen")) or datetime.min.replace(tzinfo=timezone.utc),
    ), reverse=True)
    methods = official_jd_recovery.recover_pending(
        resolver, pending, context=context, store=store, now=now,
    )

    detail = _finish_linkedin_detail(
        linkedin_candidates, originals["linkedin"], detail_admission, budget, now, blocked=linkedin_blocked, transport=transport,
    )
    linkedin_blocked = linkedin_blocked or bool(detail.get("rate_limited"))

    changed = []
    attempts = {}
    for row in remote_rows:
        if not recovery_policy.fresh(row, now) or len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS:
            continue
        attempts[recovery_policy.identity(row)] = {
            field: row.get(field) for field in (
                "source", "job_id", "company", "title", "location", "first_seen",
                "recovery_methods", "recovery_candidates", "recovery_triage",
                "recovery_input_hash", "official_search_status", "official_search_attempted_at",
            ) if row.get(field)
        }
    for name in names:
        rows = snapshots[name]["jobs"]
        if name == "remote_recovery":
            rows = [row for row in rows if row.get("enrichment_method")
                    and len(str(row.get("description") or "").strip()) >= board.THIN_JD_CHARS]
        for row in rows:
            row.pop("_linkedin_official_url", None)
            row.pop("_linkedin_official_defer", None)
        baseline = previous_remote if name == "remote_recovery" else originals[name]
        if rows == baseline and (name != "remote_recovery" or attempts == previous_attempts):
            continue
        path = OUTPUT_DIR / "sources" / f"{name}.json"
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (FileNotFoundError, ValueError, OSError):
            payload = dict(snapshots[name])
        payload["jobs"] = rows
        payload["source"] = name
        payload["count"] = len(rows)
        payload["meta"] = {**payload.get("meta", {}), "jd_recovery_at": now.isoformat()}
        if name == "remote_recovery":
            payload["attempts"] = attempts
        atomic_write(path, (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
        changed.append(name)

    if int(detail.get("requests", 0) or 0):
        try:
            health = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
        except (FileNotFoundError, ValueError, OSError):
            health = {"schema_version": HEALTH_SCHEMA_VERSION, "sources": {}}
        state = health.setdefault("sources", {}).setdefault("linkedin", {})
        state["detail_enrichment"] = detail
        runtime = _linkedin_runner_state() if os.environ.get("LOCAL_SOURCE_PROFILE") == "mac" else state
        _update_linkedin_detail_health(runtime, detail, now)
        if runtime is not state:
            _persist_linkedin_runner_state(runtime)
            state.setdefault("runner_states", {})["mac"] = runtime
            for key in ("detail_last_attempt_at", "detail_429_streak", "detail_cooldown_until",
                        "detail_cooldown_reason", "detail_status", "detail_retry_after_until"):
                if key in runtime:
                    state[key] = runtime[key]
        atomic_write(HEALTH_PATH, (json.dumps(health, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    after = {name: sum(len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS
                       for row in snapshots[name]["jobs"]) for name in names}
    post_429_jds = (max(0, sum(before.values()) - sum(after.values())) if blocked_before_recovery else
                    0 if detail.get("rate_limited") else None)
    report: Dict[str, object] = {
        "run_at": now.isoformat(), "before_no_jd": before, "after_no_jd": after,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "before_total": sum(before.values()), "after_total": sum(after.values()),
        "cheap_matches": cheap_counts, "methods": dict(resolver.stats),
        "official_matches": dict(resolver.stats),
        "official_jds_recovered": max(0, sum(before.values()) - sum(after.values())
                                       - int(detail.get("jds_resolved", 0) or 0)),
        "linkedin_detail_recoveries": int(detail.get("jds_resolved", 0) or 0),
        "linkedin_detail": detail, "search_requests": resolver.search_requests,
        "initial_detail": initial_detail or {},
        "queue_expired_without_attempt": [str(row.get("job_id")) for row in snapshots["linkedin"]["jobs"]
            if _linkedin_detail_waiting(row) and not _linkedin_detail_eligible(row, now)
            and (row.get("jd_tentative") or len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS)],
        "linkedin_transport": transport.summary(),
        "targeted_linkedin_search_requests": 0, "targeted_linkedin_matches": 0,
        "targeted_linkedin_detail_jds": 0, "targeted_linkedin_rate_limited": False,
        "official_page_requests": resolver.page_requests,
        "generic_jobs_processed": len(budget.attempted),
        "generic_jobs_deferred": max(0, len(pending) - len(methods)),
        "search_provider": resolver.search_provider,
        "linkedin_rate_limited": linkedin_blocked, "changed_sources": changed,
        "post_429_jds_recovered": post_429_jds,
        "glassdoor": "excluded",
    }
    log_path = OUTPUT_DIR / "logs" / "linkedin_jd_recovery_latest.json"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(log_path, (json.dumps(report, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    try:
        health = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError, OSError):
        health = {"schema_version": HEALTH_SCHEMA_VERSION, "sources": {}}
    health["local_recovery"] = {key: report[key] for key in (
        "run_at", "elapsed_seconds", "official_jds_recovered", "linkedin_detail_recoveries",
        "post_429_jds_recovered",
        "targeted_linkedin_search_requests", "targeted_linkedin_detail_jds",
        "targeted_linkedin_rate_limited", "generic_jobs_processed",
        "search_requests", "official_page_requests", "linkedin_rate_limited", "linkedin_detail", "linkedin_transport",
        "initial_detail", "queue_expired_without_attempt", "methods", "cheap_matches",
        "generic_jobs_deferred", "search_provider",
    )}
    history = [item for item in health.get("local_recovery_history", []) if item.get("run_at") != report["run_at"]]
    history.append(health["local_recovery"])
    health["local_recovery_history"] = history[-SOURCE_HISTORY_LIMIT:]
    atomic_write(HEALTH_PATH, (json.dumps(health, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return report

def main() -> None:
    parser = argparse.ArgumentParser(description="Run local best-effort job sources")
    parser.add_argument("--only", choices=sorted(SOURCES.keys()), help="Run a single source")
    parser.add_argument("--recover-jds", action="store_true", help="Recover JDs for LinkedIn and remote candidates")
    args = parser.parse_args()

    transport = _linkedin_transport()
    if args.recover_jds:
        recover_jds(transport=transport)
        return

    names = [args.only] if args.only else list(SOURCES.keys())
    collector = collector_provenance()
    recovery_budget = recovery_policy.RecoveryBudget()
    results = [run_one(name, collector, force=args.only == "glassdoor", budget=recovery_budget, transport=transport)
               for name in names]
    write_health(results, collector)
    if not args.only and os.environ.get("LOCAL_SOURCE_PROFILE") == "mac":
        linkedin_blocked = any(
            result.get("source") == "linkedin" and (
                (result.get("search_collection") or {}).get("rate_limited")
                or (result.get("detail_enrichment") or {}).get("rate_limited")
            ) for result in results
        )
        recover_jds(budget=recovery_budget, linkedin_blocked=linkedin_blocked, transport=transport,
                    initial_detail=next((result.get("detail_enrichment") for result in results
                                         if result.get("source") == "linkedin"), None))

    diagnostics_path = OUTPUT_DIR / "logs" / "local_sources_latest.json"
    diagnostics_path.parent.mkdir(parents=True, exist_ok=True)
    diagnostics_path.write_text(
        json.dumps({"run_at": datetime.now(timezone.utc).isoformat(), "sources": results, "linkedin_transport": transport.summary()}, indent=2) + "\n",
        encoding="utf-8",
    )

    ok = [r for r in results if r["status"] == "ok"]
    print(f"\nDone. {len(ok)}/{len(results)} source(s) updated: "
          + ", ".join(f"{r['source']}={r['status']}" for r in results))
    if names != ["glassdoor"] and not any(
        (r["status"] in ("ok", "partial") or (r["status"] == "cooldown" and r.get("data_usable")))
        and r["source"] not in OPTIONAL_SOURCES for r in results
    ):
        raise SystemExit("No required local source succeeded; last-good snapshots were preserved.")
    if not args.only and os.environ.get("LOCAL_SOURCE_PROFILE") == "mac":
        # This travels with the source commit. A failed push cannot make a
        # Local round appear successful in the published health report.
        health = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
        health["mac_last_completed_at"] = datetime.now(timezone.utc).isoformat()
        atomic_write(HEALTH_PATH, (json.dumps(health, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
