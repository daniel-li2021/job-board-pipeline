# Job pipelines

Two parallel pipelines live here:

1. Syncareer pipeline (`daily_pipeline.py`) — documented below.
2. Multi-source board pipeline (`board_pipeline.py`) — see
   [the board pipeline section](#multi-source-board-pipeline).

# Syncareer job pipeline

Automated daily job search over [Syncareer](https://syncareer.com): keyword search,
hard filtering, a rolling 7-day watchlist, and a GitHub Issue alert with downloadable
CSV/TXT.

## Scripts

- `daily_pipeline.py` — keyword search across all companies, dedup, hard filter,
  optional LLM tiering, outputs.
- `syncareer_deep_scrape.py` — per-company snapshot scraper (`--snapshot`).

## Daily alert flow (what GitHub Actions runs)

```bash
python3 daily_pipeline.py --alert --no-llm --time last3days
```

- `--alert`: dedup against the rolling 7-day watchlist (`output/watchlist.json`)
  instead of the ever-growing `seen_job_ids.json`, and write alert deliverables.
- `--no-llm`: skip resume-matching/tiering. Hard filters still run
  (drops senior/lead/staff, US-citizen/clearance, non-US locations).
- `--time`: `24hours` | `last3days` | `last7days`.

### Outputs

- `output/alerts/<YYYY-MM-DD_HHMM>.csv` — new jobs this run (Excel-friendly).
- `output/alerts/<YYYY-MM-DD_HHMM>.txt` — same, plain text.
- `output/alerts/latest.csv` — always the most recent alert.
- `output/alerts/issue_body.md` — markdown table used as the GitHub Issue body.
- `output/watchlist.json` — rolling 7-day dedup store (auto-pruned each run).
- `output/daily/<date>_jobs.csv` — full detail for the run.

When run inside GitHub Actions, the script also writes `new_count`, `stamp`,
`issue_title`, and `issue_body_path` to `$GITHUB_OUTPUT` so the workflow can decide
whether to open an Issue.

## Local run with resume matching (optional)

LLM tiering is only for manual, deeper review. Put keys in `.env`
(`OPENAI_API_KEY` and/or `GROQ_API_KEY`), then:

```bash
python3 daily_pipeline.py --time last3days      # LLM on, standard seen_ids store
```

This writes `output/daily/<date>_tier1.csv` and `_tier2.csv`.

## GitHub Actions

`.github/workflows/daily-jobs.yml` runs twice a day (cron, UTC) plus manual
`workflow_dispatch`. It:

1. Runs the alert-mode pipeline (no LLM, no secrets required).
2. Commits `output/watchlist.json` and `output/alerts/` back to the repo.
3. Uploads the CSV/TXT as run artifacts.
4. Opens a GitHub Issue (which emails you per your notification settings) when
   there is at least one new job.

The repo root is this `job_scrape_feasibility/` folder. Large/derived CSVs are
git-ignored; only the watchlist and alert files are tracked (see `.gitignore`).

---

# Multi-source board pipeline

Aggregates jobs from public ATS boards (Greenhouse / Lever / Ashby), company
career pages (Amazon, Google), and locally-scraped LinkedIn + Glassdoor
snapshots, then dedups, verifies official links, hard-filters, scores with an
LLM (rule fallback), and ranks into Tier A/B/C.

Flow: `Sources -> Normalize -> Dedup(first_seen) -> Official Verify -> Hard
Filter -> Match (LLM or rules) -> Rank -> jobs.json + latest.md + alert`.

## Layout

- `board_pipeline.py` — orchestrator. **Only writer** of `output/board/jobs.json`
  and `output/board/latest.md`.
- `sources/schema.py` — unified job schema, US/recency/date helpers, dedup keys.
- `sources/ats.py` + `source/ats_boards.json` — Greenhouse/Lever/Ashby adapters.
- `sources/official.py` — Amazon + Google career-page adapters (CI-safe HTTP).
- `sources/linkedin_local.py`, `sources/glassdoor_local.py` — **local-only**
  best-effort adapters (guest search / public HTML).
- `local_sources.py` — runs the two local adapters, writing
  `output/sources/{linkedin,glassdoor}.json`. A source that hits a login wall /
  captcha / 403 / 429 is skipped and its previous snapshot is preserved.
- `scripts/local_source_sync.sh` — scrape then commit/push **only**
  `output/sources/*.json` when changed. Never touches `jobs.json` / `latest.md`.
- `scripts/macos/com.jobboard.local-sources.plist` — launchd agent (every 3h).

## Division of responsibility (avoids git conflicts)

- **Local machine (launchd):** scrapes LinkedIn/Glassdoor and pushes only
  `output/sources/*.json`.
- **GitHub Actions:** fetches ATS + official, ingests the pushed source JSONs,
  runs the full pipeline, and is the sole committer of `output/board/` and
  `output/alerts/board_*`.

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
SKIP_PUSH=1 bash scripts/local_source_sync.sh    # commit locally, no push
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

The LLM runs **only on rule-filter survivors** (top 300 by rule score) to control
cost. If the key is missing or the API errors, the pipeline falls back to
rule-based scoring and still succeeds — it never fails the run. `--no-llm` forces
rule-based scoring for local debugging.

## GitHub Actions

`.github/workflows/board-jobs.yml` runs twice daily (cron), on manual dispatch,
and on any push to `output/sources/*.json` (i.e. after the local scraper syncs).
It runs the pipeline, commits `output/board/` + `output/alerts/`, uploads
artifacts, and opens a GitHub Issue for new Tier A/B jobs on scheduled/manual
runs (source-push runs ingest without opening an issue, to avoid spam).
