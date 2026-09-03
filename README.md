# Job board pipeline

Three independent job-discovery pipelines feed one public dashboard and share the same filtering/matching stack.

| Pipeline | Script | Main inbox |
|---|---|---|
| **Syncareer** | `daily_pipeline.py` | [`output/syncareer/inbox.md`](output/syncareer/inbox.md) |
| **ATS / LinkedIn / Glassdoor** | `board_pipeline.py` | [`output/board/inbox.md`](output/board/inbox.md) |
| **Official Careers** | `official_careers.py` | [`output/official_careers/inbox.md`](output/official_careers/inbox.md) |

Each inbox is the rolling **last 3 days** of actionable jobs. `latest.md` is the wider 7-day view.

Public dashboard: **https://daniel-li2021.github.io/job-board-pipeline/**

## Architecture

### 1. Syncareer

Searches Syncareer, applies the shared hard filters and matching policy, maintains a rolling watchlist, and opens a GitHub Issue when a run finds new actionable jobs.

```bash
python3 daily_pipeline.py --alert --time last3days
```

Outputs live under `output/syncareer/`.

### 2. ATS / LinkedIn / Glassdoor

`board_pipeline.py` combines:

- public ATS boards such as Greenhouse / Lever / Ashby;
- locally collected LinkedIn and Glassdoor snapshots;
- cross-source deduplication and official-link verification.

```bash
python3 board_pipeline.py --local-out
python3 board_pipeline.py --local-out --no-llm
python3 board_pipeline.py --skip-network
```

GitHub runners do **not** scrape LinkedIn/Glassdoor directly. The Mac launchd job runs `local_sources.py` through `scripts/local_source_sync.sh` roughly every 3 hours and pushes only `output/sources/*.json`.

Outputs live under `output/board/`.

### 3. Official Careers

`official_careers.py` discovers relevant US jobs directly from large-company career sites and then sends them through the same matching stack as the other pipelines.

```bash
python3 official_careers.py run
python3 official_careers.py scrape --only google
python3 official_careers.py match --no-llm
```

Registry: [`source/official_careers.json`](source/official_careers.json)

Per-company scrape diagnostics: [`output/official_careers/scrape_report.md`](output/official_careers/scrape_report.md)

Official discovery is **role-targeted, not guaranteed to enumerate every posting at every company**. Many adapters search a shared set of SWE / AI / data / platform / FDE role families, with company-specific extra queries where useful. Generic ATS adapters may fetch the full board. Cross-pipeline coverage is used to identify observed jobs that Official may have missed.

Outputs live under `output/official_careers/`.

## Shared matching

All three pipelines reuse `board_pipeline.py` rather than maintaining separate ranking logic:

`hard_filter -> role_seniority_prefilter -> score_survivors -> assign_tier -> user_facing_sort_key`

The matcher uses:

- `candidate_profile.md`;
- routed `resume_swe.md` / `resume_ai.md`;
- deterministic hard filters and role/seniority gates;
- cached LLM scoring for eligible jobs;
- rule-based fallback when a JD is too thin, the API is unavailable, or LLM scoring is intentionally skipped.

Tier A/B/C is deterministic after scoring. Referral status affects action/ranking, not the underlying match score.

Referral companies have one source of truth: [`source/target_companies.json`](source/target_companies.json).

## Official coverage reconciliation

`coverage_reconcile.py` compares recent Board/Syncareer jobs with the latest Official snapshot.

Important states:

- `covered_unvalidated` — exact Official counterpart found, but company coverage has not been manually trusted yet;
- `official_duplicate` — exact counterpart found for a manually validated company and external alert can be suppressed;
- `pending_official_refresh` — external job is newer than the latest Official snapshot or that company is awaiting refresh;
- `official_gap` — comparable external job was observed but no exact Official counterpart was found;
- `official_unsupported` — Official adapter is intentionally unavailable/link-only.

Manual validation lives in [`profile/official_coverage.json`](profile/official_coverage.json). Unmatched external jobs are never hidden just because a company has an Official adapter.

## Schedule

GitHub Actions target the following **America/Los_Angeles** times:

| Workflow | Morning | Evening |
|---|---:|---:|
| ATS / LinkedIn board | 8:07 AM | 5:07 PM |
| Syncareer | 8:10 AM | 5:10 PM |
| Official Careers | 8:30 AM | 5:20 PM |
| Reconcile + Pages fallback | 9:30 AM | 9:30 PM |

Reconcile + Pages also runs after successful completion of any of the three discovery workflows. GitHub scheduled workflows can occasionally start later than their target cron time.

Each discovery workflow is independently runnable with `workflow_dispatch`.

## Alerts and outputs

Each pipeline keeps its own state and output directory. A failure in one pipeline does not block the others.

Useful files:

- `output/*/inbox.md` — rolling 3-day actionable view;
- `output/*/latest.md` — wider current view where available;
- `output/*/runs/` — per-run diagnostics/snapshots;
- `output/*/jobs.json` or watchlist state — dedup/matching history;
- `output/cross_pipeline/` — coverage audit artifacts when generated;
- `public/` — generated dashboard files.

User-facing digests are deduplicated so reruns, rescoring, and ordinary JD changes do not repeatedly alert the same job.

## Main configuration

- `source/official_careers.json` — Official company registry and adapter configuration;
- `source/ats_boards.json` — reusable ATS sources;
- `source/target_companies.json` — referral companies;
- `profile/company_filters.json` — exclusions, staffing, clearance-risk, and visibility rules;
- `profile/official_coverage.json` — manual Official validation state;
- `sources/careers/query_terms.py` — shared Official role-search queries.

## Tests

Current regression suites live under `tests/`:

- `test_matching_incremental.py`
- `test_official_careers_adapters.py`
- `test_visibility.py`
