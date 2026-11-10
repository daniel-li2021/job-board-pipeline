# Official careers scrape report — 2026-11-10_0031

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Runtime metrics

- Wall time: 837.044s
- HTTP requests/cumulative request time: 7175 / 2834.269s
- Listing pages/detail fetched/cache reused/prefilter skipped: 1295 / 5840 / 308 / 856
- Detail cache statuses: {'fetched:changed': 1, 'fetched:missing_detail': 176, 'fetched:new': 5479, 'fetched:stale': 9, 'reuse_after_error:missing_detail': 1, 'reuse_after_error:stale': 41, 'reused': 259}
- Relevant JD coverage: 5421 / 5432; added detail requests 25 / 150; deferred 0

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 12.915s
- Company elapsed time: 28.018s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 125, 'usable_jd': 125}
- Raw jobs found: 796
- After US/location filtering: 251
- With trustworthy posted_date: 251
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.422, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "\"Ai Engineer\"", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.122, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Machine Learning Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.152, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "\"Data Scientist\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.304, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Solutions Architect\"", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.239, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Data Engineer\"", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 2.078, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "\"Platform Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.043, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Full Stack Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.077, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "\"Forward Deployed Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.25, "first_pass_survivors": 66, "group": "official", "jds_resolved": 66, "original_postings_resolved": 66, "page_budget": 12, "pages_fetched": 8, "query": "\"Software Engineer\"", "raw_jobs": 160, "stop_reason": "early_stop", "unique_contribution": 66, "unique_jobs": 160}
- Query diagnostic: {"elapsed_seconds": 2.102, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "\"Infrastructure Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.238, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 5, "pages_fetched": 4, "query": "\"Software Engineer III\"", "raw_jobs": 74, "stop_reason": "early_stop", "unique_contribution": 16, "unique_jobs": 74}
- Query diagnostic: {"elapsed_seconds": 1.558, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 2, "pages_fetched": 2, "query": "\"Web Solutions Engineer\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 1.432, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 2, "pages_fetched": 2, "query": "\"DeepMind\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "81817033515115206",
    "title": "Software Engineer III, Full Stack",
    "location": "Cambridge, MA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/81817033515115206-software-engineer-iii-full-stack",
    "posted_date": "2026-11-09",
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:31:15.251786+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "132332995741655750",
    "title": "Senior Software Engineer, Mobile, Android",
    "location": "Raleigh, NC, USA; Durham, NC, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/132332995741655750-senior-software-engineer-mobile-android",
    "posted_date": "2026-11-09",
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:31:15.251786+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "140241645441295046",
    "title": "Senior Software Engineer, Cloud- Foundation and Security Platform (multiple openings)",
    "location": "Raleigh, NC, USA; Durham, NC, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/140241645441295046-senior-software-engineer-cloud-foundation-and-security-platform-multiple-openings",
    "posted_date": "2026-11-09",
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:31:15.251786+00:00",
    "date_confidence": "high",
    "description": "Google Cloud accelerates every organization’s ability to digitally transform its business and industry. We deliver enterprise-grade solutions that leverage Google’s cutting-edge te"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "100233715841409734",
    "title": "Senior Software Engineer",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/100233715841409734-senior-software-engineer",
    "posted_date": "2026-11-09",
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:31:15.251786+00:00",
    "date_confidence": "high",
    "description": "The US base salary range for this full-time position is $221,450 - $253,000 + 15.00% bonus target + equity + benefits determined by role, level, and location. Individual pay is det"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "133148695930512070",
    "title": "Software Engineer III, Core Data (multiple openings)",
    "location": "Madison, WI, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/133148695930512070-software-engineer-iii-core-data-multiple-openings",
    "posted_date": "2026-11-09",
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:31:15.251786+00:00",
    "date_confidence": "high",
    "description": "The Core team builds the technical foundation behind Google’s flagship products. We are owners and advocates for the underlying design elements, developer platforms, product compon"
  }
]
```

## Amazon

- Status: ok
- Scraping method: HTTP GET search.json
- Search URL/API: `https://www.amazon.jobs/en/search?base_query=software+engineer&country=USA&offset=0&result_limit=10&sort=recent`
- Pagination: newest-first offset by 20; minimum 2 pages, then two seen pages + one overlap page; otherwise hits/cap
- Pages/requests fetched: 45
- HTTP requests/cumulative request time: 45 / 13.824s
- Company elapsed time: 25.955s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 483, 'usable_jd': 483}
- Raw jobs found: 859
- After US/location filtering: 746
- With trustworthy posted_date: 746
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.688, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 1.474, "first_pass_survivors": 55, "group": "official", "jds_resolved": 55, "original_postings_resolved": 55, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 55, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 1.522, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 1.862, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.867, "first_pass_survivors": 56, "group": "official", "jds_resolved": 56, "original_postings_resolved": 56, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 56, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.407, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.404, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 15, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.914, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 39, "stop_reason": "early_stop", "unique_contribution": 39, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 7.187, "first_pass_survivors": 209, "group": "official", "jds_resolved": 209, "original_postings_resolved": 209, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 209, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.087, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.758, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 3, "pages_fetched": 3, "query": "systems development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.247, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.538, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 2, "pages_fetched": 2, "query": "applied scientist", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10600530",
    "title": "Software Development Engineer, AIO Visualization and Reporting",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10600530/software-development-engineer-aio-visualization-and-reporting",
    "posted_date": "2026-11-09",
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-10T00:31:15.252510+00:00",
    "date_confidence": "high",
    "description": "Join a team that builds the experiences every AWS customer uses to understand, monitor, and optimize what they spend, from individual developers to enterprise FinOps teams managing"
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
    "fetched_at": "2026-11-10T00:31:15.252510+00:00",
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
    "fetched_at": "2026-11-10T00:31:15.252510+00:00",
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
    "fetched_at": "2026-11-10T00:31:15.252510+00:00",
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
    "fetched_at": "2026-11-10T00:31:15.252510+00:00",
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
- HTTP requests/cumulative request time: 45 / 28.386s
- Company elapsed time: 43.452s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 3 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 205, 'detail_requests': 3, 'detail_failure': 3, 'budget_deferred': 0, 'usable_jd': 202}
- Raw jobs found: 840
- After US/location filtering: 291
- With trustworthy posted_date: 291
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.879, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.196, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.285, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.184, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.088, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.18, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.154, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.121, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.738, "first_pass_survivors": 121, "group": "official", "jds_resolved": 121, "original_postings_resolved": 121, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 121, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.283, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "apps-and-frameworks-SFTWR-AF", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200693714-0836",
    "title": "Analog IC Design Engineer",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200693714/analog-ic-design-engineer",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.253957+00:00",
    "date_confidence": "high",
    "description": "At Apple, we work every single day to craft products that enrich people’s lives. Do you love working on challenges that no one has solved yet? Do you like changing the game? We hav"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200693714-3956",
    "title": "Analog IC Design Engineer",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200693714/analog-ic-design-engineer",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.253957+00:00",
    "date_confidence": "high",
    "description": "At Apple, we work every single day to craft products that enrich people’s lives. Do you love working on challenges that no one has solved yet? Do you like changing the game? We hav"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200643766-3749",
    "title": "Workplace Design Test Fit Program Manager",
    "location": "San Jose, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200643766/workplace-design-test-fit-program-manager",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.253957+00:00",
    "date_confidence": "high",
    "description": "In Places, we don’t sit back and let things happen, we make things happen, and we do this in service to all Apple employees and customers. We develop and manage Apple’s global real"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200693773-0836",
    "title": "Storefront Insights Specialist",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200693773/storefront-insights-specialist",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.253957+00:00",
    "date_confidence": "high",
    "description": "Imagine what you could do here! The people at Apple do not just create products. They build the kind of wonder that has revolutionized entire industries. It is the diversity of tho"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200682498-0836",
    "title": "AI/ML Engineer: System RF Data Ecosystem",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200682498/ai-ml-engineer-system-rf-data-ecosystem",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.253957+00:00",
    "date_confidence": "high",
    "description": "At Apple, new ideas quickly transform into products, services, and customer experiences that delight millions. This innovation is fueled by cutting-edge hardware developed within t"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 242 / 58.076s
- Company elapsed time: 93.035s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 202 / 0 / 0
- Detail cache statuses: {'fetched:new': 197, 'fetched:missing_detail': 5}
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 390
- After US/location filtering: 202
- With trustworthy posted_date: 202
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.445, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.929, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 10.785, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 10.415, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.149, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.607, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.914, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.243, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 23.048, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 120}

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200065656",
    "title": "Senior Software Engineer- AI Agents",
    "location": "United States, Washington, Redmond; United States, California, Mountain View; United States, New York, New York",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557054012",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.255271+00:00",
    "date_confidence": "high",
    "description": "Overview The Agent 365 team is building the enterprise platform for managing and governing AI agents at scale. We are looking for a Senior Software Engineer who is passionate about"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200065643",
    "title": "Principal CAD Software Engineer",
    "location": "United States, California, Mountain View; United States, North Carolina, Raleigh; United States, Oregon, Hillsboro",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557053997",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.255271+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200065231",
    "title": "Senior Mechanical Engineer, AI Systems",
    "location": "United States, California, Mountain View",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557053107",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.255271+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200038893",
    "title": "Principal Silicon Design Verification Engineer",
    "location": "United States, California, Santa Clara; United States, California, Mountain View; United States, Oregon, Hillsboro; United States, Texas, Austin; United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556870706",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.255271+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200038799",
    "title": "Principal Silicon Design Verification Engineer",
    "location": "United States, California, Santa Clara; United States, California, Mountain View; United States, Oregon, Hillsboro; United States, Texas, Austin; United States, Idaho, Boise; United States, California, San Diego; United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556870474",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.255271+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 506 / 226.680s
- Company elapsed time: 293.157s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 473 / 0 / 0
- Detail cache statuses: {'fetched:new': 469, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 65, 'usable_jd': 65}
- Raw jobs found: 640
- After US/location filtering: 473
- With trustworthy posted_date: 473
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 42.816, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 28.64, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 46.134, "first_pass_survivors": 49, "group": "official", "jds_resolved": 49, "original_postings_resolved": 49, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 49, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 34.996, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 23.488, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 29.002, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 21.849, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.393, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 28.556, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 19.97, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}

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
    "fetched_at": "2026-11-10T00:31:15.255860+00:00",
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
    "fetched_at": "2026-11-10T00:31:15.255860+00:00",
    "date_confidence": "high",
    "description": "Join the AI & Automation Supply Chain Business Transformations team in NVIDIA Operations to develop the future of agentic AI at scale. As the Senior AI Engineer in Operations, you "
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2029272",
    "title": "Senior AI Engineer, AI Safety",
    "location": "US, CA, Santa Clara; US, CA, Remote",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-AI-Engineer--AI-Safety_JR2029272-1",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:15.255860+00:00",
    "date_confidence": "high",
    "description": "NVIDIA has been transforming computer graphics, PC gaming, and accelerated computing for more than 25 years. It’s a unique legacy of innovation that’s fueled by great technology—an"
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
    "fetched_at": "2026-11-10T00:31:15.255860+00:00",
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
    "fetched_at": "2026-11-10T00:31:15.255860+00:00",
    "date_confidence": "high",
    "description": "NVIDIA has been transforming computer graphics, PC gaming, and accelerated computing for more than 25 years. It’s a unique legacy of innovation that’s fueled by great technology—an"
  }
]
```

## Salesforce

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://salesforce.wd12.myworkdayjobs.com/External_Career_Site`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 28
- HTTP requests/cumulative request time: 208 / 59.955s
- Company elapsed time: 88.355s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 179 / 0 / 0
- Detail cache statuses: {'fetched:new': 176, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 48, 'usable_jd': 48}
- Raw jobs found: 450
- After US/location filtering: 179
- With trustworthy posted_date: 179
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.938, "first_pass_survivors": 75, "group": "official", "jds_resolved": 75, "original_postings_resolved": 75, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 75, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 8.742, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 3.791, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 14.102, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.1, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.13, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.512, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 33, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 7.057, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 6.308, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.099, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "software engineering mts", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 13}

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR367261",
    "title": "Senior Software Engineer, Human Agent Interfaces (Agentforce)",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Senior-Software-Engineer--Human-Agent-Interfaces--Agentforce-_JR367261",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:41.209032+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR367737",
    "title": "Senior Director, Product & Community Engagement,Tableau",
    "location": "Illinois - Chicago; Texas - Dallas",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Illinois---Chicago/Senior-Director--Product---Community-Engagement-Tableau_JR367737-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:41.209032+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Product Job Details"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR367622",
    "title": "AI Product Associate Analyst, Early Talent",
    "location": "Illinois - Chicago; Indiana - Indianapolis",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Illinois---Chicago/AI-Product-Associate-Analyst--Early-Talent_JR367622-2",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:41.209032+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. About Futureforce University Rec"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR353498",
    "title": "Account SE",
    "location": "New York - Remote; Illinois - Chicago Metro - Remote; California - San Francisco Metro - Remote; Georgia - Atlanta Metro - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/New-York---Remote/Senior-Client-Solution-Engineer_JR353498",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:41.209032+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR361738",
    "title": "Strategic Partner Account Sr. Manager",
    "location": "New York - New York; Illinois - Chicago; California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/New-York---New-York/Strategic-Partner-Account-Sr-Manager_JR361738",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:41.209032+00:00",
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
- HTTP requests/cumulative request time: 129 / 54.228s
- Company elapsed time: 72.391s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 100 / 0 / 0
- Detail cache statuses: {'fetched:new': 99, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 29, 'usable_jd': 29}
- Raw jobs found: 425
- After US/location filtering: 100
- With trustworthy posted_date: 100
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 42.511, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 4.428, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 2.023, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 3.94, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 31, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 31}
- Query diagnostic: {"elapsed_seconds": 2.545, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.236, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.035, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 2.89, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 7.708, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 2.335, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 57}

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
    "fetched_at": "2026-11-10T00:31:43.271009+00:00",
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
    "fetched_at": "2026-11-10T00:31:43.271009+00:00",
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
    "fetched_at": "2026-11-10T00:31:43.271009+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are looking for a Senior AI Systems Engineer with deep C++ expertise to help build the next generation of AI-enabled product and platform capabilities. This role"
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
    "fetched_at": "2026-11-10T00:31:43.271009+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are seeking a Senior Director of AI, Data Science & Engineering to lead the technical organization responsible for building the next generation of AI-powered fra"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R171801",
    "title": "Senior AI / Machine Learning Engineer — Fraud Prevention",
    "location": "San Jose; Austin; Seattle; New York; Chicago; Washington D.C.",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Senior-AI---Machine-Learning-Engineer---Fraud-Detection_R171801-1",
    "posted_date": "2026-10-07",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:43.271009+00:00",
    "date_confidence": "high",
    "description": "Senior AI / Machine Learning Engineer — Fraud Detection The Opportunity We are in search of an experienced Senior AI/ML Engineer to develop and broaden fraud and abuse detection sy"
  }
]
```

## Meta

- Status: ok
- Scraping method: HTTP POST Meta Relay GraphQL; dynamic LSD and doc_id discovery
- Search URL/API: `https://www.metacareers.com/jobsearch/`
- Pagination: one complete Relay payload per role query
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 25 / 19.396s
- Company elapsed time: 20.351s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 12 / 252 / 622
- Detail cache statuses: {'reused': 226, 'fetched:new': 5, 'fetched:stale': 7, 'reuse_after_error:stale': 19}
- Relevant JD recovery: {'deterministic_skip': 440, 'cache_reused': 252, 'eligible': 238, 'ai_skip': 182, 'ai_recover': 2, 'detail_requests': 12, 'detail_success': 12, 'budget_deferred': 0, 'usable_jd': 238}
- Raw jobs found: 2902
- After US/location filtering: 860
- With trustworthy posted_date: 28
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.175, "first_pass_survivors": 548, "group": "official", "jds_resolved": 0, "original_postings_resolved": 548, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 671, "stop_reason": "page_budget", "unique_contribution": 548, "unique_jobs": 671}
- Query diagnostic: {"elapsed_seconds": 0.843, "first_pass_survivors": 29, "group": "official", "jds_resolved": 0, "original_postings_resolved": 29, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 172, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 172}
- Query diagnostic: {"elapsed_seconds": 1.01, "first_pass_survivors": 52, "group": "official", "jds_resolved": 0, "original_postings_resolved": 52, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 184, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 184}
- Query diagnostic: {"elapsed_seconds": 0.868, "first_pass_survivors": 31, "group": "official", "jds_resolved": 0, "original_postings_resolved": 31, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 198, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 198}
- Query diagnostic: {"elapsed_seconds": 0.859, "first_pass_survivors": 157, "group": "official", "jds_resolved": 0, "original_postings_resolved": 157, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 736, "stop_reason": "page_budget", "unique_contribution": 157, "unique_jobs": 736}
- Query diagnostic: {"elapsed_seconds": 0.97, "first_pass_survivors": 29, "group": "official", "jds_resolved": 0, "original_postings_resolved": 29, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 433, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 433}
- Query diagnostic: {"elapsed_seconds": 0.46, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 0.734, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 0.707, "first_pass_survivors": 14, "group": "official", "jds_resolved": 0, "original_postings_resolved": 14, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 435, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 435}

Sample normalized records:

```json
[
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "4455569504707135",
    "title": "Research Scientist Intern, On-Device AI Model Optimization (PhD)",
    "location": "Menlo Park, CA; Burlingame, CA",
    "official_url": "https://www.metacareers.com/jobs/4455569504707135",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:46.362178+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2199155494335856",
    "title": "AI Research Scientist - FAIR, MSL",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/2199155494335856",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:46.362178+00:00",
    "date_confidence": "unknown",
    "description": "Meta is seeking a Research Scientist to advance core machine learning research that powers products and systems at global scale. In this role, you will conduct original research in"
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1050754181130466",
    "title": "Software Engineering Manager, Systems",
    "location": "Sunnyvale, CA; Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/1050754181130466",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:46.362178+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2091557968116092",
    "title": "Supply Chain Enterprise Program Manager",
    "location": "Sunnyvale, CA",
    "official_url": "https://www.metacareers.com/jobs/2091557968116092",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:46.362178+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1436360758394361",
    "title": "Research Engineer, Robotics - Meta Superintelligence Labs",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/1436360758394361",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:31:46.362178+00:00",
    "date_confidence": "unknown",
    "description": "Meta is seeking a Robotics and Embodied AI Researcher to join Meta Superintelligence Labs. Individuals in this role are proficient in identified research areas such as artificial i"
  }
]
```

## TikTok

- Status: ok
- Scraping method: HTTP POST public supplier /search/job/posts
- Search URL/API: `https://api.lifeattiktok.com/api/v1/public/supplier/search/job/posts`
- Pagination: offset=0,50,...; limit=50; US city filter
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 26 / 25.378s
- Company elapsed time: 29.661s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 429, 'usable_jd': 429}
- Raw jobs found: 1237
- After US/location filtering: 715
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.992, "first_pass_survivors": 199, "group": "official", "jds_resolved": 199, "original_postings_resolved": 199, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 199, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 5.068, "first_pass_survivors": 131, "group": "official", "jds_resolved": 131, "original_postings_resolved": 131, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 131, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.321, "first_pass_survivors": 111, "group": "official", "jds_resolved": 111, "original_postings_resolved": 111, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 111, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.841, "first_pass_survivors": 77, "group": "official", "jds_resolved": 77, "original_postings_resolved": 77, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 77, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.93, "first_pass_survivors": 63, "group": "official", "jds_resolved": 63, "original_postings_resolved": 63, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 63, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.996, "first_pass_survivors": 61, "group": "official", "jds_resolved": 61, "original_postings_resolved": 61, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 61, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 1.517, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 86, "stop_reason": "early_stop", "unique_contribution": 25, "unique_jobs": 86}
- Query diagnostic: {"elapsed_seconds": 0.574, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 3.42, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 200}

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
    "fetched_at": "2026-11-10T00:31:54.977717+00:00",
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
    "fetched_at": "2026-11-10T00:31:54.977717+00:00",
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
    "fetched_at": "2026-11-10T00:31:54.977717+00:00",
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
    "fetched_at": "2026-11-10T00:31:54.977717+00:00",
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
    "fetched_at": "2026-11-10T00:31:54.977717+00:00",
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
- HTTP requests/cumulative request time: 215 / 59.090s
- Company elapsed time: 88.845s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 187 / 0 / 0
- Detail cache statuses: {'fetched:new': 187}
- Relevant JD recovery: {'eligible': 34, 'usable_jd': 34}
- Raw jobs found: 546
- After US/location filtering: 187
- With trustworthy posted_date: 187
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 28.802, "first_pass_survivors": 71, "group": "official", "jds_resolved": 71, "original_postings_resolved": 71, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 71, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 11.66, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.454, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 35, "stop_reason": "early_stop", "unique_contribution": 17, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 9.982, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 51, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 51}
- Query diagnostic: {"elapsed_seconds": 4.79, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.814, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.111, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.827, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.407, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 80}

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
    "fetched_at": "2026-11-10T00:32:24.639588+00:00",
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
    "fetched_at": "2026-11-10T00:32:24.639588+00:00",
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
    "fetched_at": "2026-11-10T00:32:24.639588+00:00",
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
    "fetched_at": "2026-11-10T00:32:24.639588+00:00",
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
    "fetched_at": "2026-11-10T00:32:24.639588+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.377s
- Company elapsed time: 2.374s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 109, 'usable_jd': 109}
- Raw jobs found: 436
- After US/location filtering: 435
- With trustworthy posted_date: 435
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8139265",
    "title": "Account Executive",
    "location": "Seattle, WA; Washington",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8139265",
    "posted_date": "2026-10-07",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-10T00:32:48.291192+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7467955",
    "title": "Account Executive",
    "location": "Tempe, AZ; Dallas, TX; Indianapolis, IN; Kansas City, MO; Richmond, VA; St. Louis, MO; Oklahoma City, OK; New Orleans, LA; Charleston, SC; Tempe, AZ",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7467955",
    "posted_date": "2025-12-12",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-10T00:32:48.291192+00:00",
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
    "fetched_at": "2026-11-10T00:32:48.291192+00:00",
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
    "fetched_at": "2026-11-10T00:32:48.291192+00:00",
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
    "fetched_at": "2026-11-10T00:32:48.291192+00:00",
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
- HTTP requests/cumulative request time: 123 / 44.465s
- Company elapsed time: 61.430s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 99 / 0 / 0
- Detail cache statuses: {'fetched:new': 99}
- Relevant JD recovery: {'eligible': 17, 'usable_jd': 17}
- Raw jobs found: 368
- After US/location filtering: 99
- With trustworthy posted_date: 99
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.19, "first_pass_survivors": 64, "group": "official", "jds_resolved": 64, "original_postings_resolved": 64, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 64, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 4.24, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 33, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 0.616, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 6.062, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 6.382, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.146, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.872, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 0.7, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 6.299, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 80}

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
    "fetched_at": "2026-11-10T00:32:50.666058+00:00",
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
    "fetched_at": "2026-11-10T00:32:50.666058+00:00",
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
    "fetched_at": "2026-11-10T00:32:50.666058+00:00",
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
    "fetched_at": "2026-11-10T00:32:50.666058+00:00",
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
    "fetched_at": "2026-11-10T00:32:50.666058+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.154s
- Company elapsed time: 0.722s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 22, 'usable_jd': 22}
- Raw jobs found: 170
- After US/location filtering: 132
- With trustworthy posted_date: 132
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:32:55.663517+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:32:55.663517+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:32:55.663517+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:32:55.663517+00:00",
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
    "fetched_at": "2026-11-10T00:32:55.663517+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.197s
- Company elapsed time: 0.755s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 40, 'usable_jd': 40}
- Raw jobs found: 368
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
    "fetched_at": "2026-11-10T00:32:56.388176+00:00",
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
    "fetched_at": "2026-11-10T00:32:56.388176+00:00",
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
    "fetched_at": "2026-11-10T00:32:56.388176+00:00",
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
    "fetched_at": "2026-11-10T00:32:56.388176+00:00",
    "date_confidence": "high",
    "description": "At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to "
  },
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "c6b398be-85db-4390-9c41-563185039dfb",
    "title": "Majors Account Executive",
    "location": "KR-Seoul; Seoul, South Korea",
    "official_url": "https://jobs.ashbyhq.com/snowflake/c6b398be-85db-4390-9c41-563185039dfb",
    "posted_date": "2026-09-21",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:32:56.388176+00:00",
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
- HTTP requests/cumulative request time: 442 / 198.610s
- Company elapsed time: 254.128s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 420 / 0 / 0
- Detail cache statuses: {'fetched:new': 420}
- Relevant JD recovery: {'eligible': 53, 'usable_jd': 53}
- Raw jobs found: 1911
- After US/location filtering: 420
- With trustworthy posted_date: 420
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 185.142, "first_pass_survivors": 319, "group": "official", "jds_resolved": 319, "original_postings_resolved": 319, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 319, "stop_reason": "page_budget", "unique_contribution": 319, "unique_jobs": 319}
- Query diagnostic: {"elapsed_seconds": 1.074, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 108, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 108}
- Query diagnostic: {"elapsed_seconds": 9.995, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 185, "stop_reason": "early_stop", "unique_contribution": 15, "unique_jobs": 185}
- Query diagnostic: {"elapsed_seconds": 45.675, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 76, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 276, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 276}
- Query diagnostic: {"elapsed_seconds": 1.926, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 5.506, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 0.99, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 71, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 71}
- Query diagnostic: {"elapsed_seconds": 0.441, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 67, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 67}
- Query diagnostic: {"elapsed_seconds": 3.379, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 285, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 285}

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075536",
    "title": "Staff Inbound Product Manager - ServiceNow University",
    "location": "San Diego, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000160740103-staff-inbound-product-manager-servicenow-university",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:32:57.144859+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0073319",
    "title": "Staff MLE, GAI Search Platform - Moveworks",
    "location": "Mountain View, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000160739819-staff-mle-gai-search-platform-moveworks-",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:32:57.144859+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0073058",
    "title": "Staff Software Engineer, Frontend/Fullstack - Moveworks",
    "location": "Mountain View, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000160737185-staff-software-engineer-frontend-fullstack-moveworks",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:32:57.144859+00:00",
    "date_confidence": "high",
    "description": "It all started in sunny San Diego, California in 2004 when a visionary engineer, Fred Luddy, saw the potential to transform how we work. Fast forward to today — ServiceNow stands a"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076560",
    "title": "Senior Software Engineer",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000160737829-senior-software-engineer",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:32:57.144859+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076863",
    "title": "Sr Solution Sales Executive Data & Analytics - Healthcare",
    "location": "Boston, Massachusetts, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000160736029-sr-solution-sales-executive-data-analytics-healthcare",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:32:57.144859+00:00",
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
- HTTP requests/cumulative request time: 49 / 57.083s
- Company elapsed time: 69.244s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 20 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 20}
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 348
- After US/location filtering: 20
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.034, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.611, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 4.668, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 4.665, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 4.881, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 4.73, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 4.751, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 4.703, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 6.201, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 45}

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46069",
    "title": "M365 Engineer (CW)",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/M365-Engineer-CW/46069",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:09.565104+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Our Team Bloomberg’s Workplace Productivity team builds internal solutions across Microsoft 365/Azure and Google Workspace for over 25,000 employees. We "
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46061",
    "title": "Senior Data Management Professional - Data Product Owner - Holdings",
    "location": "Princeton, New Jersey, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Data-Management-Professional-Data-Product-Owner-Holdings/46061",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:09.565104+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg runs on data. Our products bring together data, context, news, and analytics to help clients understand global markets and make informed decisi"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46059",
    "title": "Senior Data Management Professional - Data Product Owner - Holdings",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Data-Management-Professional-Data-Product-Owner-Holdings/46059",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:09.565104+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg runs on data. Our products bring together data, context, news, and analytics to help clients understand global markets and make informed decisi"
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
    "fetched_at": "2026-11-10T00:33:09.565104+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg runs on data. Our products are fueled by powerful information. We combine data and context to paint the whole picture for our clients, around t"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46037",
    "title": "Bloomberg Intelligence Consumer Senior Research Analyst: Beverages",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Bloomberg-Intelligence-Consumer-Senior-Research-Analyst-Beverages/46037",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:09.565104+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg Intelligence (BI) delivers independent, data-driven research and interactive datasets integrated into the Bloomberg Terminal, helping investmen"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 63
- HTTP requests/cumulative request time: 618 / 132.455s
- Company elapsed time: 216.593s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 555 / 0 / 0
- Detail cache statuses: {'fetched:new': 544, 'fetched:missing_detail': 11}
- Relevant JD recovery: {'eligible': 125, 'usable_jd': 125}
- Raw jobs found: 1260
- After US/location filtering: 555
- With trustworthy posted_date: 555
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 19.651, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 14.782, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.794, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.032, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.878, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.522, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.9, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.981, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.76, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 14.004, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "full stack", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.065, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "python react", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.501, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 2, "query": "pyspark databricks", "raw_jobs": 40, "stop_reason": "early_stop", "unique_contribution": 21, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 8.351, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "experienced software engineer java python", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.256, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "agentic ai", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.524, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.718, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "software engineer ii", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.141, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.433, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "security engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.066, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "quantitative developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.298, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "software engineer java spring", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.879, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 1, "pages_fetched": 1, "query": "software engineer python authe", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.19, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "aws data platform engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.39, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data engineer applied ai", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 3.475, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 1, "pages_fetched": 1, "query": "asset management technology", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 20}

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
    "fetched_at": "2026-11-10T00:33:52.097055+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Senior Lead Software Engineer at JPMorgan Chase, within"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210803129",
    "title": "Director of Infrastructure Engineering - AI",
    "location": "New York, NY, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210803129",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:52.097055+00:00",
    "date_confidence": "high",
    "description": "At a world-renowned company like JPMorganChase, you can take the lead in shaping the future of technology, unleashing your full potential, and making your mark on the industry. As "
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
    "fetched_at": "2026-11-10T00:33:52.097055+00:00",
    "date_confidence": "high",
    "description": "Be an integral part of an agile team that's constantly pushing the envelope to enhance, build, and deliver top-notch technology products. As a Senior Lead Software Engineer at JPMo"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210772271",
    "title": "Lead Software Engineer - AI/ML OPS Engineer",
    "location": "Houston, TX, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210772271",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:52.097055+00:00",
    "date_confidence": "high",
    "description": "Be an integral part of an agile team that's constantly pushing the envelope to enhance, build, and deliver top-notch technology products. As a Lead Software Engineer at JPMorganCha"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210805334",
    "title": "Senior Lead Software Engineer- AI Platform engineer",
    "location": "Seattle, WA, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210805334",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:52.097055+00:00",
    "date_confidence": "high",
    "description": "Be an integral part of an agile team that's constantly pushing the envelope to enhance, build, and deliver top-notch technology products. As a Senior Lead Software Engineer at JPMo"
  }
]
```

## Capital One

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://capitalone.wd12.myworkdayjobs.com/Capital_One`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 181 / 40.610s
- Company elapsed time: 66.404s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 153 / 0 / 0
- Detail cache statuses: {'fetched:new': 135, 'fetched:missing_detail': 18}
- Relevant JD recovery: {'eligible': 49, 'usable_jd': 49}
- Raw jobs found: 526
- After US/location filtering: 153
- With trustworthy posted_date: 153
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.551, "first_pass_survivors": 70, "group": "official", "jds_resolved": 70, "original_postings_resolved": 70, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 70, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 12.054, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.469, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.831, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.812, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.725, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.253, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.775, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 4.657, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001834",
    "title": "Data Engineer 4",
    "location": "McLean, VA; Chicago, IL",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Data-Engineer-4_R1001834-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:53.486134+00:00",
    "date_confidence": "high",
    "description": "Data Engineer 4 Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclusive and iterative "
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1000725",
    "title": "Manager, Product Manager, Audit Insights & Innovation, AI and Data Engineering",
    "location": "McLean, VA; Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Manager--Product-Manager--Audit-Insights---Innovation--AI-and-Data-Engineering_R1000725-2",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:53.486134+00:00",
    "date_confidence": "high",
    "description": "Manager, Product Manager, Audit Insights & Innovation, AI and Data Engineering Product Management at Capital One is a booming, vibrant craft that requires reimagining the status qu"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005455",
    "title": "Full Stack Engineer 5",
    "location": "Plano, TX",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Plano-TX/Full-Stack-Engineer-5_R1005455-2",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:53.486134+00:00",
    "date_confidence": "high",
    "description": "Full Stack Engineer 5 Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclusive and iter"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001603",
    "title": "Full-stack Engineer 4 - RiskTech",
    "location": "McLean, VA; Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Full-stack-Engineer-4---RiskTech_R1001603-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:53.486134+00:00",
    "date_confidence": "high",
    "description": "Full-stack Engineer 4 - RiskTech Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclusi"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005486",
    "title": "Staff Data Engineer - (Director, IC - Card Tech)",
    "location": "McLean, VA; Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Staff-Data-Engineer----Director--IC---Card-Tech-_R1005486-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:33:53.486134+00:00",
    "date_confidence": "high",
    "description": "Staff Data Engineer - (Director, IC - Card Tech) As a Staff Data Engineer at Capital One, you will be part of a community of technical experts working to define the future of data "
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 41
- HTTP requests/cumulative request time: 482 / 148.461s
- Company elapsed time: 214.082s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 441 / 0 / 0
- Detail cache statuses: {'fetched:new': 435, 'fetched:missing_detail': 6}
- Relevant JD recovery: {'eligible': 59, 'usable_jd': 59}
- Raw jobs found: 818
- After US/location filtering: 441
- With trustworthy posted_date: 441
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 26.76, "first_pass_survivors": 62, "group": "official", "jds_resolved": 62, "original_postings_resolved": 62, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 62, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 19.255, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.818, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.924, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 22.175, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 20.215, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.562, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.68, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.393, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 17.752, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "core infrastructure", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.411, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "cleared site reliability engineer database", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.791, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "software developer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 14.345, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "applications developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}

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
    "fetched_at": "2026-11-10T00:34:18.809812+00:00",
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
    "fetched_at": "2026-11-10T00:34:18.809812+00:00",
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
    "fetched_at": "2026-11-10T00:34:18.809812+00:00",
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
    "fetched_at": "2026-11-10T00:34:18.809812+00:00",
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
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:34:18.809812+00:00",
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
- HTTP requests/cumulative request time: 389 / 229.698s
- Company elapsed time: 282.403s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 360 / 0 / 1
- Detail cache statuses: {'fetched:new': 355, 'fetched:missing_detail': 5, 'reuse_after_error:missing_detail': 1}
- Relevant JD recovery: {'eligible': 53, 'ai_skip': 1, 'usable_jd': 53}
- Raw jobs found: 544
- After US/location filtering: 361
- With trustworthy posted_date: 360
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 54.526, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 32.442, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 48.874, "first_pass_survivors": 55, "group": "official", "jds_resolved": 55, "original_postings_resolved": 55, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 55, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 31.57, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 21.573, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 27.12, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 37.421, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.257, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 16.676, "first_pass_survivors": 20, "group": "official", "jds_resolved": 19, "original_postings_resolved": 20, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 7.069, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 1, "pages_fetched": 1, "query": "usa software engineer ii", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 20}

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
    "fetched_at": "2026-11-10T00:34:59.891639+00:00",
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
    "fetched_at": "2026-11-10T00:34:59.891639+00:00",
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
    "fetched_at": "2026-11-10T00:34:59.891639+00:00",
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
    "fetched_at": "2026-11-10T00:34:59.891639+00:00",
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
    "fetched_at": "2026-11-10T00:34:59.891639+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.599s
- Company elapsed time: 2.103s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 92, 'usable_jd': 92}
- Raw jobs found: 464
- After US/location filtering: 461
- With trustworthy posted_date: 461
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:08.414748+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:08.414748+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:08.414748+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:08.414748+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:08.414748+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.333s
- Company elapsed time: 1.340s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 154, 'usable_jd': 154}
- Raw jobs found: 772
- After US/location filtering: 425
- With trustworthy posted_date: 425
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
    "fetched_at": "2026-11-10T00:36:10.518569+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>Who we are </strong></h2> <h3><strong>About Stripe</strong></h3> <p><span style=\"font-weight: 400;\">Stripe is a financial infrastructure platform for businesses. Millio"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8332467",
    "title": "Account Executive, AI Sales",
    "location": "San Francisco, CA; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8332467",
    "posted_date": "2026-11-06",
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:36:10.518569+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies - from the world’s largest enterprises to the most "
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
    "fetched_at": "2026-11-10T00:36:10.518569+00:00",
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
    "fetched_at": "2026-11-10T00:36:10.518569+00:00",
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
    "fetched_at": "2026-11-10T00:36:10.518569+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies - from the world’s largest enterprises to the most "
  }
]
```

## Coinbase

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/coinbase/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.133s
- Company elapsed time: 0.795s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 54, 'usable_jd': 54}
- Raw jobs found: 285
- After US/location filtering: 208
- With trustworthy posted_date: 208
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
    "fetched_at": "2026-11-10T00:36:11.860033+00:00",
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
    "fetched_at": "2026-11-10T00:36:11.860033+00:00",
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
    "fetched_at": "2026-11-10T00:36:11.860033+00:00",
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
    "fetched_at": "2026-11-10T00:36:11.860033+00:00",
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
    "fetched_at": "2026-11-10T00:36:11.860033+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.178s
- Company elapsed time: 0.771s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 41, 'usable_jd': 41}
- Raw jobs found: 154
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
    "fetched_at": "2026-11-10T00:36:12.656302+00:00",
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
    "fetched_at": "2026-11-10T00:36:12.656302+00:00",
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
    "fetched_at": "2026-11-10T00:36:12.656302+00:00",
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
    "fetched_at": "2026-11-10T00:36:12.656302+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8303977",
    "title": "Clearing Operations Program Manager",
    "location": "Chicago, IL; Denver, CO; Lake Mary, FL; New York, NY; Chicago, IL; Denver, CO; Lake Mary, FL; New York, NY",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8303977?t=gh_src=&gh_jid=8303977",
    "posted_date": "2026-10-28",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-10T00:36:12.656302+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.162s
- Company elapsed time: 0.551s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 41, 'usable_jd': 41}
- Raw jobs found: 146
- After US/location filtering: 95
- With trustworthy posted_date: 95
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
    "fetched_at": "2026-11-10T00:36:13.428816+00:00",
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
    "fetched_at": "2026-11-10T00:36:13.428816+00:00",
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
    "fetched_at": "2026-11-10T00:36:13.428816+00:00",
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
    "fetched_at": "2026-11-10T00:36:13.428816+00:00",
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
    "fetched_at": "2026-11-10T00:36:13.428816+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.188s
- Company elapsed time: 0.829s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 251
- After US/location filtering: 145
- With trustworthy posted_date: 145
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:36:13.981293+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:36:13.981293+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:36:13.981293+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8891301002",
    "title": "Backend Engineer (Ruby), Create: Change Record",
    "location": "Remote, Poland; Remote, United Kingdom; Turkey",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8891301002",
    "posted_date": "2026-10-19",
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:13.981293+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:36:13.981293+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.082s
- Company elapsed time: 0.165s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 27
- After US/location filtering: 27
- With trustworthy posted_date: 27
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:14.810665+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:14.810665+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:14.810665+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:14.810665+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:36:14.810665+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.134s
- Company elapsed time: 0.460s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 13, 'usable_jd': 13}
- Raw jobs found: 111
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
    "fetched_at": "2026-11-10T00:36:14.977031+00:00",
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
    "fetched_at": "2026-11-10T00:36:14.977031+00:00",
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
    "fetched_at": "2026-11-10T00:36:14.977031+00:00",
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
    "fetched_at": "2026-11-10T00:36:14.977031+00:00",
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
    "fetched_at": "2026-11-10T00:36:14.977031+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.181s
- Company elapsed time: 0.917s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 42, 'usable_jd': 42}
- Raw jobs found: 265
- After US/location filtering: 251
- With trustworthy posted_date: 251
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
    "fetched_at": "2026-11-10T00:36:15.438544+00:00",
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
    "fetched_at": "2026-11-10T00:36:15.438544+00:00",
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
    "fetched_at": "2026-11-10T00:36:15.438544+00:00",
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
    "fetched_at": "2026-11-10T00:36:15.438544+00:00",
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
    "fetched_at": "2026-11-10T00:36:15.438544+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.267s
- Company elapsed time: 1.541s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 58, 'usable_jd': 58}
- Raw jobs found: 314
- After US/location filtering: 276
- With trustworthy posted_date: 276
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
    "fetched_at": "2026-11-10T00:36:16.356599+00:00",
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
    "fetched_at": "2026-11-10T00:36:16.356599+00:00",
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
    "fetched_at": "2026-11-10T00:36:16.356599+00:00",
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
    "fetched_at": "2026-11-10T00:36:16.356599+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8319771",
    "title": "Account Development Representative II - Atlanta",
    "location": "Atlanta, Georgia, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8319771?gh_jid=8319771",
    "posted_date": "2026-10-23",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-10T00:36:16.356599+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.126s
- Company elapsed time: 0.393s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 24, 'usable_jd': 24}
- Raw jobs found: 156
- After US/location filtering: 90
- With trustworthy posted_date: 90
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
    "fetched_at": "2026-11-10T00:36:17.899200+00:00",
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
    "fetched_at": "2026-11-10T00:36:17.899200+00:00",
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
    "fetched_at": "2026-11-10T00:36:17.899200+00:00",
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
    "fetched_at": "2026-11-10T00:36:17.899200+00:00",
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
    "fetched_at": "2026-11-10T00:36:17.899200+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.173s
- Company elapsed time: 0.270s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 13, 'usable_jd': 13}
- Raw jobs found: 85
- After US/location filtering: 62
- With trustworthy posted_date: 62
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
    "fetched_at": "2026-11-10T00:36:18.293467+00:00",
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
    "fetched_at": "2026-11-10T00:36:18.293467+00:00",
    "date_confidence": "high",
    "description": "• Identify and pursue new business opportunities with organizations of 1,000+ employees. This is a “Hunter” role with significant inbound and SDR support. • Research and prospect i"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "a4651332-6400-40e8-8c22-5491e7a34161",
    "title": "Analyst, Royalty Operations",
    "location": "Stockholm",
    "official_url": "https://jobs.lever.co/spotify/a4651332-6400-40e8-8c22-5491e7a34161",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:18.293467+00:00",
    "date_confidence": "high",
    "description": "Build a deep understanding of Spotify’s label, publishing, lyrics, and audiobook contracts, how they’re implemented in our royalty systems, and how they flow into royalty calculati"
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
    "fetched_at": "2026-11-10T00:36:18.293467+00:00",
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
    "fetched_at": "2026-11-10T00:36:18.293467+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.111s
- Company elapsed time: 0.469s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 65, 'usable_jd': 65}
- Raw jobs found: 171
- After US/location filtering: 157
- With trustworthy posted_date: 157
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
    "fetched_at": "2026-11-10T00:36:18.565526+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $275B in annualized"
  },
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "f564dcf9-9390-4a3f-896f-8047a5086040",
    "title": "Software Engineer, Android",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote (Canada); San Francisco, CA; Remote (US)",
    "official_url": "https://jobs.ashbyhq.com/ramp/f564dcf9-9390-4a3f-896f-8047a5086040",
    "posted_date": "2025-07-31",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:18.565526+00:00",
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
    "fetched_at": "2026-11-10T00:36:18.565526+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $275B in annualized"
  },
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "4859cd5e-f2a9-44d7-81f7-8bfc0e62369f",
    "title": "Software Engineer, iOS",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote (Canada); San Francisco, CA; Remote (US)",
    "official_url": "https://jobs.ashbyhq.com/ramp/4859cd5e-f2a9-44d7-81f7-8bfc0e62369f",
    "posted_date": "2025-07-31",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:18.565526+00:00",
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
    "fetched_at": "2026-11-10T00:36:18.565526+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.118s
- Company elapsed time: 0.318s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 37, 'usable_jd': 37}
- Raw jobs found: 153
- After US/location filtering: 78
- With trustworthy posted_date: 78
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
    "fetched_at": "2026-11-10T00:36:19.035095+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.035095+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.035095+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.035095+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.035095+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.043s
- Company elapsed time: 0.090s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 32
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
    "fetched_at": "2026-11-10T00:36:19.354462+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.354462+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.354462+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.354462+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.354462+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.099s
- Company elapsed time: 0.347s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 36, 'usable_jd': 36}
- Raw jobs found: 127
- After US/location filtering: 105
- With trustworthy posted_date: 105
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "7133d205-5421-4336-a8e2-6037b5f55073",
    "title": "Senior Full-Stack Engineer, Annotation Platform",
    "location": "Toronto; Toronto, Ontario, Canada; Canada; United States; New York; Vancouver; Ottawa; Montreal; Remote, Canada",
    "official_url": "https://jobs.ashbyhq.com/cohere/7133d205-5421-4336-a8e2-6037b5f55073",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:19.445522+00:00",
    "date_confidence": "high",
    "description": "WHO ARE WE? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  },
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "3136a5a5-06fd-4c82-8b72-a43467e6b128",
    "title": "Member of Technical Staff, Modeling",
    "location": "London; London, London, United Kingdom; San Francisco; New York; Paris; Toronto; Montreal; Remote, United Kingdom",
    "official_url": "https://jobs.ashbyhq.com/cohere/3136a5a5-06fd-4c82-8b72-a43467e6b128",
    "posted_date": "2024-11-01",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:19.445522+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.445522+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.445522+00:00",
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
    "fetched_at": "2026-11-10T00:36:19.445522+00:00",
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
- HTTP requests/cumulative request time: 272 / 71.856s
- Company elapsed time: 110.434s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 227 / 0 / 0
- Detail cache statuses: {'fetched:new': 215, 'fetched:missing_detail': 12}
- Relevant JD recovery: {'eligible': 63, 'usable_jd': 63}
- Raw jobs found: 840
- After US/location filtering: 227
- With trustworthy posted_date: 227
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 21.085, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 16.387, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.905, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 4.031, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.705, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.473, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.041, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.197, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 47, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 47}
- Query diagnostic: {"elapsed_seconds": 5.047, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 1.546, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "full stack backend", "raw_jobs": 33, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 7.727, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.862, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "cloud engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.248, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "security engineer remote", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.142, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "software engineer collaboration devices", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 6.832, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "splunk engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.208, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer solution test iq platform", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2029363",
    "title": "Senior Hardware Design Engineer",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Senior-Hardware-Design-Engineer_2029363",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:19.793160+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 01/28/2027 Meet the Team Our Hardware Engineering team is the backbone of Cisco's innovation, designing and delivering next-generati"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2029360",
    "title": "Hardware Design Engineer",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Hardware-Design-Engineer_2029360",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:19.793160+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 01/28/2027 Meet the Team Our Hardware Engineering team is the backbone of Cisco's innovation, designing and delivering next-generati"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2024550",
    "title": "CX Machine Learning Engineer",
    "location": "San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/CX-Machine-Learning-Engineer_2024550",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:19.793160+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 11/15/2026 This is a hybrid role, requiring 3 days per week in office in San Jose, CA Meet the Team Cisco’s Customer Experience (CX)"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2028307",
    "title": "Senior Software Engineer",
    "location": "San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Senior-Software-Engineer_2028307",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:19.793160+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 11/19/2026 Meet the Team We're building an enterprise platform for AI agents — the shared foundation that lets engineering teams bui"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2026192",
    "title": "Technical Product Manager",
    "location": "RTP, North Carolina, US; San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/RTP-North-Carolina-US/Technical-Product-Manager_2026192",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:36:19.793160+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 11/29/2026 Meet the Team The Enterprise AI & Analytics team is dedicated to defining and advancing AI product capabilities that inte"
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://careers.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 139 / 56.827s
- Company elapsed time: 83.189s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 107 / 0 / 0
- Detail cache statuses: {'fetched:new': 107}
- Relevant JD recovery: {'eligible': 38, 'usable_jd': 38}
- Raw jobs found: 800
- After US/location filtering: 107
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 56.156, "first_pass_survivors": 95, "group": "official", "jds_resolved": 95, "original_postings_resolved": 95, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 95, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.19, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 5.636, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 4.851, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.152, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.247, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.192, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.167, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 3.43, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.168, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "cloud developer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}

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
    "fetched_at": "2026-11-10T00:37:11.273995+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1409064033",
    "title": "Machine Learning Engineer - Bellevue, WA",
    "location": "Bellevue, WA, US, 98004",
    "official_url": "https://careers.sap.com/job/Bellevue-Machine-Learning-Engineer-Bellevue%2C-WA-WA-98004/1409064033/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:37:11.273995+00:00",
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
    "fetched_at": "2026-11-10T00:37:11.273995+00:00",
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
    "fetched_at": "2026-11-10T00:37:11.273995+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1445797733",
    "title": "Distinguished AI Architect, oCTO Industry AI",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://careers.sap.com/job/Palo-Alto-Distinguished-AI-Architect%2C-oCTO-Industry-AI-CA-94304/1445797733/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:37:11.273995+00:00",
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
- HTTP requests/cumulative request time: 319 / 141.435s
- Company elapsed time: 184.562s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 292 / 0 / 0
- Detail cache statuses: {'fetched:new': 281, 'fetched:missing_detail': 11}
- Relevant JD recovery: {'eligible': 132, 'usable_jd': 132}
- Raw jobs found: 492
- After US/location filtering: 292
- With trustworthy posted_date: 292
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 42.617, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 23.483, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 56, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 2.416, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 29.772, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.152, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 23.948, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.176, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.677, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 17.6, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.324, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "ai workflow specialist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 7}

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
    "fetched_at": "2026-11-10T00:37:28.691427+00:00",
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
    "fetched_at": "2026-11-10T00:37:28.691427+00:00",
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
    "fetched_at": "2026-11-10T00:37:28.691427+00:00",
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
    "fetched_at": "2026-11-10T00:37:28.691427+00:00",
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
    "fetched_at": "2026-11-10T00:37:28.691427+00:00",
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
- HTTP requests/cumulative request time: 36 / 15.359s
- Company elapsed time: 21.843s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 9 / 7 / 81
- Detail cache statuses: {'reused': 5, 'fetched:stale': 1, 'reuse_after_error:stale': 1}
- Relevant JD recovery: {'deterministic_skip': 72, 'cache_reused': 7, 'eligible': 14, 'ai_skip': 9, 'detail_requests': 9, 'detail_failure': 8, 'detail_success': 1, 'last_good_reused': 1, 'budget_deferred': 0, 'usable_jd': 7}
- Raw jobs found: 270
- After US/location filtering: 95
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.727, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.254, "first_pass_survivors": 14, "group": "official", "jds_resolved": 0, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.944, "first_pass_survivors": 16, "group": "official", "jds_resolved": 0, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.796, "first_pass_survivors": 15, "group": "official", "jds_resolved": 0, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.466, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.491, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.515, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.938, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.916, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

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
    "fetched_at": "2026-11-10T00:37:52.893364+00:00",
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
    "fetched_at": "2026-11-10T00:37:52.893364+00:00",
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
    "fetched_at": "2026-11-10T00:37:52.893364+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "102963747664",
    "title": "Lead Software Engineer",
    "location": "Lake Buena Vista, Florida",
    "official_url": "https://www.disneycareers.com/en/job/lake-buena-vista/lead-software-engineer/391/102963747664",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:37:52.893364+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10142399",
    "title": "Sr Software Engineer - Content Platform Engineering",
    "location": "Glendale, California / Bristol, Connecticut",
    "official_url": "https://www.disneycareers.com/en/job/glendale/sr-software-engineer-content-platform-engineering/391/92060003760",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:37:52.893364+00:00",
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
- Pages/requests fetched: 17
- HTTP requests/cumulative request time: 59 / 29.490s
- Company elapsed time: 36.566s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 41 / 0 / 0
- Detail cache statuses: {'fetched:new': 40, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 13, 'usable_jd': 13}
- Raw jobs found: 192
- After US/location filtering: 41
- With trustworthy posted_date: 41
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 22.296, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 39, "stop_reason": "early_stop", "unique_contribution": 39, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 0.706, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.685, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.67, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 2.952, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 3.121, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 2.87, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 0.664, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.671, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 18}

Sample normalized records:

```json
[
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0077480",
    "title": "Network Engineer 3",
    "location": "San Jose",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/San-Jose/Network-Engineer-3_R0077480",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:10.228216+00:00",
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
    "fetched_at": "2026-11-10T00:38:10.228216+00:00",
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
    "fetched_at": "2026-11-10T00:38:10.228216+00:00",
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
    "fetched_at": "2026-11-10T00:38:10.228216+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0076916",
    "title": "Security Operations Engineer",
    "location": "Austin",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Austin/Security-Operations-Engineer_R0076916",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:10.228216+00:00",
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
- HTTP requests/cumulative request time: 152 / 24.162s
- Company elapsed time: 46.341s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 125 / 0 / 0
- Detail cache statuses: {'fetched:new': 122, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 255
- After US/location filtering: 125
- With trustworthy posted_date: 125
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 9.099, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.495, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.885, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 8.244, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.498, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.381, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.263, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.473, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.669, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 29}

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3099009",
    "title": "Director, Product Management - Camera & Machine Vision",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446722038050",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:12.941329+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Operations Group, Operations Group > Product Management General Summary: Qualcomm is seeking a Director of Product Management to own "
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3099011",
    "title": "Senior Director, Product Management - IoT Processors - Camera and Industrial",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446722038056",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:12.941329+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Operations Group, Operations Group > Product Management General Summary: Qualcomm is seeking a Senior Director of Product Management "
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3099089",
    "title": "Embedded Software Engineer, Senior",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446722039937",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:12.941329+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Software Engineering General Summary: The Products team within the Core Platform development g"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3098816",
    "title": "Graphics Software Engineer, Staff",
    "location": "San Diego, California, United States of America; Boxborough, Massachusetts, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721915454",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:12.941329+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Graphics Software Engineering General Summary: As a leading technology innovator, Qualcomm pus"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095472",
    "title": "Sr, Technical Program Manager",
    "location": "Santa Clara, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720845422",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:12.941329+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Services Group, Engineering Services Group > Program Management General Summary: The successful candidate will own techni"
  }
]
```

## AMD

- Status: ok
- Scraping method: HTTP GET public Jibe/iCIMS jobs JSON
- Search URL/API: `https://careers.amd.com/api/jobs`
- Pagination: page=1,2,... per role query; stop on total/empty/repeat/short page
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 14 / 9.533s
- Company elapsed time: 11.491s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 221, 'usable_jd': 221}
- Raw jobs found: 1378
- After US/location filtering: 564
- With trustworthy posted_date: 564
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.764, "first_pass_survivors": 379, "group": "official", "jds_resolved": 379, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 379, "stop_reason": "page_budget", "unique_contribution": 379, "unique_jobs": 379}
- Query diagnostic: {"elapsed_seconds": 0.793, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning", "raw_jobs": 100, "stop_reason": "early_stop", "unique_contribution": 29, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.423, "first_pass_survivors": 75, "group": "official", "jds_resolved": 75, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 75, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 2.239, "first_pass_survivors": 67, "group": "official", "jds_resolved": 67, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "AI research", "raw_jobs": 299, "stop_reason": "page_budget", "unique_contribution": 67, "unique_jobs": 299}
- Query diagnostic: {"elapsed_seconds": 2.27, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 300}

Sample normalized records:

```json
[
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92045",
    "title": "HPC & AI Research Engineer / Software Engineer",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-09-10",
    "updated_date": "2026-11-07",
    "fetched_at": "2026-11-10T00:38:34.463937+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "86806",
    "title": "Security Software Engineer",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-06-17",
    "updated_date": "2026-11-07",
    "fetched_at": "2026-11-10T00:38:34.463937+00:00",
    "date_confidence": "high",
    "description": "WHAT YOU DO AT AMD CHANGES EVERYTHING At AMD, our mission is to build great products that accelerate next-generation computing experiences—from AI and data centers, to PCs, gaming "
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92004",
    "title": "Senior GPU Performance Software Engineer",
    "location": "Austin, Texas",
    "official_url": "",
    "posted_date": "2026-10-05",
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:38:34.463937+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:38:34.463937+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92603",
    "title": "Software Engineer - Networking, firmware and C++",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-10-05",
    "updated_date": "2026-11-07",
    "fetched_at": "2026-11-10T00:38:34.463937+00:00",
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
- Pages/requests fetched: 15
- HTTP requests/cumulative request time: 41 / 45.172s
- Company elapsed time: 49.818s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 25 / 0 / 0
- Detail cache statuses: {'fetched:new': 24, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 106
- After US/location filtering: 25
- With trustworthy posted_date: 25
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 40.688, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 21, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.461, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.423, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.837, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 2.39, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 2.044, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 0.591, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.418, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.431, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}

Sample normalized records:

```json
[
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19678",
    "title": "Premier Support Manager",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Premier-Support-Manager_R19678-1",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:45.956133+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect Lead a team of Technical Account Managers at the center of Zoom's most strategic enterprise relationships, directly shaping customer outcomes and the long-term "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19753",
    "title": "Audio AI Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Audio-AI-Engineer_R19753-1",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:45.956133+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect As an Audio AI Engineer on Zoom's applied research team, you will advance the frontier of audio intelligence by developing and deploying machine-learning models"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19731",
    "title": "Full Stack Developer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Full-Stack-Developer_R19731-1",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:45.956133+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect As a Full Stack Developer at Zoom, you will take end-to-end ownership of features and services that reach users worldwide, from design through deployment, monit"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19605",
    "title": "Lead Technical SEO Manager",
    "location": "Remote (US)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--US/Lead-Technical-SEO-Manager_R19605",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:45.956133+00:00",
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
    "fetched_at": "2026-11-10T00:38:45.956133+00:00",
    "date_confidence": "high",
    "description": "AI Scientist - (AI Verticals) What You Can Expect In this role, you will tackle one of the most compelling challenges in production AI: enabling agents to continuously improve with"
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
- HTTP requests/cumulative request time: 1 / 0.212s
- Company elapsed time: 1.081s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 57, 'usable_jd': 57}
- Raw jobs found: 369
- After US/location filtering: 234
- With trustworthy posted_date: 234
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
    "fetched_at": "2026-11-10T00:38:46.795414+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8352551",
    "title": "Account Executive, Cloud & Data Services",
    "location": "Remote, United States; North America",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8352551",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-08",
    "fetched_at": "2026-11-10T00:38:46.795414+00:00",
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
    "fetched_at": "2026-11-10T00:38:46.795414+00:00",
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
    "fetched_at": "2026-11-10T00:38:46.795414+00:00",
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
    "fetched_at": "2026-11-10T00:38:46.795414+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.331s
- Company elapsed time: 2.202s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 76, 'usable_jd': 76}
- Raw jobs found: 915
- After US/location filtering: 489
- With trustworthy posted_date: 489
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
    "fetched_at": "2026-11-10T00:38:47.877706+00:00",
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
    "fetched_at": "2026-11-10T00:38:47.877706+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:38:47.877706+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:38:47.877706+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:38:47.877706+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.142s
- Company elapsed time: 0.893s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 31, 'usable_jd': 31}
- Raw jobs found: 272
- After US/location filtering: 254
- With trustworthy posted_date: 254
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:38:50.080591+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:38:50.080591+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:38:50.080591+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:38:50.080591+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:38:50.080591+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.139s
- Company elapsed time: 0.600s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 202
- After US/location filtering: 108
- With trustworthy posted_date: 108
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
    "fetched_at": "2026-11-10T00:38:50.975048+00:00",
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
    "fetched_at": "2026-11-10T00:38:50.975048+00:00",
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
    "fetched_at": "2026-11-10T00:38:50.975048+00:00",
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
    "fetched_at": "2026-11-10T00:38:50.975048+00:00",
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
    "fetched_at": "2026-11-10T00:38:50.975048+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.315s
- Company elapsed time: 2.812s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 164, 'usable_jd': 164}
- Raw jobs found: 671
- After US/location filtering: 539
- With trustworthy posted_date: 539
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
    "fetched_at": "2026-11-10T00:38:51.576090+00:00",
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
    "fetched_at": "2026-11-10T00:38:51.576090+00:00",
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
    "fetched_at": "2026-11-10T00:38:51.576090+00:00",
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
    "fetched_at": "2026-11-10T00:38:51.576090+00:00",
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
    "fetched_at": "2026-11-10T00:38:51.576090+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.102s
- Company elapsed time: 0.231s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 40
- After US/location filtering: 30
- With trustworthy posted_date: 30
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4724999006",
    "title": "Agency Development Lead - Independent Agencies",
    "location": "Los Angeles/Santa Monica, CA; New York City, NY",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4724999006?gh_jid=4724999006",
    "posted_date": "2026-10-26",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-10T00:38:54.389203+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4724788006",
    "title": "Agency Development Lead - Independent Agencies",
    "location": "New York City, NY",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4724788006?gh_jid=4724788006",
    "posted_date": "2026-10-26",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-10T00:38:54.389203+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4681211006",
    "title": "Business Development Associate (Consumer)",
    "location": "Guangzhou - Remote; Remote - Shenzhen; Shanghai; Shanghai",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4681211006?gh_jid=4681211006",
    "posted_date": "2026-05-12",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-10T00:38:54.389203+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4723470006",
    "title": "Business Operations Analyst",
    "location": "Toronto; Palo Alto, CA",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4723470006?gh_jid=4723470006",
    "posted_date": "2026-10-21",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-10T00:38:54.389203+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4723320006",
    "title": "Business Operations Analyst",
    "location": "Palo Alto, CA",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4723320006?gh_jid=4723320006",
    "posted_date": "2026-10-20",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-10T00:38:54.389203+00:00",
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
- HTTP requests/cumulative request time: 24 / 24.668s
- Company elapsed time: 28.273s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 235, 'usable_jd': 235}
- Raw jobs found: 1067
- After US/location filtering: 461
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.952, "first_pass_survivors": 142, "group": "official", "jds_resolved": 142, "original_postings_resolved": 142, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 142, "unique_jobs": 147}
- Query diagnostic: {"elapsed_seconds": 4.045, "first_pass_survivors": 103, "group": "official", "jds_resolved": 103, "original_postings_resolved": 103, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 103, "unique_jobs": 147}
- Query diagnostic: {"elapsed_seconds": 3.123, "first_pass_survivors": 64, "group": "official", "jds_resolved": 64, "original_postings_resolved": 64, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 109, "stop_reason": "page_budget", "unique_contribution": 64, "unique_jobs": 109}
- Query diagnostic: {"elapsed_seconds": 3.416, "first_pass_survivors": 64, "group": "official", "jds_resolved": 64, "original_postings_resolved": 64, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 64, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.333, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 148}
- Query diagnostic: {"elapsed_seconds": 3.247, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 149}
- Query diagnostic: {"elapsed_seconds": 1.975, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 55, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 55}
- Query diagnostic: {"elapsed_seconds": 0.878, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 3.303, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 150}

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
    "fetched_at": "2026-11-10T00:38:54.621336+00:00",
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
    "fetched_at": "2026-11-10T00:38:54.621336+00:00",
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
    "fetched_at": "2026-11-10T00:38:54.621336+00:00",
    "date_confidence": "unknown",
    "description": "We are seeking an experienced Research Scientist or Engineer to help define and build the next generation of AI infrastructure. In this role, you will work at the intersection of l"
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
    "fetched_at": "2026-11-10T00:38:54.621336+00:00",
    "date_confidence": "unknown",
    "description": "About the Team Join ByteDance’s database R&D team, where you’ll build and own cutting-edge database products supporting ByteDance’s global infrastructure. Our diverse portfolio inc"
  },
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7499642155158554898",
    "title": "Software Engineer / Researcher, AI-Native database systems",
    "location": "Seattle, Washington, United States of America",
    "official_url": "https://joinbytedance.com/search/7499642155158554898",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:54.621336+00:00",
    "date_confidence": "unknown",
    "description": "About the Team Join ByteDance’s database R&D team, where you’ll build and own cutting-edge database products supporting Bytedance’s global infrastructure. Our diverse portfolio inc"
  }
]
```

## Chime

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/chime/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.169s
- Company elapsed time: 0.480s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 66
- After US/location filtering: 66
- With trustworthy posted_date: 66
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
    "fetched_at": "2026-11-10T00:38:59.283486+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role</h2> <p>Chime's Data Science &amp; Machine Learning team builds the models, services, and platforms behind how millions of members manage and grow their financia"
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
    "fetched_at": "2026-11-10T00:38:59.283486+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\"><strong>About the Role</strong></span></h2> <p><span style=\"font-family: helvetica, arial, sans-serif;\">We are hiring a"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8918533002",
    "title": "Content Marketing Manager, SEO & AI Search",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8918533002?gh_jid=8918533002",
    "posted_date": "2026-10-26",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-10T00:38:59.283486+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the Role</strong></h2> <p>People increasingly find financial products by asking ChatGPT, Gemini, and Google's AI Overviews and AI Mode instead of scrolling search"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8904126002",
    "title": "Data Scientist, Dispute Risk",
    "location": "Chicago, IL, USA; Chicago, Illinois, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8904126002?gh_jid=8904126002",
    "posted_date": "2026-11-09",
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:38:59.283486+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the role</strong></h2> <p>We’re hiring a data-driven Risk Analyst with strong analytical skills and an investigative mindset. You’ll help reduce fraud losses, imp"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8529549002",
    "title": "Director, Corporate Strategy",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8529549002?gh_jid=8529549002",
    "posted_date": "2026-05-13",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-10T00:38:59.283486+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the role</strong></h2> <p>We are hiring for a Director, Strategy and Growth Initiatives to help define and drive the long-term strategy and growth of the company."
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
- HTTP requests/cumulative request time: 139 / 45.779s
- Company elapsed time: 65.941s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 114 / 0 / 0
- Detail cache statuses: {'fetched:new': 112, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 33, 'usable_jd': 33}
- Raw jobs found: 490
- After US/location filtering: 114
- With trustworthy posted_date: 114
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.393, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.358, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.583, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 7.545, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.202, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.586, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.961, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.184, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.129, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "302373",
    "title": "AI PC Performance Engineer",
    "location": "Austin, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/302373",
    "posted_date": "2026-11-07",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:59.764589+00:00",
    "date_confidence": "high",
    "description": "AI PC Performance Engineer Dell's Client Product Group (CPG) is seeking an AI Performance Engineer to join the PC Systems Performance team. In this role, you will build foundationa"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "299245",
    "title": "AI Performance Engineer",
    "location": "Austin, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/299245",
    "posted_date": "2026-10-23",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:38:59.764589+00:00",
    "date_confidence": "high",
    "description": "AI Performance Engineer Dell's Client Product Group (CPG) is seeking an AI Performance Engineer to join the PC Systems Performance team. In this role, you will build foundational e"
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
    "fetched_at": "2026-11-10T00:38:59.764589+00:00",
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
    "fetched_at": "2026-11-10T00:38:59.764589+00:00",
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
    "fetched_at": "2026-11-10T00:38:59.764589+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.122s
- Company elapsed time: 0.215s
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:39:22.895532+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:39:22.895532+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:39:22.895532+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:39:22.895532+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:39:22.895532+00:00",
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
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 69 / 19.019s
- Company elapsed time: 28.553s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 50 / 0 / 0
- Detail cache statuses: {'fetched:new': 50}
- Relevant JD recovery: {'eligible': 14, 'usable_jd': 14}
- Raw jobs found: 319
- After US/location filtering: 50
- With trustworthy posted_date: 50
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.836, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.742, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 32, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 0.27, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 1.217, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 39, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 1.596, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.944, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.315, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.241, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.391, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 42}

Sample normalized records:

```json
[
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-110889",
    "title": "Software Development Engineer III, Advertising Technology",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Software-Development-Engineer-III--Advertising-Technology_R-110889-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:23.111271+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-110864",
    "title": "Software Development Engineer II, Advertising Technology",
    "location": "USA - Illinois - Chicago",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---Illinois---Chicago/Software-Development-Engineer-II--Advertising-Technology_R-110864-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:23.111271+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109908",
    "title": "Software Development Engineer III",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Software-Development-Engineer-III_R-109908",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:23.111271+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-110856",
    "title": "Sr Manager, Software Engineering",
    "location": "Austin Domain 11 - HomeAway; Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Austin-Domain-11---HomeAway/Sr-Manager--Software-Engineering_R-110856",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:23.111271+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-110857",
    "title": "Data Engineer III",
    "location": "Austin Domain 11 - HomeAway; Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Austin-Domain-11---HomeAway/Data-Engineer-III_R-110857-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:23.111271+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.148s
- Company elapsed time: 0.225s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 127
- After US/location filtering: 14
- With trustworthy posted_date: 14
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
    "fetched_at": "2026-11-10T00:39:35.775706+00:00",
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
    "fetched_at": "2026-11-10T00:39:35.775706+00:00",
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
    "fetched_at": "2026-11-10T00:39:35.775706+00:00",
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
    "fetched_at": "2026-11-10T00:39:35.775706+00:00",
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
    "fetched_at": "2026-11-10T00:39:35.775706+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.141s
- Company elapsed time: 0.434s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
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
    "fetched_at": "2026-11-10T00:39:36.002247+00:00",
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
    "fetched_at": "2026-11-10T00:39:36.002247+00:00",
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
    "fetched_at": "2026-11-10T00:39:36.002247+00:00",
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
    "fetched_at": "2026-11-10T00:39:36.002247+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8232312",
    "title": "Billing Operations Lead",
    "location": "Canada - Remote (ON, AB, BC, or NS Only); Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8232312",
    "posted_date": "2026-09-25",
    "updated_date": "2026-09-25",
    "fetched_at": "2026-11-10T00:39:36.002247+00:00",
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
- HTTP requests/cumulative request time: 179 / 81.546s
- Company elapsed time: 106.649s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 151 / 0 / 0
- Detail cache statuses: {'fetched:new': 136, 'fetched:missing_detail': 15}
- Relevant JD recovery: {'eligible': 97, 'usable_jd': 97}
- Raw jobs found: 493
- After US/location filtering: 151
- With trustworthy posted_date: 151
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.601, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 7.238, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 8.922, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 12.097, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 19.317, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 10.311, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 12.466, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 1.287, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 8.485, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 80}

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
    "fetched_at": "2026-11-10T00:39:36.437666+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: About the Job Intel is seeking exceptional Computer Science, Electrical Engineering, Computer Engineering, and AI/ML students to join an AI Hardware E"
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
    "fetched_at": "2026-11-10T00:39:36.437666+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Software and AI (SAI) organization is looking for a software development engineer to work on oneDNN project ( https://github.com/uxlfoundation/oneDNN "
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0284193",
    "title": "Neuromorphic/AI Research Scientist",
    "location": "US, California, Santa Clara; US, Oregon, Hillsboro; US, California, Folsom; US, Texas, Austin; US, Arizona, Phoenix",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-California-Santa-Clara/Neuromorphic-AI-Research-Scientist_JR0284193",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:36.437666+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel's Neuromorphic Computing Lab has been at the forefront of brain-inspired computing for nearly a decade, working alongside a global ecosystem of "
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
    "fetched_at": "2026-11-10T00:39:36.437666+00:00",
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
    "fetched_at": "2026-11-10T00:39:36.437666+00:00",
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
- HTTP requests/cumulative request time: 50 / 18.601s
- Company elapsed time: 20.251s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 38 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 109
- After US/location filtering: 38
- With trustworthy posted_date: 38
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.975, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 20, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.217, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 0.958, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 2.784, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 2.413, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 1.167, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.557, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.455, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.724, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 26, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 26}

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
    "fetched_at": "2026-11-10T00:39:42.296211+00:00",
    "date_confidence": "high",
    "description": "<p>About this Program</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage"
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
    "fetched_at": "2026-11-10T00:39:42.296211+00:00",
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
    "fetched_at": "2026-11-10T00:39:42.296211+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37377",
    "title": "Senior Application Engineer - AI and Embedded Systems",
    "location": "US-TX-Plano",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37377-senior-application-engineer-ai-and-embedded-systems?keywords=ai+engineer",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:42.296211+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "12382",
    "title": "Compiler Engineer LLVM",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/12382-compiler-engineer-llvm?keywords=ai+engineer",
    "posted_date": "2025-04-01",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:42.296211+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.262s
- Company elapsed time: 1.057s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 31, 'usable_jd': 31}
- Raw jobs found: 375
- After US/location filtering: 237
- With trustworthy posted_date: 237
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
    "fetched_at": "2026-11-10T00:39:51.665473+00:00",
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
    "fetched_at": "2026-11-10T00:39:51.665473+00:00",
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
    "fetched_at": "2026-11-10T00:39:51.665473+00:00",
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
    "fetched_at": "2026-11-10T00:39:51.665473+00:00",
    "date_confidence": "high",
    "description": "<p>At MongoDB, our Account Development team works closely with our partners in both Sales and Marketing to build fanatical customer enthusiasm around MongoDB. ADR reps are responsi"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7217822",
    "title": "Account Executive, Growth",
    "location": "Zurich; Zürich, Zürich, Switzerland",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7217822",
    "posted_date": "2025-10-07",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-10T00:39:51.665473+00:00",
    "date_confidence": "high",
    "description": "<p>We’re looking for a hardworking, driven individual with superb energy, passion and initiative for new business acquisition. The Enterprise Account Executive role focuses exclusi"
  }
]
```

## Morgan Stanley

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://morganstanley.eightfold.ai/api/pcsx/search?domain=morganstanley.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 126 / 19.069s
- Company elapsed time: 36.925s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 101 / 0 / 0
- Detail cache statuses: {'fetched:new': 101}
- Relevant JD recovery: {'eligible': 26, 'usable_jd': 26}
- Raw jobs found: 226
- After US/location filtering: 101
- With trustworthy posted_date: 101
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 9.432, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.226, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.688, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 5.531, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 2.713, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.004, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.529, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.192, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.349, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "JR042774",
    "title": "Director, Lead Software Engineer",
    "location": "Alpharetta, Georgia, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800007824",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:52.724225+00:00",
    "date_confidence": "high",
    "description": "Company Profile: Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment, and wealth management services. Th"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "JR042778",
    "title": "Director, QA Engineer",
    "location": "Alpharetta, Georgia, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800008069",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:52.724225+00:00",
    "date_confidence": "high",
    "description": "Company Profile: Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment, and wealth management services. Th"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "JR042814",
    "title": "Associate, Software Engineer",
    "location": "Alpharetta, Georgia, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800008226",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:52.724225+00:00",
    "date_confidence": "high",
    "description": "Company Profile: Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment, and wealth management services. Th"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR046036",
    "title": "Vice President - Lead Software Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800999704",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:52.724225+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "JR040314",
    "title": "Director - Applied AI",
    "location": "Dallas, Texas, United States of America; Austin, TX, USA; Houston, TX, USA; San Antonio, TX, USA",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549799200737",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:39:52.724225+00:00",
    "date_confidence": "high",
    "description": "Since 1935, Morgan Stanley is known as a global leader in financial services, always evolving and innovating to better serve our clients and our communities in more than 40 countri"
  }
]
```

## NetApp

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.netapp.com/en/search-jobs`
- Pagination: p=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 29
- HTTP requests/cumulative request time: 115 / 33.016s
- Company elapsed time: 50.641s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 86 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 33, 'usable_jd': 33}
- Raw jobs found: 435
- After US/location filtering: 86
- With trustworthy posted_date: 86
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 16.809, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.15, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 5.862, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 8.012, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.432, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.605, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.509, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.794, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.465, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

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
    "fetched_at": "2026-11-10T00:40:02.548140+00:00",
    "date_confidence": "high",
    "description": "Job Summary ONTAP is NetApp’s flagship storage operating system. The ONTAP team drives the product strategy, roadmap, and engineering delivery for ONTAP software and systems. You a"
  },
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "102549034016",
    "title": "Principal Engineer, AI BU",
    "location": "United States; San Jose, California, United States; Morrisville, North Carolina, United States",
    "official_url": "https://careers.netapp.com/en/job/united-states/principal-engineer-ai-bu/27600/102549034016",
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:02.548140+00:00",
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
    "fetched_at": "2026-11-10T00:40:02.548140+00:00",
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
    "fetched_at": "2026-11-10T00:40:02.548140+00:00",
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
    "fetched_at": "2026-11-10T00:40:02.548140+00:00",
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
- HTTP requests/cumulative request time: 9 / 2.485s
- Company elapsed time: 3.481s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 35 / 41
- Detail cache statuses: {'reused': 16, 'reuse_after_error:stale': 19}
- Relevant JD recovery: {'deterministic_skip': 11, 'cache_reused': 35, 'eligible': 16, 'ai_skip': 30, 'usable_jd': 16}
- Raw jobs found: 90
- After US/location filtering: 57
- With trustworthy posted_date: 57
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.524, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.345, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.384, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.3, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.308, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.332, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.689, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.291, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.308, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}

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
    "fetched_at": "2026-11-10T00:40:05.706735+00:00",
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
    "fetched_at": "2026-11-10T00:40:05.706735+00:00",
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
    "fetched_at": "2026-11-10T00:40:05.706735+00:00",
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
    "fetched_at": "2026-11-10T00:40:05.706735+00:00",
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
    "fetched_at": "2026-11-10T00:40:05.706735+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.476s
- Company elapsed time: 1.996s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 349, 'usable_jd': 349}
- Raw jobs found: 820
- After US/location filtering: 656
- With trustworthy posted_date: 656
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
    "fetched_at": "2026-11-10T00:40:09.189243+00:00",
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
    "fetched_at": "2026-11-10T00:40:09.189243+00:00",
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
    "fetched_at": "2026-11-10T00:40:09.189243+00:00",
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
    "fetched_at": "2026-11-10T00:40:09.189243+00:00",
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
    "fetched_at": "2026-11-10T00:40:09.189243+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.307s
- Company elapsed time: 0.586s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 2 / 2
- Detail cache statuses: {'reuse_after_error:stale': 2}
- Relevant JD recovery: {'eligible': 182, 'cache_reused': 2, 'ai_skip': 2, 'usable_jd': 182}
- Raw jobs found: 304
- After US/location filtering: 239
- With trustworthy posted_date: 239
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
    "fetched_at": "2026-11-10T00:40:11.188942+00:00",
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
    "fetched_at": "2026-11-10T00:40:11.188942+00:00",
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
    "fetched_at": "2026-11-10T00:40:11.188942+00:00",
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
    "fetched_at": "2026-11-10T00:40:11.188942+00:00",
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
    "fetched_at": "2026-11-10T00:40:11.188942+00:00",
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
- HTTP requests/cumulative request time: 81 / 12.379s
- Company elapsed time: 23.773s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 60 / 0 / 0
- Detail cache statuses: {'fetched:new': 59, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 179
- After US/location filtering: 60
- With trustworthy posted_date: 60
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 9.425, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.577, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 1.326, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 2.933, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 2.04, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.039, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.375, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 0.528, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.26, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139003",
    "title": "Senior Data Scientist",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923336362",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:11.776260+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139000",
    "title": "Software Engineer",
    "location": "Scottsdale, Arizona, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923336364",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:11.776260+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138526",
    "title": "Sr Software Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923300658",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:11.776260+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138527",
    "title": "Staff Data Scientist",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922946085",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:11.776260+00:00",
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
    "fetched_at": "2026-11-10T00:40:11.776260+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.179s
- Company elapsed time: 0.764s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 154
- After US/location filtering: 134
- With trustworthy posted_date: 134
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:40:29.651112+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:40:29.651112+00:00",
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
    "fetched_at": "2026-11-10T00:40:29.651112+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:40:29.651112+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:40:29.651112+00:00",
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
- Pages/requests fetched: 13
- HTTP requests/cumulative request time: 51 / 18.078s
- Company elapsed time: 23.775s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 37 / 0 / 0
- Detail cache statuses: {'fetched:new': 34, 'fetched:missing_detail': 2, 'fetched:stale': 1}
- Relevant JD recovery: {'eligible': 16, 'usable_jd': 16}
- Raw jobs found: 91
- After US/location filtering: 37
- With trustworthy posted_date: 37
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.14, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 16, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.37, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.31, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 9.319, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 0.4, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.386, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.453, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.577, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 2.305, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 21}

Sample normalized records:

```json
[
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-057956",
    "title": "Senior Software Engineer",
    "location": "Lowell",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Lowell/Senior-Software-Engineer_R-057956-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:30.416681+00:00",
    "date_confidence": "high",
    "description": "The Red Hat Identity Management (IdM) Engineering team seeks a Senior Software Engineer who will join us in Lowell , MA to help us deliver on the next generation of Public Key Infr"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-056868",
    "title": "Senior Software Engineer",
    "location": "Raleigh",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Raleigh/Senior-Software-Engineer_R-056868-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:30.416681+00:00",
    "date_confidence": "high",
    "description": "The Red Hat Identity Management (IdM) Engineering team seeks a Senior Software Engineer to help us deliver on the next generation of Public Key Infrastructure (PKI) product functio"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-057957",
    "title": "Software Engineer",
    "location": "Lowell; Raleigh",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Lowell/Software-Engineer_R-057957-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:30.416681+00:00",
    "date_confidence": "high",
    "description": "The Red Hat Identity Management (IdM) Engineering team seeks a Software Engineer to help us deliver on the next generation of Public Key Infrastructure (PKI) product functionalitie"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-060399",
    "title": "AI Architect - Top Secret Clearance (TS/SCI CI Poly) required",
    "location": "Remote US VA",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Remote-US-VA/AI-Architect---Top-Secret-Clearance--TS-SCI-CI-Poly--required_R-060399-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:30.416681+00:00",
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
    "fetched_at": "2026-11-10T00:40:30.416681+00:00",
    "date_confidence": "high",
    "description": "*Telecommuting permitted: work may be performed within normal commuting distance from the Red Hat, LLC office in Boston, MA. Lead the design and implementation of high-performance "
  }
]
```

## Roku

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roku/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.159s
- Company elapsed time: 0.557s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 93
- After US/location filtering: 78
- With trustworthy posted_date: 78
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:40:33.257115+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:40:33.257115+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:40:33.257115+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:40:33.257115+00:00",
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
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:40:33.257115+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.174s
- Company elapsed time: 1.029s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 202
- After US/location filtering: 184
- With trustworthy posted_date: 184
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5410307008",
    "title": "Account Executive Manager",
    "location": "Tokyo, Japan; JP - TO - Minato",
    "official_url": "http://block.xyz/careers/jobs/5410307008?gh_jid=5410307008",
    "posted_date": "2026-11-09",
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-10T00:40:33.815194+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>The Role</strong></h2> <p>As a Sales Manager, you'll lead a team of Account Executives and own one of our most critical growth levers in-market: developing talent that "
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5108007008",
    "title": "Applied Research Intern, Proactive Intelligence & Customer World Models (PhD / Graduate Co-op)",
    "location": "Bay Area, CA, United States of America; CA - ON - Toronto - Remote",
    "official_url": "http://block.xyz/careers/jobs/5108007008?gh_jid=5108007008",
    "posted_date": "2026-06-09",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-10T00:40:33.815194+00:00",
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
    "fetched_at": "2026-11-10T00:40:33.815194+00:00",
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
    "fetched_at": "2026-11-10T00:40:33.815194+00:00",
    "date_confidence": "high",
    "description": "<h3><strong>Overview&nbsp;</strong></h3> <p>The Global Seller Onboarding team works directly with sellers and internal teams to ensure they are able to take full advantage of Squar"
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
    "fetched_at": "2026-11-10T00:40:33.815194+00:00",
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
- HTTP requests/cumulative request time: 59 / 66.869s
- Company elapsed time: 76.428s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 42 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 42}
- Relevant JD recovery: {'eligible': 37, 'usable_jd': 37}
- Raw jobs found: 117
- After US/location filtering: 42
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 18.049, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 12.641, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 2.397, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 6.27, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 21.103, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.519, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.119, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.058, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 7.272, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 34, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 34}

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
    "fetched_at": "2026-11-10T00:40:34.845004+00:00",
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
    "fetched_at": "2026-11-10T00:40:34.845004+00:00",
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
    "fetched_at": "2026-11-10T00:40:34.845004+00:00",
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
    "fetched_at": "2026-11-10T00:40:34.845004+00:00",
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
    "fetched_at": "2026-11-10T00:40:34.845004+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.165s
- Company elapsed time: 1.033s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 53, 'usable_jd': 53}
- Raw jobs found: 343
- After US/location filtering: 274
- With trustworthy posted_date: 274
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:40:35.550844+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:40:35.550844+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:40:35.550844+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:40:35.550844+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:40:35.550844+00:00",
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
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 142 / 51.286s
- Company elapsed time: 70.646s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 120 / 0 / 0
- Detail cache statuses: {'fetched:new': 120}
- Relevant JD recovery: {'eligible': 24, 'usable_jd': 24}
- Raw jobs found: 358
- After US/location filtering: 120
- With trustworthy posted_date: 120
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 26.795, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.044, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 6.262, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 9.965, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.565, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.699, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.495, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.916, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 4.231, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF090087W",
    "title": "Staff SW Engineer - .NET AI Engineer",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Staff-SW-Engineer---NET-AI-Engineer_REF090087W",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:36.585134+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF084844W",
    "title": "Sr. SW Engineer",
    "location": "US - Bellevue, WA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Bellevue-WA/Sr-SW-Engineer_REF084844W-2",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:36.585134+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF089194W",
    "title": "Chief Software Engineer, Database Architecture",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Chief-SW-Engineer_REF089194W",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:36.585134+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF089844W",
    "title": "Staff SW Engineer - Front-End / UI",
    "location": "US - Bellevue, WA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Bellevue-WA/Staff-SW-Engineer---Front-End---UI_REF089844W",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:36.585134+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF089618W",
    "title": "Associate Data Engineer",
    "location": "US - Foster City, CA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Associate-Data-Engineer_REF089618W",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:36.585134+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.338s
- Company elapsed time: 0.349s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 11
- After US/location filtering: 9
- With trustworthy posted_date: 9
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
    "fetched_at": "2026-11-10T00:40:53.189801+00:00",
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
    "fetched_at": "2026-11-10T00:40:53.189801+00:00",
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
    "fetched_at": "2026-11-10T00:40:53.189801+00:00",
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
    "fetched_at": "2026-11-10T00:40:53.189801+00:00",
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
    "fetched_at": "2026-11-10T00:40:53.189801+00:00",
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
- Pages/requests fetched: 25
- HTTP requests/cumulative request time: 150 / 102.367s
- Company elapsed time: 123.524s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 124 / 0 / 0
- Detail cache statuses: {'fetched:new': 119, 'fetched:changed': 1, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 447
- After US/location filtering: 124
- With trustworthy posted_date: 124
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 47.772, "first_pass_survivors": 77, "group": "official", "jds_resolved": 77, "original_postings_resolved": 77, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 77, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 3.946, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 2.45, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 16.903, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.041, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.334, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.508, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.751, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 10.053, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 80}

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
    "fetched_at": "2026-11-10T00:40:53.540209+00:00",
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
    "fetched_at": "2026-11-10T00:40:53.540209+00:00",
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
    "fetched_at": "2026-11-10T00:40:53.540209+00:00",
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
    "fetched_at": "2026-11-10T00:40:53.540209+00:00",
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
    "fetched_at": "2026-11-10T00:40:53.540209+00:00",
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
- HTTP requests/cumulative request time: 67 / 25.679s
- Company elapsed time: 34.336s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 51 / 0 / 0
- Detail cache statuses: {'fetched:new': 51}
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 219
- After US/location filtering: 51
- With trustworthy posted_date: 51
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 22.486, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.686, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.688, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 1.022, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 3.654, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 2.475, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 50, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 50}
- Query diagnostic: {"elapsed_seconds": 0.682, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.687, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.889, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}

Sample normalized records:

```json
[
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P747954",
    "title": "Principal Machine Learning Engineer, Agentic AI",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Principal-Machine-Learning-Engineer--Agentic-AI_P747954",
    "posted_date": "2026-10-20",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:54.192687+00:00",
    "date_confidence": "high",
    "description": "About the team The Agentic AI team at Zillow is at the forefront of transforming the real estate industry by helping millions of people use AI assistants to find their next home. W"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751267",
    "title": "Senior AI-Native Product Engineer, Mobile",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Senior-AI-Native-Product-Engineer--Mobile_P751267-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:54.192687+00:00",
    "date_confidence": "high",
    "description": "About the team The Mercury Mobile team builds Zillow Instant Messaging (ZIM) — the conversation layer where millions of movers participate in a multiplayer, integrated experience t"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751408",
    "title": "Director, Marketing AI & Automation",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Director--Marketing-AI---Automation_P751408-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:40:54.192687+00:00",
    "date_confidence": "high",
    "description": "About the team Zillow Group is seeking a Director, Marketing AI & Automation to lead a new team within Marketing, Technology & Operations. This role will be accountable for deliver"
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
    "fetched_at": "2026-11-10T00:40:54.192687+00:00",
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
    "fetched_at": "2026-11-10T00:40:54.192687+00:00",
    "date_confidence": "high",
    "description": "About the team The Product AI team is building the shared intelligence, capabilities, and foundation that let every Zillow experience become truly agentic, for the people searching"
  }
]
```

## Zscaler

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/zscaler/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.280s
- Company elapsed time: 1.188s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 15, 'usable_jd': 15}
- Raw jobs found: 376
- After US/location filtering: 230
- With trustworthy posted_date: 230
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
    "fetched_at": "2026-11-10T00:41:23.087585+00:00",
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
    "fetched_at": "2026-11-10T00:41:23.087585+00:00",
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
    "fetched_at": "2026-11-10T00:41:23.087585+00:00",
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
    "fetched_at": "2026-11-10T00:41:23.087585+00:00",
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
    "fetched_at": "2026-11-10T00:41:23.087585+00:00",
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
- HTTP requests/cumulative request time: 13 / 5.684s
- Company elapsed time: 6.057s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 3 / 0 / 0
- Detail cache statuses: {'fetched:new': 3}
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 13
- After US/location filtering: 3
- With trustworthy posted_date: 3
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.991, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.405, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.416, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.435, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.441, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.417, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.592, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.412, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.413, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}

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
    "fetched_at": "2026-11-10T00:41:24.277186+00:00",
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
    "fetched_at": "2026-11-10T00:41:24.277186+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity: Chewy is seeking Senior Software Engineer, Level III in Boston, MA or Minneapolis MN. Chewy is growing! We’re looking for a Senior Backend Softwar"
  },
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R31317",
    "title": "IAM Engineer III, Identity & Access Management",
    "location": "Plantation, FL; USA - MA - Boston - BOS1; Minneapolis, MN; Bellevue, WA",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/Plantation-FL/IAM-Engineer-III--Identity---Access-Management_R31317",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:24.277186+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity Chewy's IAM team keeps the right people, services, and AI agents connected to the right access, from someone's first day to their last. As an IAM E"
  }
]
```

## CVS Health

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 23
- HTTP requests/cumulative request time: 150 / 88.796s
- Company elapsed time: 109.337s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 126 / 0 / 0
- Detail cache statuses: {'fetched:new': 125, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 14, 'usable_jd': 14}
- Raw jobs found: 389
- After US/location filtering: 126
- With trustworthy posted_date: 126
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 58.207, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.211, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 26, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 6.143, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 12.193, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.221, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.988, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.708, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 0.317, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 4.703, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1092993",
    "title": "Senior Data Scientist – Payment Accuracy",
    "location": "NY - New York",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/NY---New-York/Senior-Data-Scientist---Payment-Accuracy_R1092993-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:28.530194+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1045908",
    "title": "Senior Data Engineer - MongoDB and PostgreSQL",
    "location": "NY - Work from hom; Work At Home-South Carolina; Work At Home-Georgia; Work At Home-South Dakota; Work At Home-Minnesota",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/NY---Work-from-hom/Senior-Data-Engineer_R1045908-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:28.530194+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1023505",
    "title": "Sr Manager - Project Program Management",
    "location": "Work At Home-Illinois",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/Work-At-Home-Illinois/Sr-Manager---Project-Program-Management_R1023505",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:28.530194+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1095147",
    "title": "Senior Software Development Engineer",
    "location": "TX - Work from home; MS - Work from home; MT - Work from home; NC - Work from home; LA - Work from home; MD - Work from home; ME - Work from home; MN - Work from home; NE - Work from home; MO - Work from home; ND - Work from home; NY - Work from hom; NJ - Work from home; NM - Work from home; NV - Work from home; OH - Work from hom; SC - Work from home; RI - Work from home; SD - Work from home; VT - Work from home; TN - Work from home; VA - Work from home; WA - Work from home; UT - Work from home; WI - Work from home; WV - Work from home; OR - Work from home; WY - Work from home; OK - Work from home; PA - Work from home; CO - Work from home; AL - Work from home; AZ - Work from home; CA - Work from home; CT - Work from home; DC - Work from home; FL - Work from home; IA - Work from home; AR - Work from home; ID - Work from home; IL - Work from home; KS - Work from home; DE - Work from home; GA - Work from home; IN - Work from home; KY - Work from home; MI - Work from home; MA - Work from home; NH - Work from home",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/TX---Work-from-home/Senior-Software-Development-Engineer_R1095147",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:28.530194+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1085251",
    "title": "Staff Software Development Engineer",
    "location": "MI - Work from home",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/MI---Work-from-home/Staff-Software-Development-Engineer_R1085251",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:28.530194+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.106s
- Company elapsed time: 0.283s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 61
- After US/location filtering: 52
- With trustworthy posted_date: 52
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
    "fetched_at": "2026-11-10T00:41:30.335098+00:00",
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
    "fetched_at": "2026-11-10T00:41:30.335098+00:00",
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
    "fetched_at": "2026-11-10T00:41:30.335098+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8928712002",
    "title": "AI Research Intern (PhD)",
    "location": "New York, NY; Pittsburgh, PA; New York, New York, United States; Pittsburgh, Pennsylvania, United States",
    "official_url": "https://careers.duolingo.com/jobs/8928712002?gh_jid=8928712002",
    "posted_date": "2026-11-06",
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:41:30.335098+00:00",
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
    "fetched_at": "2026-11-10T00:41:30.335098+00:00",
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
- HTTP requests/cumulative request time: 22 / 16.373s
- Company elapsed time: 24.503s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 5 / 67
- Detail cache statuses: {'reused': 5}
- Relevant JD recovery: {'deterministic_skip': 41, 'cache_reused': 5, 'eligible': 5, 'ai_skip': 26, 'usable_jd': 5}
- Raw jobs found: 328
- After US/location filtering: 72
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.212, "first_pass_survivors": 41, "group": "official", "jds_resolved": 0, "original_postings_resolved": 41, "page_budget": 2, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 2.57, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 2, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 39, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 1.292, "first_pass_survivors": 19, "group": "official", "jds_resolved": 0, "original_postings_resolved": 19, "page_budget": 2, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 19, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 0.957, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 2, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 6.869, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 2.376, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 2.252, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 2.349, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 2.625, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164105",
    "title": "Staff Software Engineer, AI Infrastructure",
    "location": "Redwood City, California, United States",
    "official_url": "https://careers.equinix.com/jobs/staff-software-engineer-ai-infrastructure-redwood-city-california-united-states",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:30.618824+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164103",
    "title": "Principal Software Engineer, AI Infrastructure",
    "location": "Burnaby, British Columbia, Canada; Toronto, Ontario, Canada; Montreal, Quebec, Canada; Redwood City, California, United States; Denver, Colorado, United States; Tampa, Florida, United States; New York, United States; Dallas, Texas, United States; Frisco, Texas, United States; Burnaby, British Columbia, Canada; Toronto, Ontario, Canada; Montreal, Quebec, Canada",
    "official_url": "https://careers.equinix.com/jobs/principal-software-engineer-ai-infrastructure-redwood-city-california-united-states-dallas-texas-denver-colorado-frisco-montreal-quebec-canada-new-york-tampa-florida-toronto-ontario-burnaby-b",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:30.618824+00:00",
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
    "fetched_at": "2026-11-10T00:41:30.618824+00:00",
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
    "fetched_at": "2026-11-10T00:41:30.618824+00:00",
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
    "fetched_at": "2026-11-10T00:41:30.618824+00:00",
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
- HTTP requests/cumulative request time: 16 / 8.752s
- Company elapsed time: 10.134s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: {'fetched:new': 1}
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 125
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.0, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.528, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.639, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.424, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.381, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.24, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.58, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.469, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.208, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

Sample normalized records:

```json
[
  {
    "company": "F5",
    "source": "f5_official_careers",
    "job_id": "RP1039338",
    "title": "Account Executive US Federal Civilian Agencies",
    "location": "Field-DC; Field-MD",
    "official_url": "https://ffive.wd5.myworkdayjobs.com/f5jobs/job/Field-DC/Account-Executive-US-Federal-Civilian-Agencies_RP1039338",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:47.232555+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.213s
- Company elapsed time: 0.444s
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
    "fetched_at": "2026-11-10T00:41:51.273786+00:00",
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
    "fetched_at": "2026-11-10T00:41:51.273786+00:00",
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
    "fetched_at": "2026-11-10T00:41:51.273786+00:00",
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
    "fetched_at": "2026-11-10T00:41:51.273786+00:00",
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
    "fetched_at": "2026-11-10T00:41:51.273786+00:00",
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
- HTTP requests/cumulative request time: 78 / 48.988s
- Company elapsed time: 59.251s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 58 / 0 / 0
- Detail cache statuses: {'fetched:new': 57, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 210
- After US/location filtering: 58
- With trustworthy posted_date: 58
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 19.225, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 4.053, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.827, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 11.763, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 33, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 13.823, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 54, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 3.12, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 47, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 47}
- Query diagnostic: {"elapsed_seconds": 0.918, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.862, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 3.648, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 38}

Sample normalized records:

```json
[
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-569594",
    "title": "Principal AI Engineer",
    "location": "BOSTON, MA",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/BOSTON-MA/Principal-Enigneer_R-569594",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:51.719590+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Principal AI Engineer to join the CCIBT Gen AI team, which is responsible for building AI frameworks, intelligent agents, and technology p"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-584168",
    "title": "Lead AI Engineer",
    "location": "BOSTON, MA; CHARLOTTE, NC",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/BOSTON-MA/Lead-AI-Engineer_R-584168",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:51.719590+00:00",
    "date_confidence": "high",
    "description": "Wells Fargo is seeking a Lead AI Engineer in Technology as part of Commercial and Corporate & Investment Banking Technology (CCIBT). The primary focus of this group will be to acce"
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
    "fetched_at": "2026-11-10T00:41:51.719590+00:00",
    "date_confidence": "high",
    "description": "About this role: The Equipment & Vendor Finance business enables commercial clients to acquire, lease, and manage capital equipment through flexible financing solutions. Software e"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-580307",
    "title": "Software Engineering Manager",
    "location": "CHARLOTTE, NC; CHICAGO, IL",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Software-Engineering-Manager_R-580307",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:51.719590+00:00",
    "date_confidence": "high",
    "description": "Are you looking for more? Find it here. At Wells Fargo, we believe that a meaningful career is much more than just a job. It’s about finding all the elements that help you thrive, "
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
    "fetched_at": "2026-11-10T00:41:51.719590+00:00",
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
- Pages/requests fetched: 17
- HTTP requests/cumulative request time: 68 / 30.835s
- Company elapsed time: 39.854s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 50 / 0 / 0
- Detail cache statuses: {'fetched:new': 49, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 197
- After US/location filtering: 50
- With trustworthy posted_date: 50
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.862, "first_pass_survivors": 46, "group": "official", "jds_resolved": 46, "original_postings_resolved": 46, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 46, "unique_jobs": 46}
- Query diagnostic: {"elapsed_seconds": 1.241, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.638, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 1.552, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 3.45, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 2.368, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 0.621, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.663, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 2.692, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 21}

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
    "fetched_at": "2026-11-10T00:41:55.122902+00:00",
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
    "fetched_at": "2026-11-10T00:41:55.122902+00:00",
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
    "fetched_at": "2026-11-10T00:41:55.122902+00:00",
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
    "fetched_at": "2026-11-10T00:41:55.122902+00:00",
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
    "fetched_at": "2026-11-10T00:41:55.122902+00:00",
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
- HTTP requests/cumulative request time: 21 / 9.501s
- Company elapsed time: 12.408s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 18 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 45
- After US/location filtering: 18
- With trustworthy posted_date: 18
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 12.408, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "Ansys", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 45}

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
    "fetched_at": "2026-11-10T00:41:57.367773+00:00",
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
    "fetched_at": "2026-11-10T00:41:57.367773+00:00",
    "date_confidence": "high",
    "description": "We Are: At Synopsys, we drive the innovations that shape the way we live and connect. Our technology is central to the Era of Pervasive Intelligence, from self-driving cars to lear"
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
    "fetched_at": "2026-11-10T00:41:57.367773+00:00",
    "date_confidence": "high",
    "description": "We Are: At Synopsys, we drive the innovations that shape the way we live and connect. Our technology is central to the Era of Pervasive Intelligence, from self-driving cars to lear"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "101288479216",
    "title": "Staff Application Engineer- FA&D",
    "location": "United States Off-site",
    "official_url": "https://careers.synopsys.com/job/california/staff-application-engineer-fa-and-d/44408/101288479216",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:57.367773+00:00",
    "date_confidence": "high",
    "description": "**Please note that this role can be flexibly based in the Southern California area.** We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling custo"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "100768196032",
    "title": "Technical Support Engineer, Sr. Engineer",
    "location": "Austin, Texas",
    "official_url": "https://careers.synopsys.com/job/austin/technical-support-engineer-sr-engineer/44408/100768196032",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:41:57.367773+00:00",
    "date_confidence": "high",
    "description": "We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling customers to rapidly innovate AI-powered products. We deliver industry-leading silicon desi"
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
- HTTP requests/cumulative request time: 116 / 54.924s
- Company elapsed time: 69.198s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 99 / 0 / 0
- Detail cache statuses: {'fetched:new': 98, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 85, 'usable_jd': 85}
- Raw jobs found: 166
- After US/location filtering: 99
- With trustworthy posted_date: 99
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 15.303, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 23, "stop_reason": "early_stop", "unique_contribution": 23, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 1.342, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.205, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 4.772, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 26.262, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.554, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 1.095, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.058, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 14.361, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 58}

Sample normalized records:

```json
[
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD229353",
    "title": "Manufacturing Engineer",
    "location": "USA, MI, Coopersville",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-MI-Coopersville/Industrial-Engineer_WD229353",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:09.776677+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD233574",
    "title": "Business Excellence Leader",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Business-Excellence-Leader_WD233574",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:09.776677+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD232571",
    "title": "Automation Technician",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Automation-Technician_WD232571",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:09.776677+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD233588",
    "title": "Business Excellence Leader",
    "location": "USA, SC, Orangeburg",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-SC-Orangeburg/Business-Excellence-Leader_WD233588",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:09.776677+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD233173",
    "title": "Commodity Buyer, Facilities",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Commodity-Buyer--Facilities_WD233173",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:09.776677+00:00",
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
- HTTP requests/cumulative request time: 24 / 14.899s
- Company elapsed time: 16.637s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 14 / 0 / 0
- Detail cache statuses: {'fetched:new': 14}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 46
- After US/location filtering: 14
- With trustworthy posted_date: 14
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.85, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.774, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.781, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 3.858, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.834, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.808, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.798, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.789, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.693, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}

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
    "fetched_at": "2026-11-10T00:42:34.978538+00:00",
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
    "fetched_at": "2026-11-10T00:42:34.978538+00:00",
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
    "fetched_at": "2026-11-10T00:42:34.978538+00:00",
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
    "fetched_at": "2026-11-10T00:42:34.978538+00:00",
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
    "fetched_at": "2026-11-10T00:42:34.978538+00:00",
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
- HTTP requests/cumulative request time: 209 / 76.487s
- Company elapsed time: 104.677s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 186 / 0 / 0
- Detail cache statuses: {'fetched:new': 185, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 43, 'usable_jd': 43}
- Raw jobs found: 412
- After US/location filtering: 186
- With trustworthy posted_date: 186
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.077, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.821, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 40, "stop_reason": "early_stop", "unique_contribution": 22, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 22.664, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.573, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.327, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.029, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.868, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.267, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 7.712, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-109147",
    "title": "Staff NPI Engineer - Johnson and Johnson MedTech, Circulatory Restoration",
    "location": "Santa Clara, California, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Santa-Clara-California-United-States-of-America/Staff-NPI-Engineer---Johnson-and-Johnson-MedTech--Circulatory-Restoration_R-109147-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:50.971765+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-109128",
    "title": "WithMe CRM and Portal Data Lead",
    "location": "Titusville, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Titusville-New-Jersey-United-States-of-America/WithMe-CRM-and-Portal-Data-Lead_R-109128-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:50.971765+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-104149",
    "title": "Environmental, Health & Safety (EHS) Summer Intern",
    "location": "Cincinnati, Ohio, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Cincinnati-Ohio-United-States-of-America/Environmental--Health---Safety--EHS--Summer-Intern_R-104149-1",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:50.971765+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-080485",
    "title": "Data Quality & Automation Specialist (US)",
    "location": "Raritan, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raritan-New-Jersey-United-States-of-America/Senior-Analyst--Data-Quality---Automation--US-_R-080485",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:50.971765+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-106639",
    "title": "Senior Manager, AI Architecture",
    "location": "Raritan, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raritan-New-Jersey-United-States-of-America/Senior-Manager--AI-Architecture_R-106639",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:50.971765+00:00",
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
- HTTP requests/cumulative request time: 24 / 12.932s
- Company elapsed time: 14.661s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 14 / 0 / 0
- Detail cache statuses: {'fetched:new': 14}
- Relevant JD recovery: {'eligible': 2, 'usable_jd': 2}
- Raw jobs found: 59
- After US/location filtering: 14
- With trustworthy posted_date: 14
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 6.781, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.54, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.56, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.414, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 1.81, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.617, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.6, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.597, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.996, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 13}

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
    "fetched_at": "2026-11-10T00:42:51.616794+00:00",
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
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:51.616794+00:00",
    "date_confidence": "high",
    "description": "We're looking for a Senior AI Application Engineer (.NET) to design, build, and scale intelligent enterprise applications. This role is ideal for an experienced C#/.NET software en"
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
    "fetched_at": "2026-11-10T00:42:51.616794+00:00",
    "date_confidence": "high",
    "description": "As a Lead Engineer reporting to the AVP of Software Engineering, you'll play a critical role in shaping the cloud, platform, and reliability engineering foundation that powers Nasd"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026600",
    "title": "Senior Specialist - Software Engineer",
    "location": "USA - Philadelphia - Pennsylvania",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---Philadelphia---Pennsylvania/Senior-Specialist---Software-Engineer_R0026600",
    "posted_date": "2026-08-04",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:51.616794+00:00",
    "date_confidence": "high",
    "description": "As a Sr. Specialist Software Engineer reporting to the VP - Software Engineering, you'll play a critical role in developing and maintaining the technology that powers Nasdaq's Deri"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0024835",
    "title": "Senior Data Scientist",
    "location": "USA - Boston - Massachusetts",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---Boston---Massachusetts/Senior-Data-Scientist_R0024835",
    "posted_date": "2025-12-23",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:51.616794+00:00",
    "date_confidence": "high",
    "description": "When you work at Nasdaq, you’re working for more open and transparent markets so that more people can access opportunities. Connections can be made, jobs can be created, and commun"
  }
]
```

## PointClickCare

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/pointclickcare`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 2 / 2.824s
- Company elapsed time: 2.877s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 1 / 7 / 42
- Detail cache statuses: {'reused': 7}
- Relevant JD recovery: {'deterministic_skip': 36, 'eligible': 11, 'cache_reused': 7, 'ai_skip': 6, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 10}
- Raw jobs found: 76
- After US/location filtering: 70
- With trustworthy posted_date: 70
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
    "fetched_at": "2026-11-10T00:42:57.065665+00:00",
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
    "fetched_at": "2026-11-10T00:42:57.065665+00:00",
    "date_confidence": "high",
    "description": ""
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
    "fetched_at": "2026-11-10T00:42:57.065665+00:00",
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
    "fetched_at": "2026-11-10T00:42:57.065665+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "dd8a5cee-054e-46fe-be82-f246d4dda50e",
    "title": "Accounts Receivable Escalations Analyst",
    "location": "Mississauga, Ontario",
    "official_url": "https://jobs.lever.co/pointclickcare/dd8a5cee-054e-46fe-be82-f246d4dda50e",
    "posted_date": "2026-10-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:57.065665+00:00",
    "date_confidence": "high",
    "description": "Preparation of demand letters, termination letters and final collection notices for Senior Care accounts, QuickMar, Pharmacy and other streams of business as needed. Investigation "
  }
]
```

## Stryker

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://stryker.wd1.myworkdayjobs.com/StrykerCareers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 20
- HTTP requests/cumulative request time: 157 / 72.233s
- Company elapsed time: 92.415s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 136 / 0 / 0
- Detail cache statuses: {'fetched:new': 135, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 48, 'usable_jd': 48}
- Raw jobs found: 231
- After US/location filtering: 136
- With trustworthy posted_date: 136
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 15.582, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 25, "stop_reason": "early_stop", "unique_contribution": 23, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 1.952, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 1.175, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 13.779, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 22.248, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.408, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.628, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.857, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 20.89, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 80}

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
    "fetched_at": "2026-11-10T00:42:57.426543+00:00",
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
    "fetched_at": "2026-11-10T00:42:57.426543+00:00",
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
    "fetched_at": "2026-11-10T00:42:57.426543+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Remote As a Lead Full-Stack Software Engineer, you will go beyond building applications to design, lead, and guide the engineering direction of our internal web s"
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
    "fetched_at": "2026-11-10T00:42:57.426543+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Onsite As an Interaction Designer for Emergency Care, you will collaborate with our existing team of experienced designers in their process to define, design, and"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R572941",
    "title": "Summer 2027 Internship - Software Engineering, Commercial Operations - Texas",
    "location": "Flower Mound, Texas",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Flower-Mound-Texas/Commercial-Operations-Software-Engineering-Intern---Flower-Mound--TX_R572941",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:42:57.426543+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Onsite What You Get Out of the Internship ​​ At Stryker, we believe that developing the next generation of talent is just as important as developing life-changing"
  }
]
```

## TransUnion

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://transunion.wd5.myworkdayjobs.com/TransUnion`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 13
- HTTP requests/cumulative request time: 40 / 13.385s
- Company elapsed time: 17.640s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 26 / 0 / 0
- Detail cache statuses: {'fetched:new': 25, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 117
- After US/location filtering: 26
- With trustworthy posted_date: 26
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.238, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 23, "stop_reason": "early_stop", "unique_contribution": 23, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 0.457, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.817, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 1.146, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.481, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 0.489, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 2.192, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 0.422, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.816, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}

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
    "fetched_at": "2026-11-10T00:43:06.278812+00:00",
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
    "fetched_at": "2026-11-10T00:43:06.278812+00:00",
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
    "fetched_at": "2026-11-10T00:43:06.278812+00:00",
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
    "fetched_at": "2026-11-10T00:43:06.278812+00:00",
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
    "fetched_at": "2026-11-10T00:43:06.278812+00:00",
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
- HTTP requests/cumulative request time: 107 / 40.735s
- Company elapsed time: 55.476s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 83 / 0 / 0
- Detail cache statuses: {'fetched:new': 81, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 44, 'usable_jd': 44}
- Raw jobs found: 310
- After US/location filtering: 83
- With trustworthy posted_date: 83
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 21.631, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 3.118, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 2.549, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 6.363, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 46}
- Query diagnostic: {"elapsed_seconds": 9.334, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 2.909, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.683, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 2.611, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 5.446, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 51, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 51}

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
    "fetched_at": "2026-11-10T00:43:17.868981+00:00",
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
    "fetched_at": "2026-11-10T00:43:17.868981+00:00",
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
    "fetched_at": "2026-11-10T00:43:17.868981+00:00",
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
    "fetched_at": "2026-11-10T00:43:17.868981+00:00",
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
    "fetched_at": "2026-11-10T00:43:17.868981+00:00",
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
- HTTP requests/cumulative request time: 27 / 4.627s
- Company elapsed time: 4.938s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 21 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 46
- After US/location filtering: 21
- With trustworthy posted_date: 21
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.69, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.54, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 1.248, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 1.733, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.38, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.347, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}

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
    "fetched_at": "2026-11-10T00:43:18.976064+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1101085",
    "title": "Associate Director - Responsible AI",
    "location": "Irving, Texas; Colorado Springs, Colorado; Ashburn, Virginia; Cary, North Carolina; Basking Ridge, New Jersey; Miami, Florida; Rolling Meadows, Illinois; Seattle, Washington; Bakersfield, California",
    "official_url": "https://mycareer.verizon.com/jobs/r-1101085/associate-director-responsible-ai/",
    "posted_date": "2026-11-06",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:43:18.976064+00:00",
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
    "fetched_at": "2026-11-10T00:43:18.976064+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1100559",
    "title": "B2B Data Scientist",
    "location": "Basking Ridge, New Jersey; Alpharetta, Georgia; Irving, Texas",
    "official_url": "https://mycareer.verizon.com/jobs/r-1100559/b2b-data-scientist/",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-10T00:43:18.976064+00:00",
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
    "fetched_at": "2026-11-10T00:43:18.976064+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.174s
- Company elapsed time: 0.242s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 31
- After US/location filtering: 18
- With trustworthy posted_date: 18
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:43:23.914927+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:43:23.914927+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:43:23.914927+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:43:23.914927+00:00",
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
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-10T00:43:23.914927+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
