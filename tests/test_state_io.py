from __future__ import annotations

import gzip
import json
from datetime import datetime, timedelta, timezone
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import alert_history
import board_pipeline as board
import official_careers as official
import pipeline_health
import review_state
import state_io


class StateSafetyTests(unittest.TestCase):
    def test_failed_atomic_write_leaves_previous_file_and_cleans_temporary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state_io.atomic_write(path, b"previous")
            for operation in ("fsync", "replace"):
                with patch.object(state_io.os, operation, side_effect=OSError("disk failure")):
                    with self.assertRaises(OSError):
                        state_io.atomic_write(path, b"replacement")
                self.assertEqual(b"previous", path.read_bytes())
                self.assertEqual([path], list(path.parent.iterdir()))
            state_io.atomic_write(path, b"complete")
            self.assertEqual(b"complete", path.read_bytes())

    def test_owned_stores_reject_corruption_but_optional_peer_cache_does_not_block(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "jobs.json"
            with patch.object(board, "JOBS_STORE_PATH", path), patch.object(official, "STORE_PATH", path):
                self.assertEqual({}, board.load_store())
                for text in ('{', 'null', '{}', '{"entries": [null]}', '{"entries": [{}]}'):
                    path.write_text(text)
                    for reader in (board.load_store, official.load_careers_store):
                        with self.assertRaises(ValueError):
                            reader()
                    self.assertEqual({}, board.load_store_path(path))
                    self.assertEqual(text, path.read_text())
                entry = {"key": "job", "first_seen": "2026-09-01", "review_status": "applied", "match_score": 75}
                for payload in ([entry], {"entries": [entry]}):
                    path.write_text(json.dumps(payload))
                    self.assertEqual({"job": entry}, board.load_store())
                    self.assertEqual(board.load_store(), official.load_careers_store())

    def test_job_store_round_trips_gzip_and_legacy_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "jobs.json"
            entry = {"key": "job", "first_seen": "2026-09-01", "description": "Build APIs. " * 20}
            board.save_store_path(path, {"job": entry}, 7)
            raw = path.read_bytes()
            self.assertTrue(raw.startswith(b"\x1f\x8b"))
            self.assertLess(len(raw), len(json.dumps({"entries": [entry]}, indent=2)))
            loaded = board.load_store_path(path, strict=True)
            self.assertEqual(entry["description"], loaded["job"]["description"])
            path.write_text(json.dumps({"entries": [entry]}), encoding="utf-8")
            self.assertEqual(entry["description"], board.load_store_path(path, strict=True)["job"]["description"])
            self.assertEqual(
                entry["description"],
                review_state._read(path, {})["entries"][0]["description"],
            )
            self.assertEqual(
                entry["description"],
                pipeline_health._read(path, {})["entries"][0]["description"],
            )

    def test_corrupt_digest_history_and_review_state_are_never_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            with patch.object(review_state, "STATE_PATH", path), patch.object(review_state, "STORE_PATHS", ()):
                for text in ('{', 'null', '{"jobs": [], "events": [], "alerted_keys": "invalid"}'):
                    path.write_text(text)
                    with self.assertRaises(ValueError):
                        board.load_digest_state(path)
                    with self.assertRaises(ValueError):
                        review_state.set_status("id::job", "applied")
                    if text != '{"jobs": [], "events": [], "alerted_keys": "invalid"}':
                        with self.assertRaises(ValueError):
                            alert_history.append_event(path, pipeline="board", stamp="2026-09-07_1200", jobs=[], event_kind="digest")
                    self.assertEqual(text, path.read_text())
                path.write_text(json.dumps({"jobs": {"id::job": {"notes": "Keep these notes", "status": "in_progress"}}}))
                review_state.set_status("id::job", "applied")
                self.assertEqual("Keep these notes", json.loads(path.read_text())["jobs"]["id::job"]["notes"])

    def test_legacy_entry_defaults_do_not_share_mutable_fields(self):
        first, second = board.ensure_entry_defaults({}), board.ensure_entry_defaults({})
        for key, value in first.items():
            if isinstance(value, list):
                value.append("first job only")
                self.assertEqual([], second[key])
            elif isinstance(value, dict):
                value["first job only"] = True
                self.assertEqual({}, second[key])
        existing = {"main_gaps": ["existing gap"], "match_score": 75, "review_status": "applied"}
        self.assertIs(existing, board.ensure_entry_defaults(existing))
        self.assertEqual(["existing gap"], existing["main_gaps"])
        self.assertEqual(75, existing["match_score"])
        self.assertEqual("applied", existing["review_status"])

    def test_retention_and_history_treat_naive_dates_as_utc(self):
        now = datetime(2026, 9, 7, tzinfo=timezone.utc)
        rows = {
            "date": {"first_seen": "2026-08-31"},
            "offset": {"first_seen": "2026-08-30T17:00:00-07:00"},
            "old": {"first_seen": "2026-08-29"},
            "unknown": {"first_seen": 123},
        }
        self.assertEqual({"date", "offset", "unknown"}, set(board.prune_store(rows, now)))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "history.json"
            path.write_text(json.dumps({"events": [{"emitted_at": "2026-09-06T23:00:00", "jobs": []}]}))
            self.assertEqual(1, len(alert_history.recent_events(path, now, hours=2)))

    def test_shared_output_emitter_keeps_explicit_and_environment_prefixes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "outputs"
            with patch.dict("os.environ", {"GITHUB_OUTPUT": str(path), "GITHUB_OUTPUT_PREFIX": "official_"}):
                board.emit_github_output({"count": "1"})
                board.emit_github_output({"count": "2"}, prefix="")
            self.assertEqual("official_count=1\ncount=2\n", path.read_text())

    def test_invalid_official_raw_snapshot_cannot_be_replaced_during_merge(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "raw.json.gz"
            with patch.object(official, "RAW_PATH", path), patch.object(official, "CAREERS_DIR", path.parent):
                for data in (b"truncated gzip", gzip.compress(b'{'), gzip.compress(b'{"jobs": [null]}')):
                    path.write_bytes(data)
                    with self.assertRaises((OSError, ValueError)):
                        official.write_scrape_outputs([], "2026-09-07_1200")
                    self.assertEqual(data, path.read_bytes())


if __name__ == "__main__":
    unittest.main()
