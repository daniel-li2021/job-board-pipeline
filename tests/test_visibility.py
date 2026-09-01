from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlsplit

import board_pipeline
import alert_history
import coverage_reconcile
import daily_pipeline
import dashboard
import review_state
from sources.company_aliases import load_alias_file, match_company_alias, prepare_alias_entries
from sources.schema import combined_cache_key_from_hash, dedup_key, make_job, normalize_job_url, normalize_location_key
from sources.schema import classify_location_bucket
from sources import linkedin_local
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


class ReferralAliasTests(unittest.TestCase):
    def test_single_alias_file_is_consistent_across_pipelines(self) -> None:
        targets = load_alias_file(ROOT / "source" / "target_companies.json")
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
        targets = load_alias_file(ROOT / "source" / "target_companies.json")
        self.assertIsNone(match_company_alias("Sapios", targets))
        self.assertIsNone(match_company_alias("Metadata Systems", targets))
        self.assertIsNone(match_company_alias("GE HealthCare", targets))


class DashboardPolicyTests(unittest.TestCase):
    def test_sponsorship_labels_use_existing_source_data(self) -> None:
        self.assertEqual("Sponsor", dashboard.sponsorship_label({"sponsorship": "H-1B Sponsor"}))
        self.assertEqual("No sponsor", dashboard.sponsorship_label({"sponsorship": "No H-1B Sponsor"}))
        self.assertEqual("Sponsor", dashboard.sponsorship_label({"description": "Visa sponsorship is available for this role."}))
        self.assertEqual("No sponsor", dashboard.sponsorship_label({"description": "We are unable to provide visa sponsorship."}))
        self.assertEqual("No sponsor", dashboard.sponsorship_label({"description": "Visa sponsorship is not available."}))
        self.assertEqual("Unknown", dashboard.sponsorship_label({"description": "Applicants may require sponsorship."}))
        self.assertEqual("Unknown", dashboard.sponsorship_label({}))
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

    def test_sort_is_tier_then_discovery_then_score(self) -> None:
        now = datetime(2026, 8, 29, 12, tzinfo=timezone.utc)

        def row(tier: str, score: int, age: int, company: str) -> dict:
            return {
                "tier": tier,
                "score": score,
                "company": company,
                "freshness": dashboard.recency(
                    {"first_seen": (now - timedelta(hours=age)).isoformat()}, now
                ),
            }

        ordered = dashboard._sort_rows([
            row("B", 99, 1, "B Co"),
            row("A", 85, 5, "A lower"),
            row("A", 92, 20, "A higher"),
        ])
        self.assertEqual(["A lower", "A higher", "B Co"], [item["company"] for item in ordered])

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

    def test_current_ats_issue_fallback_parses_current_alert_rows(self) -> None:
        event = dashboard.parse_issue_event(ROOT / "output" / "board" / "issue_body.md", "board")
        self.assertIsNotNone(event)
        self.assertRegex(event["stamp"], r"^\d{4}-\d{2}-\d{2}_\d{4}$")
        self.assertEqual(event["count"], len(event["jobs"]))
        self.assertGreater(len(event["jobs"]), 0)

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
            self.assertEqual("alert_history_or_issue", basis["official"])
            self.assertEqual(1, fresh[0]["activity_age_hours"])

    def test_public_template_has_compact_navigation_and_shared_status_control(self) -> None:
        self.assertNotIn("Official coverage", dashboard.HTML_TEMPLATE)
        self.assertNotIn("<th>Coverage</th>", dashboard.HTML_TEMPLATE)
        self.assertIn("status-select", dashboard.HTML_TEMPLATE)
        self.assertIn("document.getElementById('updated').textContent=D.updated_pt", dashboard.HTML_TEMPLATE)
        self.assertNotIn("Dashboard last updated:", dashboard.HTML_TEMPLATE)
        self.assertIn("companyTab.style.display=active==='official'?'flex':'none'", dashboard.HTML_TEMPLATE)
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
        self.assertIn("persist();renderReviewMessage();renderAll();pushState(next)", dashboard.HTML_TEMPLATE)
        self.assertNotIn("reviewStates[key]=previous", dashboard.HTML_TEMPLATE)
        self.assertNotIn("delete reviewStates[key]", dashboard.HTML_TEMPLATE)
        self.assertIn("<details class=\"panel\"><summary>Referral opportunities</summary>", dashboard.HTML_TEMPLATE)
        self.assertLess(dashboard.HTML_TEMPLATE.index('id="main-view-applied"'), dashboard.HTML_TEMPLATE.index("<h2>Deleted</h2>"))
        self.assertLess(dashboard.HTML_TEMPLATE.index("<h2>Deleted</h2>"), dashboard.HTML_TEMPLATE.index("Referral opportunities"))
        self.assertLess(dashboard.HTML_TEMPLATE.index("Referral opportunities"), dashboard.HTML_TEMPLATE.index("Official company search links"))
        self.assertIn("<th>Sponsorship</th>", dashboard.HTML_TEMPLATE)
        self.assertIn("'Amazon','Meta','TikTok'", dashboard.HTML_TEMPLATE)


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

    def test_validated_exact_suppresses_but_unvalidated_does_not(self) -> None:
        external = make_job(
            source="linkedin",
            company="Example Tech",
            title="Machine Learning Engineer",
            location="Seattle, WA",
            job_id="10003",
            source_url="https://www.linkedin.com/jobs/view/10003",
        )
        coverage_reconcile.annotate_jobs([external], "board", context("validated"))
        self.assertEqual("official_duplicate", external["coverage_status"])
        self.assertTrue(external["suppress_alert"])
        self.assertEqual("official", external["canonical_source"])

        other = dict(external)
        coverage_reconcile.annotate_jobs([other], "board", context("unvalidated"))
        self.assertEqual("covered_unvalidated", other["coverage_status"])
        self.assertFalse(other["suppress_alert"])

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
        self.assertEqual("lausanne|switzerland", normalize_location_key("Lausanne, Switzerland"))

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
        self.assertEqual(["covered_unvalidated", "covered_unvalidated", "official_gap"], [j["coverage_status"] for j in external])
        self.assertEqual("unvalidated", ctx["config"]["example"]["status"])

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
    def test_board_does_not_collect_legacy_official_source(self) -> None:
        ats_result = {"jobs": [make_job(source="greenhouse", company="SmallCo", title="Software Engineer I")], "per_board": {}, "errors": []}
        with patch.object(board_pipeline.ats, "fetch_all_ats", return_value=ats_result), patch.object(
            board_pipeline, "read_source_snapshot", return_value=[]
        ):
            jobs, _meta = board_pipeline.collect_sources(object(), skip_network=False)
        self.assertEqual(["greenhouse"], [job["source"] for job in jobs])
        self.assertNotIn("sources.official", (ROOT / "board_pipeline.py").read_text(encoding="utf-8"))

    def test_linkedin_search_covers_entry_and_associate_levels(self) -> None:
        self.assertEqual("2,3", linkedin_local.EXPERIENCE_LEVEL_FILTER)
        terms = {term.lower() for term in linkedin_local.DEFAULT_KEYWORDS}
        self.assertIn("software engineer i", terms)
        self.assertIn("software engineer ii", terms)
        self.assertIn("associate software engineer", terms)
        self.assertIn("forward deployed engineer", terms)

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

    def test_local_sync_targets_main_from_an_isolated_worktree(self) -> None:
        script = (ROOT / "scripts/local_source_sync.sh").read_text(encoding="utf-8")
        self.assertIn('TARGET_BRANCH="${TARGET_BRANCH:-main}"', script)
        self.assertIn("git worktree add --detach", script)
        self.assertIn('push origin "HEAD:${TARGET_BRANCH}"', script)


class ReportingWorkflowTests(unittest.TestCase):
    def test_generated_issue_body_has_no_owner_cc(self) -> None:
        body = daily_pipeline.build_issue_body([], "2026-08-28_1200", False).lower()
        self.assertNotIn("cc @daniel-li2021", body)
        self.assertNotIn("cc @daniel-li2021", (ROOT / "board_pipeline.py").read_text(encoding="utf-8").lower())
        self.assertNotIn("cc @daniel-li2021", (ROOT / "official_careers.py").read_text(encoding="utf-8").lower())

    def test_workflows_are_independent_staggered_and_pages_enabled(self) -> None:
        board = (ROOT / ".github/workflows/board-jobs.yml").read_text(encoding="utf-8")
        official = (ROOT / ".github/workflows/official-careers.yml").read_text(encoding="utf-8")
        syncareer = (ROOT / ".github/workflows/daily-jobs.yml").read_text(encoding="utf-8")
        pages = (ROOT / ".github/workflows/reconcile-pages.yml").read_text(encoding="utf-8")
        self.assertIn('cron: "7 8,17 * * *"', board)
        self.assertIn('cron: "30 8 * * *"', official)
        self.assertIn('cron: "20 17 * * *"', official)
        self.assertIn('cron: "10 8,17 * * *"', syncareer)
        self.assertIn('cron: "30 9,21 * * *"', pages)
        timezone = 'timezone: "America/Los_Angeles"'
        self.assertEqual(1, board.count(timezone))
        self.assertEqual(2, official.count(timezone))
        self.assertEqual(1, syncareer.count(timezone))
        self.assertEqual(1, pages.count(timezone))
        self.assertNotRegex(official, r"git add[^\n]*output/alerts")
        self.assertIn("workflow_dispatch:", board)
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
        self.assertIn("contents: read", pages)
        self.assertIn("persist-credentials: false", pages)
        self.assertIn('".github/workflows/reconcile-pages.yml"', pages)
        self.assertNotIn("git commit", pages)
        self.assertNotIn("git push", pages)
        self.assertNotIn('"profile/review_state.json"', pages)
        self.assertFalse((ROOT / ".github/workflows/scheduled-jobs.yml").exists())

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
        payload = json.loads((ROOT / "source" / "official_careers.json").read_text(encoding="utf-8"))
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
        registry = json.loads((ROOT / "source" / "official_careers.json").read_text(encoding="utf-8"))
        coverage = json.loads((ROOT / "profile" / "official_coverage.json").read_text(encoding="utf-8"))
        active = {company["id"] for company in registry["companies"] if company.get("adapter") != "skip"}
        stale = {
            company_id
            for company_id, config in coverage["companies"].items()
            if config.get("status") == "unsupported" and company_id in active
        }
        self.assertEqual(set(), stale)

    def test_ats_and_syncareer_have_explicit_official_cross_check_coverage(self) -> None:
        official = json.loads((ROOT / "source" / "official_careers.json").read_text(encoding="utf-8"))
        ats = json.loads((ROOT / "source" / "ats_boards.json").read_text(encoding="utf-8"))
        syncareer = json.loads((ROOT / "source" / "company_links.json").read_text(encoding="utf-8"))
        official_ids = {company["id"] for company in official["companies"]}
        ats_ids = {board["token"] for board in ats["boards"]}
        sync_ids = {company["key"] for company in syncareer["companies"]}
        self.assertTrue(ats_ids.issubset(official_ids))
        self.assertGreaterEqual(len(official_ids & sync_ids), 38)
        self.assertGreaterEqual(len(official_ids & ats_ids & sync_ids), 7)
        self.assertEqual(len(sync_ids), len(syncareer["companies"]))

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

        registry = json.loads((ROOT / "source" / "official_careers.json").read_text(encoding="utf-8"))
        companies = {company["id"]: company for company in registry["companies"]}
        self.assertIn("core infrastructure", companies["oracle"]["oracle_hcm"]["extra_queries"])


if __name__ == "__main__":
    unittest.main()
