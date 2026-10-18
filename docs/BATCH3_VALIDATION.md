# Batch 3: protected recovery, employer identity, and selective-review pilot

Implemented against `48ca805` on October 17, 2026 (Pacific). Production discovery limits, technical scoring policy, and primary job keys are unchanged. No saved job, application, digest, review, or seen ledger was migrated.

## Protected LinkedIn Detail opportunity

Already-admitted (`needs_jd=true`), never-attempted thin cards deferred by cooldown or a 429 now receive the same one-opportunity protection as budget deferrals: eligibility ends 72 hours after the original `first_seen`. Legacy cooldown/rate-limit annotations are recognized; new deferrals retain a timestamp. An attempted card, rejected/unavailable triage, future discovery date, or expired card cannot gain this extension. Generic outbound recovery remains Fresh-only.

Cooldown performs no HTTP or triage calls. The shared round/hour/day budgets, Retry-After, global pause, request spacing, and one-probe cap retain authority. Mid-round 429 protects the remaining admitted cards without giving the attempted card another protected opportunity. Higher-value cards retain their existing queue precedence.

Detail receipts now include `protected_requests` and `protected_jds_resolved` for attempted cards past Fresh, plus `protected_deferred` for admitted, never-attempted cards deferred in this phase (including Fresh cards). The existing per-card queue retains IDs, discovery dates, attempt flags, resolution status, and reasons. To measure downstream value, join those exact source IDs to the next normal Board output and separately adjudicate suitability; A/B counts alone do not prove suitability.

Saved snapshot replay at **2026-10-18 04:30 UTC / October 17, 9:30 PM Pacific** found **zero newly eligible thin cards**. The cooldown cohort was either still Fresh or already expired beyond 72 hours. This is a fix for fair handling of subsequent deferrals, not a measured immediate recall gain. The two-round mocked scenario recovers one verified JD after cooldown while enforcing the single-probe cap and preserving discovery dates. No live LinkedIn recovery ran.

## Missing employers and small profile enrichment

Board snapshot ingestion now names anonymous source-ID cards only when their HTTPS Ashby job URL contains an exact, curated employer tenant and UUID. It rejects unknown/ambiguous tenants, board roots, spoofed hosts, missing source IDs, and conflicting known tenants. Existing employer names remain authoritative. The method and query-free board URL survive store construction and compaction as `company_identity_method` and `company_identity_url`. Tenant identity does not verify the posting/JD, upgrade the application link to an official URL, or establish role eligibility.

Two profiles were added, with neutral priority, technology type, and **unknown size, maturity, and sponsorship**:

- Dialogue AI: [employer website](https://www.dialogueai.com/) and [named Ashby posting](https://jobs.ashbyhq.com/dialogueai/48219357-056f-4089-981a-0c773b196130).
- Autoscience: [employer website](https://www.autoscience.ai/) and [named Ashby posting](https://jobs.ashbyhq.com/autoscience/b6a5a7bf-9895-4fc5-9fa1-b049d595a344). The existing pending brand “Autoscience Institute” is retained as an alias.

The saved Board replay recovers **2 / 41 anonymous A/B records**: Indeed `in-216e827c48493b4a` (Dialogue AI, A) and `in-8bbb13ae6d5c30fb` (Autoscience, B). Assertions preserve their keys, canonical keys, URLs, first_seen, technical scores, tiers, recommended actions, and sponsorship. These names will appear when normal ingestion next processes the cards; the saved production outputs were not rewritten here. The remaining 39 stay anonymous rather than receiving guessed employers.

## Frozen selective-review development pilot

[Packet](BATCH3_PILOT.json): **40 source-identity-distinct cases**, **20 development / 20 held out**, with input SHA-256 hashes, frozen candidate/resume context, descriptions, baseline decisions, and empty human labels. It reuses **21 unique historical regression fixtures** after collapsing overlap across the 10- and 15-case sets, plus **19 saved pipeline records**. Historical fixtures include edited summaries and older model baselines; they are labelled as such, not represented as full current JDs. Some baselines have no comparable tier.

Sampling stresses early-career/Engineer II roles, unrelated and senior controls, staffing/internship priorities, thin JDs, anonymous employers, sponsorship conflicts, and boundaries. The `confirmed_recall` stratum samples previously affected employers; its four Meta source records include ignored/senior controls, not four proven suitable opportunities or four reproduced Batch 1 failures. This small, purposive packet cannot estimate global recall or population accuracy.

Canonical packet SHA-256: `858370c65f77991cf7ce9f873bb9bc4ea0c3b3d1a538c7242be395fdf2d430b1`.

[Development receipt](BATCH3_DEV_REVIEW.json): **two real OpenAI requests**, `gpt-6-luna`, medium reasoning, reviewing only the 20 development cases. The request returns separate technical-tier and eligibility proposals with exact JD/resume excerpts. It receives no baseline decisions. **13 / 20 responses passed identity, enum, and exact-quote validation; seven were rejected.** Exact quotation establishes textual provenance, not semantic correctness. Rejected results were not retried. All 20 held-out cases remain unsubmitted.

Usage: **15,571 input + 6,793 output = 22,364 total tokens**. Output includes **2,433 reasoning tokens**; do not add those twice. No current dollar-price or accuracy claim is made. The runner follows the existing Chat Completions contract; see [official API reference](https://developers.openai.com/api/reference/resources/chat). Receipts are reused without credentials or new requests on repeated commands; another packet hash is rejected. API failure is not silently converted into a successful review.

**Zero human adjudications are available.** Corrected/harmed-tier counts, actionable precision, suitable C rescues, and review-time benefit are therefore unmeasured. Production selective review stays disabled and has no call path from normal pipelines. Proposals never write scores, tiers, actions, application state, or eligibility. The report does not recommend enabling it from 13 validated outputs.

Next, independently label technical tier and eligibility for the development cases, inspect the seven rejected cases, and assess corrected versus harmed decisions and blocked high-priority proposals. Refine only on development data. Freeze the policy before a separately authorized held-out run. Compare precision@10 and suitable C rescues only on cases with comparable evidence/baselines, record human review time, and require held-out net benefit with no constraint escapes before any production integration. Historical application status alone is not a ground-truth label.

Offline inspection (no requests):

```bash
python3 scripts/selective_review_pilot.py --packet docs/BATCH3_PILOT.json
python3 scripts/selective_review_pilot.py --packet docs/BATCH3_PILOT.json \
  --review-development docs/BATCH3_DEV_REVIEW.json
```

For adjudication, add `--labels /path/to/human-labels.json` to the second command. Labels are a JSON object keyed by packet case ID, each with separate `tier` (`A`, `B`, `C`) and `eligibility` (`supported`, `blocked`, `unknown`). Keep labels separate from the hashed packet. An empty label set returns no quality metrics, not zero errors. `--build --packet /new/path.json` makes a new packet from current saved inputs and refuses to overwrite an existing one; any review of that new packet requires a new receipt and would make paid calls.

## Validation and limits

The expanded source-change CI group passed **275 Python tests, 1 skipped** (opt-in live matching regression), plus both Node dashboard checks. It covers Batch 1/2 regressions, shared traffic budgets and queue ordering, cooldown/429 persistence, 72-hour/attempt/admission boundaries, employer-name provenance through ingestion/persistence, unchanged job keys/scores/dates, frozen splits, general-search URL exclusion, fabricated-quote rejection, human-label gating, held-out isolation, and receipt reuse. A separate focused recovery/local-source group passed **168 tests, 6 skipped** (optional integrations).

No full suite, crawler, hosted workflow validation, Supabase write, identity migration, historical rescoring, or live notification ran. Normal scheduled behavior and actual downstream recommendation gains remain unobserved. Batch 2's application-history safeguards still hold its identity migration; this delivery does not bypass them.
