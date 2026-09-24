from __future__ import annotations

import gzip
import json
import tempfile
import unittest
from contextlib import ExitStack
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock, patch
from urllib.parse import parse_qs, urlsplit

import board_pipeline
import alert_history
import coverage_reconcile
import daily_pipeline
import dashboard
import official_careers
import review_state
from sources.company_aliases import company_risk_rank, load_alias_file, match_company_alias, match_company_entry, prepare_alias_entries
from sources.schema import combined_cache_key_from_hash, dedup_key, make_job, match_content_hash, normalize_job_url, normalize_location_key
from sources.schema import classify_location_bucket
from sources import linkedin_local, local_search, schema
from sources.careers.query_terms import ROLE_SEARCH_QUERIES
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


class SyncareerStateTests(unittest.TestCase):
    def test_legacy_watchlist_round_trip_preserves_ids_and_review_fields(self) -> None:
        entry = {"title": "Engineer", "first_seen": "2026-09-01", "review_status": "applied", "tier": "B", "match_score": 75}
        with tempfile.TemporaryDirectory() as tmpdir:
            current, legacy = Path(tmpdir) / "current.json", Path(tmpdir) / "legacy.json"
            with patch.object(daily_pipeline, "WATCHLIST_PATH", current), patch.object(daily_pipeline, "LEGACY_WATCHLIST_PATH", legacy):
                self.assertEqual({}, daily_pipeline.load_watchlist())
                for payload in ({"entries": {"123": entry}}, {"entries": [{**entry, "job_id": "123"}]}, [{**entry, "job_id": "123"}]):
                    legacy.write_text(json.dumps(payload))
                    loaded = daily_pipeline.load_watchlist()
                    self.assertEqual({"123": {**entry, "job_id": "123"}}, loaded)
                    daily_pipeline.save_watchlist(loaded)
                    reloaded = daily_pipeline.load_watchlist()["123"]
                    for field, value in loaded["123"].items():
                        self.assertEqual(value, reloaded[field])
                    self.assertEqual("yes", reloaded["kept"])
                    self.assertFalse(reloaded["description_available"])
                    current.unlink()

    def test_corrupt_state_is_not_treated_as_empty_or_replaced_by_legacy(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            current, legacy = Path(tmpdir) / "current.json", Path(tmpdir) / "legacy.json"
            legacy_seen = Path(tmpdir) / "legacy_seen.json"
            legacy.write_text('{"entries": []}')
            with patch.object(daily_pipeline, "WATCHLIST_PATH", current), patch.object(daily_pipeline, "LEGACY_WATCHLIST_PATH", legacy), patch.object(daily_pipeline, "SEEN_IDS_PATH", current), patch.object(daily_pipeline, "LEGACY_SEEN_IDS_PATH", legacy_seen):
                for text in ('{', 'null', '{}', '{"entries": [null]}', '{"entries": [{}]}'):
                    current.write_text(text)
                    with self.assertRaises(ValueError):
                        daily_pipeline.load_watchlist()
                    with self.assertRaises(ValueError):
                        daily_pipeline.load_seen_ids()
                    self.assertEqual(text, current.read_text())
                for payload in (["123", 456], {"seen_ids": ["123", 456]}):
                    current.write_text(json.dumps(payload))
                    self.assertEqual({"123", "456"}, daily_pipeline.load_seen_ids())
                current.unlink()
                self.assertEqual(set(), daily_pipeline.load_seen_ids())


class MatchingProfileTests(unittest.TestCase):
    def test_required_profiles_preserve_text_and_invalidate_cache_on_change(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, ExitStack() as stack:
            paths = []
            for name in ("CANDIDATE_PROFILE_PATH", "RESUME_SWE_PATH", "RESUME_AI_PATH"):
                path = Path(tmpdir) / name
                path.write_text(f"{name}\n", encoding="utf-8")
                paths.append(path)
                stack.enter_context(patch.object(board_pipeline, name, path))
            before = board_pipeline.load_profiles()
            self.assertEqual("RESUME_SWE_PATH\n", before["resume_swe"])
            for path in paths:
                original = path.read_text(encoding="utf-8")
                path.write_text(original + "updated", encoding="utf-8")
                self.assertNotEqual(before["fingerprint"], board_pipeline.load_profiles()["fingerprint"])
                path.write_text(" \n", encoding="utf-8")
                with self.assertRaises(ValueError):
                    board_pipeline.load_profiles()
                path.unlink()
                with self.assertRaises(FileNotFoundError):
                    board_pipeline.load_profiles()
                path.write_text(original, encoding="utf-8")
            self.assertEqual(before, board_pipeline.load_profiles())


class ReferralAliasTests(unittest.TestCase):
    def test_single_alias_file_is_consistent_across_pipelines(self) -> None:
        targets = load_alias_file(ROOT / "config" / "target_companies.json")
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
        targets = load_alias_file(ROOT / "config" / "target_companies.json")
        self.assertIsNone(match_company_alias("Sapios", targets))
        self.assertIsNone(match_company_alias("Metadata Systems", targets))
        self.assertIsNone(match_company_alias("GE HealthCare", targets))

    def test_declared_company_exclusions_prevent_short_alias_collisions(self) -> None:
        entries = prepare_alias_entries([{
            "id": "flex", "name": "Flex",
            "exclude_aliases": ["Flex Employee Services", "Trade Flex Supply Chain Solutions Inc."],
        }])
        self.assertEqual("Flex", match_company_alias("Flex", entries))
        self.assertIsNone(match_company_alias("Flex Employee Services", entries))
        self.assertIsNone(match_company_alias("Trade Flex Supply Chain Solutions Inc.", entries))


class DashboardPolicyTests(unittest.TestCase):
    def test_pending_company_profiles_are_a_separate_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            public = Path(tmpdir)
            local_pending = public / "local-company-profiles-pending.json"
            coverage = public / "source-coverage.md"
            coverage.write_text("coverage", encoding="utf-8")
            (public / "dashboard.json").write_text(json.dumps({
                "history_details": {
                    "old": ["board", "Old Co", "Old Job", "Remote", "https://old", "B", 80],
                    "same": ["board", "Same Co", "Old Title", "Remote", "https://same", "A", 91],
                },
            }), encoding="utf-8")
            payload = {
                "generated_at": "2026-09-15T12:00:00+00:00",
                "company_profiles_pending": ["A Co", "B Co"],
                "history_details": {
                    "same": ["board", "Same Co", "New Title", "Remote", "https://same", "-", ""],
                },
                "health": {}, "health_history": [],
            }
            with patch.object(dashboard, "PUBLIC_DIR", public), patch.object(
                dashboard, "DASHBOARD_JSON", public / "dashboard.json",
            ), patch.object(dashboard, "DASHBOARD_HTML", public / "index.html"), patch.object(
                dashboard, "PENDING_COMPANY_PROFILES_JSON", public / "company_profiles_pending.json",
            ), patch.object(
                dashboard, "LOCAL_PENDING_COMPANY_PROFILES_JSON", local_pending,
            ), patch.object(dashboard.coverage_reconcile, "COVERAGE_MD_PATH", coverage), patch.object(
                dashboard.pipeline_health, "write",
            ):
                dashboard.write_dashboard(payload)
            main = json.loads((public / "dashboard.json").read_text(encoding="utf-8"))
            pending = json.loads((public / "company_profiles_pending.json").read_text(encoding="utf-8"))
            self.assertNotIn("company_profiles_pending", main)
            self.assertEqual("Old Job", main["history_details"]["old"][2])
            self.assertEqual("New Title", main["history_details"]["same"][2])
            self.assertEqual(["A", 91], main["history_details"]["same"][5:])
            self.assertEqual({"generated_at": payload["generated_at"], "count": 2, "companies": ["A Co", "B Co"]}, pending)
            self.assertEqual(pending, json.loads(local_pending.read_text(encoding="utf-8")))

    def test_pending_company_profiles_accumulate_and_drop_curated_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            stored = Path(tmpdir) / "company_profiles_pending.json"
            stored.write_text(json.dumps({"companies": ["Legacy Co", "Profiled Alias"]}), encoding="utf-8")
            profiles = prepare_alias_entries([{"name": "Profiled Co", "aliases": ["Profiled Alias"]}])
            with patch.object(dashboard, "LOCAL_PENDING_COMPANY_PROFILES_JSON", stored):
                self.assertEqual(
                    ["Legacy Co", "New Co"],
                    dashboard.pending_company_profiles(["New Co", "Profiled Co"], profiles),
                )

    def test_pending_company_capture_precedes_dashboard_filtering(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            stored = Path(tmpdir) / "company_profiles_pending.json"
            stored.write_text(json.dumps({"companies": ["Legacy Co"]}), encoding="utf-8")
            filtered_entry = {"company": "Filtered Co", "title": "Engineer"}
            stores = [({}, [filtered_entry]), ({}, []), ({}, [])]
            with patch.object(dashboard, "LOCAL_PENDING_COMPANY_PROFILES_JSON", stored), patch.object(
                dashboard, "load_alias_file", return_value=[],
            ), patch.object(
                dashboard, "_load_entries", side_effect=stores,
            ), patch.object(
                dashboard, "config_company_match", return_value={"name": "Filtered Co"},
            ), patch.object(
                dashboard.coverage_reconcile, "build_coverage_payload", return_value={"records": []},
            ), patch.object(
                dashboard.pipeline_health, "build", return_value=({}, []),
            ):
                payload = dashboard.build_payload(datetime(2026, 9, 16, tzinfo=timezone.utc))
            self.assertEqual([], payload["workflow_rows"])
            self.assertEqual(["Filtered Co", "Legacy Co"], payload["company_profiles_pending"])

    def test_observability_cards_share_one_responsive_row_and_legacy_telemetry_is_unknown(self) -> None:
        template = dashboard.HTML_TEMPLATE
        self.assertIn('<div class="cards"><div class="card"><span>LLM Matching Today</span>', template)
        self.assertIn('<div class="card"><span>Coverage</span>', template)
        self.assertIn('<div class="card"><span>Matching</span>', template)
        self.assertIn("r.latency_measured?`${r.latency_seconds}s`:'Unknown'", template)
        self.assertIn("r.json_reliability_measured", template)
        self.assertIn("r.batch_outcomes_measured", template)
        self.assertIn("official presence ${presence}", template)

    def test_dashboard_company_key_reuses_canonical_referral_alias(self) -> None:
        referrals = load_alias_file(ROOT / "config" / "target_companies.json")
        row = dashboard.normalize_row(
            {
                "canonical_job_key": "test-job",
                "company": "Amazon Web Services (AWS)",
                "title": "Software Engineer",
            },
            "board",
            datetime(2026, 8, 29, 12, tzinfo=timezone.utc),
            referrals,
            {},
        )
        self.assertEqual("Amazon", row["referral"])
        self.assertEqual("amazon", row["company_key"])

    def test_sponsorship_labels_use_existing_source_data(self) -> None:
        self.assertEqual("Sponsor", dashboard.sponsorship_label({"sponsorship": "H-1B Sponsor"}))
        self.assertEqual("No sponsor", dashboard.sponsorship_label({"sponsorship": "No H-1B Sponsor"}))
        self.assertEqual("Sponsor", dashboard.sponsorship_label({"description": "Visa sponsorship is available for this role."}))
        self.assertEqual("No sponsor", dashboard.sponsorship_label({"description": "We are unable to provide visa sponsorship."}))
        self.assertEqual("No sponsor", dashboard.sponsorship_label({"description": "Visa sponsorship is not available."}))
        self.assertEqual("Unknown", dashboard.sponsorship_label({"description": "Applicants may require sponsorship."}))
        self.assertEqual("Unknown", dashboard.sponsorship_label({}))
        self.assertEqual("Likely", dashboard.sponsorship_label({}, {"sponsor": "likely"}))
        self.assertEqual("Unlikely", dashboard.sponsorship_label({}, {"sponsor": "unlikely"}))
        self.assertEqual("No sponsor", dashboard.sponsorship_label(
            {"description": "Applicants must be authorized to work without sponsorship now or in the future."},
            {"sponsor": "likely"},
        ))
        self.assertEqual("Sponsor", dashboard.sponsorship_label(
            {"description": "H-1B sponsorship is available for this role."},
            {"sponsor": "unlikely"},
        ))
        self.assertEqual("Likely", dashboard.sponsorship_label(
            {"description": "H-1B sponsorship may be available on a case-by-case basis."},
            {"sponsor": "unlikely"},
        ))
        likely_phrases = [
            "OPT and STEM OPT candidates are welcome.",
            "CPT candidates may apply.",
            "We support H-1B transfers.",
            "Candidates in F-1 visa status are accepted.",
        ]
        for description in likely_phrases:
            with self.subTest(description=description):
                self.assertEqual("Likely", dashboard.sponsorship_label({"description": description}))
        no_sponsor_phrases = [
            "U.S. citizenship is required for this role.",
            "Candidates must be permanent residents.",
            "We cannot support CPT, OPT, or STEM OPT employment.",
            "You must not require visa sponsorship now or at any time in the future.",
        ]
        for description in no_sponsor_phrases:
            with self.subTest(description=description):
                self.assertEqual("No sponsor", dashboard.sponsorship_label({"description": description}))
        self.assertEqual("No sponsor", dashboard.sponsorship_label({
            "sponsorship": "Sponsor",
            "requirements": "The employer will not provide visa sponsorship now or in the future, even though OPT candidates are welcome.",
        }))
        self.assertEqual("Sponsor", daily_pipeline.sponsorship_from_supports(["H-1B"]))
        self.assertEqual("No sponsor", daily_pipeline.sponsorship_from_supports(["OPT"]))
        self.assertEqual("Unknown", daily_pipeline.sponsorship_from_supports([]))
        job = make_job(
            source="test", company="Example", title="Engineer",
            description="Visa sponsorship is available for this role.",
        )
        self.assertEqual("Sponsor", job["sponsorship"])
        self.assertEqual("Sponsor", board_pipeline.build_store_entry(job, "test")["sponsorship"])

    def test_board_c_fallback_uses_thresholds_and_existing_scores(self) -> None:
        now = datetime(2026, 8, 29, 12, tzinfo=timezone.utc)

        def row(tier: str, score: int, age: int, key: str, pipeline: str = "board") -> dict:
            return {
                "canonical_job_key": key,
                "pipeline": pipeline,
                "tier": tier,
                "score": score,
                "company": key,
                "location": "Seattle, WA",
                "filter_status": "kept",
                "suppress_alert": False,
                "review_status": "unreviewed",
                "freshness": dashboard.recency(
                    {"first_seen": (now - timedelta(hours=age)).isoformat()}, now
                ),
            }

        base = [row("A", 90, 2, "ab-1")]
        stored = base + [
            row("C", 64, 1, "c-64"),
            row("C", 70, 6, "c-70-old"),
            row("C", 70, 3, "c-70-new"),
            row("C", 59, 1, "c-59"),
            row("C", 99, 1, "other-pipeline", pipeline="official"),
        ]
        filled = dashboard.append_board_c_fallback(
            base, stored, minimum_ab=10, target=20, window="fresh"
        )
        self.assertEqual(
            ["ab-1", "c-70-new", "c-70-old", "c-64"],
            [item["canonical_job_key"] for item in filled],
        )
        self.assertTrue(all(item["score"] >= 60 for item in filled))

    def test_board_c_fallback_does_nothing_at_ab_minimum(self) -> None:
        base = [
            {"pipeline": "board", "tier": "B", "canonical_job_key": f"b-{index}"}
            for index in range(10)
        ]
        self.assertEqual(
            base,
            dashboard.append_board_c_fallback(
                base, [], minimum_ab=10, target=20, window="fresh"
            ),
        )

    def test_discovery_metadata_follows_first_seen_not_posted_date(self) -> None:
        now = datetime(2026, 8, 29, 12, tzinfo=timezone.utc)
        recent_discovery = dashboard.recency(
            {
                "posted_date": "2026-08-01",
                "date_confidence": "high",
                "first_seen": (now - timedelta(hours=2)).isoformat(),
            },
            now,
        )
        self.assertTrue(recent_discovery["fresh_activity"])
        self.assertTrue(recent_discovery["rolling_activity"])
        self.assertEqual("gt7d", recent_discovery["posted"]["bucket"])

        old_discovery = dashboard.recency(
            {
                "posted_date": now.isoformat(),
                "date_confidence": "high",
                "first_seen": (now - timedelta(days=4)).isoformat(),
            },
            now,
        )
        self.assertFalse(old_discovery["fresh_activity"])
        self.assertFalse(old_discovery["rolling_activity"])

    def test_rolling_discovery_window_includes_exactly_72_hours(self) -> None:
        now = datetime(2026, 8, 29, 12, tzinfo=timezone.utc)
        boundary = dashboard.recency({"first_seen": (now - timedelta(hours=72)).isoformat()}, now)
        expired = dashboard.recency({"first_seen": (now - timedelta(hours=72, seconds=1)).isoformat()}, now)
        self.assertTrue(boundary["rolling_activity"])
        self.assertFalse(expired["rolling_activity"])

    def test_sort_is_tier_then_posting_day_then_quality_then_exact_age(self) -> None:
        now = datetime(2026, 8, 29, 12, tzinfo=timezone.utc)

        def row(tier: str, score: int, age: int, company: str) -> dict:
            return {
                "tier": tier,
                "score": score,
                "company": company,
                "freshness": dashboard.recency(
                    {
                        "posted_date": (now - timedelta(hours=age)).isoformat(),
                        "date_confidence": "high",
                        "first_seen": now.isoformat(),
                    },
                    now,
                ),
            }

        ordered = dashboard._sort_rows([
            row("B", 99, 1, "B Co"),
            row("A", 85, 5, "A lower"),
            row("A", 92, 20, "A higher"),
            row("A", 99, 30, "Yesterday best"),
        ])
        self.assertEqual(
            ["A higher", "A lower", "Yesterday best", "B Co"],
            [item["company"] for item in ordered],
        )

    def test_company_profiles_and_internships_change_application_order_not_score(self) -> None:
        profiles = load_alias_file(ROOT / "profile" / "company_profiles.json")
        self.assertEqual("high", match_company_entry("Amazon Web Services", profiles)["priority"])
        self.assertEqual("low", match_company_entry("Randstad USA", profiles)["priority"])
        now = datetime(2026, 9, 13, 12, tzinfo=timezone.utc)

        def normalized(company: str, title: str) -> dict:
            return dashboard.normalize_row({
                "company": company,
                "title": title,
                "location": "Seattle, WA",
                "match_score": 90,
                "tier": "A",
                "first_seen": now.isoformat(),
            }, "board", now, [], {}, profiles)

        amazon = normalized("Amazon", "Software Engineer I")
        staffing = normalized("Randstad USA", "Junior Software Engineer")
        internship = normalized("Figma", "Software Engineer Intern")
        figma_full_time = normalized("Figma", "Software Engineer I")
        ibm = normalized("IBM", "Software Engineer I")
        cloudflare = normalized("Cloudflare", "Software Engineer I")
        self.assertEqual("Amazon", dashboard._sort_rows([internship, staffing, amazon])[0]["company"])
        self.assertEqual(
            ["Software Engineer I", "Software Engineer Intern"],
            [row["title"] for row in dashboard._sort_rows([internship, figma_full_time])],
        )
        self.assertEqual(90, internship["score"])
        self.assertEqual("low", internship["application_priority"])
        self.assertEqual("Amazon", dashboard._sort_rows([ibm, amazon])[0]["company"])
        self.assertEqual(90, ibm["score"])
        self.assertTrue(ibm["tech_service"])
        self.assertEqual(1, company_risk_rank(match_company_entry("Cloudflare", profiles)))
        self.assertEqual(2, company_risk_rank(match_company_entry("Lockheed Martin", profiles)))
        self.assertEqual("Amazon", dashboard._sort_rows([cloudflare, amazon])[0]["company"])

    def test_why_is_concise_and_order_uses_experience_and_evidence_not_fallback_label(self) -> None:
        now = datetime(2026, 9, 15, 12, tzinfo=timezone.utc)
        base = {
            "company": "New Company",
            "title": "AI Engineer",
            "location": "New York, NY",
            "match_score": 95,
            "tier": "A",
            "first_seen": now.isoformat(),
            "role_family": "ai",
            "seniority_fit": "good",
            "score_source": "cached_llm",
            "score_model": "legacy_unknown",
            "scoring_version": "legacy_unknown",
            "reasoning_effort": "unknown",
            "description_available": True,
        }
        normalized = dashboard.normalize_row(base, "board", now, [], {}, [])
        self.assertEqual(["AI/ML fit", "Experience fit"], normalized["why_match"])
        self.assertEqual(["Profile pending", "Neutral priority"], normalized["why_company"])
        self.assertEqual(["LLM"], normalized["why_evidence"])

        strong_fallback = dashboard.normalize_row(
            {**base, "company": "Fallback", "score_source": "rule_fallback"}, "board", now, [], {}, [],
        )
        weak_cached = dashboard.normalize_row(
            {**base, "company": "Cached", "description_available": False, "main_gaps": ["Requires 3+ years"]},
            "board", now, [], {}, [],
        )
        self.assertEqual("3+ yrs required", weak_cached["why_gap"])
        self.assertEqual(["LLM", "Title only"], weak_cached["why_evidence"])
        self.assertEqual("Fallback", dashboard._sort_rows([weak_cached, strong_fallback])[0]["company"])
        self.assertNotIn("legacy_unknown", dashboard.HTML_TEMPLATE)

    def test_official_registry_has_search_link_only_targets(self) -> None:
        catalog = {entry["id"]: entry for entry in dashboard.official_search_catalog()}
        for company_id in ("goldman-sachs", "citadel", "tesla", "wayfair"):
            self.assertEqual("search_link_only", catalog[company_id]["automation"])
            self.assertTrue(catalog[company_id]["search_links"])
        for company_id in (
            "disney", "qualcomm", "meta", "tiktok", "linkedin", "walmart",
            "zoom", "pure-storage", "databricks", "roblox", "ebay", "amd",
            "mathworks", "netapp", "netflix", "two-sigma", "cvs",
            "wells-fargo", "yahoo", "ansys", "verizon",
        ):
            self.assertEqual("active", catalog[company_id]["automation"])
            self.assertTrue(catalog[company_id]["search_links"])
        self.assertEqual("A", catalog["meta"]["priority_tier"])

    def test_known_foreign_city_only_locations_are_not_visible(self) -> None:
        for location in ("Bucharest", "Noida", "Bratislava, Slovakia", "Basel"):
            self.assertEqual("non_us", classify_location_bucket(location))
            self.assertFalse(dashboard.visible_candidate({
                "location": location,
                "filter_status": "kept",
                "suppress_alert": False,
                "tier": "B",
            }))

    def test_status_command_resolves_url_and_persists_applied(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            store = root / "jobs.json"
            state = root / "review_state.json"
            job = official_job("10001", "Software Engineer I", "Seattle, WA")
            store.write_text(json.dumps({"entries": [job]}), encoding="utf-8")
            state.write_text(json.dumps({"jobs": {}}), encoding="utf-8")
            with patch.object(review_state, "STORE_PATHS", (store,)), patch.object(review_state, "STATE_PATH", state):
                key = review_state.set_status(job["official_url"], "applied", "Applied 2026-08-29")
            saved = json.loads(state.read_text(encoding="utf-8"))
            self.assertEqual("applied", saved["jobs"][key]["status"])
            self.assertEqual("Applied 2026-08-29", saved["jobs"][key]["notes"])

    def test_ats_issue_fallback_round_trips_the_current_writer(self) -> None:
        job = official_job("10001", "Software Engineer I", "Seattle, WA")
        job.update(tier="B", match_score=75)
        with tempfile.TemporaryDirectory() as tmpdir:
            directory = Path(tmpdir)
            with patch.object(board_pipeline, "BOARD_DIR", directory), patch.object(board_pipeline, "RUNS_DIR", directory / "runs"):
                paths = board_pipeline.write_alert([job], "2026-09-07_1200")
            event = dashboard.parse_issue_event(paths["issue_body"], "board")
        self.assertEqual("2026-09-07_1200", event["stamp"])
        self.assertEqual(1, event["count"])
        self.assertEqual(job["company"], event["jobs"][0]["company"])
        self.assertEqual(job["official_url"], event["jobs"][0]["url"])
        self.assertEqual("B", event["jobs"][0]["tier"])

    def test_alert_history_is_idempotent_and_drives_fresh_even_for_old_job(self) -> None:
        now = datetime(2026, 8, 29, 12, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as tmp:
            history = Path(tmp) / "alerts.json"
            job = official_job("10001", "Software Engineer I", "Seattle, WA")
            job["tier"] = "A"
            job["match_score"] = 88
            job["first_seen"] = (now - timedelta(days=5)).isoformat()
            alert_history.append_event(
                history, pipeline="official", stamp="2026-08-29_1100",
                jobs=[job], event_kind="new_or_promoted_ab", emitted_at=now - timedelta(hours=1),
            )
            alert_history.append_event(
                history, pipeline="official", stamp="2026-08-29_1100",
                jobs=[job], event_kind="new_or_promoted_ab", emitted_at=now - timedelta(hours=1),
            )
            self.assertEqual(1, len(json.loads(history.read_text())["events"]))

            row = {
                "canonical_job_key": alert_history.job_snapshot(job)["canonical_job_key"],
                "pipeline": "official", "tier": "A", "score": 88,
                "company": "Example Tech", "title": job["title"], "location": "Seattle, WA",
                "url": job["official_url"], "filter_status": "kept", "suppress_alert": False,
                "review_status": "unreviewed", "freshness": dashboard.recency(job, now),
            }
            paths = {"board": Path(tmp) / "none1", "official": history, "syncareer": Path(tmp) / "none2"}
            bodies = {key: Path(tmp) / f"{key}.md" for key in paths}
            with patch.object(dashboard, "ALERT_HISTORY_PATHS", paths), patch.object(dashboard, "ISSUE_BODY_PATHS", bodies):
                fresh, basis = dashboard.alert_fresh_rows([row], now)
            self.assertEqual(1, len(fresh))
            self.assertEqual("alerts_and_new_discoveries", basis["official"])
            self.assertEqual(1, fresh[0]["activity_age_hours"])

    def test_official_fresh_includes_unalerted_discoveries_without_caps(self) -> None:
        now = datetime(2026, 9, 8, tzinfo=timezone.utc)
        rows = [dict(canonical_job_key=str(i), pipeline="official", tier="B",
                     company="Example", location="Seattle, WA", score=80,
                     filter_status="kept", freshness=dashboard.recency(
                         {"first_seen": now.isoformat()}, now)) for i in range(600)]
        rows.extend([dict(rows[0], canonical_job_key="excluded", suppress_alert=True),
                     dict(rows[0], canonical_job_key="filtered", filter_status="dropped")])
        with patch.object(dashboard.alert_history, "recent_events", side_effect=lambda path, *args, **kwargs: [{
            "emitted_at": now.isoformat(), "jobs": [{"canonical_job_key": "0"}]}] if path == dashboard.ALERT_HISTORY_PATHS["official"] else []), \
                patch.object(dashboard, "parse_issue_event", return_value=None):
            fresh, _ = dashboard.alert_fresh_rows(rows, now)
        official = [row for row in fresh if row["pipeline"] == "official"]
        self.assertEqual(600, len(official))
        self.assertEqual(600, len({row["canonical_job_key"] for row in official}))

    def test_board_fresh_includes_unalerted_discovery_when_digest_is_skipped(self) -> None:
        now = datetime(2026, 9, 11, 5, tzinfo=timezone.utc)
        rows = [dict(canonical_job_key=key, pipeline="board", tier="B",
                     company="Example", location="Seattle, WA", score=80,
                     filter_status="kept", freshness=dashboard.recency(
                         {"first_seen": now.isoformat()}, now))
                for key in ("alerted", "unalerted")]
        with patch.object(dashboard.alert_history, "recent_events", side_effect=lambda path, *args, **kwargs: [{
            "emitted_at": now.isoformat(), "jobs": [{"canonical_job_key": "alerted"}]}]
                if path == dashboard.ALERT_HISTORY_PATHS["board"] else []), \
                patch.object(dashboard, "parse_issue_event", return_value=None):
            fresh, basis = dashboard.alert_fresh_rows(rows, now)
        self.assertEqual({"alerted", "unalerted"}, {row["canonical_job_key"] for row in fresh})
        self.assertEqual("alerts_and_new_discoveries", basis["board"])

    def test_fresh_omits_explicit_2027_student_cohorts_only(self) -> None:
        now = datetime(2026, 9, 16, tzinfo=timezone.utc)
        titles = {
            "intern": "Software Engineer Intern - 2027 Summer",
            "graduate": "Software Engineer Graduate - 2027 Start",
            "keep": "Software Engineer Intern - 2026 Summer",
        }
        rows = [dict(
            canonical_job_key=key, pipeline="official", tier="B", company="Example",
            title=title, location="Seattle, WA", score=80, filter_status="kept",
            freshness=dashboard.recency({"first_seen": now.isoformat()}, now),
        ) for key, title in titles.items()]
        with patch.object(dashboard.alert_history, "recent_events", return_value=[]), \
                patch.object(dashboard, "parse_issue_event", return_value=None):
            fresh, _ = dashboard.alert_fresh_rows(rows, now)
        self.assertEqual({"keep"}, {row["canonical_job_key"] for row in fresh})

        fallback = dict(rows[0], pipeline="board", tier="C", score=80)
        self.assertEqual([], dashboard.append_board_c_fallback(
            [], [fallback], minimum_ab=10, target=20, window="fresh",
        ))

    def test_public_template_has_compact_navigation_and_shared_status_control(self) -> None:
        self.assertNotIn("Official coverage", dashboard.HTML_TEMPLATE)
        self.assertNotIn("<th>Coverage</th>", dashboard.HTML_TEMPLATE)
        self.assertIn("status-select", dashboard.HTML_TEMPLATE)
        self.assertIn("document.getElementById('updated').textContent=D.updated_pt", dashboard.HTML_TEMPLATE)
        self.assertNotIn("Dashboard last updated:", dashboard.HTML_TEMPLATE)
        self.assertIn("companyTab.style.display=active==='official'?'flex':'none'", dashboard.HTML_TEMPLATE)
        self.assertIn("active=tab.querySelector('[data-k].on')?.dataset.k||'all'", dashboard.HTML_TEMPLATE)
        self.assertIn("company=companyTab.querySelector('[data-company].on')?.dataset.company||'all'", dashboard.HTML_TEMPLATE)
        self.assertNotIn("let active='all',company='all'", dashboard.HTML_TEMPLATE)
        self.assertNotIn('<div class="small">Big Company Official</div>', dashboard.HTML_TEMPLATE)
        self.assertIn("job_review_status", dashboard.HTML_TEMPLATE)
        self.assertNotIn("signInWithOtp", dashboard.HTML_TEMPLATE)
        self.assertIn('id="mainViewTabs"', dashboard.HTML_TEMPLATE)
        self.assertIn('role="tablist"', dashboard.HTML_TEMPLATE)
        self.assertIn('role="tabpanel"', dashboard.HTML_TEMPLATE)
        self.assertIn('data-main-view="fresh"', dashboard.HTML_TEMPLATE)
        self.assertIn('data-main-view="rolling"', dashboard.HTML_TEMPLATE)
        self.assertIn('data-main-view="in-progress"', dashboard.HTML_TEMPLATE)
        self.assertIn('data-main-view="applied"', dashboard.HTML_TEMPLATE)
        self.assertIn("let activeMainView='fresh'", dashboard.HTML_TEMPLATE)
        self.assertIn("renderMainViewTabs(rows)", dashboard.HTML_TEMPLATE)
        self.assertNotIn('href="#section-', dashboard.HTML_TEMPLATE)
        self.assertNotIn("initializeSectionNav", dashboard.HTML_TEMPLATE)
        self.assertNotIn("requestAnimationFrame(update)", dashboard.HTML_TEMPLATE)
        self.assertNotIn("position:sticky;top:0;z-index:30", dashboard.HTML_TEMPLATE)
        self.assertIn("box.textContent='● Synced'", dashboard.HTML_TEMPLATE)
        self.assertIn("sync-expanded", dashboard.HTML_TEMPLATE)
        self.assertIn('class="countline"', dashboard.HTML_TEMPLATE)
        self.assertIn("const statusChoices=['unreviewed','in_progress','applied_complete']", dashboard.HTML_TEMPLATE)
        self.assertIn("Applied/Complete", dashboard.HTML_TEMPLATE)
        self.assertIn("<h2>Deleted</h2>", dashboard.HTML_TEMPLATE)
        self.assertNotIn("jobBoardStatusesV2", dashboard.HTML_TEMPLATE)
        self.assertIn("pending:true", dashboard.HTML_TEMPLATE)
        self.assertIn("Pending sync", dashboard.HTML_TEMPLATE)
        self.assertIn("window.addEventListener('online',refreshSharedStates)", dashboard.HTML_TEMPLATE)
        self.assertIn("persist();renderReviewMessage();renderAll();keys.forEach", dashboard.HTML_TEMPLATE)
        self.assertNotIn("reviewStates[key]=previous", dashboard.HTML_TEMPLATE)
        self.assertNotIn("delete reviewStates[key]", dashboard.HTML_TEMPLATE)
        self.assertIn("<details class=\"panel\"><summary>Referral opportunities</summary>", dashboard.HTML_TEMPLATE)
        self.assertLess(dashboard.HTML_TEMPLATE.index('id="main-view-applied"'), dashboard.HTML_TEMPLATE.index("<h2>Deleted</h2>"))
        self.assertLess(dashboard.HTML_TEMPLATE.index("<h2>Deleted</h2>"), dashboard.HTML_TEMPLATE.index("Referral opportunities"))
        self.assertLess(dashboard.HTML_TEMPLATE.index("Referral opportunities"), dashboard.HTML_TEMPLATE.index("Official company search links"))
        self.assertIn("<th>Sponsorship</th>", dashboard.HTML_TEMPLATE)
        self.assertIn("'Amazon','Meta','TikTok'", dashboard.HTML_TEMPLATE)
        self.assertIn("const companyStatePrefix='company::'", dashboard.HTML_TEMPLATE)
        self.assertIn("const normalRows=rows=>rows.filter(r=>statusOf(r)==='unreviewed'&&!isDeleted(r)&&!isCompanyHidden(r))", dashboard.HTML_TEMPLATE)
        self.assertIn("renderBox('referrals',normalRows(D.referrals))", dashboard.HTML_TEMPLATE)
        self.assertIn("renderSummary()", dashboard.HTML_TEMPLATE)
        self.assertIn("<summary>Hidden companies", dashboard.HTML_TEMPLATE)
        self.assertIn("Show again", dashboard.HTML_TEMPLATE)
        self.assertIn("Enter password to ${hidden?'hide':'show again'} this company", dashboard.HTML_TEMPLATE)
        self.assertIn("allRows.filter(r=>!isPreferenceKey(r.canonical_job_key))", dashboard.HTML_TEMPLATE)
        self.assertIn("renderBox('inProgress',searchedRows(rows.filter(r=>statusOf(r)==='in_progress'&&!isDeleted(r))))", dashboard.HTML_TEMPLATE)
        self.assertIn("renderBox('applied',searchedRows(rows.filter(r=>statusOf(r)==='applied_complete'&&!isDeleted(r))))", dashboard.HTML_TEMPLATE)
        self.assertIn("fresh:discoveryRows(normalRows(D.fresh_24h)).length", dashboard.HTML_TEMPLATE)
        self.assertIn("rolling:discoveryRows(normalRows(D.rolling_3d)).length", dashboard.HTML_TEMPLATE)
        self.assertIn("<span>usable · updated", dashboard.HTML_TEMPLATE)
        self.assertIn("h.keywords", dashboard.HTML_TEMPLATE)


class MatchingPolicyTests(unittest.TestCase):
    def _job(self, *, score: float, bucket: str, title: str = "Software Engineer", seniority: str = "good", gaps: list[str] | None = None) -> dict:
        return {
            "title": title,
            "company": "Example Tech",
            "location": "Seattle, WA",
            "match_score": score,
            "recency_bucket": bucket,
            "score_source": board_pipeline.SCORE_CACHED_LLM,
            "seniority_fit": seniority,
            "main_gaps": gaps or [],
            "hard_constraint_status": "ok",
            "role_family": "swe",
        }

    def test_tiering_has_smooth_recency_decay_and_tighter_b(self) -> None:
        self.assertEqual("B", board_pipeline.assign_tier(self._job(score=82, bucket="3to7d"), False))
        self.assertEqual("C", board_pipeline.assign_tier(self._job(score=70, bucket="1to3d"), False))
        self.assertEqual("B", board_pipeline.assign_tier(self._job(score=75, bucket="1to3d"), False))
        self.assertEqual("B", board_pipeline.assign_tier(self._job(score=92, bucket="gt7d"), False))

    def test_early_career_decays_slowly_but_is_not_auto_a(self) -> None:
        old = self._job(score=80, bucket="gt7d", title="Software Engineer I")
        self.assertEqual("B", board_pipeline.assign_tier(old, False))
        self.assertEqual("A", board_pipeline.assign_tier(self._job(score=94, bucket="gt7d", title="New Grad Software Engineer"), False))
        self.assertEqual("B", board_pipeline.assign_tier(
            self._job(score=99, bucket="lt3h", title="Software Engineer Intern"), False,
        ))
        self.assertEqual("C", board_pipeline.assign_tier(
            self._job(score=99, bucket="lt3h", title="2027 Summer Software Engineer Intern"), False,
        ))

    def test_early_career_requirements_drop_only_explicitly_ineligible_roles(self) -> None:
        filler = " Build production software and collaborate with engineers." * 5
        required_2027 = self._job(score=90, bucket="lt3h", title="Software Engineer New Grad")
        required_2027["description"] = filler + " Graduation in Spring 2027 with a computer science degree is required."
        self.assertEqual(
            (False, "ineligible_2027_graduate_requirement"), board_pipeline.hard_filter(required_2027),
        )

        multiple_years = self._job(score=90, bucket="lt3h", title="Software Engineer New Grad")
        multiple_years["description"] = filler + " Graduation in Spring 2026 or Spring 2027 is required."
        self.assertEqual((True, "keep"), board_pipeline.hard_filter(multiple_years))

        student_only = self._job(score=90, bucket="lt3h", title="Software Engineer Intern")
        student_only["description"] = filler + " Candidates must be currently enrolled in a bachelor's degree program."
        self.assertEqual(
            (False, "ineligible_current_student_requirement"), board_pipeline.hard_filter(student_only),
        )

        graduate_allowed = self._job(score=90, bucket="lt3h", title="Software Engineer Intern")
        graduate_allowed["description"] = filler + " Currently pursuing or recently completed a computer science degree."
        self.assertEqual((True, "keep"), board_pipeline.hard_filter(graduate_allowed))

        current_degree_student = self._job(score=90, bucket="lt3h", title="Software Engineer Intern")
        current_degree_student["description"] = filler + " Current Bachelor's, Master's, or PhD student in computer science."
        self.assertEqual(
            (False, "ineligible_current_student_requirement"), board_pipeline.hard_filter(current_degree_student),
        )

        pursuing_degree = self._job(score=90, bucket="lt3h", title="Software Engineer Intern")
        pursuing_degree["description"] = filler + " You are working toward a BS or MS in computer science."
        self.assertEqual(
            (False, "ineligible_current_student_requirement"), board_pipeline.hard_filter(pursuing_degree),
        )

        student_or_grad = self._job(score=90, bucket="lt3h", title="Software Engineer Intern")
        student_or_grad["description"] = filler + " Open to current undergraduate students or recent graduates."
        self.assertEqual((True, "keep"), board_pipeline.hard_filter(student_or_grad))

        pursuing_or_holding = self._job(score=90, bucket="lt3h", title="Software Engineer Early Career")
        pursuing_or_holding["description"] = filler + " Pursuing or in possession of an undergraduate degree."
        self.assertEqual((True, "keep"), board_pipeline.hard_filter(pursuing_or_holding))

        student_friendly = self._job(score=90, bucket="lt3h", title="Software Engineer Intern")
        student_friendly["description"] = filler + " This program is designed for students interested in software."
        self.assertEqual((True, "keep"), board_pipeline.hard_filter(student_friendly))

        unknown = self._job(score=90, bucket="lt3h", title="Software Engineer Intern 2027")
        unknown["description"] = ""
        self.assertEqual((True, "keep"), board_pipeline.hard_filter(unknown))

    def test_thin_jobs_use_title_and_record_quality_without_auto_demotion(self) -> None:
        def thin(title: str) -> dict:
            job = self._job(score=0, bucket="lt3h", title=title)
            job.update(source="linkedin", source_url="https://www.linkedin.com/jobs/view/42", description="")
            job["score_source"] = board_pipeline.SCORE_FALLBACK
            job["role_family"] = board_pipeline.detect_role_family(job)
            job["match_score"] = board_pipeline.rule_match_score(job)
            return job

        junior = thin("Junior Software Engineer")
        level_two = thin("Software Engineer II")
        level_three = thin("Software Engineer III")
        self.assertEqual((88.0, "A"), (junior["match_score"], board_pipeline.assign_tier(junior, False)))
        self.assertEqual((80.0, "B"), (level_two["match_score"], board_pipeline.assign_tier(level_two, False)))
        self.assertEqual("C", board_pipeline.assign_tier(level_three, False))

        incomplete = thin("Full Stack Developer")
        incomplete["source_url"] = ""
        incomplete["match_score"] = board_pipeline.rule_match_score(incomplete)
        self.assertEqual("C", board_pipeline.assign_tier(incomplete, False))

        nsa = thin("Software Engineer - Entry Level")
        nsa["company"] = "National Security Agency"
        self.assertEqual((False, "incomplete_jd_clearance_risk"), board_pipeline.hard_filter(nsa))

        generic = thin("Engineer I")
        self.assertLess(generic["match_score"], 70)
        self.assertEqual("C", board_pipeline.assign_tier(generic, False))

    def test_lazy_cache_and_failed_only_retry_across_sequential_runs(self) -> None:
        now = datetime.now(timezone.utc).isoformat()

        def job(description: str = "Build Python services and APIs. " * 12) -> dict:
            value = make_job(
                source="greenhouse", company="Example Tech", title="Software Engineer",
                location="Seattle, WA", job_id="one", description=description,
                source_url="https://example.test/jobs/one",
            )
            value["first_seen"] = now
            value["recency_bucket"] = "3to24h"
            board_pipeline.role_seniority_prefilter(value)
            return value

        def result(batch, _profiles, _key, model, _route):
            key = dedup_key(batch[0])
            usage = {
                "model": model, "api_requests": 1, "jobs_scored": 1,
                "input_tokens": 100, "cached_input_tokens": 0, "output_tokens": 20,
                "reasoning_tokens": 5, "estimated_usd": 0.001,
            }
            return {key: {
                "match_score": 88, "seniority_fit": "good", "hard_constraint_status": "ok",
                "top_match_reasons": ["Relevant API work"], "main_gaps": [],
            }}, usage

        profiles = {"fingerprint": "prompt-a", "candidate_fingerprint": "candidate-a"}
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test"}), patch.object(
            board_pipeline, "llm_match_batch", side_effect=result
        ) as call:
            first = job()
            _, _, first_counts = board_pipeline.score_survivors([first], {}, profiles, {}, True)
            self.assertEqual(1, call.call_count)
            self.assertEqual(1, first_counts["llm"])
            cached = {dedup_key(first): board_pipeline.build_store_entry(first, dedup_key(first))}

            second = job()
            _, _, second_counts = board_pipeline.score_survivors(
                [second], {}, {"fingerprint": "prompt-b", "candidate_fingerprint": "candidate-a"}, cached, True
            )
            self.assertEqual(2, call.call_count)
            self.assertEqual(1, second_counts["llm"])
            self.assertEqual("gpt-6-luna", second["score_model"])

            changed = job("Build Java distributed systems and streaming services. " * 10)
            board_pipeline.score_survivors([changed], {}, profiles, cached, True)
            self.assertEqual(3, call.call_count)

        failed = job()
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test"}), patch.object(
            board_pipeline, "llm_match_batch", side_effect=RuntimeError("rate limited")
        ):
            board_pipeline.score_survivors([failed], {}, profiles, {}, True)
        self.assertTrue(failed["llm_retryable"])
        self.assertEqual(board_pipeline.SCORE_FALLBACK, failed["score_source"])
        failed_store = {dedup_key(failed): board_pipeline.build_store_entry(failed, dedup_key(failed))}

        recovered = job()
        recovered["recency_bucket"] = "gt7d"
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test"}), patch.object(
            board_pipeline, "llm_match_batch", side_effect=result
        ) as retry_call:
            _, _, retry_counts = board_pipeline.score_survivors([recovered], {}, profiles, failed_store, True)
        self.assertEqual(1, retry_call.call_count)
        self.assertEqual(1, retry_counts["llm"])
        self.assertFalse(recovered["llm_retryable"])
        self.assertEqual(failed["llm_retry_count"], recovered["llm_retry_count"])
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(0, board_pipeline.save_matching_retry(Path(tmp) / "retry.json.gz", [recovered]))

    def test_match_content_hash_ignores_formatting_but_preserves_constraints(self) -> None:
        base = make_job(
            source="test", company="Example Tech", title="Software Engineer",
            location="Seattle, WA", job_id="one",
            description="Responsibilities Build APIs Required Qualifications 3+ years.",
            sponsorship="No",
        )
        formatted = {
            **base,
            "description": (
                "<p>Responsibilities</p><p>Build&nbsp; APIs</p>"
                "<p>Required Qualifications</p><p>3+ years.</p>"
            ),
        }
        self.assertNotEqual(board_pipeline.jd_hash(base), board_pipeline.jd_hash(formatted))
        self.assertEqual(match_content_hash(base), match_content_hash(formatted))
        for changed in (
            {**base, "description": base["description"].replace("Build APIs", "Design hardware")},
            {**base, "description": base["description"].replace("3+ years", "6+ years")},
            {**base, "description": base["description"] + " US citizenship and clearance required."},
            {**base, "sponsorship": "Yes"},
            {**base, "location": "Toronto, Canada"},
        ):
            self.assertNotEqual(match_content_hash(base), match_content_hash(changed))

        core = (
            "Overview\n" + ("company context " * 500) + "\n"
            "Responsibilities\nBuild APIs.\nRequired Qualifications\n3+ years Python.\nBenefits\n"
        )
        long_a = {**base, "description": core + ("health plan " * 800)}
        long_b = {**base, "description": core + ("wellness plan " * 800)}
        self.assertNotEqual(board_pipeline.jd_hash(long_a), board_pipeline.jd_hash(long_b))
        self.assertEqual(
            board_pipeline.decision_content_hash(long_a),
            board_pipeline.decision_content_hash(long_b),
        )

    def test_non_material_change_reuses_cache(self) -> None:
        profiles = {"fingerprint": "prompt-a", "candidate_fingerprint": "candidate-a"}
        old = make_job(
            source="test", company="Example Tech", title="Software Engineer",
            location="Seattle, WA", job_id="one",
            description="Responsibilities Build APIs Required Qualifications 3+ years.",
        )
        old.update({
            "jd_hash": board_pipeline.jd_hash(old),
            "match_content_hash": board_pipeline.decision_content_hash(old),
            "match_score": 86,
            "score_source": board_pipeline.SCORE_LLM,
            "screen_method": board_pipeline.SCORE_LLM,
            "cache_key": combined_cache_key_from_hash(board_pipeline.decision_content_hash(old), profiles["fingerprint"]),
        })
        store = {dedup_key(old): board_pipeline.build_store_entry(old, dedup_key(old))}
        current = {
            **old,
            "description": "<p>Responsibilities</p><p>Build&nbsp; APIs</p><p>Required Qualifications</p><p>3+ years.</p>",
        }
        current.pop("jd_hash")
        current.pop("match_content_hash")
        current.pop("cache_key")
        with patch.object(board_pipeline, "llm_match_batch", side_effect=AssertionError("cache should win")):
            _method, _errors, counts = board_pipeline.score_survivors(
                [current], {}, profiles, store, use_llm=True
            )
        self.assertEqual(board_pipeline.SCORE_CACHED_LLM, current["score_source"])
        self.assertEqual(1, counts["non_material_change_reused"])
        self.assertEqual(0, counts["new_or_changed"])

        legacy = dict(store[dedup_key(old)])
        legacy.pop("match_content_hash")
        legacy["cache_key"] = combined_cache_key_from_hash(legacy["jd_hash"], profiles["fingerprint"])
        unchanged = make_job(
            source="test", company="Example Tech", title="Software Engineer",
            location="Seattle, WA", job_id="one", description=old["description"],
        )
        _method, _errors, legacy_counts = board_pipeline.score_survivors(
            [unchanged], {}, profiles, {dedup_key(old): legacy}, use_llm=False
        )
        self.assertEqual(1, legacy_counts["reused"])
        self.assertTrue(unchanged["match_content_hash"])

    def test_same_content_jobs_share_one_llm_result_but_remain_separate(self) -> None:
        now = datetime.now(timezone.utc).isoformat()
        jobs = [
            make_job(
                source="test", company="Example Tech", title="Software Engineer",
                location=location, job_id=job_id,
                description="Responsibilities Build Python APIs. Required Qualifications 2+ years. " * 5,
            )
            for job_id, location in (("one", "Seattle, WA"), ("two", "Austin, TX"))
        ]
        for job in jobs:
            job.update(first_seen=now, recency_bucket="3to24h")
            board_pipeline.role_seniority_prefilter(job)

        def result(batch, _profiles, _key, model, _route):
            self.assertEqual(1, len(batch))
            key = dedup_key(batch[0])
            return {key: {
                "match_score": 88, "seniority_fit": "good", "hard_constraint_status": "ok",
                "top_match_reasons": ["Python APIs"], "main_gaps": [],
            }}, {"model": model, "api_requests": 1, "jobs_scored": 1}

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test"}), patch.object(
            board_pipeline, "llm_match_batch", side_effect=result
        ) as call:
            _method, _errors, counts = board_pipeline.score_survivors(
                jobs, {}, {"fingerprint": "prompt-a", "candidate_fingerprint": "candidate-a"}, {}, True
            )
        self.assertEqual(1, call.call_count)
        self.assertEqual((1, 1, 1), (counts["llm"], counts["reused"], counts["same_content_reused"]))
        self.assertNotEqual(dedup_key(jobs[0]), dedup_key(jobs[1]))
        self.assertEqual(
            {board_pipeline.SCORE_LLM, board_pipeline.SCORE_CACHED_LLM},
            {job["score_source"] for job in jobs},
        )

    def test_material_rescore_and_prior_rule_reentry_are_visible(self) -> None:
        profiles = {"fingerprint": "prompt-a", "candidate_fingerprint": "candidate-a"}
        old = make_job(
            source="test", company="Example Tech", title="Software Engineer",
            location="Seattle, WA", job_id="one", description="Build Python APIs. " * 20,
        )
        old.update({
            "jd_hash": board_pipeline.jd_hash(old), "match_content_hash": board_pipeline.decision_content_hash(old),
            "cache_key": combined_cache_key_from_hash(board_pipeline.decision_content_hash(old), profiles["fingerprint"]),
            "match_score": 88, "score_source": board_pipeline.SCORE_LLM,
            "screen_method": board_pipeline.SCORE_LLM, "score_at": datetime.now(timezone.utc).isoformat(),
        })
        changed = {**old, "description": "Design distributed Java services. Required 5+ years. " * 10}
        for field in ("jd_hash", "match_content_hash", "cache_key", "match_score", "score_source", "screen_method"):
            changed.pop(field, None)
        changed["recency_bucket"] = "3to24h"
        board_pipeline.role_seniority_prefilter(changed)

        def result(batch, _profiles, _key, model, _route):
            key = dedup_key(batch[0])
            return {key: {
                "match_score": 70, "seniority_fit": "stretch", "hard_constraint_status": "ok",
                "top_match_reasons": ["distributed systems"], "main_gaps": ["5+ YOE"],
            }}, {"model": model, "api_requests": 1, "jobs_scored": 1}

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test"}), patch.object(
            board_pipeline, "llm_match_batch", side_effect=result
        ):
            _method, _errors, counts = board_pipeline.score_survivors(
                [changed], {}, profiles, {dedup_key(old): board_pipeline.build_store_entry(old, dedup_key(old))}, True
            )
        self.assertEqual(1, counts["new_or_changed_reasons"]["material_jd_change"])
        self.assertEqual(1, counts["rescored_within_24h"])

        rule = {**old, "score_source": board_pipeline.SCORE_FALLBACK, "screen_method": board_pipeline.SCORE_FALLBACK}
        candidate = {**old}
        for field in ("jd_hash", "match_content_hash", "cache_key", "match_score", "score_source", "screen_method"):
            candidate.pop(field, None)
        candidate["recency_bucket"] = "3to24h"
        board_pipeline.role_seniority_prefilter(candidate)
        _method, _errors, rule_counts = board_pipeline.score_survivors(
            [candidate], {}, profiles, {dedup_key(rule): board_pipeline.build_store_entry(rule, dedup_key(rule))}, False
        )
        self.assertEqual(
            1,
            rule_counts["new_or_changed_reasons"]["prior_rule_result_now_eligible_for_llm"],
        )

    def test_repeated_digest_run_does_not_duplicate_alert(self) -> None:
        job = self._job(score=90, bucket="3to24h", title="Junior Software Engineer")
        job.update(source="greenhouse", job_id="one", company="Example Tech", location="Seattle, WA", tier="A")
        state = {"last_digest_date": "", "alerted_keys": [], "alerted_tier": {}}
        first, emit, day = board_pipeline.decide_digest([job], state)
        self.assertTrue(emit)
        board_pipeline.apply_digest_state(state, first, day)
        second, emit_again, _ = board_pipeline.decide_digest([job], state)
        self.assertEqual([], second)
        self.assertFalse(emit_again)

    def test_exact_richer_peer_hydrates_thin_job_but_ambiguous_peers_do_not(self) -> None:
        job = make_job(
            source="linkedin", company="Example Tech", title="Software Engineer I",
            location="Seattle, WA", job_id="linkedin-1",
        )
        peer = make_job(
            source="indeed", company="Example Tech", title="Software Engineer I",
            location="Seattle, WA", job_id="indeed-1", description="x" * 250,
        )
        count = board_pipeline.enrich_from_exact_peers([job], [("board", {"peer": peer})])
        self.assertEqual(1, count)
        self.assertEqual("x" * 250, job["description"])

        other = make_job(
            source="linkedin", company="Example Tech", title="Software Engineer I",
            location="Seattle, WA", job_id="linkedin-2",
        )
        count = board_pipeline.enrich_from_exact_peers(
            [other], [("board", {"one": peer, "two": {**peer, "job_id": "indeed-2"}})],
        )
        self.assertEqual(0, count)
        self.assertFalse(other["description"])

    def test_core_gap_and_stretch_block_easy_a_or_b(self) -> None:
        self.assertEqual("B", board_pipeline.assign_tier(self._job(score=95, bucket="3to24h", gaps=["distributed systems"]), False))
        self.assertEqual("C", board_pipeline.assign_tier(self._job(score=78, bucket="3to24h", seniority="stretch"), False))

    def test_exact_official_peer_llm_result_is_reused_with_official_recency(self) -> None:
        profile_fp = "profile-v1"
        peer_hash = "abc123"
        url = "https://careers.example.com/jobs/10001?utm_source=linkedin"
        peer = {
            "key": "url::https://careers.example.com/jobs/10001",
            "canonical_job_key": "url::https://careers.example.com/jobs/10001",
            "official_url": "https://careers.example.com/jobs/10001",
            "jd_hash": peer_hash,
            "cache_key": combined_cache_key_from_hash(peer_hash, profile_fp),
            "match_score": 91,
            "score_source": "llm",
            "screen_method": "llm",
            "role_family": "swe",
            "resume_profile_used": "resume_swe",
            "seniority_fit": "good",
            "hard_constraint_status": "ok",
            "top_match_reasons": ["exact experience"],
            "main_gaps": [],
            "recommended_action": "apply_now",
            "posted_date": "2026-08-29T10:00:00+00:00",
            "date_confidence": "high",
            "recency_bucket": "3to24h",
        }
        job = make_job(
            source="linkedin", company="Example Tech", title="Software Engineer",
            location="Seattle, WA", official_url=url, description="short card",
        )
        job["canonical_job_key"] = f"url::{normalize_job_url(url)}"
        job["first_seen"] = "2026-08-29T18:00:00+00:00"
        _method, _errors, counts = board_pipeline.score_survivors(
            [job], {}, {"fingerprint": profile_fp}, {}, use_llm=False,
            peer_stores=[("official", {peer["key"]: peer})], prefer_peer=True,
        )
        self.assertEqual(91, job["match_score"])
        self.assertEqual("cached_llm", job["score_source"])
        self.assertEqual("official", job["match_source_pipeline"])
        self.assertEqual("3to24h", job["recency_bucket"])
        self.assertEqual(1, counts["peer_reused"])

        changed = make_job(
            source="greenhouse", company="Example Tech", title="Software Engineer",
            location="Seattle, WA", official_url=url,
            description="Different responsibilities and required qualifications. " * 10,
        )
        changed["canonical_job_key"] = f"url::{normalize_job_url(url)}"
        _method, _errors, changed_counts = board_pipeline.score_survivors(
            [changed], {}, {"fingerprint": profile_fp}, {}, use_llm=False,
            peer_stores=[("official", {peer["key"]: peer})], prefer_peer=True,
        )
        self.assertEqual(0, changed_counts["peer_reused"])
        self.assertEqual(board_pipeline.SCORE_RULE, changed["score_source"])

        stale_profile = make_job(
            source="linkedin", company="Example Tech", title="Software Engineer",
            location="Seattle, WA", official_url=url, description="short card",
        )
        stale_profile["canonical_job_key"] = f"url::{normalize_job_url(url)}"
        _method, _errors, stale_counts = board_pipeline.score_survivors(
            [stale_profile], {}, {"fingerprint": "profile-v2"}, {}, use_llm=False,
            peer_stores=[("official", {peer["key"]: peer})], prefer_peer=True,
        )
        self.assertEqual(0, stale_counts["peer_reused"])
        self.assertEqual(board_pipeline.SCORE_FALLBACK, stale_profile["score_source"])

    def test_shared_official_queries_cover_requested_role_families(self) -> None:
        for query in ("software engineer", "ai engineer", "data engineer", "platform engineer", "full stack engineer", "forward deployed engineer"):
            self.assertIn(query, ROLE_SEARCH_QUERIES)


class CoverageMatchingTests(unittest.TestCase):
    def test_tracking_parameters_do_not_split_one_official_requisition(self) -> None:
        base = official_job("10001", "Software Engineer I", "Seattle, WA")
        tracked = dict(base)
        tracked["official_url"] += "?utm_source=linkedin&trackingId=abc"
        self.assertEqual(dedup_key(base), dedup_key(tracked))

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

    def test_exact_match_reads_raw_syncareer_url_and_requisition_fields(self) -> None:
        official = official_job("R-12345", "Software Engineer", "Austin, TX")
        official["official_url"] = "https://careers.example/jobs/R-12345"
        method, matched = coverage_reconcile.exact_match(
            {"url": "https://careers.example/jobs/R-12345?utm_source=syncareer"},
            [official],
        )
        self.assertEqual("url", method)
        self.assertIs(official, matched)
        method, matched = coverage_reconcile.exact_match(
            {"req_id": "R-12345", "source_url": "https://www.linkedin.com/jobs/view/12345"},
            [official],
        )
        self.assertEqual("job_id", method)
        self.assertIs(official, matched)

    def test_aggregator_url_digits_are_not_requisition_ids(self) -> None:
        method, matched = coverage_reconcile.exact_match(
            {"source_url": "https://www.linkedin.com/jobs/view/12345678"},
            [official_job("12345678", "Different Role", "Boston, MA")],
        )
        self.assertEqual("", method)
        self.assertIsNone(matched)

        self.assertEqual(set(), coverage_reconcile.job_ids({
            "source": "linkedin",
            "application_url": "https://click.appcast.io/track/29893004?cs=71665",
        }))

        method, matched = coverage_reconcile.exact_match(
            {"source": "linkedin", "job_id": "12345678", "title": "Different Role", "location": "Boston, MA"},
            [official_job("12345678", "Another Role", "Seattle, WA")],
        )
        self.assertEqual("", method)
        self.assertIsNone(matched)

    def test_stable_employer_id_disagreement_is_not_hidden_by_title_location(self) -> None:
        external = make_job(
            source="indeed", company="Example Tech", title="Software Engineer I",
            location="Seattle, WA", job_id="indeed-1",
            source_url="https://indeed.test/view/indeed-1",
        )
        external["application_url"] = "https://careers.example.com/jobs/99999"
        coverage_reconcile.annotate_jobs([external], "board", context("validated"))
        self.assertEqual("official_identity_unmatched", external["coverage_status"])
        self.assertEqual(["99999"], external["coverage_stable_ids"])
        self.assertFalse(external["suppress_alert"])

    def test_board_scope_prefers_current_application_identity(self) -> None:
        now = datetime(2026, 9, 15, 12, tzinfo=timezone.utc)
        base = {
            "source": "indeed", "job_id": "in-1", "company": "Example Tech",
            "title": "Software Engineer", "location": "Seattle, WA", "filter_status": "kept",
            "first_seen": "2026-09-15T10:00:00+00:00",
        }
        entries = [
            {**base, "last_seen": "2026-09-15T10:00:00+00:00"},
            {**base, "last_seen": "2026-09-15T11:00:00+00:00", "official_url": "https://careers.example/jobs/11111"},
        ]
        snapshot = {"jobs": [{**base, "application_url": "https://careers.example/jobs/22222"}]}
        with patch.object(coverage_reconcile, "_load_store_entries", return_value=({}, entries)), patch.object(
            coverage_reconcile, "read_source_snapshot_payload", return_value=snapshot,
        ):
            scoped = coverage_reconcile.board_scope(now)
        self.assertEqual(1, len(scoped))
        self.assertFalse(scoped[0]["official_url"])
        self.assertEqual("https://careers.example/jobs/22222", scoped[0]["application_url"])

        entries[-1]["official_url"] = "https://jobs.uber.com/en/jobs/302349"
        snapshot["jobs"][0]["application_url"] = "https://click.appcast.io/track/29893004?cs=71665"
        with patch.object(coverage_reconcile, "_load_store_entries", return_value=({}, entries)), patch.object(
            coverage_reconcile, "read_source_snapshot_payload", return_value=snapshot,
        ):
            scoped = coverage_reconcile.board_scope(now)
        self.assertEqual("https://jobs.uber.com/en/jobs/302349", scoped[0]["official_url"])

    def test_exact_official_match_suppresses_regardless_of_manual_validation(self) -> None:
        external = make_job(
            source="linkedin",
            company="Example Tech",
            title="Machine Learning Engineer",
            location="Seattle, WA",
            job_id="10003",
            source_url="https://www.linkedin.com/jobs/view/10003",
        )
        external["requisition_id"] = "10003"
        coverage_reconcile.annotate_jobs([external], "board", context("validated"))
        self.assertEqual("official_duplicate", external["coverage_status"])
        self.assertTrue(external["suppress_alert"])
        self.assertEqual("official", external["canonical_source"])

        other = dict(external)
        coverage_reconcile.annotate_jobs([other], "board", context("unvalidated"))
        self.assertEqual("official_duplicate", other["coverage_status"])
        self.assertTrue(other["suppress_alert"])

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
        self.assertTrue(coverage_reconcile.locations_compatible(
            normalize_location_key("New York, NY"),
            normalize_location_key("San Francisco, CA • New York, NY • United States"),
        ))
        self.assertTrue(coverage_reconcile.locations_compatible(
            normalize_location_key("Reston, VA"), normalize_location_key("USA.VA.Reston")
        ))
        self.assertTrue(coverage_reconcile.locations_compatible(
            normalize_location_key("Seattle, WA"), normalize_location_key("US")
        ))
        self.assertTrue(coverage_reconcile.locations_compatible(
            normalize_location_key("Seattle, WA"),
            normalize_location_key("San Francisco, CA; Seattle; Remote, United States"),
        ))
        self.assertEqual("bellevue|wa", normalize_location_key("US-WA-Bellevue"))
        self.assertEqual("ca|san jose", normalize_location_key("San Jose (CA)"))
        self.assertEqual(
            normalize_location_key("Research Triangle Park, NC"), normalize_location_key("RTP, North Carolina")
        )
        self.assertTrue(coverage_reconcile.locations_compatible(
            normalize_location_key("Seattle, WA"), normalize_location_key("Washington - Seattle Campus")
        ))
        self.assertTrue(coverage_reconcile.locations_compatible(
            normalize_location_key("Houston, TX"), normalize_location_key("United States - TX Houston")
        ))
        self.assertEqual(normalize_location_key("McLean, VA"), normalize_location_key("Mc Lean, VA"))
        self.assertEqual("lausanne|switzerland", normalize_location_key("Lausanne, Switzerland"))
        self.assertEqual("san francisco", normalize_location_key("San Francisco Bay Area"))
        self.assertEqual("new york", normalize_location_key("New York Privy HQ"))
        self.assertEqual("new york", normalize_location_key("New York HQ"))

    def test_unique_remote_title_can_match_geo_targeted_external_rows(self) -> None:
        official = official_job("21001", "Forward Deployed Engineer (Remote)", "Austin, TX, US")
        method, matched = coverage_reconcile.exact_match(
            {"title": "Forward Deployed Engineer (Remote)", "location": "Denver, CO"},
            [official],
        )
        self.assertEqual("title_location", method)
        self.assertEqual("21001", matched["job_id"])

        method, matched = coverage_reconcile.exact_match(
            {"title": "Remote Sensing Engineer", "location": "Denver, CO"},
            [official_job("21002", "Remote Sensing Engineer", "Austin, TX")],
        )
        self.assertEqual("", method)
        self.assertIsNone(matched)

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

        external = make_job(
            source="linkedin", company="Example Tech", title="Software Development Engineer",
            location="San Jose, CA", source_url="https://linkedin.test/ambiguous",
        )
        ctx = context("validated")
        ctx["by_company"]["example"] = jobs
        coverage_reconcile.annotate_jobs([external], "board", ctx)
        self.assertEqual("official_ambiguous", external["coverage_status"])
        self.assertEqual(2, external["coverage_candidate_count"])
        self.assertFalse(external["suppress_alert"])

    def test_official_url_propagation_requires_unique_evidence(self) -> None:
        peers = [
            official_job("30001", "Software Engineer", "Seattle, WA"),
            official_job("30002", "Software Engineer", "Seattle, WA"),
        ]
        ambiguous = make_job(
            source="linkedin", company="Example Tech", title="Software Engineer",
            location="Seattle, WA", job_id="linkedin-1",
        )
        direct = {**ambiguous, "job_id": "indeed-1", "source": "indeed", "application_url": "https://apply.test/redirect"}
        board_pipeline.verify_official([*peers, ambiguous, direct])
        self.assertFalse(ambiguous["official_url"])
        self.assertFalse(direct["official_url"])

    def test_rich_ambiguous_job_resolves_canonical_application_redirect(self) -> None:
        job = make_job(
            source="indeed", company="Example Tech", title="Software Engineer",
            location="Seattle, WA", job_id="indeed-1", description="x" * 250,
        )
        job.update(
            application_url="https://contacthr.com/track/123456",
            coverage_status="official_ambiguous",
        )
        response = Mock(
            status_code=200,
            url="https://careers.example.com/jobs/30001",
            text="<html></html>",
        )
        session = Mock()
        session.get.return_value = response
        stats = board_pipeline.resolve_exposed_originals([job], session, {})
        self.assertEqual("https://careers.example.com/jobs/30001", job["official_url"])
        self.assertTrue(job["direct_original_fetched"])
        self.assertEqual(1, stats["identities_resolved"])

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
        self.assertEqual(
            ["official_duplicate", "official_duplicate", "official_identity_unmatched"],
            [j["coverage_status"] for j in external],
        )
        self.assertEqual("unvalidated", ctx["config"]["example"]["status"])

    def test_linkedin_indeed_overlap_reports_exact_unique_query_contribution(self) -> None:
        jobs = [
            make_job(source="linkedin", company="Example", title="Software Engineer", location="Austin, TX"),
            make_job(source="linkedin", company="LinkedIn Only", title="AI Engineer", location="Seattle, WA"),
            make_job(source="indeed", company="Example", title="Software Engineer", location="Austin, TX"),
            make_job(source="indeed", company="Indeed Only", title="ML Engineer", location="Boston, MA"),
        ]
        for job, query in zip(jobs, ("software engineer", "ai engineer", "software engineer", "ai engineer")):
            job["discovery_queries"] = {job["source"]: [query]}
        report = board_pipeline.local_source_coverage(jobs)
        self.assertEqual(1, report["overlap"])
        self.assertEqual(1, report["sources"]["linkedin"]["unique_contribution"])
        self.assertEqual(1, report["sources"]["indeed"]["unique_contribution"])
        self.assertEqual(1, report["queries"]["indeed"]["ai engineer"]["cross_source_unique"])

    def test_overlap_prefers_employer_url_and_falls_back_only_without_one(self) -> None:
        common = {"company": "Example", "title": "Engineer", "location": "Austin, TX"}
        linkedin = dict(common, source="linkedin", official_url="https://jobs.example.com/123?utm_source=linkedin")
        indeed = dict(source="indeed", company="Different", title="Different", location="Remote",
                      official_url="https://indeed.com/viewjob?jk=1",
                      application_url="https://jobs.example.com/123")
        for job in (linkedin, indeed):
            job["discovery_queries"] = {job["source"]: ["engineer"]}
        report = board_pipeline.local_source_coverage([linkedin, indeed])
        self.assertEqual(1, report["overlap"])
        self.assertEqual(1, report["queries"]["indeed"]["engineer"]["cross_source_overlap"])
        other_url = dict(common, source="indeed", official_url="https://jobs.example.com/456")
        self.assertEqual(0, board_pipeline.local_source_coverage([linkedin, other_url])["overlap"])
        for unusable in ("", "not a URL", "/jobs/123", "https://[broken", "mailto:jobs@example.com", "https://www.linkedin.com/jobs/123"):
            with self.subTest(url=unusable):
                fallback = dict(common, source="linkedin", official_url=unusable)
                no_url = dict(common, source="indeed")
                self.assertEqual(1, board_pipeline.local_source_coverage([fallback, no_url])["overlap"])
                self.assertEqual(0, board_pipeline.local_source_coverage([linkedin, no_url])["overlap"])

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


class ComplementaryDiscoveryTests(unittest.TestCase):
    def test_official_digest_and_fresh_exclude_historical_c_to_b(self) -> None:
        now = datetime.now(timezone.utc)
        old_c = official_job("old-c", "Software Engineer I", "Seattle, WA")
        new_b = official_job("new-b", "Software Engineer I", "Seattle, WA")
        promoted = official_job("promoted", "Software Engineer I", "Seattle, WA")
        carried = official_job("carried", "Software Engineer I", "Seattle, WA")
        for job in (old_c, new_b, promoted, carried):
            job.update(
                canonical_job_key=dedup_key(job), source_pipeline="official",
                tier="B", match_score=75,
            )
        promoted["tier"] = "A"
        promoted["match_score"] = 90
        old_seen = (now - timedelta(days=3)).isoformat()
        recent_seen = (now - timedelta(hours=9)).isoformat()
        for job in (old_c, promoted):
            job["first_seen"] = old_seen
        for job in (new_b, carried):
            job["first_seen"] = recent_seen
        previous = {
            dedup_key(old_c): {"tier": "C", "first_seen": old_seen},
            dedup_key(promoted): {"tier": "B", "first_seen": old_seen},
            dedup_key(carried): {"tier": "B", "first_seen": recent_seen},
        }
        eligible = official_careers.digest_new_keys({dedup_key(new_b)}, previous, now)
        self.assertNotIn(dedup_key(old_c), eligible)
        self.assertIn(dedup_key(carried), eligible)
        self.assertEqual(1, official_careers.count_new_jobs_added(
            [old_c, new_b, promoted, carried], {dedup_key(new_b)},
        ))
        state = {
            "last_digest_date": "", "alerted_keys": [dedup_key(promoted)],
            "alerted_tier": {dedup_key(promoted): "B"},
        }
        digest, emit, _ = board_pipeline.decide_digest(
            [old_c, new_b, promoted, carried], state, eligible_new_keys=eligible,
        )
        self.assertTrue(emit)
        self.assertEqual(
            {dedup_key(new_b), dedup_key(promoted), dedup_key(carried)},
            {dedup_key(job) for job in digest},
        )

        rows = [dict(
            canonical_job_key=dedup_key(job), pipeline="official", tier=job["tier"],
            company=job["company"], title=job["title"], location=job["location"],
            url=job["official_url"], filter_status="kept", score=job["match_score"],
            freshness=dashboard.recency(job, now),
        ) for job in (old_c, new_b, promoted, carried)]
        with patch.object(dashboard.alert_history, "recent_events", side_effect=lambda path, *args, **kwargs: [{
            "emitted_at": now.isoformat(),
            "jobs": [{"canonical_job_key": dedup_key(job)} for job in digest],
        }] if path == dashboard.ALERT_HISTORY_PATHS["official"] else []), patch.object(
            dashboard, "parse_issue_event", return_value=None
        ):
            fresh, _ = dashboard.alert_fresh_rows(rows, now)
        self.assertEqual(
            {dedup_key(new_b), dedup_key(promoted), dedup_key(carried)},
            {row["canonical_job_key"] for row in fresh},
        )

    def test_official_and_syncareer_added_counts_only_include_new_visible_jobs(self) -> None:
        official_new = make_job(
            source="google_official_careers", company="Google", title="Software Engineer I",
            location="Mountain View, CA", job_id="new",
        )
        official_known = make_job(
            source="google_official_careers", company="Google", title="Data Engineer",
            location="Seattle, WA", job_id="known",
        )
        self.assertEqual(
            1,
            official_careers.count_new_jobs_added(
                [official_new, official_known], {dedup_key(official_new)},
            ),
        )
        self.assertEqual(
            1,
            daily_pipeline.count_new_jobs_added(
                [{"job_id": "new"}, {"job_id": "known"}], ["new"],
            ),
        )

    def test_official_reconciliation_reads_compressed_raw_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            raw = Path(tmpdir) / "raw.json.gz"
            payload = {"scraped_at": "2026-09-05T00:00:00+00:00", "jobs": [], "scraped_company_ids": ["example"]}
            raw.write_bytes(gzip.compress(json.dumps(payload).encode()))
            with patch.object(coverage_reconcile, "OFFICIAL_RAW_PATH", raw), patch.object(
                coverage_reconcile, "LEGACY_OFFICIAL_RAW_PATH", Path(tmpdir) / "missing-legacy.gz"
            ), patch.object(
                coverage_reconcile, "OFFICIAL_STORE_PATH", Path(tmpdir) / "missing-store.json"
            ), patch.object(
                coverage_reconcile, "load_registry_entries", return_value=([], {})
            ), patch.object(coverage_reconcile, "load_coverage_config", return_value={}):
                context = coverage_reconcile.load_official_context()
        self.assertEqual({"example"}, context["scraped_company_ids"])

    def test_official_reconciliation_uses_newest_snapshot_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            raw = root / "raw.json.gz"
            raw.write_bytes(gzip.compress(json.dumps({
                "scraped_at": "2026-09-04T00:00:00+00:00", "jobs": [],
                "scraped_company_ids": ["stale"],
            }).encode()))
            store = root / "jobs.json"
            store.write_text(json.dumps({
                "scraped_at": "2026-09-05T00:00:00+00:00", "entries": [],
                "scraped_company_ids": ["fresh"],
            }))
            with patch.object(coverage_reconcile, "OFFICIAL_RAW_PATH", raw), patch.object(
                coverage_reconcile, "LEGACY_OFFICIAL_RAW_PATH", root / "missing-legacy.gz"
            ), patch.object(coverage_reconcile, "OFFICIAL_STORE_PATH", store), patch.object(
                coverage_reconcile, "load_registry_entries", return_value=([], {})
            ), patch.object(coverage_reconcile, "load_coverage_config", return_value={}):
                loaded = coverage_reconcile.load_official_context()
        self.assertEqual("published_store", loaded["coverage_source"])
        self.assertEqual({"fresh"}, loaded["scraped_company_ids"])

    def test_official_reconciliation_uses_compact_remote_index_without_raw_cache(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            store = root / "jobs.json"
            store.write_text(json.dumps({
                "scraped_at": "2026-09-05T00:00:00+00:00",
                "scraped_company_ids": ["example"],
                "coverage_fields": ["company", "title", "location", "job_id", "official_url", "source"],
                "coverage_entries": [["Example Tech", "Software Engineer I", "Seattle, WA", "10001", "https://example.test/jobs/10001", "official"]],
                "entries": [],
            }))
            expected_context = context()
            with patch.object(coverage_reconcile, "OFFICIAL_RAW_PATH", root / "missing-cache.gz"), patch.object(
                coverage_reconcile, "LEGACY_OFFICIAL_RAW_PATH", root / "missing-legacy.gz"
            ), patch.object(coverage_reconcile, "OFFICIAL_STORE_PATH", store), patch.object(
                coverage_reconcile,
                "load_registry_entries",
                return_value=(expected_context["registry_entries"], expected_context["registry_by_id"]),
            ):
                loaded = coverage_reconcile.load_official_context()
        self.assertEqual({"example"}, loaded["scraped_company_ids"])
        self.assertEqual("10001", loaded["jobs"][0]["job_id"])

    def test_board_does_not_collect_legacy_official_source(self) -> None:
        session = Mock()
        session.get.side_effect = AssertionError("unexpected direct collection")
        session.post.side_effect = AssertionError("unexpected direct collection")
        ats_result = {"jobs": [make_job(source="greenhouse", company="SmallCo", title="Software Engineer I")], "per_board": {}, "errors": []}
        with patch.object(board_pipeline.ats, "fetch_all_ats", return_value=ats_result), patch.object(
            board_pipeline, "read_source_snapshot_payload", return_value={"jobs": [], "meta": {}}
        ):
            jobs, meta = board_pipeline.collect_sources(session, skip_network=False)
        self.assertEqual(["greenhouse"], [job["source"] for job in jobs])
        self.assertEqual([], meta["errors"])
        self.assertEqual([], session.mock_calls)

    def test_linkedin_search_focuses_two_titles_at_entry_and_associate_levels(self) -> None:
        self.assertEqual("2,3", linkedin_local.EXPERIENCE_LEVEL_FILTER)
        self.assertEqual(["software engineer", "ai engineer"], linkedin_local.DEFAULT_KEYWORDS)
        self.assertEqual([5, 3], [spec[2] for spec in linkedin_local.SEARCH_SPECS])
        self.assertEqual(8, linkedin_local.SEARCH_PAGE_LIMIT)
        self.assertEqual({"primary": 3, "secondary": 1, "specialty": 1}, local_search.SOURCE_PAGE_BUDGETS["indeed"])
        self.assertEqual({"primary": 1, "secondary": 1, "specialty": 1}, local_search.SOURCE_PAGE_BUDGETS["glassdoor"])
        self.assertNotIn("Applied Scientist", daily_pipeline.SEARCH_KEYWORDS)

    def test_original_hydration_keeps_aggregator_date_auditable(self) -> None:
        card = make_job(
            source="linkedin", company="Example Tech", title="Software Engineer",
            location="Austin, TX", job_id="li-1", posted_date="2026-09-04",
        )
        original = make_job(
            source="greenhouse", company="Example Tech", title="Software Engineer II",
            location="Austin, Texas", job_id="gh-1", posted_date="2026-09-01",
            updated_date="2026-09-03", official_url="https://example.test/jobs/gh-1",
            description="Complete employer job description",
        )
        coverage_reconcile.hydrate_from_original(card, original)
        self.assertEqual("2026-09-04", card["aggregator_posted_date"])
        self.assertEqual("2026-09-01", card["posted_date"])
        self.assertEqual("2026-09-03", card["updated_date"])
        self.assertEqual(original["official_url"], card["official_url"])
        self.assertEqual(original["description"], card["description"])

    def test_temporal_fields_survive_merge_enrichment_and_store_round_trip(self) -> None:
        first_seen = "2026-09-01T12:00:00+00:00"
        key = "id::greenhouse::job-1"
        prior = make_job(
            source="greenhouse", company="Example Tech", title="Software Engineer",
            location="Austin, TX", job_id="job-1", posted_date="2026-08-30",
            date_confidence="medium",
        )
        prior.update(key=key, first_seen=first_seen)
        current = make_job(
            source="greenhouse", company="Example Tech", title="Software Engineer",
            location="Austin, TX", job_id="job-1", posted_date="",
        )
        current["first_seen"] = "2026-09-03T12:00:00+00:00"
        seen = {key: first_seen}

        self.assertEqual([], board_pipeline.finalize_new_jobs(
            [current], {key: prior}, seen, "2026-09-03T12:00:00+00:00"
        ))
        self.assertEqual(first_seen, current["first_seen"])
        self.assertEqual("2026-08-30", current["posted_date"])
        merged = board_pipeline._merge_pair(current, {
            **current, "first_seen": "2026-08-31T12:00:00+00:00",
        })
        self.assertEqual(first_seen, merged["first_seen"])

        official = make_job(
            source="example_official_careers", company="Example Tech",
            title="Software Engineer", location="Austin, TX", job_id="job-1",
            posted_date="2026-08-29", date_confidence="high",
        )
        coverage_reconcile.hydrate_from_original(current, official)
        self.assertEqual("2026-08-29", current["posted_date"])
        lower_quality = make_job(
            source="linkedin", company="Example Tech", title="Software Engineer",
            location="Austin, TX", job_id="job-1", posted_date="2026-09-02",
            date_confidence="low",
        )
        coverage_reconcile.hydrate_from_original(current, lower_quality)
        self.assertEqual("2026-08-29", current["posted_date"])

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "jobs.json"
            entry = board_pipeline.build_store_entry(current, key, prior)
            board_pipeline.save_store_path(path, {key: entry}, 7)
            stored = board_pipeline.load_store_path(path, strict=True)[key]
        self.assertEqual(first_seen, stored["first_seen"])
        self.assertEqual("2026-08-29", stored["posted_date"])

        missing_again = make_job(
            source="greenhouse", company="Example Tech", title="Software Engineer",
            location="Austin, TX", job_id="job-1", posted_date="",
        )
        board_pipeline.finalize_new_jobs(
            [missing_again], {key: stored}, seen, "2026-09-04T12:00:00+00:00"
        )
        self.assertEqual(first_seen, missing_again["first_seen"])
        self.assertEqual("2026-08-29", missing_again["posted_date"])

    def test_source_snapshots_do_not_erase_temporal_history(self) -> None:
        first_seen = "2026-09-01T12:00:00+00:00"
        prior = make_job(
            source="linkedin", company="Example Tech", title="Software Engineer",
            location="Austin, TX", job_id="job-1", posted_date="2026-08-30",
            date_confidence="low",
        )
        prior["first_seen"] = first_seen
        degraded = make_job(
            source="linkedin", company="Example Tech", title="Software Engineer",
            location="Austin, TX", job_id="job-1", posted_date="",
        )
        result = {
            "company": "Example Tech", "company_id": "example", "jobs": [prior],
            "errors": [],
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            with patch.object(schema, "SOURCES_DIR", root / "sources"):
                schema.write_source_snapshot("linkedin", [prior])
                schema.write_source_snapshot("linkedin", [degraded])
                saved = schema.read_source_snapshot_payload("linkedin")["jobs"][0]
            self.assertEqual(first_seen, saved["first_seen"])
            self.assertEqual("2026-08-30", saved["posted_date"])

            raw = root / "raw.json.gz"
            report = root / "report.md"
            with patch.object(official_careers, "RAW_PATH", raw), patch.object(
                official_careers, "REPORT_PATH", report
            ), patch.object(official_careers, "CAREERS_DIR", root):
                official_careers.write_scrape_outputs([result], "first", merge_previous=False)
                result["jobs"] = [degraded]
                official_careers.write_scrape_outputs([result], "second")
                saved = official_careers.load_raw_jobs()[0]
            self.assertEqual(first_seen, saved["first_seen"])
            self.assertEqual("2026-08-30", saved["posted_date"])

    def test_relevant_engineering_titles_survive_positive_family_gate(self) -> None:
        for title in (
            "AI Solutions Engineer",
            "Computer Vision Engineer",
            "Solutions Integration Engineer II",
            "AI Automation Engineer",
            "Product Engineer",
            "ETL Engineer",
        ):
            job = make_job(source="linkedin", company="SmallCo", title=title, location="Austin, TX")
            keep, reason = board_pipeline.role_seniority_prefilter(job)
            self.assertTrue(keep, (title, reason))

    def test_amazon_and_apple_are_hidden_only_on_external_surfaces(self) -> None:
        filters = board_pipeline.load_company_filters()
        self.assertEqual("Amazon", board_pipeline.hidden_external_company("Amazon Web Services", filters))
        self.assertEqual("Apple", board_pipeline.hidden_external_company("Apple Inc.", filters))
        self.assertIsNone(board_pipeline.hidden_external_company("Pineapple Labs", filters))
        row = {"company": "Apple", "title": "Software Engineer I"}
        self.assertTrue(daily_pipeline.apply_external_company_policy(row, filters))
        self.assertTrue(row["suppress_alert"])

    def test_syncareer_rule_fallback_persists_shared_score_and_tier(self) -> None:
        now = datetime.now(timezone.utc)
        row = {
            "job_id": "sync-1",
            "company": "SmallCo",
            "title": "New Grad Data Engineer",
            "location": "Austin, TX",
            "posting_date": now.strftime("%Y-%m-%d"),
            "job_url": "https://small.example/jobs/sync-1",
            "description": "Build data platforms and backend software.",
            "requirements": "Bachelor degree and Python.",
            "first_seen": now.isoformat(),
            "target_company_match": "",
        }
        decisions, counts, errors, _method = daily_pipeline.assign_shared_scores(
            [row], {}, use_llm=False
        )
        decision = decisions["sync-1"]
        self.assertGreaterEqual(float(decision["match_score"]), 0)
        self.assertLessEqual(float(decision["match_score"]), 100)
        self.assertIn(decision["tier"], {"A", "B", "C"})
        self.assertTrue(decision["score_source"])
        self.assertEqual(1, counts["rule"])
        self.assertEqual([], errors)

    def test_syncareer_run_persists_real_rule_scores_without_alerting_tier_c(self) -> None:
        row = {
            "job_id": "sync-1",
            "company": "SmallCo",
            "title": "Software Engineer I",
            "location": "Austin, TX",
            "posting_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "job_url": "https://small.example/jobs/sync-1",
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            syncareer_dir = root / "syncareer"
            with ExitStack() as stack:
                stack.enter_context(patch("sys.argv", ["daily_pipeline.py", "--alert", "--time", "last3days", "--no-llm"]))
                stack.enter_context(patch.object(daily_pipeline, "DAILY_DIR", root / "daily"))
                stack.enter_context(patch.object(daily_pipeline, "SYNCAREER_DIR", syncareer_dir))
                stack.enter_context(patch.object(daily_pipeline, "RUNS_DIR", syncareer_dir / "runs"))
                stack.enter_context(patch.object(daily_pipeline, "WATCHLIST_PATH", syncareer_dir / "watchlist.json"))
                stack.enter_context(patch.object(daily_pipeline, "SEEN_IDS_PATH", syncareer_dir / "seen_jobs.json"))
                stack.enter_context(patch.object(daily_pipeline, "LEGACY_SEEN_IDS_PATH", root / "legacy_seen_jobs.json"))
                stack.enter_context(patch.object(daily_pipeline, "ALERT_HISTORY_PATH", syncareer_dir / "alert_history.json"))
                stack.enter_context(patch.object(daily_pipeline, "LEGACY_WATCHLIST_PATH", root / "legacy_watchlist.json"))
                stack.enter_context(patch.object(daily_pipeline.board, "load_env_file"))
                stack.enter_context(patch.object(daily_pipeline.board, "make_session", return_value=object()))
                stack.enter_context(patch.object(daily_pipeline, "load_target_companies", return_value=[]))
                stack.enter_context(patch.object(daily_pipeline.board, "load_company_filters", return_value={}))
                stack.enter_context(patch.object(
                    daily_pipeline,
                    "run_search",
                    return_value=(
                        {"sync-1": {}}, {"sync-1": ["software engineer"]},
                        {"software engineer": 1},
                        [local_search.query_stat("software engineer", "syncareer", 1)],
                    ),
                ))
                fetch_detail = stack.enter_context(patch.object(daily_pipeline, "fetch_job_detail", return_value={}))
                stack.enter_context(patch.object(daily_pipeline, "normalize_job_row", return_value=row))
                stack.enter_context(patch.object(daily_pipeline, "hard_filter", return_value=(True, "keep")))
                stack.enter_context(patch.object(daily_pipeline.coverage_reconcile, "syncareer_job_in_scope", return_value=True))
                stack.enter_context(patch.object(daily_pipeline.coverage_reconcile, "annotate_jobs"))
                stack.enter_context(patch.object(daily_pipeline, "apply_external_company_policy", return_value=False))
                stack.enter_context(patch.object(board_pipeline, "load_store_path", return_value={}))
                stack.enter_context(patch("requests.post", side_effect=AssertionError("no LLM calls in rule mode")))
                stack.enter_context(patch.object(daily_pipeline.time, "sleep"))
                stack.enter_context(patch.object(daily_pipeline.board, "emit_github_output"))
                daily_pipeline.run()
                first_stats = json.loads(next((syncareer_dir / "runs").glob("*_stats.json")).read_text())
                first_store = daily_pipeline.load_watchlist()
                first_store["sync-1"]["review_status"] = "applied"
                first_store["sync-1"]["notes"] = "Keep on repeated runs"
                daily_pipeline.save_watchlist(first_store)
                row.update(posting_date="", posted_date="", date_confidence="unknown")
                daily_pipeline.run()
                self.assertEqual(2, fetch_detail.call_count)  # thin known rows retry enrichment
                second_store = daily_pipeline.load_watchlist()
                for field in (
                    "first_seen", "posted_date", "date_confidence", "match_score",
                    "tier", "review_status", "notes",
                ):
                    self.assertEqual(first_store["sync-1"][field], second_store["sync-1"][field])

            stats_paths = list((syncareer_dir / "runs").glob("*_stats.json"))
            self.assertTrue(stats_paths)
            stats = first_stats
            self.assertEqual({"scoring_candidates": 1}, stats["funnel"])
            self.assertEqual(1, stats["llm"]["rule"])
            self.assertEqual(0, stats["llm"]["scored"])
            self.assertEqual(
                {
                    "tier_a": 0, "tier_b": 0, "tier_c": 1, "shown": 0,
                    "new_jobs": 1, "new_jobs_added": 0,
                },
                stats["output"],
            )
            self.assertEqual("rule", stats["screen_method"])
            self.assertGreaterEqual(
                json.loads((syncareer_dir / "latest_stats.json").read_text())["run_at"], stats["run_at"]
            )
            stored = json.loads((syncareer_dir / "watchlist.json").read_text())["entries"]
            self.assertEqual(1, len(stored))
            self.assertEqual("C", stored[0]["tier"])
            self.assertEqual("rule", stored[0]["score_source"])
            self.assertEqual(65, stored[0]["match_score"])
            self.assertEqual("sync-1", stored[0]["job_id"])
            self.assertTrue(stored[0]["first_seen"])
            self.assertIn("0 new jobs", (syncareer_dir / "issue_body.md").read_text())
            self.assertNotIn("SmallCo", (syncareer_dir / "inbox.md").read_text())

    def test_syncareer_source_dates_accept_epochs_and_reject_invalid_values(self) -> None:
        stamp = datetime(2026, 9, 1, tzinfo=timezone.utc).timestamp()
        for value in (stamp, stamp * 1000, str(int(stamp)), "2026-09-01T00:00:00Z"):
            with self.subTest(value=value):
                row = daily_pipeline.normalize_job_row({"publishAt": value}, {}, [], [])
                self.assertEqual("2026-09-01", row["posting_date"])
        for value in (None, -1, float("inf"), float("nan"), 1e100, "invalid"):
            with self.subTest(value=value):
                row = daily_pipeline.normalize_job_row({"publishAt": value}, {}, [], [])
                self.assertEqual("", row["posting_date"])

    def test_syncareer_retention_preserves_legacy_dates_and_unknown_age(self) -> None:
        now = datetime(2026, 9, 7, tzinfo=timezone.utc)
        rows = {
            "boundary": {"first_seen": "2026-08-31"},
            "offset": {"first_seen": "2026-08-30T17:00:00-07:00"},
            "old": {"first_seen": "2026-08-30T23:59:59Z"},
            "fallback": {"first_seen": None, "posted_date": "2026-09-01"},
            "unknown": {"first_seen": 123},
        }
        kept = daily_pipeline.prune_watchlist(rows, now=now)
        self.assertEqual({"boundary", "offset", "fallback", "unknown"}, set(kept))
        self.assertEqual(rows["offset"], kept["offset"])

    def test_syncareer_rolling_activity_prefers_first_seen(self) -> None:
        now = datetime.now(timezone.utc)
        entry = {
            "first_seen": (now - timedelta(hours=2)).isoformat(),
            "posting_date": (now - timedelta(days=20)).strftime("%Y-%m-%d"),
        }
        self.assertGreater(daily_pipeline._entry_age_ref(entry), now - timedelta(days=1))

    def test_thin_linkedin_card_uses_rules_not_llm(self) -> None:
        now = datetime.now(timezone.utc)
        job = make_job(
            source="linkedin", company="SmallCo", title="Software Engineer II",
            location="Austin, TX", job_id="li-1", description="",
            source_url="https://linkedin.com/jobs/view/li-1",
        )
        job["first_seen"] = now.isoformat()
        board_pipeline.role_seniority_prefilter(job)
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}), patch.object(
            board_pipeline, "llm_match_batch", side_effect=AssertionError("LLM must not run")
        ):
            _method, errors, counts = board_pipeline.score_survivors(
                [job], {}, board_pipeline.load_profiles(), {}, use_llm=True
            )
        self.assertEqual(board_pipeline.SCORE_FALLBACK, job["score_source"])
        self.assertEqual(1, counts["thin_source_rule"])
        self.assertEqual(0, counts["api_requests"])
        self.assertEqual([], errors)

    def test_retained_title_only_llm_score_is_replaced_by_current_rule_policy(self) -> None:
        now = datetime.now(timezone.utc)
        entry = make_job(
            source="linkedin", company="SmallCo", title="Software Engineer II",
            location="Austin, TX", job_id="li-old", description="",
            source_url="https://linkedin.com/jobs/view/li-old",
        )
        entry.update({
            "first_seen": now.isoformat(), "recency_bucket": "newly_discovered",
            "match_score": 94, "tier": "A", "score_source": "llm",
            "screen_method": "llm", "filter_status": "kept",
        })
        board_pipeline.refresh_retained_entry_policy(
            entry, board_pipeline.load_company_filters()
        )
        self.assertEqual(board_pipeline.SCORE_FALLBACK, entry["score_source"])
        self.assertLess(float(entry["match_score"]), 94)
        self.assertNotEqual("A", entry["tier"])



class ReportingWorkflowTests(unittest.TestCase):
    def test_generated_issue_body_has_no_owner_cc(self) -> None:
        body = daily_pipeline.build_issue_body([], "2026-08-28_1200", False).lower()
        self.assertNotIn("cc @daniel-li2021", body)
        self.assertNotIn("cc @daniel-li2021", (ROOT / "board_pipeline.py").read_text(encoding="utf-8").lower())
        self.assertNotIn("cc @daniel-li2021", (ROOT / "official_careers.py").read_text(encoding="utf-8").lower())

    def test_workflows_are_independent_externally_scheduled_and_pages_enabled(self) -> None:
        board = (ROOT / ".github/workflows/board-jobs.yml").read_text(encoding="utf-8")
        official = (ROOT / ".github/workflows/official-careers.yml").read_text(encoding="utf-8")
        syncareer = (ROOT / ".github/workflows/daily-jobs.yml").read_text(encoding="utf-8")
        pages = (ROOT / ".github/workflows/reconcile-pages.yml").read_text(encoding="utf-8")
        for workflow in (board, official, syncareer, pages):
            self.assertNotIn("schedule:", workflow)
            self.assertNotIn("cron:", workflow)
        self.assertNotRegex(official, r"git add[^\n]*output/alerts")
        self.assertIn("workflow_dispatch:", board)
        self.assertIn("actions: write", board)
        self.assertIn("gh workflow run reconcile-pages.yml --ref main", board)
        self.assertIn("workflow_dispatch:", official)
        self.assertIn("workflow_dispatch:", syncareer)
        self.assertIn("OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}", syncareer)
        self.assertNotIn("--no-llm", syncareer)
        for workflow in (board, official, syncareer):
            self.assertIn("for attempt in 1 2 3", workflow)
            self.assertIn('git rebase "origin/${GITHUB_REF_NAME}"', workflow)
            self.assertNotIn('git pull --rebase --autostash origin "${GITHUB_REF_NAME}" || true', workflow)
        self.assertIn("actions/deploy-pages@v4", pages)
        self.assertIn("concurrency:", pages)
        self.assertIn("contents: write", pages)
        self.assertIn('".github/workflows/reconcile-pages.yml"', pages)
        self.assertIn('workflows: ["Official careers", "Syncareer job alert"]', pages)
        self.assertNotIn('"Board job alert"', pages)
        self.assertIn("git add -- profile/company_profiles_pending.json", pages)
        self.assertIn("git push origin HEAD:main", pages)
        self.assertIn("git stash push --include-untracked --message pending-company-generated-files", pages)
        self.assertLess(pages.index("Deploy GitHub Pages"), pages.index("Persist pending company profiles"))
        self.assertNotIn("git add -A", pages)
        self.assertNotIn('"profile/review_state.json"', pages)
        self.assertFalse((ROOT / ".github/workflows/scheduled-jobs.yml").exists())
        self.assertIn('f"{PAGES_URL}coverage.md"', (ROOT / "dashboard.py").read_text(encoding="utf-8"))

    def test_supabase_schema_allows_public_read_and_write(self) -> None:
        sql = (ROOT / "supabase" / "job_review_setup.sql").read_text(encoding="utf-8")
        self.assertIn("to anon, authenticated\nusing (true)", sql)
        self.assertIn('create policy "Public can insert job review status"', sql)
        self.assertIn('create policy "Public can update job review status"', sql)
        self.assertIn("on table public.job_review_status to anon, authenticated", sql)
        self.assertIn("'unreviewed', 'in_progress', 'applied_complete'", sql)
        self.assertIn("if old.updated_at > new.updated_at then", sql)
        self.assertIn("create trigger keep_newest_job_review_status", sql)
        self.assertNotIn("for delete", sql.lower())


class RegistryCoverageTests(unittest.TestCase):
    def test_official_registry_is_structurally_complete(self) -> None:
        payload = json.loads((ROOT / "config" / "official_careers.json").read_text(encoding="utf-8"))
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
                "pcsx": "pcsx",
                "radancy": "radancy",
                "eightfold_html": "eightfold_html",
                "happydance": "happydance",
                "jibe": "jibe",
            }.get(adapter)
            if config_key:
                self.assertTrue(company.get(config_key), company["id"])
            if company.get("covered_by") == "ats":
                self.assertEqual("ats", adapter)
        self.assertEqual(len(urls), len(set(urls)))
        self.assertGreaterEqual(sum(company.get("adapter") != "skip" for company in companies), 70)

    def test_manual_unsupported_overrides_do_not_mask_active_adapters(self) -> None:
        registry = json.loads((ROOT / "config" / "official_careers.json").read_text(encoding="utf-8"))
        coverage = json.loads((ROOT / "profile" / "official_coverage.json").read_text(encoding="utf-8"))
        active = {company["id"] for company in registry["companies"] if company.get("adapter") != "skip"}
        stale = {
            company_id
            for company_id, config in coverage["companies"].items()
            if config.get("status") == "unsupported" and company_id in active
        }
        self.assertEqual(set(), stale)

    def test_ats_boards_have_official_cross_check_coverage(self) -> None:
        official = json.loads((ROOT / "config" / "official_careers.json").read_text(encoding="utf-8"))
        ats = json.loads((ROOT / "config" / "ats_boards.json").read_text(encoding="utf-8"))
        official_ids = {company["id"] for company in official["companies"]}
        ats_ids = {board["token"] for board in ats["boards"]}
        self.assertTrue(ats_ids.issubset(official_ids))

    def test_syncareer_search_is_keyword_based_without_company_restrictions(self) -> None:
        url = daily_pipeline.build_search_url("Software Engineer", "last3days", 2)
        self.assertEqual("/", urlsplit(url).path)
        self.assertEqual({"q": ["Software Engineer"], "loc": ["United States"], "time": ["last3days"], "exps": [daily_pipeline.EXPERIENCE_FILTER], "page": ["2"]}, parse_qs(urlsplit(url).query))

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

        registry = json.loads((ROOT / "config" / "official_careers.json").read_text(encoding="utf-8"))
        companies = {company["id"]: company for company in registry["companies"]}
        self.assertIn("core infrastructure", companies["oracle"]["oracle_hcm"]["extra_queries"])


if __name__ == "__main__":
    unittest.main()
