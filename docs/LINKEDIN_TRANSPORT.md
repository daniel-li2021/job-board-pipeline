# LinkedIn transport and queue review — 2026-10-05

## Current change and expectations

The Oct 2–4 Pacific production sample supports a modest relaxation, not a claim
that larger allowances are proven safe. Adopt the requested nearby configuration:

| Scope | Previous | Current |
| --- | ---: | ---: |
| Search per round | 10 | 10 |
| Detail per round / rolling hour | 8 | 12 |
| Search + Detail per round / rolling hour | 18 | 22 |
| Detail per rolling 24 hours | 24 | 36 |
| Search + Detail per rolling 24 hours | 54 | 72 |

Three fully utilized scheduled rounds can issue 66 total requests (30 Search,
36 Detail); the 72-total rolling cap leaves six total requests of headroom for
catch-up/manual traffic, but no extra Detail when all 36 daily Detail slots were
used. Rolling windows, not Pacific midnight, enforce these allowances. The
relaxation adds four Detail opportunities per full round; it does not guarantee
four extra recovered JDs. For the frozen 18-worthwhile case, 12 slots would leave
six deferred instead of ten if all requests succeeded. This is a capacity
counterfactual, not a measured post-change production outcome. Keep the caps at
these values until the two-day review; no Search-depth increase is justified.

## Friday–Sunday production evidence

Nine distinct Local round recovery reports in the installed automation
checkout's `output/logs/local-sources.out.log`, cross-checked with committed
source snapshot metadata, show:

| Pacific day | Rounds | Search attempts | Detail attempts | Total | Recorded LinkedIn 429 events |
| --- | ---: | ---: | ---: | ---: | ---: |
| Friday Oct 2 | 3 | 20 | 16 | 36 | 0 |
| Saturday Oct 3 | 3 | 22 | 16 | 38 | 0 |
| Sunday Oct 4 | 3 | 22 | 13 | 35 | 0 |
| Total | 9 | 64 | 45 | 109 | 0 |

Actual run times were Friday 12:45/18:08/21:58, Saturday 12:00/15:00/21:00,
and Sunday 13:38/15:00/22:24 Pacific. These are recorded Local attempts,
not an account/IP-wide trace. Five rounds consumed all eight Detail requests.
Saturday 15:00 stopped at `global_day_budget`, with 30 Search + 24 Detail in
its rolling day; its two searches and zero Detail demonstrate capacity pressure
rather than an HTTP failure. The small zero-429 sample supports a guarded
experiment; it cannot establish LinkedIn's safe rate threshold.

Committed source receipts: `2659674`, `d007581`, `c3b4994`, `0324a08`,
`8c2408b`, `d21c9b7`, `7a8b432`, `f895d67`. Friday noon's recovery report
is retained in the local log; it did not produce a new LinkedIn source snapshot.

## The 18-worthwhile / 8-Detail cohort

At Friday Oct 2 18:08 Pacific (`2659674`), initial admission recorded 58 Fresh
thin candidates, 29 rules skips, 10 non-LinkedIn resolutions, 19 LLM evaluations,
one triage deferral, and 18 explicit `needs_jd=true` admissions. Eight Detail
attempts all returned 200 and recovered a JD; ten were budget-deferred. The ten
non-LinkedIn resolutions happened **before** that 18-job admission and are a
separate cohort from the ten Detail deferrals.

Trace the deferred cohort by immutable LinkedIn job ID across all eight source
snapshots through Sunday 22:24, plus current Board entries and recovery handoff:

| Job ID | Employer / role | Later Detail | Outcome through Sunday |
| --- | --- | --- | --- |
| 4474564016 | AWS / Software Dev Engineer, IAM | Friday 21:59 follow-up | JD recovered |
| 4474731508 | Rippling / Engineer II Backend | Friday 21:58 initial | JD recovered |
| 4474742062 | Rippling / Engineer II Backend | Friday 21:58 initial | JD recovered |
| 4473159456 | Boeing / Java Software Engineer | None | Unresolved; aged out of Fresh |
| 4474599498 | Deloitte / Full Stack Engineer II | None | Unresolved; aged out of Fresh |
| 4474706198 | Deloitte / Full Stack Engineer II | None | Unresolved; aged out of Fresh |
| 4473197371 | Haystack / Mid-level Software Engineer | None | Unresolved; aged out of Fresh |
| 4472847721 | Scribd / Engineer II Fullstack | None | Unresolved; aged out of Fresh |
| 4472855479 | Scribd / Engineer II Fullstack | None | Unresolved; aged out of Fresh |
| 4473364054 | Spectrum Equity / Engineer II Fullstack | None | Unresolved; aged out of Fresh |

Totals: 3/10 later Detail recoveries, 0/10 recorded Official/ATS/peer/generic
recoveries, 7/10 still unresolved, and those same 7/10 expired from Fresh without
any Detail attempt. Their `first_seen` was Friday 18:08; Fresh ended Saturday
18:08, before Saturday's evening round. These are ten distinct IDs, including
similar-title pairs; no claim of ten distinct employer requisitions is made.

Two causes are visible in code: equivalent LLM priorities were sorted newest
first, and initial discovery consumed the shared allowance before follow-up
could consider the entire saved snapshot. At Friday evening one follow-up slot
remained and went to AWS; Saturday's initial eight again exhausted the allowance.
The rows retained their positive triage but did not retain an explicit waiting
age and were excluded from outbound recovery after Fresh expired.

## Queue policy and preserved protections

Use LLM high/normal/low priority first, then already budget-deferred and
never-attempted cards, then oldest discovery time, then deterministic identity.
Include saved admitted unresolved cards in initial recovery/admission alongside
current discovery. Before Detail, retain the safe metadata rules, saved-JD cache,
exact Official/ATS/Indeed/remote peers, and bounded non-LinkedIn recovery. The
batched GPT-6 Luna Medium `needs_jd` and priority decision remains mandatory;
its existing evidence/profile hash controls cache reuse. Fit scoring is unchanged.

Persist first budget deferral (`linkedin_detail_deferred_at`) and actual
`attempted_ids`; rediscovery of unchanged metadata carries that queue state
forward. A never-attempted, already admitted budget waiter retains one Detail
opportunity through 72 hours (the existing Rolling visibility window). This
narrow Local Detail exception prevents automatic loss at 24 hours without
refreshing `first_seen`, source verification, or generic outbound recovery
eligibility. Old untriaged/negative rows and previously attempted rows do not
receive the exception. Fresh retries still obey their existing retry timer.
At 72 hours, report missed opportunities explicitly. Sustained overload or
cooldowns can still prevent an attempt; the queue never bypasses transport or
recovery budgets to promise coverage.

Search max 10, new-to-ledger early stops, 2.5–3.25-second randomized spacing,
immediate first-429 stop, Retry-After, independent Search/Detail cooldowns,
guarded single probes, persistent request accounting, and last-good snapshots
remain enforced. Carried JD recovery does not count as new discovery or refresh
its verification timestamp. Normal scheduled collectors fetch `main` before
running; no extra crawler or external LLM/API call was launched for validation.

## Observability and two-day evaluation

`health.json.local_recovery_history` retains 120 bounded reports, including
`initial_detail` and follow-up `linkedin_detail`, each with `queue` job IDs,
priority, admission, first-seen/first-deferral/attempt timestamps, current-phase
attempt flags, resolution method, deferral reason, and past-Fresh status.
Transport summaries now expose hour caps as well as round/day caps and counts.
`queue_expired_without_attempt` names budget waiters still unresolved beyond
72 hours. Generic provider failures, methods, cheap matches and job deferrals
are retained separately. Existing console/latest JSON reports remain available.

For the next two days, review normal published receipts and the durable local
request journal without launching extra collectors. Check collector commit,
per-round/rolling caps, both endpoint 429s and probe/cooldown state, attempted
versus recovered JDs, saved-waiter resolution and maximum wait, unresolved
past-Fresh/72-hour expirations, triage-unavailable cases, and non-LinkedIn
methods/provider/budget failures. Report denominators and missing evidence.
Compare with the nine-round 109-attempt / 45-Detail baseline above. Notify on a
meaningful coverage change, any new 429, missed opportunity, execution failure,
or required action; produce a final comparison at the end of the review period.
A new 429 is evidence to review/revert the relaxation, never to raise caps or
bypass the cooldown.

Validation: 124 focused offline unittest checks passed (transport, Local source,
Fresh recovery, Detail/cache, and Official recovery), plus Python compilation
and `git diff --check`. Added checks cover high-priority precedence, saved-waiter
and aging order, next-round catch-up after Fresh, rediscovery persistence, the
one-opportunity/72-hour boundary, initial-phase saved queue inclusion, retained
verification dates, both-phase history, and rolling-hour/day ceilings. The
scheduled follow-up reviews run at 21:30 Pacific on Oct 5 and Oct 6 and then stop.

## Separate recovery bottleneck

Seven of nine weekend recovery reports recorded generic search-provider failures
(eight failure events); Friday noon disabled both DuckDuckGo and Bing. Many
`dedicated_matches` are matches to an Official card without a usable JD, so they
must not be reported as recovered JDs. The observed generic job counts were
below the 100-job ceiling; increasing LinkedIn Detail does not repair provider
availability, failed exact postings, cached no-match evidence, or unavailable
triage. Keep these outcomes separate from LinkedIn capacity in the next review.

# Historical investigation — 2026-10-02

This workstream changes transport and discovery scheduling limits. Software
Engineer, AI Engineer, and alternating Backend Engineer / Full-Stack Engineer
remain the search families. Machine Learning Engineer stays removed. Title
filtering, LLM fit triage, Detail eligibility, scoring, and Online ↔ Local
recovery decisions are unchanged.

## Request ceilings

| Scope | At investigation start (before A) | Merged A + B |
| --- | ---: | ---: |
| Search per discovery round | 10 (5 + 3 + 2) | 10, often fewer after ledger stops |
| Initial + follow-up Detail per round | 8 + 8 | 8 combined |
| LinkedIn requests per round | 26 | 18 |
| Three scheduled rounds | 78 | 54 maximum |
| Catch-up/manual rounds | No shared daily/hourly ceiling | 18 per rolling hour, 54 per rolling 24 hours |
| Detail across extra rounds | Separate per-call limits | 8 per rolling hour, 24 per rolling 24 hours |

Workstream A (`94592b2`) landed during this investigation and independently
made Detail last-resort with one eight-request round allowance. This transport
change preserves that admission logic and shares its network allowance; it adds
persistent hourly/daily limits, circuit breaking, pacing, and ledger yield. The
combined scheduled theoretical ceiling falls 31% from the investigation-start
baseline; that reduction must not be attributed to B alone. It is not a measured reduction in
429s or actual traffic. A recovery-only invocation has no discovery and at most
eight Detail requests. Zero-budget/cooldown rounds still run non-LinkedIn
recovery and can publish usable saved snapshots. Search and Detail share the
same attempt allowance; connection failures consume it too. Automatic retries
and redirects are disabled. There is no proxy, identity/session rotation, or
challenge bypass.

## Observed requests

Evidence: committed `output/sources/health.json` Search counters and snapshot
Detail counters, combined with the installed automation checkout's existing
`output/logs/local-sources.out.log` recovery reports. Distinct collection attempt
timestamps are counted once; repeated snapshot timestamps are not new discovery
runs. These are requests recorded for the sampled published Local rounds, not
an account/IP-wide network trace. Search counters include the failed 429
request; successful-page counters alone would undercount it. Historical rounds
below used older configurations, including a 14-page Search cap and five query
families; the new three-family 10-page configuration has not yet accumulated a
comparable production sample.

| Pacific day | Recorded Local rounds | Search | Initial Detail | Follow-up Detail | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Sep 26 | 4 | 56 | 32 | 22 | 110 |
| Sep 27 | 3 | 42 | 14 | 16 | 72 |
| Sep 28 | 3 | 40 | 8 | 3 | 51 |
| Sep 29 | 2 | 28 | 9 | 11 | 48 |
| Sep 30 | 2 | 18 | 0 | 0 | 18 |
| Oct 1 | 4 | 1 | 8 | 17 | 26 |

Individual observed rounds ranged from zero traffic during deferral to 30
requests (14 Search + 8 initial Detail + 8 follow-up Detail). On Oct 1, three
Search-cooldown retries at 14:21, 14:33, and 14:44 Pacific issued 1 + 8 + 8
recovery Detail requests. The new persistent hourly Detail cap prevents that
burst even across collector restarts. The local request journal and endpoint cooldown/cursor state survive a discarded
worktree or unsuccessful publication; published Health carries the same traffic
state forward. The existing runner lock and single-local-runner ownership
remain necessary for serialized updates.

## Middle discovery: retain for now

To estimate rediscovery, compare the source `first_seen_ledger` with its parent
commit and count newly added deterministic LinkedIn IDs, including cards later
rejected by the existing filters. Compare that delta with the snapshot's raw
unique collected cards, not retained inventory or `first_seen` timestamp
coincidence. This measures ledger novelty, not how many relevant jobs pass
Workstream A's policy. Page ordering and query families changed over this sample.

| Middle Local run (Pacific) | Earlier discovery that day | Unique collected cards | New ledger IDs | Rediscovery |
| --- | --- | ---: | ---: | ---: |
| Sep 27, 15:00 | 13:50 | 107 | 2 | 98.1% |
| Sep 28, 15:00 | 12:00 | 111 | 29 | 73.9% |
| Sep 29, 15:23 | None recorded | 119 | 92 | 22.7% |

A recovery-only middle round would save up to ten searches (three scheduled
rounds would then have a 44-request ceiling), but the Sep 28 sample still added
29 ledger IDs, 24 of which were retained as new jobs. Moving discovery to 21:00
would delay discovery by up to six hours and may miss cards displaced from the
bounded ranked result pages. A missed noon round makes unconditional middle
recovery especially costly. The evidence supports first removing redundant
Detail allowances and low-novelty pages. Noon/15:00/21:00 discovery remains;
new per-page novelty receipts make a later scheduling decision measurable.

## Early stops and coverage tradeoffs

Search compares parsed deterministic identities with the existing source ledger
and prior snapshot, before selection. Two consecutive non-empty pages yielding
at most one genuinely new identity stop that query, subject to its existing
minimum-page floor. Empty and low-current-uniqueness stops remain. A high-novelty
page resets the consecutive-page counter. Cross-query repeats do not count as
new a second time. Returned cards continue through the existing pipeline,
including known cards that may still need cached/official recovery. Partial
snapshots merge with last-good rows without refreshing carried verification
or first-seen timestamps.

This is a bounded heuristic: LinkedIn's ranked pages are not guaranteed to be
chronological, so new IDs can exist beyond two low-yield pages. Actual request
savings depend on that page distribution; historical aggregate snapshots cannot
replay individual pages. The shared eight-Detail cap can delay JD recovery
relative to the old sixteen-call combined allowance. Deferred cards and the
existing official-web/Online ↔ Local recovery paths remain available, subject to
their existing Fresh eligibility and budgets.

## Dynamic `f_TPR`: not enabled

LinkedIn's [official filter documentation](https://www.linkedin.com/help/linkedin/answer/a507441/filter-and-sort-job-search-results?lang=en)
documents the past-24-hours, week, and month choices. It does not establish an
arbitrary-seconds contract for the unauthenticated guest endpoint. Keep
`f_TPR=r86400`; no extra guest probes were made during this investigation.

A future narrower-window experiment needs bounded paired requests using the
same query/page/filter settings, checks that older cards are actually excluded,
comparison of new ledger IDs with the 24-hour baseline across multiple rounds,
and fallback after failures/sleep. Use the last completed successful discovery,
not a carried snapshot's timestamp or cooldown receipt; partial/probe runs do
not establish a complete discovery baseline. Alternating third-query coverage
also needs a per-query successful-discovery timestamp. Time since last success
plus a safety margin is only a candidate window until those checks establish
behavior; one apparently valid response does not prove completeness.

## Circuit breaker and validation

The minimum start-to-start interval is randomized between 2.5 and 3.25 seconds;
slow responses or intervening recovery work can extend that gap.

Any 429 closes Search and Detail for the remainder of that round and persists
an all-LinkedIn pause of at least an hour or the longer `Retry-After`. Search's
two-429/24-hour/single-page policy and Detail's first-429/12-hour/single-probe
policy remain separate. A longer server retry deadline extends the endpoint
cooldown. A successful Detail probe permits no more Detail calls that round.
Non-LinkedIn recovery continues without aggressive retries.

The latest 20 429 records include the raw retry header, parsed retry deadline,
endpoint URL, query (Detail title), zero-based Search page or null for Detail,
combined and endpoint request ordinals, round counts, and per-endpoint rolling
60-second/hour/day counts. Request attempts persist before transport; 429 state
persists before returning the response.

Offline checks cover shared Search + both Detail phases, hourly/daily caps,
failed-publication journal recovery, numeric and HTTP-date Retry-After,
independent endpoint state, the shared single probe, network-error accounting,
modest jitter, redirect suppression, and ledger early stops. Existing focused
checks cover last-good merging, first_seen, cooldowns, and shared official
recovery. No crawler, LLM scoring, or production guest experiment was needed.

Validation: 129 focused unittest checks passed, plus Python compilation,
`bash -n scripts/local_source_sync.sh`, and `git diff --check`. Production traffic
reduction remains to be measured in normal scheduled rounds; no extra Local
crawler or workflow run was launched for validation.
