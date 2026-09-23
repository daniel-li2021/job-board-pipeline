from __future__ import annotations

import unittest
from datetime import datetime, timedelta, timezone
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
    def test_http_429_stops_before_scrapling(self, _sleep: Mock) -> None:
        row = make_job(
            source="linkedin", company="Example", title="Junior Software Engineer",
            location="New York, NY", job_id="4",
        )
        session = Mock()
        session.get.return_value = Mock(status_code=429, text="rate limited")
        with patch.object(linkedin_local, "_scrapling_fetch_html") as scrapling:
            stats = linkedin_local.enrich_details([row], session=session)

        scrapling.assert_not_called()
        self.assertTrue(stats["rate_limited"])
        self.assertEqual(1, stats["requests"])
        self.assertFalse(row.get("description"))

    @patch("sources.linkedin_local.time.sleep")
    def test_detail_budget_is_combined_and_bounded(self, _sleep: Mock) -> None:
        rows = [make_job(
            source="linkedin", company="Example", title=f"Engineer {index}",
            location="Austin, TX", job_id=str(index),
        ) for index in range(10)]
        session = Mock()
        session.get.return_value = Mock(status_code=200, text='<div class="description__text">JD</div>')

        stats = linkedin_local.enrich_details(rows, session=session, request_limit=8)

        self.assertEqual(8, stats["requests"])
        self.assertEqual(2, stats["budget_deferred"])
        self.assertTrue(stats["budget_exhausted"])

    def test_recent_detail_attempt_is_deferred_for_24_hours(self) -> None:
        prior = make_job(source="linkedin", company="Example", title="Engineer", location="Austin, TX", job_id="5")
        prior["linkedin_detail_attempted_at"] = datetime.now(timezone.utc).isoformat()
        prior["enrichment_failure_reason"] = "linkedin_http_500"
        row = make_job(source="linkedin", company="Example", title="Engineer", location="Austin, TX", job_id="5")
        session = Mock()

        stats = linkedin_local.enrich_details([row], previous_jobs=[prior], session=session)

        session.get.assert_not_called()
        self.assertEqual(1, stats["retry_deferred"])
        self.assertEqual(prior["linkedin_detail_attempted_at"], row["linkedin_detail_attempted_at"])

    @patch("sources.linkedin_local.time.sleep")
    def test_later_retry_uses_one_scrapling_attempt(self, _sleep: Mock) -> None:
        prior = make_job(source="linkedin", company="Example", title="Engineer", location="Austin, TX", job_id="6")
        prior["linkedin_detail_attempted_at"] = (datetime.now(timezone.utc) - timedelta(hours=25)).isoformat()
        prior["enrichment_failure_reason"] = "linkedin_http_500"
        row = make_job(source="linkedin", company="Example", title="Engineer", location="Austin, TX", job_id="6")
        session = Mock()
        html = '<div class="description__text">Recovered JD</div>'

        with patch.object(linkedin_local, "_scrapling_fetch_html", return_value=(html, 200, "")):
            stats = linkedin_local.enrich_details([row], previous_jobs=[prior], session=session)

        session.get.assert_not_called()
        self.assertEqual(1, stats["requests"])
        self.assertEqual(1, stats["retry_attempts"])
        self.assertEqual("Recovered JD", row["description"])

    def test_scrapling_429_stops_the_remaining_batch(self) -> None:
        prior_rows = []
        rows = []
        for job_id in ("9", "10"):
            prior = make_job(source="linkedin", company="Example", title="Engineer", location="Austin, TX", job_id=job_id)
            prior["linkedin_detail_attempted_at"] = (datetime.now(timezone.utc) - timedelta(hours=25)).isoformat()
            prior["enrichment_failure_reason"] = "linkedin_http_500"
            prior_rows.append(prior)
            rows.append(make_job(source="linkedin", company="Example", title="Engineer", location="Austin, TX", job_id=job_id))

        with patch.object(linkedin_local, "_scrapling_fetch_html", return_value=("", 429, "scrapling_http_429")) as scrapling:
            stats = linkedin_local.enrich_details(rows, previous_jobs=prior_rows)

        scrapling.assert_called_once()
        self.assertEqual(1, stats["requests"])
        self.assertTrue(stats["rate_limited"])

    def test_exact_official_match_defers_linkedin_until_board_fallback(self) -> None:
        deferred = make_job(source="linkedin", company="Example", title="Engineer", location="Austin, TX", job_id="7")
        deferred["_linkedin_official_url"] = "https://jobs.example.com/7"
        deferred["_linkedin_official_defer"] = True
        fallback = make_job(source="linkedin", company="Example", title="Engineer", location="Austin, TX", job_id="8")
        fallback["_linkedin_official_url"] = "https://jobs.example.com/8"
        fallback["_linkedin_official_defer"] = False
        session = Mock()
        session.get.return_value = Mock(status_code=200, text='<div class="description__text">Fallback JD</div>')

        with patch.object(linkedin_local.time, "sleep"):
            stats = linkedin_local.enrich_details([deferred, fallback], session=session)

        self.assertEqual("official_detail_deferred", deferred["enrichment_failure_reason"])
        self.assertEqual("Fallback JD", fallback["description"])
        self.assertEqual(2, stats["exact_official"])
        self.assertEqual(1, stats["official_deferred"])


class DashboardSearchTests(unittest.TestCase):
    def test_dashboard_template_contains_title_company_search(self) -> None:
        self.assertIn("jobSearch", dashboard.HTML_TEMPLATE)
        self.assertIn("matchesSearch", dashboard.HTML_TEMPLATE)
        self.assertIn("Search title or company", dashboard.HTML_TEMPLATE)
        self.assertIn("healthIndicator", dashboard.HTML_TEMPLATE)
        self.assertIn("D.health?.components", dashboard.HTML_TEMPLATE)

    def test_dashboard_cards_keep_usable_health_and_recent_run_yields(self) -> None:
        self.assertIn("h.last_good_count", dashboard.HTML_TEMPLATE)
        self.assertIn("h.last_good_at", dashboard.HTML_TEMPLATE)
        self.assertIn("h.keywords", dashboard.HTML_TEMPLATE)
        self.assertIn("health details", dashboard.HTML_TEMPLATE)
        self.assertIn("run.mode==='pipeline'", dashboard.HTML_TEMPLATE)
        self.assertIn("k==='board'?4:2", dashboard.HTML_TEMPLATE)
        self.assertIn("runMetric(run,'new_jobs')", dashboard.HTML_TEMPLATE)
        self.assertIn("runMetric(run,'new_jobs_added')", dashboard.HTML_TEMPLATE)
        self.assertIn("Recent runs", dashboard.HTML_TEMPLATE)
        self.assertIn("America/Los_Angeles", dashboard.HTML_TEMPLATE)

    def test_search_is_applied_without_replacing_main_view_state(self) -> None:
        self.assertIn("activeMainView", dashboard.HTML_TEMPLATE)
        self.assertIn("discoveryRows(normalRows", dashboard.HTML_TEMPLATE)
        self.assertIn("const discoveryRows=rows=>searchedRows(rows).filter(matchesDiscoveryFilters)", dashboard.HTML_TEMPLATE)
        self.assertNotIn("activeMainView='fresh';searchQuery", dashboard.HTML_TEMPLATE)

    def test_discovery_filters_are_presentation_only_for_fresh_and_rolling(self) -> None:
        self.assertIn("class=\"min-score-filter\"", dashboard.HTML_TEMPLATE)
        self.assertIn('type="checkbox" value="${value}"', dashboard.HTML_TEMPLATE)
        self.assertIn("const sponsorshipChoices=['Sponsor','Likely','Unknown','Unlikely','No sponsor']", dashboard.HTML_TEMPLATE)
        self.assertIn("jobs(shown,false,true)", dashboard.HTML_TEMPLATE)
        job_search = dashboard.HTML_TEMPLATE.split('<div class="job-search">', 1)[1].split("</div>", 1)[0]
        self.assertNotIn("min-score-filter", job_search)
        self.assertNotIn("sponsorship-filter", job_search)
        self.assertIn('<th class="tier-header">Tier<div class="header-filter">', dashboard.HTML_TEMPLATE)
        self.assertIn('<th class="sponsorship-header">Sponsorship', dashboard.HTML_TEMPLATE)
        self.assertIn("function bindDiscoveryFilters(box,draw)", dashboard.HTML_TEMPLATE)
        self.assertIn("function renderDiscoveryViews()", dashboard.HTML_TEMPLATE)
        self.assertIn("score.oninput=()=>{minScore=score.value.trim();draw()", dashboard.HTML_TEMPLATE)
        self.assertIn("body.innerHTML=jobRows(shown)", dashboard.HTML_TEMPLATE)
        self.assertNotIn("const start=event.target.selectionStart;renderAll()", dashboard.HTML_TEMPLATE)
        self.assertIn("fresh:discoveryRows(normalRows(D.fresh_24h)).length", dashboard.HTML_TEMPLATE)
        self.assertIn("rolling:discoveryRows(normalRows(D.rolling_3d)).length", dashboard.HTML_TEMPLATE)
        self.assertIn("renderBox('inProgress',searchedRows(rows.filter(r=>statusOf(r)==='in_progress'&&!isDeleted(r))))", dashboard.HTML_TEMPLATE)
        self.assertIn("renderBox('applied',searchedRows(rows.filter(r=>statusOf(r)==='applied_complete'&&!isDeleted(r))))", dashboard.HTML_TEMPLATE)
        self.assertIn("box.innerHTML=jobs(rows.filter(isDeleted),true)", dashboard.HTML_TEMPLATE)
        self.assertIn("exportViewRows[elId]=displayRows(shown)", dashboard.HTML_TEMPLATE)

    def test_multi_location_display_keeps_each_job_state_and_url(self) -> None:
        self.assertIn("function displayRows(rows)", dashboard.HTML_TEMPLATE)
        self.assertIn("Collapsed same role · individual location links preserved", dashboard.HTML_TEMPLATE)
        self.assertIn('data-keys="${keyData}"', dashboard.HTML_TEMPLATE)
        self.assertIn("saveStates(keys", dashboard.HTML_TEMPLATE)

    def test_dashboard_checks_for_newer_deployments_only_on_return(self) -> None:
        self.assertIn("method:'HEAD',cache:'no-store'", dashboard.HTML_TEMPLATE)
        self.assertIn("remote>loaded", dashboard.HTML_TEMPLATE)
        self.assertIn("location.replace(checkUrl.href)", dashboard.HTML_TEMPLATE)
        self.assertIn("window.addEventListener('focus',checkForDashboardUpdate)", dashboard.HTML_TEMPLATE)
        self.assertIn("document.visibilityState==='visible'", dashboard.HTML_TEMPLATE)


if __name__ == "__main__":
    unittest.main()
