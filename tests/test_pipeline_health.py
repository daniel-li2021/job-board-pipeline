from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import pipeline_health


class PipelineHealthTests(unittest.TestCase):
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
                (run_dir.parent / store_name).write_text(json.dumps({"entries": [{
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

    def test_official_link_only_failures_are_limitations_and_linkedin_name_is_explicit(self) -> None:
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

            report, _history = pipeline_health.build(root, now)

            official = report["components"]["official"]
            self.assertEqual(1, official["failure_count"])
            self.assertIn("linkedin_company_official_adapter", official["detail"])
            self.assertNotIn("citadel", official["detail"])
            self.assertTrue(any("citadel" in item for item in report["limitations"]))

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
