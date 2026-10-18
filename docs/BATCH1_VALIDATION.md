# Batch 1 — Evidence and recall correctness

Implemented from the October 17, 2026 investigation against latest `origin/main`, `16b8bcdbbf3f9fd1b4bac13b968701313e3fc0f3`. Validation used that revision's saved records and the investigation's saved public employer responses. No crawler, scoring API call, production-state repair, or Supabase write ran.

## Scope

- Context-aware experience admission; company age and preferred/ambiguous experience do not hard-reject roles. Explicit required experience, including multiline headings, independent requirements, and actual degree alternatives, retains deterministic handling.
- Description/provenance roundtrips across remote handoff, local rehydration, and resolver caches. Legacy tentative methods restore uncertainty. Confirmed peer paths exclude tentative evidence.
- Exposed-original recovery validates structured posting identity before replacing fields; rejects conflicting requisitions/employers and ambiguous collections; accepts stable-ID minor title expansion. Failed HTTP and aggregator redirects cannot verify an identity.
- Meta's exact known URL aliases and complete responsibilities/qualifications; Two Sigma's actual Avature detail article. Avature retries metadata-only caches and retains last-good details without refreshing their age on failure.

Tier/gap/referral policy, identity migrations, notification delivery, recovery budgets, scoring/ranking, and the AI review pilot belong to later batches. SAP and HubSpot remain deferred because their replacement contracts were not established by this implementation.

## Saved-record replay

Each side ran against an isolated copy of the pinned baseline or changed source, reading identical saved evidence. All employer HTTP responses were replayed locally; no saved description or discovery timestamp was modified.

| Evidence | Before | After |
|---|---|---|
| CoStar SWE I–BizBuySell, Syncareer `8d87d67b97c87efa1542b704877bdda5` | `prefilter:high_yoe` on 35 years of company history | `keep` at role prefilter |
| Six early-title records from recovery handoffs, representing four company/title pairs | 6 rejected for high YOE | 6 pass role prefilter; four unique saved-description fixtures retained |
| Five saved legacy tentative remote rows | Handoff calls them `jd_available`; all five can become verified remote peers in an isolated replay | Handoff restores `jd_tentative` / `tentative` status; none becomes a verified peer |
| Meta `1404071541713403`, Production Systems Engineer, Edge | Alias rejected; description 991 characters, separate qualifications omitted | Exact alias accepted; assembled JD 3,523 characters including responsibilities and qualifications |
| Two Sigma `13079`, Quantitative Software Engineer: Generative AI | First article yields 80 characters; second run reuses that metadata | Actual JD yields 3,959 characters; second run reuses complete JD with no detail request |
| Two Sigma fresh metadata-only cache | Reuses 80 characters without attempting detail | Retries detail and obtains 3,959 characters from the saved response |

The six early-title records are WEX `4f01c77cb250595e31566b6e83df890f`, CoStar above, NVIDIA `a494c9221ec0584b175dafdbfb59c1fe` / `JR2026576`, and NVIDIA `0473cb8a89868458d632773f8a3b4ea0` / `JR2025458`. The replay count includes source representations; it is not six distinct opportunities. It used a bounded early-title pattern, so it does not reproduce the investigation's broader eight-record historical cohort.

The five legacy tentative IDs are Microsoft `200053670`, `200051537`, `200052807`, `200052779`, and Netflix `JR42273`. Their missing tentative match URLs cannot be reconstructed; the fix preserves uncertainty rather than inventing identity evidence. Stored production artifacts are left intact; normalization applies when these records are read/reused.

CoStar's replayed description SHA-256: `2525b53cf9da261b2aca091f0299068e48a4ff5e90bb4e0afa64967f30c46fd9`.

These results establish parser, prefilter, and reuse behavior on saved evidence. They do not establish current job availability, suitability, final recommendation gains, or source-wide recovery rates. Existing fallback scoring still has separate experience heuristics; passing the prefilter does not imply an A/B recommendation.

## Regression validation

Focused group: **216 passed, 1 skipped** (the opt-in live matching regression). No live key was loaded. Command:

```bash
python3 -m pytest -q -p no:cacheprovider \
  tests/test_batch1_correctness.py tests/test_matching_incremental.py \
  tests/test_remote_recovery.py tests/test_official_jd_recovery.py \
  tests/test_coverage_jd_recovery.py tests/test_official_careers_adapters.py \
  tests/test_fresh_recovery.py tests/test_visibility.py
```

The new Batch 1 file contains 19 tests, including public page fragments, saved early-career descriptions, two-run JD reuse, thin-cache retry, last-good retention, tentative handoff/rehydration, legacy uncertainty, unrelated redirects, conflicting requisitions, valid title-slug identity, and failed HTTP paths. The existing missing-listing-date test now freezes its fixture clock; its September timestamp must not age past the production cache TTL during the test. Public fixture lineage and sanitization are documented in [the fixture README](../tests/fixtures/jd_recovery/README.md).

Independent review reproduced three initial defects: a remaining legacy-tentative fast path, overly strict slug/title matching, and mixed/multiline experience handling. They were corrected and covered by regression cases. A follow-up caught a missing `at least` cue; that cue and employer-history controls were added. Additional independent probes checked valid postings, changed IDs/employers, aggregator redirects, HTTP/fallback failure, and provenance copy. The final narrow recheck passed seven checks and reported no blocking findings.

No full suite, scheduled production run, live employer request, or paid model evaluation was performed. Generated test artifacts were discarded from the disposable worktree; only source, tests, fixtures, and documentation are published.
