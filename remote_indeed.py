#!/usr/bin/env python3
"""Collect Indeed on GitHub and retain its last-good full-JD snapshot."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import local_sources
from sources import jobspy_local
from sources.schema import OUTPUT_DIR


def main() -> None:
    collector = local_sources.collector_provenance()
    result = local_sources.run_one(
        "indeed", collector, scraper=lambda: jobspy_local.scrape("indeed"), recover_missing=False,
    )
    local_sources.write_health([result], collector)
    path = OUTPUT_DIR / "logs" / "remote_indeed_latest.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"run_at": datetime.now(timezone.utc).isoformat(),
                                "source": result}, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
