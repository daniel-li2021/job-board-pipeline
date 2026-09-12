# Pipeline algorithm and ownership

## Discovery

- **Board** discovers public ATS jobs and ingests locally collected LinkedIn, Indeed, and Glassdoor snapshots.
- **Official Careers** searches company career sites through public APIs, ATS endpoints, or rendered listings.
- **Syncareer** searches its public index and detail API.
- Page/query depth is bounded per source. Those ceilings control discovery traffic only; they never truncate processing of records already discovered.
- Glassdoor first uses JobSpy. Its retired location lookup currently returns 404 before results; the fallback reads the normal static search page with Scrapling and keeps its cards/snippets. Detail-page 403s remain explicit enrichment failures.

## Normalization and deduplication

Every source is normalized to the shared job schema. Exact job IDs and canonical URLs are preferred; company + title + location is the conservative fallback. Cross-pipeline reconciliation suppresses only exact Official duplicates. Unmatched external jobs at covered companies remain visible.

## JD enrichment

Every discovered record is processed. There is no total job/request cap after discovery.

1. Reuse fresh cached detail.
2. Hydrate an exact Official/Board/Syncareer peer.
3. Try a known official or direct application URL.
4. Parse ATS responses, JSON-LD `JobPosting`, and embedded JSON.
5. Use the source detail page, then Scrapling's browser-impersonating Fetcher when ordinary HTTP is blocked.

Requests use existing bounded concurrency or sequential per-domain pacing, caching, and backoff. An ordinary LinkedIn path is disabled for the rest of a run after a 429. Missing JDs do not delete otherwise valid cards; unresolved records keep an `enrichment_failure_reason`.

## Filtering, matching, and tiering

All discovered records receive an enrichment outcome and then deterministic company and hard filters. Survivors receive the shared role/seniority prefilter and a score. Cached LLM results are reused; remaining eligible jobs are sent in small batches without a total candidate cap. If an LLM result is unavailable, the rule fallback still gives every survivor a matching outcome.

Thin/no-JD records use conservative evidence confidence rather than automatic rejection. Explicit senior, clearance/citizenship, non-US, and hard-negative rules still apply. Tier assignment and display ordering remain deterministic.

## Automation and health ownership

- The primary checkout is for development.
- `/Users/daniel/Projects/job_scrape_feasibility-automation` owns launchd collection and writes only `output/sources/*.json`.
- GitHub Actions owns `output/board/`, `output/official_careers/`, and `output/syncareer/`.
- Reconciliation runs after every completed discovery workflow, including failures, and publishes the dashboard.

The dashboard build reuses source health, snapshots, per-run stats, and stores to generate `public/health.json`, `public/health-history.json`, and `public/health.html`. Dashboard badges link to that report. Statuses are **Healthy**, **Warning**, **Problem**, or **Stale**.
