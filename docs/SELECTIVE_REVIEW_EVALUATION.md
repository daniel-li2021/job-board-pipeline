# Selective review evaluation — October 18, 2026

**Do not integrate into production yet.** The experiment shows possible C-tier rescues, but the small, purposive packet, AI-only assessments, missing eligibility evidence, and one held-out false positive do not establish reliable practical value. No production score, action, eligibility policy, or application state was changed.

## Method and reliability

The original packet is unchanged: canonical SHA-256 `858370c65f77991cf7ce9f873bb9bc4ea0c3b3d1a538c7242be395fdf2d430b1`. A separate reviewer assessed 20 development records blind to model outputs and baseline scores/tiers. Those assessments are **AI silver labels, not verified human ground truth**. The reviewer later assessed the 20 held-out records after policy freeze, again blind to outputs and baselines. Each assessment retains evidence excerpts and reasoning. Historical summaries already contain prior interpretations, so their labels are not independent of all earlier modeling.

The seven original rejected IDs are enumerated in [rejection analysis](SELECTIVE_REJECTION_ANALYSIS.json). The old runner discarded raw responses and rejection reasons: their exact original failure causes cannot honestly be recovered. One rejected case has an empty JD, and several have long escaped/Unicode text, but neither observation proves the original cause. Replaying a new response would not recover the discarded response.

V2 asks for numbered contiguous JD/resume evidence references, resolves those references locally to exact excerpts, validates IDs/enums/references, requires resume support for A/B, keeps raw responses/usage/finish reasons, and retries only rejected cases once. It remains a standalone experiment with no pipeline call path. Exact references establish provenance, not semantic correctness. Two first-attempt development results used out-of-range references; both passed the bounded retry. No validator was weakened.

| Partition | First attempt valid | Final valid | Requests | Input tokens | Output tokens | Total |
|---|---:|---:|---:|---:|---:|---:|
| Development | 18/20 | 20/20 | 6 | 28,526 | 12,072 | 40,598 |
| Held out | 20/20 | 20/20 | 4 | 25,928 | 10,608 | 36,536 |

V2 used **77,134 billed API tokens** for 40 records; reasoning tokens are included in output tokens and must not be added again. The prior V1 development run used 22,364 tokens; both generations together total 99,498. These receipts exclude the separate reviewer's agent usage. No current dollar price or human review-time saving is claimed. Reliability improved from V1's 13/20 validated development outputs, but the samples/requests differ and retries cost tokens.

[Policy freeze](SELECTIVE_POLICY_FREEZE.json) was written at **2026-10-18 14:26:28.647545 UTC / 7:26 AM Pacific**, before submitting held-out evidence. It pins the packet, policy and runner and hashes the development receipt/assessment. The runner remains byte-identical. Both receipts use the same `gpt-6-luna`/medium settings. The freeze did not pin imported helper/configuration bytes; Git confirms those files stayed unchanged from the task baseline. This is a reproducibility limitation, not a claim of a stronger preregistration. No tuning or requerying followed the held-out results.

## Quality comparison

[Development metrics](SELECTIVE_DEV_METRICS.json) and [held-out metrics](SELECTIVE_HELD_OUT_METRICS.json) include per-record comparisons and explicit denominators. Independent review found the frozen runner's complete-case metric gate could hide baseline errors when review abstained. A separate offline summarizer corrects those denominators and verifies assessment fingerprints/partitions without changing the frozen runner or rerunning API requests.

| AI-assessment comparison | Development | Held out |
|---|---:|---:|
| Comparable baseline/review/assessment tiers | 9/20 | 11/20 |
| Exact tier corrections / harms | 2 / 1 | 2 / 0 |
| Proposed suitable C→A/B rescues / lost opportunities | 2 / 0 | 4 / 0 |
| Baseline false positives / assessable baseline tiers | 0 / 9 | 0 / 11 |
| Review false positives / assessable review tiers | 0 / 18 | 1 / 15 |
| Assessment unknown / review abstentions | 2 / 2 | 5 / 4 |
| Missing comparable baseline tier | 9 | 4 |
| Assessable eligibility cases | 0 | 0 |
| Eligibility claims unsupported by AI assessment | 2 | 0 |

Exact-tier corrections and rescues differ: a C→A proposal against expected B is an opportunity rescue but not an exact-tier correction. Review false positives use all assessable review tiers, including records without comparable baselines. Thus the held-out false positive must not disappear behind the 11-case baseline comparison.

All 40 independent eligibility assessments are unknown because the candidate evidence does not establish authorization/sponsorship need. **Eligibility error rate is null, not 0%.** No known-constraint escape was observed in this packet, but it has no assessable eligibility denominator. Precision@10, population recall/accuracy, application conversion, human review time and production ranking benefit remain unmeasured; a partial case packet is not a complete production ranking.

The development cohort includes two representations of Figma posting `6131089004`: 20 records represent at most 19 opportunities. No exact cross-partition source/posting-ID collisions were found, but many records omit original URLs, limiting that audit. The unchanged packet must not be advertised as 40 proven unique opportunities.

## Reproduction and decision

Reuse receipts without requests:

```bash
python3 scripts/summarize_selective_review.py development
python3 scripts/summarize_selective_review.py held_out
python3 -m pytest -q -p no:cacheprovider tests/test_selective_review_eval.py
```

The request runner reuses completed receipts and refuses mismatched packet/policy/partition fingerprints; held-out mode requires the freeze. Do not delete receipts to rerun held-out cases under a tuned policy. A later experiment needs a new untouched cohort.

The useful next decision is whether to supply explicit candidate eligibility constraints and obtain human adjudication of the disputed/rescued cases. No production review rollout is recommended from this evidence. Application Brief, Gmail sync and bulk profile enrichment remain deferred.
