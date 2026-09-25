"""Mac launchd gate decisions never invoke a crawler in tests."""

import unittest
import fcntl
import tempfile
from datetime import datetime
from pathlib import Path
from unittest.mock import patch
from zoneinfo import ZoneInfo

from scripts.macos import local_source_gate as gate
from scripts.macos.local_source_gate import decision

PACIFIC = ZoneInfo("America/Los_Angeles")


class MacGateTests(unittest.TestCase):
    def at(self, hour, minute=0):
        return datetime(2026, 9, 24, hour, minute, tzinfo=PACIFIC)

    def test_every_minute_of_five_pm_is_quiet(self):
        for minute in range(60):
            with self.subTest(minute=minute):
                run, _, state = decision(self.at(17, minute), {"last_check_at": self.at(15).isoformat()})
                self.assertFalse(run)
                self.assertTrue(state["deferred_evening"])

    def test_six_pm_replays_deferred_evening_once(self):
        run, _, state = decision(self.at(18), {"deferred_evening": True,
                                              "last_check_at": self.at(17, 50).isoformat()})
        self.assertTrue(run)
        state["deferred_evening"] = False
        state["evening_success_date"] = self.at(18).date().isoformat()
        self.assertFalse(decision(self.at(21), state)[0])

    def test_wake_gap_and_three_hour_spacing(self):
        state = {"last_check_at": self.at(8).isoformat(),
                 "last_success_at": self.at(9).isoformat()}
        self.assertFalse(decision(self.at(10), state)[0])
        self.assertTrue(decision(self.at(12), state)[0])
        self.assertFalse(decision(self.at(12, 10), {"last_check_at": self.at(12).isoformat()})[0])

    def test_after_six_wake_runs_but_active_evening_waits_for_nine(self):
        self.assertTrue(decision(self.at(19), {"last_check_at": self.at(16).isoformat()})[0])
        self.assertFalse(decision(self.at(19), {"last_check_at": self.at(18, 50).isoformat()})[0])
        self.assertTrue(decision(self.at(21), {"last_check_at": self.at(20, 50).isoformat()})[0])

    def test_active_lock_coalesces_another_launch(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(gate, "LOCK", Path(temp) / "lock"), \
             patch.object(gate, "STATE", Path(temp) / "state.json"):
            with gate.LOCK.open("a+") as held:
                fcntl.flock(held, fcntl.LOCK_EX | fcntl.LOCK_NB)
                with patch.object(gate.subprocess, "run") as runner:
                    self.assertEqual(0, gate.main())
                    runner.assert_not_called()


if __name__ == "__main__":
    unittest.main()
