"""Shared OpenAI model, context-selection, usage, and pricing helpers."""

from __future__ import annotations

import os
import re
from typing import Any, Dict, Iterable


DEFAULT_MODEL = "gpt-5.6-terra"
DEFAULT_REASONING_EFFORT = "low"
OPENAI_CHAT_COMPLETIONS_ENDPOINT = "https://api.openai.com/v1/chat/completions"
GROQ_CHAT_COMPLETIONS_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
GROQ_FALLBACK_MODEL = "llama-3.1-8b-instant"
JD_CONTEXT_CHARS = 7800
OPENAI_PRICING_SOURCE = "https://developers.openai.com/api/docs/models/gpt-5.6-terra"
OPENAI_PRICING_VERIFIED_DATE = "2026-08-31"

# OpenAI API pricing verified 2026-08-31 from the GPT-5.6 Terra model page.
# USD per one million tokens. Reasoning tokens are included in output tokens.
MODEL_PRICING_USD_PER_MILLION: Dict[str, Dict[str, float]] = {
    "gpt-5.6-terra": {
        "input": 2.00,
        "cached_input": 0.20,
        "output": 12.00,
    },
}

_REQUIRED_HEADING_RE = re.compile(
    r"(?im)^\s*(?:minimum|required|basic|must[- ]have)\s+qualifications?\s*[:\-]?\s*$"
)
_RESPONSIBILITY_HEADING_RE = re.compile(
    r"(?im)^\s*(?:responsibilities|what you(?:'|’)ll do|the role|role responsibilities)\s*[:\-]?\s*$"
)
_ANY_HEADING_RE = re.compile(r"(?m)^\s*[A-Z][A-Za-z0-9 &/'’(),+\-]{2,70}\s*[:\-]?\s*$")


def configured_model() -> str:
    return (os.getenv("OPENAI_MODEL") or DEFAULT_MODEL).strip()


def configured_reasoning_effort() -> str:
    return (os.getenv("OPENAI_REASONING_EFFORT") or DEFAULT_REASONING_EFFORT).strip()


def _section(text: str, heading: re.Pattern[str], max_chars: int) -> str:
    chunks = []
    for match in heading.finditer(text):
        following = text[match.start() :]
        next_heading = _ANY_HEADING_RE.search(following, max(1, match.end() - match.start()))
        end = next_heading.start() if next_heading else len(following)
        chunk = following[:end].strip()
        if chunk and chunk not in chunks:
            chunks.append(chunk)
        if sum(len(c) for c in chunks) >= max_chars:
            break
    return "\n\n".join(chunks)[:max_chars]


def select_jd_context(text: str, max_chars: int = JD_CONTEXT_CHARS) -> str:
    """Keep a broad JD view while guaranteeing core sections survive truncation."""
    value = (text or "").strip()
    if len(value) <= max_chars:
        return value
    required = _section(value, _REQUIRED_HEADING_RE, 4200)
    responsibilities = _section(value, _RESPONSIBILITY_HEADING_RE, 2600)
    # Some APIs flatten headings into one long line. Preserve the surrounding
    # qualification/responsibility text even when line-based sections vanish.
    if not required:
        hit = re.search(r"(?i)\b(?:minimum|required|basic|must[- ]have)\s+qualifications?\b", value)
        if hit:
            required = value[hit.start() : hit.start() + 4200]
    if not responsibilities:
        hit = re.search(r"(?i)\b(?:responsibilities|what you(?:'|’)ll do|role responsibilities)\b", value)
        if hit:
            responsibilities = value[hit.start() : hit.start() + 2600]
    selected = "\n\n".join(part for part in (responsibilities, required) if part)
    remaining = max_chars - len(selected) - (2 if selected else 0)
    intro = value[: max(0, remaining)].strip()
    result = "\n\n".join(part for part in (intro, selected) if part)
    return result[:max_chars]


def empty_usage(model: str | None = None) -> Dict[str, Any]:
    return {
        "model": model or configured_model(),
        "api_requests": 0,
        "jobs_scored": 0,
        "input_tokens": 0,
        "cached_input_tokens": 0,
        "output_tokens": 0,
        "reasoning_tokens": 0,
        "estimated_usd": 0.0,
    }


def usage_from_response(payload: Dict[str, Any], model: str) -> Dict[str, Any]:
    usage = payload.get("usage") or {}
    prompt_details = usage.get("prompt_tokens_details") or usage.get("input_tokens_details") or {}
    completion_details = usage.get("completion_tokens_details") or usage.get("output_tokens_details") or {}
    return {
        "model": model,
        "api_requests": 1,
        "jobs_scored": 0,
        "input_tokens": int(usage.get("prompt_tokens") or usage.get("input_tokens") or 0),
        "cached_input_tokens": int(prompt_details.get("cached_tokens") or 0),
        "output_tokens": int(usage.get("completion_tokens") or usage.get("output_tokens") or 0),
        "reasoning_tokens": int(completion_details.get("reasoning_tokens") or 0),
        "estimated_usd": 0.0,
    }


def merge_usage(target: Dict[str, Any], additions: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    total_cost = float(target.get("estimated_usd", 0) or 0)
    for item in additions:
        if item.get("model"):
            existing = [m.strip() for m in str(target.get("model") or "").split(",") if m.strip()]
            if item["model"] not in existing:
                existing.append(str(item["model"]))
            target["model"] = ", ".join(existing)
        for key in (
            "api_requests", "jobs_scored", "input_tokens", "cached_input_tokens",
            "output_tokens", "reasoning_tokens",
        ):
            target[key] = int(target.get(key, 0) or 0) + int(item.get(key, 0) or 0)
        total_cost += float(item.get("estimated_usd") or estimate_cost_usd(item))
    target["estimated_usd"] = round(total_cost, 6)
    return target


def estimate_cost_usd(usage: Dict[str, Any]) -> float:
    rates = MODEL_PRICING_USD_PER_MILLION.get(str(usage.get("model") or ""))
    if not rates:
        return 0.0
    total_input = int(usage.get("input_tokens", 0) or 0)
    cached = min(total_input, int(usage.get("cached_input_tokens", 0) or 0))
    uncached = total_input - cached
    output = int(usage.get("output_tokens", 0) or 0)
    cost = (
        uncached * rates["input"]
        + cached * rates["cached_input"]
        + output * rates["output"]
    ) / 1_000_000
    return round(cost, 6)


def format_usage(usage: Dict[str, Any]) -> str:
    return (
        f"model {usage.get('model') or '-'} / API requests {usage.get('api_requests', 0)} / "
        f"jobs scored {usage.get('jobs_scored', 0)} / tokens input {usage.get('input_tokens', 0)} "
        f"(cached {usage.get('cached_input_tokens', 0)}) / output {usage.get('output_tokens', 0)} "
        f"(reasoning {usage.get('reasoning_tokens', 0)}) / estimated cost "
        f"${float(usage.get('estimated_usd', 0) or 0):.4f}"
    )
