#!/usr/bin/env python3
"""Run LOCAL best-effort sources (LinkedIn + Glassdoor) and snapshot them.

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
    python3 local_sources.py                 # both sources
    python3 local_sources.py --only linkedin
    python3 local_sources.py --only glassdoor
"""

from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from typing import Callable, Dict

import board_pipeline as board
from sources import glassdoor_local, linkedin_local
from sources.schema import (
    OUTPUT_DIR,
    SourceUnavailable,
    read_source_snapshot_payload,
    write_source_snapshot,
)

SOURCES: Dict[str, Callable[[], Dict[str, object]]] = {
    "linkedin": linkedin_local.scrape,
    "glassdoor": glassdoor_local.scrape,
}


def run_one(name: str) -> Dict[str, object]:
    scraper = SOURCES[name]
    stamp = datetime.now(timezone.utc).isoformat()
    started = time.monotonic()
    try:
        result = scraper()
    except SourceUnavailable as exc:
        print(f"[{name}] SKIP (blocked/unavailable): {exc} -> keeping last good snapshot")
        return {"source": name, "status": "skipped_unavailable", "reason": str(exc), "count": 0}
    except Exception as exc:  # noqa: BLE001
        print(f"[{name}] SKIP (unexpected {type(exc).__name__}): {exc} -> keeping last good snapshot")
        return {"source": name, "status": "skipped_error", "reason": str(exc), "count": 0}

    rows = list(result.get("jobs") or [])
    query_stats = list(result.get("query_stats") or [])
    if result.get("status") != "ok":
        reason = str(result.get("reason") or result.get("status"))
        print(f"[{name}] SKIP ({reason}) -> keeping last good snapshot")
        return {
            "source": name, "status": "skipped_unavailable", "reason": reason,
            "count": 0, "query_stats": query_stats,
            "elapsed_seconds": round(time.monotonic() - started, 3),
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
            "source": name, "status": "skipped_empty", "count": 0,
            "query_stats": query_stats, "detail_enrichment": detail_enrichment,
            "elapsed_seconds": round(time.monotonic() - started, 3),
        }

    elapsed = round(time.monotonic() - started, 3)
    meta = {"scraped_at": stamp, "elapsed_seconds": elapsed, "query_stats": query_stats}
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
        "source": name, "status": "ok", "count": len(survivors), "path": str(path),
        "query_stats": query_stats, "detail_enrichment": detail_enrichment,
        "elapsed_seconds": elapsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local best-effort job sources")
    parser.add_argument("--only", choices=sorted(SOURCES.keys()), help="Run a single source")
    args = parser.parse_args()

    names = [args.only] if args.only else list(SOURCES.keys())
    results = [run_one(name) for name in names]

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
