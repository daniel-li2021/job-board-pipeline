"""Durable Issue digests: publication reserves jobs, delivery acknowledges receipts."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from state_io import atomic_write, read_json

LABELS = {"board": "ats-linkedin-alert", "syncareer": "syncareer-alert", "official": "job-alert"}
DIRECTORIES = {"board": "board", "syncareer": "syncareer", "official": "official_careers"}


def _load(path: Path) -> dict:
    data = read_json(path, {"receipts": []})
    if not isinstance(data, dict) or not isinstance(data.get("receipts"), list):
        raise ValueError(f"Invalid notification outbox: {path}")
    for receipt in data["receipts"]:
        if (not isinstance(receipt, dict) or not all(receipt.get(k) for k in ("id", "pipeline", "title", "body"))
                or receipt.get("status") not in {"pending", "delivered"}):
            raise ValueError(f"Invalid notification receipt: {path}")
    return data


def _save(path: Path, data: dict) -> None:
    atomic_write(path, (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode())


def enqueue(path: Path, *, pipeline: str, stamp: str, title: str, body: str) -> str:
    identity = hashlib.sha256(json.dumps([pipeline, stamp, title, body]).encode()).hexdigest()
    data = _load(path)
    if any(r["id"] == identity for r in data["receipts"]):
        return identity
    cutoff = (datetime.now(timezone.utc) - timedelta(days=14)).isoformat()
    data["receipts"] = [r for r in data["receipts"]
                        if r["status"] == "pending" or r.get("delivered_at", "") >= cutoff]
    data["receipts"].append({"id": identity, "pipeline": pipeline, "stamp": stamp,
                             "title": title, "body": body, "status": "pending"})
    _save(path, data)
    return identity


def _gh(*args: str) -> str:
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout


def deliver(path: Path, repo: str) -> int:
    data = _load(path)
    pending = [r for r in data["receipts"] if r["status"] == "pending"]
    if not pending:
        return 0
    # List directly rather than search: newly-created Issues may not be search-indexed yet.
    pages = json.loads(_gh("api", "--paginate", "--slurp", f"repos/{repo}/issues?state=all&per_page=100"))
    issues = [issue for page in pages for issue in page if "pull_request" not in issue]
    labels = json.loads(_gh("api", "--paginate", "--slurp", f"repos/{repo}/labels?per_page=100"))
    available_labels = {item["name"] for page in labels for item in page}
    count = 0
    for receipt in pending:
        marker = f"<!-- job-board-digest:{receipt['id']} -->"
        existing = next((issue for issue in issues if marker in (issue.get("body") or "")), None)
        if existing:
            url = existing["html_url"]
        else:
            with tempfile.TemporaryDirectory() as directory:
                body_path = Path(directory) / "digest.md"
                body_path.write_text(receipt["body"] + "\n\n" + marker + "\n", encoding="utf-8")
                args = ["issue", "create", "--repo", repo, "--title", receipt["title"], "--body-file", str(body_path)]
                label = LABELS[receipt["pipeline"]]
                if label in available_labels:
                    args.extend(["--label", label])
                url = _gh(*args).strip()
                if not url.startswith("https://"):
                    raise ValueError("Issue creation returned no URL; receipt remains pending")
        receipt.update(status="delivered", issue_url=url, delivered_at=datetime.now(timezone.utc).isoformat())
        _save(path, data)
        count += 1
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pipeline", choices=LABELS)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    outbox = Path(__file__).resolve().parent / "output" / DIRECTORIES[args.pipeline] / "notification_outbox.json"
    print(f"Acknowledged {deliver(outbox, args.repo)} digest(s)")
