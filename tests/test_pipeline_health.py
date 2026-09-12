from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

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
                name: {"healthy": True, "required": name != "glassdoor", "last_success_at": now.isoformat()}
                for name in ("linkedin", "indeed", "glassdoor")
            }}))
            source_dir.joinpath("linkedin.json").write_text(json.dumps({"meta": {"detail_enrichment": {"needed": 3}}}))

            report, history = pipeline_health.build(root, now)

            self.assertEqual("Healthy", report["overall"])
            self.assertEqual(3, report["enrichment"]["unresolved_thin_or_no_jd"])
            self.assertEqual("https://example.test/job", report["unresolved_examples"][0]["url"])
            self.assertEqual(3, len(history))


if __name__ == "__main__":
    unittest.main()
