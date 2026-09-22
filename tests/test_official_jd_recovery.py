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
        results = f'<a class="result__a" href="{url}">Software Engineer</a>'
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
            report = local_sources.recover_jds()
            saved = json.loads((Path(temp) / "sources" / "linkedin.json").read_text())
        self.assertEqual(["linkedin", "indeed"], seen)
        self.assertEqual(1, report["before_total"])
        self.assertEqual(0, report["after_total"])
        self.assertEqual(original["first_seen"], saved["jobs"][0]["first_seen"])
        self.assertEqual(original["last_seen"], saved["jobs"][0]["last_seen"])
        self.assertEqual(original["source_verified_at"], saved["jobs"][0]["source_verified_at"])
        self.assertEqual(snapshot["meta"]["scraped_at"], saved["meta"]["scraped_at"])

    def test_search_budget_rotation_low_yield_and_cooldown_state(self):
        card = (
            '<div class="base-card" data-entity-urn="urn:li:jobPosting:111">'
            '<h3>Software Engineer</h3><h4>Abridge</h4>'
            '<span class="job-search-card__location">Austin, TX</span>'
            '<a class="base-card__full-link" href="https://linkedin.com/jobs/view/111"></a></div>'
        )
        session = Mock()
        session.get.return_value = response(linkedin_local.GUEST_SEARCH_URL, card)
        with patch.object(linkedin_local.time, "sleep"):
            result = linkedin_local.scrape(session=session, query_cursor=1, page_limit=1)
        self.assertEqual(1, result["requests"])
        self.assertEqual("ai engineer", result["query_stats"][0]["query"])
        self.assertEqual("low_unique_yield", result["query_stats"][0]["stop_reason"])
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
            self.assertEqual(2, state["search_query_cursor"])
            self.assertTrue(local_sources._linkedin_search_control(now + timedelta(minutes=2))[1])
            self.assertEqual(1, local_sources._linkedin_search_control(now + timedelta(hours=25))[0])
            local_sources.write_health([{"source": "linkedin", "status": "skipped_unavailable",
                "attempted_at": (now + timedelta(hours=25)).isoformat(),
                "search_collection": {"requests": 1, "responses": 1, "rate_limited": False},
                "detail_enrichment": {"requests": 0}}], {})
            self.assertEqual(0, json.loads(local_sources.HEALTH_PATH.read_text())["sources"]["linkedin"]["search_429_streak"])


if __name__ == "__main__":
    unittest.main()
