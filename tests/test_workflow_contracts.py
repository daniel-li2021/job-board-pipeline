"""Offline checks of the workflow's actual shell argument handling."""
import os
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WorkflowContractTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
