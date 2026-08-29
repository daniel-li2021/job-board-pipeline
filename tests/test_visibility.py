from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import board_pipeline
import coverage_reconcile
import daily_pipeline
import dashboard
import review_state
from sources.company_aliases import load_alias_file, match_company_alias, prepare_alias_entries
from sources.schema import make_job
from sources.schema import classify_location_bucket

ROOT = Path(__file__).resolve().parents[1]


def official_job(job_id: str, title: str, location: str) -> dict:
    return make_job(
        source="official_careers",
        company="Example Tech",
        title=title,
        location=location,
        job_id=job_id,
        official_url=f"https://careers.example.com/jobs/{job_id}",
        source_url=f"https://careers.example.com/jobs/{job_id}",
        posted_date="2026-08-28",
        date_confidence="high",
    )


def context(status: str = "unvalidated", snapshot: datetime | None = None) -> dict:
    registry = prepare_alias_entries([
        {"id": "example", "name": "Example Tech", "aliases": ["example tech"], "adapter": "test"}
    ])[0]
    jobs = [
        official_job("10001", "Software Engineer I", "Seattle, WA"),
        official_job("10002", "Software Engineer I", "Austin, TX"),
        official_job("10003", "Machine Learning Engineer", "Seattle, WA"),
    ]
    return {
        "snapshot_at": snapshot or datetime(2026, 8, 28, 12, tzinfo=timezone.utc),
        "registry_entries": [registry],
        "registry_by_id": {"example": registry},
        "by_company": {"example": jobs},
        "config": {"example": {"status": status}},
    }


class ReferralAliasTests(unittest.TestCase):
    def test_single_alias_file_is_consistent_across_pipelines(self) -> None:
        targets = load_alias_file(ROOT / "source" / "target_companies.json")
        samples = {
            "Amazon Web Services, Inc.": "Amazon",
            "JPMorganChase": "J.P. Morgan",
            "The Walt Disney Company": "Disney",
            "SAP America": "SAP",
        }
        for company, expected in samples.items():
            self.assertEqual(expected, match_company_alias(company, targets))
            self.assertEqual(expected, board_pipeline.match_target_company(company, targets))
            self.assertEqual(expected, daily_pipeline.match_target_company(company, targets))

    def test_short_alias_does_not_match_substring(self) -> None:
        targets = load_alias_file(ROOT / "source" / "target_companies.json")
        self.assertIsNone(match_company_alias("Sapios", targets))
        self.assertIsNone(match_company_alias("Metadata Systems", targets))
        self.assertIsNone(match_company_alias("GE HealthCare", targets))


class DashboardPolicyTests(unittest.TestCase):
    def test_fresh_and_rolling_follow_first_seen_not_posted_date(self) -> None:
        now = datetime(2026, 8, 29, 12, tzinfo=timezone.utc)
        recent_discovery = dashboard.recency(
            {
                "posted_date": "2026-08-01",
                "date_confidence": "high",
                "first_seen": (now - timedelta(hours=2)).isoformat(),
            },
            now,
        )
        self.assertTrue(recent_discovery["fresh_activity"])
        self.assertTrue(recent_discovery["rolling_activity"])
        self.assertEqual("gt7d", recent_discovery["posted"]["bucket"])

        old_discovery = dashboard.recency(
            {
                "posted_date": now.isoformat(),
                "date_confidence": "high",
                "first_seen": (now - timedelta(days=4)).isoformat(),
            },
            now,
        )
        self.assertFalse(old_discovery["fresh_activity"])
        self.assertFalse(old_discovery["rolling_activity"])

    def test_sort_is_tier_then_score_then_discovery(self) -> None:
        now = datetime(2026, 8, 29, 12, tzinfo=timezone.utc)

        def row(tier: str, score: int, age: int, company: str) -> dict:
            return {
                "tier": tier,
                "score": score,
                "company": company,
                "freshness": dashboard.recency(
                    {"first_seen": (now - timedelta(hours=age)).isoformat()}, now
                ),
            }

        ordered = dashboard._sort_rows([
            row("B", 99, 1, "B Co"),
            row("A", 85, 5, "A lower"),
            row("A", 92, 20, "A higher"),
        ])
        self.assertEqual(["A higher", "A lower", "B Co"], [item["company"] for item in ordered])

    def test_official_registry_has_search_link_only_targets(self) -> None:
        catalog = {entry["id"]: entry for entry in dashboard.official_search_catalog()}
        for company_id in ("disney", "ebay", "qualcomm", "amd", "zoom", "goldman-sachs", "pure-storage"):
            self.assertEqual("search_link_only", catalog[company_id]["automation"])
            self.assertTrue(catalog[company_id]["search_links"])

    def test_known_foreign_city_only_locations_are_not_visible(self) -> None:
        for location in ("Bucharest", "Noida", "Bratislava, Slovakia", "Basel"):
            self.assertEqual("non_us", classify_location_bucket(location))
            self.assertFalse(dashboard.visible_candidate({
                "location": location,
                "filter_status": "kept",
                "suppress_alert": False,
                "tier": "B",
            }))

    def test_status_command_resolves_url_and_persists_completed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            store = root / "jobs.json"
            state = root / "review_state.json"
            job = official_job("10001", "Software Engineer I", "Seattle, WA")
            store.write_text(json.dumps({"entries": [job]}), encoding="utf-8")
            state.write_text(json.dumps({"jobs": {}}), encoding="utf-8")
            with patch.object(review_state, "STORE_PATHS", (store,)), patch.object(review_state, "STATE_PATH", state):
                key = review_state.set_status(job["official_url"], "completed", "applied")
            saved = json.loads(state.read_text(encoding="utf-8"))
            self.assertEqual("completed", saved["jobs"][key]["status"])
            self.assertEqual("applied", saved["jobs"][key]["notes"])


class CoverageMatchingTests(unittest.TestCase):
    def test_exact_match_order_and_location_safety(self) -> None:
        ctx = context()
        jobs = ctx["by_company"]["example"]
        method, matched = coverage_reconcile.exact_match(
            {"company": "Example Tech", "title": "Software Engineer I", "location": "Austin, TX", "job_id": "10002"},
            jobs,
        )
        self.assertEqual("job_id", method)
        self.assertEqual("10002", matched["job_id"])

        method, matched = coverage_reconcile.exact_match(
            {"company": "Example Tech", "title": "Software Engineer I", "location": "Boston, MA"},
            jobs,
        )
        self.assertEqual("", method)
        self.assertIsNone(matched)

    def test_validated_exact_suppresses_but_unvalidated_does_not(self) -> None:
        external = make_job(
            source="linkedin",
            company="Example Tech",
            title="Machine Learning Engineer",
            location="Seattle, WA",
            job_id="10003",
            source_url="https://www.linkedin.com/jobs/view/10003",
        )
        coverage_reconcile.annotate_jobs([external], "board", context("validated"))
        self.assertEqual("official_duplicate", external["coverage_status"])
        self.assertTrue(external["suppress_alert"])
        self.assertEqual("official", external["canonical_source"])

        other = dict(external)
        coverage_reconcile.annotate_jobs([other], "board", context("unvalidated"))
        self.assertEqual("covered_unvalidated", other["coverage_status"])
        self.assertFalse(other["suppress_alert"])

    def test_gap_and_newer_snapshot_guard(self) -> None:
        snapshot = datetime(2026, 8, 28, 12, tzinfo=timezone.utc)
        missing = make_job(
            source="syncareer",
            company="Example Tech",
            title="Backend Engineer",
            location="Denver, CO",
            job_id="99999",
            source_url="https://syncareer.com/job/99999",
        )
        missing["first_seen"] = (snapshot - timedelta(minutes=1)).isoformat()
        coverage_reconcile.annotate_jobs([missing], "syncareer", context("validated", snapshot))
        self.assertEqual("official_gap", missing["coverage_status"])
        self.assertFalse(missing["suppress_alert"])

        newer = dict(missing)
        newer["first_seen"] = (snapshot + timedelta(minutes=1)).isoformat()
        coverage_reconcile.annotate_jobs([newer], "syncareer", context("validated", snapshot))
        self.assertEqual("pending_official_refresh", newer["coverage_status"])

    def test_fixture_company_remains_unvalidated_with_dynamic_miss(self) -> None:
        ctx = context("unvalidated")
        external = [
            {"company": "Example Tech", "title": "Software Engineer I", "location": "Seattle, WA", "job_id": "10001"},
            {"company": "Example Tech", "title": "Software Engineer I", "location": "Austin, TX", "job_id": "10002"},
            {"company": "Example Tech", "title": "Backend Engineer", "location": "Denver, CO", "job_id": "99999"},
        ]
        for job in external:
            job["first_seen"] = "2026-08-28T11:00:00+00:00"
        coverage_reconcile.annotate_jobs(external, "board", ctx)
        self.assertEqual(["covered_unvalidated", "covered_unvalidated", "official_gap"], [j["coverage_status"] for j in external])
        self.assertEqual("unvalidated", ctx["config"]["example"]["status"])

    def test_hard_filtered_senior_role_is_out_of_scope_but_relevant_low_score_is_in(self) -> None:
        senior = {
            "job_id": "1", "company": "Example Tech", "title": "Principal Product Manager",
            "location": "Seattle, WA", "description": "10+ years", "requirements": "",
        }
        relevant = {
            "job_id": "2", "company": "Example Tech", "title": "Software Engineer I",
            "location": "Seattle, WA", "description": "Build backend services", "requirements": "",
        }
        self.assertFalse(coverage_reconcile.syncareer_job_in_scope(senior))
        self.assertTrue(coverage_reconcile.syncareer_job_in_scope(relevant))


class ReportingWorkflowTests(unittest.TestCase):
    def test_generated_issue_body_has_no_owner_cc(self) -> None:
        body = daily_pipeline.build_issue_body([], "2026-08-28_1200", False).lower()
        self.assertNotIn("cc @daniel-li2021", body)
        self.assertNotIn("cc @daniel-li2021", (ROOT / "board_pipeline.py").read_text(encoding="utf-8").lower())
        self.assertNotIn("cc @daniel-li2021", (ROOT / "official_careers.py").read_text(encoding="utf-8").lower())

    def test_workflows_are_independent_staggered_and_pages_enabled(self) -> None:
        board = (ROOT / ".github/workflows/board-jobs.yml").read_text(encoding="utf-8")
        official = (ROOT / ".github/workflows/official-careers.yml").read_text(encoding="utf-8")
        syncareer = (ROOT / ".github/workflows/daily-jobs.yml").read_text(encoding="utf-8")
        pages = (ROOT / ".github/workflows/reconcile-pages.yml").read_text(encoding="utf-8")
        self.assertIn('cron: "10 3 * * *"', board)
        self.assertIn('cron: "0 3 * * *"', official)
        self.assertIn('cron: "20 3 * * *"', syncareer)
        self.assertIn('cron: "30 3 * * *"', pages)
        self.assertIn("workflow_dispatch:", board)
        self.assertIn("workflow_dispatch:", official)
        self.assertIn("workflow_dispatch:", syncareer)
        self.assertIn("actions/deploy-pages@v4", pages)
        self.assertIn("concurrency:", pages)
        self.assertIn('"profile/review_state.json"', pages)
        self.assertFalse((ROOT / ".github/workflows/scheduled-jobs.yml").exists())


if __name__ == "__main__":
    unittest.main()
