from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import pipeline_health


class PipelineHealthTests(unittest.TestCase):
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

    def test_failed_attempt_with_fresh_last_good_is_degradation_not_unusable(self) -> None:
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

            self.assertEqual("Warning", report["components"]["linkedin"]["status"])
            self.assertTrue(report["components"]["linkedin"]["data_usable"])
            self.assertIn("search/discovery", report["components"]["linkedin"]["detail"])
            self.assertFalse(any(item.startswith("LinkedIn:") for item in report["problems"]))
            self.assertTrue(any(item.startswith("LinkedIn:") for item in report["degradations"]))

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
            self.assertIn("Scrapling fallback resolved 5/8", linkedin["detail"])
            self.assertNotIn("search/discovery attempt", linkedin["detail"])

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
            self.assertEqual("Warning", official["status"])
            self.assertEqual(2, official["failure_count"])
            self.assertIn("meta: blocked with HTTP 429", official["detail"])
            self.assertIn("chunk_1: timeout", official["detail"])
            self.assertFalse(any("scrape/auth/LLM failures" in item for item in report["degradations"]))
            self.assertEqual("official", history[0]["pipeline"])

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
