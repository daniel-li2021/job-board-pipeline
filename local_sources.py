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
"""

from __future__ import annotations

import argparse
import json

from state_io import atomic_write
import os
import subprocess
import time
from datetime import datetime, timedelta, timezone
from typing import Callable, Dict

import board_pipeline as board
import coverage_reconcile
from sources import jobspy_local, linkedin_local
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
LINKEDIN_DETAIL_COOLDOWN_HOURS = 24


def _health_source(name: str) -> Dict[str, object]:
    try:
        payload = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}
    source = payload.get("sources", {}).get(name, {}) if isinstance(payload, dict) else {}
    return dict(source) if isinstance(source, dict) else {}


def _linkedin_detail_control(now: datetime) -> tuple[int, bool, bool]:
    state = _health_source("linkedin")
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
    probe = streak >= 2
    return (1 if probe else LINKEDIN_DETAIL_LIMIT), False, probe


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


def run_one(name: str, collector: Dict[str, object] | None = None) -> Dict[str, object]:
    scraper = SOURCES[name]
    stamp = datetime.now(timezone.utc).isoformat()
    collector = collector or collector_provenance()
    source_provenance: Dict[str, object] = {
        "implementation": "sources.linkedin_local" if name == "linkedin" else "sources.jobspy_local",
    }
    started = time.monotonic()
    try:
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
    # A rate-limited LinkedIn run still collected real coverage before the
    # block. Keep it and merge it over the last-good snapshot instead of
    # throwing the whole run away; any non-empty collection qualifies, even
    # when the first query never finished.
    partial = bool(
        name == "linkedin"
        and result.get("status") == "blocked"
        and int(result.get("http_status") or 0) == 429
        and rows
    )
    if result.get("status") != "ok" and not partial:
        reason = str(result.get("reason") or result.get("status"))
        print(f"[{name}] SKIP ({reason}) -> keeping last good snapshot")
        return {
            "source": name, "status": "skipped_unavailable", "source_healthy": False, "reason": reason,
            "count": 0, "query_stats": query_stats,
            "elapsed_seconds": round(time.monotonic() - started, 3),
            "attempted_at": stamp, "collector": collector, "source_provenance": source_provenance,
        }

    detail_enrichment: Dict[str, object] = {}
    if name != "linkedin":
        for row in rows:
            if len(str(row.get("description") or "").strip()) < board.THIN_JD_CHARS and not row.get("enrichment_failure_reason"):
                row["enrichment_status"] = "unresolved"
                row["enrichment_failure_reason"] = f"{name}_detail_missing_or_thin"
    if name == "linkedin" and rows:
        detail_candidates = [row for row in rows if not row.get("description")]
        previous = read_source_snapshot_payload(name)
        try:
            official_context = coverage_reconcile.load_official_context()
        except (OSError, ValueError, json.JSONDecodeError):
            official_context = {}
        try:
            board_store = board.load_store()
        except (OSError, ValueError, json.JSONDecodeError):
            board_store = {}
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
            allow_requests=not partial and not cooldown_active,
            request_limit=detail_limit,
        )
        detail_enrichment["cooldown_active"] = cooldown_active
        detail_enrichment["probe"] = probe

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
        if row.get("description"):
            row["direct_original_fetched"] = True

    survivors = stage1_survivors

    if not survivors and not partial:
        print(f"[{name}] SKIP (0 first-pass survivors) -> keeping last good snapshot")
        return {
            "source": name, "status": "skipped_empty", "source_healthy": False, "reason": "0 first-pass survivors", "count": 0,
            "query_stats": query_stats, "detail_enrichment": detail_enrichment,
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
    carried_count = 0
    if partial:
        fresh_keys = {board.dedup_key(job) for job in survivors}
        carried_count = sum(
            1 for job in read_source_snapshot_payload(name).get("jobs") or []
            if board.dedup_key(job) not in fresh_keys
        )
        meta.update({
            "partial": True,
            "blocked_reason": str(result.get("reason") or ""),
            "collected_count": len(rows),
            "carried_count": carried_count,
        })
    path = write_source_snapshot(name, survivors, meta=meta, merge_previous=partial)
    if partial:
        merged_count = len(survivors) + carried_count
        print(
            f"[{name}] PARTIAL {len(survivors)} fresh + {carried_count} carried = {merged_count} rows "
            f"({elapsed:.1f}s; {result.get('reason')}) -> {path}"
        )
        return {
            "source": name, "status": "partial", "source_healthy": False, "data_usable": True,
            "reason": str(result.get("reason") or "rate limited"),
            "count": len(survivors), "collected_count": len(rows), "fresh_kept": len(survivors),
            "carried_count": carried_count, "merged_count": merged_count, "path": str(path),
            "query_stats": query_stats, "detail_enrichment": detail_enrichment,
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
        "query_stats": query_stats, "detail_enrichment": detail_enrichment,
        "elapsed_seconds": elapsed,
        "attempted_at": stamp, "succeeded_at": stamp, "collector": collector,
        "source_provenance": source_provenance,
    }


def write_health(results: list[Dict[str, object]], collector: Dict[str, object]) -> None:
    try:
        previous = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        previous = {}
    previous_sources = previous.get("sources", {}) if isinstance(previous, dict) else {}
    sources = dict(previous_sources) if isinstance(previous_sources, dict) else {}
    for result in results:
        name = str(result["source"])
        prior = sources.get(name, {}) if isinstance(sources.get(name), dict) else {}
        snapshot = read_source_snapshot_payload(name)
        snapshot_meta = snapshot.get("meta", {})
        healthy = bool(result.get("source_healthy", result.get("status") == "ok"))
        partial = result.get("status") == "partial"
        # ``last_success_at`` means a complete collection that verified the
        # whole snapshot. A partial run rewrites the snapshot, so its
        # ``scraped_at`` must never be adopted as a full success.
        snapshot_full_success = "" if snapshot_meta.get("partial") else str(snapshot_meta.get("scraped_at", ""))
        state = dict(prior)
        state.update({
            "required": name not in OPTIONAL_SOURCES,
            "healthy": healthy,
            "status": result.get("status", "unknown"),
            "reason": "" if healthy else result.get("reason", "unknown failure"),
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
            "consecutive_failures": 0 if healthy else int(prior.get("consecutive_failures", 0) or 0) + 1,
            "query_stats": list(result.get("query_stats") or []),
            "detail_enrichment": dict(result.get("detail_enrichment") or {}),
            "last_good_count": len(snapshot.get("jobs", [])),
        })
        if name == "linkedin":
            detail = state["detail_enrichment"]
            requests_made = int(detail.get("requests", 0) or 0)
            if requests_made:
                state["detail_last_attempt_at"] = result.get("attempted_at", "")
            if requests_made and detail.get("rate_limited"):
                streak = int(prior.get("detail_429_streak", 0) or 0) + 1
                state["detail_429_streak"] = streak
                if streak >= 2:
                    try:
                        attempted_at = datetime.fromisoformat(
                            str(result.get("attempted_at") or "").replace("Z", "+00:00")
                        )
                    except ValueError:
                        attempted_at = datetime.now(timezone.utc)
                    state["detail_cooldown_until"] = (
                        attempted_at + timedelta(hours=LINKEDIN_DETAIL_COOLDOWN_HOURS)
                    ).isoformat()
            elif requests_made and int(detail.get("responses", 0) or 0):
                state["detail_429_streak"] = 0
                state["detail_cooldown_until"] = ""
        sources[name] = state
    HEALTH_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": HEALTH_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "collector": collector,
        "sources": sources,
    }
    atomic_write(HEALTH_PATH, (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local best-effort job sources")
    parser.add_argument("--only", choices=sorted(SOURCES.keys()), help="Run a single source")
    args = parser.parse_args()

    names = [args.only] if args.only else list(SOURCES.keys())
    collector = collector_provenance()
    results = [run_one(name, collector) for name in names]
    write_health(results, collector)

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
