from __future__ import annotations

import json
import logging
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import local_sources
import board_pipeline
from sources import jobspy_local, schema

ROOT = Path(__file__).resolve().parents[1]


class Frame:
    def __init__(self, records: list[dict]) -> None:
        self.records = records

    def to_dict(self, *, orient: str) -> list[dict]:
        assert orient == "records"
        return self.records


class LocalSourceTests(unittest.TestCase):
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
        self.assertEqual(100, calls[0]["results_wanted"])

    def test_empty_primary_jobspy_query_is_unverified_not_a_good_snapshot(self) -> None:
        def blocked(**_kwargs):
            logging.getLogger("JobSpy:Glassdoor").error("HTTP 403")
            return Frame([])

        result = jobspy_local.scrape(
            "glassdoor", keywords=["software engineer"],
            scrape_jobs_func=blocked,
        )
        self.assertEqual("empty_unverified", result["status"])
        self.assertEqual("HTTP 403", result["reason"])
        self.assertEqual("empty_unverified", result["query_stats"][0]["stop_reason"])

    def test_codegraph_generated_data_is_ignored(self) -> None:
        self.assertIn(".codegraph/", (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines())

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
            }], new)
            health = json.loads((Path(tmpdir) / "health.json").read_text(encoding="utf-8"))["sources"]["glassdoor"]
            self.assertFalse(health["healthy"])
            self.assertEqual("HTTP 403", health["reason"])
            self.assertEqual("2026-09-01T00:00:00+00:00", health["last_success_at"])
            self.assertEqual("old", health["last_success_collector"]["commit"])
            self.assertEqual(1, health["last_good_count"])

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
            subprocess.run(["git", "-C", str(repo), "add", "local_sources.py"], check=True)
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
            self.assertIn(f"current collector {current}", run.stdout)
            self.assertIn(f"collector commit: {current}", run.stdout)


if __name__ == "__main__":
    unittest.main()
