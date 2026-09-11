# Cross-pipeline official coverage audit

- Generated: 2026-09-11T05:43:02.288767+00:00
- Official snapshot: 2026-09-11T00:25:25.178379+00:00
- Coverage scope: jobs from the last 3 days that pass shared hard + role/seniority prefilters; LLM score is not used.
- Validation: 100% exact observed coverage is the current review target; final validation is manual.
- Registry adapters: 97 implemented / 102 companies; 5 remain link-only.

## Company coverage

| Company | Manual state | Adapter | In scope | Exact | Gaps | Pending refresh | Coverage |
|---|---|---|---:|---:|---:|---:|---:|
| TikTok | unvalidated | tiktok | 52 | 47 | 4 | 1 | 92% |
| Google | unvalidated | google | 32 | 15 | 12 | 5 | 56% |
| JPMorgan Chase | unvalidated | oracle_hcm | 28 | 7 | 15 | 6 | 32% |
| Meta | unvalidated | meta | 15 | 12 | 3 | 0 | 80% |
| Microsoft | unvalidated | microsoft | 15 | 9 | 2 | 4 | 82% |
| ByteDance | unvalidated | bytedance | 13 | 11 | 2 | 0 | 85% |
| Cisco | unvalidated | workday | 10 | 0 | 9 | 1 | 0% |
| Salesforce | unvalidated | workday | 10 | 4 | 5 | 1 | 44% |
| Tesla | unvalidated | skip | 9 | 0 | 0 | 0 | - |
| Walmart Global Tech | unvalidated | walmart | 9 | 0 | 6 | 3 | 0% |
| Oracle | unvalidated | oracle_hcm | 8 | 1 | 5 | 2 | 17% |
| Qualcomm | unvalidated | pcsx | 8 | 3 | 4 | 1 | 43% |
| Two Sigma | unvalidated | avature | 7 | 5 | 2 | 0 | 71% |
| Workday | unvalidated | workday | 6 | 4 | 2 | 0 | 67% |
| AMD | unvalidated | jibe | 5 | 2 | 0 | 3 | 100% |
| Apple | unvalidated | apple | 4 | 4 | 0 | 0 | 100% |
| HPE | unvalidated | workday | 4 | 0 | 3 | 1 | 0% |
| Stripe | unvalidated | ats | 4 | 1 | 3 | 0 | 25% |
| Travelers | unvalidated | workday | 4 | 3 | 0 | 1 | 100% |
| Anthropic | unvalidated | greenhouse | 3 | 3 | 0 | 0 | 100% |
| Coinbase | unvalidated | ats | 3 | 3 | 0 | 0 | 100% |
| Intel | unvalidated | workday | 3 | 1 | 2 | 0 | 33% |
| Netflix | unvalidated | eightfold_html | 3 | 1 | 1 | 1 | 50% |
| Snap | unvalidated | workday | 3 | 2 | 0 | 1 | 100% |
| Verizon | unvalidated | happydance | 3 | 0 | 3 | 0 | 0% |
| Zoom | unvalidated | workday | 3 | 0 | 1 | 2 | 0% |
| Adobe | unvalidated | workday | 2 | 0 | 2 | 0 | 0% |
| Blizzard Entertainment | unvalidated | skip | 2 | 0 | 0 | 0 | - |
| Chewy | unvalidated | workday | 2 | 0 | 1 | 1 | 0% |
| Goldman Sachs | unsupported | skip | 2 | 0 | 0 | 0 | - |
| NVIDIA | unvalidated | workday | 2 | 1 | 1 | 0 | 50% |
| OpenAI | unvalidated | ashby | 2 | 2 | 0 | 0 | 100% |
| Red Hat | unvalidated | workday | 2 | 1 | 0 | 1 | 100% |
| Reddit | unvalidated | greenhouse | 2 | 1 | 0 | 1 | 100% |
| Robinhood | unvalidated | ats | 2 | 0 | 0 | 2 | - |
| Roblox | unvalidated | greenhouse | 2 | 2 | 0 | 0 | 100% |
| Snowflake | unvalidated | ashby | 2 | 0 | 1 | 1 | 0% |
| Uber | unvalidated | uber | 2 | 1 | 1 | 0 | 50% |
| Verkada | unvalidated | greenhouse | 2 | 1 | 1 | 0 | 50% |
| Wells Fargo | unvalidated | workday | 2 | 0 | 2 | 0 | 0% |
| Amazon | unvalidated | amazon | 1 | 0 | 1 | 0 | 0% |
| AppLovin | unvalidated | greenhouse | 1 | 1 | 0 | 0 | 100% |
| Bloomberg | unvalidated | avature | 1 | 0 | 1 | 0 | 0% |
| Brex | unvalidated | ats | 1 | 0 | 1 | 0 | 0% |
| CVS Health | unvalidated | workday | 1 | 1 | 0 | 0 | 100% |
| Databricks | unvalidated | greenhouse | 1 | 1 | 0 | 0 | 100% |
| Dell | unvalidated | oracle_hcm | 1 | 1 | 0 | 0 | 100% |
| Disney | unvalidated | disney | 1 | 0 | 1 | 0 | 0% |
| DoorDash | unvalidated | greenhouse | 1 | 1 | 0 | 0 | 100% |
| Expedia Group | unvalidated | workday | 1 | 0 | 1 | 0 | 0% |
| Figma | unvalidated | ats | 1 | 1 | 0 | 0 | 100% |
| LinkedIn | unvalidated | linkedin_company | 1 | 0 | 0 | 1 | - |
| MongoDB | unvalidated | greenhouse | 1 | 0 | 0 | 1 | - |
| Ramp | unvalidated | ats | 1 | 1 | 0 | 0 | 100% |
| SAP | unvalidated | sap | 1 | 1 | 0 | 0 | 100% |
| Samsara | unvalidated | ats | 1 | 1 | 0 | 0 | 100% |
| ServiceNow | unvalidated | smartrecruiters | 1 | 0 | 1 | 0 | 0% |
| Stryker | unvalidated | workday | 1 | 0 | 1 | 0 | 0% |
| Airbnb | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Ansys | unvalidated | radancy | 0 | 0 | 0 | 0 | - |
| Asana | unvalidated | ats | 0 | 0 | 0 | 0 | - |
| Block / Square | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Capital One | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| Chime | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Citadel | unvalidated | skip | 0 | 0 | 0 | 0 | - |
| Cloudflare | unvalidated | ats | 0 | 0 | 0 | 0 | - |
| Cohere | unvalidated | ats | 0 | 0 | 0 | 0 | - |
| Discord | unvalidated | ats | 0 | 0 | 0 | 0 | - |
| Dropbox | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Duolingo | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Equinix | unvalidated | radancy | 0 | 0 | 0 | 0 | - |
| F5 | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| Flex | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| GitLab | unvalidated | ats | 0 | 0 | 0 | 0 | - |
| HubSpot | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| IQVIA | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| IXL Learning | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Instacart | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Johnson & Johnson | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| Linear | unvalidated | ats | 0 | 0 | 0 | 0 | - |
| Lyft | unvalidated | ats | 0 | 0 | 0 | 0 | - |
| MathWorks | unvalidated | mathworks | 0 | 0 | 0 | 0 | - |
| Morgan Stanley | unvalidated | pcsx | 0 | 0 | 0 | 0 | - |
| Nasdaq | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| NetApp | unvalidated | radancy | 0 | 0 | 0 | 0 | - |
| Notion | unvalidated | ats | 0 | 0 | 0 | 0 | - |
| Palantir | unvalidated | lever | 0 | 0 | 0 | 0 | - |
| PayPal | unvalidated | pcsx | 0 | 0 | 0 | 0 | - |
| Pinterest | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| PointClickCare | unvalidated | lever | 0 | 0 | 0 | 0 | - |
| Pure Storage | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Roku | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Spotify | unvalidated | ats | 0 | 0 | 0 | 0 | - |
| TransUnion | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| Visa | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| Wayfair | unvalidated | skip | 0 | 0 | 0 | 0 | - |
| WeRide | unvalidated | lever | 0 | 0 | 0 | 0 | - |
| Yahoo | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| Yext | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| Zillow | unvalidated | workday | 0 | 0 | 0 | 0 | - |
| Zscaler | unvalidated | greenhouse | 0 | 0 | 0 | 0 | - |
| eBay | unvalidated | workday | 0 | 0 | 0 | 0 | - |

## Gaps / pending review (141)

| Status | Pipeline | Company | Title | Location | Link |
|---|---|---|---|---|---|
| pending_official_refresh | board | Reddit | Frontend Engineer, Ads | Remote - United States | [open](https://job-boards.greenhouse.io/reddit/jobs/8194576) |
| pending_official_refresh | board | Zoom | Software Development Engineer | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-development-engineer-at-zoom-4465878494) |
| pending_official_refresh | board | Cisco | Software Engineer | Milpitas, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-at-cisco-4465869490) |
| pending_official_refresh | board | LinkedIn | Software Engineer - Web Infrastructure | Mountain View, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-web-infrastructure-at-linkedin-4465865381) |
| pending_official_refresh | board | TikTok USDS Joint Venture | Site Reliability Engineer - Video Platform - USDS | San Jose, CA | [open](https://www.linkedin.com/jobs/view/site-reliability-engineer-video-platform-usds-at-tiktok-usds-joint-venture-4465839324) |
| pending_official_refresh | board | JPMorganChase | Software Engineer III (Full Stack) | Jersey City, NJ | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-full-stack-at-jpmorganchase-4465804131) |
| pending_official_refresh | board | Microsoft | Software Engineer II | Redmond, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-ii-at-microsoft-4465679126) |
| pending_official_refresh | board | Google | Software Engineer III, Infrastructure, Google Cloud Platforms | Kirkland, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-infrastructure-google-cloud-platforms-at-google-4464195807) |
| pending_official_refresh | board | Oracle | Software Developer 3 | Nashville, TN | [open](https://www.linkedin.com/jobs/view/software-developer-3-at-oracle-4463936233) |
| pending_official_refresh | board | AMD | Software Development Engineer — GPU Fleet Management & AI Infrastructure | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-development-engineer-%E2%80%94-gpu-fleet-management-ai-infrastructure-at-amd-4463901981) |
| pending_official_refresh | board | Robinhood | Software Engineer, Tokenization | Menlo Park, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-tokenization-at-robinhood-4463488473) |
| pending_official_refresh | board | Robinhood | Software Engineer, Tokenization | New York, NY | [open](https://www.linkedin.com/jobs/view/software-engineer-tokenization-at-robinhood-4463470511) |
| pending_official_refresh | board | JPMorganChase | Software Engineer III — Asset & Wealth Management (AM Services) — New Jersey (Onsite) | Jersey City, NJ | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-%E2%80%94-asset-wealth-management-am-services-%E2%80%94-new-jersey-onsite-at-jpmorganchase-4456443729) |
| pending_official_refresh | board | Google | Software Engineer III, Google Cloud Storage, Infrastructure | Sunnyvale, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-google-cloud-storage-infrastructure-at-google-4455427327) |
| pending_official_refresh | board | Walmart Global Tech | (USA) Software Engineer III | Bentonville, AR | [open](https://www.linkedin.com/jobs/view/usa-software-engineer-iii-at-walmart-global-tech-4453848056) |
| pending_official_refresh | board | Netflix | Distributed Systems Engineer (L5) - Compute | United States | [open](https://www.linkedin.com/jobs/view/distributed-systems-engineer-l5-compute-at-netflix-4453463405) |
| pending_official_refresh | board | Oracle | Software Developer 3 | Nashville, TN | [open](https://www.linkedin.com/jobs/view/software-developer-3-at-oracle-4452538247) |
| pending_official_refresh | board | MongoDB | Software Engineer 3 | New York, NY | [open](https://www.linkedin.com/jobs/view/software-engineer-3-at-mongodb-4446841326) |
| pending_official_refresh | board | JPMorganChase | Site Reliability Engineer II | Chicago, IL | [open](https://www.linkedin.com/jobs/view/site-reliability-engineer-ii-at-jpmorganchase-4446576361) |
| pending_official_refresh | board | Google | Forward Deployed Engineer IV, GenAI, Google Cloud | New York, NY | [open](https://www.linkedin.com/jobs/view/forward-deployed-engineer-iv-genai-google-cloud-at-google-4446425866) |
| pending_official_refresh | board | Snowflake | Software Engineer - Backend | Bellevue, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-backend-at-snowflake-4214697219) |
| pending_official_refresh | board | JPMorganChase | Software Engineer III (Full Stack) | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=f47fa7b48a77f536) |
| pending_official_refresh | board | Walmart | Summer 2027 Intern:: Software Engineer II | Bentonville, AR, US | [open](https://www.indeed.com/viewjob?jk=e902280db0835cca) |
| pending_official_refresh | board | Microsoft | Software Engineer II | Redmond, WA, US | [open](https://www.indeed.com/viewjob?jk=e13e9fd0f4cc53f4) |
| pending_official_refresh | board | Google | Software Engineer III, Infrastructure, Google Cloud Platforms | Kirkland, WA, US | [open](https://www.indeed.com/viewjob?jk=dccc72d580d106c2) |
| pending_official_refresh | board | Snap Inc. | Security Engineer, Level 5, Detection & Response | Los Angeles, CA, US | [open](https://www.indeed.com/viewjob?jk=ce75328df4376ec5) |
| pending_official_refresh | board | Walmart | (USA) Software Engineer III | Sunnyvale, CA, US | [open](https://www.indeed.com/viewjob?jk=b28bdd744f24edfc) |
| pending_official_refresh | board | AMD | Software Development Engineer — GPU Fleet Management & AI Infrastructure | San Jose, CA, US | [open](https://www.indeed.com/viewjob?jk=9f02ec060f130081) |
| pending_official_refresh | board | JPMorganChase | Infrastructure Engineer III | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=9edf28d107bf8ecf) |
| pending_official_refresh | board | Hewlett Packard Enterprise / HPE | Software Developer Cloud & Distributed Systems | San Juan, PR, US | [open](https://www.indeed.com/viewjob?jk=9407487c3afcb12c) |
| pending_official_refresh | board | Qualcomm | Modem Software Engineer | San Diego, CA, US | [open](https://www.indeed.com/viewjob?jk=8663b807254002e4) |
| pending_official_refresh | board | Red Hat | Specialist Solution Architect, Cloud Services | NC, US | [open](https://www.indeed.com/viewjob?jk=67bb168eab24c623) |
| pending_official_refresh | board | Microsoft | Software Engineer II | Redmond, WA, US | [open](https://www.indeed.com/viewjob?jk=5753875b2d44c209) |
| pending_official_refresh | board | Microsoft | Software Engineer | Redmond, WA, US | [open](https://www.indeed.com/viewjob?jk=39980b58238349d9) |
| pending_official_refresh | board | AMD | Software Development Engineer — GPU Fleet Management & AI Infrastructure | San Jose, CA, US | [open](https://www.indeed.com/viewjob?jk=362705868566eb0a) |
| pending_official_refresh | board | JPMorganChase | Security Engineer III | Wilmington, DE, US | [open](https://www.indeed.com/viewjob?jk=34b69d6d0a79f231) |
| pending_official_refresh | board | Zoom Communications | Software Development Engineer | San Jose, CA, US | [open](https://www.indeed.com/viewjob?jk=2a76c2d82f6e3440) |
| pending_official_refresh | board | Salesforce | Software Engineering SMTS | San Francisco, CA, US | [open](https://www.indeed.com/viewjob?jk=2a186112cea93ee3) |
| pending_official_refresh | board | Travelers | Data Engineer I (AWS, Databricks) | Hartford, CT, US | [open](https://www.indeed.com/viewjob?jk=2419b7ea620915f3) |
| pending_official_refresh | board | Google | Agentic Data Cloud Databases Engineer, Google Cloud | Austin, TX, US | [open](https://www.indeed.com/viewjob?jk=179f0313eadf5ed8) |
| pending_official_refresh | board | Chewy | Software Engineer II | Bellevue, WA, US | [open](https://www.indeed.com/viewjob?jk=03a2fc9c5205e0a0) |
| official_gap | board | ServiceNow | Software Engineer | Santa Clara, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-at-servicenow-4465314231) |
| official_gap | board | JPMorganChase | Software Engineer III (Agentic) | New York, NY | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-agentic-at-jpmorganchase-4465386624) |
| official_gap | board | Zoom | Zoom AI DevOps Engineer | San Jose, CA | [open](https://www.linkedin.com/jobs/view/zoom-ai-devops-engineer-at-zoom-4464150206) |
| official_gap | board | Meta | Software Engineer, LLVM Compiler | Menlo Park, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-llvm-compiler-at-meta-4463417864) |
| official_gap | board | Meta | Software Engineer, LLVM Compiler | Menlo Park, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-llvm-compiler-at-meta-4463413882) |
| official_gap | board | Walmart Global Tech | Software Engineer III | Sunnyvale, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-at-walmart-global-tech-4463086312) |
| official_gap | board | Walmart | (USA) Software Engineer III | Sunnyvale, CA | [open](https://www.linkedin.com/jobs/view/usa-software-engineer-iii-at-walmart-4463080310) |
| official_gap | board | Walmart | (USA) Software Engineer III | Bentonville, AR | [open](https://www.linkedin.com/jobs/view/usa-software-engineer-iii-at-walmart-4456159154) |
| official_gap | board | Stryker | Software Development Engineer | Fort Wayne, IN | [open](https://www.linkedin.com/jobs/view/software-development-engineer-at-stryker-4456155195) |
| official_gap | board | Stripe | Full Stack Engineer, Link | San Francisco, CA | [open](https://www.linkedin.com/jobs/view/full-stack-engineer-link-at-stripe-4456135062) |
| official_gap | board | Stripe | Full Stack Engineer, Link | Seattle, WA | [open](https://www.linkedin.com/jobs/view/full-stack-engineer-link-at-stripe-4456131110) |
| official_gap | board | Cisco | Forward Deployed Engineer- Splunk | San Francisco, CA | [open](https://www.linkedin.com/jobs/view/forward-deployed-engineer-splunk-at-cisco-4455965524) |
| official_gap | board | Google | Software Engineer III, AI/ML, Google Cloud Platforms | Sunnyvale, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-ai-ml-google-cloud-platforms-at-google-4454949219) |
| official_gap | board | Adobe | Software Development Engineer | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-development-engineer-at-adobe-4454946469) |
| official_gap | board | Google | Forward Deployed Engineer, Core, DevAI | San Jose, CA | [open](https://www.linkedin.com/jobs/view/forward-deployed-engineer-core-devai-at-google-4454786473) |
| official_gap | board | Google | Software Engineer III, Core Security | Chicago, IL | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-core-security-at-google-4454779567) |
| official_gap | board | Google | Software Engineer III, Home Infrastructure | Los Angeles, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-home-infrastructure-at-google-4454778542) |
| official_gap | board | Workday | Software Development Engineer - US Federal | Reston, VA | [open](https://www.linkedin.com/jobs/view/software-development-engineer-us-federal-at-workday-4453428037) |
| official_gap | board | Bloomberg | Cloud Site Reliability Engineer (SRE) - Data Management & Analytics Platform | Princeton, NJ | [open](https://www.linkedin.com/jobs/view/cloud-site-reliability-engineer-sre-data-management-analytics-platform-at-bloomberg-4452896784) |
| official_gap | board | Cisco | Site Reliability Engineer | Durham, NC | [open](https://www.linkedin.com/jobs/view/site-reliability-engineer-at-cisco-4452022991) |
| official_gap | board | Snowflake | Software Engineer - Database Engineering | Bellevue, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-database-engineering-at-snowflake-4446557429) |
| official_gap | board | JPMorganChase | Site Reliability Engineer III | Chicago, IL | [open](https://www.linkedin.com/jobs/view/site-reliability-engineer-iii-at-jpmorganchase-4446532767) |
| official_gap | board | Google | Software Engineer | Mountain View, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-at-google-4445404095) |
| official_gap | board | Qualcomm | #Video Software Engineer | San Diego, CA | [open](https://www.linkedin.com/jobs/view/%23video-software-engineer-at-qualcomm-4436814013) |
| official_gap | board | Google | Software Engineer III, Infrastructure, Google Cloud Global Networking | Sunnyvale, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-infrastructure-google-cloud-global-networking-at-google-4417867713) |
| official_gap | board | Microsoft | Site Reliability Engineering- CTJ- Poly | Redmond, WA | [open](https://www.linkedin.com/jobs/view/site-reliability-engineering-ctj-poly-at-microsoft-4387946613) |
| official_gap | board | JPMorganChase | Software Engineer III - React, Java | New York, NY | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-react-java-at-jpmorganchase-4465020285) |
| official_gap | board | Uber | Machine Learning Engineer II - AV Labs | Sunnyvale, CA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-ii-av-labs-at-uber-4465001320) |
| official_gap | board | Expedia Group | Full Stack Software Development Engineer III | Seattle, WA | [open](https://www.linkedin.com/jobs/view/full-stack-software-development-engineer-iii-at-expedia-group-4464982597) |
| official_gap | board | JPMorganChase | Experienced Software Engineer Java / Python (Full Stack or Back End) | Plano, TX | [open](https://www.linkedin.com/jobs/view/experienced-software-engineer-java-python-full-stack-or-back-end-at-jpmorganchase-4464956808) |
| official_gap | board | Verkada | Embedded Software Engineer - Access Control | San Mateo, CA, US | [open](https://www.indeed.com/viewjob?jk=9f2a9cd00ac8a2e2) |
| official_gap | board | JPMorganChase | Software Engineer III - IBM i (AS/400) Engineer | Plano, TX, US | [open](https://www.indeed.com/viewjob?jk=16bd55c95eee8fe8) |
| official_gap | board | Wells Fargo | AI Engineer, Innovation & AI (contract) | Charlotte, NC | [open](https://www.linkedin.com/jobs/view/ai-engineer-innovation-ai-contract-at-wells-fargo-4464966694) |
| official_gap | board | JPMorganChase | Software Engineer III - GenAI Foundational Services | McLean, VA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-genai-foundational-services-at-jpmorganchase-4464963284) |
| official_gap | board | Cisco | Software Engineer, Collaboration Devices | Durham, NC | [open](https://www.linkedin.com/jobs/view/software-engineer-collaboration-devices-at-cisco-4463592650) |
| official_gap | board | Wells Fargo | AI Engineer, Innovation & AI (contract) | Charlotte, NC, US | [open](https://www.indeed.com/viewjob?jk=f28f1c59ab76f307) |
| official_gap | board | Qualcomm | AI Model Optimization Architect | Austin, TX, US | [open](https://www.indeed.com/viewjob?jk=94e99a638384ff89) |
| official_gap | board | Meta | Computer Vision Engineer | Burlingame, CA, US | [open](https://www.indeed.com/viewjob?jk=9343546381739e54) |
| official_gap | board | Qualcomm | #Software Engineer | San Diego, CA, US | [open](https://www.indeed.com/viewjob?jk=558cd6c85bd3c5ac) |
| official_gap | board | Salesforce | Software Engineering MTS | Bellevue, WA | [open](https://www.linkedin.com/jobs/view/software-engineering-mts-at-salesforce-4464938136) |
| official_gap | board | Chewy | Software Engineer II | Bellevue, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-ii-at-chewy-4464935636) |
| official_gap | board | Salesforce | Software Engineering (SMTS/LMTS) | San Francisco, CA | [open](https://www.linkedin.com/jobs/view/software-engineering-smts-lmts-at-salesforce-4464927854) |
| official_gap | board | Verizon | AI Engineer — AI Platform Engineering | Basking Ridge, NJ | [open](https://www.linkedin.com/jobs/view/ai-engineer-%E2%80%94-ai-platform-engineering-at-verizon-4464665075) |
| official_gap | board | Workday | Software Engineer | San Francisco Bay Area | [open](https://www.linkedin.com/jobs/view/software-engineer-at-workday-4463556098) |
| official_gap | board | The Walt Disney Company | Software Engineer II | Glendale, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-ii-at-the-walt-disney-company-4463537265) |
| official_gap | board | Microsoft | Software Engineer II - CTJ - Poly | Redmond, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-ii-ctj-poly-at-microsoft-4455735271) |
| official_gap | board | Oracle | Software Developer | Austin, TX, US | [open](https://www.indeed.com/viewjob?jk=ef14bb83598eebf9) |
| official_gap | board | Cisco | Leader, Solutions Engineer | San Jose, CA, US | [open](https://www.indeed.com/viewjob?jk=c89b0a1f2a43a880) |
| official_gap | board | JPMorganChase | Software Engineer III - React, Java | New York, NY, US | [open](https://www.indeed.com/viewjob?jk=b6ed06479eee1355) |
| official_gap | board | Cisco | Software Consulting Engineer I (Intern) United States | Research Triangle Park, NC, US | [open](https://www.indeed.com/viewjob?jk=a2055a1d372de233) |
| official_gap | board | Oracle | Applications Developer | Redwood City, CA, US | [open](https://www.indeed.com/viewjob?jk=87ac311d127733a5) |
| official_gap | board | Oracle | Software Developer | Austin, TX, US | [open](https://www.indeed.com/viewjob?jk=52b4b23724237cd0) |
| official_gap | board | Cisco | Solutions Engineer-US Commercial, North Florida Select | Maitland, FL, US | [open](https://www.indeed.com/viewjob?jk=4e3188a7e59cbe65) |
| official_gap | board | Cisco | Software Engineering Technical Leader | San Jose, CA, US | [open](https://www.indeed.com/viewjob?jk=48c1452c8981c9fe) |
| official_gap | board | JPMorganChase | Quantitative Trading & Research - Quantitative Developer Systematic Trading - Associate | New York, NY, US | [open](https://www.indeed.com/viewjob?jk=3ca6df36c400b0be) |
| official_gap | board | Salesforce | Software Engineering MTS | Bellevue, WA, US | [open](https://www.indeed.com/viewjob?jk=2bbe5469b433e310) |
| official_gap | board | Verizon | AI Engineer — AI Platform Engineering | Irving, TX, US | [open](https://www.indeed.com/viewjob?jk=11261eef85e22149) |
| official_gap | board | Cisco | Solutions Engineer-US Commercial, Nashville | Nashville, TN, US | [open](https://www.indeed.com/viewjob?jk=087202263180306d) |
| official_gap | board | Oracle | Software Developer | Austin, TX, US | [open](https://www.indeed.com/viewjob?jk=00d9f11fe3f18af7) |
| official_gap | board | Verizon | AI Engineer — AI Platform Engineering | Irving, TX | [open](https://www.linkedin.com/jobs/view/ai-engineer-%E2%80%94-ai-platform-engineering-at-verizon-4464654894) |
| official_gap | board | Cisco | Technical Leader, SIte Reliability Engineer | San Francisco, CA | [open](https://www.linkedin.com/jobs/view/technical-leader-site-reliability-engineer-at-cisco-4464620777) |
| official_gap | board | Walmart Global Tech | Software Engineer III (Backend Java/Rust) | Sunnyvale, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-backend-java-rust-at-walmart-global-tech-4462561119) |
| official_gap | board | Oracle | Software Developer 3 | Austin, TX | [open](https://www.linkedin.com/jobs/view/software-developer-3-at-oracle-4462550442) |
| official_gap | board | Two Sigma | Software Engineering Full-Time Campus Hire (Houston) | Houston, TX | [open](https://www.linkedin.com/jobs/view/software-engineering-full-time-campus-hire-houston-at-two-sigma-4462537752) |
| official_gap | board | Two Sigma | Software Engineering Full-Time Campus Hire - NYC 2027 | New York, United States | [open](https://www.linkedin.com/jobs/view/software-engineering-full-time-campus-hire-nyc-2027-at-two-sigma-4462529784) |
| official_gap | board | JPMorganChase | Software Engineer III - Java Fullstack / AWS | Austin, TX | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-java-fullstack-aws-at-jpmorganchase-4455597270) |
| official_gap | board | ByteDance | Multi-Cloud CDN Scheduling Platform Engineer Graduate (CDN Platform) - 2027 Start | Seattle, WA | [open](https://www.linkedin.com/jobs/view/multi-cloud-cdn-scheduling-platform-engineer-graduate-cdn-platform-2027-start-at-bytedance-4454515369) |
| official_gap | board | TikTok | Self-Built Engineer Graduate (CDN Platform) - 2027 Start | Seattle, WA | [open](https://www.linkedin.com/jobs/view/self-built-engineer-graduate-cdn-platform-2027-start-at-tiktok-4454467306) |
| official_gap | board | ByteDance | Multi-Cloud CDN Scheduling Platform Engineer Graduate (CDN Platform) - 2027 Start | San Jose, CA | [open](https://www.linkedin.com/jobs/view/multi-cloud-cdn-scheduling-platform-engineer-graduate-cdn-platform-2027-start-at-bytedance-4453614116) |
| official_gap | board | TikTok | Software Engineer Graduate (Foundation Platform) - 2027 Start | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-graduate-foundation-platform-2027-start-at-tiktok-4452901177) |
| official_gap | board | Google | Software Engineer III, Mobile (iOS) | Sunnyvale, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-mobile-ios-at-google-4426950905) |
| official_gap | board | Google | Software Engineer III, Mobile (Android) | San Bruno, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-mobile-android-at-google-4426937971) |
| official_gap | board | TikTok | Machine Learning Engineer Graduate - (TikTok Trust and Safety - CV/NLP/Multimodal LLM) - 2 | Seattle, WA | [open](https://www.linkedin.com/jobs/view/machine-learning-engineer-graduate-tiktok-trust-and-safety-cv-nlp-multimodal-llm-2026-start-phd-at-tiktok-4262549276) |
| official_gap | board | Hewlett Packard Enterprise / HPE | Software UI Engineer II - React & Enterprise Web Platforms | San Juan, PR, US | [open](https://www.indeed.com/viewjob?jk=bea0c8836ab4dec3) |
| official_gap | board | JPMorganChase | Software Engineer II - AI Research | Jersey City, NJ, US | [open](https://www.indeed.com/viewjob?jk=b5fcf7c5672cc861) |
| official_gap | board | JPMorganChase | Software Engineer III - GenAI Foundational Services | McLean, VA, US | [open](https://www.indeed.com/viewjob?jk=8aeb704a2905702c) |
| official_gap | board | Hewlett Packard Enterprise / HPE | DevOps Engineer – Generative AI & Enterprise Web Platforms | San Juan, PR, US | [open](https://www.indeed.com/viewjob?jk=660f42f62fb233f1) |
| official_gap | board | Hewlett Packard Enterprise / HPE | Software Engineer II – Generative AI & LLM Platforms | San Juan, PR, US | [open](https://www.indeed.com/viewjob?jk=51506997cf019eed) |
| official_gap | board | JPMorganChase | Infrastructure Engineer III - Site Reliability | Plano, TX, US | [open](https://www.indeed.com/viewjob?jk=4d6e37be7ed84d69) |
| official_gap | board | Salesforce | Software Engineering LMTS | San Francisco, CA | [open](https://www.linkedin.com/jobs/view/software-engineering-lmts-at-salesforce-4455554009) |
| official_gap | board | Salesforce | Software Engineering LMTS | Bellevue, WA | [open](https://www.linkedin.com/jobs/view/software-engineering-lmts-at-salesforce-4455537999) |
| official_gap | board | Google | Software Engineer, Reliability, Public Sector | Reston, VA | [open](https://www.linkedin.com/jobs/view/software-engineer-reliability-public-sector-at-google-4454710660) |
| official_gap | board | Stripe | Software Engineer, Product Security Data Platforms | Seattle, WA | [open](https://www.linkedin.com/jobs/view/software-engineer-product-security-data-platforms-at-stripe-4454549345) |
| official_gap | board | Adobe | Software Development Engineer 4 | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-development-engineer-4-at-adobe-4454449044) |
| official_gap | board | Google | Software Engineer III | Cambridge, MA | [open](https://www.linkedin.com/jobs/view/software-engineer-iii-at-google-4454291339) |
| official_gap | board | Google | Software Engineer, Infrastructure, Public Sector | Reston, VA | [open](https://www.linkedin.com/jobs/view/software-engineer-infrastructure-public-sector-at-google-4454279169) |
| official_gap | board | TikTok | Software Engineer Graduate (Media Engine) - 2027 Start | San Jose, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-graduate-media-engine-2027-start-at-tiktok-4452798180) |
| official_gap | board | Walmart Global Tech | (USA) Software Engineer III | Bentonville, AR | [open](https://www.linkedin.com/jobs/view/usa-software-engineer-iii-at-walmart-global-tech-4452527063) |
| official_gap | board | Intel | System Software Engineer | Phoenix, AZ | [open](https://www.linkedin.com/jobs/view/system-software-engineer-at-intel-4445193157) |
| official_gap | board | Google | Web Solutions Engineer | San Bruno, CA | [open](https://www.linkedin.com/jobs/view/web-solutions-engineer-at-google-4445185207) |
| official_gap | board | Intel | System Software Engineer | Phoenix, AZ | [open](https://www.linkedin.com/jobs/view/system-software-engineer-at-intel-4445174374) |
| official_gap | board | Brex | Software Engineer II, Backend | San Francisco, CA | [open](https://www.linkedin.com/jobs/view/software-engineer-ii-backend-at-brex-4410777817) |
| official_gap | board | Qualcomm | GPU Compiler Performance | Santa Clara, CA | [open](https://www.linkedin.com/jobs/view/gpu-compiler-performance-at-qualcomm-4368994836) |
| official_gap | board | Netflix | Software Engineer 5 - Content & Business Products | New York, NY | [open](https://www.linkedin.com/jobs/view/software-engineer-5-content-business-products-at-netflix-4220344508) |
| official_gap | board | Walmart | Software Engineer III (Backend Java/Rust) | Sunnyvale, CA, US | [open](https://www.indeed.com/viewjob?jk=f778ae5a1ad013be) |
| official_gap | board | JPMorganChase | Software Engineer II - Automation Tester | New York, NY, US | [open](https://www.indeed.com/viewjob?jk=09ab7f1974e96ec0) |
| official_gap | board | JPMorganChase | Software Engineer II - Automation Tester | New York, NY | [open](https://www.glassdoor.com/job-listing/j?jl=1010256146458) |
| official_gap | board | NVIDIA AI | Software Engineer, DOCA Networking | Palestine, TX | [open](https://www.linkedin.com/jobs/view/software-engineer-doca-networking-at-nvidia-ai-4462264840) |
| official_gap | syncareer | JPMorgan Chase | Software Engineer III (Agentic) | New York, New York, United States | [open](https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210711797) |
| official_gap | syncareer | Amazon | ID-Install Technician, Infrastructure Delivery | New Carlisle, Indiana, United States | [open](https://amazon.jobs/en/jobs/10532323/id-install-technician-infrastructure-delivery) |
