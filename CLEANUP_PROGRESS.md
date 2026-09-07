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

## Remaining high-value work
- Review resume fallbacks and missing-profile behavior before removing historical resume copies.
- Trace duplicated Board/Syncareer utilities, environment/profile loading and large root modules; extract only where it reduces coupling.
- Review persistent-state compatibility and tests against real production invariants; retain needed old-format readers.

## Next recommended batch
Remove confirmed unused collectors and strengthen the Board collection boundary test. Generated `public/` artifacts are rebuilt by Pages; do not regenerate job data for this cleanup.
