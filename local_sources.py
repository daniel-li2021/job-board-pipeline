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
from datetime import datetime, timezone
from typing import Callable, Dict, List

from sources import glassdoor_local, linkedin_local
from sources.schema import SourceUnavailable, write_source_snapshot

SOURCES: Dict[str, Callable[[], List[dict]]] = {
    "linkedin": linkedin_local.scrape,
    "glassdoor": glassdoor_local.scrape,
}


def run_one(name: str) -> Dict[str, object]:
    scraper = SOURCES[name]
    stamp = datetime.now(timezone.utc).isoformat()
    try:
        rows = scraper()
    except SourceUnavailable as exc:
        print(f"[{name}] SKIP (blocked/unavailable): {exc} -> keeping last good snapshot")
        return {"source": name, "status": "skipped_unavailable", "reason": str(exc), "count": 0}
    except Exception as exc:  # noqa: BLE001
        print(f"[{name}] SKIP (unexpected {type(exc).__name__}): {exc} -> keeping last good snapshot")
        return {"source": name, "status": "skipped_error", "reason": str(exc), "count": 0}

    if not rows:
        print(f"[{name}] SKIP (0 rows) -> keeping last good snapshot")
        return {"source": name, "status": "skipped_empty", "count": 0}

    path = write_source_snapshot(name, rows, meta={"scraped_at": stamp})
    print(f"[{name}] OK {len(rows)} rows -> {path}")
    return {"source": name, "status": "ok", "count": len(rows), "path": str(path)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local best-effort job sources")
    parser.add_argument("--only", choices=sorted(SOURCES.keys()), help="Run a single source")
    args = parser.parse_args()

    names = [args.only] if args.only else list(SOURCES.keys())
    results = [run_one(name) for name in names]

    ok = [r for r in results if r["status"] == "ok"]
    print(f"\nDone. {len(ok)}/{len(results)} source(s) updated: "
          + ", ".join(f"{r['source']}={r['status']}" for r in results))


if __name__ == "__main__":
    main()
