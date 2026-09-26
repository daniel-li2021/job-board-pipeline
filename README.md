# Job board pipeline

Three independent job-discovery pipelines feed one public dashboard and share the same filtering/matching stack.

| Pipeline | Script | Main inbox |
|---|---|---|
| **Syncareer** | `daily_pipeline.py` | [`output/syncareer/inbox.md`](output/syncareer/inbox.md) |
| **ATS / broad job boards** | `board_pipeline.py` | [`output/board/inbox.md`](output/board/inbox.md) |
| **Official Careers** | `official_careers.py` | [`output/official_careers/inbox.md`](output/official_careers/inbox.md) |

Each inbox is the rolling **last 3 days** of actionable jobs. `latest.md` is the wider 7-day view.

Public dashboard: **https://daniel-li2021.github.io/job-board-pipeline/**

Detailed current flow and ownership: [`docs/PIPELINE_ALGORITHM.md`](docs/PIPELINE_ALGORITHM.md)

## Architecture

### 1. Syncareer

Searches Syncareer, applies the shared hard filters and matching policy, maintains a rolling watchlist, and opens a GitHub Issue when a run finds new actionable jobs.

```bash
python3 daily_pipeline.py --alert --time last3days
```

Outputs live under `output/syncareer/`.

### 2. ATS / broad job boards

`board_pipeline.py` combines:

- public ATS boards such as Greenhouse / Lever / Ashby;
- GitHub-collected Indeed and Mac-collected LinkedIn and Glassdoor snapshots;
- cross-source deduplication and official-link verification.

```bash
python3 board_pipeline.py --local-out
python3 board_pipeline.py --local-out --no-llm
python3 board_pipeline.py --skip-network
```

GitHub's 8:20 AM / 5:20 PM Pacific Board dispatch runs Indeed collection, ATS discovery, online JD recovery, then matching/LLM. Online company/title recovery shares a limit of 100 search queries and 150 candidate-page fetches per run, with a 15-minute deadline. GitHub does not request LinkedIn. The Mac launchd job owns LinkedIn and Glassdoor; install its dependencies with `python3 -m pip install -r requirements-local.txt`. The Mac job runs at noon, 3 PM, and 9 PM Pacific, plus one gated catch-up after wake; it never starts from 5:00–5:59 PM. Its LinkedIn discovery searches Software Engineer, AI Engineer, Backend Engineer, Full-Stack Engineer, and Machine Learning Engineer with a 14-page total limit and separate LinkedIn cooldown controls. Mac JD recovery processes every candidate without a global search/page cap, reusing the committed Indeed snapshot before web or targeted LinkedIn detail. [`output/sources/health.json`](output/sources/health.json) records last attempts and last-good snapshots.

Board run stats report exact LinkedIn/Indeed/Glassdoor overlap, each source's unique contribution, per-query exact-unique counts, and the full enrichment funnel. Discovery depth is bounded, but every discovered record is processed; there is no post-discovery job-count cap.

Outputs live under `output/board/`.

### 3. Official Careers

`official_careers.py` discovers relevant US jobs directly from large-company career sites and then sends them through the same matching stack as the other pipelines.

```bash
python3 official_careers.py run
python3 official_careers.py scrape --only google
python3 official_careers.py match --no-llm
```

Registry: [`config/official_careers.json`](config/official_careers.json)

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

Referral companies have one source of truth: [`config/target_companies.json`](config/target_companies.json).

## Official coverage reconciliation

`coverage_reconcile.py` compares recent Board/Syncareer jobs with the latest Official snapshot.

Important states:

- `official_duplicate` — exact Official counterpart found, so the external copy is suppressed regardless of manual company validation;
- `pending_official_refresh` — external job is newer than the latest Official snapshot or that company is awaiting refresh;
- `official_gap` — comparable external job was observed but no exact Official counterpart was found;
- `official_unsupported` — Official adapter is intentionally unavailable/link-only.

Manual validation lives in [`profile/official_coverage.json`](profile/official_coverage.json) for coverage auditing. Unmatched external jobs are never hidden just because a company has an Official adapter.

## Schedule

AWS EventBridge Scheduler dispatches the independent workflows at these
**America/Los_Angeles** times:

| Workflow | Morning | Evening |
|---|---:|---:|
| Indeed → ATS / Board | 8:20 AM | 5:20 PM |
| Syncareer | 7:50 AM | 4:50 PM |
| Official Careers | 7:30 AM | 4:30 PM |

Reconcile + Pages runs after every completed discovery workflow so failures are visible in health reporting.
Its push and manual triggers remain available; it has no redundant timer.

Each discovery workflow is independently runnable with `workflow_dispatch`.

The [external scheduler](infra/scheduler/README.md) uses a shared Lambda dispatcher,
fixed Pacific wall-clock schedules, retry policies, and an SQS failure queue. GitHub
cron blocks were removed after end-to-end verification. The optional `scheduler_probe`
dispatch input verifies trigger receipt without crawling or scoring.

## Alerts and outputs

Each pipeline keeps its own state and output directory. A failure in one pipeline does not block the others.

GitHub keeps only the small durable/current state each independent pipeline owns:

- `output/*/inbox.md` — rolling 3-day actionable view;
- `output/*/latest.md` — wider current view where available;
- `output/*/seen_jobs.json` — permanent lightweight identity history;
- `output/*/jobs.json` — compact current 7-day board state;
- `output/cross_pipeline/` — coverage audit artifacts when generated;
- `public/` — generated dashboard files.

Full descriptions, source snippets, enrichment/LLM evidence, raw Official snapshots,
and full scoring caches stay under gitignored `output/cache/`. Per-run diagnostics
under `output/*/runs/` are local or workflow artifacts, not repository history.
GitHub commits `output/sources/indeed.json` with full Indeed JDs and its health state;
the Mac reads that snapshot as an exact peer and never recollects Indeed.
In-progress and applied jobs remain durable in the existing Supabase-backed review
state, so pipelines do not contend on a shared `tracked_jobs.json` commit.

User-facing digests are deduplicated so reruns, rescoring, and ordinary JD changes do not repeatedly alert the same job.

## Main configuration

- `config/official_careers.json` — Official company registry and adapter configuration;
- `config/ats_boards.json` — reusable ATS sources;
- `config/target_companies.json` — referral companies;
- `profile/company_filters.json` — exclusions, staffing, clearance-risk, and visibility rules;
- `profile/official_coverage.json` — manual Official validation state;
- `sources/careers/query_terms.py` — shared Official role-search queries.

Company profiles use only `size`, `maturity`, `sponsor`, `type`, names/aliases, and screening-relevant tags for offline enrichment. The dashboard keeps new unprofiled companies in `profile/company_profiles_pending.json` with unknown screening fields; it preserves any values already filled there. Each pending entry also keeps `seen_count` and compact `seen_job_keys`, so repeat pipeline runs do not count the same job again. Older entries without retained job keys have a conservative minimum `seen_count` of 1. To list companies seen in at least two or three distinct jobs, run `python3 scripts/pending_company_subset.py 2` or `python3 scripts/pending_company_subset.py 3`; the JSON output includes the number and subset (without job-key hashes). To import curated findings, run:

```bash
python3 scripts/enrich_company_profiles.py --findings /path/to/batch1.json --findings /path/to/batch2.json --apply
```

Add `--data-dir /path/to/downloads` when USCIS/DOL/SEC enrichment is needed; it reads `Employer Information.csv`, the FY2024–FY2026 LCA workbooks, and `company_tickers.json`. Omit `--apply` to preview counts. The script does not crawl or use an API. It keeps unknown values when evidence is absent, preserves existing size and conflicting classifications, and writes uncertain matches to `profile/company_profiles_manual_review.json`. JD sponsorship remains authoritative over company-level values. Raw downloads are local inputs, not committed artifacts.

## State and validation

Owned job stores, watchlists, digest histories and the optional committed review overlay reject corrupt data rather than resetting it. Writes use atomic replacement to retain the previous complete file if writing fails. Missing files can initialize empty state; unavailable optional peer caches do not block another pipeline. Supported legacy record formats remain readable.

Matching requires nonempty `profile/candidate_profile.md`, `profile/resume_swe.md`, and `profile/resume_ai.md`. Missing or blank inputs stop scoring; no legacy resume fallback is used. Run stamps and persisted timestamps use UTC; display and schedules use Pacific time.

Run the offline regression checks without crawling, scoring API calls, or generated-output updates:

```bash
python3 -m unittest discover -s tests -q
python3 infra/scheduler/test_scheduler.py
bash -n scripts/local_source_sync.sh
```

These cover matching/cache invariants, adapters, state recovery, repeated runs, dashboard rendering and the local runner. Cleanup decisions and validation are recorded in [CLEANUP_PROGRESS.md](CLEANUP_PROGRESS.md).
