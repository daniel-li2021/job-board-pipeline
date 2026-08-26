#!/usr/bin/env python3
"""ATS adapters: Greenhouse, Lever, Ashby public job-board JSON APIs.

These endpoints are anonymous and CI-friendly (no login, low block risk),
so they run in GitHub Actions. Each board is described in
``source/ats_boards.json``:

    {
      "boards": [
        {"company": "Databricks", "ats": "greenhouse", "token": "databricks"},
        {"company": "Palantir",   "ats": "lever",      "token": "palantir"},
        {"company": "OpenAI",     "ats": "ashby",       "token": "openai"}
      ]
    }
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

import requests

from .schema import (
    SourceUnavailable,
    is_us_location,
    make_job,
    normalize_space,
)

BASE_DIR = Path(__file__).resolve().parent.parent
ATS_BOARDS_JSON = BASE_DIR / "source" / "ats_boards.json"
REQUEST_TIMEOUT = 25


def _html_to_text(value: str) -> str:
    if not value:
        return ""
    from bs4 import BeautifulSoup

    return normalize_space(BeautifulSoup(value, "html.parser").get_text(" ", strip=True))


def _get_json(session: requests.Session, url: str, params: Dict[str, Any] | None = None) -> Any:
    try:
        resp = session.get(url, params=params, timeout=REQUEST_TIMEOUT)
    except requests.RequestException as exc:
        raise SourceUnavailable(f"network error: {exc}") from exc
    if resp.status_code in (401, 403, 429):
        raise SourceUnavailable(f"blocked with HTTP {resp.status_code}")
    if resp.status_code == 404:
        # Wrong/removed board token: treat as empty, not fatal for the whole run.
        return None
    if resp.status_code >= 400:
        raise SourceUnavailable(f"HTTP {resp.status_code}")
    try:
        return resp.json()
    except json.JSONDecodeError as exc:
        raise SourceUnavailable(f"non-JSON response: {exc}") from exc


def fetch_greenhouse(session: requests.Session, company: str, token: str) -> List[Dict[str, str]]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{token}/jobs"
    data = _get_json(session, url, params={"content": "true"})
    if not data:
        return []
    rows: List[Dict[str, str]] = []
    for item in data.get("jobs", []):
        location = (item.get("location") or {}).get("name", "")
        if location and not is_us_location(location):
            continue
        rows.append(
            make_job(
                source="greenhouse",
                company=company,
                title=item.get("title", ""),
                location=location,
                job_id=str(item.get("id", "")),
                posted_date=item.get("updated_at") or item.get("first_published") or "",
                date_confidence="medium",
                source_url=item.get("absolute_url", ""),
                official_url=item.get("absolute_url", ""),
                description=_html_to_text(item.get("content", "")),
            )
        )
    return rows


def fetch_lever(session: requests.Session, company: str, token: str) -> List[Dict[str, str]]:
    url = f"https://api.lever.co/v0/postings/{token}"
    data = _get_json(session, url, params={"mode": "json"})
    if not data:
        return []
    rows: List[Dict[str, str]] = []
    for item in data:
        cats = item.get("categories") or {}
        location = cats.get("location") or ""
        if location and not is_us_location(location):
            continue
        desc = item.get("descriptionPlain") or _html_to_text(item.get("description", ""))
        rows.append(
            make_job(
                source="lever",
                company=company,
                title=item.get("text", ""),
                location=location,
                job_id=str(item.get("id", "")),
                posted_date=item.get("createdAt") or "",
                date_confidence="medium",
                source_url=item.get("hostedUrl", "") or item.get("applyUrl", ""),
                official_url=item.get("hostedUrl", "") or item.get("applyUrl", ""),
                description=desc,
            )
        )
    return rows


def fetch_ashby(session: requests.Session, company: str, token: str) -> List[Dict[str, str]]:
    url = f"https://api.ashbyhq.com/posting-api/job-board/{token}"
    data = _get_json(session, url, params={"includeCompensation": "false"})
    if not data:
        return []
    rows: List[Dict[str, str]] = []
    for item in data.get("jobs", []):
        location = item.get("location") or ""
        if location and not is_us_location(location):
            continue
        rows.append(
            make_job(
                source="ashby",
                company=company,
                title=item.get("title", ""),
                location=location,
                job_id=str(item.get("id", "")),
                posted_date=item.get("publishedAt") or item.get("updatedAt") or "",
                date_confidence="medium",
                source_url=item.get("jobUrl", "") or item.get("applyUrl", ""),
                official_url=item.get("jobUrl", "") or item.get("applyUrl", ""),
                description=_html_to_text(item.get("descriptionHtml", "")),
            )
        )
    return rows


_FETCHERS = {
    "greenhouse": fetch_greenhouse,
    "lever": fetch_lever,
    "ashby": fetch_ashby,
}


def load_boards() -> List[Dict[str, str]]:
    if not ATS_BOARDS_JSON.exists():
        return []
    data = json.loads(ATS_BOARDS_JSON.read_text(encoding="utf-8"))
    boards = data.get("boards", []) if isinstance(data, dict) else data
    return [b for b in boards if isinstance(b, dict) and b.get("ats") and b.get("token")]


def fetch_all_ats(session: requests.Session) -> Dict[str, Any]:
    """Fetch every configured board. One board failing skips only that board.

    Returns {"jobs": [...], "per_board": {label: count}, "errors": [...]}.
    """
    jobs: List[Dict[str, str]] = []
    per_board: Dict[str, int] = {}
    errors: List[str] = []
    for board in load_boards():
        ats = board["ats"].lower()
        token = board["token"]
        company = board.get("company") or token
        label = f"{ats}:{token}"
        fetcher = _FETCHERS.get(ats)
        if not fetcher:
            errors.append(f"{label}: unknown ATS")
            continue
        try:
            board_rows = fetcher(session, company, token)
            jobs.extend(board_rows)
            per_board[label] = len(board_rows)
        except SourceUnavailable as exc:
            errors.append(f"{label}: {exc}")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{label}: unexpected {type(exc).__name__}: {exc}")
    return {"jobs": jobs, "per_board": per_board, "errors": errors}
