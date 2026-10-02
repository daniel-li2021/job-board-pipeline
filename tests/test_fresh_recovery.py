"""Fresh-only recovery, handoff, budget, and metadata fallback contracts."""

import json
import gzip
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock, patch

import board_pipeline as board
import dashboard
import pipeline_health
import recovery_ai
import local_sources
import recovery_policy
import remote_recovery
from sources import linkedin_local, schema
from sources.official_jd_recovery import Resolver, recover_pending


NOW = datetime(2026, 9, 26, 12, tzinfo=timezone.utc)


def job(**extra):
    return {"source": "linkedin", "job_id": "123", "company": "Abridge",
            "title": "Software Engineer", "location": "Austin, TX",
            "source_url": "https://linkedin.com/jobs/view/123", "description": "",
            "first_seen": NOW.isoformat(), **extra}


class FreshRecoveryTests(unittest.TestCase):
    def test_linkedin_detail_metadata_admission_is_conservative(self):
        filters = {"exclude": board.prepare_alias_entries([{"name": "Excluded Corp", "aliases": ["excluded corp"]}])}
        for title in ("Senior Software Engineer", "Staff Engineer", "Principal Engineer",
                      "Lead Developer", "Engineering Manager", "Recruiter", "Sales Associate"):
            with self.subTest(title=title):
                self.assertTrue(local_sources._linkedin_metadata_skip(job(title=title), {}))
        self.assertEqual("company_excluded", local_sources._linkedin_metadata_skip(job(company="Excluded Corp"), filters))
        self.assertEqual("non_us_location", local_sources._linkedin_metadata_skip(job(location="Toronto, Canada"), {}))
        for title in ("Software Engineer", "Engineer II", "Research Engineer", "Junior Engineer"):
            self.assertEqual("", local_sources._linkedin_metadata_skip(job(title=title, location="Remote"), {}))

    def test_linkedin_detail_triage_accepts_only_explicit_boolean(self):
        rows = [job(job_id=str(i)) for i in range(4)]
        with patch.object(recovery_ai, "_ask", return_value={"results": [
            {"id": recovery_policy.identity(rows[0]), "needs_jd": True},
            {"id": recovery_policy.identity(rows[1]), "needs_jd": False},
            {"id": recovery_policy.identity(rows[2]), "needs_jd": "true"},
            {"id": "unrequested", "needs_jd": True},
        ]}) as ask:
            decisions = recovery_ai.triage_linkedin_detail(rows)
        self.assertEqual(2, len(decisions))
        self.assertIs(True, decisions[recovery_policy.identity(rows[0])]["needs_jd"])
        self.assertIs(False, decisions[recovery_policy.identity(rows[1])]["needs_jd"])
        self.assertNotIn("description", ask.call_args.args[1][0])
        with patch.object(recovery_ai, "_ask", side_effect=ValueError("bad JSON")):
            self.assertEqual({}, recovery_ai.triage_linkedin_detail(rows))

    def test_linkedin_detail_round_budget_and_cached_triage(self):
        rows = [job(job_id=str(i)) for i in range(12)]
        budget = recovery_policy.RecoveryBudget()
        session = Mock()
        session.get.return_value.status_code = 200
        session.get.return_value.text = "page"
        decisions = {recovery_policy.identity(row): {"needs_jd": True} for row in rows}
        admission = {"cache_reused": 0}
        with patch.object(local_sources, "_linkedin_detail_control", return_value=(8, False, False)), \
             patch.object(board, "load_profiles", return_value={}), \
             patch.object(recovery_ai, "triage_linkedin_detail", return_value=decisions) as triage, \
             patch.object(linkedin_local, "_make_session", return_value=session), \
             patch.object(linkedin_local, "_check_blocked"), \
             patch.object(linkedin_local, "_parse_detail", return_value={"description": "", "application_url": ""}), \
             patch.object(linkedin_local.time, "sleep"):
            first = local_sources._finish_linkedin_detail(rows, [], dict(admission), budget, NOW)
            second = local_sources._finish_linkedin_detail(rows, rows, dict(admission), budget, NOW)
            self.assertEqual(8, first["requests"])
            self.assertEqual(0, second["requests"])
            self.assertEqual(8, budget.linkedin_detail_requests)
            self.assertEqual(8, session.get.call_count)
            triage.assert_called_once()
            # A new round reuses unchanged metadata decisions without a new LLM call.
            third = local_sources._finish_linkedin_detail(rows[8:], rows, dict(admission),
                                                         recovery_policy.RecoveryBudget(), NOW)
            triage.assert_called_once()
            self.assertEqual(4, third["requests"])
            probe_budget = recovery_policy.RecoveryBudget()
            with patch.object(local_sources, "_linkedin_detail_control", return_value=(1, False, True)):
                probe = local_sources._finish_linkedin_detail(rows[8:], rows, dict(admission), probe_budget, NOW)
            later = local_sources._finish_linkedin_detail(rows[8:], rows, dict(admission), probe_budget, NOW)
            self.assertEqual(1, probe["requests"])
            self.assertEqual(0, later["requests"])
            self.assertEqual(1, probe_budget.linkedin_detail_requests)
        self.assertTrue(all(row.get("first_seen") == NOW.isoformat() for row in rows))

    def test_linkedin_cache_only_precedes_outbound_and_rejects_tentative_cache(self):
        now = datetime.now(timezone.utc)
        rows = [job(job_id="cached", first_seen=now.isoformat()),
                job(job_id="tentative", first_seen=now.isoformat())]
        previous = [dict(row, description="Saved JD " * 30, linkedin_detail_fetched_at=now.isoformat(),
                         jd_tentative=row["job_id"] == "tentative") for row in rows]
        with patch.object(linkedin_local, "_make_session") as session:
            candidates, admission = local_sources._prepare_linkedin_detail(rows, previous, now)
        session.return_value.get.assert_not_called()
        self.assertEqual(1, admission["cache_reused"])
        self.assertEqual("linkedin_cache", candidates[0]["enrichment_method"])
        self.assertFalse(candidates[1].get("description"))

    def test_linkedin_detail_skip_or_unavailable_keeps_card(self):
        rows = [job(job_id="skip"), job(job_id="missing")]
        with patch.object(local_sources, "_linkedin_detail_control", return_value=(8, False, False)), \
             patch.object(board, "load_profiles", return_value={}), \
             patch.object(recovery_ai, "triage_linkedin_detail", return_value={
                 recovery_policy.identity(rows[0]): {"needs_jd": False}}), \
             patch.object(linkedin_local, "_make_session") as session:
            detail = local_sources._finish_linkedin_detail(rows, [], {"cache_reused": 0},
                                                          recovery_policy.RecoveryBudget(), NOW)
        self.assertEqual(0, detail["requests"])
        session.return_value.get.assert_not_called()
        self.assertEqual("linkedin_detail_not_worthwhile", rows[0]["enrichment_deferred_reason"])
        self.assertEqual("linkedin_detail_triage_unavailable", rows[1]["enrichment_deferred_reason"])
        self.assertTrue(all(board.hard_filter(row)[0] for row in rows))

    def test_linkedin_last_resort_order_in_both_local_phases(self):
        now = datetime.now(timezone.utc)
        rows = [job(job_id="senior", title="Senior Software Engineer", first_seen=now.isoformat()),
                job(job_id="official", first_seen=now.isoformat()),
                job(job_id="detail", first_seen=now.isoformat()),
                job(job_id="old", first_seen=(now - timedelta(days=2)).isoformat())]
        calls = []

        def recover(_resolver, pending, **_kwargs):
            calls.append("non_linkedin")
            self.assertNotIn("senior", [row["job_id"] for row, _ in pending])
            for row, _ in pending:
                if row["job_id"] == "official":
                    row["description"] = "Official JD " * 30
            return []

        def triage(candidates, _profile):
            calls.append("triage")
            self.assertEqual(["detail"], [row["job_id"] for row in candidates])
            return {recovery_policy.identity(row): {"needs_jd": True} for row in candidates}

        session = Mock()
        session.get.return_value.status_code = 200
        session.get.return_value.text = "page"
        with tempfile.TemporaryDirectory() as tmp, \
             patch.object(schema, "SOURCES_DIR", Path(tmp) / "sources"), \
             patch.object(schema, "OUTPUT_DIR", Path(tmp)), \
             patch.object(local_sources, "OUTPUT_DIR", Path(tmp)), \
             patch.object(local_sources, "HEALTH_PATH", Path(tmp) / "health.json"), \
             patch.object(local_sources, "_remote_handoff_rows", return_value=[]), \
             patch.object(local_sources, "_linkedin_detail_control", return_value=(8, False, False)), \
             patch.object(linkedin_local, "scrape", return_value={"status": "ok", "jobs": rows}), \
             patch.object(board, "load_store", return_value={}), \
             patch.object(board, "load_profiles", return_value={}), \
             patch.object(local_sources.coverage_reconcile, "load_official_context", return_value={}), \
             patch.object(local_sources.official_jd_recovery, "recover_pending", side_effect=recover), \
             patch.object(recovery_ai, "triage_linkedin_detail", side_effect=triage), \
             patch.object(linkedin_local, "_make_session", return_value=session), \
             patch.object(linkedin_local, "_check_blocked"), \
             patch.object(linkedin_local, "_parse_detail", return_value={"description": "Detail JD " * 30, "application_url": ""}), \
             patch.object(linkedin_local.time, "sleep"):
            schema.write_source_snapshot("linkedin", [dict(
                rows[-1], description="Saved LinkedIn JD " * 30,
                linkedin_detail_fetched_at=now.isoformat(),
            )])
            budget = recovery_policy.RecoveryBudget()
            first = local_sources.run_one("linkedin", {"commit": "test"}, scraper=linkedin_local.scrape, budget=budget)
            second = local_sources.recover_jds(budget=budget)
            saved = schema.read_source_snapshot_payload("linkedin")["jobs"]
        self.assertEqual(["non_linkedin", "triage", "non_linkedin"], calls)
        self.assertEqual(1, first["detail_enrichment"]["requests"])
        self.assertEqual(0, second["linkedin_detail"]["requests"])
        self.assertEqual(1, session.get.call_count)
        self.assertEqual(4, len(saved))
        self.assertTrue(next(row for row in saved if row["job_id"] == "old")["description"])
        self.assertEqual(1, first["detail_enrichment"]["admission"]["rules_skipped"])
        self.assertEqual(1, first["detail_enrichment"]["admission"]["non_linkedin_resolved"])

    def test_exact_fresh_and_rolling_boundaries(self):
        at_24 = job(first_seen=(NOW - timedelta(hours=24)).isoformat())
        at_72 = job(first_seen=(NOW - timedelta(hours=72)).isoformat())
        expired = job(first_seen=(NOW - timedelta(hours=72, seconds=1)).isoformat())
        self.assertTrue(recovery_policy.fresh(at_24, NOW))
        self.assertFalse(recovery_policy.fresh(at_72, NOW))
        self.assertTrue(dashboard.recency(at_24, NOW)["fresh_activity"])
        self.assertTrue(dashboard.recency(at_72, NOW)["rolling_activity"])
        self.assertFalse(dashboard.recency(expired, NOW)["rolling_activity"])

    def test_first_seen_new_prior_and_legacy_unknown(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(schema, "OUTPUT_DIR", Path(tmp)):
            ledger = Path(tmp) / "board" / "seen_jobs.json"
            ledger.parent.mkdir()
            existing = job(job_id="known", first_seen="")
            ledger.write_text(json.dumps({"seen": {schema.dedup_key(existing):
                                                    (NOW - timedelta(days=2)).isoformat()}}))
            legacy = job(job_id="legacy", first_seen="")
            rows = [job(job_id="new", first_seen=""), job(job_id="known", first_seen=""),
                    job(job_id="legacy", first_seen="")]
            schema.assign_source_first_seen(rows, [legacy], NOW.isoformat())
            self.assertEqual(NOW.isoformat(), rows[0]["first_seen"])
            self.assertEqual((NOW - timedelta(days=2)).isoformat(), rows[1]["first_seen"])
            self.assertEqual("", rows[2]["first_seen"])
            self.assertFalse(recovery_policy.fresh(rows[1], NOW))
            self.assertFalse(recovery_policy.fresh(rows[2], NOW))
            self.assertTrue(recovery_policy.fresh(rows[0], NOW))

    def test_budget_counts_distinct_outbound_jobs_and_starts_lazily(self):
        budget = recovery_policy.RecoveryBudget(max_jobs=2, seconds=1200)
        a, b, c = (job(job_id=value) for value in ("a", "b", "c"))
        self.assertIsNone(budget.deadline)
        resolver = Resolver(session=Mock(), budget=budget)
        self.assertEqual("pending", resolver.recover(a, previous={}, context={}, store={}, now=NOW, cheap_only=True))
        self.assertEqual(set(), budget.attempted)
        self.assertTrue(budget.claim(a))
        self.assertTrue(budget.claim(a))
        self.assertTrue(budget.claim(b))
        self.assertFalse(budget.claim(c))
        self.assertEqual(2, len(budget.attempted))
        with patch("recovery_policy.time.monotonic", return_value=budget.deadline):
            self.assertFalse(budget.claim(a))
            self.assertTrue(budget.deadline_reached)

    def test_filtered_first_discovery_is_durable(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(schema, "OUTPUT_DIR", Path(tmp)), \
             patch.object(schema, "SOURCES_DIR", Path(tmp) / "sources"):
            filtered = job(job_id="filtered", first_seen="")
            schema.assign_source_first_seen([filtered], [], NOW.isoformat(), {})
            schema.write_source_snapshot("linkedin", [], {"scraped_at": NOW.isoformat()},
                                         observed_jobs=[filtered])
            prior = schema.read_source_snapshot_payload("linkedin")
            self.assertEqual([], prior["jobs"])
            later = job(job_id="filtered", first_seen="")
            schema.assign_source_first_seen([later], prior["jobs"],
                                             (NOW + timedelta(days=2)).isoformat(), prior["first_seen_ledger"])
            self.assertEqual(NOW.isoformat(), later["first_seen"])

    def test_handoff_keeps_unknown_and_method_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "handoff.json.gz"
            old = job(first_seen="", recovery_methods={"generic_search": {"outcome": "no_match"}},
                      recovery_candidates=["https://abridge.com/jobs/1"])
            path.write_bytes(gzip.compress(json.dumps({"jobs": [old]}).encode()))
            remote_recovery.write_snapshot(path, "board", [job(first_seen="")])
            saved = remote_recovery.read_snapshot(path)[0]
            self.assertEqual("", saved["first_seen"])
            self.assertEqual("no_match", saved["recovery_methods"]["generic_search"]["outcome"])
            self.assertEqual(["https://abridge.com/jobs/1"], saved["recovery_candidates"])

    def test_method_cache_reuses_same_evidence_but_new_url_retries(self):
        response = Mock(status_code=200, text="", url="https://html.duckduckgo.com/html/")
        session = Mock()
        session.get.return_value = response
        resolver = Resolver(session=session)
        with patch("sources.official_jd_recovery.time.sleep"):
            first = job()
            self.assertEqual("no_match", resolver.recover(first, previous={}, context={}, store={}, now=NOW))
            later = Resolver(session=Mock())
            second = job()
            self.assertEqual("no_match_cached", later.recover(second, previous=first, context={}, store={},
                                                                now=NOW + timedelta(hours=1)))
            later.session.get.assert_not_called()
            changed = job(application_url="https://abridge.com/jobs/new")
            later = Resolver(session=session)
            before = session.get.call_count
            later.recover(changed, previous=first, context={}, store={}, now=NOW + timedelta(hours=1))
            self.assertGreater(session.get.call_count, before)

    def test_handoff_does_not_refetch_failed_candidate_url(self):
        url = "https://abridge.com/jobs/software-engineer"
        first = job(_ranked_candidates=[url], _generic_searched=True)
        online = Resolver(session=Mock())
        online.page = Mock(return_value=("", url, "ok"))
        online.recover(first, previous={}, context={}, store={}, now=NOW)
        self.assertEqual(1, online.page.call_count)
        handed_off = job(_ranked_candidates=[url], _generic_searched=True)
        local = Resolver(session=Mock())
        local.page = Mock(return_value=("", url, "ok"))
        local.recover(handed_off, previous=first, context={}, store={}, now=NOW + timedelta(hours=1))
        local.page.assert_not_called()

    def test_new_known_url_uses_direct_path_before_generic_search(self):
        candidate = job(application_url="https://abridge.com/jobs/software-engineer")
        posting = {"@type": "JobPosting", "title": "Software Engineer",
                   "hiringOrganization": {"name": "Abridge"},
                   "jobLocation": {"address": {"addressLocality": "Austin", "addressRegion": "TX"}},
                   "description": "Build software services. " * 20}
        page = '<script type="application/ld+json">' + json.dumps(posting) + "</script>"
        resolver = Resolver(session=Mock())
        resolver.page = Mock(return_value=(page, candidate["application_url"], "ok"))
        resolver.search = Mock(side_effect=AssertionError("known URL should win"))
        self.assertEqual(["known_url"], recover_pending(resolver, [(candidate, {})],
                                                          context={}, store={}, now=NOW))
        resolver.search.assert_not_called()

    def test_ranked_first_failure_tries_second_verified_page(self):
        candidate = job()
        urls = ["https://abridge.com/jobs/one", "https://abridge.com/jobs/two"]
        def posting(title):
            data = {"@type": "JobPosting", "title": title,
                    "hiringOrganization": {"name": "Abridge"},
                    "jobLocation": {"address": {"addressLocality": "Austin", "addressRegion": "TX"}},
                    "description": "Build software services. " * 20}
            return '<script type="application/ld+json">' + json.dumps(data) + "</script>"
        resolver = Resolver(session=Mock())
        resolver.search = Mock(return_value=(urls, "ok"))
        resolver.page = Mock(side_effect=[(posting("Wrong Title"), urls[0], "ok"),
                                          (posting("Software Engineer"), urls[1], "ok")])
        with patch.object(recovery_ai, "rank_candidates", return_value={recovery_policy.identity(candidate): urls}) as rank:
            result = recover_pending(resolver, [(candidate, {})], context={}, store={}, now=NOW)
        self.assertEqual(["generic_ranked"], result)
        self.assertEqual(2, resolver.page.call_count)
        rank.assert_called_once()

    def test_empty_generic_search_is_not_repeated_in_same_run(self):
        candidate = job()
        resolver = Resolver(session=Mock())
        resolver.search = Mock(return_value=([], "ok"))
        with patch("sources.official_jd_recovery.time.sleep"):
            recover_pending(resolver, [(candidate, {})], context={}, store={}, now=NOW)
        self.assertEqual(1, resolver.search.call_count)

    def test_first_linkedin_429_stops_further_detail_requests(self):
        session = Mock()
        session.get.return_value = Mock(status_code=429, text="", url="https://linkedin.com/jobs/view/123")
        budget = recovery_policy.RecoveryBudget()
        rows = [job(job_id="a"), job(job_id="b")]
        result = linkedin_local.enrich_details(rows, session=session, budget=budget,
                                               min_description_chars=200)
        self.assertTrue(result["rate_limited"])
        self.assertEqual(1, session.get.call_count)
        self.assertEqual(1, len(budget.attempted))

    def test_health_counts_current_pending_attempted_and_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            board_dir = root / "output" / "board"
            board_dir.mkdir(parents=True)
            entries = [
                job(job_id="pending"),
                job(job_id="attempted", recovery_methods={"generic_search": {"outcome": "no_match"}}),
                job(job_id="rolling", first_seen=(NOW - timedelta(hours=30)).isoformat(),
                    score_source="metadata_ai_fallback"),
                job(job_id="skipped", recovery_triage={"action": "skip"}),
                job(job_id="expired", first_seen=(NOW - timedelta(hours=73)).isoformat()),
            ]
            board_dir.joinpath("jobs.json").write_text(json.dumps({"entries": entries}))
            report, _ = pipeline_health.build(root, NOW)
            summary = report["recovery_summary"]
            self.assertEqual(4, summary["no_jd_current"])
            self.assertEqual(1, summary["pending_fresh"])
            self.assertEqual(1, summary["attempted_unresolved"])
            self.assertEqual(1, summary["fallback_current"])

    def test_metadata_delta_is_low_evidence_and_full_jd_replaces_it(self):
        candidate = job(title="Machine Learning Engineer")
        candidate["recovery_triage"] = {"confidence": .92, "action": "skip", "delta": -7,
                                        "reason": "unlikely role"}
        profiles = board.load_profiles()
        board.score_survivors([candidate], {}, profiles, {}, use_llm=False)
        self.assertEqual(board.SCORE_METADATA, candidate["score_source"])
        self.assertEqual(candidate["rule_score"] - 7, candidate["match_score"])
        full = job(title="Machine Learning Engineer", description="Build machine learning services. " * 20,
                   recovery_triage=dict(candidate["recovery_triage"]), recovery_input_hash="old")
        board.score_survivors([full], {}, profiles, {}, use_llm=False)
        self.assertNotEqual(board.SCORE_METADATA, full["score_source"])
        self.assertNotIn("recovery_triage", full)


if __name__ == "__main__":
    unittest.main()
