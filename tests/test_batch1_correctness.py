"""Offline regressions for evidence/recall Batch 1; no crawls or model calls."""
import copy
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

import board_pipeline as board
import local_sources
import remote_recovery
from sources.careers import avature, jd_recovery
from sources.careers.incremental import DetailCache
from sources.official_jd_recovery import Resolver
from sources.schema import copy_jd_evidence

FIXTURES = Path(__file__).parent / "fixtures" / "jd_recovery"
NOW = datetime.now(timezone.utc)


def candidate(**extra):
    return {"company": "Example", "title": "Software Engineer", "location": "Austin, TX",
            "source": "linkedin", "job_id": "li-1", "description": "", **extra}


def tentative(**extra):
    return candidate(description="Unverified requirements. " * 20, jd_tentative=True,
                     tentative_official_url="https://example.com/jobs/12345",
                     enrichment_method="tentative_official", enrichment_status="tentative",
                     jd_recovery_at=NOW.isoformat(), first_seen=NOW.isoformat(), **extra)


class ExperienceContextTests(unittest.TestCase):
    def test_saved_early_title_descriptions_survive_prefilter(self):
        records = json.loads((FIXTURES / "early_career_saved.json").read_text())
        self.assertEqual(4, len(records))
        for record in records:
            with self.subTest(job_id=record["job_id"]):
                self.assertEqual((True, "keep"), board.role_seniority_prefilter(record))

    def test_company_history_and_preferred_experience_survive(self):
        for text in ("CoStar has over 35 years of experience in commercial real estate.",
                     "For 30 years NVIDIA has built innovative computing platforms.",
                     "Preferred qualifications: 8+ years building APIs.",
                     "Ideally you have 8 years of software experience.",
                     "Our clients have 20 years of experience.",
                     "For at least 35 years CoStar has served real estate customers.",
                     "CoStar has at least 35 years of commercial real estate experience.",
                     "8 years building APIs."):
            with self.subTest(text=text):
                self.assertTrue(board.role_seniority_prefilter(candidate(description=text))[0])

    def test_explicit_requirements_still_reject_even_for_early_title(self):
        for title in ("Software Engineer", "Software Engineer I", "Software Engineer New Grad"):
            for text in ("Requires 6+ years building APIs.", "Minimum 8 years of professional experience.",
                         "You have 7 years of software development experience.",
                         "Minimum qualifications:\n8+ years of software development experience.",
                         "Must have 8 years of software development and preferably 2 years of Go.",
                         "Requires 8+ years of software engineering experience and 2 years of Python.",
                         "Minimum 8 years of development experience, including 2 years building APIs.",
                         "At least 8 years of software development experience."):
                with self.subTest(title=title, text=text):
                    self.assertEqual((False, "prefilter:high_yoe"), board.role_seniority_prefilter(
                        candidate(title=title, description=text)))

    def test_lower_experience_alternative_and_senior_guard(self):
        self.assertTrue(board.role_seniority_prefilter(candidate(
            description="Requires 6 years with a bachelor's degree or 4 years with a master's."))[0])
        self.assertEqual("prefilter:senior", board.role_seniority_prefilter(candidate(title="Senior Software Engineer"))[1])


class ProvenanceTests(unittest.TestCase):
    def test_handoff_two_runs_keep_tentative_evidence(self):
        for legacy in (False, True):
            row = tentative()
            if legacy:
                row.pop("jd_tentative")
            with self.subTest(legacy=legacy), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "handoff.json.gz"
                remote_recovery.write_snapshot(path, "board", [row])
                first = remote_recovery.read_snapshot(path)[0]
                self.assertTrue(first["jd_tentative"])
                self.assertEqual("tentative", first["recovery_status"])
                self.assertEqual(row["tentative_official_url"], first["tentative_official_url"])
                remote_recovery.write_snapshot(path, "board", [candidate()])
                second = remote_recovery.read_snapshot(path)[0]
                self.assertEqual(first["description"], second["description"])
                self.assertEqual(first["first_seen"], second["first_seen"])
                self.assertTrue(second["jd_tentative"])
                self.assertEqual("tentative", second["enrichment_status"])
                self.assertEqual(first["jd_recovery_at"], second["jd_recovery_at"])
                remote_recovery.write_snapshot(path, "board", [candidate(description="Native verified JD. " * 20)])
                verified = remote_recovery.read_snapshot(path)[0]
                self.assertFalse(verified.get("jd_tentative"))
                self.assertEqual("jd_available", verified["recovery_status"])

    def test_confidence_copy_removes_stale_verification(self):
        target = candidate(official_search_verified=True, direct_original_fetched=True,
                           official_jd_fetched_at=NOW.isoformat())
        copy_jd_evidence(target, tentative())
        self.assertTrue(target["jd_tentative"])
        self.assertFalse(target.get("official_search_verified"))
        self.assertFalse(target.get("direct_original_fetched"))

    def test_tentative_peers_are_never_verified(self):
        for legacy in (False, True):
            peer = tentative(source="official", job_id="12345", official_url="https://example.com/jobs/12345", remote_recovery=True)
            if legacy:
                peer.pop("jd_tentative")
            with self.subTest(legacy=legacy):
                row = candidate()
                resolver = Resolver(search_limit=0, page_limit=0)
                result = resolver.recover(row, previous={}, context={}, store={"peer": peer}, now=NOW, cheap_only=True)
                self.assertEqual("pending", result)
                self.assertFalse(row.get("description"))
                self.assertFalse(row.get("official_search_verified"))
                self.assertEqual(0, board.enrich_from_exact_peers([row], [("remote", {"peer": peer})]))

    def test_same_source_tentative_cache_never_becomes_verified(self):
        previous = tentative(official_jd_fetched_at=NOW.isoformat(), official_search_verified=True)
        row = candidate()
        result = Resolver(search_limit=0, page_limit=0).recover(
            row, previous=previous, context={}, store={}, now=NOW, cheap_only=True)
        self.assertEqual("tentative_cache", result)
        self.assertTrue(row["jd_tentative"])
        self.assertFalse(row.get("official_search_verified"))
        again = Resolver().recover(row, previous={}, context={}, store={}, now=NOW, cheap_only=True)
        self.assertEqual("tentative_cache", again)

    def test_local_rehydration_retains_provenance_and_dates(self):
        prior = tentative(remote_recovery=True)
        handoff = candidate(first_seen=prior["first_seen"], remote_recovery=True)
        def snapshot(name):
            return {"jobs": [copy.deepcopy(prior)] if name == "remote_recovery" else [], "meta": {}}
        with tempfile.TemporaryDirectory() as tmp, patch.object(local_sources, "OUTPUT_DIR", Path(tmp)), \
             patch.object(local_sources, "HEALTH_PATH", Path(tmp) / "health.json"), \
             patch.object(local_sources, "read_source_snapshot_payload", side_effect=snapshot), \
             patch.object(local_sources, "_remote_handoff_rows", return_value=[handoff]), \
             patch.object(local_sources.coverage_reconcile, "load_official_context", return_value={}), \
             patch.object(local_sources.board, "load_store", return_value={}), \
             patch.object(local_sources.official_jd_recovery.Resolver, "recover", return_value="tentative_cache"):
            local_sources.recover_jds()
        self.assertEqual(prior["description"], handoff["description"])
        self.assertTrue(handoff["jd_tentative"])
        self.assertEqual("tentative", handoff["enrichment_status"])
        self.assertEqual(prior["first_seen"], handoff["first_seen"])


class EmployerParserTests(unittest.TestCase):
    def test_meta_real_page_includes_requirements_and_safe_alias(self):
        html = (FIXTURES / "meta_detail.html").read_text()
        description, title, _, identifier = jd_recovery.extract_detail(html, "Meta")
        posting = jd_recovery._posting(html)
        from sources.careers.http import html_to_text
        self.assertIn(html_to_text(posting["qualifications"]), description)
        self.assertIn(html_to_text(posting["responsibilities"]), description)
        self.assertGreater(len(description), 3500)
        job = candidate(company="Meta", job_id="1404071541713403", title=title,
                        official_url="https://www.metacareers.com/jobs/1404071541713403")
        url = "https://www.metacareers.com/profile/job_details/1404071541713403/"
        self.assertTrue(jd_recovery._same_job(job, url, title, identifier))
        for bad in (url.replace("3403/", "34030/"), url.replace("www.metacareers.com", "other.example")):
            self.assertFalse(jd_recovery._same_job(job, bad, title, identifier))
        self.assertFalse(jd_recovery._same_job(job, url, "Different Engineer", identifier))
        self.assertFalse(jd_recovery._same_job({**job, "official_url": "https://example.com/jobs/1404071541713403"},
                                             "https://example.com/profile/job_details/1404071541713403", title, identifier))

    def test_meta_recovery_second_run_uses_complete_cache(self):
        html = (FIXTURES / "meta_detail.html").read_text()
        title = jd_recovery._posting(html)["title"]
        job = candidate(company="Meta", job_id="1404071541713403", title=title, fetched_at=NOW.isoformat(),
                        official_url="https://www.metacareers.com/jobs/1404071541713403")
        url = "https://www.metacareers.com/profile/job_details/1404071541713403"
        with patch.object(jd_recovery, "make_session", return_value=Mock()), \
             patch.object(jd_recovery, "http_get", return_value=SimpleNamespace(text=html, url=url)) as fetch:
            stats = jd_recovery.recover([{"company": "Meta", "jobs": [job]}], [], lambda _: "clear")
            repeat = {**job, "description": "", "posted_date": ""}
            stats2 = jd_recovery.recover([{"company": "Meta", "jobs": [repeat]}], [job], lambda _: "clear")
        self.assertEqual(1, stats["detail_success"])
        self.assertEqual(1, fetch.call_count)
        self.assertEqual(job["description"], repeat["description"])
        self.assertEqual(1, stats2["cache_reused"])

    def test_twosigma_real_articles_select_complete_jd(self):
        html = (FIXTURES / "twosigma_detail.html").read_text()
        text = avature.extract_description(html)
        self.assertGreater(len(text), 3900)
        self.assertIn("generative", text)
        self.assertEqual(text, jd_recovery.extract_detail(html, "Two Sigma")[0])

    def test_avature_retries_thin_cache_and_preserves_good_cache_on_failure(self):
        url = "https://careers.example/careers/JobDetail/Software-Engineer/13079"
        listing = f'<article><a href="{url}">Software Engineer</a><span class="location">Austin, TX</span></article>'
        cached = candidate(company="Two Sigma", job_id="13079", title="Software Engineer", official_url=url,
                           fetched_at=NOW.isoformat(), detail_fetched_at=NOW.isoformat(), description="Metadata only")
        good = (FIXTURES / "twosigma_detail.html").read_text()
        def scrape(cache, detail):
            responses = [SimpleNamespace(text=listing), SimpleNamespace(text=detail)]
            with patch.object(avature, "http_get", side_effect=responses) as fetch, patch.object(avature.time, "sleep"):
                result = avature.scrape_avature(Mock(), company="Two Sigma", queries=["software"], max_pages=1,
                                                detail_cache=DetailCache([cache]), base_url="https://careers.example")
            return result, fetch.call_count
        result, calls = scrape(cached, good)
        recovered = result["jobs"][0]
        self.assertEqual(2, calls)
        self.assertGreater(len(recovered["description"]), 3900)
        self.assertEqual(1, result["detail_fetches"])
        # A second run reuses the complete result without a detail request.
        result2, calls = scrape(recovered, "unused")
        self.assertEqual(1, calls)
        self.assertEqual(recovered["description"], result2["jobs"][0]["description"])
        result3, _ = scrape({**recovered, "detail_fetched_at": "2000-01-01T00:00:00+00:00"}, "<article>Metadata</article>")
        self.assertEqual(recovered["description"], result3["jobs"][0]["description"])
        self.assertEqual(0, result3["detail_fetches"])
        self.assertEqual("2000-01-01T00:00:00+00:00", result3["jobs"][0]["detail_fetched_at"])
        self.assertIn("thin_detail", result3["errors"][0])


class DirectIdentityTests(unittest.TestCase):
    def run_recovery(self, postings, *, url="https://example.com/jobs/12345", status=200):
        row = candidate(application_url="https://example.com/jobs/12345")
        html = '<script type="application/ld+json">' + json.dumps(postings) + '</script>'
        session = Mock()
        session.get.return_value = SimpleNamespace(status_code=status, url=url, text=html)
        with patch.object(board, "_scrapling_fetch", return_value=("", url, "unavailable")):
            stats = board.resolve_exposed_originals([row], session, {})
        return row, stats

    def posting(self, **extra):
        return {"@type": "JobPosting", "title": "Software Engineer", "hiringOrganization": {"name": "Example"},
                "identifier": "12345", "description": "Verified requirements. " * 20, **extra}

    def test_unrelated_redirect_cannot_replace_fields(self):
        row, stats = self.run_recovery(self.posting(title="Chief Sales Officer", hiringOrganization={"name": "Other"}),
                                       url="https://example.com/careers")
        self.assertEqual("Software Engineer", row["title"])
        self.assertEqual("Austin, TX", row["location"])
        self.assertFalse(row.get("description"))
        self.assertFalse(row.get("original_resolved"))
        self.assertEqual("identity_mismatch", row["enrichment_failure_reason"])
        self.assertEqual(0, stats.get("jds_resolved", 0))

    def test_title_slug_and_minor_title_drift_with_stable_id(self):
        row = candidate(application_url="https://example.com/jobs/software-engineer-12345")
        response = "https://example.com/jobs/software-engineer-backend-12345"
        html = '<script type="application/ld+json">' + json.dumps(self.posting(title="Software Engineer, Backend")) + '</script>'
        session = Mock()
        session.get.return_value = SimpleNamespace(status_code=200, url=response, text=html)
        stats = board.resolve_exposed_originals([row], session, {})
        self.assertEqual(1, stats["jds_resolved"])
        self.assertEqual("Software Engineer, Backend", row["title"])

    def test_legacy_tentative_current_row_cannot_take_verified_fast_path(self):
        row = tentative(application_url="https://example.com/jobs/12345", official_search_verified=True,
                        official_jd_fetched_at=NOW.isoformat())
        row.pop("jd_tentative")
        session = Mock()
        session.get.return_value = SimpleNamespace(status_code=500, url=row["application_url"], text="")
        stats = board.resolve_exposed_originals([row], session, {})
        self.assertFalse(row.get("original_resolved"))
        self.assertFalse(row.get("direct_original_fetched"))
        self.assertEqual(0, stats.get("cache_reused", 0))

    def test_different_requisition_with_same_metadata_rejected(self):
        row, _ = self.run_recovery(self.posting(identifier="99999"), url="https://example.com/jobs/99999")
        self.assertFalse(row.get("description"))
        self.assertFalse(row.get("official_url"))

    def test_collection_selects_unique_expected_posting(self):
        row, stats = self.run_recovery([self.posting(title="Sales", identifier="99999"), self.posting()])
        self.assertEqual(1, stats["jds_resolved"])
        self.assertTrue(row["original_resolved"])
        row, _ = self.run_recovery([self.posting(), self.posting(description="Different requirements. " * 20)])
        self.assertFalse(row.get("description"))

    def test_http_failure_does_not_verify_identity(self):
        row, _ = self.run_recovery(self.posting(), status=500)
        self.assertFalse(row.get("original_resolved"))
        self.assertFalse(row.get("official_url"))


if __name__ == "__main__":
    unittest.main()
