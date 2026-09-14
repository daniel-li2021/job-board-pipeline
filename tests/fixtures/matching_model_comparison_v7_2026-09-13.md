# GPT-5.6 Terra vs Sol matching regression — v7

## Scope

- Prompt/scoring version: `v7-compact-early-career`
- Reasoning effort: `medium`
- Population: the 15 cases in `matching_regression_round2.json` (13 JD-backed, 2 deterministic no-JD)
- Harness: current production matching code, current candidate profile/routed resumes, empty score cache, current batch size 15
- Routing: identical two batches for each model (`resume_swe`: 10 jobs; `both`: 3 jobs)
- Production model was not changed.

## Telemetry

| Model | Run (UTC) | Requests | JSON decisions | Input | Output | Reasoning | Latency | Estimated cost |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.6 Terra | 2026-09-14 05:01:25 | 2 | 13/13 | 5,963 | 1,451 | 185 | 16.223s | $0.029338 |
| GPT-5.6 Sol | 2026-09-14 05:00:17 | 2 | 13/13 | 5,963 | 1,902 | 638 | 37.791s | $0.061892 |

Sol cost 111% more and took 133% longer on this sample. Both models returned valid decisions for every JD-backed case. The two no-JD cases stayed on deterministic fallback and cost no model tokens.

An earlier $0.011988 Sol harness-validation request is excluded from the comparison because shortened JDs retained aggregator source labels and 12 valid JD cases were incorrectly routed as thin. Total API cost incurred while establishing this comparison was $0.103218.

## Decisions

| Case | Category | Terra | Sol | Sol−Terra | Terra rank | Sol rank |
|---|---|---:|---:|---:|---:|---:|
| recent_429_swe_i | strong early career | 84 / B | 88 / B | +4 | 8 | 7 |
| recent_429_junior_swe | strong early career | 86 / A | 90 / A | +4 | 2 | 2 |
| recent_429_software_engineer_ii_cj | Level II / thin requirements | 72 / C | 68 / C | -4 | 9 | 11 |
| recent_429_software_engineer_ii_verisk | Level II / strong stack fit | 89 / B | 87 / B | -2 | 3 | 3 |
| recent_429_software_developer_engineer_ii | Level II / thin requirements | 70 / C | 72 / C | +2 | 10 | 10 |
| recent_429_tech_service_fde | tech service / stretch | 82 / B | 76 / C | -6 | 5 | 9 |
| recent_429_tech_service_no_sponsor | tech service / hard constraint | 74 / C | 76 / C | +2 | 11 | 8 |
| recent_429_embedded_coop | hardware-first co-op | 18 / C | 24 / C | +6 | 15 | 15 |
| recent_429_nonsoftware_automation | non-software false positive | 8 / C | 24 / C | +16 | 13 | 12 |
| thin_early_career_positive | no JD / positive title | 83 / B | 83 / B | 0 | 4 | 4 |
| thin_clearance_watch | no JD / clearance risk | 70 / C | 70 / C | 0 | 14 | 14 |
| known_good_early_career | strong early career | 96 / A | 96 / A | 0 | 1 | 1 |
| known_staffing_strong_fit | staffing / strong technical fit | 91 / B | 93 / B | +2 | 6 | 6 |
| known_nonsoftware_engineer_i | non-software Engineer I | 12 / C | 18 / C | +6 | 12 | 13 |
| known_strong_software_internship | strong software internship | 88 / B | 92 / B | +4 | 7 | 5 |

## Assessment

Sol modestly strengthened the explicit early-career and internship scores, but Terra already kept the genuine early-career cases in the strong range and produced the same A/B decisions for those cases. Level II/stretch behavior was mixed rather than consistently better. Terra was more decisive on the two non-software “engineer” false positives: it assigned lower scores and `seniority_fit=mismatch`, while Sol kept the rows in Tier C but labeled seniority `good`.

The sample does not show enough net quality improvement to justify Sol's roughly 2.1× cost and 2.3× latency. Keep GPT-5.6 Terra with medium reasoning as the production default and revisit only if a larger labeled set demonstrates a repeatable quality gain.
