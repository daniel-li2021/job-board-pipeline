# Official careers scrape report — 2026-10-05_2331

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Runtime metrics

- Wall time: 927.055s
- HTTP requests/cumulative request time: 7247 / 3043.754s
- Listing pages/detail fetched/cache reused/prefilter skipped: 1292 / 5912 / 265 / 728
- Detail cache statuses: {'fetched:missing_detail': 132, 'fetched:new': 5542, 'missing:new': 3, 'reuse_after_error:missing_detail': 2, 'reused': 265}
- Relevant JD coverage: 5336 / 5417; added detail requests 83 / 150; deferred 0

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 43
- HTTP requests/cumulative request time: 43 / 12.986s
- Company elapsed time: 29.271s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 133, 'usable_jd': 133}
- Raw jobs found: 818
- After US/location filtering: 269
- With trustworthy posted_date: 269
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.53, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "\"Ai Engineer\"", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.151, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Machine Learning Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.23, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Data Scientist\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.234, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "\"Solutions Architect\"", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.233, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "\"Data Engineer\"", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 2.154, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "\"Platform Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.165, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Full Stack Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.082, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "\"Forward Deployed Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.888, "first_pass_survivors": 95, "group": "official", "jds_resolved": 95, "original_postings_resolved": 95, "page_budget": 12, "pages_fetched": 9, "query": "\"Software Engineer\"", "raw_jobs": 180, "stop_reason": "early_stop", "unique_contribution": 95, "unique_jobs": 180}
- Query diagnostic: {"elapsed_seconds": 2.228, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Infrastructure Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.334, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 5, "pages_fetched": 4, "query": "\"Software Engineer III\"", "raw_jobs": 71, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 71}
- Query diagnostic: {"elapsed_seconds": 1.469, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "\"Web Solutions Engineer\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 1.572, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 2, "pages_fetched": 2, "query": "\"DeepMind\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "78416022054281926",
    "title": "Software Engineer III, Google Cloud Storage, Infrastructure",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/78416022054281926-software-engineer-iii-google-cloud-storage-infrastructure",
    "posted_date": "2026-10-05",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:31:08.577183+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "137322632390288070",
    "title": "Software Engineer, AI/ML, Shopping Relevance Models",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/137322632390288070-software-engineer-ai-ml-shopping-relevance-models",
    "posted_date": "2026-10-05",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:31:08.577183+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "122998194903622342",
    "title": "Senior Software Engineer, Agentic AI Systems, Google Cloud Security",
    "location": "San Francisco, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/122998194903622342-senior-software-engineer-agentic-ai-systems-google-cloud-security",
    "posted_date": "2026-10-05",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:31:08.577183+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "82369041234043590",
    "title": "Software Engineer, Google Health, Nutrition",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/82369041234043590-software-engineer-google-health-nutrition",
    "posted_date": "2026-10-05",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:31:08.577183+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "113403444122788550",
    "title": "Senior Software Engineer, Google Cloud Kubernetes Networking",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/113403444122788550-senior-software-engineer-google-cloud-kubernetes-networking",
    "posted_date": "2026-10-05",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:31:08.577183+00:00",
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
- Pages/requests fetched: 44
- HTTP requests/cumulative request time: 44 / 14.411s
- Company elapsed time: 27.315s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 457, 'usable_jd': 457}
- Raw jobs found: 809
- After US/location filtering: 710
- With trustworthy posted_date: 710
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.541, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 1.507, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 1.848, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.049, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.934, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.74, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 0.272, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.278, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 7.902, "first_pass_survivors": 209, "group": "official", "jds_resolved": 209, "original_postings_resolved": 209, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 209, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.75, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.135, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "systems development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.196, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.164, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 2, "pages_fetched": 2, "query": "applied scientist", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10569497",
    "title": "Sr. Software Dev Engineer, AI Security",
    "location": "New York, New York, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10569497/sr-software-dev-engineer-ai-security",
    "posted_date": "2026-10-05",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:31:08.578018+00:00",
    "date_confidence": "high",
    "description": "We are looking for a Senior Software Development Engineer who thrives at the forefront of technology, science, and security to join Artificial Intelligence Security (AISec), workin"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10568156",
    "title": "Software Development Engineer, AWS Agentic AI",
    "location": "Bellevue, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10568156/software-development-engineer-aws-agentic-ai",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:31:08.578018+00:00",
    "date_confidence": "high",
    "description": "Come shape the future with us! As a major Agentic AI agent creation and execution provider, our technology powers many of Amazon's internal organizations via AgentZ and external or"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10567360",
    "title": "Software Development Engineer – AI/ML Networking Disaggregated Inference, Annapurna Labs , Elastic Collectives",
    "location": "Cupertino, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10567360/software-development-engineer-ai-ml-networking-disaggregated-inference-annapurna-labs-elastic-collectives",
    "posted_date": "2026-10-01",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:31:08.578018+00:00",
    "date_confidence": "high",
    "description": "Every token a large language model generates depends on data reaching the right accelerator at the right moment. As AI models outgrow any single chip, the network between accelerat"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10567905",
    "title": "Senior Security Engineer, AI & AGI Security",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10567905/senior-security-engineer-ai-agi-security",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:31:08.578018+00:00",
    "date_confidence": "high",
    "description": "Come join Earth's most customer-centric company! Amazon is looking for an AI Security Engineer with strong insight and passion for security to ensure our AI applications are design"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10566212",
    "title": "Software Development Engineer, Agentic AI",
    "location": "Jersey City, New Jersey, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10566212/software-development-engineer-agentic-ai",
    "posted_date": "2026-10-01",
    "updated_date": "2026-09-30",
    "fetched_at": "2026-10-05T23:31:08.578018+00:00",
    "date_confidence": "high",
    "description": "Interested in building the future of intelligent AI agents? The Agentic AI organization at AWS is on a mission to empower developers and enterprises to store and retrieve memory fo"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=ai+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 16.290s
- Company elapsed time: 31.457s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 186, 'usable_jd': 186}
- Raw jobs found: 840
- After US/location filtering: 284
- With trustworthy posted_date: 284
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.591, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.346, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.326, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.28, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.166, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.117, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.29, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.223, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.859, "first_pass_survivors": 117, "group": "official", "jds_resolved": 117, "original_postings_resolved": 117, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 117, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.258, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "apps-and-frameworks-SFTWR-AF", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200687353-0836",
    "title": "Software Engineer, Apple Intelligence Model Platform",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200687353/software-engineer-apple-intelligence-model-platform",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.578472+00:00",
    "date_confidence": "high",
    "description": "The Proactive Intelligence Platform is at the heart of an intelligent system experience that understands you and anticipates your needs. We are building an on-device personal and c"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200686858-3956",
    "title": "ASIC Design Engineering Lead - SoC IP DMA",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200686858/asic-design-engineering-lead-soc-ip-dma",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.578472+00:00",
    "date_confidence": "high",
    "description": "In this highly visible, hands-on role, you will lead a team of engineers at the center of Apple's SOC IP DMA design effort. Balancing equal parts people management and technical le"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200687250-0157",
    "title": "Apple Business Commercial Channel Account Executive",
    "location": "Austin, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200687250/apple-business-commercial-channel-account-executive",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.578472+00:00",
    "date_confidence": "high",
    "description": "The people here at Apple don't just create products — they create the kind of wonder that's revolutionized entire industries. It's the diversity of those people and their ideas tha"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200681793-0157",
    "title": "Partnership Development Lead - Health",
    "location": "Austin, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200681793/partnership-development-lead-health",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.578472+00:00",
    "date_confidence": "high",
    "description": "The Health team is seeking a senior leader to take end-to-end accountability for the partner-dependent tracks of our most critical health initiatives. In this role, you will own th"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200687345-0836",
    "title": "Product Design Producer, Find My",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200687345/product-design-producer-find-my",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.578472+00:00",
    "date_confidence": "high",
    "description": "At Apple great ideas have a way of becoming great products, services, and customer experiences. We believe design matters and are passionate about providing high quality services t"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 235 / 52.982s
- Company elapsed time: 87.283s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 195 / 0 / 0
- Detail cache statuses: {'fetched:new': 181, 'fetched:missing_detail': 14}
- Relevant JD recovery: {'eligible': 53, 'usable_jd': 53}
- Raw jobs found: 390
- After US/location filtering: 195
- With trustworthy posted_date: 195
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 24.001, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 6.017, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 11.524, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.736, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.566, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.202, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.753, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.615, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 23.639, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 120}

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200059541",
    "title": "Senior Software Engineer",
    "location": "United States, Washington, Redmond; United States, Georgia, Atlanta; United States, Texas, San Antonio; United States, District of Columbia, Washington D.C.; United States, Arizona, Phoenix",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557023012",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.579779+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Cloud Operations + Innovation is the team behind the infrastructure that powers Microsoft’s cloud. Within the organization, our engineering teams build secure, s"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200059649",
    "title": "GPU Deployment Execution Program Manager",
    "location": "United States, Washington, Redmond; United States, Texas, San Antonio; United States, Arizona, Phoenix; United States, Georgia, Atlanta; United States, District of Columbia, Washington D.C.",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557023188",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.579779+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft’s Cloud Operations & Innovation (CO+I) powers our cloud services and supports over 1 billion customers and 20 million businesses in 90+ countries. With over 100 "
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200059833",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557024062",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.579779+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft 365(M365) Intelligent Conversation and Communications Cloud is the platform that powers billions of real-time customer conversations across Teams, Skype, Dynamic"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200059341",
    "title": "Software Engineer II - MBO",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557022479",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.579779+00:00",
    "date_confidence": "high",
    "description": "Overview Most people experience Microsoft through products like Windows, Office, Xbox, Azure, and Copilot. Behind each of those experiences are the platforms, systems, and operatio"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200058587",
    "title": "Principal Optical Network System Engineer",
    "location": "United States, California, Mountain View; United States, Washington, Redmond; United States, Oregon, Hillsboro",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557016442",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.579779+00:00",
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
- HTTP requests/cumulative request time: 503 / 225.336s
- Company elapsed time: 291.821s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 470 / 0 / 0
- Detail cache statuses: {'fetched:new': 460, 'fetched:missing_detail': 9, 'reuse_after_error:missing_detail': 1}
- Relevant JD recovery: {'eligible': 79, 'ai_recover': 1, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 78}
- Raw jobs found: 640
- After US/location filtering: 470
- With trustworthy posted_date: 469
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 45.742, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 35.753, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 24.739, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 31.753, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 24.904, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 25.786, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 21.351, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.354, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 41.484, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 17.223, "first_pass_survivors": 33, "group": "official", "jds_resolved": 32, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2026233",
    "title": "AI Engineering Manager - Finance",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/AI-Engineering-Manager---Finance_JR2026233",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.581450+00:00",
    "date_confidence": "high",
    "description": "NVIDIA has been transforming computer graphics, PC gaming, and accelerated computing for more than 25 years. It’s a unique legacy of innovation that’s fueled by great technology—an"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2019190",
    "title": "Applied AI Engineer - VLSI Design",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Applied-AI-Engineer---VLSI-Design_JR2019190",
    "posted_date": "2026-08-17",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.581450+00:00",
    "date_confidence": "high",
    "description": "NVIDIA has been transforming computer graphics, PC gaming, and accelerated computing for more than 25 years. It’s a unique legacy of innovation that’s fueled by great technology—an"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2020550",
    "title": "Senior SOCD Applied AI Engineer",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-SOCD-Applied-AI-Engineer_JR2020550",
    "posted_date": "2026-09-02",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.581450+00:00",
    "date_confidence": "high",
    "description": "Nvidia's SOC Design (SOCD) team is looking for an Applied AI Engineer who is passionate about eliminating bottlenecks in SOC integration workflows through intelligent automation. I"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2025164",
    "title": "Senior High Performance AI Engineer, Agentic AI",
    "location": "US, CA, Santa Clara; US, GA, Remote; US, TX, Austin; US, TX, Remote; US, CA, Remote; US, WA, Redmond",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-High-Performance-AI-Engineer--Agentic-AI_JR2025164",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.581450+00:00",
    "date_confidence": "high",
    "description": "We are looking for outstanding Senior High Performance AI Engineers to build the next generation of agentic AI systems for the CUDA ecosystem. Our team works across the full agenti"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2025163",
    "title": "Senior Context Fusion AI Engineer - Autonomous Vehicles",
    "location": "US, CA, Santa Clara; US, NV, Remote; US, WA, Redmond; US, WA, Seattle",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Context-Fusion-AI-Engineer---Autonomous-Vehicles_JR2025163",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:08.581450+00:00",
    "date_confidence": "high",
    "description": "We are looking for a strong engineer to join the DRIVE Road Structure / Online Mapping / Context Fusion team. In this role, you will help craft and guide the future of our L3/L4 au"
  }
]
```

## Salesforce

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://salesforce.wd12.myworkdayjobs.com/External_Career_Site`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 190 / 57.552s
- Company elapsed time: 83.760s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 163 / 0 / 0
- Detail cache statuses: {'fetched:new': 159, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 43, 'usable_jd': 43}
- Raw jobs found: 438
- After US/location filtering: 163
- With trustworthy posted_date: 163
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 31.631, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 76, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 3.381, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 3.285, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 10.283, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.124, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.092, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.113, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 7.833, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 10.677, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 1.792, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "software engineering mts", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 13}

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR347388",
    "title": "Data Engineer (SMTS / LMTS) - MDM",
    "location": "California - San Francisco; New York - New York; Washington - Seattle; Indiana - Indianapolis",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Data-Engineer--SMTS---LMTS----MDM_JR347388",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:35.893804+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR362775",
    "title": "Director, AgentExchange Security & Labs",
    "location": "California - San Francisco; Illinois - Chicago; New York - New York; Georgia - Atlanta",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Director--AgentExchange-Security---Labs_JR362775",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:35.893804+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Product Job Details"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR354316",
    "title": "Technical Architect",
    "location": "Ohio - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Ohio---Remote/Technical-Architect_JR354316",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:35.893804+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Customer Success Jo"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR360283",
    "title": "Customer Success Manager, Director - Retail",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Customer-Success-Manager--Director---Retail_JR360283-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:35.893804+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Customer Success Jo"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR349609",
    "title": "Software Engineering MTS",
    "location": "Washington - Bellevue; Virginia - Mclean; California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Washington---Bellevue/Software-Engineering-MTS_JR349609",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:35.893804+00:00",
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
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 191 / 77.707s
- Company elapsed time: 105.541s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 158 / 0 / 0
- Detail cache statuses: {'fetched:new': 157, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 49, 'usable_jd': 49}
- Raw jobs found: 548
- After US/location filtering: 158
- With trustworthy posted_date: 158
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 41.991, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 11.233, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 6.354, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 16.888, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.247, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.674, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.848, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 4.916, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 5.935, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 3.659, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}

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
    "fetched_at": "2026-10-05T23:31:37.848706+00:00",
    "date_confidence": "high",
    "description": "We build the agentic AI platform that Adobe teams use to get real work done — OneAI , our unified intelligence layer, along with the reusable skills, agents, and dashboards that ru"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R171752",
    "title": "Sr. Applied AI Engineer",
    "location": "San Francisco",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Francisco/Sr-Applied-AI-Engineer_R171752",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:37.848706+00:00",
    "date_confidence": "high",
    "description": "The Opportunity The GTM Agentic AI Operations team is leading the shift to an Agentic operating model for Adobe GTM and Sales. This function is the orchestration layer that operati"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170387",
    "title": "Senior AI/ DevOps Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Job-Posting-Title-AI--DevOps-Engineer_R170387-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:37.848706+00:00",
    "date_confidence": "high",
    "description": "Senior SRE — RTCDP Datastores & AI/ML Ops Adobe’s Real-Time Customer Data Platform (RTCDP) powers personalized experiences for some of the world’s largest brands. As a Senior SRE o"
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
    "fetched_at": "2026-10-05T23:31:37.848706+00:00",
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
    "fetched_at": "2026-10-05T23:31:37.848706+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are looking for a Senior AI Systems Engineer with deep C++ expertise to help build the next generation of AI-enabled product and platform capabilities. This role"
  }
]
```

## Meta

- Status: ok
- Scraping method: HTTP POST Meta Relay GraphQL; dynamic LSD and doc_id discovery
- Search URL/API: `https://www.metacareers.com/jobsearch/`
- Pagination: one complete Relay payload per role query
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 61 / 35.963s
- Company elapsed time: 36.917s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 48 / 163 / 476
- Detail cache statuses: {'reused': 163}
- Relevant JD recovery: {'cache_reused': 163, 'eligible': 211, 'deterministic_skip': 320, 'ai_skip': 156, 'ai_recover': 12, 'detail_requests': 48, 'detail_failure': 48, 'budget_deferred': 0, 'usable_jd': 163}
- Raw jobs found: 2239
- After US/location filtering: 687
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.713, "first_pass_survivors": 417, "group": "official", "jds_resolved": 0, "original_postings_resolved": 417, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 511, "stop_reason": "page_budget", "unique_contribution": 417, "unique_jobs": 511}
- Query diagnostic: {"elapsed_seconds": 0.424, "first_pass_survivors": 25, "group": "official", "jds_resolved": 0, "original_postings_resolved": 25, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 0.48, "first_pass_survivors": 37, "group": "official", "jds_resolved": 0, "original_postings_resolved": 37, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 117, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 117}
- Query diagnostic: {"elapsed_seconds": 0.46, "first_pass_survivors": 27, "group": "official", "jds_resolved": 0, "original_postings_resolved": 27, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 168, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 168}
- Query diagnostic: {"elapsed_seconds": 0.659, "first_pass_survivors": 142, "group": "official", "jds_resolved": 0, "original_postings_resolved": 142, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 594, "stop_reason": "page_budget", "unique_contribution": 142, "unique_jobs": 594}
- Query diagnostic: {"elapsed_seconds": 0.54, "first_pass_survivors": 26, "group": "official", "jds_resolved": 0, "original_postings_resolved": 26, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 351, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 351}
- Query diagnostic: {"elapsed_seconds": 0.37, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 0.409, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.535, "first_pass_survivors": 12, "group": "official", "jds_resolved": 0, "original_postings_resolved": 12, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 334, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 334}

Sample normalized records:

```json
[
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1436360758394361",
    "title": "Research Engineer, Robotics - Meta Superintelligence Labs",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/1436360758394361",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:40.036391+00:00",
    "date_confidence": "unknown",
    "description": "Meta is seeking a Robotics and Embodied AI Researcher to join Meta Superintelligence Labs. Individuals in this role are proficient in identified research areas such as artificial i"
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "704019139159184",
    "title": "Software Engineer (Leadership) - Infrastructure",
    "location": "Sunnyvale, CA; Remote, US; Bellevue, WA; Redmond, WA; Menlo Park, CA; Seattle, WA; Burlingame, CA; New York, NY",
    "official_url": "https://www.metacareers.com/jobs/704019139159184",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:40.036391+00:00",
    "date_confidence": "unknown",
    "description": "Meta is seeking talented principal engineers to join our teams in building cutting-edge products that connect billions of people around the world. As a member of our team, you will"
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1826062781882324",
    "title": "Hardware Engineer, PCB Layout",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/1826062781882324",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:40.036391+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2176103592946953",
    "title": "Hardware Engineer, AI Accelerator Module Design",
    "location": "Santa Clara, CA",
    "official_url": "https://www.metacareers.com/jobs/2176103592946953",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:40.036391+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2554796438372458",
    "title": "Hardware Engineer, AI Accelerator Module Design",
    "location": "Fremont, CA",
    "official_url": "https://www.metacareers.com/jobs/2554796438372458",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:31:40.036391+00:00",
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
- HTTP requests/cumulative request time: 26 / 20.809s
- Company elapsed time: 25.230s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 417, 'usable_jd': 417}
- Raw jobs found: 1238
- After US/location filtering: 708
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.198, "first_pass_survivors": 200, "group": "official", "jds_resolved": 200, "original_postings_resolved": 200, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 200, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 2.756, "first_pass_survivors": 132, "group": "official", "jds_resolved": 132, "original_postings_resolved": 132, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 132, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.7, "first_pass_survivors": 109, "group": "official", "jds_resolved": 109, "original_postings_resolved": 109, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 109, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.832, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.602, "first_pass_survivors": 62, "group": "official", "jds_resolved": 62, "original_postings_resolved": 62, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 62, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.736, "first_pass_survivors": 62, "group": "official", "jds_resolved": 62, "original_postings_resolved": 62, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 62, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.178, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 87, "stop_reason": "early_stop", "unique_contribution": 22, "unique_jobs": 87}
- Query diagnostic: {"elapsed_seconds": 0.597, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 3.631, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 200}

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
    "fetched_at": "2026-10-05T23:31:45.603753+00:00",
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
    "fetched_at": "2026-10-05T23:31:45.603753+00:00",
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
    "fetched_at": "2026-10-05T23:31:45.603753+00:00",
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
    "fetched_at": "2026-10-05T23:31:45.603753+00:00",
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
    "fetched_at": "2026-10-05T23:31:45.603753+00:00",
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
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 181 / 54.712s
- Company elapsed time: 80.055s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 154 / 0 / 0
- Detail cache statuses: {'fetched:new': 149, 'fetched:missing_detail': 5}
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 516
- After US/location filtering: 154
- With trustworthy posted_date: 154
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 31.035, "first_pass_survivors": 72, "group": "official", "jds_resolved": 72, "original_postings_resolved": 72, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 72, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 11.627, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.987, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 7.128, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 6.903, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.842, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.358, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.305, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 5.87, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "152899",
    "title": "Staff ML Engineer, Generative AI",
    "location": "Sunnyvale, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/152899",
    "posted_date": "2026-06-19",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:32:10.834470+00:00",
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
    "fetched_at": "2026-10-05T23:32:10.834470+00:00",
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
    "fetched_at": "2026-10-05T23:32:10.834470+00:00",
    "date_confidence": "high",
    "description": "About the Team The Applied AI team collaborates with product teams across Uber to deliver innovative AI solutions for core business problems. We work closely with engineering, prod"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "300982",
    "title": "Staff Machine Learning Engineer - Uber AI Solutions",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/300982",
    "posted_date": "2026-08-06",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:32:10.834470+00:00",
    "date_confidence": "high",
    "description": "Uber AI Solutions (UAIS) is a startup inside Uber, building the data and evaluation infrastructure behind the next generation of AI. The models making headlines are only as good as"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "155456",
    "title": "Senior ML Engineer, Computer Vision - Applied AI",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/155456",
    "posted_date": "2026-07-30",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:32:10.834470+00:00",
    "date_confidence": "high",
    "description": "About the Role Applied AI at Uber builds intelligent systems that power critical product experiences across the platform. As a Senior Machine Learning Engineer — Computer Vision, y"
  }
]
```

## DoorDash

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/doordashusa/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.337s
- Company elapsed time: 3.148s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 111, 'usable_jd': 111}
- Raw jobs found: 459
- After US/location filtering: 458
- With trustworthy posted_date: 458
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7858932",
    "title": "Account Executive",
    "location": "Charlotte, NC; Raleigh, NC; Tampa, FL; Orlando, FL; Pittsburgh, PA; Richmond, VA; Jacksonville, FL; Columbus, OH; Dallas, TX; Houston, TX; Minneapolis, MN; Nashville, TN; Kansas City, MO; St. Louis, MO; Tempe, AZ; Indianapolis, IN; Oklahoma City, OK; New Orleans, LA; Charleston, SC; Atlanta, GA; Tempe, AZ",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7858932",
    "posted_date": "2026-04-27",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:32:35.863418+00:00",
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
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:32:35.863418+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8160362",
    "title": "Account Executive - Field Sales, New Verticals",
    "location": "New York, NY; Tempe, AZ",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8160362",
    "posted_date": "2026-08-26",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:32:35.863418+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7852785",
    "title": "Account Manager, CPG",
    "location": "San Francisco, CA; New York, NY; Chicago, IL; Los Angeles, CA; Atlanta, GA; New York",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7852785",
    "posted_date": "2026-04-27",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:32:35.863418+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7951406",
    "title": "Account Manager, Enterprise Ad Sales",
    "location": "New York, NY; San Francisco, CA; Los Angeles, CA; Chicago, IL; Atlanta, GA; New York",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7951406",
    "posted_date": "2026-05-27",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:32:35.863418+00:00",
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
- HTTP requests/cumulative request time: 126 / 49.337s
- Company elapsed time: 66.815s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 102 / 0 / 0
- Detail cache statuses: {'fetched:new': 100, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 16, 'usable_jd': 16}
- Raw jobs found: 366
- After US/location filtering: 102
- With trustworthy posted_date: 102
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.815, "first_pass_survivors": 63, "group": "official", "jds_resolved": 63, "original_postings_resolved": 63, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 76, "stop_reason": "page_budget", "unique_contribution": 63, "unique_jobs": 76}
- Query diagnostic: {"elapsed_seconds": 4.601, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 39, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 0.689, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 5.436, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 7.552, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.685, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.865, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.99, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 8.423, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0045781",
    "title": "Staff Software Engineer, Platform Engineering",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Staff-Software-Engineer--Platform-Engineering_R0045781-1",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:32:39.012315+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046467",
    "title": "Staff Machine Learning Engineer, Diffusion, Generative Modeling and Inference",
    "location": "Los Angeles, California; Seattle, Washington; Palo Alto, California; New York, New York; Bellevue, Washington",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Staff-Machine-Learning-Engineer--Generative-AI-Modeling-and-Inference_R0046467",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:32:39.012315+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046612",
    "title": "Privacy Engineer, Level 4",
    "location": "Los Angeles, California; Palo Alto, California; New York, New York; Bellevue, Washington",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Privacy-Engineer--Level-4_R0046612-1",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:32:39.012315+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046161",
    "title": "Manager, Privacy Engineering",
    "location": "Los Angeles, California; Bellevue, Washington",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Manager--Privacy-Engineering_R0046161-1",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:32:39.012315+00:00",
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
    "fetched_at": "2026-10-05T23:32:39.012315+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.834s
- Company elapsed time: 1.528s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 22, 'usable_jd': 22}
- Raw jobs found: 174
- After US/location filtering: 133
- With trustworthy posted_date: 133
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8103612",
    "title": "Administrative Business Partner I - Engineering, Product and Design",
    "location": "San Francisco, CA, US; Palo Alto, CA, US; San Francisco, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8103612",
    "posted_date": "2026-08-14",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:32:59.654425+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8202207",
    "title": "Client Account Manager II",
    "location": "Buenos Aires, AR; Argentina, AR",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8202207",
    "posted_date": "2026-09-17",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:32:59.654425+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8130612",
    "title": "Client Account Manager II, Affiliate (tvScientific)",
    "location": "New York, NY, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8130612",
    "posted_date": "2026-09-11",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:32:59.654425+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8223489",
    "title": "Client Account Manager II, Beauty CPG",
    "location": "New York, NY, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8223489",
    "posted_date": "2026-10-01",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:32:59.654425+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8114760",
    "title": "Client Account Manager II, CPG (Food)",
    "location": "Chicago, IL, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8114760",
    "posted_date": "2026-09-01",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:32:59.654425+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.254s
- Company elapsed time: 0.852s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 40, 'usable_jd': 40}
- Raw jobs found: 349
- After US/location filtering: 252
- With trustworthy posted_date: 252
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
    "fetched_at": "2026-10-05T23:33:01.183561+00:00",
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
    "fetched_at": "2026-10-05T23:33:01.183561+00:00",
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
    "fetched_at": "2026-10-05T23:33:01.183561+00:00",
    "date_confidence": "high",
    "description": "At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to "
  },
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "e2739aab-b0a2-4583-92c1-13bbd4fd9672",
    "title": "Principal Software Engineer I - Metadata",
    "location": "US-WA-Bellevue; Bellevue, Washington, United States",
    "official_url": "https://jobs.ashbyhq.com/snowflake/e2739aab-b0a2-4583-92c1-13bbd4fd9672",
    "posted_date": "2026-03-23",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:01.183561+00:00",
    "date_confidence": "high",
    "description": "At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to "
  },
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "97813cac-e55c-4631-94fe-5eda15c7eaed",
    "title": "Senior Forward Deployed Engineer -Spark",
    "location": "US-CA-Menlo Park; Menlo Park, California, United States; US-WA-Bellevue",
    "official_url": "https://jobs.ashbyhq.com/snowflake/97813cac-e55c-4631-94fe-5eda15c7eaed",
    "posted_date": "2026-04-01",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:01.183561+00:00",
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
- HTTP requests/cumulative request time: 429 / 194.356s
- Company elapsed time: 248.581s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 407 / 0 / 0
- Detail cache statuses: {'fetched:new': 407}
- Relevant JD recovery: {'eligible': 50, 'usable_jd': 50}
- Raw jobs found: 1825
- After US/location filtering: 407
- With trustworthy posted_date: 407
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 180.268, "first_pass_survivors": 307, "group": "official", "jds_resolved": 307, "original_postings_resolved": 307, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 307, "stop_reason": "page_budget", "unique_contribution": 307, "unique_jobs": 307}
- Query diagnostic: {"elapsed_seconds": 1.247, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 104, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 104}
- Query diagnostic: {"elapsed_seconds": 10.222, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 175, "stop_reason": "early_stop", "unique_contribution": 15, "unique_jobs": 175}
- Query diagnostic: {"elapsed_seconds": 47.484, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 268, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 268}
- Query diagnostic: {"elapsed_seconds": 1.852, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 289, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 289}
- Query diagnostic: {"elapsed_seconds": 4.264, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 0.42, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 75, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 0.435, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 50, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 50}
- Query diagnostic: {"elapsed_seconds": 2.389, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 257, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 257}

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075626",
    "title": "Staff Data Platform Software Engineer - Persistence",
    "location": "San Diego, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153624789-staff-data-platform-software-engineer-persistence",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:02.036722+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075626",
    "title": "Staff Data Platform Software Engineer - Persistence",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153624639-staff-data-platform-software-engineer-persistence",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:02.036722+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075704",
    "title": "Sr Advisory Solution Consultant- US Public Sector- Moveworks",
    "location": "Chicago, Illinois, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153614183-sr-advisory-solution-consultant-us-public-sector-moveworks",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:02.036722+00:00",
    "date_confidence": "high",
    "description": "Moveworks is the Agentic AI Assistant platform that empowers the entire workforce. Our platform enables employees to converse with all of their business systems through natural lan"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075704",
    "title": "Sr Advisory Solution Consultant- US Public Sector- Moveworks",
    "location": "New York, New York, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153615549-sr-advisory-solution-consultant-us-public-sector-moveworks",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:02.036722+00:00",
    "date_confidence": "high",
    "description": "Moveworks is the Agentic AI Assistant platform that empowers the entire workforce. Our platform enables employees to converse with all of their business systems through natural lan"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075704",
    "title": "Sr Advisory Solution Consultant- US Public Sector- Moveworks",
    "location": "Boston, Massachusetts, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153615369-sr-advisory-solution-consultant-us-public-sector-moveworks",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:02.036722+00:00",
    "date_confidence": "high",
    "description": "Moveworks is the Agentic AI Assistant platform that empowers the entire workforce. Our platform enables employees to converse with all of their business systems through natural lan"
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
- HTTP requests/cumulative request time: 57 / 70.308s
- Company elapsed time: 83.309s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 28 / 6 / 32
- Detail cache statuses: {'fetched:new': 27, 'reused': 6}
- Relevant JD recovery: {'deterministic_skip': 25, 'ai_skip': 7, 'eligible': 1, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 0}
- Raw jobs found: 348
- After US/location filtering: 33
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 41.998, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 4.758, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.954, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.887, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.954, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.946, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.501, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.67, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 6.249, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 48}

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45089",
    "title": "Contracts Coordinator - Finance & Administration",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Contracts-Coordinator-Finance-Administration/45089",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:23.391271+00:00",
    "date_confidence": "unknown",
    "description": "Contracts Coordinator - Finance & Administration"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45087",
    "title": "Booking Producer, Surveillance",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Booking-Producer-Surveillance/45087",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:23.391271+00:00",
    "date_confidence": "unknown",
    "description": "Booking Producer, Surveillance"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45084",
    "title": "Legal Data Analyst - Data Enrichment",
    "location": "Princeton, New Jersey, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Legal-Data-Analyst-Data-Enrichment/45084",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:23.391271+00:00",
    "date_confidence": "unknown",
    "description": "Legal Data Analyst - Data Enrichment"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45066",
    "title": "Index Sales Relationship Manager, Investment Managers - Financial Solutions",
    "location": "San Francisco, California, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Index-Sales-Relationship-Manager-Investment-Managers-Financial-Solutions/45066",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:23.391271+00:00",
    "date_confidence": "unknown",
    "description": "Index Sales Relationship Manager, Investment Managers - Financial Solutions"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45046",
    "title": "Senior Full-Stack Qlik Sense Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Full-Stack-Qlik-Sense-Engineer/45046",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:23.391271+00:00",
    "date_confidence": "unknown",
    "description": "Senior Full-Stack Qlik Sense Engineer"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 64
- HTTP requests/cumulative request time: 609 / 126.958s
- Company elapsed time: 210.660s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 545 / 0 / 0
- Detail cache statuses: {'fetched:new': 531, 'fetched:missing_detail': 14}
- Relevant JD recovery: {'eligible': 108, 'usable_jd': 108}
- Raw jobs found: 1271
- After US/location filtering: 545
- With trustworthy posted_date: 545
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.635, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 14.255, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.826, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.243, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.833, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.317, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.894, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.626, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.44, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 13.632, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "full stack", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.475, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "python react", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.573, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "pyspark databricks", "raw_jobs": 51, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 51}
- Query diagnostic: {"elapsed_seconds": 8.322, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "experienced software engineer java python", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.392, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "agentic ai", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.583, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.243, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "software engineer ii", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.78, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.825, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "security engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.544, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "quantitative developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.125, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "software engineer java spring", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.594, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "software engineer python authe", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.433, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "aws data platform engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.008, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "data engineer applied ai", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 4.062, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 1, "pages_fetched": 1, "query": "asset management technology", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 20}

Sample normalized records:

```json
[
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210795270",
    "title": "Sr Lead Software Engineer - AI Engineer",
    "location": "Columbus, OH, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210795270",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:30.890774+00:00",
    "date_confidence": "high",
    "description": "Be an integral part of an agile team that's constantly pushing the envelope to enhance, build, and deliver top-notch technology products. Job Summary As a Senior Lead Software Engi"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210779849",
    "title": "Lead Software Engineer - Cloud/AI Engineer",
    "location": "Plano, TX, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210779849",
    "posted_date": "2026-08-14",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:30.890774+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorganChase within the Corp"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210782895",
    "title": "Lead Software Engineer - Data & AI Platform Engineer",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210782895",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:30.890774+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorgan Chase, within the Co"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210791945",
    "title": "AI Engineer - Sr Lead Software Engineer",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210791945",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:30.890774+00:00",
    "date_confidence": "high",
    "description": "Be an integral part of an agile team that's constantly pushing the envelope to enhance, build, and deliver top-notch technology products. As a Senior Lead Software Engineer at JPMo"
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
    "fetched_at": "2026-10-05T23:33:30.890774+00:00",
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
- HTTP requests/cumulative request time: 196 / 80.039s
- Company elapsed time: 108.070s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 168 / 0 / 0
- Detail cache statuses: {'fetched:new': 137, 'fetched:missing_detail': 31}
- Relevant JD recovery: {'eligible': 58, 'usable_jd': 58}
- Raw jobs found: 526
- After US/location filtering: 168
- With trustworthy posted_date: 168
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 44.235, "first_pass_survivors": 74, "group": "official", "jds_resolved": 74, "original_postings_resolved": 74, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 74, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 22.752, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.846, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.032, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.302, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.001, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.417, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.577, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 4.625, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1003028",
    "title": "Manager - Product Management - Travel Communication Platform",
    "location": "New York, NY",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/New-York-NY/Manager---Product-Management---Travel-Communication-Platform_R1003028-2",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:45.828359+00:00",
    "date_confidence": "high",
    "description": "Manager - Product Management - Travel Communication Platform Manager, Product Management (PXDP50) Do you want to build and scale the communication platforms that reach every Capita"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1000592",
    "title": "Part-Time Applied Data Scientist",
    "location": "Cambridge, MA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Cambridge-MA/Part-Time-Applied-Data-Scientist_R1000592",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:45.828359+00:00",
    "date_confidence": "high",
    "description": "Part-Time Applied Data Scientist This role is located at the Capital One Cambridge office, and you must be enrolled as a student at MIT to apply. As a part-time associate at Capita"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001957",
    "title": "Senior Manager, Data Analyst - Product Analytics",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Manager-Data-Analytics---Analytics---Transformation_R1001957-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:45.828359+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Data Analyst - Product Analytics At Capital One, data is at the center of everything we do. When we launched as a startup we disrupted the credit card industry by i"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R248275",
    "title": "Data Analysis Manager - Analytics & Transformation",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Data-Analysis-Manager---Analytics---Transformation_R248275-2",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:45.828359+00:00",
    "date_confidence": "high",
    "description": "Data Analysis Manager - Analytics & Transformation At Capital One, data is at the center of everything we do. When we launched as a startup we disrupted the credit card industry by"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001188",
    "title": "Full Stack Engineer 4",
    "location": "New York, NY; McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/New-York-NY/Full-Stack-Engineer-4_R1001188-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:33:45.828359+00:00",
    "date_confidence": "high",
    "description": "Full Stack Engineer 4 Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclusive and iter"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 41
- HTTP requests/cumulative request time: 532 / 300.881s
- Company elapsed time: 373.250s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 488 / 0 / 3
- Detail cache statuses: {'fetched:new': 483, 'missing:new': 3, 'fetched:missing_detail': 5}
- Relevant JD recovery: {'eligible': 48, 'deterministic_skip': 3, 'usable_jd': 48}
- Raw jobs found: 813
- After US/location filtering: 491
- With trustworthy posted_date: 491
- Errors/403s: ["detail 345385: Oracle oracle hcm detail network error: HTTPSConnectionPool(host='eeho.fa.us2.oraclecloud.com', port=443): Read timed out. (read timeout=30)", "detail 336554: Oracle oracle hcm detail network error: HTTPSConnectionPool(host='eeho.fa.us2.oraclecloud.com', port=443): Read timed out. (read timeout=30)", "detail 345235: Oracle oracle hcm detail network error: HTTPSConnectionPool(host='eeho.fa.us2.oraclecloud.com', port=443): Read timed out. (read timeout=30)"]

- Query diagnostic: {"elapsed_seconds": 92.918, "first_pass_survivors": 78, "group": "official", "jds_resolved": 78, "original_postings_resolved": 78, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 78, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 21.372, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.992, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 56, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 16.998, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 23.648, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 29.827, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.144, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 45.466, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 45.366, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 78}
- Query diagnostic: {"elapsed_seconds": 31.555, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "core infrastructure", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 20.657, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "cleared site reliability engineer database", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 7.215, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "software developer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 14.093, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "applications developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "336795",
    "title": "Senior Principal Engineer - AI Networking",
    "location": "Seattle, WA, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/336795",
    "posted_date": "2026-09-29",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:34:45.309288+00:00",
    "date_confidence": "high",
    "description": "You will work at the intersection of distributed systems, networking, and AI infrastructure, driving architecture, design, implementation, and performance optimization across softw"
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
    "fetched_at": "2026-10-05T23:34:45.309288+00:00",
    "date_confidence": "high",
    "description": "Oracle Health is seeking a Senior AI Agent Engineer to build production AI agents and workflow automation capabilities that accelerate analytics delivery, improve insight generatio"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "336797",
    "title": "Principal Engineer - AI Networking",
    "location": "Seattle, WA, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/336797",
    "posted_date": "2026-09-21",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:34:45.309288+00:00",
    "date_confidence": "high",
    "description": "The ideal candidate is an experienced RDMA software engineer with a strong background in high-performance networking, distributed communication systems, and systems programming. Yo"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "335707",
    "title": "Senior AI Agent Engineer",
    "location": "United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/335707",
    "posted_date": "2026-09-22",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:34:45.309288+00:00",
    "date_confidence": "high",
    "description": "Oracle Health is seeking an AI Platform Reliability Engineer to ensure our AI agent platform and AI-enabled analytics workflows are reliable, observable, measurable, and safe in pr"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "333513",
    "title": "Software Engineer, Core Infrastructure (AI Infrastructure)",
    "location": "Austin, TX, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/333513",
    "posted_date": "2026-06-11",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:34:45.309288+00:00",
    "date_confidence": "high",
    "description": "As a Senior Software Engineer within Oracle Cloud Infrastructure (OCI), you’ll have the opportunity to solve large-scale, mission-critical engineering challenges with broad technic"
  }
]
```

## Walmart Global Tech

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://walmart.wd504.myworkdayjobs.com/WalmartExternal`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 28
- HTTP requests/cumulative request time: 406 / 233.266s
- Company elapsed time: 289.425s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 377 / 0 / 0
- Detail cache statuses: {'fetched:new': 370, 'fetched:missing_detail': 6, 'reuse_after_error:missing_detail': 1}
- Relevant JD recovery: {'eligible': 51, 'ai_recover': 1, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 50}
- Raw jobs found: 547
- After US/location filtering: 377
- With trustworthy posted_date: 376
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 56.28, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 32.032, "first_pass_survivors": 46, "group": "official", "jds_resolved": 46, "original_postings_resolved": 46, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 46, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 40.34, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 28.987, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 19.351, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 26.324, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 43.541, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.584, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 16.599, "first_pass_survivors": 23, "group": "official", "jds_resolved": 22, "original_postings_resolved": 23, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 19.042, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 1, "pages_fetched": 1, "query": "usa software engineer ii", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 20}

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
    "fetched_at": "2026-10-05T23:35:33.899733+00:00",
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
    "fetched_at": "2026-10-05T23:35:33.899733+00:00",
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
    "posted_date": "2026-06-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:35:33.899733+00:00",
    "date_confidence": "high",
    "description": "Position Summary... As a Distinguished AI/ML Engineer within Walmart Global Tech's Site Reliability Engineering organization, you will lead the technical development of next-genera"
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
    "fetched_at": "2026-10-05T23:35:33.899733+00:00",
    "date_confidence": "high",
    "description": "Position Summary... What you'll do... The Opportunity: Walmart’s Supply Chain AI Lab & Innovation Factory is building a new generation of production-grade agentic AI systems that r"
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
    "fetched_at": "2026-10-05T23:35:33.899733+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.368s
- Company elapsed time: 2.143s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 77, 'usable_jd': 77}
- Raw jobs found: 413
- After US/location filtering: 409
- With trustworthy posted_date: 409
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
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:35:59.970931+00:00",
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
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:35:59.970931+00:00",
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
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:35:59.970931+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "8144669",
    "title": "Associate General Counsel, Privacy Compliance",
    "location": "Hybrid; London, United Kingdom",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/8144669?gh_jid=8144669",
    "posted_date": "2026-08-21",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:35:59.970931+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "7167659",
    "title": "Business Development Representative - Bahasa Indonesia Speaking",
    "location": "Hybrid; Singapore",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/7167659?gh_jid=7167659",
    "posted_date": "2025-08-17",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:35:59.970931+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.222s
- Company elapsed time: 1.553s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 137, 'usable_jd': 137}
- Raw jobs found: 718
- After US/location filtering: 415
- With trustworthy posted_date: 415
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
    "updated_date": "2026-09-25",
    "fetched_at": "2026-10-05T23:36:02.114375+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>Who we are </strong></h2> <h3><strong>About Stripe</strong></h3> <p><span style=\"font-weight: 400;\">Stripe is a financial infrastructure platform for businesses. Millio"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8172503",
    "title": "Abuse Research Engineer",
    "location": "Remote from the US; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8172503",
    "posted_date": "2026-09-09",
    "updated_date": "2026-09-25",
    "fetched_at": "2026-10-05T23:36:02.114375+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p><span style=\"font-weight: 400;\">Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s la"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8138044",
    "title": "Account Executive, AI Sales",
    "location": "San Francisco, CA; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8138044",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-25",
    "fetched_at": "2026-10-05T23:36:02.114375+00:00",
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
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:36:02.114375+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s largest enterprises to the most am"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8204645",
    "title": "Account Executive, AI Startups - Grower",
    "location": "New York; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8204645",
    "posted_date": "2026-09-15",
    "updated_date": "2026-09-25",
    "fetched_at": "2026-10-05T23:36:02.114375+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s largest enterprises to the most am"
  }
]
```

## Coinbase

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/coinbase/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.174s
- Company elapsed time: 0.992s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 52, 'usable_jd': 52}
- Raw jobs found: 224
- After US/location filtering: 190
- With trustworthy posted_date: 190
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8175363",
    "title": "Accelerations Programs Intern",
    "location": "Hybrid - New York, NY; US - Remote Zone 1 (Job Requisitions Only)",
    "official_url": "https://www.coinbase.com/careers/positions/8175363?gh_jid=8175363",
    "posted_date": "2026-09-08",
    "updated_date": "2026-09-22",
    "fetched_at": "2026-10-05T23:36:03.668240+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? At&nbsp;<a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sou"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8053751",
    "title": "Accountant, Cyprus",
    "location": "Remote - Cyprus",
    "official_url": "https://www.coinbase.com/careers/positions/8053751?gh_jid=8053751",
    "posted_date": "2026-07-09",
    "updated_date": "2026-09-24",
    "fetched_at": "2026-10-05T23:36:03.668240+00:00",
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
    "updated_date": "2026-09-08",
    "fetched_at": "2026-10-05T23:36:03.668240+00:00",
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
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:36:03.668240+00:00",
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
    "updated_date": "2026-09-03",
    "fetched_at": "2026-10-05T23:36:03.668240+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.186s
- Company elapsed time: 0.928s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 44, 'usable_jd': 44}
- Raw jobs found: 155
- After US/location filtering: 140
- With trustworthy posted_date: 140
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
    "fetched_at": "2026-10-05T23:36:04.661465+00:00",
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
    "fetched_at": "2026-10-05T23:36:04.661465+00:00",
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
    "fetched_at": "2026-10-05T23:36:04.661465+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "7943204",
    "title": "Assistant General Counsel, Credit Cards",
    "location": "Menlo Park, CA; New York, NY; Washington, DC; Menlo Park, CA; New York, NY; Washington, DC",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/7943204?t=gh_src=&gh_jid=7943204",
    "posted_date": "2026-06-01",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:36:04.661465+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8199973",
    "title": "Associate Product Manager (New Grad)",
    "location": "New York, NY; Menlo Park, CA",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8199973?t=gh_src=&gh_jid=8199973",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:36:04.661465+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.176s
- Company elapsed time: 0.740s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 43, 'usable_jd': 43}
- Raw jobs found: 164
- After US/location filtering: 109
- With trustworthy posted_date: 109
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
    "updated_date": "2026-07-22",
    "fetched_at": "2026-10-05T23:36:05.590426+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all. Figma’s platform helps teams bring ideas"
  },
  {
    "company": "Figma",
    "source": "figma_official_careers",
    "job_id": "5422236004",
    "title": "Account Executive, Mid-Market",
    "location": "San Francisco, CA • New York, NY • United States; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/5422236004?gh_jid=5422236004",
    "posted_date": "2025-01-22",
    "updated_date": "2026-08-20",
    "fetched_at": "2026-10-05T23:36:05.590426+00:00",
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
    "updated_date": "2026-07-22",
    "fetched_at": "2026-10-05T23:36:05.590426+00:00",
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
    "updated_date": "2026-07-22",
    "fetched_at": "2026-10-05T23:36:05.590426+00:00",
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
    "updated_date": "2026-07-22",
    "fetched_at": "2026-10-05T23:36:05.590426+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.182s
- Company elapsed time: 0.947s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 15, 'usable_jd': 15}
- Raw jobs found: 210
- After US/location filtering: 121
- With trustworthy posted_date: 121
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
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:36:06.331724+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8716179002",
    "title": "AI Transformation Owner, Product & Design",
    "location": "Remote, Canada; Remote, United Kingdom; Remote, United States",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8716179002",
    "posted_date": "2026-08-19",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:36:06.331724+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8857185002",
    "title": "Associate Renewals Manager",
    "location": "Remote, Canada; Remote, United States; North America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8857185002",
    "posted_date": "2026-09-29",
    "updated_date": "2026-09-30",
    "fetched_at": "2026-10-05T23:36:06.331724+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8698314002",
    "title": "Backend Engineer, AI Engineering: Duo Chat",
    "location": "Remote, Canada; Remote, United States; Canada; United States of America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8698314002",
    "posted_date": "2026-08-20",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:36:06.331724+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8532274002",
    "title": "Business Development Representative",
    "location": "Remote, EMEA; Remote, France; Remote, Germany; Remote, Ireland; Remote, Netherlands; Remote, United Kingdom",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8532274002",
    "posted_date": "2026-05-01",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:36:06.331724+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.087s
- Company elapsed time: 0.266s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 51
- After US/location filtering: 51
- With trustworthy posted_date: 51
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8806482002",
    "title": "Commercial Policy Lead",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8806482002",
    "posted_date": "2026-09-15",
    "updated_date": "2026-09-15",
    "fetched_at": "2026-10-05T23:36:07.279620+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8840756002",
    "title": "Data Scientist - Client Platform",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8840756002",
    "posted_date": "2026-09-24",
    "updated_date": "2026-09-24",
    "fetched_at": "2026-10-05T23:36:07.279620+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8722538002",
    "title": "Engineering Manager, Machine Learning (Safety)",
    "location": "San Francisco Bay Area (or Remote U.S.); Remote (U.S.)",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8722538002",
    "posted_date": "2026-08-20",
    "updated_date": "2026-09-22",
    "fetched_at": "2026-10-05T23:36:07.279620+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8649856002",
    "title": "Engineering Manager, Platform Security",
    "location": "Remote (West Coast); Remote (U.S.)",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8649856002",
    "posted_date": "2026-07-27",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:36:07.279620+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8637688002",
    "title": "Engineering Manager, Safety",
    "location": "San Francisco Bay Area, Greater Seattle Area, Greater Los Angeles Area (U.S.); Remote (U.S.)",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8637688002",
    "posted_date": "2026-07-29",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:36:07.279620+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.135s
- Company elapsed time: 0.575s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 20, 'usable_jd': 20}
- Raw jobs found: 101
- After US/location filtering: 77
- With trustworthy posted_date: 77
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8092044",
    "title": "Analytical Engineer",
    "location": "Warsaw; Warszawa, Masovian Voivodeship, Poland",
    "official_url": "https://www.asana.com/jobs/apply/8092044?gh_jid=8092044",
    "posted_date": "2026-07-30",
    "updated_date": "2026-09-15",
    "fetched_at": "2026-10-05T23:36:07.545849+00:00",
    "date_confidence": "high",
    "description": "<p>The Data Science &amp; Analytics team at Asana is how the company turns data into decisions — defining the questions that matter, surfacing the answers, and making sure insight "
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
    "fetched_at": "2026-10-05T23:36:07.545849+00:00",
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
    "updated_date": "2026-09-15",
    "fetched_at": "2026-10-05T23:36:07.545849+00:00",
    "date_confidence": "high",
    "description": "<p id=\"p-rc_10838ec6a95bc2d4-72\" data-path-to-node=\"3\"><span data-path-to-node=\"3,0\">We are looking for a detail-oriented, strategic team player to join as a Benefits Manager on As"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8161860",
    "title": "Channel Account Executive, LATAM",
    "location": "US FL Miami - Remote; Chicago",
    "official_url": "https://www.asana.com/jobs/apply/8161860?gh_jid=8161860",
    "posted_date": "2026-09-21",
    "updated_date": "2026-09-23",
    "fetched_at": "2026-10-05T23:36:07.545849+00:00",
    "date_confidence": "high",
    "description": "<p data-pm-slice=\"1 1 []\">We’re seeking a driven and strategic Channel Account Executive to manage sales cycles and accelerate revenue growth within the LATAM region. In this role,"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8082010",
    "title": "Compensation Business Partner",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://www.asana.com/jobs/apply/8082010?gh_jid=8082010",
    "posted_date": "2026-07-30",
    "updated_date": "2026-09-15",
    "fetched_at": "2026-10-05T23:36:07.545849+00:00",
    "date_confidence": "high",
    "description": "<p id=\"p-rc_4b152f88e5bc4c86-59\" data-path-to-node=\"3\"><span data-path-to-node=\"3,0\"><span class=\"citation-3850 citation-3851 citation-end-3851\">The People Team at Asana works to e"
  }
]
```

## Brex

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/brex/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.208s
- Company elapsed time: 1.356s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 48, 'usable_jd': 48}
- Raw jobs found: 284
- After US/location filtering: 277
- With trustworthy posted_date: 277
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8721806002",
    "title": "Account Executive, YC",
    "location": "San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8721806002?gh_jid=8721806002",
    "posted_date": "2026-08-17",
    "updated_date": "2026-08-19",
    "fetched_at": "2026-10-05T23:36:08.121672+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8795500002",
    "title": "Account Protection Specialist",
    "location": "Vancouver, British Columbia, Canada; Remote",
    "official_url": "https://www.brex.com/careers/8795500002?gh_jid=8795500002",
    "posted_date": "2026-09-10",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-10-05T23:36:08.121672+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8606845002",
    "title": "AI Engineer, Workbench",
    "location": "San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8606845002?gh_jid=8606845002",
    "posted_date": "2026-06-24",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:36:08.121672+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8853828002",
    "title": "Banking Relationship Manager",
    "location": "San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8853828002?gh_jid=8853828002",
    "posted_date": "2026-09-28",
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:36:08.121672+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8860097002",
    "title": "Brand Marketing Lead",
    "location": "New York, New York, United States; San Francisco, California, United States; United States; New York, New York, United States; Salt Lake City, Utah, United States; San Francisco, California, United States; Seattle, Washington, United States",
    "official_url": "https://www.brex.com/careers/8860097002?gh_jid=8860097002",
    "posted_date": "2026-10-01",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:36:08.121672+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.215s
- Company elapsed time: 1.513s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 45, 'usable_jd': 45}
- Raw jobs found: 244
- After US/location filtering: 204
- With trustworthy posted_date: 204
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8094367",
    "title": "Account Development Representative II",
    "location": "Atlanta, Georgia, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8094367?gh_jid=8094367",
    "posted_date": "2026-08-12",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:36:09.479008+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8094314",
    "title": "Account Development Representative II - Phoenix",
    "location": "Phoenix, Arizona, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8094314?gh_jid=8094314",
    "posted_date": "2026-09-02",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:36:09.479008+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8103119",
    "title": "Account Development Representative Intern - Atlanta",
    "location": "Atlanta, Georgia, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8103119?gh_jid=8103119",
    "posted_date": "2026-08-21",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:36:09.479008+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8099799",
    "title": "Account Development Representative Intern - Phoenix",
    "location": "Phoenix, Arizona, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8099799?gh_jid=8099799",
    "posted_date": "2026-08-21",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:36:09.479008+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8162034",
    "title": "Account Executive, Commercial",
    "location": "Remote - US",
    "official_url": "https://www.samsara.com/company/careers/roles/8162034?gh_jid=8162034",
    "posted_date": "2026-09-03",
    "updated_date": "2026-09-25",
    "fetched_at": "2026-10-05T23:36:09.479008+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.183s
- Company elapsed time: 0.555s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 27, 'usable_jd': 27}
- Raw jobs found: 189
- After US/location filtering: 96
- With trustworthy posted_date: 96
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8792050002",
    "title": "Account Manager, Automotive Vertical",
    "location": "New York, NY; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8792050002?gh_jid=8792050002",
    "posted_date": "2026-09-10",
    "updated_date": "2026-09-17",
    "fetched_at": "2026-10-05T23:36:10.993170+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8791500002",
    "title": "Account Manager, Automotive Vertical",
    "location": "San Francisco, CA; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8791500002?gh_jid=8791500002",
    "posted_date": "2026-09-10",
    "updated_date": "2026-09-17",
    "fetched_at": "2026-10-05T23:36:10.993170+00:00",
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
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:36:10.993170+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-10-05T23:36:10.993170+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8843341002",
    "title": "Applied Scientist Intern (Summer 2027)",
    "location": "San Francisco, CA; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8843341002?gh_jid=8843341002",
    "posted_date": "2026-09-28",
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:36:10.993170+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.231s
- Company elapsed time: 0.382s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 3 / 0
- Detail cache statuses: {'reused': 3}
- Relevant JD recovery: {'eligible': 17, 'cache_reused': 3, 'usable_jd': 17}
- Raw jobs found: 80
- After US/location filtering: 65
- With trustworthy posted_date: 65
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "2193db3f-77c5-43b8-b030-8f92c9882bf1",
    "title": "Android Engineer - Experience",
    "location": "London; Stockholm",
    "official_url": "https://jobs.lever.co/spotify/2193db3f-77c5-43b8-b030-8f92c9882bf1",
    "posted_date": "2026-06-23",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:11.549405+00:00",
    "date_confidence": "high",
    "description": "Develop and maintain mobile client components that capture and report listening and user behavior signals across Spotify. Build high-quality, well-tested, and well-documented Kotli"
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
    "fetched_at": "2026-10-05T23:36:11.549405+00:00",
    "date_confidence": "high",
    "description": "Maintain positive partnerships across artist and label communities within Vietnam. Support our key partners in Vietnam on Spotify tools, resources and insights. Work closely with o"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "4310f31c-90e1-4e8d-bdcf-dce39c145b8c",
    "title": "Associate – Audiobook Licensing & Author Partnerships",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/4310f31c-90e1-4e8d-bdcf-dce39c145b8c",
    "posted_date": "2026-07-09",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:11.549405+00:00",
    "date_confidence": "high",
    "description": "Identify and evaluate audiobook catalogs from independent authors, hybrid publishers, independent presses, and distribution partners that will resonate with Spotify listeners. Nego"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "65d6caca-6d7c-4049-8256-a128e0e7249e",
    "title": "Backend Engineer - Music",
    "location": "New York, NY; Boston, MA; Miami, FL",
    "official_url": "https://jobs.lever.co/spotify/65d6caca-6d7c-4049-8256-a128e0e7249e",
    "posted_date": "2026-09-29",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:11.549405+00:00",
    "date_confidence": "high",
    "description": "Build and run production backend systems that improve how listeners discover and enjoy music videos. Design, develop, and evolve scalable backend services and APIs that support hig"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "186b763a-2a61-4563-8813-ff6b40c9c8a7",
    "title": "Backend Engineer II - Data Platform",
    "location": "Stockholm; London",
    "official_url": "https://jobs.lever.co/spotify/186b763a-2a61-4563-8813-ff6b40c9c8a7",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:11.549405+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.127s
- Company elapsed time: 0.547s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 66, 'usable_jd': 66}
- Raw jobs found: 159
- After US/location filtering: 141
- With trustworthy posted_date: 141
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
    "fetched_at": "2026-10-05T23:36:11.932765+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $200B in annualized"
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
    "fetched_at": "2026-10-05T23:36:11.932765+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $200B in annualized"
  },
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "4e64ab86-4e30-403b-b1b9-41dc052570ce",
    "title": "Software Engineer, Frontend",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote (Canada); San Francisco, CA; Remote (US); Miami, FL",
    "official_url": "https://jobs.ashbyhq.com/ramp/4e64ab86-4e30-403b-b1b9-41dc052570ce",
    "posted_date": "2023-03-09",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:11.932765+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $200B in annualized"
  },
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "4745807e-82f4-4b1a-857c-dc8dadc73076",
    "title": "Credit Risk Associate",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote, USA",
    "official_url": "https://jobs.ashbyhq.com/ramp/4745807e-82f4-4b1a-857c-dc8dadc73076",
    "posted_date": "2026-08-12",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:11.932765+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $200B in annualized"
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
    "fetched_at": "2026-10-05T23:36:11.932765+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $200B in annualized"
  }
]
```

## Notion

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/notion`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.113s
- Company elapsed time: 0.377s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 36, 'usable_jd': 36}
- Raw jobs found: 135
- After US/location filtering: 80
- With trustworthy posted_date: 80
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Notion",
    "source": "notion_official_careers",
    "job_id": "1fc309c8-da20-4ff2-84c7-8b863ece2b0a",
    "title": "Software Engineer, Developer Platform",
    "location": "San Francisco, California; San Francisco, California, United States; New York, New York; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/notion/1fc309c8-da20-4ff2-84c7-8b863ece2b0a",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:12.480827+00:00",
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
    "fetched_at": "2026-10-05T23:36:12.480827+00:00",
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
    "fetched_at": "2026-10-05T23:36:12.480827+00:00",
    "date_confidence": "high",
    "description": "WHO WE ARE Notion is the collaborative AI workspace where teams and agents think together https://www.youtube.com/watch?v=vkpYpWfEK5s. We're building one place where your knowledge"
  },
  {
    "company": "Notion",
    "source": "notion_official_careers",
    "job_id": "d177d052-ef57-4900-acf2-d58e9eded620",
    "title": "Product Designer",
    "location": "San Francisco, California; San Francisco, California, United States; New York, New York; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/notion/d177d052-ef57-4900-acf2-d58e9eded620",
    "posted_date": "2026-07-02",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:12.480827+00:00",
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
    "fetched_at": "2026-10-05T23:36:12.480827+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.069s
- Company elapsed time: 0.139s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 29
- After US/location filtering: 27
- With trustworthy posted_date: 27
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
    "fetched_at": "2026-10-05T23:36:12.858571+00:00",
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
    "fetched_at": "2026-10-05T23:36:12.858571+00:00",
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
    "fetched_at": "2026-10-05T23:36:12.858571+00:00",
    "date_confidence": "high",
    "description": "At Linear, we're building the product development system for teams and agents. AI is fundamentally changing how software gets built, and we’re shaping the tools this new era requir"
  },
  {
    "company": "Linear",
    "source": "linear_official_careers",
    "job_id": "f04f398b-6320-499d-8a60-290239d62da8",
    "title": "Design Engineer (Web & Brand)",
    "location": "North America; United States; Europe; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/linear/f04f398b-6320-499d-8a60-290239d62da8",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:12.858571+00:00",
    "date_confidence": "high",
    "description": "At Linear, we're building the product development system for teams and agents. AI is fundamentally changing how software gets built, and we’re shaping the tools this new era requir"
  },
  {
    "company": "Linear",
    "source": "linear_official_careers",
    "job_id": "ea0b5868-6d7a-46fa-99d8-207cd19357a6",
    "title": "Design Engineer (Web & Brand)",
    "location": "Europe; European Union; Remote, European Union",
    "official_url": "https://jobs.ashbyhq.com/linear/ea0b5868-6d7a-46fa-99d8-207cd19357a6",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:12.858571+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.136s
- Company elapsed time: 0.448s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 37, 'usable_jd': 37}
- Raw jobs found: 135
- After US/location filtering: 106
- With trustworthy posted_date: 106
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
    "fetched_at": "2026-10-05T23:36:12.999349+00:00",
    "date_confidence": "high",
    "description": "Who are we? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  },
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "595a2d50-46a5-4ff9-af1c-d58cea9d8e68",
    "title": "Revenue Enablement Program Manager - EMEA",
    "location": "Europe; European Union; London; Remote, European Union",
    "official_url": "https://jobs.ashbyhq.com/cohere/595a2d50-46a5-4ff9-af1c-d58cea9d8e68",
    "posted_date": "2026-09-20",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:12.999349+00:00",
    "date_confidence": "high",
    "description": "Who are we? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
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
    "fetched_at": "2026-10-05T23:36:12.999349+00:00",
    "date_confidence": "high",
    "description": "Who are we? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  },
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "bde93d36-4a41-4c8c-bd98-b4e44f9061e4",
    "title": "Lead - US Government Affairs & Public Policy",
    "location": "Washington, DC; Washington, DC, Washington, DC, United States; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/cohere/bde93d36-4a41-4c8c-bd98-b4e44f9061e4",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:12.999349+00:00",
    "date_confidence": "high",
    "description": "Who are we? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
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
    "fetched_at": "2026-10-05T23:36:12.999349+00:00",
    "date_confidence": "high",
    "description": "Who are we? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  }
]
```

## Cisco

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cisco.wd5.myworkdayjobs.com/Cisco_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 44
- HTTP requests/cumulative request time: 250 / 67.380s
- Company elapsed time: 103.293s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 206 / 0 / 0
- Detail cache statuses: {'fetched:new': 202, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 73, 'usable_jd': 73}
- Raw jobs found: 828
- After US/location filtering: 206
- With trustworthy posted_date: 206
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.303, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 11.699, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.878, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 2.567, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.668, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.521, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.382, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.084, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 35, "stop_reason": "early_stop", "unique_contribution": 23, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 6.807, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.322, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 2, "query": "full stack backend", "raw_jobs": 40, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 10.432, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.957, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "cloud engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.975, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "security engineer remote", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.676, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "software engineer collaboration devices", "raw_jobs": 28, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 4.51, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "splunk engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.511, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "software engineer solution test iq platform", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2026363",
    "title": "Hardware Engineering Technical Leader",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Hardware-Engineering-Technical-Leader_2026363",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:13.448265+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 12/03/2026 Meet the Team The Common Hardware Group (CHG) creates innovative hardware platforms central to the AI era, power ing Cisc"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2022041",
    "title": "Detection Engineering Technical Leader",
    "location": "Denver, Colorado, US; Saint Paul, Minnesota, US; Boulder, Colorado, US; Houston, Texas, US; Knoxville, Tennessee, US; Chicago, Illinois, US; Philadelphia, Pennsylvania, US; Birmingham, Alabama, US; Portland, Oregon, US; Minneapolis, Minnesota, US; Elk Grove Village, Illinois, US; Dallas, Texas, US; Atlanta, Georgia, US; Little Rock, Arkansas, US; Hillsboro, Oregon, US; Colorado Springs, Colorado, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Denver-Colorado-US/Detection-Engineering-Technical-Leader_2022041-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:13.448265+00:00",
    "date_confidence": "high",
    "description": "The successful applicant will be performing work in FedRAMP High or IL-5 environments, and therefore, must be a U.S. Person ( i.e. U.S. citizen, U.S. national, lawful permanent res"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2021423",
    "title": "Distinguished Machine Learning Engineer, AISWP (Hybrid)",
    "location": "San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Distinguished-Machine-Learning-Engineer--AISWP---Hybrid-_2021423",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:13.448265+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 11/22/2026 This is a hybrid role based out of Cisco's San Jose office. Meet the team Cisco’s AI Software & Platform team (AISWP) is "
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2026474",
    "title": "Hardware Engineering Project Manager",
    "location": "San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Hardware-Engineering-Project-Manager_2026474",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:13.448265+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 11/04/2026 This is an onsite position at the San Jose, CA location. Meet the team The hardware engineering group creates innovative "
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2027035",
    "title": "ASIC Design Verification Engineer",
    "location": "Armenia",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Armenia/ASIC-Design-Verification-Engineer_2027035",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:36:13.448265+00:00",
    "date_confidence": "high",
    "description": "This is a hybrid role with four days per week at Cisco’s Yerevan office. Meet the Team The Silicon One team creates innovative hardware platforms central to the AI era, powering Ci"
  }
]
```

## SAP

- Status: empty
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 10
- HTTP requests/cumulative request time: 10 / 5.644s
- Company elapsed time: 5.984s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.733, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.495, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.646, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.577, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.536, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.563, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.598, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.496, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.79, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.548, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "cloud developer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}

## HPE

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://hpe.wd5.myworkdayjobs.com/Jobsathpe`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 282 / 169.251s
- Company elapsed time: 208.284s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 255 / 0 / 0
- Detail cache statuses: {'fetched:new': 245, 'fetched:missing_detail': 10}
- Relevant JD recovery: {'eligible': 99, 'usable_jd': 99}
- Raw jobs found: 467
- After US/location filtering: 255
- With trustworthy posted_date: 255
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 55.326, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 31.853, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 2.518, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 27.162, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 36.509, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 20.432, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.16, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.671, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 11.887, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.307, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "ai workflow specialist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 5}

Sample normalized records:

```json
[
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1209445",
    "title": "Senior AI Engineer Developer",
    "location": "Spring, Texas, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Spring-Texas-United-States-of-America/Senior-AI-Engineer-Developer_1209445-2",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:07.536723+00:00",
    "date_confidence": "high",
    "description": "Senior AI Engineer Developer This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enterprise is"
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
    "fetched_at": "2026-10-05T23:37:07.536723+00:00",
    "date_confidence": "high",
    "description": "AI/ML Engineer - Agentic This role has been designed as ‘Hybrid’ with an expectation that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Packard E"
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
    "fetched_at": "2026-10-05T23:37:07.536723+00:00",
    "date_confidence": "high",
    "description": "HPC and AI Performance Engineer This role has been designed as 'Hybrid' with a requirement that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Pac"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1209875",
    "title": "HPE Labs – AI/ML Research Scientist III",
    "location": "Milpitas, California, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Milpitas-California-United-States-of-America/HPE-Labs---AI-ML-Research-Scientist-III_1209875-2",
    "posted_date": "2026-07-13",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:07.536723+00:00",
    "date_confidence": "high",
    "description": "HPE Labs – AI/ML Research Scientist III This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard En"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1210921",
    "title": "Principal AI Research Scientist (HPE Labs)",
    "location": "Milpitas, California, United States of America; Westford, Massachusetts, United States of America; Spring, Texas, United States of America; Andover, Massachusetts, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Milpitas-California-United-States-of-America/HPE-Labs---Senior-AI-Researcher--Foundational-AI_1210921-2",
    "posted_date": "2026-08-16",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:07.536723+00:00",
    "date_confidence": "high",
    "description": "Principal AI Research Scientist (HPE Labs) This role has been designed as 'Hybrid' with a requirement that you will work on average 2 days per week from an HPE office. Who We Are: "
  }
]
```

## Disney

- Status: ok
- Scraping method: HTTP GET Disney server-rendered US search results
- Search URL/API: `https://www.disneycareers.com/en/search-jobs/software%20engineer/United%20States/391/1/2/6252001/39x76/-98x5/100/2`
- Pagination: ?p=1,2,3 per role query (intentional request cap)
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 28 / 10.908s
- Company elapsed time: 18.997s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 1 / 19 / 103
- Detail cache statuses: {'reused': 19, 'fetched:new': 1}
- Relevant JD recovery: {'deterministic_skip': 102, 'cache_reused': 19, 'eligible': 20, 'ai_skip': 1, 'detail_requests': 1, 'detail_success': 1, 'budget_deferred': 0, 'usable_jd': 20}
- Raw jobs found: 270
- After US/location filtering: 123
- With trustworthy posted_date: 2
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.328, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.043, "first_pass_survivors": 13, "group": "official", "jds_resolved": 0, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.888, "first_pass_survivors": 17, "group": "official", "jds_resolved": 0, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.879, "first_pass_survivors": 21, "group": "official", "jds_resolved": 0, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.038, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.404, "first_pass_survivors": 13, "group": "official", "jds_resolved": 0, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 2.205, "first_pass_survivors": 9, "group": "official", "jds_resolved": 0, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.066, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.917, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10150905",
    "title": "Manager - Applied AI",
    "location": "Burbank, California / Seattle, Washington",
    "official_url": "https://www.disneycareers.com/en/job/burbank/manager-applied-ai/391/95395074208",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:10.618569+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10161130",
    "title": "Director, AI Enablement & Legal Engineering",
    "location": "Burbank, California / New York, New York",
    "official_url": "https://www.disneycareers.com/en/job/burbank/director-ai-enablement-and-legal-engineering/391/101107920944",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:10.618569+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10160195",
    "title": "Senior Manager, AI & Machine Learning Engineering",
    "location": "Orlando, Florida / Burbank, California / Seattle, Washington",
    "official_url": "https://www.disneycareers.com/en/job/orlando/senior-manager-ai-and-machine-learning-engineering/391/101125079440",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:10.618569+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10132666",
    "title": "Lead Software Engineer-AI Licensing & Publishing Systems",
    "location": "Orlando, Florida / Glendale, California",
    "official_url": "https://www.disneycareers.com/en/job/orlando/lead-software-engineer-ai-licensing-and-publishing-systems/391/87032371952",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:10.618569+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10145558",
    "title": "Lead Product Manager - Data & AI Value Enablement",
    "location": "Orlando, Florida",
    "official_url": "https://www.disneycareers.com/en/job/orlando/lead-product-manager-data-and-ai-value-enablement/391/100391980224",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:10.618569+00:00",
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
- Pages/requests fetched: 18
- HTTP requests/cumulative request time: 70 / 37.992s
- Company elapsed time: 47.361s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 51 / 0 / 0
- Detail cache statuses: {'fetched:new': 50, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 12, 'usable_jd': 12}
- Raw jobs found: 240
- After US/location filtering: 51
- With trustworthy posted_date: 51
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 32.071, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.927, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.893, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.454, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 2.847, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 2.996, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 2.638, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 0.736, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.696, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}

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
    "fetched_at": "2026-10-05T23:37:29.387935+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0076601",
    "title": "AI Analytics Engineer - Traffic",
    "location": "Austin",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Austin/AI-Analytics-Engineer---Traffic_R0076601",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:29.387935+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0073091",
    "title": "Senior Python Engineer, AI",
    "location": "Remote, United States; Remote Arizona; Remote Oregon; Remote Colorado; Remote Nevada; Remote Washington; Remote New Mexico",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Remote-United-States/Senior-Python-Engineer--AI_R0073091",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:29.387935+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0072744",
    "title": "Traffic Engineer",
    "location": "Austin",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Austin/Traffic-Engineer_R0072744",
    "posted_date": "2026-09-22",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:29.387935+00:00",
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
    "fetched_at": "2026-10-05T23:37:29.387935+00:00",
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
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 159 / 32.583s
- Company elapsed time: 55.884s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 131 / 0 / 0
- Detail cache statuses: {'fetched:new': 121, 'fetched:missing_detail': 10}
- Relevant JD recovery: {'eligible': 48, 'usable_jd': 48}
- Raw jobs found: 261
- After US/location filtering: 131
- With trustworthy posted_date: 131
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.229, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.957, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.365, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 8.738, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.911, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.6, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.489, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.49, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.708, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3084706",
    "title": "Datacenter Software Program Manager",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446716318834",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:56.742099+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Services Group, Engineering Services Group > Program Management General Summary: The Qualcomm Datacenter is developing ha"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3089168",
    "title": "Datacenter Software Program Manager, Senior",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446717843734",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:56.742099+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Services Group, Engineering Services Group > Program Management General Summary: General Summary: The Qualcomm Datacenter"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3092198",
    "title": "Technical Program Manager, Data Center Platform",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446718719975",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:56.742099+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Services Group, Engineering Services Group > Program Management General Summary: The Qualcomm Datacenter team stands at t"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3092199",
    "title": "Data Center Technical Software Program Manager",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446718719976",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:56.742099+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Services Group, Engineering Services Group > Program Management General Summary: The Qualcomm Datacenter team stands at t"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3094556",
    "title": "Chipset/Chip Program Manager",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720198613",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:37:56.742099+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Services Group, Engineering Services Group > Program Management General Summary: The Qualcomm Datacenter team stands at t"
  }
]
```

## AMD

- Status: ok
- Scraping method: HTTP GET public Jibe/iCIMS jobs JSON
- Search URL/API: `https://careers.amd.com/api/jobs`
- Pagination: page=1,2,... per role query; stop on total/empty/repeat/short page
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 14 / 8.571s
- Company elapsed time: 10.631s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 206, 'usable_jd': 206}
- Raw jobs found: 1270
- After US/location filtering: 496
- With trustworthy posted_date: 496
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.769, "first_pass_survivors": 335, "group": "official", "jds_resolved": 335, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 335, "stop_reason": "page_budget", "unique_contribution": 335, "unique_jobs": 335}
- Query diagnostic: {"elapsed_seconds": 0.547, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning", "raw_jobs": 100, "stop_reason": "early_stop", "unique_contribution": 32, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.238, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 2.051, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "AI research", "raw_jobs": 235, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 235}
- Query diagnostic: {"elapsed_seconds": 2.024, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 300}

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
    "updated_date": "2026-10-03",
    "fetched_at": "2026-10-05T23:38:16.749710+00:00",
    "date_confidence": "high",
    "description": "WHAT YOU DO AT AMD CHANGES EVERYTHING At AMD, our mission is to build great products that accelerate next-generation computing experiences—from AI and data centers, to PCs, gaming "
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "93216",
    "title": "Principal Software Engineer — AI Performance & Reliability",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-10-01",
    "updated_date": "2026-10-03",
    "fetched_at": "2026-10-05T23:38:16.749710+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "86744",
    "title": "Sr. Software Engineer - AI Triton Kernels",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-08-07",
    "updated_date": "2026-10-03",
    "fetched_at": "2026-10-05T23:38:16.749710+00:00",
    "date_confidence": "high",
    "description": "WHAT YOU DO AT AMD CHANGES EVERYTHING At AMD, our mission is to build great products that accelerate next-generation computing experiences—from AI and data centers, to PCs, gaming "
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92526",
    "title": "2027 PhD AI Model Optimization & Software Engineer Intern/Co-op",
    "location": "Austin, Texas",
    "official_url": "",
    "posted_date": "2026-09-16",
    "updated_date": "2026-09-17",
    "fetched_at": "2026-10-05T23:38:16.749710+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92754",
    "title": "Staff Software Development Engineer: GPU, AI/ML Ops & Quality Engineering",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-09-23",
    "updated_date": "2026-09-26",
    "fetched_at": "2026-10-05T23:38:16.749710+00:00",
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
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 70 / 22.140s
- Company elapsed time: 31.443s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 50 / 0 / 0
- Detail cache statuses: {'fetched:new': 49, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 26, 'usable_jd': 26}
- Raw jobs found: 211
- After US/location filtering: 50
- With trustworthy posted_date: 50
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 15.351, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 34, "stop_reason": "early_stop", "unique_contribution": 34, "unique_jobs": 34}
- Query diagnostic: {"elapsed_seconds": 0.773, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.434, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 5.357, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 3.837, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 2.162, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 50, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 50}
- Query diagnostic: {"elapsed_seconds": 0.475, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.48, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 2.059, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 27}

Sample normalized records:

```json
[
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19731",
    "title": "Full Stack Developer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Full-Stack-Developer_R19731-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:38:27.381557+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect As a Full Stack Developer at Zoom, you will take end-to-end ownership of features and services that reach users worldwide, from design through deployment, monit"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19444",
    "title": "AI Engineer - AI Verticals",
    "location": "San Jose (CA); Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Staff-AI-Engineer---AI-Verticals_R19444-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:38:27.381557+00:00",
    "date_confidence": "high",
    "description": "What you can expect As an AI Engineer specializing in Agentic AI, you will develop intelligent agents that can autonomously perceive, reason, and act in dynamic environments as par"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19728",
    "title": "Contact Center - Consulting Solution Engineer",
    "location": "Denver (CO)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Denver-CO/Contact-Center---Consulting-Solution-Engineer_R19728-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:38:27.381557+00:00",
    "date_confidence": "high",
    "description": "Zoom is looking to grow its global Contact Center Solution Engineering team. Do you have a passion for working with customers? Do you have experience working in the Contact Center "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R17675",
    "title": "Principal DevOps Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Principal-DevOps-Engineer_R17675",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:38:27.381557+00:00",
    "date_confidence": "high",
    "description": "We are seeking a Principal DevOps Engineer who combines deep technical expertise with broad system understanding. This engineer should be capable of diving into a wide range of ser"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19522",
    "title": "Zoom AI DevOps Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/ZoomAI-DevOps-Engineer_R19522-2",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:38:27.381557+00:00",
    "date_confidence": "high",
    "description": "What you can expect As a Zoom AI DevOps Engineer, you can expect to work on high-impact, large-scale systems that support ZoomAI and Machine Learning services. You'll be part of a "
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
- HTTP requests/cumulative request time: 1 / 0.203s
- Company elapsed time: 1.251s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 62, 'usable_jd': 62}
- Raw jobs found: 356
- After US/location filtering: 210
- With trustworthy posted_date: 210
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8145906",
    "title": "Account Executive, Commercial (Upstate New York)",
    "location": "Remote, New York; New York, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8145906",
    "posted_date": "2026-08-24",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-10-05T23:38:52.626880+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8180695",
    "title": "Account Executive, Enterprise (Chicago)",
    "location": "Remote, Illinois; Illinois, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8180695",
    "posted_date": "2026-09-21",
    "updated_date": "2026-09-21",
    "fetched_at": "2026-10-05T23:38:52.626880+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8159371",
    "title": "Account Executive, Enterprise (Indianapolis)",
    "location": "Indianapolis, Indiana; Remote, Indiana; Indiana, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8159371",
    "posted_date": "2026-09-04",
    "updated_date": "2026-09-04",
    "fetched_at": "2026-10-05T23:38:52.626880+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8059788",
    "title": "Account Executive, Enterprise (Los Angeles/Orange County)",
    "location": "Remote, California; California, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8059788",
    "posted_date": "2026-07-13",
    "updated_date": "2026-08-11",
    "fetched_at": "2026-10-05T23:38:52.626880+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8226648",
    "title": "Account Executive, Federal (Intelligence Community)",
    "location": "Remote, Virginia; Virginia, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8226648",
    "posted_date": "2026-09-24",
    "updated_date": "2026-09-24",
    "fetched_at": "2026-10-05T23:38:52.626880+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.325s
- Company elapsed time: 2.817s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 69, 'usable_jd': 69}
- Raw jobs found: 889
- After US/location filtering: 497
- With trustworthy posted_date: 497
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "7726495002",
    "title": "Account Executive, Singapore",
    "location": "Singapore; APAC",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=7726495002",
    "posted_date": "2025-05-09",
    "updated_date": "2026-09-21",
    "fetched_at": "2026-10-05T23:38:53.878718+00:00",
    "date_confidence": "high",
    "description": "<p class=\"p1\">As we continue to increase our presence in the world of Unified Data Analytics and AI, we're looking for a creative, driven, and execution-oriented Enterprise Account"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8756154002",
    "title": "Accounting Manager, Accounts Receivable",
    "location": "Austin, Texas; Denver, Colorado; Portland, Oregon; Scottsdale, Arizona, United States; San Francisco, California",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8756154002",
    "posted_date": "2026-09-22",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:38:53.878718+00:00",
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
    "updated_date": "2026-09-30",
    "fetched_at": "2026-10-05T23:38:53.878718+00:00",
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
    "updated_date": "2026-09-30",
    "fetched_at": "2026-10-05T23:38:53.878718+00:00",
    "date_confidence": "high",
    "description": "<p><span style=\"text-decoration: underline;\"><strong>PLEASE NOTE</strong></span><strong>: <br></strong>Due to federal contract requirements and client site access obligations, <str"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "7803651002",
    "title": "AI Transformation Leader",
    "location": "United States; Remote - New York",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=7803651002",
    "posted_date": "2026-08-25",
    "updated_date": "2026-09-21",
    "fetched_at": "2026-10-05T23:38:53.878718+00:00",
    "date_confidence": "high",
    "description": "<p data-renderer-start-pos=\"1648\">With the most complete data &amp; AI stack on the market, Databricks is well suited to be the strategic partner for our customers’ AI transformati"
  }
]
```

## Roblox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roblox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.156s
- Company elapsed time: 1.122s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 29, 'usable_jd': 29}
- Raw jobs found: 254
- After US/location filtering: 237
- With trustworthy posted_date: 237
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8143982",
    "title": "[2027] Associate Product Designer, Early Career",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8143982?gh_jid=8143982",
    "posted_date": "2026-09-02",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:38:56.696711+00:00",
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
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:38:56.696711+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8072244",
    "title": "[2027] Software Engineer, Early Career",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8072244?gh_jid=8072244",
    "posted_date": "2026-08-05",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:38:56.696711+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8120368",
    "title": "Business Operations Associate",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8120368?gh_jid=8120368",
    "posted_date": "2026-08-13",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:38:56.696711+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8211789",
    "title": "Compensation Programs Senior Analyst",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8211789?gh_jid=8211789",
    "posted_date": "2026-09-18",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:38:56.696711+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.138s
- Company elapsed time: 0.701s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 150
- After US/location filtering: 93
- With trustworthy posted_date: 93
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
    "fetched_at": "2026-10-05T23:38:57.819939+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8214444",
    "title": "Business Systems Engineer, Tech Foundations",
    "location": "San Francisco, CA; United States",
    "official_url": "https://careers.airbnb.com/positions/8214444?gh_jid=8214444",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:38:57.819939+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "7839229",
    "title": "Community Support Forecasting and Demand Planning Analyst",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/7839229?gh_jid=7839229",
    "posted_date": "2026-04-24",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:38:57.819939+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8152131",
    "title": "Complex Claims Manager",
    "location": "Canada; United States",
    "official_url": "https://careers.airbnb.com/positions/8152131?gh_jid=8152131",
    "posted_date": "2026-08-24",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:38:57.819939+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8153094",
    "title": "Complex Claims Manager",
    "location": "United States; Canada",
    "official_url": "https://careers.airbnb.com/positions/8153094?gh_jid=8153094",
    "posted_date": "2026-08-24",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:38:57.819939+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.308s
- Company elapsed time: 3.494s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 150, 'usable_jd': 150}
- Raw jobs found: 644
- After US/location filtering: 514
- With trustworthy posted_date: 514
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "4461450008",
    "title": "Account Executive, AI Native",
    "location": "New York City, NY; San Francisco, CA | New York City, NY; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/4461450008",
    "posted_date": "2024-12-20",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-10-05T23:38:58.522376+00:00",
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
    "fetched_at": "2026-10-05T23:38:58.522376+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5398438008",
    "title": "AI Deployment Specialist, Beneficial Deployments",
    "location": "San Francisco, CA | New York City, NY; New York, New York, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5398438008",
    "posted_date": "2026-09-11",
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:38:58.522376+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5382750008",
    "title": "AI Infrastructure Operations, Demand Planning",
    "location": "San Francisco, CA | New York City, NY; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5382750008",
    "posted_date": "2026-08-11",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-10-05T23:38:58.522376+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5391151008",
    "title": "AI Operations Engineer, Partnerships",
    "location": "San Francisco, CA; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5391151008",
    "posted_date": "2026-08-14",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-10-05T23:38:58.522376+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.682s
- Company elapsed time: 1.034s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 44
- After US/location filtering: 30
- With trustworthy posted_date: 30
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4705316006",
    "title": "Agency Growth Lead",
    "location": "Toronto; Remote - United States",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4705316006?gh_jid=4705316006",
    "posted_date": "2026-08-14",
    "updated_date": "2026-09-16",
    "fetched_at": "2026-10-05T23:38:58.825905+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4686202006",
    "title": "Associate Product Manager",
    "location": "Palo Alto, CA",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4686202006?gh_jid=4686202006",
    "posted_date": "2026-06-02",
    "updated_date": "2026-09-22",
    "fetched_at": "2026-10-05T23:38:58.825905+00:00",
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
    "updated_date": "2026-09-02",
    "fetched_at": "2026-10-05T23:38:58.825905+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-10-05T23:38:58.825905+00:00",
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
    "fetched_at": "2026-10-05T23:38:58.825905+00:00",
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
- HTTP requests/cumulative request time: 24 / 24.247s
- Company elapsed time: 28.017s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 229, 'usable_jd': 229}
- Raw jobs found: 1065
- After US/location filtering: 445
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.122, "first_pass_survivors": 146, "group": "official", "jds_resolved": 146, "original_postings_resolved": 146, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 146, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.407, "first_pass_survivors": 99, "group": "official", "jds_resolved": 99, "original_postings_resolved": 99, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 99, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.105, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 105, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 105}
- Query diagnostic: {"elapsed_seconds": 3.294, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 147}
- Query diagnostic: {"elapsed_seconds": 3.177, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.113, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 1.897, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 57, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 0.812, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 4.089, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 150}

Sample normalized records:

```json
[
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7668212952030841093",
    "title": "Software Engineer Intern (AI Platform) - 2027 Summer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7668212952030841093",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:38:59.866325+00:00",
    "date_confidence": "unknown",
    "description": "The AI Platform team is a team focusing on building advanced end-to-end AI production pipelines, including deep learning model training, optimization, deployment and applications. "
  },
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7669859743775000885",
    "title": "Software Engineer Graduate (Data-Intelligent Creation-AI Platform-Global Vision Engineering) - 2027 Start",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7669859743775000885",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:38:59.866325+00:00",
    "date_confidence": "unknown",
    "description": "The Intelligent Creation - AI Platform team is a team focusing on building advanced end-to-end AI production pipelines, including deep learning model training, optimization, deploy"
  },
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7571650125270370613",
    "title": "Machine Learning Engineer, AI Coding Tools",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7571650125270370613",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:38:59.866325+00:00",
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
    "fetched_at": "2026-10-05T23:38:59.866325+00:00",
    "date_confidence": "unknown",
    "description": "About the Team Join ByteDance’s database R&D team, where you’ll build and own cutting-edge database products supporting Bytedance’s global infrastructure. Our diverse portfolio inc"
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
    "fetched_at": "2026-10-05T23:38:59.866325+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.108s
- Company elapsed time: 0.582s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 14, 'usable_jd': 14}
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
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:39:02.017588+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role</h2> <p>Chime's Data Science &amp; Machine Learning team builds the models, services, and platforms behind how millions of members manage and grow their financia"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8684363002",
    "title": "Associate Creative Director, Growth Marketing",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8684363002?gh_jid=8684363002",
    "posted_date": "2026-08-26",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:39:02.017588+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the Role</strong></h2> <p>As our Performance Creative Program expands, we're looking for an experienced Associate Creative Director to guide a team of designers, "
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8584952002",
    "title": "Business Control Manager",
    "location": "Chicago, IL, USA; New York, NY, USA; San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8584952002?gh_jid=8584952002",
    "posted_date": "2026-06-18",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:39:02.017588+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role</h2> <p>We are hiring a <strong>Business Control Manager</strong> to join our Compliance team at Chime, where you will be responsible for strengthening the first"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8840795002",
    "title": "Creative Director, Campaigns",
    "location": "New York, NY, USA; San Francisco, CA, USA; New York Office",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8840795002?gh_jid=8840795002",
    "posted_date": "2026-09-23",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:39:02.017588+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role</h2> <p>Chime is looking for a Creative Director to shape what our brand looks, sounds and feels like — and to turn that into work people actually talk about.</p"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8681193002",
    "title": "Director Engineering",
    "location": "New York, NY, USA; San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8681193002?gh_jid=8681193002",
    "posted_date": "2026-08-10",
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:39:02.017588+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the role</strong></h2> <p>Chime is looking for a Director of Engineering to lead our AI &amp; App Experience (AAX) organization — the team building the next gener"
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
- HTTP requests/cumulative request time: 123 / 29.943s
- Company elapsed time: 47.992s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 98 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 96}
- Relevant JD recovery: {'eligible': 29, 'usable_jd': 29}
- Raw jobs found: 470
- After US/location filtering: 98
- With trustworthy posted_date: 98
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.764, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.574, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.686, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 7.122, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.225, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.21, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.396, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.154, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 2.861, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "298717",
    "title": "AI Solution Engineer, Security",
    "location": "Round Rock, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/298717",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:02.601300+00:00",
    "date_confidence": "high",
    "description": "AI Solution Engineer, Security The Dell Security & Resiliency organization manages the security risk across all aspects of Dell’s business. We are currently experiencing incredible"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "295521",
    "title": "Senior Principal Software Engineer - (ServiceNow Technical Architect)",
    "location": "Round Rock, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/295521",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:02.601300+00:00",
    "date_confidence": "high",
    "description": "Senior ServiceNow Developer (ServiceNow Technical Architect) Be a part of a team that’s ensuring Dell Technologies' product integrity and customer satisfaction. Our IT Software Eng"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "298110",
    "title": "Technical Support Engineer 2 - AI Networking",
    "location": "Round Rock, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/298110",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:02.601300+00:00",
    "date_confidence": "high",
    "description": "Technical Support Engineer 2 – Dell & Nvidia AI Networking At Dell Technologies, world-class service doesn’t end when a customer purchases our innovative products. Our Technical Su"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "296687",
    "title": "Principal Engineer - Enterprise DevOps & ALM Platforms",
    "location": "Hopkinton, MA, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/296687",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:02.601300+00:00",
    "date_confidence": "high",
    "description": "Principal Engineer - Enterprise DevOps & ALM Platforms Software Engineering delivers innovative platforms, tools, and services that enable teams across Dell Technologies to acceler"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "299014",
    "title": "Agentic Context Engineering Architect & AI Practitioner",
    "location": "Hopkinton, MA, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/299014",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:02.601300+00:00",
    "date_confidence": "high",
    "description": "SUMMARY Agentic Context Engineering Architect & AI Practitioner Join us to do the best work of your career and make a profound social impact as an Agentic Context Engineering Archi"
  }
]
```

## Dropbox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/dropbox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.303s
- Company elapsed time: 0.473s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 40
- After US/location filtering: 32
- With trustworthy posted_date: 32
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
    "updated_date": "2026-09-08",
    "fetched_at": "2026-10-05T23:39:27.883907+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z95gas6hz75zjz77zz90zpz71zz80zeoz80zz68zlz66z"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8048847",
    "title": "Business Development Manager, Strategic Partnerships",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8048847?gh_jid=8048847",
    "posted_date": "2026-07-22",
    "updated_date": "2026-09-03",
    "fetched_at": "2026-10-05T23:39:27.883907+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qowz80zsz81z8nqz122zdfz68z5coz87zsz73zz76zipqu3z86zmz88zz81zcth"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8048848",
    "title": "Business Development Manager, Strategic Partnerships",
    "location": "Remote - Canada: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8048848?gh_jid=8048848",
    "posted_date": "2026-07-22",
    "updated_date": "2026-09-03",
    "fetched_at": "2026-10-05T23:39:27.883907+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qowz80zsz81z8nqz122zdfz68z5coz87zsz73zz76zipqu3z86zmz88zz81zcth"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8137896",
    "title": "Customer Evidence Manager",
    "location": "Remote - Canada: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8137896?gh_jid=8137896",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-10-05T23:39:27.883907+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p>Dropbox is hiring a Customer Evidence Manager to<span class=\"thread-482953488634939485839339\"> own</span> <span clas"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8137895",
    "title": "Customer Evidence Manager",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8137895?gh_jid=8137895",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-10-05T23:39:27.883907+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p>Dropbox is hiring a Customer Evidence Manager to<span class=\"thread-482953488634939485839339\"> own</span> <span clas"
  }
]
```

## Expedia Group

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://expedia.wd108.myworkdayjobs.com/search`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 78 / 21.367s
- Company elapsed time: 32.620s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 57 / 0 / 0
- Detail cache statuses: {'fetched:new': 57}
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 367
- After US/location filtering: 57
- With trustworthy posted_date: 57
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 16.055, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.546, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 46}
- Query diagnostic: {"elapsed_seconds": 0.646, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 3.799, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 51, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 51}
- Query diagnostic: {"elapsed_seconds": 1.7, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.98, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.656, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.249, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.988, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109591",
    "title": "Senior Product Manager Loyalty Co-Brand Credit Card",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Senior-Product-Manager-Loyalty-Co-Brand-Credit-Card_R-109591",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:28.363104+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109571",
    "title": "Product Manager III, Recommendations Platform",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Product-Manager-III--Recommendations-Platform_R-109571-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:28.363104+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-103344",
    "title": "Senior Software Development Engineer, Loyalty - Full Stack",
    "location": "USA - California - San Jose",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---California---San-Jose/Sr-Software-Development-Engineer--Loyalty---Full-Stack_R-103344-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:28.363104+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-110073",
    "title": "Global Data Sharing Engineer",
    "location": "Washington - Seattle Campus; Austin Domain 11 - HomeAway",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Global-Data-Sharing-Engineer_R-110073-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:28.363104+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-107578",
    "title": "Senior Machine Learning Scientist - Agentic Experience",
    "location": "USA - California - San Jose; Austin Domain 11 - HomeAway; Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---California---San-Jose/Senior-Machine-Learning-Scientist---Agentic-Experience_R-107578-2",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:28.363104+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.213s
- Company elapsed time: 0.403s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 137
- After US/location filtering: 29
- With trustworthy posted_date: 29
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
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:39:50.594804+00:00",
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
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-05T23:39:50.594804+00:00",
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
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:39:50.594804+00:00",
    "date_confidence": "high",
    "description": "<p><strong>***Now accepting applications for a November 3rd, 2026 start date***</strong></p> <p>As an Account Executive on the Small Business sales team, you will identify, source,"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8128853",
    "title": "Manager, Analytics Engineering, Data & AI Foundations",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8128853?gh_jid=8128853",
    "posted_date": "2026-08-26",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:39:50.594804+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-33330</strong></p> <hr> <p><strong>Manager, Analytics Engineering, Data &amp; AI Foundations</strong></p> <p>HubSpot's mission is to Help Millions of Organizations G"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8031160",
    "title": "Outbound Business Development Representative (BDR)",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8031160?gh_jid=8031160",
    "posted_date": "2026-06-29",
    "updated_date": "2026-09-30",
    "fetched_at": "2026-10-05T23:39:50.594804+00:00",
    "date_confidence": "high",
    "description": "<p><strong>🚀 Join HubSpot as an Outbound Business Development Representative (BDR)</strong><strong><br></strong>&nbsp;📍 Remote (USA) or Cambridge, MA, USA<em><br></em></p> <p><stro"
  }
]
```

## Instacart

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/instacart/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.139s
- Company elapsed time: 0.659s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 122
- After US/location filtering: 108
- With trustworthy posted_date: 108
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
    "fetched_at": "2026-10-05T23:39:50.999188+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "7144697",
    "title": "Activation Sales Development Representative I",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=7144697",
    "posted_date": "2025-08-07",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-10-05T23:39:50.999188+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8145998",
    "title": "AI Solutions Lead, Marketing",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8145998",
    "posted_date": "2026-08-20",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-10-05T23:39:50.999188+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8146070",
    "title": "AI Solutions Lead, Marketing",
    "location": "Canada - Remote (ON, AB, BC, or NS Only); Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8146070",
    "posted_date": "2026-08-20",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-10-05T23:39:50.999188+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8212434",
    "title": "B2B Event Marketing Manager (6-Month Contract)",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8212434",
    "posted_date": "2026-09-17",
    "updated_date": "2026-09-17",
    "fetched_at": "2026-10-05T23:39:50.999188+00:00",
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
- HTTP requests/cumulative request time: 172 / 77.273s
- Company elapsed time: 101.786s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 144 / 0 / 0
- Detail cache statuses: {'fetched:new': 141, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 85, 'usable_jd': 85}
- Raw jobs found: 487
- After US/location filtering: 144
- With trustworthy posted_date: 144
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 31.399, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 11.101, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 5.807, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 11.108, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 14.457, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 10.444, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.064, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 1.332, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 7.089, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 79}

Sample normalized records:

```json
[
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0281978",
    "title": "AI Performance Library Architect",
    "location": "US, Oregon, Hillsboro; US, California, Folsom",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/AI-Performance-Library-Architect_JR0281978-1",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:51.659564+00:00",
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
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:51.659564+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel's Neuromorphic Computing Lab has been at the forefront of brain-inspired computing for nearly a decade, working alongside a global ecosystem of "
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0287524",
    "title": "AI Solution Architect - Graduate Intern",
    "location": "US, California, Santa Clara",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-California-Santa-Clara/AI-Solution-Architect---Graduate-Intern_JR0287524",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:51.659564+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel is seeking an AI Infrastructure Solution Architect Intern to join our AI Platforms team. As an intern, you will work alongside experienced engin"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0287531",
    "title": "AI Solution Architect - Undergraduate Intern",
    "location": "US, Oregon, Hillsboro",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/AI-Solution-Architect---Graduate-Intern_JR0287531",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:39:51.659564+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel is seeking an AI Infrastructure Solution Architect Intern to join our AI Platforms team. As an intern, you will work alongside experienced engin"
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
    "fetched_at": "2026-10-05T23:39:51.659564+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel is seeking an AI Infrastructure Solution Architect Intern to join our AI Platforms team. As an intern, you will work alongside experienced engin"
  }
]
```

## MathWorks

- Status: ok
- Scraping method: HTTP GET server-rendered MathWorks search + JobPosting JSON-LD
- Search URL/API: `https://www.mathworks.com/company/jobs/opportunities/search/`
- Pagination: page=2,3,... after the unnumbered first page; stop on empty/repeat/short page
- Pages/requests fetched: 10
- HTTP requests/cumulative request time: 44 / 15.215s
- Company elapsed time: 17.168s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 34 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 88
- After US/location filtering: 34
- With trustworthy posted_date: 34
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.01, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.499, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 1.313, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 3.168, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.474, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 1.054, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.524, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.492, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.634, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 22}

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
    "fetched_at": "2026-10-05T23:40:00.984477+00:00",
    "date_confidence": "high",
    "description": "<p>About this Program</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37011",
    "title": "Senior Applied AI Engineer",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37011-senior-applied-ai-engineer?keywords=ai+engineer",
    "posted_date": "2026-04-23",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:00.984477+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37010",
    "title": "Senior Applied AI Engineer",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37010-senior-applied-ai-engineer?keywords=ai+engineer",
    "posted_date": "2026-04-23",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:00.984477+00:00",
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
    "fetched_at": "2026-10-05T23:40:00.984477+00:00",
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
    "fetched_at": "2026-10-05T23:40:00.984477+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.252s
- Company elapsed time: 1.306s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 50, 'usable_jd': 50}
- Raw jobs found: 393
- After US/location filtering: 249
- With trustworthy posted_date: 249
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7318558",
    "title": "Account Development Representative",
    "location": "Gurugram; Gurugram, Haryana, India",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7318558",
    "posted_date": "2026-07-27",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:18.152850+00:00",
    "date_confidence": "high",
    "description": "<p>An Account Development Representative at MongoDB is the starting point for building a serious career in technology sales.&nbsp;</p> <p>This role is the foundation of our sales o"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7310506",
    "title": "Account Development Representative",
    "location": "New York City; New York, NY, United States",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7310506",
    "posted_date": "2025-10-15",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:18.152850+00:00",
    "date_confidence": "high",
    "description": "<p>At MongoDB, our Account Development team works closely with our partners in both Sales and Marketing to build fanatical customer enthusiasm around MongoDB. ADR reps are responsi"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7310552",
    "title": "Account Development Representative",
    "location": "Boston; Boston, MA, United States",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7310552",
    "posted_date": "2025-10-22",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:18.152850+00:00",
    "date_confidence": "high",
    "description": "<p>At MongoDB, our Account Development team works closely with our partners in both Sales and Marketing to build fanatical customer enthusiasm around MongoDB. ADR reps are responsi"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "8079914",
    "title": "Account Development Representative - English Speaking",
    "location": "Kuala Lumpur; MYS_KualaLumpur",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=8079914",
    "posted_date": "2026-07-23",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:18.152850+00:00",
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
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:18.152850+00:00",
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
- HTTP requests/cumulative request time: 143 / 28.800s
- Company elapsed time: 48.952s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 118 / 0 / 0
- Detail cache statuses: {'fetched:new': 114, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 232
- After US/location filtering: 118
- With trustworthy posted_date: 118
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.56, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.687, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.488, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 6.814, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.6, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.533, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 9.455, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.507, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.893, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR038489",
    "title": "Vice President, Human Resources Strat/Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549798077475",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:19.459640+00:00",
    "date_confidence": "high",
    "description": "Morgan Stanley Human Resources is seeking an experienced Strat/Engineer in New York to build and own internal HR applications, data services, and workflow solutions that improve ho"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR041991",
    "title": "Technical Program Manager - Vice President",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549799519552",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:19.459640+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR041902",
    "title": "AI Engineer - VP",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549799501420",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:19.459640+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "JR042832",
    "title": "Associate, Software Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800007925",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:19.459640+00:00",
    "date_confidence": "high",
    "description": "Company Profile: Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment, and wealth management services. Th"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR041494",
    "title": "VP, Generative AI, Backend Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549799388181",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:19.459640+00:00",
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
- HTTP requests/cumulative request time: 113 / 36.662s
- Company elapsed time: 56.060s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 84 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 38, 'usable_jd': 38}
- Raw jobs found: 435
- After US/location filtering: 84
- With trustworthy posted_date: 84
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 18.959, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.262, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 5.709, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 7.42, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.263, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 6.319, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 3.551, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.408, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.168, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "98734011664",
    "title": "Principal Engineer, AI BU",
    "location": "San Jose, California, United States; United States; Morrisville, North Carolina, United States",
    "official_url": "https://careers.netapp.com/en/job/san-jose/principal-engineer-ai-bu/27600/98734011664",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:22.947458+00:00",
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
    "fetched_at": "2026-10-05T23:40:22.947458+00:00",
    "date_confidence": "high",
    "description": "Job Summary Distinguished Engineer - AI Infrastructure We are seeking a Distinguished Engineer with unrivaled depth in AI/ML inferencing at scale and the distributed systems founda"
  },
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "101273235968",
    "title": "Software Engineer AI BU",
    "location": "San Jose, California, United States; United States; Morrisville, North Carolina, United States",
    "official_url": "https://careers.netapp.com/en/job/san-jose/software-engineer-ai-bu/27600/101273235968",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:22.947458+00:00",
    "date_confidence": "high",
    "description": "Job Summary As a Senior Engineer in NetApp's AI BU, you are a strong, trusted technical contributor — designing and building complex systems within your team while beginning to ext"
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
    "fetched_at": "2026-10-05T23:40:22.947458+00:00",
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
    "fetched_at": "2026-10-05T23:40:22.947458+00:00",
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
- HTTP requests/cumulative request time: 10 / 3.500s
- Company elapsed time: 4.555s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 1 / 50 / 6
- Detail cache statuses: {'reused': 50, 'fetched:new': 1}
- Relevant JD recovery: {'cache_reused': 50, 'eligible': 51, 'deterministic_skip': 2, 'ai_skip': 4, 'detail_requests': 1, 'detail_success': 1, 'budget_deferred': 0, 'usable_jd': 51}
- Raw jobs found: 90
- After US/location filtering: 57
- With trustworthy posted_date: 57
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.569, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.424, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.411, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.529, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.354, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.478, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.517, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.374, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.392, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}

Sample normalized records:

```json
[
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "AJRT30201",
    "title": "AI Engineer 6 - AI Foundation & Tooling, Ads Platform",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790298014263",
    "posted_date": "2024-07-23",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:35.821403+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR42022",
    "title": "AI Research Engineer 6 - TL, Algo Core - AI for Member Systems",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790317717814",
    "posted_date": "2026-08-08",
    "updated_date": "2026-08-08",
    "fetched_at": "2026-10-05T23:40:35.821403+00:00",
    "date_confidence": "high",
    "description": "At Netflix, our mission is to entertain the world. Together, we are writing the next episode - pushing the boundaries of storytelling, global fandom and making the unimaginable a r"
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR42630",
    "title": "Software Engineer L5 - AI Observability & Agent Evaluation",
    "location": "Los Gatos,California,United States of America",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790318510397",
    "posted_date": "2026-09-16",
    "updated_date": "2026-09-16",
    "fetched_at": "2026-10-05T23:40:35.821403+00:00",
    "date_confidence": "high",
    "description": "At Netflix, our mission is to entertain the world. Together, we are writing the next episode - pushing the boundaries of storytelling, global fandom and making the unimaginable a r"
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR41100",
    "title": "Software Engineer 5 – Agent Platform, AI Platform",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790316292023",
    "posted_date": "2026-06-09",
    "updated_date": "2026-07-13",
    "fetched_at": "2026-10-05T23:40:35.821403+00:00",
    "date_confidence": "high",
    "description": "At Netflix, our mission is to entertain the world. Together, we are writing the next episode - pushing the boundaries of storytelling, global fandom and making the unimaginable a r"
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR40898",
    "title": "Software Engineer 4/5 – Model Development and Management, AI Platform",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790316165312",
    "posted_date": "2026-06-01",
    "updated_date": "2026-06-01",
    "fetched_at": "2026-10-05T23:40:35.821403+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.533s
- Company elapsed time: 2.707s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 359, 'usable_jd': 359}
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
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://jobs.ashbyhq.com/openai/8fb1615c-34bf-47c4-a1d1-b7b2f836bbd3",
    "posted_date": "2026-03-12",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:39.871523+00:00",
    "date_confidence": "high",
    "description": "ABOUT THE TEAM The compute infrastructure team runs the GPU fleet and large-scale compute clusters that serve the models backing ChatGPT and the API, while also supporting training"
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
    "fetched_at": "2026-10-05T23:40:39.871523+00:00",
    "date_confidence": "high",
    "description": "By applying to this role, you will be considered for Research Engineer roles across all teams at OpenAI. About the Role As a Research Engineer here, you will be responsible for bui"
  },
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "7322d344-9325-4a92-8445-0a2c4e9272f8",
    "title": "Research Engineer, Retrieval & Search, Applied Engineering",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://jobs.ashbyhq.com/openai/7322d344-9325-4a92-8445-0a2c4e9272f8",
    "posted_date": "2024-03-20",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:39.871523+00:00",
    "date_confidence": "high",
    "description": "About the Team We bring OpenAI's technology to the world through products like ChatGPT and the OpenAI API. We seek to learn from deployment and distribute the benefits of AI, while"
  },
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "0b428c6d-7c06-4feb-82b6-5bbe5cda2a18",
    "title": "Account Director, Startups",
    "location": "São Paulo; Sao Paulo, Brazil, Brazil; Remote, Brazil",
    "official_url": "https://jobs.ashbyhq.com/openai/0b428c6d-7c06-4feb-82b6-5bbe5cda2a18",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:39.871523+00:00",
    "date_confidence": "high",
    "description": "About the Team OpenAI’s mission is to build safe artificial general intelligence (AGI) which benefits all of humanity. This long-term undertaking brings the world’s best scientists"
  },
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "2560ed50-5535-42b8-b069-9ebc28ce7493",
    "title": "Researcher, Robustness & Safety Training",
    "location": "San Francisco; San Francisco, California, United States; London, UK",
    "official_url": "https://jobs.ashbyhq.com/openai/2560ed50-5535-42b8-b069-9ebc28ce7493",
    "posted_date": "2023-05-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:39.871523+00:00",
    "date_confidence": "high",
    "description": "ABOUT THE TEAM The Safety Systems team https://openai.com/safety/safety-systems is responsible for various safety work to ensure our best models can be safely deployed to the real "
  }
]
```

## Palantir

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/palantir`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.485s
- Company elapsed time: 0.993s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 2 / 0
- Detail cache statuses: {'reused': 2}
- Relevant JD recovery: {'eligible': 188, 'cache_reused': 2, 'usable_jd': 188}
- Raw jobs found: 318
- After US/location filtering: 245
- With trustworthy posted_date: 245
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "a237973c-cb29-41fe-9c80-416e6f42e087",
    "title": "Administrative Business Partner - ShipOS",
    "location": "Washington, D.C.",
    "official_url": "https://jobs.lever.co/palantir/a237973c-cb29-41fe-9c80-416e6f42e087",
    "posted_date": "2026-06-18",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:42.579232+00:00",
    "date_confidence": "high",
    "description": "Own calendar management and deconfliction across multiple workstream leads — onsites, supplier visits, internal syncs, and Navy stakeholder meetings Schedule and track supplier eng"
  },
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "a5f93bb6-4f13-4451-80a4-f63090830269",
    "title": "Administrative Business Partner - ShipOS",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/palantir/a5f93bb6-4f13-4451-80a4-f63090830269",
    "posted_date": "2026-06-18",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:42.579232+00:00",
    "date_confidence": "high",
    "description": "Own calendar management and deconfliction across multiple workstream leads — onsites, supplier visits, internal syncs, and Navy stakeholder meetings Schedule and track supplier eng"
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
    "fetched_at": "2026-10-05T23:40:42.579232+00:00",
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
    "fetched_at": "2026-10-05T23:40:42.579232+00:00",
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
    "fetched_at": "2026-10-05T23:40:42.579232+00:00",
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
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 68 / 14.664s
- Company elapsed time: 23.838s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 48 / 0 / 0
- Detail cache statuses: {'fetched:new': 48}
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 159
- After US/location filtering: 48
- With trustworthy posted_date: 48
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 9.208, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 0.871, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 1.282, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.371, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 3.987, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.62, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 0.62, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.18, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 1.414, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138369",
    "title": "Sr Staff Software Engineer",
    "location": "New York City, New York, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922716047",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:43.572944+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138222",
    "title": "Staff Software Engineer - Web Full Stack",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922555804",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:43.572944+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137563",
    "title": "Staff Product Security AI Engineer",
    "location": "Austin, Texas, United States of America; Scottsdale, Arizona, United States of America; Chicago, Illinois, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922353695",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:43.572944+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137742",
    "title": "Staff Software Engineer - Platform & Infrastructure",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922449285",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:43.572944+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138185",
    "title": "Sr Manager, Software Engineering",
    "location": "San Jose, California, United States of America; Austin, Texas, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922547411",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:43.572944+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.139s
- Company elapsed time: 0.864s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 16, 'usable_jd': 16}
- Raw jobs found: 151
- After US/location filtering: 133
- With trustworthy posted_date: 133
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8089959",
    "title": "3rd Party Partnerships Manager - Signals",
    "location": "New York City, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8089959",
    "posted_date": "2026-07-29",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:58.560292+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "7792848",
    "title": "Ads Conversion Modeling, Machine Learning Engineering Manager",
    "location": "Remote - United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/7792848",
    "posted_date": "2026-04-14",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:58.560292+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8189317",
    "title": "Backend Engineer, IAM",
    "location": "Remote - United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8189317",
    "posted_date": "2026-09-10",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:58.560292+00:00",
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
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:58.560292+00:00",
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
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:40:58.560292+00:00",
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
- HTTP requests/cumulative request time: 53 / 16.564s
- Company elapsed time: 22.612s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 39 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1, 'fetched:new': 38}
- Relevant JD recovery: {'eligible': 21, 'usable_jd': 21}
- Raw jobs found: 93
- After US/location filtering: 39
- With trustworthy posted_date: 39
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.048, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.399, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.718, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 11.836, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 31, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 31}
- Query diagnostic: {"elapsed_seconds": 0.382, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.739, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.382, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.368, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.233, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 21}

Sample normalized records:

```json
[
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059026",
    "title": "Global Specialist Solution Architect - Lightwell",
    "location": "Boston; Remote US VA; Remote US SC; Remote US NC; Remote US TX; Remote US FL; Remote US CA; Remote US GA",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Boston/Global-Specialist-Solution-Architect---Lightwell_R-059026-2",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:59.425156+00:00",
    "date_confidence": "high",
    "description": "About the role: The Red Hat Technology Sales team is looking for a Lightwell Specialist Solution Architect (SSA) to join our team. This position assumes a crucial role in providing"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059799",
    "title": "Software Engineer",
    "location": "Raleigh",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Raleigh/Software-Engineer_R-059799",
    "posted_date": "2026-09-24",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:59.425156+00:00",
    "date_confidence": "high",
    "description": "*Telecommuting permitted: work may be performed within normal commuting distance from the Red Hat, LLC office in Raleigh, NC. Contribute to the architecture, design, development, a"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059025",
    "title": "Global Specialist Solution Architect - Lightwell",
    "location": "Boston; Remote US VA; Remote US SC; Remote US NC; Remote US TX; Remote US FL; Remote US CA; Remote US GA",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Boston/Global-Specialist-Solution-Architect---Lightwell_R-059025-1",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:59.425156+00:00",
    "date_confidence": "high",
    "description": "About the role: The Red Hat Technology Sales team is looking for a Lightwell Specialist Solution Architect (SSA) to join our team. This position assumes a crucial role in providing"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059027",
    "title": "Global Telco Specialist Solution Architect - Lightwell",
    "location": "Boston; Remote US VA; Remote US SC; Remote US NC; Remote US TX; Remote US FL; Remote US CA; Remote US GA",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Boston/Global-Telco-Specialist-Solution-Architect---Lightwell_R-059027-2",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:59.425156+00:00",
    "date_confidence": "high",
    "description": "About the role: The Red Hat Technology Sales team is looking for a Lightwell Specialist Solution Architect (SSA) with Telco experience to join our team. This position assumes a cru"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059024",
    "title": "Director, Specialist Solution Architecture Global Lightwell Leader",
    "location": "Boston; Remote US VA; Remote US SC; Remote US NC; Remote US TX; Remote US FL; Remote US CA; Remote Germany; Remote US GA; Remote UK",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Boston/Director--Specialist-Solution-Architecture-Global-Lightwell-Leader_R-059024-2",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:40:59.425156+00:00",
    "date_confidence": "high",
    "description": "About the role: The Red Hat Global Technology Sales team is looking for a Global Lightwell Leader to join our team. This leadership position is responsible for the quality and exec"
  }
]
```

## Roku

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roku/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.192s
- Company elapsed time: 1.322s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 211
- After US/location filtering: 170
- With trustworthy posted_date: 170
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8077965",
    "title": "Account Executive",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8077965?gh_jid=8077965",
    "posted_date": "2026-07-22",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:41:07.411892+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8186852",
    "title": "Account Executive, Media & Entertainment",
    "location": "Santa Monica, California; Santa Monica, California, United States",
    "official_url": "https://www.weareroku.com/jobs/8186852?gh_jid=8186852",
    "posted_date": "2026-09-08",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:41:07.411892+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8154533",
    "title": "Account Manager",
    "location": "Chicago, Illinois; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8154533?gh_jid=8154533",
    "posted_date": "2026-08-24",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:41:07.411892+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "7677767",
    "title": "Account Manager",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/7677767?gh_jid=7677767",
    "posted_date": "2026-03-04",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:41:07.411892+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8167560",
    "title": "Ad Marketing Coordinator",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8167560?gh_jid=8167560",
    "posted_date": "2026-08-31",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:41:07.411892+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.382s
- Company elapsed time: 1.654s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 24, 'usable_jd': 24}
- Raw jobs found: 226
- After US/location filtering: 210
- With trustworthy posted_date: 210
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5317296008",
    "title": "Account Manager, SMB",
    "location": "Sydney, Australia; AU - NSW - Remote",
    "official_url": "http://block.xyz/careers/jobs/5317296008?gh_jid=5317296008",
    "posted_date": "2026-07-09",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:41:08.418148+00:00",
    "date_confidence": "high",
    "description": "<p>Since we opened our doors in 2009, the world of commerce has evolved immensely, and so has Square. After enabling anyone to take payments and never miss a sale, we saw sellers s"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5258372008",
    "title": "Account Manager, SMB",
    "location": "Melbourne, Australia; AU - NSW - Remote",
    "official_url": "http://block.xyz/careers/jobs/5258372008?gh_jid=5258372008",
    "posted_date": "2026-06-15",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:41:08.418148+00:00",
    "date_confidence": "high",
    "description": "<p>Since we opened our doors in 2009, the world of commerce has evolved immensely, and so has Square. After enabling anyone to take payments and never miss a sale, we saw sellers s"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5317297008",
    "title": "Account Manager, SMB",
    "location": "Brisbane, Australia; AU - NSW - Remote",
    "official_url": "http://block.xyz/careers/jobs/5317297008?gh_jid=5317297008",
    "posted_date": "2026-07-09",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:41:08.418148+00:00",
    "date_confidence": "high",
    "description": "<p>Since we opened our doors in 2009, the world of commerce has evolved immensely, and so has Square. After enabling anyone to take payments and never miss a sale, we saw sellers s"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5434157008",
    "title": "AI Evaluation Infrastructure Engineer",
    "location": "Bay Area, CA, United States of America; US - CA - Bay Area - Remote",
    "official_url": "http://block.xyz/careers/jobs/5434157008?gh_jid=5434157008",
    "posted_date": "2026-09-30",
    "updated_date": "2026-10-05",
    "fetched_at": "2026-10-05T23:41:08.418148+00:00",
    "date_confidence": "high",
    "description": "<p>It all started with an idea at Block in 2013. Initially built to take the pain out of peer-to-peer payments, Cash App has gone from a simple product with a single purpose to a d"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5108007008",
    "title": "Applied Research Intern, Proactive Intelligence & Customer World Models (PhD / Graduate Co-op)",
    "location": "Bay Area, CA, United States of America; CA - ON - Toronto - Remote",
    "official_url": "http://block.xyz/careers/jobs/5108007008?gh_jid=5108007008",
    "posted_date": "2026-06-09",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:41:08.418148+00:00",
    "date_confidence": "high",
    "description": "<p><strong>Team:</strong> Apollo — Block Applied R&amp;D<br><strong>Location:</strong> Remote (US / Canada)<br><strong>Duration:</strong> Fall/Winter 2026 co-op — 8 months, flexibl"
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
- HTTP requests/cumulative request time: 76 / 91.261s
- Company elapsed time: 98.613s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 59 / 12 / 11
- Detail cache statuses: {'fetched:new': 29, 'reused': 12}
- Relevant JD recovery: {'deterministic_skip': 6, 'eligible': 30, 'ai_recover': 7, 'ai_skip': 5, 'detail_requests': 30, 'detail_failure': 30, 'budget_deferred': 0, 'usable_jd': 0}
- Raw jobs found: 111
- After US/location filtering: 41
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 15.253, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 7.057, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 2.473, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 6.627, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 18.257, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.393, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 1.166, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.851, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 7.238, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 32}

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
    "fetched_at": "2026-10-05T23:41:08.734956+00:00",
    "date_confidence": "unknown",
    "description": "Quantitative Software Engineer: Generative AI Location NY New York United States"
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
    "fetched_at": "2026-10-05T23:41:08.734956+00:00",
    "date_confidence": "unknown",
    "description": "AI Solutions Developer Location NY New York United States"
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
    "fetched_at": "2026-10-05T23:41:08.734956+00:00",
    "date_confidence": "unknown",
    "description": "AI Fluency: Program Manager Location NY New York United States"
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
    "fetched_at": "2026-10-05T23:41:08.734956+00:00",
    "date_confidence": "unknown",
    "description": "AI Research Scientist - Intern [2027 Summer] Location NY New York United States"
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
    "fetched_at": "2026-10-05T23:41:08.734956+00:00",
    "date_confidence": "unknown",
    "description": "AI Research Scientist - Campus Full-Time Location NY New York United States"
  }
]
```

## Verkada

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/verkada/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.182s
- Company elapsed time: 1.252s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 38, 'usable_jd': 38}
- Raw jobs found: 304
- After US/location filtering: 245
- With trustworthy posted_date: 245
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Verkada",
    "source": "verkada_official_careers",
    "job_id": "4866484007",
    "title": "Account Executive (Osaka, Japan)",
    "location": "Japan; Osaka Office",
    "official_url": "https://job-boards.greenhouse.io/verkada/jobs/4866484007",
    "posted_date": "2025-09-22",
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:41:10.073346+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><strong>Who We Are</strong></h3> <p>Verkada is transforming how organizations protect their people and places with an integrated, privacy-sensitive A"
  },
  {
    "company": "Verkada",
    "source": "verkada_official_careers",
    "job_id": "4248001007",
    "title": "Account Executive, Select, Austin",
    "location": "Austin, TX United States; Austin office",
    "official_url": "https://job-boards.greenhouse.io/verkada/jobs/4248001007",
    "posted_date": "2025-02-21",
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:41:10.073346+00:00",
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
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:41:10.073346+00:00",
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
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:41:10.073346+00:00",
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
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:41:10.073346+00:00",
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
- HTTP requests/cumulative request time: 127 / 56.071s
- Company elapsed time: 73.640s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 105 / 0 / 0
- Detail cache statuses: {'fetched:new': 104, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 17, 'usable_jd': 17}
- Raw jobs found: 356
- After US/location filtering: 105
- With trustworthy posted_date: 105
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 34.065, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.643, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 5.039, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 14.207, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.626, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.786, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.171, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.529, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 2.877, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088770W",
    "title": "Senior Software Engineer - SDET",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Sr-SW-Engineer--Software-Engineering---Analyst---Team-Lead_REF088770W",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:11.331971+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088944W",
    "title": "Sr. SW Engineer - SDET",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Sr-SW-Engineer--Software-Engineering---Analyst---Team-Lead_REF088944W",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:11.331971+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088661W",
    "title": "Senior Staff Fullstack Engineer (Sr. Consultant) - Corporate GenAI Technologies",
    "location": "US - Bellevue, WA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Bellevue-WA/Full-Stack-Senior-Consultant--Software-Engineer--Generative-AI_REF088661W",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:11.331971+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF087509W",
    "title": "Senior Director",
    "location": "US - Foster City, CA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Senior-Director_REF087509W",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:11.331971+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF087977W",
    "title": "Staff Software Engineer, AI Solutions",
    "location": "US - Denver, CO",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Denver-CO/Staff-Software-Engineer--AI-Solutions_REF087977W-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:11.331971+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.231s
- Company elapsed time: 0.253s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 17
- After US/location filtering: 13
- With trustworthy posted_date: 13
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "82955de9-485d-4db0-8fd9-1c018489fc8d",
    "title": "Application Engineer",
    "location": "San Jose, CA",
    "official_url": "https://jobs.lever.co/weride/82955de9-485d-4db0-8fd9-1c018489fc8d",
    "posted_date": "2019-01-17",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:19.007916+00:00",
    "date_confidence": "high",
    "description": "Role Responsibilities: System Bringup & Deployment Deploy and integrate autonomous driving software onto vehicle platforms and embedded computing systems. Validate system functiona"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "fecb0fd0-7f66-4010-af00-b6500e0ef680",
    "title": "Data Annotation QA",
    "location": "United Arab Emirates",
    "official_url": "https://jobs.lever.co/weride/fecb0fd0-7f66-4010-af00-b6500e0ef680",
    "posted_date": "2026-06-16",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:19.007916+00:00",
    "date_confidence": "high",
    "description": "Data Annotation (DA) Label and annotate data (text, image, audio, or video) based on project guidelines. Categorize and structure raw data into machine-readable formats. Follow str"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "012c818d-4ad8-4096-80b0-386cdf79f8d5",
    "title": "Forward Deployed Engineer",
    "location": "One-north",
    "official_url": "https://jobs.lever.co/weride/012c818d-4ad8-4096-80b0-386cdf79f8d5",
    "posted_date": "2024-03-27",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:19.007916+00:00",
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
    "fetched_at": "2026-10-05T23:41:19.007916+00:00",
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
    "fetched_at": "2026-10-05T23:41:19.007916+00:00",
    "date_confidence": "high",
    "description": "Own end-to-end project delivery as the single accountable owner (DRI), ensuring success across scope, schedule, cost, and quality Lead the full project lifecycle from pre-sales thr"
  }
]
```

## Workday

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://workday.wd5.myworkdayjobs.com/Workday`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 23
- HTTP requests/cumulative request time: 139 / 77.727s
- Company elapsed time: 97.615s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 115 / 0 / 0
- Detail cache statuses: {'fetched:new': 115}
- Relevant JD recovery: {'eligible': 24, 'usable_jd': 24}
- Raw jobs found: 433
- After US/location filtering: 115
- With trustworthy posted_date: 115
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 41.839, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.956, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 2.585, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 16.378, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.791, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.199, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.117, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.325, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 9.203, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0110689",
    "title": "Senior AI Engineer",
    "location": "USA, GA, Atlanta",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-GA-Atlanta/Senior-AI-Engineer_JR-0110689",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:19.262068+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  },
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0107313",
    "title": "Principal AI Researcher",
    "location": "USA, CA, Pleasanton; USA, GA, Atlanta; Canada, BC, Vancouver",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CA-Pleasanton/Principal-AI-Researcher_JR-0107313",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:19.262068+00:00",
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
    "fetched_at": "2026-10-05T23:41:19.262068+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  },
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0109463",
    "title": "Senior AI Engineer - Agent Factory",
    "location": "USA, CO, Boulder; Canada, BC, Vancouver",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CO-Boulder/Senior-AI-Engineer---Agent-Factory_JR-0109463",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:19.262068+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  },
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0107977",
    "title": "Senior AI Deployment Engineer",
    "location": "USA, IL, Chicago; USA Remote",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-IL-Chicago/Senior-Technical-Delivery-Consultant---AI-Practice_JR-0107977",
    "posted_date": "2026-09-30",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:19.262068+00:00",
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
- HTTP requests/cumulative request time: 51 / 23.033s
- Company elapsed time: 28.978s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 35 / 0 / 0
- Detail cache statuses: {'fetched:new': 35}
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 157
- After US/location filtering: 35
- With trustworthy posted_date: 35
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.047, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 0.699, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.684, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 1.143, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 3.6, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 33, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 2.756, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 0.697, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.87, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.689, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 17}

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
    "fetched_at": "2026-10-05T23:41:22.038581+00:00",
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
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:22.038581+00:00",
    "date_confidence": "high",
    "description": "About the team The Agentic AI team at Zillow is at the forefront of transforming the real estate industry by helping millions of people use AI technologies to find their next home."
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
    "fetched_at": "2026-10-05T23:41:22.038581+00:00",
    "date_confidence": "high",
    "description": "About the team The Shopping AI team is at the heart of Zillow Group’s mission to create a seamless digital real estate marketplace. We build and own the machine learning systems th"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751216",
    "title": "Principal Software Development Engineer, Full Stack",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Principal-Software-Development-Engineer--Full-Stack_P751216-1",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:22.038581+00:00",
    "date_confidence": "high",
    "description": "About the team The Data Engineering & Enterprise Tools team powers Zillow Rentals by delivering mission-critical analytics tools, AI enablement solutions, and high fidelity data pr"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751226",
    "title": "Principal Full Stack Software Development Engineer",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Principal-Full-Stack-Software-Development-Engineer_P751226-2",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:22.038581+00:00",
    "date_confidence": "high",
    "description": "About the team At Zillow our mission is to give people the power to unlock life’s next chapter. Zillow’s AI Org plays an important part in delivering unique AI-powered experiences "
  }
]
```

## Zscaler

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/zscaler/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.440s
- Company elapsed time: 1.641s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 21, 'usable_jd': 21}
- Raw jobs found: 363
- After US/location filtering: 216
- With trustworthy posted_date: 216
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5197814007",
    "title": "Account Executive, Commercial",
    "location": "Landeshauptstadt München, DEU; Remote - Germany",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5197814007",
    "posted_date": "2026-07-31",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-10-05T23:41:33.446688+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5236995007",
    "title": "Account Executive, Commercial - Kansas City",
    "location": "Remote - Illinois, USA; Remote - Missouri, USA; Remote - Illinois, USA; Remote - Kansas, USA; Remote - Missouri, USA",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5236995007",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-23",
    "fetched_at": "2026-10-05T23:41:33.446688+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-10-05T23:41:33.446688+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-10-05T23:41:33.446688+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5159494007",
    "title": "Account Executive, Commercial (West)",
    "location": "Remote - Ôsaka, Japan; Osaka, JPN",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5159494007",
    "posted_date": "2026-07-13",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-10-05T23:41:33.446688+00:00",
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
- HTTP requests/cumulative request time: 12 / 4.808s
- Company elapsed time: 5.058s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 2 / 0 / 0
- Detail cache statuses: {'fetched:new': 2}
- Relevant JD recovery: {'eligible': 2, 'usable_jd': 2}
- Raw jobs found: 9
- After US/location filtering: 2
- With trustworthy posted_date: 2
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.257, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.391, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.43, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.41, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.384, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.419, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.39, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.415, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.365, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}

Sample normalized records:

```json
[
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R29015",
    "title": "Software Engineer III (UX Engineer – Design System)",
    "location": "USA - MA - Boston - BOS1; USA - MN - Minneapolis - MSP2",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/USA---MA---Boston---BOS1/Software-Engineer-II_R29015",
    "posted_date": "2026-08-21",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:35.088895+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity Chewy is growing! We're looking for a Software Engineer III to help define and scale the frontend foundations that power consistent, accessible, an"
  },
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R30441",
    "title": "Database Engineer II",
    "location": "USA - FL - Plantation - FLL7",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/USA---FL---Plantation---FLL7/Database-Engineer-II_R30441-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:35.088895+00:00",
    "date_confidence": "high",
    "description": "Job Description: At Chewy, it is our mission to become the most trusted and convenient online destination for pet parents and our partners vets and service providers alike. Our suc"
  }
]
```

## CVS Health

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 147 / 67.414s
- Company elapsed time: 87.547s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 125 / 0 / 0
- Detail cache statuses: {'fetched:new': 125}
- Relevant JD recovery: {'eligible': 12, 'usable_jd': 12}
- Raw jobs found: 362
- After US/location filtering: 125
- With trustworthy posted_date: 125
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 38.779, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.309, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 7.018, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 12.081, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.77, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.684, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.188, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.713, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 4.674, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1046107",
    "title": "Staff Cloud Automation Engineer",
    "location": "CT - Hartford",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/CT---Hartford/Staff-Cloud-Engineer_R1046107",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:40.148306+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1055785",
    "title": "Lead Director, Software Development Engineering",
    "location": "NY - Work from hom; TX - Irving; NY - New York; MA - Wellesley",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/NY---Work-from-hom/Lead-Director--Software-Development-Engineering_R1055785-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:40.148306+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1055331",
    "title": "Health, Safety, & Environment Analyst",
    "location": "RI - Cumberland",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/RI---Cumberland/HSE-Analyst_R1055331",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:40.148306+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1025538",
    "title": "AVP, Platform Security",
    "location": "",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/AVP--Platform-Security_R1025538",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:40.148306+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1048945",
    "title": "Senior IAM Engineer - Ping Identity and Directory Services",
    "location": "TX - Work from home",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/TX---Work-from-home/Senior-IAM-Engineer---Ping-Identity-and-Directory-Services_R1048945",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:40.148306+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.198s
- Company elapsed time: 0.434s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 60
- After US/location filtering: 53
- With trustworthy posted_date: 53
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
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-05T23:41:51.018014+00:00",
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
    "updated_date": "2026-09-03",
    "fetched_at": "2026-10-05T23:41:51.018014+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8806187002",
    "title": "Associate Product Manager, Intern",
    "location": "Pittsburgh, PA; Pittsburgh, Pennsylvania, United States",
    "official_url": "https://careers.duolingo.com/jobs/8806187002?gh_jid=8806187002",
    "posted_date": "2026-09-15",
    "updated_date": "2026-09-15",
    "fetched_at": "2026-10-05T23:41:51.018014+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8625579002",
    "title": "Consumer Product Lead",
    "location": "Tokyo, Japan; Remote",
    "official_url": "https://careers.duolingo.com/jobs/8625579002?gh_jid=8625579002",
    "posted_date": "2026-07-08",
    "updated_date": "2026-07-29",
    "fetched_at": "2026-10-05T23:41:51.018014+00:00",
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
    "updated_date": "2026-07-28",
    "fetched_at": "2026-10-05T23:41:51.018014+00:00",
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
- HTTP requests/cumulative request time: 22 / 17.422s
- Company elapsed time: 35.125s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 6 / 56
- Detail cache statuses: {'reused': 6}
- Relevant JD recovery: {'cache_reused': 6, 'eligible': 6, 'deterministic_skip': 34, 'ai_skip': 22, 'usable_jd': 6}
- Raw jobs found: 305
- After US/location filtering: 62
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.589, "first_pass_survivors": 38, "group": "official", "jds_resolved": 0, "original_postings_resolved": 38, "page_budget": 2, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 2.61, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 1.108, "first_pass_survivors": 17, "group": "official", "jds_resolved": 0, "original_postings_resolved": 17, "page_budget": 2, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 25, "stop_reason": "early_stop", "unique_contribution": 17, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 1.084, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 2, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 15.466, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 3.092, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 2.424, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 2.97, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 2.781, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 2, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 38}

Sample normalized records:

```json
[
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-163407",
    "title": "AI Engineer, Product Software",
    "location": "Redwood City, California, United States",
    "official_url": "https://careers.equinix.com/jobs/ai-engineer-product-software-redwood-city-california-united-states",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:51.452949+00:00",
    "date_confidence": "unknown",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
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
    "fetched_at": "2026-10-05T23:41:51.452949+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-163585",
    "title": "Chief of Staff, Enterprise AI",
    "location": "Toronto, Ontario, Canada; Redwood City, California, United States; Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/chief-of-staff-enterprise-ai-redwood-city-california-united-states-dallas-texas-toronto-ontario-canada",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:51.452949+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-163213",
    "title": "VP, Sales AMER AI Ecosystem & Digital Native",
    "location": "Redwood City, California, United States; Bellevue, Washington, United States",
    "official_url": "https://careers.equinix.com/jobs/vp-sales-amer-ai-ecosystem-digital-native-redwood-city-california-united-states-bellevue-washington",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:51.452949+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-162405",
    "title": "DevOps Engineer",
    "location": "Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/devops-engineer-dallas-texas-united-states",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:41:51.452949+00:00",
    "date_confidence": "unknown",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
  }
]
```

## F5

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ffive.wd5.myworkdayjobs.com/f5jobs`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 16 / 7.450s
- Company elapsed time: 8.831s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: {'fetched:new': 1}
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 119
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.507, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.445, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.423, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.389, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.131, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.082, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.488, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.484, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.312, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

Sample normalized records:

```json
[
  {
    "company": "F5",
    "source": "f5_official_careers",
    "job_id": "RP1038953",
    "title": "Senior Site Reliability Engineer - FedRAMP",
    "location": "Reston",
    "official_url": "https://ffive.wd5.myworkdayjobs.com/f5jobs/job/Reston/Senior-Site-Reliability-Engineer---FedRAMP_RP1038953",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:13.052001+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.129s
- Company elapsed time: 0.626s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 54, 'usable_jd': 54}
- Raw jobs found: 119
- After US/location filtering: 105
- With trustworthy posted_date: 105
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8859221002",
    "title": "Account Manager, K-12",
    "location": "Raleigh, NC; Morrisville, North Carolina, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8859221002",
    "posted_date": "2026-09-30",
    "updated_date": "2026-09-30",
    "fetched_at": "2026-10-05T23:42:21.883882+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is seeking Account Managers to join our growing team. The ideal candidate will hav"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8734156002",
    "title": "Administrative Assistant, Proposals Team",
    "location": "San Mateo, CA; San Mateo, California, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8734156002",
    "posted_date": "2026-08-20",
    "updated_date": "2026-08-20",
    "fetched_at": "2026-10-05T23:42:21.883882+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is looking for an Administrative Assistant to support IXL’s RFP and proposals stra"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8765546002",
    "title": "American English Language Tutor, Rosetta Stone (PT)",
    "location": "United States; Remote - US",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8765546002",
    "posted_date": "2026-09-01",
    "updated_date": "2026-09-01",
    "fetched_at": "2026-10-05T23:42:21.883882+00:00",
    "date_confidence": "high",
    "description": "<p><span style=\"font-weight: 400;\">IXL Learning, developer of personalized learning products used by millions of people globally, is seeking a US English Language Tutor to join our"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8531284002",
    "title": "Associate Curriculum Alignment Specialist",
    "location": "Raleigh, NC; Morrisville, North Carolina, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8531284002",
    "posted_date": "2026-04-30",
    "updated_date": "2026-07-10",
    "fetched_at": "2026-10-05T23:42:21.883882+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is seeking an Associate Curriculum Alignment Specialist to join our curriculum dev"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8611944002",
    "title": "Associate Digital Designer",
    "location": "San Mateo, CA; San Mateo, California, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8611944002",
    "posted_date": "2026-06-29",
    "updated_date": "2026-07-30",
    "fetched_at": "2026-10-05T23:42:21.883882+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is seeking an enthusiastic, highly motivated Associate Digital Designer to join ou"
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
- HTTP requests/cumulative request time: 96 / 58.979s
- Company elapsed time: 72.101s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 76 / 0 / 0
- Detail cache statuses: {'fetched:new': 76}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 278
- After US/location filtering: 76
- With trustworthy posted_date: 76
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 27.816, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 37, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 4.8, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.923, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 14.419, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 9.409, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.408, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.928, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.987, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 6.157, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 50, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 50}

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
    "posted_date": "2026-09-23",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:22.510812+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Principal AI Engineer to join the CCIBT Gen AI team, which is responsible for building AI frameworks, intelligent agents, and technology p"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-577897",
    "title": "Lead AI Engineer",
    "location": "CHARLOTTE, NC; BOSTON, MA",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Lead-AI-Engineer_R-577897",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:22.510812+00:00",
    "date_confidence": "high",
    "description": "Wells Fargo is seeking a Lead Ai Engineer in Technology as part of Commercial and Corporate & Investment Banking Technology (CCIBT).). The primary focus of this group will be to le"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-576649",
    "title": "Principal Engineer - AI Engineering Productivity Lead",
    "location": "CHARLOTTE, NC",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Principal-Engineer---AI-Engineering-Productivity-Lead_R-576649",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:22.510812+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Principal Engineer who will function as the Chief Operating Office's (COO) Technology Group's AI Engineering Productivity Lead. This indiv"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-573422",
    "title": "Senior Lead Technology Risk Officer (Application Domain, SDLC, DevOps and AI)",
    "location": "CHARLOTTE, NC; IRVING, TX",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Senior-Lead-Technology-Risk-Officer--Application-Domain--SDLC--DevOps-and-AI-_R-573422-1",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:22.510812+00:00",
    "date_confidence": "high",
    "description": "About this role: The Application Risk Domain Officer operates within Technology Risk Management (TRM), part of Corporate Risk, providing independent second line oversight across ap"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-573427",
    "title": "Lead Software Engineer",
    "location": "ISELIN, NJ",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/ISELIN-NJ/Lead-Software-Engineer_R-573427",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:22.510812+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Lead Software Engineer in Technology as part of Cybersecurity. Learn more about the career areas and lines of business at wellsfargojobs.c"
  }
]
```

## Yahoo

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ouryahoo.wd5.myworkdayjobs.com/careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 83 / 33.550s
- Company elapsed time: 44.814s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 63 / 0 / 0
- Detail cache statuses: {'fetched:new': 63}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 256
- After US/location filtering: 63
- With trustworthy posted_date: 63
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 28.975, "first_pass_survivors": 56, "group": "official", "jds_resolved": 56, "original_postings_resolved": 56, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 56, "stop_reason": "page_budget", "unique_contribution": 56, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 0.686, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 0.994, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 3.879, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 3.189, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 2.407, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 0.681, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.66, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 2.566, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 25}

Sample normalized records:

```json
[
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0027165",
    "title": "Director, Software Apps Engineering – AI-Native Development and Product Experiences",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Director--Software-Apps-Engineering_JR0027165",
    "posted_date": "2026-09-21",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:24.973270+00:00",
    "date_confidence": "high",
    "description": "Yahoo Mail is the ultimate consumer inbox with hundreds of millions of users. It’s the best way to access your email and stay organized from a computer, phone or tablet. With its b"
  },
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0027182",
    "title": "Principal Applied Research Scientist – Generative AI and NLP",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Principal-Applied-Research-Scientist---Generative-AI-and-NLP_JR0027182",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:24.973270+00:00",
    "date_confidence": "high",
    "description": "Yahoo Mail is the ultimate consumer inbox with hundreds of millions of users. It’s the best way to access your email and stay organized from a computer, phone or tablet. With its b"
  },
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0026993",
    "title": "Senior Principal AI/ML Architect, Yahoo Mail",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Senior-Principal-AI-ML-Architect--Yahoo-Mail_JR0026993",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:24.973270+00:00",
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
    "fetched_at": "2026-10-05T23:42:24.973270+00:00",
    "date_confidence": "high",
    "description": "Yahoo serves as a trusted guide for hundreds of millions of people globally, helping them achieve their goals online through our portfolio of iconic products. For advertisers, Yaho"
  },
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0027452",
    "title": "Senior Manager/Director of Engineering, Search Query Understanding and Guidance",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Director-of-Engineering--Search-Query-Understanding-and-Guidance_JR0027452",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:24.973270+00:00",
    "date_confidence": "high",
    "description": "Yahoo serves as a trusted guide for hundreds of millions of people globally, helping them achieve their goals online through our portfolio of iconic products. For advertisers, Yaho"
  }
]
```

## Ansys

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.synopsys.com/search-jobs`
- Pagination: p=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 3
- HTTP requests/cumulative request time: 25 / 5.245s
- Company elapsed time: 8.939s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 22 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 45
- After US/location filtering: 22
- With trustworthy posted_date: 22
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.939, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "Ansys", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 45}

Sample normalized records:

```json
[
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "100992954016",
    "title": "Senior Application Engineer",
    "location": "Waltham, Massachusetts",
    "official_url": "https://careers.synopsys.com/job/waltham/senior-application-engineer/44408/100992954016",
    "posted_date": "2026-06-29",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:26.578620+00:00",
    "date_confidence": "high",
    "description": "THIS POSITION IS ELIGIBLE UNDER THE TERMS OF THE EMPLOYEE REFERRAL PROGRAM (ERP): SUMMARY ANSYS, Inc. seeks Senior Application Engineer to work in Waltham, MA RESPONSIBILITIES Lead"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "100032391312",
    "title": "Academic/Outreach, Sr Associate",
    "location": "United States Off-site",
    "official_url": "https://careers.synopsys.com/job/canonsburg/academic-outreach-sr-associate/44408/100032391312",
    "posted_date": "2026-09-01",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:26.578620+00:00",
    "date_confidence": "high",
    "description": "We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling customers to rapidly innovate AI-powered products. We deliver industry-leading silicon desi"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "96518777376",
    "title": "Technical Support Engineer, Optics & Photonics",
    "location": "Chalandri, Greece",
    "official_url": "https://careers.synopsys.com/job/chalandri/technical-support-engineer-optics-and-photonics/44408/96518777376",
    "posted_date": "2026-06-16",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:26.578620+00:00",
    "date_confidence": "high",
    "description": "We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling customers to rapidly innovate AI-powered products. We deliver industry-leading silicon desi"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "101056156880",
    "title": "Aerospace Systems Engineer",
    "location": "DC",
    "official_url": "https://careers.synopsys.com/job/dc/aerospace-systems-engineer/44408/101056156880",
    "posted_date": "2026-09-23",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:26.578620+00:00",
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
    "fetched_at": "2026-10-05T23:42:26.578620+00:00",
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
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 177 / 77.355s
- Company elapsed time: 100.513s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 155 / 0 / 0
- Detail cache statuses: {'fetched:new': 155}
- Relevant JD recovery: {'eligible': 97, 'usable_jd': 97}
- Raw jobs found: 302
- After US/location filtering: 155
- With trustworthy posted_date: 155
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 41.746, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 3.34, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.11, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 6.037, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 14.642, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.335, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 5.028, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.201, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 19.207, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD218757",
    "title": "Sales Engineer",
    "location": "USA, MA, Littleton; USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-MA-Littleton/Sales-Engineer_WD218757",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:35.518336+00:00",
    "date_confidence": "high",
    "description": "At JetCool, a Flex company, we’re at the forefront of liquid cooling innovation, delivering advanced solutions that empower our partners in AI and high-performance computing. Unite"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD228496",
    "title": "Associate Principal Engineer, Mechanical Engineering",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Associate-Principal-Engineer--Mechanical-Engineering_WD228496",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:35.518336+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD228495",
    "title": "Associate Principal Engineer, Electrical Engineering",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Associate-Principal-Engineer--Electrical-Engineering_WD228495",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:35.518336+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD228345",
    "title": "Principal Engineer, Systems Architecture Engineering",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Principal-Engineer--Systems-Architecture-Engineering_WD228345",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:35.518336+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD228344",
    "title": "Principal Engineer, Advanced Power Engineering",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Principal-Engineer--Advanced-Power-Engineering_WD228344",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:35.518336+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  }
]
```

## IQVIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://iqvia.wd1.myworkdayjobs.com/IQVIA`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 11
- HTTP requests/cumulative request time: 38 / 23.131s
- Company elapsed time: 26.889s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 26 / 0 / 0
- Detail cache statuses: {'fetched:new': 26}
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 65
- After US/location filtering: 26
- With trustworthy posted_date: 26
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.787, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 2.089, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 2.159, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 3.232, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 9.419, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 1.039, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.891, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.85, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.307, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 12}

Sample normalized records:

```json
[
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1562238",
    "title": "Healthcare Analytics, AI Product & Methodology Analyst",
    "location": "Greenwich, CT, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Greenwich-CT-United-States-of-America/Healthcare-Analytics--AI-Product---Methodology-Analyst_R1562238",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:56.878364+00:00",
    "date_confidence": "high",
    "description": "About Cedar Gate Technologies Cedar Gate Technologies, an IQVIA business, enables payers, providers, employers, and service administrators to excel at value-based care with a unifi"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1542005",
    "title": "AI Solutions Delivery 3 (Remote)",
    "location": "Wayne, PA, United States of America; Durham, North Carolina, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Wayne-PA-United-States-of-America/AI-Solutions-Delivery-3_R1542005",
    "posted_date": "2026-09-09",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:56.878364+00:00",
    "date_confidence": "high",
    "description": "This is an exciting opportunity to work as a Senior Consultant in IQVIA, one of the world's leading multi-disciplinary and cross-functional teams working with Real World patient da"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1563152",
    "title": "Manager, AI Science & Solutions,US Based Remote",
    "location": "Durham, North Carolina, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Durham-North-Carolina-United-States-of-America/Manager--AI-Science---Solutions_R1563152",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:56.878364+00:00",
    "date_confidence": "high",
    "description": "Manager, AI Science & Solutions | IQVIA Are you looking to work at the forefront of Machine Learning and Artificial Intelligence? Would you be excited to apply cutting-edge Generat"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1526366",
    "title": "Senior Software Engineer (React), IQVIA Digital",
    "location": "Red Bank, NJ, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Red-Bank-NJ-United-States-of-America/Senior-Software-Engineer_R1526366",
    "posted_date": "2026-09-23",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:56.878364+00:00",
    "date_confidence": "high",
    "description": "IQVIA Digital Overview: IQVIA Digital powers exceptional brand experiences, delivering innovative solutions based on a customer-first, insights-driven, and integrated omnichannel v"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1566486",
    "title": "MedTech Field Service Engineer or Technician - Device Upgrade - West Coast",
    "location": "Carlsbad, CA, United States of America; San Francisco , CA; Portland, Oregon, United States; Phoenix, AZ; Los Angeles, CA; Denver , Colorado, United States; Salt Lake City, UT",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Carlsbad-CA-United-States-of-America/MedTech-Field-Service-Technician-Device-Upgrade-or-Engineer_R1566486",
    "posted_date": "2026-09-24",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:42:56.878364+00:00",
    "date_confidence": "high",
    "description": "Our MedTech Field Service Technicians and Engineers experience a unique opportunity employ their technical experience by collaborating with healthcare professionals and leading tec"
  }
]
```

## Johnson & Johnson

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://jj.wd5.myworkdayjobs.com/JJ`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 23
- HTTP requests/cumulative request time: 233 / 95.664s
- Company elapsed time: 127.315s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 209 / 0 / 0
- Detail cache statuses: {'fetched:new': 208, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 69, 'usable_jd': 69}
- Raw jobs found: 420
- After US/location filtering: 209
- With trustworthy posted_date: 209
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.267, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.218, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 37, "stop_reason": "early_stop", "unique_contribution": 23, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 33.2, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.108, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.903, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.176, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.866, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 0.268, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 4.987, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-100446",
    "title": "BAIP Security Manager – SAP BTP & AI Platform Security",
    "location": "Raritan, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raritan-New-Jersey-United-States-of-America/Manager--SAP-Business-Technology-Platform-AI-Engineering_R-100446-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:07.696775+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-081548",
    "title": "Senior Manager, Global Commercial Data & AI Enablement",
    "location": "Raritan, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raritan-New-Jersey-United-States-of-America/Global-Commercial-Analytics-Sr-Manager_R-081548-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:07.696775+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-072535",
    "title": "Director, Incident Response & Threat",
    "location": "Raynham, Massachusetts, United States of America; West Chester, Pennsylvania, United States of America; Palm Beach Gardens, Florida, United States of America; Warsaw, Indiana, United States of America; Raritan, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raynham-Massachusetts-United-States-of-America/Director--Incident-Response---Threat_R-072535",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:07.696775+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-103293",
    "title": "IMM Computational Intern",
    "location": "Spring House, Pennsylvania, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Spring-House-Pennsylvania-United-States-of-America/IMM-Computational-Intern_R-103293",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:07.696775+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-101914",
    "title": "Senior Manager, PSTS",
    "location": "Spring House, Pennsylvania, United States of America; San Diego, California, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Spring-House-Pennsylvania-United-States-of-America/Senior-Manager--PSTS_R-101914-1",
    "posted_date": "2026-10-05",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:07.696775+00:00",
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
- Pages/requests fetched: 13
- HTTP requests/cumulative request time: 41 / 22.527s
- Company elapsed time: 26.928s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 27 / 0 / 0
- Detail cache statuses: {'fetched:new': 27}
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 105
- After US/location filtering: 27
- With trustworthy posted_date: 27
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.375, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 16, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.634, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.595, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 2.647, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 9.492, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 0.653, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 0.634, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.606, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.51, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 22}

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
    "fetched_at": "2026-10-05T23:43:09.788468+00:00",
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
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:09.788468+00:00",
    "date_confidence": "high",
    "description": "We're looking for a Senior AI Application Engineer (.NET) to design, build, and scale intelligent enterprise applications powered by modern AI technologies. This role is ideal for "
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
    "fetched_at": "2026-10-05T23:43:09.788468+00:00",
    "date_confidence": "high",
    "description": "s a Lead DevOps Engineer reporting to the AVP – Systems and Network Administration, you'll play a critical role in building and operating intelligent automation platforms, AI agent"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026342",
    "title": "Markets Investigator",
    "location": "Washington DC; USA - Philadelphia - Pennsylvania; USA - New York City - New York",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/Washington-DC/Investigative-Data-Scientist-AI-Engineer_R0026342",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:09.788468+00:00",
    "date_confidence": "high",
    "description": "As a Markets Investigator , you'll play a critical role in protecting market integrity by combining investigative analysis with AI and data science to support Nasdaq's Investigatio"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026782",
    "title": "Software Engineer - Cloud Solutions & AI",
    "location": "USA - Boston - Massachusetts",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---Boston---Massachusetts/Software-Engineer---Cloud-Solutions---AI_R0026782",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:09.788468+00:00",
    "date_confidence": "high",
    "description": "As a Software Engineer reporting to the Senior Director of Software Engineering, you'll play a key role in building and improving the Nasdaq Questionnaires platform — a SaaS soluti"
  }
]
```

## PointClickCare

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/pointclickcare`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.340s
- Company elapsed time: 0.398s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 4 / 41
- Detail cache statuses: {'reused': 4}
- Relevant JD recovery: {'deterministic_skip': 36, 'eligible': 11, 'cache_reused': 4, 'ai_skip': 5, 'usable_jd': 11}
- Raw jobs found: 73
- After US/location filtering: 66
- With trustworthy posted_date: 66
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
    "fetched_at": "2026-10-05T23:43:23.768455+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "6b7f5c7a-372b-4a4a-8187-b2c347157e14",
    "title": "(Canada) Software Implementation Consultant - Clinical",
    "location": "Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/6b7f5c7a-372b-4a4a-8187-b2c347157e14",
    "posted_date": "2026-07-09",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:23.768455+00:00",
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
    "fetched_at": "2026-10-05T23:43:23.768455+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "e6fd28a0-e062-499d-8004-ea3280e62f4e",
    "title": "(US) Software Implementation Consultant - Clinical",
    "location": "Remote, USA",
    "official_url": "https://jobs.lever.co/pointclickcare/e6fd28a0-e062-499d-8004-ea3280e62f4e",
    "posted_date": "2026-07-09",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:23.768455+00:00",
    "date_confidence": "high",
    "description": "Principal implementation liaison on the project team documenting customer requirements, translating technical requirements into configuration setup, business processes and goals Le"
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "4ef6a183-4c22-4103-9278-26b07185bc8e",
    "title": "Accounts Receivable Specialist (6 month contract)",
    "location": "Mississauga, Ontario",
    "official_url": "https://jobs.lever.co/pointclickcare/4ef6a183-4c22-4103-9278-26b07185bc8e",
    "posted_date": "2026-08-20",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:23.768455+00:00",
    "date_confidence": "high",
    "description": "Collection’s activities relating to mixed portfolio of customer accounts, including communication with clients regarding collections issues, actions, payment inquiries and invoicin"
  }
]
```

## Stryker

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://stryker.wd1.myworkdayjobs.com/StrykerCareers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 20
- HTTP requests/cumulative request time: 150 / 60.377s
- Company elapsed time: 79.909s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 129 / 0 / 0
- Detail cache statuses: {'fetched:new': 129}
- Relevant JD recovery: {'eligible': 56, 'usable_jd': 56}
- Raw jobs found: 224
- After US/location filtering: 129
- With trustworthy posted_date: 129
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 16.848, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 28, "stop_reason": "early_stop", "unique_contribution": 25, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 1.188, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.701, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 11.582, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 21.467, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.78, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 1.177, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.747, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 17.522, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 73, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 73}

Sample normalized records:

```json
[
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R573258",
    "title": "Senior Manager, Cybersecurity, AI SOC & Crisis Management - Remote",
    "location": "Michigan, Kalamazoo 4100 East Milham Rd",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Michigan-Kalamazoo-4100-East-Milham-Rd/Senior-Manager--Cybersecurity--AI-SOC---Crisis-Management---Remote_R573258-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:24.167014+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Remote Preference will be given to candidates residing in the Eastern or Central time zones. As a Senior Manager, AI Security Operations & Crisis Management, you "
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
    "fetched_at": "2026-10-05T23:43:24.167014+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid It's Time to Join Stryker! Stryker is seeking a Senior Staff Product Owner, Voice Intelligence to help shape the next generation of intelligent caregiver c"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R571646",
    "title": "Senior Manager - R&D",
    "location": "San Diego, California",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/San-Diego-California/Senior-Manager---R-D_R571646",
    "posted_date": "2026-09-02",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:24.167014+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid Stryker is seeking a Senior Engineering Manager to lead the development and support of the SmartCare platform, including cloud services, web applications, "
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
    "fetched_at": "2026-10-05T23:43:24.167014+00:00",
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
    "fetched_at": "2026-10-05T23:43:24.167014+00:00",
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
- Pages/requests fetched: 15
- HTTP requests/cumulative request time: 47 / 15.058s
- Company elapsed time: 20.492s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 31 / 0 / 0
- Detail cache statuses: {'fetched:new': 31}
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 128
- After US/location filtering: 31
- With trustworthy posted_date: 31
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.866, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 27, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 0.452, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.724, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.419, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 2.02, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 0.475, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 2.016, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 0.441, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.454, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}

Sample normalized records:

```json
[
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19041689",
    "title": "Vice President, Global Network Engineering",
    "location": "Chicago, Illinois",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Vice-President--Global-Network-Engineering_19041689",
    "posted_date": "2026-08-07",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:34.613245+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The Global Infrastructure, Engineering & Operations (GIO) organization "
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
    "fetched_at": "2026-10-05T23:43:34.613245+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The Core Online team is responsible for building and supporting global "
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19041837",
    "title": "Security Automation Engineer",
    "location": "Chicago, Illinois; Reston, Virginia; Crum Lynne, Pennsylvania",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Security-Automation-Engineer_19041837",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:34.613245+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The SOAR Development team designs and delivers automation capabilities "
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19041688",
    "title": "Vice President, Global Operations Management & AIOps",
    "location": "Chicago, Illinois",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Vice-President--Global-Operations-Management---AIOps_19041688",
    "posted_date": "2026-08-07",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:34.613245+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The Global Infrastructure, Engineering & Operations (GIO) organization "
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042097",
    "title": "Lead Data Scientist AI Research & Innovation",
    "location": "Chicago, Illinois",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/AI-Research---Innovation-Lead_19042097",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:34.613245+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview This role reports directly to Senior Manager, Data Science & Analytics "
  }
]
```

## Travelers

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://travelers.wd5.myworkdayjobs.com/External`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 120 / 46.223s
- Company elapsed time: 62.952s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 95 / 0 / 0
- Detail cache statuses: {'fetched:new': 92, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 51, 'usable_jd': 51}
- Raw jobs found: 342
- After US/location filtering: 95
- With trustworthy posted_date: 95
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 21.358, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 40, "stop_reason": "early_stop", "unique_contribution": 40, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 5.336, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 2.317, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 9.039, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 54, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 12.077, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.695, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 2.778, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 2.477, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.127, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 58}

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
    "posted_date": "2026-08-19",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:36.717047+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51344",
    "title": "Software Engineer II (AI, Python, Typescript)",
    "location": "CT - Hartford; MN - St. Paul",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Software-Engineer-II--AI--Python--Typescript-_R-51344",
    "posted_date": "2026-07-08",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:36.717047+00:00",
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
    "posted_date": "2026-08-04",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:36.717047+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51887",
    "title": "Software Engineer II – AI Agents & Harnesses",
    "location": "GA - Atlanta; CT - Hartford",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/GA---Atlanta/Software-Engineer-II---AI-Agents---Harnesses_R-51887",
    "posted_date": "2026-09-21",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:36.717047+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51943",
    "title": "Software Engineer I – AI Agents & Harnesses",
    "location": "GA - Atlanta; CT - Hartford",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/GA---Atlanta/Software-Engineer-I---AI-Agents---Harnesses_R-51943",
    "posted_date": "2026-09-21",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:36.717047+00:00",
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
- HTTP requests/cumulative request time: 23 / 3.366s
- Company elapsed time: 3.715s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 17 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 27
- After US/location filtering: 17
- With trustworthy posted_date: 17
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.511, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.39, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.447, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.673, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.314, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.38, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}

Sample normalized records:

```json
[
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1101425",
    "title": "Principal Firmware Engineer",
    "location": "Irving, Texas",
    "official_url": "https://mycareer.verizon.com/jobs/r-1101425/principal-firmware-engineer/",
    "posted_date": "2026-09-30",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:55.105997+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1101085",
    "title": "Assoc Director - Responsible AI",
    "location": "Irving, Texas; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1101085/assoc-director-responsible-ai/",
    "posted_date": "2026-09-20",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:55.105997+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1101071",
    "title": "Senior Agentic AI Engineer",
    "location": "Basking Ridge, New Jersey; Lake Mary, Florida; Irving, Texas; Boston, Massachusetts",
    "official_url": "https://mycareer.verizon.com/jobs/r-1101071/senior-agentic-ai-engineer/",
    "posted_date": "2026-09-25",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:55.105997+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1101033",
    "title": "AI Workflow Engineer",
    "location": "Rolling Meadows, Illinois; Irving, Texas; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1101033/ai-workflow-engineer/",
    "posted_date": "2026-09-24",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:55.105997+00:00",
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
    "posted_date": "2026-09-22",
    "updated_date": "",
    "fetched_at": "2026-10-05T23:43:55.105997+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.181s
- Company elapsed time: 0.235s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 2, 'usable_jd': 2}
- Raw jobs found: 22
- After US/location filtering: 11
- With trustworthy posted_date: 11
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8046381",
    "title": "Customer Success Manager, Enterprise",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8046381",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:43:58.822005+00:00",
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
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-05T23:43:58.822005+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "7914932",
    "title": "Director, Sales Operations",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/7914932",
    "posted_date": "2026-06-10",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:43:58.822005+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "657947",
    "title": "General Referral",
    "location": "All Locations; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/657947",
    "posted_date": "2020-02-24",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:43:58.822005+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8002946",
    "title": "Sales Coordinator",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8002946",
    "posted_date": "2026-06-22",
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-05T23:43:58.822005+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
