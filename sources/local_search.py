"""Shared query groups for local-only aggregator discovery."""

from __future__ import annotations

from typing import Dict, Iterator, Tuple

KEYWORD_GROUPS = {
    "primary": ["software engineer", "ai engineer"],
    "secondary": [
        "software engineer i", "software engineer ii", "associate software engineer",
        "new grad software engineer", "backend engineer", "full stack engineer",
        "platform engineer", "applied ai engineer", "machine learning engineer",
        "ml engineer", "llm engineer",
    ],
    "specialty": [
        "infrastructure engineer", "site reliability engineer",
        "forward deployed engineer", "data engineer",
    ],
}

SOURCE_PAGE_BUDGETS = {
    "linkedin": {"primary": 25, "secondary": 8, "specialty": 4},
    # One JobSpy page per query. Raise only after unique-contribution data says
    # another page is worth the extra requests.
    "indeed": {"primary": 1, "secondary": 1, "specialty": 1},
    "glassdoor": {"primary": 1, "secondary": 1, "specialty": 1},
}


def source_queries(source: str) -> Iterator[Tuple[str, str, int]]:
    for group, queries in KEYWORD_GROUPS.items():
        for query in queries:
            yield group, query, SOURCE_PAGE_BUDGETS[source][group]


def query_stat(query: str, group: str, page_budget: int) -> Dict[str, object]:
    return {
        "query": query,
        "group": group,
        "page_budget": page_budget,
        "pages_fetched": 0,
        "stop_reason": "page_budget",
        "raw_jobs": 0,
        "unique_jobs": 0,
        "unique_contribution": 0,
        "first_pass_survivors": 0,
        "original_postings_resolved": 0,
        "jds_resolved": 0,
        "elapsed_seconds": 0.0,
    }
