"""Shared role queries for official-careers adapters.

Discovery stays intentionally broad; the shared hard/prefilter/tiering stack
decides what is actionable. Keep this list small enough for twice-daily runs.
"""

from typing import Any, Dict, List

ROLE_SEARCH_QUERIES = [
    "ai engineer",
    "machine learning engineer",
    "data scientist",
    "solutions architect",
    "data engineer",
    "platform engineer",
    "full stack engineer",
    "forward deployed engineer",
    # Keep the broadest query last so specialty discovery runs first.
    "software engineer",
]

QUERY_PAGE_BUDGETS = {
    "software engineer": 20,
    "ai engineer": 6,
}
DEFAULT_QUERY_PAGE_BUDGET = 3


def query_page_budget(query: str, safety_cap: int) -> int:
    """Apply the shared role-query ceiling without weakening source caps."""
    normalized = " ".join(str(query or "").lower().split()).strip('"')
    return min(safety_cap, QUERY_PAGE_BUDGETS.get(normalized, DEFAULT_QUERY_PAGE_BUDGET))


def query_diagnostic(
    query: str,
    page_budget: int,
    pages_fetched: int,
    raw_jobs: int,
    unique_jobs: int,
    contributed: List[Dict[str, Any]],
    elapsed_seconds: float,
) -> Dict[str, Any]:
    return {
        "query": query,
        "group": "official",
        "page_budget": page_budget,
        "pages_fetched": pages_fetched,
        "stop_reason": "page_budget" if pages_fetched >= page_budget else "early_stop",
        "raw_jobs": raw_jobs,
        "unique_jobs": unique_jobs,
        "unique_contribution": len(contributed),
        "first_pass_survivors": len(contributed),
        "original_postings_resolved": sum(bool(job.get("official_url")) for job in contributed),
        "jds_resolved": sum(bool(job.get("description")) for job in contributed),
        "elapsed_seconds": round(elapsed_seconds, 3),
    }
