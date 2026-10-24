"""Mac launchd gate decisions never invoke a crawler in tests."""

import unittest
import fcntl
import json
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

    def test_weekend_has_only_noon_slot(self):
        for day in (17, 18):
            noon = datetime(2026, 10, day, 12, tzinfo=PACIFIC)
            self.assertTrue(decision(noon, {"last_success_at": noon.replace(hour=9).isoformat()})[0])
            for hour in (15, 21):
                with self.subTest(day=day, hour=hour):
                    run, _, state = decision(noon.replace(hour=hour), {"last_success_at": noon.isoformat()})
                    self.assertFalse(run)
                    self.assertFalse(state["scheduled_slot_missed"])

    def test_slots_cross_weekday_and_weekend_boundaries(self):
        cases = (
            ((16, 22), (16, 21), (17, 12)),
            ((17, 10), (16, 21), (17, 12)),
            ((18, 10), (17, 12), (18, 12)),
            ((19, 10), (18, 12), (19, 12)),
            ((19, 16), (19, 15), (19, 21)),
        )
        for current, previous, following in cases:
            with self.subTest(current=current):
                dt = lambda pair: datetime(2026, 10, *pair, tzinfo=PACIFIC)
                self.assertEqual((dt(previous), dt(following)), gate._slots(dt(current)))

    def test_weekend_missed_noon_catches_up_once_after_wake(self):
        now = datetime(2026, 10, 18, 16, tzinfo=PACIFIC)
        run, _, state = decision(now, {"last_success_at": now.replace(day=17, hour=12).isoformat()})
        self.assertTrue(run)
        self.assertEqual("due", state["catch_up_status"])
        state["last_success_at"] = now.isoformat()
        self.assertFalse(decision(now.replace(hour=21), state)[0])

    def test_weekend_slots_keep_pacific_dst_offsets(self):
        now = datetime(2026, 11, 1, 1, 30, tzinfo=PACIFIC)
        latest, following = gate._slots(now)
        self.assertEqual("2026-10-31T12:00:00-07:00", latest.isoformat())
        self.assertEqual("2026-11-01T12:00:00-08:00", following.isoformat())

    def test_active_lock_coalesces_another_launch(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(gate, "LOCK", Path(temp) / "lock"), \
             patch.object(gate, "STATE", Path(temp) / "state.json"):
            with gate.LOCK.open("a+") as held:
                fcntl.flock(held, fcntl.LOCK_EX | fcntl.LOCK_NB)
                with patch.object(gate.subprocess, "run") as runner:
                    self.assertEqual(0, gate.main())
                    runner.assert_not_called()

    def test_due_slot_launches_sync_with_result_path(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(gate, "LOCK", Path(temp) / "lock"), \
             patch.object(gate, "STATE", Path(temp) / "state.json"), \
             patch.object(gate, "RESULT", Path(temp) / "result.json"), \
             patch.object(gate, "decision", return_value=(True, "fixed slot", {})), \
             patch.object(gate.subprocess, "run") as runner:
            runner.return_value.returncode = 0
            self.assertEqual(0, gate.main())
            runner.assert_called_once()
            self.assertEqual(str(Path(temp) / "result.json"),
                             runner.call_args.kwargs["env"]["LOCAL_SOURCE_RESULT_PATH"])
            self.assertEqual("success", json.loads(gate.STATE.read_text())["last_run_status"])

    def test_network_failure_is_recorded_without_completing_the_slot(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(gate, "LOCK", Path(temp) / "lock"), \
             patch.object(gate, "STATE", Path(temp) / "state.json"), \
             patch.object(gate, "NETWORK_RESULT", Path(temp) / "network.json"), \
             patch.object(gate, "decision", side_effect=lambda now, state: (True, "due", state)), \
             patch.object(gate.subprocess, "run") as runner:
            def failure(*args, **kwargs):
                gate.NETWORK_RESULT.write_text(json.dumps({"finished_at": datetime.now(PACIFIC).isoformat(),
                    "status": "failed", "stage": "fetch", "reason": "timeout", "attempts": 3}))
                runner.return_value.returncode = 1
                return runner.return_value
            runner.side_effect = failure
            self.assertEqual(1, gate.main())
            state = json.loads(gate.STATE.read_text())
            self.assertNotIn("last_success_at", state)
            self.assertEqual(("fetch", "timeout", 3),
                             (state["last_failure_stage"], state["last_failure_reason"], state["last_failure_attempts"]))

    def test_stale_or_malformed_network_receipt_cannot_label_an_unrelated_failure(self):
        for receipt in ([], {"status": "failed", "stage": "fetch", "reason": "timeout",
                             "finished_at": "2000-01-01T00:00:00+00:00"}):
            with self.subTest(receipt=receipt), tempfile.TemporaryDirectory() as temp, \
                 patch.object(gate, "LOCK", Path(temp) / "lock"), \
                 patch.object(gate, "STATE", Path(temp) / "state.json"), \
                 patch.object(gate, "NETWORK_RESULT", Path(temp) / "network.json"), \
                 patch.object(gate, "decision", side_effect=lambda now, state: (True, "due", state)), \
                 patch.object(gate.subprocess, "run") as runner:
                gate.NETWORK_RESULT.write_text(json.dumps(receipt))
                runner.return_value.returncode = 1
                self.assertEqual(1, gate.main())
                self.assertNotIn("last_failure_stage", json.loads(gate.STATE.read_text()))


if __name__ == "__main__":
    unittest.main()
