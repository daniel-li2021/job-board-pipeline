"""Print pending companies meeting a minimum distinct-job count.

Usage: python3 scripts/pending_company_subset.py 2
       python3 scripts/pending_company_subset.py 3
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from sources.company_pending import pending_entry  # noqa: E402


def subset(path: Path, minimum: int) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    entries = payload.get("companies")
    if not isinstance(entries, list):
        raise ValueError("pending companies must be a list")
    companies = []
    for raw in entries:
        entry = pending_entry(raw)
        if not entry:
            raise ValueError("invalid pending company")
        if entry["seen_count"] >= minimum:
            companies.append({key: value for key, value in entry.items() if key != "seen_job_keys"})
    companies.sort(key=lambda entry: (-entry["seen_count"], entry["name"].casefold()))
    return {"minimum_seen_count": minimum, "count": len(companies), "companies": companies}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("minimum", type=int, help="minimum seen_count (for example, 2 or 3)")
    parser.add_argument("--pending", type=Path, default=ROOT / "profile/company_profiles_pending.json")
    args = parser.parse_args()
    if args.minimum < 1:
        parser.error("minimum must be at least 1")
    print(json.dumps(subset(args.pending, args.minimum), indent=2))


if __name__ == "__main__":
    main()
