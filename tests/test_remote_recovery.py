import tempfile
import time
import unittest
from collections import Counter
from unittest.mock import Mock, patch
from datetime import datetime, timezone
from pathlib import Path

import remote_recovery
import remote_indeed
import local_sources
from sources import official_jd_recovery
from sources import linkedin_local
import board_pipeline as board
from sources.official_jd_recovery import Resolver


class RemoteRecoveryTests(unittest.TestCase):
    def test_indeed_remote_collector_reuses_snapshot_writer_without_mac_collection(self):
        self.assertNotIn("indeed", local_sources.SOURCES)
        with tempfile.TemporaryDirectory() as tmp, patch.object(remote_indeed, "OUTPUT_DIR", Path(tmp)), \
             patch.object(remote_indeed.local_sources, "collector_provenance", return_value={"commit": "test"}), \
             patch.object(remote_indeed.local_sources, "run_one", return_value={
                 "source": "indeed", "status": "ok", "count": 1,
             }) as run, patch.object(remote_indeed.local_sources, "write_health") as write:
            remote_indeed.main()
            self.assertEqual("indeed", run.call_args.args[0])
            self.assertFalse(run.call_args.kwargs["recover_missing"])
            write.assert_called_once()

    def test_online_budget_is_separate_from_mac_recovery(self):
        self.assertEqual((100, 150), (official_jd_recovery.NORMAL_SEARCH_LIMIT,
                                    official_jd_recovery.NORMAL_PAGE_LIMIT))
        self.assertEqual(float("inf"), local_sources.RECOVERY_SEARCH_LIMIT)
        self.assertEqual(float("inf"), local_sources.RECOVERY_PAGE_LIMIT)
        self.assertEqual(
            ["software engineer", "ai engineer", "backend engineer",
             "full-stack engineer", "machine learning engineer"],
            [spec[1] for spec in linkedin_local.MAC_SEARCH_SPECS],
        )
        self.assertEqual(14, local_sources.MAC_SEARCH_PAGE_LIMIT)

    def test_handoff_keeps_jd_and_unresolved_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "official.json.gz"
            rows = [
                {"company": "Example", "title": "Engineer", "location": "Austin, TX",
                 "source": "official", "job_id": "123", "official_url": "https://example.com/jobs/123",
                 "description": "A" * 250},
                {"company": "Example", "title": "Designer", "location": "Austin, TX",
                 "source": "official", "job_id": "124", "official_url": "https://example.com/jobs/124"},
            ]
            remote_recovery.write_snapshot(path, "official", rows)
            jobs = remote_recovery.read_snapshot(path)
            self.assertEqual({"jd_available", "candidate"}, {job["recovery_status"] for job in jobs})
            remote_recovery.write_snapshot(path, "official", [rows[1]])
            self.assertEqual("A" * 250, next(job for job in remote_recovery.read_snapshot(path)
                                             if job["job_id"] == "123")["description"])
            remote_recovery.write_snapshot(path, "official", [{**rows[0], "official_url": "https://example.com/new/123",
                                                                "description": ""}])
            self.assertEqual(2, len(remote_recovery.read_snapshot(path)))

    def test_exact_remote_jd_precedes_search_and_linkedin_detail(self):
        resolver = Resolver(search_limit=0, page_limit=0)
        row = {"company": "Example", "title": "Engineer", "location": "Austin, TX",
               "source": "linkedin", "job_id": "li-1", "description": ""}
        peer = {"company": "Example", "title": "Engineer", "location": "Austin, TX",
                "source": "official", "job_id": "123", "official_url": "https://example.com/jobs/123",
                "description": "A" * 250, "remote_recovery": True}
        result = resolver.recover(row, previous={}, context={}, store={"remote": peer},
                                  now=datetime.now(timezone.utc), cheap_only=True)
        self.assertEqual("remote_exact_peer", result)
        self.assertEqual(peer["description"], row["description"])
        self.assertEqual(0, resolver.search_requests)
        self.assertEqual(0, resolver.page_requests)

    def test_remote_enrichment_never_fetches_linkedin_application_url(self):
        job = {"source": "linkedin", "job_id": "li-1", "company": "Example",
               "title": "Engineer", "location": "Austin, TX", "description": "",
               "application_url": "https://www.linkedin.com/jobs/view/123"}
        session = Mock()
        with patch.object(board, "_scrapling_fetch", side_effect=AssertionError("LinkedIn request")):
            board.resolve_exposed_originals([job], session, {})
        session.get.assert_not_called()

    def test_company_title_resolver_never_fetches_linkedin_page(self):
        session = Mock()
        resolver = Resolver(session=session, search_limit=100, page_limit=150)
        body, _url, status = resolver.page("https://www.linkedin.com/jobs/view/123", Counter())
        self.assertEqual(("", "unsupported"), (body, status))
        session.get.assert_not_called()

    def test_online_wall_clock_deadline_stops_requests(self):
        session = Mock()
        resolver = Resolver(session=session, deadline=time.monotonic() - 1)
        self.assertEqual(([], "budget"), resolver.search('"Engineer" "Example"'))
        self.assertEqual("budget", resolver.page("https://example.com/jobs/123", Counter())[2])
        session.get.assert_not_called()

    def test_targeted_mac_search_uses_saved_company_title_location(self):
        session = Mock()
        session.get.return_value = Mock(status_code=200, text="<div></div>")
        card, rate_limited = linkedin_local.targeted_search(
            "Example", "Software Engineer II", "Austin, TX", session=session,
        )
        self.assertIsNone(card)
        self.assertFalse(rate_limited)
        params = session.get.call_args.kwargs["params"]
        self.assertEqual('"Software Engineer II" "Example" "Austin, TX"', params["keywords"])
        self.assertEqual("Austin, TX", params["location"])
