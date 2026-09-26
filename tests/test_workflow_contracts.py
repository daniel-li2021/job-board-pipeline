"""Offline checks of the workflow's actual shell argument handling."""
import os
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WorkflowContractTests(unittest.TestCase):
    def test_board_dispatch_collects_indeed_before_matching_and_persists_snapshot(self):
        workflow = (ROOT / ".github/workflows/board-jobs.yml").read_text()
        self.assertLess(workflow.index("python3 remote_indeed.py"),
                        workflow.index("python3 board_pipeline.py"))
        self.assertIn("git add -- output/sources/indeed.json output/sources/health.json", workflow)
        self.assertIn("github.actor != 'github-actions[bot]'", workflow)

    def test_official_dispatch_input_is_a_literal_argument(self):
        workflow = (ROOT / ".github/workflows/official-careers.yml").read_text()
        step = workflow.split("      - name: Scrape official careers and match\n", 1)[1].split("\n      - name:", 1)[0]
        script = textwrap.dedent(step.split("        run: |\n", 1)[1])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            python = root / "python3"
            python.write_text('#!/bin/sh\nprintf \'%s\\n\' "$@"\n')
            python.chmod(0o755)
            value = "$(touch must-not-exist); google"
            env = {**os.environ, "PATH": f"{root}:/usr/bin:/bin", "ONLY": value, "NO_LLM": "true"}
            result = subprocess.run(["bash", "-eu", "-c", script], cwd=root, env=env, text=True, capture_output=True, check=True)
            self.assertEqual(["official_careers.py", "run", "--only", value, "--no-llm"], result.stdout.splitlines())
            self.assertFalse((root / "must-not-exist").exists())

    def test_output_commit_steps_guard_github_blob_size(self):
        for name in ("board-jobs.yml", "official-careers.yml", "daily-jobs.yml"):
            workflow = (ROOT / ".github/workflows" / name).read_text()
            self.assertIn("python3 scripts/guard_github_blob_size.py", workflow)

    def test_blob_size_guard_rejects_oversized_staged_file(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "guard_github_blob_size", ROOT / "scripts" / "guard_github_blob_size.py"
        )
        guard = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(guard)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            small = root / "small.json"
            huge = root / "jobs.json"
            small.write_text("{}", encoding="utf-8")
            huge.write_bytes(b"x" * (guard.LIMIT))
            self.assertEqual([], guard.oversized([small]))
            self.assertEqual([f"{huge} ({huge.stat().st_size} bytes)"], guard.oversized([huge]))


if __name__ == "__main__":
    unittest.main()
