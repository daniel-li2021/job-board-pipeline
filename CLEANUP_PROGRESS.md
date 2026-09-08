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

## Completed — batch 6: Syncareer persistent-state read safety
- CodeGraph traced both seen-ID and watchlist readers through CLI writes. Corrupt JSON or invalid store structure now raises instead of being treated as empty and later overwritten; missing files still initialize empty stores.
- Kept legacy watchlist fallback only when the current path is absent. Preserved list/envelope/keyed-entry formats, including restoring job IDs from keyed entries so save/reload does not lose them.
- Added malformed-state checks and round-trip coverage retaining review fields, scores, tiers and first-seen dates. Verified the current 807 watchlist records read identically.
- Validation: 56 visibility tests passed, Python compilation and diff check passed; no persisted production outputs changed.

## Completed — batch 7: shared persistent-state safety
- Added a small standard-library atomic replacement helper, reusing the sibling-temp pattern already present in local snapshots but with unique temp names and cleanup. Applied it to owned job/seen/digest/review/history/raw stores and local snapshots/health; JSON and gzip formatting stay unchanged.
- Board/Official owner reads now reject corruption; optional peer-cache reads remain nonblocking. Official reuses Board's job-store reader. Invalid compressed raw snapshots cannot be silently replaced during merge.
- Digest/history/review owners preserve corrupt state for repair rather than resetting it. Review status updates retain existing notes; corrected stale CLI instructions about Supabase and Pages.
- Validation: all 105 tests passed, including failed-write preservation and owner/peer behavior; existing 13,082 Board and 22,468 Official entries read identically; current digests/history passed validation. Production outputs untouched.

## Completed — batch 8: shared helpers and repeated runs (`6fe96e6`)
- Shared the canonical UTC/date-only parser at the schema layer, fixing Board/Official retention on naive dates and alert-history interpretation across host timezones. Syncareer run stamps are now UTC consistently with history consumers.
- Reused Board's store writer for Official and its GitHub-output emitter for Syncareer, retaining Syncareer's explicit unprefixed output and Board/Official environment-prefix behavior.
- Repeated-run CLI coverage verifies no duplicate detail request and preservation of first_seen, score, tier, review status and notes. All 107 tests passed for this batch.
- Reconciled against current main through `58c3057`; subsequent commits `8852e36`, `4638d2b`, and `58c3057` contain routine pipeline outputs, not additional cleanup changes.

## Completed — batch 9: final dead-code and compatibility audit
- CodeGraph and tracked-reference checks confirmed the old Syncareer company registry only served an obsolete count test; removed it, the uncalled `dedup_merge` alias, and four uncalled schema/Workday convenience helpers.
- Corrected mutable list defaults shared between retained records; each record now owns its default lists, matching the existing dict-factory pattern.
- Replaced the live-generated-issue test with a writer/parser round trip; replaced obsolete company-count checks with the active keyword-search contract. Removed redundant runner string assertions already covered by its local Git integration test.
- Preserved active legacy record normalization, score aliases, snapshot formats and strict incremental-cache date parsing where behavior differs intentionally. Root entrypoints remain in place; transports and reports have source-specific contracts and do not warrant another abstraction.
- Validation: all 108 tests passed in the isolated cleanup worktree. Concurrent dashboard edits in the primary checkout were left to their owning task.

## Completed — batch 10: workflow and documentation review
- Pages now rebuilds for the shared code, source modules, company filters and dependencies its renderer consumes. Independent source workflows and external schedules remain unchanged.
- Board/Syncareer staging errors now fail publication instead of being hidden. Official free-form dispatch values enter the shell through environment variables, with an executed shell-contract test proving command-substitution text remains a literal argument.
- Updated README state-recovery, UTC/Pacific and validation instructions. Reviewed root modules, adapters, operational scripts, workflow/output boundaries and compatibility paths; no further high-value deletion or structural change is supported by the traced call graph.
- Final offline validation: 109 regression tests and the scheduler contract test pass; tracked Python modules compile; local runner shell syntax and diff checks pass. Rendered the dashboard from existing snapshots into a temporary directory with network access blocked.

## Completion status
All identified high-value cleanup/correctness work is implemented. Final cleanup commits integrate cleanly with current main through `7353923`, including the newer dashboard and local-source work. Integrated validation on 2026-09-08: 114 regression tests ran, 113 passed and one JobSpy-dependent transport test was skipped because local collector dependencies are not installed; the offline scheduler contract, tracked Python compilation, shell syntax and diff checks passed. No implementation batch remains. Remote publication and Pages verification are the final delivery checks.

## Intentionally preserved
- Matching/ranking policy, score cache keys, adapter budgets and source reliability guards.
- Existing persistent contents, application/review status and needed legacy snapshot/store formats; current read/write contracts remain compatible.
- Root pipeline entrypoints, `sources/`, `scripts/`, `.codex/`, `.cursor/` and CodeGraph.
- Generated job data and scores; only Pages rendering uses stored data after publication.
- Source-specific HTML parsing, strict incremental-cache timestamps, protected-source policies, matching thresholds and current Supabase access policy. These have active contracts; changing them would exceed cleanup.
- Concurrent dashboard/local-source changes in the primary checkout remain owned by their respective tasks. Cleanup integration must not overwrite them.
