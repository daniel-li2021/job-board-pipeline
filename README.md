# Job pipelines

Two **separate** pipelines. Do not mix their folders.

| Pipeline | Script | When you skipped a day, open this |
|---|---|---|
| **Syncareer** | `daily_pipeline.py` | [`output/syncareer/inbox.md`](output/syncareer/inbox.md) (also `inbox.csv`) |
| **ATS / LinkedIn / official** | `board_pipeline.py` | [`output/board/inbox.md`](output/board/inbox.md) (also `inbox.csv`) |

Each inbox is the last **3 days** of matching jobs. You do **not** need to read every GitHub Issue.

Per-run snapshots (optional): `output/syncareer/runs/` and `output/board/runs/`.

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
- `--no-llm`: skip resume-matching. Hard filters still drop senior / US-citizen / non-US.

### Outputs (`output/syncareer/` only)

- **`inbox.md` / `inbox.csv` / `inbox.txt`** — last 3 days of kept jobs (the file to read).
- `runs/<stamp>.csv` — jobs that were *new this run* only.
- `watchlist.json` — 7-day dedup store (kept + dropped ids).
- `issue_body.md` — markdown for the GitHub Issue (this run).

## Local LLM tiering (optional)

```bash
python3 daily_pipeline.py --time last3days
```

Writes gitignored `output/daily/<date>_tier1.csv` / `_tier2.csv`.

## GitHub Actions

`.github/workflows/daily-jobs.yml` twice a day + manual run. Commits
`output/syncareer/`, uploads the inbox as an artifact, opens a
`syncareer-alert` Issue when this run found new jobs.

---

# Multi-source board pipeline

Aggregates jobs from public ATS boards (Greenhouse / Lever / Ashby), company
career pages (Amazon, Google), and locally-scraped LinkedIn + Glassdoor
snapshots, then dedups, verifies official links, hard-filters, scores with an
LLM (rule fallback), and ranks into Tier A/B/C.

Flow: `Sources -> Normalize -> Dedup(first_seen) -> Official Verify -> Hard
Filter -> Match (LLM or rules) -> Rank -> jobs.json + latest.md + alert`.

## Layout

- `board_pipeline.py` — orchestrator. **Only writer** of `output/board/`.
- `sources/schema.py` — unified job schema, US/recency/date helpers, dedup keys.
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
  runs the full pipeline, and is the sole committer of `output/board/`.

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
It runs the pipeline, commits `output/board/`, uploads the **inbox** artifact,
and opens an `ats-linkedin-alert` Issue for new Tier A/B jobs on scheduled/manual
runs (source-push runs ingest without opening an issue, to avoid spam).

**What to open:** `output/board/inbox.md` (last 3 days). `latest.md` is the 7-day dump.
