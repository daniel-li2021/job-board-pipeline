# Pipeline algorithm and execution reference

This document explains how data moves through the system, which process owns each artifact, and how to reason about partial failures. It is the detailed companion to the [README](../README.md): use the README for setup and operator commands, and use this file when changing, debugging, or recovering the pipeline.

## System map

```text
Mac collectors                      GitHub discovery workflows
  LinkedIn search + detail            Board: Indeed + public ATS + online JD recovery
  Glassdoor search                    Official Careers: company adapters
  local JD recovery                   Syncareer: search + detail API
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

The three discovery pipelines are deliberately independent. A failure in one does not prevent the other stores from being reconciled and published. GitHub owns ATS, Indeed, Big Company Official, Syncareer, Board matching, and online JD recovery. The Mac owns LinkedIn, Glassdoor, and local JD recovery. Board consumes the latest committed Mac snapshots.

Indeed query failures preserve results from completed queries. The collector reports succeeded, failed, and unrun queries; a partial run overlays its successful rows on the prior snapshot, deduplicates by source identity, and retains unobserved cached rows without advancing their verification time. Existing richer JDs are retained when a partial row is thinner. The last complete collection timestamp stays fixed. Board consumes the merged rows through its ordinary JD lookup, recovery, filtering, and matching stages, and records the Indeed error in `failures.discovery`. Indeed and Board Health show Partial, including fresh kept and cached reused counts. A later complete collection replaces the merged snapshot and advances the complete collection timestamp.

## Ownership and state

| Owner | Responsibility | Durable artifacts |
| --- | --- | --- |
| Primary checkout | Development, tests, documentation, and reviewed changes | Source code and tracked configuration |
| Local automation checkout | LinkedIn and Glassdoor collection; local JD recovery | `output/sources/{linkedin,glassdoor,remote_recovery,health}.json` |
| Board workflow | Indeed and public ATS discovery, online JD recovery, matching | `output/sources/indeed.json`, `output/board/`, `output/recovery/board.json.gz` |
| Official Careers workflow | Company career-site adapters | `output/official_careers/` |
| Syncareer workflow | Syncareer search and detail API | `output/syncareer/` plus dated reports in `output/daily/` |
| Reconciliation workflow | Cross-pipeline identity, dashboard, health, and Pages deployment | `output/cross_pipeline/coverage.*` and `public/` at build time |
| Browser/Supabase review state | Per-user review and application decisions | Remote review rows; source-expired applied rows are restored into the dashboard |

The development checkout must not become a second local collector. `scripts/local_source_sync.sh` runs collection from `/Users/daniel/Projects/job_scrape_feasibility-automation` in an isolated worktree and stages LinkedIn, Glassdoor, local recovery, and health artifacts. GitHub Actions owns the Indeed snapshot and three pipeline output trees.

Persistent JSON state is written atomically where interruption could corrupt the canonical store. Corrupt or structurally invalid state is rejected rather than silently replacing a last-good store. Large full-detail caches and timestamped local run files are gitignored; compact stores, bounded `run_history.json`, and `latest_stats.json` are tracked so Actions and Pages can consume useful current state.

## Shared record and time invariants

All sources normalize into the schema in `sources/schema.py`. The important invariants are:

- Prefer a stable source job ID or canonical application URL for identity. Company + title + location is a conservative fallback, not a claim that similar-looking requisitions are identical.
- `first_seen` records when this system first observed a job and survives rediscovery. `last_seen` records the latest successful observation.
- Local source cards receive `first_seen` when first discovered, before Board consumes their snapshot. Board counts new jobs against the seen state from before the run. If a known source job later gains an official URL, its original discovery time survives the identity change and it is not counted as new again; legacy jobs with no trustworthy discovery time remain unknown.
- A trusted source posting timestamp is used for posted-age ranking only when its confidence is high or medium. Low-confidence or missing posting dates fall back to discovery time and sort behind trusted first-three-day records.
- Dashboard Fresh and Rolling windows use exact `first_seen` datetimes (`<=24h` and `<=72h`). They are discovery views and are intentionally separate from posted-age ranking.
- In Board Online and Mac Local recovery, only Fresh jobs (`first_seen <=24h`) receive outbound JD requests. Rolling jobs remain visible until 72 hours, and missing a JD does not extend that window. Applied and In Progress history persists separately from discovery freshness.
- Compact tracked stores retain display, match, provenance, coverage, and review fields. Full Indeed descriptions persist in its source snapshot; other full descriptions and raw source material remain in source snapshots, recovery handoffs, or local caches where available.
- Every discovered canonical record receives an enrichment outcome and remains auditable even if it is later filtered or suppressed.

## Local source pipeline

`local_sources.py` runs LinkedIn and Glassdoor independently and updates `output/sources/health.json` after every attempt. The Board workflow runs `remote_indeed.py` and updates the same health state for Indeed.

### Collection

- Mac LinkedIn uses Software Engineer (up to five pages), AI Engineer (three), and an alternating Backend Engineer / Full-Stack Engineer query (two), at most 10 search pages total. The persisted query cursor advances only when search requests occur, rotates the starting query, and alternates the third query; Machine Learning Engineer is omitted from local discovery. All Search and Detail requests, including targeted search and follow-up recovery, use one ordinary HTTP transport and wait until 2.5–3.25 seconds after the preceding attempt. Empty/low-unique pages retain their existing stops; two consecutive pages yielding at most one identity absent from both the persistent source ledger and this scrape stop the query. Every returned card continues through the existing selection/recovery path. Per-page new-to-ledger and known-ID counts are recorded; this is discovery identity evidence, not a title/fit decision. The 24-hour window and middle discovery slot remain unchanged (see [measurements and tradeoffs](LINKEDIN_TRANSPORT.md)). Search 429 stops requests immediately; two attempted 429 runs trigger a 24-hour cooldown and a one-page probe. Partial cards merge with last-good rows without advancing carried-row verification time.
- GitHub Indeed and Mac Glassdoor use their own source-specific discovery page budgets. These budgets limit discovery traffic only; they do not truncate processing of cards already returned.
- Glassdoor first uses JobSpy. When its location lookup cannot produce results, the Scrapling/static-page fallback can still preserve cards and snippets. Detail-page blocking remains an explicit enrichment limitation.
- Per-query diagnostics retain pages fetched, stop reasons, results, unique contributions, and enrichment outcomes where the collector provides them.

### Last-good behavior

Each source has two distinct states:

1. **Latest attempt** — when collection was tried, its result count, status, query diagnostics, detail-enrichment diagnostics, and failure reason.
2. **Last-good snapshot** — the most recent verified non-empty data that downstream code may safely consume.

A failed or empty-unverified attempt does not overwrite a usable last-good snapshot. This distinction is fundamental: a current attempt can be degraded while the published data remains fresh and usable. An empty result replaces prior data only when the collector can verify that the empty result is authoritative.

For LinkedIn, health keeps independent search and detail 429 streaks, cooldowns, and probes. The first detail 429 starts a 12-hour detail cooldown and stops further LinkedIn detail requests. Non-LinkedIn recovery continues; Search can resume after the shared transport pause. After 12 hours (or a longer `Retry-After`), one successful detail probe clears the cooldown; another 429 restarts it. Cache and official-web enrichment continue while detail is paused. The transport caps total LinkedIn attempts at 18 per round/rolling hour and 54 per rolling 24 hours. Detail attempts share an 8-request round/hour and 24-request rolling-day cap across initial enrichment and follow-up recovery; a detail probe consumes the entire Detail allowance for its round. Any 429 closes both endpoints for the round and persists a shared pause of at least one hour or the longer `Retry-After`. Independent Search/Detail cooldowns and streaks still advance only on their endpoint attempts. Retry headers can extend their cooldowns. No automatic HTTP retries or redirect following occurs. The latest 20 429 events retain endpoint URL, query/title, zero-based Search page (null for Detail), round/endpoint ordinals, and per-endpoint 60-second, one-hour, and 24-hour counts. `health.json.linkedin_transport` retains the bounded rolling attempt journal; `scripts/local_source_sync.sh` also supplies a durable `output/logs/linkedin_transport.json` journal outside ephemeral collector worktrees, so failed publication cannot reset the local allowance. Search cooldown is an explicit `cooldown` result with zero search requests, not an HTTP failure. With a usable snapshot, the collector still runs shared JD recovery, publishes `mac_last_completed_at`, and exits successfully. Only successful publication lets the gate complete the slot; failed collection/publication remains retryable. The existing ten-minute check, fixed slots, quiet hour, and nonblocking runner lock remain unchanged.

### Publication

The local sync script validates repository and push prerequisites, collects in an isolated checkout, stages only Mac-owned snapshots and health, and pushes the source commit. If `main` advances, it retries against the current remote state without mixing pipeline-owned output into the local commit. Board Actions sees Mac jobs only after this push succeeds. Its own workflow commits the GitHub-produced Indeed snapshot and full JDs.

The Mac gate has fixed noon, 3 PM, and 9 PM Pacific slots. Every ten-minute check derives the latest missed slot from the schedule and last completed run; a missed slot can start a catch-up outside the 5:00–5:59 PM quiet hour, unless a successful Local run finished within the previous three hours. Health publishes the last and next slots plus pending or skipped catch-up state.

## Board pipeline

`board_pipeline.py` is the shared implementation for filtering, matching, tiering, and application ordering. Its execution order is significant:

1. Collect Indeed, collect public ATS jobs, and read committed LinkedIn and Glassdoor snapshots.
2. Normalize, merge exact identities, verify exposed official URLs, and collapse cross-source duplicates again.
3. Load the prior store, preserve `first_seen` across source and official-URL identity changes, set `last_seen`, and compute recency before filtering. Keep a copy of the pre-run seen identities for new-job counts.
4. Annotate cross-pipeline coverage.
5. Enrich thin records from exact peers. For Fresh, eligible records, apply deterministic filters and batched metadata triage before outbound direct-URL and web recovery; keep skipped or unresolved cards for later filtering and diagnostics.
6. Apply company exclusions and flags. A company covered by Official Careers is not globally hidden; only an exact reconciled duplicate is suppressed.
7. Apply hard eligibility filters such as non-US, explicit seniority, citizenship/clearance, and other material constraints.
8. Apply the shared role/seniority prefilter to reduce obvious mismatches before an LLM call.
9. Score active candidates, assign tiers, apply referral actions, and sort for application priority.
10. Rebuild the canonical store with kept and dropped records, then write visible Tier A/B outputs and run statistics.

`--no-digest` suppresses the user-facing digest only. It still persists stores, `first_seen`, scores, tiers, and `latest_stats.json`, which allows source-push runs to maintain state without generating duplicate notifications.

The discovery count compares both source and final canonical identities with the pre-run seen state. A source job discovered by Indeed just before Board starts counts as new; a previously seen job that acquires an official URL does not. Reported new and added counts therefore refer to this run's discoveries rather than identity rekeys.

## Official Careers pipeline

`official_careers.py` runs the company registry in `sources/careers/registry.py`. Adapters use public APIs, ATS endpoints, rendered listings, or company-specific parsers. Companies are isolated and collected with bounded concurrency, so one adapter failure does not discard successful companies.

The raw cache records per-company completion and diagnostics. A successful full sweep may retire listings that disappeared; an incomplete or failed sweep carries prior records forward rather than treating missing data as verified removal. The normalized records then reuse Board's hard filters, role prefilter, matcher, tiering, ordering, stores, and alert logic. Exact Board and Syncareer peers may supply a missing description before scoring.

Metadata-only Official listings pass location, title, seniority, and other safe metadata checks before detail retrieval. Clear survivors enter a recent-first queue rotated across companies; borderline titles can receive cached, batched GPT-6 Luna Medium `recover/skip` triage. A run makes at most 150 additional detail attempts. Targeted extractors handle Meta, Disney, Netflix, and Equinix, with a safe generic path for other eligible jobs. Detail identity is checked before adopting a JD. Equinix may use one bounded browser bootstrap when its HTTP response is a challenge; unresolved challenges retain last-good jobs or JDs. `output/official_careers/recovered_jds.json.gz` preserves selective JD and triage evidence for later runs. The scrape report gives eligible and usable JD counts, cache reuse, requests, elapsed time, deferrals, and failures. Unresolved jobs keep the thin-JD matching fallback.

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

GitHub online JD recovery checks exact caches, Official/ATS, and the persisted Indeed snapshot before company/title web search. The Mac reads the compressed Online handoff, including unresolved candidates, and the Indeed snapshot as exact peers. Both use `official_jd_recovery.Resolver` and `recover_pending`: each run stops after 100 distinct jobs with an outbound attempt or 20 elapsed minutes, with bounded search/page requests. Cheap cache and exact-peer checks do not spend the job quota. Fresh, thin-JD jobs pass safe filters and reusable batched GPT-6 Luna Medium metadata triage before costly requests; a triage `skip` defers recovery but does not remove the job. Jobs are prioritized by available evidence and discovery time. Per-method failed-attempt evidence avoids repeating unchanged work immediately. For Local LinkedIn, both `run_one()` and `recover_jds()` apply safe metadata admission before enrichment: excluded companies, explicit senior/lead/staff/principal/manager titles, clearly irrelevant titles, non-US locations, and explicit title constraints do not spend Detail requests. Ambiguous technical titles and unknown/remote locations remain eligible; JD-dependent constraints wait for JD evidence. Fresh saved LinkedIn JDs and existing exact Official/ATS/Indeed peers are tried first, followed by the bounded non-LinkedIn `recover_pending` paths. Only then does batched metadata-only Luna triage decide whether obtaining the full JD could materially change the fit decision. Explicit `needs_jd=true` admits Detail; false, malformed/missing results, and API failures defer Detail while retaining the card or tentative JD. This decision is separate from matching scores and existing `recovery_triage`. Metadata, candidate-profile, and recovery-evidence hashes invalidate cached Detail decisions when evidence changes. Both phases share a single Detail request counter on the round's existing `RecoveryBudget`: at most 8 ordinary HTTP requests, 0 during cooldown, or 1 for an expired-cooldown probe. Initial probe success cannot increase that round's allowance. A 429 stops later LinkedIn Detail requests while non-LinkedIn recovery continues. `detail_enrichment.admission` / `linkedin_detail.admission` record pre-rule candidates, rule reasons, saved-cache reuse, non-LinkedIn resolutions, newly evaluated triage, triage deferrals, and worth-Detail jobs; `round_request_limit` and `round_requests` expose the shared allowance. DuckDuckGo HTML search is preferred; transport failure switches to Bing HTML, and a second provider failure defers search rather than recording a confident no-match.

Failure to obtain a description does not delete a valid job card. The job keeps `enrichment_failure_reason`, uses title/metadata evidence conservatively, and remains visible for diagnostics. A cached metadata triage result can make only a small, bounded adjustment to the rule fallback; it is not a full-JD score and remains conservatively tiered. Explicit software/AI/data early-career titles remain useful review signals; generic `Engineer I` or `Entry Level` wording alone receives only a small title bonus. This is different from a hard eligibility failure.

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

Unknown companies are accumulated before dashboard visibility filters in `profile/company_profiles_pending.json`. Each entry retains `seen_count` and compact distinct-job keys; repeat runs do not count the same job twice. For older entries without retained identity evidence, a count of one is a lower bound. `scripts/pending_company_subset.py` lists companies seen in at least a chosen number of distinct jobs. `scripts/enrich_company_profiles.py` imports curated batches and optional local USCIS/DOL/SEC evidence, keeps unknown values where evidence is absent, and sends conflicts to manual review. Explicit JD sponsorship evidence takes precedence over company metadata.

Company metadata never changes `match_score`. Within the actionable tiers it helps application ordering:

- generally prefer high-priority, sponsor-friendly larger employers, strong technology companies, and mature or growth-stage startups;
- down-rank staffing firms, poor/unknown sponsorship where configured, and defense or clearance-heavy employers;
- apply a mild `tech_service` ordering penalty so large consulting/IT-services employers do not outrank stronger product-company opportunities on size and sponsorship alone;
- down-rank internship/co-op roles by default;
- do not enforce a fixed role-family hierarchy: retain the score's assessment of the actual work and material requirements.

Recency is calibrated as an ordering constraint rather than a single mechanical weight. Within roughly the first three posted days, posting day is compared before quality so a materially newer day remains meaningful. Within the same posting day, a five-point fit band and company/application quality come before exact age; exact hours then break otherwise similar choices. Low-confidence dates and discovery-only timestamps sort behind trusted first-three-day postings.

## Coverage reconciliation

`coverage_reconcile.py` reads all three canonical stores and assigns cross-pipeline coverage state. When both a local raw Official cache and the compact published Official store exist, it uses the candidate with the newest snapshot timestamp so a stale development cache cannot override fresh committed data. Identity uses, in order, exact canonical URL, stable job ID, and a conservative unique company/title/location match. Fuzzy similarity or mere company coverage is diagnostic only and never automatically suppresses a job.

The published audit keeps the exact reconciliation rate and adds an exclusive loss funnel: external jobs in scope, supported company, comparable Official snapshot, Official candidate found, and exact identity matched. It separates unsupported companies, discovery misses, identity mismatches, newer source records, unverified or partial Official runs, and missing company names, with top contributing companies. Batched GPT-6 Luna Medium assessments of unresolved identity pairs are cached in `output/cross_pipeline/identity_ai_cache.json`. A `likely_same` answer is evidence only; the AI-assisted path promotes an exact match only after verifying a direct employer URL redirect. Ordinary exact matching still uses deterministic URL and stable-ID evidence.

When an external record exactly matches Official Careers, the Official record remains canonical and the external copy is marked/suppressed. Multiple same-title/location Official candidates are recorded as `official_ambiguous` and remain visible rather than being attached arbitrarily. Unmatched LinkedIn, Indeed, Glassdoor, ATS, or Syncareer records remain eligible even at an officially covered company. Reconciliation retains all three snapshot timestamps, exact-match methods, pending refreshes, genuine gaps, expected unsupported sources, and review status. Every reconciliation/Pages build publishes the current Markdown audit as `coverage.md`, so it refreshes after any Board, Official, or Syncareer workflow rather than depending on a tracked report commit.

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

The dashboard build combines canonical jobs, coverage, alert history, company profiles, and browser review state into `public/dashboard.json` and `public/index.html`. It shows today's estimated LLM cost, bounded run history, batch/request/token/latency/JSON metrics, coverage and matching summaries, and per-job score reasons/gaps/provenance. Review-dependent views and counts wait for the first Supabase review-state load. A successful load uses remote rows as the baseline and merges only pending local edits; a failed load explicitly labels the cached fallback. Source-expired Applied and In Progress history remains available. Legacy run records without measured latency, JSON reliability, or batch outcomes display `Unknown`/`—`; new runs retain real measured zeroes through explicit telemetry flags. Health generation writes `public/health.json`, `public/health-history.json`, and `public/health.html`, and reconciliation also copies the current audit to `public/coverage.md`.

## Automation and publication sequence

The cloud schedule is defined in `infra/scheduler/` and dispatches the three GitHub workflows in Pacific time. Refer to its README for deployment and timing rather than duplicating those operator instructions here.

For every discovery run, the publication chain is:

1. The owning workflow checks out current `main` and runs its owned source collection and pipeline.
2. It commits its output tree and source/recovery artifacts, then retries a non-fast-forward push against current `main`.
3. `reconcile-pages.yml` runs on relevant output/config pushes and after discovery workflows complete, including failed workflows.
4. Reconciliation reads the latest committed stores, rebuilds coverage, dashboard, and health, and deploys `public/` to Pages.

A successful collector or pipeline process is therefore not the same as successful publication. Verify the source/output commit, reconciliation run, Pages deployment, and live JSON when diagnosing missing jobs or stale presentation.

## Health semantics

The main Health page uses three run states. **Healthy** means required data is usable and expected steps completed without an active failure. **Partial** means an expected search, source, JD, or workflow step failed or became stale while fallback data remains usable. **Failed** means required data is unusable. Overall state is the worst state among Board, Official, Syncareer, LinkedIn, and Indeed; optional Glassdoor appears in Today and Needs attention but does not change Overall. The detailed `Healthy` / `Warning` / `Stale` / `Problem` component status remains in `health.json` for diagnostics alongside each component's `run_state`.

Latest runs use the same Jobs → JD & recovery → Requests → Sources → Issue order for Online Board, LinkedIn Local, Big Company Official, and Indeed. Issue appears only for an abnormal run. LinkedIn distinguishes jobs first discovered in the exact attempt, earlier on the same Pacific day, and older known jobs; its JD coverage uses fresh jobs that needed a JD rather than all carried rows. Board labels its deduped source input as current source jobs, separates new jobs from A/B shown and newly added, and labels each source contribution as current / new. It combines measured direct and follow-up JD recoveries and retains the breakdown. Official labels raw listings scanned and relevant jobs after filters separately; its JD recovery pool is a candidate set, not the count of relevant jobs in this run. Indeed distinguishes current fresh rows from last-good rows during a partial run. Counts come from each owner’s latest stats, source snapshot, and Health state; missing counters are not inferred from unrelated inventory.

Today shows each source's Pacific-day new jobs, new A/B additions, run count, failed-run count, consecutive failures, latest run, and current issue. For Board, Official, and Syncareer, daily new and new A/B counts sum run-history outcomes; the latest A/B shown count remains a separate latest-run result so repeated retained output is never summed. `output/sources/health.json` keeps a bounded receipt for each LinkedIn, Indeed, and Glassdoor collection attempt with run time, raw status, new jobs, failure, elapsed time, and nullable pass/new A/B fields. A source collection cannot measure Board matching by itself; Today attributes new A/B additions from Board run history when that attribution is complete. A source without a recorded run today shows `—` for new and A/B results; a measured zero appears only after a run. Before the first receipt, same-day legacy source attempts display unavailable totals rather than inferred counts. Mac sources use tighter collection expectations: up to six hours is healthy, six to twelve hours is warning, and more than twelve hours is stale. GitHub Indeed warns after 18 hours and becomes stale after 36 hours. The main state maps usable stale/fallback data to Partial and unusable required data to Failed. Focused LinkedIn coverage can remain Healthy when it is expected and its latest attempt succeeded without a rate limit or detail failure.

Technical details retains current Board and LinkedIn JD gaps separately from older stored jobs without JD. The fresh source counts may overlap; older inventory uses the compact store's `description_available` flag rather than treating intentionally omitted JD text as missing. The full Official funnel and legacy aggregate counters also remain there. Needs attention lists current abnormal components and a fresh JD backlog only once its pending count reaches the existing actionable threshold. A healthy Indeed attempt does not display a recovered previous failure as a current issue; that history remains in technical diagnostics. Execution labels newly available JDs from measured direct and follow-up work; initial LinkedIn detail fetches are included. The Remote collector does not yet report a complete new-JD count, so the page displays an unavailable value instead of relabeling its current JD inventory as new work. Raw component statuses, source failures, consecutive failure counts, request limits, recovery methods, unresolved examples, and the Mac schedule remain under Technical details and in `health.json`. Visible times use Pacific time.

LinkedIn Local shows **Search 429 this run** and **Detail 429 this run** independently, with search/detail cooldown deadlines and independent streaks. Recovery’s aggregate `linkedin_rate_limited` flag means further LinkedIn traffic was stopped; it is not evidence of a detail 429. Follow-up `linkedin_detail` counters identify actual detail responses, including `http_status_counts`; stored `failure_reasons` describe unresolved job outcomes and can retain old HTTP reasons after a successful probe. Cooldown/deferred receipts and expected request-budget exhaustion do not count as new failures. Initial detail counters come from the matching search snapshot, with follow-up detail requests counted separately so recovery cannot overwrite the initial request history.

`LinkedIn (Mac)` search/discovery failures, detail 429s, Scrapling attempts, and remaining no-JD records are independent from the `linkedin_company_official_adapter`. Configured Official `skip` adapters remain known limitations. `PIPELINE_WORKFLOW_*` values supplied by reconciliation identify a failed triggering workflow; a fresh usable store then yields Partial, and an unusable required store yields Failed.

## Failure recovery

| Failure | Preserved behavior | First checks |
| --- | --- | --- |
| Local discovery fails or returns unverified empty | Last-good source snapshot remains published | Source status/reason, query stop reasons, last-success age |
| LinkedIn search 429 | Existing snapshot remains usable; discovery coverage is degraded | Search/discovery status and retry/backoff evidence |
| LinkedIn detail 429 | Discovered cards remain; cache/peer/Scrapling may fill descriptions | Detail request/429 counts, Scrapling resolutions, remaining no-JD |
| Missed Mac Local slot | The ten-minute gate retries outside the quiet hour unless a recent successful run suppresses catch-up | Latest scheduled slot, last completed run, `scheduled_slot_missed`, `catch_up_status` |
| Official detail or Equinix discovery challenge | Cached JD and last-good company records remain usable; unresolved work is deferred | Eligible/usable JD counts, detail attempts, browser requests, per-company failures |
| One Official adapter fails | Other companies complete; prior data is carried when the sweep is not authoritative | Per-company errors and full-sweep status |
| LLM call or response fails | Cached scores remain; affected records receive rule fallback | Failure details, score-source counts, model/prompt fingerprint |
| LLM quota/balance is exhausted | First failed batch records the API code and available rate headers, later batches are skipped, and jobs remain retryable | `latest_stats.json`, `run_history.json`, then `board_pipeline.py --retry-llm-failures` after quota recovery |
| One discovery workflow fails | Other stores still reconcile; fresh last-good data can still publish with Partial | Workflow conclusion, store age/count, `latest_stats.json` |
| Concurrent output pushes race | Owning workflow rebases/retries its scoped output commit | Push attempt logs and current `origin/main` |
| Reconciliation or Pages fails | Pipeline stores remain committed; public site may be stale | Source/output commit, reconcile run, deployment, live artifact timestamp |
| State is corrupt | Reader rejects it instead of overwriting valid data | Error, file integrity, and last known committed snapshot |

## Debugging checklist

1. Identify ownership: Mac LinkedIn/Glassdoor/recovery, GitHub Indeed/Board/Official/Syncareer, reconciliation, or browser review state.
2. Inspect the owning compact store and its update timestamp before assuming a failed latest attempt means lost data.
3. Read `latest_stats.json` for funnel counts, source failures, enrichment, LLM source counts, and shown totals.
4. For local sources, compare `last_attempt_*` with `last_success_at`/`last_good_count`; for LinkedIn, split discovery from detail and Scrapling.
5. Confirm identity and coverage fields before changing deduplication or suppressing a record.
6. Confirm score source, prompt/profile fingerprint, tier constraints, company profile match, and recency evidence before changing ranking.
7. Trace publication from committed snapshot through workflow, reconciliation, Pages deployment, and live JSON.

## Matching regression guard

`tests/fixtures/matching_regression_round2.json` records the recent Board 429 population baseline and representative strong early-career, 70s/stretch, Level II, staffing/tech-service, internship, thin/no-JD, and non-software Engineer I cases. `matching_model_comparison_v7_2026-09-13.md` records the apples-to-apples Terra/Sol quality, cost, and latency comparison for the current prompt. Offline sequential-run tests verify cache reuse across prompt/model changes, changed-JD scoring, safe failure fallback, retryability, and failed-only recovery behavior.
