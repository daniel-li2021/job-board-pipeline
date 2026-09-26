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
            self.assertEqual(good_at, item["last_good_at"])
            self.assertEqual(now.isoformat(), item["latest_attempt_at"])
            public = root / "public"
            pipeline_health.write(public, report, history)
            page = (public / "health.html").read_text()
            self.assertIn(good_at, page)
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
            self.assertEqual(3, report["enrichment"]["unresolved_thin_or_no_jd"])
            self.assertEqual("https://example.test/job", report["unresolved_examples"][0]["url"])
            self.assertEqual(3, len(history))

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
            self.assertEqual("Healthy", linkedin["status"])
            self.assertIn("detail enrichment blocked: blocked with HTTP 429", linkedin["detail"])
            self.assertIn("Scrapling fallback recovered 5/8", linkedin["detail"])
            self.assertIn("rate-limited", linkedin["keywords"])
            self.assertNotIn("search/discovery attempt", linkedin["detail"])

    def test_linkedin_detail_429_with_high_scrapling_recovery_is_not_warning(self) -> None:
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

            self.assertEqual("Healthy", report["components"]["linkedin"]["status"])
            self.assertFalse(report["degradations"])
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
                    self.assertEqual(1, official["consecutive_failures"])
                    self.assertEqual("degraded" if count >= 5 else "limited", official["latest_attempt_status"])
                    self.assertIn(f"{count} scraper failures", official["keywords"])
                    self.assertIn(f"{count} scraper failures", official["detail"])
                    for index in range(count):
                        self.assertIn(f"source-{index} (", official["detail"])
                    self.assertIn("rate-limited", official["keywords"])
                    self.assertEqual(expected, report["overall"])

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
                    self.assertEqual("Healthy", report["overall"])
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
