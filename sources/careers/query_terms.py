"""Shared role queries for official-careers adapters.

Discovery stays intentionally broad; the shared hard/prefilter/tiering stack
decides what is actionable. Keep this list small enough for twice-daily runs.
"""

ROLE_SEARCH_QUERIES = [
    "ai engineer",
    "machine learning engineer",
    "data engineer",
    "platform engineer",
    "full stack engineer",
    "forward deployed engineer",
    # Keep the broadest query last so per-run detail limits do not consume the
    # entire budget before the specialty coverage queries execute.
    "software engineer",
]
