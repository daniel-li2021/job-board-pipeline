# Remaining work — October 18, 2026

- [x] Selective review: diagnose seven rejects; independently assess development evidence; freeze policy; evaluate untouched held-out cases and costs. Keep production disabled and AI assessments distinct from human labels.
- [x] Identity: classify 613 key changes and three conflicts; add safe compatibility; back up available state and run a complete read-only migration rehearsal. No live history writes.
- [x] Careers: bounded SAP/HubSpot public-interface probes; inspect saved failure receipts; fix reproducible adapter defects and measure discovery/JD results.
- [x] Dashboard/security: measure loading, inspect actual access boundary, preserve layout/access, implement safe client safeguards; prepare permission changes for approval only.
- [x] Post-fix verification: reuse scheduled receipts for JD/ranking/delivery/coverage/freshness; separate observed runs from replay evidence.
- [x] Independently review and validate focused batches; update documentation and prepare safe main publication with Git cleanup.

No full crawls, bulk rescoring, production scoring changes, live history migration, or production permission changes are authorized by this checklist.

Results: [implementation/security/verification](REMAINING_VALIDATION.md), [selective review](SELECTIVE_REVIEW_EVALUATION.md), [SAP/HubSpot](SAP_ADAPTER_VALIDATION.md), [identity rehearsal](IDENTITY_COMPATIBILITY_DRY_RUN.json).

Remaining boundaries: HubSpot upstream 404; human/eligibility evidence for AI value; future protected-recovery/suitability/failure-retry measurements; owner-approved coordinated Auth/RLS rollout; no mass rekey recommended for unsupported proposals. One pre-existing production page-load backfill refreshed an archive timestamp during verification; all other fields were preserved and redundant refreshes are now guarded.
