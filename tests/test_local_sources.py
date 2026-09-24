from __future__ import annotations

import json
import logging
import os
import plistlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

import local_sources
import board_pipeline
from sources import jobspy_local, linkedin_local, schema

ROOT = Path(__file__).resolve().parents[1]


class Frame:
    def __init__(self, records: list[dict]) -> None:
        self.records = records

    def to_dict(self, *, orient: str) -> list[dict]:
        assert orient == "records"
        return self.records


class LocalSourceTests(unittest.TestCase):
    def test_glassdoor_known_us_location_skips_obsolete_lookup(self) -> None:
        try:
            from jobspy.glassdoor import Glassdoor
        except ImportError:
            self.skipTest("python-jobspy is not installed")
        jobspy_local._patch_glassdoor_transport()
        scraper = Glassdoor()
        scraper.base_url = "https://www.glassdoor.com/"
        scraper.session = Mock()
        scraper.session.get.return_value = SimpleNamespace(
            status_code=200, json=lambda: [{"locationType": "C", "locationId": 42}],
        )

        self.assertEqual((1, "COUNTRY"), scraper._get_location("United States", False))
        scraper.session.get.assert_not_called()
        self.assertEqual(("11047", "STATE"), scraper._get_location("United States", True))
        scraper.session.get.assert_not_called()
        self.assertEqual((42, "CITY"), scraper._get_location("New York, NY", False))
        self.assertIn("term=New%20York%2C%20NY", scraper.session.get.call_args.args[0])

    def test_glassdoor_graphql_403_stops_without_static_retry(self) -> None:
        try:
            import jobspy.glassdoor
        except ImportError:
            self.skipTest("python-jobspy is not installed")
        session = Mock()
        session.headers = {}
        session.get.return_value = SimpleNamespace(status_code=200, text='"token":"csrf"')
        session.post.return_value = SimpleNamespace(status_code=403)
        with patch.object(jobspy.glassdoor, "create_session", return_value=session), patch.object(
            jobspy_local, "_scrapling_glassdoor_records",
        ) as fallback:
            result = jobspy_local.scrape("glassdoor", keywords=["software engineer"])

        self.assertEqual("blocked", result["status"])
        self.assertIn("HTTP 403", result["reason"])
        self.assertEqual("blocked_http_403", result["query_stats"][0]["stop_reason"])
        self.assertEqual(1, session.post.call_count)
        self.assertEqual(1, session.get.call_count)
        fallback.assert_not_called()

    def test_glassdoor_homepage_403_stops_before_search(self) -> None:
        try:
            import jobspy.glassdoor
        except ImportError:
            self.skipTest("python-jobspy is not installed")
        session = Mock()
        session.headers = {}
        session.get.return_value = SimpleNamespace(status_code=403, text="Access denied")
        with patch.object(jobspy.glassdoor, "create_session", return_value=session), patch.object(
            jobspy_local, "_scrapling_glassdoor_records",
        ) as fallback:
            result = jobspy_local.scrape("glassdoor", keywords=["software engineer"])

        self.assertEqual("blocked", result["status"])
        self.assertIn("homepage HTTP 403", result["reason"])
        self.assertEqual("blocked_http_403", result["query_stats"][0]["stop_reason"])
        session.post.assert_not_called()
        fallback.assert_not_called()

    def test_glassdoor_graphql_card_and_description_fixture(self) -> None:
        try:
            from jobspy.glassdoor import Glassdoor
            from jobspy.model import DescriptionFormat, ScraperInput, Site
        except ImportError:
            self.skipTest("python-jobspy is not installed")
        jobspy_local._patch_glassdoor_transport()
        scraper = Glassdoor()
        scraper.base_url = "https://www.glassdoor.com/"
        scraper.jobs_per_page = 1
        scraper.scraper_input = ScraperInput(
            site_type=[Site.GLASSDOOR], search_term="software engineer",
            location="United States", hours_old=24, results_wanted=1,
            description_format=DescriptionFormat.MARKDOWN,
        )
        card = {
            "jobview": {
                "job": {"listingId": 42, "jobTitleText": "Software Engineer"},
                "header": {
                    "employerNameFromSearch": "Example", "employer": {"id": 7},
                    "locationName": "Austin, TX", "locationType": "C", "ageInDays": 1,
                },
            },
        }
        session = Mock()
        session.post.side_effect = [
            SimpleNamespace(status_code=200, json=lambda: [{"data": {"jobListings": {
                "jobListings": [card], "paginationCursors": [],
            }}}]),
            SimpleNamespace(status_code=200, json=lambda: [{"data": {"jobview": {
                "job": {"description": "<p>Build APIs and services.</p>"},
            }}}]),
        ]
        scraper.session = session

        jobs, cursor = scraper._fetch_jobs_page(scraper.scraper_input, 1, "COUNTRY", 1, None)

        self.assertIsNone(cursor)
        self.assertEqual(1, len(jobs))
        self.assertEqual("gd-42", jobs[0].id)
        self.assertEqual("Software Engineer", jobs[0].title)
        self.assertIn("Build APIs and services.", jobs[0].description)
        self.assertEqual(2, session.post.call_count)

    def test_glassdoor_recovery_defer_preserves_health_and_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(schema, "SOURCES_DIR", Path(tmpdir)), patch.object(
            local_sources, "HEALTH_PATH", Path(tmpdir) / "health.json",
        ):
            snapshot = schema.write_source_snapshot("glassdoor", [{"job_id": "last-good"}])
            previous = snapshot.read_bytes()
            now = datetime.now(timezone.utc)
            health = {
                "sources": {"glassdoor": {
                    "healthy": False, "last_attempt_at": (now - timedelta(hours=1)).isoformat(),
                    "consecutive_failures": 29,
                }},
            }
            local_sources.HEALTH_PATH.write_text(json.dumps(health), encoding="utf-8")
            prior_health = local_sources.HEALTH_PATH.read_bytes()
            blocked = {"status": "blocked", "reason": "HTTP 403", "jobs": [], "query_stats": []}
            scraper = Mock(return_value=blocked)
            with patch.dict(local_sources.SOURCES, {"glassdoor": scraper}):
                deferred = local_sources.run_one("glassdoor", {"commit": "test"})
                local_sources.write_health([deferred], {"commit": "test"})
                self.assertEqual("deferred", deferred["status"])
                scraper.assert_not_called()
                self.assertEqual(previous, snapshot.read_bytes())
                self.assertEqual(prior_health, local_sources.HEALTH_PATH.read_bytes())

                health["sources"]["glassdoor"]["last_attempt_at"] = (now - timedelta(hours=25)).isoformat()
                local_sources.HEALTH_PATH.write_text(json.dumps(health), encoding="utf-8")
                self.assertEqual("skipped_unavailable", local_sources.run_one("glassdoor", {"commit": "test"})["status"])
                health["sources"]["glassdoor"]["last_attempt_at"] = now.isoformat()
                local_sources.HEALTH_PATH.write_text(json.dumps(health), encoding="utf-8")
                self.assertEqual("skipped_unavailable", local_sources.run_one("glassdoor", {"commit": "test"}, force=True)["status"])
                self.assertEqual(2, scraper.call_count)
                self.assertEqual(previous, snapshot.read_bytes())

    def test_explicit_glassdoor_only_forces_recovery_probe(self) -> None:
        result = {"source": "glassdoor", "status": "skipped_unavailable"}
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            local_sources, "OUTPUT_DIR", Path(tmpdir),
        ), patch.object(sys, "argv", ["local_sources.py", "--only", "glassdoor"]), patch.object(
            local_sources, "collector_provenance", return_value={"commit": "test"},
        ), patch.object(local_sources, "run_one", return_value=result) as run, patch.object(
            local_sources, "write_health",
        ):
            local_sources.main()
        run.assert_called_once_with("glassdoor", {"commit": "test"}, force=True)

    def test_new_job_telemetry_is_final_unique_and_credits_overlapping_sources(self) -> None:
        now = "2026-09-16T12:00:00+00:00"
        old = "2026-09-15T12:00:00+00:00"
        added = schema.make_job(
            source="linkedin", company="One", title="Software Engineer I",
            location="Austin, TX", job_id="one",
        )
        added.update(first_seen=now, tier="A", discovered_via=["linkedin", "indeed"])
        filtered = schema.make_job(
            source="glassdoor", company="Two", title="Software Engineer Intern",
            location="Seattle, WA", job_id="two",
        )
        filtered.update(first_seen=now, tier="C", discovered_via=["glassdoor"])
        known = schema.make_job(
            source="greenhouse", company="Three", title="Data Engineer",
            location="Remote, US", job_id="three",
        )
        known["first_seen"] = now
        seen = {schema.dedup_key(known): old}

        new_jobs = board_pipeline.finalize_new_jobs([added, filtered, known], {}, seen, now)
        telemetry = board_pipeline.new_job_telemetry(new_jobs, [added])

        self.assertEqual(2, telemetry["new_jobs"])
        self.assertEqual(1, telemetry["new_jobs_added"])
        self.assertEqual({"found": 1, "added": 1}, telemetry["new_jobs_by_source"]["linkedin"])
        self.assertEqual({"found": 1, "added": 1}, telemetry["new_jobs_by_source"]["indeed"])
        self.assertEqual({"found": 1, "added": 0}, telemetry["new_jobs_by_source"]["glassdoor"])
        self.assertEqual({"found": 0, "added": 0}, telemetry["new_jobs_by_source"]["ats"])
        self.assertEqual(old, known["first_seen"])

    def test_glassdoor_static_cards_preserve_partial_discovery(self) -> None:
        records = jobspy_local._parse_glassdoor_cards('''
          <div data-test="job-card-wrapper">
            <span class="EmployerProfile_compactEmployerName__x">Example</span>
            <a data-test="job-title" href="/job-listing/software-engineer-JV.htm?jl=42">Software Engineer</a>
            <span data-test="emp-location">Austin, TX</span>
            <div data-test="descSnippet">Build APIs and services.</div>
          </div>
        ''')
        self.assertEqual("42", records[0]["id"])
        self.assertEqual("Example", records[0]["company"])
        self.assertEqual("", records[0]["description"])
        self.assertEqual("Build APIs and services.", records[0]["source_snippet"])
        self.assertEqual("glassdoor_detail_http_403_static_card_only", records[0]["enrichment_failure_reason"])

    def test_jobspy_rows_use_shared_schema_and_keep_direct_apply_url(self) -> None:
        calls = []

        def fake_scrape(**kwargs):
            calls.append(kwargs)
            return Frame([{
                "id": "in-42", "title": "Software Engineer", "company": "Example",
                "location": "Austin, TX, US", "date_posted": "2026-09-06",
                "job_url": "https://www.indeed.com/viewjob?jk=42",
                "job_url_direct": "https://jobs.example.com/42",
                "description": "Build Python services.",
            }])

        result = jobspy_local.scrape(
            "indeed", keywords=["software engineer"], scrape_jobs_func=fake_scrape,
        )

        self.assertEqual("ok", result["status"])
        self.assertEqual(1, len(result["jobs"]))
        row = result["jobs"][0]
        self.assertEqual("indeed", row["source"])
        self.assertEqual("2026-09-06", row["aggregator_posted_date"])
        self.assertEqual("https://jobs.example.com/42", row["application_url"])
        self.assertEqual(300, calls[0]["results_wanted"])
        self.assertEqual(48, calls[0]["hours_old"])
        self.assertEqual("United States", calls[0]["location"])

    def test_jobspy_does_not_treat_aggregator_redirect_as_original_employer(self) -> None:
        result = jobspy_local.scrape(
            "indeed", keywords=["software engineer"],
            scrape_jobs_func=lambda **_kwargs: Frame([{
                "id": "in-43", "title": "Software Engineer", "company": "Example",
                "location": "Austin, TX, US", "job_url": "https://indeed.com/viewjob?jk=43",
                "job_url_direct": "https://www.indeed.com/job/example-43",
                "description": "Build Python services.",
            }]),
        )
        self.assertNotIn("application_url", result["jobs"][0])

    def test_empty_primary_jobspy_query_is_unverified_not_a_good_snapshot(self) -> None:
        def blocked(**_kwargs):
            logging.getLogger("JobSpy:Glassdoor").error("HTTP 403")
            return Frame([])

        result = jobspy_local.scrape(
            "glassdoor", keywords=["software engineer"],
            scrape_jobs_func=blocked,
        )
        self.assertEqual("blocked", result["status"])
        self.assertIn("HTTP 403", result["reason"])
        self.assertEqual("blocked_http_403", result["query_stats"][0]["stop_reason"])

    def test_partial_or_later_transport_failure_is_not_a_good_snapshot(self) -> None:
        for fail_at in (1, 2):
            calls = []
            def partial(**_kwargs):
                calls.append(1)
                if len(calls) == fail_at:
                    logging.getLogger("JobSpy:Glassdoor").error("HTTP 429")
                return Frame([{
                    "id": f"gd-{len(calls)}", "title": "Software Engineer",
                    "company": "Example", "location": "Austin, TX, US",
                    "description": "Build Python services.",
                }])
            result = jobspy_local.scrape(
                "glassdoor", keywords=["software engineer", "ai engineer"],
                scrape_jobs_func=partial,
            )
            self.assertEqual("blocked", result["status"])
            self.assertIn("HTTP 429", result["reason"])

    def test_glassdoor_joins_three_source_unique_contribution(self) -> None:
        rows = [dict(source=source, official_url="https://jobs.example.com/1",
                     discovery_queries={source: ["software engineer"]})
                for source in ("linkedin", "indeed", "glassdoor")]
        rows.append(dict(source="glassdoor", official_url="https://jobs.example.com/2",
                         discovery_queries={"glassdoor": ["software engineer"]}))
        report = board_pipeline.local_source_coverage(rows)
        self.assertEqual(1, report["overlap"])
        self.assertEqual(1, report["sources"]["glassdoor"]["unique_contribution"])
        self.assertEqual(1, report["queries"]["glassdoor"]["software engineer"]["cross_source_unique"])

    def test_transport_page_cap_and_exhaustion_are_measured(self) -> None:
        try:
            import jobspy.indeed
        except ImportError:
            self.skipTest("requires local collector dependencies")
        from types import SimpleNamespace
        for cursor in ("next", None):
            class FakeIndeed:
                def __init__(self):
                    self.session = SimpleNamespace(post=lambda: SimpleNamespace(status_code=200))
                def _scrape_page(self, _cursor):
                    self.session.post()
                    return [SimpleNamespace()], cursor
                def scrape(self, _input):
                    for _ in range(5):
                        jobs, _cursor = self._scrape_page(None)
                        if not jobs:
                            break
                    return SimpleNamespace(jobs=[])
            stat = {"pages_fetched": 0, "stop_reason": "page_budget"}
            with patch.object(jobspy.indeed, "Indeed", FakeIndeed):
                jobspy_local._fetch_records("indeed", "software engineer", 2, 24, stat)
            self.assertEqual(2 if cursor else 1, stat["pages_fetched"])
            self.assertEqual("page_budget" if cursor else "exhausted", stat["stop_reason"])

    def test_codegraph_generated_data_is_ignored(self) -> None:
        self.assertIn(".codegraph/", (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines())

    def test_launchd_agent_runs_after_wake_and_uses_noninteractive_ssh_push(self) -> None:
        with (ROOT / "scripts/macos/com.jobboard.local-sources.plist").open("rb") as handle:
            agent = plistlib.load(handle)
        self.assertNotIn("StartInterval", agent)
        self.assertEqual(list(range(0, 24, 3)), [item["Hour"] for item in agent["StartCalendarInterval"]])
        env = agent["EnvironmentVariables"]
        self.assertEqual("remote.origin.pushurl", env["GIT_CONFIG_KEY_0"])
        self.assertEqual("git@github.com:daniel-li2021/job-board-pipeline.git", env["GIT_CONFIG_VALUE_0"])
        self.assertEqual("/usr/bin/ssh -o BatchMode=yes", env["GIT_SSH_COMMAND"])
        self.assertEqual("0", env["GIT_TERMINAL_PROMPT"])

    def test_cloud_collector_is_daytime_serialized_and_commits_only_durable_state(self) -> None:
        workflow = (ROOT / ".github/workflows/local-sources.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("schedule:", workflow)
        self.assertNotIn("cron:", workflow)
        self.assertIn("scheduler_probe:", workflow)
        self.assertIn("Record external scheduler receipt", workflow)
        self.assertIn("group: local-source-collection", workflow)
        self.assertIn("cancel-in-progress: false", workflow)
        self.assertIn("source_ingest=true", workflow)
        self.assertNotIn("steps.publish.outputs.changed == 'true'", workflow)
        for name in ("linkedin", "indeed", "glassdoor", "health"):
            self.assertIn(f"output/sources/{name}.json", workflow)
        self.assertNotIn("git add -A", workflow)

    def test_snapshot_schema_is_versioned_and_reads_legacy_lists(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(schema, "SOURCES_DIR", Path(tmpdir)):
            path = schema.write_source_snapshot("indeed", [{"job_id": "1"}], {"collector": {"commit": "abc"}})
            payload = schema.read_source_snapshot_payload("indeed")
            self.assertEqual(schema.SNAPSHOT_SCHEMA_VERSION, payload["schema_version"])
            self.assertEqual("abc", payload["meta"]["collector"]["commit"])

            path.write_text(json.dumps([{"job_id": "legacy"}]), encoding="utf-8")
            legacy = schema.read_source_snapshot_payload("indeed")
            self.assertEqual(0, legacy["schema_version"])
            self.assertEqual("legacy", legacy["jobs"][0]["job_id"])

    def test_board_ingests_new_local_source_without_network(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(schema, "SOURCES_DIR", Path(tmpdir)):
            schema.write_source_snapshot("indeed", [{"source": "indeed", "job_id": "in-1"}])
            jobs, meta = board_pipeline.collect_sources(object(), skip_network=True)
        self.assertEqual(["in-1"], [job["job_id"] for job in jobs])
        self.assertEqual(1, meta["per_source"]["local:indeed"])

    def test_failed_attempt_updates_health_but_keeps_last_success(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(schema, "SOURCES_DIR", Path(tmpdir)), patch.object(
            local_sources, "HEALTH_PATH", Path(tmpdir) / "health.json",
        ):
            old = {"commit": "old", "dirty": False}
            new = {"commit": "new", "dirty": False}
            schema.write_source_snapshot(
                "glassdoor", [{"job_id": "last-good"}],
                {"scraped_at": "2026-09-01T00:00:00+00:00", "collector": old},
            )
            local_sources.write_health([{
                "source": "glassdoor", "status": "ok", "count": 1,
                "attempted_at": "2026-09-01T00:00:00+00:00",
                "succeeded_at": "2026-09-01T00:00:00+00:00",
            }], old)
            local_sources.write_health([{
                "source": "glassdoor", "status": "skipped_unavailable", "count": 0,
                "reason": "HTTP 403", "attempted_at": "2026-09-07T00:00:00+00:00",
                "query_stats": [{"query": "software engineer", "stop_reason": "HTTP 403"}],
                "detail_enrichment": {"remaining_no_jd": 1},
            }], new)
            health = json.loads((Path(tmpdir) / "health.json").read_text(encoding="utf-8"))["sources"]["glassdoor"]
            self.assertFalse(health["required"])
            self.assertFalse(health["healthy"])
            self.assertEqual("HTTP 403", health["reason"])
            self.assertEqual("2026-09-01T00:00:00+00:00", health["last_success_at"])
            self.assertEqual("old", health["last_success_collector"]["commit"])
            self.assertEqual(1, health["last_good_count"])
            self.assertEqual(0, health["last_attempt_count"])
            self.assertEqual("HTTP 403", health["query_stats"][0]["stop_reason"])
            self.assertEqual(1, health["detail_enrichment"]["remaining_no_jd"])

    def test_collector_fails_when_no_required_source_succeeds(self) -> None:
        failed = {"source": "linkedin", "status": "skipped_unavailable"}
        with patch.object(sys, "argv", ["local_sources.py"]), patch.object(
            local_sources, "run_one", return_value=failed,
        ), patch.object(local_sources, "write_health"):
            with self.assertRaisesRegex(SystemExit, "No required local source succeeded"):
                local_sources.main()

    def test_empty_attempt_updates_health_but_keeps_last_success(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(schema, "SOURCES_DIR", Path(tmpdir)), patch.object(
            local_sources, "HEALTH_PATH", Path(tmpdir) / "health.json",
        ), patch.dict(local_sources.SOURCES, {"indeed": lambda: {"status": "ok", "jobs": []}}):
            old = {"commit": "old", "dirty": False}
            new = {"commit": "new", "dirty": False}
            schema.write_source_snapshot(
                "indeed", [{"job_id": "last-good"}],
                {"scraped_at": "2026-09-01T00:00:00+00:00", "collector": old},
            )
            result = local_sources.run_one("indeed", new)
            local_sources.write_health([result], new)
            health = json.loads((Path(tmpdir) / "health.json").read_text(encoding="utf-8"))["sources"]["indeed"]
            self.assertFalse(health["healthy"])
            self.assertEqual("0 first-pass survivors", health["reason"])
            self.assertEqual("old", health["last_success_collector"]["commit"])
            self.assertEqual(1, health["last_good_count"])

    @staticmethod
    def _linkedin_card(job_id: str, title: str = "Software Engineer", location: str = "Austin, TX") -> dict:
        card = schema.make_job(
            source="linkedin", company="Example Tech", title=title,
            location=location, job_id=job_id,
            description="Build Python services for a growing platform team.",
        )
        card["discovery_queries"] = {"linkedin": ["software engineer"]}
        return card

    def _partial_scrape(self, rows: list[dict], *, queries_completed: int = 1) -> dict:
        return {
            "status": "blocked", "reason": "blocked with HTTP 429", "http_status": 429,
            "jobs": rows, "queries_completed": queries_completed, "queries_total": 22,
            "query_stats": [{"query": "software engineer", "stop_reason": "blocked_http_429"}],
        }

    def test_rate_limited_linkedin_merges_partial_rows_over_last_good(self) -> None:
        collector = {"commit": "new", "dirty": False}
        fresh, carried = self._linkedin_card("li-1"), self._linkedin_card("li-2")
        carried["first_seen"] = "2026-09-10T00:00:00+00:00"
        carried["last_seen"] = "2026-09-17T15:00:01+00:00"
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir)
        ), patch.dict(
            local_sources.SOURCES,
            {"linkedin": lambda: self._partial_scrape([fresh, self._linkedin_card("li-3")])},
        ):
            schema.write_source_snapshot(
                "linkedin", [fresh, carried],
                {"scraped_at": "2026-09-17T15:00:00+00:00", "collector": {"commit": "old"}},
            )
            result = local_sources.run_one("linkedin", collector)
            payload = schema.read_source_snapshot_payload("linkedin")

        self.assertEqual("partial", result["status"])
        self.assertFalse(result["source_healthy"])
        self.assertTrue(result["data_usable"])
        self.assertEqual(2, result["fresh_kept"])
        self.assertEqual(1, result["carried_count"])
        self.assertEqual(3, result["merged_count"])
        by_id = {job["job_id"]: job for job in payload["jobs"]}
        self.assertEqual({"li-1", "li-2", "li-3"}, set(by_id))
        self.assertTrue(by_id["li-1"]["verified_this_run"])
        self.assertTrue(by_id["li-3"]["verified_this_run"])
        self.assertFalse(by_id["li-2"]["verified_this_run"])
        self.assertEqual("2026-09-17T15:00:00+00:00", by_id["li-2"]["source_verified_at"])
        self.assertEqual("2026-09-10T00:00:00+00:00", by_id["li-2"]["first_seen"])
        self.assertEqual("2026-09-17T15:00:01+00:00", by_id["li-2"]["last_seen"])
        self.assertTrue(payload["meta"]["partial"])
        self.assertEqual(1, payload["meta"]["carried_count"])

    def test_rate_limit_on_first_page_still_preserves_its_rows(self) -> None:
        collector = {"commit": "new", "dirty": False}
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir)
        ), patch.dict(
            local_sources.SOURCES,
            {"linkedin": lambda: self._partial_scrape([self._linkedin_card("li-9")], queries_completed=0)},
        ):
            schema.write_source_snapshot("linkedin", [self._linkedin_card("li-8")])
            result = local_sources.run_one("linkedin", collector)
            payload = schema.read_source_snapshot_payload("linkedin")

        self.assertEqual("partial", result["status"])
        self.assertEqual(1, result["fresh_kept"])
        self.assertEqual({"li-8", "li-9"}, {job["job_id"] for job in payload["jobs"]})

    def test_global_page_budget_merges_coverage_and_keeps_detail_eligible(self) -> None:
        fresh, carried = self._linkedin_card("li-1"), self._linkedin_card("li-2")
        carried.update(first_seen="2026-09-10T00:00:00+00:00",
                       last_seen="2026-09-17T15:00:01+00:00",
                       description="Cached official description " * 12)
        result_rows = [fresh, self._linkedin_card("li-3")]
        bounded = {
            "status": "ok", "jobs": result_rows, "requests": 12, "responses": 12,
            "pages_fetched": 12, "query_stats": [
                {"query": "software engineer", "stop_reason": "global_page_budget"},
            ],
        }
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir)
        ), patch.object(
            local_sources, "HEALTH_PATH", Path(tmpdir) / "health.json"
        ), patch.dict(local_sources.SOURCES, {"linkedin": lambda: bounded}), patch.object(
            linkedin_local, "enrich_details", return_value={"requests": 0, "responses": 0}
        ) as enrich:
            schema.write_source_snapshot("linkedin", [fresh, carried],
                                         {"scraped_at": "2026-09-17T15:00:00+00:00"})
            result = local_sources.run_one("linkedin", {"commit": "new", "dirty": False})
            payload = schema.read_source_snapshot_payload("linkedin")

        self.assertEqual("partial", result["status"])
        self.assertEqual("search page budget exhausted", result["reason"])
        self.assertTrue(result["search_collection"]["budget_exhausted"])
        self.assertTrue(enrich.call_args.kwargs["allow_requests"])
        self.assertEqual(3, result["merged_count"])
        by_id = {job["job_id"]: job for job in payload["jobs"]}
        self.assertEqual({"li-1", "li-2", "li-3"}, set(by_id))
        self.assertFalse(by_id["li-2"]["verified_this_run"])
        self.assertEqual("2026-09-10T00:00:00+00:00", by_id["li-2"]["first_seen"])
        self.assertEqual("2026-09-17T15:00:01+00:00", by_id["li-2"]["last_seen"])
        self.assertEqual(carried["description"], by_id["li-2"]["description"])
        self.assertTrue(payload["meta"]["partial"])

    def test_focused_linkedin_queries_carry_unqueried_jobs_without_refreshing_them(self) -> None:
        fresh, carried = self._linkedin_card("li-1"), self._linkedin_card("li-2")
        carried.update(first_seen="2026-09-10T00:00:00+00:00",
                       last_seen="2026-09-17T15:00:01+00:00")
        focused = {"status": "ok", "jobs": [fresh], "coverage_limited": True,
                   "query_stats": [{"query": "software engineer", "stop_reason": "low_unique_yield"}]}
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir)
        ), patch.object(local_sources, "HEALTH_PATH", Path(tmpdir) / "health.json"), patch.dict(
            local_sources.SOURCES, {"linkedin": lambda: focused}
        ), patch.object(
            linkedin_local, "enrich_details", return_value={"requests": 0, "responses": 0}
        ) as enrich:
            schema.write_source_snapshot("linkedin", [fresh, carried],
                                         {"scraped_at": "2026-09-17T15:00:00+00:00"})
            result = local_sources.run_one("linkedin", {"commit": "new", "dirty": False})
            payload = schema.read_source_snapshot_payload("linkedin")
        self.assertEqual("partial", result["status"])
        self.assertEqual("focused query coverage", result["reason"])
        self.assertTrue(enrich.call_args.kwargs["allow_requests"])
        by_id = {job["job_id"]: job for job in payload["jobs"]}
        self.assertEqual(2, len(by_id))
        self.assertFalse(by_id["li-2"]["verified_this_run"])
        self.assertEqual("2026-09-10T00:00:00+00:00", by_id["li-2"]["first_seen"])
        self.assertEqual("2026-09-17T15:00:01+00:00", by_id["li-2"]["last_seen"])

    def test_rate_limited_partial_with_every_fresh_row_filtered_is_still_partial(self) -> None:
        collector = {"commit": "new", "dirty": False}
        dropped = self._linkedin_card("li-ca", location="Toronto, ON, Canada")
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir)
        ), patch.dict(local_sources.SOURCES, {"linkedin": lambda: self._partial_scrape([dropped])}):
            schema.write_source_snapshot("linkedin", [self._linkedin_card("li-7")])
            result = local_sources.run_one("linkedin", collector)
            payload = schema.read_source_snapshot_payload("linkedin")

        self.assertEqual("partial", result["status"])
        self.assertEqual(0, result["fresh_kept"])
        self.assertEqual(1, result["carried_count"])
        self.assertEqual(["li-7"], [job["job_id"] for job in payload["jobs"]])

    def test_empty_rate_limited_collection_keeps_last_good_untouched(self) -> None:
        collector = {"commit": "new", "dirty": False}
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir)
        ), patch.dict(local_sources.SOURCES, {"linkedin": lambda: self._partial_scrape([])}):
            schema.write_source_snapshot(
                "linkedin", [self._linkedin_card("li-6")], {"scraped_at": "2026-09-17T15:00:00+00:00"},
            )
            result = local_sources.run_one("linkedin", collector)
            payload = schema.read_source_snapshot_payload("linkedin")

        self.assertEqual("skipped_unavailable", result["status"])
        self.assertEqual("2026-09-17T15:00:00+00:00", payload["meta"]["scraped_at"])
        self.assertNotIn("partial", payload["meta"])

    def test_rate_limited_enrichment_issues_no_further_linkedin_requests(self) -> None:
        session = Mock()
        session.get.side_effect = AssertionError("no LinkedIn request after HTTP 429")
        row = self._linkedin_card("li-5")
        row["description"] = ""
        with patch.object(linkedin_local, "_scrapling_fetch_html") as scrapling:
            stats = linkedin_local.enrich_details(
                [row], session=session, allow_requests=False,
            )
        scrapling.assert_not_called()
        self.assertEqual([], session.mock_calls)
        self.assertEqual(0, stats["requests"])
        self.assertEqual("rate_limited_no_further_requests", stats["blocked"])
        self.assertEqual("linkedin_rate_limited", row["enrichment_failure_reason"])

    def test_rate_limited_enrichment_still_reuses_cached_details(self) -> None:
        row = self._linkedin_card("li-4")
        row["description"] = ""
        prior = self._linkedin_card("li-4")
        prior["linkedin_detail_fetched_at"] = datetime.now(timezone.utc).isoformat()
        session = Mock()
        session.get.side_effect = AssertionError("no LinkedIn request after HTTP 429")
        stats = linkedin_local.enrich_details(
            [row], previous_jobs=[prior], session=session, allow_requests=False, cooldown=True,
        )
        self.assertEqual(1, stats["cache_reused"])
        self.assertEqual(prior["description"], row["description"])
        self.assertEqual(0, stats["requests"])

    def test_linkedin_search_returns_cards_collected_before_the_429(self) -> None:
        card_html = (
            '<div class="base-card" data-entity-urn="urn:li:jobPosting:111">'
            '<h3>Software Engineer</h3><h4>Example Tech</h4>'
            '<span class="job-search-card__location">Austin, TX</span>'
            '<a class="base-card__full-link" href="https://www.linkedin.com/jobs/view/111?ref=x"></a>'
            "</div>"
        )
        responses = [Mock(status_code=200, text=card_html + card_html.replace("111", "112")), Mock(status_code=429, text="")]
        session = Mock()
        session.get.side_effect = responses
        with patch.object(linkedin_local.time, "sleep"):
            result = linkedin_local.scrape(keywords=["software engineer"], session=session)

        self.assertEqual("blocked", result["status"])
        self.assertEqual(429, result["http_status"])
        self.assertEqual(0, result["queries_completed"])
        self.assertEqual(["111", "112"], [job["job_id"] for job in result["jobs"]])

    def test_partial_attempt_keeps_last_success_and_records_partial_freshness(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir)
        ), patch.object(local_sources, "HEALTH_PATH", Path(tmpdir) / "health.json"):
            old = {"commit": "old", "dirty": False}
            new = {"commit": "new", "dirty": False}
            schema.write_source_snapshot(
                "linkedin", [self._linkedin_card("li-1")],
                {"scraped_at": "2026-09-17T15:00:00+00:00", "collector": old},
            )
            local_sources.write_health([{
                "source": "linkedin", "status": "ok", "count": 1,
                "attempted_at": "2026-09-17T15:00:00+00:00",
                "succeeded_at": "2026-09-17T15:00:00+00:00",
            }], old)
            schema.write_source_snapshot(
                "linkedin", [self._linkedin_card("li-1"), self._linkedin_card("li-2")],
                {"scraped_at": "2026-09-18T00:00:00+00:00", "partial": True},
            )
            local_sources.write_health([{
                "source": "linkedin", "status": "partial", "source_healthy": False,
                "reason": "blocked with HTTP 429", "count": 1, "collected_count": 4,
                "fresh_kept": 1, "carried_count": 1,
                "attempted_at": "2026-09-18T00:00:00+00:00",
                "partial_at": "2026-09-18T00:00:00+00:00",
            }], new)
            health = json.loads((Path(tmpdir) / "health.json").read_text(encoding="utf-8"))["sources"]["linkedin"]

        self.assertEqual("partial", health["status"])
        self.assertFalse(health["healthy"])
        self.assertEqual("2026-09-17T15:00:00+00:00", health["last_success_at"])
        self.assertEqual("2026-09-18T00:00:00+00:00", health["last_partial_at"])
        self.assertEqual("old", health["last_success_collector"]["commit"])
        self.assertEqual(4, health["partial_collected_count"])
        self.assertEqual(1, health["partial_fresh_kept"])
        self.assertEqual(1, health["partial_carried_count"])
        self.assertEqual(2, health["last_good_count"])

    def test_partial_snapshot_is_never_adopted_as_a_full_success(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir)
        ), patch.object(local_sources, "HEALTH_PATH", Path(tmpdir) / "health.json"):
            schema.write_source_snapshot(
                "linkedin", [self._linkedin_card("li-1")],
                {"scraped_at": "2026-09-18T00:00:00+00:00", "partial": True},
            )
            local_sources.write_health([{
                "source": "linkedin", "status": "partial", "source_healthy": False,
                "attempted_at": "2026-09-18T00:00:00+00:00",
                "partial_at": "2026-09-18T00:00:00+00:00",
            }], {"commit": "new", "dirty": False})
            health = json.loads((Path(tmpdir) / "health.json").read_text(encoding="utf-8"))["sources"]["linkedin"]

        self.assertEqual("", health["last_success_at"])

    def test_partial_required_source_does_not_fail_the_collector(self) -> None:
        partial = {"source": "linkedin", "status": "partial"}
        with patch.object(sys, "argv", ["local_sources.py", "--only", "linkedin"]), patch.object(
            local_sources, "run_one", return_value=partial,
        ), patch.object(local_sources, "write_health"), patch.object(
            local_sources, "OUTPUT_DIR", Path(tempfile.mkdtemp()),
        ):
            local_sources.main()

    def test_carried_rows_keep_their_earned_last_seen(self) -> None:
        now_iso = "2026-09-18T00:00:00+00:00"
        verified_at = "2026-09-17T15:00:00+00:00"
        carried = self._linkedin_card("li-2")
        carried.update(verified_this_run=False, source_verified_at=verified_at)

        stored = board_pipeline.resolve_last_seen(
            dict(carried), {"last_seen": "2026-09-17T15:00:01+00:00"}, now_iso,
        )
        pruned = board_pipeline.resolve_last_seen(dict(carried), None, now_iso)
        discovery_only = dict(carried)
        discovery_only["source_verified_at"] = ""
        discovery_only["first_seen"] = "2026-09-10T00:00:00+00:00"
        fallback = board_pipeline.resolve_last_seen(discovery_only, None, now_iso)
        fresh = board_pipeline.resolve_last_seen(self._linkedin_card("li-1"), None, now_iso)

        self.assertEqual("2026-09-17T15:00:01+00:00", stored)
        self.assertEqual(verified_at, pruned)
        self.assertEqual("2026-09-10T00:00:00+00:00", fallback)
        self.assertEqual(now_iso, fresh)

    def test_official_matching_reuses_prior_identifier_then_allows_later_fallback(self) -> None:
        row = self._linkedin_card("li-official")
        row["description"] = ""
        prior = dict(row, application_url="https://jobs.example.com/req-42")
        official_jobs = [
            dict(company="Example Tech", title="Software Engineer", location="Austin, TX", official_url="https://jobs.example.com/req-41"),
            dict(company="Example Tech", title="Software Engineer", location="Austin, TX", official_url="https://jobs.example.com/req-42"),
        ]
        context = {"registry_entries": [], "by_company": {"example": official_jobs}}
        with patch.object(local_sources.coverage_reconcile, "company_id_for", return_value="example"):
            matched = local_sources._mark_linkedin_official_matches([row], [prior], context, {})

        self.assertEqual(1, matched)
        self.assertEqual("https://jobs.example.com/req-42", row["_linkedin_official_url"])
        self.assertTrue(row["_linkedin_official_defer"])
        self.assertEqual("", row["official_url"])

        board_store = {"key": {
            "source": "linkedin", "job_id": "li-official",
            "official_url": "https://jobs.example.com/req-42", "description_available": False,
        }}
        with patch.object(local_sources.coverage_reconcile, "company_id_for", return_value="example"):
            local_sources._mark_linkedin_official_matches([row], [prior], context, board_store)
        self.assertFalse(row["_linkedin_official_defer"])

    def test_detail_429_cooldown_survives_health_writes_and_recovers_with_probe(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir) / "sources",
        ), patch.object(local_sources, "HEALTH_PATH", Path(tmpdir) / "health.json"):
            collector = {"commit": "test", "dirty": False}
            first = "2026-09-18T00:00:00+00:00"
            second = "2026-09-18T03:00:00+00:00"
            rate_limited = {"requests": 1, "responses": 1, "rate_limited": True}
            local_sources.write_health([{
                "source": "linkedin", "status": "ok", "count": 1,
                "attempted_at": first, "detail_enrichment": rate_limited,
            }], collector)
            local_sources.write_health([{
                "source": "linkedin", "status": "partial", "count": 1,
                "attempted_at": "2026-09-18T01:00:00+00:00", "detail_enrichment": {"requests": 0},
            }], collector)
            local_sources.write_health([{
                "source": "linkedin", "status": "ok", "count": 1,
                "attempted_at": second, "detail_enrichment": rate_limited,
            }], collector)
            before = local_sources._health_source("linkedin")
            local_sources.write_health([{
                "source": "indeed", "status": "ok", "count": 1,
                "attempted_at": second,
            }], collector)
            preserved = local_sources._health_source("linkedin")
            active = local_sources._linkedin_detail_control(datetime(2026, 9, 18, 4, tzinfo=timezone.utc))
            probe = local_sources._linkedin_detail_control(datetime(2026, 9, 19, 4, tzinfo=timezone.utc))
            local_sources.write_health([{
                "source": "linkedin", "status": "ok", "count": 1,
                "attempted_at": "2026-09-19T04:00:00+00:00",
                "detail_enrichment": {"requests": 1, "responses": 1, "rate_limited": False,
                                      "probe": True, "detail_jds_fetched": 1},
            }], collector)
            recovered = local_sources._health_source("linkedin")

        self.assertEqual(2, before["detail_429_streak"])
        self.assertEqual(before["detail_cooldown_until"], preserved["detail_cooldown_until"])
        self.assertEqual((0, True, False), active)
        self.assertEqual((1, False, True), probe)
        self.assertEqual(0, recovered["detail_429_streak"])
        self.assertEqual("", recovered["detail_cooldown_until"])

    def test_intentional_detail_pause_keeps_discovery_and_does_not_count_failures(self) -> None:
        now = datetime.now(timezone.utc)
        until = (now + timedelta(hours=24)).isoformat()
        card = self._linkedin_card("li-paused")
        card["description"] = ""
        calls = []

        def discover(**_kwargs):
            calls.append("search")
            return {"status": "ok", "jobs": [card], "requests": 1, "responses": 1,
                    "pages_fetched": 1, "query_stats": [{"query": "software engineer", "stop_reason": "empty_page"}]}

        resolver = Mock()
        resolver.recover.return_value = "unresolved"
        resolver.stats = {}
        resolver.search_requests = resolver.page_requests = 0
        resolver.search_provider = ""
        session = Mock()
        session.get.side_effect = AssertionError("LinkedIn detail was requested during cooldown")
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            schema, "SOURCES_DIR", Path(tmpdir) / "sources",
        ), patch.object(local_sources, "HEALTH_PATH", Path(tmpdir) / "health.json"), patch.object(
            linkedin_local, "scrape", discover,
        ), patch.dict(local_sources.SOURCES, {"linkedin": discover}), patch.object(
            local_sources.coverage_reconcile, "load_official_context", return_value={},
        ), patch.object(local_sources.board, "load_store", return_value={}), patch.object(
            local_sources.official_jd_recovery, "Resolver", return_value=resolver,
        ), patch.object(linkedin_local, "_make_session", return_value=session):
            health_path = Path(tmpdir) / "health.json"
            health_path.write_text(json.dumps({"sources": {"linkedin": {
                "detail_cooldown_until": until, "detail_cooldown_reason": "intentional pause",
                "detail_429_streak": 3,
            }}}), encoding="utf-8")
            schema.write_source_snapshot("linkedin", [dict(
                card, linkedin_detail_attempted_at=now.isoformat(),
                enrichment_failure_reason="linkedin_http_429",
            )])
            result = local_sources.run_one("linkedin", {"commit": "test", "dirty": False})
            local_sources.write_health([result], {"commit": "test", "dirty": False})
            health = local_sources._health_source("linkedin")
            saved = schema.read_source_snapshot_payload("linkedin")["jobs"]

        self.assertEqual(["search"], calls)
        session.get.assert_not_called()
        self.assertEqual("ok", result["status"])
        self.assertEqual(1, len(saved))
        self.assertEqual("", saved[0]["description"])
        self.assertEqual("deferred", saved[0]["enrichment_status"])
        self.assertNotIn("enrichment_failure_reason", saved[0])
        self.assertEqual(0, health["detail_enrichment"]["requests"])
        self.assertEqual(1, health["detail_enrichment"]["intentional_skips"])
        self.assertEqual(0, health["detail_enrichment"]["retry_deferred"])
        self.assertEqual(0, health["detail_enrichment"]["failed"])
        self.assertEqual({}, health["detail_enrichment"]["failure_reasons"])
        self.assertEqual("cooldown", health["detail_status"])
        self.assertEqual(3, health["detail_429_streak"])
        self.assertEqual(until, health["detail_cooldown_until"])
        self.assertNotIn("detail_last_attempt_at", health)

    def test_failed_detail_probe_restarts_cooldown_without_retry(self) -> None:
        row = self._linkedin_card("li-probe")
        row["description"] = ""
        prior = dict(row, linkedin_detail_attempted_at=datetime.now(timezone.utc).isoformat(),
                     enrichment_failure_reason="linkedin_http_403")
        response = SimpleNamespace(status_code=429, text="")
        session = Mock()
        session.get.return_value = response
        with patch.object(linkedin_local, "_scrapling_fetch_html") as scrapling:
            detail = linkedin_local.enrich_details([row], previous_jobs=[prior], session=session,
                                                   request_limit=1, probe=True)
        detail["probe"] = True
        state = {"detail_cooldown_until": datetime.now(timezone.utc).isoformat(), "detail_429_streak": 0}
        now = datetime.now(timezone.utc)
        local_sources._update_linkedin_detail_health(state, detail, now)
        session.get.assert_called_once()
        scrapling.assert_not_called()
        self.assertEqual(1, detail["requests"])
        self.assertEqual("cooldown", state["detail_status"])
        self.assertGreater(datetime.fromisoformat(state["detail_cooldown_until"]), now)
        self.assertEqual(1, state["detail_429_streak"])

    def test_successful_detail_probe_restores_normal_budget(self) -> None:
        row = self._linkedin_card("li-probe-success")
        row["description"] = ""
        session = Mock()
        session.get.return_value = SimpleNamespace(
            status_code=200,
            text='<div class="show-more-less-html__markup">A full verified job description.</div>',
        )
        with patch.object(linkedin_local.time, "sleep"):
            detail = linkedin_local.enrich_details([row], session=session, request_limit=1, probe=True)
        detail["probe"] = True
        state = {"detail_cooldown_until": datetime.now(timezone.utc).isoformat(), "detail_429_streak": 2}
        local_sources._update_linkedin_detail_health(state, detail, datetime.now(timezone.utc))
        self.assertEqual(1, detail["detail_jds_fetched"])
        self.assertEqual("active", state["detail_status"])
        self.assertEqual("", state["detail_cooldown_until"])
        self.assertEqual(0, state["detail_429_streak"])

    def test_runner_executes_collector_from_fetched_origin_main(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            remote, repo = base / "remote.git", base / "repo"
            subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
            subprocess.run(["git", "init", "-b", "main", str(repo)], check=True, capture_output=True)
            (repo / "scripts").mkdir()
            shutil.copy(ROOT / "scripts" / "local_source_sync.sh", repo / "scripts" / "local_source_sync.sh")
            collector = repo / "local_sources.py"
            collector.write_text("print('old collector')\n", encoding="utf-8")
            for key, value in (("user.name", "Test"), ("user.email", "test@example.com")):
                subprocess.run(["git", "-C", str(repo), "config", key, value], check=True)
            subprocess.run(["git", "-C", str(repo), "remote", "add", "origin", str(remote)], check=True)
            subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
            subprocess.run(["git", "-C", str(repo), "commit", "-m", "old"], check=True, capture_output=True)
            old = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
            subprocess.run(["git", "-C", str(repo), "push", "-u", "origin", "main"], check=True, capture_output=True)

            collector.write_text(
                "import json, subprocess\nfrom pathlib import Path\n"
                "sha=subprocess.run(['git','rev-parse','HEAD'],check=True,capture_output=True,text=True).stdout.strip()\n"
                "path=Path('output/sources/linkedin.json');path.parent.mkdir(parents=True,exist_ok=True)\n"
                "path.write_text(json.dumps({'collector':sha}))\nprint('current collector',sha)\n",
                encoding="utf-8",
            )
            runner = repo / "scripts" / "local_source_sync.sh"
            runner.write_text(
                runner.read_text(encoding="utf-8").replace(
                    "set -uo pipefail", "set -uo pipefail\necho 'current runner logic'", 1,
                ),
                encoding="utf-8",
            )
            subprocess.run(["git", "-C", str(repo), "add", "local_sources.py", "scripts/local_source_sync.sh"], check=True)
            subprocess.run(["git", "-C", str(repo), "commit", "-m", "current"], check=True, capture_output=True)
            current = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
            subprocess.run(["git", "-C", str(repo), "push", "origin", "main"], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(repo), "checkout", "--detach", old], check=True, capture_output=True)

            env = os.environ.copy()
            env.update({"PYTHON_BIN": sys.executable, "SKIP_PUSH": "1", "TMPDIR": str(base)})
            run = subprocess.run(
                ["bash", "scripts/local_source_sync.sh"], cwd=repo, env=env,
                check=True, capture_output=True, text=True,
            )
            self.assertIn("current runner logic", run.stdout)
            self.assertIn(f"current collector {current}", run.stdout)
            self.assertIn(f"collector commit: {current}", run.stdout)
            self.assertFalse(list(base.glob("jobboard-source-*")))


if __name__ == "__main__":
    unittest.main()
