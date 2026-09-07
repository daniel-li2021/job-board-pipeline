from __future__ import annotations

import gzip
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import alert_history
import board_pipeline as board
import official_careers as official
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
