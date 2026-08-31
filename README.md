# Job pipelines

Three **separate** components. Do not mix their folders.

| # | Component | Script | When you skipped a day, open this |
|---|---|---|---|
| 1 | **Syncareer** | `daily_pipeline.py` | [`output/syncareer/inbox.md`](output/syncareer/inbox.md) |
| 2 | **ATS / LinkedIn / Glassdoor** | `board_pipeline.py` | [`output/board/inbox.md`](output/board/inbox.md) |
| 3 | **Big Tech Official Careers** | `official_careers.py` | [`output/official_careers/inbox.md`](output/official_careers/inbox.md) |

Each inbox is the last **3 days** of matching jobs. You do **not** need to read every GitHub Issue.

Public rolling dashboard: **https://daniel-li2021.github.io/job-board-pipeline/**
(deployed by `.github/workflows/reconcile-pages.yml`). It includes the last 24
hours of GitHub alert activity, three-day rolling views, lightweight status
sections, a collapsible referral view, and official-search links. Coverage
reconciliation remains in the repo audit files but is intentionally hidden from
the public page. Review status is shared through Supabase and editable by
anyone who can access the dashboard.

**Matching/scoring is shared, not implemented three times.** All three components
use the same `board_pipeline.py` role-family logic, 0–100 resume/JD matcher,
resume routing (`resume_swe.md` / `resume_ai.md`), LLM/cache scoring, and
deterministic Tier A/B/C policy. Components 1 and 3 normalize their jobs into
the shared schema and persist `match_score`, `tier`, and `score_source`.

Referral companies have one source of truth:
[`source/target_companies.json`](source/target_companies.json). All three
pipelines use `sources/company_aliases.py`; do not create a second referral list.

Per-run snapshots: `output/syncareer/runs/`, `output/board/runs/`,
`output/official_careers/runs/`.

# Syncareer job pipeline

Automated search over [Syncareer](https://syncareer.com): keyword search, hard
filtering, a rolling 7-day watchlist, and a GitHub Issue for *this run*.

## Scripts

- `daily_pipeline.py` — keyword search, dedup, hard filter, optional LLM, outputs.
- `syncareer_deep_scrape.py` — per-company snapshot scraper (`--snapshot`).

## Daily alert flow (GitHub Actions)

```bash
python3 daily_pipeline.py --alert --no-llm --time last3days
```

- `--alert`: 7-day watchlist at `output/syncareer/watchlist.json` + inbox files.
- `--no-llm`: use the shared conservative rule score/tier fallback. Score/Tier
  are still persisted; hard filters still drop senior / US-citizen / non-US.

### Outputs (`output/syncareer/` only)

- **`inbox.md` / `inbox.csv` / `inbox.txt`** — last 3 days of kept jobs (the file to read).
- `runs/<stamp>.csv` — jobs that were *new this run* only.
- `watchlist.json` — 7-day dedup store (kept + dropped ids).
- `issue_body.md` — markdown for the GitHub Issue (this run).

## Local LLM matching (optional)

```bash
python3 daily_pipeline.py --time last3days
```

Writes gitignored `output/daily/<date>_tier_a.csv` / `_tier_b.csv` using the
same 0–100 score and A/B/C policy as the other pipelines.

## GitHub Actions

`.github/workflows/daily-jobs.yml` twice a day + manual run. Commits
`output/syncareer/`, uploads the inbox as an artifact, opens a
`syncareer-alert` Issue when this run found new A/B jobs. The workflow injects
`OPENAI_API_KEY` from the Repository Secret and uses the shared LLM matcher;
missing-key or API failures automatically fall back to shared rule scoring.

---

# Multi-source board pipeline

Aggregates jobs from public ATS boards (Greenhouse / Lever / Ashby) and
locally-scraped LinkedIn + Glassdoor
snapshots, then dedups, verifies official links, hard-filters, scores with an
LLM (rule fallback), and ranks into Tier A/B/C.

Big-company career discovery is owned exclusively by `official_careers.py`;
the Board pipeline intentionally does not run the legacy Official source.

Flow: `Sources -> Normalize -> Dedup(first_seen) -> Official Verify -> Hard
Filter -> Match (LLM or rules) -> Rank -> jobs.json + latest.md + alert`.

## Layout

- `board_pipeline.py` — orchestrator. **Only writer** of `output/board/`.
- `sources/schema.py` — unified job schema, US/recency/date helpers, dedup keys.
- `sources/ats.py` + `source/ats_boards.json` — Greenhouse/Lever/Ashby adapters.
- `sources/linkedin_local.py`, `sources/glassdoor_local.py` — **local-only**
  best-effort adapters (guest search / public HTML).
- `local_sources.py` — runs the two local adapters, writing
  `output/sources/{linkedin,glassdoor}.json`. A source that hits a login wall /
  captcha / 403 / 429 is skipped and its previous snapshot is preserved.
- `scripts/local_source_sync.sh` — scrape then create an isolated source-only
  commit against `origin/main`. It works even when the developer checkout is
  dirty or on a feature branch, and never touches `jobs.json` / `latest.md`.
- `scripts/macos/com.jobboard.local-sources.plist` — launchd agent (every 3h).

## Division of responsibility (avoids git conflicts)

- **Local machine (launchd):** scrapes LinkedIn/Glassdoor and pushes only
  `output/sources/*.json`. GitHub-hosted runners never scrape those sites.
- **GitHub Actions:** each cloud pipeline runs and commits independently.
  Board writes only `output/board/`; Official writes only
  `output/official_careers/` plus its alert; Syncareer writes only
  `output/syncareer/`. Reconciliation alone writes `output/cross_pipeline/`
  and `public/`.

## Local usage

```bash
# One-off local scrape of the two local sources:
python3 local_sources.py

# Full pipeline locally, writing to gitignored output/board-local/:
python3 board_pipeline.py --local-out            # LLM on if OPENAI_API_KEY set
python3 board_pipeline.py --local-out --no-llm   # rule-based only
python3 board_pipeline.py --skip-network         # ingest local snapshots only

# The launchd wrapper (scrape + git sync). Test before installing launchd:
NO_GIT=1 bash scripts/local_source_sync.sh       # scrape only
SKIP_PUSH=1 bash scripts/local_source_sync.sh    # compare with main, no commit/push
SKIP_SCRAPE=1 bash scripts/local_source_sync.sh  # push the last good snapshots
bash scripts/local_source_sync.sh                # full: scrape + commit + push
```

## Install the launchd scheduler

Edit the absolute paths in
`scripts/macos/com.jobboard.local-sources.plist`, then:

```bash
cp scripts/macos/com.jobboard.local-sources.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.jobboard.local-sources.plist
```

It runs every 3 hours (`StartInterval` 10800; set 7200 for 2h). launchd does
not fire while the Mac is asleep; it runs at the next wake.

## LLM matching

`OPENAI_API_KEY` is read from the environment only (`os.getenv`):

- Local: put it in `.env` (git-ignored).
- GitHub Actions: add a repository secret `OPENAI_API_KEY`; the workflow injects
  it via `${{ secrets.OPENAI_API_KEY }}`.

The LLM runs **only on rule-filter survivors** (bounded per run) to control
cost. If the key is missing or the API errors, the pipeline falls back to
rule-based scoring and still succeeds — it never fails the run. `--no-llm` forces
rule-based scoring for local debugging.

## GitHub Actions

The pipelines are isolated and staggered twice daily (all cron times UTC):

- Official careers: `03:00` / `15:00`;
- ATS / LinkedIn board: `03:10` / `15:10`;
- Syncareer: `03:20` / `15:20`;
- coverage reconciliation + Pages: `03:30` / `15:30`, plus a successful
  `workflow_run` trigger after each pipeline.

Each workflow also has an independent manual dispatch. A failure in one source
does not block the others. Source pushes to `output/sources/linkedin.json` or
`glassdoor.json` still run board-only with `--no-digest`.

**What to open:** `output/board/inbox.md` (last 3 days). `latest.md` is the 7-day dump.

At most **one useful digest per Pacific day** per pipeline: newly visible
Tier A/B, or a B→A promotion. Rescores, JD-only edits, and the evening
rerun do not re-alert. State: `output/board/digest_state.json`.

Big Tech official discovery is component 3 and writes only under
`output/official_careers/`.
`covered_elsewhere` is a discovery hint, not a company-wide drop. External jobs
are suppressed only when the company is manually `validated` in
`profile/official_coverage.json` **and** the record has an exact official URL,
requisition ID, or company+title+location match. Unmatched jobs remain visible
as `official_gap` or `pending_official_refresh`.

---

# Big Tech Official Careers scraper

Direct discovery from official company career sites. **Discovery only** —
no second matching implementation. After each scrape, jobs are normalized
with `sources.schema.make_job` and handed to the existing board matching
stack (hard filter, prefilter, LLM/cache scoring, Tier A/B).

`posted_date` is the official posting time from the career site.
`fetched_at` is scrape time. `first_seen` is when *this* store first saw
the job. Discovery time is never treated as posting time.

## Purpose

Catch new/updated SWE and ML roles on large-company career sites that the
ATS/LinkedIn pipeline either skips (`covered_elsewhere`) or only samples
lightly (`sources/official.py`).

## Sources (initial)

| Company | Adapter | Method | Pagination |
|---|---|---|---|
| Google | `sources/careers/google.py` | HTML GET + `AF_initDataCallback` ds:1 JSON | `page=1,2,...` |
| Amazon | `sources/careers/amazon.py` | `search.json` (`country=USA`) | `offset=0,20,40,...` |
| Apple | `sources/careers/apple.py` | HTML GET + `__staticRouterHydrationData` (`location=united-states-USA`) | `page=1,2,...` |
| Microsoft | `sources/careers/microsoft.py` | Eightfold PCSX `GET /api/pcsx/search` (`location=United States`) | `start=0,10,20,...` |
| NVIDIA / Salesforce / Adobe | `sources/careers/workday.py` (one reusable CXS adapter) | `POST /wday/cxs/{tenant}/{site}/jobs` (US facet) | `offset=0,20,40,...` |
| Uber | `sources/careers/uber.py` | Oracle HCM list+detail (`iaziqy.fa.ocs.oraclecloud.com`, site `CX_1`) | `offset=(page-1)*limit` until `TotalJobsCount` exhausted (do not stop at pages 1–7) |
| Meta | `sources/careers/meta.py` | Careers Relay/GraphQL; discovers the current `lsd` and persisted-query `doc_id` from the public page/bundle | one complete result payload per role query |
| TikTok | `sources/careers/tiktok.py` | LifeAtTikTok public supplier `/search/job/posts` API with US city filters | `offset` + `limit=50` |
| LinkedIn | `sources/careers/linkedin_company.py` | logged-out guest jobs endpoint pinned to company id `1337` | `start=0,10,...` |
| Walmart | `sources/careers/walmart.py` | combined hybrid-search POST API | `page=0,1,...`, `size=25` |
| Disney / Qualcomm | `sources/careers/disney.py`, generic PCSX in `microsoft.py` | server-rendered US results / Eightfold search+detail | bounded per role query |
| Palantir / WeRide | `sources/careers/lever.py` | public Lever postings API | single JSON payload |
| Greenhouse / Lever / Ashby companies | existing generic ATS adapters via registry `adapter: ats` or direct adapter config | public board APIs from `source/ats_boards.json` or a verified official token | provider pagination |

Registry: `source/official_careers.json`. Source-side US filters are used
when the API actually honors them. Uber’s HCM finder does not, so rows are
collected then passed through conservative `keep_us_or_unknown` (keep US /
Remote-US / multi-office if any US / ambiguous; drop confirmed all-non-US).

Companies without a verified, sufficiently complete low-risk public adapter
remain link-only registry entries. They make no external scrape call, but keep
an official search link for manual review and cross-pipeline coverage audits.
All links and automation state are rendered directly from the registry on the
dashboard.

## Entry point

```bash
python3 official_careers.py scrape --only google   # discovery
python3 official_careers.py match --no-llm         # shared matching
python3 official_careers.py run                    # scrape + match (scheduled)
```

`--only` takes a company id from the registry. `--max-pages` is a per-query
safety cap (default 12). `--no-digest` updates the store without a
user-facing alert. `--force-digest` sends a digest even if one already went
out today.

## Schedule / workflow

`.github/workflows/official-careers.yml` runs independently at 15:00 and 03:00
UTC and supports manual `--only` debugging. LinkedIn/Glassdoor scraping stays
on the local launchd agent; GHA never hits those sites.

- Every run scrapes, normalizes, and re-runs matching.
- **At most one user-facing digest per Pacific day per pipeline.** The
  evening run updates `output/official_careers/` silently if a digest
  already went out today.
- Alert only on newly visible Tier A/B or a B→A promotion. Score/JD-only
  changes are not re-alerted (`digest_state.json` stores last alerted tier).

## Outputs (`output/official_careers/` only)

- `raw.json` — last scrape, normalized JobRecords.
- `scrape_report.md` — per-company method, pages, counts, sample records.
- `jobs.json` — 7-day store (`first_seen` / `last_seen` / LLM cache).
- `latest.md` — 7-day Tier A/B view.
- `inbox.md` / `inbox.csv` — last 3 days (the file to read).
- `digest_state.json` — last digest date + already-alerted keys and last alerted tier.

Digest CSV / issue body (when emitted): `output/alerts/official_*`.

## What handles matching

`official_careers.py match` imports `board_pipeline` functions:

hard_filter → role_seniority_prefilter → score_survivors (resume_swe / resume_ai
+ candidate_profile + LLM cache) → assign_tier → user_facing_sort_key.

`covered_elsewhere` is **not** applied here (these companies *are* the
target). The `exclude` list still is.

---

# Coverage, dashboard, and notifications

Run reconciliation and static dashboard generation locally with:

```bash
python3 coverage_reconcile.py
python3 dashboard.py --json
```

Outputs:

- `output/cross_pipeline/coverage.json` / `coverage.md` — exact coverage audit,
  dynamic gaps, pending refreshes, and manual company states;
- `public/index.html` / `dashboard.json` — GitHub Pages site;
- `profile/official_coverage.json` — manual `unvalidated` / `validated` /
  `unsupported` company decisions;
- `profile/review_state.json` — legacy CLI/pipeline state; the dashboard does
  not read or write it.

**Fresh** mirrors jobs emitted by GitHub alert Issues during the last 24 hours,
including B→A promotions whose original `first_seen` is older. Each pipeline
persists exact events in `output/<pipeline>/alert_history.json`. **Rolling** is
still work first seen in the last three days. Employer `posted_date` remains
visible reference metadata but does not decide those windows. Active rows sort
Tier A first, then alert/discovery recency and match score. For ATS/LinkedIn
only, stored Tier C rows provide a presentation fallback when A/B volume is low:
Fresh can fill from fewer than 10 A/B to 20 total, and Rolling from fewer than
30 A/B to 50 total. Fallback C rows never score below 60 and remain labeled C.

The public page reads `public.job_review_status` directly from Supabase and
merges rows by `canonical_job_key`. Status updates never touch GitHub, run an
Action, or rebuild Pages. The browser caches the latest successful shared read
in `localStorage` only as a temporary fallback; Supabase remains authoritative.
Edits are saved locally first and marked pending until the shared upsert
succeeds. Pending edits retry on page load or reconnect, and `updated_at`
provides simple last-write-wins conflict resolution.

One-time setup:

1. In the Supabase SQL editor, run
   [`supabase/job_review_setup.sql`](supabase/job_review_setup.sql).

The supplied project URL and publishable browser key are defaults in
`dashboard.py`. Publishable keys are safe in public clients when RLS is enabled;
never put a Supabase secret/service-role key in this repository. This setup
intentionally permits anonymous inserts and updates, so the dashboard link is
not a strong security boundary. To build for a different project without
editing source:

```bash
SUPABASE_URL=https://PROJECT.supabase.co \
SUPABASE_PUBLISHABLE_KEY=sb_publishable_REPLACE_ME \
python3 dashboard.py --json
```

Fuzzy title/location matches are suggestions only and never suppress a job.
100% exact observed coverage is the current manual audit target, not a permanent
automatic rule. Amazon and every other company stay unvalidated until the
generated audit is reviewed and manually approved.

Issue bodies do not mention the repository owner. For email notifications, use
GitHub **Watch → Issues** (or **All Activity**) on the repository. No email API
or provider is required.

## Data flow

```
Official career sites
    -> sources/careers/* adapters
    -> output/official_careers/raw.json   (discovery snapshot)
    -> board_pipeline matching functions   (shared; not copied)
    -> output/official_careers/jobs.json + latest.md + inbox.md
    -> at most one digest/day (new A/B or B→A) -> GitHub Issue
```

Component 1 (Syncareer) and component 2 (board) are unchanged and keep
writing to their own folders. Component 3 never writes `output/board/` or
`output/syncareer/`.
