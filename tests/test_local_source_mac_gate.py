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

    def test_every_minute_of_five_pm_defers_a_missed_slot(self):
        for minute in range(60):
            with self.subTest(minute=minute):
                run, _, state = decision(self.at(17, minute), {"last_success_at": self.at(12).isoformat()})
                self.assertFalse(run)
                self.assertTrue(state["scheduled_slot_missed"])
                self.assertTrue(state["catch_up_pending"])
                self.assertEqual("pending", state["catch_up_status"])

    def test_six_pm_reconsiders_missed_slot_without_deferred_flag(self):
        run, _, state = decision(self.at(18), {"last_success_at": self.at(14, 14).isoformat(),
                                              "last_check_at": self.at(17, 50).isoformat()})
        self.assertTrue(run)
        self.assertEqual("due", state["catch_up_status"])
        self.assertEqual(self.at(21).isoformat(), state["next_scheduled_run_at"])

    def test_fixed_slots_ignore_catch_up_spacing(self):
        state = {"last_success_at": self.at(14, 14).isoformat()}
        run, reason, _ = decision(self.at(15), state)
        self.assertTrue(run)
        self.assertEqual("fixed slot", reason)
        self.assertTrue(decision(self.at(21), {"last_success_at": self.at(18).isoformat(),
                                               "evening_success_date": self.at(21).date().isoformat()})[0])

    def test_short_sleep_and_first_load_use_missed_slot(self):
        recent_check = {"last_check_at": self.at(12, 5).isoformat(),
                        "last_success_at": self.at(9).isoformat()}
        self.assertTrue(decision(self.at(12, 20), recent_check)[0])
        self.assertTrue(decision(self.at(16), {"last_success_at": self.at(10).isoformat()})[0])

    def test_recent_success_skips_catch_up_until_three_hours_pass(self):
        state = {"last_success_at": self.at(14, 14).isoformat()}
        run, _, skipped = decision(self.at(16), state)
        self.assertFalse(run)
        self.assertEqual("skipped", skipped["catch_up_status"])
        self.assertTrue(skipped["catch_up_pending"])
        self.assertTrue(decision(self.at(18), skipped)[0])

    def test_completed_slot_needs_no_catch_up(self):
        run, _, state = decision(self.at(15, 30), {"last_success_at": self.at(15, 10).isoformat()})
        self.assertFalse(run)
        self.assertFalse(state["scheduled_slot_missed"])
        self.assertEqual("not_needed", state["catch_up_status"])

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
