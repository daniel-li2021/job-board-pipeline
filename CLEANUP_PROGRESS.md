# Cleanup progress

## Completed — batch 1: configuration directory
- Traced config consumers with CodeGraph and checked tracked code, workflow triggers, tests and docs.
- Renamed `source/` to `config/`; updated runtime paths, referral links, Pages triggers and repository guidance.
- Preserved config contents, profile inputs, generated snapshots and persistent state.
- Validation: visibility tests (51 passing), Python compilation and diff whitespace check.

## Remaining high-value work
- Remove obsolete standalone discovery/screening programs and unused Official adapter import after caller verification.
- Review resume fallbacks and missing-profile behavior before removing historical resume copies.
- Trace duplicated Board/Syncareer utilities, environment/profile loading and large root modules; extract only where it reduces coupling.
- Review persistent-state compatibility and tests against real production invariants; retain needed old-format readers.

## Next recommended batch
Remove confirmed unused collectors and strengthen the Board collection boundary test. Generated `public/` artifacts are rebuilt by Pages; do not regenerate job data for this cleanup.
