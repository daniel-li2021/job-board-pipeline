# Cleanup progress

## Completed — batch 1: configuration directory
- Traced config consumers with CodeGraph and checked tracked code, workflow triggers, tests and docs.
- Renamed `source/` to `config/`; updated runtime paths, referral links, Pages triggers and repository guidance.
- Preserved config contents, profile inputs, generated snapshots and persistent state.
- Validation: visibility tests (51 passing), Python compilation and diff whitespace check.

## Completed — batch 2: obsolete collectors
- CodeGraph caller traces plus tracked imports, workflow commands and operational scripts show no production entrypoints for `syncareer_deep_scrape.py`, `google_screening.py` or `scrape_jobs.py`; removed all three (3,049 lines).
- Removed unused `sources/official.py` (152 lines) and Board import; maintained dedicated registry-driven Official discovery.
- Removed Playwright dependency, whose only consumer was the deleted prototype; retained BeautifulSoup used by active adapters.
- Replaced a source-text import assertion with observable Board output/error/network-boundary checks.
- Validation: all 96 offline tests passed in 1.1 seconds; Python compilation, shell syntax and diff checks passed. No crawlers, scoring calls or snapshot writes.

## Completed — batch 3: required matching profiles
- Traced `load_profiles` into Board, Official and Syncareer scoring; all use the tracked `profile/` files.
- Removed two historical resume copies and fallback path constants. Replaced silent read-error/empty-profile behavior with explicit failure before shared scoring.
- Added a regression check covering each required file missing/blank, exact text preservation and cache invalidation on each profile change.
- Validation: 52 visibility tests passed; existing real profile payload and cache fingerprint match the pre-change baseline exactly; diff check passed.

## Completed — batch 4: legacy Syncareer scoring
- CodeGraph traced the isolated `assign_tiers` -> provider/LLM/fallback graph; neither CLI mode calls it. Removed it and its private parser/text helpers, unused local filter definitions and obsolete profile/config constants.
- Removed duplicate Board import; reused Board's identical environment loader and HTTP-session setup without adding a module or changing transport settings.
- Kept the active shared scorer, both CLI modes, independent outputs and persistent-state readers.
- Validation: 52 visibility tests passed, Python compilation and diff check passed. Removed 314 net lines.

## Completed — batch 5: Syncareer dates and meaningful CLI validation
- Replaced Syncareer's seconds-only epoch converter with `sources.schema.to_iso_date`; millisecond/overflow/nonfinite timestamps no longer abort normalization. Valid epoch dates retain the same values.
- Reused `coverage_reconcile.parse_datetime` for retention/inbox dates; preserved date-only, offset and first-seen precedence semantics while treating invalid non-string dates as unknown.
- Replaced mocked scorer results in the CLI test with real shared rule scoring and persisted-watchlist assertions: Tier C remains stored, produces no alert and stays out of the actionable inbox. Peer caches and external calls are isolated.
- Added boundary tests through source normalization and retention. Inspected current watchlist shape (807 entries, string first-seen timestamps); did not rewrite it.
- Validation: 54 visibility tests passed, Python compilation and diff check passed.

## Remaining high-value work
- Trace duplicated Board/Syncareer utilities, environment/profile loading and large root modules; extract only where it reduces coupling.
- Review persistent-state compatibility and tests against real production invariants; retain needed old-format readers.

## Next recommended batch
Trace persistent-store read/write failure behavior: distinguish missing files from corrupt/unreadable files before any overwrite; test compatibility readers and repeated-run preservation. Review duplicated GitHub-output emitters with prefix semantics before consolidating. Avoid splitting large modules until shared dependencies are mapped. Generated `public/` artifacts are rebuilt by Pages; do not regenerate job data for this cleanup.

## Intentionally preserved
- Matching/ranking policy, score cache keys, adapter budgets and source reliability guards.
- Persistent stores, application/review state and old snapshot readers; their migrations need separate evidence.
- Root pipeline entrypoints, `sources/`, `scripts/`, `.codex/`, `.cursor/` and CodeGraph.
- Existing generated outputs; Pages rebuilds the dashboard from stored data after publication.
