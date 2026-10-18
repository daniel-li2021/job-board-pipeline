"""Offline Batch 2 decisions, delivery failures, and migration-preview safety."""
import json
import subprocess
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

import pytest
import board_pipeline as board
import daily_pipeline as daily
import notification_outbox as outbox
from scripts.preview_batch2_migration import derived_changes, normalized_key


def job(**extra):
    return {**dict(title="Software Engineer I", company="Example", location="Austin, TX",
                source="syncareer", job_id="one", description="Build APIs. " * 30,
                match_score=90, seniority_fit="good", hard_constraint_status="ok",
                score_source="llm", recency_bucket="3to24h", tier="B"), **extra}


@pytest.mark.parametrize("count", [None, 0])
def test_gap_count_survives_export_compaction_and_reuse(count):
    row = {"job_id": "one", "title": "Software Engineer I", "company": "Example",
           "location": "Austin, TX", "job_url": "https://example.test/jobs/one"}

    def score(jobs, *_args, **_kwargs):
        jobs[0].update(job(main_gaps=["Core skill missing"], main_gaps_count=count))
        return "llm", [], {"llm": 1}

    with patch.object(board, "score_survivors", side_effect=score), patch.object(board, "load_profiles", return_value={}), patch.object(board, "load_store_path", return_value={}):
        decisions, _, _, _ = daily.assign_shared_scores([row], {}, True)
    entry = {**row, **decisions["one"]}
    compact = daily.compact_watchlist_entry(entry)
    reused = job()
    board._apply_cached_result(reused, compact)
    assert decisions["one"]["tier"] == "B"
    assert compact["main_gaps_count"] == reused["main_gaps_count"] == 1
    assert board.assign_tier(reused, False) == "B"


def test_truncated_gap_examples_keep_total_and_fresh_results_clear_stale_counts():
    row = job(main_gaps=["one", "two", "three"], main_gaps_count=3)
    row["key"] = "test"
    compact = board.compact_store_entry(row)
    assert len(compact["main_gaps"]) == 2
    assert board.main_gaps_count(compact) == 3
    board._apply_rule_result(row, board.SCORE_RULE, "Rule")
    assert board.main_gaps_count(row) == 0


@pytest.mark.parametrize("status", ["other", "citizenship", "no_sponsorship", " blocked "])
def test_hard_constraints_are_terminal_even_for_high_score_referrals(status):
    row = job(main_gaps=[])
    row.update(hard_constraint_status=status, match_score=99, referral_name="Contact")
    row["tier"] = board.assign_tier(row, True)
    board.apply_referral_action(row)
    assert (row["tier"], row["recommended_action"]) == ("C", "skip")


@pytest.mark.parametrize("field", ["referral_name", "target_company_match"])
def test_tier_c_referral_is_skip_and_valid_referral_still_works(field):
    row = job(main_gaps=[])
    row.update(tier="C", **{field: "Example"})
    board.apply_referral_action(row)
    assert row["recommended_action"] == "skip"
    row["tier"] = "A"
    board.apply_referral_action(row)
    assert row["recommended_action"] == "referral_now"


def test_preview_does_not_mutate_history_or_merge_requisitions():
    row = job(main_gaps=["one"], main_gaps_count=0)
    row.update(tier="A", first_seen="2026-10-15T01:00:00Z", review_status="applied", canonical_job_key="id::syncareer::one", job_url="https://example.test/jobs/11111")
    original = deepcopy(row)
    changes = derived_changes(row)
    assert changes["tier"] == {"before": "A", "after": "B"}
    assert row == original
    assert normalized_key(row, "syncareer") != row["canonical_job_key"]
    assert normalized_key(row, "syncareer") != normalized_key({**row, "job_url": "https://example.test/jobs/22222"}, "syncareer")
    assert derived_changes({**row, "tier": "ignored"}) == {}


def enqueue(path, stamp="2026-10-17_2100", body="Saved digest"):
    return outbox.enqueue(path, pipeline="board", stamp=stamp, title="Digest", body=body)


def test_failed_delivery_remains_pending_and_retry_after_creation_uses_marker(tmp_path):
    path = tmp_path / "outbox.json"
    identity = enqueue(path)
    assert enqueue(path) == identity
    with patch.object(outbox, "_gh", side_effect=subprocess.CalledProcessError(1, ["gh"])):
        with pytest.raises(subprocess.CalledProcessError):
            outbox.deliver(path, "owner/repo")
    assert json.loads(path.read_text())["receipts"][0]["status"] == "pending"
    marker = f"<!-- job-board-digest:{identity} -->"
    # Issue exists, but acknowledgement never reached Git; closed Issues count too.
    with patch.object(outbox, "_gh", side_effect=[json.dumps([[{"body": marker, "html_url": "https://github.com/owner/repo/issues/1", "state": "closed"}]]), "[[]]"]) as gh:
        assert outbox.deliver(path, "owner/repo") == 1
        assert all(call.args[0] == "api" for call in gh.call_args_list)
    with patch.object(outbox, "_gh", side_effect=AssertionError("No network for acknowledged receipts")):
        assert outbox.deliver(path, "owner/repo") == 0


def test_delivery_retains_immutable_body_and_acknowledges_each_success(tmp_path):
    path = tmp_path / "outbox.json"
    enqueue(path, body="First body")
    enqueue(path, stamp="2026-10-17_2200", body="Second body")
    bodies = []

    def gh(*args):
        if args[0] == "api":
            return "[[]]"
        bodies.append(Path(args[args.index("--body-file") + 1]).read_text())
        if len(bodies) == 2:
            raise subprocess.CalledProcessError(1, ["gh"])
        return "https://github.com/owner/repo/issues/1\n"

    with patch.object(outbox, "_gh", side_effect=gh):
        with pytest.raises(subprocess.CalledProcessError):
            outbox.deliver(path, "owner/repo")
    assert bodies[0].startswith("First body") and bodies[1].startswith("Second body")
    assert [r["status"] for r in json.loads(path.read_text())["receipts"]] == ["delivered", "pending"]
    enqueue(path, stamp="2026-10-18_0100")
    assert len(json.loads(path.read_text())["receipts"]) == 3


def test_corrupt_outbox_is_not_overwritten(tmp_path):
    path = tmp_path / "outbox.json"
    path.write_text('{"receipts":[{}]}')
    with pytest.raises(ValueError):
        enqueue(path)
    assert path.read_text() == '{"receipts":[{}]}'


def test_actual_fresh_match_replaces_old_gap_total():
    row = job(main_gaps=["old"], main_gaps_count=4)
    row.pop("match_score")
    row.pop("tier")
    decisions = {board.dedup_key(row): {"match_score": 90, "seniority_fit": "good", "hard_constraint_status": "ok", "top_match_reasons": ["APIs"], "main_gaps": ["Core skill"]}}
    with patch.dict("os.environ", {"OPENAI_API_KEY": "mock-only"}), patch.object(board, "llm_match_batch", return_value=(decisions, {})), patch.object(board.time, "sleep"):
        board.score_survivors([row], {}, {"fingerprint": "test", "candidate_fingerprint": "test"}, {}, True)
    assert row["score_source"] == board.SCORE_LLM
    assert row["main_gaps_count"] == 1
    assert board.assign_tier(row, False) == "B"


def test_identity_preview_keeps_url_added_lost_statuses_and_conflicts_separate(tmp_path):
    from scripts.preview_batch2_migration import preview
    url = "https://example.test/jobs/11111"
    board_rows = [
        job(official_url="", key="id::syncareer::one", first_seen="2026-10-15T01:00:00Z"),
        job(official_url=url, key="url::" + url, first_seen="2026-10-16T01:00:00Z"),
        job(job_id="two", official_url="https://example.test/jobs/22222", key="url::https://example.test/jobs/22222"),
        job(job_id="conflict", official_url=url, key="conflict-a"),
        job(job_id="conflict", official_url="https://example.test/jobs/33333", key="conflict-b"),
    ]
    for directory, rows in (("board", board_rows), ("syncareer", []), ("official_careers", [])):
        path = tmp_path / "output" / directory / "jobs.json"
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps({"entries": rows}))
    profile = tmp_path / "profile/review_state.json"
    profile.parent.mkdir()
    profile.write_text(json.dumps({"jobs": {"id::syncareer::one": {"status": "applied", "notes": "Preserve me"}}}))
    originals = {p: p.read_bytes() for p in tmp_path.rglob("*.json")}
    report = preview(tmp_path)
    assert report["counts"]["affected_local_review_keys"] == 1
    assert report["counts"]["conflicting_groups"] >= 1
    group = next(g for g in report["alias_candidates"] if g["evidence_type"] == "source_id" and g["evidence"] == ("syncareer", "one"))
    assert len(group["first_seen_values"]) == 2
    assert len(group["members"]) == 2
    assert not any(m["job_id"] == "two" for g in report["alias_candidates"] for m in g["members"])
    assert not report["applied"]
    assert all(p.read_bytes() == data for p, data in originals.items())


def test_workflow_delivery_retries_without_new_jobs_and_pages_survives_failure():
    root = Path(__file__).resolve().parents[1]
    for filename, pipeline in (("board-jobs.yml", "board"), ("daily-jobs.yml", "syncareer"), ("official-careers.yml", "official")):
        workflow = (root / ".github/workflows" / filename).read_text()
        step = workflow.split("      - name: Deliver pending Issue digests", 1)[1].split("      - name:", 1)[0]
        assert "new_count" not in step and "digest_emitted" not in step
        assert f"notification_outbox.py {pipeline}" in step
        assert "always() && steps.publish.outcome == 'success' && steps.delivery.outcome != 'skipped'" in workflow
        assert workflow.index("id: publish") < workflow.index("id: delivery")
    board_workflow = (root / ".github/workflows/board-jobs.yml").read_text()
    assert "gh workflow run reconcile-pages.yml" not in board_workflow
    assert '"Board job alert"' in (root / ".github/workflows/reconcile-pages.yml").read_text()
