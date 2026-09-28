from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import pipeline_health
import board_pipeline


class PipelineHealthTests(unittest.TestCase):
    def test_missing_required_snapshot_is_failed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report, _ = pipeline_health.build(Path(tmp), datetime(2026, 9, 28, tzinfo=timezone.utc))
        self.assertEqual("Failed", report["overall"])
        self.assertEqual("Failed", report["components"]["board"]["run_state"])

    def test_latest_runs_use_one_format_and_current_run_jd_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 28, 12, tzinfo=timezone.utc)
            attempt = now.isoformat()
            for key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": attempt, "entries": [{"title": "Engineer", "description_available": True}],
                }))
            (root / "output" / "board" / "latest_stats.json").write_text(json.dumps({
                "run_at": attempt, "funnel": {"after_dedup": 10},
                "source_raw": {"ats": 6, "linkedin": 2, "indeed": 2},
                "output": {"new_jobs": 2, "new_jobs_added": 1, "shown": 4,
                           "new_jobs_by_source": {"ats": {"found": 1, "added": 1},
                                                  "linkedin": {"found": 1, "added": 0}}},
                "enrichment": {"direct": {"http_requests": 2, "jds_resolved": 1}},
                "online_recovery": {"jobs_processed": 3, "jds_recovered": 1,
                                    "search_requests": 1, "page_requests": 1},
                "failures": {"discovery": ["Indeed discovery partial: connection reset"]},
            }))
            (root / "output" / "official_careers" / "latest_stats.json").write_text(json.dumps({
                "run_at": attempt, "enrichment": {"discovered": 20},
                "output": {"new_jobs": 2, "shown": 3}, "funnel": {"after_prefilter": 10},
                "jd_recovery": {"eligible": 10, "usable_jd": 8, "cache_reused": 2,
                                "detail_requests": 2, "per_company": {
                                    "Example": {"eligible": 10, "usable_jd": 8, "detail_success": 1}}},
            }))
            (root / "output" / "syncareer" / "latest_stats.json").write_text(json.dumps({"run_at": attempt}))
            sources = root / "output" / "sources"
            sources.mkdir(parents=True)
            sources.joinpath("health.json").write_text(json.dumps({"sources": {
                "linkedin": {"status": "partial", "healthy": False, "required": True,
                             "reason": "focused query coverage", "last_attempt_at": attempt,
                             "last_partial_at": attempt, "last_success_at": (now - timedelta(days=6)).isoformat(),
                             "partial_collected_count": 2, "partial_fresh_kept": 2,
                             "partial_carried_count": 1,
                             "search_collection": {"requests": 2, "responses": 2, "coverage_limited": True},
                             "detail_enrichment": {"eligible": 1, "jds_resolved": 1,
                                                   "detail_jds_fetched": 1, "requests": 1, "responses": 1}},
                "indeed": {"status": "partial", "healthy": False, "required": True,
                           "reason": "connection reset", "last_attempt_at": attempt,
                           "last_partial_at": attempt, "last_success_at": (now - timedelta(hours=2)).isoformat(),
                           "partial_fresh_kept": 1, "partial_carried_count": 1,
                           "queries_succeeded": 1, "queries_failed": 1, "queries_not_run": 1},
                "glassdoor": {"status": "skipped_unavailable", "healthy": False, "required": False,
                              "reason": "HTTP 403", "last_attempt_at": attempt,
                              "last_success_at": (now - timedelta(days=10)).isoformat()},
            }, "local_recovery": {"run_at": attempt, "generic_jobs_processed": 2,
                                   "search_requests": 1, "official_page_requests": 1}}))
            sources.joinpath("linkedin.json").write_text(json.dumps({
                "meta": {"scraped_at": attempt}, "jobs": [
                    {"first_seen": attempt, "source_verified_at": attempt, "verified_this_run": True},
                    {"first_seen": (now - timedelta(hours=1)).isoformat(),
                     "source_verified_at": attempt, "verified_this_run": True},
                    {"first_seen": (now - timedelta(days=2)).isoformat(), "verified_this_run": False},
                ],
            }))
            sources.joinpath("indeed.json").write_text(json.dumps({
                "meta": {"scraped_at": attempt}, "jobs": [
                    {"description": "x" * 250, "verified_this_run": True, "source_verified_at": attempt},
                    {"description": "y" * 250, "verified_this_run": False},
                ],
            }))
            sources.joinpath("glassdoor.json").write_text(json.dumps({"jobs": [{}]}))
            report, history = pipeline_health.build(root, now)
            pipeline_health.write(root / "public", report, history)
            page = (root / "public" / "health.html").read_text()
        self.assertEqual("Partial", report["overall"])
        self.assertEqual("Healthy", report["components"]["linkedin"]["run_state"])
        self.assertIn("2 found · 2 kept · 1 new this run · 1 seen earlier today",
                      report["latest_runs"]["linkedin"]["jobs"])
        self.assertIn("1 fresh jobs needed JD · 1 resolved", report["latest_runs"]["linkedin"]["jd"])
        self.assertEqual(1, report["groups"]["Local Mac"]["new_jds_this_run"])
        self.assertEqual("Partial", report["latest_runs"]["board"]["status"])
        self.assertIn("10 current source jobs · 2 new to Board · 4 A/B shown · 1 newly added to A/B",
                      report["latest_runs"]["board"]["jobs"])
        self.assertIn("current / new: ATS 6 / 1 · LinkedIn 2 / 1 · Indeed 2 / 0",
                      report["latest_runs"]["board"]["sources"])
        self.assertIn("20 raw listings scanned · 10 relevant after filters · 2 new",
                      report["latest_runs"]["official"]["jobs"])
        self.assertIn("JD recovery pool: 10 candidates · 8 have JD (80.0%) · 2 unresolved",
                      report["latest_runs"]["official"]["jd"])
        self.assertEqual(2, report["today"]["board"]["new"])
        self.assertEqual(1, report["today"]["board"]["new_added"])
        self.assertIn("ATS healthy · Indeed partial", report["latest_runs"]["board"]["sources"])
        self.assertIn("1 searches completed · 1 failed · 1 not run", report["latest_runs"]["indeed"]["requests"])
        self.assertIn("1/1 fresh jobs kept have JD · 0 missing", report["latest_runs"]["indeed"]["jd"])
        self.assertLess(page.index("Online Board"), page.index("LinkedIn Local"))
        self.assertLess(page.index("LinkedIn Local"), page.index("Big Company Official"))
        self.assertLess(page.index("Big Company Official"), page.index("<h2>Today</h2>"))
        self.assertEqual(4, page.count('<article class="run-card">'))
        for heading in ("Latest runs", "Today", "Needs attention", "Execution", "Technical details"):
            self.assertIn(heading, page)
        self.assertIn("<th>Consecutive failures</th>", page)
        self.assertNotIn("<h2>Components</h2>", page)
        self.assertNotIn("<h2>Coverage</h2>", page)
        self.assertIn("<th>New JDs this run</th>", page)
        self.assertIn("1 fetched directly · 0 recovered later", page)
        self.assertNotIn("JDs recovered</th>", page)

    def test_indeed_partial_counts_and_board_failure_are_visible(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 28, 12, tzinfo=timezone.utc)
            for key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"title": "Engineer"}],
                }))
                if key == "board":
                    out.joinpath("run_history.json").write_text(json.dumps({"runs": [{
                        "run_at": now.isoformat(),
                        "failures": {"discovery": ["Indeed discovery partial: connection reset"]},
                    }]}))
            sources = root / "output" / "sources"
            sources.mkdir(parents=True)
            sources.joinpath("health.json").write_text(json.dumps({"sources": {
                "linkedin": {"status": "ok", "healthy": True, "required": True,
                             "last_attempt_at": now.isoformat(), "last_success_at": now.isoformat()},
                "indeed": {"status": "partial", "healthy": False, "required": True,
                           "reason": "ConnectionResetError: connection reset",
                           "last_attempt_at": now.isoformat(), "last_partial_at": now.isoformat(),
                           "last_success_at": (now - timedelta(hours=2)).isoformat(),
                           "partial_fresh_kept": 2, "partial_carried_count": 1,
                           "queries_succeeded": 1, "queries_failed": 1, "queries_not_run": 1},
            }}))
            sources.joinpath("linkedin.json").write_text(json.dumps({"jobs": [{}]}))
            sources.joinpath("indeed.json").write_text(json.dumps({"jobs": [{}, {}, {}]}))
            report, _ = pipeline_health.build(root, now)
        self.assertEqual("Partial", report["components"]["indeed"]["status"])
        self.assertEqual("Partial", report["components"]["board"]["status"])
        self.assertEqual("Partial", report["overall"])
        self.assertEqual("Partial", report["components"]["indeed"]["run_state"])
        self.assertIn("1 searches completed · 1 failed · 1 not run", report["latest_runs"]["indeed"]["requests"])
        self.assertIn("1 queries succeeded · 1 failed / 1 not run · 2 fresh jobs kept · 1 cached jobs reused",
                      report["components"]["indeed"]["detail"])

    def test_linkedin_latest_run_counts_and_429_are_prominent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 27, 4, tzinfo=timezone.utc)
            attempt = now.isoformat()
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": attempt, "entries": [{"title": "Engineer"}],
                }))
            sources = root / "output" / "sources"
            sources.mkdir(parents=True)
            sources.joinpath("health.json").write_text(json.dumps({
                "sources": {
                    "linkedin": {
                        "status": "partial", "required": True, "last_attempt_at": attempt,
                        "last_partial_at": attempt, "last_success_at": attempt,
                        "partial_collected_count": 4, "partial_fresh_kept": 2,
                        "detail_enrichment": {"rate_limited": True, "blocked": "HTTP 429"},
                    },
                    "indeed": {"last_success_at": attempt},
                    "glassdoor": {"last_success_at": attempt, "required": False},
                },
                "local_recovery": {
                    "run_at": (now + timedelta(minutes=1)).isoformat(),
                    "linkedin_detail_recoveries": 1, "official_jds_recovered": 0,
                    "linkedin_rate_limited": True,
                },
            }))
            sources.joinpath("linkedin.json").write_text(json.dumps({
                "meta": {"scraped_at": attempt, "detail_enrichment": {"jds_resolved": 1}},
                "jobs": [
                    {"title": "A", "description": "x" * 200, "verified_this_run": True,
                     "source_verified_at": attempt},
                    {"title": "B", "verified_this_run": True, "source_verified_at": attempt},
                    {"title": "old", "description": "y" * 200, "verified_this_run": False},
                ],
            }))
            for source in ("indeed", "glassdoor"):
                sources.joinpath(f"{source}.json").write_text(json.dumps({"jobs": [{}]}))

            report, history = pipeline_health.build(root, now)
            linkedin = report["components"]["linkedin"]
            self.assertEqual("Warning", linkedin["status"])
            self.assertEqual(4, linkedin["latest_run"]["titles_found"])
            self.assertEqual(2, linkedin["latest_run"]["titles_kept"])
            self.assertEqual(1, linkedin["latest_run"]["jds_on_kept_titles"])
            self.assertEqual(1, linkedin["latest_run"]["recovery_linkedin_jds"])
            pipeline_health.write(root / "public", report, history)
            page = (root / "public" / "health.html").read_text()
            self.assertIn("4 found · 2 kept", page)
            self.assertIn("1 recovered later", page)
            self.assertIn("Detail 429", page)
            self.assertLess(page.index("LinkedIn Local"), page.index("<h2>Today</h2>"))
            self.assertLess(page.index("<h2>Today</h2>"), page.index("Local Mac schedule"))
            self.assertIn("9:00 PM PT, 26 September", page)
            self.assertNotIn("2026-09-27T04:00:00+00:00", page)

    def test_execution_elapsed_and_local_recovery_counts_do_not_overlap(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 25, 18, tzinfo=timezone.utc)
            timings = {
                "board": {"elapsed_seconds": 100, "remote_elapsed_seconds": 40},
                "official": {"elapsed_seconds": 20, "scrape_elapsed_seconds": 30},
                "syncareer": {"elapsed_seconds": 60, "remote_elapsed_seconds": 25},
            }
            for key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
                out.joinpath("latest_stats.json").write_text(json.dumps({"run_at": now.isoformat(), **timings[key]}))
            sources = root / "output" / "sources"
            sources.mkdir(parents=True)
            sources.joinpath("health.json").write_text(json.dumps({
                "mac_last_completed_at": now.isoformat(),
                "sources": {name: {"healthy": True, "last_success_at": now.isoformat(),
                                   "last_attempt_elapsed_seconds": seconds}
                            for name, seconds in (("linkedin", 5), ("indeed", 10), ("glassdoor", 6))},
                "local_recovery": {"elapsed_seconds": 7, "official_jds_recovered": 2,
                                   "linkedin_detail_recoveries": 3,
                                   "targeted_linkedin_detail_jds": 4},
            }))
            for name in ("linkedin", "indeed", "glassdoor"):
                sources.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}]}))
            report, _ = pipeline_health.build(root, now)
            self.assertEqual(105, report["groups"]["Remote"]["elapsed_seconds"])
            self.assertEqual(115, report["groups"]["GitHub Actions"]["elapsed_seconds"])
            self.assertEqual(18, report["groups"]["Local Mac"]["elapsed_seconds"])
            self.assertEqual(9, report["groups"]["Local Mac"]["jds_recovered"])
            self.assertEqual(10, report["groups"]["Remote"]["subcomponents"]["Indeed"]["elapsed_seconds"])
            scheduler = report["local_scheduler"]
            self.assertEqual(now.isoformat(), scheduler["last_successful_local_run_at"])
            self.assertFalse(scheduler["scheduled_slot_missed"])
            self.assertEqual("not_needed", scheduler["catch_up_status"])
            pipeline_health.write(root / "public", report, [])
            self.assertIn("Next scheduled run", (root / "public" / "health.html").read_text())

    def test_official_cause_streak_and_last_good_updated_time(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 25, 18, tzinfo=timezone.utc)
            good_at = (now - timedelta(hours=2)).isoformat()
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                (out / store_name).write_text(json.dumps({
                    "updated_at": good_at, "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            official = root / "output" / "official_careers"
            official.joinpath("latest_stats.json").write_text(json.dumps({
                "run_at": now.isoformat(),
                "failures": {"scrape": {"oracle": ["Read timed out (30s)"]}},
            }))
            official.joinpath("run_history.json").write_text(json.dumps({"runs": [
                {"run_at": (now - timedelta(hours=index)).isoformat(),
                 "scrape_failure_sources": ["oracle"],
                 "scrape_failure_causes": {"oracle": "timeout"}}
                for index in range(3)
            ]}))
            sources = root / "output" / "sources"
            sources.mkdir(parents=True)
            sources.joinpath("health.json").write_text(json.dumps({"sources": {
                name: {"healthy": True, "last_success_at": good_at}
                for name in ("linkedin", "indeed", "glassdoor")
            }}))
            for name in ("linkedin", "indeed", "glassdoor"):
                sources.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}]}))
            report, history = pipeline_health.build(root, now)
            item = report["components"]["official"]
            self.assertEqual("Big Company Official (GitHub)", item["label"])
            self.assertEqual("1 scraper failed: Oracle timeout ×3", item["issue"])
            self.assertEqual({"oracle timeout": 3}, item["failure_streaks"])
            self.assertEqual(0, item["consecutive_failures"])
            self.assertEqual(good_at, item["last_good_at"])
            self.assertEqual(now.isoformat(), item["latest_attempt_at"])
            public = root / "public"
            pipeline_health.write(public, report, history)
            page = (public / "health.html").read_text()
            self.assertIn("11:00 AM PT, 25 September", page)
            self.assertNotIn(f"<td>{now.isoformat()}</td>", page)

    def test_llm_impact_keeps_specific_timeout_reason(self) -> None:
        impact = pipeline_health._llm_impact({
            "llm": {"batches_total": 3, "batches_attempted": 3, "batches_failed": 1},
            "failures": {"llm": ["batch_1: ReadTimeout: read timed out"]},
        })
        self.assertIn("ReadTimeout: read timed out", impact)

    def test_repeated_llm_429s_are_collapsed_with_retryable_impact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 13, 22, tzinfo=timezone.utc)
            for key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
                if key == "board":
                    runs = [{
                        "pipeline": "board", "run_at": (now - timedelta(hours=i)).isoformat(),
                        "health": "degraded", "batches_total": 11, "batches_failed": 11,
                        "fallback_count": 111, "output": {"shown": 20},
                    } for i in range(3)]
                    out.joinpath("run_history.json").write_text(json.dumps({"runs": runs}))
                    out.joinpath("latest_stats.json").write_text(json.dumps({
                        "run_at": now.isoformat(), "output": {"shown": 20},
                        "llm": {"batches_total": 11, "batches_failed": 11, "retryable_fallbacks": 111},
                        "failures": {"llm": [f"batch_{i}: HTTP 429: rate_limit_exceeded" for i in range(1, 12)]},
                    }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                name: {"healthy": True, "last_success_at": now.isoformat()}
                for name in ("linkedin", "indeed", "glassdoor")
            }}))
            for name in ("linkedin", "indeed", "glassdoor"):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}]}))

            report, history = pipeline_health.build(root, now)
            board = report["components"]["board"]
            self.assertEqual("Warning", board["status"])
            self.assertEqual(3, board["consecutive_failures"])
            self.assertIn("11/11 LLM batches failed with HTTP 429", board["detail"])
            self.assertIn("rate_limit_exceeded", board["detail"])
            self.assertIn("111 jobs used retryable rule fallback", board["impact"])
            self.assertEqual(3, len([run for run in history if run["pipeline"] == "board"]))

    def test_reuses_runs_and_source_health_and_keeps_unresolved_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 12, 12, tzinfo=timezone.utc)
            for key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                run_dir = root / "output" / folder / "runs"
                run_dir.mkdir(parents=True)
                (run_dir / "2026-09-12_1200_stats.json").write_text(json.dumps({
                    "run_at": now.isoformat(), "output": {"shown": 20},
                    "enrichment": {"needed": 2, "remaining_no_jd": 1},
                }))
                (run_dir.parent / store_name).write_text(json.dumps({"updated_at": now.isoformat(), "entries": [{
                    "company": "Example", "title": "Junior Engineer", "description": "",
                    "source_url": "https://example.test/job", "filter_status": "kept",
                    "enrichment_failure_reason": "no_direct_or_official_url",
                }]}))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                name: {
                    "healthy": True, "required": name != "glassdoor",
                    "last_success_at": now.isoformat(), "last_good_count": 10,
                    **({"status": "ok", "previous_failure": {"cause": "collection", "count": 1}}
                       if name == "indeed" else {}),
                    **({"status": "skipped_unavailable", "healthy": False,
                        "reason": "HTTP 403", "last_attempt_at": now.isoformat()}
                       if name == "glassdoor" else {}),
                }
                for name in ("linkedin", "indeed", "glassdoor")
            }}))
            for name in ("linkedin", "indeed", "glassdoor"):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({
                    "jobs": [{}] * 10,
                    "meta": {"detail_enrichment": {"needed": 3}} if name == "linkedin" else {},
                }))

            report, history = pipeline_health.build(root, now)

            self.assertEqual("Healthy", report["overall"])
            self.assertEqual("Partial", report["components"]["glassdoor"]["run_state"])
            self.assertEqual("Healthy", report["groups"]["Local Mac"]["run_state"])
            self.assertEqual("", report["components"]["indeed"]["issue"])
            self.assertEqual({"cause": "collection", "count": 1},
                             report["components"]["indeed"]["recent_history"])
            self.assertEqual(3, report["enrichment"]["unresolved_thin_or_no_jd"])
            self.assertEqual("https://example.test/job", report["unresolved_examples"][0]["url"])
            self.assertEqual(3, len(history))

    def test_today_counts_new_additions_across_runs_without_summing_retained_shown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sources = root / "output" / "sources"
            sources.mkdir(parents=True)
            sources.joinpath("indeed.json").write_text(json.dumps({
                "meta": {"scraped_at": "2026-09-28T18:40:00+00:00"}, "jobs": [
                {"first_seen": "2026-09-28T16:00:00+00:00"},
                {"first_seen": "2026-09-28T06:00:00+00:00"},
            ]}))
            now = datetime(2026, 9, 28, 20, tzinfo=timezone.utc)
            history = [
                {"pipeline": "board", "run_at": "2026-09-28T15:00:00+00:00", "health": "success",
                 "output": {"new_jobs": 2, "new_jobs_added": 1, "shown": 100,
                            "new_jobs_by_source": {"indeed": {"added": 1}}}},
                {"pipeline": "board", "run_at": "2026-09-28T18:30:00+00:00", "health": "degraded",
                 "output": {"new_jobs": 3, "new_jobs_added": 2, "shown": 101,
                            "new_jobs_by_source": {"indeed": {"added": 2}}}},
                {"pipeline": "board", "run_at": "2026-09-28T06:30:00+00:00", "health": "success",
                 "output": {"new_jobs": 50, "new_jobs_added": 10, "shown": 99}},
            ]
            components = {key: {"run_state": "Healthy", "consecutive_failures": 0, "issue": ""}
                          for key in (*pipeline_health.PIPELINES, "linkedin", "indeed", "glassdoor")}
            today = pipeline_health._today_summary(
                root, now, {"board": history[1]}, history,
                {"indeed": {"last_attempt_at": "2026-09-28T18:40:00+00:00"}}, components)
        self.assertEqual(5, today["board"]["new"])
        self.assertEqual(3, today["board"]["new_added"])
        self.assertEqual(101, today["board"]["shown_latest"])
        self.assertEqual(2, today["board"]["runs"])
        self.assertEqual(1, today["board"]["failed_runs"])
        self.assertEqual(1, today["indeed"]["new"])
        self.assertEqual(3, today["indeed"]["new_added"])
        self.assertEqual("≥1", today["indeed"]["runs"])
        self.assertEqual("—", today["indeed"]["failed_runs"])

    def test_isolated_failed_attempt_with_fresh_last_good_is_recovered_limitation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 12, 12, tzinfo=timezone.utc)
            for key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                "linkedin": {
                    "healthy": False, "required": True, "status": "skipped_unavailable",
                    "reason": "blocked with HTTP 429", "last_attempt_at": now.isoformat(),
                    "last_success_at": now.isoformat(), "last_good_count": 120,
                },
                "indeed": {"healthy": True, "required": True, "last_success_at": now.isoformat(), "last_good_count": 80},
                "glassdoor": {"healthy": True, "required": False, "last_success_at": now.isoformat(), "last_good_count": 20},
            }}))
            for name, count in (("linkedin", 120), ("indeed", 80), ("glassdoor", 20)):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}] * count}))

            report, _history = pipeline_health.build(root, now)

            self.assertEqual("Healthy", report["components"]["linkedin"]["status"])
            self.assertTrue(report["components"]["linkedin"]["data_usable"])
            self.assertIn("search/discovery", report["components"]["linkedin"]["detail"])
            self.assertFalse(any(item.startswith("LinkedIn:") for item in report["problems"]))
            self.assertFalse(report["degradations"])
            self.assertTrue(any(item.startswith("LinkedIn (local/general):") for item in report["limitations"]))

    def test_fresh_partial_does_not_refresh_carried_row_staleness(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 18, 12, tzinfo=timezone.utc)
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                "linkedin": {
                    "healthy": False, "required": True, "status": "partial",
                    "reason": "blocked with HTTP 429",
                    "last_attempt_at": now.isoformat(),
                    "last_partial_at": now.isoformat(),
                    "last_success_at": (now - timedelta(hours=20)).isoformat(),
                    "partial_collected_count": 300, "partial_fresh_kept": 240,
                    "partial_carried_count": 572, "last_good_count": 812,
                },
                "indeed": {"healthy": True, "required": True, "last_success_at": now.isoformat(), "last_good_count": 80},
                "glassdoor": {"healthy": True, "required": False, "last_success_at": now.isoformat(), "last_good_count": 20},
            }}))
            for name, count in (("linkedin", 812), ("indeed", 80), ("glassdoor", 20)):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}] * count}))

            report, _history = pipeline_health.build(root, now)
            linkedin = report["components"]["linkedin"]

        self.assertEqual("Stale", linkedin["status"])
        self.assertTrue(linkedin["data_usable"])
        self.assertEqual(0.0, linkedin["latest_partial_age_hours"])
        self.assertIn("rate_limited_partial_collection", linkedin["degradation_kinds"])
        self.assertIn("collected 300 rows, kept 240", linkedin["detail"])
        self.assertIn("812 (572 carried, last full collection 20.0h old)", linkedin["detail"])
        self.assertIn("partial collection", linkedin["impact"])
        self.assertTrue(any("rate-limited partial collection" in item for item in report["limitations"]))

    def test_partial_over_fresh_full_success_is_healthy_before_three_failures(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 18, 12, tzinfo=timezone.utc)
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                "linkedin": {
                    "healthy": False, "required": True, "status": "partial",
                    "reason": "blocked with HTTP 429",
                    "last_attempt_at": now.isoformat(), "last_partial_at": now.isoformat(),
                    "last_success_at": (now - timedelta(hours=2)).isoformat(),
                    "consecutive_failures": 2,
                    "partial_collected_count": 100, "partial_fresh_kept": 90,
                    "partial_carried_count": 30, "last_good_count": 120,
                },
                "indeed": {"healthy": True, "required": True, "last_success_at": now.isoformat(), "last_good_count": 80},
                "glassdoor": {"healthy": True, "required": False, "last_success_at": now.isoformat(), "last_good_count": 20},
            }}))
            for name, count in (("linkedin", 120), ("indeed", 80), ("glassdoor", 20)):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}] * count}))

            report, _history = pipeline_health.build(root, now)
            linkedin = report["components"]["linkedin"]

        self.assertEqual("Healthy", linkedin["status"])
        self.assertEqual(["partial", "rate-limited", "cached", "scraper errors"], linkedin["keywords"])
        self.assertFalse(any(item.startswith("LinkedIn (local/general):") for item in report["problems"]))

    def test_linkedin_detail_429_and_scrapling_are_reported_separately(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 12, 12, tzinfo=timezone.utc)
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                "linkedin": {
                    "healthy": True, "required": True, "status": "ok",
                    "last_attempt_at": now.isoformat(), "last_success_at": now.isoformat(),
                    "last_good_count": 120,
                    "detail_enrichment": {
                        "blocked": "blocked with HTTP 429", "scrapling_requests": 8,
                        "scrapling_jds_resolved": 5, "remaining_no_jd": 3,
                    },
                },
                "indeed": {"healthy": True, "required": True, "last_success_at": now.isoformat(), "last_good_count": 80},
                "glassdoor": {"healthy": True, "required": False, "last_success_at": now.isoformat(), "last_good_count": 20},
            }}))
            for name, count in (("linkedin", 120), ("indeed", 80), ("glassdoor", 20)):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}] * count}))

            report, _history = pipeline_health.build(root, now)
            linkedin = report["components"]["linkedin"]
            self.assertEqual("Warning", linkedin["status"])
            self.assertIn("detail enrichment blocked: blocked with HTTP 429", linkedin["detail"])
            self.assertIn("Scrapling fallback recovered 5/8", linkedin["detail"])
            self.assertIn("rate-limited", linkedin["keywords"])
            self.assertNotIn("search/discovery attempt", linkedin["detail"])

    def test_linkedin_detail_429_stays_visible_despite_high_scrapling_recovery(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 12, 12, tzinfo=timezone.utc)
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                "linkedin": {
                    "healthy": True, "required": True, "last_success_at": now.isoformat(),
                    "last_attempt_at": now.isoformat(), "last_good_count": 120,
                    "detail_enrichment": {
                        "blocked": "HTTP 429", "scrapling_requests": 100,
                        "scrapling_jds_resolved": 99, "remaining_no_jd": 1,
                    },
                },
                "indeed": {"healthy": True, "last_success_at": now.isoformat()},
                "glassdoor": {"healthy": True, "required": False, "last_success_at": now.isoformat()},
            }}))
            for name, count in (("linkedin", 120), ("indeed", 1), ("glassdoor", 1)):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}] * count}))

            report, _history = pipeline_health.build(root, now)

            self.assertEqual("Warning", report["components"]["linkedin"]["status"])
            self.assertTrue(report["degradations"])
            self.assertTrue(any("recovered detail limitation" in item for item in report["limitations"]))

    def test_intentional_linkedin_detail_pause_is_reported_as_cooldown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 24, 4, tzinfo=timezone.utc)
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({"updated_at": now.isoformat(), "entries": [{}]}))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                "linkedin": {
                    "healthy": True, "required": True, "status": "ok",
                    "last_attempt_at": now.isoformat(), "last_success_at": now.isoformat(),
                    "detail_status": "cooldown", "detail_cooldown_reason": "intentional pause",
                    "detail_cooldown_until": (now + timedelta(hours=24)).isoformat(),
                    "detail_enrichment": {"requests": 0, "intentional_skips": 1,
                                          "blocked": "", "remaining_no_jd": 1},
                },
                "indeed": {"healthy": True, "last_success_at": now.isoformat()},
                "glassdoor": {"healthy": True, "required": False, "last_success_at": now.isoformat()},
            }}))
            for name in ("linkedin", "indeed", "glassdoor"):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}]}))

            report, _history = pipeline_health.build(root, now)

        linkedin = report["components"]["linkedin"]
        self.assertEqual("Healthy", linkedin["status"])
        self.assertEqual("cooldown", linkedin["detail_status"])
        self.assertIn("detail intentionally paused/cooldown", linkedin["detail"])
        self.assertIn("search/discovery continues", linkedin["detail"])
        self.assertNotIn("rate-limited", linkedin["keywords"])

    def test_committed_latest_stats_exposes_specific_failure_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 12, 12, tzinfo=timezone.utc)
            for key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
                if key == "official":
                    out.joinpath("latest_stats.json").write_text(json.dumps({
                        "run_at": now.isoformat(), "output": {"shown": 12},
                        "failures": {
                            "scrape": {"meta": ["blocked with HTTP 429"]},
                            "llm": ["chunk_1: timeout"],
                        },
                    }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                name: {"healthy": True, "last_success_at": now.isoformat(), "last_good_count": 10}
                for name in ("linkedin", "indeed", "glassdoor")
            }}))
            for name in ("linkedin", "indeed", "glassdoor"):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}] * 10}))

            report, history = pipeline_health.build(root, now)

            official = report["components"]["official"]
            self.assertEqual("Healthy", official["status"])
            self.assertEqual(2, official["failure_count"])
            self.assertIn("meta: blocked with HTTP 429", official["detail"])
            self.assertIn("chunk_1: timeout", official["detail"])
            self.assertFalse(report["degradations"])
            self.assertEqual("official", history[0]["pipeline"])

    def test_official_link_only_and_linkedin_failures_are_limitations(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 12, 12, tzinfo=timezone.utc)
            for key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
                if key == "official":
                    out.joinpath("latest_stats.json").write_text(json.dumps({
                        "run_at": now.isoformat(),
                        "failures": {"scrape": {"citadel": ["link only"], "linkedin": ["HTTP 429"]}},
                    }))
                    out.joinpath("run_history.json").write_text(json.dumps({"runs": [
                        {"run_at": (now - timedelta(hours=index)).isoformat(), "health": "degraded"}
                        for index in range(10)
                    ]}))
            config = root / "config"
            config.mkdir()
            config.joinpath("official_careers.json").write_text(json.dumps({"companies": [
                {"id": "citadel", "adapter": "skip"}, {"id": "linkedin", "adapter": "linkedin_company"},
            ]}))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                name: {"healthy": True, "last_success_at": now.isoformat()}
                for name in ("linkedin", "indeed", "glassdoor")
            }}))
            for name in ("linkedin", "indeed", "glassdoor"):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}]}))

            report, history = pipeline_health.build(root, now)

            official = report["components"]["official"]
            self.assertEqual("Healthy", official["status"])
            self.assertEqual(0, official["failure_count"])
            self.assertEqual("limited", official["latest_attempt_status"])
            self.assertEqual(0, official["consecutive_failures"])
            self.assertIn("LinkedIn company adapter excluded from status: HTTP 429", official["detail"])
            self.assertNotIn("Warning at 5", official["detail"])
            self.assertNotIn("prior scraper identities", official["detail"])
            self.assertNotIn("citadel", official["detail"])
            self.assertTrue(any("citadel" in item for item in report["limitations"]))
            self.assertTrue(any("linkedin_company_official_adapter" in item for item in report["limitations"]))
            official_runs = [item for item in history if item["pipeline"] == "official"]
            self.assertEqual("limited", official_runs[0]["health"])
            self.assertEqual("unknown", official_runs[1]["health"])
            pipeline_health.write(root / "public", report, history)
            self.assertIn("Consecutive failures", (root / "public" / "health.html").read_text())

    def test_official_scraper_error_thresholds(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 22, 12, tzinfo=timezone.utc)
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                name: {"healthy": True, "last_success_at": now.isoformat()}
                for name in ("linkedin", "indeed", "glassdoor")
            }}))
            for name in ("linkedin", "indeed", "glassdoor"):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}]}))

            official_stats = root / "output" / "official_careers" / "latest_stats.json"
            for count, expected in ((2, "Healthy"), (4, "Healthy"), (5, "Warning"), (9, "Warning"), (10, "Problem")):
                with self.subTest(count=count):
                    official_stats.write_text(json.dumps({
                        "run_at": now.isoformat(), "output": {"shown": 20},
                        "failures": {"scrape": {
                            f"source-{index}": ["HTTP 429", "retry timeout"] if index == 0 else ["error"]
                            for index in range(count)
                        }},
                    }))
                    report, _history = pipeline_health.build(root, now)
                    official = report["components"]["official"]
                    self.assertEqual(expected, official["status"])
                    self.assertEqual(count, official["scraper_error_count"])
                    self.assertEqual(1 if count >= 5 else 0, official["consecutive_failures"])
                    self.assertEqual("degraded" if count >= 5 else "limited", official["latest_attempt_status"])
                    self.assertIn(f"{count} scraper failures", official["keywords"])
                    self.assertIn(f"{count} scraper failures", official["detail"])
                    for index in range(count):
                        self.assertIn(f"source-{index} (", official["detail"])
                    self.assertIn("rate-limited", official["keywords"])
                    self.assertEqual(expected, report["overall_detail_status"])
                    self.assertEqual("Partial", report["overall"])

    def test_official_scraper_streak_tracks_each_cause(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = root / "config"
            config.mkdir()
            config.joinpath("official_careers.json").write_text(json.dumps({"companies": [
                {"id": "link-only", "adapter": "skip"},
            ]}))
            sources = [f"source-{index}" for index in range(5)]
            now = datetime(2026, 9, 22, 12, tzinfo=timezone.utc)
            run = {"run_at": now.isoformat()}
            history = [
                {"pipeline": "official", "run_at": run["run_at"],
                 "scrape_failure_sources": sources, "scrape_failure_causes": {"source-0": "429"}},
                {"pipeline": "official", "run_at": (now - timedelta(hours=1)).isoformat(),
                 "scrape_failure_sources": [*sources, "linkedin", "link-only"],
                 "scrape_failure_causes": {"source-0": "429"}},
                {"pipeline": "official", "run_at": (now - timedelta(hours=2)).isoformat(),
                 "scrape_failure_sources": [*sources[:4], "linkedin"],
                 "scrape_failure_causes": {"source-0": "timeout"}},
                {"pipeline": "official", "run_at": (now - timedelta(hours=3)).isoformat(),
                 "scrape_failure_sources": sources},
            ]
            self.assertEqual(2, pipeline_health._official_scraper_streak(history, "source-0", "429", run["run_at"]))
            history[1].pop("scrape_failure_causes")
            self.assertEqual(1, pipeline_health._official_scraper_streak(history, "source-0", "429", run["run_at"]))
            self.assertEqual(2, pipeline_health._consecutive_official_degraded(root, history, run, 5))
            self.assertEqual(0, pipeline_health._consecutive_official_degraded(root, history, run, 4))
            history[1].pop("scrape_failure_sources")
            self.assertEqual(1, pipeline_health._consecutive_official_degraded(root, history, run, 5))

            official_dir = root / "output" / "official_careers"
            official_dir.mkdir(parents=True)
            path = official_dir / "run_history.json"
            board_pipeline.append_run_history(path, "official", {
                "run_at": run["run_at"],
                "ignored_scrape_sources": ["linkedin", "link-only"],
                "failures": {"scrape": {
                    "linkedin": ["HTTP 429"], "link-only": ["not scraped"],
                    **{source: ["error"] for source in sources},
                }},
            })
            recorded = json.loads(path.read_text())["runs"][0]
            self.assertEqual(["linkedin", "link-only", *sources], recorded["scrape_failure_sources"])
            self.assertEqual("429", recorded["scrape_failure_causes"]["linkedin"])
            self.assertEqual("degraded", recorded["health"])
            board_pipeline.append_run_history(path, "official", {
                "run_at": (now + timedelta(hours=1)).isoformat(),
                "ignored_scrape_sources": ["linkedin", "link-only"],
                "failures": {"scrape": {"linkedin": ["HTTP 429"], "link-only": ["not scraped"]}},
            })
            limited = json.loads(path.read_text())["runs"][0]
            self.assertEqual("limited", limited["health"])
            official_dir.joinpath("latest_stats.json").write_text(json.dumps({
                "run_at": limited["run_at"],
                "failures": {"scrape": {"linkedin": ["HTTP 429"], "link-only": ["not scraped"]}},
            }))
            _latest, normalized = pipeline_health._run_history(root)
            official_runs = [item for item in normalized if item["pipeline"] == "official"]
            self.assertEqual(["limited", "degraded"], [item["health"] for item in official_runs])

    def test_linkedin_threshold_and_optional_children_do_not_warn_board(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 22, 12, tzinfo=timezone.utc)
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            for name in ("linkedin", "indeed", "glassdoor"):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}]}))

            for failures, expected in ((1, "Healthy"), (2, "Healthy"), (3, "Warning")):
                with self.subTest(failures=failures):
                    source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                        "linkedin": {
                            "healthy": False, "required": True, "status": "partial",
                            "reason": "blocked with HTTP 429", "last_attempt_at": now.isoformat(),
                            "last_success_at": now.isoformat(), "last_partial_at": now.isoformat(),
                            "consecutive_failures": failures,
                        },
                        "indeed": {"healthy": True, "required": True, "last_success_at": now.isoformat()},
                        "glassdoor": {
                            "healthy": False, "required": False, "status": "skipped_unavailable",
                            "reason": "HTTP 403", "last_attempt_at": now.isoformat(),
                            "last_success_at": now.isoformat(), "consecutive_failures": 10,
                        },
                    }}))
                    report, _history = pipeline_health.build(root, now)
                    self.assertEqual(expected, report["components"]["linkedin"]["status"])
                    self.assertEqual("Healthy", report["components"]["board"]["status"])
                    self.assertEqual("Partial", report["overall"])
                    self.assertIn("scraper errors", report["components"]["board"]["keywords"])

    def test_syncareer_low_volume_requires_two_consecutive_runs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 22, 12, tzinfo=timezone.utc)
            for _key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                name: {"healthy": True, "last_success_at": now.isoformat()}
                for name in ("linkedin", "indeed", "glassdoor")
            }}))
            for name in ("linkedin", "indeed", "glassdoor"):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}]}))

            syncareer = root / "output" / "syncareer"
            current = {"run_at": now.isoformat(), "mode": "pipeline", "health": "success", "output": {"shown": 2}}
            syncareer.joinpath("latest_stats.json").write_text(json.dumps(current))
            for previous, expected in ((8, "Healthy"), (3, "Warning")):
                with self.subTest(previous=previous):
                    runs = [current, {
                        "run_at": (now - timedelta(hours=12)).isoformat(), "mode": "pipeline",
                        "health": "success", "output": {"shown": previous},
                    }, *[{
                        "run_at": (now - timedelta(days=index)).isoformat(), "mode": "pipeline",
                        "health": "success", "output": {"shown": 20},
                    } for index in range(1, 6)]]
                    syncareer.joinpath("run_history.json").write_text(json.dumps({"runs": runs}))
                    report, _history = pipeline_health.build(root, now)
                    component = report["components"]["syncareer"]
                    self.assertEqual(expected, component["status"])
                    self.assertEqual(expected == "Warning", "low-volume" in component["keywords"])

    def test_legacy_zero_telemetry_is_marked_unknown_but_measured_zero_is_preserved(self) -> None:
        legacy = pipeline_health._normalize_run_telemetry({
            "latency_seconds": 0, "json_reliability": 0, "batches_succeeded": 0,
        })
        measured = pipeline_health._normalize_run_telemetry({
            "latency_seconds": 0, "latency_measured": True,
            "json_reliability_measured": True, "batch_outcomes_measured": True,
        })
        self.assertFalse(legacy["latency_measured"])
        self.assertFalse(legacy["json_reliability_measured"])
        self.assertFalse(legacy["batch_outcomes_measured"])
        self.assertTrue(measured["latency_measured"])

    def test_failed_workflow_distinguishes_fresh_last_good_from_unusable_data(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime(2026, 9, 12, 12, tzinfo=timezone.utc)
            for key, (_label, folder, store_name) in pipeline_health.PIPELINES.items():
                out = root / "output" / folder
                out.mkdir(parents=True)
                out.joinpath(store_name).write_text(json.dumps({
                    "updated_at": now.isoformat(), "entries": [{"company": "Example", "title": "Engineer"}],
                }))
            source_dir = root / "output" / "sources"
            source_dir.mkdir(parents=True)
            source_dir.joinpath("health.json").write_text(json.dumps({"sources": {
                name: {"healthy": True, "last_success_at": now.isoformat()}
                for name in ("linkedin", "indeed", "glassdoor")
            }}))
            for name in ("linkedin", "indeed", "glassdoor"):
                source_dir.joinpath(f"{name}.json").write_text(json.dumps({"jobs": [{}]}))

            workflow = {
                "PIPELINE_WORKFLOW_NAME": "Official careers",
                "PIPELINE_WORKFLOW_CONCLUSION": "failure",
            }
            with patch.dict("os.environ", workflow, clear=False):
                report, _history = pipeline_health.build(root, now)
            self.assertEqual("Warning", report["components"]["official"]["status"])
            self.assertTrue(report["components"]["official"]["data_usable"])
            self.assertIn("last-good data remains usable", report["components"]["official"]["detail"])

            official_store = root / "output" / "official_careers" / "jobs.json"
            official_store.write_text(json.dumps({"updated_at": now.isoformat(), "entries": []}))
            with patch.dict("os.environ", workflow, clear=False):
                report, _history = pipeline_health.build(root, now)
            self.assertEqual("Problem", report["components"]["official"]["status"])
            self.assertFalse(report["components"]["official"]["data_usable"])
            self.assertIn("last-good data remains unusable", report["components"]["official"]["detail"])


if __name__ == "__main__":
    unittest.main()
