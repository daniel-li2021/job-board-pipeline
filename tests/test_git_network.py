"""Exercise the self-contained bootstrap helper without a remote or a crawler."""
import json
import subprocess
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


class GitNetworkTests(unittest.TestCase):
    def setUp(self):
        script = (Path(__file__).resolve().parents[1] / "scripts/local_source_sync.sh").read_text()
        source = script.split("<<'PY_GIT_NETWORK'\n", 1)[1].split("\nPY_GIT_NETWORK", 1)[0]
        self.helper = types.ModuleType("git_network_bootstrap")
        exec(compile(source, "local_source_sync.sh:git_network", "exec"), self.helper.__dict__)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "git_network_latest.json"

    def process(self, code, stderr=""):
        process = Mock(returncode=code)
        process.communicate.return_value = ("", stderr)
        return process

    def test_dns_failure_retries_then_recovers(self):
        with patch.object(self.helper.subprocess, "Popen", side_effect=[
                self.process(128, "Could not resolve host: github.com"), self.process(0)]) as popen, \
             patch.object(self.helper.time, "sleep") as sleep:
            self.assertEqual(0, self.helper.run(self.path, "fetch", ["fetch", "origin", "main"]))
        self.assertEqual(2, popen.call_count)
        sleep.assert_called_once_with(5)
        receipt = json.loads(self.path.read_text())
        self.assertEqual(("success", 2), (receipt["status"], receipt["attempts"]))
        self.assertTrue(popen.call_args.kwargs["start_new_session"])

    def test_authentication_failure_is_not_retried_or_stored_as_raw_error(self):
        with patch.object(self.helper.subprocess, "Popen", return_value=self.process(
                128, "Permission denied (publickey). private diagnostic text")) as popen, \
             patch.object(self.helper.time, "sleep") as sleep:
            self.assertEqual(128, self.helper.run(self.path, "push_preflight", ["push", "--dry-run"]))
        popen.assert_called_once()
        sleep.assert_not_called()
        receipt = json.loads(self.path.read_text())
        self.assertEqual(("push_preflight", "git_failed", 1),
                         (receipt["stage"], receipt["reason"], receipt["attempts"]))
        self.assertNotIn("private diagnostic", self.path.read_text())

    def test_timeout_kills_process_group_and_stops_after_three_attempts(self):
        processes = [self.process(-9) for _ in range(3)]
        for i, process in enumerate(processes):
            process.pid = 9000 + i
            process.communicate.side_effect = [subprocess.TimeoutExpired("git", 45), ("", "")]
        with patch.object(self.helper.subprocess, "Popen", side_effect=processes), \
             patch.object(self.helper.os, "killpg") as kill, \
             patch.object(self.helper.time, "sleep") as sleep:
            self.assertEqual(124, self.helper.run(self.path, "fetch", ["fetch", "origin", "main"]))
        self.assertEqual(3, kill.call_count)
        self.assertEqual([5, 10], [call.args[0] for call in sleep.call_args_list])
        for process in processes:
            self.assertEqual(45, process.communicate.call_args_list[0].kwargs["timeout"])
        failure = json.loads(self.path.with_name("git_network_last_failure.json").read_text())
        self.assertEqual(("failed", "timeout", 3),
                         (failure["status"], failure["reason"], failure["attempts"]))

    def test_non_fast_forward_is_not_a_network_retry(self):
        with patch.object(self.helper.subprocess, "Popen", return_value=self.process(
                1, "[rejected] HEAD -> main (fetch first)")) as popen:
            self.assertEqual(1, self.helper.run(self.path, "publish", ["push", "origin", "HEAD:main"]))
        popen.assert_called_once()


if __name__ == "__main__":
    unittest.main()
