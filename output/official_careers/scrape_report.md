# Official careers scrape report — 2026-11-18_0031

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Runtime metrics

- Wall time: 479.948s
- HTTP requests/cumulative request time: 3517 / 1628.944s
- Listing pages/detail fetched/cache reused/prefilter skipped: 708 / 2608 / 51 / 262
- Detail cache statuses: {'fetched:changed': 1, 'fetched:missing_detail': 123, 'fetched:new': 2284, 'fetched:stale': 2, 'reuse_after_error:changed': 3, 'reuse_after_error:stale': 16, 'reused': 29}
- Relevant JD coverage: 4189 / 4206; added detail requests 22 / 150; deferred 0

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 12.833s
- Company elapsed time: 28.584s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 133, 'usable_jd': 133}
- Raw jobs found: 795
- After US/location filtering: 255
- With trustworthy posted_date: 255
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.347, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "\"Ai Engineer\"", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.069, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Machine Learning Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.29, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Data Scientist\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.236, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "\"Solutions Architect\"", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.216, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Data Engineer\"", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 2.027, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "\"Platform Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.566, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Full Stack Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.181, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "\"Forward Deployed Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.343, "first_pass_survivors": 70, "group": "official", "jds_resolved": 70, "original_postings_resolved": 70, "page_budget": 12, "pages_fetched": 8, "query": "\"Software Engineer\"", "raw_jobs": 160, "stop_reason": "early_stop", "unique_contribution": 70, "unique_jobs": 160}
- Query diagnostic: {"elapsed_seconds": 2.115, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Infrastructure Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.352, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 5, "pages_fetched": 4, "query": "\"Software Engineer III\"", "raw_jobs": 73, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 73}
- Query diagnostic: {"elapsed_seconds": 1.419, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "\"Web Solutions Engineer\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 1.424, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 2, "pages_fetched": 2, "query": "\"DeepMind\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "100597091549487814",
    "title": "Senior Software Engineer, Security/Privacy, Google Cloud Security and Privacy",
    "location": "Kirkland, WA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/100597091549487814-senior-software-engineer-security-privacy-google-cloud-security-and-privacy",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:31:16.808695+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "112627947780612806",
    "title": "Business Data Scientist, gUP Analytics",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/112627947780612806-business-data-scientist-gup-analytics",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:31:16.808695+00:00",
    "date_confidence": "high",
    "description": "Google's leadership team hand-picks thorny business challenges, and members of BizOps work in small teams to find solutions. As part of this team you fully immerse yourself in data"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "83493088667804358",
    "title": "Senior Software Engineer, Embedded Systems/Firmware, Google Cloud Platforms",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/83493088667804358-senior-software-engineer-embedded-systems-firmware-google-cloud-platforms",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:31:16.808695+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "121215133593543366",
    "title": "Software Engineer III, AI/ML GenAI, Google Workspace",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/121215133593543366-software-engineer-iii-ai-ml-genai-google-workspace",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:31:16.808695+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "102776873351553734",
    "title": "Senior Software Engineer, BigQuery Data Protection",
    "location": "Kirkland, WA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/102776873351553734-senior-software-engineer-bigquery-data-protection",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:31:16.808695+00:00",
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
- Pages/requests fetched: 46
- HTTP requests/cumulative request time: 46 / 15.565s
- Company elapsed time: 28.693s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 472, 'usable_jd': 472}
- Raw jobs found: 861
- After US/location filtering: 738
- With trustworthy posted_date: 738
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.17, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.344, "first_pass_survivors": 49, "group": "official", "jds_resolved": 49, "original_postings_resolved": 49, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 49, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 1.647, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.027, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.959, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.628, "first_pass_survivors": 49, "group": "official", "jds_resolved": 49, "original_postings_resolved": 49, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 50, "stop_reason": "page_budget", "unique_contribution": 49, "unique_jobs": 50}
- Query diagnostic: {"elapsed_seconds": 0.307, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 1.908, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 7.126, "first_pass_survivors": 206, "group": "official", "jds_resolved": 206, "original_postings_resolved": 206, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 206, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.833, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.323, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "systems development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.227, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.193, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 2, "pages_fetched": 2, "query": "applied scientist", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10604833",
    "title": "Software Development Engineer, AWS Transform Migrations",
    "location": "Boston, Massachusetts, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10604833/software-development-engineer-aws-transform-migrations",
    "posted_date": "2026-11-13",
    "updated_date": "2026-11-14",
    "fetched_at": "2026-11-18T00:31:16.809627+00:00",
    "date_confidence": "high",
    "description": "AWS Transform is building the next generation of Agentic AI services that autonomously migrate the world's largest enterprises to the cloud. With approximately 7/8 of all enterpris"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10604856",
    "title": "Software Development Engineer, Agentic AI, Velocity Labs",
    "location": "New York, New York, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10604856/software-development-engineer-agentic-ai-velocity-labs",
    "posted_date": "2026-11-15",
    "updated_date": "2026-11-14",
    "fetched_at": "2026-11-18T00:31:16.809627+00:00",
    "date_confidence": "high",
    "description": "The Velocity Labs team mission is to think beyond the confines of the normal product-orientated approach and to discover new ways to apply and embrace agentic AI. We have noticed h"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10604854",
    "title": "Sr. Software Development Engineer, Agentic AI, Velocity Labs",
    "location": "New York, New York, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10604854/sr-software-development-engineer-agentic-ai-velocity-labs",
    "posted_date": "2026-11-15",
    "updated_date": "2026-11-14",
    "fetched_at": "2026-11-18T00:31:16.809627+00:00",
    "date_confidence": "high",
    "description": "The Velocity Labs team mission is to think beyond the confines of the normal product-orientated approach and to discover new ways to apply and embrace agentic AI. We have noticed h"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10604939",
    "title": "Software Development Engineer, Audible AI Voice Production",
    "location": "Cambridge, Massachusetts, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10604939/software-development-engineer-audible-ai-voice-production",
    "posted_date": "2026-11-13",
    "updated_date": "2026-11-14",
    "fetched_at": "2026-11-18T00:31:16.809627+00:00",
    "date_confidence": "high",
    "description": "At Audible, we believe stories have the power to transform lives. It’s why we work with some of the world’s leading creators to produce and share audio storytelling with our millio"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10605453",
    "title": "Machine Learning Engineer, CreativeFlux, AI Studios",
    "location": "New York, New York, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10605453/machine-learning-engineer-creativeflux-ai-studios",
    "posted_date": "2026-11-15",
    "updated_date": "2026-11-15",
    "fetched_at": "2026-11-18T00:31:16.809627+00:00",
    "date_confidence": "high",
    "description": "Join the AI Studios Engineering org within Prime Video and Amazon MGM Studios as a Machine Learning Engineer on CreativeFlux, the ML platform powering Nara, our AI-native content c"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=ai+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 272.310s
- Company elapsed time: 287.452s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 143, 'usable_jd': 143}
- Raw jobs found: 840
- After US/location filtering: 271
- With trustworthy posted_date: 271
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 27.167, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 20.718, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.118, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.69, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.727, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 31.485, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 27.189, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.972, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 110.798, "first_pass_survivors": 119, "group": "official", "jds_resolved": 119, "original_postings_resolved": 119, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 119, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 23.588, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "apps-and-frameworks-SFTWR-AF", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200693970-0836",
    "title": "Wireless RF OTA MIMO Systems Engineer",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200693970/wireless-rf-ota-mimo-systems-engineer",
    "posted_date": "2026-11-18",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.812353+00:00",
    "date_confidence": "high",
    "description": "At Apple, we work every single day to craft products that enrich people’s lives. Do you love working on challenges that no one has solved yet? Do you like changing the game? As a W"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200693968-0836",
    "title": "Wireless RF OTA MIMO Validation Engineer",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200693968/wireless-rf-ota-mimo-validation-engineer",
    "posted_date": "2026-11-18",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.812353+00:00",
    "date_confidence": "high",
    "description": "At Apple, we work every single day to craft products that enrich people’s lives. Do you love working on challenges that no one has solved yet? Do you like changing the game? As a W"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200694534-3543",
    "title": "PHY Design Verification Engineer",
    "location": "San Diego, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200694534/phy-design-verification-engineer",
    "posted_date": "2026-11-18",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.812353+00:00",
    "date_confidence": "high",
    "description": "Would you like to join Apple’s growing wireless silicon development team? Our wireless SoC organization is responsible for all aspects of wireless silicon development with a partic"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200694534-3956",
    "title": "PHY Design Verification Engineer",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200694534/phy-design-verification-engineer",
    "posted_date": "2026-11-18",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.812353+00:00",
    "date_confidence": "high",
    "description": "Would you like to join Apple’s growing wireless silicon development team? Our wireless SoC organization is responsible for all aspects of wireless silicon development with a partic"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200695572-0157",
    "title": "SoC RTL Design Engineer",
    "location": "Austin, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200695572/soc-rtl-design-engineer",
    "posted_date": "2026-11-18",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.812353+00:00",
    "date_confidence": "high",
    "description": "At Apple, phenomenal ideas have a way of becoming great products and customer experiences very quickly. The industry is accustomed to Apple taping out the SOC’s for our various pro"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 239 / 61.043s
- Company elapsed time: 95.912s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 199 / 0 / 0
- Detail cache statuses: {'fetched:new': 178, 'fetched:missing_detail': 21}
- Relevant JD recovery: {'eligible': 45, 'usable_jd': 45}
- Raw jobs found: 390
- After US/location filtering: 199
- With trustworthy posted_date: 199
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 27.384, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.836, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 10.918, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.986, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.229, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.157, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.042, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 10.281, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 21.864, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 120}

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200067577",
    "title": "Memory Circuit Design Engineer",
    "location": "United States, North Carolina, Raleigh",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557074579",
    "posted_date": "2026-11-18",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.813249+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200064838",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond; United States, New York, New York; United States, California, Mountain View; United States, California, Sunnyvale",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557051068",
    "posted_date": "2026-11-18",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.813249+00:00",
    "date_confidence": "high",
    "description": "Overview As a Principal Software Engineer, on the Substrate Application Platform team, you will help build the next generation platform for internal and external developers and age"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200055415",
    "title": "Software Engineer II - CTJ - Poly",
    "location": "United States, Washington, Redmond; United States, Virginia, Reston; United States, Maryland, Annapolis Junction",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556995354",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.813249+00:00",
    "date_confidence": "high",
    "description": "Overview Join Microsoft’s Microsoft Specialized Cloud Team as a Software Engineer working on one of the most challenging and impactful problems in cloud computing: enabling Azure s"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200043524",
    "title": "Principal Physical Design Engineer",
    "location": "United States, Washington, Redmond; United States, California, Mountain View; United States, California, Santa Clara; United States, Oregon, Hillsboro; United States, Texas, Austin; United States, Idaho, Boise; United States, North Carolina, Raleigh",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556933623",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.813249+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200065031",
    "title": "Senior Software Engineer-Distributed System",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557051548",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:16.813249+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft is a company where passionate innovators come to collaborate, envision what can be and take their careers further. This is a world of more possibilities, more in"
  }
]
```

## NVIDIA

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.044s
- Company elapsed time: 0.044s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['NVIDIA workday probe blocked with HTTP 429']

## Salesforce

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.076s
- Company elapsed time: 0.076s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Salesforce workday probe blocked with HTTP 429']

## Adobe

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.038s
- Company elapsed time: 0.039s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Adobe workday probe blocked with HTTP 429']

## Meta

- Status: blocked
- Scraping method: meta
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 11 / 3.165s
- Company elapsed time: 3.180s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Meta careers Relay bundle did not expose the current job-search doc_id']

## TikTok

- Status: ok
- Scraping method: HTTP POST public supplier /search/job/posts
- Search URL/API: `https://api.lifeattiktok.com/api/v1/public/supplier/search/job/posts`
- Pagination: offset=0,50,...; limit=50; US city filter
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 26 / 20.114s
- Company elapsed time: 24.556s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 421, 'usable_jd': 421}
- Raw jobs found: 1237
- After US/location filtering: 704
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.086, "first_pass_survivors": 199, "group": "official", "jds_resolved": 199, "original_postings_resolved": 199, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 199, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 2.777, "first_pass_survivors": 128, "group": "official", "jds_resolved": 128, "original_postings_resolved": 128, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 128, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.667, "first_pass_survivors": 109, "group": "official", "jds_resolved": 109, "original_postings_resolved": 109, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 109, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.723, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 76, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.751, "first_pass_survivors": 61, "group": "official", "jds_resolved": 61, "original_postings_resolved": 61, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 61, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.52, "first_pass_survivors": 62, "group": "official", "jds_resolved": 62, "original_postings_resolved": 62, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 62, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 1.779, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 83, "stop_reason": "early_stop", "unique_contribution": 26, "unique_jobs": 83}
- Query diagnostic: {"elapsed_seconds": 0.591, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 3.662, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 200}

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
    "fetched_at": "2026-11-18T00:31:20.155804+00:00",
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
    "fetched_at": "2026-11-18T00:31:20.155804+00:00",
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
    "fetched_at": "2026-11-18T00:31:20.155804+00:00",
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
    "fetched_at": "2026-11-18T00:31:20.155804+00:00",
    "date_confidence": "unknown",
    "description": "The Commercial AI-CRM and Transaction team focuses on TikTok advertiser growth algorithms. Leveraging deep learning and large language model technologies, the team builds an algori"
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
    "fetched_at": "2026-11-18T00:31:20.155804+00:00",
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
- HTTP requests/cumulative request time: 218 / 60.229s
- Company elapsed time: 90.612s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 190 / 0 / 0
- Detail cache statuses: {'fetched:new': 187, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 30, 'usable_jd': 30}
- Raw jobs found: 544
- After US/location filtering: 190
- With trustworthy posted_date: 190
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 28.277, "first_pass_survivors": 65, "group": "official", "jds_resolved": 65, "original_postings_resolved": 65, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 65, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 10.957, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.862, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 38, "stop_reason": "early_stop", "unique_contribution": 19, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 11.24, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 46}
- Query diagnostic: {"elapsed_seconds": 7.871, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.607, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.144, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.88, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.773, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 80}

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
    "posted_date": "2026-10-28",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:44.712775+00:00",
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
    "fetched_at": "2026-11-18T00:31:44.712775+00:00",
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
    "fetched_at": "2026-11-18T00:31:44.712775+00:00",
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
    "fetched_at": "2026-11-18T00:31:44.712775+00:00",
    "date_confidence": "high",
    "description": "About the role and team At Uber, machine learning powers some of the most complex real-time decisions in the world — from matching riders with drivers and optimizing marketplace ef"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "303435",
    "title": "Staff Software Engineer - AI Developer Platform (AIFX)",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/303435",
    "posted_date": "2026-10-22",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:44.712775+00:00",
    "date_confidence": "high",
    "description": "About the Role As a Staff Software Engineer on Uber's AI Foundations & Developer Experience (AIFX) team, you will set technical direction across multiple AIFX projects and lead eff"
  }
]
```

## DoorDash

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/doordashusa/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.478s
- Company elapsed time: 2.838s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 95, 'usable_jd': 95}
- Raw jobs found: 415
- After US/location filtering: 414
- With trustworthy posted_date: 414
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
    "fetched_at": "2026-11-18T00:31:45.393481+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8068432",
    "title": "Account Executive, Emerging Markets",
    "location": "Atlanta, GA; Tempe, AZ; Tampa, FL; Raleigh, NC; Nashville, TN; Las Vegas, NV; Dallas, TX; Houston, TX; Chicago, IL; Austin, TX; Denver, CO; Philadelphia, PA; Tempe, AZ",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8068432",
    "posted_date": "2026-07-15",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:31:45.393481+00:00",
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
    "fetched_at": "2026-11-18T00:31:45.393481+00:00",
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:31:45.393481+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7958917",
    "title": "Account Manager, Platform Innovation",
    "location": "Chicago, IL; Detroit, MI; San Francisco, CA",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7958917",
    "posted_date": "2026-05-27",
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-18T00:31:45.393481+00:00",
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
- HTTP requests/cumulative request time: 126 / 45.795s
- Company elapsed time: 63.300s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 102 / 0 / 0
- Detail cache statuses: {'fetched:new': 102}
- Relevant JD recovery: {'eligible': 20, 'usable_jd': 20}
- Raw jobs found: 364
- After US/location filtering: 102
- With trustworthy posted_date: 102
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 30.068, "first_pass_survivors": 62, "group": "official", "jds_resolved": 62, "original_postings_resolved": 62, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 62, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 4.04, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 0.668, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 6.238, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 7.518, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.732, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.976, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 0.677, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 6.571, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 80}

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
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:45.503897+00:00",
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
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:45.503897+00:00",
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
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:45.503897+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "H226PE10",
    "title": "Principal Software Engineer",
    "location": "Los Angeles, California; New York - 229 W 43rd St; Bellevue - 110 110th Ave NE; San Francisco - 1160 Battery St; Palo Alto - 395 Page Mill Rd",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Principal-Software-Engineer_H226PE10",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:45.503897+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0047473",
    "title": "Design Engineer, Core Snapchat",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Design-Engineer--Core-Snapchat_R0047473-2",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:45.503897+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.134s
- Company elapsed time: 0.753s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 23, 'usable_jd': 23}
- Raw jobs found: 174
- After US/location filtering: 129
- With trustworthy posted_date: 129
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8396724",
    "title": "Administrative Business Partner I - Engineering, Product and Design",
    "location": "San Francisco, CA, US; Hybrid, CA, US; San Francisco, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8396724",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:31:48.232875+00:00",
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:31:48.232875+00:00",
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
    "fetched_at": "2026-11-18T00:31:48.232875+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8334884",
    "title": "Content Enablement Intern 2027 (USA)",
    "location": "San Francisco, CA, US; Remote, US; San Francisco, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8334884",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-18T00:31:48.232875+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8268336",
    "title": "Designer, PPM",
    "location": "Remote, US; San Francisco, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8268336",
    "posted_date": "2026-10-24",
    "updated_date": "2026-11-06",
    "fetched_at": "2026-11-18T00:31:48.232875+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.215s
- Company elapsed time: 0.829s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 41, 'usable_jd': 41}
- Raw jobs found: 372
- After US/location filtering: 271
- With trustworthy posted_date: 271
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "57131f28-cdf8-4776-aa87-8f9339e494ab",
    "title": "Staff Software Engineer - Compiler & Spark Runtime",
    "location": "US-CA-Menlo Park; Menlo Park, California, United States; US-WA-Bellevue; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/snowflake/57131f28-cdf8-4776-aa87-8f9339e494ab",
    "posted_date": "2026-11-13",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:48.986659+00:00",
    "date_confidence": "high",
    "description": "At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to "
  },
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "db1375f0-ea5d-404a-b640-259f94dbc995",
    "title": "Software Engineer - Database Engineering",
    "location": "US-CA-Menlo Park; Menlo Park, California, United States; US-WA-Bellevue",
    "official_url": "https://jobs.ashbyhq.com/snowflake/db1375f0-ea5d-404a-b640-259f94dbc995",
    "posted_date": "2026-07-28",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:48.986659+00:00",
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
    "fetched_at": "2026-11-18T00:31:48.986659+00:00",
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
    "fetched_at": "2026-11-18T00:31:48.986659+00:00",
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
    "fetched_at": "2026-11-18T00:31:48.986659+00:00",
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
- HTTP requests/cumulative request time: 473 / 214.459s
- Company elapsed time: 274.487s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 451 / 0 / 0
- Detail cache statuses: {'fetched:new': 451}
- Relevant JD recovery: {'eligible': 60, 'usable_jd': 60}
- Raw jobs found: 1928
- After US/location filtering: 451
- With trustworthy posted_date: 451
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 187.71, "first_pass_survivors": 319, "group": "official", "jds_resolved": 319, "original_postings_resolved": 319, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 319, "stop_reason": "page_budget", "unique_contribution": 319, "unique_jobs": 319}
- Query diagnostic: {"elapsed_seconds": 1.092, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 110, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 110}
- Query diagnostic: {"elapsed_seconds": 9.586, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 182, "stop_reason": "early_stop", "unique_contribution": 15, "unique_jobs": 182}
- Query diagnostic: {"elapsed_seconds": 64.268, "first_pass_survivors": 108, "group": "official", "jds_resolved": 108, "original_postings_resolved": 108, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 298, "stop_reason": "page_budget", "unique_contribution": 108, "unique_jobs": 298}
- Query diagnostic: {"elapsed_seconds": 2.558, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 5.415, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 1.079, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 70, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 70}
- Query diagnostic: {"elapsed_seconds": 0.444, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 67, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 67}
- Query diagnostic: {"elapsed_seconds": 2.334, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 282, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 282}

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076452",
    "title": "Senior Staff Technical Program Manager, Vulnerability, Configuration & Attack Surface Management",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162185079-senior-staff-technical-program-manager-vulnerability-configuration-attack-surface-management",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:49.819212+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076452",
    "title": "Senior Staff Technical Program Manager, Vulnerability, Configuration & Attack Surface Management",
    "location": "West Palm Beach, Florida, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162184959-senior-staff-technical-program-manager-vulnerability-configuration-attack-surface-management",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:49.819212+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0077233",
    "title": "Principal Outbound Product Manager",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162184569-principal-outbound-product-manager",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:49.819212+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0076226",
    "title": "Technical Product Manager, Legal AI and Platforms",
    "location": "Chicago, ILLINOIS, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162182430-technical-product-manager-legal-ai-and-platforms-",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:49.819212+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075511",
    "title": "Global Partner Manager, Deloitte – Autonomous Workforce/GBS",
    "location": "Baltimore, Maryland, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162177539-global-partner-manager-deloitte-autonomous-workforce-gbs",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:31:49.819212+00:00",
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
- HTTP requests/cumulative request time: 49 / 55.165s
- Company elapsed time: 67.741s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 20 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 20}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 348
- After US/location filtering: 20
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.774, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 4.607, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.475, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.665, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.584, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.517, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.513, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.543, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 6.062, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 48}

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46164",
    "title": "Data Risk Program Manager - Data Risk Office",
    "location": "Princeton, New Jersey, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Data-Risk-Program-Manager-Data-Risk-Office/46164",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:32:48.805207+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements The mission of the newly created Data Risk Office is to proactively mitigate and prevent risk across the Data Department by governing audit and control r"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46160",
    "title": "Data Center Warehouse Representative",
    "location": "Dayton, New Jersey, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Data-Center-Warehouse-Representative/46160",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:32:48.805207+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements The energy of a newsroom, the pace of a trading floor, the buzz of a recent tech breakthrough; we work hard, and we work fast - while keeping up the qual"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46149",
    "title": "AMER Logistics Representative",
    "location": "Middle Village, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/AMER-Logistics-Representative/46149",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:32:48.805207+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Position Summary We are seeking a highly motivated Logistics Representative to join our AMER Supply Chain team. This role is responsible for coordinating"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46147",
    "title": "Logistics Business Analyst – Finance & Controls",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Logistics-Business-Analyst-Finance-Controls/46147",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:32:48.805207+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements What is the role? We are strengthening our end-to-end Logistics Finance processes to improve how logistics costs are budgeted, forecasted, recorded, reco"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46152",
    "title": "Implementation Specialist, Systems & Tooling - ProdX",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Implementation-Specialist-Systems-Tooling-ProdX/46152",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:32:48.805207+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements About the Role: We’re hiring an Implementation Specialist to help support Product Management practice at Bloomberg. As part of the ProdX Systems+Tooling "
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 64
- HTTP requests/cumulative request time: 620 / 124.053s
- Company elapsed time: 209.153s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 556 / 0 / 0
- Detail cache statuses: {'fetched:new': 536, 'fetched:missing_detail': 20}
- Relevant JD recovery: {'eligible': 126, 'usable_jd': 126}
- Raw jobs found: 1263
- After US/location filtering: 556
- With trustworthy posted_date: 556
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.603, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 15.371, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.791, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.265, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.39, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.491, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.42, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.824, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.289, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 12.514, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "full stack", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.928, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "python react", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.145, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "pyspark databricks", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 7.919, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "experienced software engineer java python", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.286, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "agentic ai", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.061, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.599, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "software engineer ii", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.785, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.767, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "security engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.737, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "quantitative developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.986, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 1, "pages_fetched": 1, "query": "software engineer java spring", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.653, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 1, "pages_fetched": 1, "query": "software engineer python authe", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.127, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "aws data platform engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.896, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "data engineer applied ai", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 3.303, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 1, "pages_fetched": 1, "query": "asset management technology", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 20}

Sample normalized records:

```json
[
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210769834",
    "title": "Software Engineer III- Python / AWS / AI Enablement",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210769834",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:32:52.726463+00:00",
    "date_confidence": "high",
    "description": "We have an exciting and rewarding opportunity for you to take your software engineering career to the next level. As a Software Engineer III- Python / AWS / AI Enablement at JPMorg"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210808894",
    "title": "Software Engineer III-Gen AI/RAG/Python",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210808894",
    "posted_date": "2026-11-13",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:32:52.726463+00:00",
    "date_confidence": "high",
    "description": "We have an exciting and rewarding opportunity for you to take your software engineering career to the next level. As a Software Engineer III-Gen AI/RAG/Python at JPMorgan Chase wit"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210808518",
    "title": "Sr Lead Software Engineer - AI Engineer",
    "location": "NY, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210808518",
    "posted_date": "2026-11-12",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:32:52.726463+00:00",
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
    "posted_date": "2026-11-16",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:32:52.726463+00:00",
    "date_confidence": "high",
    "description": "Be an integral part of an agile team that's constantly pushing the envelope to enhance, build, and deliver top-notch technology products. As a Lead Software Engineer at JPMorganCha"
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
    "fetched_at": "2026-11-18T00:32:52.726463+00:00",
    "date_confidence": "high",
    "description": "We have an exciting opportunity to advance your career and drive meaningful impact by pushing the limits of modern engineering. As a Lead Software Engineer at JPMorganChase within "
  }
]
```

## Capital One

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.093s
- Company elapsed time: 0.093s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Capital One workday probe blocked with HTTP 429']

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 41
- HTTP requests/cumulative request time: 488 / 130.274s
- Company elapsed time: 197.663s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 447 / 0 / 0
- Detail cache statuses: {'fetched:new': 441, 'fetched:missing_detail': 6}
- Relevant JD recovery: {'eligible': 67, 'usable_jd': 67}
- Raw jobs found: 818
- After US/location filtering: 447
- With trustworthy posted_date: 447
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.419, "first_pass_survivors": 63, "group": "official", "jds_resolved": 63, "original_postings_resolved": 63, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 63, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 18.45, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.292, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 19.487, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 21.12, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.25, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.22, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.056, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.558, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 14.561, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "core infrastructure", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.143, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "cleared site reliability engineer database", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.433, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "software developer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 11.673, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "applications developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}

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
    "fetched_at": "2026-11-18T00:33:15.419007+00:00",
    "date_confidence": "high",
    "description": "Oracle Hardware Platform Development Engineering is seeking a highly driven AI Systems Engineer to evaluate and characterize next-generation GPU and AI accelerator platforms for Or"
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
    "fetched_at": "2026-11-18T00:33:15.419007+00:00",
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
    "fetched_at": "2026-11-18T00:33:15.419007+00:00",
    "date_confidence": "high",
    "description": "Oracle Health is seeking a Senior AI Agent Engineer to build production AI agents and workflow automation capabilities that accelerate analytics delivery, improve insight generatio"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "350644",
    "title": "Principal Software Engineer – Mobile & AI",
    "location": "BRNO, Czech Republic",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/350644",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:33:15.419007+00:00",
    "date_confidence": "high",
    "description": "We are looking for an experienced, hands-on engineer to lead the architecture and technical direction of NetSuite’s Mobile team across our applications and supporting services. You"
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
    "fetched_at": "2026-11-18T00:33:15.419007+00:00",
    "date_confidence": "high",
    "description": "You will work at the intersection of distributed systems, networking, and AI infrastructure, driving architecture, design, implementation, and performance optimization across softw"
  }
]
```

## Walmart Global Tech

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 44 / 12.755s
- Company elapsed time: 15.514s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Walmart Global Tech workday blocked with HTTP 429']

## Cloudflare

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/cloudflare/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.674s
- Company elapsed time: 2.657s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 97, 'usable_jd': 97}
- Raw jobs found: 481
- After US/location filtering: 478
- With trustworthy posted_date: 478
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
    "fetched_at": "2026-11-18T00:34:12.061698+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "8394342",
    "title": "AI & Automation Intern, Communications (Winter 2027)",
    "location": "In-Office; Austin, TX, United States; San Francisco, CA, United States",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/8394342?gh_jid=8394342",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:34:12.061698+00:00",
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
    "fetched_at": "2026-11-18T00:34:12.061698+00:00",
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
    "fetched_at": "2026-11-18T00:34:12.061698+00:00",
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
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-18T00:34:12.061698+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.277s
- Company elapsed time: 1.556s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 151, 'usable_jd': 151}
- Raw jobs found: 791
- After US/location filtering: 426
- With trustworthy posted_date: 426
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
    "fetched_at": "2026-11-18T00:34:14.719457+00:00",
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
    "fetched_at": "2026-11-18T00:34:14.719457+00:00",
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
    "fetched_at": "2026-11-18T00:34:14.719457+00:00",
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
    "fetched_at": "2026-11-18T00:34:14.719457+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s largest enterprises to the most am"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8393708",
    "title": "Account Executive, Amer Platform Grower (Velocity)",
    "location": "San Francisco; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8393708",
    "posted_date": "2026-11-16",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:34:14.719457+00:00",
    "date_confidence": "high",
    "description": "<div class=\"JobPostPage-content ⚙ ⚙g067fb\"> <p><strong>About Stripe</strong></p> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the wor"
  }
]
```

## Coinbase

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/coinbase/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.157s
- Company elapsed time: 1.064s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 55, 'usable_jd': 55}
- Raw jobs found: 257
- After US/location filtering: 212
- With trustworthy posted_date: 212
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
    "fetched_at": "2026-11-18T00:34:16.276644+00:00",
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
    "fetched_at": "2026-11-18T00:34:16.276644+00:00",
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
    "fetched_at": "2026-11-18T00:34:16.276644+00:00",
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
    "fetched_at": "2026-11-18T00:34:16.276644+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? At&nbsp;<a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sou"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8281622",
    "title": "Analyst, Privacy (Privacy Assessments)",
    "location": "Remote - USA; US - Remote Zone 1 (Job Requisitions Only)",
    "official_url": "https://www.coinbase.com/careers/positions/8281622?gh_jid=8281622",
    "posted_date": "2026-10-22",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-18T00:34:16.276644+00:00",
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
- Company elapsed time: 0.958s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 41, 'usable_jd': 41}
- Raw jobs found: 165
- After US/location filtering: 155
- With trustworthy posted_date: 155
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8379685",
    "title": "Accounts Receivable Operations Analyst",
    "location": "Menlo Park, CA; Chicago, IL; New York, NY",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8379685?t=gh_src=&gh_jid=8379685",
    "posted_date": "2026-11-12",
    "updated_date": "2026-11-13",
    "fetched_at": "2026-11-18T00:34:17.342131+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8259642",
    "title": "AML Investigator",
    "location": "Denver, CO; New York, NY; Westlake, TX; Denver, CO; New York, NY; Westlake, TX",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8259642?t=gh_src=&gh_jid=8259642",
    "posted_date": "2026-11-12",
    "updated_date": "2026-11-13",
    "fetched_at": "2026-11-18T00:34:17.342131+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "6669758",
    "title": "Android Engineer, Government Products",
    "location": "New York, NY; Menlo Park, CA",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/6669758?t=gh_src=&gh_jid=6669758",
    "posted_date": "2025-05-08",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-11-18T00:34:17.342131+00:00",
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
    "fetched_at": "2026-11-18T00:34:17.342131+00:00",
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
    "fetched_at": "2026-11-18T00:34:17.342131+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.129s
- Company elapsed time: 0.610s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 139
- After US/location filtering: 92
- With trustworthy posted_date: 92
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
    "fetched_at": "2026-11-18T00:34:18.301159+00:00",
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
    "fetched_at": "2026-11-18T00:34:18.301159+00:00",
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
    "fetched_at": "2026-11-18T00:34:18.301159+00:00",
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
    "fetched_at": "2026-11-18T00:34:18.301159+00:00",
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
    "fetched_at": "2026-11-18T00:34:18.301159+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.211s
- Company elapsed time: 1.061s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 17, 'usable_jd': 17}
- Raw jobs found: 254
- After US/location filtering: 147
- With trustworthy posted_date: 147
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
    "fetched_at": "2026-11-18T00:34:18.912743+00:00",
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
    "fetched_at": "2026-11-18T00:34:18.912743+00:00",
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
    "fetched_at": "2026-11-18T00:34:18.912743+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8760233002",
    "title": "Backend Engineer, Trusted Agentic Development",
    "location": "Remote, Poland; Turkey",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8760233002",
    "posted_date": "2026-09-08",
    "updated_date": "2026-11-12",
    "fetched_at": "2026-11-18T00:34:18.912743+00:00",
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
    "fetched_at": "2026-11-18T00:34:18.912743+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.084s
- Company elapsed time: 0.178s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 25
- After US/location filtering: 25
- With trustworthy posted_date: 25
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8927168002",
    "title": "Account Executive, Mobile Gaming",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8927168002",
    "posted_date": "2026-11-13",
    "updated_date": "2026-11-13",
    "fetched_at": "2026-11-18T00:34:19.974938+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8917177002",
    "title": "Associate Commercial Counsel",
    "location": "San Francisco Bay Area or Remote (U.S.); San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8917177002",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-09",
    "fetched_at": "2026-11-18T00:34:19.974938+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8761356002",
    "title": "Engineering Manager, Machine Learning - Safety",
    "location": "San Francisco Bay Area or Remote (U.S.); San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8761356002",
    "posted_date": "2026-11-16",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:34:19.974938+00:00",
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
    "fetched_at": "2026-11-18T00:34:19.974938+00:00",
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
    "fetched_at": "2026-11-18T00:34:19.974938+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.186s
- Company elapsed time: 0.617s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 13, 'usable_jd': 13}
- Raw jobs found: 114
- After US/location filtering: 77
- With trustworthy posted_date: 77
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
    "fetched_at": "2026-11-18T00:34:20.154103+00:00",
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
    "fetched_at": "2026-11-18T00:34:20.154103+00:00",
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
    "fetched_at": "2026-11-18T00:34:20.154103+00:00",
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
    "fetched_at": "2026-11-18T00:34:20.154103+00:00",
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
    "fetched_at": "2026-11-18T00:34:20.154103+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.134s
- Company elapsed time: 1.117s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 45, 'usable_jd': 45}
- Raw jobs found: 266
- After US/location filtering: 258
- With trustworthy posted_date: 258
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
    "fetched_at": "2026-11-18T00:34:20.771936+00:00",
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
    "fetched_at": "2026-11-18T00:34:20.771936+00:00",
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
    "fetched_at": "2026-11-18T00:34:20.771936+00:00",
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
    "fetched_at": "2026-11-18T00:34:20.771936+00:00",
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
    "fetched_at": "2026-11-18T00:34:20.771936+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.189s
- Company elapsed time: 1.864s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 51, 'usable_jd': 51}
- Raw jobs found: 312
- After US/location filtering: 272
- With trustworthy posted_date: 272
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8332753",
    "title": "Account Development Representative - Canada",
    "location": "Canada; Remote - Canada; Remote - Quebec; Remote - Toronto; Remote - Toronto",
    "official_url": "https://www.samsara.com/company/careers/roles/8332753?gh_jid=8332753",
    "posted_date": "2026-10-28",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:34:21.890448+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8207928",
    "title": "Account Development Representative - Canada",
    "location": "Remote - Canada; Remote - Ontario; Remote - Quebec; Remote - Toronto; Remote - Toronto",
    "official_url": "https://www.samsara.com/company/careers/roles/8207928?gh_jid=8207928",
    "posted_date": "2026-09-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:34:21.890448+00:00",
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
    "fetched_at": "2026-11-18T00:34:21.890448+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:34:21.890448+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "8325046",
    "title": "Account Development Representative II - Atlanta",
    "location": "Atlanta, Georgia, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8325046?gh_jid=8325046",
    "posted_date": "2026-10-26",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:34:21.890448+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.331s
- Company elapsed time: 0.623s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 146
- After US/location filtering: 76
- With trustworthy posted_date: 76
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8927794002",
    "title": "Accountant, Lease & Fleet",
    "location": "San Francisco, CA; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8927794002?gh_jid=8927794002",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-18T00:34:23.755702+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8927798002",
    "title": "Accountant, Lease & Fleet",
    "location": "New York, NY; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8927798002?gh_jid=8927798002",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-18T00:34:23.755702+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8948757002",
    "title": "Analytics Lead, Growth Strategy & Analytics",
    "location": "San Francisco, CA; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8948757002?gh_jid=8948757002",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:34:23.755702+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8948773002",
    "title": "Analytics Lead, Growth Strategy & Analytics",
    "location": "New York, NY; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8948773002?gh_jid=8948773002",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:34:23.755702+00:00",
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
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-18T00:34:23.755702+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.223s
- Company elapsed time: 0.365s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 12, 'usable_jd': 12}
- Raw jobs found: 87
- After US/location filtering: 65
- With trustworthy posted_date: 65
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
    "fetched_at": "2026-11-18T00:34:24.379563+00:00",
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
    "fetched_at": "2026-11-18T00:34:24.379563+00:00",
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
    "fetched_at": "2026-11-18T00:34:24.379563+00:00",
    "date_confidence": "high",
    "description": "Build a deep understanding of Spotify’s label, publishing, lyrics, and audiobook contracts, how they’re implemented in our royalty systems, and how they flow into royalty calculati"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "8251142e-f213-45df-89a9-914e814bd7a7",
    "title": "Associate Director, Proposition Strategy",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/8251142e-f213-45df-89a9-914e814bd7a7",
    "posted_date": "2026-09-02",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:34:24.379563+00:00",
    "date_confidence": "high",
    "description": "Evaluate the commercial and economic viability of new propositions — including new offerings, complementary products, and packaging structures. Build robust business cases end to e"
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
    "fetched_at": "2026-11-18T00:34:24.379563+00:00",
    "date_confidence": "high",
    "description": "Own the AV experience across EMEA, including meeting rooms, boardrooms, common areas, labs, lounges, and digital signage. Provide thoughtful, high-quality AV support for executive "
  }
]
```

## Ramp

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/ramp`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.113s
- Company elapsed time: 0.561s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 66, 'usable_jd': 66}
- Raw jobs found: 181
- After US/location filtering: 169
- With trustworthy posted_date: 169
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "34413f8d-26bf-4bbc-8ade-eb309a0e2245",
    "title": "Software Engineer, Security, Cloud",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote (Canada); Remote (US); Miami, FL",
    "official_url": "https://jobs.ashbyhq.com/ramp/34413f8d-26bf-4bbc-8ade-eb309a0e2245",
    "posted_date": "2026-04-07",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:34:24.745601+00:00",
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
    "fetched_at": "2026-11-18T00:34:24.745601+00:00",
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
    "fetched_at": "2026-11-18T00:34:24.745601+00:00",
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
    "fetched_at": "2026-11-18T00:34:24.745601+00:00",
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
    "fetched_at": "2026-11-18T00:34:24.745601+00:00",
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
- Company elapsed time: 0.372s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 166
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
    "title": "Software Engineer, AI Connections (Developer Platform)",
    "location": "San Francisco, California; San Francisco, California, United States; New York, New York; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/notion/1fc309c8-da20-4ff2-84c7-8b863ece2b0a",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:34:25.308465+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.308465+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.308465+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.308465+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.308465+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.048s
- Company elapsed time: 0.107s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 33
- After US/location filtering: 25
- With trustworthy posted_date: 25
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
    "fetched_at": "2026-11-18T00:34:25.681571+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.681571+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.681571+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.681571+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.681571+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.103s
- Company elapsed time: 0.408s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 37, 'usable_jd': 37}
- Raw jobs found: 127
- After US/location filtering: 104
- With trustworthy posted_date: 104
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
    "fetched_at": "2026-11-18T00:34:25.790003+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.790003+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.790003+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.790003+00:00",
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
    "fetched_at": "2026-11-18T00:34:25.790003+00:00",
    "date_confidence": "high",
    "description": "WHO ARE WE? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  }
]
```

## Cisco

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.043s
- Company elapsed time: 0.044s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Cisco workday blocked with HTTP 429']

## SAP

- Status: blocked
- Scraping method: sap
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 104 / 256.283s
- Company elapsed time: 274.211s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ["sap search network error: HTTPSConnectionPool(host='careers.sap.com', port=443): Read timed out. (read timeout=30)"]

## HPE

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.074s
- Company elapsed time: 0.074s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['HPE workday probe blocked with HTTP 429']

## Disney

- Status: ok
- Scraping method: HTTP GET Disney server-rendered US search results
- Search URL/API: `https://www.disneycareers.com/en/search-jobs/software%20engineer/United%20States/391/1/2/6252001/39x76/-98x5/100/2`
- Pagination: ?p=1,2,3 per role query (intentional request cap)
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 43 / 20.408s
- Company elapsed time: 28.121s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 16 / 3 / 94
- Detail cache statuses: {'reused': 3}
- Relevant JD recovery: {'deterministic_skip': 88, 'cache_reused': 3, 'eligible': 19, 'ai_skip': 6, 'ai_recover': 5, 'detail_requests': 16, 'detail_failure': 16, 'budget_deferred': 0, 'usable_jd': 3}
- Raw jobs found: 270
- After US/location filtering: 113
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.522, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.631, "first_pass_survivors": 17, "group": "official", "jds_resolved": 0, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.294, "first_pass_survivors": 19, "group": "official", "jds_resolved": 0, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.43, "first_pass_survivors": 20, "group": "official", "jds_resolved": 0, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.693, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.873, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.557, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.352, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.291, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "103169129808",
    "title": "Software Engineer II - AI Performance",
    "location": "New York, New York",
    "official_url": "https://www.disneycareers.com/en/job/new-york/software-engineer-ii-ai-performance/391/103169129808",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:04.339609+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "103169132480",
    "title": "Software Engineer II - AI Insights",
    "location": "New York, New York",
    "official_url": "https://www.disneycareers.com/en/job/new-york/software-engineer-ii-ai-insights/391/103169132480",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:04.339609+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "103431216976",
    "title": "Sr Software Engineer - AI and Observability",
    "location": "New York, New York / Glendale, California",
    "official_url": "https://www.disneycareers.com/en/job/new-york/sr-software-engineer-ai-and-observability/391/103431216976",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:04.339609+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "103435648512",
    "title": "Lead Software Engineer-AI Licensing & Publishing Systems",
    "location": "Orlando, Florida",
    "official_url": "https://www.disneycareers.com/en/job/orlando/lead-software-engineer-ai-licensing-and-publishing-systems/391/103435648512",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:04.339609+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "R-04157",
    "title": "Facilities Operations Building Engineer",
    "location": "Emeryville, California",
    "official_url": "https://www.disneycareers.com/en/job/emeryville/facilities-operations-building-engineer/391/102250956944",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:04.339609+00:00",
    "date_confidence": "high",
    "description": ""
  }
]
```

## eBay

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.071s
- Company elapsed time: 0.071s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['eBay workday probe blocked with HTTP 429']

## Qualcomm

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://careers.qualcomm.com/api/pcsx/search?domain=qualcomm.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 145 / 23.555s
- Company elapsed time: 45.332s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 118 / 0 / 0
- Detail cache statuses: {'fetched:new': 115, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 43, 'usable_jd': 43}
- Raw jobs found: 253
- After US/location filtering: 118
- With trustworthy posted_date: 118
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 9.801, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.892, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.856, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 8.022, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.876, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.724, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.023, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.372, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.392, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3099490",
    "title": "Staff Security Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446722174672",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:21.952492+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Security Engineering General Summary: Qualcomm relentlessly innovates to deliver intelligent c"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3087655",
    "title": "PCIE Subsystem Architect",
    "location": "San Diego, California, United States of America; Austin, Texas, United States of America; Santa Clara, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446717356390",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:21.952492+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > SoC Architecture General Summary: Job Overview: Qualcomm is looking for an experienced PCIe Su"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3097651",
    "title": "Multimedia-System HW Validation and Integration Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721491121",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:21.952492+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Video Systems, HW Architecture General Summary: Qualcomm Multimedia Validation and Integration"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3099189",
    "title": "#Software Engineer - Automotive Platform",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446722119778",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:21.952492+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Software Engineering General Summary: ** This position is not eligible for Qualcomm immigratio"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3099505",
    "title": "Director Compute Chipset Product Manager",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446722176749",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:21.952492+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Operations Group, Operations Group > Product Management General Summary: Directs a comprehensive product strategy from product concep"
  }
]
```

## AMD

- Status: ok
- Scraping method: HTTP GET public Jibe/iCIMS jobs JSON
- Search URL/API: `https://careers.amd.com/api/jobs`
- Pagination: page=1,2,... per role query; stop on total/empty/repeat/short page
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 14 / 13.608s
- Company elapsed time: 15.892s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 199, 'usable_jd': 199}
- Raw jobs found: 1344
- After US/location filtering: 542
- With trustworthy posted_date: 542
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.533, "first_pass_survivors": 357, "group": "official", "jds_resolved": 357, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 357, "stop_reason": "page_budget", "unique_contribution": 357, "unique_jobs": 357}
- Query diagnostic: {"elapsed_seconds": 1.591, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning", "raw_jobs": 89, "stop_reason": "early_stop", "unique_contribution": 24, "unique_jobs": 89}
- Query diagnostic: {"elapsed_seconds": 3.384, "first_pass_survivors": 82, "group": "official", "jds_resolved": 82, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 82, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 4.06, "first_pass_survivors": 65, "group": "official", "jds_resolved": 65, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "AI research", "raw_jobs": 298, "stop_reason": "page_budget", "unique_contribution": 65, "unique_jobs": 298}
- Query diagnostic: {"elapsed_seconds": 2.323, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 300}

Sample normalized records:

```json
[
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "68391",
    "title": "Senior Staff Software Development Engineer, Routing",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-02-26",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:24.307083+00:00",
    "date_confidence": "high",
    "description": "WHAT YOU DO AT AMD CHANGES EVERYTHING At AMD, our mission is to build great products that accelerate next-generation computing experiences—from AI and data centers, to PCs, gaming "
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92605",
    "title": "Software Development Engineer - GPU Interconnects and Ethernet AI",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-11-02",
    "updated_date": "2026-11-14",
    "fetched_at": "2026-11-18T00:36:24.307083+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92045",
    "title": "HPC & AI Research Engineer / Software Engineer",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-09-10",
    "updated_date": "2026-11-14",
    "fetched_at": "2026-11-18T00:36:24.307083+00:00",
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
    "updated_date": "2026-11-13",
    "fetched_at": "2026-11-18T00:36:24.307083+00:00",
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
    "updated_date": "2026-11-14",
    "fetched_at": "2026-11-18T00:36:24.307083+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  }
]
```

## Zoom

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.039s
- Company elapsed time: 0.040s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Zoom workday probe blocked with HTTP 429']

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
- HTTP requests/cumulative request time: 1 / 0.654s
- Company elapsed time: 1.902s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 60, 'usable_jd': 60}
- Raw jobs found: 378
- After US/location filtering: 237
- With trustworthy posted_date: 237
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
    "fetched_at": "2026-11-18T00:36:27.024114+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8395558",
    "title": "Account Executive, Cloud and Data Services-Federal",
    "location": "Remote, Washington D.C.; Washington, D.C., United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8395558",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:27.024114+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8384262",
    "title": "Account Executive, Cloud and Data Services-SLED",
    "location": "Austin, Texas; Chicago, Illinois; Dallas, Texas; Illinois, United States; Texas, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8384262",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:27.024114+00:00",
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
    "fetched_at": "2026-11-18T00:36:27.024114+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8396658",
    "title": "Account Executive, Commercial (Chicago)",
    "location": "Chicago, Illinois; Chicago, Illinois, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8396658",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:27.024114+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.341s
- Company elapsed time: 2.779s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 76, 'usable_jd': 76}
- Raw jobs found: 901
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:28.926809+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:28.926809+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:28.926809+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:28.926809+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:28.926809+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.189s
- Company elapsed time: 1.125s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 31, 'usable_jd': 31}
- Raw jobs found: 267
- After US/location filtering: 247
- With trustworthy posted_date: 247
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:31.706724+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:31.706724+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:31.706724+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8384186",
    "title": "[2027] Data Scientist - PhD Early Career - Safety",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8384186?gh_jid=8384186",
    "posted_date": "2026-11-16",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:31.706724+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:31.706724+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.203s
- Company elapsed time: 0.749s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 202
- After US/location filtering: 98
- With trustworthy posted_date: 98
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8380007",
    "title": "Advanced Analytics Intern",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8380007?gh_jid=8380007",
    "posted_date": "2026-11-11",
    "updated_date": "2026-11-11",
    "fetched_at": "2026-11-18T00:36:32.836775+00:00",
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
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-18T00:36:32.836775+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8381807",
    "title": "Category Lead, Airbnb Services",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8381807?gh_jid=8381807",
    "posted_date": "2026-11-12",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:36:32.836775+00:00",
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
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-18T00:36:32.836775+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8372149",
    "title": "Connectivity Partner Specialist",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8372149?gh_jid=8372149",
    "posted_date": "2026-11-10",
    "updated_date": "2026-11-12",
    "fetched_at": "2026-11-18T00:36:32.836775+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.827s
- Company elapsed time: 4.024s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 159, 'usable_jd': 159}
- Raw jobs found: 660
- After US/location filtering: 530
- With trustworthy posted_date: 530
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
    "fetched_at": "2026-11-18T00:36:33.089013+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.089013+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.089013+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.089013+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.089013+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.145s
- Company elapsed time: 0.308s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
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
    "job_id": "4724999006",
    "title": "Agency Development Lead - Independent Agencies",
    "location": "Los Angeles/Santa Monica, CA; New York City, NY",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4724999006?gh_jid=4724999006",
    "posted_date": "2026-10-26",
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-18T00:36:33.587072+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.587072+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.587072+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.587072+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.587072+00:00",
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
- HTTP requests/cumulative request time: 24 / 24.641s
- Company elapsed time: 28.435s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 234, 'usable_jd': 234}
- Raw jobs found: 1068
- After US/location filtering: 458
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.417, "first_pass_survivors": 145, "group": "official", "jds_resolved": 145, "original_postings_resolved": 145, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 145, "unique_jobs": 149}
- Query diagnostic: {"elapsed_seconds": 3.942, "first_pass_survivors": 101, "group": "official", "jds_resolved": 101, "original_postings_resolved": 101, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 101, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.068, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 107, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 107}
- Query diagnostic: {"elapsed_seconds": 3.201, "first_pass_survivors": 64, "group": "official", "jds_resolved": 64, "original_postings_resolved": 64, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 64, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.321, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.299, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.013, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 55, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 55}
- Query diagnostic: {"elapsed_seconds": 0.867, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 3.306, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 149}

Sample normalized records:

```json
[
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7542987377129457938",
    "title": "Senior Software Engineer / Researcher, AI-Native database systems",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7542987377129457938",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:33.896218+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.896218+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.896218+00:00",
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
    "fetched_at": "2026-11-18T00:36:33.896218+00:00",
    "date_confidence": "unknown",
    "description": "The mission of our AML team is to push the next-generation AI infrastructure and recommendation platform for the ads ranking, search ranking, live & ecom ranking in our company. We"
  },
  {
    "company": "ByteDance",
    "source": "bytedance_official_careers",
    "job_id": "7642279421516941573",
    "title": "Software Engineer - AI Agent Infra",
    "location": "San Jose, California, United States of America",
    "official_url": "https://joinbytedance.com/search/7642279421516941573",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:33.896218+00:00",
    "date_confidence": "unknown",
    "description": "We are building the dedicated AI Agent infrastructure and product platform for the Security organization, enabling different business teams to rapidly build, deploy, and scale AI A"
  }
]
```

## Chime

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/chime/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.136s
- Company elapsed time: 0.583s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
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
    "fetched_at": "2026-11-18T00:36:37.113784+00:00",
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
    "fetched_at": "2026-11-18T00:36:37.113784+00:00",
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
    "fetched_at": "2026-11-18T00:36:37.113784+00:00",
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
    "fetched_at": "2026-11-18T00:36:37.113784+00:00",
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
    "fetched_at": "2026-11-18T00:36:37.113784+00:00",
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
- HTTP requests/cumulative request time: 123 / 42.428s
- Company elapsed time: 60.954s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 98 / 0 / 0
- Detail cache statuses: {'fetched:new': 94, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 28, 'usable_jd': 28}
- Raw jobs found: 490
- After US/location filtering: 98
- With trustworthy posted_date: 98
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.49, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.723, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.807, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 12.276, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.553, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.288, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.556, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 8.795, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.467, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "299281",
    "title": "Software Principal Engineer / Autonomous AI Software Engineering",
    "location": "Hopkinton, MA, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/299281",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:37.698158+00:00",
    "date_confidence": "high",
    "description": "Software Principal Engineer – Autonomous AI Software Engineering Software engineering is being reshaped by autonomous AI agents that can plan, write, test, and review code with inc"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "299282",
    "title": "Software Senior Principal Engineer / Autonomous AI Software Engineering",
    "location": "Hopkinton, MA, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/299282",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:37.698158+00:00",
    "date_confidence": "high",
    "description": "Software Senior Principal Engineer – Autonomous AI Software Engineering Software engineering is being reshaped by autonomous AI agents that can plan, write, test, and review code w"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "301993",
    "title": "Senior Analyst, Agentic AI Engineer",
    "location": "Hopkinton, MA, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/301993",
    "posted_date": "2026-11-16",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:37.698158+00:00",
    "date_confidence": "high",
    "description": "Senior Analyst, Agentic AI Engineer Our team sits at the forefront of Dell's Agentic AI transformation. We are building AI-native workflows, autonomous agents, and enterprise opera"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "299014",
    "title": "Agentic Context Engineering Architect & AI Practitioner",
    "location": "Hopkinton, MA, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/299014",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:37.698158+00:00",
    "date_confidence": "high",
    "description": "SUMMARY Agentic Context Engineering Architect & AI Practitioner Join us to do the best work of your career and make a profound social impact as an Agentic Context Engineering Archi"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "299294",
    "title": "Principal Engineer - AI, HPC & Storage Deployment",
    "location": "Round Rock, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/299294",
    "posted_date": "2026-10-26",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:37.698158+00:00",
    "date_confidence": "high",
    "description": "Principal Engineer - AI, HPC & Storage Deployment Infrastructure Solutions Group (ISG) builds the products that power infrastructure, solutions, and data management our customers n"
  }
]
```

## Dropbox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/dropbox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.100s
- Company elapsed time: 0.252s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 41
- After US/location filtering: 29
- With trustworthy posted_date: 29
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8328516",
    "title": "Application Security Engineer",
    "location": "Remote - Mexico; Mexico; US",
    "official_url": "https://jobs.dropbox.com/listing/8328516?gh_jid=8328516",
    "posted_date": "2026-11-12",
    "updated_date": "2026-11-12",
    "fetched_at": "2026-11-18T00:36:40.199999+00:00",
    "date_confidence": "high",
    "description": "<h2>Role Description</h2> <p>As part of the Product Security Engineering team, you’ll focus on reducing risk at scale by building the security infrastructure, automation, and tooli"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8328511",
    "title": "Application Security Engineer",
    "location": "Remote - US: Select locations; Mexico; US",
    "official_url": "https://jobs.dropbox.com/listing/8328511?gh_jid=8328511",
    "posted_date": "2026-11-12",
    "updated_date": "2026-11-12",
    "fetched_at": "2026-11-18T00:36:40.199999+00:00",
    "date_confidence": "high",
    "description": "<h2>Role Description</h2> <p>As part of the Product Security Engineering team, you’ll focus on reducing risk at scale by building the security infrastructure, automation, and tooli"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8356282",
    "title": "Director, Data Science & Engineering, Finance",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8356282?gh_jid=8356282",
    "posted_date": "2026-11-05",
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-18T00:36:40.199999+00:00",
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
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-18T00:36:40.199999+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qotuz85z92z66zpz73zz122zz67z0z78zz78zgz85z5f2sngz82zz65z4z69zm6"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8356674",
    "title": "GTM Program Manager",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8356674?gh_jid=8356674",
    "posted_date": "2026-11-10",
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-18T00:36:40.199999+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qowz81zz86zez84zz78zgbz86zrnz89zz122zz85zj2bn8u0kwwduz71zz86zwq"
  }
]
```

## Expedia Group

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.050s
- Company elapsed time: 0.051s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Expedia Group workday blocked with HTTP 429']

## HubSpot

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/hubspotjobs/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.171s
- Company elapsed time: 0.288s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 137
- After US/location filtering: 16
- With trustworthy posted_date: 16
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
    "fetched_at": "2026-11-18T00:36:40.503917+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:40.503917+00:00",
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
    "fetched_at": "2026-11-18T00:36:40.503917+00:00",
    "date_confidence": "high",
    "description": "<p><strong>***Now accepting applications for a December 1st, 2026 start date***</strong></p> <p>As an Account Executive on the Small Business sales team, you will identify, source,"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8356758",
    "title": "Head of Performance Partnerships",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8356758?gh_jid=8356758",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:36:40.503917+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-34030</strong></p> <p><strong>Application deadline: </strong>Monday, November 30th at 9am ET</p> <hr> <p>&nbsp;</p> <h2><strong>Role Summary</strong></h2> <p>Our mis"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8031160",
    "title": "Outbound Business Development Representative (BDR)",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8031160?gh_jid=8031160",
    "posted_date": "2026-06-29",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:36:40.503917+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.160s
- Company elapsed time: 0.496s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 83
- After US/location filtering: 74
- With trustworthy posted_date: 74
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
    "fetched_at": "2026-11-18T00:36:40.793458+00:00",
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
    "fetched_at": "2026-11-18T00:36:40.793458+00:00",
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
    "fetched_at": "2026-11-18T00:36:40.793458+00:00",
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
    "fetched_at": "2026-11-18T00:36:40.793458+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8250361",
    "title": "Commercial Counsel",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8250361",
    "posted_date": "2026-10-02",
    "updated_date": "2026-10-02",
    "fetched_at": "2026-11-18T00:36:40.793458+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  }
]
```

## Intel

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.084s
- Company elapsed time: 0.085s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Intel workday probe blocked with HTTP 429']

## MathWorks

- Status: ok
- Scraping method: HTTP GET server-rendered MathWorks search + JobPosting JSON-LD
- Search URL/API: `https://www.mathworks.com/company/jobs/opportunities/search/`
- Pagination: page=2,3,... after the unnumbered first page; stop on empty/repeat/short page
- Pages/requests fetched: 13
- HTTP requests/cumulative request time: 57 / 21.046s
- Company elapsed time: 23.978s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 44 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 17, 'usable_jd': 17}
- Raw jobs found: 133
- After US/location filtering: 44
- With trustworthy posted_date: 44
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.752, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 24, "stop_reason": "early_stop", "unique_contribution": 24, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 1.152, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 24, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 1.05, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 3.287, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 3.21, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 23, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 1.393, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.625, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.614, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.895, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 33, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 33}

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
    "fetched_at": "2026-11-18T00:36:41.376147+00:00",
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
    "fetched_at": "2026-11-18T00:36:41.376147+00:00",
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
    "fetched_at": "2026-11-18T00:36:41.376147+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37926",
    "title": "Development Applications Engineer",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37926-development-applications-engineer?keywords=ai+engineer",
    "posted_date": "2026-11-12",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:41.376147+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37921",
    "title": "Senior Software Engineer",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37921-senior-software-engineer?keywords=ai+engineer",
    "posted_date": "2026-11-12",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:36:41.376147+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.182s
- Company elapsed time: 1.330s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 34, 'usable_jd': 34}
- Raw jobs found: 394
- After US/location filtering: 249
- With trustworthy posted_date: 249
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:02.332667+00:00",
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:02.332667+00:00",
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:02.332667+00:00",
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:02.332667+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:37:02.332667+00:00",
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
- HTTP requests/cumulative request time: 138 / 21.192s
- Company elapsed time: 40.853s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 113 / 0 / 0
- Detail cache statuses: {'fetched:new': 110, 'fetched:missing_detail': 3}
- Relevant JD recovery: {'eligible': 41, 'usable_jd': 41}
- Raw jobs found: 223
- After US/location filtering: 113
- With trustworthy posted_date: 113
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 9.696, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.746, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.658, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 5.163, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 3.553, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.547, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.315, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.279, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 1.622, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "JR031478",
    "title": "Vice President, Lead Software Engineer",
    "location": "Alpharetta, Georgia, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549796478388",
    "posted_date": "2026-11-13",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:03.663541+00:00",
    "date_confidence": "high",
    "description": "Company Profile: Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment, and wealth management services. Th"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "JR038631",
    "title": "Vice President, Lead Cybersecurity Engineer",
    "location": "Alpharetta, Georgia, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549798264252",
    "posted_date": "2026-11-13",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:03.663541+00:00",
    "date_confidence": "high",
    "description": "Company Profile: Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment, and wealth management services. Th"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR036109",
    "title": "Java & Spark Developer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549797565648",
    "posted_date": "2026-11-12",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:03.663541+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "JR024846",
    "title": "Associate, Software Engineer",
    "location": "Alpharetta, Georgia, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549794721569",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:03.663541+00:00",
    "date_confidence": "high",
    "description": "Company Profile: Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment, and wealth management services. Th"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR046069",
    "title": "Equity Derivatives Pricing Platform Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549801018692",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:03.663541+00:00",
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
- HTTP requests/cumulative request time: 123 / 43.830s
- Company elapsed time: 65.253s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 94 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 38, 'usable_jd': 38}
- Raw jobs found: 435
- After US/location filtering: 94
- With trustworthy posted_date: 94
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 20.362, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 9.934, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 7.199, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 7.622, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 3.099, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 5.287, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 4.067, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.88, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.803, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

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
    "fetched_at": "2026-11-18T00:37:05.355636+00:00",
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
    "fetched_at": "2026-11-18T00:37:05.355636+00:00",
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
    "fetched_at": "2026-11-18T00:37:05.355636+00:00",
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
    "fetched_at": "2026-11-18T00:37:05.355636+00:00",
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
    "fetched_at": "2026-11-18T00:37:05.355636+00:00",
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
- HTTP requests/cumulative request time: 12 / 2.770s
- Company elapsed time: 3.811s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 3 / 31 / 41
- Detail cache statuses: {'reuse_after_error:stale': 14, 'reuse_after_error:changed': 3, 'reused': 12, 'fetched:new': 1, 'fetched:changed': 1, 'fetched:stale': 1}
- Relevant JD recovery: {'deterministic_skip': 11, 'cache_reused': 31, 'eligible': 15, 'ai_skip': 30, 'detail_requests': 3, 'detail_success': 3, 'budget_deferred': 0, 'usable_jd': 15}
- Raw jobs found: 90
- After US/location filtering: 56
- With trustworthy posted_date: 56
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.465, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.315, "first_pass_survivors": 9, "group": "official", "jds_resolved": 0, "original_postings_resolved": 9, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.313, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.282, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.32, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.374, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.303, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.301, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.297, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}

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
    "fetched_at": "2026-11-18T00:37:07.285518+00:00",
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
    "fetched_at": "2026-11-18T00:37:07.285518+00:00",
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
    "fetched_at": "2026-11-18T00:37:07.285518+00:00",
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
    "fetched_at": "2026-11-18T00:37:07.285518+00:00",
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
    "fetched_at": "2026-11-18T00:37:07.285518+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.460s
- Company elapsed time: 2.720s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 355, 'usable_jd': 355}
- Raw jobs found: 836
- After US/location filtering: 665
- With trustworthy posted_date: 665
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
    "fetched_at": "2026-11-18T00:37:10.257738+00:00",
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
    "fetched_at": "2026-11-18T00:37:10.257738+00:00",
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
    "fetched_at": "2026-11-18T00:37:10.257738+00:00",
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
    "fetched_at": "2026-11-18T00:37:10.257738+00:00",
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
    "fetched_at": "2026-11-18T00:37:10.257738+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.327s
- Company elapsed time: 0.754s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 2 / 2
- Detail cache statuses: {'reuse_after_error:stale': 2}
- Relevant JD recovery: {'eligible': 177, 'cache_reused': 2, 'ai_skip': 2, 'usable_jd': 177}
- Raw jobs found: 301
- After US/location filtering: 234
- With trustworthy posted_date: 234
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
    "fetched_at": "2026-11-18T00:37:12.979159+00:00",
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
    "fetched_at": "2026-11-18T00:37:12.979159+00:00",
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
    "fetched_at": "2026-11-18T00:37:12.979159+00:00",
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
    "fetched_at": "2026-11-18T00:37:12.979159+00:00",
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
    "fetched_at": "2026-11-18T00:37:12.979159+00:00",
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
- Pages/requests fetched: 22
- HTTP requests/cumulative request time: 91 / 15.642s
- Company elapsed time: 28.677s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 68 / 0 / 0
- Detail cache statuses: {'fetched:new': 66, 'fetched:missing_detail': 2}
- Relevant JD recovery: {'eligible': 12, 'usable_jd': 12}
- Raw jobs found: 198
- After US/location filtering: 68
- With trustworthy posted_date: 68
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.02, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.629, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 1.926, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 4.173, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 3.103, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.856, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.114, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.766, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 1.831, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137880",
    "title": "Principal Agentic Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922421877",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:13.734198+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139028",
    "title": "Sr Machine Learning Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923465515",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:13.734198+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139029",
    "title": "Staff Machine Learning Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923465527",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:13.734198+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139050",
    "title": "Staff Machine Learning Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923465539",
    "posted_date": "2026-11-16",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:13.734198+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0138308",
    "title": "Senior Software Engineer, Database & Caching Infra",
    "location": "San Jose, California, United States of America; Austin, Texas, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923253759",
    "posted_date": "2026-11-16",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:13.734198+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.183s
- Company elapsed time: 0.918s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 14, 'usable_jd': 14}
- Raw jobs found: 147
- After US/location filtering: 129
- With trustworthy posted_date: 129
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:38.653235+00:00",
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:38.653235+00:00",
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:38.653235+00:00",
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:38.653235+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8337440",
    "title": "Client Account Manager, Large Customer Sales (Big Box Retail)",
    "location": "Chicago, IL; Chicago",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8337440",
    "posted_date": "2026-11-10",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:38.653235+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  }
]
```

## Red Hat

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.088s
- Company elapsed time: 0.089s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Red Hat workday probe blocked with HTTP 429']

## Roku

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roku/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.222s
- Company elapsed time: 0.759s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 96
- After US/location filtering: 81
- With trustworthy posted_date: 81
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
    "fetched_at": "2026-11-18T00:37:39.662469+00:00",
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
    "fetched_at": "2026-11-18T00:37:39.662469+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8353024",
    "title": "Assistant General Counsel, Business & Legal Affairs - Content Distribution and Acquisition",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8353024?gh_jid=8353024",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:37:39.662469+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8352981",
    "title": "Assistant General Counsel, Business & Legal Affairs - Content Distribution and Acquisition",
    "location": "Santa Monica, California; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8352981?gh_jid=8352981",
    "posted_date": "2026-11-04",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:37:39.662469+00:00",
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
    "fetched_at": "2026-11-18T00:37:39.662469+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.258s
- Company elapsed time: 1.342s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 22, 'usable_jd': 22}
- Raw jobs found: 186
- After US/location filtering: 168
- With trustworthy posted_date: 168
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:37:40.427721+00:00",
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
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:37:40.427721+00:00",
    "date_confidence": "high",
    "description": "<p><strong>Team:</strong> Apollo — Block Applied R&amp;D<br><strong>Location:</strong> Remote (US / Canada)<br><strong>Duration:</strong> Fall/Winter 2026 co-op — 8 months, flexibl"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5415993008",
    "title": "Business Development Lead, AI Commercialization",
    "location": "Bay Area, CA, United States of America; US - CA - San Francisco City - Remote",
    "official_url": "http://block.xyz/careers/jobs/5415993008?gh_jid=5415993008",
    "posted_date": "2026-09-15",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:37:40.427721+00:00",
    "date_confidence": "high",
    "description": "<p>Block is building a new generation of AI-powered products with the potential to create entirely new ways for businesses to operate, engage with customers, and grow. We are looki"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5231999008",
    "title": "Business Development Rep Associate",
    "location": "Atlanta, GA, United States of America; US - GA - Atlanta Metro - Remote",
    "official_url": "http://block.xyz/careers/jobs/5231999008?gh_jid=5231999008",
    "posted_date": "2026-05-26",
    "updated_date": "2026-08-03",
    "fetched_at": "2026-11-18T00:37:40.427721+00:00",
    "date_confidence": "high",
    "description": "<p>Square is looking for high-energy, motivated professionals with sound business insight and natural sales instincts. You will be joining our Restaurant or Generalist team to help"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5232007008",
    "title": "Business Development Rep Associate",
    "location": "Bay Area, CA, United States of America; US - CA - San Francisco City - Remote",
    "official_url": "http://block.xyz/careers/jobs/5232007008?gh_jid=5232007008",
    "posted_date": "2026-05-27",
    "updated_date": "2026-08-03",
    "fetched_at": "2026-11-18T00:37:40.427721+00:00",
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
- HTTP requests/cumulative request time: 58 / 66.638s
- Company elapsed time: 76.957s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 41 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 41}
- Relevant JD recovery: {'eligible': 36, 'usable_jd': 36}
- Raw jobs found: 117
- After US/location filtering: 41
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 19.267, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 12.944, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 1.191, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 6.28, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 21.26, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.66, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.168, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.763, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 7.424, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 34, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 34}

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
    "fetched_at": "2026-11-18T00:37:41.771322+00:00",
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
    "fetched_at": "2026-11-18T00:37:41.771322+00:00",
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
    "fetched_at": "2026-11-18T00:37:41.771322+00:00",
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
    "fetched_at": "2026-11-18T00:37:41.771322+00:00",
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
    "fetched_at": "2026-11-18T00:37:41.771322+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.200s
- Company elapsed time: 1.404s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 52, 'usable_jd': 52}
- Raw jobs found: 346
- After US/location filtering: 276
- With trustworthy posted_date: 276
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
    "fetched_at": "2026-11-18T00:37:42.412227+00:00",
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
    "fetched_at": "2026-11-18T00:37:42.412227+00:00",
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
    "fetched_at": "2026-11-18T00:37:42.412227+00:00",
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
    "fetched_at": "2026-11-18T00:37:42.412227+00:00",
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
    "fetched_at": "2026-11-18T00:37:42.412227+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><strong>Who We Are</strong></h3> <p>Verkada is transforming how organizations protect their people and places with an integrated, privacy-sensitive A"
  }
]
```

## Visa

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.084s
- Company elapsed time: 0.084s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Visa workday probe blocked with HTTP 429']

## WeRide

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/weride`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.124s
- Company elapsed time: 0.140s
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
    "fetched_at": "2026-11-18T00:37:43.902742+00:00",
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
    "fetched_at": "2026-11-18T00:37:43.902742+00:00",
    "date_confidence": "high",
    "description": "BS/MS/PhD degree in Robotics, Computer Science, Electrical Engineering or equivalent practical experience. Experience in data structures and advanced algorithms Experience programm"
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
    "fetched_at": "2026-11-18T00:37:43.902742+00:00",
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
    "fetched_at": "2026-11-18T00:37:43.902742+00:00",
    "date_confidence": "high",
    "description": "Team Introduction: The AI team is responsible for developing CV/ML algorithms to understand the surroundings of ego vehicles in real time , including obstacle detection, online map"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "5a7cbc83-2381-482e-9d6d-e9c9d59ad63b",
    "title": "New Grads 2027 - Software Engineer, Algorithm",
    "location": "San Jose, CA",
    "official_url": "https://jobs.lever.co/weride/5a7cbc83-2381-482e-9d6d-e9c9d59ad63b",
    "posted_date": "2026-08-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:43.902742+00:00",
    "date_confidence": "high",
    "description": "Prediction : Design models that forecast the behaviors and intentions of surrounding vehicles, pedestrians, and other dynamic agents, enabling safer driving decisions Mapping & Loc"
  }
]
```

## Workday

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.086s
- Company elapsed time: 0.087s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Workday workday probe blocked with HTTP 429']

## Zillow

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.069s
- Company elapsed time: 0.070s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Zillow workday probe blocked with HTTP 429']

## Zscaler

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/zscaler/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.200s
- Company elapsed time: 1.618s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 16, 'usable_jd': 16}
- Raw jobs found: 373
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
    "fetched_at": "2026-11-18T00:37:44.200590+00:00",
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
    "fetched_at": "2026-11-18T00:37:44.200590+00:00",
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
    "fetched_at": "2026-11-18T00:37:44.200590+00:00",
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
    "fetched_at": "2026-11-18T00:37:44.200590+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5273283007",
    "title": "Account Executive, Commercial - Ohio",
    "location": "Remote - Ohio, USA",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5273283007",
    "posted_date": "2026-10-26",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-18T00:37:44.200590+00:00",
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
- HTTP requests/cumulative request time: 13 / 5.702s
- Company elapsed time: 6.090s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 3 / 0 / 0
- Detail cache statuses: {'fetched:new': 3}
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 12
- After US/location filtering: 3
- With trustworthy posted_date: 3
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.22, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.417, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.54, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.834, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.427, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.423, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.58, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.453, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.442, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}

Sample normalized records:

```json
[
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R31091",
    "title": "Software Engineer III",
    "location": "USA - MA - Boston - BOS1",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/USA---MA---Boston---BOS1/Software-Engineer-II_R31091",
    "posted_date": "2026-10-26",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:44.523076+00:00",
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
    "fetched_at": "2026-11-18T00:37:44.523076+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity Chewy's IAM team keeps the right people, services, and AI agents connected to the right access, from someone's first day to their last. As an IAM E"
  },
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R31215",
    "title": "Software Engineer II",
    "location": "USA - MA - Boston - BOS1",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/USA---MA---Boston---BOS1/Software-Engineer-II_R31215",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:44.523076+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity: Chewy Plus Team is building innovative and exciting solutions towards chewy’s mission to be the most trusted and convenient destination for pet pa"
  }
]
```

## CVS Health

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.054s
- Company elapsed time: 0.055s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['CVS Health workday probe blocked with HTTP 429']

## Duolingo

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/duolingo/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.101s
- Company elapsed time: 0.343s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 58
- After US/location filtering: 50
- With trustworthy posted_date: 50
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
    "fetched_at": "2026-11-18T00:37:45.874257+00:00",
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
    "fetched_at": "2026-11-18T00:37:45.874257+00:00",
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
    "fetched_at": "2026-11-18T00:37:45.874257+00:00",
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
    "fetched_at": "2026-11-18T00:37:45.874257+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8943317002",
    "title": "Associate Creative Director",
    "location": "New York, NY; New York, New York, United States",
    "official_url": "https://careers.duolingo.com/jobs/8943317002?gh_jid=8943317002",
    "posted_date": "2026-11-13",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:45.874257+00:00",
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
- HTTP requests/cumulative request time: 29 / 23.439s
- Company elapsed time: 40.728s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 2 / 7 / 71
- Detail cache statuses: {'reused': 6, 'fetched:stale': 1}
- Relevant JD recovery: {'deterministic_skip': 51, 'cache_reused': 7, 'eligible': 7, 'ai_skip': 20, 'detail_requests': 2, 'detail_success': 1, 'budget_deferred': 0, 'usable_jd': 7}
- Raw jobs found: 336
- After US/location filtering: 78
- With trustworthy posted_date: 3
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.487, "first_pass_survivors": 45, "group": "official", "jds_resolved": 0, "original_postings_resolved": 45, "page_budget": 2, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 3.447, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 1.632, "first_pass_survivors": 16, "group": "official", "jds_resolved": 0, "original_postings_resolved": 16, "page_budget": 2, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 23, "stop_reason": "early_stop", "unique_contribution": 16, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 1.214, "first_pass_survivors": 12, "group": "official", "jds_resolved": 0, "original_postings_resolved": 12, "page_budget": 2, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 15.909, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 55, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 55}
- Query diagnostic: {"elapsed_seconds": 2.464, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 4.25, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 39, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 2.874, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 39, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 3.148, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 2, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164654",
    "title": "Senior AI Engineer. Innovation and R&D",
    "location": "Toronto, Ontario, Canada; Redwood City, California, United States",
    "official_url": "https://careers.equinix.com/jobs/senior-ai-engineer-innovation-and-r-d-toronto-ontario-canada-redwood-city-california-united-states",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:46.223525+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164645",
    "title": "Production Reliability Engineer, AI Platform",
    "location": "Toronto, Ontario, Canada; Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/production-reliability-engineer-ai-platform-toronto-ontario-canada-dallas-texas-united-states",
    "posted_date": "2026-11-13T14:13:59Z",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:46.223525+00:00",
    "date_confidence": "high",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164652",
    "title": "AI/Machine Learning Experience Engineer",
    "location": "Toronto, Ontario, Canada; Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/ai-machine-learning-experience-engineer-dallas-texas-united-states-toronto-ontario-canada",
    "posted_date": "2026-11-13T14:13:59Z",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:46.223525+00:00",
    "date_confidence": "high",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
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
    "fetched_at": "2026-11-18T00:37:46.223525+00:00",
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
    "fetched_at": "2026-11-18T00:37:46.223525+00:00",
    "date_confidence": "unknown",
    "description": ""
  }
]
```

## F5

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.075s
- Company elapsed time: 0.076s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['F5 workday probe blocked with HTTP 429']

## IXL Learning

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/ixllearning/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.162s
- Company elapsed time: 0.463s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 52, 'usable_jd': 52}
- Raw jobs found: 111
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
    "updated_date": "2026-11-05",
    "fetched_at": "2026-11-18T00:37:50.689698+00:00",
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
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-18T00:37:50.689698+00:00",
    "date_confidence": "high",
    "description": "<p><span style=\"font-weight: 400;\">IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide, is seeking a US English Language"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8856961002",
    "title": "Associate Digital Designer",
    "location": "San Mateo, CA; San Mateo, California, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8856961002",
    "posted_date": "2026-10-13",
    "updated_date": "2026-11-11",
    "fetched_at": "2026-11-18T00:37:50.689698+00:00",
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
    "fetched_at": "2026-11-18T00:37:50.689698+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide, is seeking an upbeat, focused, high-energy individual to join ou"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8590063002",
    "title": "Associate Educational Sales Consultant, Inside Sales, New Grad",
    "location": "San Mateo, CA; San Mateo, California, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8590063002",
    "posted_date": "2026-06-15",
    "updated_date": "2026-10-22",
    "fetched_at": "2026-11-18T00:37:50.689698+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide,&nbsp;is seeking an upbeat, focused, high-energy individual to jo"
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

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.162s
- Company elapsed time: 0.163s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Wells Fargo workday probe blocked with HTTP 429']

## Yahoo

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.064s
- Company elapsed time: 0.064s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Yahoo workday probe blocked with HTTP 429']

## Ansys

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.synopsys.com/search-jobs`
- Pagination: p=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 3
- HTTP requests/cumulative request time: 21 / 4.525s
- Company elapsed time: 7.785s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 18 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 45
- After US/location filtering: 18
- With trustworthy posted_date: 18
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 7.785, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "Ansys", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 45}

Sample normalized records:

```json
[
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "103259314912",
    "title": "Applications Engineer, Aerospace & Defense",
    "location": "",
    "official_url": "https://careers.synopsys.com/job/united-states/applications-engineer-aerospace-and-defense/44408/103259314912",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:51.381251+00:00",
    "date_confidence": "high",
    "description": "We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling customers to rapidly innovate AI-powered products. We deliver industry-leading silicon desi"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "103122221264",
    "title": "Sales Account Management, Staff",
    "location": "United States Off-site",
    "official_url": "https://careers.synopsys.com/job/michigan/sales-account-management-staff/44408/103122221264",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:51.381251+00:00",
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
    "fetched_at": "2026-11-18T00:37:51.381251+00:00",
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
    "fetched_at": "2026-11-18T00:37:51.381251+00:00",
    "date_confidence": "high",
    "description": "**Please note that this role can be flexibly based in the Southern California area.** We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling custo"
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
    "fetched_at": "2026-11-18T00:37:51.381251+00:00",
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

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.063s
- Company elapsed time: 0.064s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Flex workday probe blocked with HTTP 429']

## IQVIA

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.072s
- Company elapsed time: 0.073s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['IQVIA workday probe blocked with HTTP 429']

## Johnson & Johnson

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.079s
- Company elapsed time: 0.080s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Johnson & Johnson workday probe blocked with HTTP 429']

## Nasdaq

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.064s
- Company elapsed time: 0.065s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Nasdaq workday probe blocked with HTTP 429']

## PointClickCare

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/pointclickcare`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 2 / 0.789s
- Company elapsed time: 0.863s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 1 / 8 / 54
- Detail cache statuses: {'reused': 8}
- Relevant JD recovery: {'deterministic_skip': 45, 'eligible': 11, 'cache_reused': 8, 'ai_skip': 9, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 10}
- Raw jobs found: 87
- After US/location filtering: 83
- With trustworthy posted_date: 83
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "d668b17e-8c5c-4287-bf44-c7681701d5ce",
    "title": "(Canada) Deal Desk Analyst",
    "location": "Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/d668b17e-8c5c-4287-bf44-c7681701d5ce",
    "posted_date": "2026-11-16",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:59.455787+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "ccdecc93-aef2-4b2b-a981-6843f3c16221",
    "title": "(Canada) Principal ML System Engineer",
    "location": "Remote or Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/ccdecc93-aef2-4b2b-a981-6843f3c16221",
    "posted_date": "2026-08-13",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:59.455787+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "7a6a265e-2bb2-4d5c-adf7-1c9029e76841",
    "title": "(Canada) Sr. Revenue Operations Manager - Acute & Payer Partner",
    "location": "Remote or Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/7a6a265e-2bb2-4d5c-adf7-1c9029e76841",
    "posted_date": "2026-11-16",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:59.455787+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "f5851738-ab35-4969-849d-b1c938242fcc",
    "title": "(Canada) Sr. Revenue Operations Manager - Senior Living Partner",
    "location": "Remote or Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/f5851738-ab35-4969-849d-b1c938242fcc",
    "posted_date": "2026-11-16",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:59.455787+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "29937081-c433-4573-bc55-47dce4debe58",
    "title": "(US) Deal Desk Analyst",
    "location": "Remote, USA",
    "official_url": "https://jobs.lever.co/pointclickcare/29937081-c433-4573-bc55-47dce4debe58",
    "posted_date": "2026-11-16",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:37:59.455787+00:00",
    "date_confidence": "high",
    "description": ""
  }
]
```

## Stryker

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.061s
- Company elapsed time: 0.062s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Stryker workday probe blocked with HTTP 429']

## TransUnion

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.043s
- Company elapsed time: 0.044s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['TransUnion workday probe blocked with HTTP 429']

## Travelers

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.048s
- Company elapsed time: 0.049s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Travelers workday probe blocked with HTTP 429']

## Verizon

- Status: ok
- Scraping method: HTTP GET public Happydance jobs JSON + server-rendered detail flight data
- Search URL/API: `https://mycareer.verizon.com/api/jobs/search/`
- Pagination: page=1,2,... with pagesize=100; stop on total/empty/repeat
- Pages/requests fetched: 6
- HTTP requests/cumulative request time: 30 / 3.566s
- Company elapsed time: 4.147s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 24 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 49
- After US/location filtering: 24
- With trustworthy posted_date: 24
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.517, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.14, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.617, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.873, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.645, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.354, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}

Sample normalized records:

```json
[
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1103683",
    "title": "Java Full Stack Developer",
    "location": "Temple Terrace, Florida",
    "official_url": "https://mycareer.verizon.com/jobs/r-1103683/java-full-stack-developer/",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:38:00.170287+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1103685",
    "title": "Forward Deployed AI Engineer",
    "location": "Irving, Texas; Alpharetta, Georgia; Temple Terrace, Florida; Charlotte, North Carolina; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1103685/forward-deployed-ai-engineer/",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:38:00.170287+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1103673",
    "title": "Principal Forward Deployed AI Engineer",
    "location": "Basking Ridge, New Jersey; Alpharetta, Georgia; Irving, Texas; Temple Terrace, Florida; Charlotte, North Carolina",
    "official_url": "https://mycareer.verizon.com/jobs/r-1103673/principal-forward-deployed-ai-engineer/",
    "posted_date": "2026-11-13",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:38:00.170287+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1101085",
    "title": "Senior Manager - Responsible AI",
    "location": "Basking Ridge, New Jersey; Ashburn, Virginia; Cary, North Carolina; Rolling Meadows, Illinois; Alpharetta, Georgia; Seattle, Washington; San Francisco, California; Temple Terrace, Florida",
    "official_url": "https://mycareer.verizon.com/jobs/r-1101085/senior-manager-responsible-ai/",
    "posted_date": "2026-11-12",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:38:00.170287+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1103666",
    "title": "Principal Forward Deployed AI Engineer",
    "location": "Basking Ridge, New Jersey; Alpharetta, Georgia; Irving, Texas; Ashburn, Virginia; Temple Terrace, Florida",
    "official_url": "https://mycareer.verizon.com/jobs/r-1103666/principal-forward-deployed-ai-engineer/",
    "posted_date": "2026-11-11",
    "updated_date": "",
    "fetched_at": "2026-11-18T00:38:00.170287+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.089s
- Company elapsed time: 0.181s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 31
- After US/location filtering: 20
- With trustworthy posted_date: 20
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
    "fetched_at": "2026-11-18T00:38:04.318341+00:00",
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
    "fetched_at": "2026-11-18T00:38:04.318341+00:00",
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
    "fetched_at": "2026-11-18T00:38:04.318341+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8046381",
    "title": "Customer Success Manager, Enterprise - Healthcare",
    "location": "Chicago, IL; Remote - U.S.",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8046381",
    "posted_date": "2026-09-18",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-18T00:38:04.318341+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8301609",
    "title": "Director, Enterprise Sales",
    "location": "London, UK; Yext UK",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8301609",
    "posted_date": "2026-11-11",
    "updated_date": "2026-11-11",
    "fetched_at": "2026-11-18T00:38:04.318341+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
