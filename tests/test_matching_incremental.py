from __future__ import annotations

import json
import threading
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import Mock, patch

import board_pipeline as board
import llm_config
from sources.careers.incremental import DetailCache, NewestFirstPager, annotate_detail, listing_signature
from sources.careers import registry
from sources.schema import SourceUnavailable


class LlmMatchingTests(unittest.TestCase):
    def test_long_jd_preserves_required_qualifications(self) -> None:
        text = (
            "Overview\n" + ("introductory context " * 420) + "\n"
            "Responsibilities\nBuild reliable backend services and own production operations.\n"
            "Required Qualifications\nFive years building distributed Python services.\n"
            "Preferred Qualifications\nKubernetes certification."
        )
        selected = llm_config.select_jd_context(text)
        self.assertLessEqual(len(selected), llm_config.JD_CONTEXT_CHARS)
        self.assertIn("Required Qualifications", selected)
        self.assertIn("distributed Python services", selected)
        self.assertIn("Responsibilities", selected)

    @patch("board_pipeline.requests.post")
    def test_llm_batch_sends_only_complete_routed_resume(self, post: Mock) -> None:
        job = {
            "title": "Backend Engineer",
            "company": "Example",
            "location": "Remote, US",
            "job_id": "1",
            "source": "example",
            "source_url": "https://example.test/jobs/1",
            "description": "Responsibilities\nBuild APIs\nRequired Qualifications\nPython",
            "role_family": "swe",
        }
        key = board.dedup_key(job)
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {
            "choices": [{"message": {"content": json.dumps({"results": [{
                "key": key,
                "role_family": "swe",
                "resume_profile_used": "resume_swe",
                "match_score": 82,
                "seniority_fit": "good",
                "hard_constraint_status": "ok",
                "top_match_reasons": ["Python APIs"],
                "main_gaps": [],
                "recommended_action": "apply_now",
            }]})}}],
            "usage": {
                "prompt_tokens": 100,
                "completion_tokens": 20,
                "prompt_tokens_details": {"cached_tokens": 25},
                "completion_tokens_details": {"reasoning_tokens": 5},
            },
        }
        post.return_value = response
        full_resume = "SWE-START\n" + ("experience\n" * 1000) + "SWE-END"
        results, usage = board.llm_match_batch(
            [job],
            {"candidate": "candidate", "resume_swe": full_resume, "resume_ai": "AI RESUME"},
            "test-key",
            "gpt-5.6-terra",
            "resume_swe",
        )
        sent = post.call_args.kwargs["json"]
        prompt = json.loads(sent["messages"][1]["content"])
        self.assertEqual(full_resume, prompt["resume_swe"])
        self.assertNotIn("resume_ai", prompt)
        self.assertEqual("low", sent["reasoning_effort"])
        self.assertEqual(82, results[key]["match_score"])
        self.assertEqual(25, usage["cached_input_tokens"])
        self.assertEqual(5, usage["reasoning_tokens"])

    def test_cost_and_quality_first_sort(self) -> None:
        usage = {
            "model": "gpt-5.6-terra",
            "input_tokens": 1_000_000,
            "cached_input_tokens": 200_000,
            "output_tokens": 100_000,
        }
        self.assertAlmostEqual(2.84, llm_config.estimate_cost_usd(usage))
        base = {"recency_bucket": "1to3d", "tier": "B", "seniority_fit": "good"}
        high_quality = {**base, "match_score": 78, "date_confidence": "low"}
        high_confidence = {**base, "match_score": 71, "date_confidence": "high"}
        self.assertLess(board.user_facing_sort_key(high_quality), board.user_facing_sort_key(high_confidence))

    def test_five_year_role_reaches_llm_prefilter(self) -> None:
        five = {"title": "Backend Software Engineer", "description": "Requires 5+ years building APIs"}
        six = {"title": "Backend Software Engineer", "description": "Requires 6+ years building APIs"}
        self.assertTrue(board.role_seniority_prefilter(five)[0])
        self.assertFalse(board.role_seniority_prefilter(six)[0])


class IncrementalOfficialTests(unittest.TestCase):
    def test_detail_cache_reuse_change_and_staleness(self) -> None:
        now = datetime(2026, 8, 31, tzinfo=timezone.utc)
        cached = {
            "company": "Example",
            "job_id": "42",
            "official_url": "https://example.test/42",
            "title": "Software Engineer",
            "posted_date": "2026-08-30",
            "description": "Full cached JD",
            "fetched_at": (now - timedelta(days=2)).isoformat(),
        }
        cache = DetailCache([cached], now=now)
        reusable = cache.decide(
            company="Example", job_id="42", url=cached["official_url"],
            title=cached["title"], posted_date=cached["posted_date"],
        )
        self.assertFalse(reusable.should_fetch)
        relative_cache = DetailCache([{**cached,
            "listing_signature": listing_signature(cached["title"], "Posted 2 Days Ago"),
        }], now=now)
        self.assertFalse(relative_cache.decide(
            company="Example", job_id="42", url=cached["official_url"],
            title=cached["title"], posted_date="Posted Today",
        ).should_fetch)
        changed = cache.decide(
            company="Example", job_id="42", url=cached["official_url"],
            title="Software Engineer II", posted_date=cached["posted_date"],
        )
        self.assertEqual("changed", changed.reason)
        stale_cache = DetailCache([{**cached, "fetched_at": (now - timedelta(days=20)).isoformat()}], now=now)
        self.assertEqual(
            "stale",
            stale_cache.decide(
                company="Example", job_id="42", url=cached["official_url"],
                title=cached["title"], posted_date=cached["posted_date"],
            ).reason,
        )
        absolute_date_changed = cache.decide(
            company="Example", job_id="42", url=cached["official_url"],
            title=cached["title"], posted_date="2026-08-31",
        )
        self.assertEqual("changed", absolute_date_changed.reason)

    def test_newest_pager_keeps_one_overlap_page(self) -> None:
        pager = NewestFirstPager({"a", "b"})
        self.assertFalse(pager.should_stop_after(1, ["a", "b"]))
        self.assertFalse(pager.should_stop_after(2, ["a", "b"]))
        self.assertFalse(pager.should_stop_after(3, ["a", "b"]))
        self.assertTrue(pager.should_stop_after(4, ["a", "b"]))

    @patch("sources.careers.registry.scrape_company")
    @patch("sources.careers.registry.enabled_companies")
    def test_unsorted_daily_depth_and_periodic_full_depth(self, enabled: Mock, scrape: Mock) -> None:
        enabled.return_value = [{"id": "example", "name": "Example", "adapter": "workday", "enabled": True}]
        scrape.return_value = {"company": "Example", "jobs": [], "errors": []}
        registry.scrape_enabled(Mock(), max_pages=12, full_sweep=False)
        self.assertEqual(4, scrape.call_args.kwargs["max_pages"])
        registry.scrape_enabled(Mock(), max_pages=12, full_sweep=True)
        self.assertEqual(12, scrape.call_args.kwargs["max_pages"])

    @patch("sources.careers.registry.make_session")
    @patch("sources.careers.registry.scrape_company")
    @patch("sources.careers.registry.enabled_companies")
    def test_company_concurrency_is_isolated_ordered_and_error_safe(
        self, enabled: Mock, scrape: Mock, make_session: Mock,
    ) -> None:
        enabled.return_value = [
            {"id": "one", "name": "One", "adapter": "workday", "enabled": True},
            {"id": "two", "name": "Two", "adapter": "workday", "enabled": True},
            {"id": "three", "name": "Three", "adapter": "workday", "enabled": True},
        ]
        sessions = []

        def session_factory():
            item = Mock(request_count=2, request_seconds=0.25)
            sessions.append(item)
            return item

        make_session.side_effect = session_factory
        barrier = threading.Barrier(3)

        def run(_session, company, **_kwargs):
            barrier.wait(timeout=2)
            if company["id"] == "two":
                raise SourceUnavailable("blocked")
            if company["id"] == "three":
                raise ValueError("broken")
            return {"company": company["name"], "jobs": [], "errors": []}

        scrape.side_effect = run
        results = registry.scrape_enabled(full_sweep=False, max_workers=3)
        self.assertEqual(["one", "two", "three"], [r["company_id"] for r in results])
        self.assertEqual([None, "blocked", "error"], [r.get("status") for r in results])
        self.assertEqual(3, len({id(item) for item in sessions}))
        self.assertTrue(all(r["http_requests"] == 2 for r in results))


if __name__ == "__main__":
    unittest.main()
