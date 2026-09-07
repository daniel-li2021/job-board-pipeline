"""Offline dispatcher contract checks: python3 infra/scheduler/test_scheduler.py."""
import io
import json
import os
from pathlib import Path
import types
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError


class SchedulerTests(unittest.TestCase):
    def test_dispatch_contract_and_failures(self):
        template = Path(__file__).with_name("template.yaml").read_text()
        code = template.split("        ZipFile: |\n", 1)[1].split("  DispatchLogs:", 1)[0]
        code = "\n".join(line[10:] for line in code.splitlines())
        secrets = Mock()
        secrets.get_secret_value.return_value = {"SecretString": "test-token"}
        boto = types.ModuleType("boto3")
        boto.client = Mock(return_value=secrets)
        config = types.ModuleType("botocore.config")
        config.Config = Mock()
        namespace = {}
        with patch.dict("sys.modules", {"boto3": boto, "botocore": types.ModuleType("botocore"), "botocore.config": config}):
            exec(compile(code, "inline-dispatcher", "exec"), namespace)
        handler = namespace["handler"]
        response = Mock()
        response.__enter__ = Mock(return_value=types.SimpleNamespace(status=204))
        response.__exit__ = Mock(return_value=False)
        context = types.SimpleNamespace(aws_request_id="test-request")
        with patch.dict(os.environ, {"TOKEN_SECRET_ARN": "test-secret", "REPOSITORY": "owner/repo"}), \
             patch("urllib.request.urlopen", return_value=response) as send, \
             patch("sys.stdout", new_callable=io.StringIO) as log:
            for workflow in namespace["WORKFLOWS"]:
                receipt = handler({"workflow": workflow}, context)
                request = send.call_args.args[0]
                self.assertEqual({"ref": "main"}, json.loads(request.data))
                self.assertTrue(request.full_url.endswith(f"/{workflow}/dispatches"))
                self.assertEqual(204, receipt["status"])
            handler({"workflow": "board-jobs.yml", "probe_id": "probe-1"}, context)
            self.assertEqual({"scheduler_probe": "probe-1"}, json.loads(send.call_args.args[0].data)["inputs"])
            self.assertNotIn("test-token", log.getvalue())
            before = send.call_count
            for event in ({"workflow": "unknown.yml"}, {"workflow": "board-jobs.yml", "probe_id": 123},
                          {"workflow": "reconcile-pages.yml", "probe_id": "probe"}):
                with self.assertRaises(ValueError):
                    handler(event, context)
            self.assertEqual(before, send.call_count)
            for status in (401, 403, 429, 500):
                send.side_effect = HTTPError("https://api.github.com", status, "failure", {}, None)
                with self.assertRaisesRegex(RuntimeError, str(status)):
                    handler({"workflow": "board-jobs.yml"}, context)
            send.side_effect = TimeoutError("timed out")
            with self.assertRaises(TimeoutError):
                handler({"workflow": "board-jobs.yml"}, context)


if __name__ == "__main__":
    unittest.main()
