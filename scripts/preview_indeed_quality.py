"""Read-only saved-data comparison. No scoring, crawling, or state migration."""
import copy
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import board_pipeline as board
from sources.job_quality import evidence_warnings, JD_UNVERIFIED


def compare(snapshot, entries):
    by_id = {(r.get("source"), r.get("job_id")): r for r in snapshot["jobs"] if r.get("job_id")}
    results, transitions = [], Counter()
    anonymous_after = anonymous_ab_after = 0
    anonymous = [r for r in entries if r.get("source") == "indeed" and not r.get("company")]
    # Include named controls and metadata-only cohort records, not only affected jobs.
    for before in entries:
        after = copy.deepcopy(before)
        peer = by_id.get((before.get("source"), before.get("job_id")))
        if peer:
            after["description"] = peer.get("description", "")
        board.refresh_evidence_policy(after)
        if after.get("source") == "indeed" and not after.get("company"):
            anonymous_after += 1
            anonymous_ab_after += after.get("tier") in {"A", "B"}
        changes = {k: {"before": before.get(k), "after": after.get(k)}
                   for k in ("company", "tier", "recommended_action") if before.get(k) != after.get(k)}
        # Every original field outside the explicitly allowed policy outputs is immutable.
        allowed = {"company", "company_identity_method", "company_identity_url", "evidence_warnings",
                   "tier", "recommended_action", "description"}
        assert all(after.get(k) == v for k, v in before.items() if k not in allowed), before.get("key")
        assert board.dedup_key(after) == board.dedup_key(before), before.get("key")
        if changes or after["evidence_warnings"]:
            results.append({"key": before.get("key"), "job_id": before.get("job_id"), "title": before.get("title"),
                            "changes": changes, "evidence_warnings": after["evidence_warnings"],
                            "snapshot_jd_joined": peer is not None})
        if before.get("tier") != after.get("tier"):
            transitions[f"{before.get('tier')}->{after.get('tier')}"] += 1
    recovered = [r for r in results if "company" in r["changes"]]
    placeholder = [r for r in snapshot["jobs"] if JD_UNVERIFIED in evidence_warnings(r)]
    return {
        "board_population": len(entries), "snapshot_population": len(snapshot["jobs"]),
        "snapshot_usable_length_jds": sum(len(r.get("description", "").strip()) >= board.THIN_JD_CHARS for r in snapshot["jobs"]),
        "snapshot_anonymous": sum(not r.get("company") for r in snapshot["jobs"]),
        "board_anonymous_before": len(anonymous), "board_anonymous_ab_before": sum(r.get("tier") in {"A", "B"} for r in anonymous),
        "board_anonymous_after": anonymous_after, "board_anonymous_ab_after": anonymous_ab_after, "recovered": recovered,
        "explicit_placeholder_jds": [{"job_id": r["job_id"], "title": r["title"]} for r in placeholder],
        "tier_transitions": dict(transitions),
        "action_changes": sum("recommended_action" in r["changes"] for r in results),
        "immutable_field_checks": len(entries), "assertions_passed": True, "affected_or_warned_records": results,
        "limits": "In-memory policy replay using exact source/ID joins to current saved JDs; not a rescore, adjudication, or production write. Historical compact JDs outside the snapshot cannot be assessed for placeholders.",
    }


def main():
    paths = [ROOT / "output/sources/indeed.json", ROOT / "output/board/jobs.json"]
    data = [json.loads(p.read_text()) for p in paths]
    result = compare(data[0], data[1]["entries"])
    result["inputs"] = [{"path": str(p.relative_to(ROOT)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                         "updated_at": d.get("updated_at") or d.get("meta", {}).get("scraped_at", "")} for p, d in zip(paths, data)]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
