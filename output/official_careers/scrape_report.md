# Official careers scrape report — 2026-11-05_1531

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Runtime metrics

- Wall time: 911.418s
- HTTP requests/cumulative request time: 7104 / 3320.501s
- Listing pages/detail fetched/cache reused/prefilter skipped: 1292 / 5773 / 303 / 885
- Detail cache statuses: {'fetched:changed': 1, 'fetched:missing_detail': 213, 'fetched:new': 5378, 'fetched:stale': 6, 'reuse_after_error:missing_detail': 2, 'reuse_after_error:stale': 40, 'reused': 258}
- Relevant JD coverage: 5329 / 5337; added detail requests 15 / 150; deferred 0

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 13.495s
- Company elapsed time: 28.588s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 122, 'usable_jd': 122}
- Raw jobs found: 797
- After US/location filtering: 255
- With trustworthy posted_date: 255
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.424, "first_pass_survivors": 119, "group": "official", "jds_resolved": 119, "original_postings_resolved": 119, "page_budget": 6, "pages_fetched": 6, "query": "\"Ai Engineer\"", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 119, "unique_jobs": 119}
- Query diagnostic: {"elapsed_seconds": 2.148, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Machine Learning Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.069, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Data Scientist\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 0.28, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Solutions Architect\"", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.272, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Data Engineer\"", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 2.119, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "\"Platform Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.105, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Full Stack Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.813, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "\"Forward Deployed Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.217, "first_pass_survivors": 69, "group": "official", "jds_resolved": 69, "original_postings_resolved": 69, "page_budget": 12, "pages_fetched": 8, "query": "\"Software Engineer\"", "raw_jobs": 160, "stop_reason": "early_stop", "unique_contribution": 69, "unique_jobs": 160}
- Query diagnostic: {"elapsed_seconds": 2.083, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Infrastructure Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.295, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 5, "pages_fetched": 4, "query": "\"Software Engineer III\"", "raw_jobs": 75, "stop_reason": "early_stop", "unique_contribution": 18, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 1.353, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "\"Web Solutions Engineer\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 1.41, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 2, "pages_fetched": 2, "query": "\"DeepMind\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "126255533265953478",
    "title": "Senior Cloud Infrastructure Engineer, Google Public Sector",
    "location": "Reston, VA, USA; Washington D.C., DC, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/126255533265953478-senior-cloud-infrastructure-engineer-google-public-sector",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-05T15:31:18.833904+00:00",
    "date_confidence": "high",
    "description": "Google Cloud's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. We're "
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "144094559670805190",
    "title": "Software Engineer III, AI/ML GenAI",
    "location": "New York, NY, USA; Kirkland, WA, USA; Mountain View, CA, USA; Seattle, WA, USA; San Francisco, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/144094559670805190-software-engineer-iii-ai-ml-genai",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-05T15:31:18.833904+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "78947808530309830",
    "title": "Applied AI Insights Lead, Creator and Consumer Experience Operations, YouTube",
    "location": "New York, NY, USA; San Bruno, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/78947808530309830-applied-ai-insights-lead-creator-and-consumer-experience-operations-youtube",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-05T15:31:18.833904+00:00",
    "date_confidence": "high",
    "description": "The mission for Creator and Consumer Experience Operations (CCXO) at YouTube is to give everyone a voice and show them the world, by removing everything that stands in their way. W"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "113164610386698950",
    "title": "Senior Software Engineer, Machine Learning, Discover Interest Modeling",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/113164610386698950-senior-software-engineer-machine-learning-discover-interest-modeling",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-05T15:31:18.833904+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "117034891316470470",
    "title": "Senior Software Engineer, Agentic Automations, Connect Sales AI, Google Ads",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/117034891316470470-senior-software-engineer-agentic-automations-connect-sales-ai-google-ads",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-05T15:31:18.833904+00:00",
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
- HTTP requests/cumulative request time: 45 / 15.715s
- Company elapsed time: 27.851s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 482, 'usable_jd': 482}
- Raw jobs found: 851
- After US/location filtering: 738
- With trustworthy posted_date: 738
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.731, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 1.627, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 51, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 51}
- Query diagnostic: {"elapsed_seconds": 1.536, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 1.982, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.142, "first_pass_survivors": 55, "group": "official", "jds_resolved": 55, "original_postings_resolved": 55, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 55, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.432, "first_pass_survivors": 46, "group": "official", "jds_resolved": 46, "original_postings_resolved": 46, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 46, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 0.297, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 15, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 1.21, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 37, "stop_reason": "early_stop", "unique_contribution": 37, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 7.036, "first_pass_survivors": 211, "group": "official", "jds_resolved": 211, "original_postings_resolved": 211, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 211, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.538, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.235, "first_pass_survivors": 55, "group": "official", "jds_resolved": 55, "original_postings_resolved": 55, "page_budget": 3, "pages_fetched": 3, "query": "systems development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 55, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.695, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.387, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 2, "pages_fetched": 2, "query": "applied scientist", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 40}

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
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-05T15:31:18.834588+00:00",
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
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-05T15:31:18.834588+00:00",
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
    "fetched_at": "2026-11-05T15:31:18.834588+00:00",
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
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-05T15:31:18.834588+00:00",
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
    "updated_date": "2026-10-28",
    "fetched_at": "2026-11-05T15:31:18.834588+00:00",
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
- HTTP requests/cumulative request time: 42 / 15.719s
- Company elapsed time: 30.710s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 173, 'usable_jd': 173}
- Raw jobs found: 840
- After US/location filtering: 286
- With trustworthy posted_date: 286
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.728, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.17, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.125, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.298, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.112, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.107, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.183, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.143, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.655, "first_pass_survivors": 119, "group": "official", "jds_resolved": 119, "original_postings_resolved": 119, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 119, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.19, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "apps-and-frameworks-SFTWR-AF", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200691489-0157",
    "title": "Design Verification",
    "location": "Austin, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200691489/design-verification",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.834910+00:00",
    "date_confidence": "high",
    "description": "Imagine what you can do here. Apple is a place where extraordinary people gather to do their lives best work. Together we create products and experiences people once couldn't have "
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200691703-0836",
    "title": "System Product Design Engineer",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200691703/system-product-design-engineer",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.834910+00:00",
    "date_confidence": "high",
    "description": "Imagine what you can do here. Apple is a place where extraordinary people gather to do their lives best work. Together we create products and experiences people once couldn't have "
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200691246-0157",
    "title": "Performance and Modeling Engineer",
    "location": "Austin, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200691246/performance-and-modeling-engineer",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.834910+00:00",
    "date_confidence": "high",
    "description": "Imagine what you can do here. Apple is a place where extraordinary people gather to do their lives best work. Together we create products and experiences people once couldn't have "
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200691711-3543",
    "title": "Hardware Development",
    "location": "San Diego, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200691711/hardware-development",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.834910+00:00",
    "date_confidence": "high",
    "description": "Imagine what you can do here. Apple is a place where extraordinary people gather to do their lives best work. Together we create products and experiences people once couldn't have "
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200691779-0836",
    "title": "Design Verification Engineer",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200691779/design-verification-engineer",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.834910+00:00",
    "date_confidence": "high",
    "description": "Imagine what you can do here. Apple is a place where extraordinary people gather to do their lives best work. Together we create products and experiences people once couldn't have "
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 233 / 63.703s
- Company elapsed time: 97.495s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 193 / 0 / 0
- Detail cache statuses: {'fetched:new': 184, 'fetched:missing_detail': 9}
- Relevant JD recovery: {'eligible': 40, 'usable_jd': 40}
- Raw jobs found: 390
- After US/location filtering: 193
- With trustworthy posted_date: 193
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 26.514, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.562, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 10.721, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 10.476, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.207, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.659, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.923, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 11.23, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 22.896, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 120}

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200063394",
    "title": "Software Engineer II",
    "location": "United States, California, Mountain View",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557045509",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.836899+00:00",
    "date_confidence": "high",
    "description": "Overview Security represents the most critical priorities for our customers in a world awash in digital threats, regulatory scrutiny, and estate complexity. Microsoft Security aspi"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200062014",
    "title": "Critical Environment Technician Manager (Mechanical SME)",
    "location": "United States, Wisconsin, Mount Pleasant; United States, Wisconsin, Milwaukee",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557041079",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.836899+00:00",
    "date_confidence": "high",
    "description": "Overview In alignment with our Microsoft values, we are committed to cultivating an inclusive work environment for all employees to positively impact our culture every day and we n"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200058479",
    "title": "Senior Software Engineer - CoreAI",
    "location": "United States, Washington, Redmond; United States, California, Mountain View",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557014905",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.836899+00:00",
    "date_confidence": "high",
    "description": "Overview Do you want to help build and operate the platform that powers serverless computing at global scale? Azure Functions is at the heart of Azure's serverless platform and ena"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200053667",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556988211",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.836899+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft is a company where passionate innovators come to collaborate, envision what can be and take their careers further. This is a world of more possibilities, more in"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200041660",
    "title": "Senior Software Engineer - Fullstack/Frontend",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556915388",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:18.836899+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft is a company where passionate innovators come to collaborate, envision what can be, and take their careers further. This is a world of more possibilities, more i"
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 512 / 242.015s
- Company elapsed time: 309.192s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 479 / 0 / 0
- Detail cache statuses: {'fetched:new': 471, 'fetched:missing_detail': 8}
- Relevant JD recovery: {'eligible': 64, 'usable_jd': 64}
- Raw jobs found: 640
- After US/location filtering: 479
- With trustworthy posted_date: 479
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 60.394, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 46.014, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 27.157, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 28.22, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 21.633, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 30.143, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 24.107, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.101, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 33.423, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 19.475, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}

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
    "fetched_at": "2026-11-05T15:31:18.838070+00:00",
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
    "fetched_at": "2026-11-05T15:31:18.838070+00:00",
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
    "fetched_at": "2026-11-05T15:31:18.838070+00:00",
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
    "fetched_at": "2026-11-05T15:31:18.838070+00:00",
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
    "fetched_at": "2026-11-05T15:31:18.838070+00:00",
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
- HTTP requests/cumulative request time: 214 / 81.377s
- Company elapsed time: 110.474s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 185 / 0 / 0
- Detail cache statuses: {'fetched:new': 181, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 47, 'usable_jd': 47}
- Raw jobs found: 456
- After US/location filtering: 185
- With trustworthy posted_date: 185
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 31.612, "first_pass_survivors": 73, "group": "official", "jds_resolved": 73, "original_postings_resolved": 73, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 73, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 9.459, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 3.36, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 31.201, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.16, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.163, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.448, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 34, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 34}
- Query diagnostic: {"elapsed_seconds": 7.608, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 9.41, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.478, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "software engineering mts", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 14}

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR366831",
    "title": "Software Engineering LMTS",
    "location": "California - San Francisco; California - Palo Alto; Washington - Seattle; Washington - Bellevue",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Software-Engineering-LMTS_JR366831",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:46.686322+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR317953",
    "title": "Solution Engineer (Pre-Sales) - All Levels",
    "location": "New York - New York; Illinois - Chicago; Massachusetts - Boston; Washington - Seattle; Texas - Dallas; California - Irvine; Colorado - Denver; Michigan - Remote; Georgia - Atlanta; California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/New-York---New-York/Solution-Engineer--Pre-Sales----All-Levels_JR317953",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:46.686322+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR356908",
    "title": "Senior Incident Responder, Global CSIRT",
    "location": "Virginia - Mclean; Washington - Bellevue",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Virginia---Mclean/Senior-Incident-Responder--Global-CSIRT_JR356908-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:46.686322+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Enterprise Technolo"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR343322",
    "title": "Real-time Data Platform Software Engineer- Senior/Lead",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Flink-Lead-Software-Engineer_JR343322",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:46.686322+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR366844",
    "title": "Senior Software Engineer (LMTS), Backend – Enterprise Productivity",
    "location": "California - San Francisco; Washington - Seattle; New York - New York",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Senior-Software-Engineer--LMTS---Backend---Enterprise-Productivity_JR366844",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:46.686322+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  }
]
```

## Adobe

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://adobe.wd5.myworkdayjobs.com/external_experienced`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 28
- HTTP requests/cumulative request time: 131 / 64.922s
- Company elapsed time: 83.574s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 102 / 0 / 0
- Detail cache statuses: {'fetched:new': 100, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 31, 'usable_jd': 31}
- Raw jobs found: 430
- After US/location filtering: 102
- With trustworthy posted_date: 102
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 48.951, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 4.169, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 2.351, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 4.457, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 2.78, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.571, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.144, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 5.262, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 8.304, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 61, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 61}
- Query diagnostic: {"elapsed_seconds": 2.771, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 58}

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
    "fetched_at": "2026-11-05T15:31:47.422478+00:00",
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
    "fetched_at": "2026-11-05T15:31:47.422478+00:00",
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
    "fetched_at": "2026-11-05T15:31:47.422478+00:00",
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
    "fetched_at": "2026-11-05T15:31:47.422478+00:00",
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
    "fetched_at": "2026-11-05T15:31:47.422478+00:00",
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
- HTTP requests/cumulative request time: 17 / 11.185s
- Company elapsed time: 12.134s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 5 / 244 / 628
- Detail cache statuses: {'reused': 221, 'fetched:stale': 5, 'reuse_after_error:stale': 18}
- Relevant JD recovery: {'cache_reused': 244, 'eligible': 226, 'deterministic_skip': 439, 'ai_skip': 189, 'detail_requests': 5, 'detail_success': 5, 'budget_deferred': 0, 'usable_jd': 226}
- Raw jobs found: 2892
- After US/location filtering: 854
- With trustworthy posted_date: 23
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.004, "first_pass_survivors": 535, "group": "official", "jds_resolved": 0, "original_postings_resolved": 535, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 662, "stop_reason": "page_budget", "unique_contribution": 535, "unique_jobs": 662}
- Query diagnostic: {"elapsed_seconds": 0.68, "first_pass_survivors": 29, "group": "official", "jds_resolved": 0, "original_postings_resolved": 29, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 167, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 167}
- Query diagnostic: {"elapsed_seconds": 0.867, "first_pass_survivors": 55, "group": "official", "jds_resolved": 0, "original_postings_resolved": 55, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 184, "stop_reason": "page_budget", "unique_contribution": 55, "unique_jobs": 184}
- Query diagnostic: {"elapsed_seconds": 0.911, "first_pass_survivors": 31, "group": "official", "jds_resolved": 0, "original_postings_resolved": 31, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 0.912, "first_pass_survivors": 161, "group": "official", "jds_resolved": 0, "original_postings_resolved": 161, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 736, "stop_reason": "page_budget", "unique_contribution": 161, "unique_jobs": 736}
- Query diagnostic: {"elapsed_seconds": 0.768, "first_pass_survivors": 29, "group": "official", "jds_resolved": 0, "original_postings_resolved": 29, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 435, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 435}
- Query diagnostic: {"elapsed_seconds": 0.772, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 54, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 0.874, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.625, "first_pass_survivors": 12, "group": "official", "jds_resolved": 0, "original_postings_resolved": 12, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 433, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 433}

Sample normalized records:

```json
[
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "704019139159184",
    "title": "Software Engineer (Leadership) - Infrastructure",
    "location": "Sunnyvale, CA; Bellevue, WA; Redmond, WA; Menlo Park, CA; Seattle, WA; Burlingame, CA; New York, NY; Remote, US",
    "official_url": "https://www.metacareers.com/jobs/704019139159184",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:49.545870+00:00",
    "date_confidence": "unknown",
    "description": "Meta is seeking talented principal engineers to join our teams in building cutting-edge products that connect billions of people around the world. As a member of our team, you will"
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1038128235640215",
    "title": "Lead Counsel, Infrastructure and Telecom Legal",
    "location": "Los Angeles, CA; Denver, CO; Menlo Park, CA; Washington, DC; New York, NY",
    "official_url": "https://www.metacareers.com/jobs/1038128235640215",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:49.545870+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1367959535215289",
    "title": "Systems Analyst, Access and Compromise Integrity",
    "location": "New York, NY",
    "official_url": "https://www.metacareers.com/jobs/1367959535215289",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:49.545870+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1023800746932113",
    "title": "Product Configuration Analyst",
    "location": "Sunnyvale, CA",
    "official_url": "https://www.metacareers.com/jobs/1023800746932113",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:49.545870+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2111078129773109",
    "title": "Research Scientist Intern, Foundation Model Optimization (PhD)",
    "location": "Bellevue, WA",
    "official_url": "https://www.metacareers.com/jobs/2111078129773109",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:49.545870+00:00",
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
- HTTP requests/cumulative request time: 26 / 21.079s
- Company elapsed time: 25.349s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 428, 'usable_jd': 428}
- Raw jobs found: 1237
- After US/location filtering: 714
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.145, "first_pass_survivors": 199, "group": "official", "jds_resolved": 199, "original_postings_resolved": 199, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 199, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 3.464, "first_pass_survivors": 131, "group": "official", "jds_resolved": 131, "original_postings_resolved": 131, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 131, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.878, "first_pass_survivors": 111, "group": "official", "jds_resolved": 111, "original_postings_resolved": 111, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 111, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.363, "first_pass_survivors": 77, "group": "official", "jds_resolved": 77, "original_postings_resolved": 77, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 77, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.697, "first_pass_survivors": 65, "group": "official", "jds_resolved": 65, "original_postings_resolved": 65, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 65, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.556, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.138, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 86, "stop_reason": "early_stop", "unique_contribution": 24, "unique_jobs": 86}
- Query diagnostic: {"elapsed_seconds": 0.52, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 3.587, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 200}

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
    "fetched_at": "2026-11-05T15:31:57.759819+00:00",
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
    "fetched_at": "2026-11-05T15:31:57.759819+00:00",
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
    "fetched_at": "2026-11-05T15:31:57.759819+00:00",
    "date_confidence": "unknown",
    "description": "The AIGE (AI-Generated Effects) team is building AI-native creative tools that enable TikTok creators to turn natural-language and multimodal ideas into high-quality, interactive e"
  },
  {
    "company": "TikTok",
    "source": "tiktok_official_careers",
    "job_id": "7669702699627661573",
    "title": "Machine Learning Engineer Graduate (Commercial AI-CRM and Transaction) - 2027 Start",
    "location": "San Jose, California, United States of America",
    "official_url": "https://lifeattiktok.com/search/7669702699627661573",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:31:57.759819+00:00",
    "date_confidence": "unknown",
    "description": "The Commercial AI-CRM and Transaction team focuses on TikTok advertiser growth algorithms. Leveraging deep learning and large language model technologies, the team builds an algori"
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
    "fetched_at": "2026-11-05T15:31:57.759819+00:00",
    "date_confidence": "unknown",
    "description": "The Commercial AI-CRM and Transaction team focuses on TikTok advertiser growth algorithms. Leveraging deep learning and large language model technologies, the team builds an algori"
  }
]
```

## Uber

- Status: ok
- Scraping method: HTTP GET Oracle HCM recruitingCEJobRequisitions on iaziqy.fa.ocs.oraclecloud.com (offset pagination) + recruitingCEJobRequisitionDetails
- Search URL/API: `https://jobs.uber.com/en/jobs/?search=software%20engineer&page=1&pagesize=10`
- Pagination: HCM finder offset=(page-1)*limit ; limit=20; stop on empty/repeat or TotalJobsCount (do not stop at pages 1–7)
- Pages/requests fetched: 28
- HTTP requests/cumulative request time: 212 / 58.412s
- Company elapsed time: 87.758s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 184 / 0 / 0
- Detail cache statuses: {'fetched:new': 184}
- Relevant JD recovery: {'eligible': 33, 'usable_jd': 33}
- Raw jobs found: 548
- After US/location filtering: 184
- With trustworthy posted_date: 184
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.369, "first_pass_survivors": 70, "group": "official", "jds_resolved": 70, "original_postings_resolved": 70, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 70, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 12.076, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.619, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 37, "stop_reason": "early_stop", "unique_contribution": 15, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 11.08, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 51, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 51}
- Query diagnostic: {"elapsed_seconds": 5.152, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.484, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.265, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.721, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.99, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 80}

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
    "fetched_at": "2026-11-05T15:32:23.109830+00:00",
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
    "fetched_at": "2026-11-05T15:32:23.109830+00:00",
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
    "fetched_at": "2026-11-05T15:32:23.109830+00:00",
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
    "fetched_at": "2026-11-05T15:32:23.109830+00:00",
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
    "fetched_at": "2026-11-05T15:32:23.109830+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.804s
- Company elapsed time: 2.734s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 109, 'usable_jd': 109}
- Raw jobs found: 440
- After US/location filtering: 439
- With trustworthy posted_date: 439
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
    "fetched_at": "2026-11-05T15:32:56.332767+00:00",
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
    "fetched_at": "2026-11-05T15:32:56.332767+00:00",
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
    "fetched_at": "2026-11-05T15:32:56.332767+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8353606",
    "title": "Account Executive, CPG",
    "location": "New York, NY; Los Angeles, CA; Atlanta, GA; Chicago, IL; San Francisco, CA; New York",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8353606",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-05T15:32:56.332767+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7490373",
    "title": "Account Executive - CPG Ads",
    "location": "San Francisco, CA; New York, NY; Los Angeles, CA; Atlanta, GA; Chicago, IL; New York",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7490373",
    "posted_date": "2026-01-05",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-05T15:32:56.332767+00:00",
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
- HTTP requests/cumulative request time: 123 / 60.843s
- Company elapsed time: 77.752s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 99 / 0 / 0
- Detail cache statuses: {'fetched:new': 99}
- Relevant JD recovery: {'eligible': 15, 'usable_jd': 15}
- Raw jobs found: 374
- After US/location filtering: 99
- With trustworthy posted_date: 99
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 34.65, "first_pass_survivors": 64, "group": "official", "jds_resolved": 64, "original_postings_resolved": 64, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 64, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 11.426, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 37, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 0.708, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 7.006, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 7.988, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.599, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.145, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 0.8, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 6.701, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 80}

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
    "fetched_at": "2026-11-05T15:32:59.067878+00:00",
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
    "fetched_at": "2026-11-05T15:32:59.067878+00:00",
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
    "fetched_at": "2026-11-05T15:32:59.067878+00:00",
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
    "fetched_at": "2026-11-05T15:32:59.067878+00:00",
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
    "fetched_at": "2026-11-05T15:32:59.067878+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.145s
- Company elapsed time: 0.623s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 167
- After US/location filtering: 129
- With trustworthy posted_date: 129
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
    "fetched_at": "2026-11-05T15:33:10.997862+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8267923",
    "title": "Brand Marketing Manager",
    "location": "San Francisco, CA, US; Remote, US; San Francisco, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8267923",
    "posted_date": "2026-10-21",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-05T15:33:10.997862+00:00",
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
    "fetched_at": "2026-11-05T15:33:10.997862+00:00",
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
    "fetched_at": "2026-11-05T15:33:10.997862+00:00",
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
    "fetched_at": "2026-11-05T15:33:10.997862+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.229s
- Company elapsed time: 0.710s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 44, 'usable_jd': 44}
- Raw jobs found: 372
- After US/location filtering: 268
- With trustworthy posted_date: 268
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
    "fetched_at": "2026-11-05T15:33:11.622439+00:00",
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
    "fetched_at": "2026-11-05T15:33:11.622439+00:00",
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
    "fetched_at": "2026-11-05T15:33:11.622439+00:00",
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
    "fetched_at": "2026-11-05T15:33:11.622439+00:00",
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
    "fetched_at": "2026-11-05T15:33:11.622439+00:00",
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
- HTTP requests/cumulative request time: 438 / 271.678s
- Company elapsed time: 326.709s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 416 / 0 / 0
- Detail cache statuses: {'fetched:new': 416}
- Relevant JD recovery: {'eligible': 56, 'usable_jd': 56}
- Raw jobs found: 1928
- After US/location filtering: 416
- With trustworthy posted_date: 416
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 258.609, "first_pass_survivors": 331, "group": "official", "jds_resolved": 331, "original_postings_resolved": 331, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 331, "stop_reason": "page_budget", "unique_contribution": 331, "unique_jobs": 331}
- Query diagnostic: {"elapsed_seconds": 1.066, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 109, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 109}
- Query diagnostic: {"elapsed_seconds": 9.619, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 185, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 185}
- Query diagnostic: {"elapsed_seconds": 42.826, "first_pass_survivors": 64, "group": "official", "jds_resolved": 64, "original_postings_resolved": 64, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 263, "stop_reason": "page_budget", "unique_contribution": 64, "unique_jobs": 263}
- Query diagnostic: {"elapsed_seconds": 2.213, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 5.672, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 1.206, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 77, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 77}
- Query diagnostic: {"elapsed_seconds": 0.458, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 67, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 67}
- Query diagnostic: {"elapsed_seconds": 5.04, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 296, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 296}

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074775",
    "title": "Senior HRBP Manager, Finance & Strategy",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159887359-senior-hrbp-manager-finance-strategy-",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:33:12.333084+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075740",
    "title": "Senior DevOps Engineer (Kubernetes) - Federal",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159871179-senior-devops-engineer-kubernetes-federal",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:33:12.333084+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076859",
    "title": "Senior Data & Analytics Solution Sales Executive - Energy",
    "location": "San Diego, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159773559-senior-data-analytics-solution-sales-executive-energy",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:33:12.333084+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076864",
    "title": "Senior Data & Analytics Solution Sales Executive - Healthcare West",
    "location": "San Diego, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159773060-senior-data-analytics-solution-sales-executive-healthcare-west",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:33:12.333084+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076656",
    "title": "Sr Software Engineer",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000159760671-sr-software-engineer",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:33:12.333084+00:00",
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
- HTTP requests/cumulative request time: 48 / 71.241s
- Company elapsed time: 83.251s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 19 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 19}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 348
- After US/location filtering: 19
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 35.343, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 5.71, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 5.815, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 5.738, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 5.773, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 5.845, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 6.171, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 5.782, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 7.075, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 48}

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46026",
    "title": "Containerboard Market Research Sales Consultant - Remote (Contract)",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Containerboard-Market-Research-Sales-Consultant-Remote-Contract/46026",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:33:37.161766+00:00",
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
    "fetched_at": "2026-11-05T15:33:37.161766+00:00",
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
    "fetched_at": "2026-11-05T15:33:37.161766+00:00",
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
    "fetched_at": "2026-11-05T15:33:37.161766+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg LP has built a significant global media business across television, digital, magazine, radio, and live event platforms. Amid a transformative p"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45958",
    "title": "Senior Software Engineer - Hadoop Infrastructure",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Software-Engineer-Hadoop-Infrastructure/45958",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:33:37.161766+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements The Team Bloomberg runs on data! It's our business and our product. Financial institutions need timely, accurate data to capture opportunities and evalua"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 64
- HTTP requests/cumulative request time: 603 / 144.852s
- Company elapsed time: 227.310s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 539 / 0 / 0
- Detail cache statuses: {'fetched:new': 516, 'fetched:missing_detail': 23}
- Relevant JD recovery: {'eligible': 116, 'usable_jd': 116}
- Raw jobs found: 1267
- After US/location filtering: 539
- With trustworthy posted_date: 539
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 19.736, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 17.69, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 12.847, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.599, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.931, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.407, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.502, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.824, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.76, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 16.082, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "full stack", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.54, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "python react", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.646, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "pyspark databricks", "raw_jobs": 47, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 47}
- Query diagnostic: {"elapsed_seconds": 7.571, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "experienced software engineer java python", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.585, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "agentic ai", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.095, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.346, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "software engineer ii", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.815, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.823, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "security engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.101, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "quantitative developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.32, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "software engineer java spring", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.826, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 1, "pages_fetched": 1, "query": "software engineer python authe", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.223, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "aws data platform engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.382, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data engineer applied ai", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 3.659, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 1, "pages_fetched": 1, "query": "asset management technology", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 20}

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
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:33:50.868568+00:00",
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
    "fetched_at": "2026-11-05T15:33:50.868568+00:00",
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
    "fetched_at": "2026-11-05T15:33:50.868568+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorganChase within the Corp"
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
    "fetched_at": "2026-11-05T15:33:50.868568+00:00",
    "date_confidence": "high",
    "description": "As a Senior Lead Software Engineer at JPMorgan Chase within the Commercial & Investment Bank Digital Channel's team, you will build autonomous agent capabilities that can plan, exe"
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
    "fetched_at": "2026-11-05T15:33:50.868568+00:00",
    "date_confidence": "high",
    "description": "We have an exciting opportunity to advance your career and drive meaningful impact by pushing the limits of modern engineering. As a Lead Software Engineer at JPMorganChase within "
  }
]
```

## Capital One

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://capitalone.wd12.myworkdayjobs.com/Capital_One`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 175 / 56.701s
- Company elapsed time: 81.689s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 147 / 0 / 0
- Detail cache statuses: {'fetched:new': 135, 'fetched:missing_detail': 12}
- Relevant JD recovery: {'eligible': 49, 'usable_jd': 49}
- Raw jobs found: 526
- After US/location filtering: 147
- With trustworthy posted_date: 147
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 34.765, "first_pass_survivors": 78, "group": "official", "jds_resolved": 78, "original_postings_resolved": 78, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 78, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 14.841, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.707, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.049, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.605, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.486, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.815, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.38, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 3.78, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999632",
    "title": "Manager, Product Management- Bedrock Payments Team",
    "location": "New York, NY; McLean, VA; Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/New-York-NY/Manager--Product-Management--Bedrock-Payments-Team_R999632-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:34:16.820751+00:00",
    "date_confidence": "high",
    "description": "Manager, Product Management- Bedrock Payments Team Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, finding value creation op"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005195",
    "title": "Principal Associate, Data Scientist - SBB Marketing & Deposit Strategy",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Principal-Associate--Data-Scientist---SBB-Marketing---Deposit-Strategy_R1005195-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:34:16.820751+00:00",
    "date_confidence": "high",
    "description": "Principal Associate, Data Scientist - SBB Marketing & Deposit Strategy Data is at the center of everything we do. As a startup, we disrupted the credit card industry by individuall"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005246",
    "title": "Full-stack Engineer 4 (Python, AWS)",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Full-stack-Engineer-4--Python--AWS-_R1005246-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:34:16.820751+00:00",
    "date_confidence": "high",
    "description": "Full-stack Engineer 4 (Python, AWS) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, incl"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005241",
    "title": "Machine Learning Engineer 4 - Manager IC",
    "location": "New York, NY; McLean, VA; San Jose, CA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/New-York-NY/Machine-Learning-Engineer-4---Manager-IC_R1005241-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:34:16.820751+00:00",
    "date_confidence": "high",
    "description": "Machine Learning Engineer 4 - Manager IC Do you love building and pioneering in the AI and technology space? Do you enjoy solving complex business problems in a fast-paced, collabo"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1005189",
    "title": "Senior Manager, Full-stack Engineer",
    "location": "McLean, VA; Cambridge, MA; Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Manager--Full-stack-Engineer_R1005189-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:34:16.820751+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Full-stack Engineer Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, incl"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 41
- HTTP requests/cumulative request time: 469 / 170.500s
- Company elapsed time: 234.659s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 428 / 0 / 0
- Detail cache statuses: {'fetched:new': 420, 'fetched:missing_detail': 8}
- Relevant JD recovery: {'eligible': 54, 'usable_jd': 54}
- Raw jobs found: 817
- After US/location filtering: 428
- With trustworthy posted_date: 428
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 31.892, "first_pass_survivors": 63, "group": "official", "jds_resolved": 63, "original_postings_resolved": 63, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 63, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 21.862, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.469, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 24.007, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 23.471, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.46, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.428, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.841, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 26.66, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 16.99, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "core infrastructure", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.426, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "cleared site reliability engineer database", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.16, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "software developer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 8.991, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "applications developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}

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
    "fetched_at": "2026-11-05T15:35:00.413666+00:00",
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
    "fetched_at": "2026-11-05T15:35:00.413666+00:00",
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
    "fetched_at": "2026-11-05T15:35:00.413666+00:00",
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
    "fetched_at": "2026-11-05T15:35:00.413666+00:00",
    "date_confidence": "high",
    "description": "Oracle Health is seeking a Senior AI Agent Engineer to build production AI agents and workflow automation capabilities that accelerate analytics delivery, improve insight generatio"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "336795",
    "title": "Senior Principal Engineer - AI Networking",
    "location": "Seattle, WA, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/336795",
    "posted_date": "2026-09-29",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:35:00.413666+00:00",
    "date_confidence": "high",
    "description": "You will work at the intersection of distributed systems, networking, and AI infrastructure, driving architecture, design, implementation, and performance optimization across softw"
  }
]
```

## Walmart Global Tech

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://walmart.wd504.myworkdayjobs.com/WalmartExternal`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 28
- HTTP requests/cumulative request time: 389 / 264.759s
- Company elapsed time: 317.713s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 360 / 0 / 0
- Detail cache statuses: {'fetched:new': 331, 'fetched:missing_detail': 29}
- Relevant JD recovery: {'eligible': 54, 'usable_jd': 54}
- Raw jobs found: 544
- After US/location filtering: 360
- With trustworthy posted_date: 360
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 62.799, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 31.608, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 31.797, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 55.674, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 24.238, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 29.89, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 27.766, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.944, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 39.75, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 7.163, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "usa software engineer ii", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 20}

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
    "fetched_at": "2026-11-05T15:35:38.510371+00:00",
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
    "fetched_at": "2026-11-05T15:35:38.510371+00:00",
    "date_confidence": "high",
    "description": "Position Summary... What you'll do... Role summary: As the Group Director, Applied AI & Engineering you will lead an elite, high-caliber applied AI and engineering team dedicated t"
  },
  {
    "company": "Walmart Global Tech",
    "source": "walmart_global_tech_official_careers",
    "job_id": "R-2612602",
    "title": "Principal, Data Scientist, Agentic AI Systems Engineering & Model Post-Training",
    "location": "(USA) Supply Chain Optimization AR Bentonville Home Office",
    "official_url": "https://walmart.wd504.myworkdayjobs.com/WalmartExternal/job/USA-Supply-Chain-Optimization-AR-Bentonville-Home-Office/Principal--Data-Scientist--Agentic-AI-Systems-Engineering---Model-Post-Training_R-2612602",
    "posted_date": "2026-08-22",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:35:38.510371+00:00",
    "date_confidence": "high",
    "description": "Position Summary... What you'll do... The Opportunity: Walmart’s Supply Chain AI Lab & Innovation Factory is building a new generation of production-grade agentic AI systems that r"
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
    "fetched_at": "2026-11-05T15:35:38.510371+00:00",
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
    "fetched_at": "2026-11-05T15:35:38.510371+00:00",
    "date_confidence": "high",
    "description": "Position Summary... What you'll do... The Opportunity: Walmart’s Supply Chain AI Lab & Innovation Factory is building a new generation of production-grade agentic AI systems that r"
  }
]
```

## Cloudflare

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/cloudflare/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.386s
- Company elapsed time: 1.840s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 92, 'usable_jd': 92}
- Raw jobs found: 463
- After US/location filtering: 460
- With trustworthy posted_date: 460
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
    "fetched_at": "2026-11-05T15:36:28.031124+00:00",
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
    "fetched_at": "2026-11-05T15:36:28.031124+00:00",
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
    "fetched_at": "2026-11-05T15:36:28.031124+00:00",
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
    "fetched_at": "2026-11-05T15:36:28.031124+00:00",
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
    "fetched_at": "2026-11-05T15:36:28.031124+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.250s
- Company elapsed time: 1.235s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 148, 'usable_jd': 148}
- Raw jobs found: 760
- After US/location filtering: 417
- With trustworthy posted_date: 417
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
    "fetched_at": "2026-11-05T15:36:29.871786+00:00",
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
    "fetched_at": "2026-11-05T15:36:29.871786+00:00",
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
    "fetched_at": "2026-11-05T15:36:29.871786+00:00",
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
    "fetched_at": "2026-11-05T15:36:29.871786+00:00",
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
    "fetched_at": "2026-11-05T15:36:29.871786+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.160s
- Company elapsed time: 0.799s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 55, 'usable_jd': 55}
- Raw jobs found: 278
- After US/location filtering: 203
- With trustworthy posted_date: 203
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
    "fetched_at": "2026-11-05T15:36:31.108353+00:00",
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
    "fetched_at": "2026-11-05T15:36:31.108353+00:00",
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
    "fetched_at": "2026-11-05T15:36:31.108353+00:00",
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
    "fetched_at": "2026-11-05T15:36:31.108353+00:00",
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
    "fetched_at": "2026-11-05T15:36:31.108353+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.162s
- Company elapsed time: 0.737s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 152
- After US/location filtering: 141
- With trustworthy posted_date: 141
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
    "fetched_at": "2026-11-05T15:36:31.908448+00:00",
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
    "fetched_at": "2026-11-05T15:36:31.908448+00:00",
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
    "fetched_at": "2026-11-05T15:36:31.908448+00:00",
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
    "fetched_at": "2026-11-05T15:36:31.908448+00:00",
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
    "fetched_at": "2026-11-05T15:36:31.908448+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.220s
- Company elapsed time: 0.609s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 144
- After US/location filtering: 94
- With trustworthy posted_date: 94
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
    "fetched_at": "2026-11-05T15:36:32.646841+00:00",
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
    "fetched_at": "2026-11-05T15:36:32.646841+00:00",
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
    "fetched_at": "2026-11-05T15:36:32.646841+00:00",
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
    "fetched_at": "2026-11-05T15:36:32.646841+00:00",
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
    "fetched_at": "2026-11-05T15:36:32.646841+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.246s
- Company elapsed time: 0.856s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 16, 'usable_jd': 16}
- Raw jobs found: 243
- After US/location filtering: 134
- With trustworthy posted_date: 134
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8638232002",
    "title": "AI Transformation Owner, CRO",
    "location": "Remote, United States",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8638232002",
    "posted_date": "2026-07-22",
    "updated_date": "2026-10-28",
    "fetched_at": "2026-11-05T15:36:33.259143+00:00",
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
    "fetched_at": "2026-11-05T15:36:33.259143+00:00",
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
    "fetched_at": "2026-11-05T15:36:33.259143+00:00",
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
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-05T15:36:33.259143+00:00",
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
    "fetched_at": "2026-11-05T15:36:33.259143+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.123s
- Company elapsed time: 0.206s
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
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-05T15:36:34.115198+00:00",
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
    "fetched_at": "2026-11-05T15:36:34.115198+00:00",
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
    "fetched_at": "2026-11-05T15:36:34.115198+00:00",
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
    "fetched_at": "2026-11-05T15:36:34.115198+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8801465002",
    "title": "Marketing Program Manager",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8801465002",
    "posted_date": "2026-09-15",
    "updated_date": "2026-10-20",
    "fetched_at": "2026-11-05T15:36:34.115198+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.155s
- Company elapsed time: 0.487s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 14, 'usable_jd': 14}
- Raw jobs found: 109
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
    "fetched_at": "2026-11-05T15:36:34.323214+00:00",
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
    "fetched_at": "2026-11-05T15:36:34.323214+00:00",
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
    "fetched_at": "2026-11-05T15:36:34.323214+00:00",
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
    "fetched_at": "2026-11-05T15:36:34.323214+00:00",
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
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-05T15:36:34.323214+00:00",
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
- Company elapsed time: 0.962s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 42, 'usable_jd': 42}
- Raw jobs found: 271
- After US/location filtering: 258
- With trustworthy posted_date: 258
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8912603002",
    "title": "Accountant Partnerships Manager",
    "location": "New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8912603002?gh_jid=8912603002",
    "posted_date": "2026-10-23",
    "updated_date": "2026-10-23",
    "fetched_at": "2026-11-05T15:36:34.813366+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8912605002",
    "title": "Accountant Partnerships Manager",
    "location": "San Francisco, California, United States; New York, New York, United States",
    "official_url": "https://www.brex.com/careers/8912605002?gh_jid=8912605002",
    "posted_date": "2026-10-23",
    "updated_date": "2026-10-23",
    "fetched_at": "2026-11-05T15:36:34.813366+00:00",
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
    "fetched_at": "2026-11-05T15:36:34.813366+00:00",
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
    "fetched_at": "2026-11-05T15:36:34.813366+00:00",
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
    "fetched_at": "2026-11-05T15:36:34.813366+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.224s
- Company elapsed time: 1.493s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 60, 'usable_jd': 60}
- Raw jobs found: 312
- After US/location filtering: 269
- With trustworthy posted_date: 269
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8332753",
    "title": "Account Development Representative - Canada",
    "location": "Remote - Quebec; Remote - Toronto",
    "official_url": "https://www.samsara.com/company/careers/roles/8332753?gh_jid=8332753",
    "posted_date": "2026-10-28",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-05T15:36:35.776230+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8207928",
    "title": "Account Development Representative - Canada",
    "location": "Remote - Quebec; Remote - Toronto",
    "official_url": "https://www.samsara.com/company/careers/roles/8207928?gh_jid=8207928",
    "posted_date": "2026-09-17",
    "updated_date": "2026-11-01",
    "fetched_at": "2026-11-05T15:36:35.776230+00:00",
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
    "fetched_at": "2026-11-05T15:36:35.776230+00:00",
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
    "fetched_at": "2026-11-05T15:36:35.776230+00:00",
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
    "fetched_at": "2026-11-05T15:36:35.776230+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.169s
- Company elapsed time: 0.441s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 174
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
    "fetched_at": "2026-11-05T15:36:37.270268+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.270268+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8868958002",
    "title": "Analytics Lead, Decisions & Insights",
    "location": "New York, NY; New York, New York, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8868958002?gh_jid=8868958002",
    "posted_date": "2026-10-05",
    "updated_date": "2026-10-19",
    "fetched_at": "2026-11-05T15:36:37.270268+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
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
    "fetched_at": "2026-11-05T15:36:37.270268+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.270268+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
  }
]
```

## Spotify

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/spotify`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.184s
- Company elapsed time: 0.282s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 13, 'usable_jd': 13}
- Raw jobs found: 87
- After US/location filtering: 64
- With trustworthy posted_date: 64
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
    "fetched_at": "2026-11-05T15:36:37.712440+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.712440+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.712440+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.712440+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.712440+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.132s
- Company elapsed time: 0.472s
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
    "fetched_at": "2026-11-05T15:36:37.997881+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.997881+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.997881+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.997881+00:00",
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
    "fetched_at": "2026-11-05T15:36:37.997881+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.105s
- Company elapsed time: 0.309s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 35, 'usable_jd': 35}
- Raw jobs found: 151
- After US/location filtering: 77
- With trustworthy posted_date: 77
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
    "fetched_at": "2026-11-05T15:36:38.469444+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.469444+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.469444+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.469444+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.469444+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.054s
- Company elapsed time: 0.101s
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
    "fetched_at": "2026-11-05T15:36:38.782168+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.782168+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.782168+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.782168+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.782168+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.086s
- Company elapsed time: 0.307s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 33, 'usable_jd': 33}
- Raw jobs found: 118
- After US/location filtering: 96
- With trustworthy posted_date: 96
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
    "fetched_at": "2026-11-05T15:36:38.884131+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.884131+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.884131+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.884131+00:00",
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
    "fetched_at": "2026-11-05T15:36:38.884131+00:00",
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
- HTTP requests/cumulative request time: 265 / 85.354s
- Company elapsed time: 122.832s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 220 / 0 / 0
- Detail cache statuses: {'fetched:new': 210, 'fetched:missing_detail': 9, 'reuse_after_error:missing_detail': 1}
- Relevant JD recovery: {'eligible': 57, 'ai_recover': 1, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 56}
- Raw jobs found: 838
- After US/location filtering: 220
- With trustworthy posted_date: 219
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 22.456, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 17.326, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.619, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 5.558, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.94, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.797, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.555, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.773, "first_pass_survivors": 23, "group": "official", "jds_resolved": 22, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 46}
- Query diagnostic: {"elapsed_seconds": 6.488, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 1.751, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "full stack backend", "raw_jobs": 31, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 31}
- Query diagnostic: {"elapsed_seconds": 7.445, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.408, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "cloud engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.664, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "security engineer remote", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.796, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "software engineer collaboration devices", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 5.503, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "splunk engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.22, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer solution test iq platform", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2012214",
    "title": "ASIC Design Verification Technical Leader",
    "location": "Carlsbad, California, US; Allentown, Pennsylvania, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Carlsbad-California-US/ASIC-Design-Verification-Technical-Leader_2012214",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:36:39.192710+00:00",
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
    "fetched_at": "2026-11-05T15:36:39.192710+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 01/18/2027 Meet the Team The Silicon One team creates innovative hardware platforms central to the AI era, powering Cisco’s core Swi"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2021051",
    "title": "Enterprise Hardware Design Engineer",
    "location": "RTP, North Carolina, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/RTP-North-Carolina-US/Enterprise-Hardware-Engineering-Technical-Lead_2021051",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:36:39.192710+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 01/03/2027 Meet the Team: The Enterprise Routing organization designs and develops Cisco's Edge and Access routing products. We arch"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2027138",
    "title": "Software Engineering Technical Leader - Embedded Systems",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Software-Engineering-Technical-Leader---Embedded-Systems_2027138",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:36:39.192710+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 11/30/2026 This role requires working onsite in Milpitas, CA. Meet the Team: The Networking Hardware Engineering (NHE) group creates"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2018124",
    "title": "Cloud Engineer II (Full Time) - United States",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Cloud-Engineer_2018124",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:36:39.192710+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 11/05/2026 Meet the Team Our Security Policy and Access team is at the heart of Cisco’s mission, building and operating market-leadi"
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://careers.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 144 / 63.066s
- Company elapsed time: 90.237s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 112 / 0 / 0
- Detail cache statuses: {'fetched:new': 112}
- Relevant JD recovery: {'eligible': 40, 'usable_jd': 40}
- Raw jobs found: 800
- After US/location filtering: 112
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 59.78, "first_pass_survivors": 96, "group": "official", "jds_resolved": 96, "original_postings_resolved": 96, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 96, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.304, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 6.784, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 6.523, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.219, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.211, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.325, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.24, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 3.002, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.848, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "cloud developer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 75}

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
    "fetched_at": "2026-11-05T15:37:38.179948+00:00",
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
    "fetched_at": "2026-11-05T15:37:38.179948+00:00",
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
    "fetched_at": "2026-11-05T15:37:38.179948+00:00",
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
    "fetched_at": "2026-11-05T15:37:38.179948+00:00",
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
    "fetched_at": "2026-11-05T15:37:38.179948+00:00",
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
- HTTP requests/cumulative request time: 313 / 132.040s
- Company elapsed time: 174.365s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 286 / 0 / 0
- Detail cache statuses: {'fetched:new': 278, 'fetched:missing_detail': 8}
- Relevant JD recovery: {'eligible': 135, 'usable_jd': 135}
- Raw jobs found: 495
- After US/location filtering: 286
- With trustworthy posted_date: 286
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 42.102, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 26.316, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 3.117, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 26.631, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.069, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.217, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.109, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.916, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 19.347, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.696, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "ai workflow specialist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 7}

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
    "fetched_at": "2026-11-05T15:38:39.043319+00:00",
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
    "fetched_at": "2026-11-05T15:38:39.043319+00:00",
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
    "fetched_at": "2026-11-05T15:38:39.043319+00:00",
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
    "fetched_at": "2026-11-05T15:38:39.043319+00:00",
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
    "fetched_at": "2026-11-05T15:38:39.043319+00:00",
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
- HTTP requests/cumulative request time: 34 / 36.256s
- Company elapsed time: 42.729s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 7 / 8 / 110
- Detail cache statuses: {'reused': 6, 'reuse_after_error:stale': 2}
- Relevant JD recovery: {'deterministic_skip': 103, 'cache_reused': 8, 'eligible': 13, 'ai_skip': 7, 'detail_requests': 7, 'detail_failure': 7, 'last_good_reused': 2, 'budget_deferred': 0, 'usable_jd': 8}
- Raw jobs found: 270
- After US/location filtering: 123
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 18.988, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.121, "first_pass_survivors": 21, "group": "official", "jds_resolved": 0, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.249, "first_pass_survivors": 17, "group": "official", "jds_resolved": 0, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.712, "first_pass_survivors": 19, "group": "official", "jds_resolved": 0, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.854, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.855, "first_pass_survivors": 13, "group": "official", "jds_resolved": 0, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.456, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.286, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.243, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}

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
    "fetched_at": "2026-11-05T15:38:41.492256+00:00",
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
    "fetched_at": "2026-11-05T15:38:41.492256+00:00",
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
    "fetched_at": "2026-11-05T15:38:41.492256+00:00",
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
    "fetched_at": "2026-11-05T15:38:41.492256+00:00",
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
    "fetched_at": "2026-11-05T15:38:41.492256+00:00",
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
- HTTP requests/cumulative request time: 57 / 43.436s
- Company elapsed time: 50.272s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 39 / 0 / 0
- Detail cache statuses: {'fetched:new': 39}
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 186
- After US/location filtering: 39
- With trustworthy posted_date: 39
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 34.831, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 37, "stop_reason": "early_stop", "unique_contribution": 37, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 0.914, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.871, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 1.613, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 2.968, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 3.327, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 3.278, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 0.794, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.753, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 19}

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
    "fetched_at": "2026-11-05T15:38:55.073599+00:00",
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
    "fetched_at": "2026-11-05T15:38:55.073599+00:00",
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
    "posted_date": "2026-10-21",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:38:55.073599+00:00",
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
    "fetched_at": "2026-11-05T15:38:55.073599+00:00",
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
    "fetched_at": "2026-11-05T15:38:55.073599+00:00",
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
- HTTP requests/cumulative request time: 150 / 24.969s
- Company elapsed time: 46.851s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 123 / 0 / 0
- Detail cache statuses: {'fetched:new': 117, 'fetched:missing_detail': 6}
- Relevant JD recovery: {'eligible': 33, 'usable_jd': 33}
- Raw jobs found: 256
- After US/location filtering: 123
- With trustworthy posted_date: 123
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.271, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.657, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.652, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 8.2, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.146, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.403, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.447, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.344, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.382, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3096146",
    "title": "Machine Learning / Computer Vision Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720988289",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:39:08.418155+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Video Systems, HW Architecture General Summary: Qualcomm’s Computer Vision Systems team is bui"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3092821",
    "title": "CPU Physical Electrical Analysis Engineer, Santa Clara/Austin",
    "location": "Santa Clara, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446719402682",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:39:08.418155+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > CPU Engineering General Summary: Our Mission We are dedicated to transforming the industry by "
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3094445",
    "title": "Compiler Toolchain Engineer",
    "location": "Austin, Texas, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720171328",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:39:08.418155+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Compiler Toolchain Software General Summary: As a leading technology innovator, Qualcomm pushe"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3098857",
    "title": "Machine Learning Senior Engineer - Generative AI",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721916659",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:39:08.418155+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Modem Technologies Software General Summary: We are seeking an experienced Machine Learning En"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3096704",
    "title": "CPU Physical Electrical Analysis Engineer",
    "location": "Santa Clara, California, United States of America; Santa Clara, CA, USA",
    "official_url": "https://careers.qualcomm.com/careers/job/446721139146",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:39:08.418155+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > CPU Engineering General Summary: Our Mission We are dedicated to transforming the industry by "
  }
]
```

## AMD

- Status: ok
- Scraping method: HTTP GET public Jibe/iCIMS jobs JSON
- Search URL/API: `https://careers.amd.com/api/jobs`
- Pagination: page=1,2,... per role query; stop on total/empty/repeat/short page
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 14 / 21.642s
- Company elapsed time: 23.407s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 199, 'usable_jd': 199}
- Raw jobs found: 1220
- After US/location filtering: 479
- With trustworthy posted_date: 479
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.332, "first_pass_survivors": 317, "group": "official", "jds_resolved": 317, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 317, "stop_reason": "page_budget", "unique_contribution": 317, "unique_jobs": 317}
- Query diagnostic: {"elapsed_seconds": 10.502, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning", "raw_jobs": 89, "stop_reason": "early_stop", "unique_contribution": 29, "unique_jobs": 89}
- Query diagnostic: {"elapsed_seconds": 2.234, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 4.603, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "AI research", "raw_jobs": 214, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 214}
- Query diagnostic: {"elapsed_seconds": 2.735, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 300}

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
    "fetched_at": "2026-11-05T15:39:21.257341+00:00",
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
    "fetched_at": "2026-11-05T15:39:21.257341+00:00",
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
    "fetched_at": "2026-11-05T15:39:21.257341+00:00",
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
    "fetched_at": "2026-11-05T15:39:21.257341+00:00",
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
    "fetched_at": "2026-11-05T15:39:21.257341+00:00",
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
- HTTP requests/cumulative request time: 38 / 23.242s
- Company elapsed time: 27.283s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 24 / 0 / 0
- Detail cache statuses: {'fetched:new': 22, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 8, 'usable_jd': 8}
- Raw jobs found: 92
- After US/location filtering: 24
- With trustworthy posted_date: 24
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.942, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 17, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 0.41, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.425, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 4.153, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 3.981, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 2.101, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 0.427, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.437, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.429, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}

Sample normalized records:

```json
[
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19773",
    "title": "Senior General Ledger Accountant",
    "location": "Remote (US)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--US/Senior-General-Ledger-Accountant_R19773",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:39:44.665918+00:00",
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
    "fetched_at": "2026-11-05T15:39:44.665918+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect As a Senior Product Designer for Zoom Virtual Agent, you will shape the conversational and agentic AI experiences that define how businesses and their customers"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19706",
    "title": "AI Deployment Strategist",
    "location": "Remote (US)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--US/AI-Deployment-Strategist_R19706-1",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:39:44.665918+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect As an AI Deployment Strategist at Zoom, you will be at the intersection of cutting-edge AI and real-world customer impact, leading the deployment of next-genera"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R18761",
    "title": "Staff AI Engineer",
    "location": "Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Seattle-WA/Staff-AI-Engineer_R18761-1",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:39:44.665918+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect You'll design, implement, and own the inference systems that serve Zoom's AI models at production scale -- across real-time communication, vision, and language "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19832",
    "title": "Principal AI Product Manager",
    "location": "Seattle (WA); San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Seattle-WA/Principal-AI-Product-Manager_R19832-1",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:39:44.665918+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect As a Principal AI Product Manager at Zoom AI Services, you will own meaningful product outcomes at the intersection of AI innovation, platform strategy, and dev"
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
- HTTP requests/cumulative request time: 1 / 0.232s
- Company elapsed time: 1.043s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 50, 'usable_jd': 50}
- Raw jobs found: 355
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
    "fetched_at": "2026-11-05T15:39:45.346956+00:00",
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
    "fetched_at": "2026-11-05T15:39:45.346956+00:00",
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
    "fetched_at": "2026-11-05T15:39:45.346956+00:00",
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
    "fetched_at": "2026-11-05T15:39:45.346956+00:00",
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
    "fetched_at": "2026-11-05T15:39:45.346956+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.458s
- Company elapsed time: 2.375s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 81, 'usable_jd': 81}
- Raw jobs found: 923
- After US/location filtering: 502
- With trustworthy posted_date: 502
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
    "fetched_at": "2026-11-05T15:39:46.396598+00:00",
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
    "fetched_at": "2026-11-05T15:39:46.396598+00:00",
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
    "fetched_at": "2026-11-05T15:39:46.396598+00:00",
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
    "fetched_at": "2026-11-05T15:39:46.396598+00:00",
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
    "fetched_at": "2026-11-05T15:39:46.396598+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.167s
- Company elapsed time: 0.907s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 32, 'usable_jd': 32}
- Raw jobs found: 272
- After US/location filtering: 255
- With trustworthy posted_date: 255
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
    "fetched_at": "2026-11-05T15:39:48.772565+00:00",
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
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-05T15:39:48.772565+00:00",
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
    "fetched_at": "2026-11-05T15:39:48.772565+00:00",
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
    "fetched_at": "2026-11-05T15:39:48.772565+00:00",
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
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-05T15:39:48.772565+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.140s
- Company elapsed time: 0.657s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 207
- After US/location filtering: 116
- With trustworthy posted_date: 116
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
    "fetched_at": "2026-11-05T15:39:49.681069+00:00",
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
    "fetched_at": "2026-11-05T15:39:49.681069+00:00",
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
    "fetched_at": "2026-11-05T15:39:49.681069+00:00",
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
    "fetched_at": "2026-11-05T15:39:49.681069+00:00",
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
    "fetched_at": "2026-11-05T15:39:49.681069+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.399s
- Company elapsed time: 2.847s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 160, 'usable_jd': 160}
- Raw jobs found: 681
- After US/location filtering: 546
- With trustworthy posted_date: 546
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
    "fetched_at": "2026-11-05T15:39:50.341130+00:00",
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
    "fetched_at": "2026-11-05T15:39:50.341130+00:00",
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
    "fetched_at": "2026-11-05T15:39:50.341130+00:00",
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
    "fetched_at": "2026-11-05T15:39:50.341130+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5471539008",
    "title": "Accounting Analytics & BI Engineer",
    "location": "San Francisco, CA | New York City, NY; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5471539008",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-05T15:39:50.341130+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.097s
- Company elapsed time: 0.241s
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
    "job_id": "4724999006",
    "title": "Agency Development Lead - Independent Agencies",
    "location": "Los Angeles/Santa Monica, CA; New York City, NY",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4724999006?gh_jid=4724999006",
    "posted_date": "2026-10-26",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-05T15:39:53.189153+00:00",
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
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-05T15:39:53.189153+00:00",
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
    "updated_date": "2026-11-02",
    "fetched_at": "2026-11-05T15:39:53.189153+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4705311006",
    "title": "Business Development Associate",
    "location": "Toronto; New York",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4705311006?gh_jid=4705311006",
    "posted_date": "2026-08-14",
    "updated_date": "2026-09-02",
    "fetched_at": "2026-11-05T15:39:53.189153+00:00",
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
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-05T15:39:53.189153+00:00",
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
- HTTP requests/cumulative request time: 24 / 25.472s
- Company elapsed time: 29.093s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 235, 'usable_jd': 235}
- Raw jobs found: 1066
- After US/location filtering: 459
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.2, "first_pass_survivors": 146, "group": "official", "jds_resolved": 146, "original_postings_resolved": 146, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 146, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.794, "first_pass_survivors": 101, "group": "official", "jds_resolved": 101, "original_postings_resolved": 101, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 101, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.256, "first_pass_survivors": 63, "group": "official", "jds_resolved": 63, "original_postings_resolved": 63, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 109, "stop_reason": "page_budget", "unique_contribution": 63, "unique_jobs": 109}
- Query diagnostic: {"elapsed_seconds": 3.384, "first_pass_survivors": 63, "group": "official", "jds_resolved": 63, "original_postings_resolved": 63, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 63, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.264, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 142}
- Query diagnostic: {"elapsed_seconds": 3.221, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 147}
- Query diagnostic: {"elapsed_seconds": 1.943, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 54, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 0.908, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 4.123, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 150}

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
    "fetched_at": "2026-11-05T15:39:53.430968+00:00",
    "date_confidence": "unknown",
    "description": "About the team: TRAE (The Real AI Engineer) is an intelligent engineer capable of understanding requirements, orchestrating tools, and independently completing development tasks, p"
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
    "fetched_at": "2026-11-05T15:39:53.430968+00:00",
    "date_confidence": "unknown",
    "description": "We are seeking an experienced Research Scientist or Engineer to help define and build the next generation of AI infrastructure. In this role, you will work at the intersection of l"
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
    "fetched_at": "2026-11-05T15:39:53.430968+00:00",
    "date_confidence": "unknown",
    "description": "About the Team Join ByteDance’s database R&D team, where you’ll build and own cutting-edge database products supporting Bytedance’s global infrastructure. Our diverse portfolio inc"
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
    "fetched_at": "2026-11-05T15:39:53.430968+00:00",
    "date_confidence": "unknown",
    "description": "About the Team Join ByteDance’s database R&D team, where you’ll build and own cutting-edge database products supporting Bytedance’s global infrastructure. Our diverse portfolio inc"
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
    "fetched_at": "2026-11-05T15:39:53.430968+00:00",
    "date_confidence": "unknown",
    "description": "The mission of our AML team is to push the next-generation AI infrastructure and recommendation platform for the ads ranking, search ranking, live & ecom ranking in our company. We"
  }
]
```

## Chime

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/chime/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.125s
- Company elapsed time: 0.472s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 74
- After US/location filtering: 74
- With trustworthy posted_date: 74
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
    "fetched_at": "2026-11-05T15:39:55.270533+00:00",
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
    "fetched_at": "2026-11-05T15:39:55.270533+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\"><strong>About the Role</strong></span></h2> <p><span style=\"font-family: helvetica, arial, sans-serif;\">We are hiring a"
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
    "fetched_at": "2026-11-05T15:39:55.270533+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the role</strong></h2> <p>We are hiring a Business Control Manager to join Chime’s Compliance Business Control Management team, with a primary focus on control de"
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
    "fetched_at": "2026-11-05T15:39:55.270533+00:00",
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
    "fetched_at": "2026-11-05T15:39:55.270533+00:00",
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
- HTTP requests/cumulative request time: 134 / 45.379s
- Company elapsed time: 64.970s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 109 / 0 / 0
- Detail cache statuses: {'fetched:new': 108, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 32, 'usable_jd': 32}
- Raw jobs found: 490
- After US/location filtering: 109
- With trustworthy posted_date: 109
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.294, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.626, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.813, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 7.722, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.629, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 8.523, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 6.189, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.902, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 4.272, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}

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
    "fetched_at": "2026-11-05T15:39:55.743783+00:00",
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
    "fetched_at": "2026-11-05T15:39:55.743783+00:00",
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
    "fetched_at": "2026-11-05T15:39:55.743783+00:00",
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
    "fetched_at": "2026-11-05T15:39:55.743783+00:00",
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
    "fetched_at": "2026-11-05T15:39:55.743783+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.120s
- Company elapsed time: 0.209s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 31
- After US/location filtering: 20
- With trustworthy posted_date: 20
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
    "fetched_at": "2026-11-05T15:40:11.950413+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z95gas6hz75zjz77zz90zpz71zz80zeoz80zz68zlz66z"
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
    "fetched_at": "2026-11-05T15:40:11.950413+00:00",
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
    "fetched_at": "2026-11-05T15:40:11.950413+00:00",
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
    "fetched_at": "2026-11-05T15:40:11.950413+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90za3wz122zz77zjz88zx7z66zz78zz69zbz70znpvz79z6"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8328469",
    "title": "Legal Operations Associate",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8328469?gh_jid=8328469",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-03",
    "fetched_at": "2026-11-05T15:40:11.950413+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qowz82zfwz66zwhdz68zz78zz74zl2vz70z03z66zz80zrz77zt56z90zz81zz7"
  }
]
```

## Expedia Group

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://expedia.wd108.myworkdayjobs.com/search`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 62 / 21.266s
- Company elapsed time: 29.936s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 43 / 0 / 0
- Detail cache statuses: {'fetched:new': 43}
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 328
- After US/location filtering: 43
- With trustworthy posted_date: 43
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 18.414, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.023, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 32, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 0.3, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 1.416, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 40, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 1.798, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.806, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.34, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.287, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.552, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 47, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 47}

Sample normalized records:

```json
[
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-110938",
    "title": "Senior Technical Integration Consultant",
    "location": "USA - Illinois - Chicago; UK - London",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---Illinois---Chicago/Senior-Technical-Integration-Consultant_R-110938",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:40:12.160903+00:00",
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
    "fetched_at": "2026-11-05T15:40:12.160903+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109868",
    "title": "Software Development Engineer II",
    "location": "USA - Illinois - Chicago",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---Illinois---Chicago/Software-Development-Engineer-II_R-109868-1",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:40:12.160903+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-110515",
    "title": "UX Designer III, ProServe – Strategic Partners",
    "location": "USA - Illinois - Chicago",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---Illinois---Chicago/UX-Designer-III--ProServe---Strategic-Partners_R-110515-2",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:40:12.160903+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-111084",
    "title": "Senior Software Development Engineer",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Senior-Software-Development-Engineer_R-111084-1",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:40:12.160903+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.125s
- Company elapsed time: 0.202s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 110
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
    "fetched_at": "2026-11-05T15:40:22.525526+00:00",
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
    "fetched_at": "2026-11-05T15:40:22.525526+00:00",
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
    "fetched_at": "2026-11-05T15:40:22.525526+00:00",
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
    "fetched_at": "2026-11-05T15:40:22.525526+00:00",
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
    "fetched_at": "2026-11-05T15:40:22.525526+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.122s
- Company elapsed time: 0.407s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 8, 'usable_jd': 8}
- Raw jobs found: 88
- After US/location filtering: 80
- With trustworthy posted_date: 80
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
    "fetched_at": "2026-11-05T15:40:22.729049+00:00",
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
    "fetched_at": "2026-11-05T15:40:22.729049+00:00",
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
    "fetched_at": "2026-11-05T15:40:22.729049+00:00",
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
    "fetched_at": "2026-11-05T15:40:22.729049+00:00",
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
    "fetched_at": "2026-11-05T15:40:22.729049+00:00",
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
- HTTP requests/cumulative request time: 173 / 109.192s
- Company elapsed time: 133.531s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 145 / 0 / 0
- Detail cache statuses: {'fetched:new': 129, 'fetched:missing_detail': 16}
- Relevant JD recovery: {'eligible': 91, 'usable_jd': 91}
- Raw jobs found: 493
- After US/location filtering: 145
- With trustworthy posted_date: 145
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.817, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 8.975, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 11.829, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 15.712, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 21.99, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 19.454, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 13.956, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 1.654, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 8.643, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 79}

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
    "fetched_at": "2026-11-05T15:40:23.137794+00:00",
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
    "fetched_at": "2026-11-05T15:40:23.137794+00:00",
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
    "fetched_at": "2026-11-05T15:40:23.137794+00:00",
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
    "fetched_at": "2026-11-05T15:40:23.137794+00:00",
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
    "fetched_at": "2026-11-05T15:40:23.137794+00:00",
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
- HTTP requests/cumulative request time: 50 / 17.246s
- Company elapsed time: 18.997s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 38 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 112
- After US/location filtering: 38
- With trustworthy posted_date: 38
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 7.689, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 22, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 1.359, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 0.997, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 2.388, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.296, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 1.127, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.566, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.633, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.94, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 27}

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
    "fetched_at": "2026-11-05T15:40:42.098531+00:00",
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
    "fetched_at": "2026-11-05T15:40:42.098531+00:00",
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
    "fetched_at": "2026-11-05T15:40:42.098531+00:00",
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
    "fetched_at": "2026-11-05T15:40:42.098531+00:00",
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
    "fetched_at": "2026-11-05T15:40:42.098531+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.299s
- Company elapsed time: 1.061s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 32, 'usable_jd': 32}
- Raw jobs found: 364
- After US/location filtering: 231
- With trustworthy posted_date: 231
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
    "fetched_at": "2026-11-05T15:40:56.227085+00:00",
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
    "fetched_at": "2026-11-05T15:40:56.227085+00:00",
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
    "fetched_at": "2026-11-05T15:40:56.227085+00:00",
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
    "fetched_at": "2026-11-05T15:40:56.227085+00:00",
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
    "fetched_at": "2026-11-05T15:40:56.227085+00:00",
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
- HTTP requests/cumulative request time: 129 / 20.358s
- Company elapsed time: 38.702s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 104 / 0 / 0
- Detail cache statuses: {'fetched:new': 103, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 30, 'usable_jd': 30}
- Raw jobs found: 224
- After US/location filtering: 104
- With trustworthy posted_date: 104
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.066, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.508, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.101, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 4.917, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 2.813, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.548, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.753, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.342, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.364, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR046034",
    "title": "Vice President - Java Lead for Investment Banking Advisory Technology",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800999790",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:40:57.288860+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR036109",
    "title": "Senior Java Developer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549797565648",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:40:57.288860+00:00",
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
    "fetched_at": "2026-11-05T15:40:57.288860+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR045730",
    "title": "Cloud & Digital Assets Platform Engineering Lead",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800830699",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:40:57.288860+00:00",
    "date_confidence": "high",
    "description": "Position Overview We are seeking a highly experienced Executive Director, Cloud Infrastructure & Digital Assets Platform Engineering, with deep hands-on AWS and GCP infrastructure "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR043635",
    "title": "Back-end Engineer - Data Platforms",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800249911",
    "posted_date": "2026-10-30",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:40:57.288860+00:00",
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
- HTTP requests/cumulative request time: 116 / 39.547s
- Company elapsed time: 57.428s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 87 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 29, 'usable_jd': 29}
- Raw jobs found: 435
- After US/location filtering: 87
- With trustworthy posted_date: 87
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 20.541, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.183, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 6.815, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 9.503, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.691, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.893, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.636, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.649, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.518, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

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
    "fetched_at": "2026-11-05T15:41:00.715033+00:00",
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
    "fetched_at": "2026-11-05T15:41:00.715033+00:00",
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
    "fetched_at": "2026-11-05T15:41:00.715033+00:00",
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
    "fetched_at": "2026-11-05T15:41:00.715033+00:00",
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
    "fetched_at": "2026-11-05T15:41:00.715033+00:00",
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
- HTTP requests/cumulative request time: 9 / 1.881s
- Company elapsed time: 2.888s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 37 / 35
- Detail cache statuses: {'reused': 19, 'reuse_after_error:stale': 18}
- Relevant JD recovery: {'deterministic_skip': 8, 'cache_reused': 37, 'eligible': 19, 'ai_skip': 27, 'usable_jd': 19}
- Raw jobs found: 90
- After US/location filtering: 54
- With trustworthy posted_date: 54
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.46, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.334, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.272, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.306, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.263, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.327, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.335, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.315, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.276, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}

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
    "fetched_at": "2026-11-05T15:41:01.097881+00:00",
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
    "fetched_at": "2026-11-05T15:41:01.097881+00:00",
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
    "fetched_at": "2026-11-05T15:41:01.097881+00:00",
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
    "fetched_at": "2026-11-05T15:41:01.097881+00:00",
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
    "fetched_at": "2026-11-05T15:41:01.097881+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.435s
- Company elapsed time: 2.024s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 349, 'usable_jd': 349}
- Raw jobs found: 814
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
    "fetched_at": "2026-11-05T15:41:03.987146+00:00",
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
    "fetched_at": "2026-11-05T15:41:03.987146+00:00",
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
    "fetched_at": "2026-11-05T15:41:03.987146+00:00",
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
    "fetched_at": "2026-11-05T15:41:03.987146+00:00",
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
    "fetched_at": "2026-11-05T15:41:03.987146+00:00",
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
- HTTP requests/cumulative request time: 1 / 2.853s
- Company elapsed time: 3.171s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 2 / 2
- Detail cache statuses: {'reuse_after_error:stale': 2}
- Relevant JD recovery: {'eligible': 186, 'cache_reused': 2, 'ai_skip': 2, 'usable_jd': 186}
- Raw jobs found: 307
- After US/location filtering: 244
- With trustworthy posted_date: 244
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
    "fetched_at": "2026-11-05T15:41:06.014357+00:00",
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
    "fetched_at": "2026-11-05T15:41:06.014357+00:00",
    "date_confidence": "high",
    "description": "Architecting, developing, and maintaining high-performance, scalable backend services that underpin our our operational data and AI systems Maintaining high coding standards throug"
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
    "fetched_at": "2026-11-05T15:41:06.014357+00:00",
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
    "fetched_at": "2026-11-05T15:41:06.014357+00:00",
    "date_confidence": "high",
    "description": "Build for high-scale, collaborative, geospatial workflows ( Gaia ) Design sophisticated frameworks to enable complex workflows across applications in a single workspace Develop the"
  },
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "d33e0c31-ac7e-4f57-ba74-36f2df6ae2f5",
    "title": "Backend Software Engineer - Defense",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/palantir/d33e0c31-ac7e-4f57-ba74-36f2df6ae2f5",
    "posted_date": "2025-02-24",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:41:06.014357+00:00",
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
- HTTP requests/cumulative request time: 80 / 14.827s
- Company elapsed time: 26.107s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 59 / 0 / 0
- Detail cache statuses: {'fetched:new': 58, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 177
- After US/location filtering: 59
- With trustworthy posted_date: 59
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.046, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.166, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 1.351, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 2.573, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 2.631, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.026, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.241, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 0.552, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.258, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138582",
    "title": "Data Scientist Intern - Summer 2027",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922982821",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:41:09.189281+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138583",
    "title": "Mobile Engineer Intern - Summer 2027",
    "location": "San Jose, California, United States of America; Chicago, Illinois, United States of America; Omaha, Nebraska, United States of America; Scottsdale, Arizona, United States of America; Austin, Texas, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922982818",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:41:09.189281+00:00",
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
    "fetched_at": "2026-11-05T15:41:09.189281+00:00",
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
    "fetched_at": "2026-11-05T15:41:09.189281+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138553",
    "title": "Staff Machine Learning Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923137313",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:41:09.189281+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.186s
- Company elapsed time: 0.784s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 17, 'usable_jd': 17}
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
    "fetched_at": "2026-11-05T15:41:33.410131+00:00",
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
    "fetched_at": "2026-11-05T15:41:33.410131+00:00",
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
    "fetched_at": "2026-11-05T15:41:33.410131+00:00",
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
    "fetched_at": "2026-11-05T15:41:33.410131+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8049518",
    "title": "Client Account Manager, Large Customer Sales (Tech)",
    "location": "Los Angeles, CA; San Francisco, CA; San Francisco, CA, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8049518",
    "posted_date": "2026-09-09",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-05T15:41:33.410131+00:00",
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
- HTTP requests/cumulative request time: 41 / 13.732s
- Company elapsed time: 17.859s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 29 / 0 / 0
- Detail cache statuses: {'fetched:new': 26, 'fetched:stale': 1, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 15, 'usable_jd': 15}
- Raw jobs found: 83
- After US/location filtering: 29
- With trustworthy posted_date: 29
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 6.646, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.652, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.8, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 6.75, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 0.432, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.425, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.461, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.398, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.753, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 19}

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
    "fetched_at": "2026-11-05T15:41:34.194897+00:00",
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
    "fetched_at": "2026-11-05T15:41:34.194897+00:00",
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
    "fetched_at": "2026-11-05T15:41:34.194897+00:00",
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
    "fetched_at": "2026-11-05T15:41:34.194897+00:00",
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
    "fetched_at": "2026-11-05T15:41:34.194897+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.120s
- Company elapsed time: 0.456s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 90
- After US/location filtering: 73
- With trustworthy posted_date: 73
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
    "fetched_at": "2026-11-05T15:41:35.297947+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.297947+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.297947+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.297947+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.297947+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.161s
- Company elapsed time: 0.966s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 198
- After US/location filtering: 180
- With trustworthy posted_date: 180
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
    "fetched_at": "2026-11-05T15:41:35.755315+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.755315+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.755315+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.755315+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.755315+00:00",
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
- HTTP requests/cumulative request time: 59 / 78.419s
- Company elapsed time: 88.126s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 42 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 42}
- Relevant JD recovery: {'eligible': 37, 'usable_jd': 37}
- Raw jobs found: 117
- After US/location filtering: 42
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 21.377, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 13.952, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 2.609, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 6.815, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 24.357, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.614, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.39, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.982, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 9.031, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 34, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 34}

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
    "fetched_at": "2026-11-05T15:41:35.998063+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.998063+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.998063+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.998063+00:00",
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
    "fetched_at": "2026-11-05T15:41:35.998063+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.237s
- Company elapsed time: 1.077s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 52, 'usable_jd': 52}
- Raw jobs found: 337
- After US/location filtering: 271
- With trustworthy posted_date: 271
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
    "fetched_at": "2026-11-05T15:41:36.722331+00:00",
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
    "fetched_at": "2026-11-05T15:41:36.722331+00:00",
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
    "fetched_at": "2026-11-05T15:41:36.722331+00:00",
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
    "fetched_at": "2026-11-05T15:41:36.722331+00:00",
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
    "fetched_at": "2026-11-05T15:41:36.722331+00:00",
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
- HTTP requests/cumulative request time: 153 / 74.863s
- Company elapsed time: 95.824s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 129 / 0 / 0
- Detail cache statuses: {'fetched:new': 129}
- Relevant JD recovery: {'eligible': 31, 'usable_jd': 31}
- Raw jobs found: 360
- After US/location filtering: 129
- With trustworthy posted_date: 129
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 36.359, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.312, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 8.921, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 16.87, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.465, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.305, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.226, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 1.367, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 4.251, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088549W",
    "title": "Software Engineer",
    "location": "US - Foster City, CA; US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Software-Engineer_REF088549W",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:41:37.800471+00:00",
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
    "fetched_at": "2026-11-05T15:41:37.800471+00:00",
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
    "fetched_at": "2026-11-05T15:41:37.800471+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF090054W",
    "title": "Sr. Manager, Strategic Planning",
    "location": "US - San Francisco, CA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---San-Francisco-CA/Sr-Manager--Strategic-Planning_REF090054W",
    "posted_date": "2026-11-03",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:41:37.800471+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF089838W",
    "title": "Staff SW Engineer - Performance Engineering",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Staff-SW-Engineer---Performance-Engineering_REF089838W",
    "posted_date": "2026-11-02",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:41:37.800471+00:00",
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
- HTTP requests/cumulative request time: 1 / 15.687s
- Company elapsed time: 15.698s
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
    "fetched_at": "2026-11-05T15:41:52.054872+00:00",
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
    "fetched_at": "2026-11-05T15:41:52.054872+00:00",
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
    "fetched_at": "2026-11-05T15:41:52.054872+00:00",
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
    "fetched_at": "2026-11-05T15:41:52.054872+00:00",
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
    "fetched_at": "2026-11-05T15:41:52.054872+00:00",
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
- HTTP requests/cumulative request time: 140 / 94.261s
- Company elapsed time: 113.904s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 116 / 0 / 0
- Detail cache statuses: {'fetched:new': 114, 'fetched:changed': 1, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 20, 'usable_jd': 20}
- Raw jobs found: 437
- After US/location filtering: 116
- With trustworthy posted_date: 116
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 48.046, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 76, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 3.359, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 2.624, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 19.665, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.269, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.098, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.76, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.865, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 10.86, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 80}

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
    "fetched_at": "2026-11-05T15:41:58.144117+00:00",
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
    "fetched_at": "2026-11-05T15:41:58.144117+00:00",
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
    "fetched_at": "2026-11-05T15:41:58.144117+00:00",
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
    "fetched_at": "2026-11-05T15:41:58.144117+00:00",
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
    "fetched_at": "2026-11-05T15:41:58.144117+00:00",
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
- HTTP requests/cumulative request time: 65 / 29.951s
- Company elapsed time: 38.396s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 49 / 0 / 0
- Detail cache statuses: {'fetched:new': 49}
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 213
- After US/location filtering: 49
- With trustworthy posted_date: 49
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.533, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 0.754, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.768, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 1.903, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 3.539, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.537, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.739, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 1.083, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.707, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}

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
    "fetched_at": "2026-11-05T15:42:07.754590+00:00",
    "date_confidence": "high",
    "description": "About the team The Mercury Mobile team builds Zillow Instant Messaging (ZIM) — the conversation layer where millions of movers participate in a multiplayer, integrated experience t"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751548",
    "title": "Senior Fullstack Engineer, Mortgage Fulfillment AI",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Senior-Fullstack-Engineer--Mortgage-Fulfillment-AI_P751548-2",
    "posted_date": "2026-10-20",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:42:07.754590+00:00",
    "date_confidence": "high",
    "description": "About the team You’ll join a close-knit engineering team in Zillow Home Loans Fulfillment who know our loan origination system in depth. Fulfillment covers the mortgage journey fro"
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
    "fetched_at": "2026-11-05T15:42:07.754590+00:00",
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
    "fetched_at": "2026-11-05T15:42:07.754590+00:00",
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
    "fetched_at": "2026-11-05T15:42:07.754590+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.283s
- Company elapsed time: 1.151s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 13, 'usable_jd': 13}
- Raw jobs found: 370
- After US/location filtering: 223
- With trustworthy posted_date: 223
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
    "fetched_at": "2026-11-05T15:42:36.670335+00:00",
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
    "fetched_at": "2026-11-05T15:42:36.670335+00:00",
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
    "fetched_at": "2026-11-05T15:42:36.670335+00:00",
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
    "fetched_at": "2026-11-05T15:42:36.670335+00:00",
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
    "fetched_at": "2026-11-05T15:42:36.670335+00:00",
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
- HTTP requests/cumulative request time: 12 / 6.413s
- Company elapsed time: 6.663s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 2 / 0 / 0
- Detail cache statuses: {'fetched:new': 2}
- Relevant JD recovery: {'eligible': 2, 'usable_jd': 2}
- Raw jobs found: 10
- After US/location filtering: 2
- With trustworthy posted_date: 2
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.893, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.484, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.48, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.473, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.469, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.48, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.744, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.501, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.505, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}

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
    "fetched_at": "2026-11-05T15:42:37.822406+00:00",
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
    "fetched_at": "2026-11-05T15:42:37.822406+00:00",
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
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 147 / 98.522s
- Company elapsed time: 118.450s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 125 / 0 / 0
- Detail cache statuses: {'fetched:new': 123, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 17, 'usable_jd': 17}
- Raw jobs found: 382
- After US/location filtering: 125
- With trustworthy posted_date: 125
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 61.734, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.65, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 23, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 7.632, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 10.272, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.287, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.196, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.922, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 39, "stop_reason": "early_stop", "unique_contribution": 16, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 0.261, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 4.195, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1043845",
    "title": "Staff Software Development Engineer",
    "location": "TX - Work from home; Work At Home-Arkansas; Work At Home-Idaho; Work At Home-Georgia; Work At Home-Montana; Work At Home-Iowa; Work At Home-Wisconsin; Work At Home-Oregon; Work At Home-Washington; Work At Home-New York; Work At Home-District of Columbia; Work At Home-Connecticut; Work At Home-Nebraska; Work At Home-Rhode Island; Work At Home-Tennessee; Work At Home-Kentucky; Work At Home-Ohio; Work At Home-West Virginia; Work At Home-Maryland; Work At Home-Massachusetts; Work At Home-South Carolina; Work At Home-Missouri; Work At Home - Utah; Work At Home-Arizona; Work At Home-South Dakota; Work At Home-Pennsylvania; Work At Home-New Hampshire; Work At Home-Vermont; Work At Home-Minnesota; Work At Home-New Mexico; Work At Home-Michigan; Work At Home-California; Work At Home-Maine; Work At Home-North Dakota; Work At Home-Kansas; Work At Home-Indiana; Work At Home-New Jersey; Work At Home-Nevada; Work At Home-Louisiana; Work At Home-Mississippi; Work At Home-Oklahoma; Work At Home-Alabama; Work At Home-Virginia; Work At Home-Illinois; Work At Home-North Carolina; Work At Home-Colorado; Work At Home-Florida; Work At Home-Wyoming; Work At Home-Delaware",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/TX---Work-from-home/Staff-Software-Development-Engineer_R1043845",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:42:44.486281+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1082052",
    "title": "Senior Data Scientist - Risk Prediction Engine",
    "location": "NY - New York",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/NY---New-York/Senior-Data-Scientist---Risk-Prediction-Engine_R1082052",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:42:44.486281+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1015953",
    "title": "Principal Software Development Engineer (AI Innovation)",
    "location": "TX - Richardson",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/TX---Richardson/Principal-Software-Development-Engineer--AI-Innovation-_R1015953",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:42:44.486281+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1088562",
    "title": "Lead Director - Cloud & Platform Engineering (Health100)",
    "location": "",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/Lead-Director---Cloud---Platform-Engineering--Health100-_R1088562-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:42:44.486281+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1064241",
    "title": "Staff Software Development Engineer",
    "location": "IL - Work from home; Work At Home-Arkansas; Work At Home-Idaho; Work At Home-Texas; Work At Home-Georgia; Work At Home-Montana; Work At Home-Iowa; Work At Home-Wisconsin; Work At Home-Oregon; Work At Home-Washington; Work At Home-New York; Work At Home-District of Columbia; Work At Home-Connecticut; Work At Home-Nebraska; Work At Home-Rhode Island; Work At Home-Tennessee; Work At Home-Kentucky; Work At Home-Ohio; Work At Home-West Virginia; Work At Home-Maryland; Work At Home-Massachusetts; Work At Home-South Carolina; Work At Home-Missouri; Work At Home - Utah; Work At Home-Arizona; Work At Home-South Dakota; Work At Home-Pennsylvania; Work At Home-New Hampshire; Work At Home-Vermont; Work At Home-Minnesota; Work At Home-New Mexico; Work At Home-Michigan; Work At Home-California; Work At Home-Maine; Work At Home-North Dakota; Work At Home-Kansas; Work At Home-Indiana; Work At Home-New Jersey; Work At Home-Nevada; Work At Home-Louisiana; Work At Home-Mississippi; Work At Home-Oklahoma; Work At Home-Alabama; Work At Home-Virginia; Work At Home-North Carolina; Work At Home-Colorado; Work At Home-Florida; Work At Home-Wyoming; Work At Home-Delaware",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/IL---Work-from-home/Staff-Software-Development-Engineer_R1064241",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:42:44.486281+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.112s
- Company elapsed time: 0.260s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 55
- After US/location filtering: 47
- With trustworthy posted_date: 47
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
    "fetched_at": "2026-11-05T15:42:46.151574+00:00",
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
    "fetched_at": "2026-11-05T15:42:46.151574+00:00",
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
    "fetched_at": "2026-11-05T15:42:46.151574+00:00",
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
    "fetched_at": "2026-11-05T15:42:46.151574+00:00",
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
    "fetched_at": "2026-11-05T15:42:46.151574+00:00",
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
- HTTP requests/cumulative request time: 22 / 18.306s
- Company elapsed time: 26.051s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 5 / 67
- Detail cache statuses: {'reused': 5}
- Relevant JD recovery: {'deterministic_skip': 41, 'cache_reused': 5, 'eligible': 5, 'ai_skip': 26, 'usable_jd': 5}
- Raw jobs found: 329
- After US/location filtering: 72
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.412, "first_pass_survivors": 41, "group": "official", "jds_resolved": 0, "original_postings_resolved": 41, "page_budget": 2, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 2.746, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 2, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 39, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 1.5, "first_pass_survivors": 21, "group": "official", "jds_resolved": 0, "original_postings_resolved": 21, "page_budget": 2, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 28, "stop_reason": "early_stop", "unique_contribution": 21, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 1.023, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 2, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 6.897, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 2.727, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 2.536, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 2.993, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 3.217, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 40}

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
    "fetched_at": "2026-11-05T15:42:46.413056+00:00",
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
    "fetched_at": "2026-11-05T15:42:46.413056+00:00",
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
    "fetched_at": "2026-11-05T15:42:46.413056+00:00",
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
    "fetched_at": "2026-11-05T15:42:46.413056+00:00",
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
    "fetched_at": "2026-11-05T15:42:46.413056+00:00",
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
- HTTP requests/cumulative request time: 16 / 7.377s
- Company elapsed time: 8.756s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: {'fetched:new': 1}
- Relevant JD recovery: {'eligible': 1, 'usable_jd': 1}
- Raw jobs found: 123
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.469, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.543, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.46, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.42, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.223, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.106, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.468, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.387, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.13, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

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
    "fetched_at": "2026-11-05T15:43:04.125731+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.130s
- Company elapsed time: 0.360s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 53, 'usable_jd': 53}
- Raw jobs found: 113
- After US/location filtering: 99
- With trustworthy posted_date: 99
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
    "updated_date": "2026-10-15",
    "fetched_at": "2026-11-05T15:43:12.465394+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.465394+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.465394+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.465394+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.465394+00:00",
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
- HTTP requests/cumulative request time: 83 / 62.244s
- Company elapsed time: 73.157s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 63 / 0 / 0
- Detail cache statuses: {'fetched:new': 62, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 225
- After US/location filtering: 63
- With trustworthy posted_date: 63
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 33.453, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 2.406, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.009, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 15.1, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 39, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 10.404, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 56, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 3.503, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 46}
- Query diagnostic: {"elapsed_seconds": 1.135, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.229, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 3.733, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 37, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 37}

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
    "fetched_at": "2026-11-05T15:43:12.827240+00:00",
    "date_confidence": "high",
    "description": "Wells Fargo is seeking a Lead Ai Engineer in Technology as part of Commercial and Corporate & Investment Banking Technology (CCIBT).). The primary focus of this group will be to le"
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
    "fetched_at": "2026-11-05T15:43:12.827240+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.827240+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.827240+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking aspiring Data Engineers to join the 2027 Technology Internship Program. Program Overview: The Wells Fargo Technology Internship Program prov"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-580307",
    "title": "Software Engineering Manager",
    "location": "CHARLOTTE, NC; CHICAGO, IL",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Software-Engineering-Manager_R-580307",
    "posted_date": "2026-10-08",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:43:12.827240+00:00",
    "date_confidence": "high",
    "description": "Are you looking for more? Find it here. At Wells Fargo, we believe that a meaningful career is much more than just a job. It’s about finding all the elements that help you thrive, "
  }
]
```

## Yahoo

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ouryahoo.wd5.myworkdayjobs.com/careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 17
- HTTP requests/cumulative request time: 67 / 43.869s
- Company elapsed time: 52.785s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 49 / 0 / 0
- Detail cache statuses: {'fetched:new': 48, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 195
- After US/location filtering: 49
- With trustworthy posted_date: 49
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 37.081, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 0.887, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.733, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 2.223, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 3.082, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 47, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 47}
- Query diagnostic: {"elapsed_seconds": 2.675, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 0.677, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.781, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 3.796, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 21}

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
    "fetched_at": "2026-11-05T15:43:12.882961+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.882961+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.882961+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.882961+00:00",
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
    "fetched_at": "2026-11-05T15:43:12.882961+00:00",
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
- HTTP requests/cumulative request time: 24 / 9.588s
- Company elapsed time: 12.845s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 21 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 45
- After US/location filtering: 21
- With trustworthy posted_date: 21
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 12.845, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "Ansys", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 45}

Sample normalized records:

```json
[
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "100032391312",
    "title": "Academic/Outreach, Sr Associate",
    "location": "United States Off-site",
    "official_url": "https://careers.synopsys.com/job/canonsburg/academic-outreach-sr-associate/44408/100032391312",
    "posted_date": "2026-09-01",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:43:13.625823+00:00",
    "date_confidence": "high",
    "description": "We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling customers to rapidly innovate AI-powered products. We deliver industry-leading silicon desi"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "102570969840",
    "title": "Applications Engineer - Staff",
    "location": "Sunnyvale, California",
    "official_url": "https://careers.synopsys.com/job/sunnyvale/applications-engineer-staff/44408/102570969840",
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:43:13.625823+00:00",
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
    "fetched_at": "2026-11-05T15:43:13.625823+00:00",
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
    "fetched_at": "2026-11-05T15:43:13.625823+00:00",
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
    "fetched_at": "2026-11-05T15:43:13.625823+00:00",
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
- HTTP requests/cumulative request time: 121 / 81.867s
- Company elapsed time: 96.764s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 104 / 0 / 0
- Detail cache statuses: {'fetched:new': 104}
- Relevant JD recovery: {'eligible': 84, 'usable_jd': 84}
- Raw jobs found: 170
- After US/location filtering: 104
- With trustworthy posted_date: 104
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 26.966, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 27, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 1.505, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.633, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 5.329, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 28.886, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.284, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.654, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.254, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 23.737, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 57}

Sample normalized records:

```json
[
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD232832",
    "title": "Operations Trainer",
    "location": "USA, CA, Milpitas",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-CA-Milpitas/Operations-Trainer_WD232832",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:43:26.472151+00:00",
    "date_confidence": "high",
    "description": "Axiom builds the digital and electrical infrastructure powering the AI era. We design, build and deploy integrated power, thermal and compute solutions that help data centers, util"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD228347",
    "title": "Associate Production Supervisor (2nd shift)",
    "location": "USA, CA, Milpitas",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-CA-Milpitas/Associate-Production-Supervisor--2nd-shift-_WD228347",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:43:26.472151+00:00",
    "date_confidence": "high",
    "description": "Axiom builds the digital and electrical infrastructure powering the AI era. We design, build and deploy integrated power, thermal and compute solutions that help data centers, util"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD230655",
    "title": "Senior Applications Engineer",
    "location": "USA, VA, Henrico",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-VA-Henrico/Senior-Applications-Engineer_WD230655-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:43:26.472151+00:00",
    "date_confidence": "high",
    "description": "Anord Mardix, a Flex company, is a global leader in critical power solutions. With facilities around the globe, Anord Mardix leads in critical power infrastructure, supporting a my"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD233423",
    "title": "Building Wireman (1st Shift)",
    "location": "USA, CA, Fontana",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-CA-Fontana/Building-Wireman--1st-Shift-_WD233423-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:43:26.472151+00:00",
    "date_confidence": "high",
    "description": "Crown Technical Systems, a Flex Company, is a leader in power distribution and protection systems concentrating on sophisticated, state-of-the-art relay and control panels, medium "
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD233421",
    "title": "Sheet Metal Assembler (1st Shift)",
    "location": "USA, CA, Fontana",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-CA-Fontana/Sheet-Metal-Assembler--1st-Shift-_WD233421-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:43:26.472151+00:00",
    "date_confidence": "high",
    "description": "Crown Technical Systems, a Flex Company, is a leader in power distribution and protection systems concentrating on sophisticated, state-of-the-art relay and control panels, medium "
  }
]
```

## IQVIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://iqvia.wd1.myworkdayjobs.com/IQVIA`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 23 / 25.916s
- Company elapsed time: 27.534s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 13 / 0 / 0
- Detail cache statuses: {'fetched:new': 13}
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 42
- After US/location filtering: 13
- With trustworthy posted_date: 13
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.742, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.386, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.468, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 5.123, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 2.732, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 1.761, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 1.262, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.932, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.238, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}

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
    "fetched_at": "2026-11-05T15:43:52.049422+00:00",
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
    "fetched_at": "2026-11-05T15:43:52.049422+00:00",
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
    "fetched_at": "2026-11-05T15:43:52.049422+00:00",
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
    "fetched_at": "2026-11-05T15:43:52.049422+00:00",
    "date_confidence": "high",
    "description": "IQVIA Digital Overview: IQVIA Digital powers exceptional brand experiences, delivering innovative solutions based on a customer-first, insights-driven, and integrated omnichannel v"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1569482",
    "title": "Sr. Director IT, Specialty Labs",
    "location": "Durham, North Carolina, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Durham-North-Carolina-United-States-of-America/Sr-Director-IT--Specialty-Labs_R1569482-1",
    "posted_date": "2026-10-12",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:43:52.049422+00:00",
    "date_confidence": "high",
    "description": "The Senior Director, Specialty Labs Technology and Product Management serves as the senior technology and product leader for the IQVIA Specialty Labs portfolio which is made up of "
  }
]
```

## Johnson & Johnson

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://jj.wd5.myworkdayjobs.com/JJ`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 22
- HTTP requests/cumulative request time: 213 / 101.200s
- Company elapsed time: 129.888s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 190 / 0 / 0
- Detail cache statuses: {'fetched:new': 189, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 47, 'usable_jd': 47}
- Raw jobs found: 410
- After US/location filtering: 190
- With trustworthy posted_date: 190
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 33.266, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.652, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 37, "stop_reason": "early_stop", "unique_contribution": 19, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 29.097, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.299, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.429, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.423, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.94, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.235, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 5.891, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-109277",
    "title": "Sr Manager Strategic Capacity Management",
    "location": "Jacksonville, Florida, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Jacksonville-Florida-United-States-of-America/Sr-Manager-Strategic-Capacity-Management_R-109277-1",
    "posted_date": "2026-11-05",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:44:05.668687+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-108464",
    "title": "Manager, Supplier Quality, Drug Delivery Systems (DDS)",
    "location": "Malvern, Pennsylvania, United States of America; Horsham, Pennsylvania, United States of America; Raritan, New Jersey, United States of America; Titusville, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Malvern-Pennsylvania-United-States-of-America/Manager--Supplier-Quality--Drug-Delivery-Systems--DDS-_R-108464-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:44:05.668687+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-106190",
    "title": "Associate Director, Customer Master – Commercial Business Owner",
    "location": "Titusville, New Jersey, United States of America; Horsham, Pennsylvania, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Titusville-New-Jersey-United-States-of-America/Associate-Director--Customer-Master---Commercial-Business-Owner_R-106190-1",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:44:05.668687+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-107211",
    "title": "Senior Mechatronics Engineer",
    "location": "Santa Clara, California, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Santa-Clara-California-United-States-of-America/Senior-Mechatronics-Engineer_R-107211",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:44:05.668687+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-106544",
    "title": "Senior Manager Distribution Engineering & Technology",
    "location": "Raritan, New Jersey, United States of America; Memphis, Tennessee, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raritan-New-Jersey-United-States-of-America/Senior-Manager-Distribution-Engineering---Technology_R-106544-2",
    "posted_date": "2026-11-04",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:44:05.668687+00:00",
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
- HTTP requests/cumulative request time: 27 / 14.815s
- Company elapsed time: 16.916s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 17 / 0 / 0
- Detail cache statuses: {'fetched:new': 17}
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 75
- After US/location filtering: 17
- With trustworthy posted_date: 17
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 7.495, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.663, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.63, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.757, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.548, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 0.643, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.992, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 0.648, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.658, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 16}

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
    "fetched_at": "2026-11-05T15:44:19.584712+00:00",
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
    "fetched_at": "2026-11-05T15:44:19.584712+00:00",
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
    "fetched_at": "2026-11-05T15:44:19.584712+00:00",
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
    "fetched_at": "2026-11-05T15:44:19.584712+00:00",
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
    "fetched_at": "2026-11-05T15:44:19.584712+00:00",
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
- HTTP requests/cumulative request time: 2 / 16.869s
- Company elapsed time: 16.921s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 1 / 7 / 43
- Detail cache statuses: {'reused': 7}
- Relevant JD recovery: {'deterministic_skip': 37, 'eligible': 13, 'cache_reused': 7, 'ai_skip': 6, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 12}
- Raw jobs found: 79
- After US/location filtering: 73
- With trustworthy posted_date: 73
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
    "fetched_at": "2026-11-05T15:44:25.985787+00:00",
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
    "fetched_at": "2026-11-05T15:44:25.985787+00:00",
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
    "fetched_at": "2026-11-05T15:44:25.985787+00:00",
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
    "fetched_at": "2026-11-05T15:44:25.985787+00:00",
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
    "fetched_at": "2026-11-05T15:44:25.985787+00:00",
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
- HTTP requests/cumulative request time: 158 / 75.770s
- Company elapsed time: 96.068s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 137 / 0 / 0
- Detail cache statuses: {'fetched:new': 137}
- Relevant JD recovery: {'eligible': 54, 'usable_jd': 54}
- Raw jobs found: 225
- After US/location filtering: 137
- With trustworthy posted_date: 137
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 14.208, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 25, "stop_reason": "early_stop", "unique_contribution": 23, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 2.347, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 1.266, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 17.046, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 24.764, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.142, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 2.719, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.955, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 24.535, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 80}

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
    "fetched_at": "2026-11-05T15:44:36.502248+00:00",
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
    "fetched_at": "2026-11-05T15:44:36.502248+00:00",
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
    "fetched_at": "2026-11-05T15:44:36.502248+00:00",
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
    "fetched_at": "2026-11-05T15:44:36.502248+00:00",
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
    "fetched_at": "2026-11-05T15:44:36.502248+00:00",
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
- HTTP requests/cumulative request time: 45 / 22.118s
- Company elapsed time: 27.250s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 29 / 0 / 0
- Detail cache statuses: {'fetched:new': 27, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 134
- After US/location filtering: 29
- With trustworthy posted_date: 29
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 15.083, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 26, "stop_reason": "early_stop", "unique_contribution": 26, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 0.681, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.158, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.214, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 3.31, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 0.524, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 2.965, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 0.81, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.719, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 12}

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
    "fetched_at": "2026-11-05T15:44:42.688059+00:00",
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
    "fetched_at": "2026-11-05T15:44:42.688059+00:00",
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
    "fetched_at": "2026-11-05T15:44:42.688059+00:00",
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
    "fetched_at": "2026-11-05T15:44:42.688059+00:00",
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
    "fetched_at": "2026-11-05T15:44:42.688059+00:00",
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
- HTTP requests/cumulative request time: 109 / 58.541s
- Company elapsed time: 73.416s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 85 / 0 / 0
- Detail cache statuses: {'fetched:new': 81, 'fetched:missing_detail': 3, 'reuse_after_error:missing_detail': 1}
- Relevant JD recovery: {'eligible': 45, 'ai_recover': 1, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 44}
- Raw jobs found: 313
- After US/location filtering: 85
- With trustworthy posted_date: 84
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 31.879, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 4.953, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 3.143, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 9.718, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 9.222, "first_pass_survivors": 13, "group": "official", "jds_resolved": 12, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 3.436, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 0.677, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.637, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 6.428, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 50, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 50}

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
    "fetched_at": "2026-11-05T15:44:42.938061+00:00",
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
    "fetched_at": "2026-11-05T15:44:42.938061+00:00",
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
    "fetched_at": "2026-11-05T15:44:42.938061+00:00",
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
    "fetched_at": "2026-11-05T15:44:42.938061+00:00",
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
    "fetched_at": "2026-11-05T15:44:42.938061+00:00",
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
- HTTP requests/cumulative request time: 25 / 5.803s
- Company elapsed time: 6.087s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 19 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 44
- After US/location filtering: 19
- With trustworthy posted_date: 19
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.531, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.427, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 1.528, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 2.685, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.291, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.627, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}

Sample normalized records:

```json
[
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1102685",
    "title": "Senior Engineer - Java Full Stack",
    "location": "Temple Terrace, Florida; Irving, Texas; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1102685/senior-engineer-java-full-stack/",
    "posted_date": "2026-10-21",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:45:03.237738+00:00",
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
    "fetched_at": "2026-11-05T15:45:03.237738+00:00",
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
    "fetched_at": "2026-11-05T15:45:03.237738+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1101033",
    "title": "AI Workflow Engineer",
    "location": "Basking Ridge, New Jersey; Irving, Texas",
    "official_url": "https://mycareer.verizon.com/jobs/r-1101033/ai-workflow-engineer/",
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:45:03.237738+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1102758",
    "title": "Data Science Consultant",
    "location": "Basking Ridge, New Jersey; Alpharetta, Georgia",
    "official_url": "https://mycareer.verizon.com/jobs/r-1102758/data-science-consultant/",
    "posted_date": "2026-10-27",
    "updated_date": "",
    "fetched_at": "2026-11-05T15:45:03.237738+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.185s
- Company elapsed time: 0.248s
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
    "fetched_at": "2026-11-05T15:45:09.326215+00:00",
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
    "fetched_at": "2026-11-05T15:45:09.326215+00:00",
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
    "fetched_at": "2026-11-05T15:45:09.326215+00:00",
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
    "fetched_at": "2026-11-05T15:45:09.326215+00:00",
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
    "fetched_at": "2026-11-05T15:45:09.326215+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
