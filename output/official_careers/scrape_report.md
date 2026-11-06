# Official careers scrape report — 2026-11-06_0031

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Runtime metrics

- Wall time: 936.571s
- HTTP requests/cumulative request time: 7162 / 3149.290s
- Listing pages/detail fetched/cache reused/prefilter skipped: 1295 / 5827 / 302 / 875
- Detail cache statuses: {'fetched:changed': 1, 'fetched:missing_detail': 215, 'fetched:new': 5423, 'fetched:stale': 4, 'missing:new': 1, 'reuse_after_error:missing_detail': 1, 'reuse_after_error:stale': 41, 'reused': 258}
- Relevant JD coverage: 5387 / 5400; added detail requests 23 / 150; deferred 0

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 11.494s
- Company elapsed time: 26.155s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 122, 'usable_jd': 122}
- Raw jobs found: 799
- After US/location filtering: 253
- With trustworthy posted_date: 253
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.268, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "\"Ai Engineer\"", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.056, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Machine Learning Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.953, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Data Scientist\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.221, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Solutions Architect\"", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.229, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Data Engineer\"", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.925, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "\"Platform Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.948, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Full Stack Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.981, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "\"Forward Deployed Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.737, "first_pass_survivors": 67, "group": "official", "jds_resolved": 67, "original_postings_resolved": 67, "page_budget": 12, "pages_fetched": 8, "query": "\"Software Engineer\"", "raw_jobs": 160, "stop_reason": "early_stop", "unique_contribution": 67, "unique_jobs": 160}
- Query diagnostic: {"elapsed_seconds": 1.848, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Infrastructure Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.292, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 5, "pages_fetched": 4, "query": "\"Software Engineer III\"", "raw_jobs": 77, "stop_reason": "early_stop", "unique_contribution": 20, "unique_jobs": 77}
- Query diagnostic: {"elapsed_seconds": 1.414, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 2, "pages_fetched": 2, "query": "\"Web Solutions Engineer\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 1.279, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 2, "pages_fetched": 2, "query": "\"DeepMind\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "129750631622550214",
    "title": "Senior Software Engineer, AI/ML GenAI, Core",
    "location": "Kirkland, WA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/129750631622550214-senior-software-engineer-ai-ml-genai-core",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:31:13.779678+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "134802887552180934",
    "title": "Senior Software Engineer, Infrastructure, Google Workspace",
    "location": "Los Angeles, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/134802887552180934-senior-software-engineer-infrastructure-google-workspace",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:31:13.779678+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "130017812948099782",
    "title": "Software Engineer III, Performance, Platforms Infrastructure Engineering",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/130017812948099782-software-engineer-iii-performance-platforms-infrastructure-engineering",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:31:13.779678+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "76216509977764550",
    "title": "Business Data Scientist, Growth and Opportunity Marketing",
    "location": "New York, NY, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/76216509977764550-business-data-scientist-growth-and-opportunity-marketing",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:31:13.779678+00:00",
    "date_confidence": "high",
    "description": "Google's leadership team hand-picks thorny business challenges, and members of BizOps work in small teams to find solutions. As part of this team you fully immerse yourself in data"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "132777561364013766",
    "title": "Software Engineer III, Infrastructure, Google Cloud Security and Privacy",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/132777561364013766-software-engineer-iii-infrastructure-google-cloud-security-and-privacy",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:31:13.779678+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  }
]
```

## Amazon

- Status: ok
- Scraping method: HTTP GET search.json
- Search URL/API: `https://www.amazon.jobs/en/search?base_query=software+engineer&country=USA&offset=0&result_limit=10&sort=recent`
- Pagination: newest-first offset by 20; minimum 2 pages, then two seen pages + one overlap page; otherwise hits/cap
- Pages/requests fetched: 45
- HTTP requests/cumulative request time: 45 / 17.675s
- Company elapsed time: 29.176s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 482, 'usable_jd': 482}
- Raw jobs found: 854
- After US/location filtering: 739
- With trustworthy posted_date: 739
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.415, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.132, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 1.863, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 1.905, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.154, "first_pass_survivors": 56, "group": "official", "jds_resolved": 56, "original_postings_resolved": 56, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 56, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.643, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 50, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 50}
- Query diagnostic: {"elapsed_seconds": 0.358, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 15, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 1.153, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 38, "stop_reason": "early_stop", "unique_contribution": 38, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 7.941, "first_pass_survivors": 209, "group": "official", "jds_resolved": 209, "original_postings_resolved": 209, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 209, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.881, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.153, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 3, "pages_fetched": 3, "query": "systems development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.238, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.34, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 2, "pages_fetched": 2, "query": "applied scientist", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10595931",
    "title": "Software Development Engineer, AI Foundations, Amazon Leo Networking Software",
    "location": "Redmond, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10595931/software-development-engineer-ai-foundations-amazon-leo-networking-software",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:31:13.780245+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon's Low Earth Orbit satellite network, built to deliver fast, reliable internet to customers beyond the reach of existing networks. The AI Foundations team build"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10595393",
    "title": "Sr Technical Account Manager, US Federal, Enterprise Support",
    "location": "Arlington, Virginia, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10595393/sr-technical-account-manager-us-federal-enterprise-support",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:31:13.780245+00:00",
    "date_confidence": "high",
    "description": "AWS Applied AI Solutions (AAIS) is building toward a future where every business innovates with Amazon AI teammates. To get there, we build AI solutions that improve human capabili"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10594100",
    "title": "Software Development Engineer, Ads AI Core Infra (ACI)",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10594100/software-development-engineer-ads-ai-core-infra-aci",
    "posted_date": "2026-11-01",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:31:13.780245+00:00",
    "date_confidence": "high",
    "description": "Amazon Advertising is one of Amazon's fastest growing and most profitable businesses, responsible for defining and delivering AI-powered solutions that transform how advertisers ma"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10591564",
    "title": "Thermal & Mechanical Engineer, Annapurna Labs - AI Silicon Packaging",
    "location": "Austin, Texas, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10591564/thermal-mechanical-engineer-annapurna-labs-ai-silicon-packaging",
    "posted_date": "2026-10-30",
    "updated_date": "2026-10-31",
    "fetched_at": "2026-11-06T00:31:13.780245+00:00",
    "date_confidence": "high",
    "description": "As a member of the Machine Learning Acceleration team you'll be responsible for the design and optimization of hardware in our data centers. You'll provide leadership in the applic"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10591537",
    "title": "Software Development Engineer, AI Foundations, Amazon Leo AI Foundations",
    "location": "Redmond, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10591537/software-development-engineer-ai-foundations-amazon-leo-ai-foundations",
    "posted_date": "2026-10-29",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:31:13.780245+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon's Low Earth Orbit satellite network, built to deliver fast, reliable internet to customers beyond the reach of existing networks. The AI Foundations team build"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=ai+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 45 / 48.623s
- Company elapsed time: 63.554s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 3 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 203, 'detail_requests': 3, 'detail_failure': 3, 'budget_deferred': 0, 'usable_jd': 200}
- Raw jobs found: 840
- After US/location filtering: 294
- With trustworthy posted_date: 294
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.715, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.247, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.302, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.198, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.105, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.413, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.343, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.238, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.975, "first_pass_survivors": 112, "group": "official", "jds_resolved": 112, "original_postings_resolved": 112, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 112, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.578, "first_pass_survivors": 46, "group": "official", "jds_resolved": 46, "original_postings_resolved": 46, "page_budget": 3, "pages_fetched": 3, "query": "apps-and-frameworks-SFTWR-AF", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 46, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200693760-3749",
    "title": "AC-DC Power Design Engineer",
    "location": "San Jose, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200693760/ac-dc-power-design-engineer",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.780576+00:00",
    "date_confidence": "high",
    "description": "Apple is looking for an experienced AC-DC Adapter Design Engineer to develop the next generation of high-density offline power supplies for our portable products. In this role, you"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200686682-3543",
    "title": "Aesthetics Science ML Research Engineer",
    "location": "San Diego, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200686682/aesthetics-science-ml-research-engineer",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.780576+00:00",
    "date_confidence": "high",
    "description": "iPhone is the most popular camera in the world, and the Aesthetics Science team is focused on infusing photographic knowledge and personal preferences into the features and algorit"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200657272-0836",
    "title": "STA Engineer",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200657272/sta-engineer",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.780576+00:00",
    "date_confidence": "high",
    "description": "Imagine what you could do here at Apple, new ideas have a way of becoming extraordinary products, services, and customer experiences very quickly. Bring passion and dedication to y"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200657272-0505",
    "title": "STA Engineer",
    "location": "Beaverton, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200657272/sta-engineer",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.780576+00:00",
    "date_confidence": "high",
    "description": "Imagine what you could do here at Apple, new ideas have a way of becoming extraordinary products, services, and customer experiences very quickly. Bring passion and dedication to y"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200657260-0836",
    "title": "STA Engineer",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200657260/sta-engineer",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.780576+00:00",
    "date_confidence": "high",
    "description": "Imagine what you could do here at Apple, new ideas have a way of becoming extraordinary products, services, and customer experiences very quickly. Bring passion and dedication to y"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 234 / 69.775s
- Company elapsed time: 103.595s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 194 / 0 / 0
- Detail cache statuses: {'fetched:new': 188, 'fetched:missing_detail': 6}
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 390
- After US/location filtering: 194
- With trustworthy posted_date: 194
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.342, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.416, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 11.827, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 9.607, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.722, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.356, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.806, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 11.9, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 25.058, "first_pass_survivors": 46, "group": "official", "jds_resolved": 46, "original_postings_resolved": 46, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 46, "unique_jobs": 120}

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200065152",
    "title": "Principal Hardware Engineer",
    "location": "United States, Washington, Redmond; United States, California, Mountain View; United States, Oregon, Hillsboro; United States, North Carolina, Raleigh; United States, Texas, Austin",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557052943",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.781812+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200065162",
    "title": "Senior Principal Design Verification Engineer",
    "location": "United States, Washington, Redmond; United States, California, Mountain View; United States, Texas, Austin; United States, North Carolina, Raleigh; United States, Oregon, Hillsboro",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557052974",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.781812+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200063916",
    "title": "Sr Digital Solution Engineer - Cloud & AI Data",
    "location": "United States, Multiple Locations, Multiple Locations",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557047461",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.781812+00:00",
    "date_confidence": "high",
    "description": "Overview About Microsoft Elevate Microsoft Elevate is Microsoft's dedicated organization for advancing Education, Nonprofit, Workforce Development, and AI-for-Good outcomes globall"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200063917",
    "title": "Digital Solution Engineer - Cloud & AI Infrastructure",
    "location": "United States, Multiple Locations, Multiple Locations",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557047462",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.781812+00:00",
    "date_confidence": "high",
    "description": "Overview About Microsoft Elevate Microsoft Elevate is Microsoft's dedicated organization for advancing Education, Nonprofit, Workforce Development, and AI-for-Good outcomes globall"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200065009",
    "title": "Senior Software Engineer - Networking",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557051508",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.781812+00:00",
    "date_confidence": "high",
    "description": "Overview Would you like to help build the networking foundation that powers Windows, Azure, and Windows Server? Our team develops core networking and TCP/IP and QUIC technologies t"
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 510 / 279.941s
- Company elapsed time: 346.471s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 477 / 0 / 0
- Detail cache statuses: {'fetched:new': 468, 'fetched:missing_detail': 8, 'reuse_after_error:missing_detail': 1}
- Relevant JD recovery: {'eligible': 68, 'ai_recover': 1, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 67}
- Raw jobs found: 640
- After US/location filtering: 477
- With trustworthy posted_date: 476
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 48.09, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 42.614, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 46.388, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 44.35, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 28.662, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 32.726, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 27.575, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 19.076, "first_pass_survivors": 28, "group": "official", "jds_resolved": 27, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 32.007, "first_pass_survivors": 49, "group": "official", "jds_resolved": 49, "original_postings_resolved": 49, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 49, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 22.81, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2025309",
    "title": "Senior AI Engineer",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-AI-Engineer_JR2025309",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.783047+00:00",
    "date_confidence": "high",
    "description": "Join the AI & Automation Supply Chain Business Transformations team in NVIDIA Operations to develop the future of agentic AI at scale. As the Senior AI Engineer in Operations, you "
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2021717",
    "title": "Senior AI Engineer",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-AI-Engineer_JR2021717",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.783047+00:00",
    "date_confidence": "high",
    "description": "Join the AI & Automation Supply Chain Business Transformations team in NVIDIA Operations to develop the future of agentic AI at scale. As the Senior AI Engineer in Operations, you "
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2025254",
    "title": "Senior Applied AI Engineer",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Applied-AI-Engineer_JR2025254-1",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.783047+00:00",
    "date_confidence": "high",
    "description": "NVIDIA is looking for a Senior Applied AI Engineer to help build intelligent software systems that improve engineering productivity and software quality at scale. In this role, you"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2026233",
    "title": "AI Engineering Manager - Finance",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/AI-Engineering-Manager---Finance_JR2026233",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.783047+00:00",
    "date_confidence": "high",
    "description": "NVIDIA has been transforming computer graphics, PC gaming, and accelerated computing for more than 25 years. It’s a unique legacy of innovation that’s fueled by great technology—an"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2016861",
    "title": "Manager, Data and AI Engineering",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Manager--Data-and-AI-Engineering_JR2016861",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:13.783047+00:00",
    "date_confidence": "high",
    "description": "We are looking for a Manager of Data & AI Engineering who combines deep technical expertise with strong delivery leadership and people management. This role will drive the build-ou"
  }
]
```

## Salesforce

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://salesforce.wd12.myworkdayjobs.com/External_Career_Site`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 28
- HTTP requests/cumulative request time: 215 / 78.234s
- Company elapsed time: 107.296s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 186 / 0 / 0
- Detail cache statuses: {'fetched:new': 182, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 48, 'usable_jd': 48}
- Raw jobs found: 455
- After US/location filtering: 186
- With trustworthy posted_date: 186
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 35.648, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 76, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 11.68, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 4.267, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 15.905, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.285, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.217, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.732, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 7.469, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 8.271, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.171, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "software engineering mts", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 13}

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR367534",
    "title": "Systems Engineering Associate, Early Talent",
    "location": "Texas - Dallas",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Texas---Dallas/Systems-Engineering-Associate--Early-Talent_JR367534-2",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:39.935514+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. About Futureforce University Rec"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR366536",
    "title": "Senior Solution Consultant",
    "location": "California - San Francisco; Washington - Seattle",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Senior-Solution-Consultant_JR366536",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:39.935514+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR361319",
    "title": "Senior UX Product Designer – Design Systems",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/User-Interface-User-Experience-Senior-Designer_JR361319",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:39.935514+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category User Experience Job"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR367508",
    "title": "Escalation Manager",
    "location": "Illinois - Chicago; Georgia - Atlanta; Washington - Seattle; Indiana - Indianapolis; Washington - Bellevue; Texas - Austin",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Illinois---Chicago/Escalation-Manager_JR367508-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:39.935514+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Program & Project M"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR366380",
    "title": "Lead/Principal Solution Engineer - Life Sciences",
    "location": "New York - New York; New York - Remote; Illinois - Chicago; Georgia - Atlanta",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/New-York---New-York/Lead-Principal-Solution-Engineer---Life-Sciences_JR366380-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:39.935514+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  }
]
```

## Adobe

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://adobe.wd5.myworkdayjobs.com/external_experienced`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 28
- HTTP requests/cumulative request time: 130 / 61.785s
- Company elapsed time: 80.212s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 101 / 0 / 0
- Detail cache statuses: {'fetched:new': 99, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 30, 'usable_jd': 30}
- Raw jobs found: 429
- After US/location filtering: 101
- With trustworthy posted_date: 101
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 46.438, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 4.6, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 2.383, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 4.769, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 2.523, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.538, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.136, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 3.59, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 8.069, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 61, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 61}
- Query diagnostic: {"elapsed_seconds": 2.96, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 58}

Sample normalized records:

```json
[
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170716",
    "title": "AI Engineer 4",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/AI-Engineer-4_R170716-1",
    "posted_date": "2026-09-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:42.957071+00:00",
    "date_confidence": "high",
    "description": "We build the agentic AI platform that Adobe teams use to get real work done — OneAI , our unified intelligence layer, along with the reusable skills, agents, and dashboards that ru"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R172095",
    "title": "Forward Deployed AI Engineer, Marketing Intelligence & Consumer Insights",
    "location": "San Jose; Seattle; San Francisco",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Forward-Deployed-AI-Engineer--Marketing-Intelligence---Consumer-Insights_R172095",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:42.957071+00:00",
    "date_confidence": "high",
    "description": "The Opportunity Adobe's Growth Marketing & Insights (GMI) organization is in the middle of a ground-up reinvention of how marketing teams operate. We're no longer adding AI tools t"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170076",
    "title": "Senior AI Systems Engineer — C++ / Applied AI",
    "location": "San Jose; San Francisco; Seattle; New York; Chicago; Remote California",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Principal-AI-Systems-Engineer---C-----Applied-AI_R170076",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:42.957071+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are looking for a Senior AI Systems Engineer with deep C++ expertise to help build the next generation of AI-enabled product and platform capabilities. This role"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170691",
    "title": "AI Product Designer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Sr-User-Experience-Designer_R170691",
    "posted_date": "2026-09-21",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:42.957071+00:00",
    "date_confidence": "high",
    "description": "The Opportunity Bridgeway is Adobe's agentic marketing partner for small businesses and solopreneurs — photographers, estheticians, fitness coaches, bakers, contractors — the peopl"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R172283",
    "title": "Sr. Director, AI, Data Science & Engineering",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Sr-Director--AI--Data-Science---Engineering_R172283",
    "posted_date": "2026-10-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:42.957071+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are seeking a Senior Director of AI, Data Science & Engineering to lead the technical organization responsible for building the next generation of AI-powered fra"
  }
]
```

## Meta

- Status: ok
- Scraping method: HTTP POST Meta Relay GraphQL; dynamic LSD and doc_id discovery
- Search URL/API: `https://www.metacareers.com/jobsearch/`
- Pagination: one complete Relay payload per role query
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 21 / 15.416s
- Company elapsed time: 16.359s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 9 / 244 / 628
- Detail cache statuses: {'reused': 221, 'fetched:stale': 3, 'reuse_after_error:stale': 20, 'fetched:missing_detail': 3, 'fetched:new': 2}
- Relevant JD recovery: {'deterministic_skip': 440, 'cache_reused': 244, 'eligible': 230, 'ai_skip': 188, 'ai_recover': 4, 'detail_requests': 9, 'detail_success': 8, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 229}
- Raw jobs found: 2900
- After US/location filtering: 858
- With trustworthy posted_date: 23
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.514, "first_pass_survivors": 537, "group": "official", "jds_resolved": 0, "original_postings_resolved": 537, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 664, "stop_reason": "page_budget", "unique_contribution": 537, "unique_jobs": 664}
- Query diagnostic: {"elapsed_seconds": 0.439, "first_pass_survivors": 29, "group": "official", "jds_resolved": 0, "original_postings_resolved": 29, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 167, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 167}
- Query diagnostic: {"elapsed_seconds": 1.037, "first_pass_survivors": 54, "group": "official", "jds_resolved": 0, "original_postings_resolved": 54, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 180, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 180}
- Query diagnostic: {"elapsed_seconds": 0.501, "first_pass_survivors": 32, "group": "official", "jds_resolved": 0, "original_postings_resolved": 32, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 0.935, "first_pass_survivors": 163, "group": "official", "jds_resolved": 0, "original_postings_resolved": 163, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 743, "stop_reason": "page_budget", "unique_contribution": 163, "unique_jobs": 743}
- Query diagnostic: {"elapsed_seconds": 0.592, "first_pass_survivors": 29, "group": "official", "jds_resolved": 0, "original_postings_resolved": 29, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 438, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 438}
- Query diagnostic: {"elapsed_seconds": 0.814, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 1.509, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.896, "first_pass_survivors": 13, "group": "official", "jds_resolved": 0, "original_postings_resolved": 13, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 434, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 434}

Sample normalized records:

```json
[
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1119822984105122",
    "title": "HR Director, Insights",
    "location": "Menlo Park, CA; New York, NY; Remote, US",
    "official_url": "https://www.metacareers.com/jobs/1119822984105122",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:45.893077+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "704019139159184",
    "title": "Software Engineer (Leadership) - Infrastructure",
    "location": "Sunnyvale, CA; Bellevue, WA; Redmond, WA; Menlo Park, CA; Seattle, WA; Burlingame, CA; New York, NY; Remote, US",
    "official_url": "https://www.metacareers.com/jobs/704019139159184",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:45.893077+00:00",
    "date_confidence": "unknown",
    "description": "Meta is seeking talented principal engineers to join our teams in building cutting-edge products that connect billions of people around the world. As a member of our team, you will"
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1134731036124414",
    "title": "QA Engineering Lead (AI)",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/1134731036124414",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:45.893077+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2350629199088420",
    "title": "QA Engineering Lead (AI)",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/2350629199088420",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:45.893077+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1583033776429868",
    "title": "Director, Business Development & Strategic Alliances",
    "location": "Menlo Park, CA; New York, NY",
    "official_url": "https://www.metacareers.com/jobs/1583033776429868",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:45.893077+00:00",
    "date_confidence": "unknown",
    "description": ""
  }
]
```

## TikTok

- Status: ok
- Scraping method: HTTP POST public supplier /search/job/posts
- Search URL/API: `https://api.lifeattiktok.com/api/v1/public/supplier/search/job/posts`
- Pagination: offset=0,50,...; limit=50; US city filter
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 26 / 21.171s
- Company elapsed time: 25.227s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 426, 'usable_jd': 426}
- Raw jobs found: 1237
- After US/location filtering: 711
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.07, "first_pass_survivors": 199, "group": "official", "jds_resolved": 199, "original_postings_resolved": 199, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 199, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 2.762, "first_pass_survivors": 130, "group": "official", "jds_resolved": 130, "original_postings_resolved": 130, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 130, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.951, "first_pass_survivors": 111, "group": "official", "jds_resolved": 111, "original_postings_resolved": 111, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 111, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.533, "first_pass_survivors": 78, "group": "official", "jds_resolved": 78, "original_postings_resolved": 78, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 78, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.923, "first_pass_survivors": 65, "group": "official", "jds_resolved": 65, "original_postings_resolved": 65, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 65, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.184, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 1.83, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 86, "stop_reason": "early_stop", "unique_contribution": 24, "unique_jobs": 86}
- Query diagnostic: {"elapsed_seconds": 0.61, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 3.364, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 200}

Sample normalized records:

```json
[
  {
    "company": "TikTok",
    "source": "tiktok_official_careers",
    "job_id": "7668578318295386373",
    "title": "Machine Learning Engineer, AI Agent",
    "location": "San Jose, California, United States of America",
    "official_url": "https://lifeattiktok.com/search/7668578318295386373",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:54.749557+00:00",
    "date_confidence": "unknown",
    "description": "Our team focuses on the R&D of algorithm for TikTok international advertising customer growth. We leverage deep learning and large language model technologies to build an algorithm"
  },
  {
    "company": "TikTok",
    "source": "tiktok_official_careers",
    "job_id": "7688211031676979509",
    "title": "Senior AI Software Engineer - Creative AI Agents - TikTok",
    "location": "San Jose, California, United States of America",
    "official_url": "https://lifeattiktok.com/search/7688211031676979509",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:54.749557+00:00",
    "date_confidence": "unknown",
    "description": "Team Introduction: The AIGE (AI-Generated Effects) team is building AI-native creative tools that enable TikTok creators to turn natural-language and multimodal ideas into high-qua"
  },
  {
    "company": "TikTok",
    "source": "tiktok_official_careers",
    "job_id": "7678497203258919221",
    "title": "Tech Lead AI Software Engineer - Creative AI Agents (TikTok)",
    "location": "San Jose, California, United States of America",
    "official_url": "https://lifeattiktok.com/search/7678497203258919221",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:54.749557+00:00",
    "date_confidence": "unknown",
    "description": "The AIGE (AI-Generated Effects) team is building AI-native creative tools that enable TikTok creators to turn natural-language and multimodal ideas into high-quality, interactive e"
  },
  {
    "company": "TikTok",
    "source": "tiktok_official_careers",
    "job_id": "7669702702763018501",
    "title": "Machine Learning Engineer Intern (Commercial AI-CRM and Transaction) - 2027 Summer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://lifeattiktok.com/search/7669702702763018501",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:54.749557+00:00",
    "date_confidence": "unknown",
    "description": "The Commercial AI-CRM and Transaction team focuses on TikTok advertiser growth algorithms. Leveraging deep learning and large language model technologies, the team builds an algori"
  },
  {
    "company": "TikTok",
    "source": "tiktok_official_careers",
    "job_id": "7667935568626043141",
    "title": "Research Engineer Intern (Agentic Systems & AI Infrastructure - TikTok-Generalized Arch) - 2027 Start (PhD)",
    "location": "San Jose, California, United States of America",
    "official_url": "https://lifeattiktok.com/search/7667935568626043141",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:31:54.749557+00:00",
    "date_confidence": "unknown",
    "description": "TikTok is an international short video platform available in over 150 countries and regions, where we aim to inspire creativity and bring joy by helping people discover authentic a"
  }
]
```

## Uber

- Status: ok
- Scraping method: HTTP GET Oracle HCM recruitingCEJobRequisitions on iaziqy.fa.ocs.oraclecloud.com (offset pagination) + recruitingCEJobRequisitionDetails
- Search URL/API: `https://jobs.uber.com/en/jobs/?search=software%20engineer&page=1&pagesize=10`
- Pagination: HCM finder offset=(page-1)*limit ; limit=20; stop on empty/repeat or TotalJobsCount (do not stop at pages 1–7)
- Pages/requests fetched: 28
- HTTP requests/cumulative request time: 211 / 61.084s
- Company elapsed time: 90.178s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 183 / 0 / 0
- Detail cache statuses: {'fetched:new': 183}
- Relevant JD recovery: {'eligible': 33, 'usable_jd': 33}
- Raw jobs found: 548
- After US/location filtering: 183
- With trustworthy posted_date: 183
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.252, "first_pass_survivors": 70, "group": "official", "jds_resolved": 70, "original_postings_resolved": 70, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 70, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 11.286, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.729, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 37, "stop_reason": "early_stop", "unique_contribution": 17, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 10.762, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 51, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 51}
- Query diagnostic: {"elapsed_seconds": 4.553, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.371, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.881, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.04, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.303, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "304461",
    "title": "Principal Engineer - Security AI",
    "location": "Seattle, WA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/304461",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:19.977978+00:00",
    "date_confidence": "high",
    "description": "About the role and team Uber’s Security Engineering team’s mission is to protect, defend, and secure Uber’s products, infrastructure and data by building highly available, scalable"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "152899",
    "title": "Staff ML Engineer, Generative AI",
    "location": "Sunnyvale, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/152899",
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:19.977978+00:00",
    "date_confidence": "high",
    "description": "About the Role Uber’s Customer Obsession team builds the platform and AI that powers world‑class support across mobile, web, and voice at global scale. We are now hiring a Staff ML"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "145860",
    "title": "Staff Machine Learning Engineer - Applied AI",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/145860",
    "posted_date": "2026-07-17",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:19.977978+00:00",
    "date_confidence": "high",
    "description": "About the Team: The Applied AI team collaborates with product teams across Uber to deliver innovative AI solutions for core business problems. We work closely with engineering, pro"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "146988",
    "title": "Sr Staff ML Engineer - Applied AI",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/146988",
    "posted_date": "2026-06-19",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:19.977978+00:00",
    "date_confidence": "high",
    "description": "About the Team The Applied AI team collaborates with product teams across Uber to deliver innovative AI solutions for core business problems. We work closely with engineering, prod"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "303785",
    "title": "Principal Engineer - ML / AI – Foundation Models",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/303785",
    "posted_date": "2026-10-19",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:19.977978+00:00",
    "date_confidence": "high",
    "description": "About the role and team At Uber, machine learning powers some of the most complex real-time decisions in the world — from matching riders with drivers and optimizing marketplace ef"
  }
]
```

## DoorDash

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/doordashusa/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.494s
- Company elapsed time: 1.991s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 110, 'usable_jd': 110}
- Raw jobs found: 439
- After US/location filtering: 438
- With trustworthy posted_date: 438
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7467955",
    "title": "Account Executive",
    "location": "Tempe, AZ; Dallas, TX; Indianapolis, IN; Kansas City, MO; Richmond, VA; St. Louis, MO; Oklahoma City, OK; New Orleans, LA; Charleston, SC; Tempe, AZ",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7467955",
    "posted_date": "2025-12-12",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:32:57.378066+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8139265",
    "title": "Account Executive",
    "location": "Seattle, WA; Washington",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8139265",
    "posted_date": "2026-10-07",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:32:57.378066+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7927511",
    "title": "Account Executive, Ad Sales",
    "location": "New York, NY; Los Angeles, CA; Atlanta, GA; Chicago, IL; San Francisco, CA; San Francisco, CA",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7927511",
    "posted_date": "2026-05-15",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:32:57.378066+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7514895",
    "title": "Account Executive, New Verticals",
    "location": "New York, NY; Los Angeles, CA; Atlanta, GA; Chicago, IL; San Francisco, CA; New York",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7514895",
    "posted_date": "2026-01-07",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:32:57.378066+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7612643",
    "title": "Account Manager, CPG",
    "location": "New York, NY; San Francisco, CA; Los Angeles, CA; Chicago, IL; Atlanta, GA; San Francisco, CA",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7612643",
    "posted_date": "2026-02-13",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:32:57.378066+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  }
]
```

## Snap

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://wd1.myworkdaysite.com/recruiting/snapchat/snap`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 23
- HTTP requests/cumulative request time: 123 / 47.587s
- Company elapsed time: 64.452s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 99 / 0 / 0
- Detail cache statuses: {'fetched:new': 99}
- Relevant JD recovery: {'eligible': 15, 'usable_jd': 15}
- Raw jobs found: 372
- After US/location filtering: 99
- With trustworthy posted_date: 99
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.135, "first_pass_survivors": 63, "group": "official", "jds_resolved": 63, "original_postings_resolved": 63, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 63, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 4.498, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 0.72, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 5.722, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 6.62, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.797, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.95, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 0.664, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 6.602, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046612",
    "title": "Privacy Engineer, Level 4",
    "location": "Los Angeles, California; Palo Alto, California; New York, New York; Bellevue, Washington",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Privacy-Engineer--Level-4_R0046612-1",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:59.371616+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0047426",
    "title": "Application Engineer, CRM Technology, Level 4",
    "location": "Los Angeles, California; Palo Alto, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Application-Engineer--CRM-Technology--Level-4_R0047426-1",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:59.371616+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0047425",
    "title": "Staff Security Engineer, Identity Access Management",
    "location": "Los Angeles, California; Palo Alto, California; San Diego, California; Bellevue, Washington",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Staff-Security-Engineer--Identity-Access-Management_R0047425-1",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:59.371616+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "H226EM8",
    "title": "Manager, Software Engineering",
    "location": "Los Angeles, California; New York - 229 W 43rd St; Bellevue - 110 110th Ave NE; San Francisco - 1160 Battery St; Palo Alto - 395 Page Mill Rd",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Manager--Software-Engineering_H226EM8-1",
    "posted_date": "2026-09-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:59.371616+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "H226PE10",
    "title": "Principal Software Engineer",
    "location": "Los Angeles, California; New York - 229 W 43rd St; Bellevue - 110 110th Ave NE; Seattle - 2025 1st Avenue; San Francisco - 1160 Battery St; Palo Alto - 395 Page Mill Rd",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Principal-Software-Engineer_H226PE10",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:32:59.371616+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  }
]
```

## Pinterest

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/pinterest/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.291s
- Company elapsed time: 0.663s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 166
- After US/location filtering: 128
- With trustworthy posted_date: 128
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8268331",
    "title": "B2B Growth Marketing Manager",
    "location": "San Francisco, CA, US; Remote, US; San Francisco, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8268331",
    "posted_date": "2026-10-29",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:33:03.170229+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8319154",
    "title": "Business Development, AI Product Partnerships",
    "location": "San Francisco, CA, US; Remote, US; San Francisco, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8319154",
    "posted_date": "2026-10-30",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:33:03.170229+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8119896",
    "title": "Business Development Lead",
    "location": "San Francisco, CA, US; Remote, US; Los Angeles, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8119896",
    "posted_date": "2026-10-30",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:33:03.170229+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "7488432",
    "title": "Chief of Staff to GM, Ads",
    "location": "San Francisco, CA, US; Palo Alto, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=7488432",
    "posted_date": "2026-10-14",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:33:03.170229+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8242487",
    "title": "Client Account Manager I (Fixed Term Contract)",
    "location": "São Paulo, BR",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8242487",
    "posted_date": "2026-10-07",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:33:03.170229+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  }
]
```

## Snowflake

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/snowflake`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.265s
- Company elapsed time: 0.612s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 44, 'usable_jd': 44}
- Raw jobs found: 372
- After US/location filtering: 270
- With trustworthy posted_date: 270
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "db1375f0-ea5d-404a-b640-259f94dbc995",
    "title": "Software Engineer - Database Engineering",
    "location": "US-CA-Menlo Park; Menlo Park, California, United States; US-WA-Bellevue",
    "official_url": "https://jobs.ashbyhq.com/snowflake/db1375f0-ea5d-404a-b640-259f94dbc995",
    "posted_date": "2026-07-28",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:03.834802+00:00",
    "date_confidence": "high",
    "description": "At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to "
  },
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "3eb872af-0ab1-4986-8f72-e7321fcd1538",
    "title": "Software Engineer - Backend",
    "location": "US-CA-Menlo Park; Menlo Park, California, United States; US-WA-Bellevue; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/snowflake/3eb872af-0ab1-4986-8f72-e7321fcd1538",
    "posted_date": "2026-02-06",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:03.834802+00:00",
    "date_confidence": "high",
    "description": "At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to "
  },
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "58aeb127-c600-4dc7-861f-6924f4125dce",
    "title": "Account Executive, Enterprise Acquisition",
    "location": "US-NY-New York; New York, New York, United States",
    "official_url": "https://jobs.ashbyhq.com/snowflake/58aeb127-c600-4dc7-861f-6924f4125dce",
    "posted_date": "2026-09-24",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:03.834802+00:00",
    "date_confidence": "high",
    "description": "At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to "
  },
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "b9b85c1d-0760-4e28-9dfe-41724c8335a1",
    "title": "Senior Data Scientist - Product",
    "location": "US-CA-Menlo Park; Menlo Park, California, United States; US-WA-Bellevue",
    "official_url": "https://jobs.ashbyhq.com/snowflake/b9b85c1d-0760-4e28-9dfe-41724c8335a1",
    "posted_date": "2025-08-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:03.834802+00:00",
    "date_confidence": "high",
    "description": "At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to "
  },
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "45535603-aa9b-4fce-b3ac-6babf38da22b",
    "title": "Sales Development Representative - German Speaker",
    "location": "DE-Munich-MSO; Munich, Bavaria, Germany",
    "official_url": "https://jobs.ashbyhq.com/snowflake/45535603-aa9b-4fce-b3ac-6babf38da22b",
    "posted_date": "2026-10-29",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:03.834802+00:00",
    "date_confidence": "high",
    "description": "At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to "
  }
]
```

## ServiceNow

- Status: ok
- Scraping method: HTTP GET SmartRecruiters /v1/companies/{slug}/postings (+ posting detail)
- Search URL/API: `https://careers.smartrecruiters.com/ServiceNow`
- Pagination: offset=0,100,... ; country=us; stop on empty/repeat or totalFound
- Pages/requests fetched: 22
- HTTP requests/cumulative request time: 443 / 255.345s
- Company elapsed time: 310.598s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 421 / 0 / 0
- Detail cache statuses: {'fetched:new': 421}
- Relevant JD recovery: {'eligible': 55, 'usable_jd': 55}
- Raw jobs found: 1929
- After US/location filtering: 421
- With trustworthy posted_date: 421
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 240.702, "first_pass_survivors": 330, "group": "official", "jds_resolved": 330, "original_postings_resolved": 330, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 330, "stop_reason": "page_budget", "unique_contribution": 330, "unique_jobs": 330}
- Query diagnostic: {"elapsed_seconds": 1.412, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 110, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 110}
- Query diagnostic: {"elapsed_seconds": 8.57, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 184, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 184}
- Query diagnostic: {"elapsed_seconds": 46.225, "first_pass_survivors": 70, "group": "official", "jds_resolved": 70, "original_postings_resolved": 70, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 265, "stop_reason": "page_budget", "unique_contribution": 70, "unique_jobs": 265}
- Query diagnostic: {"elapsed_seconds": 2.367, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 5.659, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 1.064, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 75, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 0.44, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 69, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 69}
- Query diagnostic: {"elapsed_seconds": 4.158, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 296, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 296}

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076449",
    "title": "Director, Packaging & Monetization Strategy - Employee Experience Group",
    "location": "Mountain View, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159991510--director-packaging-monetization-strategy-employee-experience-group",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:04.447581+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076871",
    "title": "Sr. Executive Sourcer - GTM",
    "location": "West Palm Beach, Florida, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159987110-sr-executive-sourcer-gtm",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:04.447581+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075818",
    "title": "Senior Director, Product Creative Direction",
    "location": "Kirkland, Washington, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159985479-senior-director-product-creative-direction",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:04.447581+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075955",
    "title": "Staff Machine Learning Engineer_Voice AI Engineer",
    "location": "Kirkland, Washington, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159969974-staff-machine-learning-engineer-voice-ai-engineer",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:04.447581+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075954",
    "title": "Senior Staff Machine Learning Engineer_Voice AI",
    "location": "Kirkland, Washington, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159967952-senior-staff-machine-learning-engineer-voice-ai-",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:04.447581+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  }
]
```

## LinkedIn

- Status: expected_limitation
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 0 / 0.000s
- Company elapsed time: 0.000s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

## Bloomberg

- Status: ok
- Scraping method: HTTP GET Avature SearchJobs HTML + JobDetail HTML
- Search URL/API: `https://bloomberg.avature.net/careers/SearchJobs?q=software+engineer&jobRecordsPerPage=12&jobOffset=0`
- Pagination: jobOffset=0,12,... ; stop on empty/repeat or short page
- Pages/requests fetched: 29
- HTTP requests/cumulative request time: 49 / 55.669s
- Company elapsed time: 67.617s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 20 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 20}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 348
- After US/location filtering: 20
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.318, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 4.791, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.496, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.657, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.639, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.601, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.622, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.364, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 6.129, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 48}

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46037",
    "title": "Bloomberg Intelligence Consumer Senior Research Analyst: Beverages",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Bloomberg-Intelligence-Consumer-Senior-Research-Analyst-Beverages/46037",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:27.232965+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg Intelligence (BI) delivers independent, data-driven research and interactive datasets integrated into the Bloomberg Terminal, helping investmen"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46026",
    "title": "Containerboard Market Research Sales Consultant - Remote (Contract)",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Containerboard-Market-Research-Sales-Consultant-Remote-Contract/46026",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:27.232965+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg runs on data. Our products are fueled by powerful information. We combine data and context to paint the whole picture for our clients, around t"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46006",
    "title": "Product Manager - Front to Back Operating Model - Buyside Post Trade",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Product-Manager-Front-to-Back-Operating-Model-Buyside-Post-Trade/46006",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:27.232965+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Powered by an unparalleled combination of automation, innovation, access and service, Bloomberg’s comprehensive and integrated enterprise solutions help "
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46004",
    "title": "Bloomberg Intelligence - Banks Equity Research Associate",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Bloomberg-Intelligence-Banks-Equity-Research-Associate/46004",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:27.232965+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg Intelligence (BI) delivers independent, data-driven research and interactive datasets integrated into the Bloomberg Terminal, helping investmen"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45985",
    "title": "Streaming Transmissions Operator",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Streaming-Transmissions-Operator/45985",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:27.232965+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg LP has built a significant global media business across television, digital, magazine, radio, and live event platforms. Amid a transformative p"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 64
- HTTP requests/cumulative request time: 604 / 112.679s
- Company elapsed time: 194.846s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 540 / 0 / 0
- Detail cache statuses: {'fetched:new': 520, 'fetched:missing_detail': 20}
- Relevant JD recovery: {'eligible': 117, 'usable_jd': 117}
- Raw jobs found: 1265
- After US/location filtering: 540
- With trustworthy posted_date: 540
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.647, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 13.335, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.776, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.653, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.58, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.196, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.889, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.63, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.223, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 13.133, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "full stack", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.744, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "python react", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.582, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "pyspark databricks", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 6.556, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "experienced software engineer java python", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 8.69, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "agentic ai", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.721, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.686, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "software engineer ii", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.585, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.197, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "security engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.753, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "quantitative developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.835, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "software engineer java spring", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.58, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 1, "pages_fetched": 1, "query": "software engineer python authe", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.099, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "aws data platform engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.304, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data engineer applied ai", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 3.45, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 1, "pages_fetched": 1, "query": "asset management technology", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 20}

Sample normalized records:

```json
[
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210782895",
    "title": "Senior Lead Software Engineer - Data & AI Platform Engineer",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210782895",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:50.156780+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Senior Lead Software Engineer at JPMorgan Chase, within"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210787977",
    "title": "Senior Lead Software Engineer - AI Engineer",
    "location": "Plano, TX, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210787977",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:50.156780+00:00",
    "date_confidence": "high",
    "description": "Be an integral part of an agile team that's constantly pushing the envelope to enhance, build, and deliver top-notch technology products. As a Senior Lead Software Engineer at JPMo"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210775122",
    "title": "Lead Software Engineer - Java, React, AWS and AI",
    "location": "Columbus, OH, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210775122",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:50.156780+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorganChase within the Corp"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210771550",
    "title": "AI Lead Software Engineer - Java",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210771550",
    "posted_date": "2026-08-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:50.156780+00:00",
    "date_confidence": "high",
    "description": "We have an exciting opportunity to advance your career and drive meaningful impact by pushing the limits of modern engineering. As a Lead Software Engineer at JPMorganChase within "
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210770122",
    "title": "Senior Lead Software Engineer - Java or Python, Agentic AI",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210770122",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:33:50.156780+00:00",
    "date_confidence": "high",
    "description": "As a Senior Lead Software Engineer at JPMorgan Chase within the Commercial & Investment Bank Digital Channel's team, you will build autonomous agent capabilities that can plan, exe"
  }
]
```

## Capital One

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://capitalone.wd12.myworkdayjobs.com/Capital_One`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 169 / 56.763s
- Company elapsed time: 80.904s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 141 / 0 / 0
- Detail cache statuses: {'fetched:new': 131, 'fetched:missing_detail': 10}
- Relevant JD recovery: {'eligible': 42, 'usable_jd': 42}
- Raw jobs found: 526
- After US/location filtering: 141
- With trustworthy posted_date: 141
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 36.367, "first_pass_survivors": 74, "group": "official", "jds_resolved": 74, "original_postings_resolved": 74, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 74, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 12.175, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.834, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.036, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.282, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.574, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.595, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.435, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 5.276, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005300",
    "title": "Full-stack Engineer 4",
    "location": "Plano, TX",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Plano-TX/Full-stack-Engineer-4_R1005300-2",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:03.825067+00:00",
    "date_confidence": "high",
    "description": "Full-stack Engineer 4 Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclusive and iter"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005163",
    "title": "Full-stack Engineer 4",
    "location": "Plano, TX",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Plano-TX/Full-stack-Engineer-4_R1005163-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:03.825067+00:00",
    "date_confidence": "high",
    "description": "Full-stack Engineer 4 Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclusive and iter"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005337",
    "title": "Senior Director, AI Engineering -Agentic AI Platform(Remote Eligible)",
    "location": "San Jose, CA; San Francisco, CA; US Remote; McLean, VA; Cambridge, MA; New York, NY",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/San-Jose-CA/Senior-Director--AI-Engineering--Agentic-AI-Platform-Remote-Eligible-_R1005337-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:03.825067+00:00",
    "date_confidence": "high",
    "description": "Senior Director, AI Engineering -Agentic AI Platform(Remote Eligible) At Capital One, we are creating responsible and reliable AI systems, changing banking for good. For years, Cap"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1004141",
    "title": "Data Engineer 4 (Manager, IC)",
    "location": "Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Richmond-VA/Data-Engineer-4--Manager--IC-_R1004141-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:03.825067+00:00",
    "date_confidence": "high",
    "description": "Data Engineer 4 (Manager, IC) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclusive "
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005326",
    "title": "Director, Global Enterprise Communications - AI, Cybersecurity, Open Source, Ventures",
    "location": "McLean, VA; Plano, TX; Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Director--Global-Enterprise-Communications---AI--Cybersecurity--Open-Source--Ventures_R1005326-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:03.825067+00:00",
    "date_confidence": "high",
    "description": "Director, Global Enterprise Communications - AI, Cybersecurity, Open Source, Ventures Director, Global Enterprise Communications - AI, Cybersecurity, Open Source, Ventures The full"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 41
- HTTP requests/cumulative request time: 469 / 150.245s
- Company elapsed time: 213.838s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 428 / 0 / 0
- Detail cache statuses: {'fetched:new': 418, 'fetched:missing_detail': 10}
- Relevant JD recovery: {'eligible': 53, 'usable_jd': 53}
- Raw jobs found: 817
- After US/location filtering: 428
- With trustworthy posted_date: 428
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 26.204, "first_pass_survivors": 66, "group": "official", "jds_resolved": 66, "original_postings_resolved": 66, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 66, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 21.216, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.127, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 20.303, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 24.67, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 19.477, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.692, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.276, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 17.4, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 17.336, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "core infrastructure", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.966, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "cleared site reliability engineer database", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.494, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "software developer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 9.676, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "applications developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "348534",
    "title": "AI Systems Engineer (OCI/AI Infrastructure)",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/348534",
    "posted_date": "2026-10-22",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:34.851059+00:00",
    "date_confidence": "high",
    "description": "Oracle Hardware Platform Development Engineering is seeking a highly driven AI Systems Engineer to evaluate and characterize next-generation GPU and AI accelerator platforms for Or"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "348975",
    "title": "Principal AI Agent / Software Engineer- Nashville",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/348975",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:34.851059+00:00",
    "date_confidence": "high",
    "description": "This role in onsite in Nashville, TN. The Principal AI Agent / Software Engineer is a Senior Staff-level, hands-on technical leadership role responsible for defining, building, and"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "341967",
    "title": "Senior AI Agent Engineer",
    "location": "United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/341967",
    "posted_date": "2026-08-12",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:34.851059+00:00",
    "date_confidence": "high",
    "description": "Oracle Health is seeking a Senior AI Agent Engineer to build production AI agents and workflow automation capabilities that accelerate analytics delivery, improve insight generatio"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "347549",
    "title": "Senior AI Agent Engineer",
    "location": "United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/347549",
    "posted_date": "2026-10-13",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:34.851059+00:00",
    "date_confidence": "high",
    "description": "Oracle Health is seeking a Senior AI Agent Engineer to build production AI agents and workflow automation capabilities that accelerate analytics delivery, improve insight generatio"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "342714",
    "title": "Principal Platform Software Engineer, AI",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/342714",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:34:34.851059+00:00",
    "date_confidence": "high",
    "description": "Oracle Cloud Infrastructure’s (OCI) Developer Platform Builder Tools organization builds the next generation of developer productivity platforms, intelligent development workflows,"
  }
]
```

## Walmart Global Tech

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://walmart.wd504.myworkdayjobs.com/WalmartExternal`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 28
- HTTP requests/cumulative request time: 384 / 218.005s
- Company elapsed time: 269.667s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 355 / 0 / 0
- Detail cache statuses: {'fetched:new': 326, 'fetched:missing_detail': 29}
- Relevant JD recovery: {'eligible': 53, 'usable_jd': 53}
- Raw jobs found: 544
- After US/location filtering: 355
- With trustworthy posted_date: 355
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 62.185, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 28.5, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 36.86, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 30.919, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 24.203, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 28.849, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 21.753, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.684, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 21.897, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 7.811, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "usa software engineer ii", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 20}

Sample normalized records:

```json
[
  {
    "company": "Walmart Global Tech",
    "source": "walmart_global_tech_official_careers",
    "job_id": "R-2451270",
    "title": "Distinguished, Software Engineer -AI/ML Engineer – Agentic Systems",
    "location": "(USA) Crossman Excellence Building CA SUNNYVALE Home Office",
    "official_url": "https://walmart.wd504.myworkdayjobs.com/WalmartExternal/job/USA-Crossman-Excellence-Building-CA-SUNNYVALE-Home-Office/Distinguished--Software-Engineer--AI-ML-Engineer---Agentic-Systems_R-2451270-1",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:35:24.730339+00:00",
    "date_confidence": "high",
    "description": "Position Summary... What you'll do... As a Distinguished AI/ML Engineer within Walmart Global Tech’s Reliability Engineering Organization , you will lead the technical development "
  },
  {
    "company": "Walmart Global Tech",
    "source": "walmart_global_tech_official_careers",
    "job_id": "R-2599274",
    "title": "Group Director, Software Engineering - Applied AI",
    "location": "(USA) Crossman Respect Building CA SUNNYVALE Home Office; (USA) Purpose Building AR Bentonville Home Office",
    "official_url": "https://walmart.wd504.myworkdayjobs.com/WalmartExternal/job/USA-Crossman-Respect-Building-CA-SUNNYVALE-Home-Office/Group-Director--Software-Engineering---Applied-AI_R-2599274",
    "posted_date": "2026-08-10",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:35:24.730339+00:00",
    "date_confidence": "high",
    "description": "Position Summary... What you'll do... Role summary: As the Group Director, Applied AI & Engineering you will lead an elite, high-caliber applied AI and engineering team dedicated t"
  },
  {
    "company": "Walmart Global Tech",
    "source": "walmart_global_tech_official_careers",
    "job_id": "R-2533229",
    "title": "(USA) Distinguished, Software Engineer-AI/ML Engineer - Agentic Systems & Site Reliability Engineering",
    "location": "(USA) Crossman Excellence Building CA SUNNYVALE Home Office",
    "official_url": "https://walmart.wd504.myworkdayjobs.com/WalmartExternal/job/USA-Crossman-Excellence-Building-CA-SUNNYVALE-Home-Office/XMLNAME--USA--Distinguished--Software-Engineer-AI-ML-Engineer---Agentic-Systems---Site-Reliability-Engineering_R-2533229-1",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:35:24.730339+00:00",
    "date_confidence": "high",
    "description": "Position Summary... As a Distinguished AI/ML Engineer within Walmart Global Tech's Site Reliability Engineering organization, you will lead the technical development of next-genera"
  },
  {
    "company": "Walmart Global Tech",
    "source": "walmart_global_tech_official_careers",
    "job_id": "R-2613286",
    "title": "(USA) Distinguished, Data Scientist - Agentic AI Systems Engineering & Model Post-Training",
    "location": "(USA) Supply Chain Optimization AR Bentonville Home Office",
    "official_url": "https://walmart.wd504.myworkdayjobs.com/WalmartExternal/job/USA-Supply-Chain-Optimization-AR-Bentonville-Home-Office/XMLNAME--USA--Distinguished--Data-Scientist---Agentic-AI-Systems-Engineering---Model-Post-Training_R-2613286",
    "posted_date": "2026-08-20",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:35:24.730339+00:00",
    "date_confidence": "high",
    "description": "Position Summary... What you'll do... The Opportunity: Walmart’s Supply Chain AI Lab & Innovation Factory is building a new generation of production-grade agentic AI systems that r"
  },
  {
    "company": "Walmart Global Tech",
    "source": "walmart_global_tech_official_careers",
    "job_id": "R-2699225",
    "title": "(USA) Principal Software Engineer",
    "location": "Sunnyvale, CA; Bellevue, WA; Bentonville, AR; Hoboken, NJ",
    "official_url": "https://walmart.wd504.myworkdayjobs.com/WalmartExternal/job/Sunnyvale-CA/XMLNAME--USA--Principal-Software-Engineer_R-2699225",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:35:24.730339+00:00",
    "date_confidence": "high",
    "description": "Position Summary... What you'll do... Role Summary As a Principal Software Engineer in Walmart Global Tech's Growth Technology organization, you'll tackle engineering challenges at"
  }
]
```

## Cloudflare

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/cloudflare/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.458s
- Company elapsed time: 1.550s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 91, 'usable_jd': 91}
- Raw jobs found: 462
- After US/location filtering: 459
- With trustworthy posted_date: 459
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "7695702",
    "title": "Account Executive, FedCiv",
    "location": "Hybrid; Washington, DC, United States",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/7695702?gh_jid=7695702",
    "posted_date": "2026-03-09",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:36:59.843608+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "8172582",
    "title": "Account Executive, Indonesia",
    "location": "Hybrid; Singapore",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/8172582?gh_jid=8172582",
    "posted_date": "2026-09-07",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:36:59.843608+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "8097321",
    "title": "AI Security Research & Red Team Engineer",
    "location": "Hybrid; Austin, TX, United States; New York, New York, United States",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/8097321?gh_jid=8097321",
    "posted_date": "2026-08-10",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:36:59.843608+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "8287256",
    "title": "Associate, Strategic Finance & Investor Relations",
    "location": "Hybrid; San Francisco, CA, United States",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/8287256?gh_jid=8287256",
    "posted_date": "2026-10-19",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:36:59.843608+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "8288902",
    "title": "Business Development Representative",
    "location": "Hybrid; Dubai, Dubai, United Arab Emirates",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/8288902?gh_jid=8288902",
    "posted_date": "2026-10-16",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:36:59.843608+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  }
]
```

## Stripe

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/stripe/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.355s
- Company elapsed time: 1.073s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 149, 'usable_jd': 149}
- Raw jobs found: 767
- After US/location filtering: 419
- With trustworthy posted_date: 419
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8172510",
    "title": "Abuse Investigator",
    "location": "Seattle, San Francisco, New York City; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8172510",
    "posted_date": "2026-09-09",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:37:01.394836+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>Who we are </strong></h2> <h3><strong>About Stripe</strong></h3> <p><span style=\"font-weight: 400;\">Stripe is a financial infrastructure platform for businesses. Millio"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8138044",
    "title": "Account Executive, AI Sales",
    "location": "San Francisco, CA; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8138044",
    "posted_date": "2026-09-18",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:37:01.394836+00:00",
    "date_confidence": "high",
    "description": "<div class=\"JobPostPage-content ⚙ ⚙1opjj73\"> <h3 id=\"about-stripe\">About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies - from t"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8238731",
    "title": "Account Executive, AI Startups - Grower",
    "location": "San Francisco; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8238731",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:37:01.394836+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s largest enterprises to the most am"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8215824",
    "title": "Account Executive - Bridge",
    "location": "SF, NYC, CHI, ATL, SEA; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8215824",
    "posted_date": "2026-10-15",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:37:01.394836+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies - from the world’s largest enterprises to the most "
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8077887",
    "title": "Account Executive, Bridge",
    "location": "SF, NYC, SEA, CHI; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8077887",
    "posted_date": "2026-07-22",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:37:01.394836+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>Who we are </strong></h2> <h3><strong>About Stripe</strong></h3> <p><span style=\"font-weight: 400;\">Stripe is a financial infrastructure platform for businesses. Millio"
  }
]
```

## Coinbase

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/coinbase/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.207s
- Company elapsed time: 0.670s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 53, 'usable_jd': 53}
- Raw jobs found: 277
- After US/location filtering: 201
- With trustworthy posted_date: 201
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8175363",
    "title": "Acceleration Programs Intern",
    "location": "Hybrid - New York, NY; US - Remote Zone 1 (Job Requisitions Only)",
    "official_url": "https://www.coinbase.com/careers/positions/8175363?gh_jid=8175363",
    "posted_date": "2026-09-08",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:37:02.469207+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? At&nbsp;<a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sou"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8173991",
    "title": "Accounting Intern",
    "location": "Hybrid - New York, NY; US - Remote Zone 1 (Job Requisitions Only)",
    "official_url": "https://www.coinbase.com/careers/positions/8173991?gh_jid=8173991",
    "posted_date": "2026-09-08",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:37:02.469207+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? At&nbsp;<a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sou"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8093264",
    "title": "Accounting Manager, GL Operations & Intercompany",
    "location": "Remote - USA; US - Remote Zone 1 (Job Requisitions Only)",
    "official_url": "https://www.coinbase.com/careers/positions/8093264?gh_jid=8093264",
    "posted_date": "2026-07-28",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:37:02.469207+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? At&nbsp;<a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sou"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "7532645",
    "title": "Accounting Manager, Lending & Credit Products",
    "location": "Remote - USA; US - Remote Zone 1 (Job Requisitions Only)",
    "official_url": "https://www.coinbase.com/careers/positions/7532645?gh_jid=7532645",
    "posted_date": "2026-01-12",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:37:02.469207+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? At&nbsp;<a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sou"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8164862",
    "title": "Accounting Manager, Tokenized Equities",
    "location": "Remote - Abu Dhabi; Remote - United Arab Emirates",
    "official_url": "https://www.coinbase.com/careers/positions/8164862?gh_jid=8164862",
    "posted_date": "2026-08-28",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:37:02.469207+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? At&nbsp;<a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sou"
  }
]
```

## Robinhood

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/robinhood/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.160s
- Company elapsed time: 0.592s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 41, 'usable_jd': 41}
- Raw jobs found: 153
- After US/location filtering: 144
- With trustworthy posted_date: 144
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "6669758",
    "title": "Android Engineer, Government Products",
    "location": "New York, NY; Menlo Park, CA",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/6669758?t=gh_src=&gh_jid=6669758",
    "posted_date": "2025-05-08",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-11-06T00:37:03.140353+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "7350823",
    "title": "Android Engineer, Money Experience",
    "location": "Menlo Park, CA",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/7350823?t=gh_src=&gh_jid=7350823",
    "posted_date": "2025-10-22",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-11-06T00:37:03.140353+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8202874",
    "title": "Android Engineer, Social",
    "location": "Menlo Park, CA; New York, NY; Menlo Park, CA",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8202874?t=gh_src=&gh_jid=8202874",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-25",
    "fetched_at": "2026-11-06T00:37:03.140353+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8174853",
    "title": "Brokerage Communications Specialist",
    "location": "Chicago, IL; Denver, CO; Lake Mary, FL; New York, NY; Chicago, IL; Denver, CO; Lake Mary, FL; New York, NY",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8174853?t=gh_src=&gh_jid=8174853",
    "posted_date": "2026-09-28",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:37:03.140353+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8262110",
    "title": "Cashiering Support Associate",
    "location": "Clearwater, FL; Westlake, TX; Clearwater, FL; Westlake, TX",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8262110?t=gh_src=&gh_jid=8262110",
    "posted_date": "2026-10-07",
    "updated_date": "2026-10-20",
    "fetched_at": "2026-11-06T00:37:03.140353+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  }
]
```

## Figma

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/figma/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.230s
- Company elapsed time: 0.503s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 143
- After US/location filtering: 93
- With trustworthy posted_date: 93
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Figma",
    "source": "figma_official_careers",
    "job_id": "5426468004",
    "title": "Account Executive, Enterprise",
    "location": "San Francisco, CA • New York, NY • United States; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/5426468004?gh_jid=5426468004",
    "posted_date": "2025-01-28",
    "updated_date": "2026-10-27",
    "fetched_at": "2026-11-06T00:37:03.733701+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all. Figma’s platform helps teams bring ideas"
  },
  {
    "company": "Figma",
    "source": "figma_official_careers",
    "job_id": "6230952004",
    "title": "Account Executive, Public Sector - State & Local",
    "location": "San Francisco, CA; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/6230952004?gh_jid=6230952004",
    "posted_date": "2026-10-22",
    "updated_date": "2026-10-28",
    "fetched_at": "2026-11-06T00:37:03.733701+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all. Figma’s platform helps teams bring ideas"
  },
  {
    "company": "Figma",
    "source": "figma_official_careers",
    "job_id": "5694259004",
    "title": "Account Executive, SMB",
    "location": "San Francisco, CA • New York, NY; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/5694259004?gh_jid=5694259004",
    "posted_date": "2025-11-01",
    "updated_date": "2026-10-27",
    "fetched_at": "2026-11-06T00:37:03.733701+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all. Figma’s platform helps teams bring ideas"
  },
  {
    "company": "Figma",
    "source": "figma_official_careers",
    "job_id": "5558737004",
    "title": "Account Executive, Strategic",
    "location": "San Francisco, CA • New York, NY • United States; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/5558737004?gh_jid=5558737004",
    "posted_date": "2025-06-16",
    "updated_date": "2026-10-27",
    "fetched_at": "2026-11-06T00:37:03.733701+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all. Figma’s platform helps teams bring ideas"
  },
  {
    "company": "Figma",
    "source": "figma_official_careers",
    "job_id": "5707966004",
    "title": "AI Applied Scientist",
    "location": "San Francisco, CA • New York, NY • United States; Canada; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/5707966004?gh_jid=5707966004",
    "posted_date": "2025-12-17",
    "updated_date": "2026-10-27",
    "fetched_at": "2026-11-06T00:37:03.733701+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all. Figma’s platform helps teams bring ideas"
  }
]
```

## GitLab

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/gitlab/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.339s
- Company elapsed time: 0.799s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 16, 'usable_jd': 16}
- Raw jobs found: 248
- After US/location filtering: 139
- With trustworthy posted_date: 139
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8638232002",
    "title": "AI Transformation Owner, CRO",
    "location": "Remote, United States; United States of America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8638232002",
    "posted_date": "2026-07-22",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:37:04.237593+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8923757002",
    "title": "Associate Renewals Manager - France",
    "location": "Remote; France",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8923757002",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:37:04.237593+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8857185002",
    "title": "Associate Renewals Manager, SMB",
    "location": "Remote, Canada; Remote, United States; North America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8857185002",
    "posted_date": "2026-09-29",
    "updated_date": "2026-10-28",
    "fetched_at": "2026-11-06T00:37:04.237593+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8771512002",
    "title": "Backend Engineer, GitLab Orbit",
    "location": "Remote, Canada; Remote, United States; North America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8771512002",
    "posted_date": "2026-10-23",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:37:04.237593+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8532272002",
    "title": "Business Development Representative",
    "location": "Remote, North America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8532272002",
    "posted_date": "2026-05-01",
    "updated_date": "2026-10-28",
    "fetched_at": "2026-11-06T00:37:04.237593+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  }
]
```

## Discord

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/discord/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.128s
- Company elapsed time: 0.209s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 26
- After US/location filtering: 26
- With trustworthy posted_date: 26
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8917177002",
    "title": "Associate Commercial Counsel",
    "location": "San Francisco Bay Area or Remote (U.S.); San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8917177002",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:37:05.034079+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8722538002",
    "title": "Engineering Manager, Machine Learning (Safety)",
    "location": "Remote (US)",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8722538002",
    "posted_date": "2026-08-20",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:37:05.034079+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8649856002",
    "title": "Engineering Manager, Platform Security",
    "location": "Remote (West Coast); Remote (US)",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8649856002",
    "posted_date": "2026-07-27",
    "updated_date": "2026-10-21",
    "fetched_at": "2026-11-06T00:37:05.034079+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8847080002",
    "title": "Group Product Manager, Data/ML",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8847080002",
    "posted_date": "2026-10-23",
    "updated_date": "2026-10-23",
    "fetched_at": "2026-11-06T00:37:05.034079+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8771059002",
    "title": "Program Manager, Fraud and Payments Risk",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8771059002",
    "posted_date": "2026-09-03",
    "updated_date": "2026-10-21",
    "fetched_at": "2026-11-06T00:37:05.034079+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  }
]
```

## Asana

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/asana/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.222s
- Company elapsed time: 0.465s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 14, 'usable_jd': 14}
- Raw jobs found: 110
- After US/location filtering: 76
- With trustworthy posted_date: 76
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8194380",
    "title": "AI GTM Account Executive",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://www.asana.com/jobs/apply/8194380?gh_jid=8194380",
    "posted_date": "2026-10-07",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:37:05.037316+00:00",
    "date_confidence": "high",
    "description": "<p id=\"p-rc_e5a03211173e7566-174\" data-path-to-node=\"0\"><span data-path-to-node=\"0,0\">We're looking for a commercially driven, AI-fluent sales professional to join Asana's AI GTM A"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8092044",
    "title": "Analytical Engineer",
    "location": "Warsaw; Warszawa, Masovian Voivodeship, Poland",
    "official_url": "https://www.asana.com/jobs/apply/8092044?gh_jid=8092044",
    "posted_date": "2026-07-30",
    "updated_date": "2026-09-15",
    "fetched_at": "2026-11-06T00:37:05.037316+00:00",
    "date_confidence": "high",
    "description": "<p>The Data Science &amp; Analytics team at Asana is how the company turns data into decisions — defining the questions that matter, surfacing the answers, and making sure insight "
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8221174",
    "title": "API Support Engineer",
    "location": "Warsaw; Warszawa, Masovian Voivodeship, Poland",
    "official_url": "https://www.asana.com/jobs/apply/8221174?gh_jid=8221174",
    "posted_date": "2026-10-07",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:37:05.037316+00:00",
    "date_confidence": "high",
    "description": "<p>As a Developer Support Engineer, you’ll be a trusted technical partner for developers and customers integrating with the Asana platform. You’ll focus on API-related troubleshoot"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "7964297",
    "title": "Backend Software Engineer",
    "location": "Reykjavík; Reykjavík, Reykjavík, Iceland",
    "official_url": "https://www.asana.com/jobs/apply/7964297?gh_jid=7964297",
    "posted_date": "2026-07-22",
    "updated_date": "2026-09-15",
    "fetched_at": "2026-11-06T00:37:05.037316+00:00",
    "date_confidence": "high",
    "description": "<p>We’re looking for an experienced backend engineer with a passion for learning and working on systems. You will work with a world-class team of engineers on deploying and operati"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8137748",
    "title": "Benefits Manager, NAMER",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://www.asana.com/jobs/apply/8137748?gh_jid=8137748",
    "posted_date": "2026-08-31",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:37:05.037316+00:00",
    "date_confidence": "high",
    "description": "<p id=\"p-rc_10838ec6a95bc2d4-72\" data-path-to-node=\"3\"><span data-path-to-node=\"3,0\">We are looking for a detail-oriented, strategic team player to join as a Benefits Manager on As"
  }
]
```

## Brex

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/brex/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.334s
- Company elapsed time: 0.912s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 42, 'usable_jd': 42}
- Raw jobs found: 274
- After US/location filtering: 261
- With trustworthy posted_date: 261
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8912605002",
    "title": "Accountant Partnerships Manager",
    "location": "San Francisco, California, United States; New York, New York, United States",
    "official_url": "https://www.brex.com/careers/8912605002?gh_jid=8912605002",
    "posted_date": "2026-10-23",
    "updated_date": "2026-10-23",
    "fetched_at": "2026-11-06T00:37:05.220767+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8912603002",
    "title": "Accountant Partnerships Manager",
    "location": "New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8912603002?gh_jid=8912603002",
    "posted_date": "2026-10-23",
    "updated_date": "2026-10-23",
    "fetched_at": "2026-11-06T00:37:05.220767+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8688112002",
    "title": "Account Executive, Small Business",
    "location": "Salt Lake City, Utah, United States; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8688112002?gh_jid=8688112002",
    "posted_date": "2026-08-06",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:37:05.220767+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8686667002",
    "title": "Account Executive, Small Business",
    "location": "San Francisco, California, United States; New York, New York, United States; Salt Lake City, Utah, United States",
    "official_url": "https://www.brex.com/careers/8686667002?gh_jid=8686667002",
    "posted_date": "2026-08-06",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:37:05.220767+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8688110002",
    "title": "Account Executive, Small Business",
    "location": "New York, New York, United States; Salt Lake City, Utah, United States; San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8688110002?gh_jid=8688110002",
    "posted_date": "2026-08-06",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:37:05.220767+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  }
]
```

## Samsara

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/samsara/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.808s
- Company elapsed time: 1.725s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 60, 'usable_jd': 60}
- Raw jobs found: 306
- After US/location filtering: 264
- With trustworthy posted_date: 264
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8207928",
    "title": "Account Development Representative - Canada",
    "location": "Remote - Quebec; Remote - Toronto",
    "official_url": "https://www.samsara.com/company/careers/roles/8207928?gh_jid=8207928",
    "posted_date": "2026-09-17",
    "updated_date": "2026-11-01",
    "fetched_at": "2026-11-06T00:37:05.503728+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8332753",
    "title": "Account Development Representative - Canada",
    "location": "Remote - Quebec; Remote - Toronto",
    "official_url": "https://www.samsara.com/company/careers/roles/8332753?gh_jid=8332753",
    "posted_date": "2026-10-28",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:37:05.503728+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8094367",
    "title": "Account Development Representative II",
    "location": "Atlanta, Georgia, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8094367?gh_jid=8094367",
    "posted_date": "2026-08-12",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:37:05.503728+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8325352",
    "title": "Account Development Representative II - Atlanta",
    "location": "Atlanta, Georgia, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8325352?gh_jid=8325352",
    "posted_date": "2026-10-26",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:37:05.503728+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8325046",
    "title": "Account Development Representative II - Atlanta",
    "location": "Remote - GA; Atlanta, Georgia, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8325046?gh_jid=8325046",
    "posted_date": "2026-10-26",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:37:05.503728+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  }
]
```

## Lyft

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/lyft/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 1.099s
- Company elapsed time: 1.305s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 168
- After US/location filtering: 93
- With trustworthy posted_date: 93
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8927798002",
    "title": "Accountant, Lease & Fleet",
    "location": "New York, NY; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8927798002?gh_jid=8927798002",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:37:06.134171+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8927794002",
    "title": "Accountant, Lease & Fleet",
    "location": "San Francisco, CA; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8927794002?gh_jid=8927794002",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:37:06.134171+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8503985002",
    "title": "Analytics Lead, Market Insights",
    "location": "San Francisco, CA; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8503985002?gh_jid=8503985002",
    "posted_date": "2026-04-14",
    "updated_date": "2026-10-19",
    "fetched_at": "2026-11-06T00:37:06.134171+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8843341002",
    "title": "Applied Scientist Intern, PhD (Summer 2027)",
    "location": "San Francisco, CA; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8843341002?gh_jid=8843341002",
    "posted_date": "2026-09-28",
    "updated_date": "2026-10-19",
    "fetched_at": "2026-11-06T00:37:06.134171+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8927242002",
    "title": "Associate Account Manager",
    "location": "New York, NY; New York, New York, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8927242002?gh_jid=8927242002",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:37:06.134171+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  }
]
```

## Spotify

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/spotify`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.679s
- Company elapsed time: 0.768s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 13, 'usable_jd': 13}
- Raw jobs found: 86
- After US/location filtering: 63
- With trustworthy posted_date: 63
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "2a55d6c9-c564-443a-be3e-a3851db5a93b",
    "title": "Account Executive - Commercial, Spotify Technology",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/2a55d6c9-c564-443a-be3e-a3851db5a93b",
    "posted_date": "2026-10-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.232125+00:00",
    "date_confidence": "high",
    "description": "• Identify and pursue new business opportunities with companies of fewer than 1,000 employees. While significant inbound demand supports the pipeline, top performers will exceed ta"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "cf13d272-92ac-407d-89bf-7f20d20f7961",
    "title": "Account Executive - Enterprise, Spotify Technology",
    "location": "New York, NY; San Francisco, CA",
    "official_url": "https://jobs.lever.co/spotify/cf13d272-92ac-407d-89bf-7f20d20f7961",
    "posted_date": "2026-10-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.232125+00:00",
    "date_confidence": "high",
    "description": "• Identify and pursue new business opportunities with organizations of 1,000+ employees. This is a “Hunter” role with significant inbound and SDR support. • Research and prospect i"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "d87833d0-fb78-4794-b45d-3fe5c8274bc8",
    "title": "Artist & Label Partnerships Contractor, Vietnam",
    "location": "Ho Chi Minh",
    "official_url": "https://jobs.lever.co/spotify/d87833d0-fb78-4794-b45d-3fe5c8274bc8",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.232125+00:00",
    "date_confidence": "high",
    "description": "Maintain positive partnerships across artist and label communities within Vietnam. Support our key partners in Vietnam on Spotify tools, resources and insights. Work closely with o"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "785989a6-b219-43b1-92d9-750a67054f24",
    "title": "AV Engineer - Platform",
    "location": "Stockholm",
    "official_url": "https://jobs.lever.co/spotify/785989a6-b219-43b1-92d9-750a67054f24",
    "posted_date": "2026-10-09",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.232125+00:00",
    "date_confidence": "high",
    "description": "Own the AV experience across EMEA, including meeting rooms, boardrooms, common areas, labs, lounges, and digital signage. Provide thoughtful, high-quality AV support for executive "
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "186b763a-2a61-4563-8813-ff6b40c9c8a7",
    "title": "Backend Engineer - Data Platform",
    "location": "Stockholm; London",
    "official_url": "https://jobs.lever.co/spotify/186b763a-2a61-4563-8813-ff6b40c9c8a7",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.232125+00:00",
    "date_confidence": "high",
    "description": "Build and Evolve Core Services: Design, build and operate the backend services and APIs behind our data catalog, lineage and publishing systems, and evolve them as the platform ado"
  }
]
```

## Ramp

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/ramp`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.150s
- Company elapsed time: 0.416s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 61, 'usable_jd': 61}
- Raw jobs found: 171
- After US/location filtering: 154
- With trustworthy posted_date: 154
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "34413f8d-26bf-4bbc-8ade-eb309a0e2245",
    "title": "Security Engineer, Cloud",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote (Canada); Remote (US); Miami, FL",
    "official_url": "https://jobs.ashbyhq.com/ramp/34413f8d-26bf-4bbc-8ade-eb309a0e2245",
    "posted_date": "2026-04-07",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.440332+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $275B in annualized"
  },
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "f564dcf9-9390-4a3f-896f-8047a5086040",
    "title": "Mobile Engineer, Android",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote (Canada); San Francisco, CA; Remote (US)",
    "official_url": "https://jobs.ashbyhq.com/ramp/f564dcf9-9390-4a3f-896f-8047a5086040",
    "posted_date": "2025-07-31",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.440332+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $275B in annualized"
  },
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "707d5f91-bcf7-42b2-a0e6-8130bf13e56b",
    "title": "Account Executive | Strategic",
    "location": "San Francisco, CA; San Fransisco, California, USA; Remote, USA",
    "official_url": "https://jobs.ashbyhq.com/ramp/707d5f91-bcf7-42b2-a0e6-8130bf13e56b",
    "posted_date": "2026-08-11",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.440332+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $275B in annualized"
  },
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "4859cd5e-f2a9-44d7-81f7-8bfc0e62369f",
    "title": "Mobile Engineer, iOS",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote (Canada); San Francisco, CA; Remote (US)",
    "official_url": "https://jobs.ashbyhq.com/ramp/4859cd5e-f2a9-44d7-81f7-8bfc0e62369f",
    "posted_date": "2025-07-31",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.440332+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $275B in annualized"
  },
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "b55447c0-4adc-42eb-9ca2-f88fd44e0e5b",
    "title": "Partner Development Representative | Accounting",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote (US)",
    "official_url": "https://jobs.ashbyhq.com/ramp/b55447c0-4adc-42eb-9ca2-f88fd44e0e5b",
    "posted_date": "2026-09-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.440332+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $275B in annualized"
  }
]
```

## Notion

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/notion`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.171s
- Company elapsed time: 0.346s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 35, 'usable_jd': 35}
- Raw jobs found: 150
- After US/location filtering: 76
- With trustworthy posted_date: 76
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Notion",
    "source": "notion_official_careers",
    "job_id": "1fc309c8-da20-4ff2-84c7-8b863ece2b0a",
    "title": "Software Engineer, AI Connections (Developer Platform)",
    "location": "San Francisco, California; San Francisco, California, United States; New York, New York; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/notion/1fc309c8-da20-4ff2-84c7-8b863ece2b0a",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.857694+00:00",
    "date_confidence": "high",
    "description": "WHO WE ARE Notion is the collaborative AI workspace where teams and agents think together https://www.youtube.com/watch?v=vkpYpWfEK5s. We're building one place where your knowledge"
  },
  {
    "company": "Notion",
    "source": "notion_official_careers",
    "job_id": "05e14247-17c4-4e98-9a13-53828a4e2f13",
    "title": "Business Development Representative, New York",
    "location": "New York, New York; New York, New York, United States; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/notion/05e14247-17c4-4e98-9a13-53828a4e2f13",
    "posted_date": "2026-04-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.857694+00:00",
    "date_confidence": "high",
    "description": "WHO WE ARE Notion is the collaborative AI workspace where teams and agents think together https://www.youtube.com/watch?v=vkpYpWfEK5s. We're building one place where your knowledge"
  },
  {
    "company": "Notion",
    "source": "notion_official_careers",
    "job_id": "b21fef72-4864-4a3e-a627-91557a0f8a36",
    "title": "Business Development Representative, San Francisco",
    "location": "San Francisco, California; San Francisco, California, United States; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/notion/b21fef72-4864-4a3e-a627-91557a0f8a36",
    "posted_date": "2026-04-01",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.857694+00:00",
    "date_confidence": "high",
    "description": "WHO WE ARE Notion is the collaborative AI workspace where teams and agents think together https://www.youtube.com/watch?v=vkpYpWfEK5s. We're building one place where your knowledge"
  },
  {
    "company": "Notion",
    "source": "notion_official_careers",
    "job_id": "10437426-14c8-4c45-8075-67959ce80393",
    "title": "Forward Deployed Engineer, GTM, AMER",
    "location": "San Francisco, California; San Francisco, California, United States; New York, New York; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/notion/10437426-14c8-4c45-8075-67959ce80393",
    "posted_date": "2025-08-07",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.857694+00:00",
    "date_confidence": "high",
    "description": "WHO WE ARE Notion is the collaborative AI workspace where teams and agents think together https://www.youtube.com/watch?v=vkpYpWfEK5s. We're building one place where your knowledge"
  },
  {
    "company": "Notion",
    "source": "notion_official_careers",
    "job_id": "d02d5ff4-fea3-4be8-b142-cb120e966399",
    "title": "Manager, Sales Development",
    "location": "New York, New York; New York, New York, United States; San Francisco, California; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/notion/d02d5ff4-fea3-4be8-b142-cb120e966399",
    "posted_date": "2026-10-13",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:07.857694+00:00",
    "date_confidence": "high",
    "description": "WHO WE ARE Notion is the collaborative AI workspace where teams and agents think together https://www.youtube.com/watch?v=vkpYpWfEK5s. We're building one place where your knowledge"
  }
]
```

## Linear

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/linear`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.208s
- Company elapsed time: 0.241s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 31
- After US/location filtering: 24
- With trustworthy posted_date: 24
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Linear",
    "source": "linear_official_careers",
    "job_id": "d3bc1ced-3ce4-4086-a050-555055dbb1ff",
    "title": "Senior / Staff Fullstack Engineer",
    "location": "Europe; European Union; Remote, European Union",
    "official_url": "https://jobs.ashbyhq.com/linear/d3bc1ced-3ce4-4086-a050-555055dbb1ff",
    "posted_date": "2021-04-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.000006+00:00",
    "date_confidence": "high",
    "description": "At Linear, we're building the product development system for teams and agents. AI is fundamentally changing how software gets built, and we’re shaping the tools this new era requir"
  },
  {
    "company": "Linear",
    "source": "linear_official_careers",
    "job_id": "cd5ae036-0223-427a-b038-ba16ef9dcb32",
    "title": "Senior / Staff Fullstack Engineer",
    "location": "North America; United States; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/linear/cd5ae036-0223-427a-b038-ba16ef9dcb32",
    "posted_date": "2021-08-18",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.000006+00:00",
    "date_confidence": "high",
    "description": "At Linear, we're building the product development system for teams and agents. AI is fundamentally changing how software gets built, and we’re shaping the tools this new era requir"
  },
  {
    "company": "Linear",
    "source": "linear_official_careers",
    "job_id": "069c4628-88d7-4e4d-b393-c996fc7f3076",
    "title": "Senior / Staff Product Engineer",
    "location": "Europe; European Union; Remote, European Union",
    "official_url": "https://jobs.ashbyhq.com/linear/069c4628-88d7-4e4d-b393-c996fc7f3076",
    "posted_date": "2022-01-22",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.000006+00:00",
    "date_confidence": "high",
    "description": "At Linear, we're building the product development system for teams and agents. AI is fundamentally changing how software gets built, and we’re shaping the tools this new era requir"
  },
  {
    "company": "Linear",
    "source": "linear_official_careers",
    "job_id": "12f8f208-0b9c-4569-bb3d-41c8a197029e",
    "title": "Senior / Staff Product Engineer",
    "location": "North America; United States; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/linear/12f8f208-0b9c-4569-bb3d-41c8a197029e",
    "posted_date": "2026-03-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.000006+00:00",
    "date_confidence": "high",
    "description": "At Linear, we're building the product development system for teams and agents. AI is fundamentally changing how software gets built, and we’re shaping the tools this new era requir"
  },
  {
    "company": "Linear",
    "source": "linear_official_careers",
    "job_id": "0c7c2e26-0a98-42cf-a47c-9a3999fb513b",
    "title": "Product Engineer",
    "location": "North America; United States; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/linear/0c7c2e26-0a98-42cf-a47c-9a3999fb513b",
    "posted_date": "2026-06-09",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.000006+00:00",
    "date_confidence": "high",
    "description": "At Linear, we're building the product development system for teams and agents. AI is fundamentally changing how software gets built, and we’re shaping the tools this new era requir"
  }
]
```

## Cohere

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/cohere`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.137s
- Company elapsed time: 0.298s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 33, 'usable_jd': 33}
- Raw jobs found: 119
- After US/location filtering: 97
- With trustworthy posted_date: 97
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "3136a5a5-06fd-4c82-8b72-a43467e6b128",
    "title": "Member of Technical Staff, Modeling",
    "location": "London; London, London, United Kingdom; San Francisco; New York; Paris; Toronto; Montreal; Remote, United Kingdom",
    "official_url": "https://jobs.ashbyhq.com/cohere/3136a5a5-06fd-4c82-8b72-a43467e6b128",
    "posted_date": "2024-11-01",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.206678+00:00",
    "date_confidence": "high",
    "description": "WHO ARE WE? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  },
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "443368a3-6276-4b90-9671-27fed40fd6d2",
    "title": "Senior Member of Technical Staff, Multimodal AI",
    "location": "San Francisco; San Francisco, California, United States; New York; Paris; Toronto; Montreal; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/cohere/443368a3-6276-4b90-9671-27fed40fd6d2",
    "posted_date": "2024-12-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.206678+00:00",
    "date_confidence": "high",
    "description": "WHO ARE WE? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  },
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "acec6038-117b-400b-92e3-0745fbb4cf53",
    "title": "Data Annotation Specialist - German Writer/Translator",
    "location": "Canada; Calgary; Boston; Nashville; Richmond; Phoenix; Seattle; United States; Vancouver; North America | Utah; Ottawa; Toronto; Montreal; Remote, Canada",
    "official_url": "https://jobs.ashbyhq.com/cohere/acec6038-117b-400b-92e3-0745fbb4cf53",
    "posted_date": "2026-10-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.206678+00:00",
    "date_confidence": "high",
    "description": "Who are we? Our mission is to scale intelligence to serve humanity. We’re training and deploying frontier models for developers and enterprises who are building AI systems to power"
  },
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "d42f5fd4-1ffc-45b9-957c-f09862db6af6",
    "title": "Member of Technical Staff, Training Performance Engineer",
    "location": "London; London, London, United Kingdom; New York; Paris; Toronto; Montreal; Remote, United Kingdom",
    "official_url": "https://jobs.ashbyhq.com/cohere/d42f5fd4-1ffc-45b9-957c-f09862db6af6",
    "posted_date": "2025-02-20",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.206678+00:00",
    "date_confidence": "high",
    "description": "WHO ARE WE? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  },
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "a13207e7-dc82-473f-8ca4-e832452fe8c3",
    "title": "Member of Technical Staff, Training Infra Engineer",
    "location": "Paris; Paris, France; San Francisco; London; New York; Toronto; Montreal; Remote, France",
    "official_url": "https://jobs.ashbyhq.com/cohere/a13207e7-dc82-473f-8ca4-e832452fe8c3",
    "posted_date": "2025-02-20",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.206678+00:00",
    "date_confidence": "high",
    "description": "WHO ARE WE? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  }
]
```

## Cisco

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cisco.wd5.myworkdayjobs.com/Cisco_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 45
- HTTP requests/cumulative request time: 263 / 86.309s
- Company elapsed time: 123.551s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 218 / 0 / 0
- Detail cache statuses: {'fetched:new': 210, 'fetched:missing_detail': 8}
- Relevant JD recovery: {'eligible': 59, 'usable_jd': 59}
- Raw jobs found: 838
- After US/location filtering: 218
- With trustworthy posted_date: 218
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 24.177, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 20.031, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.808, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 5.662, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.756, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.79, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.26, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.672, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 46}
- Query diagnostic: {"elapsed_seconds": 6.02, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 1.607, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "full stack backend", "raw_jobs": 32, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 8.824, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.702, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "cloud engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.238, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 3, "pages_fetched": 3, "query": "security engineer remote", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.559, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "software engineer collaboration devices", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 7.197, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "splunk engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.247, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer solution test iq platform", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2029178",
    "title": "Embedded Software Engineer",
    "location": "San Jose, California, US; San Francisco, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Embedded-Software-Engineer_2029178",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.242207+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 01/28/2027 Meet the Team Team Fusion develops embedded software for Cisco networking platforms, including hyperscaler-class switches"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2027589",
    "title": "Senior FPGA Engineer",
    "location": "San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Senior-FPGA-Engineer_2027589",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.242207+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 12/04/2026 This role requires the employee to work onsite from the San Jose, CA location. Meet Your team: The Network Hardware Engin"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2030105",
    "title": "Lead Performance & AI Tools Engineer, Hybrid",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Lead-Performance---AI-Tools-Engineer--Hybrid_2030105",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.242207+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 12/20/2026 This is a Hybrid role based out of Cisco's San Jose office. MEET THE TEAM Cisco’s Developer Platforms and AI Productivity"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2012214",
    "title": "ASIC Design Verification Technical Leader",
    "location": "Carlsbad, California, US; Allentown, Pennsylvania, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Carlsbad-California-US/ASIC-Design-Verification-Technical-Leader_2012214",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.242207+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 01/18/2027 Meet the Team The Silicon One team creates innovative hardware platforms central to the AI era, powering Cisco’s core Swi"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2012219",
    "title": "ASIC High Speed AMS Technical Leader",
    "location": "Carlsbad, California, US; Allentown, Pennsylvania, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Carlsbad-California-US/ASIC-High-Speed-AMS-Technical-Leader_2012219",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.242207+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 01/18/2027 Meet the Team The Silicon One team creates innovative hardware platforms central to the AI era, powering Cisco’s core Swi"
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://careers.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 145 / 47.132s
- Company elapsed time: 73.944s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 113 / 0 / 0
- Detail cache statuses: {'fetched:new': 113}
- Relevant JD recovery: {'eligible': 40, 'usable_jd': 40}
- Raw jobs found: 800
- After US/location filtering: 113
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 47.355, "first_pass_survivors": 95, "group": "official", "jds_resolved": 95, "original_postings_resolved": 95, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 95, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 1.949, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 5.079, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 6.507, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 1.936, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 1.956, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 1.894, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.03, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.889, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.349, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "cloud developer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 75}

Sample normalized records:

```json
[
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1453571533",
    "title": "Forward Deployed Senior AI Engineer",
    "location": "New York, NY, US, 10001",
    "official_url": "https://careers.sap.com/job/New-York-Forward-Deployed-Senior-AI-Engineer-NY-10001/1453571533/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.504792+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1442529933",
    "title": "Forward Deployed Chief AI Engineering Expert",
    "location": "New York, NY, US, 10001",
    "official_url": "https://careers.sap.com/job/New-York-Forward-Deployed-Chief-AI-Engineering-Expert-NY-10001/1442529933/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.504792+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1442882333",
    "title": "Senior Forward Deployed Engineering Manager",
    "location": "New York, NY, US, 10001",
    "official_url": "https://careers.sap.com/job/New-York-Senior-Forward-Deployed-Engineering-Manager-NY-10001/1442882333/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.504792+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1424105633",
    "title": "Principal Forward Deployed Architect",
    "location": "New York, NY, US, 10001",
    "official_url": "https://careers.sap.com/job/New-York-Principal-Forward-Deployed-Architect-NY-10001/1424105633/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.504792+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1453124533",
    "title": "Senior Data & Applied Scientist - Ontologies & Semantics",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://careers.sap.com/job/Palo-Alto-Senior-Data-&-Applied-Scientist-Ontologies-&-Semantics-CA-94304/1453124533/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:37:08.504792+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  }
]
```

## HPE

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://hpe.wd5.myworkdayjobs.com/Jobsathpe`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 318 / 131.078s
- Company elapsed time: 173.629s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 291 / 0 / 0
- Detail cache statuses: {'fetched:new': 280, 'fetched:missing_detail': 11}
- Relevant JD recovery: {'eligible': 135, 'usable_jd': 135}
- Raw jobs found: 496
- After US/location filtering: 291
- With trustworthy posted_date: 291
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 43.319, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 23.077, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 2.396, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 28.287, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.317, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.423, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.677, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.57, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 17.79, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.987, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "ai workflow specialist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 7}

Sample normalized records:

```json
[
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1215203",
    "title": "Principal AI Engineer",
    "location": "All, Wisconsin, United States of America; All, Georgia, United States of America; All, Texas, United States of America; All, Illinois, United States of America; All, North Carolina, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/All-Wisconsin-United-States-of-America/Principal-AI-Engineer_1215203-2",
    "posted_date": "2026-10-20",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:08.689960+00:00",
    "date_confidence": "high",
    "description": "Principal AI Engineer This role has been designated as ‘Remote/Teleworker’, which means you will primarily work from home. Who We Are: Hewlett Packard Enterprise is the global edge"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1202938",
    "title": "AI/ML Engineer - Agentic",
    "location": "San Jose, California, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/San-Jose-California-United-States-of-America/AI-ML-Engineer---Agentic_1202938-2",
    "posted_date": "2026-07-14",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:08.689960+00:00",
    "date_confidence": "high",
    "description": "AI/ML Engineer - Agentic This role has been designed as ‘Hybrid’ with an expectation that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Packard E"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1215573",
    "title": "HPC & AI Performance Engineer",
    "location": "Houston, Texas, United States of America; Bloomington, Minnesota, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Houston-Texas-United-States-of-America/HPC---AI-Performance-Engineer_1215573-2",
    "posted_date": "2026-10-07",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:08.689960+00:00",
    "date_confidence": "high",
    "description": "HPC & AI Performance Engineer This role has been designed as 'Hybrid' with a requirement that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Packa"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1213417",
    "title": "AI Performance Engineering Intern",
    "location": "Spring, Texas, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Spring-Texas-United-States-of-America/AI-Performance-Engineering-Intern_1213417",
    "posted_date": "2026-10-07",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:08.689960+00:00",
    "date_confidence": "high",
    "description": "AI Performance Engineering Intern This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enterpri"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1212980",
    "title": "HPC and AI Performance Engineer",
    "location": "Bloomington, Minnesota, United States of America; Houston, Texas, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Bloomington-Minnesota-United-States-of-America/HPC-and-AI-Performance-Engineer_1212980-3",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:08.689960+00:00",
    "date_confidence": "high",
    "description": "HPC and AI Performance Engineer This role has been designed as 'Hybrid' with a requirement that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Pac"
  }
]
```

## Disney

- Status: ok
- Scraping method: HTTP GET Disney server-rendered US search results
- Search URL/API: `https://www.disneycareers.com/en/search-jobs/software%20engineer/United%20States/391/1/2/6252001/39x76/-98x5/100/2`
- Pagination: ?p=1,2,3 per role query (intentional request cap)
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 35 / 14.258s
- Company elapsed time: 20.540s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 8 / 7 / 99
- Detail cache statuses: {'reused': 6, 'reuse_after_error:stale': 1, 'fetched:new': 1}
- Relevant JD recovery: {'deterministic_skip': 90, 'cache_reused': 7, 'eligible': 14, 'ai_skip': 9, 'detail_requests': 8, 'detail_failure': 7, 'detail_success': 1, 'last_good_reused': 1, 'budget_deferred': 0, 'usable_jd': 8}
- Raw jobs found: 270
- After US/location filtering: 113
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.16, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.04, "first_pass_survivors": 18, "group": "official", "jds_resolved": 0, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.063, "first_pass_survivors": 18, "group": "official", "jds_resolved": 0, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.96, "first_pass_survivors": 17, "group": "official", "jds_resolved": 0, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.199, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.077, "first_pass_survivors": 11, "group": "official", "jds_resolved": 0, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.92, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.116, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.18, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "R-04157",
    "title": "Facilities Operations Building Engineer",
    "location": "Emeryville, California",
    "official_url": "https://www.disneycareers.com/en/job/emeryville/facilities-operations-building-engineer/391/102250956944",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:15.046813+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10152782",
    "title": "Manager, Machine Learning Engineering - Ad Platforms",
    "location": "Seattle, Washington / Santa Monica, California",
    "official_url": "https://www.disneycareers.com/en/job/seattle/manager-machine-learning-engineering-ad-platforms/391/95937472144",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:15.046813+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10152780",
    "title": "Senior Machine Learning Engineering Manager, Ad Platforms",
    "location": "Seattle, Washington / Santa Monica, California",
    "official_url": "https://www.disneycareers.com/en/job/seattle/senior-machine-learning-engineering-manager-ad-platforms/391/95937472128",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:15.046813+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "102644648352",
    "title": "Staff Software Engineer",
    "location": "Glendale, California",
    "official_url": "https://www.disneycareers.com/en/job/glendale/staff-software-engineer/391/102644648352",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:15.046813+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "102253028336",
    "title": "Staff Workflow Engineer",
    "location": "Burbank, California",
    "official_url": "https://www.disneycareers.com/en/job/burbank/staff-workflow-engineer/391/102253028336",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:15.046813+00:00",
    "date_confidence": "high",
    "description": ""
  }
]
```

## eBay

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ebay.wd5.myworkdayjobs.com/apply`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 20
- HTTP requests/cumulative request time: 65 / 37.045s
- Company elapsed time: 46.045s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 44 / 0 / 0
- Detail cache statuses: {'fetched:new': 44}
- Relevant JD recovery: {'eligible': 15, 'usable_jd': 15}
- Raw jobs found: 210
- After US/location filtering: 44
- With trustworthy posted_date: 44
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.715, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 0.776, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.781, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 1.758, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 2.718, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 2.712, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 2.804, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 0.866, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.943, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 22}

Sample normalized records:

```json
[
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0075757",
    "title": "AI Engineer - AI & Automation",
    "location": "Austin",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Austin/Data-Scientist---AI---Automation_R0075757",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:22.450008+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0077480",
    "title": "Network Engineer 3",
    "location": "San Jose",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/San-Jose/Network-Engineer-3_R0077480",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:22.450008+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0076995",
    "title": "AI Transformation Lead",
    "location": "Austin",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Austin/AI-Transformation-Lead_R0076995",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:22.450008+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0076460",
    "title": "Sr. MTS, AI & Agentic Architect",
    "location": "Austin",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Austin/Sr-MTS--AI---Agentic-Architect_R0076460",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:22.450008+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0072836",
    "title": "Senior Platform Engineer",
    "location": "Austin",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Austin/Senior-Platform-Engineer_R0072836",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:22.450008+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  }
]
```

## Qualcomm

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://careers.qualcomm.com/api/pcsx/search?domain=qualcomm.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 152 / 44.279s
- Company elapsed time: 66.269s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 125 / 0 / 0
- Detail cache statuses: {'fetched:new': 119, 'fetched:missing_detail': 6}
- Relevant JD recovery: {'eligible': 35, 'usable_jd': 35}
- Raw jobs found: 255
- After US/location filtering: 125
- With trustworthy posted_date: 125
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.883, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 9.142, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.392, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 12.195, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.897, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.728, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.1, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.453, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.918, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3092768",
    "title": "Staff Software Engineer — SubSystem Integration Test (SSIT)",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720333630",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:33.762447+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Software Engineering General Summary: What You'll Do Feature-Level Test Strategy & Planning Pa"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3094004",
    "title": "Staff Reliability Engineer, Data Center Products",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720773196",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:33.762447+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Reliability Development Engineering General Summary: Senior Reliability Engineer – Data Center"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3096146",
    "title": "Machine Learning / Computer Vision Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720988289",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:33.762447+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Video Systems, HW Architecture General Summary: Qualcomm’s Computer Vision Systems team is bui"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3097689",
    "title": "Mixed Signal SVE Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721491128",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:33.762447+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > ASICS Engineering General Summary: Qualcomm is a company of inventors that unlocked 5G - usher"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3096516",
    "title": "Sr. Director - Engineering",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721114153",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:38:33.762447+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Mobile Chipset PE, MDM & MSM General Summary: As a leading technology innovator, Qualcomm is d"
  }
]
```

## AMD

- Status: ok
- Scraping method: HTTP GET public Jibe/iCIMS jobs JSON
- Search URL/API: `https://careers.amd.com/api/jobs`
- Pagination: page=1,2,... per role query; stop on total/empty/repeat/short page
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 14 / 8.377s
- Company elapsed time: 10.001s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 203, 'usable_jd': 203}
- Raw jobs found: 1221
- After US/location filtering: 479
- With trustworthy posted_date: 479
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.084, "first_pass_survivors": 319, "group": "official", "jds_resolved": 319, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 319, "stop_reason": "page_budget", "unique_contribution": 319, "unique_jobs": 319}
- Query diagnostic: {"elapsed_seconds": 0.579, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning", "raw_jobs": 89, "stop_reason": "early_stop", "unique_contribution": 29, "unique_jobs": 89}
- Query diagnostic: {"elapsed_seconds": 2.358, "first_pass_survivors": 73, "group": "official", "jds_resolved": 73, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 73, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 1.671, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "AI research", "raw_jobs": 213, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 213}
- Query diagnostic: {"elapsed_seconds": 2.307, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 300}

Sample normalized records:

```json
[
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "86806",
    "title": "Security Software Engineer",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-06-17",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:39:08.495980+00:00",
    "date_confidence": "high",
    "description": "WHAT YOU DO AT AMD CHANGES EVERYTHING At AMD, our mission is to build great products that accelerate next-generation computing experiences—from AI and data centers, to PCs, gaming "
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92603",
    "title": "Software Engineer - Networking, firmware and C++",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-10-05",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:08.495980+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92004",
    "title": "Senior GPU Performance Software Engineer",
    "location": "Austin, Texas",
    "official_url": "",
    "posted_date": "2026-10-05",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:39:08.495980+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "93490",
    "title": "Software Engineer, MarTech",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-10-30",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:39:08.495980+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "93487",
    "title": "Software Development Manager, MarTech",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-11-02",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:39:08.495980+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  }
]
```

## Zoom

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://zoom.wd5.myworkdayjobs.com/Zoom`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 13
- HTTP requests/cumulative request time: 41 / 21.591s
- Company elapsed time: 25.983s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 27 / 0 / 0
- Detail cache statuses: {'fetched:new': 25, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 106
- After US/location filtering: 27
- With trustworthy posted_date: 27
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.776, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 20, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 0.505, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.475, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 2.656, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 3.743, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 2.42, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 0.556, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.745, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.507, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}

Sample normalized records:

```json
[
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19605",
    "title": "Lead Technical SEO Manager",
    "location": "Remote (US)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--US/Lead-Technical-SEO-Manager_R19605",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:11.794421+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect This is a hands-on technical leadership role at the center of how Zoom gets found, understood, and surfaced across both traditional search engines and emerging "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19851",
    "title": "AI Scientist - Agentic Verticals",
    "location": "Seattle (WA); San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Seattle-WA/AI-Scientist---Agentic-Verticals_R19851-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:11.794421+00:00",
    "date_confidence": "high",
    "description": "AI Scientist - (AI Verticals) What You Can Expect In this role, you will tackle one of the most compelling challenges in production AI: enabling agents to continuously improve with"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19849",
    "title": "Senior Data Engineer (Online Data)",
    "location": "Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Seattle-WA/Senior-Data-Engineer--Online-Data-_R19849-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:11.794421+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect In this role, you will design, build, and optimize the data pipelines and analytical solutions that power Zoom’s Online business, including billing, checkout, g"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19773",
    "title": "Senior General Ledger Accountant",
    "location": "Remote (US)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--US/Senior-General-Ledger-Accountant_R19773",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:11.794421+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect As a Senior Accountant on Zoom’s General Ledger team, you will take ownership of the full accounting lifecycle for capitalized software, including Internal Use "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19839",
    "title": "Senior Product Designer, Zoom Virtual Agent",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Senior-Product-Designer--Zoom-Virtual-Agent_R19839",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:11.794421+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect As a Senior Product Designer for Zoom Virtual Agent, you will shape the conversational and agentic AI experiences that define how businesses and their customers"
  }
]
```

## Goldman Sachs

- Status: expected_limitation
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 0 / 0.000s
- Company elapsed time: 0.000s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

## Pure Storage

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/purestorage/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.254s
- Company elapsed time: 0.833s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 51, 'usable_jd': 51}
- Raw jobs found: 354
- After US/location filtering: 215
- With trustworthy posted_date: 215
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8303174",
    "title": "Account Executive, Air Force",
    "location": "Remote, United States; United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8303174",
    "posted_date": "2026-10-20",
    "updated_date": "2026-11-01",
    "fetched_at": "2026-11-06T00:39:18.498213+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8337517",
    "title": "Account Executive, Cloud & Data Services (New England)",
    "location": "Boston, Massachusetts; Massachusetts, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8337517",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:39:18.498213+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8260286",
    "title": "Account Executive, Commercial (Houston)",
    "location": "Houston, Texas; Texas, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8260286",
    "posted_date": "2026-10-09",
    "updated_date": "2026-11-01",
    "fetched_at": "2026-11-06T00:39:18.498213+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8279370",
    "title": "Account Executive, Commercial (NYC)",
    "location": "New York, New York; Remote - New York (Metro)",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8279370",
    "posted_date": "2026-10-14",
    "updated_date": "2026-11-01",
    "fetched_at": "2026-11-06T00:39:18.498213+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8145906",
    "title": "Account Executive, Commercial (Upstate New York)",
    "location": "Remote, New York; New York, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8145906",
    "posted_date": "2026-08-24",
    "updated_date": "2026-11-01",
    "fetched_at": "2026-11-06T00:39:18.498213+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  }
]
```

## Databricks

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/databricks/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.360s
- Company elapsed time: 1.746s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 81, 'usable_jd': 81}
- Raw jobs found: 923
- After US/location filtering: 501
- With trustworthy posted_date: 501
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8688861002",
    "title": "Accounting Data & Technology Manager",
    "location": "Mountain View, California; San Francisco, California; San Francisco, California",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8688861002",
    "posted_date": "2026-10-12",
    "updated_date": "2026-10-12",
    "fetched_at": "2026-11-06T00:39:19.332471+00:00",
    "date_confidence": "high",
    "description": "<p data-pm-slice=\"1 1 []\">GAQ327R291</p> <p data-renderer-start-pos=\"2729\"><span style=\"font-size: 14pt;\"><strong>Accounting Data &amp; Technology Manager</strong></span></p> <h2><"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8756154002",
    "title": "Accounting Manager, Accounts Receivable",
    "location": "California; New York; Remote - Colorado; Remote - Georgia; Remote - Ohio; Remote - Oregon; Remote - Pennsylvania; Remote - Texas; Remote - Washington; Remote - Washington D.C.; San Francisco, California",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8756154002",
    "posted_date": "2026-09-22",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:39:19.332471+00:00",
    "date_confidence": "high",
    "description": "<p data-pm-slice=\"1 1 []\">GAQ327R240</p> <p data-renderer-start-pos=\"1648\">While candidates in the listed location(s) are encouraged for this role, candidates in other locations wi"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8546367002",
    "title": "AI Engineer – Forward Deployed Engineering (AI FDE)",
    "location": "United States; Remote - California",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8546367002",
    "posted_date": "2026-05-13",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:39:19.332471+00:00",
    "date_confidence": "high",
    "description": "<p><strong>AI Engineer – Forward Deployed Engineering (AI FDE) (ALL LEVELS)</strong></p> <p><strong>CSQ327R177</strong></p> <p><strong>Mission</strong></p> <p>The AI Forward Deploy"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8760167002",
    "title": "AI Engineer – Forward Deployed Engineering (AI FDE), U.S. Public Sector (Federal Focus)",
    "location": "Maryland; Virginia; Washington, D.C.; Remote - Washington D.C.",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8760167002",
    "posted_date": "2026-08-28",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:39:19.332471+00:00",
    "date_confidence": "high",
    "description": "<p><span style=\"text-decoration: underline;\"><strong>PLEASE NOTE</strong></span><strong>: <br></strong>Due to federal contract requirements and client site access obligations, <str"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8824171002",
    "title": "AI Sales Director",
    "location": "San Francisco, California; United States; West Coast - United States; Remote - California",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8824171002",
    "posted_date": "2026-10-30",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:39:19.332471+00:00",
    "date_confidence": "high",
    "description": "<p data-pm-slice=\"1 1 []\">SLSQ427R457</p> <p>We are looking for a <strong>Director, AI Sales (IC)</strong> to grow Databricks’ enterprise AI business and shape how we take AI to ma"
  }
]
```

## Roblox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roblox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.250s
- Company elapsed time: 0.843s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 32, 'usable_jd': 32}
- Raw jobs found: 269
- After US/location filtering: 252
- With trustworthy posted_date: 252
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8242621",
    "title": "[2027] Applied Scientist - PhD Intern",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8242621?gh_jid=8242621",
    "posted_date": "2026-10-08",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:21.079731+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8143982",
    "title": "[2027] Associate Product Designer, Early Career",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8143982?gh_jid=8143982",
    "posted_date": "2026-09-02",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:21.079731+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8143976",
    "title": "[2027] Associate Product Manager, Early Career",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8143976?gh_jid=8143976",
    "posted_date": "2026-09-02",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:21.079731+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8242619",
    "title": "[2027] Data Scientist - PhD Intern",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8242619?gh_jid=8242619",
    "posted_date": "2026-10-08",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:21.079731+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8242623",
    "title": "[2027] Senior Machine Learning Engineer - PhD Early Career",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8242623?gh_jid=8242623",
    "posted_date": "2026-10-08",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:21.079731+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  }
]
```

## Airbnb

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/airbnb/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.191s
- Company elapsed time: 0.552s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 201
- After US/location filtering: 113
- With trustworthy posted_date: 113
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8231416",
    "title": "Associate Principal, Procurement Innovation Supplier Programs",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8231416?gh_jid=8231416",
    "posted_date": "2026-09-24",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-11-06T00:39:21.923661+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "7834481",
    "title": "Business Operations and Growth Lead",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/7834481?gh_jid=7834481",
    "posted_date": "2026-04-21",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:39:21.923661+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8325376",
    "title": "Business Process Improvement Manager",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8325376?gh_jid=8325376",
    "posted_date": "2026-10-27",
    "updated_date": "2026-10-27",
    "fetched_at": "2026-11-06T00:39:21.923661+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8316843",
    "title": "Connectivity Partner Manager",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8316843?gh_jid=8316843",
    "posted_date": "2026-10-23",
    "updated_date": "2026-10-24",
    "fetched_at": "2026-11-06T00:39:21.923661+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8275370",
    "title": "Counsel, Corporate",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8275370?gh_jid=8275370",
    "posted_date": "2026-10-13",
    "updated_date": "2026-10-13",
    "fetched_at": "2026-11-06T00:39:21.923661+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  }
]
```

## Anthropic

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/anthropic/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.419s
- Company elapsed time: 2.305s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 161, 'usable_jd': 161}
- Raw jobs found: 677
- After US/location filtering: 545
- With trustworthy posted_date: 545
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5456619008",
    "title": "3P Revenue Accounting & Reporting",
    "location": "San Francisco, CA | Seattle, WA; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5456619008",
    "posted_date": "2026-10-19",
    "updated_date": "2026-10-19",
    "fetched_at": "2026-11-06T00:39:22.477035+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "4461450008",
    "title": "Account Executive, AI Native",
    "location": "New York City, NY; San Francisco, CA | New York City, NY; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/4461450008",
    "posted_date": "2024-12-20",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-11-06T00:39:22.477035+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "4976314008",
    "title": "Account Executive, Nonprofit",
    "location": "San Francisco, CA | New York City, NY; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/4976314008",
    "posted_date": "2025-11-12",
    "updated_date": "2026-10-26",
    "fetched_at": "2026-11-06T00:39:22.477035+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5400138008",
    "title": "Account Executive, Startups",
    "location": "San Francisco, CA | New York City, NY; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5400138008",
    "posted_date": "2026-08-24",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-11-06T00:39:22.477035+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5398438008",
    "title": "Activation Manager, Beneficial Deployments",
    "location": "San Francisco, CA | New York City, NY; New York, New York, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5398438008",
    "posted_date": "2026-09-11",
    "updated_date": "2026-10-13",
    "fetched_at": "2026-11-06T00:39:22.477035+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  }
]
```

## AppLovin

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/applovin/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.166s
- Company elapsed time: 0.286s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 43
- After US/location filtering: 33
- With trustworthy posted_date: 33
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4724788006",
    "title": "Agency Development Lead - Independent Agencies",
    "location": "New York City, NY",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4724788006?gh_jid=4724788006",
    "posted_date": "2026-10-26",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:24.783100+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4724999006",
    "title": "Agency Development Lead - Independent Agencies",
    "location": "Los Angeles/Santa Monica, CA; New York City, NY",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4724999006?gh_jid=4724999006",
    "posted_date": "2026-10-26",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:24.783100+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4705316006",
    "title": "Agency Success Manager",
    "location": "Toronto; Remote - United States",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4705316006?gh_jid=4705316006",
    "posted_date": "2026-08-14",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:24.783100+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4622998006",
    "title": "Business Development Associate",
    "location": "Los Angeles/Santa Monica, CA; Remote - United States",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4622998006?gh_jid=4622998006",
    "posted_date": "2026-01-07",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:24.783100+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4611567006",
    "title": "Business Development Associate",
    "location": "New York",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4611567006?gh_jid=4611567006",
    "posted_date": "2025-10-25",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:24.783100+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  }
]
```

## ByteDance

- Status: ok
- Scraping method: HTTP POST public supplier /search/job/posts
- Search URL/API: `https://jobs.bytedance.com/api/v1/public/supplier/search/job/posts`
- Pagination: offset=0,50,...; limit=50; US city filter
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 24 / 27.939s
- Company elapsed time: 31.398s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 234, 'usable_jd': 234}
- Raw jobs found: 1065
- After US/location filtering: 458
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.48, "first_pass_survivors": 146, "group": "official", "jds_resolved": 146, "original_postings_resolved": 146, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 146, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.628, "first_pass_survivors": 101, "group": "official", "jds_resolved": 101, "original_postings_resolved": 101, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 101, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 4.12, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 108, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 108}
- Query diagnostic: {"elapsed_seconds": 3.59, "first_pass_survivors": 65, "group": "official", "jds_resolved": 65, "original_postings_resolved": 65, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 65, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.704, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.718, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.259, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 54, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 0.975, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 3.924, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 145}

Sample normalized records:

```json
[
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7571650125270370613",
    "title": "Machine Learning Engineer, AI Coding Tools",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7571650125270370613",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:25.070582+00:00",
    "date_confidence": "unknown",
    "description": "About the team: TRAE (The Real AI Engineer) is an intelligent engineer capable of understanding requirements, orchestrating tools, and independently completing development tasks, p"
  },
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7542987377129457938",
    "title": "Senior Software Engineer / Researcher, AI-Native database systems",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7542987377129457938",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:25.070582+00:00",
    "date_confidence": "unknown",
    "description": "About the Team Join ByteDance’s database R&D team, where you’ll build and own cutting-edge database products supporting Bytedance’s global infrastructure. Our diverse portfolio inc"
  },
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7600946112012912901",
    "title": "Senior Research Scientist/Engineer - AI Infrastructure",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7600946112012912901",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:25.070582+00:00",
    "date_confidence": "unknown",
    "description": "We are seeking an experienced Research Scientist or Engineer to help define and build the next generation of AI infrastructure. In this role, you will work at the intersection of l"
  },
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7642171416270260485",
    "title": "Machine Learning Engineer - AI Compiler Optimization",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7642171416270260485",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:25.070582+00:00",
    "date_confidence": "unknown",
    "description": "The mission of our AML team is to push the next-generation AI infrastructure and recommendation platform for the ads ranking, search ranking, live & ecom ranking in our company. We"
  },
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7499641201977723143",
    "title": "Software Engineer / Researcher, AI-Native database systems",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7499641201977723143",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:25.070582+00:00",
    "date_confidence": "unknown",
    "description": "About the Team Join ByteDance’s database R&D team, where you’ll build and own cutting-edge database products supporting ByteDance’s global infrastructure. Our diverse portfolio inc"
  }
]
```

## Chime

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/chime/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.193s
- Company elapsed time: 0.428s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 73
- After US/location filtering: 73
- With trustworthy posted_date: 73
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8569366002",
    "title": "AI/ML Engineer",
    "location": "Chicago, IL, USA; New York, NY, USA; San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8569366002?gh_jid=8569366002",
    "posted_date": "2026-06-08",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:37.778648+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role</h2> <p>Chime's Data Science &amp; Machine Learning team builds the models, services, and platforms behind how millions of members manage and grow their financia"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8853166002",
    "title": "Business Control Manager",
    "location": "Chicago, IL, USA; New York, NY, USA; San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8853166002?gh_jid=8853166002",
    "posted_date": "2026-10-07",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:37.778648+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the role</strong></h2> <p>We are hiring a Business Control Manager to join Chime’s Compliance Business Control Management team, with a primary focus on control de"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8877396002",
    "title": "Business Control Manager",
    "location": "Chicago, IL, USA; New York, NY, USA; San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8877396002?gh_jid=8877396002",
    "posted_date": "2026-10-08",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:37.778648+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\"><strong>About the Role</strong></span></h2> <p><span style=\"font-family: helvetica, arial, sans-serif;\">We are hiring a"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8584952002",
    "title": "Business Control Manager",
    "location": "Chicago, IL, USA; New York, NY, USA; San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8584952002?gh_jid=8584952002",
    "posted_date": "2026-06-18",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:37.778648+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role</h2> <p>We are hiring a <strong>Business Control Manager</strong> to join our Compliance team at Chime, where you will be responsible for strengthening the first"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8864181002",
    "title": "Commercial Counsel",
    "location": "New York, NY, USA; San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8864181002?gh_jid=8864181002",
    "posted_date": "2026-10-09",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:37.778648+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the role</strong></h2> <p>We are hiring a Commercial Counsel for our legal team. In this role, you will be a partner to the business on general commercial matters"
  }
]
```

## Citadel

- Status: expected_limitation
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 0 / 0.000s
- Company elapsed time: 0.000s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

## Dell

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 25
- HTTP requests/cumulative request time: 137 / 137.711s
- Company elapsed time: 157.368s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 111 / 0 / 0
- Detail cache statuses: {'missing:new': 1, 'fetched:new': 108, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 33, 'ai_recover': 1, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 32}
- Raw jobs found: 490
- After US/location filtering: 110
- With trustworthy posted_date: 110
- Errors/403s: ["detail 299245: Dell oracle hcm detail network error: HTTPSConnectionPool(host='enterpriseplatform.dell.com', port=443): Read timed out. (read timeout=30)"]

- Query diagnostic: {"elapsed_seconds": 43.65, "first_pass_survivors": 27, "group": "official", "jds_resolved": 26, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.361, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.479, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 9.68, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.23, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.976, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.532, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 39.894, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.514, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "299245",
    "title": "AI Performance Engineer",
    "location": "Austin, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/299245",
    "posted_date": "2026-10-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:38.207599+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "300865",
    "title": "AI Performance Engineer",
    "location": "Austin, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/300865",
    "posted_date": "2026-10-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:38.207599+00:00",
    "date_confidence": "high",
    "description": "AI Performance Engineer Dell's Client Product Group (CPG) is seeking an AI Performance Engineer to join the PC Systems Performance team. In this role, you will build foundational e"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "300866",
    "title": "AI Performance Engineer",
    "location": "Austin, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/300866",
    "posted_date": "2026-10-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:38.207599+00:00",
    "date_confidence": "high",
    "description": "AI Performance Engineer Dell's Client Product Group (CPG) is seeking an AI Performance Engineer to join the PC Systems Performance team. In this role, you will build foundational e"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "300869",
    "title": "AI Performance Engineer",
    "location": "Austin, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/300869",
    "posted_date": "2026-10-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:38.207599+00:00",
    "date_confidence": "high",
    "description": "AI Performance Engineer Dell's Client Product Group (CPG) is seeking an AI Performance Engineer to join the PC Systems Performance team. In this role, you will build foundational e"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "300879",
    "title": "AI Performance Engineer",
    "location": "Austin, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/300879",
    "posted_date": "2026-10-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:38.207599+00:00",
    "date_confidence": "high",
    "description": "AI Performance Engineer Dell's Client Product Group (CPG) is seeking an AI Performance Engineer to join the PC Systems Performance team. In this role, you will build foundational e"
  }
]
```

## Dropbox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/dropbox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.160s
- Company elapsed time: 0.224s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 33
- After US/location filtering: 22
- With trustworthy posted_date: 22
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8159652",
    "title": "Account Executive",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8159652?gh_jid=8159652",
    "posted_date": "2026-09-01",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:40.032341+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z95gas6hz75zjz77zz90zpz71zz80zeoz80zz68zlz66z"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8356282",
    "title": "Director, Data Science & Engineering, Finance",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8356282?gh_jid=8356282",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:40.032341+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qotv4z67zz122zz74z7qz70zz122z67z68zz80zp2z75zyz90zr5z83zz87z8z8"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8275002",
    "title": "Director of Pricing and Packaging",
    "location": "Remote - US: All locations; US",
    "official_url": "https://jobs.dropbox.com/listing/8275002?gh_jid=8275002",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:40.032341+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qotuz85z92z66zpz73zz122zz67z0z78zz78zgz85z5f2sngz82zz65z4z69zm6"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8249957",
    "title": "Integrated Campaign Strategist",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8249957?gh_jid=8249957",
    "posted_date": "2026-10-23",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:40.032341+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90za3wz122zz77zjz88zx7z66zz78zz69zbz70znpvz79z6"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8249958",
    "title": "Integrated Campaign Strategist",
    "location": "Remote - Canada: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8249958?gh_jid=8249958",
    "posted_date": "2026-10-23",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:39:40.032341+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90za3wz122zz77zjz88zx7z66zz78zz69zbz70znpvz79z6"
  }
]
```

## Expedia Group

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://expedia.wd108.myworkdayjobs.com/search`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 20
- HTTP requests/cumulative request time: 66 / 20.524s
- Company elapsed time: 29.737s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 46 / 0 / 0
- Detail cache statuses: {'fetched:new': 46}
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 325
- After US/location filtering: 46
- With trustworthy posted_date: 46
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 18.44, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.136, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 31, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 31}
- Query diagnostic: {"elapsed_seconds": 0.285, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 1.755, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 1.61, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.606, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.278, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.257, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.368, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 46}

Sample normalized records:

```json
[
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-111024",
    "title": "Senior Content Designer",
    "location": "Washington - Seattle Campus; Austin Domain 11 - HomeAway; USA - Illinois - Chicago",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Senior-Content-Designer_R-111024",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:40.257175+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-110161",
    "title": "Senior Software Engineer - Distribution and Supply",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Senior-Software-Engineer---Distribution-and-Supply_R-110161",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:40.257175+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109446",
    "title": "Machine Learning Scientist II - Agentic Experiences",
    "location": "Washington - Seattle Campus; Austin Domain 11 - HomeAway; USA - California - San Jose",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Machine-Learning-Scientist-II---Agentic-Experiences_R-109446",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:40.257175+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-110938",
    "title": "Senior Technical Integration Consultant",
    "location": "USA - Illinois - Chicago; UK - London",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---Illinois---Chicago/Senior-Technical-Integration-Consultant_R-110938",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:40.257175+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-111068",
    "title": "Director / Principal of Product Design – Servicing",
    "location": "USA - California - San Francisco; Austin Domain 11 - HomeAway; USA - Illinois - Chicago; USA - California - San Jose; Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---California---San-Francisco/Director---Principal-of-Product-Design---Servicing_R-111068",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:40.257175+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  }
]
```

## HubSpot

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/hubspotjobs/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.172s
- Company elapsed time: 0.226s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 113
- After US/location filtering: 13
- With trustworthy posted_date: 13
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "5990250",
    "title": "Account Executive - Enterprise",
    "location": "Remote - USA; Cambridge, MA, USA",
    "official_url": "https://www.hubspot.com/careers/jobs/5990250?gh_jid=5990250",
    "posted_date": "2024-06-13",
    "updated_date": "2026-10-20",
    "fetched_at": "2026-11-06T00:39:54.398579+00:00",
    "date_confidence": "high",
    "description": "<h3>Our Mission: Helping Millions of Organizations Grow Better</h3> <h3>Team Overview</h3> <p>Our Enterprise Sales team drives growth by connecting large organizations (500–5,000 e"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "5990166",
    "title": "Account Executive - Mid-Market (Remote)",
    "location": "Remote - USA; Cambridge, MA, USA",
    "official_url": "https://www.hubspot.com/careers/jobs/5990166?gh_jid=5990166",
    "posted_date": "2024-06-07",
    "updated_date": "2026-10-28",
    "fetched_at": "2026-11-06T00:39:54.398579+00:00",
    "date_confidence": "high",
    "description": "<p><strong>In this role, you'll:</strong></p> <ul> <li>Own the full new business cycle within mid-market accounts (51–500 employees) — hunting for new logos, not managing existing "
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "5990225",
    "title": "Account Executive - Small Business",
    "location": "Remote - USA; Cambridge, MA, USA",
    "official_url": "https://www.hubspot.com/careers/jobs/5990225?gh_jid=5990225",
    "posted_date": "2024-06-07",
    "updated_date": "2026-11-02",
    "fetched_at": "2026-11-06T00:39:54.398579+00:00",
    "date_confidence": "high",
    "description": "<p><strong>***Now accepting applications for a December 1st, 2026 start date***</strong></p> <p>As an Account Executive on the Small Business sales team, you will identify, source,"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8266540",
    "title": "Lead Counsel, Public Company Governance & Corporate Programs",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8266540?gh_jid=8266540",
    "posted_date": "2026-10-20",
    "updated_date": "2026-10-20",
    "fetched_at": "2026-11-06T00:39:54.398579+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-20140</strong></p> <hr> <h2><strong>The Legal Team</strong></h2> <p>HubSpot's Legal team is a proactive, business-enabling partner — not a back-office function. We h"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8237769",
    "title": "Lead Data Analyst",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8237769?gh_jid=8237769",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:39:54.398579+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-33722</strong></p> <hr> <p>We are seeking a highly skilled Lead Data Analyst to join our Global Incentive Compensation team. Reporting directly to the Manager of Cus"
  }
]
```

## Instacart

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/instacart/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.212s
- Company elapsed time: 0.431s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 8, 'usable_jd': 8}
- Raw jobs found: 90
- After US/location filtering: 82
- With trustworthy posted_date: 82
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8250324",
    "title": "Account Manager",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8250324",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-11-06T00:39:54.627602+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "7144697",
    "title": "Activation Sales Development Representative II",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=7144697",
    "posted_date": "2025-08-07",
    "updated_date": "2026-10-22",
    "fetched_at": "2026-11-06T00:39:54.627602+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8157774",
    "title": "Bilingual Customer Experience Specialist (Spanish)",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8157774",
    "posted_date": "2026-08-25",
    "updated_date": "2026-10-16",
    "fetched_at": "2026-11-06T00:39:54.627602+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8336857",
    "title": "Bilingual Customer Experience T3 Specialist (Spanish)",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8336857",
    "posted_date": "2026-10-30",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:39:54.627602+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8257641",
    "title": "Bilingual CX Specialist (French)",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8257641",
    "posted_date": "2026-10-05",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-11-06T00:39:54.627602+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  }
]
```

## Intel

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://intel.wd1.myworkdayjobs.com/External`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 177 / 92.854s
- Company elapsed time: 117.518s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 149 / 0 / 0
- Detail cache statuses: {'fetched:new': 133, 'fetched:missing_detail': 16}
- Relevant JD recovery: {'eligible': 94, 'usable_jd': 94}
- Raw jobs found: 493
- After US/location filtering: 149
- With trustworthy posted_date: 149
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.803, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 7.725, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 10.695, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 12.199, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 17.985, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 10.968, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 10.481, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 1.462, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 14.026, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 79}

Sample normalized records:

```json
[
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0287533",
    "title": "AI Hardware Engineering Intern",
    "location": "US, California, Santa Clara; US, California, Folsom",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-California-Santa-Clara/AI-Hardware-Engineering-Intern_JR0287533",
    "posted_date": "2026-10-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:55.059881+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: About the Job Intel is seeking exceptional Computer Science, Electrical Engineering, Computer Engineering, and AI/ML students to join an AI Hardware E"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0287530",
    "title": "AI Solution Architect Graduate Intern",
    "location": "US, California, Santa Clara",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-California-Santa-Clara/AI-Solution-Architect-Graduate-Intern_JR0287530",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:55.059881+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel is seeking an AI Infrastructure Solution Architect Intern to join our AI Platforms team. As an intern, you will work alongside experienced engin"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0281978",
    "title": "AI Performance Library Architect",
    "location": "US, Oregon, Hillsboro; US, California, Folsom",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/AI-Performance-Library-Architect_JR0281978-1",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:55.059881+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Software and AI (SAI) organization is looking for a software development engineer to work on oneDNN project ( https://github.com/uxlfoundation/oneDNN "
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0288139",
    "title": "AI Data Science / Software Engineering PhD Intern New 2027",
    "location": "US, Oregon, Hillsboro",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/AI-Data-Science---Software-Engineering-PhD-Intern-New-2027_JR0288139",
    "posted_date": "2026-10-20",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:55.059881+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: The Role and Impact As an AI Software Engineering PhD Intern, you will contribute to the design, development, and optimization of cutting-edge AI soft"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0288136",
    "title": "AI Data Science / Software Engineering PhD Intern New 2027",
    "location": "US, Oregon, Hillsboro",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/AI-Data-Science---Software-Engineering-PhD-Intern-New-2027_JR0288136",
    "posted_date": "2026-10-20",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:55.059881+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: The Role and Impact As an AI Software Engineering PhD Intern, you will contribute to the design, development, and optimization of cutting-edge AI soft"
  }
]
```

## MathWorks

- Status: ok
- Scraping method: HTTP GET server-rendered MathWorks search + JobPosting JSON-LD
- Search URL/API: `https://www.mathworks.com/company/jobs/opportunities/search/`
- Pagination: page=2,3,... after the unnumbered first page; stop on empty/repeat/short page
- Pages/requests fetched: 12
- HTTP requests/cumulative request time: 50 / 16.934s
- Company elapsed time: 18.617s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 38 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 112
- After US/location filtering: 38
- With trustworthy posted_date: 38
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 7.882, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 22, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 1.011, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 0.683, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 2.118, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.655, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 1.582, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.498, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.43, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.759, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 27}

Sample normalized records:

```json
[
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "16217",
    "title": "Multiple Openings - Engineering Development Group - U.S.",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/16217-multiple-openings-engineering-development-group-u-s?keywords=ai+engineer",
    "posted_date": "2026-09-01",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:56.469900+00:00",
    "date_confidence": "high",
    "description": "<p>About this Program</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37011",
    "title": "Senior AI Platform Engineer",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37011-senior-ai-platform-engineer?keywords=ai+engineer",
    "posted_date": "2026-04-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:56.469900+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37010",
    "title": "Senior AI Platform Engineer",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37010-senior-ai-platform-engineer?keywords=ai+engineer",
    "posted_date": "2026-04-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:56.469900+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37797",
    "title": "Principal AI Security Engineer",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37797-principal-ai-security-engineer?keywords=ai+engineer",
    "posted_date": "2026-10-09",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:56.469900+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37334",
    "title": "Sr. Product Marketing Engineer, Agentic AI",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37334-sr-product-marketing-engineer-agentic-ai?keywords=ai+engineer",
    "posted_date": "2026-07-07",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:39:56.469900+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  }
]
```

## MongoDB

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/mongodb/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.444s
- Company elapsed time: 1.046s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 32, 'usable_jd': 32}
- Raw jobs found: 368
- After US/location filtering: 236
- With trustworthy posted_date: 236
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "8209134",
    "title": "2027 - Software Engineering Intern, AMER",
    "location": "Austin; New York City; San Francisco; Austin, TX, United States; New York, NY, United States; San Francisco, CA, United States",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=8209134",
    "posted_date": "2026-10-23",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:40:09.994808+00:00",
    "date_confidence": "high",
    "description": "<p>We’re seeking curious minds like yours to collaborate with full-time engineers and cross functional teammates, learn development standard methodologies, and gain practical softw"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7318558",
    "title": "Account Development Representative",
    "location": "Gurugram; Gurugram, Haryana, India",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7318558",
    "posted_date": "2026-07-27",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:40:09.994808+00:00",
    "date_confidence": "high",
    "description": "<p>An Account Development Representative at MongoDB is the starting point for building a serious career in technology sales.&nbsp;</p> <p>This role is the foundation of our sales o"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "8079914",
    "title": "Account Development Representative",
    "location": "Kuala Lumpur; MYS_KualaLumpur",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=8079914",
    "posted_date": "2026-07-23",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:40:09.994808+00:00",
    "date_confidence": "high",
    "description": "<p>An Account Development Representative at MongoDB is the starting point for building a serious career in technology sales.&nbsp;</p> <p>This role is the foundation of our sales o"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "8352010",
    "title": "Account Development Representative",
    "location": "Beijing; Shanghai; Shenzhen; Beijing, China; Shanghai, China; Shenzhen Shi, Guangdong, China",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=8352010",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:40:09.994808+00:00",
    "date_confidence": "high",
    "description": "<p>An Account Development Representative at MongoDB is the starting point for building a serious career in technology sales.&nbsp;</p> <p>This role is the foundation of our sales o"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7334938",
    "title": "Account Development Representative, Hebrew Speaking",
    "location": "Tel Aviv; Tel Aviv-Yafo, Israel",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7334938",
    "posted_date": "2025-10-21",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:40:09.994808+00:00",
    "date_confidence": "high",
    "description": "<p>At MongoDB, our Account Development team works closely with our partners in both Sales and Marketing to build fanatical customer enthusiasm around MongoDB. ADR reps are responsi"
  }
]
```

## Morgan Stanley

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://morganstanley.eightfold.ai/api/pcsx/search?domain=morganstanley.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 128 / 42.080s
- Company elapsed time: 60.097s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 103 / 0 / 0
- Detail cache statuses: {'fetched:new': 102, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 32, 'usable_jd': 32}
- Raw jobs found: 225
- After US/location filtering: 103
- With trustworthy posted_date: 103
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 15.169, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 9.06, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.651, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 8.217, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 4.466, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.745, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 12.25, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.302, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.811, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR045727",
    "title": "Lead Site Reliability Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800830679",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:11.042277+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR046034",
    "title": "Vice President - Java Lead for Investment Banking Advisory Technology",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800999790",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:11.042277+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR039960",
    "title": "AI Full Stack Engineer (Prime Brokerage Technology)",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549798643526",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:11.042277+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR045800",
    "title": "Lead Mainframe Hardware Engineer",
    "location": "Atlanta, Georgia, United States of America; Birmingham, Alabama, United States of America; Little Rock, Arkansas, United States of America; Scottsdale, Arizona, United States of America; Greenwood Village, Colorado, United States of America; Greenwich, Connecticut, United States of America; Wilmington, Delaware, United States of America; Miami, Florida, United States of America; Davenport, Iowa, United States of America; Boise, Idaho, United States of America; Chicago, Illinois, United States of America; Indianapolis, Indiana, United States of America; Leawood, Kansas, United States of America; Louisville, Kentucky, United States of America; New Orleans, Louisiana, United States of America; Baltimore, Maryland, United States of America; Birmingham, Michigan, United States of America; Minneapolis, Minnesota, United States of America; Clayton, Missouri, United States of America; Jackson, Mississippi, United States of America; Billings, Montana, United States of America; Charlotte, North Carolina, United States of America; Fargo, North Dakota, United States of America; Omaha, Nebraska, United States of America; Manchester, New Hampshire, United States of America; Albuquerque, New Mexico, United States of America; Reno, Nevada, United States of America; Columbus, Ohio, United States of America; Tulsa, Oklahoma, United States of America; Portland, Oregon, United States of America; West Conshohocken, Pennsylvania, United States of America; Providence, Rhode Island, United States of America; Charleston, South Carolina, United States of America; Sioux City, South Dakota, United States of America; Knoxville, Tennessee, United States of America; Houston, Texas, United States of America; South Jordan, Utah, United States of America; Mclean, Virginia, United States of America; Burlington, Vermont, United States of America; Bellevue, Washington, United States of America; Wauwatosa, Wisconsin, United States of America; Charleston, West Virginia, United States of America; Sheridan, Wyoming, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800852314",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:11.042277+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR040698",
    "title": "Lead Application Security Automation Engineer",
    "location": "Alpharetta, Georgia, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549798982638",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:11.042277+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  }
]
```

## NetApp

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.netapp.com/en/search-jobs`
- Pagination: p=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 29
- HTTP requests/cumulative request time: 119 / 32.845s
- Company elapsed time: 50.405s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 90 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 32, 'usable_jd': 32}
- Raw jobs found: 435
- After US/location filtering: 90
- With trustworthy posted_date: 90
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.205, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 5.668, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 6.905, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 7.376, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.639, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 3.398, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.683, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.395, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.134, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "102797213808",
    "title": "Distinguished Engineer- AI",
    "location": "San Jose, California, United States",
    "official_url": "https://careers.netapp.com/en/job/san-jose/distinguished-engineer-ai/27600/102797213808",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:15.088279+00:00",
    "date_confidence": "high",
    "description": "Job Summary ONTAP is NetApp’s flagship storage operating system. The ONTAP team drives the product strategy, roadmap, and engineering delivery for ONTAP software and systems. You a"
  },
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "102549034016",
    "title": "Principal Engineer, AI BU",
    "location": "United States; Morrisville, North Carolina, United States; San Jose, California, United States",
    "official_url": "https://careers.netapp.com/en/job/united-states/principal-engineer-ai-bu/27600/102549034016",
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:15.088279+00:00",
    "date_confidence": "high",
    "description": "Job Summary As a Principal Engineer in NetApp's AI BU, you are a senior technical authority — architecting and tech-leading complex, cross-team initiatives and setting technical di"
  },
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "92333022944",
    "title": "Distinguished Engineer - AI",
    "location": "San Jose, California, United States",
    "official_url": "https://careers.netapp.com/en/job/san-jose/distinguished-engineer-ai/27600/92333022944",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:15.088279+00:00",
    "date_confidence": "high",
    "description": "Job Summary Distinguished Engineer - AI Infrastructure We are seeking a Distinguished Engineer with unrivaled depth in AI/ML inferencing at scale and the distributed systems founda"
  },
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "100127712432",
    "title": "Director of Engineering - AI Solutions",
    "location": "Morrisville, North Carolina, United States; San Jose, California, United States",
    "official_url": "https://careers.netapp.com/en/job/morrisville/director-of-engineering-ai-solutions/27600/100127712432",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:15.088279+00:00",
    "date_confidence": "high",
    "description": "Executive Summary We are looking for an innovative Director of Engineering – AI Solutions for Developer Productivity to transform how our software engineers build, test, and deploy"
  },
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "100664059424",
    "title": "Director, Data & AI",
    "location": "Morrisville, North Carolina, United States; United States",
    "official_url": "https://careers.netapp.com/en/job/morrisville/director-data-and-ai/27600/100664059424",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:40:15.088279+00:00",
    "date_confidence": "high",
    "description": "Job Summary As Director, Data & AI readiness you will own the strategy to enable data & intelligence layer powering NetApp’s most critical corporate functions — Sales, HR, Finance,"
  }
]
```

## Netflix

- Status: ok
- Scraping method: HTTP GET Eightfold server HTML + embedded smartApplyData positions
- Search URL/API: `https://explore.jobs.netflix.net/careers`
- Pagination: first 10 embedded positions per focused role query; PCSX remains disabled
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 9 / 2.915s
- Company elapsed time: 3.902s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 37 / 36
- Detail cache statuses: {'reused': 19, 'reuse_after_error:stale': 18}
- Relevant JD recovery: {'deterministic_skip': 10, 'cache_reused': 37, 'eligible': 19, 'ai_skip': 26, 'usable_jd': 19}
- Raw jobs found: 90
- After US/location filtering: 55
- With trustworthy posted_date: 55
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.543, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.346, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.4, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.341, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.541, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.407, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.458, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.323, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.543, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}

Sample normalized records:

```json
[
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "AJRT30201",
    "title": "AI Engineer 6 - AI Foundation & Tooling, Ads Platform",
    "location": "Los Gatos,California,United States of America",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790298014263",
    "posted_date": "2024-07-23",
    "updated_date": "2026-05-19",
    "fetched_at": "2026-11-06T00:41:02.320437+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR41408",
    "title": "Staff/ Principal Software Engineer (L6/L7): AI Platform Model Serving",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790316811164",
    "posted_date": "2026-10-27",
    "updated_date": "2026-10-27",
    "fetched_at": "2026-11-06T00:41:02.320437+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR42956",
    "title": "Senior Game Engineer, Gen AI - Games",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790318858893",
    "posted_date": "2026-10-08",
    "updated_date": "2026-10-08",
    "fetched_at": "2026-11-06T00:41:02.320437+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR42292",
    "title": "Software Engineer 5 – Model Development and Management, AI Platform",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790318081427",
    "posted_date": "2026-08-24",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-11-06T00:41:02.320437+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR41877",
    "title": "Visualization Engineer 5 - AI Infrastructure & Productivity Tooling",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790317589519",
    "posted_date": "2026-07-30",
    "updated_date": "2026-07-30",
    "fetched_at": "2026-11-06T00:41:02.320437+00:00",
    "date_confidence": "high",
    "description": "At Netflix, our mission is to entertain the world. Together, we are writing the next episode - pushing the boundaries of storytelling, global fandom and making the unimaginable a r"
  }
]
```

## OpenAI

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/openai`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.399s
- Company elapsed time: 1.446s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 348, 'usable_jd': 348}
- Raw jobs found: 821
- After US/location filtering: 663
- With trustworthy posted_date: 663
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "8fb1615c-34bf-47c4-a1d1-b7b2f836bbd3",
    "title": "Technical Program Manager, Compute Infrastructure",
    "location": "San Francisco; San Francisco, California, United States; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/openai/8fb1615c-34bf-47c4-a1d1-b7b2f836bbd3",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:05.494132+00:00",
    "date_confidence": "high",
    "description": "ABOUT THE TEAM The Compute Infrastructure team runs the GPU fleet and large-scale compute clusters that serve the models backing ChatGPT and the API, while also supporting training"
  },
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "240d459b-696d-43eb-8497-fab3e56ecd9b",
    "title": "Research Engineer",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://jobs.ashbyhq.com/openai/240d459b-696d-43eb-8497-fab3e56ecd9b",
    "posted_date": "2025-04-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:05.494132+00:00",
    "date_confidence": "high",
    "description": "By applying to this role, you will be considered for Research Engineer roles across all teams at OpenAI. About the Role As a Research Engineer here, you will be responsible for bui"
  },
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "2560ed50-5535-42b8-b069-9ebc28ce7493",
    "title": "Researcher, Safety Training",
    "location": "San Francisco; San Francisco, California, United States; London, UK",
    "official_url": "https://jobs.ashbyhq.com/openai/2560ed50-5535-42b8-b069-9ebc28ce7493",
    "posted_date": "2023-05-25",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:05.494132+00:00",
    "date_confidence": "high",
    "description": "ABOUT THE TEAM Safety Research at OpenAI is responsible for ensuring our most capable models can be safely deployed in the real world. The Safety Training team develops the researc"
  },
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "3c67f712-697d-48d8-b05c-01be896e61da",
    "title": "Software Engineer, Scaled Abuse",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://jobs.ashbyhq.com/openai/3c67f712-697d-48d8-b05c-01be896e61da",
    "posted_date": "2026-06-08",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:05.494132+00:00",
    "date_confidence": "high",
    "description": "ABOUT THE TEAM The Applied team safely brings OpenAI's technology to the world. We released ChatGPT; Plugins; DALL·E; and the APIs for GPT-5, embeddings, and fine-tuning. We also o"
  },
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "f763c6b3-5167-4a67-b691-4c3fa2c44156",
    "title": "Software Engineer, Data Infrastructure",
    "location": "San Francisco; San Francisco, California, United States; New York City; Seattle; Mountain View",
    "official_url": "https://jobs.ashbyhq.com/openai/f763c6b3-5167-4a67-b691-4c3fa2c44156",
    "posted_date": "2024-06-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:05.494132+00:00",
    "date_confidence": "high",
    "description": "About the Team Data Platform at OpenAI owns the foundational data stack powering critical product, research, and analytics workflows. We operate some of the largest Spark compute f"
  }
]
```

## Palantir

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/palantir`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.980s
- Company elapsed time: 1.208s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 2 / 2
- Detail cache statuses: {'reuse_after_error:stale': 2}
- Relevant JD recovery: {'eligible': 188, 'cache_reused': 2, 'ai_skip': 2, 'usable_jd': 188}
- Raw jobs found: 309
- After US/location filtering: 245
- With trustworthy posted_date: 245
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "0ccbe620-a3ef-41d1-a5c4-68e56b3c91d0",
    "title": "American Tech Fellowship",
    "location": "North America",
    "official_url": "https://jobs.lever.co/palantir/0ccbe620-a3ef-41d1-a5c4-68e56b3c91d0",
    "posted_date": "2025-06-17",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.223186+00:00",
    "date_confidence": "high",
    "description": "We want builders: people who are hungry to learn whatever it takes to succeed and aren't afraid to roll up their sleeves and make it happen. You might be that kind of person if you"
  },
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "ab7e3425-81d5-4705-a7b5-cd60c8a45cdb",
    "title": "Backend Software Engineer - Application Development",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/palantir/ab7e3425-81d5-4705-a7b5-cd60c8a45cdb",
    "posted_date": "2024-03-11",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.223186+00:00",
    "date_confidence": "high",
    "description": "Architecting, developing, and maintaining high-performance, scalable backend services that underpin our our operational data and AI systems Maintaining high coding standards throug"
  },
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "9aadca04-df88-4b46-95d8-c3b2628b30b0",
    "title": "Backend Software Engineer - Data Connectors",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/palantir/9aadca04-df88-4b46-95d8-c3b2628b30b0",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.223186+00:00",
    "date_confidence": "high",
    "description": "Java and Python for connectors, backend services, and developer SDKs Open-source technologies like Kafka, Kubernetes, Flink, Debezium, Iceberg Industry-standard build tooling, incl"
  },
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "1345438c-ebfc-4fa5-b545-30c1414f317c",
    "title": "Backend Software Engineer - Defense",
    "location": "Washington, D.C.",
    "official_url": "https://jobs.lever.co/palantir/1345438c-ebfc-4fa5-b545-30c1414f317c",
    "posted_date": "2025-02-24",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.223186+00:00",
    "date_confidence": "high",
    "description": "Build for high-scale, collaborative, geospatial workflows ( Gaia ) Design sophisticated frameworks to enable complex workflows across applications in a single workspace Develop the"
  },
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "a8174f9c-6f46-46b4-8e15-d1ff9e37c9eb",
    "title": "Backend Software Engineer - Defense",
    "location": "Palo Alto, CA",
    "official_url": "https://jobs.lever.co/palantir/a8174f9c-6f46-46b4-8e15-d1ff9e37c9eb",
    "posted_date": "2025-02-24",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.223186+00:00",
    "date_confidence": "high",
    "description": "Build for high-scale, collaborative, geospatial workflows ( Gaia ) Design sophisticated frameworks to enable complex workflows across applications in a single workspace Develop the"
  }
]
```

## PayPal

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://paypal.eightfold.ai/api/pcsx/search?domain=paypal.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 20
- HTTP requests/cumulative request time: 81 / 24.380s
- Company elapsed time: 35.607s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 60 / 0 / 0
- Detail cache statuses: {'fetched:new': 59, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 179
- After US/location filtering: 60
- With trustworthy posted_date: 60
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.808, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.27, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 2.202, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 5.383, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 3.593, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.805, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.586, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 0.757, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.71, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138583",
    "title": "Mobile Engineer Intern - Summer 2027",
    "location": "San Jose, California, United States of America; Chicago, Illinois, United States of America; Omaha, Nebraska, United States of America; Scottsdale, Arizona, United States of America; Austin, Texas, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922982818",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.941380+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138582",
    "title": "Data Scientist Intern - Summer 2027",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922982821",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.941380+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138581",
    "title": "Machine Learning Engineer Intern - Summer 2027",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922983149",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.941380+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138579",
    "title": "Machine Learning Engineer PhD Intern - Summer 2027",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922983152",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.941380+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138485",
    "title": "Director, Cybersecurity Engineering",
    "location": "Virginia, United States of America (Virtual); Scottsdale, Arizona, United States of America; Chicago, Illinois, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923280864",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:06.941380+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  }
]
```

## Reddit

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/reddit/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.248s
- Company elapsed time: 0.651s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 163
- After US/location filtering: 143
- With trustworthy posted_date: 143
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8282760",
    "title": "Analytics Engineer",
    "location": "Remote - United States; San Francisco, CA, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8282760",
    "posted_date": "2026-10-14",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:41:07.431920+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8148089",
    "title": "Associate General Counsel, Ads Product",
    "location": "Remote - United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8148089",
    "posted_date": "2026-10-30",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:41:07.431920+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8349881",
    "title": "Business Analyst",
    "location": "New York City, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8349881",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:41:07.431920+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8249259",
    "title": "Chief of Staff, Global Sales",
    "location": "London, United Kingdom; London, England, United Kingdom; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8249259",
    "posted_date": "2026-10-02",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:41:07.431920+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8187521",
    "title": "Chief of Staff, Global Sales",
    "location": "New York City, NY; London, England, United Kingdom; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8187521",
    "posted_date": "2026-10-02",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:41:07.431920+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  }
]
```

## Red Hat

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://redhat.wd5.myworkdayjobs.com/jobs`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 11
- HTTP requests/cumulative request time: 43 / 19.465s
- Company elapsed time: 23.805s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 31 / 0 / 0
- Detail cache statuses: {'fetched:new': 28, 'fetched:stale': 1, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 15, 'usable_jd': 15}
- Raw jobs found: 85
- After US/location filtering: 31
- With trustworthy posted_date: 31
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 7.746, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.472, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.89, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 10.59, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 0.623, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.542, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.542, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.447, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.307, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 19}

Sample normalized records:

```json
[
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-060399",
    "title": "AI Architect - Top Secret Clearance (TS/SCI CI Poly) required",
    "location": "Remote US VA",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Remote-US-VA/AI-Architect---Top-Secret-Clearance--TS-SCI-CI-Poly--required_R-060399-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:08.083513+00:00",
    "date_confidence": "high",
    "description": "The Red Hat Services team is looking for an AI Architect to design and deliver strategic solutions that solve our clients’ business challenges, through technical leadership, hands-"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-060246",
    "title": "Senior Machine Learning Engineer (vLLM)",
    "location": "Boston",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Boston/Senior-Machine-Learning-Engineer_R-060246",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:08.083513+00:00",
    "date_confidence": "high",
    "description": "*Telecommuting permitted: work may be performed within normal commuting distance from the Red Hat, LLC office in Boston, MA. Lead the design and implementation of high-performance "
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-060145",
    "title": "Consultant, OpenShift AI - Top Secret Clearance Required",
    "location": "Remote US TX",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Remote-US-TX/Consultant--OpenShift-AI---Top-Secret-Clearance-Required_R-060145-1",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:08.083513+00:00",
    "date_confidence": "high",
    "description": "About the Job: The Red Hat Services team is looking for a Consultant to implement practical AI solutions that directly solve client challenges using Red Hat OpenShift and Red Hat A"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-060282",
    "title": "Senior Software Engineer",
    "location": "Raleigh",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Raleigh/Senior-Software-Engineer_R-060282",
    "posted_date": "2026-10-29",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:08.083513+00:00",
    "date_confidence": "high",
    "description": "*Telecommuting permitted: work may be performed within normal commuting distance from the Red Hat, LLC office in Raleigh, NC. Collaborate with developers, quality engineers and arc"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-060247",
    "title": "Senior Software Engineer",
    "location": "Raleigh",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Raleigh/Senior-Software-Engineer_R-060247",
    "posted_date": "2026-10-29",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:08.083513+00:00",
    "date_confidence": "high",
    "description": "*Telecommuting role to be performed anywhere in the U.S. Design and develop new features and functionalities for OCI registries inside of Red Hat, including quay.io and registry.re"
  }
]
```

## Roku

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roku/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.178s
- Company elapsed time: 0.425s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 91
- After US/location filtering: 74
- With trustworthy posted_date: 74
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8330831",
    "title": "Ad Sales and Revenue Solutions Intern",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8330831?gh_jid=8330831",
    "posted_date": "2026-11-02",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:41:11.139992+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8345947",
    "title": "AI Engineering Internship Program (Summer 2027)",
    "location": "Cambridge, United Kingdom; Cambridge, England, U.K.",
    "official_url": "https://www.weareroku.com/jobs/8345947?gh_jid=8345947",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:41:11.139992+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8352981",
    "title": "Assistant General Counsel, Business & Legal Affairs",
    "location": "Santa Monica, California; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8352981?gh_jid=8352981",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:41:11.139992+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8353024",
    "title": "Assistant General Counsel, Business & Legal Affairs",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8353024?gh_jid=8353024",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:41:11.139992+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8261023",
    "title": "Assistant General Counsel, Legal & Business Affairs - Ad Tech & Media Transactions",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8261023?gh_jid=8261023",
    "posted_date": "2026-10-07",
    "updated_date": "2026-10-26",
    "fetched_at": "2026-11-06T00:41:11.139992+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  }
]
```

## Block / Square

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/block/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.181s
- Company elapsed time: 0.751s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 197
- After US/location filtering: 179
- With trustworthy posted_date: 179
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5108007008",
    "title": "Applied Research Intern, Proactive Intelligence & Customer World Models (PhD / Graduate Co-op)",
    "location": "Bay Area, CA, United States of America; CA - ON - Toronto - Remote",
    "official_url": "http://block.xyz/careers/jobs/5108007008?gh_jid=5108007008",
    "posted_date": "2026-06-09",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:41:11.565779+00:00",
    "date_confidence": "high",
    "description": "<p><strong>Team:</strong> Apollo — Block Applied R&amp;D<br><strong>Location:</strong> Remote (US / Canada)<br><strong>Duration:</strong> Fall/Winter 2026 co-op — 8 months, flexibl"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5422288008",
    "title": "B2B Content Marketing Lead",
    "location": "Bay Area, CA, United States of America; US - CA - Oakland City - Remote",
    "official_url": "http://block.xyz/careers/jobs/5422288008?gh_jid=5422288008",
    "posted_date": "2026-09-11",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:41:11.565779+00:00",
    "date_confidence": "high",
    "description": "<p>Since we opened our doors in 2009, the world of commerce has evolved immensely, and so has Square. After enabling anyone to take payments and never miss a sale, we saw sellers s"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5466280008",
    "title": "Bilingual Implementation Specialist",
    "location": "Los Angeles, CA, United States of America; US - NY - NYC - Remote",
    "official_url": "http://block.xyz/careers/jobs/5466280008?gh_jid=5466280008",
    "posted_date": "2026-10-28",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-06T00:41:11.565779+00:00",
    "date_confidence": "high",
    "description": "<h3><strong>Overview&nbsp;</strong></h3> <p>The Global Seller Onboarding team works directly with sellers and internal teams to ensure they are able to take full advantage of Squar"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5442638008",
    "title": "Bilingual Mandarin Business Development Rep",
    "location": "Melbourne, Australia; AU - VIC - Collins",
    "official_url": "http://block.xyz/careers/jobs/5442638008?gh_jid=5442638008",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:41:11.565779+00:00",
    "date_confidence": "high",
    "description": "<p>Square is looking for high-energy, motivated professionals with sound business insight and natural sales instincts. You will be joining our Restaurant or Generalist team to help"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5442639008",
    "title": "Bilingual Mandarin Business Development Rep",
    "location": "Melbourne, Australia; AU - VIC - Collins",
    "official_url": "http://block.xyz/careers/jobs/5442639008?gh_jid=5442639008",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:41:11.565779+00:00",
    "date_confidence": "high",
    "description": "<p>Square is looking for high-energy, motivated professionals with sound business insight and natural sales instincts. You will be joining our Restaurant or Generalist team to help"
  }
]
```

## Tesla

- Status: expected_limitation
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 0 / 0.000s
- Company elapsed time: 0.000s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

## Two Sigma

- Status: ok
- Scraping method: HTTP GET Avature SearchJobs HTML + JobDetail HTML
- Search URL/API: `https://careers.twosigma.com/careers/OpenRoles?search=software+engineer&jobRecordsPerPage=10&jobOffset=0`
- Pagination: jobOffset=0,10,... ; stop on empty/repeat or short page
- Pages/requests fetched: 17
- HTTP requests/cumulative request time: 59 / 64.659s
- Company elapsed time: 73.789s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 42 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 42}
- Relevant JD recovery: {'eligible': 37, 'usable_jd': 37}
- Raw jobs found: 117
- After US/location filtering: 42
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.291, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 12.503, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 2.248, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 5.755, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 20.792, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.314, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 1.038, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.742, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 7.107, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 34, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 34}

Sample normalized records:

```json
[
  {
    "company": "Two Sigma",
    "source": "two_sigma_official_careers",
    "job_id": "13079",
    "title": "Quantitative Software Engineer: Generative AI",
    "location": "United States - NY New York",
    "official_url": "https://careers.twosigma.com/careers/JobDetail/New-York-City-United-States-Quantitative-Software-Engineer-Generative-AI/13079",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:12.317442+00:00",
    "date_confidence": "unknown",
    "description": "Two Sigma is a leading quantitative investment management and trading firm. The company applies a scientific approach to investing, combining cutting-edge technology, artificial in"
  },
  {
    "company": "Two Sigma",
    "source": "two_sigma_official_careers",
    "job_id": "14102",
    "title": "AI Solutions Developer",
    "location": "United States - NY New York",
    "official_url": "https://careers.twosigma.com/careers/JobDetail/New-York-New-York-United-States-AI-Solutions-Developer/14102",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:12.317442+00:00",
    "date_confidence": "unknown",
    "description": "Two Sigma is a leading quantitative investment management and trading firm. The company applies a scientific approach to investing, combining cutting-edge technology, artificial in"
  },
  {
    "company": "Two Sigma",
    "source": "two_sigma_official_careers",
    "job_id": "14291",
    "title": "AI Fluency: Program Manager",
    "location": "United States - NY New York",
    "official_url": "https://careers.twosigma.com/careers/JobDetail/New-York-United-States-AI-Fluency-Program-Manager/14291",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:12.317442+00:00",
    "date_confidence": "unknown",
    "description": "Two Sigma is a leading quantitative investment management and trading firm. The company applies a scientific approach to investing, combining cutting-edge technology, artificial in"
  },
  {
    "company": "Two Sigma",
    "source": "two_sigma_official_careers",
    "job_id": "14096",
    "title": "AI Research Scientist - Intern [2027 Summer]",
    "location": "United States - NY New York",
    "official_url": "https://careers.twosigma.com/careers/JobDetail/New-York-New-York-United-States-AI-Research-Scientist-Intern-2027-Summer/14096",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:12.317442+00:00",
    "date_confidence": "unknown",
    "description": "Two Sigma is a financial sciences company, combining data analysis, invention, and rigorous inquiry to help solve the toughest challenges in investment management, securities, priv"
  },
  {
    "company": "Two Sigma",
    "source": "two_sigma_official_careers",
    "job_id": "13671",
    "title": "AI Research Scientist - Campus Full-Time",
    "location": "United States - NY New York",
    "official_url": "https://careers.twosigma.com/careers/JobDetail/New-York-New-York-United-States-AI-Research-Scientist-Campus-Full-Time/13671",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:12.317442+00:00",
    "date_confidence": "unknown",
    "description": "Two Sigma is a leading quantitative investment management and trading firm. The company applies a scientific approach to investing, combining cutting-edge technology, artificial in"
  }
]
```

## Verkada

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/verkada/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.283s
- Company elapsed time: 0.900s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 56, 'usable_jd': 56}
- Raw jobs found: 345
- After US/location filtering: 279
- With trustworthy posted_date: 279
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Verkada",
    "source": "verkada_official_careers",
    "job_id": "4248001007",
    "title": "Account Executive, Select, Austin",
    "location": "Austin, TX United States; Austin office",
    "official_url": "https://job-boards.greenhouse.io/verkada/jobs/4248001007",
    "posted_date": "2025-02-21",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:41:31.889113+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><strong>Who We Are</strong></h3> <p>Verkada is transforming how organizations protect their people and places with an integrated, privacy-sensitive A"
  },
  {
    "company": "Verkada",
    "source": "verkada_official_careers",
    "job_id": "4248006007",
    "title": "Account Executive, Select, New York City (Mid-Market)",
    "location": "New York City, NY United States; New York City office",
    "official_url": "https://job-boards.greenhouse.io/verkada/jobs/4248006007",
    "posted_date": "2026-07-28",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:41:31.889113+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><strong>Who We Are</strong></h3> <p>Verkada is transforming how organizations protect their people and places with an integrated, privacy-sensitive A"
  },
  {
    "company": "Verkada",
    "source": "verkada_official_careers",
    "job_id": "4247993007",
    "title": "Account Executive, Select, Phoenix",
    "location": "Phoenix, AZ United States; Phoenix office",
    "official_url": "https://job-boards.greenhouse.io/verkada/jobs/4247993007",
    "posted_date": "2026-03-31",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:41:31.889113+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><strong>Who We Are</strong></h3> <p>Verkada is transforming how organizations protect their people and places with an integrated, privacy-sensitive A"
  },
  {
    "company": "Verkada",
    "source": "verkada_official_careers",
    "job_id": "4247996007",
    "title": "Account Executive, Select, Salt Lake City (Mid-Market)",
    "location": "Salt Lake City, UT United States; Salt Lake City office",
    "official_url": "https://job-boards.greenhouse.io/verkada/jobs/4247996007",
    "posted_date": "2025-09-23",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:41:31.889113+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><strong>Who We Are</strong></h3> <p>Verkada is transforming how organizations protect their people and places with an integrated, privacy-sensitive A"
  },
  {
    "company": "Verkada",
    "source": "verkada_official_careers",
    "job_id": "4388198007",
    "title": "Account Executive, Select, San Mateo",
    "location": "San Mateo, CA United States; San Mateo, California, United States",
    "official_url": "https://job-boards.greenhouse.io/verkada/jobs/4388198007",
    "posted_date": "2024-06-07",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:41:31.889113+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><strong>Who We Are</strong></h3> <p>Verkada is transforming how organizations protect their people and places with an integrated, privacy-sensitive A"
  }
]
```

## Visa

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://visa.wd5.myworkdayjobs.com/Visa`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 23
- HTTP requests/cumulative request time: 153 / 67.621s
- Company elapsed time: 88.324s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 129 / 0 / 0
- Detail cache statuses: {'fetched:new': 129}
- Relevant JD recovery: {'eligible': 31, 'usable_jd': 31}
- Raw jobs found: 360
- After US/location filtering: 129
- With trustworthy posted_date: 129
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 34.456, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.017, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 6.946, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 12.949, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.94, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.039, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.389, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.959, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 4.853, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF084840W",
    "title": "Lead Software Engineer",
    "location": "US - Bellevue, WA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Bellevue-WA/Lead-Software-Engineer_REF084840W",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:32.790562+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF089579W",
    "title": "ML Production Engineer, Sr Consultant",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/ML-Engineer-Sr-Consultant_REF089579W",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:32.790562+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088549W",
    "title": "Software Engineer",
    "location": "US - Foster City, CA; US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Software-Engineer_REF088549W",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:32.790562+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF084915W",
    "title": "Manager, Orchestration & Integration Product Management",
    "location": "US - Foster City, CA; US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Manager--Orchestration---Integration-Product-Management_REF084915W",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:32.790562+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088349W",
    "title": "Sr. Data Engineer",
    "location": "US - Bellevue, WA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Bellevue-WA/Sr-Data-Engineer_REF088349W",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:32.790562+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  }
]
```

## WeRide

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/weride`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.388s
- Company elapsed time: 0.396s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 12
- After US/location filtering: 10
- With trustworthy posted_date: 10
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "012c818d-4ad8-4096-80b0-386cdf79f8d5",
    "title": "Forward Deployed Engineer",
    "location": "One-north",
    "official_url": "https://jobs.lever.co/weride/012c818d-4ad8-4096-80b0-386cdf79f8d5",
    "posted_date": "2024-03-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.550056+00:00",
    "date_confidence": "high",
    "description": "Act as a frontline technical owner for the deployment and operation of L4 autonomous driving systems in real-world environments Lead and execute system-level testing and validation"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "2f22df18-e019-450e-bcfa-9b1c7b94334f",
    "title": "General Software Engineer",
    "location": "San Jose, CA",
    "official_url": "https://jobs.lever.co/weride/2f22df18-e019-450e-bcfa-9b1c7b94334f",
    "posted_date": "2020-05-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.550056+00:00",
    "date_confidence": "high",
    "description": "BS/MS/PhD degree in Robotics, Computer Science, Electrical Engineering or equivalent practical experience. Experience in data structures and advanced algorithms Experience programm"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "109627b8-e5d0-4ca0-812d-15aaea6c6478",
    "title": "Global Technical Project Manager",
    "location": "One-north",
    "official_url": "https://jobs.lever.co/weride/109627b8-e5d0-4ca0-812d-15aaea6c6478",
    "posted_date": "2024-07-09",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.550056+00:00",
    "date_confidence": "high",
    "description": "Own end-to-end project delivery as the single accountable owner (DRI), ensuring success across scope, schedule, cost, and quality Lead the full project lifecycle from pre-sales thr"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "e151540c-f52c-4797-afef-6235f3ec8edc",
    "title": "Motion Planning Engineer",
    "location": "San Jose, CA",
    "official_url": "https://jobs.lever.co/weride/e151540c-f52c-4797-afef-6235f3ec8edc",
    "posted_date": "2020-05-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.550056+00:00",
    "date_confidence": "high",
    "description": "Building/Integrating software and algorithms for path planning, behavioral planning and vehicle control Developing/Implementing/Evaluating/Launching algorithms in Robotic motion pl"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "5cde0d09-ba2d-408d-947e-4a42028cd4f7",
    "title": "New Grads 2027 - Software Engineer - Perception/Computer Vision",
    "location": "San Jose, CA",
    "official_url": "https://jobs.lever.co/weride/5cde0d09-ba2d-408d-947e-4a42028cd4f7",
    "posted_date": "2026-08-10",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.550056+00:00",
    "date_confidence": "high",
    "description": "Team Introduction: The AI team is responsible for developing CV/ML algorithms to understand the surroundings of ego vehicles in real time , including obstacle detection, online map"
  }
]
```

## Workday

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://workday.wd5.myworkdayjobs.com/Workday`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 23
- HTTP requests/cumulative request time: 144 / 97.412s
- Company elapsed time: 117.434s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 120 / 0 / 0
- Detail cache statuses: {'fetched:new': 118, 'fetched:changed': 1, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 21, 'usable_jd': 21}
- Raw jobs found: 441
- After US/location filtering: 120
- With trustworthy posted_date: 120
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 49.112, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 76, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.964, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 2.404, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 21.781, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.399, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.513, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.583, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.183, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 10.169, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0110881",
    "title": "AI Engineer",
    "location": "USA, CA, Pleasanton",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CA-Pleasanton/AI-Engineer_JR-0110881",
    "posted_date": "2026-10-14",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.947048+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  },
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0111156",
    "title": "Senior AI Engineer",
    "location": "USA, CA, Pleasanton",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CA-Pleasanton/Senior-AI-Engineer_JR-0111156",
    "posted_date": "2026-10-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.947048+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  },
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0110768",
    "title": "Senior AI Engineer",
    "location": "USA, CA, Pleasanton; Canada, BC, Vancouver",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CA-Pleasanton/Senior-AI-Engineer_JR-0110768",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.947048+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  },
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0109765",
    "title": "Principal Software Engineer, Agentic UX",
    "location": "USA, CA, Pleasanton",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CA-Pleasanton/Principal-AI-UX-Lead_JR-0109765-1",
    "posted_date": "2026-09-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.947048+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  },
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0110688",
    "title": "Sr Manager, AI Engineering",
    "location": "USA, CA, Pleasanton; USA, WA, Seattle",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CA-Pleasanton/Sr-Manager--AI-Engineering_JR-0110688",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:42.947048+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  }
]
```

## Zillow

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 15
- HTTP requests/cumulative request time: 65 / 30.599s
- Company elapsed time: 38.919s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 49 / 0 / 0
- Detail cache statuses: {'fetched:new': 49}
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 212
- After US/location filtering: 49
- With trustworthy posted_date: 49
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.335, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 0.759, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.786, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 2.115, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 3.476, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 3.029, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.719, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.834, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.977, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 19}

Sample normalized records:

```json
[
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751267",
    "title": "Senior AI-Native Product Engineer, Mobile",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Senior-AI-Native-Product-Engineer--Mobile_P751267-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:52.579104+00:00",
    "date_confidence": "high",
    "description": "About the team The Mercury Mobile team builds Zillow Instant Messaging (ZIM) — the conversation layer where millions of movers participate in a multiplayer, integrated experience t"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P747954",
    "title": "Principal Machine Learning Engineer, Agentic AI",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Principal-Machine-Learning-Engineer--Agentic-AI_P747954",
    "posted_date": "2026-10-20",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:52.579104+00:00",
    "date_confidence": "high",
    "description": "About the team The Agentic AI team at Zillow is at the forefront of transforming the real estate industry by helping millions of people use AI assistants to find their next home. W"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751403",
    "title": "Senior Applied Scientist, Shopping AI",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Senior-Applied-Scientist_P751403",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:52.579104+00:00",
    "date_confidence": "high",
    "description": "About the team The Shopping AI team is at the heart of Zillow Group’s mission to create a seamless digital real estate marketplace. We build and own the machine learning systems th"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751533",
    "title": "Principal Product Manager, Agentic AI Platform",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Principal-Product-Manager---Agentic-AI-Platform_P751533-1",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:52.579104+00:00",
    "date_confidence": "high",
    "description": "About the team The Product AI team is building the shared intelligence, capabilities, and foundation that let every Zillow experience become truly agentic, for the people searching"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P747465",
    "title": "Principal Applied Scientist, Generative AI",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Principal-Applied-Scientist--Agentic-AI_P747465",
    "posted_date": "2026-10-20",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:41:52.579104+00:00",
    "date_confidence": "high",
    "description": "About the team The Agentic Foundations team is a focused group of 15–20 applied scientists within Zillow's broader Agentic AI organization, building the foundational AI technologie"
  }
]
```

## Zscaler

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/zscaler/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.230s
- Company elapsed time: 0.924s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 14, 'usable_jd': 14}
- Raw jobs found: 377
- After US/location filtering: 231
- With trustworthy posted_date: 231
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5276812007",
    "title": "Account Executive- Commercial",
    "location": "Mumbai, IND",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5276812007",
    "posted_date": "2026-10-29",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:42:03.525325+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5197814007",
    "title": "Account Executive, Commercial",
    "location": "Landeshauptstadt München, DEU; Remote - Germany",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5197814007",
    "posted_date": "2026-07-31",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:42:03.525325+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5282933007",
    "title": "Account Executive, Commercial - Michigan",
    "location": "Remote - Michigan, USA",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5282933007",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:42:03.525325+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5179814007",
    "title": "Account Executive, Commercial (Nagoya)",
    "location": "Remote - Japan; Osaka, JPN",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5179814007",
    "posted_date": "2026-07-13",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:42:03.525325+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5221105007",
    "title": "Account Executive, Commercial - NorCal",
    "location": "Remote - California, USA",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5221105007",
    "posted_date": "2026-09-01",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-06T00:42:03.525325+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  }
]
```

## Chewy

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://wd5.myworkdaysite.com/recruiting/chewy/External`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 12 / 6.043s
- Company elapsed time: 6.289s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 2 / 0 / 0
- Detail cache statuses: {'fetched:new': 2}
- Relevant JD recovery: {'eligible': 2, 'usable_jd': 2}
- Raw jobs found: 10
- After US/location filtering: 2
- With trustworthy posted_date: 2
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.313, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.486, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.469, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.821, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.569, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.476, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.528, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.491, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.483, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}

Sample normalized records:

```json
[
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R29015",
    "title": "Software Engineer II",
    "location": "USA - MA - Boston - BOS1; USA - MN - Minneapolis - MSP2",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/USA---MA---Boston---BOS1/Software-Engineer-II_R29015",
    "posted_date": "2026-10-29",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:04.449935+00:00",
    "date_confidence": "high",
    "description": "Job Description: Chewy is growing! We’re looking for a Software Engineer II to build and optimize the high-quality Storefront experiences that help millions of pet parents discover"
  },
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R31091",
    "title": "Software Engineer III",
    "location": "USA - MA - Boston - BOS1",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/USA---MA---Boston---BOS1/Software-Engineer-II_R31091",
    "posted_date": "2026-10-26",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:04.449935+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity: Chewy is seeking Senior Software Engineer, Level III in Boston, MA or Minneapolis MN. Chewy is growing! We’re looking for a Senior Backend Softwar"
  }
]
```

## CVS Health

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 22
- HTTP requests/cumulative request time: 151 / 73.887s
- Company elapsed time: 94.206s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 128 / 0 / 0
- Detail cache statuses: {'fetched:new': 126, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 18, 'usable_jd': 18}
- Raw jobs found: 385
- After US/location filtering: 128
- With trustworthy posted_date: 128
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 43.83, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.576, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 25, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 6.642, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 10.228, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.247, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.65, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.897, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 39, "stop_reason": "early_stop", "unique_contribution": 19, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 0.234, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 3.581, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1089974",
    "title": "Technical Delivery Manager - Digital Engineering",
    "location": "Woonsocket-1 CVS Drive; MS - Work from home; PA - Work from home; NC - Work from home; LA - Work from home; MD - Work from home; ME - Work from home; MN - Work from home; NE - Work from home; MO - Work from home; ND - Work from home; AL - Work from home; NY - Work from hom; NJ - Work from home; OH - Work from hom; SC - Work from home; CT - Work from home; DC - Work from home; FL - Work from home; RI - Work from home; IA - Work from home; AR - Work from home; SD - Work from home; IL - Work from home; VT - Work from home; KS - Work from home; TN - Work from home; VA - Work from home; DE - Work from home; WI - Work from home; GA - Work from home; IN - Work from home; WV - Work from home; KY - Work from home; MI - Work from home; MA - Work from home; NH - Work from home; OK - Work from home",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/Woonsocket-1-CVS-Drive/Technical-Delivery-Manager---Digital-Engineering_R1089974",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:10.740283+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1068486",
    "title": "Sr. Product Manager Digital Health AI",
    "location": "MA - Work from home; Work At Home-Virginia; Work At Home-Georgia; Work At Home-Minnesota; Work At Home-Florida; Work At Home-Pennsylvania; Work At Home-Connecticut; Work At Home-Rhode Island",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/MA---Work-from-home/Sr-Product-Manager-Digital-Health-AI_R1068486-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:10.740283+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R0694233",
    "title": "Principal Cloud Infrastructure Engineer (GCP)",
    "location": "RI - Woonsocket",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/RI---Woonsocket/Principal-Engineer---Cloud-Infrastructure_R0694233",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:10.740283+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1090414",
    "title": "Staff Software Development Engineer",
    "location": "RI - Woonsocket; MS - Work from home; MT - Work from home; NC - Work from home; LA - Work from home; MD - Work from home; ME - Work from home; MN - Work from home; NE - Work from home; MO - Work from home; ND - Work from home; NY - Work from hom; NJ - Work from home; NM - Work from home; NV - Work from home; OH - Work from hom; SC - Work from home; TX - Work from home; RI - Work from home; SD - Work from home; VT - Work from home; TN - Work from home; VA - Work from home; WA - Work from home; UT - Work from home; WI - Work from home; WV - Work from home; OR - Work from home; WY - Work from home; OK - Work from home; PA - Work from home; CO - Work from home; AL - Work from home; AZ - Work from home; CA - Work from home; CT - Work from home; DC - Work from home; FL - Work from home; IA - Work from home; AR - Work from home; ID - Work from home; IL - Work from home; KS - Work from home; DE - Work from home; GA - Work from home; IN - Work from home; KY - Work from home; MI - Work from home; MA - Work from home; NH - Work from home",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/RI---Woonsocket/Staff-Software-Development-Engineer_R1090414",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:10.740283+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1056949",
    "title": "Senior Data Scientist - GenAI",
    "location": "NY - New York",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/NY---New-York/Senior-Data-Scientist---GenAI_R1056949",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:10.740283+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  }
]
```

## Duolingo

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/duolingo/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.187s
- Company elapsed time: 0.299s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 57
- After US/location filtering: 49
- With trustworthy posted_date: 49
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8851677002",
    "title": "Ad Sales Lead, Programmatic",
    "location": "New York, NY; New York, New York, United States",
    "official_url": "https://careers.duolingo.com/jobs/8851677002?gh_jid=8851677002",
    "posted_date": "2026-09-28",
    "updated_date": "2026-11-02",
    "fetched_at": "2026-11-06T00:42:26.107684+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8705196002",
    "title": "Ad Sales Lead - West",
    "location": "Remote - California; Remote",
    "official_url": "https://careers.duolingo.com/jobs/8705196002?gh_jid=8705196002",
    "posted_date": "2026-08-13",
    "updated_date": "2026-11-02",
    "fetched_at": "2026-11-06T00:42:26.107684+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8881612002",
    "title": "AI Research Engineer, New PhD Graduate",
    "location": "New York, NY; Pittsburgh, PA; New York, New York, United States; Pittsburgh, Pennsylvania, United States",
    "official_url": "https://careers.duolingo.com/jobs/8881612002?gh_jid=8881612002",
    "posted_date": "2026-10-12",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-06T00:42:26.107684+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8576434002",
    "title": "Corporate Counsel",
    "location": "Pittsburgh, PA; New York, New York, United States; Pittsburgh, Pennsylvania, United States",
    "official_url": "https://careers.duolingo.com/jobs/8576434002?gh_jid=8576434002",
    "posted_date": "2026-06-03",
    "updated_date": "2026-11-02",
    "fetched_at": "2026-11-06T00:42:26.107684+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8888721002",
    "title": "Data Scientist, Intern",
    "location": "New York, NY; Pittsburgh, PA; New York, New York, United States; Pittsburgh, Pennsylvania, United States",
    "official_url": "https://careers.duolingo.com/jobs/8888721002?gh_jid=8888721002",
    "posted_date": "2026-10-15",
    "updated_date": "2026-11-02",
    "fetched_at": "2026-11-06T00:42:26.107684+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  }
]
```

## Equinix

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.equinix.com/jobs/search`
- Pagination: page=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 16
- HTTP requests/cumulative request time: 22 / 17.426s
- Company elapsed time: 31.942s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 5 / 68
- Detail cache statuses: {'reused': 5}
- Relevant JD recovery: {'deterministic_skip': 42, 'cache_reused': 5, 'eligible': 5, 'ai_skip': 26, 'usable_jd': 5}
- Raw jobs found: 336
- After US/location filtering: 73
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.988, "first_pass_survivors": 41, "group": "official", "jds_resolved": 0, "original_postings_resolved": 41, "page_budget": 2, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 3.098, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 1.468, "first_pass_survivors": 21, "group": "official", "jds_resolved": 0, "original_postings_resolved": 21, "page_budget": 2, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 28, "stop_reason": "early_stop", "unique_contribution": 21, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 0.803, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 2, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 13.57, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.326, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 2.584, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 39, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 2.847, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 39, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 2.259, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 41}

Sample normalized records:

```json
[
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164103",
    "title": "Principal Software Engineer, AI Infrastructure",
    "location": "Burnaby, British Columbia, Canada; Toronto, Ontario, Canada; Montreal, Quebec, Canada; Redwood City, California, United States; Denver, Colorado, United States; Tampa, Florida, United States; New York, United States; Dallas, Texas, United States; Frisco, Texas, United States; Burnaby, British Columbia, Canada; Toronto, Ontario, Canada; Montreal, Quebec, Canada",
    "official_url": "https://careers.equinix.com/jobs/principal-software-engineer-ai-infrastructure-redwood-city-california-united-states-dallas-texas-denver-colorado-frisco-montreal-quebec-canada-new-york-tampa-florida-toronto-ontario-burnaby-b",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:26.407234+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164105",
    "title": "Staff Software Engineer, AI Infrastructure",
    "location": "Redwood City, California, United States",
    "official_url": "https://careers.equinix.com/jobs/staff-software-engineer-ai-infrastructure-redwood-city-california-united-states",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:26.407234+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-163188",
    "title": "Senior Principal Engineer, Enterprise Networking Architecture, Automation and AI",
    "location": "Toronto, Ontario, Canada; Redwood City, California, United States; Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/senior-principal-engineer-enterprise-networking-architecture-automation-and-ai-dallas-texas-united-states-redwood-city-california-toronto-ontario-canada",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:26.407234+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164127",
    "title": "Principal Product Manager, AI Infrastructure",
    "location": "Toronto, Ontario, Canada; Redwood City, California, United States; Denver, Colorado, United States; Tampa, Florida, United States; New York, United States; Dallas, Texas, United States; Toronto, Ontario, Canada; Redwood City, California, United States; Denver, Colorado, United States",
    "official_url": "https://careers.equinix.com/jobs/principal-product-manager-ai-infrastructure-redwood-city-california-united-states-dallas-texas-denver-colorado-new-york-tampa-florida-toronto-ontario-canada",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:26.407234+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164181",
    "title": "Senior Director AI, Chief Revenue Organization",
    "location": "Toronto, Ontario, Canada; Redwood City, California, United States; Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/senior-director-ai-chief-revenue-organization-redwood-city-california-united-states-dallas-texas-toronto-ontario-canada-d1df2661-4334-450c-be5d-6f9429061430",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:26.407234+00:00",
    "date_confidence": "unknown",
    "description": ""
  }
]
```

## F5

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ffive.wd5.myworkdayjobs.com/f5jobs`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 16 / 8.158s
- Company elapsed time: 9.533s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 1, 'usable_jd': 1}
- Raw jobs found: 123
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.83, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.606, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.434, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.181, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.161, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.271, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.574, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.503, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.249, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

Sample normalized records:

```json
[
  {
    "company": "F5",
    "source": "f5_official_careers",
    "job_id": "RP1037604",
    "title": "Mgr, Software Development Engineering",
    "location": "Seattle",
    "official_url": "https://ffive.wd5.myworkdayjobs.com/f5jobs/job/Seattle/Mgr--Software-Development-Engineering_RP1037604",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:31.499429+00:00",
    "date_confidence": "high",
    "description": "At F5, we strive to bring a better digital world to life. Our teams empower organizations across the globe to create, secure, and run applications that enhance how we experience ou"
  }
]
```

## IXL Learning

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/ixllearning/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.162s
- Company elapsed time: 0.319s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 55, 'usable_jd': 55}
- Raw jobs found: 115
- After US/location filtering: 101
- With trustworthy posted_date: 101
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8881521002",
    "title": "Administrative Assistant",
    "location": "San Mateo, CA; San Mateo, California, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8881521002",
    "posted_date": "2026-10-09",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-06T00:42:41.033493+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide, is looking for an Administrative Assistant to support the execut"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8765546002",
    "title": "American English Language Tutor, Rosetta Stone (PT)",
    "location": "United States; Remote - US",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8765546002",
    "posted_date": "2026-09-01",
    "updated_date": "2026-10-21",
    "fetched_at": "2026-11-06T00:42:41.033493+00:00",
    "date_confidence": "high",
    "description": "<p><span style=\"font-weight: 400;\">IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide, is seeking a US English Language"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8531284002",
    "title": "Associate Curriculum Alignment Specialist",
    "location": "Raleigh, NC; Morrisville, North Carolina, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8531284002",
    "posted_date": "2026-04-30",
    "updated_date": "2026-10-13",
    "fetched_at": "2026-11-06T00:42:41.033493+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide, is seeking an Associate Curriculum Alignment Specialist to join "
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8856961002",
    "title": "Associate Digital Designer",
    "location": "San Mateo, CA; San Mateo, California, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8856961002",
    "posted_date": "2026-10-13",
    "updated_date": "2026-10-13",
    "fetched_at": "2026-11-06T00:42:41.033493+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is seeking an enthusiastic, highly motivated Associate Digital Designer to join ou"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8634621002",
    "title": "Associate Educational Sales Consultant, Inside Sales",
    "location": "Raleigh, NC; Morrisville, North Carolina, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8634621002",
    "posted_date": "2026-07-15",
    "updated_date": "2026-10-22",
    "fetched_at": "2026-11-06T00:42:41.033493+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide, is seeking an upbeat, focused, high-energy individual to join ou"
  }
]
```

## Wayfair

- Status: expected_limitation
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 0 / 0.000s
- Company elapsed time: 0.000s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

## Wells Fargo

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://wf.wd1.myworkdayjobs.com/WellsFargoJobs`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 89 / 52.874s
- Company elapsed time: 64.886s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 69 / 0 / 0
- Detail cache statuses: {'fetched:new': 67, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 268
- After US/location filtering: 69
- With trustworthy posted_date: 69
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.639, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 2.101, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.922, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 14.174, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 47, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 47}
- Query diagnostic: {"elapsed_seconds": 7.314, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.183, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 56, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 1.068, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 1.045, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 3.155, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 47, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 47}

Sample normalized records:

```json
[
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-577897",
    "title": "Lead AI Engineer",
    "location": "CHARLOTTE, NC; BOSTON, MA",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Lead-AI-Engineer_R-577897",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:41.353442+00:00",
    "date_confidence": "high",
    "description": "Wells Fargo is seeking a Lead Ai Engineer in Technology as part of Commercial and Corporate & Investment Banking Technology (CCIBT).). The primary focus of this group will be to le"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-584220",
    "title": "Principal AI Engineer – Enterprise Generative AI",
    "location": "CHARLOTTE, NC; IRVING, TX",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Principal-AI-Engineer---Enterprise-Generative-AI_R-584220",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:41.353442+00:00",
    "date_confidence": "high",
    "description": "Wells Fargo is seeking a Principal AI Engineer to serve as a senior technical leader driving the design, scale, and operationalize of enterprise Generative AI solutions across the "
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-584601",
    "title": "Principal Engineer - AI Enablement & Adoption",
    "location": "ISELIN, NJ; IRVING, TX; CHARLOTTE, NC",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/ISELIN-NJ/Principal-Engineer---AI-Enablement---Adoption_R-584601",
    "posted_date": "2026-10-29",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:41.353442+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Principal Engineer, AI Enablement & Adoption to help accelerate the responsible and practical adoption of Artificial Intelligence across t"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-584380",
    "title": "Principal Engineer",
    "location": "CHARLOTTE, NC; IRVING, TX",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Principal-Engineer_R-584380",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:41.353442+00:00",
    "date_confidence": "high",
    "description": "About this role: The Equipment & Vendor Finance business enables commercial clients to acquire, lease, and manage capital equipment through flexible financing solutions. Software e"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-583066",
    "title": "2027 Technology Summer Internship – Early Careers (Data Engineering)",
    "location": "CHARLOTTE, NC; IRVING, TX; ISELIN, NJ",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/XMLNAME-2027-Technology-Summer-Internship---Early-Careers--Data-Engineering-_R-583066",
    "posted_date": "2026-10-26",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:41.353442+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking aspiring Data Engineers to join the 2027 Technology Internship Program. Program Overview: The Wells Fargo Technology Internship Program prov"
  }
]
```

## Yahoo

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ouryahoo.wd5.myworkdayjobs.com/careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 15
- HTTP requests/cumulative request time: 64 / 29.753s
- Company elapsed time: 37.979s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 48 / 0 / 0
- Detail cache statuses: {'fetched:new': 47, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 191
- After US/location filtering: 48
- With trustworthy posted_date: 48
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 23.531, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 0.807, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.717, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 4.177, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 3.05, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 46}
- Query diagnostic: {"elapsed_seconds": 2.672, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 0.702, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.687, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.753, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}

Sample normalized records:

```json
[
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0026993",
    "title": "Senior Staff AI/ML Engineer / Architect - Yahoo Mail",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Senior-Principal-AI-ML-Architect--Yahoo-Mail_JR0026993",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:58.350378+00:00",
    "date_confidence": "high",
    "description": "Yahoo Mail is the ultimate consumer inbox with hundreds of millions of users. It’s the best way to access your email and stay organized from a computer, phone or tablet. With its b"
  },
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0027479",
    "title": "Senior Manager, HR AI Strategy & Governance",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Senior-Manager--HR-AI-Strategy---Governance_JR0027479",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:58.350378+00:00",
    "date_confidence": "high",
    "description": "Yahoo serves as a trusted guide for hundreds of millions of people globally, helping them achieve their goals online through our portfolio of iconic products. For advertisers, Yaho"
  },
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0027182",
    "title": "Senior Research Scientist",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Principal-Applied-Research-Scientist---Generative-AI-and-NLP_JR0027182",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:58.350378+00:00",
    "date_confidence": "high",
    "description": "Yahoo Mail is the ultimate consumer inbox with hundreds of millions of users. It’s the best way to access your email and stay organized from a computer, phone or tablet. With its b"
  },
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0027543",
    "title": "Director, Transaction & Revenue Systems",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Director--Transaction---Revenue-Systems_JR0027543",
    "posted_date": "2026-10-16",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:58.350378+00:00",
    "date_confidence": "high",
    "description": "Yahoo serves as a trusted guide for hundreds of millions of people globally, helping them achieve their goals online through our portfolio of iconic products. For advertisers, Yaho"
  },
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0027468",
    "title": "Lead Quality Engineer",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Lead-Quality-Engineer_JR0027468",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:42:58.350378+00:00",
    "date_confidence": "high",
    "description": "Yahoo Sports is one of the internet’s leading destinations for comprehensive sports news and innovative fantasy games. We produce insightful content across multiple platforms and c"
  }
]
```

## Ansys

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.synopsys.com/search-jobs`
- Pagination: p=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 3
- HTTP requests/cumulative request time: 23 / 7.488s
- Company elapsed time: 10.513s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 20 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 45
- After US/location filtering: 20
- With trustworthy posted_date: 20
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.513, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "Ansys", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 45}

Sample normalized records:

```json
[
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "102570969840",
    "title": "Applications Engineer - Staff",
    "location": "Sunnyvale, California",
    "official_url": "https://careers.synopsys.com/job/sunnyvale/applications-engineer-staff/44408/102570969840",
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:01.115996+00:00",
    "date_confidence": "high",
    "description": "We Are: At Synopsys, we drive the innovations that shape the way we live and connect. Our technology is central to the Era of Pervasive Intelligence, from self-driving cars to lear"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "101056156880",
    "title": "Mission Systems Engineer",
    "location": "DC",
    "official_url": "https://careers.synopsys.com/job/dc/mission-systems-engineer/44408/101056156880",
    "posted_date": "2026-09-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:01.115996+00:00",
    "date_confidence": "high",
    "description": "We Are: At Synopsys, we drive the innovations that shape the way we live and connect. Our technology is central to the Era of Pervasive Intelligence, from self-driving cars to lear"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "99804907584",
    "title": "Technical Support Engineer - High Frequency Electromagnetics",
    "location": "Chalandri, Greece",
    "official_url": "https://careers.synopsys.com/job/chalandri/technical-support-engineer-high-frequency-electromagnetics/44408/99804907584",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:01.115996+00:00",
    "date_confidence": "high",
    "description": "We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling customers to rapidly innovate AI-powered products. We deliver industry-leading silicon desi"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "100737605136",
    "title": "Applications Engineering, Staff Engineer",
    "location": "Sunnyvale, California",
    "official_url": "https://careers.synopsys.com/job/sunnyvale/applications-engineering-staff-engineer/44408/100737605136",
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:01.115996+00:00",
    "date_confidence": "high",
    "description": "We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling customers to rapidly innovate AI-powered products. We deliver industry-leading silicon desi"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "102570969856",
    "title": "Senior Staff Applications Engineer, Electromagnetics",
    "location": "United States Off-site",
    "official_url": "https://careers.synopsys.com/job/sunnyvale/senior-staff-applications-engineer-electromagnetics/44408/102570969856",
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:01.115996+00:00",
    "date_confidence": "high",
    "description": "We Are: At Synopsys, we drive the innovations that shape the way we live and connect. Our technology is central to the Era of Pervasive Intelligence, from self-driving cars to lear"
  }
]
```

## Blizzard Entertainment

- Status: expected_limitation
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 0 / 0.000s
- Company elapsed time: 0.000s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

## Flex

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://flextronics.wd1.myworkdayjobs.com/Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 16
- HTTP requests/cumulative request time: 127 / 52.918s
- Company elapsed time: 68.703s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 110 / 0 / 0
- Detail cache statuses: {'fetched:new': 110}
- Relevant JD recovery: {'eligible': 89, 'usable_jd': 89}
- Raw jobs found: 185
- After US/location filtering: 110
- With trustworthy posted_date: 110
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 18.499, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 33, "stop_reason": "early_stop", "unique_contribution": 33, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 1.108, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 1.041, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 4.03, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 20.52, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.213, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 1.25, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.162, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 16.712, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 63, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 63}

Sample normalized records:

```json
[
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD231256",
    "title": "LV Switchgear Assembler",
    "location": "USA, CA, Fontana",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-CA-Fontana/LV-Switchgear-Assembler_WD231256-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:11.631521+00:00",
    "date_confidence": "high",
    "description": "Crown Technical Systems, a Flex Company, is a leader in power distribution and protection systems concentrating on sophisticated, state-of-the-art relay and control panels, medium "
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD233612",
    "title": "Material Handler - LV Switchgear (2nd Shift)",
    "location": "USA, CA, Fontana",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-CA-Fontana/Material-Handler---LV-Switchgear--2nd-Shift-_WD233612-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:11.631521+00:00",
    "date_confidence": "high",
    "description": "Crown Technical Systems, a Flex Company, is a leader in power distribution and protection systems concentrating on sophisticated, state-of-the-art relay and control panels, medium "
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD233476",
    "title": "Mechanical engineer",
    "location": "USA, CA, Milpitas",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-CA-Milpitas/Mechanical-engineer_WD233476",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:11.631521+00:00",
    "date_confidence": "high",
    "description": "Axiom builds the digital and electrical infrastructure powering the AI era. We design, build and deploy integrated power, thermal and compute solutions that help data centers, util"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD232752",
    "title": "Debug Technician | A Shift",
    "location": "USA, UT, Salt Lake City",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-UT-Salt-Lake-City/Debug-Technician-3_WD232752",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:11.631521+00:00",
    "date_confidence": "high",
    "description": "Axiom builds the digital and electrical infrastructure powering the AI era. We design, build and deploy integrated power, thermal and compute solutions that help data centers, util"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD232319",
    "title": "Director, Compensation",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Director--Compensation_WD232319",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:11.631521+00:00",
    "date_confidence": "high",
    "description": "Axiom builds the digital and electrical infrastructure powering the AI era. We design, build and deploy integrated power, thermal and compute solutions that help data centers, util"
  }
]
```

## IQVIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://iqvia.wd1.myworkdayjobs.com/IQVIA`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 23 / 15.549s
- Company elapsed time: 17.153s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 13 / 0 / 0
- Detail cache statuses: {'fetched:new': 13}
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 42
- After US/location filtering: 13
- With trustworthy posted_date: 13
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.177, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 0.963, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.849, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 5.513, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.934, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.864, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.938, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.902, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.884, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}

Sample normalized records:

```json
[
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1563456",
    "title": "Director, AI Platform Engineering & DevOps",
    "location": "Wayne, PA, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Wayne-PA-United-States-of-America/Director--AI-Platform-Engineering---DevOps_R1563456",
    "posted_date": "2026-10-19",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:36.330460+00:00",
    "date_confidence": "high",
    "description": "The Director, AI Platform Engineering & DevOp s will be responsible for leading the strategy, architecture, engineering, and operational enablement of enterprise AI, Kubernetes, GP"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1562238",
    "title": "Healthcare Analytics, AI Product & Methodology Analyst",
    "location": "Greenwich, CT, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Greenwich-CT-United-States-of-America/Healthcare-Analytics--AI-Product---Methodology-Analyst_R1562238",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:36.330460+00:00",
    "date_confidence": "high",
    "description": "About Cedar Gate Technologies Cedar Gate Technologies, an IQVIA business, enables payers, providers, employers, and service administrators to excel at value-based care with a unifi"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1561755",
    "title": "Software QA Engineer 2",
    "location": "Greenwich, CT, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Greenwich-CT-United-States-of-America/Software-QA-Engineer-2_R1561755",
    "posted_date": "2026-10-26",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:36.330460+00:00",
    "date_confidence": "high",
    "description": "About Cedar Gate Technologies Cedar Gate Technologies, an IQVIA business, enables payers, providers, employers, and service administrators to excel at value-based care with a unifi"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1526366",
    "title": "Senior Software Engineer (React), IQVIA Digital",
    "location": "Red Bank, NJ, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Red-Bank-NJ-United-States-of-America/Senior-Software-Engineer_R1526366",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:36.330460+00:00",
    "date_confidence": "high",
    "description": "IQVIA Digital Overview: IQVIA Digital powers exceptional brand experiences, delivering innovative solutions based on a customer-first, insights-driven, and integrated omnichannel v"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1563204",
    "title": "Director of Product- Media OS Activation, IQVIA Digital",
    "location": "Wayne, PA, United States of America; Orlando, FL; Washington, DC; Atlanta, GA; Hartford, CT; Chicago, IL; Miami, FL; Philadelphia, PA; Newark, NJ; Austin, TX; New York, NY",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Wayne-PA-United-States-of-America/Director-of-Product--Media-OS-Activation--IQVIA-Digital_R1563204",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:36.330460+00:00",
    "date_confidence": "high",
    "description": "About IQVIA Digital IQVIA Digital powers exceptional brand experiences, delivering innovative solutions based on a customer-first, insights-driven, and integrated omnichannel visio"
  }
]
```

## Johnson & Johnson

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://jj.wd5.myworkdayjobs.com/JJ`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 22
- HTTP requests/cumulative request time: 219 / 96.773s
- Company elapsed time: 125.992s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 196 / 0 / 0
- Detail cache statuses: {'fetched:new': 195, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 46, 'usable_jd': 46}
- Raw jobs found: 413
- After US/location filtering: 196
- With trustworthy posted_date: 196
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 33.318, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.997, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 39, "stop_reason": "early_stop", "unique_contribution": 20, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 25.982, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.513, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.82, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.128, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.887, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.298, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 7.696, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-106627",
    "title": "Director, Data & AI Platforms",
    "location": "Raritan, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raritan-New-Jersey-United-States-of-America/Director--Data---AI-Platforms_R-106627-2",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:40.382145+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-109033",
    "title": "Engineering Technician V",
    "location": "Jacksonville, Florida, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Jacksonville-Florida-United-States-of-America/Engineering-Technician-V_R-109033",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:40.382145+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-109103",
    "title": "Engineer",
    "location": "Jacksonville, Florida, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Jacksonville-Florida-United-States-of-America/Engineer_R-109103",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:40.382145+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-108805",
    "title": "Director, External Innovation, DPDS (Biology Technologies) – 2 openings",
    "location": "Cambridge, Massachusetts, United States of America; South San Francisco, California, United States of America; La Jolla, California, United States of America; Spring House, Pennsylvania, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Cambridge-Massachusetts-United-States-of-America/Director--External-Innovation--DPDS--Biology-Technologies----2-openings_R-108805-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:40.382145+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-107848",
    "title": "Supply Chain Collaboration (SCC) Manager, Solutions Enablement",
    "location": "Raritan, New Jersey, United States of America; Santa Clara, California, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raritan-New-Jersey-United-States-of-America/Supply-Chain-Collaboration--SCC--Manager--Solutions-Enablement_R-107848-2",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:40.382145+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  }
]
```

## Nasdaq

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 27 / 12.097s
- Company elapsed time: 14.200s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 17 / 0 / 0
- Detail cache statuses: {'fetched:new': 17}
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 75
- After US/location filtering: 17
- With trustworthy posted_date: 17
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 6.224, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.59, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.689, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.592, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.958, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 0.598, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.605, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 0.601, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.615, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 16}

Sample normalized records:

```json
[
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0025386",
    "title": "Director, AI Engineering & Automation",
    "location": "USA - New York City - New York",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---New-York-City---New-York/AI-Product-Owner---Corporate-Finance_R0025386",
    "posted_date": "2026-06-08",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:44.947385+00:00",
    "date_confidence": "high",
    "description": "As a Director, AI Engineering & Automation , you will be accountable for leading the execution of the AI strategy within our Corporate Finance Division. This role requires a proven"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0024206",
    "title": "Senior AI Application Engineer (.NET)",
    "location": "USA - Atlanta - Georgia",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---Atlanta---Georgia/AI-Engineer_R0024206-1",
    "posted_date": "2026-10-13",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:44.947385+00:00",
    "date_confidence": "high",
    "description": "We're looking for a Senior AI Application Engineer (.NET) to design, build, and scale intelligent enterprise applications. This role is ideal for an experienced C#/.NET software en"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026613",
    "title": "AI / DevOps Engineer – Agentic Systems & Automation",
    "location": "USA - New York City - New York; USA - Philadelphia - Pennsylvania",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---New-York-City---New-York/AI---DevOps-Engineer---Agentic-Systems---Automation_R0026613",
    "posted_date": "2026-09-23",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:44.947385+00:00",
    "date_confidence": "high",
    "description": "s a Lead DevOps Engineer reporting to the AVP – Systems and Network Administration, you'll play a critical role in building and operating intelligent automation platforms, AI agent"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026782",
    "title": "Software Engineer - Cloud Solutions & Applied AI",
    "location": "USA - Boston - Massachusetts",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---Boston---Massachusetts/Software-Engineer---Cloud-Solutions---AI_R0026782",
    "posted_date": "2026-10-12",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:44.947385+00:00",
    "date_confidence": "high",
    "description": "As a Software Engineer reporting to the Senior Director of Software Engineering, you'll play a key role in building and improving the Nasdaq Questionnaires platform — a SaaS soluti"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026713",
    "title": "Lead Engineer, Platform Engineering & Reliability",
    "location": "USA - Atlanta - Georgia",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---Atlanta---Georgia/Lead-Engineer--Platform-Engineering---Reliability_R0026713",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:44.947385+00:00",
    "date_confidence": "high",
    "description": "As a Lead Engineer reporting to the AVP of Software Engineering, you'll play a critical role in shaping the cloud, platform, and reliability engineering foundation that powers Nasd"
  }
]
```

## PointClickCare

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/pointclickcare`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 2 / 1.002s
- Company elapsed time: 1.045s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 1 / 7 / 42
- Detail cache statuses: {'reused': 7}
- Relevant JD recovery: {'deterministic_skip': 36, 'eligible': 13, 'cache_reused': 7, 'ai_skip': 6, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 12}
- Raw jobs found: 80
- After US/location filtering: 74
- With trustworthy posted_date: 74
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "ccdecc93-aef2-4b2b-a981-6843f3c16221",
    "title": "(Canada) Principal ML System Engineer",
    "location": "Remote or Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/ccdecc93-aef2-4b2b-a981-6843f3c16221",
    "posted_date": "2026-08-13",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.240571+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "76cdab93-644a-47d6-a89d-9c4add288692",
    "title": "(Canada) Sales Development Representative (6 month contract)",
    "location": "Remote or Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/76cdab93-644a-47d6-a89d-9c4add288692",
    "posted_date": "2026-10-13",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.240571+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "6b7f5c7a-372b-4a4a-8187-b2c347157e14",
    "title": "(Canada) Software Implementation Consultant - Clinical",
    "location": "Remote or Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/6b7f5c7a-372b-4a4a-8187-b2c347157e14",
    "posted_date": "2026-07-09",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.240571+00:00",
    "date_confidence": "high",
    "description": "Principal implementation liaison on the project team documenting customer requirements, translating technical requirements into configuration setup, business processes and goals Le"
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "423445e1-953c-45e2-a9ac-ce46598c89d7",
    "title": "(US) Principal ML System Engineer",
    "location": "Remote, USA",
    "official_url": "https://jobs.lever.co/pointclickcare/423445e1-953c-45e2-a9ac-ce46598c89d7",
    "posted_date": "2026-08-13",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.240571+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "17f5ec11-3c10-44f8-85d3-18383e14f9af",
    "title": "(US) Sales Development Representative (6 month contract)",
    "location": "Remote, USA",
    "official_url": "https://jobs.lever.co/pointclickcare/17f5ec11-3c10-44f8-85d3-18383e14f9af",
    "posted_date": "2026-10-13",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.240571+00:00",
    "date_confidence": "high",
    "description": ""
  }
]
```

## Stryker

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://stryker.wd1.myworkdayjobs.com/StrykerCareers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 20
- HTTP requests/cumulative request time: 159 / 62.197s
- Company elapsed time: 82.485s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 138 / 0 / 0
- Detail cache statuses: {'fetched:new': 138}
- Relevant JD recovery: {'eligible': 50, 'usable_jd': 50}
- Raw jobs found: 232
- After US/location filtering: 138
- With trustworthy posted_date: 138
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 12.52, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 25, "stop_reason": "early_stop", "unique_contribution": 23, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 2.683, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 1.212, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 11.717, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 19.636, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.202, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 31, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 31}
- Query diagnostic: {"elapsed_seconds": 2.217, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.891, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 21.414, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R575543",
    "title": "Principal, Cybersecurity Automation - Remote",
    "location": "Kalamazoo, Michigan",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Kalamazoo-Michigan/Principal--Cybersecurity-Automation---Remote_R575543-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.999894+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Remote The Principal Security Automation & AI Engineer is the senior technical leader responsible for automation and AI across Cyber Defense. This role designs, b"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R573258",
    "title": "Senior Manager, Cybersecurity, AI SOC & Crisis Management - Remote",
    "location": "Michigan, Kalamazoo 4100 East Milham Rd",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Michigan-Kalamazoo-4100-East-Milham-Rd/Senior-Manager--Cybersecurity--AI-SOC---Crisis-Management---Remote_R573258-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.999894+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Remote Preference will be given to candidates residing in the Eastern or Central time zones. As a Senior Manager, AI Security Operations & Crisis Management, you "
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R575370",
    "title": "Lead Full-Stack Software Engineer (Remote)",
    "location": "Flower Mound, Texas; Kalamazoo, Michigan; Chicago, Illinois",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Flower-Mound-Texas/Lead-Full-Stack-Software-Engineer--Remote-_R575370",
    "posted_date": "2026-10-21",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.999894+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Remote As a Lead Full-Stack Software Engineer, you will go beyond building applications to design, lead, and guide the engineering direction of our internal web s"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R571251",
    "title": "Senior Staff Product Owner, Voice Intelligence",
    "location": "San Jose, California",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/San-Jose-California/Senior-Staff-Product-Owner--Voice-Intelligence_R571251",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.999894+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid It's Time to Join Stryker! Stryker is seeking a Senior Staff Product Owner, Voice Intelligence to help shape the next generation of intelligent caregiver c"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R572870",
    "title": "Summer 2027 Internship - Interaction Design - Washington",
    "location": "Redmond, Washington",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Redmond-Washington/Summer-2027-Internship---Interaction-Design---Washington_R572870",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:46.999894+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Onsite As an Interaction Designer for Emergency Care, you will collaborate with our existing team of experienced designers in their process to define, design, and"
  }
]
```

## TransUnion

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://transunion.wd5.myworkdayjobs.com/TransUnion`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 15
- HTTP requests/cumulative request time: 44 / 19.199s
- Company elapsed time: 24.165s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 28 / 0 / 0
- Detail cache statuses: {'fetched:new': 26, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 129
- After US/location filtering: 28
- With trustworthy posted_date: 28
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.637, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 25, "stop_reason": "early_stop", "unique_contribution": 25, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 0.594, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.048, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.373, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 2.38, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 0.6, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 2.601, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 0.534, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.55, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}

Sample normalized records:

```json
[
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042793",
    "title": "Senior Architect AI Engineering and Platforms",
    "location": "Chicago, Illinois; Reston, Virginia",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Senior-Architect-AI-Engineering-and-Platforms_19042793",
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:53.484139+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The AI Engineering and Platforms team designs, builds, and operates the"
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042638",
    "title": "Principal – TruIQ Product and AI Strategy",
    "location": "Chicago, Illinois; New York, New York; Reston, Virginia",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Principal---TruIQ-Product-and-AI-Strategy_19042638",
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:53.484139+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview TruIQ Analytics Enablement Solutions are a suite of SaaS/PaaS solutions"
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042911",
    "title": "Principal Engineer, Security AI Tooling and Automation",
    "location": "Chicago, Illinois",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Principal-Engineer--Security-AI-Tooling-and-Automation_19042911-1",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:53.484139+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview Security Forward Deployed Engineering (SFDE) deploys concentrated engin"
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042110",
    "title": "Lead Java Engineer",
    "location": "Chicago, Illinois; Reston, Virginia; Crum Lynne, Pennsylvania; Boca Raton, Florida",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Lead-Java-Engineer_19042110-1",
    "posted_date": "2026-09-09",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:53.484139+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The Core Online team is responsible for building and supporting global "
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042854",
    "title": "Lead, Full Stack Engineer",
    "location": "Chicago, Illinois; Reston, Virginia; Crum Lynne, Pennsylvania; Boca Raton, Florida",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Lead--Full-Stack-Engineer_19042854",
    "posted_date": "2026-10-27",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:53.484139+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview TransUnion Consumer Interactive (TUCI) develops and supports consumer-f"
  }
]
```

## Travelers

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://travelers.wd5.myworkdayjobs.com/External`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 23
- HTTP requests/cumulative request time: 108 / 46.326s
- Company elapsed time: 61.067s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 84 / 0 / 0
- Detail cache statuses: {'fetched:new': 81, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 44, 'usable_jd': 44}
- Raw jobs found: 312
- After US/location filtering: 84
- With trustworthy posted_date: 84
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.193, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 4.989, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 2.748, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 7.16, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 8.361, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 2.83, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 0.663, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.529, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 5.852, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 50, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 50}

Sample normalized records:

```json
[
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51257",
    "title": "Gen AI - Data Engineer II",
    "location": "GA - Atlanta",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/GA---Atlanta/Gen-AI---Data-Engineer-II_R-51257",
    "posted_date": "2026-10-26",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:59.148008+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51656",
    "title": "Software Engineer II - Enterprise AI Products",
    "location": "CT - Hartford; MN - St. Paul",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Software-Engineer-II---Enterprise-AI-Products_R-51656",
    "posted_date": "2026-10-26",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:59.148008+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-53193",
    "title": "Sr. Software Engineer – AI and Automation (Team Breeze)",
    "location": "CT - Hartford; GA - Atlanta",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Sr-Software-Engineer---AI-and-Automation--Team-Breeze-_R-53193",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:59.148008+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-53201",
    "title": "Senior Software Engineer, Full Stack AI (Python, React, AWS Bedrock)",
    "location": "CT - Hartford; GA - Atlanta; MN - St. Paul; MD - Hunt Valley",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Senior-Software-Engineer--Full-Stack-AI--Python--React--AWS-Bedrock-_R-53201",
    "posted_date": "2026-10-26",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:59.148008+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-52945",
    "title": "Senior Architect (AI)",
    "location": "CT - Hartford; US - Nationwide; MD - Hunt Valley; MN - North St. Paul",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Senior-Architect--AI-_R-52945",
    "posted_date": "2026-10-26",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:43:59.148008+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  }
]
```

## Verizon

- Status: ok
- Scraping method: HTTP GET public Happydance jobs JSON + server-rendered detail flight data
- Search URL/API: `https://mycareer.verizon.com/api/jobs/search/`
- Pagination: page=1,2,... with pagesize=100; stop on total/empty/repeat
- Pages/requests fetched: 6
- HTTP requests/cumulative request time: 27 / 5.103s
- Company elapsed time: 5.333s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 21 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 44
- After US/location filtering: 21
- With trustworthy posted_date: 21
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.698, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.311, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 1.316, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 2.252, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.341, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.414, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}

Sample normalized records:

```json
[
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1102281",
    "title": "Principal Firmware Engineer",
    "location": "Irving, Texas",
    "official_url": "https://mycareer.verizon.com/jobs/r-1102281/principal-firmware-engineer/",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:44:17.650280+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1102685",
    "title": "Senior Engineer - Java Full Stack",
    "location": "Temple Terrace, Florida; Irving, Texas; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1102685/senior-engineer-java-full-stack/",
    "posted_date": "2026-10-21",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:44:17.650280+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1102402",
    "title": "Forward Deployed Engineer",
    "location": "Irving, Texas; Basking Ridge, New Jersey; Charlotte, North Carolina",
    "official_url": "https://mycareer.verizon.com/jobs/r-1102402/forward-deployed-engineer/",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:44:17.650280+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1103536",
    "title": "Principal Engineer-Data Science",
    "location": "Alpharetta, Georgia",
    "official_url": "https://mycareer.verizon.com/jobs/r-1103536/principal-engineer-data-science/",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:44:17.650280+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1100559",
    "title": "Senior Data Scientist",
    "location": "Basking Ridge, New Jersey; Alpharetta, Georgia; Irving, Texas",
    "official_url": "https://mycareer.verizon.com/jobs/r-1100559/senior-data-scientist/",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-06T00:44:17.650280+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  }
]
```

## Yext

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/yext/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.207s
- Company elapsed time: 0.269s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 30
- After US/location filtering: 17
- With trustworthy posted_date: 17
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8334849",
    "title": "AI Transformation Engineer",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8334849",
    "posted_date": "2026-11-02",
    "updated_date": "2026-11-02",
    "fetched_at": "2026-11-06T00:44:20.336006+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8288963",
    "title": "Commercial Counsel",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8288963",
    "posted_date": "2026-10-16",
    "updated_date": "2026-10-16",
    "fetched_at": "2026-11-06T00:44:20.336006+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8302454",
    "title": "Commercial Counsel",
    "location": "Washington, D.C.; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8302454",
    "posted_date": "2026-10-20",
    "updated_date": "2026-10-20",
    "fetched_at": "2026-11-06T00:44:20.336006+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8119470",
    "title": "Customer Success Manager, Enterprise",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8119470",
    "posted_date": "2026-09-17",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-06T00:44:20.336006+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8237972",
    "title": "Director, Revenue Accounting",
    "location": "Remote - US; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8237972",
    "posted_date": "2026-10-01",
    "updated_date": "2026-10-15",
    "fetched_at": "2026-11-06T00:44:20.336006+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
