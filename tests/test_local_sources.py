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
        self.assertEqual("empty_unverified", result["status"])
        self.assertEqual("HTTP 403", result["reason"])
        self.assertEqual("empty_unverified", result["query_stats"][0]["stop_reason"])

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
            self.assertFalse(health["required"])
            self.assertFalse(health["healthy"])
            self.assertEqual("HTTP 403", health["reason"])
            self.assertEqual("2026-09-01T00:00:00+00:00", health["last_success_at"])
            self.assertEqual("old", health["last_success_collector"]["commit"])
            self.assertEqual(1, health["last_good_count"])

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
