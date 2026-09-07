#!/usr/bin/env python3
"""Run local best-effort job-board sources and snapshot them.

Each source is independent: if one hits a login wall / captcha / 403 / 429 /
network error, or returns zero rows, it is skipped and its previous
``output/sources/<name>.json`` snapshot is left untouched (never overwritten
with nothing). The other source and the downstream git sync proceed normally.

LinkedIn search remains card-first. Only cheap first-pass survivors that also
pass the title/seniority prefilter are considered for a bounded, cache-aware
logged-out detail fetch. Detail blocking never invalidates the search-card
snapshot; it only stops enrichment for that run.

This is invoked by launchd every 2-3 hours (see scripts/). It does NOT run the
full board pipeline and does NOT touch jobs.json / latest.md — those are
GitHub-Actions-owned to avoid local/CI git conflicts.

Usage:
    python3 local_sources.py                 # all sources
    python3 local_sources.py --only linkedin
    python3 local_sources.py --only glassdoor
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from datetime import datetime, timezone
from typing import Callable, Dict

import board_pipeline as board
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
HEALTH_PATH = OUTPUT_DIR / "sources" / "health.json"
HEALTH_SCHEMA_VERSION = 1


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
    if result.get("status") != "ok":
        reason = str(result.get("reason") or result.get("status"))
        print(f"[{name}] SKIP ({reason}) -> keeping last good snapshot")
        return {
            "source": name, "status": "skipped_unavailable", "source_healthy": False, "reason": reason,
            "count": 0, "query_stats": query_stats,
            "elapsed_seconds": round(time.monotonic() - started, 3),
            "attempted_at": stamp, "collector": collector, "source_provenance": source_provenance,
        }

    # Stage 1 stays cheap: obvious hard constraints only. This metric is kept
    # independent of detail enrichment so query diagnostics remain comparable.
    stage1_survivors = []
    for row in rows:
        keep, _reason = board.hard_filter(row)
        if keep:
            stage1_survivors.append(row)
    for stat in query_stats:
        stat["first_pass_survivors"] = sum(
            1 for row in stage1_survivors
            if stat["query"] in (row.get("discovery_queries") or {}).get(name, [])
        )

    detail_enrichment: Dict[str, object] = {}
    survivors = stage1_survivors
    if name == "linkedin" and stage1_survivors:
        # Only enrich rows whose title/seniority is already plausible. A thin
        # card failing this gate remains in the source snapshot; we simply do
        # not spend a detail request on it. Highest rule-fit rows go first when
        # the request budget is exhausted.
        detail_candidates = [
            row for row in stage1_survivors
            if board.role_seniority_prefilter(row)[0]
        ]
        detail_candidates.sort(key=lambda row: (
            -float(board.rule_match_score(row) or 0),
            str(row.get("company") or "").lower(),
            str(row.get("title") or "").lower(),
        ))
        previous = read_source_snapshot_payload(name)
        detail_enrichment = linkedin_local.enrich_details(
            detail_candidates,
            previous_jobs=list(previous.get("jobs") or []),
        )

        # The Board store currently persists rich descriptions behind its
        # direct-detail persistence marker. Mark LinkedIn detail rows so their
        # JD/score is not immediately downgraded back to a thin card. Deliberately
        # leave direct_original_fetched_at empty: the original-posting resolver
        # must still fetch a real employer URL when application_url is available.
        for row in detail_candidates:
            if row.get("linkedin_detail_resolved") and row.get("description"):
                row["direct_original_fetched"] = True

        # A full JD can reveal a citizenship/clearance restriction that the
        # search card could not show. Re-run only the hard filter after detail
        # hydration; role matching remains the Board pipeline's responsibility.
        survivors = [row for row in stage1_survivors if board.hard_filter(row)[0]]
        for stat in query_stats:
            matches = [
                row for row in survivors
                if stat["query"] in (row.get("discovery_queries") or {}).get(name, [])
            ]
            stat["jds_resolved"] = sum(bool(row.get("description")) for row in matches)

    if not survivors:
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
    path = write_source_snapshot(name, survivors, meta=meta)
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
        sources[name] = {
            "healthy": healthy,
            "status": result.get("status", "unknown"),
            "reason": "" if healthy else result.get("reason", "unknown failure"),
            "last_attempt_at": result.get("attempted_at", ""),
            "last_success_at": result.get("succeeded_at") or prior.get("last_success_at") or snapshot_meta.get("scraped_at", ""),
            "last_attempt_collector": collector,
            "last_success_collector": collector if healthy else prior.get("last_success_collector") or snapshot_meta.get("collector", {}),
            "last_attempt_source_provenance": result.get("source_provenance", {}),
            "last_success_source_provenance": result.get("source_provenance", {}) if healthy else prior.get("last_success_source_provenance") or snapshot_meta.get("source_provenance", {}),
            "last_good_count": len(snapshot.get("jobs", [])),
        }
    HEALTH_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": HEALTH_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "collector": collector,
        "sources": sources,
    }
    pending = HEALTH_PATH.with_suffix(".json.tmp")
    pending.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    pending.replace(HEALTH_PATH)


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


if __name__ == "__main__":
    main()
