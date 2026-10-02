# LinkedIn traffic investigation — 2026-10-02

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
