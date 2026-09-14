# Pipeline algorithm and execution reference

This document explains how data moves through the system, which process owns each artifact, and how to reason about partial failures. It is the detailed companion to the [README](../README.md): use the README for setup and operator commands, and use this file when changing, debugging, or recovering the pipeline.

## System map

```text
Local collectors                    GitHub discovery workflows
  LinkedIn search + detail            Board: public ATS + local snapshots
  Indeed search                       Official Careers: company adapters
  Glassdoor search                    Syncareer: search + detail API
          |                                      |
          +-- output/sources/*.json --------------+
                              |
                    normalize / deduplicate
                              |
                 enrich / filter / score / tier
                              |
               pipeline-owned jobs + run stats
                              |
                     coverage reconciliation
                              |
             dashboard + health + GitHub Pages
```

The three discovery pipelines are deliberately independent. A failure in one does not prevent the other stores from being reconciled and published. Local collection is also independent: it publishes source snapshots, and the Board workflow consumes the latest committed snapshots rather than running desktop-only collectors in Actions.

## Ownership and state

| Owner | Responsibility | Durable artifacts |
| --- | --- | --- |
| Primary checkout | Development, tests, documentation, and reviewed changes | Source code and tracked configuration |
| Local automation checkout | LinkedIn, Indeed, and Glassdoor collection | `output/sources/{linkedin,indeed,glassdoor,health}.json` |
| Board workflow | Public ATS discovery plus committed local snapshots | `output/board/` |
| Official Careers workflow | Company career-site adapters | `output/official_careers/` |
| Syncareer workflow | Syncareer search and detail API | `output/syncareer/` plus dated reports in `output/daily/` |
| Reconciliation workflow | Cross-pipeline identity, dashboard, health, and Pages deployment | `output/cross_pipeline/coverage.*` and `public/` at build time |
| Browser/Supabase review state | Per-user review and application decisions | Remote review rows; source-expired applied rows are restored into the dashboard |

The development checkout must not become a second local collector. `scripts/local_source_sync.sh` runs collection from `/Users/daniel/Projects/job_scrape_feasibility-automation` in an isolated worktree and stages only the four local-source artifacts. GitHub Actions owns the three pipeline output trees.

Persistent JSON state is written atomically where interruption could corrupt the canonical store. Corrupt or structurally invalid state is rejected rather than silently replacing a last-good store. Large full-detail caches and timestamped local run files are gitignored; compact stores, bounded `run_history.json`, and `latest_stats.json` are tracked so Actions and Pages can consume useful current state.

## Shared record and time invariants

All sources normalize into the schema in `sources/schema.py`. The important invariants are:

- Prefer a stable source job ID or canonical application URL for identity. Company + title + location is a conservative fallback, not a claim that similar-looking requisitions are identical.
- `first_seen` records when this system first observed a job and survives rediscovery. `last_seen` records the latest successful observation.
- A trusted source posting timestamp is used for posted-age ranking only when its confidence is high or medium. Low-confidence or missing posting dates fall back to discovery time and sort behind trusted first-three-day records.
- Dashboard Fresh and Rolling windows use exact `first_seen` datetimes (`<=24h` and `<=72h`). They are discovery views and are intentionally separate from posted-age ranking.
- Compact tracked stores retain display, match, provenance, coverage, and review fields. Full descriptions and raw source material belong in the local caches where available.
- Every discovered canonical record receives an enrichment outcome and remains auditable even if it is later filtered or suppressed.

## Local source pipeline

`local_sources.py` runs each collector independently and updates `output/sources/health.json` after every attempt.

### Collection

- LinkedIn searches bounded primary, secondary, and specialty query groups. Search/discovery obtains cards; detail enrichment is a separate phase that tries to obtain descriptions for the discovered records.
- Indeed and Glassdoor use their own smaller bounded page budgets. These budgets limit discovery traffic only; they do not truncate processing of cards already returned.
- Glassdoor first uses JobSpy. When its location lookup cannot produce results, the Scrapling/static-page fallback can still preserve cards and snippets. Detail-page blocking remains an explicit enrichment limitation.
- Per-query diagnostics retain pages fetched, stop reasons, results, unique contributions, and enrichment outcomes where the collector provides them.

### Last-good behavior

Each source has two distinct states:

1. **Latest attempt** — when collection was tried, its result count, status, query diagnostics, detail-enrichment diagnostics, and failure reason.
2. **Last-good snapshot** — the most recent verified non-empty data that downstream code may safely consume.

A failed or empty-unverified attempt does not overwrite a usable last-good snapshot. This distinction is fundamental: a current attempt can be degraded while the published data remains fresh and usable. An empty result replaces prior data only when the collector can verify that the empty result is authoritative.

For LinkedIn, health keeps search/discovery throttling separate from detail-enrichment throttling. A search 429 affects discovery coverage. A detail 429 affects descriptions for already discovered cards and may be partly or fully recovered by Scrapling. Scrapling request/resolution counts and any remaining no-JD count are reported separately.

### Publication

The local sync script validates repository and push prerequisites, collects in an isolated checkout, stages only local-source snapshots and health, and pushes the source commit. If `main` advances, it retries against the current remote state without mixing pipeline-owned output into the local commit. Board Actions sees local jobs only after this push succeeds.

## Board pipeline

`board_pipeline.py` is the shared implementation for filtering, matching, tiering, and application ordering. Its execution order is significant:

1. Collect public ATS jobs and read committed LinkedIn, Indeed, and Glassdoor snapshots.
2. Normalize, merge exact identities, verify exposed official URLs, and collapse cross-source duplicates again.
3. Load the prior store, preserve `first_seen`, set `last_seen`, and compute recency before filtering.
4. Annotate cross-pipeline coverage.
5. Enrich every discovered thin record from exact peers and direct/original URLs.
6. Apply company exclusions and flags. A company covered by Official Careers is not globally hidden; only an exact reconciled duplicate is suppressed.
7. Apply hard eligibility filters such as non-US, explicit seniority, citizenship/clearance, and other material constraints.
8. Apply the shared role/seniority prefilter to reduce obvious mismatches before an LLM call.
9. Score active candidates, assign tiers, apply referral actions, and sort for application priority.
10. Rebuild the canonical store with kept and dropped records, then write visible Tier A/B outputs and run statistics.

`--no-digest` suppresses the user-facing digest only. It still persists stores, `first_seen`, scores, tiers, and `latest_stats.json`, which allows source-push runs to maintain state without generating duplicate notifications.

## Official Careers pipeline

`official_careers.py` runs the company registry in `sources/careers/registry.py`. Adapters use public APIs, ATS endpoints, rendered listings, or company-specific parsers. Companies are isolated and collected with bounded concurrency, so one adapter failure does not discard successful companies.

The raw cache records per-company completion and diagnostics. A successful full sweep may retire listings that disappeared; an incomplete or failed sweep carries prior records forward rather than treating missing data as verified removal. The normalized records then reuse Board's hard filters, role prefilter, matcher, tiering, ordering, stores, and alert logic. Exact Board and Syncareer peers may supply a missing description before scoring.

Official Careers is canonical for its covered requisitions, but its coverage list is not a company-wide exclusion rule. Reconciliation suppresses an external record only when exact identity evidence exists.

## Syncareer pipeline

`daily_pipeline.py` searches Syncareer's public index with bounded pagination, fetches its detail API, normalizes records, and reuses Board's filtering, matching, tiering, and ordering. Exact Official or Board peers may hydrate missing descriptions.

The tracked Syncareer store is a seven-day watchlist, not an unbounded archive. `first_seen` and seen-ID state prevent a rediscovered job from appearing new. Dated CSV/Markdown reports live under `output/daily/`; canonical jobs, alerts, state, and run statistics live under `output/syncareer/`.

## Enrichment, cache, and fallback behavior

Enrichment is ordered to reuse reliable existing work before making network requests:

1. Keep an already sufficient description or reuse a fresh cached detail.
2. Hydrate from an exact Official, Board, or Syncareer peer.
3. Follow a known official or direct application URL.
4. Parse supported ATS payloads, JSON-LD `JobPosting`, or embedded page data.
5. Try the source detail page.
6. Where implemented, use Scrapling when normal HTTP is blocked.

Requests retain bounded concurrency, per-domain pacing, timeouts, retry/backoff, and cache behavior already owned by each adapter. A 429 can disable the affected ordinary request path for the remainder of the run rather than amplifying the throttle.

Failure to obtain a description does not delete a valid job card. The job keeps `enrichment_failure_reason`, uses title/metadata evidence conservatively, and remains visible for diagnostics. Explicit software/AI/data early-career titles remain useful review signals; generic `Engineer I` or `Entry Level` wording alone receives only a small title bonus. This is different from a hard eligibility failure.

## Filtering, scoring, and tiering

### Deterministic gates

Company classification and hard filters run before LLM scoring. The role/seniority prefilter removes clear non-software families and senior mismatches while allowing ambiguous or thin records to receive a conservative outcome. An “engineer” token alone is not evidence of software work.

### Match score

`match_score` measures job-to-candidate fit only. The production matcher uses `gpt-5.6-terra` with medium reasoning and routed batches of up to 15 jobs. Each completed score records the actual model, prompt/scoring version, reasoning effort, candidate fingerprint, JD hash, and score time.

Cache migration is lazy. A model, prompt, or reasoning-default change does not relabel or mass-rescore a job whose JD and candidate inputs are still valid; the older score remains reusable with its original provenance. New jobs, materially changed JDs, candidate-input changes, and explicit refresh/retry work are scored with the current configuration. Rule fallbacks are never treated as completed LLM cache hits.

The scoring prompt treats explicit New Grad, Early Career, Entry Level, Junior, and Engineer I roles as strong seniority-fit evidence when the actual responsibilities are relevant. Minor learnable or transferable stack/domain gaps do not by themselves force those roles below 80. Material core requirements, the actual work, hard constraints, and genuine family mismatches still control the score; title wording never receives a blind boost. Level II roles are judged from their scope and requirements rather than from a fixed family hierarchy.

Internship and co-op status does not lower `match_score`: a technically excellent internship may still be an excellent fit. It lowers application priority and normally produces `apply_if_time` unless the role has a specific unusually strong reason to prioritize it.

### Tiers

- Tier A normally requires a score of at least 85 plus acceptable seniority, recency, and gap evidence.
- Tier B normally requires at least 70 and includes reasonable stretch roles.
- Thin evidence, material gaps, senior mismatches, staffing, internships, and hard constraints can cap or lower the actionable tier even when a raw score is high.
- Rule-only matches are conservative and normally cannot claim the same confidence as a full JD-based LLM score.

Tiering is an application decision layer; it does not rewrite the underlying fit score.

## Application ordering and company metadata

`profile/company_profiles.json` is the canonical maintained source for company-ranking metadata. Each entry can supply canonical name/aliases, size, sponsor likelihood, company type, maturity, tags, priority, notes, and verification date. Matching reuses the same normalized alias logic as other company configuration.

Company metadata never changes `match_score`. Within the actionable tiers it helps application ordering:

- generally prefer high-priority, sponsor-friendly larger employers, strong technology companies, and mature or growth-stage startups;
- down-rank staffing firms, poor/unknown sponsorship where configured, and defense or clearance-heavy employers;
- apply a mild `tech_service` ordering penalty so large consulting/IT-services employers do not outrank stronger product-company opportunities on size and sponsorship alone;
- down-rank internship/co-op roles by default;
- do not enforce a fixed role-family hierarchy: retain the score's assessment of the actual work and material requirements.

Recency is calibrated as an ordering constraint rather than a single mechanical weight. Within roughly the first three posted days, posting day is compared before quality so a materially newer day remains meaningful. Within the same posting day, a five-point fit band and company/application quality come before exact age; exact hours then break otherwise similar choices. Low-confidence dates and discovery-only timestamps sort behind trusted first-three-day postings.

## Coverage reconciliation

`coverage_reconcile.py` reads all three canonical stores and assigns cross-pipeline coverage state. It uses, in order, exact canonical URL, stable job ID, and a conservative unique company/title/location identity. Fuzzy similarity or mere company coverage is diagnostic only and never automatically suppresses a job.

When an external record exactly matches Official Careers, the Official record remains canonical and the external copy is marked/suppressed. Unmatched LinkedIn, Indeed, Glassdoor, ATS, or Syncareer records remain eligible even at an officially covered company. Reconciliation also retains source snapshot timestamps and review status needed by the dashboard.

## Outputs

Each pipeline owns:

- `jobs.json`: compact canonical store used by reconciliation and the dashboard;
- `seen_jobs.json`: durable first-seen identity state;
- `alert_history.json` and `digest_state.json`: notification history and daily digest control;
- `latest.md`, inbox files, and alert bodies: human-facing pipeline views;
- `latest_stats.json`: tracked latest-attempt counts, failures, funnel, enrichment, and output totals;
- `run_history.json`: bounded tracked history with per-run cost/model/cache/fallback/token/funnel/output data and compact per-batch decisions/errors for Pages drill-down;
- Board `matching_retry.json.gz`: only the JD context and retry state needed for failed LLM records; successful records leave the queue;
- `runs/*_stats.json`: deeper local history when present; these files are intentionally gitignored.

The dashboard build combines canonical jobs, coverage, alert history, company profiles, and browser review state into `public/dashboard.json` and `public/index.html`. It shows today's estimated LLM cost, bounded run history, batch/request/token/latency/JSON metrics, coverage and matching summaries, and per-job score reasons/gaps/provenance. Health generation writes `public/health.json`, `public/health-history.json`, and `public/health.html`.

## Automation and publication sequence

The cloud schedule is defined in `infra/scheduler/` and dispatches the three GitHub workflows in Pacific time. Refer to its README for deployment and timing rather than duplicating those operator instructions here.

For every discovery run, the publication chain is:

1. The owning workflow checks out current `main` and runs only its pipeline.
2. It commits only that pipeline's output tree and retries a non-fast-forward push against current `main`.
3. `reconcile-pages.yml` runs on relevant output/config pushes and after discovery workflows complete, including failed workflows.
4. Reconciliation reads the latest committed stores, rebuilds coverage, dashboard, and health, and deploys `public/` to Pages.

A successful collector or pipeline process is therefore not the same as successful publication. Verify the source/output commit, reconciliation run, Pages deployment, and live JSON when diagnosing missing jobs or stale presentation.

## Health semantics

Overall health remains the worst component severity. Component details preserve the distinction between data usability and the latest attempt:

| Status | Meaning |
| --- | --- |
| Healthy | A usable snapshot is within its freshness target and no material degradation is reported. |
| Warning | Fresh last-good data remains usable, but the latest attempt failed, output collapsed, enrichment degraded, or the component is approaching its stale threshold. |
| Stale | A previously usable pipeline snapshot exists but is older than 36 hours, or has records without a usable update timestamp. |
| Problem | No usable required snapshot exists, or a failed workflow leaves data unusable. |

Local sources use tighter collection expectations: up to six hours is healthy, six to twelve hours is warning, and more than twelve hours is stale. A required local source with no usable snapshot is a problem; an optional source is a warning. A failed latest attempt with a fresh last-good snapshot is recoverable degradation, not data loss.

Health output separates:

- **Actionable problems**: unusable or stale required data that needs intervention.
- **Recoverable degradation / known limitations**: current data is still usable but discovery, enrichment, fallback, or output quality was degraded.
- **Unresolved enrichment**: counts and reasons for records still lacking descriptions.

Messages include source, impact, attempt age, last-good count/age, consecutive failures, and available reasons. Repeated batch failures are collapsed into counts such as “1/1 attempted batches failed; 8 later batches skipped; 106 jobs remain retryable.” LinkedIn search/discovery failures, detail-enrichment 429s, Scrapling attempts/resolutions, and remaining no-JD records are reported independently. `PIPELINE_WORKFLOW_*` values supplied by reconciliation identify whether the triggering workflow failed; a failed trigger yields Warning when a fresh store is still usable and Problem when it is not.

## Failure recovery

| Failure | Preserved behavior | First checks |
| --- | --- | --- |
| Local discovery fails or returns unverified empty | Last-good source snapshot remains published | Source status/reason, query stop reasons, last-success age |
| LinkedIn search 429 | Existing snapshot remains usable; discovery coverage is degraded | Search/discovery status and retry/backoff evidence |
| LinkedIn detail 429 | Discovered cards remain; cache/peer/Scrapling may fill descriptions | Detail request/429 counts, Scrapling resolutions, remaining no-JD |
| One Official adapter fails | Other companies complete; prior data is carried when the sweep is not authoritative | Per-company errors and full-sweep status |
| LLM call or response fails | Cached scores remain; affected records receive rule fallback | Failure details, score-source counts, model/prompt fingerprint |
| LLM quota/balance is exhausted | First failed batch records the API code and available rate headers, later batches are skipped, and jobs remain retryable | `latest_stats.json`, `run_history.json`, then `board_pipeline.py --retry-llm-failures` after quota recovery |
| One discovery workflow fails | Other stores still reconcile; fresh last-good data can still publish with Warning | Workflow conclusion, store age/count, `latest_stats.json` |
| Concurrent output pushes race | Owning workflow rebases/retries its scoped output commit | Push attempt logs and current `origin/main` |
| Reconciliation or Pages fails | Pipeline stores remain committed; public site may be stale | Source/output commit, reconcile run, deployment, live artifact timestamp |
| State is corrupt | Reader rejects it instead of overwriting valid data | Error, file integrity, and last known committed snapshot |

## Debugging checklist

1. Identify ownership: local source, Board, Official Careers, Syncareer, reconciliation, or browser review state.
2. Inspect the owning compact store and its update timestamp before assuming a failed latest attempt means lost data.
3. Read `latest_stats.json` for funnel counts, source failures, enrichment, LLM source counts, and shown totals.
4. For local sources, compare `last_attempt_*` with `last_success_at`/`last_good_count`; for LinkedIn, split discovery from detail and Scrapling.
5. Confirm identity and coverage fields before changing deduplication or suppressing a record.
6. Confirm score source, prompt/profile fingerprint, tier constraints, company profile match, and recency evidence before changing ranking.
7. Trace publication from committed snapshot through workflow, reconciliation, Pages deployment, and live JSON.

## Matching regression guard

`tests/fixtures/matching_regression_round2.json` records the recent Board 429 population baseline and representative strong early-career, 70s/stretch, Level II, staffing/tech-service, internship, thin/no-JD, and non-software Engineer I cases. It also records the latest live comparison outcome. Offline sequential-run tests verify cache reuse across prompt/model changes, changed-JD scoring, safe failure fallback, retryability, and failed-only recovery behavior.
