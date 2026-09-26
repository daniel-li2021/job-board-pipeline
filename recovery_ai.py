"""Compact, best-effort Luna decisions for metadata recovery."""

from __future__ import annotations

import json
import os

import requests

import llm_config
import recovery_policy

BATCH_SIZE = 25
MODEL = "gpt-6-luna"


def _ask(task: str, rows: list[dict]) -> dict:
    key = os.getenv("OPENAI_API_KEY", "").strip()
    if not key or not rows:
        return {}
    response = requests.post(
        llm_config.OPENAI_CHAT_COMPLETIONS_ENDPOINT,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={
            "model": MODEL, "reasoning_effort": "medium",
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "developer", "content": task + " Return JSON object with results array. No prose."},
                {"role": "user", "content": json.dumps({"jobs": rows}, separators=(",", ":"))},
            ],
        }, timeout=60,
    )
    response.raise_for_status()
    data = json.loads(response.json()["choices"][0]["message"]["content"])
    return data if isinstance(data, dict) else {}


def triage(jobs: list[dict], profile: str = "") -> dict[str, dict]:
    """High-confidence skips save web work; errors and incomplete output fail open."""
    task = (
        "For an early-career software/AI job search, triage metadata only. "
        "Skip only clearly irrelevant or senior jobs. Treat uncertainty as recover. "
        "Each result: id, action(skip|recover), priority(high|normal|low), "
        "confidence(0..1), delta(integer -7..5), reason(max 8 words). "
        f"Candidate context: {profile[:1200]}"
    )
    out: dict[str, dict] = {}
    for start in range(0, len(jobs), BATCH_SIZE):
        batch = jobs[start:start + BATCH_SIZE]
        rows = [{"id": recovery_policy.identity(j), "c": j.get("company", ""),
                 "t": j.get("title", ""), "l": j.get("location", "")}
                for j in batch]
        try:
            decisions = _ask(task, rows).get("results", [])
        except (requests.RequestException, ValueError, KeyError, TypeError):
            continue
        valid = {row["id"] for row in rows}
        for item in decisions if isinstance(decisions, list) else []:
            if not isinstance(item, dict) or item.get("id") not in valid:
                continue
            try:
                confidence = float(item.get("confidence", 0))
                delta = int(item.get("delta", 0))
            except (ValueError, TypeError):
                continue
            out[item["id"]] = {
                "action": "skip" if item.get("action") == "skip" and confidence >= .85 else "recover",
                "priority": item.get("priority") if item.get("priority") in {"high", "normal", "low"} else "normal",
                "confidence": max(0.0, min(1.0, confidence)),
                "delta": max(-7, min(5, delta)) if confidence >= .85 else 0,
                "reason": str(item.get("reason") or "")[:80],
            }
    return out


def rank_candidates(items: list[tuple[dict, list[dict]]]) -> dict[str, list[str]]:
    """Rank several jobs together; deterministic order survives API failure."""
    out: dict[str, list[str]] = {}
    task = (
        "Rank likely official job-description pages. For each id return ordered candidate "
        "indices best first, using only the listed candidates. Each result: id, order(array of integers), confidence(0..1)."
    )
    for start in range(0, len(items), BATCH_SIZE):
        batch = items[start:start + BATCH_SIZE]
        rows = [{"id": recovery_policy.identity(job), "c": job.get("company", ""),
                 "t": job.get("title", ""), "l": job.get("location", ""),
                 "candidates": [{"i": i, "domain": c.get("domain", ""),
                                 "title": str(c.get("title") or "")[:100],
                                 "snippet": str(c.get("snippet") or "")[:180]}
                                for i, c in enumerate(candidates)]}
                for job, candidates in batch]
        try:
            results = _ask(task, rows).get("results", [])
        except (requests.RequestException, ValueError, KeyError, TypeError):
            results = []
        by_id = {item.get("id"): item for item in results if isinstance(item, dict)} if isinstance(results, list) else {}
        for job, candidates in batch:
            key = recovery_policy.identity(job)
            proposed = by_id.get(key, {}).get("order", [])
            indices = [i for i in proposed if isinstance(i, int) and 0 <= i < len(candidates)] if isinstance(proposed, list) else []
            indices = list(dict.fromkeys([*indices, *range(len(candidates))]))
            out[key] = [candidates[i]["url"] for i in indices]
    return out
