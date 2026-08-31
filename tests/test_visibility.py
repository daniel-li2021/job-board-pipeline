from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit

import board_pipeline
import coverage_reconcile
import daily_pipeline
from sources.company_aliases import load_alias_file, match_company_alias, prepare_alias_entries
from sources.schema import make_job, normalize_location_key
from sources.careers.workday import _detail_location

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
        "scraped_company_ids": {"example"},
        "config": {"example": {"status": status}},
    }


class ReferralAliasTests(unittest.TestCase):
    def test_single_alias_file_is_consistent_across_pipelines(self) -> None:
        targets = load_alias_file(ROOT / "source" / "target_companies.json")
        samples = {
            "Amazon Web Services, Inc.": "Amazon",
            "JPMorganChase": "J.P. Morgan",
            "Dell Technologies Inc.": "Dell",
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

    def test_location_format_and_multi_location_match_is_safe(self) -> None:
        official = official_job("20001", "Software Engineering MTS", "Washington - Bellevue; California - San Francisco")
        method, matched = coverage_reconcile.exact_match(
            {"title": "Software Engineering MTS", "location": "Bellevue, WA"},
            [official],
        )
        self.assertEqual("title_location", method)
        self.assertEqual("20001", matched["job_id"])
        self.assertTrue(coverage_reconcile.locations_compatible(
            normalize_location_key("San Jose"), normalize_location_key("San Jose, CA")
        ))

    def test_ambiguous_same_title_location_does_not_attach_arbitrarily(self) -> None:
        jobs = [
            official_job("30001", "Software Development Engineer", "San Jose"),
            official_job("30002", "Software Development Engineer", "San Jose, CA"),
        ]
        method, matched = coverage_reconcile.exact_match(
            {"title": "Software Development Engineer", "location": "San Jose, CA"}, jobs
        )
        self.assertEqual("", method)
        self.assertIsNone(matched)

    def test_workday_detail_keeps_additional_locations(self) -> None:
        info = {
            "location": "Washington - Bellevue",
            "additionalLocations": ["California - San Francisco", "Washington - Bellevue"],
        }
        self.assertEqual(
            "Washington - Bellevue; California - San Francisco",
            _detail_location(info),
        )

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

    def test_configured_adapter_without_snapshot_rows_is_pending(self) -> None:
        ctx = context("unvalidated")
        ctx["by_company"] = {}
        ctx["scraped_company_ids"] = set()
        external = make_job(
            source="linkedin",
            company="Example Tech",
            title="Software Engineer I",
            location="Seattle, WA",
            job_id="10001",
            source_url="https://www.linkedin.com/jobs/view/10001",
        )
        external["first_seen"] = "2026-08-27T11:00:00+00:00"
        coverage_reconcile.annotate_jobs([external], "board", ctx)
        self.assertEqual("pending_official_refresh", external["coverage_status"])

        refreshed = dict(external)
        ctx["scraped_company_ids"] = {"example"}
        coverage_reconcile.annotate_jobs([refreshed], "board", ctx)
        self.assertEqual("official_gap", refreshed["coverage_status"])

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
        self.assertFalse((ROOT / ".github/workflows/scheduled-jobs.yml").exists())


class RegistryCoverageTests(unittest.TestCase):
    def test_official_registry_is_structurally_complete(self) -> None:
        payload = json.loads((ROOT / "source" / "official_careers.json").read_text(encoding="utf-8"))
        companies = payload["companies"]
        ids = [company["id"] for company in companies]
        names = [company["name"].casefold() for company in companies]
        urls = []
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(12, payload["max_pages_default"])
        for company in companies:
            links = company.get("search_links") or []
            self.assertTrue(links, company["id"])
            for link in links:
                parsed = urlsplit(link.get("url") or "")
                self.assertEqual("https", parsed.scheme, company["id"])
                self.assertTrue(parsed.netloc, company["id"])
                urls.append(link["url"])
            adapter = company.get("adapter")
            config_key = {
                "workday": "workday",
                "greenhouse": "greenhouse",
                "ashby": "ashby",
                "lever": "lever",
                "smartrecruiters": "smartrecruiters",
                "avature": "avature",
                "oracle_hcm": "oracle_hcm",
            }.get(adapter)
            if config_key:
                self.assertTrue(company.get(config_key), company["id"])
            if company.get("covered_by") == "ats":
                self.assertEqual("ats", adapter)
        self.assertEqual(len(urls), len(set(urls)))
        self.assertGreaterEqual(sum(company.get("adapter") != "skip" for company in companies), 70)

    def test_ats_and_syncareer_have_explicit_official_cross_check_coverage(self) -> None:
        official = json.loads((ROOT / "source" / "official_careers.json").read_text(encoding="utf-8"))
        ats = json.loads((ROOT / "source" / "ats_boards.json").read_text(encoding="utf-8"))
        syncareer = json.loads((ROOT / "source" / "company_links.json").read_text(encoding="utf-8"))
        official_ids = {company["id"] for company in official["companies"]}
        ats_ids = {board["token"] for board in ats["boards"]}
        sync_ids = {company["key"] for company in syncareer["companies"]}
        self.assertTrue(ats_ids.issubset(official_ids))
        self.assertGreaterEqual(len(official_ids & sync_ids), 38)
        self.assertGreaterEqual(len(official_ids & ats_ids & sync_ids), 7)
        self.assertEqual(len(sync_ids), len(syncareer["companies"]))

    def test_bounded_query_variants_are_kept_in_configuration(self) -> None:
        self.assertIn("Site Reliability", daily_pipeline.SEARCH_KEYWORDS)
        from sources.careers.amazon import DEFAULT_QUERIES as amazon_queries, QUERY_PAGE_CAPS as amazon_caps
        from sources.careers.google import DEFAULT_QUERIES as google_queries
        from sources.careers.workday import DEFAULT_QUERIES as workday_queries, QUERY_PAGE_CAPS as workday_caps

        self.assertIn("systems development engineer", amazon_queries)
        self.assertIn("site reliability engineer", amazon_queries)
        self.assertIn("applied scientist", amazon_queries)
        self.assertIn("platform engineer", workday_queries)
        self.assertIn('"Data Engineer"', {query["q"] for query in google_queries})
        self.assertIn('"Infrastructure Engineer"', {query["q"] for query in google_queries})
        self.assertIn('"DeepMind"', {query["q"] for query in google_queries})
        self.assertLessEqual(max(amazon_caps.values()), 3)
        self.assertLessEqual(max(workday_caps.values()), 3)

        registry = json.loads((ROOT / "source" / "official_careers.json").read_text(encoding="utf-8"))
        companies = {company["id"]: company for company in registry["companies"]}
        self.assertIn("core infrastructure", companies["oracle"]["oracle_hcm"]["extra_queries"])


if __name__ == "__main__":
    unittest.main()
