#!/usr/bin/env python3
"""Read-only preview of saved deterministic repairs and identity migration risks.

Run from the repository root. Writes JSON to stdout; never changes job/review state.
"""
import hashlib
import json
import sys
from collections import defaultdict
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import board_pipeline as board
import coverage_reconcile as coverage
from sources.schema import normalize_job_url


def normalized_key(row, pipeline):
    job = coverage.normalize_syncareer_job(row) if pipeline == "syncareer" else row
    return coverage.canonical_job_key(job)


def derived_changes(row):
    if row.get("tier") not in {"A", "B", "C"}:
        return {}
    changed = deepcopy(row)
    changed["main_gaps_count"] = board.main_gaps_count(changed)
    changed["tier"] = board.assign_tier(changed, False)
    board.apply_referral_action(changed)
    return {field: {"before": row.get(field), "after": changed.get(field)}
            for field in ("main_gaps_count", "tier", "recommended_action")
            if row.get(field) != changed.get(field)}


def preview(root):
    hashes, rows, repairs, key_changes = {}, [], [], []
    for pipeline, directory in (("board", "board"), ("syncareer", "syncareer"), ("official", "official_careers")):
        path = root / "output" / directory / "jobs.json"
        hashes[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
        for row in json.loads(path.read_text())["entries"]:
            key = row.get("canonical_job_key") or row.get("key") or ""
            ref = {"pipeline": pipeline, "key": key, "job_id": row.get("job_id", "")}
            rows.append((pipeline, row, ref))
            changes = derived_changes(row)
            if changes:
                repairs.append({**ref, "changes": changes})
            proposed = normalized_key(row, pipeline)
            if proposed != key:
                key_changes.append({**ref, "proposed_key": proposed, "first_seen": row.get("first_seen", "")})
    source_ids, urls = defaultdict(list), defaultdict(list)
    for pipeline, row, ref in rows:
        source = "syncareer" if pipeline == "syncareer" else str(row.get("source") or "")
        if source and row.get("job_id"):
            source_ids[(source, str(row["job_id"]))].append((row, ref))
        # These are candidate aliases only; a populated URL alone is not verified identity.
        url = normalize_job_url(row.get("job_url") or row.get("url") or "") if pipeline == "syncareer" else normalize_job_url(row.get("official_url") or "")
        if url:
            urls[url].append((row, ref))
    groups = []
    for kind, buckets in (("source_id", source_ids), ("exact_url", urls)):
        for evidence, members in buckets.items():
            if len(members) < 2:
                continue
            distinct_urls = {normalize_job_url(r.get("official_url") or r.get("job_url") or r.get("url") or "") for r, _ in members} - {""}
            ids_by_source = defaultdict(set)
            for row, ref in members:
                ids_by_source[str(row.get("source") or ref["pipeline"])].add(str(row.get("job_id") or ""))
            conflict = len(distinct_urls) > 1 or any(len(ids - {""}) > 1 for ids in ids_by_source.values())
            groups.append({"evidence_type": kind, "evidence": evidence,
                           "members": [ref for _, ref in members],
                           "first_seen_values": sorted({r.get("first_seen", "") for r, _ in members}),
                           "conflicting_identity_evidence": conflict})
    review_path = root / "profile/review_state.json"
    review = json.loads(review_path.read_text()).get("jobs", {}) if review_path.exists() else {}
    review_keys = set(review)
    ledger_keys = set()
    for directory in ("board", "official_careers"):
        path = root / "output" / directory / "digest_state.json"
        if path.exists():
            data = json.loads(path.read_text())
            ledger_keys.update(data.get("alerted_keys", []))
            ledger_keys.update(data.get("alerted_tier", {}))
    affected_keys = {c["key"] for c in key_changes} | {m["key"] for g in groups for m in g["members"]}
    return {"mode": "preview_only", "input_sha256": hashes,
            "counts": {"records": len(rows), "derived_repairs": len(repairs),
                       "canonical_key_changes": len(key_changes), "alias_candidate_groups": len(groups),
                       "conflicting_groups": sum(g["conflicting_identity_evidence"] for g in groups),
                       "affected_local_review_keys": len(affected_keys & review_keys),
                       "affected_digest_keys": len(affected_keys & ledger_keys)},
            "derived_repairs": repairs, "canonical_key_changes": key_changes,
            "alias_candidates": groups,
            "application_history": {"local_review_keys_inspected": len(review_keys),
                                    "live_supabase_inspected": False, "browser_pending_edits_inspected": False},
            "migration_blockers": ["Export live Supabase statuses and application history before rekeying.",
                                   "Preserve old keys as aliases in all review readers/writers, including offline browser edits.",
                                   "Resolve conflicting URLs/requisitions without company/title-only merging.",
                                   "Move digest/seen/history references with keys, preserving earliest first_seen and every status event."],
            "applied": False}


if __name__ == "__main__":
    print(json.dumps(preview(ROOT), indent=2, ensure_ascii=False))
