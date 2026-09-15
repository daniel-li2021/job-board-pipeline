# Cross-pipeline official coverage audit

- Generated: 2026-09-15T19:16:36.039905+00:00
- Official snapshot: 2026-09-15T15:35:35.623700+00:00
- Board snapshot: 2026-09-15T17:18:10.617431+00:00
- Syncareer snapshot: 2026-09-15T15:14:11.868378+00:00
- Official coverage source: published_store
- Coverage scope: jobs from the last 3 days that pass shared hard + role/seniority prefilters; LLM score is not used.
- Validation: 100% exact observed coverage is the current review target; final validation is manual.
- Registry adapters: 97 implemented / 102 companies; 5 remain link-only.
- Exact reconciliation rate: 207 exact / 319 comparable (64.9%).
- Official presence rate: 78.1%; this includes ambiguous candidates.
- Identity resolution within observed Official matches: 83.1%.
- Identity evidence requiring review: 42 ambiguous title/location record(s) and 5 stable-ID record(s) absent from the snapshot; all remain unsuppressed.
- Exact match methods: {'url': 193, 'job_id': 1, 'title_location': 13}

## Company coverage

| Company | Manual state | Adapter | Board / Sync | In scope | Exact | Ambiguous | ID absent | No candidate | Pending | Unsupported | Exact rate | Presence |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| JPMorgan Chase | unvalidated | oracle_hcm | 72 / 7 | 79 | 46 | 13 | 2 | 16 | 2 | 0 | 60% | 77% |
| TikTok | unvalidated | tiktok | 32 / 0 | 32 | 8 | 0 | 0 | 22 | 2 | 0 | 27% | 27% |
| Google | unvalidated | google | 27 / 0 | 27 | 23 | 1 | 0 | 3 | 0 | 0 | 85% | 89% |
| Meta | unvalidated | meta | 22 / 0 | 22 | 13 | 9 | 0 | 0 | 0 | 0 | 59% | 100% |
| Microsoft | unvalidated | microsoft | 14 / 3 | 17 | 7 | 9 | 0 | 1 | 0 | 0 | 41% | 94% |
| OpenAI | unvalidated | ashby | 13 / 0 | 13 | 13 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Tesla | unvalidated | skip | 7 / 4 | 11 | 0 | 0 | 0 | 0 | 0 | 11 | - | - |
| Stripe | unvalidated | ats | 9 / 0 | 9 | 7 | 0 | 0 | 2 | 0 | 0 | 78% | 78% |
| Cisco | unvalidated | workday | 8 / 0 | 8 | 0 | 0 | 0 | 8 | 0 | 0 | 0% | 0% |
| Samsara | unvalidated | ats | 8 / 0 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Adobe | unvalidated | workday | 7 / 0 | 7 | 4 | 3 | 0 | 0 | 0 | 0 | 57% | 100% |
| Qualcomm | unvalidated | pcsx | 7 / 0 | 7 | 4 | 0 | 0 | 3 | 0 | 0 | 57% | 57% |
| Roblox | unvalidated | greenhouse | 7 / 0 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| GitLab | unvalidated | ats | 6 / 0 | 6 | 5 | 0 | 1 | 0 | 0 | 0 | 83% | 83% |
| HPE | unvalidated | workday | 6 / 0 | 6 | 6 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| DoorDash | unvalidated | greenhouse | 5 / 0 | 5 | 4 | 0 | 1 | 0 | 0 | 0 | 80% | 80% |
| Robinhood | unvalidated | ats | 5 / 0 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Travelers | unvalidated | workday | 5 / 0 | 5 | 3 | 2 | 0 | 0 | 0 | 0 | 60% | 100% |
| ByteDance | unvalidated | bytedance | 4 / 0 | 4 | 3 | 0 | 0 | 1 | 0 | 0 | 75% | 75% |
| Coinbase | unvalidated | ats | 4 / 0 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Expedia Group | unvalidated | workday | 4 / 0 | 4 | 3 | 1 | 0 | 0 | 0 | 0 | 75% | 100% |
| Walmart Global Tech | unvalidated | walmart | 4 / 0 | 4 | 1 | 1 | 0 | 2 | 0 | 0 | 25% | 50% |
| Anthropic | unvalidated | greenhouse | 3 / 0 | 3 | 2 | 0 | 0 | 1 | 0 | 0 | 67% | 67% |
| Chime | unvalidated | greenhouse | 3 / 0 | 3 | 2 | 0 | 0 | 1 | 0 | 0 | 67% | 67% |
| Oracle | unvalidated | oracle_hcm | 3 / 0 | 3 | 2 | 0 | 0 | 1 | 0 | 0 | 67% | 67% |
| Visa | unvalidated | workday | 3 / 0 | 3 | 2 | 0 | 0 | 1 | 0 | 0 | 67% | 67% |
| AMD | unvalidated | jibe | 2 / 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Blizzard Entertainment | unvalidated | skip | 2 / 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | - | - |
| Dell | unvalidated | oracle_hcm | 2 / 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Figma | unvalidated | ats | 2 / 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Flex | unvalidated | workday | 2 / 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0% | 0% |
| MongoDB | unvalidated | greenhouse | 2 / 0 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 50% | 100% |
| Reddit | unvalidated | greenhouse | 2 / 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| CVS Health | unvalidated | workday | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Chewy | unvalidated | workday | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Cohere | unvalidated | ats | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Equinix | unvalidated | radancy | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Johnson & Johnson | unvalidated | workday | 0 / 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0% | 0% |
| Morgan Stanley | unvalidated | pcsx | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| NVIDIA | unvalidated | workday | 1 / 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0% | 0% |
| NetApp | unvalidated | radancy | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Notion | unvalidated | ats | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Red Hat | unvalidated | workday | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| SAP | unvalidated | sap | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Salesforce | unvalidated | workday | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Snowflake | unvalidated | ashby | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Stryker | unvalidated | workday | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Two Sigma | unvalidated | avature | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Uber | unvalidated | uber | 1 / 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0% | 100% |
| Workday | unvalidated | workday | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Yahoo | unvalidated | workday | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Zoom | unvalidated | workday | 1 / 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0% | 100% |
| eBay | unvalidated | workday | 1 / 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100% | 100% |
| Airbnb | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Amazon | unvalidated | amazon | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Ansys | unvalidated | radancy | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| AppLovin | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Apple | unvalidated | apple | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Asana | unvalidated | ats | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Block / Square | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Bloomberg | unvalidated | avature | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Brex | unvalidated | ats | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Capital One | unvalidated | workday | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Citadel | unvalidated | skip | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Cloudflare | unvalidated | ats | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Databricks | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Discord | unvalidated | ats | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Disney | unvalidated | disney | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Dropbox | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Duolingo | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| F5 | unvalidated | workday | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Goldman Sachs | unsupported | skip | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| HubSpot | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| IQVIA | unvalidated | workday | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| IXL Learning | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Instacart | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Intel | unvalidated | workday | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Linear | unvalidated | ats | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| LinkedIn | unvalidated | linkedin_company | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Lyft | unvalidated | ats | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| MathWorks | unvalidated | mathworks | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Nasdaq | unvalidated | workday | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Netflix | unvalidated | eightfold_html | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Palantir | unvalidated | lever | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| PayPal | unvalidated | pcsx | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Pinterest | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| PointClickCare | unvalidated | lever | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Pure Storage | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Ramp | unvalidated | ats | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Roku | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| ServiceNow | unvalidated | smartrecruiters | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Snap | unvalidated | workday | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Spotify | unvalidated | ats | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| TransUnion | unvalidated | workday | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Verizon | unvalidated | happydance | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Verkada | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Wayfair | unvalidated | skip | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| WeRide | unvalidated | lever | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Wells Fargo | unvalidated | workday | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Yext | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Zillow | unvalidated | workday | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| Zscaler | unvalidated | greenhouse | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - |

## Expected unsupported / link-only sources (5)

- Tesla
- Blizzard Entertainment
- Citadel
- Goldman Sachs
- Wayfair

## Identity evidence requiring review (47)

- `official_ambiguous` (42): Official candidates exist, but title/location does not identify one requisition.
- `official_identity_unmatched` (5): a stable employer-side ID is absent from the Official snapshot; this is stronger adapter/snapshot-gap evidence.

| Status | Pipeline | Company | Title | Location | Stable IDs | Candidate IDs | Link |
|---|---|---|---|---|---|---|---|
| official_identity_unmatched | board | GitLab | Solutions Architect - West | Remote, United States | 8790317002 | - | [open](https://job-boards.greenhouse.io/gitlab/jobs/8790317002) |
| official_ambiguous | board | Microsoft | Software Engineer II | Redmond, WA | - | 200049224, 200055252, 200054718, 200044011, 200053768, 200048083, 200045590, 200052791 | [open](https://www.linkedin.com/jobs/view/software-engineer-ii-at-microsoft-4467734640) |
| official_ambiguous | board | JPMorganChase | Software Engineer III - Full Stack | Jersey City, NJ | - | 210782891, 210770776, 210767495 | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-full-stack-at-jpmorganchase-4467708484) |
| official_ambiguous | board | Meta | Software Engineer, SystemML - AI Networking | Menlo Park, CA | - | 1124065870041690, 1823307875501968 | [open](https://www.linkedin.com/jobs/view/software-engineer-systemml-ai-networking-at-meta-4465556572) |
| official_ambiguous | board | Uber | Machine Learning Engineer II - AV Labs | Sunnyvale, CA | - | 301156, 301475 | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-ii-av-labs-at-uber-4458555223) |
| official_ambiguous | board | Expedia Group | Full Stack Software Engineer II | Seattle, WA | - | R-100331, R-108283 | [open](https://www.linkedin.com/jobs/view/full-stack-software-engineer-ii-at-expedia-group-4466181603) |
| official_ambiguous | board | Adobe | Software Development Engineer | San Jose, CA | - | R171178, R170631, R170818, R168026, R164904, R170344, R170622, R171324, R170525, R171559 | [open](https://www.linkedin.com/jobs/view/software-development-engineer-at-adobe-4466176386) |
| official_ambiguous | board | Google | Software Engineer, Agent Cloud Rate Limiting | Sunnyvale, CA | - | 93519419505812166, 127788813236740806 | [open](https://www.linkedin.com/jobs/view/software-engineer-agent-cloud-rate-limiting-at-google-4465792183) |
| official_ambiguous | board | Microsoft | Software Engineer II | United States | - | 200049224, 200046929, 200055252, 200054718, 200048248, 200044011, 200053768, 200047257, 200048083, 200053943 | [open](https://www.linkedin.com/jobs/view/software-engineer-ii-at-microsoft-4439580330) |
| official_ambiguous | board | JPMorganChase | Site Reliability Engineer III | Jersey City, NJ, US | - | 210753167, 210779081, 210783304, 210786031, 210780341 | [open](https://JPMorganChase.contacthr.com/153570048) |
| official_ambiguous | board | JPMorganChase | Site Reliability Engineer III | Chicago, IL, US | - | 210769244, 210786738, 210770017 | [open](https://JPMorganChase.contacthr.com/153575109) |
| official_ambiguous | board | JPMorganChase | Site Reliability Engineer III | Jersey City, NJ, US | - | 210753167, 210779081, 210783304, 210786031, 210780341 | [open](https://www.indeed.com/viewjob?jk=af62b2bbf9ef8f14) |
| official_ambiguous | board | JPMorganChase | Site Reliability Engineer III | Houston, TX, US | - | 210773825, 210770691, 210775445 | [open](https://www.indeed.com/viewjob?jk=a4d6db6ec76634be) |
| official_ambiguous | board | JPMorganChase | Software Engineer III - Full Stack | Jersey City, NJ, US | - | 210782891, 210770776, 210767495 | [open](https://www.indeed.com/viewjob?jk=6e3525221246b5df) |
| official_ambiguous | board | JPMorganChase | Site Reliability Engineer III | Jersey City, NJ, US | - | 210753167, 210779081, 210783304, 210786031, 210780341 | [open](https://www.indeed.com/viewjob?jk=9378e3b9fa17137f) |
| official_ambiguous | board | JPMorganChase | Site Reliability Engineer III | Houston, TX, US | - | 210773825, 210770691, 210775445 | [open](https://www.indeed.com/viewjob?jk=6e625141b6dbd1f2) |
| official_ambiguous | board | Meta | Software Engineer, SystemML - AI Networking | Menlo Park, CA | - | 1124065870041690, 1823307875501968 | [open](https://www.linkedin.com/jobs/view/software-engineer-systemml-ai-networking-at-meta-4455037839) |
| official_ambiguous | board | MongoDB | Software Engineer 3 | United States | - | 8107198, 8083761 | [open](https://www.linkedin.com/jobs/view/software-engineer-3-at-mongodb-4447720429) |
| official_ambiguous | board | Adobe | Machine Learning Engineer | San Jose, CA | - | R171645, R171719, R171718 | [open](https://www.glassdoor.com/job-listing/machine-learning-engineer-adobe-JV_IC1147436_KO0,25_KE26,31.htm?jl=1010260801852) |
| official_ambiguous | board | Adobe | Machine Learning Engineer | San Jose, CA | - | R171645, R171719, R171718 | [open](https://www.glassdoor.com/job-listing/machine-learning-engineer-adobe-JV_IC1147436_KO0,25_KE26,31.htm?jl=1010260801851) |
| official_ambiguous | board | JPMorganChase | Site Reliability Engineer III | Jersey City, NJ, US | - | 210753167, 210779081, 210783304, 210786031, 210780341 | [open](https://www.indeed.com/viewjob?jk=ff076e76eb810700) |
| official_ambiguous | board | Walmart Global Tech | Software Engineer III | Sunnyvale, CA | - | R-2413964, R-2558404, R-2577801, R-2577774, R-2558794, R-2558623 | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-at-walmart-global-tech-4436636204) |
| official_ambiguous | board | Meta | Software Engineer, Systems ML | Bellevue, WA | - | 1346637694687934, 3414246448833665 | [open](https://www.linkedin.com/jobs/view/software-engineer-systems-ml-at-meta-4351661212) |
| official_ambiguous | board | Meta | Data Engineer, Product Analytics | United States | - | 1283364266159062, 3713685685437806 | [open](https://www.linkedin.com/jobs/view/data-engineer-product-analytics-at-meta-4120828067) |
| official_ambiguous | board | Meta | Data Engineer, Product Analytics | Menlo Park, CA | - | 1283364266159062, 3713685685437806 | [open](https://www.linkedin.com/jobs/view/data-engineer-product-analytics-at-meta-4120820999) |
| official_ambiguous | board | Meta | Software Engineer, SystemML - AI Networking | Menlo Park, CA | - | 1124065870041690, 1823307875501968 | [open](https://www.linkedin.com/jobs/view/software-engineer-systemml-ai-networking-at-meta-4414084980) |
| official_ambiguous | board | Meta | Data Engineer, Product Analytics | Bellevue, WA | - | 1283364266159062, 3713685685437806 | [open](https://www.linkedin.com/jobs/view/data-engineer-product-analytics-at-meta-4120824569) |
| official_identity_unmatched | board | DoorDash | Software Engineer, Unified Gateway | San Francisco, CA; Seattle, WA; Los Angeles, CA; New York, NY; San Francisco | 8146670 | - | [open](https://job-boards.greenhouse.io/doordashusa/jobs/8146670) |
| official_ambiguous | board | Microsoft | Software Engineer | Redmond, WA | - | 200048702, 200053775, 200053268 | [open](https://www.glassdoor.com/job-listing/software-engineer-microsoft-JV_IC1150499_KO0,17_KE18,27.htm?jl=1010243019364) |
| official_ambiguous | board | Meta | Data Engineer, Product Analytics | Bellevue, WA | - | 1283364266159062, 3713685685437806 | [open](https://www.linkedin.com/jobs/view/data-engineer-product-analytics-at-meta-4120827322) |
| official_ambiguous | board | JPMorganChase | Site Reliability Engineer III | Jersey City, NJ, US | - | 210753167, 210779081, 210783304, 210786031, 210780341 | [open](https://www.indeed.com/viewjob?jk=a39ecc4ca815593a) |
| official_ambiguous | board | JPMorganChase | Software Engineer III (Full Stack) | Jersey City, NJ, US | - | 210782891, 210770776, 210767495 | [open](https://www.indeed.com/viewjob?jk=6ba3442c01284f9d) |
| official_ambiguous | board | Microsoft | Software Engineer II | Redmond, WA | - | 200049224, 200055252, 200054718, 200044011, 200053768, 200048083, 200045590, 200052791 | [open](https://www.glassdoor.com/job-listing/software-engineer-ii-microsoft-JV_IC1150499_KO0,20_KE21,30.htm?jl=1010200821821) |
| official_ambiguous | board | Travelers | Data Engineer I (Databricks, AWS, Python) | Hartford, CT | - | R-51638, R-52342 | [open](https://www.glassdoor.com/job-listing/data-engineer-i-databricks-aws-python-travelers-JV_IC1148399_KO0,37_KE38,47.htm?jl=1010253881512) |
| official_ambiguous | board | Travelers | Data Engineer I (AWS, Databricks) | Hartford, CT | - | R-51521, R-52525 | [open](https://www.glassdoor.com/job-listing/data-engineer-i-aws-databricks-travelers-JV_IC1148399_KO0,30_KE31,40.htm?jl=1010259312694) |
| official_ambiguous | board | Meta | Software Engineer, Machine Learning | United States | - | 1030771533168017, 1436181490732782, 998357492128826 | [open](https://www.glassdoor.com/job-listing/software-engineer-machine-learning-meta-JV_KO0,34_KE35,39.htm?jl=1009792905138) |
| official_ambiguous | board | JPMorganChase | Site Reliability Engineer III | Jersey City, NJ | - | 210753167, 210779081, 210783304, 210786031, 210780341 | [open](https://www.linkedin.com/jobs/view/site-reliability-engineer-iii-at-jpmorganchase-4466730212) |
| official_ambiguous | board | Microsoft | Software Engineer II | Redmond, WA | - | 200049224, 200055252, 200054718, 200044011, 200053768, 200048083, 200045590, 200052791 | [open](https://www.glassdoor.com/job-listing/software-engineer-ii-microsoft-JV_IC1150499_KO0,20_KE21,30.htm?jl=1010258836038) |
| official_ambiguous | board | Microsoft | Software Engineer | Redmond, WA | - | 200048702, 200053775, 200053268 | [open](https://www.glassdoor.com/job-listing/software-engineer-microsoft-JV_IC1150499_KO0,17_KE18,27.htm?jl=1010257746298) |
| official_ambiguous | board | Zoom Communications | Software Engineer | San Jose, CA | - | R19426, R19646, R19178, R18600 | [open](https://www.glassdoor.com/job-listing/software-engineer-zoom-video-communications-JV_IC1147436_KO0,17_KE18,43.htm?jl=1010138808603) |
| official_ambiguous | board | Microsoft | Software Engineer | Redmond, WA | - | 200048702, 200053775, 200053268 | [open](https://www.linkedin.com/jobs/view/software-engineer-at-microsoft-4457810573) |
| official_ambiguous | board | Microsoft | Software Engineer - CTJ - Poly | Redmond, WA | - | 200054221, 200042769 | [open](https://www.linkedin.com/jobs/view/software-engineer-ctj-poly-at-microsoft-4466701177) |
| official_ambiguous | board | Microsoft | Software Engineer - CTJ - Poly | Reston, VA | - | 200054221, 200042769 | [open](https://www.linkedin.com/jobs/view/software-engineer-ctj-poly-at-microsoft-4430456092) |
| official_ambiguous | board | JPMorganChase | Software Engineer II (Java/React) | New York, NY, US | - | 210744379, 210757578 | [open](https://www.indeed.com/viewjob?jk=45427b6bf6fd07a7) |
| official_identity_unmatched | syncareer | JPMorgan Chase | Software Engineer III (Java/Spring) | Jersey City, New Jersey, United States | 210785425 | - | [open](https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210785425) |
| official_identity_unmatched | syncareer | JPMorgan Chase | Software Engineer III - Java/AWS/ MQ connectivity | Tampa, Florida, United States | 210784170 | - | [open](https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210784170) |
| official_identity_unmatched | syncareer | Johnson & Johnson | Postdoctoral Scientist - Multimodal AI | Cambridge, Massachusetts, United States | 097997 | - | [open](https://www.careers.jnj.com/en/jobs/r-097997/postdoctoral-scientist-multimodal-ai/) |

## Official snapshot misses (65) and timing-pending records (4)

| Status | Pipeline | Company | Title | Location | Link |
|---|---|---|---|---|---|
| pending_official_refresh | board | JPMorganChase | Software Engineer III (Java/Spring) | Jersey City, NJ | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-java-spring-at-jpmorganchase-4467703535) |
| pending_official_refresh | board | JPMorganChase | 2027 Software Engineer Program - Full-Time - United States - July Start | Chicago, IL | [open](https://www.linkedin.com/jobs/view/2027-software-engineer-program-full-time-united-states-july-start-at-jpmorganchase-4448194736) |
| pending_official_refresh | board | TikTok USDS Joint Venture | Machine Learning Engineer Graduate (Tech and Product, USDS) - 2027 Start | San Jose, CA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-graduate-tech-and-product-usds-2027-start-at-tiktok-usds-joint-venture-4446630169) |
| pending_official_refresh | board | TikTok USDS Joint Venture | Software Engineer Graduate (Tech and Product, USDS) - 2027 Start | Seattle, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-graduate-tech-and-product-usds-2027-start-at-tiktok-usds-joint-venture-4446613511) |
| official_gap | board | TikTok USDS Joint Venture | Site Reliability Engineer, Tech Infra - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/site-reliability-engineer-tech-infra-usds-at-tiktok-usds-joint-venture-4467238247) |
| official_gap | board | TikTok USDS Joint Venture | Site Reliability Engineer, Tech Infrastructure - USDS | Seattle, WA | [open](https://www.linkedin.com/jobs/view/site-reliability-engineer-tech-infrastructure-usds-at-tiktok-usds-joint-venture-4467232362) |
| official_gap | board | TikTok USDS Joint Venture | Software Engineer, Corporate Information Systems - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-corporate-information-systems-usds-at-tiktok-usds-joint-venture-4467227682) |
| official_gap | board | Google | Software Engineer, AI/Machine Learning, PhD, Early Career, 2027 Start | Madison, WI | [open](https://www.linkedin.com/jobs/view/software-engineer-ai-machine-learning-phd-early-career-2027-start-at-google-4456889314) |
| official_gap | board | Google | Software Engineer, AI/Machine Learning, PhD, Early Career, 2027 Start | Raleigh, NC | [open](https://www.linkedin.com/jobs/view/software-engineer-ai-machine-learning-phd-early-career-2027-start-at-google-4456873380) |
| official_gap | board | Google | Software Engineer, AI/Machine Learning, PhD, Early Career, 2027 Start | Atlanta, GA | [open](https://www.linkedin.com/jobs/view/software-engineer-ai-machine-learning-phd-early-career-2027-start-at-google-4456872374) |
| official_gap | board | Stripe | Forward Deployed Engineer, Privy | New York, United States | [open](https://www.linkedin.com/jobs/view/forward-deployed-engineer-privy-at-stripe-4454540410) |
| official_gap | board | Chime | Software Engineer, Infrastructure | San Francisco Bay Area | [open](https://www.linkedin.com/jobs/view/software-engineer-infrastructure-at-chime-4436622634) |
| official_gap | board | Cisco | Cloud Engineer II (Full Time) - United States | San Francisco, CA, US | [open](https://www.indeed.com/viewjob?jk=6336d5eb0c40099a) |
| official_gap | board | Cisco | Solutions Engineer - Texas - ThousandEyes (Remote) | Austin, TX, US | [open](https://www.indeed.com/viewjob?jk=507ffeea2400f788) |
| official_gap | board | JPMorganChase | Software Engineer III (Java/Spring) | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=27e0b5d1b3ae2eb8) |
| official_gap | board | JPMorganChase | Software Engineer III — Asset & Wealth Management (AM Services) — New Jersey (Onsite) | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=ff5282a795d3a7e5) |
| official_gap | board | JPMorganChase | Software Engineer III - Asset Management Technology | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=c33f02a8035bdca7) |
| official_gap | board | JPMorganChase | AWS Software Engineer III-Full Stack/Java/Spring Boot | Tampa, FL, US | [open](https://www.indeed.com/viewjob?jk=acf99ea8798263cc) |
| official_gap | board | JPMorganChase | Java AWS Software Engineer III | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=a7eb50abf8fbed3e) |
| official_gap | board | JPMorganChase | Software Engineer III - Asset Management Research Engineer | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=7b14e30f1dc2f397) |
| official_gap | board | JPMorganChase | Software Engineer III (Java/React) | New York, NY, US | [open](https://www.indeed.com/viewjob?jk=57999baaa41bb3e6) |
| official_gap | board | TikTok USDS Joint Venture | Software Engineer, Ads Pangle - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-ads-pangle-usds-at-tiktok-usds-joint-venture-4467003250) |
| official_gap | board | TikTok USDS Joint Venture | Machine Learning Engineer, TikTok Risk & Integrity - USDS | Seattle, WA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-tiktok-risk-integrity-usds-at-tiktok-usds-joint-venture-4467002236) |
| official_gap | board | TikTok USDS Joint Venture | Software Engineer, Ads - Core Infra - USDS | Los Angeles, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-ads-core-infra-usds-at-tiktok-usds-joint-venture-4466798307) |
| official_gap | board | TikTok USDS Joint Venture | Machine Learning Engineer - Ads Pangle - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-ads-pangle-usds-at-tiktok-usds-joint-venture-4466797291) |
| official_gap | board | TikTok USDS Joint Venture | Site Reliability Engineer, Compute - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/site-reliability-engineer-compute-usds-at-tiktok-usds-joint-venture-4466796269) |
| official_gap | board | TikTok USDS Joint Venture | Machine Learning Engineer, Recommendations - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-recommendations-usds-at-tiktok-usds-joint-venture-4466795319) |
| official_gap | board | TikTok USDS Joint Venture | Machine Learning Engineer, Recommendations - USDS | Seattle, WA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-recommendations-usds-at-tiktok-usds-joint-venture-4466795312) |
| official_gap | board | TikTok USDS Joint Venture | Software Engineer, Ads Pangle - USDS | Seattle, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-ads-pangle-usds-at-tiktok-usds-joint-venture-4466793335) |
| official_gap | board | TikTok USDS Joint Venture | Software Engineer, Ads ML Infrastructure - USDS | Los Angeles, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-ads-ml-infrastructure-usds-at-tiktok-usds-joint-venture-4466788310) |
| official_gap | board | TikTok USDS Joint Venture | Machine Learning Engineer, E-Commerce - USDS | Seattle, WA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-e-commerce-usds-at-tiktok-usds-joint-venture-4466786288) |
| official_gap | board | TikTok USDS Joint Venture | Machine Learning Engineer, Ads Pangle - USDS | Seattle, WA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-ads-pangle-usds-at-tiktok-usds-joint-venture-4466785398) |
| official_gap | board | TikTok USDS Joint Venture | Machine Learning Engineer, Search - USDS | Seattle, WA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-search-usds-at-tiktok-usds-joint-venture-4466785356) |
| official_gap | board | TikTok USDS Joint Venture | Software Engineer, Recommendations - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-recommendations-usds-at-tiktok-usds-joint-venture-4466783403) |
| official_gap | board | TikTok USDS Joint Venture | Machine Learning Engineer, TikTok Risk & Integrity - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-tiktok-risk-integrity-usds-at-tiktok-usds-joint-venture-4466782419) |
| official_gap | board | TikTok USDS Joint Venture | Machine Learning Engineer, E-Commerce - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-e-commerce-usds-at-tiktok-usds-joint-venture-4466781409) |
| official_gap | board | Cisco | Data Engineer | San Jose, CA, US | [open](https://www.indeed.com/viewjob?jk=d8a94c287356117b) |
| official_gap | board | JPMorganChase | Investment Banking - Technical Transaction Team, Energy - Associate Engineer | Houston, TX, US | [open](https://www.indeed.com/viewjob?jk=ab89eb7c71891d1c) |
| official_gap | board | Trade Flex Supply Chain Solutions Inc. | Junior Customs Automation Assistant | McAllen, TX, US | [open](https://www.indeed.com/viewjob?jk=6eaa991c9bf141ed) |
| official_gap | board | Cisco | Software Engineer Full Stack / Backend I (Full Time) - United States | San Jose, CA | [open](https://www.glassdoor.com/job-listing/software-engineer-full-stack-backend-i-full-time-united-states-cisco-systems-JV_IC1147436_KO0,62_KE63,76.htm?jl=1010247053649) |
| official_gap | board | Anthropic | Research Engineer, Knowledge Team | San Francisco Bay Area | [open](https://www.linkedin.com/jobs/view/research-engineer-knowledge-team-at-anthropic-4409985166) |
| official_gap | board | Cisco | Software Engineer - BackEnd | Richardson, TX | [open](https://www.glassdoor.com/job-listing/software-engineer-backend-cisco-systems-JV_IC1140053_KO0,25_KE26,39.htm?jl=1010242140910) |
| official_gap | board | TikTok USDS Joint Venture | Software Engineer, AI Data Application – USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-ai-data-application-%E2%80%93-usds-at-tiktok-usds-joint-venture-4466723154) |
| official_gap | board | JPMorganChase | Software Engineer III (Java/React) | New York, NY | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-java-react-at-jpmorganchase-4447741609) |
| official_gap | board | Qualcomm | #AI Infrastructure Software Engineer | San Diego, CA | [open](https://www.linkedin.com/jobs/view/%23ai-infrastructure-software-engineer-at-qualcomm-4447197268) |
| official_gap | board | Qualcomm | #Embedded Software Engineer - Video Technology | San Diego, CA | [open](https://www.linkedin.com/jobs/view/%23embedded-software-engineer-video-technology-at-qualcomm-4446780119) |
| official_gap | board | Walmart Global Tech | Software Engineer III - iOS | Sunnyvale, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-ios-at-walmart-global-tech-4444171711) |
| official_gap | board | JPMorganChase | Software Engineer III - Alternative Asset Management Technology | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=a255dad48afd92a4) |
| official_gap | board | Cisco | Software Engineer I (Full Time) - United States | Milpitas, CA | [open](https://www.glassdoor.com/job-listing/software-engineer-i-full-time-united-states-cisco-systems-JV_IC1147428_KO0,43_KE44,57.htm?jl=1010239981362) |
| official_gap | board | Flex Employee Services | Entry Level Java Full Stack Developer | Chicago, IL | [open](https://www.glassdoor.com/job-listing/entry-level-java-full-stack-developer-flex-employee-services-JV_IC1128808_KO0,37_KE38,60.htm?jl=1010237936026) |
| official_gap | board | TikTok USDS Joint Venture | Software Engineer, Enterprise Platform - Frontier Generative AI | Seattle, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-enterprise-platform-frontier-generative-ai-at-tiktok-usds-joint-venture-4466723156) |
| official_gap | board | Walmart | (USA) Software Engineer III | Hoboken, NJ | [open](https://www.linkedin.com/jobs/view/usa-software-engineer-iii-at-walmart-4454679097) |
| official_gap | board | TikTok USDS Joint Venture | Software Engineer, AI Data Application – USDS | Seattle, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-ai-data-application-%E2%80%93-usds-at-tiktok-usds-joint-venture-4466711306) |
| official_gap | board | Stripe | Forward Deployed Engineer, Professional Services | United States | [open](https://www.linkedin.com/jobs/view/forward-deployed-engineer-professional-services-at-stripe-4454537427) |
| official_gap | board | JPMorganChase | Software Engineer III - Asset Management Investment Platform (AMIP) | Columbus, OH, US | [open](https://www.indeed.com/viewjob?jk=d621af1100e64532) |
| official_gap | board | JPMorganChase | Software Engineer III - Asset & Wealth Management Technology | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=68a3d47326a5ab0a) |
| official_gap | board | JPMorganChase | 2027 Software Engineer Program - Full-Time - United States - July Start | Chicago, IL, US | [open](https://www.indeed.com/viewjob?jk=580ce32fa833723a) |
| official_gap | board | Oracle | Software Developer | Nashville, TN, US | [open](https://www.indeed.com/viewjob?jk=eb03318ea2fd7b4e) |
| official_gap | board | Cisco | Software Engineer, Test Automation | San Jose, CA | [open](https://www.glassdoor.com/job-listing/software-engineer-test-automation-cisco-systems-JV_IC1147436_KO0,33_KE34,47.htm?jl=1010247816543) |
| official_gap | board | Qualcomm | Machine Learning Engineer - College Graduate | San Diego, CA | [open](https://www.glassdoor.com/job-listing/machine-learning-engineer-college-graduate-qualcomm-JV_IC1147311_KO0,42_KE43,51.htm?jl=1010094513282) |
| official_gap | board | NVIDIA | Applied Systems Engineering Rotation Engineer - New College Graduate 2026 | Santa Clara, CA | [open](https://www.glassdoor.com/job-listing/applied-systems-engineering-rotation-engineer-new-college-graduate-2026-nvidia-JV_IC1147439_KO0,71_KE72,78.htm?jl=1010250294487) |
| official_gap | board | Visa One | Java Developer (Mandarin MUST - Will Train - Nationwide) | Seattle, WA | [open](https://www.glassdoor.com/job-listing/java-developer-mandarin-must-will-train-nationwide-visa-one-corporation-JV_IC1150505_KO0,50_KE51,71.htm?jl=1010248865347) |
| official_gap | board | Microsoft | Site Reliability Engineer II - CTJ - Poly | Reston, VA | [open](https://www.glassdoor.com/job-listing/site-reliability-engineer-ii-ctj-poly-microsoft-JV_IC1130404_KO0,37_KE38,47.htm?jl=1010245083550) |
| official_gap | board | ByteDance | Research Engineer, LLM/VLM Inference Optimization (Kernel & Compiler) - Seed Infra | Seattle, WA | [open](https://www.glassdoor.com/job-listing/research-engineer-llm-vlm-inference-optimization-kernel-compiler-seed-infra-bytedance-JV_IC1150505_KO0,75_KE76,85.htm?jl=1010103925525) |
| official_gap | board | TikTok USDS Joint Venture | Site Reliability Engineer, Platform Responsibility - USDS | Seattle, WA | [open](https://www.linkedin.com/jobs/view/site-reliability-engineer-platform-responsibility-usds-at-tiktok-usds-joint-venture-4466719171) |
| official_gap | board | Cisco | Security Engineer (Remote) | Denver, CO, US | [open](https://www.indeed.com/viewjob?jk=5e9996a075158b6a) |
| official_gap | board | JPMorganChase | Software Engineer III - Front End UI/React and Playwright with Java | Plano, TX, US | [open](https://www.indeed.com/viewjob?jk=5fb39958131db6bf) |
| official_gap | board | JPMorganChase | Software Engineer III (Java) | New York, NY, US | [open](https://www.indeed.com/viewjob?jk=513854c24e96596f) |
| official_gap | board | JPMorganChase | Software Engineer III - DevOps, Python and/or JavaScript | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=096498561178c0a0) |
