# Batch 2 — Priority correctness and delivery continuity

Implemented from the consolidated October 17 investigation, starting at `634c7b5` on latest `origin/main`. This includes Batch 1 `8f38ee8`. The development checkout was behind and left untouched; implementation and offline checks used a disposable worktree.

## Implemented and repaired

- Gap counts are populated on fresh scoring and retained through Syncareer export, historical tiering, cache/peer reuse, sorting, and store compaction. A stored total greater than the two retained gap examples is preserved. New scoring replaces the old total.
- Negative hard-constraint status is checked before Tier A. Tier C and negative-status actions return `skip` before referral promotion. Syncareer historical actions use its existing target-company referral field.
- Each pipeline persists an immutable pending Issue receipt in its own `notification_outbox.json` before its digest/seen state is consumed. Workflows publish the receipt with the data, retry pending receipts even with zero new jobs, and persist acknowledgements separately. Direct paginated Issue lookup includes closed Issues and the exact receipt marker, so an Issue created before a lost acknowledgement is reused. A failed attempt retains the original body; a later run does not overwrite it. Source-ingest Board runs still send no Issues.
- Pages now follows completion of all three discovery workflows, including failed notification steps. The old explicit Board dispatch was removed to avoid two publication runs for the same completion.
- Source changes trigger offline Python and Node checks, with no production credentials, crawlers, or paid evaluation.

The historical preview was generated **before** the derived repairs. Its pinned input hashes, complete per-record proposed changes, identity candidates, and conflicts are in [BATCH2_MIGRATION_PREVIEW.json](BATCH2_MIGRATION_PREVIEW.json). Only `main_gaps_count`, `tier`, and `recommended_action` were then repaired: **458 / 3,126 retained records** (21 Board, 434 Syncareer, 3 Official). Of these, 367 Syncareer gap totals were corrected. Changes overlap and should not be summed as distinct opportunities.

Tier changes were four Syncareer A→B, three Syncareer A→C, and one Board B→C. The three negative-status A records already said `skip`; this repair removes the inconsistent A tier, without claiming an independently verified eligibility determination. Three Official C actions changed from `referral_now` to `skip`. Other action repairs align saved C records with `skip`.

Structural before/after comparison confirmed identical record counts and metadata and preserved **every field outside those three derived fields**, including fit scores/model evidence, canonical/storage keys, URLs, first_seen, posting dates, source clocks, descriptions/provenance, review statuses, and application fields. Digest, seen, alert-history, and review files were not migrated. Re-running the derived preview after repair reports zero remaining changes. No rescoring or new alert receipts were generated for this repair.

## Identity migration: preview only

The saved cohort contains **613 proposed normalized-key changes**: 604 Syncareer and 9 Board. There are **199 candidate alias groups**, including **3 groups with conflicting identity evidence**, and **35 affected digest keys**. Candidate groups overlap and are not a count of proven duplicate opportunities. Twelve distinct Syncareer IDs share Kforce's general search page: treating every equal URL as one opportunity would lose legitimate records. The other conflicts involve two NVIDIA URL variants for one source ID and two Apple title slugs for one ID; neither has been merged here.

No affected keys were found in the local review-state snapshot. **This does not establish that live Supabase application history or pending browser edits are absent.** Those stores were not exported or mutated. Normalized Syncareer keys and exact store/digest/review alias reconciliation remain unapplied until that history can be preserved together. The existing historical annotation identity behavior is intentionally unchanged in this delivery.

Safe next steps:

1. Export live statuses, status events, and known legacy/browser keys; pin hashes and take a recoverable backup.
2. Build an additive alias map from verified requisitions and job-detail URLs. Exclude general search URLs and conflicting groups. Never use company/title alone.
3. Add dual-key reads and preserve legacy aliases across dashboard, Supabase, offline pending edits, digest/seen ledgers, score-cache references, and alert history before changing primary keys.
4. Dry-run URL-added/URL-lost, earliest first_seen, status/event retention, and distinct requisitions against the actual export. Review all conflicting groups. Publish any key migration separately with rollback evidence.

The reusable command below prints a fresh **read-only** preview from the current saved stores; the committed preview records the pre-repair snapshot:

```bash
python3 scripts/preview_batch2_migration.py
```

## Batch 1 verification and validation

Before Batch 2 edits, the entire recorded Batch 1 focused group still passed: **216 passed, 1 skipped**. Its saved CoStar/NVIDIA/WEX admission, five legacy tentative rows, Meta complete-field assembly, Two Sigma detail/cache reuse, and identity/provenance boundary regressions remained intact. See [Batch 1 validation](BATCH1_VALIDATION.md) for exact saved-record IDs and evidence limits. Between `8f38ee8` and this task's `634c7b5` baseline, Git contains only a pending-company-profile update and no new pipeline-output publication. Consequently there was no saved post-fix scheduled-run cohort available here to establish realized discovery gains.

Final focused validation: **245 passed, 1 skipped** (the opt-in live matching regression), plus both Node dashboard checks. The source CI workflow contains the exact command. New tests exercise fresh score/export/compaction/reuse, full fresh matching with stale counts, terminal constraint/referral guards, immutable receipt retry, creation-before-ack recovery, partial delivery, corrupt-state retention, read-only migration preview, URL-added/lost candidates, preserved statuses/dates, and distinct-requisition conflicts. All five changed/new workflow YAML files parsed and all shell blocks passed `bash -n`.

No full suite, live employer crawl, paid API call, live Issue creation, Supabase write, identity migration, or deployment validation ran. Notification retry behavior is verified with mocked GitHub responses; hosted execution remains to be observed during normal runs. The completion trigger cannot recover Issues already lost before durable receipts existed. The preview does not authorize merging ambiguous identities.
