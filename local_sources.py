#!/usr/bin/env python3
"""Run LOCAL best-effort sources (LinkedIn + Glassdoor) and snapshot them.

Each source is independent: if one hits a login wall / captcha / 403 / 429 /
network error, or returns zero rows, it is skipped and its previous
``output/sources/<name>.json`` snapshot is left untouched (never overwritten
with nothing). The other source and the downstream git sync proceed normally.

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
from sources.schema import OUTPUT_DIR, SourceUnavailable, write_source_snapshot

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

    survivors = []
    for row in rows:
        keep, _reason = board.hard_filter(row)
        if keep:
            survivors.append(row)
    for stat in query_stats:
        stat["first_pass_survivors"] = sum(
            1 for row in survivors
            if stat["query"] in (row.get("discovery_queries") or {}).get(name, [])
        )

    if not survivors:
        print(f"[{name}] SKIP (0 first-pass survivors) -> keeping last good snapshot")
        return {
            "source": name, "status": "skipped_empty", "count": 0,
            "query_stats": query_stats, "elapsed_seconds": round(time.monotonic() - started, 3),
        }

    elapsed = round(time.monotonic() - started, 3)
    path = write_source_snapshot(
        name, survivors, meta={"scraped_at": stamp, "elapsed_seconds": elapsed, "query_stats": query_stats},
    )
    print(f"[{name}] OK {len(survivors)} rows ({elapsed:.1f}s) -> {path}")
    return {
        "source": name, "status": "ok", "count": len(survivors), "path": str(path),
        "query_stats": query_stats, "elapsed_seconds": elapsed,
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
