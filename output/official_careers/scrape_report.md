# Official careers scrape report — 2026-10-04_1431

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Runtime metrics

- Wall time: 907.529s
- HTTP requests/cumulative request time: 8121 / 2983.662s
- Listing pages/detail fetched/cache reused/prefilter skipped: 1404 / 6678 / 289 / 755
- Detail cache statuses: {'fetched:missing_detail': 220, 'fetched:new': 6227, 'reused': 289}
- Relevant JD coverage: 5591 / 5662; added detail requests 71 / 150; deferred 0

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 45
- HTTP requests/cumulative request time: 45 / 13.207s
- Company elapsed time: 28.928s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 137, 'usable_jd': 137}
- Raw jobs found: 848
- After US/location filtering: 283
- With trustworthy posted_date: 283
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.278, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "\"Ai Engineer\"", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.086, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Machine Learning Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.395, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Data Scientist\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.249, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "\"Solutions Architect\"", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.209, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "\"Data Engineer\"", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 1.944, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Platform Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.075, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Full Stack Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.009, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "\"Forward Deployed Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.137, "first_pass_survivors": 114, "group": "official", "jds_resolved": 114, "original_postings_resolved": 114, "page_budget": 12, "pages_fetched": 10, "query": "\"Software Engineer\"", "raw_jobs": 200, "stop_reason": "early_stop", "unique_contribution": 114, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 2.119, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Infrastructure Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.754, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 5, "pages_fetched": 5, "query": "\"Software Engineer III\"", "raw_jobs": 81, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 81}
- Query diagnostic: {"elapsed_seconds": 1.292, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "\"Web Solutions Engineer\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 1.38, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 2, "pages_fetched": 2, "query": "\"DeepMind\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "83358034763358918",
    "title": "Senior Software Engineer, Generative AI, Ads Safety",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/83358034763358918-senior-software-engineer-generative-ai-ads-safety",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:31:09.948607+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "75652657275904710",
    "title": "Software Engineer III, App Ads Horizontal Modeling",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/75652657275904710-software-engineer-iii-app-ads-horizontal-modeling",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:31:09.948607+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "134020781792207558",
    "title": "Senior Software Engineer, Analytics Engineering",
    "location": "San Jose, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/134020781792207558-senior-software-engineer-analytics-engineering",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:31:09.948607+00:00",
    "date_confidence": "high",
    "description": "Our AI Systems Knowledge and Intelligence Engine (ASKIE) team is seeking a full stack insights Senior Software Engineer. In this role, you will be responsible for building Google's"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "87457161382109894",
    "title": "Software Engineer III, AI/ML, Google Cloud AI",
    "location": "Sunnyvale, CA, USA; Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/87457161382109894-software-engineer-iii-ai-ml-google-cloud-ai",
    "posted_date": "2025-12-17",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:31:09.948607+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "81595622850732742",
    "title": "Data Scientist III, Research",
    "location": "Mountain View, CA, USA; New York, NY, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/81595622850732742-data-scientist-iii-research",
    "posted_date": "2026-09-23",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:31:09.948607+00:00",
    "date_confidence": "high",
    "description": "Google is and always will be an engineering company. We hire people with a broad set of technical skills who are ready to take on some of technology's greatest challenges and make "
  }
]
```

## Amazon

- Status: ok
- Scraping method: HTTP GET search.json
- Search URL/API: `https://www.amazon.jobs/en/search?base_query=software+engineer&country=USA&offset=0&result_limit=10&sort=recent`
- Pagination: newest-first offset by 20; minimum 2 pages, then two seen pages + one overlap page; otherwise hits/cap
- Pages/requests fetched: 44
- HTTP requests/cumulative request time: 44 / 13.168s
- Company elapsed time: 24.533s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 459, 'usable_jd': 459}
- Raw jobs found: 809
- After US/location filtering: 709
- With trustworthy posted_date: 709
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.844, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 1.486, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 1.658, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.976, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.712, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.277, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 0.269, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.33, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 7.108, "first_pass_survivors": 207, "group": "official", "jds_resolved": 207, "original_postings_resolved": 207, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 207, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.562, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.856, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "systems development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.207, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.246, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 2, "pages_fetched": 2, "query": "applied scientist", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10568156",
    "title": "Software Development Engineer, AWS Agentic AI",
    "location": "Bellevue, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10568156/software-development-engineer-aws-agentic-ai",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:31:09.949177+00:00",
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
    "fetched_at": "2026-10-04T14:31:09.949177+00:00",
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
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:31:09.949177+00:00",
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
    "fetched_at": "2026-10-04T14:31:09.949177+00:00",
    "date_confidence": "high",
    "description": "Interested in building the future of intelligent AI agents? The Agentic AI organization at AWS is on a mission to empower developers and enterprises to store and retrieve memory fo"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10566213",
    "title": "Software Development Engineer, Agentic AI",
    "location": "Jersey City, New Jersey, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10566213/software-development-engineer-agentic-ai",
    "posted_date": "2026-10-01",
    "updated_date": "2026-09-30",
    "fetched_at": "2026-10-04T14:31:09.949177+00:00",
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
- HTTP requests/cumulative request time: 42 / 15.514s
- Company elapsed time: 30.468s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 186, 'usable_jd': 186}
- Raw jobs found: 840
- After US/location filtering: 285
- With trustworthy posted_date: 285
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.553, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.184, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.163, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.265, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.125, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.124, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.165, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.079, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.683, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.127, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "apps-and-frameworks-SFTWR-AF", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200686152-3956",
    "title": "Director, Software Test Engineering & Quality Assurance",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200686152/director-software-test-engineering-quality-assurance",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.950201+00:00",
    "date_confidence": "high",
    "description": "At Apple, the systems and technology that power our internal operations, supply chain, and customer support are just as important as the products we build. The IS&T, Operations, an"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200682696-3956",
    "title": "Machine Learning Scientist - AppleCare WW Demand Planning",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200682696/machine-learning-scientist-applecare-ww-demand-planning",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.950201+00:00",
    "date_confidence": "high",
    "description": "Imagine what you could do here! The people here at Apple don’t just create products — they build the kind of wonder that’s revolutionized industries. It’s the diversity of those pe"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200674598-0836",
    "title": "Finance Specialist, Apple Watch",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200674598/finance-specialist-apple-watch",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.950201+00:00",
    "date_confidence": "high",
    "description": "Apple Watch Finance Specialist is responsible for leading a broad cross-functional team in discussion of Watch program budgets, leveraging a strong financial acumen to drive toward"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200686929-0836",
    "title": "Photonics Test Development Hardware Engineer",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200686929/photonics-test-development-hardware-engineer",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.950201+00:00",
    "date_confidence": "high",
    "description": "Apple is looking for a Photonics Test Development Hardware Engineer with strong optics lab skills, coding experience, and passion in scaling technology from prototype to high-volum"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200661915-0836",
    "title": "AIML - Manager, Applied AI Science - GenAI Model Autograding, Evaluation",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200661915/aiml-manager-applied-ai-science-genai-model-autograding-evaluation",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.950201+00:00",
    "date_confidence": "high",
    "description": "Do you get excited by building and leading a team that redefines how AI products are evaluated? Our Evaluation organization is responsible for providing principled assessments acro"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 234 / 47.534s
- Company elapsed time: 81.227s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 194 / 0 / 0
- Detail cache statuses: {'fetched:new': 176, 'fetched:missing_detail': 18}
- Relevant JD recovery: {'eligible': 58, 'usable_jd': 58}
- Raw jobs found: 390
- After US/location filtering: 194
- With trustworthy posted_date: 194
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 21.713, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.749, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 10.932, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.351, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.7, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.217, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.578, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.171, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 18.602, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 120}

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200059415",
    "title": "Senior Data Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557022600",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.951342+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft is a company where passionate innovators come to collaborate, envision what can be, and take their careers further. Imagine being at the forefront of a revolutio"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200045421",
    "title": "Principal Data Scientist - AI Infrastructure",
    "location": "United States, Multiple Locations, Multiple Locations",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556944486",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.951342+00:00",
    "date_confidence": "high",
    "description": "Overview As a Principal Data Scientist – AI Infrastructure Data team member, you will own end-to-end delivery of strategic data science projects and partner with customers and inte"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200057982",
    "title": "Senior Digital Cloud Solution Architect",
    "location": "United States, North Dakota, Fargo; United States, Illinois, Chicago; United States, Texas, Dallas; United States, Washington, Seattle; United States, Arizona, Phoenix; United States, California, San Diego; United States, California, Los Angeles; United States, Oregon, Portland; United States, Colorado, Denver",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557007962",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.951342+00:00",
    "date_confidence": "high",
    "description": "Overview At Small Medium Enterprises and Channel (SME&C), we are leading a high-growth, AI-powered global sales team—one that is deeply connected to our partners and driven by cust"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200048154",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556960555",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.951342+00:00",
    "date_confidence": "high",
    "description": "Overview Join the Quality, Reliability, and Telemetry (QRT) team and help reinvent how Windows is tested, validated, and proven across the broader hardware ecosystem. Our charter i"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200059113",
    "title": "Principal SWE Lead",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557021613",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.951342+00:00",
    "date_confidence": "high",
    "description": "Overview MCAPS-Core accelerates customer outcomes and business growth. By uniting product, engineering, marketing, sales, customer success, and partners around a common customer mi"
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 631 / 228.344s
- Company elapsed time: 310.964s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 588 / 0 / 0
- Detail cache statuses: {'fetched:new': 580, 'fetched:missing_detail': 8}
- Relevant JD recovery: {'eligible': 84, 'usable_jd': 84}
- Raw jobs found: 840
- After US/location filtering: 588
- With trustworthy posted_date: 588
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 57.954, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 28.087, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 23.749, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.354, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 22.239, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 23.032, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 26.789, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.24, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 79.05, "first_pass_survivors": 158, "group": "official", "jds_resolved": 158, "original_postings_resolved": 158, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 158, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 13.009, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2019190",
    "title": "Applied AI Engineer - VLSI Design",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Applied-AI-Engineer---VLSI-Design_JR2019190",
    "posted_date": "2026-08-17",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.952003+00:00",
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
    "fetched_at": "2026-10-04T14:31:09.952003+00:00",
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
    "fetched_at": "2026-10-04T14:31:09.952003+00:00",
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
    "fetched_at": "2026-10-04T14:31:09.952003+00:00",
    "date_confidence": "high",
    "description": "We are looking for a strong engineer to join the DRIVE Road Structure / Online Mapping / Context Fusion team. In this role, you will help craft and guide the future of our L3/L4 au"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2017423",
    "title": "Senior AI Frameworks Engineer",
    "location": "US, CA, Santa Clara; US, TX, Austin",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-AI-Frameworks-Engineer_JR2017423",
    "posted_date": "2026-05-28",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:09.952003+00:00",
    "date_confidence": "high",
    "description": "We are now looking for a Senior AI Frameworks Engineer (C++/Python)! NVIDIA's high-performance computing platforms are powering the AI revolution across many applications and indus"
  }
]
```

## Salesforce

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://salesforce.wd12.myworkdayjobs.com/External_Career_Site`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 36
- HTTP requests/cumulative request time: 304 / 74.073s
- Company elapsed time: 114.837s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 267 / 0 / 0
- Detail cache statuses: {'fetched:new': 263, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 66, 'usable_jd': 66}
- Raw jobs found: 616
- After US/location filtering: 267
- With trustworthy posted_date: 267
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 41.671, "first_pass_survivors": 114, "group": "official", "jds_resolved": 114, "original_postings_resolved": 114, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 114, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.775, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 3.171, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 6.736, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.024, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.168, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.106, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 5.058, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 42.192, "first_pass_survivors": 99, "group": "official", "jds_resolved": 99, "original_postings_resolved": 99, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 214, "stop_reason": "page_budget", "unique_contribution": 99, "unique_jobs": 214}
- Query diagnostic: {"elapsed_seconds": 0.407, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineering mts", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 13}

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR362683",
    "title": "Named Account Executive, K-12",
    "location": "Georgia - Atlanta Metro - Remote; Florida - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Georgia---Atlanta-Metro---Remote/Named-Account-Executive--K-12_JR362683",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:34.483531+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR355941",
    "title": "Software Engineering MTS",
    "location": "California - San Francisco; Washington - Bellevue",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Software-Engineering-MTS_JR355941",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:34.483531+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR362345",
    "title": "Technology Auditor, Internal Audit",
    "location": "Texas - Dallas; Georgia - Atlanta; Indiana - Indianapolis",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Texas---Dallas/Technology-Auditor--Internal-Audit_JR362345",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:34.483531+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Finance Job Details"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR340462",
    "title": "Senior/Lead Software Engineer, Site Reliability (Agentforce Operations)",
    "location": "California - San Francisco; Washington - Seattle; New York - New York",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Senior-Lead-Principal-Software-Engineer--Agentforce-for-Supply-Chain_JR340462",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:34.483531+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357830",
    "title": "Site Reliability Engineer (MTS) GovCloud 24x7",
    "location": "Colorado - Denver; Massachusetts - Burlington; Virginia - Mclean",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Colorado---Denver/Site-Reliability-Engineer--GovCloud-24x7_JR357830-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:34.483531+00:00",
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
- Pages/requests fetched: 38
- HTTP requests/cumulative request time: 243 / 91.892s
- Company elapsed time: 126.078s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 204 / 0 / 0
- Detail cache statuses: {'fetched:new': 203, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 57, 'usable_jd': 57}
- Raw jobs found: 672
- After US/location filtering: 204
- With trustworthy posted_date: 204
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 67.383, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 9.263, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.872, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 13.093, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.779, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.742, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.578, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 2.661, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.722, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 12, "pages_fetched": 8, "query": "software engineer", "raw_jobs": 121, "stop_reason": "early_stop", "unique_contribution": 24, "unique_jobs": 121}
- Query diagnostic: {"elapsed_seconds": 2.222, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R168901",
    "title": "Applied AI Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Applied-AI-Engineer_R168901",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:38.877294+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are looking for a hands-on AI Agent Engineer to develop, build, and maintain intelligent agents that drive automation and business impact across the enterprise. "
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170716",
    "title": "AI Engineer 4",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/AI-Engineer-4_R170716-1",
    "posted_date": "2026-09-23",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:38.877294+00:00",
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
    "fetched_at": "2026-10-04T14:31:38.877294+00:00",
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
    "fetched_at": "2026-10-04T14:31:38.877294+00:00",
    "date_confidence": "high",
    "description": "Senior SRE — RTCDP Datastores & AI/ML Ops Adobe’s Real-Time Customer Data Platform (RTCDP) powers personalized experiences for some of the world’s largest brands. As a Senior SRE o"
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
    "fetched_at": "2026-10-04T14:31:38.877294+00:00",
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
- HTTP requests/cumulative request time: 52 / 34.108s
- Company elapsed time: 35.039s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 40 / 164 / 462
- Detail cache statuses: {'reused': 164}
- Relevant JD recovery: {'cache_reused': 164, 'eligible': 204, 'deterministic_skip': 312, 'ai_skip': 150, 'ai_recover': 9, 'detail_requests': 40, 'detail_failure': 40, 'budget_deferred': 0, 'usable_jd': 164}
- Raw jobs found: 2188
- After US/location filtering: 666
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.784, "first_pass_survivors": 404, "group": "official", "jds_resolved": 0, "original_postings_resolved": 404, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 502, "stop_reason": "page_budget", "unique_contribution": 404, "unique_jobs": 502}
- Query diagnostic: {"elapsed_seconds": 0.658, "first_pass_survivors": 23, "group": "official", "jds_resolved": 0, "original_postings_resolved": 23, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 94, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 94}
- Query diagnostic: {"elapsed_seconds": 0.705, "first_pass_survivors": 37, "group": "official", "jds_resolved": 0, "original_postings_resolved": 37, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 116, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 116}
- Query diagnostic: {"elapsed_seconds": 0.529, "first_pass_survivors": 24, "group": "official", "jds_resolved": 0, "original_postings_resolved": 24, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 164, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 164}
- Query diagnostic: {"elapsed_seconds": 0.76, "first_pass_survivors": 140, "group": "official", "jds_resolved": 0, "original_postings_resolved": 140, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 581, "stop_reason": "page_budget", "unique_contribution": 140, "unique_jobs": 581}
- Query diagnostic: {"elapsed_seconds": 0.703, "first_pass_survivors": 26, "group": "official", "jds_resolved": 0, "original_postings_resolved": 26, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 344, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 344}
- Query diagnostic: {"elapsed_seconds": 0.575, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 0.427, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.584, "first_pass_survivors": 11, "group": "official", "jds_resolved": 0, "original_postings_resolved": 11, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 325, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 325}

Sample normalized records:

```json
[
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "704019139159184",
    "title": "Software Engineer (Leadership) - Infrastructure",
    "location": "Sunnyvale, CA; Remote, US; Bellevue, WA; Redmond, WA; Menlo Park, CA; Seattle, WA; Burlingame, CA; New York, NY",
    "official_url": "https://www.metacareers.com/jobs/704019139159184",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:40.419504+00:00",
    "date_confidence": "unknown",
    "description": "Meta is seeking talented principal engineers to join our teams in building cutting-edge products that connect billions of people around the world. As a member of our team, you will"
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1769900794137147",
    "title": "Technical Program Manager — Developer Productivity",
    "location": "Sunnyvale, CA; Bellevue, WA; Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/1769900794137147",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:40.419504+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1755698129195699",
    "title": "Network Engineer, Optical Deployment",
    "location": "Denver, CO; Temple, TX; Reston, VA; Menlo Park, CA; Seattle, WA; Papillion, NE; Aurora, IL; Garland, TX; Huntsville, AL; Houston, TX",
    "official_url": "https://www.metacareers.com/jobs/1755698129195699",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:40.419504+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1398363652114607",
    "title": "Reality Labs Digital Accounting Manager",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/1398363652114607",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:40.419504+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1124926043220059",
    "title": "Regulatory Escalations Manager",
    "location": "Austin, TX",
    "official_url": "https://www.metacareers.com/jobs/1124926043220059",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:31:40.419504+00:00",
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
- HTTP requests/cumulative request time: 26 / 21.160s
- Company elapsed time: 25.175s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 416, 'usable_jd': 416}
- Raw jobs found: 1239
- After US/location filtering: 707
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.815, "first_pass_survivors": 200, "group": "official", "jds_resolved": 200, "original_postings_resolved": 200, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 200, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 3.463, "first_pass_survivors": 132, "group": "official", "jds_resolved": 132, "original_postings_resolved": 132, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 132, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.77, "first_pass_survivors": 110, "group": "official", "jds_resolved": 110, "original_postings_resolved": 110, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 110, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.497, "first_pass_survivors": 78, "group": "official", "jds_resolved": 78, "original_postings_resolved": 78, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 78, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.652, "first_pass_survivors": 62, "group": "official", "jds_resolved": 62, "original_postings_resolved": 62, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 62, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.136, "first_pass_survivors": 61, "group": "official", "jds_resolved": 61, "original_postings_resolved": 61, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 61, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 1.658, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 88, "stop_reason": "early_stop", "unique_contribution": 22, "unique_jobs": 88}
- Query diagnostic: {"elapsed_seconds": 0.553, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 3.631, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 200}

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
    "fetched_at": "2026-10-04T14:31:46.950439+00:00",
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
    "fetched_at": "2026-10-04T14:31:46.950439+00:00",
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
    "fetched_at": "2026-10-04T14:31:46.950439+00:00",
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
    "fetched_at": "2026-10-04T14:31:46.950439+00:00",
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
    "fetched_at": "2026-10-04T14:31:46.950439+00:00",
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
- Pages/requests fetched: 29
- HTTP requests/cumulative request time: 187 / 55.813s
- Company elapsed time: 81.253s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 158 / 0 / 0
- Detail cache statuses: {'fetched:new': 152, 'fetched:missing_detail': 6}
- Relevant JD recovery: {'eligible': 27, 'usable_jd': 27}
- Raw jobs found: 537
- After US/location filtering: 158
- With trustworthy posted_date: 158
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 33.741, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 6, "pages_fetched": 5, "query": "ai engineer", "raw_jobs": 89, "stop_reason": "early_stop", "unique_contribution": 80, "unique_jobs": 89}
- Query diagnostic: {"elapsed_seconds": 9.731, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.957, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 7.03, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 7.063, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.797, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.128, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.024, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 52, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 52}
- Query diagnostic: {"elapsed_seconds": 6.781, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 12, "pages_fetched": 5, "query": "software engineer", "raw_jobs": 96, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 96}

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
    "fetched_at": "2026-10-04T14:32:12.126850+00:00",
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
    "fetched_at": "2026-10-04T14:32:12.126850+00:00",
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
    "fetched_at": "2026-10-04T14:32:12.126850+00:00",
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
    "fetched_at": "2026-10-04T14:32:12.126850+00:00",
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
    "fetched_at": "2026-10-04T14:32:12.126850+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.512s
- Company elapsed time: 1.977s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 111, 'usable_jd': 111}
- Raw jobs found: 458
- After US/location filtering: 457
- With trustworthy posted_date: 457
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
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-04T14:32:31.179313+00:00",
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
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-04T14:32:31.179313+00:00",
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
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-04T14:32:31.179313+00:00",
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
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-04T14:32:31.179313+00:00",
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
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-04T14:32:31.179313+00:00",
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
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 127 / 47.451s
- Company elapsed time: 64.588s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 100 / 0 / 0
- Detail cache statuses: {'fetched:new': 97, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 17, 'usable_jd': 17}
- Raw jobs found: 361
- After US/location filtering: 100
- With trustworthy posted_date: 100
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.002, "first_pass_survivors": 62, "group": "official", "jds_resolved": 62, "original_postings_resolved": 62, "page_budget": 6, "pages_fetched": 5, "query": "ai engineer", "raw_jobs": 75, "stop_reason": "early_stop", "unique_contribution": 62, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 3.811, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 37, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 0.643, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 5.132, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 6.363, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.662, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.985, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.705, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 7.563, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 12, "pages_fetched": 6, "query": "software engineer", "raw_jobs": 81, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 81}

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
    "fetched_at": "2026-10-04T14:32:33.157088+00:00",
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
    "fetched_at": "2026-10-04T14:32:33.157088+00:00",
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
    "fetched_at": "2026-10-04T14:32:33.157088+00:00",
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
    "fetched_at": "2026-10-04T14:32:33.157088+00:00",
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
    "fetched_at": "2026-10-04T14:32:33.157088+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.157s
- Company elapsed time: 0.485s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 21, 'usable_jd': 21}
- Raw jobs found: 168
- After US/location filtering: 128
- With trustworthy posted_date: 128
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
    "fetched_at": "2026-10-04T14:33:29.321384+00:00",
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
    "fetched_at": "2026-10-04T14:33:29.321384+00:00",
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
    "fetched_at": "2026-10-04T14:33:29.321384+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8223489",
    "title": "Client Account Manager II, CPG",
    "location": "New York, NY, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8223489",
    "posted_date": "2026-10-01",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:33:29.321384+00:00",
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
    "fetched_at": "2026-10-04T14:33:29.321384+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.189s
- Company elapsed time: 0.481s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 41, 'usable_jd': 41}
- Raw jobs found: 348
- After US/location filtering: 253
- With trustworthy posted_date: 253
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
    "fetched_at": "2026-10-04T14:33:29.807494+00:00",
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
    "fetched_at": "2026-10-04T14:33:29.807494+00:00",
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
    "fetched_at": "2026-10-04T14:33:29.807494+00:00",
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
    "fetched_at": "2026-10-04T14:33:29.807494+00:00",
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
    "fetched_at": "2026-10-04T14:33:29.807494+00:00",
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
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 420 / 188.046s
- Company elapsed time: 239.997s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 399 / 0 / 0
- Detail cache statuses: {'fetched:new': 399}
- Relevant JD recovery: {'eligible': 49, 'usable_jd': 49}
- Raw jobs found: 1805
- After US/location filtering: 399
- With trustworthy posted_date: 399
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 173.399, "first_pass_survivors": 300, "group": "official", "jds_resolved": 300, "original_postings_resolved": 300, "page_budget": 6, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 300, "stop_reason": "early_stop", "unique_contribution": 300, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 1.227, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 106, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 106}
- Query diagnostic: {"elapsed_seconds": 9.316, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 170, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 170}
- Query diagnostic: {"elapsed_seconds": 46.978, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 261, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 261}
- Query diagnostic: {"elapsed_seconds": 1.696, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 284, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 284}
- Query diagnostic: {"elapsed_seconds": 4.266, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 0.431, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 77, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 77}
- Query diagnostic: {"elapsed_seconds": 0.434, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 49, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 2.25, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 12, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 258, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 258}

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075717",
    "title": "Sr Software Engineer",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153333219-sr-software-engineer",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:30.289401+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076058",
    "title": "Software Engineer, Core Infrastructure - Moveworks (New Grad)",
    "location": "Mountain View, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153279380-software-engineer-core-infrastructure-moveworks-new-grad-",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:30.289401+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075819",
    "title": "Sr Mobile Software Engineer (Native Android and Backend)",
    "location": "San Diego, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153266480-sr-mobile-software-engineer-native-android-and-backend-",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:30.289401+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075885",
    "title": "Sr Software Engineer, Platform Cryptography",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153256860-sr-software-engineer-platform-cryptography",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:30.289401+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075885",
    "title": "Sr Software Engineer, Platform Cryptography",
    "location": "San Diego, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000153256639-sr-software-engineer-platform-cryptography",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:30.289401+00:00",
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
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 91 / 95.311s
- Company elapsed time: 114.027s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 52 / 28 / 78
- Detail cache statuses: {'fetched:new': 51, 'reused': 28}
- Relevant JD recovery: {'deterministic_skip': 49, 'ai_skip': 29, 'eligible': 1, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 0}
- Raw jobs found: 468
- After US/location filtering: 79
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 42.835, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 72, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 72}
- Query diagnostic: {"elapsed_seconds": 4.375, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.41, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.427, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.427, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.375, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.411, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.389, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 39.015, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 144, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 144}

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45046",
    "title": "Senior Full-Stack Qlik Sense Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Full-Stack-Qlik-Sense-Engineer/45046",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:33.380996+00:00",
    "date_confidence": "unknown",
    "description": "Senior Full-Stack Qlik Sense Engineer"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45045",
    "title": "Financial Analyst – Electronic Markets Sales Finance",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Financial-Analyst-Electronic-Markets-Sales-Finance/45045",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:33.380996+00:00",
    "date_confidence": "unknown",
    "description": "Financial Analyst – Electronic Markets Sales Finance"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45036",
    "title": "Project Manager – Financial Management Systems and Solutions – New York - Contractor",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Project-Manager-Financial-Management-Systems-and-Solutions-New-York-Contractor/45036",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:33.380996+00:00",
    "date_confidence": "unknown",
    "description": "Project Manager – Financial Management Systems and Solutions – New York - Contractor"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45035",
    "title": "Bloomberg On-Site Support Specialist",
    "location": "San Francisco, California, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Bloomberg-On-Site-Support-Specialist/45035",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:33.380996+00:00",
    "date_confidence": "unknown",
    "description": "Bloomberg On-Site Support Specialist"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "45033",
    "title": "Product Manager, Private Markets - Enterprise Data Products",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Product-Manager-Private-Markets-Enterprise-Data-Products/45033",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:33.380996+00:00",
    "date_confidence": "unknown",
    "description": "Product Manager, Private Markets - Enterprise Data Products"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 74
- HTTP requests/cumulative request time: 689 / 138.779s
- Company elapsed time: 232.469s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 615 / 0 / 0
- Detail cache statuses: {'fetched:new': 600, 'fetched:missing_detail': 15}
- Relevant JD recovery: {'eligible': 132, 'usable_jd': 132}
- Raw jobs found: 1472
- After US/location filtering: 615
- With trustworthy posted_date: 615
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 26.293, "first_pass_survivors": 78, "group": "official", "jds_resolved": 78, "original_postings_resolved": 78, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 78, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 12.745, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.088, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.101, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.504, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.041, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.123, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.317, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 31.735, "first_pass_survivors": 79, "group": "official", "jds_resolved": 79, "original_postings_resolved": 79, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 79, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 12.06, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "full stack", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.8, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "python react", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.069, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "pyspark databricks", "raw_jobs": 52, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 52}
- Query diagnostic: {"elapsed_seconds": 6.339, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "experienced software engineer java python", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.196, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "agentic ai", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.4, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.564, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "software engineer ii", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.684, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.374, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "security engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.335, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "quantitative developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.715, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "software engineer java spring", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.138, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "software engineer python authe", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.382, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "aws data platform engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.055, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "data engineer applied ai", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 3.408, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "asset management technology", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 20}

Sample normalized records:

```json
[
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210795809",
    "title": "AI Senior Lead Infrastructure Engineer",
    "location": "OH, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210795809",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:37.745784+00:00",
    "date_confidence": "high",
    "description": "Job responsibilities Lead the design and delivery of AI-enabled capabilities for Mainframe and Midrange systems management, focusing on intelligent automation that improves stabili"
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
    "fetched_at": "2026-10-04T14:33:37.745784+00:00",
    "date_confidence": "high",
    "description": "Be an integral part of an agile team that's constantly pushing the envelope to enhance, build, and deliver top-notch technology products. As a Senior Lead Software Engineer at JPMo"
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
    "fetched_at": "2026-10-04T14:33:37.745784+00:00",
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
    "fetched_at": "2026-10-04T14:33:37.745784+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorgan Chase, within the Co"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210795818",
    "title": "AI Senior Lead Infrastructure Engineer",
    "location": "Columbus, OH, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210795818",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:37.745784+00:00",
    "date_confidence": "high",
    "description": "Become a member of a team where you can contribute significantly to shaping the future of a world-renowned and influential company. Among top performers, you can make a direct and "
  }
]
```

## Capital One

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://capitalone.wd12.myworkdayjobs.com/Capital_One`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 37
- HTTP requests/cumulative request time: 312 / 114.950s
- Company elapsed time: 158.117s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 274 / 0 / 0
- Detail cache statuses: {'fetched:new': 181, 'fetched:missing_detail': 93}
- Relevant JD recovery: {'eligible': 115, 'usable_jd': 115}
- Raw jobs found: 726
- After US/location filtering: 274
- With trustworthy posted_date: 274
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 63.624, "first_pass_survivors": 117, "group": "official", "jds_resolved": 117, "original_postings_resolved": 117, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 117, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 16.425, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.304, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.871, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.582, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.367, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.357, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.339, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 47.003, "first_pass_survivors": 82, "group": "official", "jds_resolved": 82, "original_postings_resolved": 82, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 82, "unique_jobs": 240}

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1002949",
    "title": "AI Engineer 5 (MLX, Agentic AI, Gen AI platform Services)",
    "location": "San Jose, CA; San Francisco, CA; McLean, VA; Cambridge, MA; New York, NY",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/San-Jose-CA/AI-Engineer-5--MLX--Agentic-AI--Gen-AI-platform-Services-_R1002949-1",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:44.956050+00:00",
    "date_confidence": "high",
    "description": "AI Engineer 5 (MLX, Agentic AI, Gen AI platform Services) At Capital One, we are creating responsible and reliable AI systems, changing banking for good. For years, Capital One has"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1002940",
    "title": "Senior Associate, Data Scientist - Applied AI (Financial Services)",
    "location": "Plano, TX",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Plano-TX/Senior-Associate--Data-Scientist---Applied-AI--Financial-Services-_R1002940-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:44.956050+00:00",
    "date_confidence": "high",
    "description": "Senior Associate, Data Scientist - Applied AI (Financial Services) Data is at the center of everything we do. As a startup, we disrupted the credit card industry by individually pe"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1002300",
    "title": "Full-stack Engineer 4 (Go & Kubernetes) (Enterprise Platforms Technology)",
    "location": "Plano, TX",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Plano-TX/Full-stack-Engineer-4--Go---Kubernetes---Cloud-Operations-Resilience-Engineering-_R1002300-1",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:44.956050+00:00",
    "date_confidence": "high",
    "description": "Full-stack Engineer 4 (Go & Kubernetes) (Enterprise Platforms Technology) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problem"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001683",
    "title": "Data Analysis Manager - Office of the Chief Data Officer, Central Analytics",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Data-Analysis-Manager---Office-of-the-Chief-Data-Officer--Central-Analytics-and-Reporting_R1001683-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:44.956050+00:00",
    "date_confidence": "high",
    "description": "Data Analysis Manager - Office of the Chief Data Officer, Central Analytics At Capital One, data is at the center of everything we do. When we launched as a startup we disrupted th"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1002908",
    "title": "Full Stack Engineer 4",
    "location": "Plano, TX",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Plano-TX/Full-Stack-Engineer-4_R1002908-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:33:44.956050+00:00",
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
- Pages/requests fetched: 51
- HTTP requests/cumulative request time: 627 / 174.349s
- Company elapsed time: 258.471s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 576 / 0 / 0
- Detail cache statuses: {'fetched:new': 570, 'fetched:missing_detail': 6}
- Relevant JD recovery: {'eligible': 49, 'usable_jd': 49}
- Raw jobs found: 1014
- After US/location filtering: 576
- With trustworthy posted_date: 576
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 46.375, "first_pass_survivors": 116, "group": "official", "jds_resolved": 116, "original_postings_resolved": 116, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 116, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 15.639, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.236, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 18.617, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 21.278, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.725, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.832, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.113, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 59.323, "first_pass_survivors": 125, "group": "official", "jds_resolved": 125, "original_postings_resolved": 125, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 239, "stop_reason": "page_budget", "unique_contribution": 125, "unique_jobs": 234}
- Query diagnostic: {"elapsed_seconds": 13.305, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "core infrastructure", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 15.6, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "cleared site reliability engineer database", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 3.61, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software developer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 12.816, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "applications developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}

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
    "fetched_at": "2026-10-04T14:35:26.045679+00:00",
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
    "fetched_at": "2026-10-04T14:35:26.045679+00:00",
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
    "fetched_at": "2026-10-04T14:35:26.045679+00:00",
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
    "fetched_at": "2026-10-04T14:35:26.045679+00:00",
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
    "fetched_at": "2026-10-04T14:35:26.045679+00:00",
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
- HTTP requests/cumulative request time: 416 / 211.143s
- Company elapsed time: 266.863s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 387 / 0 / 0
- Detail cache statuses: {'fetched:new': 381, 'fetched:missing_detail': 6}
- Relevant JD recovery: {'eligible': 58, 'usable_jd': 58}
- Raw jobs found: 547
- After US/location filtering: 387
- With trustworthy posted_date: 387
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 53.42, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 26.072, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 42.88, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 26.113, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 27.668, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 23.452, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 32.79, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.239, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 21.312, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 7.019, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "usa software engineer ii", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 20}

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
    "fetched_at": "2026-10-04T14:36:20.917281+00:00",
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
    "fetched_at": "2026-10-04T14:36:20.917281+00:00",
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
    "fetched_at": "2026-10-04T14:36:20.917281+00:00",
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
    "fetched_at": "2026-10-04T14:36:20.917281+00:00",
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
    "fetched_at": "2026-10-04T14:36:20.917281+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.346s
- Company elapsed time: 1.251s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 75, 'usable_jd': 75}
- Raw jobs found: 405
- After US/location filtering: 401
- With trustworthy posted_date: 401
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
    "fetched_at": "2026-10-04T14:36:23.074415+00:00",
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
    "fetched_at": "2026-10-04T14:36:23.074415+00:00",
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
    "fetched_at": "2026-10-04T14:36:23.074415+00:00",
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
    "fetched_at": "2026-10-04T14:36:23.074415+00:00",
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
    "fetched_at": "2026-10-04T14:36:23.074415+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.230s
- Company elapsed time: 0.909s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 138, 'usable_jd': 138}
- Raw jobs found: 716
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
    "fetched_at": "2026-10-04T14:36:24.325952+00:00",
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
    "fetched_at": "2026-10-04T14:36:24.325952+00:00",
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
    "fetched_at": "2026-10-04T14:36:24.325952+00:00",
    "date_confidence": "high",
    "description": "<div class=\"JobPostPage-content ⚙ ⚙1opjj73\"> <h3 id=\"about-stripe\">About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies - from t"
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
    "fetched_at": "2026-10-04T14:36:24.325952+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s largest enterprises to the most am"
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
    "fetched_at": "2026-10-04T14:36:24.325952+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.231s
- Company elapsed time: 0.665s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 53, 'usable_jd': 53}
- Raw jobs found: 229
- After US/location filtering: 193
- With trustworthy posted_date: 193
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
    "fetched_at": "2026-10-04T14:36:25.235825+00:00",
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
    "fetched_at": "2026-10-04T14:36:25.235825+00:00",
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
    "fetched_at": "2026-10-04T14:36:25.235825+00:00",
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
    "fetched_at": "2026-10-04T14:36:25.235825+00:00",
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
    "fetched_at": "2026-10-04T14:36:25.235825+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.148s
- Company elapsed time: 0.552s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 50, 'usable_jd': 50}
- Raw jobs found: 162
- After US/location filtering: 147
- With trustworthy posted_date: 147
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
    "fetched_at": "2026-10-04T14:36:25.902063+00:00",
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
    "fetched_at": "2026-10-04T14:36:25.902063+00:00",
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
    "fetched_at": "2026-10-04T14:36:25.902063+00:00",
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
    "fetched_at": "2026-10-04T14:36:25.902063+00:00",
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
    "fetched_at": "2026-10-04T14:36:25.902063+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.148s
- Company elapsed time: 0.425s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 40, 'usable_jd': 40}
- Raw jobs found: 162
- After US/location filtering: 107
- With trustworthy posted_date: 107
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
    "fetched_at": "2026-10-04T14:36:26.460748+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all. Figma’s platform helps teams bring ideas"
  },
  {
    "company": "Figma",
    "source": "figma_official_careers",
    "job_id": "6143113004",
    "title": "Account Executive, Federal - Civilian",
    "location": "Washington, DC; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/6143113004?gh_jid=6143113004",
    "posted_date": "2026-08-14",
    "updated_date": "2026-08-14",
    "fetched_at": "2026-10-04T14:36:26.460748+00:00",
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
    "fetched_at": "2026-10-04T14:36:26.460748+00:00",
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
    "fetched_at": "2026-10-04T14:36:26.460748+00:00",
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
    "fetched_at": "2026-10-04T14:36:26.460748+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.210s
- Company elapsed time: 0.630s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 15, 'usable_jd': 15}
- Raw jobs found: 211
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
    "fetched_at": "2026-10-04T14:36:26.886754+00:00",
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
    "fetched_at": "2026-10-04T14:36:26.886754+00:00",
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
    "fetched_at": "2026-10-04T14:36:26.886754+00:00",
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
    "fetched_at": "2026-10-04T14:36:26.886754+00:00",
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
    "updated_date": "2026-09-29",
    "fetched_at": "2026-10-04T14:36:26.886754+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.117s
- Company elapsed time: 0.215s
- Incremental mode/page cap: full_sweep / 12
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
    "fetched_at": "2026-10-04T14:36:27.521489+00:00",
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
    "fetched_at": "2026-10-04T14:36:27.521489+00:00",
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
    "fetched_at": "2026-10-04T14:36:27.521489+00:00",
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
    "fetched_at": "2026-10-04T14:36:27.521489+00:00",
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
    "fetched_at": "2026-10-04T14:36:27.521489+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.119s
- Company elapsed time: 0.327s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 97
- After US/location filtering: 74
- With trustworthy posted_date: 74
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
    "fetched_at": "2026-10-04T14:36:27.734342+00:00",
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
    "fetched_at": "2026-10-04T14:36:27.734342+00:00",
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
    "fetched_at": "2026-10-04T14:36:27.734342+00:00",
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
    "fetched_at": "2026-10-04T14:36:27.734342+00:00",
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
    "fetched_at": "2026-10-04T14:36:27.734342+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.129s
- Company elapsed time: 0.700s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 48, 'usable_jd': 48}
- Raw jobs found: 282
- After US/location filtering: 275
- With trustworthy posted_date: 275
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
    "fetched_at": "2026-10-04T14:36:28.063469+00:00",
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
    "fetched_at": "2026-10-04T14:36:28.063469+00:00",
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
    "fetched_at": "2026-10-04T14:36:28.063469+00:00",
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
    "fetched_at": "2026-10-04T14:36:28.063469+00:00",
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
    "fetched_at": "2026-10-04T14:36:28.063469+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.190s
- Company elapsed time: 0.857s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 43, 'usable_jd': 43}
- Raw jobs found: 247
- After US/location filtering: 205
- With trustworthy posted_date: 205
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
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-04T14:36:28.763987+00:00",
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
    "fetched_at": "2026-10-04T14:36:28.763987+00:00",
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
    "updated_date": "2026-09-25",
    "fetched_at": "2026-10-04T14:36:28.763987+00:00",
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
    "fetched_at": "2026-10-04T14:36:28.763987+00:00",
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
    "fetched_at": "2026-10-04T14:36:28.763987+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.129s
- Company elapsed time: 0.326s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 27, 'usable_jd': 27}
- Raw jobs found: 192
- After US/location filtering: 99
- With trustworthy posted_date: 99
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
    "fetched_at": "2026-10-04T14:36:29.621631+00:00",
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
    "fetched_at": "2026-10-04T14:36:29.621631+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-10-04T14:36:29.621631+00:00",
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
    "fetched_at": "2026-10-04T14:36:29.621631+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8402813002",
    "title": "Applied Scientist- Pricing, Dynamic Pricing & Offer Selection",
    "location": "San Francisco, CA; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8402813002?gh_jid=8402813002",
    "posted_date": "2026-02-11",
    "updated_date": "2026-09-04",
    "fetched_at": "2026-10-04T14:36:29.621631+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.462s
- Company elapsed time: 0.533s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 3 / 0
- Detail cache statuses: {'reused': 3}
- Relevant JD recovery: {'eligible': 17, 'cache_reused': 3, 'usable_jd': 17}
- Raw jobs found: 82
- After US/location filtering: 67
- With trustworthy posted_date: 67
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
    "fetched_at": "2026-10-04T14:36:29.948579+00:00",
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
    "fetched_at": "2026-10-04T14:36:29.948579+00:00",
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
    "fetched_at": "2026-10-04T14:36:29.948579+00:00",
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
    "fetched_at": "2026-10-04T14:36:29.948579+00:00",
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
    "fetched_at": "2026-10-04T14:36:29.948579+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.123s
- Company elapsed time: 0.328s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 66, 'usable_jd': 66}
- Raw jobs found: 158
- After US/location filtering: 140
- With trustworthy posted_date: 140
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
    "fetched_at": "2026-10-04T14:36:30.483462+00:00",
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
    "fetched_at": "2026-10-04T14:36:30.483462+00:00",
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
    "fetched_at": "2026-10-04T14:36:30.483462+00:00",
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
    "fetched_at": "2026-10-04T14:36:30.483462+00:00",
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
    "fetched_at": "2026-10-04T14:36:30.483462+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.121s
- Company elapsed time: 0.258s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 37, 'usable_jd': 37}
- Raw jobs found: 137
- After US/location filtering: 82
- With trustworthy posted_date: 82
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
    "fetched_at": "2026-10-04T14:36:30.812535+00:00",
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
    "fetched_at": "2026-10-04T14:36:30.812535+00:00",
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
    "fetched_at": "2026-10-04T14:36:30.812535+00:00",
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
    "fetched_at": "2026-10-04T14:36:30.812535+00:00",
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
    "fetched_at": "2026-10-04T14:36:30.812535+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.059s
- Company elapsed time: 0.094s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 30
- After US/location filtering: 28
- With trustworthy posted_date: 28
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
    "fetched_at": "2026-10-04T14:36:31.071979+00:00",
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
    "fetched_at": "2026-10-04T14:36:31.071979+00:00",
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
    "fetched_at": "2026-10-04T14:36:31.071979+00:00",
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
    "fetched_at": "2026-10-04T14:36:31.071979+00:00",
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
    "fetched_at": "2026-10-04T14:36:31.071979+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.101s
- Company elapsed time: 0.265s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 38, 'usable_jd': 38}
- Raw jobs found: 137
- After US/location filtering: 108
- With trustworthy posted_date: 108
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
    "fetched_at": "2026-10-04T14:36:31.166821+00:00",
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
    "fetched_at": "2026-10-04T14:36:31.166821+00:00",
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
    "fetched_at": "2026-10-04T14:36:31.166821+00:00",
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
    "fetched_at": "2026-10-04T14:36:31.166821+00:00",
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
    "fetched_at": "2026-10-04T14:36:31.166821+00:00",
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
- Pages/requests fetched: 54
- HTTP requests/cumulative request time: 298 / 64.382s
- Company elapsed time: 106.924s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 244 / 0 / 0
- Detail cache statuses: {'fetched:new': 227, 'fetched:missing_detail': 16}
- Relevant JD recovery: {'eligible': 97, 'usable_jd': 97}
- Raw jobs found: 1034
- After US/location filtering: 243
- With trustworthy posted_date: 243
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 24.898, "first_pass_survivors": 66, "group": "official", "jds_resolved": 66, "original_postings_resolved": 66, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 66, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 10.862, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.704, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 2.074, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.447, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.436, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.875, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.313, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 37, "stop_reason": "early_stop", "unique_contribution": 23, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 24.689, "first_pass_survivors": 56, "group": "official", "jds_resolved": 56, "original_postings_resolved": 56, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 56, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.632, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "full stack backend", "raw_jobs": 36, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 3.82, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.991, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "cloud engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.996, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "security engineer remote", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.88, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "software engineer collaboration devices", "raw_jobs": 30, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.124, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "splunk engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.183, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer solution test iq platform", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2008454",
    "title": "Photonic Test Engineer",
    "location": "Carlsbad, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Carlsbad-California-US/Photonic-Test-Engineer_2008454",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:36:31.433015+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 12/14/2026 This is an onsite role and will require working out of our Carlsbad, CA office location. Meet the Team The Silicon One te"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2002242",
    "title": "Photonic Packaging Engineer",
    "location": "Carlsbad, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Carlsbad-California-US/Photonic-Packaging-Engineer_2002242",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:36:31.433015+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 12/14/2026 This is an onsite role and will require working out of our Carlsbad, CA office location. Meet the Team The Silicon One te"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2022971",
    "title": "Sr Software Engineer--Routing Platform & Infrastructure",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Sr-Software-Engineer--Routing-Platform---Infrastructure_2022971-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:36:31.433015+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 11/01/2026 ***Candidates must be local to Milpitas as this hybrid role requires being in office there at least 3 days each week*** M"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2027449",
    "title": "Senior AI Researcher, AISWP (Hybrid)",
    "location": "Milpitas, California, US; Seattle, Washington, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Senior-AI-Researcher--AISWP--Hybrid-_2027449-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:36:31.433015+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/29/2026 This is a hybrid role based out of Cisco's Seattle or San Jose office. Meet the Team The Cisco AI Research team is a dyna"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2018241",
    "title": "ASIC DFT Engineer",
    "location": "Austin, Texas, US; San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Austin-Texas-US/ASIC-DFT-Engineer_2018241",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:36:31.433015+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/15/2026 Meet the Team: The Common Hardware Group (CHG) creates innovative hardware platforms central to the AI era, powering Cisc"
  }
]
```

## SAP

- Status: empty
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 10
- HTTP requests/cumulative request time: 10 / 5.201s
- Company elapsed time: 5.390s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.654, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 6, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.439, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.712, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.524, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.463, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.549, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.577, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.501, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.476, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.494, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "cloud developer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}

## HPE

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://hpe.wd5.myworkdayjobs.com/Jobsathpe`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 36
- HTTP requests/cumulative request time: 376 / 158.966s
- Company elapsed time: 209.860s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 339 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 13, 'fetched:new': 326}
- Relevant JD recovery: {'eligible': 119, 'usable_jd': 119}
- Raw jobs found: 669
- After US/location filtering: 339
- With trustworthy posted_date: 339
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 68.179, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 16.182, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 1.494, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 22.032, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.681, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.88, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.085, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.641, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 47.288, "first_pass_survivors": 73, "group": "official", "jds_resolved": 73, "original_postings_resolved": 73, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 73, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.04, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "ai workflow specialist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 5}

Sample normalized records:

```json
[
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1207650",
    "title": "AI Engineer - Developer Productivity",
    "location": "Spring, Texas, United States of America; Ft. Collins, Colorado, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Spring-Texas-United-States-of-America/AI-Engineer---Developer-Productivity_1207650-2",
    "posted_date": "2026-09-29",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:37:30.287712+00:00",
    "date_confidence": "high",
    "description": "AI Engineer - Developer Productivity This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enter"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1209445",
    "title": "Senior AI Engineer Developer",
    "location": "Spring, Texas, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Spring-Texas-United-States-of-America/Senior-AI-Engineer-Developer_1209445-2",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:37:30.287712+00:00",
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
    "fetched_at": "2026-10-04T14:37:30.287712+00:00",
    "date_confidence": "high",
    "description": "AI/ML Engineer - Agentic This role has been designed as ‘Hybrid’ with an expectation that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Packard E"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1206826",
    "title": "HPC & AI Performance Engineer",
    "location": "Bloomington, Minnesota, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Bloomington-Minnesota-United-States-of-America/HPC---AI-Performance-Engineer_1206826-3",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:37:30.287712+00:00",
    "date_confidence": "high",
    "description": "HPC & AI Performance Engineer This role has been designed as 'Hybrid' with a requirement that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Packa"
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
    "fetched_at": "2026-10-04T14:37:30.287712+00:00",
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
- HTTP requests/cumulative request time: 27 / 14.527s
- Company elapsed time: 20.746s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 19 / 102
- Detail cache statuses: {'reused': 19}
- Relevant JD recovery: {'deterministic_skip': 100, 'cache_reused': 19, 'eligible': 19, 'ai_skip': 2, 'usable_jd': 19}
- Raw jobs found: 270
- After US/location filtering: 121
- With trustworthy posted_date: 2
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.965, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.852, "first_pass_survivors": 12, "group": "official", "jds_resolved": 0, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.972, "first_pass_survivors": 17, "group": "official", "jds_resolved": 0, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.813, "first_pass_survivors": 22, "group": "official", "jds_resolved": 0, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.289, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.851, "first_pass_survivors": 12, "group": "official", "jds_resolved": 0, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 1.764, "first_pass_survivors": 9, "group": "official", "jds_resolved": 0, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.036, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.202, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10161130",
    "title": "Director, AI Enablement & Legal Engineering",
    "location": "Burbank, California / New York, New York",
    "official_url": "https://www.disneycareers.com/en/job/burbank/director-ai-enablement-and-legal-engineering/391/101107920944",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:37:35.606618+00:00",
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
    "fetched_at": "2026-10-04T14:37:35.606618+00:00",
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
    "fetched_at": "2026-10-04T14:37:35.606618+00:00",
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
    "fetched_at": "2026-10-04T14:37:35.606618+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10143797",
    "title": "Sr Data Engineer",
    "location": "Seattle, Washington / Glendale, California",
    "official_url": "https://www.disneycareers.com/en/job/seattle/sr-data-engineer/391/95106486176",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:37:35.606618+00:00",
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
- HTTP requests/cumulative request time: 70 / 33.576s
- Company elapsed time: 42.846s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 51 / 0 / 0
- Detail cache statuses: {'fetched:new': 51}
- Relevant JD recovery: {'eligible': 12, 'usable_jd': 12}
- Raw jobs found: 239
- After US/location filtering: 51
- With trustworthy posted_date: 51
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.158, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 6, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "early_stop", "unique_contribution": 48, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.672, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.648, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.147, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 2.719, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 2.848, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 2.48, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 0.662, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.671, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 19}

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
    "fetched_at": "2026-10-04T14:37:56.353361+00:00",
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
    "fetched_at": "2026-10-04T14:37:56.353361+00:00",
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
    "fetched_at": "2026-10-04T14:37:56.353361+00:00",
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
    "fetched_at": "2026-10-04T14:37:56.353361+00:00",
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
    "fetched_at": "2026-10-04T14:37:56.353361+00:00",
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
- HTTP requests/cumulative request time: 162 / 30.900s
- Company elapsed time: 54.102s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 134 / 0 / 0
- Detail cache statuses: {'fetched:new': 122, 'fetched:missing_detail': 12}
- Relevant JD recovery: {'eligible': 53, 'usable_jd': 53}
- Raw jobs found: 261
- After US/location filtering: 134
- With trustworthy posted_date: 134
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.641, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.625, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.971, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 8.04, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.458, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.951, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.319, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.397, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.385, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3093801",
    "title": "Power Delivery and Voltage Regulator Validation Engineer – Datacenter",
    "location": "Santa Clara, California, United States of America; Austin, Texas, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446719655199",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:18.357971+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Systems Engineering General Summary: Our Mission We are dedicated to transforming the industry"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095054",
    "title": "CPU Performance Modeling Engineer (Multiple Levels)",
    "location": "Santa Clara, California, United States of America; Austin, Texas, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720361953",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:18.357971+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > CPU Architecture General Summary: As a leading technology innovator, Qualcomm pushes the bound"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095249",
    "title": "CPU STA CAD Engineer",
    "location": "Santa Clara, California, United States of America; Austin, Texas, United States of America; San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720476815",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:18.357971+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > CPU Engineering General Summary: NUVIA is now part of Qualcomm. Our mission is to reimagine si"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3097076",
    "title": "Data Center Engineering - Post Silicon Power and Performance Engineer",
    "location": "Austin, Texas, United States of America; Santa Clara, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721293506",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:18.357971+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Systems Engineering General Summary: Job Description As a Data Center Post Silicon Power and P"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3097256",
    "title": "System Validation Lead, Staff (AI Accelerator Platform)",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721330866",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:18.357971+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > ASICS Engineering General Summary: Qualcomm’s System Validation & Emulation (SVE) team is part"
  }
]
```

## AMD

- Status: ok
- Scraping method: HTTP GET public Jibe/iCIMS jobs JSON
- Search URL/API: `https://careers.amd.com/api/jobs`
- Pagination: page=1,2,... per role query; stop on total/empty/repeat/short page
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 14 / 8.501s
- Company elapsed time: 10.099s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 207, 'usable_jd': 207}
- Raw jobs found: 1267
- After US/location filtering: 492
- With trustworthy posted_date: 492
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.421, "first_pass_survivors": 335, "group": "official", "jds_resolved": 335, "original_postings_resolved": 0, "page_budget": 6, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 335, "stop_reason": "early_stop", "unique_contribution": 335, "unique_jobs": 335}
- Query diagnostic: {"elapsed_seconds": 0.681, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning", "raw_jobs": 100, "stop_reason": "early_stop", "unique_contribution": 31, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.161, "first_pass_survivors": 73, "group": "official", "jds_resolved": 73, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 73, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 1.778, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "AI research", "raw_jobs": 232, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 232}
- Query diagnostic: {"elapsed_seconds": 2.057, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 300}

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
    "fetched_at": "2026-10-04T14:38:39.200211+00:00",
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
    "fetched_at": "2026-10-04T14:38:39.200211+00:00",
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
    "fetched_at": "2026-10-04T14:38:39.200211+00:00",
    "date_confidence": "high",
    "description": "WHAT YOU DO AT AMD CHANGES EVERYTHING At AMD, our mission is to build great products that accelerate next-generation computing experiences—from AI and data centers, to PCs, gaming "
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "88685",
    "title": "AI Networking System/Solution Test Engineer",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-08-04",
    "updated_date": "2026-10-03",
    "fetched_at": "2026-10-04T14:38:39.200211+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology can change lives for the better. It can heal us, entertain us, and make us more connected, productive, and und"
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
    "fetched_at": "2026-10-04T14:38:39.200211+00:00",
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
- HTTP requests/cumulative request time: 65 / 18.895s
- Company elapsed time: 27.441s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 45 / 0 / 0
- Detail cache statuses: {'fetched:new': 44, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 22, 'usable_jd': 22}
- Raw jobs found: 185
- After US/location filtering: 45
- With trustworthy posted_date: 45
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.589, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 6, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 29, "stop_reason": "early_stop", "unique_contribution": 29, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 0.432, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.666, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 5.517, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 3.946, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 1.941, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 0.437, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.414, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.969, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 24, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 24}

Sample normalized records:

```json
[
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19721",
    "title": "CX Vertical Industry Lead - Financial Services",
    "location": "Remote (US)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--US/Contact-Center-Vertical-Industry-Lead---Financial-Services_R19721",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:49.300370+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect This role sits at the intersection of Financial Services expertise and go-to-market strategy, giving you the opportunity to define how Zoom's Customer Experienc"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19452",
    "title": "Manager of Platform DevOps",
    "location": "San Jose (CA); Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Manager-of-Platform-DevOps_R19452-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:49.300370+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect You will be the leader of our Platforms DevOps team. This team is responsible for Zoom’s Kubernetes clusters in both datacenters and clouds, as well as for our "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R18761",
    "title": "Staff AI Engineer",
    "location": "Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Seattle-WA/Staff-AI-Engineer_R18761-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:49.300370+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect You'll design, implement, and own the inference systems that serve Zoom's AI models at production scale -- across real-time communication, vision, and language "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19149",
    "title": "Senior Data Scientist",
    "location": "San Jose (CA); Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Senior-Data-Scientist_R19149-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:49.300370+00:00",
    "date_confidence": "high",
    "description": "Immigration sponsorship is not available for this position . What you can expect​ You will build production machine-learning systems that predict customer growth and retention sign"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19391",
    "title": "Head of Search & AI Visibility",
    "location": "Remote (US)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--US/Head-of-Search---AI-Visibility_R19391-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:38:49.300370+00:00",
    "date_confidence": "high",
    "description": "What you can expect You will own Zoom's end-to-end search strategy across traditional SEO and AI-powered answer engines. You will build unified infrastructure, metrics, and content"
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
- HTTP requests/cumulative request time: 1 / 0.295s
- Company elapsed time: 0.826s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 61, 'usable_jd': 61}
- Raw jobs found: 360
- After US/location filtering: 217
- With trustworthy posted_date: 217
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
    "fetched_at": "2026-10-04T14:39:12.460808+00:00",
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
    "fetched_at": "2026-10-04T14:39:12.460808+00:00",
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
    "fetched_at": "2026-10-04T14:39:12.460808+00:00",
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
    "fetched_at": "2026-10-04T14:39:12.460808+00:00",
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
    "fetched_at": "2026-10-04T14:39:12.460808+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.336s
- Company elapsed time: 1.617s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 68, 'usable_jd': 68}
- Raw jobs found: 887
- After US/location filtering: 498
- With trustworthy posted_date: 498
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
    "fetched_at": "2026-10-04T14:39:13.288272+00:00",
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
    "fetched_at": "2026-10-04T14:39:13.288272+00:00",
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
    "fetched_at": "2026-10-04T14:39:13.288272+00:00",
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
    "fetched_at": "2026-10-04T14:39:13.288272+00:00",
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
    "fetched_at": "2026-10-04T14:39:13.288272+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.173s
- Company elapsed time: 0.665s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 29, 'usable_jd': 29}
- Raw jobs found: 253
- After US/location filtering: 236
- With trustworthy posted_date: 236
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:39:14.905900+00:00",
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:39:14.905900+00:00",
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:39:14.905900+00:00",
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:39:14.905900+00:00",
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:39:14.905900+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.126s
- Company elapsed time: 0.414s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 154
- After US/location filtering: 94
- With trustworthy posted_date: 94
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
    "fetched_at": "2026-10-04T14:39:15.571908+00:00",
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
    "fetched_at": "2026-10-04T14:39:15.571908+00:00",
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
    "fetched_at": "2026-10-04T14:39:15.571908+00:00",
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
    "fetched_at": "2026-10-04T14:39:15.571908+00:00",
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
    "fetched_at": "2026-10-04T14:39:15.571908+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.565s
- Company elapsed time: 2.227s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 148, 'usable_jd': 148}
- Raw jobs found: 639
- After US/location filtering: 511
- With trustworthy posted_date: 511
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
    "fetched_at": "2026-10-04T14:39:15.987518+00:00",
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
    "fetched_at": "2026-10-04T14:39:15.987518+00:00",
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
    "fetched_at": "2026-10-04T14:39:15.987518+00:00",
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
    "fetched_at": "2026-10-04T14:39:15.987518+00:00",
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
    "fetched_at": "2026-10-04T14:39:15.987518+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.698s
- Company elapsed time: 0.883s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 43
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
    "fetched_at": "2026-10-04T14:39:16.747355+00:00",
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
    "fetched_at": "2026-10-04T14:39:16.747355+00:00",
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
    "fetched_at": "2026-10-04T14:39:16.747355+00:00",
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
    "fetched_at": "2026-10-04T14:39:16.747355+00:00",
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
    "fetched_at": "2026-10-04T14:39:16.747355+00:00",
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
- HTTP requests/cumulative request time: 24 / 28.336s
- Company elapsed time: 31.760s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 229, 'usable_jd': 229}
- Raw jobs found: 1065
- After US/location filtering: 445
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.123, "first_pass_survivors": 146, "group": "official", "jds_resolved": 146, "original_postings_resolved": 146, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 146, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.771, "first_pass_survivors": 100, "group": "official", "jds_resolved": 100, "original_postings_resolved": 100, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 100, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 4.911, "first_pass_survivors": 56, "group": "official", "jds_resolved": 56, "original_postings_resolved": 56, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 105, "stop_reason": "page_budget", "unique_contribution": 56, "unique_jobs": 105}
- Query diagnostic: {"elapsed_seconds": 3.788, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 147}
- Query diagnostic: {"elapsed_seconds": 3.172, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 4.347, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.556, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 57, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 0.863, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 3.229, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 150}

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
    "fetched_at": "2026-10-04T14:39:17.636787+00:00",
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
    "fetched_at": "2026-10-04T14:39:17.636787+00:00",
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
    "fetched_at": "2026-10-04T14:39:17.636787+00:00",
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
    "fetched_at": "2026-10-04T14:39:17.636787+00:00",
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
    "fetched_at": "2026-10-04T14:39:17.636787+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.142s
- Company elapsed time: 0.358s
- Incremental mode/page cap: full_sweep / 12
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
    "fetched_at": "2026-10-04T14:39:18.217984+00:00",
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
    "fetched_at": "2026-10-04T14:39:18.217984+00:00",
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
    "fetched_at": "2026-10-04T14:39:18.217984+00:00",
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
    "fetched_at": "2026-10-04T14:39:18.217984+00:00",
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
    "fetched_at": "2026-10-04T14:39:18.217984+00:00",
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
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 113 / 28.219s
- Company elapsed time: 44.679s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 89 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 87}
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 468
- After US/location filtering: 89
- With trustworthy posted_date: 89
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 12.432, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.016, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.77, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 6.282, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.799, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.297, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.056, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.315, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 40, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 2.711, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

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
    "fetched_at": "2026-10-04T14:39:18.576644+00:00",
    "date_confidence": "high",
    "description": "AI Solution Engineer, Security The Dell Security & Resiliency organization manages the security risk across all aspects of Dell’s business. We are currently experiencing incredible"
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
    "fetched_at": "2026-10-04T14:39:18.576644+00:00",
    "date_confidence": "high",
    "description": "Technical Support Engineer 2 – Dell & Nvidia AI Networking At Dell Technologies, world-class service doesn’t end when a customer purchases our innovative products. Our Technical Su"
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
    "fetched_at": "2026-10-04T14:39:18.576644+00:00",
    "date_confidence": "high",
    "description": "Senior ServiceNow Developer (ServiceNow Technical Architect) Be a part of a team that’s ensuring Dell Technologies' product integrity and customer satisfaction. Our IT Software Eng"
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
    "fetched_at": "2026-10-04T14:39:18.576644+00:00",
    "date_confidence": "high",
    "description": "SUMMARY Agentic Context Engineering Architect & AI Practitioner Join us to do the best work of your career and make a profound social impact as an Agentic Context Engineering Archi"
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
    "fetched_at": "2026-10-04T14:39:18.576644+00:00",
    "date_confidence": "high",
    "description": "Principal Engineer - Enterprise DevOps & ALM Platforms Software Engineering delivers innovative platforms, tools, and services that enable teams across Dell Technologies to acceler"
  }
]
```

## Dropbox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/dropbox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.103s
- Company elapsed time: 0.196s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 39
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
    "fetched_at": "2026-10-04T14:39:44.517979+00:00",
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
    "fetched_at": "2026-10-04T14:39:44.517979+00:00",
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
    "fetched_at": "2026-10-04T14:39:44.517979+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qowz80zsz81z8nqz122zdfz68z5coz87zsz73zz76zipqu3z86zmz88zz81zcth"
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
    "fetched_at": "2026-10-04T14:39:44.517979+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p>Dropbox is hiring a Customer Evidence Manager to<span class=\"thread-482953488634939485839339\"> own</span> <span clas"
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
    "fetched_at": "2026-10-04T14:39:44.517979+00:00",
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
- HTTP requests/cumulative request time: 69 / 22.138s
- Company elapsed time: 32.345s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 48 / 0 / 0
- Detail cache statuses: {'fetched:new': 48}
- Relevant JD recovery: {'eligible': 17, 'usable_jd': 17}
- Raw jobs found: 380
- After US/location filtering: 48
- With trustworthy posted_date: 48
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.571, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.609, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 0.791, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 3.961, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.666, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.935, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.864, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.256, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.692, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109666",
    "title": "Software Development Engineer III, Media Solutions",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Software-Development-Engineer-III--Media-Solutions_R-109666-2",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:39:44.715068+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-107932",
    "title": "Software Development Engineer II - Payments",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Software-Development-Engineer-II_R-107932-1",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:39:44.715068+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-104546",
    "title": "Software Development Engineer III, Advertising Technology",
    "location": "USA - Illinois - Chicago; Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---Illinois---Chicago/Software-Development-Engineer-III--Advertising-Technology_R-104546",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:39:44.715068+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109663",
    "title": "Sr Director Engineering - Experience Platform",
    "location": "Washington - Seattle Campus; USA - Illinois - Chicago",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Sr-Director-Engineering---Experience-Platform_R-109663-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:39:44.715068+00:00",
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
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:39:44.715068+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.144s
- Company elapsed time: 0.246s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 1, 'usable_jd': 1}
- Raw jobs found: 132
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
    "fetched_at": "2026-10-04T14:39:49.397904+00:00",
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
    "fetched_at": "2026-10-04T14:39:49.397904+00:00",
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
    "fetched_at": "2026-10-04T14:39:49.397904+00:00",
    "date_confidence": "high",
    "description": "<p><strong>***Now accepting applications for a November 3rd, 2026 start date***</strong></p> <p>As an Account Executive on the Small Business sales team, you will identify, source,"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8044961",
    "title": "Associate, Corporate Development",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8044961?gh_jid=8044961",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:39:49.397904+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-24470</strong></p> <hr> <h2>About The Team</h2> <p>HubSpot’s mission is to help millions of organizations grow better.</p> <p>At HubSpot, strategy isn’t just a plan "
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
    "fetched_at": "2026-10-04T14:39:49.397904+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-33330</strong></p> <hr> <p><strong>Manager, Analytics Engineering, Data &amp; AI Foundations</strong></p> <p>HubSpot's mission is to Help Millions of Organizations G"
  }
]
```

## Instacart

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/instacart/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.109s
- Company elapsed time: 0.402s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 8, 'usable_jd': 8}
- Raw jobs found: 131
- After US/location filtering: 115
- With trustworthy posted_date: 115
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
    "updated_date": "2026-10-02",
    "fetched_at": "2026-10-04T14:39:49.645003+00:00",
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
    "fetched_at": "2026-10-04T14:39:49.645003+00:00",
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
    "fetched_at": "2026-10-04T14:39:49.645003+00:00",
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
    "fetched_at": "2026-10-04T14:39:49.645003+00:00",
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
    "fetched_at": "2026-10-04T14:39:49.645003+00:00",
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
- Pages/requests fetched: 37
- HTTP requests/cumulative request time: 223 / 94.495s
- Company elapsed time: 126.100s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 185 / 0 / 0
- Detail cache statuses: {'fetched:new': 182, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 106, 'usable_jd': 106}
- Raw jobs found: 687
- After US/location filtering: 185
- With trustworthy posted_date: 185
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 42.715, "first_pass_survivors": 73, "group": "official", "jds_resolved": 73, "original_postings_resolved": 73, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 73, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 8.586, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 5.151, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 10.301, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 13.234, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 9.239, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.443, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 1.299, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 29.239, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 234}

Sample normalized records:

```json
[
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0287544",
    "title": "AI Software Technical Intern",
    "location": "US, California, Santa Clara",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-California-Santa-Clara/AI-Software-Technical-Intern_JR0287544",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:39:50.047988+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Role Overview We are seeking a driven and curious Technical Intern to join our AI Software and Hardware Architecture team. In this role, you will work"
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
    "fetched_at": "2026-10-04T14:39:50.047988+00:00",
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
    "fetched_at": "2026-10-04T14:39:50.047988+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel's Neuromorphic Computing Lab has been at the forefront of brain-inspired computing for nearly a decade, working alongside a global ecosystem of "
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0286946",
    "title": "AI/ML Software App Development Intern",
    "location": "PRC, Chengdu",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/PRC-Chengdu/AI-ML-Software-App-Development-Intern_JR0286946",
    "posted_date": "2026-09-07",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:39:50.047988+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel Foundry Automation - Data Analytics and Process Group is seeking a motivated and technically curious intern to join our Manufacturing Automation"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0287335",
    "title": "AI Software Development Engineer - Neuromorphic Computing",
    "location": "US, California, Santa Clara",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-California-Santa-Clara/AI-Software-Development-Engineer---Neuromorphic-Computing_JR0287335",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:39:50.047988+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: What if you could help define how developers program an entirely new class of AI hardware? For nearly a decade, Intel's Neuromorphic Computing Lab, to"
  }
]
```

## MathWorks

- Status: ok
- Scraping method: HTTP GET server-rendered MathWorks search + JobPosting JSON-LD
- Search URL/API: `https://www.mathworks.com/company/jobs/opportunities/search/`
- Pagination: page=2,3,... after the unnumbered first page; stop on empty/repeat/short page
- Pages/requests fetched: 10
- HTTP requests/cumulative request time: 44 / 15.747s
- Company elapsed time: 16.821s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 34 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 88
- After US/location filtering: 34
- With trustworthy posted_date: 34
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.469, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.747, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 1.318, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 2.546, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.605, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 1.465, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.507, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.7, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.462, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 22}

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
    "fetched_at": "2026-10-04T14:40:03.256880+00:00",
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
    "fetched_at": "2026-10-04T14:40:03.256880+00:00",
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
    "fetched_at": "2026-10-04T14:40:03.256880+00:00",
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
    "fetched_at": "2026-10-04T14:40:03.256880+00:00",
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
    "fetched_at": "2026-10-04T14:40:03.256880+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.276s
- Company elapsed time: 0.853s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 51, 'usable_jd': 51}
- Raw jobs found: 390
- After US/location filtering: 248
- With trustworthy posted_date: 248
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
    "updated_date": "2026-09-24",
    "fetched_at": "2026-10-04T14:40:17.061087+00:00",
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
    "updated_date": "2026-09-24",
    "fetched_at": "2026-10-04T14:40:17.061087+00:00",
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
    "updated_date": "2026-09-24",
    "fetched_at": "2026-10-04T14:40:17.061087+00:00",
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
    "updated_date": "2026-09-24",
    "fetched_at": "2026-10-04T14:40:17.061087+00:00",
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
    "updated_date": "2026-09-24",
    "fetched_at": "2026-10-04T14:40:17.061087+00:00",
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
- HTTP requests/cumulative request time: 143 / 26.588s
- Company elapsed time: 46.391s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 118 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 4, 'fetched:new': 114}
- Relevant JD recovery: {'eligible': 35, 'usable_jd': 35}
- Raw jobs found: 232
- After US/location filtering: 118
- With trustworthy posted_date: 118
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.058, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.828, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.835, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 6.037, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.15, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.416, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.473, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.251, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.947, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "JR042832",
    "title": "Associate, Software Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800007925",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:40:17.915463+00:00",
    "date_confidence": "high",
    "description": "Company Profile: Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment, and wealth management services. Th"
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
    "fetched_at": "2026-10-04T14:40:17.915463+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
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
    "fetched_at": "2026-10-04T14:40:17.915463+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR045015",
    "title": "NNA and Transaction Flow Insights Analyst, Vice President",
    "location": "Purchase, New York, United States of America; New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800542949",
    "posted_date": "2026-09-30",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:40:17.915463+00:00",
    "date_confidence": "high",
    "description": "Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment management and wealth management services. The Firm'"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR044035",
    "title": "Agentic AI Developer, Cybersecurity",
    "location": "Baltimore, Maryland, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800350224",
    "posted_date": "2026-09-29",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:40:17.915463+00:00",
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
- Pages/requests fetched: 31
- HTTP requests/cumulative request time: 118 / 33.528s
- Company elapsed time: 51.190s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 87 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 465
- After US/location filtering: 87
- With trustworthy posted_date: 87
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 20.352, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 5, "pages_fetched": 5, "query": "ai engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 4.257, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.947, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 5.196, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 1.981, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.781, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.445, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.624, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.606, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 5, "pages_fetched": 5, "query": "software engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 75}

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
    "fetched_at": "2026-10-04T14:40:20.078898+00:00",
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
    "fetched_at": "2026-10-04T14:40:20.078898+00:00",
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
    "fetched_at": "2026-10-04T14:40:20.078898+00:00",
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
    "fetched_at": "2026-10-04T14:40:20.078898+00:00",
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
    "fetched_at": "2026-10-04T14:40:20.078898+00:00",
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
- HTTP requests/cumulative request time: 9 / 2.632s
- Company elapsed time: 3.616s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 51 / 6
- Detail cache statuses: {'reused': 51}
- Relevant JD recovery: {'cache_reused': 51, 'eligible': 51, 'deterministic_skip': 2, 'ai_skip': 4, 'usable_jd': 51}
- Raw jobs found: 90
- After US/location filtering: 57
- With trustworthy posted_date: 57
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.539, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.35, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.378, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.507, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.379, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.39, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.34, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.324, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.41, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}

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
    "updated_date": "2026-05-19",
    "fetched_at": "2026-10-04T14:40:47.781748+00:00",
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
    "fetched_at": "2026-10-04T14:40:47.781748+00:00",
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
    "fetched_at": "2026-10-04T14:40:47.781748+00:00",
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
    "fetched_at": "2026-10-04T14:40:47.781748+00:00",
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
    "fetched_at": "2026-10-04T14:40:47.781748+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.403s
- Company elapsed time: 1.453s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 362, 'usable_jd': 362}
- Raw jobs found: 828
- After US/location filtering: 676
- With trustworthy posted_date: 676
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
    "fetched_at": "2026-10-04T14:40:51.398645+00:00",
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
    "fetched_at": "2026-10-04T14:40:51.398645+00:00",
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
    "fetched_at": "2026-10-04T14:40:51.398645+00:00",
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
    "fetched_at": "2026-10-04T14:40:51.398645+00:00",
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
    "fetched_at": "2026-10-04T14:40:51.398645+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.395s
- Company elapsed time: 0.609s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 2 / 0
- Detail cache statuses: {'reused': 2}
- Relevant JD recovery: {'eligible': 189, 'cache_reused': 2, 'usable_jd': 189}
- Raw jobs found: 319
- After US/location filtering: 246
- With trustworthy posted_date: 246
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
    "fetched_at": "2026-10-04T14:40:52.852931+00:00",
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
    "fetched_at": "2026-10-04T14:40:52.852931+00:00",
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
    "fetched_at": "2026-10-04T14:40:52.852931+00:00",
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
    "fetched_at": "2026-10-04T14:40:52.852931+00:00",
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
    "fetched_at": "2026-10-04T14:40:52.852931+00:00",
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
- HTTP requests/cumulative request time: 67 / 15.634s
- Company elapsed time: 24.532s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 47 / 0 / 0
- Detail cache statuses: {'fetched:new': 47}
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 157
- After US/location filtering: 47
- With trustworthy posted_date: 47
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.487, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 1.156, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 1.247, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.113, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 3.549, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.639, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 0.631, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.144, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.256, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137563",
    "title": "Staff Product Security AI Engineer",
    "location": "Austin, Texas, United States of America; Scottsdale, Arizona, United States of America; Chicago, Illinois, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922353695",
    "posted_date": "2026-10-01",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:40:53.463143+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138171",
    "title": "Director, Debit & Money Management Engineering",
    "location": "San Jose, California, United States of America; Scottsdale, Arizona, United States of America; Chicago, Illinois, United States of America; Austin, Texas, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922536607",
    "posted_date": "2026-09-28",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:40:53.463143+00:00",
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
    "fetched_at": "2026-10-04T14:40:53.463143+00:00",
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
    "fetched_at": "2026-10-04T14:40:53.463143+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137734",
    "title": "Senior Database Engineer",
    "location": "San Jose, California, United States of America; Austin, Texas, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922547415",
    "posted_date": "2026-09-24",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:40:53.463143+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.120s
- Company elapsed time: 0.478s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 16, 'usable_jd': 16}
- Raw jobs found: 152
- After US/location filtering: 134
- With trustworthy posted_date: 134
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:41:00.148379+00:00",
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
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-04T14:41:00.148379+00:00",
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
    "updated_date": "2026-10-01",
    "fetched_at": "2026-10-04T14:41:00.148379+00:00",
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:41:00.148379+00:00",
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:41:00.148379+00:00",
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
- HTTP requests/cumulative request time: 53 / 17.673s
- Company elapsed time: 23.501s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 39 / 0 / 0
- Detail cache statuses: {'fetched:new': 38, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 20, 'usable_jd': 20}
- Raw jobs found: 99
- After US/location filtering: 39
- With trustworthy posted_date: 39
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.885, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 6, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.372, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.697, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 11.651, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 0.67, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.502, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.38, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.376, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.475, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 12, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 21}

Sample normalized records:

```json
[
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059523",
    "title": "Senior AI Platform Specialist Solution Architect",
    "location": "Remote US CA; Remote US WA; Remote US OR",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Remote-US-CA/Senior-AI-Platform-Specialist-Solution-Architect_R-059523-1",
    "posted_date": "2026-10-04",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:00.627213+00:00",
    "date_confidence": "high",
    "description": "About the role: ​ The Red Hat North America Technology Sales team is looking for an AI Platform Specialist Solution Architect (SSA) to join our team. This position assumes a crucia"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059026",
    "title": "Global Specialist Solution Architect - Lightwell",
    "location": "Boston; Remote US VA; Remote US SC; Remote US NC; Remote US TX; Remote US FL; Remote US CA; Remote US GA",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Boston/Global-Specialist-Solution-Architect---Lightwell_R-059026-2",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:00.627213+00:00",
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
    "fetched_at": "2026-10-04T14:41:00.627213+00:00",
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
    "fetched_at": "2026-10-04T14:41:00.627213+00:00",
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
    "fetched_at": "2026-10-04T14:41:00.627213+00:00",
    "date_confidence": "high",
    "description": "About the role: The Red Hat Technology Sales team is looking for a Lightwell Specialist Solution Architect (SSA) with Telco experience to join our team. This position assumes a cru"
  }
]
```

## Roku

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roku/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.184s
- Company elapsed time: 0.826s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 26, 'usable_jd': 26}
- Raw jobs found: 233
- After US/location filtering: 191
- With trustworthy posted_date: 191
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:41:04.307113+00:00",
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:41:04.307113+00:00",
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
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-04T14:41:04.307113+00:00",
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
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-04T14:41:04.307113+00:00",
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
    "updated_date": "2026-10-04",
    "fetched_at": "2026-10-04T14:41:04.307113+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.198s
- Company elapsed time: 0.844s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 24, 'usable_jd': 24}
- Raw jobs found: 227
- After US/location filtering: 211
- With trustworthy posted_date: 211
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
    "updated_date": "2026-09-22",
    "fetched_at": "2026-10-04T14:41:05.134850+00:00",
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
    "updated_date": "2026-09-22",
    "fetched_at": "2026-10-04T14:41:05.134850+00:00",
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
    "updated_date": "2026-09-22",
    "fetched_at": "2026-10-04T14:41:05.134850+00:00",
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
    "updated_date": "2026-09-30",
    "fetched_at": "2026-10-04T14:41:05.134850+00:00",
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
    "fetched_at": "2026-10-04T14:41:05.134850+00:00",
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
- HTTP requests/cumulative request time: 75 / 87.986s
- Company elapsed time: 94.675s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 58 / 12 / 10
- Detail cache statuses: {'fetched:new': 28, 'reused': 12}
- Relevant JD recovery: {'deterministic_skip': 5, 'eligible': 30, 'ai_recover': 7, 'ai_skip': 5, 'detail_requests': 30, 'detail_failure': 30, 'budget_deferred': 0, 'usable_jd': 0}
- Raw jobs found: 108
- After US/location filtering: 40
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 14.402, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 6.873, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 2.279, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 5.12, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 18.231, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.399, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 1.114, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.781, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 6.474, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 31, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 31}

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
    "fetched_at": "2026-10-04T14:41:05.984032+00:00",
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
    "fetched_at": "2026-10-04T14:41:05.984032+00:00",
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
    "fetched_at": "2026-10-04T14:41:05.984032+00:00",
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
    "fetched_at": "2026-10-04T14:41:05.984032+00:00",
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
    "fetched_at": "2026-10-04T14:41:05.984032+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.200s
- Company elapsed time: 0.696s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 307
- After US/location filtering: 247
- With trustworthy posted_date: 247
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
    "fetched_at": "2026-10-04T14:41:11.269730+00:00",
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
    "fetched_at": "2026-10-04T14:41:11.269730+00:00",
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
    "fetched_at": "2026-10-04T14:41:11.269730+00:00",
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
    "fetched_at": "2026-10-04T14:41:11.269730+00:00",
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
    "fetched_at": "2026-10-04T14:41:11.269730+00:00",
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
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 127 / 44.868s
- Company elapsed time: 61.845s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 107 / 0 / 0
- Detail cache statuses: {'fetched:new': 106, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 18, 'usable_jd': 18}
- Raw jobs found: 354
- After US/location filtering: 107
- With trustworthy posted_date: 107
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 28.416, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.227, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.841, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 13.75, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.285, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.168, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.263, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.523, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 2.704, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088746W",
    "title": "Senior Data Scientist, AI Solutions Engineering - Client Services",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Senior-Data-Scientist--AI-Solutions-Engineering---Client-Services_REF088746W",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:11.966709+00:00",
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
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:11.966709+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088588W",
    "title": "SW Engineer",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/SW-Engineer_REF088588W",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:11.966709+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088545W",
    "title": "Sr. ML Engineer",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Sr-ML-Engineer_REF088545W",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:11.966709+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF085174W",
    "title": "Sr. SW AI Engineer",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Sr-SW-AI-Engineer_REF085174W-2",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:11.966709+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.243s
- Company elapsed time: 0.253s
- Incremental mode/page cap: full_sweep / 12
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
    "fetched_at": "2026-10-04T14:41:17.996445+00:00",
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
    "fetched_at": "2026-10-04T14:41:17.996445+00:00",
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
    "fetched_at": "2026-10-04T14:41:17.996445+00:00",
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
    "fetched_at": "2026-10-04T14:41:17.996445+00:00",
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
    "fetched_at": "2026-10-04T14:41:17.996445+00:00",
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
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 151 / 88.418s
- Company elapsed time: 109.496s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 123 / 0 / 0
- Detail cache statuses: {'fetched:new': 123}
- Relevant JD recovery: {'eligible': 23, 'usable_jd': 23}
- Raw jobs found: 472
- After US/location filtering: 123
- With trustworthy posted_date: 123
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 54.953, "first_pass_survivors": 106, "group": "official", "jds_resolved": 106, "original_postings_resolved": 106, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 108, "stop_reason": "page_budget", "unique_contribution": 106, "unique_jobs": 108}
- Query diagnostic: {"elapsed_seconds": 1.882, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 1.793, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 13.843, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.088, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.07, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.434, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.196, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 14.081, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 6, "query": "software engineer", "raw_jobs": 87, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 87}

Sample normalized records:

```json
[
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0109765",
    "title": "Principal Software Engineer, Agentic UX",
    "location": "USA, CA, Pleasanton",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CA-Pleasanton/Principal-AI-UX-Lead_JR-0109765-1",
    "posted_date": "2026-09-30",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:18.250068+00:00",
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
    "fetched_at": "2026-10-04T14:41:18.250068+00:00",
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
    "fetched_at": "2026-10-04T14:41:18.250068+00:00",
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
    "fetched_at": "2026-10-04T14:41:18.250068+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  },
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0109923",
    "title": "Senior Director, Context and Semantics Engineering (AI)",
    "location": "USA, CA, Pleasanton",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CA-Pleasanton/Senior-Director--Context-and-Semantics-Engineering--AI-_JR-0109923",
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:18.250068+00:00",
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
- HTTP requests/cumulative request time: 51 / 20.895s
- Company elapsed time: 26.726s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 35 / 0 / 0
- Detail cache statuses: {'fetched:new': 35}
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 157
- After US/location filtering: 35
- With trustworthy posted_date: 35
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 14.923, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 0.687, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.68, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 1.174, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 3.668, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 33, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 2.78, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 0.659, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.726, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.648, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 17}

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
    "fetched_at": "2026-10-04T14:41:24.128835+00:00",
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
    "fetched_at": "2026-10-04T14:41:24.128835+00:00",
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
    "fetched_at": "2026-10-04T14:41:24.128835+00:00",
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
    "fetched_at": "2026-10-04T14:41:24.128835+00:00",
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
    "fetched_at": "2026-10-04T14:41:24.128835+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.222s
- Company elapsed time: 0.821s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 22, 'usable_jd': 22}
- Raw jobs found: 364
- After US/location filtering: 218
- With trustworthy posted_date: 218
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
    "fetched_at": "2026-10-04T14:41:50.855764+00:00",
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
    "fetched_at": "2026-10-04T14:41:50.855764+00:00",
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
    "fetched_at": "2026-10-04T14:41:50.855764+00:00",
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
    "fetched_at": "2026-10-04T14:41:50.855764+00:00",
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
    "fetched_at": "2026-10-04T14:41:50.855764+00:00",
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
- HTTP requests/cumulative request time: 11 / 4.881s
- Company elapsed time: 5.005s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: {'fetched:new': 1}
- Relevant JD recovery: {'eligible': 1, 'usable_jd': 1}
- Raw jobs found: 4
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.914, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 6, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.556, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.421, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.421, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.423, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.443, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.362, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.369, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.457, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

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
    "fetched_at": "2026-10-04T14:41:51.678107+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity Chewy is growing! We're looking for a Software Engineer III to help define and scale the frontend foundations that power consistent, accessible, an"
  }
]
```

## CVS Health

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 148 / 65.621s
- Company elapsed time: 85.475s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 126 / 0 / 0
- Detail cache statuses: {'fetched:new': 125, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 12, 'usable_jd': 12}
- Raw jobs found: 362
- After US/location filtering: 126
- With trustworthy posted_date: 126
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 37.378, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.879, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 4.705, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 12.055, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.653, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.953, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.737, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.686, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 6.12, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1054125",
    "title": "Lead Director, Software Product Management",
    "location": "Work At Home-Arizona",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/Work-At-Home-Arizona/Lead-Director--Software-Product-Management_R1054125",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:56.148750+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1040005",
    "title": "Senior Data Engineer",
    "location": "TX - Irving",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/TX---Irving/Senior-Data-Engineer_R1040005",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:56.148750+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R0992094",
    "title": "Senior Decision Scientist - AI",
    "location": "NY - New York",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/NY---New-York/Senior-Decision-Scientist---Growth-Analytics_R0992094",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:56.148750+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R0950427",
    "title": "Principal Software Engineer",
    "location": "IRL - Galway",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/IRL---Galway/Principal-Software-Engineer_R0950427",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:56.148750+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R0978850",
    "title": "Software Development Engineer",
    "location": "Galway-Bonham Quay Dock Road",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/Galway-Bonham-Quay-Dock-Road/Software-Development-Engineer_R0978850",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:41:56.148750+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.091s
- Company elapsed time: 0.212s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 59
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
    "updated_date": "2026-09-28",
    "fetched_at": "2026-10-04T14:41:56.683676+00:00",
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
    "fetched_at": "2026-10-04T14:41:56.683676+00:00",
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
    "fetched_at": "2026-10-04T14:41:56.683676+00:00",
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
    "fetched_at": "2026-10-04T14:41:56.683676+00:00",
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
    "fetched_at": "2026-10-04T14:41:56.683676+00:00",
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
- HTTP requests/cumulative request time: 22 / 16.070s
- Company elapsed time: 21.865s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 6 / 54
- Detail cache statuses: {'reused': 6}
- Relevant JD recovery: {'cache_reused': 6, 'eligible': 6, 'deterministic_skip': 34, 'ai_skip': 20, 'usable_jd': 6}
- Raw jobs found: 296
- After US/location filtering: 60
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.496, "first_pass_survivors": 37, "group": "official", "jds_resolved": 0, "original_postings_resolved": 37, "page_budget": 2, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 37, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 3.105, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 1.141, "first_pass_survivors": 16, "group": "official", "jds_resolved": 0, "original_postings_resolved": 16, "page_budget": 2, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 24, "stop_reason": "early_stop", "unique_contribution": 16, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 0.829, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 2, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 4.731, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 51, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 51}
- Query diagnostic: {"elapsed_seconds": 2.374, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 37, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 2.543, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 2.407, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 2.239, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 2, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 37, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 37}

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
    "fetched_at": "2026-10-04T14:41:56.896806+00:00",
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
    "fetched_at": "2026-10-04T14:41:56.896806+00:00",
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
    "fetched_at": "2026-10-04T14:41:56.896806+00:00",
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
    "fetched_at": "2026-10-04T14:41:56.896806+00:00",
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
    "fetched_at": "2026-10-04T14:41:56.896806+00:00",
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
- HTTP requests/cumulative request time: 16 / 6.741s
- Company elapsed time: 8.117s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: {'fetched:new': 1}
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 114
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.606, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 6, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.39, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.399, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.05, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.069, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.096, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.385, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.495, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.042, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

Sample normalized records:

```json
[
  {
    "company": "F5",
    "source": "f5_official_careers",
    "job_id": "RP1038890",
    "title": "Principal Product Manager – Partner/Channel",
    "location": "San Jose; Seattle",
    "official_url": "https://ffive.wd5.myworkdayjobs.com/f5jobs/job/San-Jose/Principal-Product-Manager---Partner-Channel_RP1038890",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:42:06.658376+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.090s
- Company elapsed time: 0.283s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 54, 'usable_jd': 54}
- Raw jobs found: 118
- After US/location filtering: 104
- With trustworthy posted_date: 104
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
    "fetched_at": "2026-10-04T14:42:13.813223+00:00",
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
    "fetched_at": "2026-10-04T14:42:13.813223+00:00",
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
    "fetched_at": "2026-10-04T14:42:13.813223+00:00",
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
    "fetched_at": "2026-10-04T14:42:13.813223+00:00",
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
    "fetched_at": "2026-10-04T14:42:13.813223+00:00",
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
- HTTP requests/cumulative request time: 90 / 60.296s
- Company elapsed time: 72.506s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 70 / 0 / 0
- Detail cache statuses: {'fetched:new': 70}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 265
- After US/location filtering: 70
- With trustworthy posted_date: 70
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 32.929, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 34, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 34}
- Query diagnostic: {"elapsed_seconds": 5.426, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.846, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 11.922, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 10.176, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.05, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 1.826, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 1.207, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 3.046, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 49}

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
    "fetched_at": "2026-10-04T14:42:14.102877+00:00",
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
    "fetched_at": "2026-10-04T14:42:14.102877+00:00",
    "date_confidence": "high",
    "description": "Wells Fargo is seeking a Lead Ai Engineer in Technology as part of Commercial and Corporate & Investment Banking Technology (CCIBT).). The primary focus of this group will be to le"
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
    "fetched_at": "2026-10-04T14:42:14.102877+00:00",
    "date_confidence": "high",
    "description": "About this role: The Application Risk Domain Officer operates within Technology Risk Management (TRM), part of Corporate Risk, providing independent second line oversight across ap"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-574285",
    "title": "2027 Technology Summer Internship – Early Careers (Software Engineering)",
    "location": "CHARLOTTE, NC; IRVING, TX; PHOENIX, AZ; CHANDLER, AZ; SAINT LOUIS, MO; ISELIN, NJ",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/XMLNAME-2027-Technology-Summer-Internship---Early-Careers--Software-Engineering-_R-574285",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:42:14.102877+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking aspiring Software Engineers to join the 2027 Technology Internship Program. Program Overview: The Wells Fargo Technology Internship Program "
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-566145",
    "title": "Principal Engineer Fixed Income, Currencies & Commodities (FICC)",
    "location": "CHARLOTTE, NC",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Principal-Engineer-Fixed-Income--Currencies---Commodities--FICC-_R-566145",
    "posted_date": "2026-09-30",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:42:14.102877+00:00",
    "date_confidence": "high",
    "description": "Wells Fargo is seeking a Principal Engineer within the Commercial Corporate & Investment Bank Technology (CCIBT) organization. Candidate will architect, build, and lead the next-ge"
  }
]
```

## Yahoo

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ouryahoo.wd5.myworkdayjobs.com/careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 84 / 33.562s
- Company elapsed time: 44.759s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 64 / 0 / 0
- Detail cache statuses: {'fetched:new': 63, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 256
- After US/location filtering: 64
- With trustworthy posted_date: 64
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 28.631, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 0.694, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 0.971, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 3.853, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 3.516, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 2.368, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 49, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 49}
- Query diagnostic: {"elapsed_seconds": 0.666, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.628, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 2.686, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 25}

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
    "fetched_at": "2026-10-04T14:42:14.776332+00:00",
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
    "fetched_at": "2026-10-04T14:42:14.776332+00:00",
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
    "fetched_at": "2026-10-04T14:42:14.776332+00:00",
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
    "fetched_at": "2026-10-04T14:42:14.776332+00:00",
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
    "fetched_at": "2026-10-04T14:42:14.776332+00:00",
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
- HTTP requests/cumulative request time: 25 / 2.728s
- Company elapsed time: 5.925s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 22 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 45
- After US/location filtering: 22
- With trustworthy posted_date: 22
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.925, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "Ansys", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 45}

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
    "fetched_at": "2026-10-04T14:42:18.762906+00:00",
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
    "fetched_at": "2026-10-04T14:42:18.762906+00:00",
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
    "fetched_at": "2026-10-04T14:42:18.762906+00:00",
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
    "fetched_at": "2026-10-04T14:42:18.762906+00:00",
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
    "fetched_at": "2026-10-04T14:42:18.762906+00:00",
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
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 250 / 106.446s
- Company elapsed time: 138.625s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 223 / 0 / 0
- Detail cache statuses: {'fetched:new': 223}
- Relevant JD recovery: {'eligible': 147, 'usable_jd': 147}
- Raw jobs found: 379
- After US/location filtering: 223
- With trustworthy posted_date: 223
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 60.821, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 3.574, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.122, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 6.125, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 19.315, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.643, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 31, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 31}
- Query diagnostic: {"elapsed_seconds": 4.008, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.12, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 35.04, "first_pass_survivors": 55, "group": "official", "jds_resolved": 55, "original_postings_resolved": 55, "page_budget": 12, "pages_fetched": 7, "query": "software engineer", "raw_jobs": 118, "stop_reason": "early_stop", "unique_contribution": 55, "unique_jobs": 118}

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
    "fetched_at": "2026-10-04T14:42:24.688770+00:00",
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
    "fetched_at": "2026-10-04T14:42:24.688770+00:00",
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
    "fetched_at": "2026-10-04T14:42:24.688770+00:00",
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
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:42:24.688770+00:00",
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
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:42:24.688770+00:00",
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
- HTTP requests/cumulative request time: 39 / 18.151s
- Company elapsed time: 21.970s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 27 / 0 / 0
- Detail cache statuses: {'fetched:new': 27}
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 68
- After US/location filtering: 27
- With trustworthy posted_date: 27
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.542, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 6, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 1.239, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 1.587, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 2.472, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 8.058, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 0.759, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.801, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.784, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.772, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 12}

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
    "fetched_at": "2026-10-04T14:42:59.536727+00:00",
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
    "fetched_at": "2026-10-04T14:42:59.536727+00:00",
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
    "posted_date": "2026-09-24",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:42:59.536727+00:00",
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
    "fetched_at": "2026-10-04T14:42:59.536727+00:00",
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
    "fetched_at": "2026-10-04T14:42:59.536727+00:00",
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
- HTTP requests/cumulative request time: 228 / 92.379s
- Company elapsed time: 122.487s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 204 / 0 / 0
- Detail cache statuses: {'fetched:new': 202, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 66, 'usable_jd': 66}
- Raw jobs found: 413
- After US/location filtering: 204
- With trustworthy posted_date: 204
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 35.203, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.786, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "early_stop", "unique_contribution": 23, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 17.376, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 55, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 55}
- Query diagnostic: {"elapsed_seconds": 15.009, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.623, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.413, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.551, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.205, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 16.048, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-102363",
    "title": "Manager, AI Next Frontier for Patient Engagements",
    "location": "Titusville, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Titusville-New-Jersey-United-States-of-America/Manager--AI-Next-Frontier-for-Patient-Engagements_R-102363",
    "posted_date": "2026-10-03",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:43:07.747534+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-093342",
    "title": "Manager, Product Group Engineering, PLM",
    "location": "Raynham, Massachusetts, United States of America; West Chester, Pennsylvania, United States of America; Palm Beach Gardens, Florida, United States of America; Warsaw, Indiana, United States of America; Raritan, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raynham-Massachusetts-United-States-of-America/Manager--Product-Group-Engineering--PLM_R-093342-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:43:07.747534+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-075011",
    "title": "Sr. Manager, Materials Management",
    "location": "Raynham, Massachusetts, United States of America; West Chester, Pennsylvania, United States of America; Palm Beach Gardens, Florida, United States of America; Warsaw, Indiana, United States of America; Raritan, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raynham-Massachusetts-United-States-of-America/Sr-Manager--Materials-Management_R-075011-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:43:07.747534+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-093335",
    "title": "Manager, Medical Affairs",
    "location": "Raynham, Massachusetts, United States of America; New Brunswick, New Jersey, United States of America; West Chester, Pennsylvania, United States of America; Palm Beach Gardens, Florida, United States of America; Warsaw, Indiana, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raynham-Massachusetts-United-States-of-America/Manager--Medical-Affairs_R-093335-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:43:07.747534+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-102017",
    "title": "Director, Regulatory Compliance",
    "location": "Santa Clara, California, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Santa-Clara-California-United-States-of-America/Director--Regulatory-Compliance_R-102017-1",
    "posted_date": "2026-10-02",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:43:07.747534+00:00",
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
- HTTP requests/cumulative request time: 41 / 17.997s
- Company elapsed time: 22.330s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 27 / 0 / 0
- Detail cache statuses: {'fetched:new': 27}
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 106
- After US/location filtering: 27
- With trustworthy posted_date: 27
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 7.483, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 6, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 15, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.606, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.595, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 3.031, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 5.664, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 0.628, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 0.612, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.584, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.378, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 22}

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
    "fetched_at": "2026-10-04T14:43:21.507709+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.507709+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.507709+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.507709+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.507709+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.315s
- Company elapsed time: 0.344s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 4 / 43
- Detail cache statuses: {'reused': 4}
- Relevant JD recovery: {'deterministic_skip': 38, 'eligible': 11, 'cache_reused': 4, 'ai_skip': 5, 'usable_jd': 11}
- Raw jobs found: 76
- After US/location filtering: 68
- With trustworthy posted_date: 68
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
    "fetched_at": "2026-10-04T14:43:21.625069+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.625069+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.625069+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.625069+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.625069+00:00",
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
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 155 / 57.203s
- Company elapsed time: 76.864s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 133 / 0 / 0
- Detail cache statuses: {'fetched:new': 133}
- Relevant JD recovery: {'eligible': 56, 'usable_jd': 56}
- Raw jobs found: 229
- After US/location filtering: 133
- With trustworthy posted_date: 133
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.73, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 6, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 29, "stop_reason": "early_stop", "unique_contribution": 26, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 1.164, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.664, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 10.432, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 21.295, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.423, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 1.159, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.732, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 19.381, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 12, "pages_fetched": 5, "query": "software engineer", "raw_jobs": 76, "stop_reason": "early_stop", "unique_contribution": 35, "unique_jobs": 76}

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
    "fetched_at": "2026-10-04T14:43:21.969737+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.969737+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.969737+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.969737+00:00",
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
    "fetched_at": "2026-10-04T14:43:21.969737+00:00",
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
- HTTP requests/cumulative request time: 48 / 15.791s
- Company elapsed time: 21.256s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 32 / 0 / 0
- Detail cache statuses: {'fetched:new': 32}
- Relevant JD recovery: {'eligible': 12, 'usable_jd': 12}
- Raw jobs found: 129
- After US/location filtering: 32
- With trustworthy posted_date: 32
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 12.519, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 6, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 27, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 0.422, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 1.071, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.358, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 2.021, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.476, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 1.93, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 0.413, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.426, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}

Sample normalized records:

```json
[
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042110",
    "title": "Lead Java Engineer",
    "location": "Chicago, Illinois; Reston, Virginia; Crum Lynne, Pennsylvania; Boca Raton, Florida",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Lead-Java-Engineer_19042110-1",
    "posted_date": "2026-09-09",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:43:26.610024+00:00",
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
    "fetched_at": "2026-10-04T14:43:26.610024+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The SOAR Development team designs and delivers automation capabilities "
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19041689",
    "title": "Vice President, Global Network Engineering",
    "location": "Chicago, Illinois",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Vice-President--Global-Network-Engineering_19041689",
    "posted_date": "2026-08-07",
    "updated_date": "",
    "fetched_at": "2026-10-04T14:43:26.610024+00:00",
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
    "fetched_at": "2026-10-04T14:43:26.610024+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview This role reports directly to Senior Manager, Data Science & Analytics "
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
    "fetched_at": "2026-10-04T14:43:26.610024+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The Global Infrastructure, Engineering & Operations (GIO) organization "
  }
]
```

## Travelers

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://travelers.wd5.myworkdayjobs.com/External`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 25
- HTTP requests/cumulative request time: 121 / 44.674s
- Company elapsed time: 61.322s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 95 / 0 / 0
- Detail cache statuses: {'fetched:new': 92, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 51, 'usable_jd': 51}
- Raw jobs found: 343
- After US/location filtering: 95
- With trustworthy posted_date: 95
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 21.198, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 6, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 41, "stop_reason": "early_stop", "unique_contribution": 41, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 4.564, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 2.623, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 9.218, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 54, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 11.846, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.63, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 2.431, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 2.409, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.655, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 12, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 58, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 58}

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
    "fetched_at": "2026-10-04T14:43:43.838927+00:00",
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
    "fetched_at": "2026-10-04T14:43:43.838927+00:00",
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
    "fetched_at": "2026-10-04T14:43:43.838927+00:00",
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
    "fetched_at": "2026-10-04T14:43:43.838927+00:00",
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
    "fetched_at": "2026-10-04T14:43:43.838927+00:00",
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
- HTTP requests/cumulative request time: 22 / 4.821s
- Company elapsed time: 5.001s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 16 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 24
- After US/location filtering: 16
- With trustworthy posted_date: 16
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.584, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.635, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.723, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 1.963, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.387, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.708, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}

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
    "fetched_at": "2026-10-04T14:43:47.866555+00:00",
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
    "fetched_at": "2026-10-04T14:43:47.866555+00:00",
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
    "fetched_at": "2026-10-04T14:43:47.866555+00:00",
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
    "fetched_at": "2026-10-04T14:43:47.866555+00:00",
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
    "fetched_at": "2026-10-04T14:43:47.866555+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.205s
- Company elapsed time: 0.233s
- Incremental mode/page cap: full_sweep / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 2, 'usable_jd': 2}
- Raw jobs found: 23
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
    "fetched_at": "2026-10-04T14:43:52.868490+00:00",
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
    "fetched_at": "2026-10-04T14:43:52.868490+00:00",
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
    "fetched_at": "2026-10-04T14:43:52.868490+00:00",
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
    "fetched_at": "2026-10-04T14:43:52.868490+00:00",
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
    "fetched_at": "2026-10-04T14:43:52.868490+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
