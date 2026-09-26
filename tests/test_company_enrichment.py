import unittest
from collections import Counter
import json
import tempfile
from pathlib import Path

from scripts.enrich_company_profiles import (
    apply_evidence, company_key, import_findings, load_pending, names_index, prune_profile_tags, resolve,
    validate_findings,
)
from sources.company_aliases import match_company_entry, prepare_alias_entries
from sources.company_pending import pending_entry


class CompanyEnrichmentTests(unittest.TestCase):
    def test_curated_import_preserves_existing_values_and_reviews_entity_conflicts(self):
        profiles = [
            {"name": "Scale AI", "aliases": [], "size": "1k-5k", "maturity": "growth",
             "sponsor": "likely", "type": "tech", "tags": [], "priority": "high"},
            {"name": "Mercedes-Benz USA", "aliases": ["Mercedes-Benz Group"], "size": "5k-20k",
             "maturity": "established", "sponsor": "likely", "type": "industrial",
             "tags": [], "priority": "normal"},
        ]
        findings = [
            {"name": "Scale AI", "aliases": [], "size": "200-1k", "maturity": "growth",
             "sponsor": "unknown", "type": "tech", "tags": ["ai_company"]},
            {"name": "Mercedes-Benz Group", "aliases": [], "size": "20k+", "maturity": "established",
             "sponsor": "unknown", "type": "industrial", "tags": []},
            {"name": "New Employer", "aliases": [], "size": "50-200", "maturity": "growth",
             "sponsor": "unknown", "type": "tech", "tags": ["startup", "tech_service"]},
        ]
        review = []
        counts = import_findings(profiles, findings, review)
        self.assertEqual(1, counts["added"])
        self.assertEqual("1k-5k", profiles[0]["size"])
        self.assertEqual("likely", profiles[0]["sponsor"])
        self.assertEqual("high", profiles[0]["priority"])
        self.assertEqual("Mercedes-Benz USA", profiles[1]["name"])
        self.assertEqual(["tech_service"], profiles[2]["tags"])
        self.assertEqual("normal", profiles[2]["priority"])
        self.assertEqual({("Scale AI", "size"), ("Mercedes-Benz Group", "identity")},
                         {(item["name"], item["field"]) for item in review})

    def test_recent_evidence_is_positive_only_and_sec_fills_unknown_maturity(self):
        entries = [
            {"name": "Strong", "aliases": [], "size": "unknown", "maturity": "unknown",
             "sponsor": "unknown", "type": "unknown", "tags": []},
            {"name": "No Record", "aliases": [], "size": "unknown", "maturity": "unknown",
             "sponsor": "unknown", "type": "unknown", "tags": []},
            {"name": "Negative", "aliases": [], "size": "unknown", "maturity": "growth",
             "sponsor": "unlikely", "type": "tech", "tags": []},
        ]
        review = []
        counts = apply_evidence([], entries, Counter({"Strong": 3, "Negative": 5}),
                                {"Strong": Counter({"52": 2})},
                                {2024: Counter(), 2025: Counter(), 2026: Counter()},
                                {"Strong", "Negative"}, review)
        self.assertEqual("likely", entries[0]["sponsor"])
        self.assertEqual("established", entries[0]["maturity"])
        self.assertEqual("finance", entries[0]["type"])
        self.assertEqual("unknown", entries[0]["size"])
        self.assertEqual("unknown", entries[1]["sponsor"])
        self.assertEqual("unlikely", entries[2]["sponsor"])
        self.assertEqual({("Negative", "sponsor"), ("Negative", "maturity")},
                         {(item["name"], item["field"]) for item in review})
        self.assertEqual(1, counts["sponsor_likely"])

    def test_legal_suffix_matching_does_not_conflate_group_with_subsidiary(self):
        self.assertEqual("coxautomotive", company_key("Cox Automotive Inc."))
        self.assertNotEqual(company_key("Mercedes-Benz Group"), company_key("Mercedes-Benz USA"))
        index = names_index([{"name": "Cox Automotive Inc.", "aliases": []}])
        self.assertEqual({"Cox Automotive Inc."}, resolve("Cox Automotive", index))
        profiles = prepare_alias_entries([
            {"name": "Mercedes-Benz USA", "aliases": []},
            {"name": "Mercedes-Benz Group", "aliases": []},
        ])
        self.assertEqual("Mercedes-Benz Group", match_company_entry("Mercedes-Benz Group", profiles)["name"])
        self.assertEqual("Mercedes-Benz USA", match_company_entry("Mercedes-Benz USA", profiles)["name"])

    def test_only_screening_tags_survive(self):
        profiles = [{"tags": ["startup", "cybersecurity", "staffing", "public_company"]}]
        self.assertEqual(1, prune_profile_tags(profiles))
        self.assertEqual(["cybersecurity", "staffing"], profiles[0]["tags"])

    def test_short_curated_brand_joins_unique_legal_name(self):
        profile = {"name": "HP Inc.", "aliases": [], "size": "20k+", "maturity": "established",
                   "sponsor": "likely", "type": "tech", "tags": [], "priority": "normal"}
        finding = {"name": "HP", "aliases": [], "size": "20k+", "maturity": "established",
                   "sponsor": "likely", "type": "tech", "tags": []}
        review = []
        self.assertEqual(1, import_findings([profile], [finding], review)["existing_matched"])
        self.assertIn("HP", profile["aliases"])

    def test_batch_count_and_pending_job_keys_survive_import(self):
        finding = {"name": "Profiled", "aliases": [], "size": "50-200", "maturity": "growth",
                   "sponsor": "unknown", "type": "tech", "tags": []}
        self.assertEqual([finding], validate_findings({"canonical_profile_count": 1, "companies": [finding]}))
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "pending.json"
            key = "a" * 24
            path.write_text(json.dumps({"companies": [
                {"name": "Profiled", "seen_job_keys": [key]},
                {"name": "Still Pending", "seen_job_keys": [key]},
            ]}), encoding="utf-8")
            pending = load_pending(path, [finding])
            self.assertEqual(["Still Pending"], [row["name"] for row in pending])
            self.assertEqual(1, pending[0]["seen_count"])

    def test_pending_rejects_inconsistent_job_count(self):
        with self.assertRaises(ValueError):
            pending_entry({"name": "Example", "seen_job_keys": ["a" * 24], "seen_count": 2})


if __name__ == "__main__":
    unittest.main()
