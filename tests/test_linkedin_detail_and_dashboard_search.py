from __future__ import annotations

import unittest
from datetime import datetime, timezone
from unittest.mock import Mock, patch

import dashboard
from sources import linkedin_local
from sources.schema import make_job


class LinkedInDetailTests(unittest.TestCase):
    def test_dashboard_shows_one_row_for_an_exact_cross_pipeline_job(self) -> None:
        rows = [
            {"canonical_job_key": "url::https://jobs.example.com/42", "pipeline": "syncareer"},
            {"canonical_job_key": "url::https://jobs.example.com/42", "pipeline": "board"},
            {"canonical_job_key": "url::https://jobs.example.com/43", "pipeline": "board"},
        ]
        result = dashboard.dedup_canonical_rows(rows)
        self.assertEqual(2, len(result))
        self.assertEqual("board", result[0]["pipeline"])

    def test_parse_detail_extracts_jd_and_only_apply_labelled_external_url(self) -> None:
        html = """
        <a href="https://www.linkedin.com/company/example">Example company</a>
        <div class="show-more-less-html__markup">
          <p>Build reliable Python APIs and distributed systems.</p>
        </div>
        <a class="apply-button" href="https://jobs.example.com/42">Apply</a>
        """
        detail = linkedin_local._parse_detail(html)
        self.assertIn("Build reliable Python APIs", detail["description"])
        self.assertEqual("https://jobs.example.com/42", detail["application_url"])

    def test_parse_detail_does_not_treat_company_link_as_application_url(self) -> None:
        detail = linkedin_local._parse_detail(
            '<div class="description__text">Full JD</div>'
            '<a href="https://example.com/about">Visit company</a>'
        )
        self.assertEqual("Full JD", detail["description"])
        self.assertEqual("", detail["application_url"])

    @patch("sources.linkedin_local.time.sleep")
    def test_enrich_details_reuses_cache_and_fetches_only_uncached(self, _sleep: Mock) -> None:
        cached = make_job(
            source="linkedin", company="Example", title="Software Engineer",
            location="Austin, TX", job_id="1",
        )
        cached["description"] = "Cached full JD"
        cached["linkedin_detail_fetched_at"] = datetime.now(timezone.utc).isoformat()

        first = make_job(
            source="linkedin", company="Example", title="Software Engineer",
            location="Austin, TX", job_id="1",
        )
        second = make_job(
            source="linkedin", company="Example AI", title="AI Engineer",
            location="Remote, US", job_id="2",
        )
        response = Mock(
            status_code=200,
            text='<div class="description__text">Full AI JD</div>',
        )
        session = Mock()
        session.get.return_value = response

        stats = linkedin_local.enrich_details(
            [first, second], previous_jobs=[cached], session=session,
        )

        self.assertEqual(1, stats["cache_reused"])
        self.assertEqual(1, stats["requests"])
        self.assertEqual(2, stats["jds_resolved"])
        self.assertEqual("Cached full JD", first["description"])
        self.assertEqual("Full AI JD", second["description"])
        session.get.assert_called_once_with(
            linkedin_local.GUEST_DETAIL_URL.format(job_id="2"),
            timeout=linkedin_local.REQUEST_TIMEOUT,
        )

    @patch("sources.linkedin_local.time.sleep")
    def test_enrichment_block_preserves_existing_cards(self, _sleep: Mock) -> None:
        row = make_job(
            source="linkedin", company="Example", title="Backend Engineer",
            location="New York, NY", job_id="3",
        )
        response = Mock(status_code=429, text="rate limited")
        session = Mock()
        session.get.return_value = response

        with patch.object(linkedin_local, "_scrapling_fetch_html", return_value=None):
            stats = linkedin_local.enrich_details([row], session=session)

        self.assertIn("HTTP 429", stats["blocked"])
        self.assertEqual("Backend Engineer", row["title"])
        self.assertFalse(row.get("description"))

    @patch("sources.linkedin_local.time.sleep")
    def test_scrapling_recovers_detail_after_requests_is_blocked(self, _sleep: Mock) -> None:
        row = make_job(
            source="linkedin", company="Example", title="Junior Software Engineer",
            location="New York, NY", job_id="4",
        )
        session = Mock()
        session.get.return_value = Mock(status_code=429, text="rate limited")
        html = '<div class="description__text">Build production Python services.</div>'

        with patch.object(linkedin_local, "_scrapling_fetch_html", return_value=html):
            stats = linkedin_local.enrich_details([row], session=session)

        self.assertEqual("Build production Python services.", row["description"])
        self.assertEqual(1, stats["scrapling_requests"])
        self.assertEqual(1, stats["scrapling_jds_resolved"])


class DashboardSearchTests(unittest.TestCase):
    def test_dashboard_template_contains_title_company_search(self) -> None:
        self.assertIn("jobSearch", dashboard.HTML_TEMPLATE)
        self.assertIn("matchesSearch", dashboard.HTML_TEMPLATE)
        self.assertIn("Search title or company", dashboard.HTML_TEMPLATE)
        self.assertIn("healthIndicator", dashboard.HTML_TEMPLATE)
        self.assertIn("D.health?.components", dashboard.HTML_TEMPLATE)

    def test_search_is_applied_without_replacing_main_view_state(self) -> None:
        self.assertIn("activeMainView", dashboard.HTML_TEMPLATE)
        self.assertIn("searchedRows(normalRows", dashboard.HTML_TEMPLATE)
        self.assertNotIn("activeMainView='fresh';searchQuery", dashboard.HTML_TEMPLATE)

    def test_multi_location_display_keeps_each_job_state_and_url(self) -> None:
        self.assertIn("function displayRows(rows)", dashboard.HTML_TEMPLATE)
        self.assertIn("Collapsed same role · individual location links preserved", dashboard.HTML_TEMPLATE)
        self.assertIn('data-keys="${keyData}"', dashboard.HTML_TEMPLATE)
        self.assertIn("saveStates(keys", dashboard.HTML_TEMPLATE)


if __name__ == "__main__":
    unittest.main()
