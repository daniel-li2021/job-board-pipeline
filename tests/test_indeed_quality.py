"""Offline employer and evidence-quality regressions; no crawling or scoring calls."""
import copy
import unittest
from datetime import datetime, timezone
from unittest.mock import patch

import board_pipeline as board
import dashboard
from sources.company_aliases import preserve_source_company
from sources.job_quality import (
    evidence_warnings, EMPLOYER_UNKNOWN, JD_UNVERIFIED, COHORT_UNVERIFIED,
)
from sources import jobspy_local


class IndeedQualityTests(unittest.TestCase):
    def row(self, **extra):
        return dict(source="indeed", job_id="in-123", company="", title="Software Engineer",
                    description="Build and test Python APIs. " * 15, location="Remote, US",
                    tier="A", match_score=94, score_source="cached_llm", seniority_fit="good",
                    hard_constraint_status="ok", recency_bucket="lt3h", first_seen="2026-10-17",
                    canonical_job_key="id::indeed::in-123", cache_key="unchanged", **extra)

    def test_company_model_field_and_missing_values(self):
        for value in [None, float("nan"), "", "  "]:
            row = jobspy_local._normalize("indeed", {"company": value, "company_name": "Named"}, "now")
            self.assertEqual("Named", row["company"])
        row = jobspy_local._normalize("indeed", {"company": "Recruiter", "company_name": "Client"}, "now")
        self.assertEqual("Recruiter", row["company"])

    def test_duplicate_query_can_fill_name_without_replacing_jd_or_dates(self):
        class Frame:
            def __init__(self, rows): self.rows = rows
            def to_dict(self, **_): return self.rows
        row = {"id": "in-123", "company": "", "title": "Engineer", "description": "original JD",
               "date_posted": "2026-10-17", "location": "Remote, US"}
        with patch.object(jobspy_local, "source_queries", return_value=[("primary", "one", 1), ("primary", "two", 1)]), \
             patch.object(jobspy_local, "provenance", return_value={}):
            result = jobspy_local.scrape("indeed", scrape_jobs_func=lambda **kw: Frame([
                row if kw["search_term"] == "one" else dict(row, company="Named", description="different JD")]))
        actual = result["jobs"][0]
        self.assertEqual(1, len(result["jobs"]))
        self.assertEqual("Named", actual["company"])
        self.assertEqual("original JD", actual["description"])
        self.assertEqual(["one", "two"], actual["discovery_queries"]["indeed"])
        self.assertNotIn(EMPLOYER_UNKNOWN, actual["evidence_warnings"])

    def test_previous_name_requires_exact_source_id_and_never_overwrites_name(self):
        prior = self.row(); prior["company"] = "Named"
        for changes in [{"job_id": "other"}, {"source": "linkedin"}, {"job_id": ""}, {"company": "Recruiter"}]:
            row = dict(prior, company="", **{k:v for k,v in changes.items() if k != "company"})
            if "company" in changes: row["company"] = changes["company"]
            before = copy.deepcopy(row)
            preserve_source_company(row, prior)
            self.assertEqual(before, row)
        row = dict(prior, company="")
        key = board.dedup_key(row)
        entry = board.build_store_entry(row, key, prior)
        self.assertEqual("Named", entry["company"])
        for field in ["job_id", "canonical_job_key", "match_score", "cache_key", "first_seen"]:
            self.assertEqual(prior[field], entry[field])

    def test_anonymous_fit_retained_but_action_requires_verification_before_referral(self):
        row = self.row(); row["referral_name"] = "Referral"
        before = copy.deepcopy(row)
        self.assertEqual("A", board.assign_tier(row, True))
        board.refresh_evidence_policy(row)
        self.assertEqual("verify_details", row["recommended_action"])
        self.assertEqual([EMPLOYER_UNKNOWN], row["evidence_warnings"])
        for field in before:
            self.assertEqual(before[field], row[field])
        row["tier"] = "C"
        board.apply_referral_action(row)
        self.assertEqual("skip", row["recommended_action"])
        row.update(tier="A", hard_constraint_status="citizen_or_clearance")
        board.apply_referral_action(row)
        self.assertEqual("skip", row["recommended_action"])

    def test_explicit_placeholder_is_not_trusted_fit_evidence_and_survives_compaction(self):
        for description in ["This suggested job description is intended for developers.",
                            "K SSS, Inc. is listed as the employer for this proposed Software Developer position.",
                            "Softadom is listed as the company for this Software Developer position."]:
            row = self.row(); row.update(company="Named", description=description + " Build APIs." * 30)
            self.assertEqual([JD_UNVERIFIED], evidence_warnings(row))
            self.assertEqual("B", board.assign_tier(row, False))
            board.refresh_evidence_policy(row)
            self.assertEqual(94, row["match_score"])
            self.assertEqual("B", row["tier"])
            compact = board.compact_store_entry(board.build_store_entry(row, board.dedup_key(row)))
            self.assertEqual([JD_UNVERIFIED], evidence_warnings(compact))
            board.refresh_evidence_policy(compact)
            self.assertEqual("verify_details", compact["recommended_action"])
            compact["description"] = "Authentic responsibilities and required qualifications. " * 10
            self.assertNotIn(JD_UNVERIFIED, evidence_warnings(compact))

    def test_generic_jd_mentions_and_fraud_warnings_are_not_automatic_employer_or_fraud_proof(self):
        for description in ["We seek energetic developers for a dynamic team.",
                            "Recruiter is seeking an engineer for our client Named.",
                            "Recruitment Fraud Alert: scammers impersonate Named employees.",
                            "We suggested job description improvements to the team."]:
            row = self.row(); row.update(company="Recruiter", description=description)
            self.assertEqual([], evidence_warnings(row))
            board.refresh_evidence_policy(row)
            self.assertEqual("Recruiter", row["company"])

    def test_quality_policy_does_not_expand_to_unrelated_pipelines(self):
        for source in ["syncareer", "official", "greenhouse"]:
            row = self.row(); row.update(source=source)
            self.assertEqual([], evidence_warnings(row))

    def test_readonly_replay_counts_indeed_separately_from_other_recoveries(self):
        from scripts.preview_indeed_quality import compare
        indeed, linkedin = self.row(), self.row()
        indeed.update(key="indeed", review_status="applied")
        linkedin.update(source="linkedin", key="linkedin", application_url=
            "https://jobs.ashbyhq.com/example/48219357-056f-4089-981a-0c773b196130")
        before = copy.deepcopy([indeed, linkedin])
        with patch.object(board, "load_company_profiles", return_value=[{
            "name": "Example", "career_board_url": "https://jobs.ashbyhq.com/example"}]):
            result = compare({"jobs": []}, [indeed, linkedin])
        self.assertEqual(1, result["board_anonymous_after"])
        self.assertEqual(1, result["board_anonymous_ab_after"])
        self.assertEqual(before, [indeed, linkedin])

    def test_recovered_employer_clears_stale_verification_action(self):
        row = self.row(); row.update(recommended_action="verify_details", evidence_warnings=[EMPLOYER_UNKNOWN],
            application_url="https://jobs.ashbyhq.com/example/48219357-056f-4089-981a-0c773b196130")
        with patch.object(board, "load_company_profiles", return_value=[{
            "name": "Example", "career_board_url": "https://jobs.ashbyhq.com/example"}]):
            board.refresh_evidence_policy(row)
        self.assertEqual("Example", row["company"])
        self.assertEqual([], row["evidence_warnings"])
        self.assertEqual("apply_now", row["recommended_action"])

    def test_upstream_parser_does_not_discard_company_names(self):
        try:
            from jobspy.indeed import Indeed
            from jobspy.model import ScraperInput, Site
        except ImportError:
            self.skipTest("optional python-jobspy integration")
        for employer in [None, {"name": None, "dossier": None, "relativeCompanyPageUrl": None},
                         {"name": "Named", "dossier": None, "relativeCompanyPageUrl": "/cmp/named"}]:
            scraper = Indeed()
            scraper.base_url = "https://www.indeed.com"
            scraper.scraper_input = ScraperInput(site_type=[Site.INDEED])
            raw = dict(key="123", title="Engineer", employer=employer, description={"html": "Build Python APIs."},
                       attributes=[], datePublished=1792281600000,
                       compensation={"baseSalary": None, "estimated": None},
                       location={"countryCode": "US", "formatted": {"long": "Remote, US"}})
            parsed = scraper._process_job(raw)
            expected = employer.get("name") if employer else None
            self.assertEqual(expected, parsed.company_name)
            normalized = jobspy_local._normalize("indeed", parsed.model_dump(), "now")
            self.assertEqual(expected or "", normalized["company"])

    def test_2027_graduate_metadata_caps_priority_but_retains_role_and_score(self):
        row = self.row(); row.update(company="Atlassian", source="linkedin", title="Machine Learning Engineer, 2027 Graduate U.S.",
                                     description="", description_available=False, score_source=board.SCORE_METADATA,
                                     recovery_input_hash="fixture", match_score=88, role_family="ai")
        self.assertTrue(board.hard_filter(row)[0])
        self.assertEqual("B", board.assign_tier(row, True))
        board.refresh_retained_entry_policy(row, {})
        self.assertEqual("B", row["tier"])
        self.assertEqual(88, row["match_score"])
        self.assertIn(COHORT_UNVERIFIED, row["evidence_warnings"])
        self.assertEqual("verify_details", row["recommended_action"])
        row.update(description="Candidates graduating in 2026 or 2027 are welcome. " * 10)
        self.assertNotIn(COHORT_UNVERIFIED, evidence_warnings(row))
        self.assertTrue(board.hard_filter(row)[0])

    def test_dashboard_exposes_all_warnings_without_mutating_history(self):
        entry = self.row(); entry.update(description="", description_available=True,
            evidence_warnings=[JD_UNVERIFIED], review_status="applied")
        before = copy.deepcopy(entry)
        row = dashboard.normalize_row(entry, "board", datetime.now(timezone.utc), [], {}, [])
        self.assertEqual([EMPLOYER_UNKNOWN, JD_UNVERIFIED], row["evidence_warnings"])
        self.assertEqual(before, entry)


if __name__ == "__main__":
    unittest.main()
