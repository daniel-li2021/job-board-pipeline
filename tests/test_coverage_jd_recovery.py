"""Focused tests for coverage loss attribution and bounded Official detail recovery."""

from __future__ import annotations

import tempfile
import json
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import coverage_reconcile as coverage
import official_careers as official
from sources.careers import jd_recovery


NOW = datetime(2026, 9, 26, tzinfo=timezone.utc)


class CoverageLossTests(unittest.TestCase):
    def test_failed_or_page_limited_official_run_preserves_last_comparable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = Path(tmp) / "jobs.json"
            store.write_text(json.dumps({"coverage_company_runs": {
                "disney": {"last_success_at": "2026-09-24T00:00:00+00:00",
                           "last_comparable_at": "2026-09-24T00:00:00+00:00"}}}))
            with patch.object(official, "DEFAULT_STORE_PATH", store), patch.object(
                official, "load_companies", return_value={"companies": [{"id": "disney", "adapter": "disney"}]}
            ):
                runs = official._coverage_company_runs([{
                    "company_id": "disney", "status": "ok", "errors": [],
                    "query_diagnostics": [{"stop_reason": "page_budget", "raw_jobs": 30}],
                }], NOW.isoformat())
                self.assertEqual("limited", runs["disney"]["latest_status"])
                self.assertEqual("2026-09-24T00:00:00+00:00", runs["disney"]["last_comparable_at"])
                runs = official._coverage_company_runs([{
                    "company_id": "disney", "status": "blocked", "errors": ["HTTP 403"],
                }], NOW.isoformat())
                self.assertEqual("2026-09-24T00:00:00+00:00", runs["disney"]["last_success_at"])

    def test_loss_reason_requires_comparable_company_run(self) -> None:
        base = {"company": "Example", "official_company_id": "example", "coverage_status": "official_gap",
                "first_seen": "2026-09-25T00:00:00+00:00"}
        context = {"company_runs": {"example": {"last_success_at": "2026-09-26T00:00:00+00:00",
                                                 "last_comparable_at": "2026-09-26T00:00:00+00:00"}}}
        self.assertEqual("discovery_miss", coverage._loss_reason(base, context, NOW))
        self.assertEqual("identity_mismatch", coverage._loss_reason(
            {**base, "coverage_status": "official_identity_unmatched", "coverage_candidate_count": 1}, context, NOW))
        self.assertEqual("discovery_miss", coverage._loss_reason(
            {**base, "coverage_status": "official_identity_unmatched", "coverage_candidate_count": 0}, context, NOW))
        self.assertEqual("source_timing", coverage._loss_reason(
            {**base, "first_seen": "2026-09-26T01:00:00+00:00"}, context, NOW))
        self.assertEqual("unverified_snapshot", coverage._loss_reason(base, {"company_runs": {}}, NOW))
        self.assertEqual("unsupported_company", coverage._loss_reason(
            {**base, "coverage_status": "not_dedicated"}, context, NOW))
        self.assertEqual("unclassifiable", coverage._loss_reason({**base, "company": ""}, context, NOW))

    def test_ai_evidence_is_batched_cached_and_never_suppresses(self) -> None:
        official = {"company": "Example", "title": "Software Engineer", "location": "Seattle, WA",
                    "job_id": "12345", "official_url": "https://example.com/jobs/12345"}
        records = [{"company": "Example", "title": "Software Engineer", "location": "Seattle, WA",
                    "job_id": "external-1", "source": "linkedin", "official_company_id": "example",
                    "coverage_status": "official_ambiguous", "suppress_alert": False}]
        context = {"by_company": {"example": [official]}}
        with tempfile.TemporaryDirectory() as tmp, patch.object(
            coverage, "IDENTITY_AI_CACHE_PATH", Path(tmp) / "cache.json"
        ), patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}), patch.object(
            coverage.compact_ai, "decide", return_value={}
        ) as decide:
            # The response is keyed by a content digest generated inside the audit.
            def answer(**kwargs):
                case = list(kwargs["cases"])[0]
                return {case["case_id"]: {"decision": "likely_same", "confidence": 0.95}}
            decide.side_effect = answer
            first = coverage._identity_ai(records, context, use_ai=True)
            self.assertEqual(1, first["api_requests"])
            self.assertEqual("likely_same", records[0]["identity_ai"]["decision"])
            self.assertFalse(records[0]["suppress_alert"])
            coverage._identity_ai(records, context, use_ai=True)
            self.assertEqual(1, decide.call_count)

    def test_only_verified_employer_redirect_promotes_ai_candidate(self) -> None:
        candidate = {"company": "Example", "title": "Software Engineer", "location": "Seattle, WA",
                     "job_id": "12345", "official_url": "https://example.com/jobs/12345"}
        record = {"company": "Example", "title": "Software Engineer", "location": "Seattle, WA",
                  "application_url": "https://example.com/old/12345", "source": "linkedin",
                  "official_company_id": "example", "coverage_status": "official_identity_unmatched",
                  "suppress_alert": False}
        context = {"by_company": {"example": [candidate]}}
        def answer(**kwargs):
            case = list(kwargs["cases"])[0]
            return {case["case_id"]: {"decision": "likely_same", "confidence": 0.95}}
        with tempfile.TemporaryDirectory() as tmp, patch.object(
            coverage, "IDENTITY_AI_CACHE_PATH", Path(tmp) / "cache.json"
        ), patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}), patch.object(
            coverage.compact_ai, "decide", side_effect=answer
        ), patch.object(coverage.requests, "get", return_value=SimpleNamespace(
            status_code=200, url=candidate["official_url"]
        )) as get:
            stats = coverage._identity_ai([record], context, use_ai=True)
            self.assertEqual(1, stats["verification_requests"])
            self.assertEqual("official_duplicate", record["coverage_status"])
            self.assertTrue(record["suppress_alert"])
            get.assert_called_once()


class DetailRecoveryTests(unittest.TestCase):
    def test_metadata_gate_defers_jd_only_constraints(self) -> None:
        self.assertEqual("clear", official._metadata_detail_candidate_kind({
            "company": "Example", "title": "Software Engineer", "location": "Seattle, WA",
            "description": "US citizenship required for this contract. " * 10,
        }))
        self.assertEqual("skip", official._metadata_detail_candidate_kind({
            "company": "Example", "title": "Senior Software Engineer", "location": "Seattle, WA",
            "description": "",
        }))

    def _job(self, company: str, number: int) -> dict:
        return {"company": company, "title": "Software Engineer", "location": "Seattle, WA",
                "job_id": str(number), "official_url": f"https://example.com/jobs/{number}",
                "description": "", "posted_date": "2026-09-25", "fetched_at": NOW.isoformat()}

    def _html(self, number: int) -> str:
        return ('<script type="application/ld+json">'
                '{"@type":"JobPosting","title":"Software Engineer",'
                f'"identifier":"{number}","description":"' + 'Build reliable software. ' * 18 + '"}'
                '</script>')

    def test_parses_jsonld_and_equinix_dom(self) -> None:
        description, title, _, identifier = jd_recovery.extract_detail(self._html(1), "Meta")
        self.assertGreaterEqual(len(description), 200)
        self.assertEqual(("Software Engineer", "1"), (title, identifier))
        description, _, _, _ = jd_recovery.extract_detail(
            '<div class="job-description">' + 'Build network systems. ' * 20 + '</div>', "Equinix")
        self.assertGreaterEqual(len(description), 200)

    def test_request_cap_and_identity_validation(self) -> None:
        jobs = [self._job(company, n) for n, company in enumerate(("Meta", "Disney", "Netflix"), 1)]
        results = [{"company": job["company"], "jobs": [job], "http_requests": 0} for job in jobs]
        def fetch(_session, url, **_kwargs):
            number = int(url.rsplit("/", 1)[-1])
            return SimpleNamespace(text=self._html(number), url=url)
        with patch.object(jd_recovery, "http_get", side_effect=fetch), patch.object(
            jd_recovery, "make_session", return_value=SimpleNamespace(close=lambda: None)
        ):
            stats = jd_recovery.recover(results, [], lambda _: "clear", request_cap=2)
        self.assertEqual(2, stats["detail_requests"])
        self.assertEqual(2, stats["detail_success"])
        self.assertEqual(1, stats["budget_deferred"])
        self.assertEqual(2, stats["usable_jd"])
        self.assertFalse(jd_recovery._same_job(jobs[0], "https://example.com/jobs/999", "Other Job", "999"))

    def test_stale_last_good_survives_detail_failure(self) -> None:
        job = self._job("Meta", 1)
        previous = {**job, "description": "Good complete JD. " * 20,
                    "detail_fetched_at": (NOW - timedelta(days=30)).isoformat()}
        result = {"company": "Meta", "jobs": [job], "http_requests": 0}
        with patch.object(jd_recovery, "http_get", side_effect=ValueError("HTTP 404")), patch.object(
            jd_recovery, "make_session", return_value=SimpleNamespace(close=lambda: None)
        ):
            stats = jd_recovery.recover([result], [previous], lambda _: "clear", request_cap=1)
        self.assertEqual(1, stats["detail_requests"])
        self.assertGreaterEqual(len(job["description"]), 200)
        self.assertEqual(1, stats["usable_jd"])

    def test_ai_skip_avoids_detail_and_keeps_scoring_fields(self) -> None:
        job = self._job("Netflix", 1)
        result = {"company": "Netflix", "jobs": [job]}
        def answer(**kwargs):
            case = list(kwargs["cases"])[0]
            return {case["case_id"]: {"decision": "skip", "confidence": 0.94, "priority": "low"}}
        with patch.object(jd_recovery.compact_ai, "decide", side_effect=answer), patch.object(
            jd_recovery, "http_get"
        ) as fetch:
            stats = jd_recovery.recover([result], [], lambda _: "borderline", api_key="test-key")
        self.assertEqual(1, stats["ai_skip"])
        self.assertEqual(0, stats.get("detail_requests", 0))
        self.assertEqual("", job["description"])
        fetch.assert_not_called()

    def test_selective_jd_and_triage_cache_survive_runner_restart(self) -> None:
        job = self._job("Meta", 1)
        job.update(description="Full official description. " * 16,
                   jd_recovery_source="detail", detail_fetched_at=NOW.isoformat(),
                   detail_triage_hash="hash", detail_triage_decision="recover")
        with tempfile.TemporaryDirectory() as tmp, patch.object(
            official, "RECOVERED_JDS_PATH", Path(tmp) / "recovered_jds.json.gz"
        ):
            official.save_recovered_jds([{"jobs": [job]}], [])
            saved = official.load_recovered_jds()
        self.assertEqual(1, len(saved))
        self.assertGreaterEqual(len(saved[0]["description"]), 200)
        self.assertEqual("recover", saved[0]["detail_triage_decision"])


if __name__ == "__main__":
    unittest.main()
