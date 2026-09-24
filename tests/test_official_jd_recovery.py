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
    def test_generic_exact_match_reuses_fetched_jd_and_board_promotes_without_fetch(self):
        url = "https://jobs.ashbyhq.com/abridge/123"
        results = (f'<a class="result__a" href="https://www.abridge.com/">Abridge</a>'
                   f'<a class="result__a" href="{url}">Software Engineer</a>')
        session = Mock()
        session.get.side_effect = [response(recovery.SEARCH_URL, results), response(url, posting())]
        resolver = recovery.Resolver(session=session, search_limit=5, page_limit=4)
        job = row()
        method = resolver.recover(job, previous={}, context={}, store={}, now=datetime.now(timezone.utc))
        self.assertEqual("generic_1", method)
        self.assertEqual(url, job["application_url"])
        self.assertTrue(job["official_search_verified"])
        self.assertGreaterEqual(len(job["description"]), board.THIN_JD_CHARS)
        self.assertNotIn("official_url", job)
        self.assertEqual(1, resolver.search_requests)
        self.assertEqual(1, resolver.page_requests)
        job["coverage_status"] = "not_dedicated"
        board_session = Mock()
        stats = board.resolve_exposed_originals([job], board_session, {})
        board_session.get.assert_not_called()
        self.assertEqual(url, job["official_url"])
        self.assertEqual(1, stats["cache_reused"])

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
        session.get.side_effect = [requests.ConnectionError("timeout"),
                                   response(recovery.BING_SEARCH_URL, results), response(url, posting())]
        resolver = recovery.Resolver(session=session, search_limit=5, page_limit=4)
        with patch.object(recovery.time, "sleep"):
            self.assertEqual("generic_2", resolver.recover(row(), previous={}, context={}, store={}, now=datetime.now(timezone.utc)))
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
