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

GitHub's 8:20 AM / 5:20 PM Pacific Board dispatch runs Indeed collection, ATS discovery, online JD recovery, then matching/LLM. If an Indeed query fails after earlier queries succeeded, their jobs are merged with the last complete snapshot and still enter Board JD recovery and matching; the partial attempt does not count as a complete refresh. Indeed and Board Health show Partial with completed, failed, and unrun query counts plus fresh and cached job counts. The next complete Indeed collection replaces the merged snapshot normally. Online and Mac Local JD recovery each stop after 100 distinct jobs with an outbound attempt or 20 elapsed minutes, whichever comes first; cheap cache and exact-peer checks do not use the job quota. Only jobs within 24 hours of their immutable `first_seen` receive expensive recovery. Board's new-job counts compare source and final canonical identities with the seen state from before the run. A job stamped by Indeed seconds before Board starts counts as new; an already-seen source job that gains an official URL keeps its original discovery time and does not count again. GitHub does not request LinkedIn.

The Mac launchd job owns LinkedIn and Glassdoor; install its dependencies with `python3 -m pip install -r requirements-local.txt`. It runs at noon, 3 PM, and 9 PM Pacific, plus gated catch-up after wake; it never starts from 5:00–5:59 PM. LinkedIn search runs before detail enrichment, uses up to 10 pages across Software Engineer, AI Engineer, and an alternating Backend Engineer / Full-Stack Engineer query, and rotates the starting query after each attempted search run. All LinkedIn requests share a transport allowance: at most 18 attempts per round or rolling hour, 54 per rolling 24 hours, and 8 Detail attempts per round/hour or 24 per rolling 24 hours, including follow-up recovery. Requests are spaced by 2.5–3.25 seconds with modest jitter. Two consecutive pages with at most one new-to-ledger ID stop a query; existing empty/low-unique stops also apply. The middle slot remains discovery because saved runs show meaningful new coverage. [Transport measurements and tradeoffs](docs/LINKEDIN_TRANSPORT.md) explain this choice. The 24-hour search window remains unchanged until narrower guest windows are validated. A 429 stops both endpoints for that round and pauses all LinkedIn traffic for at least an hour or the longer `Retry-After`, while separate endpoint cooldowns remain in force. Retry context and rolling request counts are recorded in Health; the local sync wrapper also keeps a durable request journal across failed publication. LinkedIn uses one ordinary HTTP transport with no alternate fingerprint fallback. Search has a separate 24-hour cooldown after two attempted 429 runs, followed by a one-page probe. A published cooldown round with usable saved data completes its scheduled slot, so the 10-minute gate does not repeat catch-up work; fixed slots and the existing non-overlap lock remain unchanged. The first detail HTTP 429 stops further detail requests for 12 hours while shared official-web JD recovery continues; Search may resume after the shared pause. After 12 hours, one detail probe is allowed: a successful response clears the cooldown, and another 429 starts a new 12-hour cooldown. Mac recovery uses the same `official_jd_recovery.Resolver` and `recover_pending` path as GitHub Board recovery, with the shared 100-job or 20-minute budget. LinkedIn Detail is a last resort: Fresh thin cards pass safe title, company, and US-location checks, reuse saved JDs and exact Official/ATS/Indeed peers, then try bounded non-LinkedIn recovery. Remaining cards require a cached metadata-only Luna `needs_jd=true` decision before Detail. A skip, missing key, or unavailable triage keeps the thin card. Collection and follow-up recovery share at most 8 Detail requests per Local round (0 during cooldown, 1 for a probe); a successful initial probe cannot unlock another budget in that round. Admission counters distinguish rules, cache, non-LinkedIn resolutions, and LLM deferrals. The Local gate launches `scripts/local_source_sync.sh` and writes its result path under `output/logs/`. [`output/sources/health.json`](output/sources/health.json) records last attempts, last-good snapshots, and bounded per-source run history. The [pipeline health page](public/health.html) presents Online Board, LinkedIn Local, Big Company Official, and Indeed in the same Jobs → JD & recovery → Requests → Sources → Issue format. It uses Healthy, Partial, and Failed as the main run states; optional Glassdoor failures remain visible without changing the overall state. Latest runs distinguish current input, new jobs, A/B results, and JD recovery. Today sums new jobs and failures across recorded Pacific-day source runs and attributes new A/B additions from Board run history while showing the latest run's retained A/B result separately. A dash means no run or measurable result is available today; source history starts with the first run after this update. Search 429 and Detail 429 are shown separately for the latest run, alongside cooldown deadlines. Deferred searches make zero HTTP requests and do not count as new failures. Stored unresolved-job reasons remain historical diagnostics; current HTTP response counters determine live failures. Consecutive failures remain visible. Retained inventory, JD coverage history, and raw diagnostics sit under Technical details. Execution shows measured new JDs, including initial LinkedIn detail fetches, and marks remote collector totals unavailable when they cannot be measured accurately. Displayed times use Pacific time.

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

Metadata-only Official jobs are checked with the existing location, title, and seniority rules before detail retrieval; JD-dependent hard constraints wait for the JD. Clear survivors receive detail requests directly. Borderline titles can receive batched GPT-6 Luna Medium `recover/skip` triage. One run adds at most 150 detail attempts, shared across companies; the queue favors recent jobs and rotates between companies. Meta, Disney, Netflix, and Equinix have targeted detail extraction, with safe generic extraction for other eligible thin-JD jobs. Equinix can use one bounded browser challenge for discovery or detail to establish a reusable HTTP session; its browser requests appear in the HTTP metrics. An unresolved challenge marks discovery blocked and retains last-good jobs. The report records relevant-job JD coverage, cache reuse, requests, deferrals, and failures. A job still missing its JD keeps the existing thin-JD matching fallback.

Selective JD and triage results are retained in `output/official_careers/recovered_jds.json.gz` so later GitHub runs can reuse them without repeating page or AI requests.

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

The coverage report keeps the existing exact reconciliation rate and adds a loss funnel for external in-scope records: supported company, comparable Official snapshot, Official candidate observed, and exact identity matched. It separates unsupported companies, discovery misses, identity mismatches, source timing, stale or partial Official comparisons, and missing company metadata, with the largest company contributors for each loss. The report uses each company's last successful and comparable Official run to avoid calling a failed or bounded scrape a discovery miss.

Genuinely ambiguous identity pairs may receive batched GPT-6 Luna Medium assessments. Their compact decisions are cached in `output/cross_pipeline/identity_ai_cache.json`. AI evidence appears in the report but never suppresses a job by itself; only a separately verified direct employer URL redirect can promote an exact match. Scheduled reconciliation uses the API key when available and otherwise produces the deterministic report.

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
- `output/cross_pipeline/` — coverage audit artifacts and compact identity AI cache when generated;
- `public/` — generated dashboard files.

Most full descriptions, source snippets, enrichment/LLM evidence, raw Official snapshots,
and full scoring caches stay under gitignored `output/cache/`; the selective Official JD cache above is a small committed exception. Per-run diagnostics
under `output/*/runs/` are local or workflow artifacts, not repository history.
GitHub commits `output/sources/indeed.json` with full Indeed JDs and its health state;
the Mac reads that snapshot as an exact peer and never recollects Indeed.
In-progress and applied jobs remain durable in the existing Supabase-backed review
state, so pipelines do not contend on a shared `tracked_jobs.json` commit.
The dashboard waits for that shared review state before showing review-dependent
tabs and counts. A successful load uses Supabase as the baseline and merges only
pending local edits; if it fails, the fallback is labeled `Cached review state`.

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
