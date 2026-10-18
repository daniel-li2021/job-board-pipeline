# Remaining improvements — October 18, 2026

Started from clean, fast-forwarded `origin/main` `44ff25e`. Reviewed the original `/tmp/job-board-audit/investigation-report.md`, Batch 1–3 reports and the pinned migration preview. Safe changes are implemented; production selective AI review, live identity migration and database permission changes remain disabled/unapplied.

## Identity compatibility and backups

The original **613 proposals** are still 604 Syncareer and nine Board key changes. Rather than replacing them, the shared compatibility module recognizes exact source IDs and a deliberately narrow set of employer posting IDs. It excludes general search URLs, tentative URL bridges, mismatched key/requisition pairs and conflicting components. Company/title alone never forms an identity.

The three conflicting preview groups were investigated:

- NVIDIA `in-567257fd06181979`: Workday locale variants retain the same tenant/site/requisition `JR2026802`; additive aliases are safe.
- Apple `200688902-2459`: two title slugs identify Apple posting `200688902`; additive aliases are safe.
- Kforce: 12 different Syncareer IDs share a general search page. They remain distinct; the URL is not an identity.

Dashboard primary keys and saved pipeline records remain unchanged. Alias reads find Applied/In Progress/Deleted status under an existing compatible key; duplicate display rows/counts collapse only for proven aliases. Explicit status changes update the resolved existing key, not every alias. Loading aliases inserts no synthetic statuses. Existing archive backfill behavior remains intact; it is not an identity migration. The durable discovery ledger preserves `first_seen` across recognized URL changes even after retained rows expire. Unknown discovery dates remain unknown. Digest checks recognize prior source-ID/detail-URL identities, suppress duplicate aliases within a digest and retain legitimate B→A promotions. Unsupported identities stay separate.

A private, gitignored backup is at `output/logs/remaining-backup-2026-10-18/`. It contains all three stores, discovery/digest/alert ledgers, local review state, the public REST table export and a hash manifest. The **4,681-row** export SHA-256 is `85193e73661e7b69deb6f50678485a5b9a44e8cb43f296bf2850f54348b6bced`. This includes **2,682 archive metadata rows**, with **1,867 populated archived application dates**; it is not 4,681 applications. Raw application history is not committed.

The [dry-run receipt](IDENTITY_COMPATIBILITY_DRY_RUN.json) covers all **3,126 stored records**, all 613 proposals and every exported status/archive row. The actual dashboard JavaScript readers run in an isolated VM against the export. Original expanded status hashes match the no-alias baseline, current alias statuses agree, and a simulated explicit deletion touches one existing key. No network or database writes occur. All original records, application metadata/dates, alert/digest/seen ledgers and source dates remain retained. No original row/event is deleted or rekeyed. The receipt covers **135 / 613** proposals through **761 groups / 1669 alias keys** and defers **478** proposals. It finds 21 directly saved remote alias keys, no conflicting saved alias statuses and zero local review-overlay keys.

```bash
python3 scripts/identity_compatibility_dry_run.py \
  --backup output/logs/remaining-backup-2026-10-18
```

This is a complete rehearsal of **additive compatibility**, not approval for a destructive merge. The REST export is paginated and not a transactional database backup. Browser-only pending edits are not inspected; historical status events absent from the existing table cannot be reconstructed. Before any live rekey/merge, obtain a consistent database backup, export pending browser edits, reconcile conflicts, and seek owner approval. Rollback of this release removes the additive compatibility layer; no database restoration is necessary because this release does not migrate the database.

## Dashboard performance and client protections

Measured deployed HTML: **9,706,611 decoded bytes**, downloaded in **0.428 seconds** in one bounded local HTTP sample. Five sequential status-export requests took **0.441, 0.349, 0.380, 0.195 and 0.167 seconds**. These are local transport samples, not a page-load SLA. JSON whitespace reduction saved under 1% of gzip bytes and did not improve a seven-parse local median (27.34 ms versus 33.06 ms), so that change was discarded. No payload/history architecture rewrite was made.

Repeated application-history badge rendering was measurable: the final offline runtime receipt took **72.043 ms for 100 rows**, versus **1.17 ms including index construction** for identical badge text. Archive indexing now lasts only through a synchronous render and is cleared in `finally`, avoiding stale cross-render state. These are bounded Node CPU measurements, not claimed browser load-time gains.

A real browser showed Last 7 Days rendering jobs before shared status finished loading, while the main views correctly waited. Both Last 7 Days render paths now obey the same loading guard. Existing tabs, search, filters, exports, application tracking and layout are retained. Job links are constrained to HTTP(S), including archive-recovered links, preventing `javascript:`/`data:` URLs from executing as dashboard-origin code. This client protection does not secure the database's write boundary.

## Application-state security: deferred

The deployed bundle initializes Supabase with its public key and no sign-in. Anonymous REST reads succeed. The checked-in legacy setup explicitly grants anonymous insert/update with unconditional policies and removes prior allowlist objects. **A deployment using those policies allows unauthorized visitors to change statuses, soft-delete jobs and write archive metadata directly through REST; hiding buttons or the public key cannot prevent that.** The current database policies cannot be introspected with the available public credentials; no admin credential was configured and no live mutation probe was performed. Therefore this review cannot claim to have verified the exact currently installed RLS policy definitions.

[The hardening SQL proposal](../supabase/job_review_hardening.sql) keeps public reads and limits writes to authenticated, allowlisted editors, including restrictive guards against other permissive authenticated policies. It revokes both table and column write grants, preserves all records and refuses to proceed without an enrolled editor. The legacy setup is clearly marked unsafe to rerun. Neither script was executed. SQL was inspected, not run against a database.

**Browser-check exception:** opening the unmodified production page triggered its pre-existing automatic archive backfill at **7:24:23 AM Pacific**. A read-only comparison against the backup confirmed one existing archive row changed only `updated_at`; its key, status, Deleted flag, embedded metadata and application date were identical. Before/after records remain in the private backup folder. No unapproved rollback was attempted. The production tab was closed and all later interaction checks used a local simulated backend. An exact remote archive-key/status guard now avoids redundant backfill upserts and preserves the remote timestamp; changed metadata still saves normally. Its Node regression verifies zero writes for identical archives and one for changed metadata.

**Owner decision — October 18, 2026:** defer access-control and permission changes while use is limited to Daniel and trusted people. Before any future public release, untrusted visitors should see only a template with demo data; all real job listings, application history and personal data should remain private, including in downloadable data and unauthenticated endpoints. The existing SQL proposal preserves public reads, so it would need revisiting for that future privacy requirement. No access settings were changed.

## Scheduled-run verification and evidence limits

Normal scheduled runs completed during finalization; none was triggered for this task. The new Official run started **October 18 7:30 AM Pacific** on `44ff25e`, which contains Batch 1–3, and recorded matching at **7:47 AM**. Syncareer recorded its run at **7:53 AM**. Their data/acknowledgement commits and subsequent pending-profile update were preserved when integrating the task. [The saved operational receipt](POSTFIX_SCHEDULED_EVIDENCE.json) pins source revisions, input hashes, denominators and notification IDs.

| Real scheduled observation | Previous Official run | First observed post-fix Official run |
|---|---:|---:|
| Added detail successes / requests | 2 / 150 | 143 / 150 |
| Meta detail successes / requests | 0 / 111 | 141 / 141 |
| Relevant usable JDs / eligible records | 5,141 / 5,258 | 5,480 / 5,482 |
| Meta relevant usable JDs / eligible records | 129 / 214 | 214 / 214 |
| Two Sigma relevant usable JDs / eligible records | 0 / 30 | 36 / 36 |

These are **different cohorts**, not a controlled accuracy or suitability experiment. The ≥200-character JD rule does not establish complete requirements. A stricter join of the two compact Official recovery caches finds **18 thin→usable descriptions among 420 shared Meta source IDs**. Two Sigma's native adapter now supplies the 36 usable descriptions; its older generic-recovery cache is not the evidence for that gain. No independent suitable-recommendation gain is asserted from these counts.

Official's persisted outbox records delivered receipt `07e3e0b9a49bbf9f95f994b49735af6848f08e3605c16e40b49b38debcb5e18f`, and [Issue 198](https://github.com/daniel-li2021/job-board-pipeline/issues/198) contains the exact receipt marker. Syncareer's delivered receipt `664e7498fd9cdf8d2a7f09dcc066e91d7f42cee5cd2c520acdd49fd68b68b697` is likewise verified in [Issue 199](https://github.com/daniel-li2021/job-board-pipeline/issues/199). This establishes ordinary scheduled outbox delivery/acknowledgement, while failure/retry remains offline regression evidence. The task itself sent no Issue or digest.

The supplemental private backup `output/logs/remaining-backup-2026-10-18-final/` pins the newer stores and ledgers and reuses the valid 4,681-row application export from the post-Official backup (SHA-256 `6d81d0b8506fb4f3d0c9f54154626963e809b0f11478b40487fba682fe4e220e`, including the disclosed timestamp refresh). [The supplemental runtime rehearsal](IDENTITY_POSTSCHEDULED_DRY_RUN.json) repeats the actual-reader/status/archive checks against these **3,043 records / 602 proposed key changes**; 132 proposals have supported aliases, while 470 remain deferred. It preserves all expanded statuses and archive rows and adds zero automatic writes. The original backup/report remain unchanged, so natural pruning/discovery is not confused with a task migration.

- Both the original **3,126-record** snapshot and the newer **3,043-record** snapshot show **zero further derived repairs** for gap totals, tier and action. This checks deterministic consistency, not suitability.
- Official's normal run observed 74 discoveries and one new A/B addition; Syncareer observed 35 discoveries and four new A/B additions. Its 23 shown A/B rows are a different denominator. These are saved pipeline telemetry, not independently adjudicated successful opportunities.
- Board's newest observed run remains October 17 9:01 PM Pacific. The local LinkedIn receipt at 9:00 PM predates Batch 3, with a search 429 and zero Detail requests. Protected Detail successes and limited employer recovery therefore remain unobserved operationally. Glassdoor stays cached; no bypass was attempted.
- SAP is still empty and HubSpot returns 404 in that scheduled run, which predates this task's SAP adapter change. SAP's 25-card/two-JD check is bounded development-machine evidence; hosted gains await its next normal run. The Stryker probe returned 200 / total 184 and did not justify changing its healthy latest adapter.
- The initially observed deployed page was rebuilt October 17 11:56 PM Pacific. Later scheduled publication followed the new discovery runs. A current compiled page and current source snapshot are separate clocks; committed `public/dashboard.json` is not treated as current operational evidence.

No full crawl, bulk rescoring, live identity migration, production permission change or production AI scoring-policy change was performed by the task. The one incidental existing archive timestamp refresh is disclosed above. Further protected-recovery/suitability/retry denominators require future normal runs; no extra crawl is manufactured for them.

## Validation and independent review

The reviewer assessed both AI partitions independently, then reviewed compatibility/evaluation/security changes. Review reproduced stale-key cross-requisition aliasing, lost durable discovery dates, metric denominator errors and a weak initial dry-run assertion. Those findings were fixed with focused regressions, actual runtime projection checks and a separate audited metrics summarizer. Freeze import/configuration limits are documented in [the AI evaluation](SELECTIVE_REVIEW_EVALUATION.md).

Final focused validation: **290 Python tests passed, 1 skipped** (opt-in live matching regression), plus both Node dashboard checks and parsed changed workflow YAML. The offline CI group includes the new identity, evaluation and SAP tests. A later focused Node check also verifies archive backfill idempotence.

Local real-browser acceptance loaded the frozen production payload plus the exported statuses through a simulated backend: shared loading completed, Applied/In Progress remained available, search filtered application history and Escape restored it. No live status action was clicked. Real-browser checks exposed the existing redundant archive backfill, which was fixed as described above. No full suite or live permission mutation test is part of this release.
