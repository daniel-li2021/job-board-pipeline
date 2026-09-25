from __future__ import annotations

import json
import tempfile
import unittest
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock, patch

import board_pipeline as board
import local_sources
from sources import linkedin_local, official_jd_recovery as recovery


def row() -> dict:
    return {
        "source": "linkedin", "job_id": "li-1", "company": "Abridge",
        "title": "Software Engineer", "location": "Austin, TX", "description": "",
        "first_seen": "2026-09-01T00:00:00+00:00",
        "last_seen": "2026-09-20T00:00:00+00:00",
        "source_verified_at": "2026-09-20T00:00:00+00:00",
        "verified_this_run": False,
    }


def posting(*, company: str = "Abridge", title: str = "Software Engineer", city: str = "Austin") -> str:
    data = {
        "@context": "https://schema.org", "@type": "JobPosting",
        "hiringOrganization": {"name": company}, "title": title,
        "jobLocation": {"address": {"addressLocality": city, "addressRegion": "TX", "addressCountry": "US"}},
        "description": "Build reliable engineering systems. " * 12,
    }
    return '<script type="application/ld+json">' + json.dumps(data) + "</script>"


def response(url: str, text: str, status: int = 200) -> Mock:
    return Mock(url=url, text=text, status_code=status)


class OfficialRecoveryTests(unittest.TestCase):
    def test_mac_search_cooldown_does_not_modify_github_control_state(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(local_sources, "HEALTH_PATH", Path(temp) / "health.json"), \
             patch.object(local_sources, "read_source_snapshot_payload", return_value={"jobs": [], "meta": {}}), \
             patch.dict("os.environ", {"LOCAL_SOURCE_PROFILE": "mac"}):
            now = datetime.now(timezone.utc)
            local_sources.HEALTH_PATH.write_text(json.dumps({"sources": {"linkedin": {
                "search_429_streak": 2,
                "search_cooldown_until": (now + timedelta(hours=24)).isoformat(),
            }}}))
            self.assertEqual(14, local_sources._linkedin_search_control(now)[0])
            local_sources.write_health([{"source": "linkedin", "status": "partial",
                "attempted_at": now.isoformat(), "search_collection": {"requests": 1, "responses": 1, "rate_limited": True},
                "detail_enrichment": {"requests": 0}}], {})
            state = json.loads(local_sources.HEALTH_PATH.read_text())["sources"]["linkedin"]
            self.assertEqual(2, state["search_429_streak"])
            self.assertEqual(1, state["runner_states"]["mac"]["search_429_streak"])

    def test_linkedin_mac_and_github_query_profiles_have_independent_global_caps(self):
        def fake_get(_url, *, params, timeout):
            return response(_url, f"{params['keywords']}:{params['start']}")

        def fake_cards(text):
            return [{"job_id": f"{text}:{index}", "company": "Abridge",
                     "title": "Software Engineer", "location": "Austin, TX",
                     "source_url": "https://linkedin.com/jobs/view/1"}
                    for index in range(2)]

        for profile, limit, names in (
            ("github", 8, ["software engineer", "ai engineer"]),
            ("mac", 14, ["software engineer", "ai engineer", "backend engineer",
                         "full-stack engineer", "machine learning engineer"]),
        ):
            with self.subTest(profile=profile):
                session = Mock()
                session.get.side_effect = fake_get
                with patch.object(linkedin_local, "_parse_cards", side_effect=fake_cards), \
                     patch.object(linkedin_local.time, "sleep"):
                    result = linkedin_local.scrape(session=session, profile=profile, page_limit=limit)
                self.assertEqual(limit, result["requests"])
                self.assertEqual(names, [item["query"] for item in result["query_stats"]])
                self.assertEqual([5, 3] if profile == "github" else [5, 3, 2, 2, 2],
                                 [item["pages_fetched"] for item in result["query_stats"]])

    def test_generic_exact_match_reuses_fetched_jd_and_board_promotes_without_fetch(self):
        url = "https://jobs.ashbyhq.com/abridge/123"
        results = (f'<a class="result__a" href="https://www.abridge.com/">Abridge</a>'
                   f'<a class="result__a" href="{url}">Software Engineer</a>')
        session = Mock()
        api_response = response("https://api.ashbyhq.com/posting-api/job-board/abridge", "")
        api_response.json.return_value = {"jobs": []}
        session.get.side_effect = [response(recovery.SEARCH_URL, results), api_response, response(url, posting())]
        resolver = recovery.Resolver(session=session, search_limit=5, page_limit=4)
        job = row()
        method = resolver.recover(job, previous={}, context={}, store={}, now=datetime.now(timezone.utc))
        self.assertEqual("generic_1", method)
        self.assertEqual(url, job["application_url"])
        self.assertTrue(job["official_search_verified"])
        self.assertGreaterEqual(len(job["description"]), board.THIN_JD_CHARS)
        self.assertNotIn("official_url", job)
        self.assertEqual(1, resolver.search_requests)
        self.assertEqual(2, resolver.page_requests)
        job["coverage_status"] = "not_dedicated"
        board_session = Mock()
        stats = board.resolve_exposed_originals([job], board_session, {})
        board_session.get.assert_not_called()
        self.assertEqual(url, job["official_url"])
        self.assertEqual(1, stats["cache_reused"])

    def test_generic_ats_link_uses_verified_api_jd_without_html_refetch(self):
        url = "https://jobs.ashbyhq.com/abridge/123"
        results = f'<a class="result__a" href="{url}">Software Engineer</a>'
        ats_response = response("https://api.ashbyhq.com/posting-api/job-board/abridge", "")
        ats_response.json.return_value = {"jobs": [{"id": "123", "title": "Software Engineer",
            "location": "Austin", "jobUrl": url,
            "descriptionHtml": "<p>Build reliable engineering systems.</p>" * 12}]}
        session = Mock()
        session.get.side_effect = [response(recovery.SEARCH_URL, results), ats_response]
        resolver = recovery.Resolver(session=session)
        job = row()
        self.assertEqual("generic_1", resolver.recover(
            job, previous={}, context={}, store={}, now=datetime.now(timezone.utc)))
        self.assertEqual(2, session.get.call_count)
        self.assertEqual(url, job["application_url"])
        self.assertFalse(job.get("jd_tentative"))

    def test_company_careers_finds_exact_ats_board_jd_without_detail_refetch(self):
        board_url = "https://jobs.ashbyhq.com/Abridge"
        job_url = board_url + "/123"
        careers_results = (f'<a class="result__a" href="https://www.abridge.com/">Abridge</a>'
                           f'<a class="result__a" href="{board_url}">Abridge careers</a>')
        board_response = response("https://api.ashbyhq.com/posting-api/job-board/Abridge", "")
        board_response.json.return_value = {"jobs": [{
            "id": "123", "title": "Software Engineer", "location": "Austin, TX",
            "jobUrl": job_url, "descriptionHtml": "<p>Build reliable engineering systems.</p>" * 12,
        }]}
        session = Mock()
        session.get.side_effect = [response(recovery.SEARCH_URL, ""), response(recovery.SEARCH_URL, ""),
                                   response(recovery.SEARCH_URL, careers_results), board_response]
        resolver = recovery.Resolver(session=session, search_limit=5, page_limit=4)
        job = row()
        with patch.object(recovery.time, "sleep"):
            self.assertEqual("direct_ats_board", resolver.recover(
                job, previous={}, context={}, store={}, now=datetime.now(timezone.utc)))
        self.assertEqual(3, resolver.search_requests)
        self.assertEqual(1, resolver.page_requests)
        self.assertEqual(job_url, job["application_url"])
        self.assertNotIn("official_url", job)
        self.assertGreaterEqual(len(job["description"]), board.THIN_JD_CHARS)
        self.assertIsNone(recovery._ats_board("https://jobs.ashbyhq.com/Other", "Abridge", []))
        second = row()
        second["job_id"] = "li-2"
        self.assertEqual("ats_board_cache", resolver.recover(
            second, previous={}, context={}, store={}, now=datetime.now(timezone.utc)))
        self.assertEqual(3, resolver.search_requests)
        self.assertEqual(1, resolver.page_requests)

    def test_verified_ats_pattern_is_tried_before_web_search(self):
        url = "https://jobs.ashbyhq.com/Abridge/123"
        ats_response = response("https://api.ashbyhq.com/posting-api/job-board/Abridge", "")
        ats_response.json.return_value = {"jobs": [{
            "id": "123", "title": "Software Engineer", "location": "Austin, TX",
            "jobUrl": url, "descriptionHtml": "<p>Build reliable engineering systems.</p>" * 12,
        }]}
        session = Mock()
        session.get.return_value = ats_response
        resolver = recovery.Resolver(session=session, search_limit=5, page_limit=4)
        known = {"old": {"company": "Abridge", "official_url": "https://jobs.ashbyhq.com/Abridge/old"}}
        self.assertEqual("known_ats_board", resolver.recover(
            row(), previous={}, context={}, store=known, now=datetime.now(timezone.utc)))
        self.assertEqual(0, resolver.search_requests)
        self.assertEqual(1, resolver.page_requests)
        self.assertIn("posting-api/job-board/Abridge", session.get.call_args.args[0])

    def test_known_ashby_board_accepts_city_only_location_for_reconciliation(self):
        url = "https://jobs.ashbyhq.com/Abridge/123"
        ats_response = response("https://api.ashbyhq.com/posting-api/job-board/Abridge", "")
        ats_response.json.return_value = {"jobs": [{
            "id": "123", "title": "Software Engineer", "location": "Austin",
            "jobUrl": url, "descriptionHtml": "<p>Build reliable engineering systems.</p>" * 12,
        }]}
        resolver = recovery.Resolver(session=Mock(get=Mock(return_value=ats_response)))
        known = {"old": {"company": "Abridge", "official_url": "https://jobs.ashbyhq.com/Abridge/old"}}
        job = row()
        self.assertEqual("known_ats_board", resolver.recover(
            job, previous={}, context={}, store=known, now=datetime.now(timezone.utc)))
        self.assertEqual(url, job["application_url"])

    def test_greenhouse_city_only_location_is_usable_but_foreign_city_is_not(self):
        url = "https://job-boards.greenhouse.io/workstream/jobs/6204349004"
        api_response = response("https://boards-api.greenhouse.io/v1/boards/workstream/jobs", "")
        api_response.json.return_value = {"jobs": [
            {"id": 6204349004, "title": "Staff Full Stack Engineer ", "location": {"name": "Lehi"},
             "absolute_url": url, "content": "<p>Build reliable systems.</p>" * 15},
            {"id": 6204364004, "title": "Staff Full Stack Engineer ",
             "location": {"name": "Vancouver, British Columbia, Canada"},
             "absolute_url": "https://job-boards.greenhouse.io/workstream/jobs/6204364004",
             "content": "<p>Build reliable systems.</p>" * 15},
        ]}
        session = Mock(get=Mock(return_value=api_response))
        candidate = {**row(), "company": "Workstream", "title": "Staff Full Stack Engineer",
                     "location": "Lehi, UT"}
        resolver = recovery.Resolver(session=session)
        known = {"prior": {"company": "Workstream", "official_url": url}}
        self.assertEqual("known_ats_board", resolver.recover(
            candidate, previous={}, context={}, store=known, now=datetime.now(timezone.utc)))
        self.assertEqual(url, candidate["application_url"])
        self.assertEqual(1, len(resolver.ats_matches["workstream"]))

    def test_ats_board_rejects_wrong_location_and_ambiguous_requisitions(self):
        url = "https://jobs.ashbyhq.com/Abridge/123"
        base = {"title": "Software Engineer", "descriptionHtml": "Build reliable systems. " * 15}
        known = {"old": {"company": "Abridge", "official_url": "https://jobs.ashbyhq.com/Abridge/old"}}
        for jobs in ([{**base, "id": "123", "location": "Dallas, TX", "jobUrl": url}],
                     [{**base, "id": str(n), "location": "Austin, TX", "jobUrl": url + str(n)}
                      for n in (1, 2)]):
            with self.subTest(jobs=jobs):
                ats_response = response("https://api.ashbyhq.com/posting-api/job-board/Abridge", "")
                ats_response.json.return_value = {"jobs": jobs}
                session = Mock()
                session.get.side_effect = [ats_response] + [response(recovery.SEARCH_URL, "") for _ in range(4)]
                resolver = recovery.Resolver(session=session, search_limit=5, page_limit=4)
                candidate = row()
                with patch.object(recovery.time, "sleep"):
                    self.assertNotIn(resolver.recover(
                        candidate, previous={}, context={}, store=known, now=datetime.now(timezone.utc)),
                        {"known_ats_board", "direct_ats_board"})
                self.assertFalse(candidate.get("application_url"))

    def test_query_sequence_no_match_and_budget_exhaustion_is_deferred(self):
        session = Mock()
        session.get.return_value = response(recovery.SEARCH_URL, "")
        job = row()
        resolver = recovery.Resolver(session=session, search_limit=3, page_limit=4)
        with patch.object(recovery.time, "sleep"):
            self.assertEqual("no_match", resolver.recover(job, previous={}, context={}, store={}, now=datetime.now(timezone.utc)))
        self.assertEqual(3, resolver.search_requests)
        self.assertEqual("no_match", job["official_search_status"])
        queries = [call.kwargs["params"]["q"] for call in session.get.call_args_list]
        self.assertIn('"Software Engineer" "Abridge"', queries[0])
        self.assertIn('"Austin, TX"', queries[1])
        self.assertIn("careers jobs", queries[2])
        limited = recovery.Resolver(session=session, search_limit=1, page_limit=4)
        later = row()
        with patch.object(recovery.time, "sleep"):
            self.assertEqual("deferred", limited.recover(later, previous={}, context={}, store={}, now=datetime.now(timezone.utc)))
        self.assertNotEqual("no_match", later["official_search_status"])

    def test_search_provider_failure_moves_to_bounded_bing_fallback(self):
        import requests

        url = "https://jobs.ashbyhq.com/abridge/123"
        results = f'<li class="b_algo"><h2><a href="{url}">Software Engineer</a></h2></li>'
        session = Mock()
        api_response = response("https://api.ashbyhq.com/posting-api/job-board/abridge", "")
        api_response.json.return_value = {"jobs": []}
        session.get.side_effect = [requests.ConnectionError("timeout"),
                                   response(recovery.BING_SEARCH_URL, results), api_response, response(url, posting())]
        resolver = recovery.Resolver(session=session, search_limit=5, page_limit=4)
        with patch.object(recovery.time, "sleep"):
            self.assertEqual("generic_1", resolver.recover(row(), previous={}, context={}, store={}, now=datetime.now(timezone.utc)))
        self.assertEqual("bing", resolver.search_provider)
        self.assertEqual(2, resolver.search_requests)
        self.assertEqual(1, resolver.stats["search_provider_failures"])

    def test_wrong_identity_and_recent_no_match(self):
        source = row()
        self.assertEqual("", recovery._verified_posting(source, posting(company="Other")))
        self.assertEqual("", recovery._verified_posting(source, posting(title="Data Engineer")))
        self.assertEqual("", recovery._verified_posting(source, posting(city="Dallas")))
        self.assertEqual("", recovery._verified_posting(source, posting() + posting()))
        self.assertFalse(recovery._credible("https://linkedin.com/jobs/view/123", "Abridge", set()))
        self.assertFalse(recovery._credible("https://appcast.io/redirect/123", "Abridge", set()))
        now = datetime.now(timezone.utc)
        prior = {"official_search_status": "no_match", "official_search_attempted_at": now.isoformat()}
        session = Mock()
        resolver = recovery.Resolver(session=session)
        self.assertEqual("no_match_cached", resolver.recover(source, previous=prior, context={}, store={}, now=now))
        session.get.assert_not_called()

    def test_unique_wrong_city_is_tentative_without_official_identity(self):
        url = "https://jobs.ashbyhq.com/abridge/123"
        candidate = row()
        before = {field: candidate[field] for field in ("first_seen", "last_seen", "source_verified_at", "verified_this_run")}
        resolver = recovery.Resolver(session=Mock(), search_limit=5, page_limit=4)
        resolver.search = Mock(side_effect=[([url], "ok"), ([], "ok"), ([], "ok"), ([], "ok")])
        resolver.page = Mock(return_value=(posting(city="Dallas"), url, "ok"))
        resolver.ats_board = Mock(return_value=([], "unsupported"))
        self.assertEqual("tentative_official", resolver.recover(
            candidate, previous={}, context={}, store={}, now=datetime.now(timezone.utc)))
        self.assertTrue(candidate["jd_tentative"])
        self.assertEqual(url, candidate["tentative_official_url"])
        self.assertNotIn("application_url", candidate)
        self.assertNotIn("official_url", candidate)
        self.assertEqual(before, {field: candidate[field] for field in before})
        board_session = Mock()
        board.resolve_exposed_originals([candidate], board_session, {})
        board_session.get.assert_not_called()
        self.assertNotIn("official_url", candidate)

        fresh = row()
        self.assertEqual("tentative_cache", resolver.recover(
            fresh, previous=candidate, context={}, store={}, now=datetime.now(timezone.utc)))
        self.assertTrue(fresh["jd_tentative"])

    def test_unique_richer_indeed_peer_precedes_web_search(self):
        peer = {"source": "indeed", "job_id": "indeed-1", "company": "Abridge",
                "title": "Software Engineer", "location": "Austin, TX", "description": "Peer JD " * 40}
        job = row()
        session = Mock()
        resolver = recovery.Resolver(session=session)
        self.assertEqual("exact_indeed_peer", resolver.recover(
            job, previous={}, context={}, store={"peer": peer}, now=datetime.now(timezone.utc), cheap_only=True))
        self.assertEqual(peer["description"], job["description"])
        self.assertNotIn("application_url", job)
        session.get.assert_not_called()

    def test_linkedin_detail_can_replace_tentative_jd(self):
        job = {**row(), "description": "Tentative " * 30, "jd_tentative": True,
               "tentative_official_url": "https://jobs.ashbyhq.com/abridge/123"}
        prior = dict(job)
        session = Mock()
        session.get.return_value = response("https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/li-1", "")
        with patch.object(linkedin_local, "_parse_detail", return_value={"description": "Verified " * 35, "application_url": ""}), \
             patch.object(linkedin_local.time, "sleep"):
            stats = linkedin_local.enrich_details([job], previous_jobs=[prior], session=session,
                                                  request_limit=1, min_description_chars=board.THIN_JD_CHARS)
        self.assertEqual(1, stats["detail_jds_fetched"])
        self.assertFalse(job.get("jd_tentative"))
        self.assertNotIn("tentative_official_url", job)
        self.assertEqual(prior["first_seen"], job["first_seen"])
        self.assertEqual(prior["last_seen"], job["last_seen"])

    def test_dedicated_match_and_fresh_cache_need_no_web_request(self):
        now = datetime.now(timezone.utc)
        url = "https://careers.abridge.com/jobs/123"
        prior = {**row(), "description": "A" * 250, "application_url": url,
                 "official_search_verified": True, "official_jd_fetched_at": now.isoformat()}
        session = Mock()
        resolver = recovery.Resolver(session=session)
        self.assertEqual("cache", resolver.recover(row(), previous=prior, context={}, store={}, now=now))
        official = {"company": "Abridge", "title": "Software Engineer", "location": "Austin, TX",
                    "description": "B" * 250, "official_url": url}
        with patch.object(recovery.coverage_reconcile, "company_id_for", return_value="abridge"):
            job = row()
            self.assertEqual("dedicated_official", resolver.recover(
                job, previous={}, context={"registry_entries": [], "by_company": {"abridge": [official]}},
                store={}, now=now))
        self.assertEqual(url, job["application_url"])
        self.assertNotIn("official_url", job)
        session.get.assert_not_called()

    def test_direct_careers_and_unique_title_variant(self):
        host = "careers.abridge.com"
        old = {"key": "old", "company": "Abridge", "official_url": f"https://{host}/old"}
        homepage = f"https://{host}/"
        careers = f"https://{host}/careers"
        candidate = f"https://{host}/jobs/123"
        session = Mock()
        session.get.side_effect = [
            response(recovery.SEARCH_URL, "") for _ in range(3)
        ] + [response(homepage, '<a href="/careers">Careers</a>'),
             response(careers, '<a href="/jobs/123">Software Engineer</a>'),
             response(candidate, posting())]
        resolver = recovery.Resolver(session=session, search_limit=5, page_limit=4)
        with patch.object(recovery.time, "sleep"):
            self.assertEqual("direct_careers", resolver.recover(row(), previous={}, context={}, store={"old": old}, now=datetime.now(timezone.utc)))
        self.assertEqual(3, resolver.search_requests)
        self.assertEqual(3, resolver.page_requests)

        site_result = f'<a class="result__a" href="{candidate}">Software Engineer Remote</a>'
        session = Mock()
        session.get.side_effect = [response(recovery.SEARCH_URL, "") for _ in range(3)] + [
            response(homepage, ""), response(recovery.SEARCH_URL, site_result),
            response(candidate, posting(title="Software Engineer (Remote)")),
        ]
        resolver = recovery.Resolver(session=session, search_limit=5, page_limit=4)
        with patch.object(recovery.time, "sleep"):
            self.assertEqual("title_fallback", resolver.recover(row(), previous={}, context={}, store={"old": old}, now=datetime.now(timezone.utc)))
        self.assertEqual(4, resolver.search_requests)

    def test_recovery_preserves_temporal_fields_and_never_loads_glassdoor(self):
        original = row()
        snapshot = {"schema_version": 1, "jobs": [original], "meta": {"scraped_at": "2026-09-20T00:00:00+00:00"}}
        seen = []

        def read(name):
            seen.append(name)
            return json.loads(json.dumps(snapshot)) if name == "linkedin" else {"jobs": [], "meta": {}}

        class FakeResolver:
            def __init__(self, **_kwargs):
                self.stats = Counter()
                self.pattern_cache = {}
                self.search_requests = 0
                self.page_requests = 0
                self.search_provider = "duckduckgo"

            def recover(self, job, **_kwargs):
                job["description"] = "A" * 250
                return "dedicated_official"

        with tempfile.TemporaryDirectory() as temp, patch.object(local_sources, "OUTPUT_DIR", Path(temp)), patch.object(
            local_sources, "HEALTH_PATH", Path(temp) / "sources" / "health.json"
        ), patch.object(local_sources, "read_source_snapshot_payload", side_effect=read), patch.object(
            local_sources.coverage_reconcile, "load_official_context", return_value={}
        ), patch.object(local_sources.board, "load_store", return_value={}), patch.object(
            local_sources.official_jd_recovery, "Resolver", FakeResolver
        ):
            path = Path(temp) / "sources" / "linkedin.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"schema_version": 1, "source": "linkedin", "count": 1,
                                        "meta": snapshot["meta"], "jobs": [original]}))
            report = local_sources.recover_jds()
            saved = json.loads(path.read_text())
        self.assertEqual(["linkedin", "indeed"], seen)
        self.assertEqual(1, report["before_total"])
        self.assertEqual(0, report["after_total"])
        self.assertEqual(original["first_seen"], saved["jobs"][0]["first_seen"])
        self.assertEqual(original["last_seen"], saved["jobs"][0]["last_seen"])
        self.assertEqual(original["source_verified_at"], saved["jobs"][0]["source_verified_at"])
        self.assertEqual(snapshot["meta"]["scraped_at"], saved["meta"]["scraped_at"])
        self.assertEqual(["schema_version", "source", "count", "meta", "jobs"], list(saved))

    def test_focused_search_order_adaptive_pages_429_and_cooldown_state(self):
        def cards(index, count=2):
            return "".join(
                f'<div class="base-card" data-entity-urn="urn:li:jobPosting:{index * 10 + n}">'
                '<h3>Software Engineer</h3><h4>Abridge</h4>'
                '<span class="job-search-card__location">Austin, TX</span>'
                f'<a class="base-card__full-link" href="https://linkedin.com/jobs/view/{index * 10 + n}"></a></div>'
                for n in range(count)
            )
        session = Mock()
        session.get.side_effect = [response(linkedin_local.GUEST_SEARCH_URL, cards(i)) for i in range(8)]
        with patch.object(linkedin_local.time, "sleep"):
            result = linkedin_local.scrape(session=session, query_cursor=7)
        self.assertEqual(8, result["requests"])
        self.assertTrue(result["coverage_limited"])
        self.assertEqual(["software engineer", "ai engineer"], [stat["query"] for stat in result["query_stats"]])
        self.assertEqual([5, 3], [stat["pages_fetched"] for stat in result["query_stats"]])
        self.assertEqual(["software engineer"] * 5 + ["ai engineer"] * 3,
                         [call.kwargs["params"]["keywords"] for call in session.get.call_args_list])
        session = Mock()
        session.get.return_value = response(linkedin_local.GUEST_SEARCH_URL, cards(0))
        with patch.object(linkedin_local.time, "sleep"):
            probe = linkedin_local.scrape(session=session, query_cursor=99, page_limit=1)
        self.assertEqual(1, probe["requests"])
        self.assertEqual("software engineer", session.get.call_args.kwargs["params"]["keywords"])
        session = Mock()
        session.get.side_effect = [response(linkedin_local.GUEST_SEARCH_URL, cards(i, 1)) for i in range(3)]
        with patch.object(linkedin_local.time, "sleep"):
            low_yield = linkedin_local.scrape(session=session)
        self.assertEqual([2, 1], [stat["pages_fetched"] for stat in low_yield["query_stats"]])
        session = Mock()
        session.get.side_effect = [response(linkedin_local.GUEST_SEARCH_URL, cards(0)),
                                   response(linkedin_local.GUEST_SEARCH_URL, "", status=429)]
        with patch.object(linkedin_local.time, "sleep"):
            blocked = linkedin_local.scrape(session=session)
        self.assertEqual("blocked", blocked["status"])
        self.assertEqual(2, len(blocked["jobs"]))
        self.assertEqual(2, session.get.call_count)
        with tempfile.TemporaryDirectory() as temp, patch.object(local_sources, "HEALTH_PATH", Path(temp) / "health.json"), patch.object(
            local_sources, "read_source_snapshot_payload", return_value={"jobs": [], "meta": {}}
        ):
            now = datetime.now(timezone.utc)
            for index in range(2):
                local_sources.write_health([{
                    "source": "linkedin", "status": "skipped_unavailable", "attempted_at": (now + timedelta(minutes=index)).isoformat(),
                    "search_collection": {"requests": 1, "responses": 1, "rate_limited": True},
                    "detail_enrichment": {"requests": 0},
                }], {})
            state = json.loads(local_sources.HEALTH_PATH.read_text())["sources"]["linkedin"]
            self.assertEqual(2, state["search_429_streak"])
            self.assertEqual(0, state.get("detail_429_streak", 0))
            self.assertEqual(0, state.get("search_query_cursor", 0))
            self.assertTrue(local_sources._linkedin_search_control(now + timedelta(minutes=2))[1])
            self.assertEqual(1, local_sources._linkedin_search_control(now + timedelta(hours=25))[0])
            local_sources.write_health([{"source": "linkedin", "status": "skipped_unavailable",
                "attempted_at": (now + timedelta(hours=25)).isoformat(),
                "search_collection": {"requests": 1, "responses": 1, "rate_limited": False},
                "detail_enrichment": {"requests": 0}}], {})
            self.assertEqual(0, json.loads(local_sources.HEALTH_PATH.read_text())["sources"]["linkedin"]["search_429_streak"])


if __name__ == "__main__":
    unittest.main()
