# Indeed employer identity and JD evidence quality

Investigated October 18, 2026 (Pacific), from `origin/main` **7c41338**. This change preserves technical fit scores, cache fields, job/source/canonical IDs, discovery dates, application/review state, and historical records. Production snapshots were not rewritten or rescored.

## Root cause

The saved Indeed snapshot at **2026-10-18 15:20:47 UTC / 8:20 AM Pacific** has **492/492 usable-length JDs**, including **27 blank employer names**. The saved Board at **22:03:24 UTC / 3:03 PM Pacific** contains **135 anonymous Indeed records, 41 at Tier A/B**.

JobSpy **1.1.82** reads `company_name` directly from `job.employer.name`; the repository's bounded transport explicitly maps that model field into `company`, then normalizes null/NaN to an empty string. See the [pinned upstream parser](https://github.com/speedyapply/JobSpy/blob/v1.1.82/jobspy/indeed/__init__.py) and local `sources/jobspy_local.py`.

A single successful, 100-result Indeed GraphQL page using the production search settings (`software engineer`, US, distance 50, 48 hours) produced **17 unnamed employers**: **15 employer objects with null `name`, two null employer objects**. All **100/100 parsed names matched the response field**, with **zero parser mismatches**. Several anonymous IDs overlap the saved snapshot, including `in-88723c5124d02f8e`, `in-4738557a44d3fbcf`, `in-3f513e92e0417313`, `in-5ddf2c924620f208`, and `in-87128eb945c60319`.

This establishes loss in Indeed's employer field for the sampled records; it does not establish why Indeed omitted it, or prove every historical blank has the same cause. Source attribution, company-profile prose, and JD mentions are not substitutes for a verified employer field. The first diagnostic request omitted the radius and returned HTTP 400; the corrected request returned HTTP 200. Total diagnostic traffic: **two requests, one result page, no pagination or retries**. [Sanitized live receipt](INDEED_LIVE_PROBE.json) retains only field presence/names/IDs and the parser source hash, without headers or application tokens.

## Targeted behavior

- A later query's nonblank source name can fill an earlier blank for the **same source/job ID** without replacing its JD, dates, URLs, or discovery-query history. The adapter accepts both JobSpy dataframe `company` and direct-model `company_name` fields.
- Board refreshes retain a known name when the same source/job ID temporarily loses it. An existing nonblank name wins, including a recruiter's name; client-company mentions never replace it.
- Existing exact curated HTTPS Ashby tenant + UUID attribution now also reaches retained history. It adds only the name and identity provenance, without changing IDs or promoting application URLs to official URLs. No new tenant mapping or JD-derived automatic naming was added.
- Anonymous jobs retain technical scores and A/B discovery eligibility. Their action is **`verify_details`**, ahead of referral/application urgency. The dashboard shows **Unknown employer** and **Verify details: Employer unverified** beside the title.
- JDs explicitly describing themselves as suggested/proposed receive **Suggested/proposed JD; verify original**. Such records cap at **B**, retain their fit score, and require verification. Known employer names do not remove this warning. Generic writing alone, employer mentions, and recruitment-fraud warnings do not prove fraud or trigger this JD flag.
- A title-only **2027 Graduate** role receives **Graduation eligibility unverified**, caps at **B**, and requires verification. Atlassian's `4472265615` remains retained with score **88** rather than being treated as a confirmed restriction or urgent Tier A match. A full JD allowing 2026/2027 alternatives follows the existing constraint policy. Explicit full-JD restrictions retain the existing hard-filter behavior.
- Warnings survive compact-store persistence, are derived again for dashboard rows, and clear when stronger current evidence resolves them. This policy is limited to Board aggregator sources (Indeed, LinkedIn, Glassdoor). This is a deterministic policy layer; no prompt, model, cache version, ranking weights, or score was changed.

## Employer evidence reviewed

The 27 current anonymous JDs contain a mixture of explicit brand claims, recruiting/intermediary language, short application redirects, and generic text. These examples explain why automatic extraction would overstate identity:

| Saved source evidence | Decision |
|---|---|
| Techi247 LLC / AeroCharge / A Labs Technology LLC described as seeking a developer | JD claim only; leave employer unverified without independent identity evidence. |
| Alleviate Health and Watney named in JDs, with matching-looking Ashby tenants | Useful corroboration, but tenants are not in the curated registry; no automatic slug-to-company conversion. |
| Latent Defense JD with an encoded Ashby tenant | Unknown/non-curated tenant; no automatic naming. |
| Allspring JD + `careers-allspringglobal.icims.com` | Plausible attribution pending independent verification; no hostname-to-brand guess. |
| Shimmick / subsidiary Axia Electric + Shimmick iCIMS link | Parent/subsidiary ambiguity; do not silently choose a legal employer. |
| Highrise AI and A.J. Boggs JD mentions + `grnh.se` short URLs | Short links do not establish a verified ATS tenant without resolving/validating them; not followed. A.J. Boggs's fraud alert is not proof this posting is fraudulent. |
| UPPER / Cocient / AuraOne engineering-review or contractor tracks | Named service/intermediary is not evidence of an underlying client employer; do not infer the client or a conventional SWE role. |
| Softadom / K SSS, Inc. / Abhisam Software “listed as” or “proposed” descriptions | Explicitly unverified JD evidence; no automatic employer extraction. |
| Generic React Developer / Software Developer text | No reliable employer evidence; length and technical keywords cannot establish identity. |

The retained-history replay attributes only **Dialogue AI** (`in-216e827c48493b4a`) and **Autoscience** (`in-8bbb13ae6d5c30fb`) through the already-curated ATS rule. This extends the prior rule to retained records; it is not a new discovery of either mapping. The current 27-row anonymous snapshot receives **zero new names**. No original posting, corporate employer, recruiter/client relationship, sponsorship, or eligibility claim was independently verified for the remaining records.

## Saved-data before/after

[Frozen replay](INDEED_QUALITY_REPLAY.json) records input SHA-256 hashes, exact source/ID joins, affected records, and immutable-field assertions across all **1,831 Board records**. The replay joins current saved JDs for evidence inspection without claiming those texts were independently verified or identical to the older scoring input.

| Measure | Before | After policy replay |
|---|---:|---:|
| Anonymous Indeed Board records | 135 | 133 |
| Anonymous Indeed A/B records | 41 | 39 |
| Anonymous jobs in current Indeed snapshot | 27 | 27 |
| Explicit suggested/proposed JDs in 492 saved JDs | Unlabelled | 15 flagged (3 anonymous, 12 named) |
| Priority tier changes | — | 4 A→B; no job removed |
| Recommended-action changes | — | 48 to `verify_details` |
| Technical score/cache/ID/date/state mutations | — | 0 |

The four priority changes are Atlassian plus named Indeed records `in-098ff0d1970b23fc` (Custom Software Development), `in-ebc15f486e932a32` (Alpha Bravo Development), and `in-e4a451709a50e8a9` (BurjSoft). The three anonymous proposed Software Developer JDs were already B. The 15 flagged JDs repeat generic software-development responsibilities, but explicit self-disclaimers drive the rule; no semantic “AI-generated” or fraud classifier was introduced. These findings establish evidence limitations, not that the companies or jobs are illegitimate.

Repeat the read-only comparison:

```bash
python3 scripts/preview_indeed_quality.py > /tmp/indeed-quality-replay.json
```

## Validation and independent review

Focused shared-policy/source/dashboard tests: **267 passed, 7 skipped** (optional integrations/live matching); both Node dashboard checks passed. The installed pinned JobSpy environment additionally passed **12/12** focused tests, including null employer, null name, and named-employer raw-parser round trips without network access. Coverage includes duplicate-query name recovery, exact-source-ID retention, recruiter-name precedence, immutable cached fit fields, compact warnings, cohort alternatives, proposed-JD controls, referral/negative-status precedence, warning escaping, and warning removal after verified attribution.

A separate reviewer inspected connected callers and preservation paths. It found a stale `verify_details` action after employer recovery; this was fixed and regression-tested. Final review reported no remaining actionable findings. An isolated local browser sample confirmed both employer and proposed-JD warnings appear beside titles and scores. Its shared-state connection was intentionally absent; no application-state writes occurred.

No broad crawl, bulk/historical rescoring, LLM request, external application/redirect follow-up, Supabase write, historical migration, or hosted CI/deployment verification ran. Compact historical records without retained JD text cannot be assessed for proposed/generic wording. The new policy takes effect in normal future Board/dashboard runs; the frozen comparisons are previews, not rewritten production outputs.
