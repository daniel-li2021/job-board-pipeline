"""Small, batched AI judgments used only for diagnostic and retrieval triage."""

from __future__ import annotations

import json
from typing import Any, Dict, Iterable, List

import requests

import llm_config


BATCH_SIZE = 25


def decide(
    *, task: str, cases: Iterable[Dict[str, Any]], choices: Iterable[str], api_key: str,
    batch_size: int = BATCH_SIZE,
) -> Dict[str, Dict[str, Any]]:
    """Return only well-formed, keyed decisions; callers own failure fallback."""
    allowed = set(choices)
    rows = list(cases)
    decisions: Dict[str, Dict[str, Any]] = {}
    for start in range(0, len(rows), batch_size):
        batch = rows[start:start + batch_size]
        expected = {str(row["case_id"]) for row in batch}
        instruction = (
            "For an early-career software/AI engineer, prioritize a full job description only when the title could plausibly fit. "
            "Skip obvious senior leadership or unrelated roles. Recover uncertain plausible roles."
            if task == "detail_retrieval" else task
        )
        prompt = {
            "task": instruction,
            "choices": sorted(allowed),
            "instructions": "Return one short result per case. No explanations. Use only supplied evidence; uncertain cases remain ambiguous.",
            "output": {"results": [{"case_id": "string", "decision": "choice", "confidence": "0..1", "priority": "high|medium|low (triage only)"}]},
        }
        response = requests.post(
            llm_config.OPENAI_CHAT_COMPLETIONS_ENDPOINT,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": "gpt-6-luna", "reasoning_effort": "medium",
                "response_format": {"type": "json_object"},
                "messages": [
                    {"role": "developer", "content": json.dumps(prompt, separators=(",", ":"))},
                    {"role": "user", "content": json.dumps({"cases": batch}, separators=(",", ":"))},
                ],
            },
            timeout=90,
        )
        response.raise_for_status()
        payload = response.json()["choices"][0]["message"]["content"]
        parsed = json.loads(payload) if isinstance(payload, str) else payload
        for item in parsed.get("results", []):
            if not isinstance(item, dict):
                continue
            case_id = str(item.get("case_id") or "")
            decision = str(item.get("decision") or "")
            try:
                confidence = float(item.get("confidence"))
            except (TypeError, ValueError):
                continue
            if case_id not in expected or decision not in allowed or not 0 <= confidence <= 1:
                continue
            decisions[case_id] = {
                "decision": decision,
                "confidence": confidence,
                "priority": str(item.get("priority") or "medium") if task == "detail_retrieval" else "",
            }
    return decisions
