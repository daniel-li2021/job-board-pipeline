# SAP / HubSpot adapter follow-up — October 18, 2026

SAP discovery is restored through the public legacy recruitment interface linked from SAP's new site. No anti-bot bypass, browser fingerprinting, private credentials or guessed tenant is used. HubSpot remains blocked by its own upstream recruitment feed.

## Bounded public evidence

- Original SAP request: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States&startrow=0` returns 200 after redirect to `/en/jobs/`, drops the filter and yields **zero legacy-parser cards**.
- SAP's new page links **Visit our old careers site** to `https://careers.sap.com/`. The same filtered search on that hostname returned 200 with **25 cards**. The changed adapter replay against that exact saved HTTP response retains 25 normalized rows with detail fetching disabled. This is one query/page, not a full discovery run or 25 newly suitable opportunities.
- Two sampled public detail requests returned 200 and the expected posting URLs. `1438239233`, Senior Machine Learning Engineer – Research & Innovation Team: **7,108 JD characters**, SHA-256 `33d6343ea143c186e61b0aaf839a6adb1cd87730f68568a237f3becec835fc94`. `1408906233`, Expert DevOps Engineer: **9,581 JD characters**, SHA-256 `ae38e827f3733caed94231594ea35c8e84396dd0d83fd1e5770aac3eb7e407e3`.
- Both samples are senior roles. These results demonstrate usable discovery/JD extraction and do not claim early-career recommendation gains. No scoring request or alert was generated.
- HubSpot's configured `boards-api.greenhouse.io/v1/boards/hubspotjobs/jobs?content=true` returned **404**. Its employer careers page returned 200, but the public browser directory itself logged **GraphQL error: 404: Not Found** and showed no jobs. Its published Apollo bundle still references the same recruitment backend. No reliable replacement feed was established; changing to a guessed endpoint would hide the failure rather than fix it.
- Latest saved Official run has 94 OK sources, one empty SAP, one blocked HubSpot and six intentional link-only limitations. Stryker's older transient error was checked with one public CXS search (`limit=1`), which returned **200 / total 184**; its latest saved run is already healthy, so no adapter change was justified.

[Current SAP careers](https://jobs.sap.com/en/jobs/), [linked legacy SAP search](https://careers.sap.com/search/?q=software+engineer&locationsearch=United+States&startrow=0), [HubSpot careers](https://www.hubspot.com/careers/jobs).

## Implementation and protection

Only SAP's supported public hostname and manual search link change. Pagination/query budgets and role/eligibility/ranking policy stay intact. An unexpected search redirect now raises an explicit adapter failure instead of reporting a successful empty source. Missing job-content selectors retain missing/last-good descriptions and record a failure; full navigation HTML is not counted as a JD.

The identity compatibility layer preserves the legacy SAP host as an alias. Recognized posting IDs retain discovery dates from the durable ledger even if the old store row expired, and digest comparison recognizes old/new host URLs. Historical application keys are not rewritten.

Offline regressions cover search normalization, changed redirect contract, missing detail content, and the actual Official matching path preserving the old discovery date before scoring. Raw employer pages remain temporary files; minimal synthetic public-shape fixtures avoid committing page navigation/tracking data. The bounded live checks are development-machine evidence; the next normal hosted run must establish hosted adapter performance.
