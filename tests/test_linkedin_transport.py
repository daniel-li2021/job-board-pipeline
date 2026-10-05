"""Offline checks for shared LinkedIn traffic limits and ledger yield."""
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

import local_sources
import recovery_policy
from sources import linkedin_local
from sources import schema
from sources.linkedin_transport import LinkedInTransport, RequestDeferred
from sources.schema import make_job


def row(job_id):
    return make_job(source="linkedin", job_id=str(job_id), company="Example",
                    title="Software Engineer", location="Austin, TX",
                    source_url=f"https://linkedin.com/jobs/view/{job_id}")


def response(status=200, headers=None):
    return SimpleNamespace(status_code=status, text="", headers=headers or {})


@patch("sources.linkedin_transport.time.sleep")
class LinkedInTransportTests(unittest.TestCase):
    def test_priority_then_saved_waiter_then_oldest_and_next_round(self, sleep):
        now = datetime.now(timezone.utc)
        jobs = [row(i) for i in range(5)]
        for job, hours, priority in zip(jobs, (1, 22, 3, 23, 1), ("normal", "normal", "high", "normal", "low")):
            job["first_seen"] = (now - timedelta(hours=hours)).isoformat()
            job["linkedin_detail_triage"] = {"needs_jd": True, "priority": priority}
        jobs[0]["linkedin_detail_deferred_at"] = (now - timedelta(minutes=30)).isoformat()
        jobs[1]["linkedin_detail_deferred_at"] = (now - timedelta(hours=20)).isoformat()
        session = Mock()
        session.get.return_value = response()
        decisions = {recovery_policy.identity(r): dict(r["linkedin_detail_triage"]) for r in jobs}
        triage = lambda rows, _: {recovery_policy.identity(r): decisions[recovery_policy.identity(r)] for r in rows}
        with patch.object(local_sources, "_linkedin_detail_control", return_value=(3, False, False)), \
             patch.object(local_sources.board, "load_profiles", return_value={}), \
             patch.object(local_sources.recovery_ai, "triage_linkedin_detail", side_effect=triage), \
             patch.object(linkedin_local, "_make_session", return_value=session), \
             patch.object(linkedin_local, "_parse_detail", return_value={"description": "JD " * 150, "application_url": ""}):
            first = local_sources._finish_linkedin_detail(jobs, [], {"cache_reused": 0},
                recovery_policy.RecoveryBudget(), now, transport=LinkedInTransport())
            self.assertEqual(["2", "1", "0"], first["attempted_ids"])
            self.assertEqual("linkedin_detail_round_budget", jobs[3]["enrichment_deferred_reason"])
            next_now = now + timedelta(hours=3)
            candidates, admission = local_sources._prepare_linkedin_detail(jobs, jobs, next_now)
            second = local_sources._finish_linkedin_detail(candidates, jobs, admission,
                recovery_policy.RecoveryBudget(), next_now, transport=LinkedInTransport())
        self.assertEqual(["3", "4"], second["attempted_ids"])
        self.assertTrue(next(q for q in second["queue"] if q["job_id"] == "3")["past_fresh"])
        self.assertEqual((now - timedelta(hours=23)).isoformat(), jobs[3]["first_seen"])

    def test_waiter_grace_is_one_opportunity_and_does_not_broaden_fresh(self, sleep):
        now = datetime.now(timezone.utc)
        waiter = dict(row(1), first_seen=(now - timedelta(hours=25)).isoformat(),
                      linkedin_detail_triage={"needs_jd": True}, linkedin_detail_deferred_at=now.isoformat())
        self.assertFalse(recovery_policy.fresh(waiter, now))
        self.assertTrue(local_sources._linkedin_detail_eligible(waiter, now))
        rediscovered = {k: v for k, v in waiter.items() if not k.startswith("linkedin_detail")}
        prepared, _ = local_sources._prepare_linkedin_detail([rediscovered], [waiter], now)
        self.assertEqual([rediscovered], prepared)
        self.assertEqual(waiter["linkedin_detail_deferred_at"], rediscovered["linkedin_detail_deferred_at"])
        self.assertFalse(local_sources._linkedin_detail_eligible(dict(waiter, linkedin_detail_attempted_at=now.isoformat()), now))
        self.assertFalse(local_sources._linkedin_detail_eligible(dict(waiter, first_seen=(now - timedelta(hours=73)).isoformat()), now))
        self.assertFalse(local_sources._linkedin_detail_eligible(dict(waiter, linkedin_detail_triage={"needs_jd": False}), now))

    def test_initial_phase_includes_saved_queue_without_refreshing_verification(self, sleep):
        now = datetime.now(timezone.utc)
        old_seen = (now - timedelta(hours=23)).isoformat()
        saved = dict(row("saved"), first_seen=old_seen, source_verified_at=old_seen,
                     linkedin_detail_deferred_at=old_seen, linkedin_detail_triage={"needs_jd": True, "priority": "normal"})
        discovered = dict(row("new"), first_seen=now.isoformat())
        calls = []
        def recovery(_resolver, pending, **kwargs):
            calls.append("recovery")
            self.assertIn("saved", [r["job_id"] for r, _ in pending])
            return []
        def triage(rows, _):
            calls.append("triage")
            return {recovery_policy.identity(r): {"needs_jd": True, "priority": "normal"} for r in rows}
        session = Mock()
        session.get.return_value = response()
        with tempfile.TemporaryDirectory() as temp, \
             patch.object(schema, "SOURCES_DIR", Path(temp) / "sources"), \
             patch.object(local_sources, "HEALTH_PATH", Path(temp) / "health.json"), \
             patch.object(local_sources, "_linkedin_detail_control", return_value=(1, False, False)), \
             patch.object(linkedin_local, "scrape", return_value={"status": "ok", "jobs": [discovered], "coverage_limited": True}), \
             patch.object(local_sources.board, "load_store", return_value={}), \
             patch.object(local_sources.board, "load_profiles", return_value={}), \
             patch.object(local_sources, "_remote_handoff_rows", return_value=[]), \
             patch.object(local_sources.coverage_reconcile, "load_official_context", return_value={}), \
             patch.object(local_sources.official_jd_recovery, "recover_pending", side_effect=recovery), \
             patch.object(local_sources.recovery_ai, "triage_linkedin_detail", side_effect=triage), \
             patch.object(linkedin_local, "_make_session", return_value=session), \
             patch.object(linkedin_local, "_parse_detail", return_value={"description": "JD " * 150, "application_url": ""}):
            schema.write_source_snapshot("linkedin", [saved], meta={"scraped_at": old_seen})
            result = local_sources.run_one("linkedin", {}, scraper=linkedin_local.scrape)
            snapshot = schema.read_source_snapshot_payload("linkedin")
        self.assertEqual(["recovery", "triage"], calls)
        self.assertEqual(["saved"], result["detail_enrichment"]["attempted_ids"])
        retained = next(r for r in snapshot["jobs"] if r["job_id"] == "saved")
        self.assertEqual(old_seen, retained["first_seen"])
        self.assertEqual(old_seen, retained["source_verified_at"])
        self.assertFalse(retained["verified_this_run"])
        self.assertEqual("linkedin_http", retained["enrichment_method"])

    def test_discovery_and_both_detail_phases_share_limits(self, sleep):
        transport = LinkedInTransport()
        session = Mock()
        session.get.return_value = response()
        for page in range(10):
            transport.get(session, linkedin_local.GUEST_SEARCH_URL, endpoint="search", page=page)
        first = linkedin_local.enrich_details([row(i) for i in range(6)], session=session, transport=transport)
        follow = linkedin_local.enrich_details([row(i) for i in range(6, 14)], session=session, transport=transport)
        self.assertEqual((6, 6), (first["requests"], follow["requests"]))
        self.assertEqual(22, session.get.call_count)
        self.assertFalse(transport.available("search"))
        self.assertTrue(follow["budget_exhausted"])
        self.assertTrue(all(2.4 < call.args[0] <= 3.25 for call in sleep.call_args_list))

    def test_workstream_a_admission_shares_transport_across_both_phases(self, sleep):
        import recovery_policy
        transport = LinkedInTransport()
        budget = recovery_policy.RecoveryBudget()
        session = Mock()
        session.get.return_value = response()
        for _ in range(10):
            transport.get(session, "search", endpoint="search")
        triage = lambda rows, _profile: {recovery_policy.identity(r): {"needs_jd": True} for r in rows}
        now = datetime.now(timezone.utc)
        with patch.object(local_sources, "_linkedin_detail_control", return_value=(12, False, False)), \
             patch.object(local_sources.board, "load_profiles", return_value={}), \
             patch.object(local_sources.recovery_ai, "triage_linkedin_detail", side_effect=triage), \
             patch.object(linkedin_local, "_make_session", return_value=session):
            first = local_sources._finish_linkedin_detail([row(i) for i in range(6)], [],
                {"cache_reused": 0}, budget, now, transport=transport)
            follow = local_sources._finish_linkedin_detail([row(i) for i in range(6, 14)], [],
                {"cache_reused": 0}, budget, now, transport=transport)
        self.assertEqual((6, 6, 12, 22),
                         (first["requests"], follow["requests"], budget.linkedin_detail_requests, session.get.call_count))

    def test_transport_pause_prevents_admission_work_without_changing_fit_decisions(self, sleep):
        import recovery_policy
        transport = LinkedInTransport()
        transport.closed = True
        with patch.object(local_sources, "_linkedin_detail_control", return_value=(12, False, False)), \
             patch.object(local_sources.recovery_ai, "triage_linkedin_detail") as triage, \
             patch.object(linkedin_local, "_make_session") as session:
            detail = local_sources._finish_linkedin_detail([row(1)], [], {"cache_reused": 0},
                recovery_policy.RecoveryBudget(), datetime.now(timezone.utc), transport=transport)
        triage.assert_not_called()
        session.return_value.get.assert_not_called()
        self.assertEqual(0, detail["requests"])

    def test_local_journal_survives_unpublished_health_and_day_limits(self, sleep):
        with tempfile.TemporaryDirectory() as temp:
            health, journal = Path(temp) / "health.json", Path(temp) / "journal.json"
            transport = LinkedInTransport(health, journal)
            session = Mock()
            session.get.return_value = response()
            for _ in range(12):
                transport.get(session, "detail", endpoint="detail")
            health.unlink()  # Collector worktree discarded after a failed push.
            resumed = LinkedInTransport(None, journal)
            self.assertFalse(resumed.available("detail"))
            self.assertEqual("shared_detail_hour_budget", resumed.stop_reason)
            self.assertTrue(resumed.available("search"))
            now = datetime.now(timezone.utc)
            resumed.events = [{"at": (now - timedelta(hours=2, seconds=i)).isoformat(), "endpoint": "search"}
                              for i in range(72)]
            self.assertFalse(resumed.available("search"))
            self.assertEqual("global_day_budget", resumed.stop_reason)
            resumed.events = [{"at": (now - timedelta(hours=2, seconds=i)).isoformat(), "endpoint": "detail"}
                              for i in range(36)]
            self.assertFalse(resumed.available("detail"))
            self.assertEqual("shared_detail_day_budget", resumed.stop_reason)
            resumed.events = [{"at": (now - timedelta(hours=25)).isoformat(), "endpoint": "search"}]
            self.assertTrue(resumed.available("search"))
            resumed.events = [{"at": (now - timedelta(minutes=30, seconds=i)).isoformat(), "endpoint": "search"}
                              for i in range(22)]
            self.assertFalse(resumed.available("search"))
            self.assertEqual("global_hour_budget", resumed.stop_reason)
            self.assertFalse(resumed.available("detail"))

    def test_429_closes_both_endpoints_and_records_retry_context(self, sleep):
        with tempfile.TemporaryDirectory() as temp:
            health = Path(temp) / "health.json"
            session = Mock()
            session.get.side_effect = [response(), response(429, {"Retry-After": "7200"})]
            transport = LinkedInTransport(health)
            transport.get(session, "detail", endpoint="detail")
            transport.get(session, linkedin_local.GUEST_SEARCH_URL, endpoint="search", query="ai engineer", page=2)
            with self.assertRaises(RequestDeferred):
                transport.get(session, "detail", endpoint="detail")
            event = transport.rate_limits[-1]
            self.assertEqual(("search", "ai engineer", 2, 2, "7200"),
                             (event["endpoint"], event["query"], event["page"], event["request_ordinal"], event["retry_after"]))
            self.assertEqual({"search": 1, "detail": 1}, event["rolling_counts"]["3600"])
            self.assertFalse(LinkedInTransport(health).available("search"))
            with patch.object(local_sources, "HEALTH_PATH", health), patch.object(
                local_sources, "read_source_snapshot_payload", return_value={"jobs": [], "meta": {}}
            ), patch.dict("os.environ", {"LOCAL_SOURCE_PROFILE": "mac"}):
                local_sources.write_health([{"source": "linkedin", "status": "skipped_unavailable",
                    "attempted_at": event["at"], "search_collection": {"requests": 1, "responses": 1,
                    "rate_limited": True, "rate_limit_event": event}}], {})
            runner = json.loads(health.read_text())["sources"]["linkedin"]["runner_states"]["mac"]
            self.assertEqual(1, runner["search_429_streak"])
            self.assertNotIn("detail_429_streak", runner)
            self.assertEqual(2, session.get.call_count)
            self.assertIn("linkedin_transport", json.loads(health.read_text()))

    def test_unpublished_endpoint_cooldown_survives_journal_checkpoints(self, sleep):
        with tempfile.TemporaryDirectory() as temp:
            health, journal = Path(temp) / "health.json", Path(temp) / "journal.json"
            now = datetime.now(timezone.utc)
            with patch.object(local_sources, "HEALTH_PATH", health), patch.dict("os.environ", {
                "LOCAL_SOURCE_PROFILE": "mac", "LINKEDIN_TRANSPORT_STATE_PATH": str(journal),
            }):
                runtime = {"search_last_attempt_at": now.isoformat(), "search_query_cursor": 7,
                           "search_429_streak": 2, "search_cooldown_until": (now + timedelta(hours=24)).isoformat(),
                           "detail_last_attempt_at": now.isoformat(), "detail_429_streak": 1,
                           "detail_cooldown_until": (now + timedelta(hours=12)).isoformat()}
                local_sources._persist_linkedin_runner_state(runtime)
                transport = LinkedInTransport(health, journal)
                session = Mock()
                session.get.return_value = response()
                transport.get(session, "search", endpoint="search")
                health.unlink()
                self.assertEqual((0, True, False), local_sources._linkedin_detail_control(now))
                self.assertEqual((0, True, False), local_sources._linkedin_search_control(now))
                self.assertEqual(7, local_sources._linkedin_runner_state()["search_query_cursor"])

    def test_http_date_retry_after_extends_detail_cooldown_and_probe_is_shared(self, sleep):
        now = datetime.now(timezone.utc)
        retry = now + timedelta(hours=30)
        session = Mock()
        session.get.return_value = response(429, {"Retry-After": retry.strftime("%a, %d %b %Y %H:%M:%S GMT")})
        transport = LinkedInTransport()
        detail = linkedin_local.enrich_details([row(1)], session=session, transport=transport)
        state = {}
        local_sources._update_linkedin_detail_health(state, detail, now)
        self.assertGreater(datetime.fromisoformat(state["detail_cooldown_until"]), now + timedelta(hours=29))
        self.assertNotIn("search_429_streak", state)
        transport = LinkedInTransport()
        session.get.return_value = response()
        first = linkedin_local.enrich_details([row(2)], session=session, transport=transport, probe=True)
        follow = linkedin_local.enrich_details([row(3)], session=session, transport=transport)
        self.assertEqual((1, 0), (first["requests"], follow["requests"]))
        self.assertEqual("single_detail_probe", follow["transport_stop_reason"])

    def test_consecutive_known_pages_stop_even_with_unique_current_cards(self, sleep):
        session = Mock()
        session.get.return_value = response()
        pages = [[row(i) for i in range(10)], [row(i) for i in range(10, 20)], [row(999)]]
        known = {f"linkedin|id|{i}" for i in range(20)}
        with patch.object(linkedin_local, "_parse_cards", side_effect=pages):
            result = linkedin_local.scrape(keywords=["software engineer"], session=session, known_identities=known)
        stat = result["query_stats"][0]
        self.assertEqual((2, 20, 0), (result["requests"], len(result["jobs"]), stat["new_to_ledger"]))
        self.assertEqual("low_new_to_ledger_yield", stat["stop_reason"])
        self.assertEqual([0, 0], [p["new_to_ledger"] for p in stat["page_yields"]])
        self.assertTrue(result["coverage_limited"])
        self.assertEqual("r86400", session.get.call_args.kwargs["params"]["f_TPR"])

    def test_novel_page_resets_consecutive_stop_and_cross_query_duplicates_are_not_new(self, sleep):
        session = Mock()
        session.get.return_value = response()
        known = {f"linkedin|id|{i}" for i in range(30)}
        pages = [[row(i) for i in range(10)], [row(100), row(101)],
                 [row(i) for i in range(10, 20)], [row(i) for i in range(20, 30)],
                 [row(100), row(101)], [row(100), row(101)]]
        with patch.object(linkedin_local, "_parse_cards", side_effect=pages):
            result = linkedin_local.scrape(session=session, known_identities=known)
        self.assertEqual([4, 1], [s["pages_fetched"] for s in result["query_stats"]])
        self.assertEqual([2, 0], [s["new_to_ledger"] for s in result["query_stats"]])
        self.assertEqual("low_new_to_ledger_yield", result["query_stats"][0]["stop_reason"])

    def test_network_failure_counts_attempt_without_429_and_no_redirect_retry(self, sleep):
        import requests
        session = Mock()
        session.get.side_effect = requests.ConnectionError("offline")
        transport = LinkedInTransport()
        detail = linkedin_local.enrich_details([row(1)], session=session, transport=transport)
        self.assertEqual((1, 0, False), (detail["requests"], detail["responses"], detail["rate_limited"]))
        self.assertEqual(1, len(transport.events))
        self.assertFalse(session.get.call_args.kwargs["allow_redirects"])


if __name__ == "__main__":
    unittest.main()
