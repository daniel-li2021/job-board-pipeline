"""Shared HTTP helpers for official-careers adapters."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any, Dict, Optional

import requests

from ..schema import SourceUnavailable, normalize_space

REQUEST_TIMEOUT = 30
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
DEFAULT_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.9",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    return session


def raise_for_status(resp: requests.Response, label: str) -> None:
    if resp.status_code in (401, 403, 429):
        raise SourceUnavailable(f"{label} blocked with HTTP {resp.status_code}")
    if resp.status_code >= 400:
        raise SourceUnavailable(f"{label} HTTP {resp.status_code}")


def http_get(
    session: requests.Session,
    url: str,
    *,
    label: str,
    params: Any = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = REQUEST_TIMEOUT,
) -> requests.Response:
    try:
        resp = session.get(url, params=params, headers=headers, timeout=timeout)
    except requests.RequestException as exc:
        raise SourceUnavailable(f"{label} network error: {exc}") from exc
    raise_for_status(resp, label)
    return resp


def http_post(
    session: requests.Session,
    url: str,
    *,
    label: str,
    json_body: Optional[Dict[str, Any]] = None,
    params: Any = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = REQUEST_TIMEOUT,
) -> requests.Response:
    try:
        resp = session.post(url, params=params, json=json_body, headers=headers, timeout=timeout)
    except requests.RequestException as exc:
        raise SourceUnavailable(f"{label} network error: {exc}") from exc
    raise_for_status(resp, label)
    return resp


def html_to_text(value: str) -> str:
    if not value:
        return ""
    try:
        from bs4 import BeautifulSoup

        text = BeautifulSoup(value, "html.parser").get_text(" ", strip=True)
    except Exception:  # noqa: BLE001
        text = re.sub(r"<[^>]+>", " ", value)
    return normalize_space(text)


PLACEHOLDER_LOCATION_RE = re.compile(
    r"^(new city|\d+\s+locations?|multiple locations?|various locations?|several locations?)$",
    re.IGNORECASE,
)
REMOTE_US_RE = re.compile(
    r"\b(remote[\s,\-/]*(us|usa|u\.s\.|united states)|(us|usa|u\.s\.|united states)[\s,\-/]*remote)\b",
    re.IGNORECASE,
)
WORKDAY_US_PATH_RE = re.compile(r"(?:/job/)?US[-,_]", re.IGNORECASE)


def location_from_workday_path(external_path: str) -> str:
    """Turn ``/job/US-CA-Santa-Clara/Title_JR`` into ``US, CA, Santa Clara``."""
    path = normalize_space(external_path).replace("\\", "/")
    match = re.search(r"/job/([^/]+)/", path)
    slug = match.group(1) if match else ""
    if not slug:
        return ""
    slug = slug.replace("_", " ")
    parts = [p for p in slug.split("-") if p]
    if not parts:
        return ""
    if len(parts) >= 3 and parts[0].upper() == "US" and len(parts[1]) == 2:
        return ", ".join([parts[0], parts[1], " ".join(parts[2:])])
    return ", ".join(parts)


def is_placeholder_location(location: str) -> bool:
    return bool(PLACEHOLDER_LOCATION_RE.match(normalize_space(location)))


def keep_us_or_unknown(location: str, *, path_hint: str = "") -> bool:
    """US-only discovery filter for official career sites.

    Keep when any listed office is US, or the role is explicit Remote-US.
    Multi-office rows stay if at least one office is US.
    Drop when every listed office is confirmed non-US.
    Workday ``/job/US-...`` paths count as US even if the card says "2 Locations".
    """
    from ..schema import classify_location_bucket

    if path_hint and WORKDAY_US_PATH_RE.search(path_hint):
        loc = normalize_space(location)
        if loc and classify_location_bucket(loc) == "non_us" and not is_placeholder_location(loc):
            # Path says US but the only human location is foreign — still keep
            # multi-office US+abroad; drop only when the text is purely non-US
            # and not a placeholder.
            parts = [p.strip() for p in re.split(r"[;|/]", loc) if p.strip()]
            if parts and all(classify_location_bucket(p) == "non_us" for p in parts):
                if not any(classify_location_bucket(p) == "us" for p in parts):
                    return False
        return True
    loc = normalize_space(location)
    if not loc or is_placeholder_location(loc):
        return True  # unresolved card; caller should fill from details/path
    if REMOTE_US_RE.search(loc):
        return True
    parts = [p.strip() for p in re.split(r"[;|/]", loc) if p.strip()]
    if not parts:
        return True
    buckets = [classify_location_bucket(p) for p in parts]
    if "us" in buckets:
        return True
    if all(b == "non_us" for b in buckets):
        return False
    return True


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (title or "").lower()).strip("-")
    return slug[:120]
