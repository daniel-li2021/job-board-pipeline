# Official careers scrape report — 2026-09-15_0021

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Runtime metrics

- Wall time: 753.371s
- HTTP requests/cumulative request time: 6720 / 2633.004s
- Listing pages/detail fetched/cache reused/prefilter skipped: 1220 / 5459 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 562, 'fetched:new': 4693}

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 36
- HTTP requests/cumulative request time: 36 / 10.422s
- Company elapsed time: 22.046s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 684
- After US/location filtering: 185
- With trustworthy posted_date: 185
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.322, "first_pass_survivors": 100, "group": "official", "jds_resolved": 100, "original_postings_resolved": 100, "page_budget": 6, "pages_fetched": 5, "query": "\"Ai Engineer\"", "raw_jobs": 100, "stop_reason": "early_stop", "unique_contribution": 100, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 1.953, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Machine Learning Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.038, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Data Scientist\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.216, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Solutions Architect\"", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.206, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "\"Data Engineer\"", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 2.135, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Platform Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.976, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Full Stack Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.046, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "\"Forward Deployed Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.244, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 12, "pages_fetched": 4, "query": "\"Software Engineer\"", "raw_jobs": 80, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.011, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Infrastructure Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.249, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 5, "pages_fetched": 4, "query": "\"Software Engineer III\"", "raw_jobs": 80, "stop_reason": "early_stop", "unique_contribution": 48, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 1.357, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "\"Web Solutions Engineer\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 0.292, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 2, "pages_fetched": 1, "query": "\"DeepMind\"", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 19, "unique_jobs": 20}

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "124642289057178310",
    "title": "Software Engineer, Mobile (iOS), Google Maps Platform",
    "location": "Mountain View, CA, USA; Seattle, WA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/124642289057178310-software-engineer-mobile-ios-google-maps-platform",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:21:13.197318+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "73900377191129798",
    "title": "Senior Software Engineer, Infrastructure, Cloud New Product Intro and Software Development Tooling",
    "location": "New York, NY, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/73900377191129798-senior-software-engineer-infrastructure-cloud-new-product-intro-and-software-development-tooling",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:21:13.197318+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "85418857782485702",
    "title": "Software Engineer, GDC Networking, Google Cloud",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/85418857782485702-software-engineer-gdc-networking-google-cloud",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:21:13.197318+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "87304520224121542",
    "title": "Senior Embedded Software Engineer, Microcontroller OS",
    "location": "San Francisco, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/87304520224121542-senior-embedded-software-engineer-microcontroller-os",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:21:13.197318+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "119791515412112070",
    "title": "Software Engineer III, GDCH Infrastructure",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/119791515412112070-software-engineer-iii-gdch-infrastructure",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:21:13.197318+00:00",
    "date_confidence": "high",
    "description": "Google Cloud's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. We're "
  }
]
```

## Amazon

- Status: ok
- Scraping method: HTTP GET search.json
- Search URL/API: `https://www.amazon.jobs/en/search?base_query=software+engineer&country=USA&offset=0&result_limit=10&sort=recent`
- Pagination: newest-first offset by 20; minimum 2 pages, then two seen pages + one overlap page; otherwise hits/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 14.640s
- Company elapsed time: 25.503s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 796
- After US/location filtering: 692
- With trustworthy posted_date: 692
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.377, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 0.937, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 38, "stop_reason": "early_stop", "unique_contribution": 35, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 1.865, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.924, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.864, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.924, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 40, "stop_reason": "early_stop", "unique_contribution": 35, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 0.275, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.29, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 7.77, "first_pass_survivors": 219, "group": "official", "jds_resolved": 219, "original_postings_resolved": 219, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 219, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.817, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.095, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "systems development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.215, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.148, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 2, "pages_fetched": 2, "query": "applied scientist", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10537393",
    "title": "Software Development Engineer, AI Studios Engineering",
    "location": "Culver City, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10537393/software-development-engineer-ai-studios-engineering",
    "posted_date": "2026-09-11",
    "updated_date": "2026-09-12",
    "fetched_at": "2026-09-15T00:21:13.198222+00:00",
    "date_confidence": "high",
    "description": "Join us as a Software Development Engineer on the AI Studios Engineering org within Prime Video and Amazon MGM Studios, where you'll build intelligent systems at the intersection o"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10532198",
    "title": "Principal Machine Learning Engineer, Conversational AI Modeling and Learning",
    "location": "Bellevue, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10532198/principal-machine-learning-engineer-conversational-ai-modeling-and-learning",
    "posted_date": "2026-09-08",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:21:13.198222+00:00",
    "date_confidence": "high",
    "description": "Alexa AI is building the next generation of Alexa+, Amazon's LLM-powered conversational assistant, and its future is agentic: LLM systems that reason and act over dozens of chained"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10534272",
    "title": "Principal Technical Program Manager - Prime Video, PV Personalization and Discovery",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10534272/principal-technical-program-manager-prime-video-pv-personalization-and-discovery",
    "posted_date": "2026-09-09",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:21:13.198222+00:00",
    "date_confidence": "high",
    "description": "Prime Video is a first-stop entertainment destination offering customers a vast collection of premium programming in one app available across thousands of devices. Prime members ca"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10536015",
    "title": "Senior Software Engineer - AI/ML, AWS Neuron Inference",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10536015/senior-software-engineer-ai-ml-aws-neuron-inference",
    "posted_date": "2026-09-10",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:21:13.198222+00:00",
    "date_confidence": "high",
    "description": "AWS Neuron is the complete software stack for the AWS Inferentia and Trainium cloud-scale machine learning accelerators. This role is for a senior software engineer in the Machine "
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10528710",
    "title": "Sr. Software Development Engineer, Agentic AI",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10528710/sr-software-development-engineer-agentic-ai",
    "posted_date": "2026-09-03",
    "updated_date": "2026-09-04",
    "fetched_at": "2026-09-15T00:21:13.198222+00:00",
    "date_confidence": "high",
    "description": "We are building new capabilities in the Amazon Web Service (AWS) Agentic AI / Automated Reasoning (AR) group, by using Automated Reasoning in new, novel and exciting ways to enhanc"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=ai+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 17.736s
- Company elapsed time: 32.646s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 840
- After US/location filtering: 295
- With trustworthy posted_date: 295
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.878, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.314, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.292, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.247, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.327, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.318, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.436, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.244, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.184, "first_pass_survivors": 123, "group": "official", "jds_resolved": 123, "original_postings_resolved": 123, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 123, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.405, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 3, "pages_fetched": 3, "query": "apps-and-frameworks-SFTWR-AF", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200683686-0836",
    "title": "Machine Learning Engineer - Notifications & Personalization",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200683686/machine-learning-engineer-notifications-personalization",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.198910+00:00",
    "date_confidence": "high",
    "description": "Our team is looking for you to help make iOS more intelligent, proactive and personal. Our team is part of the core iOS experience, using privacy preserving on-device intelligence "
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200683681-0836",
    "title": "Software Development Engineer - iOS for Keyboard",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200683681/software-development-engineer-ios-for-keyboard",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.198910+00:00",
    "date_confidence": "high",
    "description": "Join the Keyboard Infrastructure team to build and maintain the foundational systems that power keyboard behavior across iOS & iPadOS. You'll own keyboard focus, lifecycle manageme"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680821-0836",
    "title": "Engineering Program Manager - SWE Photos",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680821/engineering-program-manager-swe-photos",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.198910+00:00",
    "date_confidence": "high",
    "description": "Apple is where individual imaginations gather together, committing to the values that lead to great work. Every new product we build, service we create, or Apple Store experience w"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200682986-3543",
    "title": "Senior iOS Software Engineer — CloudKit",
    "location": "San Diego, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200682986/senior-ios-software-engineer-cloudkit",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.198910+00:00",
    "date_confidence": "high",
    "description": "Imagine what we could create together! At Apple, new ideas have a way of becoming phenomenal products, services, and customer experiences very quickly. Bring passion and dedication"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200679102-3337",
    "title": "Sr. Software Development Engineer, ASE Storage",
    "location": "Seattle, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200679102/sr-software-development-engineer-ase-storage",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.198910+00:00",
    "date_confidence": "high",
    "description": "Apple Services Engineering (ASE) designs, builds, and operates the cloud infrastructure, server systems, and platform technologies that power many of Apple's most beloved experienc"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 247 / 69.117s
- Company elapsed time: 104.524s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 207 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 19, 'fetched:new': 188}
- Raw jobs found: 390
- After US/location filtering: 207
- With trustworthy posted_date: 207
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 27.609, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.745, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 13.99, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 9.186, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.007, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.67, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.892, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 9.244, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 26.612, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 120}

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200054251",
    "title": "Software Engineering Manager - Build and Tools",
    "location": "United States, California, Santa Clara",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556991368",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.199280+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200055510",
    "title": "Senior Azure Storage Validation Architect",
    "location": "United States, Washington, Redmond; United States, Texas, Austin; United States, California, Aliso Viejo; United States, North Carolina, Raleigh; United States, Oregon, Hillsboro",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556995533",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.199280+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and is responsible for powering Mic"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200055158",
    "title": "Senior Firmware Validation Engineer",
    "location": "United States, Washington, Redmond; United States, California, Mountain View; United States, Oregon, Hillsboro; United States, Texas, Austin; United States, North Carolina, Raleigh",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556994522",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.199280+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon and Cloud Hardware Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Microsof"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200038558",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556870050",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.199280+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft is a company where passionate innovators come to collaborate, envision what can be and take their careers to levels they cannot achieve anywhere else. This is a "
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200029223",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556803683",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.199280+00:00",
    "date_confidence": "high",
    "description": "Overview As Microsoft scales its Sovereign capabilities and aligns to increasing regulatory expectations and customer demands, our team is evolving to meet this challenge—by deepen"
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 506 / 241.851s
- Company elapsed time: 307.973s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 473 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 47, 'fetched:new': 426}
- Raw jobs found: 640
- After US/location filtering: 473
- With trustworthy posted_date: 473
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 50.323, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 36.394, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 31.157, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 27.754, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 25.357, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 32.948, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 24.548, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 21.315, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 33.396, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 23.276, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2018178",
    "title": "Applied AI Engineer",
    "location": "US, CA, Remote; US, AZ, Remote; US, FL, Remote; US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Remote/Applied-AI-Engineer_JR2018178-3",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.201776+00:00",
    "date_confidence": "high",
    "description": "NVIDIA's Silicon Co-Design Group is seeking an Applied AI Engineer to innovate, develop, and integrate innovative AI solutions into the design and automation infrastructure that po"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2018181",
    "title": "Applied AI Engineer",
    "location": "US, CA, Remote; US, GA, Remote; US, TX, Remote; US, AZ, Remote; US, FL, Remote; US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Remote/Applied-AI-Engineer_JR2018181-1",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.201776+00:00",
    "date_confidence": "high",
    "description": "NVIDIA's Silicon Co-Design Group is seeking an Applied AI Engineer to innovate, develop, and integrate innovative AI solutions into the design and automation infrastructure that po"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2020962",
    "title": "Senior Platform AI Engineer",
    "location": "US, CA, Santa Clara; US, CA, Remote",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Platform-AI-Engineer_JR2020962",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.201776+00:00",
    "date_confidence": "high",
    "description": "For over 25 years, NVIDIA has been revolutionizing computer graphics, PC gaming, and accelerated computing. It’s a unique legacy of innovation that’s fueled by great technology—and"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2025254",
    "title": "Senior Applied AI Engineer",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Applied-AI-Engineer_JR2025254-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:13.201776+00:00",
    "date_confidence": "high",
    "description": "NVIDIA is looking for a Senior Applied AI Engineer to help build intelligent software systems that improve engineering productivity and software quality at scale. In this role, you"
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
    "fetched_at": "2026-09-15T00:21:13.201776+00:00",
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
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 183 / 54.993s
- Company elapsed time: 79.484s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 158 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 18, 'fetched:new': 140}
- Raw jobs found: 425
- After US/location filtering: 158
- With trustworthy posted_date: 158
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.879, "first_pass_survivors": 75, "group": "official", "jds_resolved": 75, "original_postings_resolved": 75, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 75, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 4.882, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 3.203, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 10.929, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.325, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.162, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.275, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 4.602, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 10.458, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 1.163, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "software engineering mts", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 8}

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR359754",
    "title": "Principal Design Engineer, Mobile (iOS)",
    "location": "California - San Francisco; New York - New York",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Principal-Design-Engineer--Mobile--iOS-_JR359754-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:35.244722+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category User Experience Job"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR359460",
    "title": "Principal Data and AI Architect",
    "location": "Virginia - Mclean; New York - New York City Metro - Remote; District of Columbia - Washington; Indiana - Chicago Metro - Remote; California - San Francisco Metro - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Virginia---Mclean/Principal-Data-and-AI-Architect_JR359460",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:35.244722+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR359070",
    "title": "Manager, Software Engineering - Cloud Atlas",
    "location": "California - San Francisco; Washington - Seattle; Washington - Bellevue",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Manager--Software-Engineering---Cloud-Atlas_JR359070",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:35.244722+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR359178",
    "title": "Sr. Product Manager, Enterprise Security Technology",
    "location": "Washington - Bellevue",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Washington---Bellevue/Sr-Product-Manager--Enterprise-Security-Technology_JR359178-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:35.244722+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Product Job Details"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR359157",
    "title": "Senior Manager, Performance Analytics",
    "location": "Washington - Seattle; Illinois - Chicago; Massachusetts - Boston; Massachusetts - Burlington; Washington - Bellevue; Arizona - Phoenix; District of Columbia - Washington; California - Irvine; North Carolina - Raleigh; Indiana - Indianapolis; Arizona - Tempe; Texas - Dallas; Colorado - Denver; Georgia - Atlanta; Virginia - Mclean; Texas - Austin",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Washington---Seattle/Senior-Manager--Performance-Analytics_JR359157",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:35.244722+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Operations Job Deta"
  }
]
```

## Adobe

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://adobe.wd5.myworkdayjobs.com/external_experienced`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 284 / 123.830s
- Company elapsed time: 163.295s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 251 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 57, 'fetched:new': 194}
- Raw jobs found: 620
- After US/location filtering: 251
- With trustworthy posted_date: 251
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 42.613, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 13.263, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.556, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 35.816, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.387, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.576, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.656, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 4.509, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.323, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 4.604, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}

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
    "posted_date": "2026-08-06",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:38.702162+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are looking for a hands-on AI Agent Engineer to develop, build, and maintain intelligent agents that drive automation and business impact across the enterprise. "
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R171752",
    "title": "Sr. Applied AI Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Sr-Applied-AI-Engineer_R171752",
    "posted_date": "2026-09-09",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:38.702162+00:00",
    "date_confidence": "high",
    "description": "The Opportunity The GTM Agentic AI Operations team is leading the shift to an Agentic operating model for Adobe GTM and Sales. This function is the orchestration layer that operati"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R168433",
    "title": "Staff AI VFX Engineer",
    "location": "Los Angeles; San Francisco; San Jose; Seattle",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/Los-Angeles/Staff-AI-VFX-Engineer_R168433",
    "posted_date": "2026-05-20",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:38.702162+00:00",
    "date_confidence": "high",
    "description": "The Opportunity As AI rapidly transforms creative industries, professional production workflows must evolve alongside it. At Firefly Foundry , we’re leading an industry-first initi"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R168858",
    "title": "Senior Applied AI Engineer– Creative Systems & Brand Intelligence, Adobe Express",
    "location": "San Francisco; San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Francisco/Senior-Applied-AI-Engineer--Creative-Systems---Brand-Intelligence--Adobe-Express_R168858",
    "posted_date": "2026-07-23",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:38.702162+00:00",
    "date_confidence": "high",
    "description": "The Opportunity Our pillar, Assets and Collaboration, focuses on building foundational capabilities in Adobe Express that help users create, organize, govern, and collaborate on co"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170076",
    "title": "Principal AI Systems Engineer — C++ / Applied AI",
    "location": "San Jose; San Francisco; Seattle; New York; Chicago; Remote California",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Principal-AI-Systems-Engineer---C-----Applied-AI_R170076",
    "posted_date": "2026-06-23",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:38.702162+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are looking for a Principal AI Systems Engineer with deep C++ expertise to help build the next generation of AI-enabled product and platform capabilities. This r"
  }
]
```

## Meta

- Status: ok
- Scraping method: HTTP POST Meta Relay GraphQL; dynamic LSD and doc_id discovery
- Search URL/API: `https://www.metacareers.com/jobsearch/`
- Pagination: one complete Relay payload per role query
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 12 / 4.584s
- Company elapsed time: 5.522s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 1913
- After US/location filtering: 584
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.573, "first_pass_survivors": 340, "group": "official", "jds_resolved": 0, "original_postings_resolved": 340, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 428, "stop_reason": "page_budget", "unique_contribution": 340, "unique_jobs": 428}
- Query diagnostic: {"elapsed_seconds": 0.433, "first_pass_survivors": 19, "group": "official", "jds_resolved": 0, "original_postings_resolved": 19, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 0.481, "first_pass_survivors": 31, "group": "official", "jds_resolved": 0, "original_postings_resolved": 31, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 101, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 101}
- Query diagnostic: {"elapsed_seconds": 0.581, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 147, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 147}
- Query diagnostic: {"elapsed_seconds": 0.612, "first_pass_survivors": 130, "group": "official", "jds_resolved": 0, "original_postings_resolved": 130, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 506, "stop_reason": "page_budget", "unique_contribution": 130, "unique_jobs": 506}
- Query diagnostic: {"elapsed_seconds": 0.537, "first_pass_survivors": 24, "group": "official", "jds_resolved": 0, "original_postings_resolved": 24, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 302, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 302}
- Query diagnostic: {"elapsed_seconds": 0.343, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 0.43, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 0.56, "first_pass_survivors": 9, "group": "official", "jds_resolved": 0, "original_postings_resolved": 9, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 285, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 285}

Sample normalized records:

```json
[
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1420853345578936",
    "title": "Product Manager",
    "location": "Bellevue, WA; Redmond, WA; Austin, TX; Menlo Park, CA; Seattle, WA; Burlingame, CA; Washington, DC; New York, NY; San Francisco, CA",
    "official_url": "https://www.metacareers.com/jobs/1420853345578936",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:45.845743+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2883715245318000",
    "title": "Strategic Partner Manager, Connected TV",
    "location": "Menlo Park, CA; New York, NY; San Francisco, CA",
    "official_url": "https://www.metacareers.com/jobs/2883715245318000",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:45.845743+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1124065870041690",
    "title": "Software Engineer, SystemML - AI Networking",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/1124065870041690",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:45.845743+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2202484277812909",
    "title": "Research Scientist, Server Demand Forecasting",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/2202484277812909",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:45.845743+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2176819739360965",
    "title": "Production Engineering",
    "location": "Bellevue, WA; Menlo Park, CA; Boston, MA; New York, NY",
    "official_url": "https://www.metacareers.com/jobs/2176819739360965",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:45.845743+00:00",
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
- HTTP requests/cumulative request time: 26 / 23.980s
- Company elapsed time: 27.891s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 1236
- After US/location filtering: 716
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.687, "first_pass_survivors": 200, "group": "official", "jds_resolved": 200, "original_postings_resolved": 200, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 200, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 4.918, "first_pass_survivors": 132, "group": "official", "jds_resolved": 132, "original_postings_resolved": 132, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 132, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.407, "first_pass_survivors": 114, "group": "official", "jds_resolved": 114, "original_postings_resolved": 114, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 114, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.079, "first_pass_survivors": 81, "group": "official", "jds_resolved": 81, "original_postings_resolved": 81, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 81, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.597, "first_pass_survivors": 64, "group": "official", "jds_resolved": 64, "original_postings_resolved": 64, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 64, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.528, "first_pass_survivors": 62, "group": "official", "jds_resolved": 62, "original_postings_resolved": 62, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 62, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 1.443, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 86, "stop_reason": "early_stop", "unique_contribution": 19, "unique_jobs": 86}
- Query diagnostic: {"elapsed_seconds": 0.409, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 3.824, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 200}

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
    "fetched_at": "2026-09-15T00:21:51.369585+00:00",
    "date_confidence": "unknown",
    "description": "Our team focuses on the R&D of algorithm for TikTok international advertising customer growth. We leverage deep learning and large language model technologies to build an algorithm"
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
    "fetched_at": "2026-09-15T00:21:51.369585+00:00",
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
    "fetched_at": "2026-09-15T00:21:51.369585+00:00",
    "date_confidence": "unknown",
    "description": "TikTok is an international short video platform available in over 150 countries and regions, where we aim to inspire creativity and bring joy by helping people discover authentic a"
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
    "fetched_at": "2026-09-15T00:21:51.369585+00:00",
    "date_confidence": "unknown",
    "description": "The Commercial AI-CRM and Transaction team focuses on TikTok advertiser growth algorithms. Leveraging deep learning and large language model technologies, the team builds an algori"
  },
  {
    "company": "TikTok",
    "source": "tiktok_official_careers",
    "job_id": "7658191476207339829",
    "title": "Frontend Infrastructure Engineer (AI Tooling), TikTok Client Arch",
    "location": "San Jose, California, United States of America",
    "official_url": "https://lifeattiktok.com/search/7658191476207339829",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:21:51.369585+00:00",
    "date_confidence": "unknown",
    "description": "TikTok’s Web Architecture team is looking for a visionary Frontend Infrastructure Engineer (AI Tooling) to shape the future of AI-driven frontend engineering. You will work on the "
  }
]
```

## Uber

- Status: ok
- Scraping method: HTTP GET Oracle HCM recruitingCEJobRequisitions on iaziqy.fa.ocs.oraclecloud.com (offset pagination) + recruitingCEJobRequisitionDetails
- Search URL/API: `https://jobs.uber.com/en/jobs/?search=software%20engineer&page=1&pagesize=10`
- Pagination: HCM finder offset=(page-1)*limit ; limit=20; stop on empty/repeat or TotalJobsCount (do not stop at pages 1–7)
- Pages/requests fetched: 26
- HTTP requests/cumulative request time: 142 / 42.538s
- Company elapsed time: 62.104s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 116 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 5, 'fetched:new': 111}
- Raw jobs found: 472
- After US/location filtering: 116
- With trustworthy posted_date: 116
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 23.509, "first_pass_survivors": 61, "group": "official", "jds_resolved": 61, "original_postings_resolved": 61, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 66, "stop_reason": "page_budget", "unique_contribution": 61, "unique_jobs": 66}
- Query diagnostic: {"elapsed_seconds": 7.154, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.127, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 4.302, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 34, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 34}
- Query diagnostic: {"elapsed_seconds": 9.887, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.928, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.478, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.803, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 47, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 47}
- Query diagnostic: {"elapsed_seconds": 3.917, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 71, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 71}

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
    "fetched_at": "2026-09-15T00:22:19.261839+00:00",
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
    "fetched_at": "2026-09-15T00:22:19.261839+00:00",
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
    "fetched_at": "2026-09-15T00:22:19.261839+00:00",
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
    "fetched_at": "2026-09-15T00:22:19.261839+00:00",
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
    "fetched_at": "2026-09-15T00:22:19.261839+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.319s
- Company elapsed time: 1.612s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 454
- After US/location filtering: 452
- With trustworthy posted_date: 452
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7858932",
    "title": "Account Executive",
    "location": "Charlotte, NC; Raleigh, NC; Tampa, FL; Orlando, FL; Pittsburgh, PA; Richmond, VA; Jacksonville, FL; Columbus, OH; Dallas, TX; Houston, TX; Minneapolis, MN; Nashville, TN; Kansas City, MO; St. Louis, MO; Tempe, AZ; Indianapolis, IN; Oklahoma City, OK; New Orleans, LA; Charleston, SC; Atlanta, GA; Tempe",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7858932",
    "posted_date": "2026-04-27",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:54.729772+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8068432",
    "title": "Account Executive, Emerging Markets",
    "location": "Atlanta, GA; Tempe, AZ; Tampa, FL; Raleigh, NC; Nashville, TN; Las Vegas, NV; Dallas, TX; Houston, TX; Tempe",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8068432",
    "posted_date": "2026-07-15",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:54.729772+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8160362",
    "title": "Account Executive - Field Sales, New Verticals",
    "location": "New York, NY; Tempe",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8160362",
    "posted_date": "2026-08-26",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:54.729772+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:54.729772+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8114531",
    "title": "Account Manager, CPG Enterprise Ad Sales",
    "location": "Chicago, IL; Chicago",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8114531",
    "posted_date": "2026-08-10",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:54.729772+00:00",
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
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 114 / 40.034s
- Company elapsed time: 55.258s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 92 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 90}
- Raw jobs found: 322
- After US/location filtering: 92
- With trustworthy posted_date: 92
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 21.757, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 6.394, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 1.408, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 3.336, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 6.715, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.358, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.619, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.66, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 6.241, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 72, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 72}

Sample normalized records:

```json
[
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046467",
    "title": "Staff Machine Learning Engineer, Diffusion, Generative Modeling and Inference",
    "location": "Los Angeles, California; Seattle, Washington; Palo Alto, California; New York, New York; Bellevue, Washington",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Staff-Machine-Learning-Engineer--Generative-AI-Modeling-and-Inference_R0046467",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:56.342404+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0045781",
    "title": "Staff Software Engineer, Platform Engineering",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Staff-Software-Engineer--Platform-Engineering_R0045781-1",
    "posted_date": "2026-06-23",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:56.342404+00:00",
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
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:56.342404+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046622",
    "title": "Quality Engineer",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Quality-Engineer_R0046622-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:56.342404+00:00",
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
    "posted_date": "2026-07-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:56.342404+00:00",
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
- Company elapsed time: 0.474s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 181
- After US/location filtering: 135
- With trustworthy posted_date: 135
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:57.724605+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8089250",
    "title": "Client Account Manager I",
    "location": "Buenos Aires, AR; Argentina, AR",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8089250",
    "posted_date": "2026-07-28",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:57.724605+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:57.724605+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8130612",
    "title": "Client Account Manager II (tvScientific)",
    "location": "New York, NY, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8130612",
    "posted_date": "2026-09-11",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:57.724605+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "7908767",
    "title": "Content Designer II, Personalization",
    "location": "San Francisco, CA, US; Remote, US; San Francisco, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=7908767",
    "posted_date": "2026-08-26",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:22:57.724605+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.363s
- Company elapsed time: 0.596s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 361
- After US/location filtering: 272
- With trustworthy posted_date: 272
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
    "fetched_at": "2026-09-15T00:22:58.199036+00:00",
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
    "fetched_at": "2026-09-15T00:22:58.199036+00:00",
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
    "fetched_at": "2026-09-15T00:22:58.199036+00:00",
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
    "fetched_at": "2026-09-15T00:22:58.199036+00:00",
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
    "fetched_at": "2026-09-15T00:22:58.199036+00:00",
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
- Pages/requests fetched: 20
- HTTP requests/cumulative request time: 380 / 175.597s
- Company elapsed time: 222.432s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 360 / 0 / 0
- Detail cache statuses: {'fetched:new': 360}
- Raw jobs found: 1545
- After US/location filtering: 360
- With trustworthy posted_date: 360
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 152.243, "first_pass_survivors": 256, "group": "official", "jds_resolved": 256, "original_postings_resolved": 256, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 256, "stop_reason": "early_stop", "unique_contribution": 256, "unique_jobs": 256}
- Query diagnostic: {"elapsed_seconds": 0.445, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 86, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 86}
- Query diagnostic: {"elapsed_seconds": 9.362, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 154, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 154}
- Query diagnostic: {"elapsed_seconds": 51.923, "first_pass_survivors": 86, "group": "official", "jds_resolved": 86, "original_postings_resolved": 86, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 249, "stop_reason": "page_budget", "unique_contribution": 86, "unique_jobs": 249}
- Query diagnostic: {"elapsed_seconds": 1.731, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.955, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 254, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 254}
- Query diagnostic: {"elapsed_seconds": 0.44, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 48, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.418, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 50, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 50}
- Query diagnostic: {"elapsed_seconds": 2.914, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 208, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 208}

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074710",
    "title": "Director of Product Marketing",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000149461119-director-of-product-marketing",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:58.796023+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075355",
    "title": "Senior Director, Lifecycle & Customer Excellence Marketing",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000149459549-senior-director-lifecycle-customer-excellence-marketing-",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:58.796023+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075376",
    "title": "Senior Staff Product Manager, ServiceNow Cloud Platform",
    "location": "Kirkland, Washington, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000149457369-senior-staff-product-manager-servicenow-cloud-platform",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:58.796023+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075025",
    "title": "Director, AI Data & Analytics GTM",
    "location": "Austin, TEXAS, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000149456429-director-ai-data-analytics-gtm",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:58.796023+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074446",
    "title": "Process Optimization Specialist",
    "location": "West Palm Beach, Florida, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000149452669-process-optimization-specialist",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:22:58.796023+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  }
]
```

## LinkedIn

- Status: blocked
- Scraping method: linkedin_company
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 6 / 1.612s
- Company elapsed time: 2.668s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['LinkedIn company guest search blocked with HTTP 429']

## Bloomberg

- Status: ok
- Scraping method: HTTP GET Avature SearchJobs HTML + JobDetail HTML
- Search URL/API: `https://bloomberg.avature.net/careers/SearchJobs?q=software+engineer&jobRecordsPerPage=12&jobOffset=0`
- Pagination: jobOffset=0,12,... ; stop on empty/repeat or short page
- Pages/requests fetched: 29
- HTTP requests/cumulative request time: 49 / 57.089s
- Company elapsed time: 68.921s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 20 / 0 / 0
- Detail cache statuses: {'fetched:new': 20}
- Raw jobs found: 348
- After US/location filtering: 20
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 28.614, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 4.619, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.653, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.73, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.721, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.742, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.744, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.852, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 7.245, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 48}

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22103",
    "title": "Staff Accountant, Compensation Accounting",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Staff-Accountant-Compensation-Accounting/22103",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:23:24.035280+00:00",
    "date_confidence": "unknown",
    "description": "Staff Accountant, Compensation Accounting"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22100",
    "title": "BVAL (Bloomberg's Evaluated Pricing Service) Evaluator - US Agency Structured Products",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/BVAL-Bloomberg-s-Evaluated-Pricing-Service-Evaluator-US-Agency-Structured-Products/22100",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:23:24.035280+00:00",
    "date_confidence": "unknown",
    "description": "BVAL (Bloomberg's Evaluated Pricing Service) Evaluator - US Agency Structured Products"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22094",
    "title": "Team Leader - Entities",
    "location": "Princeton, New Jersey, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Team-Leader-Entities/22094",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:23:24.035280+00:00",
    "date_confidence": "unknown",
    "description": "Team Leader - Entities"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22086",
    "title": "Metals & Commodities Market Specialist, Specialist Sales - Financial Solutions",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Metals-Commodities-Market-Specialist-Specialist-Sales-Financial-Solutions/22086",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:23:24.035280+00:00",
    "date_confidence": "unknown",
    "description": "Metals & Commodities Market Specialist, Specialist Sales - Financial Solutions"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22081",
    "title": "HR Business Advisor, Engineering",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/HR-Business-Advisor-Engineering/22081",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:23:24.035280+00:00",
    "date_confidence": "unknown",
    "description": "HR Business Advisor, Engineering"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 59
- HTTP requests/cumulative request time: 580 / 92.115s
- Company elapsed time: 170.719s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 521 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 88, 'fetched:new': 432}
- Raw jobs found: 1174
- After US/location filtering: 520
- With trustworthy posted_date: 520
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 16.727, "first_pass_survivors": 55, "group": "official", "jds_resolved": 55, "original_postings_resolved": 55, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 55, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 12.96, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.794, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.701, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.226, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.162, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.754, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.501, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.835, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 10.368, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "full stack", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.691, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "python react", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.247, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "pyspark databricks", "raw_jobs": 54, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 6.786, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "experienced software engineer java python", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.731, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "agentic ai", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.363, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.828, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "software engineer ii", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.621, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.832, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "security engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 8.589, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "quantitative developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210751920",
    "title": "Sr Lead Software Engineer - Artificial Intelligence",
    "location": "Plano, TX, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210751920",
    "posted_date": "2026-07-27",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:23:51.601758+00:00",
    "date_confidence": "high",
    "description": "Build and operate the AI toolchain that is accelerating mainframe modernization at scale. As an Sr Lead Software Engineer within Core Processing, Wealth Management Technology, you "
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
    "fetched_at": "2026-09-15T00:23:51.601758+00:00",
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
    "fetched_at": "2026-09-15T00:23:51.601758+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorgan Chase, within the Co"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210786989",
    "title": "Principal Software Engineer - AI Foundations",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210786989",
    "posted_date": "2026-09-02",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:23:51.601758+00:00",
    "date_confidence": "high",
    "description": "As a Principal Software Engineer at JPMorganChase within the Chief Data and Analytics Office (CDAO), you provide expertise and engineering excellence as an integral part of an agil"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210780109",
    "title": "AI/ML Engineer - Senior Associate",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210780109",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:23:51.601758+00:00",
    "date_confidence": "high",
    "description": "JPMC is hiring to join the growing Asset and Wealth Management AI Engineering team. We are executing like a startup and building next-generation technology that combines JPMC uniqu"
  }
]
```

## Capital One

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://capitalone.wd12.myworkdayjobs.com/Capital_One`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 27
- HTTP requests/cumulative request time: 204 / 44.739s
- Company elapsed time: 73.279s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 176 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 3, 'fetched:new': 173}
- Raw jobs found: 529
- After US/location filtering: 176
- With trustworthy posted_date: 176
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 27.367, "first_pass_survivors": 74, "group": "official", "jds_resolved": 74, "original_postings_resolved": 74, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 74, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 9.273, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.088, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.7, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.148, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.142, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.521, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.766, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 2.978, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R249443",
    "title": "Senior Manager, Software Engineering, Full Stack",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Manager--Software-Engineering--Full-Stack_R249443-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:24:21.998087+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Software Engineering, Full Stack Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collab"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R241036",
    "title": "Staff Engineer - Agentic AI (Remote-Eligible)",
    "location": "McLean, VA; US Remote; Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Distinguished-Engineer_R241036-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:24:21.998087+00:00",
    "date_confidence": "high",
    "description": "Staff Engineer - Agentic AI (Remote-Eligible) As a Staff Engineer at Capital One, you will be a part of a community of technical experts working to define the future of banking in "
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R246324",
    "title": "Manager, Product Management - Enterprise Data",
    "location": "McLean, VA; New York, NY; Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Manager--Product-Management---Enterprise-Data_R246324-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:24:21.998087+00:00",
    "date_confidence": "high",
    "description": "Manager, Product Management - Enterprise Data Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, finding value creation opportu"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R247941",
    "title": "Lead Software Engineer, Enterprise Platform (Marketing Technology)",
    "location": "McLean, VA; Chicago, IL; Plano, TX; Riverwoods, IL",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Lead-Software-Engineer--Enterprise-Platform--Marketing-Technology-_R247941-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:24:21.998087+00:00",
    "date_confidence": "high",
    "description": "Lead Software Engineer, Enterprise Platform (Marketing Technology) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a "
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R249356",
    "title": "Senior Manager, Product Manager - Controls & Process Automation",
    "location": "McLean, VA; New York, NY; Wilmington, DE",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Manager--Product-Manager---Controls---Process-Automation_R249356",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:24:21.998087+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Product Manager - Controls & Process Automation Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, finding valu"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 41
- HTTP requests/cumulative request time: 522 / 103.238s
- Company elapsed time: 173.420s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 481 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 24, 'fetched:new': 457}
- Raw jobs found: 814
- After US/location filtering: 481
- With trustworthy posted_date: 481
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 24.601, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 76, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 12.898, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.226, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 57, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 12.863, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.979, "first_pass_survivors": 49, "group": "official", "jds_resolved": 49, "original_postings_resolved": 49, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 49, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.363, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.532, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.146, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 14.223, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 19.928, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 3, "pages_fetched": 3, "query": "core infrastructure", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.33, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "cleared site reliability engineer database", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.397, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "software developer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 11.933, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "applications developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "343962",
    "title": "AI Systems Engineer (OCI/AI Infrastructure)",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/343962",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:24:32.957052+00:00",
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
    "fetched_at": "2026-09-15T00:24:32.957052+00:00",
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
    "posted_date": "2026-06-10",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:24:32.957052+00:00",
    "date_confidence": "high",
    "description": "You will work at the intersection of distributed systems, networking, and AI infrastructure, driving architecture, design, implementation, and performance optimization across softw"
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
    "fetched_at": "2026-09-15T00:24:32.957052+00:00",
    "date_confidence": "high",
    "description": "As a Senior Software Engineer within Oracle Cloud Infrastructure (OCI), you’ll have the opportunity to solve large-scale, mission-critical engineering challenges with broad technic"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "343790",
    "title": "Senior Manager - AI Network Engineering",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/343790",
    "posted_date": "2026-09-01",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:24:32.957052+00:00",
    "date_confidence": "high",
    "description": "Manage a team that designs, develops, troubleshoots and debugs software programs for databases, applications, tools, networks etc. Lead the end-to-end NPI lifecycle for current and"
  }
]
```

## Walmart Global Tech

- Status: blocked
- Scraping method: walmart
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 2 / 1.110s
- Company elapsed time: 1.111s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Walmart hybrid search HTTP 520']

## Cloudflare

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/cloudflare/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.272s
- Company elapsed time: 1.126s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 356
- After US/location filtering: 352
- With trustworthy posted_date: 352
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
    "updated_date": "2026-09-04",
    "fetched_at": "2026-09-15T00:25:36.389064+00:00",
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
    "updated_date": "2026-09-04",
    "fetched_at": "2026-09-15T00:25:36.389064+00:00",
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
    "updated_date": "2026-09-04",
    "fetched_at": "2026-09-15T00:25:36.389064+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "8152697",
    "title": "Associate Solutions Engineer - Beijing",
    "location": "Hybrid; Beijing Shi, China",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/8152697?gh_jid=8152697",
    "posted_date": "2026-08-25",
    "updated_date": "2026-09-08",
    "fetched_at": "2026-09-15T00:25:36.389064+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "8084358",
    "title": "Business Development Manager",
    "location": "Hybrid; Austin, TX, United States; New York, New York, United States",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/8084358?gh_jid=8084358",
    "posted_date": "2026-07-28",
    "updated_date": "2026-09-04",
    "fetched_at": "2026-09-15T00:25:36.389064+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.274s
- Company elapsed time: 0.778s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 632
- After US/location filtering: 371
- With trustworthy posted_date: 371
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
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:25:37.515715+00:00",
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
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:25:37.515715+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p><span style=\"font-weight: 400;\">Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s la"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "7532733",
    "title": "Account Executive, AI Sales",
    "location": "San Francisco, CA; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=7532733",
    "posted_date": "2026-02-03",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:25:37.515715+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies - from the world’s largest enterprises to the most "
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8130725",
    "title": "Account Executive, AI Startups (Hunter)",
    "location": "San Francisco; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8130725",
    "posted_date": "2026-08-19",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:25:37.515715+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p><span style=\"font-weight: 400;\">Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s la"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8077887",
    "title": "Account Executive, Bridge",
    "location": "SF, NYC, SEA, CHI; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8077887",
    "posted_date": "2026-07-22",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:25:37.515715+00:00",
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
- HTTP requests/cumulative request time: 1 / 7.288s
- Company elapsed time: 7.647s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 216
- After US/location filtering: 179
- With trustworthy posted_date: 179
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
    "updated_date": "2026-09-08",
    "fetched_at": "2026-09-15T00:25:38.295040+00:00",
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
    "updated_date": "2026-08-28",
    "fetched_at": "2026-09-15T00:25:38.295040+00:00",
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
    "fetched_at": "2026-09-15T00:25:38.295040+00:00",
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
    "updated_date": "2026-08-03",
    "fetched_at": "2026-09-15T00:25:38.295040+00:00",
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
    "fetched_at": "2026-09-15T00:25:38.295040+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.135s
- Company elapsed time: 0.450s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 154
- After US/location filtering: 143
- With trustworthy posted_date: 143
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8198153",
    "title": "Accounting Intern (Summer 2027)",
    "location": "New York, NY",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8198153?t=gh_src=&gh_jid=8198153",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:45.942881+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8114351",
    "title": "Account Maintenance Associate",
    "location": "Clearwater, FL",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8114351?t=gh_src=&gh_jid=8114351",
    "posted_date": "2026-08-07",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-09-15T00:25:45.942881+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8162157",
    "title": "AML Investigator",
    "location": "Denver, CO; New York, NY; Westlake, TX; Denver, CO; New York, NY; Westlake, TX",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8162157?t=gh_src=&gh_jid=8162157",
    "posted_date": "2026-09-03",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:45.942881+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-09-15T00:25:45.942881+00:00",
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
    "updated_date": "2026-09-12",
    "fetched_at": "2026-09-15T00:25:45.942881+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.145s
- Company elapsed time: 0.356s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 158
- After US/location filtering: 99
- With trustworthy posted_date: 99
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
    "fetched_at": "2026-09-15T00:25:46.394429+00:00",
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
    "fetched_at": "2026-09-15T00:25:46.394429+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Figma is growing our team of passionate creatives and builders on a mission to make design accessible to all. Figma’s platform helps teams bring ideas"
  },
  {
    "company": "Figma",
    "source": "figma_official_careers",
    "job_id": "6163045004",
    "title": "Account Executive, Federal - Federal Systems Integrators",
    "location": "San Francisco, CA • New York, NY • United States; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/6163045004?gh_jid=6163045004",
    "posted_date": "2026-08-31",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-09-15T00:25:46.394429+00:00",
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
    "fetched_at": "2026-09-15T00:25:46.394429+00:00",
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
    "fetched_at": "2026-09-15T00:25:46.394429+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.168s
- Company elapsed time: 0.515s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 223
- After US/location filtering: 125
- With trustworthy posted_date: 125
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:46.751389+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:46.751389+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8631068002",
    "title": "Area Vice President - Financial Services",
    "location": "Remote, US; United States of America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8631068002",
    "posted_date": "2026-07-15",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:46.751389+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:46.751389+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8532274002",
    "title": "Business Development Representative",
    "location": "Remote, EMEA; Remote, Germany; Remote, Ireland; Remote, Netherlands; Remote, United Kingdom",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8532274002",
    "posted_date": "2026-05-01",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:46.751389+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.108s
- Company elapsed time: 0.179s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 44
- After US/location filtering: 44
- With trustworthy posted_date: 44
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8686353002",
    "title": "Advertising Operations Manager",
    "location": "San Francisco Bay Area or New York (Remote); New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8686353002",
    "posted_date": "2026-08-06",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:25:47.269029+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8571766002",
    "title": "Director of Engineering, Safety",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8571766002",
    "posted_date": "2026-05-29",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:25:47.269029+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8722538002",
    "title": "Engineering Manager, Machine Learning (Safety)",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8722538002",
    "posted_date": "2026-08-20",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:25:47.269029+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8537955002",
    "title": "Engineering Manager, Notifications",
    "location": "Remote; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8537955002",
    "posted_date": "2026-05-11",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:25:47.269029+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8649856002",
    "title": "Engineering Manager, Platform Security",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8649856002",
    "posted_date": "2026-07-27",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:25:47.269029+00:00",
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
- Company elapsed time: 0.306s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 101
- After US/location filtering: 76
- With trustworthy posted_date: 76
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
    "updated_date": "2026-09-01",
    "fetched_at": "2026-09-15T00:25:47.449474+00:00",
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
    "updated_date": "2026-09-01",
    "fetched_at": "2026-09-15T00:25:47.449474+00:00",
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
    "updated_date": "2026-09-04",
    "fetched_at": "2026-09-15T00:25:47.449474+00:00",
    "date_confidence": "high",
    "description": "<p id=\"p-rc_10838ec6a95bc2d4-72\" data-path-to-node=\"3\"><span data-path-to-node=\"3,0\">We are looking for a detail-oriented, strategic team player to join as a Benefits Manager on As"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8120432",
    "title": "Brand Designer",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://www.asana.com/jobs/apply/8120432?gh_jid=8120432",
    "posted_date": "2026-09-01",
    "updated_date": "2026-09-04",
    "fetched_at": "2026-09-15T00:25:47.449474+00:00",
    "date_confidence": "high",
    "description": "<p>The Asana Marketing team is responsible for fueling business growth and building a brand customers love. We create campaigns and content to attract new accounts and inspire curr"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8052235",
    "title": "Chief of Staff",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://www.asana.com/jobs/apply/8052235?gh_jid=8052235",
    "posted_date": "2026-07-21",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:47.449474+00:00",
    "date_confidence": "high",
    "description": "<p>As Chief of Staff to the Chief Product Officer, you will be a force multiplier for Asana's product leadership team. This role helps the CPO run a high-functioning organization b"
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
- Company elapsed time: 0.577s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 269
- After US/location filtering: 264
- With trustworthy posted_date: 264
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8686667002",
    "title": "Account Executive, Small Business",
    "location": "San Francisco, California, United States; New York, New York, United States; Salt Lake City, Utah, United States",
    "official_url": "https://www.brex.com/careers/8686667002?gh_jid=8686667002",
    "posted_date": "2026-08-06",
    "updated_date": "2026-08-19",
    "fetched_at": "2026-09-15T00:25:47.756346+00:00",
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
    "updated_date": "2026-08-19",
    "fetched_at": "2026-09-15T00:25:47.756346+00:00",
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
    "updated_date": "2026-08-19",
    "fetched_at": "2026-09-15T00:25:47.756346+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8721806002",
    "title": "Account Executive, YC",
    "location": "San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8721806002?gh_jid=8721806002",
    "posted_date": "2026-08-17",
    "updated_date": "2026-08-19",
    "fetched_at": "2026-09-15T00:25:47.756346+00:00",
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
    "fetched_at": "2026-09-15T00:25:47.756346+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.185s
- Company elapsed time: 0.801s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 264
- After US/location filtering: 221
- With trustworthy posted_date: 221
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:48.334159+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:48.334159+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:48.334159+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:48.334159+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:25:48.334159+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.136s
- Company elapsed time: 0.326s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 182
- After US/location filtering: 101
- With trustworthy posted_date: 101
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8791500002",
    "title": "Account Manager, Automotive Vertical",
    "location": "San Francisco, CA; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8791500002?gh_jid=8791500002",
    "posted_date": "2026-09-10",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:25:49.136590+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8792050002",
    "title": "Account Manager, Automotive Vertical",
    "location": "New York, NY; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8792050002?gh_jid=8792050002",
    "posted_date": "2026-09-10",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:25:49.136590+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8503985002",
    "title": "Analytics Lead, Market Insights",
    "location": "San Francisco, CA; California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8503985002?gh_jid=8503985002",
    "posted_date": "2026-04-14",
    "updated_date": "2026-09-04",
    "fetched_at": "2026-09-15T00:25:49.136590+00:00",
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
    "fetched_at": "2026-09-15T00:25:49.136590+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8779945002",
    "title": "Associate Counsel, Employment",
    "location": "Nashville, TN; Nashville, Tennessee, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8779945002?gh_jid=8779945002",
    "posted_date": "2026-09-02",
    "updated_date": "2026-09-04",
    "fetched_at": "2026-09-15T00:25:49.136590+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.464s
- Company elapsed time: 0.532s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 71
- After US/location filtering: 56
- With trustworthy posted_date: 56
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
    "fetched_at": "2026-09-15T00:25:49.465918+00:00",
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
    "fetched_at": "2026-09-15T00:25:49.465918+00:00",
    "date_confidence": "high",
    "description": "Maintain positive partnerships across artist and label communities within Vietnam. Support our key partners in Vietnam on Spotify tools, resources and insights. Work closely with o"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "973b0b71-e8d2-4d7d-9c4b-1c716bd45c8b",
    "title": "Business Development Senior Manager, APAC",
    "location": "Singapore; Seoul",
    "official_url": "https://jobs.lever.co/spotify/973b0b71-e8d2-4d7d-9c4b-1c716bd45c8b",
    "posted_date": "2026-01-15",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:25:49.465918+00:00",
    "date_confidence": "high",
    "description": "Identify, structure, negotiate, amend, close, and manage strategic distribution partnerships across APAC that advance Spotify’s growth and long‑term vision. Develop and refine part"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "29b0056f-f163-4728-a32a-214bcb3232e8",
    "title": "C++ Engineer - Experience",
    "location": "Stockholm; London",
    "official_url": "https://jobs.lever.co/spotify/29b0056f-f163-4728-a32a-214bcb3232e8",
    "posted_date": "2026-09-04",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:25:49.465918+00:00",
    "date_confidence": "high",
    "description": "Contribute to and maintain Spotify’s Desktop C++ application across macOS and Windows. Develop native container capabilities that enable UI teams to build new experiences and take "
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "0b8ea4d4-57ee-49c1-a57f-9a37248ee24f",
    "title": "Creative Lead - Visual Merchandising",
    "location": "London; Stockholm",
    "official_url": "https://jobs.lever.co/spotify/0b8ea4d4-57ee-49c1-a57f-9a37248ee24f",
    "posted_date": "2026-07-06",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:25:49.465918+00:00",
    "date_confidence": "high",
    "description": "Define and evolve Spotify's global visual merchandising vision, setting the creative direction for artwork, visual systems, and brand expression across the Spotify experience. Lead"
  }
]
```

## Ramp

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/ramp`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.141s
- Company elapsed time: 0.290s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 145
- After US/location filtering: 129
- With trustworthy posted_date: 129
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
    "fetched_at": "2026-09-15T00:25:49.998864+00:00",
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
    "fetched_at": "2026-09-15T00:25:49.998864+00:00",
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
    "fetched_at": "2026-09-15T00:25:49.998864+00:00",
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
    "fetched_at": "2026-09-15T00:25:49.998864+00:00",
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
    "fetched_at": "2026-09-15T00:25:49.998864+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.140s
- Company elapsed time: 0.218s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 126
- After US/location filtering: 74
- With trustworthy posted_date: 74
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
    "fetched_at": "2026-09-15T00:25:50.288378+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.288378+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.288378+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.288378+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.288378+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.197s
- Company elapsed time: 0.219s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
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
    "fetched_at": "2026-09-15T00:25:50.507408+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.507408+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.507408+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.507408+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.507408+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.135s
- Company elapsed time: 0.253s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 144
- After US/location filtering: 120
- With trustworthy posted_date: 120
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
    "fetched_at": "2026-09-15T00:25:50.727041+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.727041+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.727041+00:00",
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
    "fetched_at": "2026-09-15T00:25:50.727041+00:00",
    "date_confidence": "high",
    "description": "Who are we? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
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
    "fetched_at": "2026-09-15T00:25:50.727041+00:00",
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
- Pages/requests fetched: 13
- HTTP requests/cumulative request time: 37 / 10.294s
- Company elapsed time: 13.159s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 23 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 8, 'fetched:new': 15}
- Raw jobs found: 99
- After US/location filtering: 23
- With trustworthy posted_date: 23
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.001, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 20, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 0.186, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.204, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.317, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.626, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 0.292, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.284, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.267, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.29, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.248, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack backend", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.533, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.215, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer collaboration devices", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.264, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "splunk engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2022480",
    "title": "Senior Software Engineer, Control Plane (Go) - Hypershield",
    "location": "San Jose, California, US; Remote - North Dakota, USA; Remote - Montana, USA; Remote - Maine, USA; Remote - Ohio, USA; Remote - Nebraska, USA; Remote - Louisiana, USA; Remote - Texas, USA; Remote - Nevada, USA; Remote - Hawaii, USA; Remote - Georgia, USA; Remote - Mississippi, USA; Remote - Connecticut, USA; Remote - Colorado, USA; Remote - Wyoming, USA; Remote - Wisconsin, USA; Remote - West Virginia, USA; Remote - Maryland, USA; Remote - California, USA; Remote - Vermont, USA; Remote - New York, USA; Remote - New Jersey, USA; Remote - Arkansas, USA; Remote - South Dakota, USA; Remote - Pennsylvania, USA; Remote - Michigan, USA; Remote - Indiana, USA; Remote - Idaho, USA; Remote - Arizona, USA; Remote - New Mexico, USA; Remote - New Hampshire, USA; Remote - Kentucky, USA; Remote - Alabama, USA; Remote - South Carolina, USA; Remote - Illinois, USA; Remote - Missouri, USA; Remote - Massachusetts, USA; Remote - Iowa, USA; Remote - Tennessee, USA; Remote - North Carolina, USA; Remote - Minnesota, USA; Remote - Kansas, USA; Remote - Alaska, USA; Remote - Rhode Island, USA; Remote - Delaware, USA; RTP, North Carolina, US; Remote - Washington, USA; Remote - Virginia, USA; Remote - Utah, USA; Remote - Oregon, USA; Remote - Florida, USA; Remote - Oklahoma, USA",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Senior-Software-Engineer--Control-Plane--Go----Hypershield_2022480",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:25:50.980701+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/15/2026 Note: This is a remote U.S. based role, requiring work within the Pacific Time Zone. Meet the Team Join Cisco’s Cisco Hyp"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2023832",
    "title": "Leader, Solutions Engineer, Splunk",
    "location": "RTP, North Carolina, US; Remote - North Carolina, USA; Remote - New York, USA; Remote - New Jersey, USA; Remote - Virginia, USA; Remote - Florida, USA; Remote - Maryland, USA; Remote - Massachusetts, USA; Remote - Rhode Island, USA; Remote - Connecticut, USA; Remote - South Carolina, USA",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/RTP-North-Carolina-US/Leader--Solutions-Engineer--Splunk_2023832",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:25:50.980701+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/15/2026 This role can be performed remote within the East Coast Must be authorized to work in the United States; this position do"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2020044",
    "title": "Leader, Sales, Splunk - PBST - USAF",
    "location": "Remote - Virginia, USA; Remote - Colorado, USA; Remote - Texas, USA; Remote - Georgia, USA; Remote - West Virginia, USA; Remote - Florida, USA; Remote - Maryland, USA; Remote - Pennsylvania, USA; Remote - Delaware, USA",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Remote---Virginia-USA/Leader--Sales--Splunk---US-Military-Defense_2020044-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:25:50.980701+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/29/2026 This role can be performed remotely from: MD, DC, VA, NC, FL, TX, CO, PA or DE Your impact: Federal Sales Leaders are at "
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2016949",
    "title": "Solutions Engineer - Charlotte, NC",
    "location": "Remote - North Carolina, USA",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Remote---North-Carolina-USA/Solutions-Engineer_2016949",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:25:50.980701+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/15/2026 The application window is expected to close on: 09/16/2026 Job posting may be removed earlier if the position is filled o"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2024417",
    "title": "Account Executive - Splunk - Air Force",
    "location": "Remote - Florida, USA; Remote - Colorado, USA; Remote - Maryland, USA; Remote - Texas, USA; Remote - Virginia, USA; Remote - Delaware, USA",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Remote---Florida-USA/Account-Executive---Splunk---Air-Force_2024417-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:25:50.980701+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/29/2026 The application window is expected to close on: 09/10/2026 Meet the Team We are the front line of security within the Dep"
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 186 / 66.246s
- Company elapsed time: 100.751s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 154 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 10, 'fetched:new': 144}
- Raw jobs found: 800
- After US/location filtering: 154
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 54.22, "first_pass_survivors": 100, "group": "official", "jds_resolved": 100, "original_postings_resolved": 100, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 100, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 5.727, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 12.51, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 13.226, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.008, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.083, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.567, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.08, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.818, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 3.509, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "cloud developer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 75}

Sample normalized records:

```json
[
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1421516633",
    "title": "Forward Deployed Senior AI Engineer",
    "location": "New York, NY, US, 10001",
    "official_url": "https://jobs.sap.com/job/New-York-Forward-Deployed-Senior-AI-Engineer-NY-10001/1421516633/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:04.140889+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1422592533",
    "title": "Head Engineering - SAP Business Network Core",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://jobs.sap.com/job/Palo-Alto-Head-Engineering-SAP-Business-Network-Core-CA-94304/1422592533/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:04.140889+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1409064033",
    "title": "Machine Learning Engineer",
    "location": "Bellevue, WA, US, 98004",
    "official_url": "https://jobs.sap.com/job/Bellevue-Machine-Learning-Engineer-WA-98004/1409064033/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:04.140889+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1422581433",
    "title": "Forward Deployed Application/ ML Principal Engineer",
    "location": "New York, NY, US, 10001",
    "official_url": "https://jobs.sap.com/job/New-York-Forward-Deployed-Application-ML-Principal-Engineer-NY-10001/1422581433/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:04.140889+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1431261533",
    "title": "Principal Data & Applied Scientist - Ontologies & Semantics",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://jobs.sap.com/job/Palo-Alto-Principal-Data-&-Applied-Scientist-Ontologies-&-Semantics-CA-94304/1431261533/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:04.140889+00:00",
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
- Pages/requests fetched: 25
- HTTP requests/cumulative request time: 241 / 114.884s
- Company elapsed time: 148.063s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 215 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 52, 'fetched:new': 163}
- Raw jobs found: 463
- After US/location filtering: 215
- With trustworthy posted_date: 215
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 49.73, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 18.357, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 1.454, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 21.185, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.739, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.621, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.071, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.921, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 11.478, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 80}

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
    "fetched_at": "2026-09-15T00:26:21.175976+00:00",
    "date_confidence": "high",
    "description": "Senior AI Engineer Developer This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enterprise is"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1209447",
    "title": "Senior AI Engineer Developer",
    "location": "Spring, Texas, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Spring-Texas-United-States-of-America/Senior-AI-Engineer-Developer_1209447-2",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:21.175976+00:00",
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
    "fetched_at": "2026-09-15T00:26:21.175976+00:00",
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
    "fetched_at": "2026-09-15T00:26:21.175976+00:00",
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
    "fetched_at": "2026-09-15T00:26:21.175976+00:00",
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
- HTTP requests/cumulative request time: 27 / 16.347s
- Company elapsed time: 23.567s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 270
- After US/location filtering: 124
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.762, "first_pass_survivors": 29, "group": "official", "jds_resolved": 0, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 2.712, "first_pass_survivors": 16, "group": "official", "jds_resolved": 0, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.55, "first_pass_survivors": 20, "group": "official", "jds_resolved": 0, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.397, "first_pass_survivors": 17, "group": "official", "jds_resolved": 0, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 3.098, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.496, "first_pass_survivors": 14, "group": "official", "jds_resolved": 0, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.488, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.748, "first_pass_survivors": 9, "group": "official", "jds_resolved": 0, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.317, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10156962",
    "title": "Senior AI / Data Engineer",
    "location": "Celebration, Florida",
    "official_url": "https://www.disneycareers.com/en/job/celebration/senior-ai-data-engineer/391/98814483936",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:41.229127+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10146000",
    "title": "Lead Software Engineer - AI Assisted Engineering Practices",
    "location": "Celebration, Florida",
    "official_url": "https://www.disneycareers.com/en/job/celebration/lead-software-engineer-ai-assisted-engineering-practices/391/94498288272",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:41.229127+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10157759",
    "title": "Lead Software Engineer - AI and Observability",
    "location": "New York, New York / Glendale, California",
    "official_url": "https://www.disneycareers.com/en/job/new-york/lead-software-engineer-ai-and-observability/391/99405820704",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:41.229127+00:00",
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
    "fetched_at": "2026-09-15T00:26:41.229127+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10159627",
    "title": "Senior Manager, Product Software Engineering - Foundations Engineering",
    "location": "Glendale, California / San Francisco, California",
    "official_url": "https://www.disneycareers.com/en/job/glendale/senior-manager-product-software-engineering-foundations-engineering/391/100143638208",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:41.229127+00:00",
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
- HTTP requests/cumulative request time: 75 / 59.302s
- Company elapsed time: 69.325s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 56 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 7, 'fetched:new': 49}
- Raw jobs found: 255
- After US/location filtering: 56
- With trustworthy posted_date: 56
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 50.888, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 0.767, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 0.72, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 3.787, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 4.779, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 54, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 3.125, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 54, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 2.857, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 54, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 0.787, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.731, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 18}

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
    "fetched_at": "2026-09-15T00:26:42.322477+00:00",
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
    "fetched_at": "2026-09-15T00:26:42.322477+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0073001",
    "title": "Director, AI Transformation",
    "location": "San Jose; Portland; Austin",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/San-Jose/Director--AI-Change-Enablement_R0073001",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:42.322477+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0076311",
    "title": "Detection & Response Engineer",
    "location": "Austin",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Austin/Detection---Response-Engineer_R0076311",
    "posted_date": "2026-09-09",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:42.322477+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0076856",
    "title": "Software Engineer 2",
    "location": "Portland",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Portland/Software-Engineer-2_R0076856",
    "posted_date": "2026-09-10",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:26:42.322477+00:00",
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
- HTTP requests/cumulative request time: 156 / 41.667s
- Company elapsed time: 64.133s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 129 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 21, 'fetched:new': 108}
- Raw jobs found: 258
- After US/location filtering: 129
- With trustworthy posted_date: 129
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 12.225, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.502, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.184, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 9.762, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.775, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.313, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.484, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.93, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.584, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3096530",
    "title": "Machine Learning Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721085768",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:04.797038+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Machine Learning Engineering General Summary: As a leading technology innovator, Qualcomm push"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3096521",
    "title": "Senior AI Application Development Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721085177",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:04.797038+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Software Engineering General Summary: This individual independently plans, performs the modera"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3096546",
    "title": "Staff Embedded Software Development Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721086329",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:04.797038+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Software Engineering General Summary: This individual leads, plans, synthesizes ambiguous or c"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3096537",
    "title": "Senior Machine Learning Software Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721085855",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:04.797038+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Machine Learning Engineering General Summary: This individual independently plans, performs th"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3096348",
    "title": "SOC Power Architect",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721063472",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:04.797038+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > ASICS Engineering General Summary: As a leading technology innovator, Qualcomm pushes the boun"
  }
]
```

## AMD

- Status: ok
- Scraping method: HTTP GET public Jibe/iCIMS jobs JSON
- Search URL/API: `https://careers.amd.com/api/jobs`
- Pagination: page=1,2,... per role query; stop on total/empty/repeat/short page
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 14 / 12.271s
- Company elapsed time: 13.913s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 1243
- After US/location filtering: 470
- With trustworthy posted_date: 470
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.974, "first_pass_survivors": 328, "group": "official", "jds_resolved": 328, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 328, "stop_reason": "page_budget", "unique_contribution": 328, "unique_jobs": 328}
- Query diagnostic: {"elapsed_seconds": 0.683, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning", "raw_jobs": 84, "stop_reason": "early_stop", "unique_contribution": 20, "unique_jobs": 84}
- Query diagnostic: {"elapsed_seconds": 3.157, "first_pass_survivors": 78, "group": "official", "jds_resolved": 78, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 78, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 3.032, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "AI research", "raw_jobs": 231, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 231}
- Query diagnostic: {"elapsed_seconds": 3.066, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 300}

Sample normalized records:

```json
[
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "88610",
    "title": "Fellow Software Engineer — AI Performance & Reliability",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-07-30",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:27:26.378456+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology can change lives for the better. It can heal us, entertain us, and make us more connected, productive, and und"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "86806",
    "title": "Security Software Engineer",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-06-17",
    "updated_date": "2026-09-12",
    "fetched_at": "2026-09-15T00:27:26.378456+00:00",
    "date_confidence": "high",
    "description": "WHAT YOU DO AT AMD CHANGES EVERYTHING At AMD, our mission is to build great products that accelerate next-generation computing experiences—from AI and data centers, to PCs, gaming "
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "90723",
    "title": "Principal Software Developer – AI/ML Performance Validation & Systems Testing",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-08-18",
    "updated_date": "2026-09-12",
    "fetched_at": "2026-09-15T00:27:26.378456+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "90795",
    "title": "Software Engineer, Devops Platform Engineering",
    "location": "Longmont, Colorado",
    "official_url": "",
    "posted_date": "2026-08-20",
    "updated_date": "2026-09-12",
    "fetched_at": "2026-09-15T00:27:26.378456+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "91374",
    "title": "FPGA/SoC Embedded Cybersecurity Engineer",
    "location": "Austin, Texas",
    "official_url": "",
    "posted_date": "2026-09-10",
    "updated_date": "2026-09-12",
    "fetched_at": "2026-09-15T00:27:26.378456+00:00",
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
- HTTP requests/cumulative request time: 63 / 22.367s
- Company elapsed time: 30.715s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 43 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 22, 'fetched:new': 21}
- Raw jobs found: 189
- After US/location filtering: 43
- With trustworthy posted_date: 43
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 12.744, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 28, "stop_reason": "early_stop", "unique_contribution": 28, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 1.178, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 0.446, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 5.349, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 4.599, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 2.172, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 0.454, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.447, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.048, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 28, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 28}

Sample normalized records:

```json
[
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19609",
    "title": "Account Executive - State & Local Government",
    "location": "Remote (TX)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--TX/Account-Executive---State---Local-Government_R19609-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:40.292704+00:00",
    "date_confidence": "high",
    "description": "About the Role The Zoom Public Sector Team seeks an Account Executive to sell the Zoom Workplace platform to State & Local Government accounts in Texas, Oklahoma, Louisiana and Ark"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19648",
    "title": "Contact Center - Consulting Solutions Engineer",
    "location": "Remote (MS)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--MS/Contact-Center---Consulting-Solutions-Engineer_R19648-1",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:40.292704+00:00",
    "date_confidence": "high",
    "description": "About the Team The Contact Center Solutions Engineer designs, implements, and optimizes solutions to meet organizational and customer needs. They collaborate with cross-functional "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19526",
    "title": "Senior Product Manager",
    "location": "Remote (US)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Remote--US/Senior-Product-Manager_R19526-1",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:40.292704+00:00",
    "date_confidence": "high",
    "description": "What you can expect We're hiring a Product Manager to own Common Room's integrations and data-sync surface. This is the capabilities customers trust with their most critical GTM da"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19646",
    "title": "Software Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Software-Engineer_R19646-1",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:40.292704+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect In this role, you will design and ship AI-powered features within Zoom's Workforce Engagement Management (WEM) platform, directly improving how enterprise organ"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19357",
    "title": "Software Development Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Software-Development-Engineer_R19357-1",
    "posted_date": "2026-09-10",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:40.292704+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect Join the Zoom Contact Center engineering team at a genuinely exciting moment: we are building an AI-powered analytics engine that acts as a virtual data analyst"
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
- HTTP requests/cumulative request time: 1 / 0.231s
- Company elapsed time: 0.660s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 327
- After US/location filtering: 192
- With trustworthy posted_date: 192
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8157796",
    "title": "Account Executive, Commercial (Alaska)",
    "location": "Remote, Alaska; Alaska, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8157796",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-09-15T00:27:44.893070+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8069472",
    "title": "Account Executive, Commercial (Pittsburgh)",
    "location": "Remote, Pennsylvania; Pennsylvania, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8069472",
    "posted_date": "2026-07-20",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:27:44.893070+00:00",
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
    "updated_date": "2026-08-24",
    "fetched_at": "2026-09-15T00:27:44.893070+00:00",
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
    "fetched_at": "2026-09-15T00:27:44.893070+00:00",
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
    "fetched_at": "2026-09-15T00:27:44.893070+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.314s
- Company elapsed time: 1.525s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 893
- After US/location filtering: 493
- With trustworthy posted_date: 493
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
    "updated_date": "2026-08-18",
    "fetched_at": "2026-09-15T00:27:45.553991+00:00",
    "date_confidence": "high",
    "description": "<p class=\"p1\">As we continue to increase our presence in the world of Unified Data Analytics and AI, we're looking for a creative, driven, and execution-oriented Enterprise Account"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8546367002",
    "title": "AI Engineer - FDE (Forward Deployed Engineer)",
    "location": "United States; Remote - California",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8546367002",
    "posted_date": "2026-05-13",
    "updated_date": "2026-09-02",
    "fetched_at": "2026-09-15T00:27:45.553991+00:00",
    "date_confidence": "high",
    "description": "<p><strong>AI Engineer - FDE (Forward Deployed Engineer) (ALL LEVELS)</strong></p> <p><strong>CSQ327R177</strong></p> <p><strong>Mission</strong></p> <p>The AI Forward Deployed Eng"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8760167002",
    "title": "AI Engineer - FDE (Forward Deployed Engineer) - U.S. Federal Sector",
    "location": "Maryland; Virginia; Washington, D.C.; Remote - Washington D.C.",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8760167002",
    "posted_date": "2026-08-28",
    "updated_date": "2026-09-02",
    "fetched_at": "2026-09-15T00:27:45.553991+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-09-15T00:27:45.553991+00:00",
    "date_confidence": "high",
    "description": "<p data-renderer-start-pos=\"1648\">With the most complete data &amp; AI stack on the market, Databricks is well suited to be the strategic partner for our customers’ AI transformati"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8632401002",
    "title": "Alliance RVP, Boston Consulting Group (BCG)",
    "location": "Atlanta, Georgia; Boston, Massachusetts; Chicago, Illinois; Dallas, Texas; New York City, New York; San Francisco, California; Seattle, Washington; San Francisco, California",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8632401002",
    "posted_date": "2026-07-15",
    "updated_date": "2026-09-02",
    "fetched_at": "2026-09-15T00:27:45.553991+00:00",
    "date_confidence": "high",
    "description": "<p data-pm-slice=\"1 1 []\">SLSQ327R469</p> <p data-renderer-start-pos=\"1846\">While candidates in the listed locations are encouraged for this role, we are open to remote candidates "
  }
]
```

## Roblox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roblox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.148s
- Company elapsed time: 0.511s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 236
- After US/location filtering: 219
- With trustworthy posted_date: 219
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "7350081",
    "title": "[2026] Senior Machine Learning Engineer, Recommendation Systems - PhD Early Career",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/7350081?gh_jid=7350081",
    "posted_date": "2025-10-27",
    "updated_date": "2026-08-17",
    "fetched_at": "2026-09-15T00:27:47.080706+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8027588",
    "title": "[2026] Senior Machine Learning Engineer (Systems), Embodied AI/NPCs, ML Platform - PhD Early Career",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8027588?gh_jid=8027588",
    "posted_date": "2026-06-30",
    "updated_date": "2026-08-17",
    "fetched_at": "2026-09-15T00:27:47.080706+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8027587",
    "title": "[2026] Senior Machine Learning Engineer (Systems), Embodied AI/NPCs, ML Platform - PhD Early Career",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8027587?gh_jid=8027587",
    "posted_date": "2026-06-30",
    "updated_date": "2026-08-17",
    "fetched_at": "2026-09-15T00:27:47.080706+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:27:47.080706+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:27:47.080706+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.154s
- Company elapsed time: 0.384s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 164
- After US/location filtering: 89
- With trustworthy posted_date: 89
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "7839229",
    "title": "Community Support Forecasting and Demand Planning Analyst",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/7839229?gh_jid=7839229",
    "posted_date": "2026-04-24",
    "updated_date": "2026-04-24",
    "fetched_at": "2026-09-15T00:27:47.596170+00:00",
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
    "updated_date": "2026-08-24",
    "fetched_at": "2026-09-15T00:27:47.596170+00:00",
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
    "updated_date": "2026-08-24",
    "fetched_at": "2026-09-15T00:27:47.596170+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8152132",
    "title": "Gestionnaire des réclamations complexes",
    "location": "Canada; United States",
    "official_url": "https://careers.airbnb.com/positions/8152132?gh_jid=8152132",
    "posted_date": "2026-08-24",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-09-15T00:27:47.596170+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8070656",
    "title": "Growth Marketing Lead, SEM",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8070656?gh_jid=8070656",
    "posted_date": "2026-07-22",
    "updated_date": "2026-08-05",
    "fetched_at": "2026-09-15T00:27:47.596170+00:00",
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
- Company elapsed time: 1.698s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 593
- After US/location filtering: 480
- With trustworthy posted_date: 480
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
    "fetched_at": "2026-09-15T00:27:47.981348+00:00",
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
    "fetched_at": "2026-09-15T00:27:47.981348+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5205545008",
    "title": "Accounting, Revenue Internal Controls",
    "location": "San Francisco, CA | Seattle, WA; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5205545008",
    "posted_date": "2026-08-20",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-09-15T00:27:47.981348+00:00",
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
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:27:47.981348+00:00",
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
    "fetched_at": "2026-09-15T00:27:47.981348+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.121s
- Company elapsed time: 0.194s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 34
- After US/location filtering: 25
- With trustworthy posted_date: 25
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4700129006",
    "title": "Agency Growth Lead",
    "location": "Los Angeles/Santa Monica, CA; Remote - United States",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4700129006?gh_jid=4700129006",
    "posted_date": "2026-07-28",
    "updated_date": "2026-09-09",
    "fetched_at": "2026-09-15T00:27:49.680394+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4705316006",
    "title": "Agency Growth Lead",
    "location": "Toronto; Remote - United States",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4705316006?gh_jid=4705316006",
    "posted_date": "2026-08-14",
    "updated_date": "2026-09-09",
    "fetched_at": "2026-09-15T00:27:49.680394+00:00",
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
    "fetched_at": "2026-09-15T00:27:49.680394+00:00",
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
    "updated_date": "2026-09-09",
    "fetched_at": "2026-09-15T00:27:49.680394+00:00",
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
    "fetched_at": "2026-09-15T00:27:49.680394+00:00",
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
- HTTP requests/cumulative request time: 24 / 28.823s
- Company elapsed time: 32.183s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 1065
- After US/location filtering: 448
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 6.199, "first_pass_survivors": 145, "group": "official", "jds_resolved": 145, "original_postings_resolved": 145, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 145, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.907, "first_pass_survivors": 104, "group": "official", "jds_resolved": 104, "original_postings_resolved": 104, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 104, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.539, "first_pass_survivors": 56, "group": "official", "jds_resolved": 56, "original_postings_resolved": 56, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 106, "stop_reason": "page_budget", "unique_contribution": 56, "unique_jobs": 106}
- Query diagnostic: {"elapsed_seconds": 4.905, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.509, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.742, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.194, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 56, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 0.858, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 3.331, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 150}

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
    "fetched_at": "2026-09-15T00:27:49.876127+00:00",
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
    "fetched_at": "2026-09-15T00:27:49.876127+00:00",
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
    "fetched_at": "2026-09-15T00:27:49.876127+00:00",
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
    "fetched_at": "2026-09-15T00:27:49.876127+00:00",
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
    "fetched_at": "2026-09-15T00:27:49.876127+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.130s
- Company elapsed time: 0.342s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 70
- After US/location filtering: 70
- With trustworthy posted_date: 70
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8684363002",
    "title": "Associate Creative Director, Growth Marketing",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8684363002?gh_jid=8684363002",
    "posted_date": "2026-08-26",
    "updated_date": "2026-09-09",
    "fetched_at": "2026-09-15T00:27:51.648081+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the Role</strong></h2> <p>As our Performance Creative Program expands, we're looking for an experienced Associate Creative Director to guide a team of designers, "
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8656772002",
    "title": "Chief of Staff, Head of Legal Ops",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8656772002?gh_jid=8656772002",
    "posted_date": "2026-08-03",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:27:51.648081+00:00",
    "date_confidence": "high",
    "description": "<h2>About the Role</h2> <p>We are hiring a Chief of Staff / Head of Legal Operations to join our growing Legal team. This role sits at the intersection of executive strategy and le"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8792463002",
    "title": "Creative Director, Brand",
    "location": "New York, NY, USA; San Francisco, CA, USA; New York Office",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8792463002?gh_jid=8792463002",
    "posted_date": "2026-09-09",
    "updated_date": "2026-09-09",
    "fetched_at": "2026-09-15T00:27:51.648081+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role</h2> <p>Chime is looking for a Creative Director to shape what our brand looks, sounds and feels like — and to turn that into work people actually talk about.</p"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8564916002",
    "title": "CX Partner Manager",
    "location": "Remote, USA; Remote - US",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8564916002?gh_jid=8564916002",
    "posted_date": "2026-05-29",
    "updated_date": "2026-09-09",
    "fetched_at": "2026-09-15T00:27:51.648081+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\"><strong>About the role</strong></span></h2> <p><span style=\"font-family: helvetica, arial, sans-serif;\">We are hiring a"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8586430002",
    "title": "Data Scientist, Growth Product",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8586430002?gh_jid=8586430002",
    "posted_date": "2026-06-10",
    "updated_date": "2026-09-09",
    "fetched_at": "2026-09-15T00:27:51.648081+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\"><strong>About the role</strong></span></h2> <p class=\"p2\">We're looking for a Growth Product Scientist to partner with "
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
- HTTP requests/cumulative request time: 125 / 26.972s
- Company elapsed time: 44.980s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 101 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 11, 'fetched:new': 90}
- Raw jobs found: 472
- After US/location filtering: 101
- With trustworthy posted_date: 101
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 9.376, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 5.086, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 0.658, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 10.177, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.635, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.726, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 5.897, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.203, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 38, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 3.221, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "295521",
    "title": "Senior Principal Software Engineer - (Modernization, Automation & AI)",
    "location": "Round Rock, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/295521",
    "posted_date": "2026-09-05",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:51.990768+00:00",
    "date_confidence": "high",
    "description": "Senior ServiceNow Developer (Modernization, Automation & AI) Be a part of a team that’s ensuring Dell Technologies' product integrity and customer satisfaction. Our IT Software Eng"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "299006",
    "title": "Senior Principal Mechanical Engineer, Custom AI Infrastructure Solutions",
    "location": "Round Rock, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/299006",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:51.990768+00:00",
    "date_confidence": "high",
    "description": "Infrastructure Solutions Group (ISG) builds the products that power infrastructure, solutions, and data management our customers need most. Our teams design and develop the hardwar"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "298379",
    "title": "AI Development & Agent Ops-Software Senior Engineer",
    "location": "Hopkinton, MA, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/298379",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:51.990768+00:00",
    "date_confidence": "high",
    "description": "AI Development & Agent Ops — Senior Software Engineer Why This Role This is not a support role. Dell's AI Development & Agents Ops organization is operating at the frontier of what"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "295587",
    "title": "AI Development & Agent Ops — Principal Software Engineer",
    "location": "Hopkinton, MA, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/295587",
    "posted_date": "2026-09-09",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:51.990768+00:00",
    "date_confidence": "high",
    "description": "AI Development & Agent Ops — Principal Software Engineer Why This Role This is not a support role. Dell's AI Development & Agents Ops organization is operating at the frontier of w"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "294077",
    "title": "Senior Software Engineer - Data Protection Software Engineering (C, C++)",
    "location": "Santa Clara, CA, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/294077",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:27:51.990768+00:00",
    "date_confidence": "high",
    "description": "Senior Software Engineer - Data Protection Software Engineering (C, C++) Infrastructure Solutions Group (ISG) builds the products that power infrastructure, solutions, and data man"
  }
]
```

## Dropbox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/dropbox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.140s
- Company elapsed time: 0.239s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 39
- After US/location filtering: 31
- With trustworthy posted_date: 31
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
    "fetched_at": "2026-09-15T00:28:08.931595+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z95gas6hz75zjz77zz90zpz71zz80zeoz80zz68zlz66z"
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
    "fetched_at": "2026-09-15T00:28:08.931595+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qowz80zsz81z8nqz122zdfz68z5coz87zsz73zz76zipqu3z86zmz88zz81zcth"
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
    "fetched_at": "2026-09-15T00:28:08.931595+00:00",
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
    "fetched_at": "2026-09-15T00:28:08.931595+00:00",
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
    "fetched_at": "2026-09-15T00:28:08.931595+00:00",
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
- HTTP requests/cumulative request time: 77 / 21.859s
- Company elapsed time: 32.589s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 56 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 12, 'fetched:new': 44}
- Raw jobs found: 370
- After US/location filtering: 56
- With trustworthy posted_date: 56
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 16.208, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.926, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.295, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 4.955, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 1.707, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.127, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.686, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.279, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.405, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 55, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 55}

Sample normalized records:

```json
[
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109789",
    "title": "Director of Product Management, Advertiser Experience",
    "location": "Washington - Seattle Campus; Austin Domain 11 - HomeAway; USA - Illinois - Chicago; USA - California - San Jose",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Director-of-Product-Management--Advertiser-Experience_R-109789",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:09.171349+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-108283",
    "title": "Full Stack Software Engineer II",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Full-Stack-Software-Engineer-II_R-108283-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:09.171349+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-108695",
    "title": "Senior Software Development Engineer",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Senior-Software-Development-Engineer_R-108695-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:09.171349+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109511",
    "title": "Economist III",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Economist-III_R-109511-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:09.171349+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-108423",
    "title": "Forward Deployed AI Engineer III",
    "location": "Austin Domain 11 - HomeAway",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Austin-Domain-11---HomeAway/Enterprise-AI-Engineer-III_R-108423-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:09.171349+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.253s
- Company elapsed time: 0.361s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 140
- After US/location filtering: 32
- With trustworthy posted_date: 32
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
    "updated_date": "2026-09-02",
    "fetched_at": "2026-09-15T00:28:11.009104+00:00",
    "date_confidence": "high",
    "description": "<h3>Our Mission: Helping Millions of Organizations Grow Better</h3> <h3>Team Overview</h3> <p>Our Enterprise Sales team drives growth by connecting large organizations (500–5,000 e"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "5990225",
    "title": "Account Executive - Small Business",
    "location": "Remote - USA; Cambridge, MA, USA",
    "official_url": "https://www.hubspot.com/careers/jobs/5990225?gh_jid=5990225",
    "posted_date": "2024-06-07",
    "updated_date": "2026-09-02",
    "fetched_at": "2026-09-15T00:28:11.009104+00:00",
    "date_confidence": "high",
    "description": "<p><strong>***Now accepting applications for an October 6th, 2026 start date***</strong></p> <p>&nbsp;</p> <p>As a Small Business Account Executive at HubSpot, you will&nbsp;<stron"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8097687",
    "title": "Internal Partner Enablement Lead",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8097687?gh_jid=8097687",
    "posted_date": "2026-09-02",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:28:11.009104+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-26231</strong></p> <hr> <p><span style=\"font-size: 14pt;\"><strong>Internal Partner Enablement Lead</strong></span></p> <p><strong>About the Role</strong></p> <p>We'r"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8060346",
    "title": "Lead Account Executive, Sales Specialization",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8060346?gh_jid=8060346",
    "posted_date": "2026-07-15",
    "updated_date": "2026-09-02",
    "fetched_at": "2026-09-15T00:28:11.009104+00:00",
    "date_confidence": "high",
    "description": "<p>This is a hunter role with deep product specialization serving HubSpot’s Corporate segment. You build your own pipeline by prospecting aggressively into HubSpot's existing custo"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8128853",
    "title": "Manager, Analytics Engineering, Data & AI Foundations",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8128853?gh_jid=8128853",
    "posted_date": "2026-08-26",
    "updated_date": "2026-09-02",
    "fetched_at": "2026-09-15T00:28:11.009104+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.111s
- Company elapsed time: 0.301s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 102
- After US/location filtering: 87
- With trustworthy posted_date: 87
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "7144697",
    "title": "Activation Sales Development Representative I",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=7144697",
    "posted_date": "2025-08-07",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-09-15T00:28:11.371636+00:00",
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
    "fetched_at": "2026-09-15T00:28:11.371636+00:00",
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
    "fetched_at": "2026-09-15T00:28:11.371636+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8157774",
    "title": "Bilingual Customer Experience Specialist",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8157774",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-09-15T00:28:11.371636+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "8163246",
    "title": "Director, Compensation",
    "location": "United States - Remote; Remote - United States",
    "official_url": "https://instacart.careers/job/?gh_jid=8163246",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-09-15T00:28:11.371636+00:00",
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
- Pages/requests fetched: 25
- HTTP requests/cumulative request time: 170 / 89.707s
- Company elapsed time: 113.374s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 144 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 23, 'fetched:new': 121}
- Raw jobs found: 485
- After US/location filtering: 144
- With trustworthy posted_date: 144
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 28.224, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 12.162, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.263, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 14.525, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 15.188, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.636, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 16.709, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 1.009, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 6.567, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 78}

Sample normalized records:

```json
[
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0285206",
    "title": "AI Frameworks Engineer",
    "location": "US, California, Santa Clara; US, Texas, Austin; US, Oregon, Hillsboro",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-California-Santa-Clara/AI-Frameworks-Engineer_JR0285206-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:11.673669+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Join Intel's AI Frameworks PyTorch team to shape the future of Artificial Intelligence (AI) and High-Performance Computing (HPC). As an AI Frameworks "
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0286629",
    "title": "AI Solutions Engineering Undergraduate Intern",
    "location": "US, Oregon, Hillsboro",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/AI-Solutions-Engineering-Undergraduate-Intern_JR0286629",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:11.673669+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Supports the development of integrated AI solutions through AI domain expertise in assisting in system design, performance benchmarking, and deploymen"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0281978",
    "title": "AI Performance Library Architect",
    "location": "US, Oregon, Hillsboro; US, California, Folsom",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/AI-Performance-Library-Architect_JR0281978-1",
    "posted_date": "2026-03-27",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:11.673669+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Software and AI (SAI) organization is looking for a software development engineer to work on oneDNN project ( https://github.com/uxlfoundation/oneDNN "
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
    "fetched_at": "2026-09-15T00:28:11.673669+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel Foundry Automation - Data Analytics and Process Group is seeking a motivated and technically curious intern to join our Manufacturing Automation"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0286415",
    "title": "Physical AI Solutions Architect",
    "location": "US, Oregon, Hillsboro; US, California, Folsom; US, California, Santa Clara; US, Arizona, Phoenix",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/Physical-AI-Solutions-Architect_JR0286415",
    "posted_date": "2026-09-04",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:11.673669+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: The Role and Impact Intel is seeking an experienced Physical AI Solutions Architect to help accelerate adoption of Intel technologies across the rapid"
  }
]
```

## MathWorks

- Status: ok
- Scraping method: HTTP GET server-rendered MathWorks search + JobPosting JSON-LD
- Search URL/API: `https://www.mathworks.com/company/jobs/opportunities/search/`
- Pagination: page=2,3,... after the unnumbered first page; stop on empty/repeat/short page
- Pages/requests fetched: 10
- HTTP requests/cumulative request time: 45 / 20.729s
- Company elapsed time: 22.222s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 35 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 88
- After US/location filtering: 35
- With trustworthy posted_date: 34
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 6.634, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 2.082, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.24, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 2.982, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 4.103, "first_pass_survivors": 7, "group": "official", "jds_resolved": 6, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 1.353, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.469, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.468, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.89, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 23, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 23}

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
    "fetched_at": "2026-09-15T00:28:22.060099+00:00",
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
    "fetched_at": "2026-09-15T00:28:22.060099+00:00",
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
    "fetched_at": "2026-09-15T00:28:22.060099+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37334",
    "title": "Sr. Product Marketing Engineer - Agentic AI",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37334-sr-product-marketing-engineer-agentic-ai?keywords=ai+engineer",
    "posted_date": "2026-07-07",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:22.060099+00:00",
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
    "fetched_at": "2026-09-15T00:28:22.060099+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.187s
- Company elapsed time: 0.683s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 403
- After US/location filtering: 247
- With trustworthy posted_date: 247
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
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:28:36.971761+00:00",
    "date_confidence": "high",
    "description": "<p>An Account Development Representative at MongoDB is the starting point for building a serious career in technology sales.&nbsp;</p> <p>This role is the foundation of our sales o"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "8079914",
    "title": "Account Development Representative - English Speaking",
    "location": "Kuala Lumpur; MYS_KualaLumpur",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=8079914",
    "posted_date": "2026-07-23",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:28:36.971761+00:00",
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
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:28:36.971761+00:00",
    "date_confidence": "high",
    "description": "<p>At MongoDB, our Account Development team works closely with our partners in both Sales and Marketing to build fanatical customer enthusiasm around MongoDB. ADR reps are responsi"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "6531094",
    "title": "Account Executive, Growth",
    "location": "São Paulo; São Paulo, São Paulo, Brazil",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=6531094",
    "posted_date": "2026-04-30",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:28:36.971761+00:00",
    "date_confidence": "high",
    "description": "<p>MongoDB is always developing and innovating — not only in our technology, but also in our sales go-to-market strategy. Our sales leadership is committed to building the best sal"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7217822",
    "title": "Account Executive, Growth",
    "location": "Zurich; Zürich, Zürich, Switzerland",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7217822",
    "posted_date": "2025-10-07",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:28:36.971761+00:00",
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
- HTTP requests/cumulative request time: 132 / 35.291s
- Company elapsed time: 53.818s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 107 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 10, 'fetched:new': 97}
- Raw jobs found: 225
- After US/location filtering: 107
- With trustworthy posted_date: 107
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.098, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 9.834, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.755, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 6.288, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 4.375, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.769, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 10.682, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 0.772, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.909, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR041639",
    "title": "Software Engineer - Backend",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549799423962",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:37.657566+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR037517",
    "title": "Product Owner Crypto - Assistant Vice President",
    "location": "Purchase, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549797802584",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:37.657566+00:00",
    "date_confidence": "high",
    "description": "Product Owner Crypto - Assistant Vice President Purchase, New York Company Profile: Morgan Stanley is a leading global financial services firm providing a wide range of investment "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR038723",
    "title": "Lead Software Engineer - Parametric",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549798138380",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:37.657566+00:00",
    "date_confidence": "high",
    "description": "ABOUT MORGAN STANLEY Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, wealth management and investment managemen"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR035754",
    "title": "Associate, Platforms - EquityZen",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549797480189",
    "posted_date": "2026-09-10",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:37.657566+00:00",
    "date_confidence": "high",
    "description": "Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment management and wealth management services. The Firm’"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR043099",
    "title": "Third Party Risk & Site Management, Director",
    "location": "Dallas, Texas, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800101040",
    "posted_date": "2026-09-10",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:37.657566+00:00",
    "date_confidence": "high",
    "description": "We're seeking someone to join our team as Third Party Risk & Site Management - Director (AVP equivalent) to manage the day to day operations, infrastructure oversight, audits, and "
  }
]
```

## NetApp

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.netapp.com/en/search-jobs`
- Pagination: p=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 29
- HTTP requests/cumulative request time: 119 / 41.850s
- Company elapsed time: 60.730s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 90 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 435
- After US/location filtering: 90
- With trustworthy posted_date: 90
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 24.362, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.91, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 5.628, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 6.544, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.89, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 5.541, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.865, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.8, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.189, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "98734011664",
    "title": "Principal Engineer, AI BU",
    "location": "San Jose, California, United States; Morrisville, North Carolina, United States; United States",
    "official_url": "https://careers.netapp.com/en/job/san-jose/principal-engineer-ai-bu/27600/98734011664",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:41.761368+00:00",
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
    "fetched_at": "2026-09-15T00:28:41.761368+00:00",
    "date_confidence": "high",
    "description": "Job Summary Distinguished Engineer - AI Infrastructure We are seeking a Distinguished Engineer with unrivaled depth in AI/ML inferencing at scale and the distributed systems founda"
  },
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "98734013184",
    "title": "Senior Engineer, AI BU",
    "location": "San Jose, California, United States; United States; Morrisville, North Carolina, United States",
    "official_url": "https://careers.netapp.com/en/job/san-jose/senior-engineer-ai-bu/27600/98734013184",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:41.761368+00:00",
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
    "fetched_at": "2026-09-15T00:28:41.761368+00:00",
    "date_confidence": "high",
    "description": "Executive Summary We are looking for an innovative Director of Engineering – AI Solutions for Developer Productivity to transform how our software engineers build, test, and deploy"
  },
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "98424409296",
    "title": "Talent Acquisition AI Operations Specialist",
    "location": "San Jose, California, United States; Morrisville, North Carolina, United States",
    "official_url": "https://careers.netapp.com/en/job/san-jose/talent-acquisition-ai-operations-specialist/27600/98424409296",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:41.761368+00:00",
    "date_confidence": "high",
    "description": "Job Summary We are looking for a Mid-Level AI Solutions Developer to join our Talent Acquisition team as a Talent Acquisition AI Operations Specialist . This is a unique, hybrid te"
  }
]
```

## Netflix

- Status: ok
- Scraping method: HTTP GET Eightfold server HTML + embedded smartApplyData positions
- Search URL/API: `https://explore.jobs.netflix.net/careers`
- Pagination: first 10 embedded positions per focused role query; PCSX remains disabled
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 9 / 2.901s
- Company elapsed time: 3.912s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 90
- After US/location filtering: 58
- With trustworthy posted_date: 58
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.473, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.395, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.44, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.38, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.4, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.379, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.588, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.396, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.462, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}

Sample normalized records:

```json
[
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "AJRT30201",
    "title": "AI Engineer 6 - AI Foundation & Tooling, Ads Platform",
    "location": "USA - Remote",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790298014263",
    "posted_date": "2024-07-23",
    "updated_date": "2026-09-15",
    "fetched_at": "2026-09-15T00:28:44.282799+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR42022",
    "title": "AI Research Engineer 6 - TL, Algo Core - AI for Member Systems",
    "location": "USA - Remote",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790317717814",
    "posted_date": "2026-08-08",
    "updated_date": "2026-08-08",
    "fetched_at": "2026-09-15T00:28:44.282799+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR41100",
    "title": "Software Engineer 5 – Agent Platform, AI Platform",
    "location": "USA - Remote",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790316292023",
    "posted_date": "2026-06-09",
    "updated_date": "2026-06-09",
    "fetched_at": "2026-09-15T00:28:44.282799+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR40898",
    "title": "Software Engineer 4/5 – Model Development and Management, AI Platform",
    "location": "USA - Remote",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790316165312",
    "posted_date": "2026-06-01",
    "updated_date": "2026-06-01",
    "fetched_at": "2026-09-15T00:28:44.282799+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR31056",
    "title": "Software Engineer 4/5 – Model Serving Systems, AI Platform",
    "location": "USA - Remote",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790300350307",
    "posted_date": "2025-01-09",
    "updated_date": "2026-01-01",
    "fetched_at": "2026-09-15T00:28:44.282799+00:00",
    "date_confidence": "high",
    "description": ""
  }
]
```

## OpenAI

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/openai`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.563s
- Company elapsed time: 1.270s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 803
- After US/location filtering: 668
- With trustworthy posted_date: 668
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
    "fetched_at": "2026-09-15T00:28:48.195906+00:00",
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
    "fetched_at": "2026-09-15T00:28:48.195906+00:00",
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
    "fetched_at": "2026-09-15T00:28:48.195906+00:00",
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
    "fetched_at": "2026-09-15T00:28:48.195906+00:00",
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
    "fetched_at": "2026-09-15T00:28:48.195906+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.826s
- Company elapsed time: 1.069s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 314
- After US/location filtering: 244
- With trustworthy posted_date: 244
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
    "fetched_at": "2026-09-15T00:28:49.246171+00:00",
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
    "fetched_at": "2026-09-15T00:28:49.246171+00:00",
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
    "fetched_at": "2026-09-15T00:28:49.246171+00:00",
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
    "fetched_at": "2026-09-15T00:28:49.246171+00:00",
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
    "fetched_at": "2026-09-15T00:28:49.246171+00:00",
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
- Pages/requests fetched: 18
- HTTP requests/cumulative request time: 59 / 17.426s
- Company elapsed time: 25.249s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 40 / 0 / 0
- Detail cache statuses: {'fetched:new': 40}
- Raw jobs found: 143
- After US/location filtering: 40
- With trustworthy posted_date: 40
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.336, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 19, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 1.533, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.059, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 3.61, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 5.007, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 29, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 2.793, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 0.75, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.226, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.55, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137732",
    "title": "Staff Machine Learning Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922370282",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:49.467380+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137727",
    "title": "Staff Software Engineer",
    "location": "Austin, Texas, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922370095",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:49.467380+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0134436",
    "title": "Staff Software Engineer - BE Python",
    "location": "San Jose, California, United States of America; Austin, Texas, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274917627800",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:49.467380+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137563",
    "title": "Staff Product Security AI Engineer",
    "location": "Austin, Texas, United States of America; Chicago, Illinois, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922353695",
    "posted_date": "2026-09-10",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:49.467380+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0134448",
    "title": "Senior Software Engineer - Python",
    "location": "San Jose, California, United States of America; Austin, Texas, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274917627749",
    "posted_date": "2026-09-10",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:49.467380+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.143s
- Company elapsed time: 0.438s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 149
- After US/location filtering: 131
- With trustworthy posted_date: 131
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:28:50.315936+00:00",
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
    "updated_date": "2026-06-01",
    "fetched_at": "2026-09-15T00:28:50.315936+00:00",
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
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:28:50.315936+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8148431",
    "title": "Backend Software Engineer, PDP Experience",
    "location": "Remote - United States; San Francisco, CA, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8148431",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-09-15T00:28:50.315936+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8113265",
    "title": "Client Account Manager, Large Customer Sales (CPG)",
    "location": "Chicago, IL; New York City, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8113265",
    "posted_date": "2026-08-11",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:28:50.315936+00:00",
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
- HTTP requests/cumulative request time: 60 / 23.034s
- Company elapsed time: 29.742s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 46 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 9, 'fetched:new': 37}
- Raw jobs found: 102
- After US/location filtering: 46
- With trustworthy posted_date: 46
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 6.679, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.476, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.788, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 16.691, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 37, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 37}
- Query diagnostic: {"elapsed_seconds": 0.422, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.787, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.413, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.652, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.287, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 23, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 23}

Sample normalized records:

```json
[
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059027",
    "title": "Global Telco Specialist Solution Architect - Lightwell",
    "location": "Boston; Remote US VA; Remote US SC; Remote US NC; Remote US TX; Remote US FL; Remote US CA; Remote US GA",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Boston/Global-Telco-Specialist-Solution-Architect---Lightwell_R-059027-2",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:50.755786+00:00",
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
    "fetched_at": "2026-09-15T00:28:50.755786+00:00",
    "date_confidence": "high",
    "description": "About the role: The Red Hat Global Technology Sales team is looking for a Global Lightwell Leader to join our team. This leadership position is responsible for the quality and exec"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-058807",
    "title": "OpenShift Sales Specialist – Carolinas Region",
    "location": "Raleigh; Remote US FL; Charlotte - MSO",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Raleigh/OpenShift-Sales-Specialist---Carolinas-Region_R-058807-1",
    "posted_date": "2026-09-09",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:50.755786+00:00",
    "date_confidence": "high",
    "description": "About the Role This role is designed for a strategic dealmaker with an application developer's mindset. It requires technical acumen and the ability to build and drive comprehensiv"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059526",
    "title": "Technical Product Intern",
    "location": "Raleigh; Boston; Durham",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Raleigh/Technical-Product-Intern_R-059526-1",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:50.755786+00:00",
    "date_confidence": "high",
    "description": "About the Role Do you love learning how technology works and then figuring out the best way to explain its value to others? As a Technical Product Intern, you'll get hands-on exper"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059060",
    "title": "Product Manager Intern",
    "location": "Raleigh; Boston",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Raleigh/Product-Manager-Intern_R-059060",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:28:50.755786+00:00",
    "date_confidence": "high",
    "description": "Job Summary At Red Hat, our interns are an integral part of the team. They don’t get relegated to busywork or unimportant tasks, but participate in the day-to-day work and are acti"
  }
]
```

## Roku

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roku/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.173s
- Company elapsed time: 0.748s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 255
- After US/location filtering: 192
- With trustworthy posted_date: 192
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8109578",
    "title": "Account Coordinator",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8109578?gh_jid=8109578",
    "posted_date": "2026-08-06",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:29:14.718006+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8077965",
    "title": "Account Executive",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8077965?gh_jid=8077965",
    "posted_date": "2026-07-22",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:29:14.718006+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:29:14.718006+00:00",
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
    "updated_date": "2026-08-19",
    "fetched_at": "2026-09-15T00:29:14.718006+00:00",
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
    "updated_date": "2026-08-24",
    "fetched_at": "2026-09-15T00:29:14.718006+00:00",
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
- Company elapsed time: 0.699s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 208
- After US/location filtering: 192
- With trustworthy posted_date: 192
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
    "updated_date": "2026-08-28",
    "fetched_at": "2026-09-15T00:29:15.467559+00:00",
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
    "updated_date": "2026-08-28",
    "fetched_at": "2026-09-15T00:29:15.467559+00:00",
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
    "updated_date": "2026-08-28",
    "fetched_at": "2026-09-15T00:29:15.467559+00:00",
    "date_confidence": "high",
    "description": "<p>Since we opened our doors in 2009, the world of commerce has evolved immensely, and so has Square. After enabling anyone to take payments and never miss a sale, we saw sellers s"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5108007008",
    "title": "Applied Research Intern, Proactive Intelligence & Customer World Models (PhD / Graduate Co-op)",
    "location": "Bay Area, CA, United States of America; CA - ON - Toronto - Remote",
    "official_url": "http://block.xyz/careers/jobs/5108007008?gh_jid=5108007008",
    "posted_date": "2026-06-09",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-09-15T00:29:15.467559+00:00",
    "date_confidence": "high",
    "description": "<p><strong>Team:</strong> Apollo — Block Applied R&amp;D<br><strong>Location:</strong> Remote (US / Canada)<br><strong>Duration:</strong> Fall/Winter 2026 co-op — 8 months, flexibl"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5422288008",
    "title": "B2B Marketing Manager, Content & Social",
    "location": "Bay Area, CA, United States of America; US - CA - Oakland City - Remote",
    "official_url": "http://block.xyz/careers/jobs/5422288008?gh_jid=5422288008",
    "posted_date": "2026-09-11",
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:29:15.467559+00:00",
    "date_confidence": "high",
    "description": "<p>Since we opened our doors in 2009, the world of commerce has evolved immensely, and so has Square. After enabling anyone to take payments and never miss a sale, we saw sellers s"
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
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

## Two Sigma

- Status: ok
- Scraping method: HTTP GET Avature SearchJobs HTML + JobDetail HTML
- Search URL/API: `https://careers.twosigma.com/careers/OpenRoles?search=software+engineer&jobRecordsPerPage=10&jobOffset=0`
- Pagination: jobOffset=0,10,... ; stop on empty/repeat or short page
- Pages/requests fetched: 15
- HTTP requests/cumulative request time: 53 / 64.086s
- Company elapsed time: 71.916s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 38 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 23, 'fetched:new': 15}
- Raw jobs found: 101
- After US/location filtering: 38
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.479, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 11.659, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 2.427, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 6.232, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 19.9, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.988, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 1.285, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.981, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 7.966, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 26, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 26}

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
    "fetched_at": "2026-09-15T00:29:16.168176+00:00",
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
    "fetched_at": "2026-09-15T00:29:16.168176+00:00",
    "date_confidence": "unknown",
    "description": "AI Solutions Developer Location NY New York United States"
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
    "fetched_at": "2026-09-15T00:29:16.168176+00:00",
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
    "fetched_at": "2026-09-15T00:29:16.168176+00:00",
    "date_confidence": "unknown",
    "description": "AI Research Scientist - Campus Full-Time Location NY New York United States"
  },
  {
    "company": "Two Sigma",
    "source": "two_sigma_official_careers",
    "job_id": "13080",
    "title": "Quantitative Software Engineer: Techniques Engineering",
    "location": "United States - NY New York",
    "official_url": "https://careers.twosigma.com/careers/JobDetail/New-York-City-United-States-Quantitative-Software-Engineer-Techniques-Engineering/13080",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:16.168176+00:00",
    "date_confidence": "unknown",
    "description": "Quantitative Software Engineer: Techniques Engineering Location NY New York United States"
  }
]
```

## Verkada

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/verkada/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.164s
- Company elapsed time: 0.664s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 293
- After US/location filtering: 238
- With trustworthy posted_date: 238
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
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:29:20.498914+00:00",
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
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:29:20.498914+00:00",
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
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:29:20.498914+00:00",
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
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:29:20.498914+00:00",
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
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:29:20.498914+00:00",
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
- HTTP requests/cumulative request time: 130 / 50.453s
- Company elapsed time: 67.880s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 110 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 108}
- Raw jobs found: 331
- After US/location filtering: 110
- With trustworthy posted_date: 110
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.796, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.655, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 1.342, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 12.668, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.98, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.433, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.792, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.558, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 4.665, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF087855W",
    "title": "Visa Consulting & Analytics Director – Portfolio Optimization & Solutions",
    "location": "US - Miami, FL",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Miami-FL/Visa-Consulting---Analytics-Director---Portfolio-Optimization---Solutions_REF087855W",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:21.163777+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF077610W",
    "title": "Software Test Engineer",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Software-Test-Engineer_REF077610W",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:21.163777+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF081500W",
    "title": "Staff Software Engineer",
    "location": "US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Austin-TX/Staff-Software-Engineer_REF081500W-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:21.163777+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088064W",
    "title": "Data Engineer",
    "location": "US - Foster City, CA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Data-Engineer_REF088064W",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:21.163777+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088359W",
    "title": "Director, Backend Product Management",
    "location": "US - Foster City, CA; US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Director--Backend-Product-Management_REF088359W",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:21.163777+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.410s
- Company elapsed time: 0.420s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 16
- After US/location filtering: 11
- With trustworthy posted_date: 11
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
    "fetched_at": "2026-09-15T00:29:31.477224+00:00",
    "date_confidence": "high",
    "description": "Role Responsibilities: System Bringup & Deployment Deploy and integrate autonomous driving software onto vehicle platforms and embedded computing systems. Validate system functiona"
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
    "fetched_at": "2026-09-15T00:29:31.477224+00:00",
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
    "fetched_at": "2026-09-15T00:29:31.477224+00:00",
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
    "fetched_at": "2026-09-15T00:29:31.477224+00:00",
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
    "fetched_at": "2026-09-15T00:29:31.477224+00:00",
    "date_confidence": "high",
    "description": "Building/Integrating software and algorithms for path planning, behavioral planning and vehicle control Developing/Implementing/Evaluating/Launching algorithms in Robotic motion pl"
  }
]
```

## Workday

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://workday.wd5.myworkdayjobs.com/Workday`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 25
- HTTP requests/cumulative request time: 143 / 99.410s
- Company elapsed time: 119.635s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 117 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 20, 'fetched:new': 97}
- Raw jobs found: 442
- After US/location filtering: 117
- With trustworthy posted_date: 117
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 54.521, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 9.066, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 2.498, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 16.753, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.164, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.94, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.89, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.427, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 8.132, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0108761",
    "title": "Principal AI Engineer",
    "location": "USA, GA, Atlanta; Canada, BC, Vancouver; USA, CO, Boulder",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-GA-Atlanta/Principal-AI-Engineer_JR-0108761",
    "posted_date": "2026-09-02",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:31.898756+00:00",
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
    "posted_date": "2026-09-01",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:31.898756+00:00",
    "date_confidence": "high",
    "description": "Your work days are brighter here. We’re obsessed with making hard work pay off, for our people, our customers, and the world around us. As a Fortune 500 company and a leading AI pl"
  },
  {
    "company": "Workday",
    "source": "workday_official_careers",
    "job_id": "JR-0109765",
    "title": "Principal AI UX Lead",
    "location": "USA, CA, Pleasanton",
    "official_url": "https://workday.wd5.myworkdayjobs.com/Workday/job/USA-CA-Pleasanton/Principal-AI-UX-Lead_JR-0109765-1",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:31.898756+00:00",
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
    "fetched_at": "2026-09-15T00:29:31.898756+00:00",
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
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:31.898756+00:00",
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
- HTTP requests/cumulative request time: 52 / 25.710s
- Company elapsed time: 31.680s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 36 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 34}
- Raw jobs found: 149
- After US/location filtering: 36
- With trustworthy posted_date: 36
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 16.024, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 0.952, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.755, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 2.917, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 4.198, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.632, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 0.739, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.848, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 0.753, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 14}

Sample normalized records:

```json
[
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751037",
    "title": "Agentic AI, Senior Software Development Engineer",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Senior-Software-Development-Engineer_P751037-1",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:42.492929+00:00",
    "date_confidence": "high",
    "description": "About the team The Agentic AI team at Zillow is transforming the real estate industry by helping millions of people use AI assistants to find their next home. We are building alway"
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P747954",
    "title": "Principal Machine Learning Engineer, Agentic AI",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Principal-Machine-Learning-Engineer--Agentic-AI_P747954",
    "posted_date": "2026-06-24",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:42.492929+00:00",
    "date_confidence": "high",
    "description": "About the team The Agentic AI team at Zillow is at the forefront of transforming the real estate industry by helping millions of people use AI technologies to find their next home."
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P751278",
    "title": "Agentic AI, Principal Machine Learning Engineer",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Agentic-AI--Principal-Machine-Learning-Engineer_P751278-1",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:42.492929+00:00",
    "date_confidence": "high",
    "description": "About the team ​​The Agentic AI team at Zillow is at the forefront of transforming the real estate industry by helping millions of people use AI assistants to find their next home."
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P750295",
    "title": "Senior AI-Native Product Engineer, Full Stack",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Senior-AI-Native-Product-Engineer--Full-Stack_P750295-1",
    "posted_date": "2026-09-01",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:29:42.492929+00:00",
    "date_confidence": "high",
    "description": "About the team The Metro team works on the systems that shape how customers connect with real estate agents on Zillow. We build tools that real estate professionals rely on to run "
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
    "fetched_at": "2026-09-15T00:29:42.492929+00:00",
    "date_confidence": "high",
    "description": "About the team The Data Engineering & Enterprise Tools team powers Zillow Rentals by delivering mission-critical analytics tools, AI enablement solutions, and high fidelity data pr"
  }
]
```

## Zscaler

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/zscaler/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.252s
- Company elapsed time: 0.865s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 371
- After US/location filtering: 241
- With trustworthy posted_date: 241
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5164593007",
    "title": "Account Executive - Commercial",
    "location": "Mumbai, IND",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5164593007",
    "posted_date": "2026-07-10",
    "updated_date": "2026-08-19",
    "fetched_at": "2026-09-15T00:30:05.048777+00:00",
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
    "updated_date": "2026-08-19",
    "fetched_at": "2026-09-15T00:30:05.048777+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5236995007",
    "title": "Account Executive, Commercial - Chicago",
    "location": "Remote - Illinois, USA; Remote - Kansas, USA; Remote - Missouri, USA",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5236995007",
    "posted_date": "2026-09-14",
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-15T00:30:05.048777+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5203734007",
    "title": "Account Executive, Commercial - Mountain West",
    "location": "Remote - Colorado, USA; Remote - Montana, USA; Remote - Oregon, USA; Remote - Wyoming, USA; Remote - Colorado, USA; Remote - Nevada, USA",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5203734007",
    "posted_date": "2026-08-05",
    "updated_date": "2026-09-08",
    "fetched_at": "2026-09-15T00:30:05.048777+00:00",
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
    "updated_date": "2026-09-11",
    "fetched_at": "2026-09-15T00:30:05.048777+00:00",
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
- HTTP requests/cumulative request time: 11 / 6.510s
- Company elapsed time: 6.635s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1}
- Raw jobs found: 4
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.936, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.449, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.447, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.455, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.497, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.449, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.804, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.453, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.547, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

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
    "fetched_at": "2026-09-15T00:30:05.914879+00:00",
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
- HTTP requests/cumulative request time: 144 / 91.763s
- Company elapsed time: 111.196s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 122 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 5, 'fetched:new': 117}
- Raw jobs found: 369
- After US/location filtering: 122
- With trustworthy posted_date: 122
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 56.827, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.374, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 0.775, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 18.511, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.556, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.669, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.209, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 31, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 31}
- Query diagnostic: {"elapsed_seconds": 0.257, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 7.695, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R0999504",
    "title": "Senior Manager Software Engineering",
    "location": "IL - Work from home; MS - Work from home; MT - Work from home; NC - Work from home; LA - Work from home; MD - Work from home; ME - Work from home; MN - Work from home; NE - Work from home; MO - Work from home; ND - Work from home; NY - Work from hom; NJ - Work from home; NM - Work from home; NV - Work from home; OH - Work from hom; SC - Work from home; TX - Work from home; RI - Work from home; SD - Work from home; VT - Work from home; TN - Work from home; VA - Work from home; WA - Work from home; UT - Work from home; WI - Work from home; WV - Work from home; OR - Work from home; WY - Work from home; OK - Work from home; PA - Work from home; CO - Work from home; AL - Work from home; AZ - Work from home; CA - Work from home; CT - Work from home; DC - Work from home; FL - Work from home; IA - Work from home; AR - Work from home; ID - Work from home; KS - Work from home; DE - Work from home; GA - Work from home; IN - Work from home; KY - Work from home; MI - Work from home; MA - Work from home; NH - Work from home",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/IL---Work-from-home/Senior-Manager-Software-Engineering_R0999504",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:12.550893+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1032981",
    "title": "Staff AI Development Engineer",
    "location": "AZ - Work from home",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/AZ---Work-from-home/Staff-AI-Development-Engineer_R1032981",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:12.550893+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R0903961",
    "title": "Senior Software Development Engineer Search AI",
    "location": "Work At Home-California; Work At Home-Arizona; Work At Home-Connecticut; Work At Home-Texas; Work At Home-Illinois",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/Work-At-Home-California/Senior-Software-Development-Engineer-Search-Machine-Learning_R0903961",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:12.550893+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R0976253",
    "title": "Lead Director, Medicare Advantage and Group ACA Risk Adjustment Informatics",
    "location": "CT - Work from home; Work At Home-Arkansas; Work At Home-Idaho; Work At Home-Texas; Work At Home-Georgia; Work At Home-Montana; Work At Home-Iowa; Work At Home-Wisconsin; Work At Home-Oregon; Work At Home-Washington; Work At Home-New York; Work At Home-District of Columbia; Work At Home-Connecticut; Work At Home-Nebraska; Work At Home-Rhode Island; Work At Home-Tennessee; Work At Home-Kentucky; Work At Home-Ohio; Work At Home-West Virginia; Work At Home-Maryland; Work At Home-Massachusetts; Work At Home-South Carolina; Work At Home-Missouri; Work At Home - Utah; Work At Home-Arizona; Work At Home-South Dakota; Work At Home-Pennsylvania; Work At Home-New Hampshire; Work At Home-Vermont; Work At Home-Minnesota; Work At Home-New Mexico; Work At Home-Michigan; Work At Home-California; Work At Home-Maine; Work At Home-North Dakota; Work At Home-Kansas; Work At Home-Indiana; Work At Home-New Jersey; Work At Home-Nevada; Work At Home-Louisiana; Work At Home-Mississippi; Work At Home-Oklahoma; Work At Home-Alabama; Work At Home-Virginia; Work At Home-Illinois; Work At Home-North Carolina; Work At Home-Colorado; Work At Home-Florida; Work At Home-Wyoming; Work At Home-Delaware",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/CT---Work-from-home/Lead-Director--Risk-Adjustment-Informatics_R0976253",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:12.550893+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1038966",
    "title": "Senior Manager - Software Development Engineering",
    "location": "RI - Woonsocket",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/RI---Woonsocket/Senior-Manager---Software-Development-Engineering_R1038966",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:12.550893+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.125s
- Company elapsed time: 0.271s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 80
- After US/location filtering: 71
- With trustworthy posted_date: 71
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8653419002",
    "title": "Ad Sales Lead, Central",
    "location": "Remote - Illinois; Remote",
    "official_url": "https://careers.duolingo.com/jobs/8653419002?gh_jid=8653419002",
    "posted_date": "2026-07-28",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-09-15T00:30:14.174131+00:00",
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
    "fetched_at": "2026-09-15T00:30:14.174131+00:00",
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
    "fetched_at": "2026-09-15T00:30:14.174131+00:00",
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
    "fetched_at": "2026-09-15T00:30:14.174131+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8442934002",
    "title": "Creative Director, Marketing",
    "location": "London, England; London, England, United Kingdom; New York, New York, United States",
    "official_url": "https://careers.duolingo.com/jobs/8442934002?gh_jid=8442934002",
    "posted_date": "2026-02-27",
    "updated_date": "2026-09-10",
    "fetched_at": "2026-09-15T00:30:14.174131+00:00",
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
- Pages/requests fetched: 10
- HTTP requests/cumulative request time: 40 / 4.665s
- Company elapsed time: 8.283s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 30 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 30
- After US/location filtering: 30
- With trustworthy posted_date: 7
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.177, "first_pass_survivors": 30, "group": "official", "jds_resolved": 7, "original_postings_resolved": 30, "page_budget": 2, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 0.013, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.014, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.013, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.013, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.013, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.013, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.013, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.013, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}

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
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:14.446079+00:00",
    "date_confidence": "high",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-161117",
    "title": "Software Development Engineer -AI/Agentic Systems",
    "location": "Redwood City, California, United States",
    "official_url": "https://careers.equinix.com/jobs/software-development-engineer-ai-agentic-systems-redwood-city-california-united-states",
    "posted_date": "2026-05-28",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:14.446079+00:00",
    "date_confidence": "high",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-160186",
    "title": "Senior Director AI - Chief Revenue Organization",
    "location": "Toronto, Ontario, Canada; Redwood City, California, United States; Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/senior-director-ai-chief-revenue-organization-redwood-city-california-united-states-dallas-texas-toronto-ontario-canada",
    "posted_date": "2026-04-21",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:14.446079+00:00",
    "date_confidence": "high",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-162135",
    "title": "AI and Business Process Strategic Portfolio Integrator",
    "location": "Toronto, Ontario, Canada; Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/ai-and-business-process-strategic-portfolio-integrator-dallas-texas-united-states-toronto-ontario-canada",
    "posted_date": "2026-07-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:14.446079+00:00",
    "date_confidence": "high",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-162405",
    "title": "DevOps Engineer",
    "location": "Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/devops-engineer-dallas-texas-united-states",
    "posted_date": "2026-07-24",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:14.446079+00:00",
    "date_confidence": "high",
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
- HTTP requests/cumulative request time: 16 / 7.114s
- Company elapsed time: 8.492s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: {'fetched:new': 1}
- Raw jobs found: 110
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.524, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.492, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.398, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.12, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.124, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.235, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.473, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.393, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.12, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

Sample normalized records:

```json
[
  {
    "company": "F5",
    "source": "f5_official_careers",
    "job_id": "RP1038648",
    "title": "Security Engineer III",
    "location": "Reston",
    "official_url": "https://ffive.wd5.myworkdayjobs.com/f5jobs/job/Reston/Security-Engineer-III_RP1038648",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:22.729759+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.132s
- Company elapsed time: 0.281s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 112
- After US/location filtering: 101
- With trustworthy posted_date: 101
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8734156002",
    "title": "Administrative Assistant, Proposals Team",
    "location": "San Mateo, CA; San Mateo, California, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8734156002",
    "posted_date": "2026-08-20",
    "updated_date": "2026-08-20",
    "fetched_at": "2026-09-15T00:30:28.085453+00:00",
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
    "fetched_at": "2026-09-15T00:30:28.085453+00:00",
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
    "fetched_at": "2026-09-15T00:30:28.085453+00:00",
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
    "fetched_at": "2026-09-15T00:30:28.085453+00:00",
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
    "updated_date": "2026-07-15",
    "fetched_at": "2026-09-15T00:30:28.085453+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is seeking an upbeat, focused, high-energy individual to join our Inside Sales tea"
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
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: none

## Wells Fargo

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://wf.wd1.myworkdayjobs.com/WellsFargoJobs`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 119 / 78.173s
- Company elapsed time: 94.610s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 97 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 4, 'fetched:new': 93}
- Raw jobs found: 335
- After US/location filtering: 97
- With trustworthy posted_date: 97
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 50.597, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.327, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 0.86, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 10.17, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.178, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.971, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.951, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.958, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 5.499, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}

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
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:28.367560+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Principal AI Engineer to join the CCIBT Gen AI team, which is responsible for building AI frameworks, intelligent agents, and technology p"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-573858",
    "title": "Lead Software Engineer – GenAI-Assisted & Autonomous Engineering",
    "location": "WEST DES MOINES, IA; IRVING, TX; CHARLOTTE, NC",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/WEST-DES-MOINES-IA/Lead-Software-Engineer---GenAI-Assisted---Autonomous-Engineering_R-573858",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:28.367560+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Lead Software Engineer to join the CDXO team and drive the development, enablement, and optimization of AI-Assisted and Autonomous Enginee"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-559960",
    "title": "Lead Infrastructure Engineer - Solace",
    "location": "ISELIN, NJ; IRVING, TX; CHARLOTTE, NC",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/ISELIN-NJ/Lead-Infrastructure-Engineer---Solace_R-559960",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:28.367560+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Lead Infrastructure Engineer–Solace to join the Solace Engineering team. We design and engineer low‑latency Solace platform made up of Sol"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-574294",
    "title": "2027 Technology Summer Internship – Early Careers (Software Engineering - California)",
    "location": "SAN FRANCISCO, CA; CONCORD, CA; SAN LEANDRO, CA",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/SAN-FRANCISCO-CA/XMLNAME-2027-Technology-Summer-Internship---Early-Careers--Software-Engineering---California-_R-574294",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:28.367560+00:00",
    "date_confidence": "high",
    "description": "This role is specifically for California ONLY (San Francisco Bay Market Area) About this role: Wells Fargo is seeking aspiring Software Engineers to join the 2027 Technology Intern"
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
    "fetched_at": "2026-09-15T00:30:28.367560+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking aspiring Software Engineers to join the 2027 Technology Internship Program. Program Overview: The Wells Fargo Technology Internship Program "
  }
]
```

## Yahoo

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ouryahoo.wd5.myworkdayjobs.com/careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 83 / 30.557s
- Company elapsed time: 41.659s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 63 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 4, 'fetched:new': 59}
- Raw jobs found: 272
- After US/location filtering: 63
- With trustworthy posted_date: 63
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 26.385, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.984, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 1.361, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 2.625, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 2.818, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.448, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 51, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 51}
- Query diagnostic: {"elapsed_seconds": 0.669, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.668, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 2.825, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

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
    "posted_date": "2026-08-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:29.045592+00:00",
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
    "fetched_at": "2026-09-15T00:30:29.045592+00:00",
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
    "fetched_at": "2026-09-15T00:30:29.045592+00:00",
    "date_confidence": "high",
    "description": "Yahoo Mail is the ultimate consumer inbox with hundreds of millions of users. It’s the best way to access your email and stay organized from a computer, phone or tablet. With its b"
  },
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0026054",
    "title": "Sr. Principal AI Architect, IT Workforce Experiences & Communication",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/IT-Sr-Princ-Architect_JR0026054",
    "posted_date": "2026-04-06",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:29.045592+00:00",
    "date_confidence": "high",
    "description": "It takes powerful technology to connect our brands and partners with an audience of hundreds of millions of people. Whether you’re looking to write mobile app code, engineer the se"
  },
  {
    "company": "Yahoo",
    "source": "yahoo_official_careers",
    "job_id": "JR0027091",
    "title": "Design Operations Manager, Systems and AI Enablement",
    "location": "United States of America",
    "official_url": "https://ouryahoo.wd5.myworkdayjobs.com/careers/job/United-States-of-America/Design-Operations-Manager--Systems-and-AI-Enablement_JR0027091",
    "posted_date": "2026-07-10",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:29.045592+00:00",
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
- HTTP requests/cumulative request time: 33 / 8.648s
- Company elapsed time: 13.120s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 30 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 45
- After US/location filtering: 30
- With trustworthy posted_date: 30
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 13.119, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "Ansys", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 45}

Sample normalized records:

```json
[
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "98682479840",
    "title": "Senior Application Engineer",
    "location": "Waltham, Massachusetts",
    "official_url": "https://careers.synopsys.com/job/waltham/senior-application-engineer/44408/98682479840",
    "posted_date": "2026-06-29",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:31.223195+00:00",
    "date_confidence": "high",
    "description": "THIS POSITION IS ELIGIBLE UNDER THE TERMS OF THE EMPLOYEE REFERRAL PROGRAM (ERP): SUMMARY ANSYS, Inc. seeks Senior Application Engineer to work in Waltham, MA RESPONSIBILITIES Lead"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "98682479648",
    "title": "Marketing Coordinator",
    "location": "Canonsburg, Pennsylvania",
    "official_url": "https://careers.synopsys.com/job/canonsburg/marketing-coordinator/44408/98682479648",
    "posted_date": "2026-06-29",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:31.223195+00:00",
    "date_confidence": "high",
    "description": "THIS POSITION IS ELIGIBLE UNDER THE TERMS OF THE EMPLOYEE REFERRAL PROGRAM (ERP): SUMMARY ANSYS, Inc. seeks Marketing Coordinator to work in Canonsburg, PA and various unanticipate"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "89569494560",
    "title": "Staff Application Engineer (Electronics Thermal Management) - Southern California (13730)",
    "location": "Irvine, California",
    "official_url": "https://careers.synopsys.com/job/irvine/staff-application-engineer-electronics-thermal-management-southern-california-13730/44408/89569494560",
    "posted_date": "2025-12-15",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:31.223195+00:00",
    "date_confidence": "high",
    "description": "We Are: At Synopsys, we drive the innovations that shape the way we live and connect. Our technology is central to the Era of Pervasive Intelligence, from self-driving cars to lear"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "98682479680",
    "title": "UX Designer II",
    "location": "Canonsburg, Pennsylvania",
    "official_url": "https://careers.synopsys.com/job/canonsburg/ux-designer-ii/44408/98682479680",
    "posted_date": "2026-06-29",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:31.223195+00:00",
    "date_confidence": "high",
    "description": "THIS POSITION IS ELIGIBLE UNDER THE TERMS OF THE EMPLOYEE REFERRAL PROGRAM (ERP): SUMMARY ANSYS, Inc. seeks UX Designer II to work in Canonsburg, PA RESPONSIBILITIES The User Exper"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "98682479744",
    "title": "Senior R&D Engineer",
    "location": "Canonsburg, Pennsylvania",
    "official_url": "https://careers.synopsys.com/job/canonsburg/senior-r-and-d-engineer/44408/98682479744",
    "posted_date": "2026-06-29",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:31.223195+00:00",
    "date_confidence": "high",
    "description": "THIS POSITION IS ELIGIBLE UNDER THE TERMS OF THE EMPLOYEE REFERRAL PROGRAM (ERP): SUMMARY ANSYS, Inc. seeks Senior R&D Engineer to work in Canonsburg, PA, and various unanticipated"
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
- HTTP requests/cumulative request time: 196 / 87.492s
- Company elapsed time: 112.726s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 174 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 9, 'fetched:new': 165}
- Raw jobs found: 330
- After US/location filtering: 174
- With trustworthy posted_date: 174
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 43.191, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 9.391, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 17, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 1.094, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 7.24, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 33, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 17.733, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.229, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 6.767, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.133, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 16.163, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 80}

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
    "posted_date": "2026-09-02",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:44.343952+00:00",
    "date_confidence": "high",
    "description": "At JetCool, a Flex company, we’re at the forefront of liquid cooling innovation, delivering advanced solutions that empower our partners in AI and high-performance computing. Unite"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD226261",
    "title": "Test Engineer",
    "location": "USA, CA, Milpitas",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-CA-Milpitas/Test-Engineer_WD226261",
    "posted_date": "2026-08-03",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:30:44.343952+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
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
    "fetched_at": "2026-09-15T00:30:44.343952+00:00",
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
    "fetched_at": "2026-09-15T00:30:44.343952+00:00",
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
    "fetched_at": "2026-09-15T00:30:44.343952+00:00",
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
- HTTP requests/cumulative request time: 53 / 29.640s
- Company elapsed time: 35.203s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 41 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1, 'fetched:new': 40}
- Raw jobs found: 114
- After US/location filtering: 41
- With trustworthy posted_date: 41
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.389, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 15, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 1.261, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.814, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 5.569, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 10.082, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 1.183, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.84, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.771, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.291, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 20}

Sample normalized records:

```json
[
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1555683",
    "title": "Senior Machine Learning Engineer, Analytics Center of Excellence (Remote/WFH)",
    "location": "Durham, North Carolina, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Durham-North-Carolina-United-States-of-America/Senior-Machine-Learning-Engineer--Analytics-Center-of-Excellence--Remote-WFH-_R1555683-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:31:10.705333+00:00",
    "date_confidence": "high",
    "description": "As one of our Senior Machine Learning Engineers, you will lead the design and development of ML applications across our product portfolio, with a strong focus on generative AI and "
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
    "fetched_at": "2026-09-15T00:31:10.705333+00:00",
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
    "fetched_at": "2026-09-15T00:31:10.705333+00:00",
    "date_confidence": "high",
    "description": "This is an exciting opportunity to work as a Senior Consultant in IQVIA, one of the world's leading multi-disciplinary and cross-functional teams working with Real World patient da"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1547949",
    "title": "Manager, Laboratory Automation & AI Transformation Lab",
    "location": "Durham, North Carolina, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Durham-North-Carolina-United-States-of-America/Manager--Laboratory-Automation---AI-Transformation-Lab_R1547949",
    "posted_date": "2026-06-18",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:31:10.705333+00:00",
    "date_confidence": "high",
    "description": "We are seeking Manager for our Laboratory Automation & AI Transformation Lab to join IQVIA Laboratories at Durham, NC . We hire passionate innovators who drive healthcare forward t"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1563152",
    "title": "Manager, AI Science & Solutions,US Based Remote",
    "location": "Durham, North Carolina, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Durham-North-Carolina-United-States-of-America/Manager--AI-Science---Solutions_R1563152",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:31:10.705333+00:00",
    "date_confidence": "high",
    "description": "Manager, AI Science & Solutions | IQVIA Are you looking to work at the forefront of Machine Learning and Artificial Intelligence? Would you be excited to apply cutting-edge Generat"
  }
]
```

## Johnson & Johnson

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://jj.wd5.myworkdayjobs.com/JJ`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 22
- HTTP requests/cumulative request time: 226 / 78.883s
- Company elapsed time: 109.038s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 203 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 201}
- Raw jobs found: 419
- After US/location filtering: 203
- With trustworthy posted_date: 203
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 28.561, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.487, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 39, "stop_reason": "early_stop", "unique_contribution": 25, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 20.65, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.643, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.439, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.774, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.578, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 0.259, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 7.282, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-099654",
    "title": "Robotics Controls & Autonomy Interns - Robotics R&D",
    "location": "Santa Clara, California, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Santa-Clara-California-United-States-of-America/RC---A---Robotics-R-D_R-099654-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:31:31.534644+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-099647",
    "title": "Mechanical Engineering Intern - Robotics R&D",
    "location": "Santa Clara, California, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Santa-Clara-California-United-States-of-America/Mechanical-Engineering-Intern---Robotics-R-D_R-099647-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:31:31.534644+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-099626",
    "title": "Electrical Engineering Intern - Robotics R&D",
    "location": "Santa Clara, California, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Santa-Clara-California-United-States-of-America/Electrical-Engineering-Intern---Robotics-R-D_R-099626-1",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:31:31.534644+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-098458",
    "title": "Director, AI Native Operations – Spring House, PA",
    "location": "Spring House, Pennsylvania, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Spring-House-Pennsylvania-United-States-of-America/Director--AI-Native-Operations---Spring-House--PA_R-098458-2",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:31:31.534644+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-098250",
    "title": "Process/Project Engineering Co-op",
    "location": "Wilson, North Carolina, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Wilson-North-Carolina-United-States-of-America/Process-Project-Engineering-Co-op_R-098250",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:31:31.534644+00:00",
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
- Pages/requests fetched: 15
- HTTP requests/cumulative request time: 45 / 21.345s
- Company elapsed time: 26.476s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 29 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 4, 'fetched:new': 25}
- Raw jobs found: 116
- After US/location filtering: 29
- With trustworthy posted_date: 29
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 9.939, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 19, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 0.604, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.683, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 2.512, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 5.727, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 28, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 28}
- Query diagnostic: {"elapsed_seconds": 2.475, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 0.587, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.602, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.491, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 22}

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
    "fetched_at": "2026-09-15T00:31:45.909273+00:00",
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
    "fetched_at": "2026-09-15T00:31:45.909273+00:00",
    "date_confidence": "high",
    "description": "We're looking for a Senior AI Application Engineer (.NET) to design, build, and scale intelligent enterprise applications powered by modern AI technologies. This role is ideal for "
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026576",
    "title": "AI / DevOps Engineer – Agentic Systems & Automation",
    "location": "USA - New York City - New York; USA - Philadelphia - Pennsylvania",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---New-York-City---New-York/AI---DevOps-Engineer---Agentic-Systems---Automation_R0026576",
    "posted_date": "2026-09-08",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:31:45.909273+00:00",
    "date_confidence": "high",
    "description": "As a Lead DevOps Engineer reporting to the AVP – Systems and Network Administration , y ou'll play a critical role in building and o perating intelligent automation platforms, AI a"
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
    "fetched_at": "2026-09-15T00:31:45.909273+00:00",
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
    "fetched_at": "2026-09-15T00:31:45.909273+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.691s
- Company elapsed time: 0.730s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 79
- After US/location filtering: 72
- With trustworthy posted_date: 72
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
    "fetched_at": "2026-09-15T00:32:02.978447+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "dae9f71b-9f8c-4669-a786-3d17c913c959",
    "title": "(Canada) Regional Named Account Executive - Northeast",
    "location": "Remote or Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/dae9f71b-9f8c-4669-a786-3d17c913c959",
    "posted_date": "2026-07-23",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:02.978447+00:00",
    "date_confidence": "high",
    "description": "3–5+ years of experience in B2B SaaS sales, preferably in healthcare, digital health, or care delivery platforms. Proven track record of building high-value relationships and closi"
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
    "fetched_at": "2026-09-15T00:32:02.978447+00:00",
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
    "fetched_at": "2026-09-15T00:32:02.978447+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "2123a700-c912-42d6-85ff-ec7e264c2a77",
    "title": "(US) Regional Named Account Executive - Northeast",
    "location": "Remote, USA",
    "official_url": "https://jobs.lever.co/pointclickcare/2123a700-c912-42d6-85ff-ec7e264c2a77",
    "posted_date": "2026-07-23",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:02.978447+00:00",
    "date_confidence": "high",
    "description": "3–5+ years of experience in B2B SaaS sales, preferably in healthcare, digital health, or care delivery platforms. Proven track record of building high-value relationships and closi"
  }
]
```

## Stryker

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://stryker.wd1.myworkdayjobs.com/StrykerCareers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 18
- HTTP requests/cumulative request time: 153 / 62.953s
- Company elapsed time: 82.317s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 134 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 7, 'fetched:new': 127}
- Raw jobs found: 226
- After US/location filtering: 134
- With trustworthy posted_date: 134
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 21.116, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 39, "stop_reason": "early_stop", "unique_contribution": 38, "unique_jobs": 39}
- Query diagnostic: {"elapsed_seconds": 0.708, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.59, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 10.651, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 21.977, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.518, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 0.771, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.689, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 18.332, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 76, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 76}

Sample normalized records:

```json
[
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R571006",
    "title": "Staff AI Engineer (Hybrid)",
    "location": "Menlo Park, California",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Menlo-Park-California/Staff-AI-Engineer--Hybrid-_R571006",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:03.709318+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid We're hiring a Staff AI Engineer to build GenAI and voice agents for medical devices, deployed both on-device and in the cloud. You'll own the technical di"
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
    "fetched_at": "2026-09-15T00:32:03.709318+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Remote Preference will be given to candidates residing in the Eastern or Central time zones. As a Senior Manager, AI Security Operations & Crisis Management, you "
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R572673",
    "title": "Software Engineer, Cloud",
    "location": "Menlo Park, California; Dallas, Texas; Redmond, Washington; Chicago, Illinois",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Menlo-Park-California/Software-Engineer--Cloud_R572673",
    "posted_date": "2026-09-10",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:03.709318+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Remote What You Will Do: As a backend Software Engineer, you will design, develop, and maintain platforms and APIs built on Cloud infrastructure and services that"
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
    "fetched_at": "2026-09-15T00:32:03.709318+00:00",
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
    "fetched_at": "2026-09-15T00:32:03.709318+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid Stryker is seeking a Senior Engineering Manager to lead the development and support of the SmartCare platform, including cloud services, web applications, "
  }
]
```

## TransUnion

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://transunion.wd5.myworkdayjobs.com/TransUnion`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 13
- HTTP requests/cumulative request time: 42 / 14.995s
- Company elapsed time: 19.483s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 28 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 4, 'fetched:new': 24}
- Raw jobs found: 112
- After US/location filtering: 28
- With trustworthy posted_date: 28
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.662, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 22, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 0.461, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 1.207, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 1.883, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.495, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 0.483, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 2.686, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 0.456, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.471, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}

Sample normalized records:

```json
[
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042097",
    "title": "AI Research & Innovation Lead",
    "location": "Chicago, Illinois",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/AI-Research---Innovation-Lead_19042097",
    "posted_date": "2026-09-09",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:03.747928+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview This role reports directly to Senior Manager, Data Science & Analytics "
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
    "fetched_at": "2026-09-15T00:32:03.747928+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The Global Infrastructure, Engineering & Operations (GIO) organization "
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
    "fetched_at": "2026-09-15T00:32:03.747928+00:00",
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
    "fetched_at": "2026-09-15T00:32:03.747928+00:00",
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
    "fetched_at": "2026-09-15T00:32:03.747928+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The SOAR Development team designs and delivers automation capabilities "
  }
]
```

## Travelers

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://travelers.wd5.myworkdayjobs.com/External`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 25
- HTTP requests/cumulative request time: 119 / 77.694s
- Company elapsed time: 94.112s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 93 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 26, 'fetched:new': 67}
- Raw jobs found: 344
- After US/location filtering: 93
- With trustworthy posted_date: 93
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.945, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 4.662, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 1.897, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 11.815, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 55, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 55}
- Query diagnostic: {"elapsed_seconds": 30.388, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.553, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 55, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 55}
- Query diagnostic: {"elapsed_seconds": 2.766, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 3.039, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 29, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 5.159, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 58}

Sample normalized records:

```json
[
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-49982",
    "title": "Senior Data & AI Engineer",
    "location": "CT - Hartford; MN - St. Paul",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Senior-Data---AI-Engineer_R-49982",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:12.386187+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51257",
    "title": "Gen AI - Data Engineer II",
    "location": "GA - Atlanta",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/GA---Atlanta/Gen-AI---Data-Engineer-II_R-51257",
    "posted_date": "2026-08-19",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:12.386187+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-50865",
    "title": "Senior Software Engineer – AI Agents & Harnesses",
    "location": "CT - Hartford; GA - Atlanta; MN - St. Paul",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Senior-Software-Engineer---AI-Agents---Harnesses_R-50865",
    "posted_date": "2026-08-05",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:12.386187+00:00",
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
    "fetched_at": "2026-09-15T00:32:12.386187+00:00",
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
    "fetched_at": "2026-09-15T00:32:12.386187+00:00",
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
- HTTP requests/cumulative request time: 24 / 4.927s
- Company elapsed time: 5.181s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 18 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 31
- After US/location filtering: 18
- With trustworthy posted_date: 18
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.652, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.236, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.67, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.5, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.183, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.94, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}

Sample normalized records:

```json
[
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1100903",
    "title": "Associate Director-Software Development",
    "location": "Alpharetta, Georgia",
    "official_url": "https://mycareer.verizon.com/jobs/r-1100903/associate-director-software-development/",
    "posted_date": "2026-09-14",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:23.232197+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1099880",
    "title": "Principal Engineer-Software Development",
    "location": "Irving, Texas; Alpharetta, Georgia; Ashburn, Virginia; Temple Terrace, Florida; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1099880/principal-engineer-software-development/",
    "posted_date": "2026-08-20",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:23.232197+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1099881",
    "title": "Principal Engineer-Software Development",
    "location": "Irving, Texas; Alpharetta, Georgia; Ashburn, Virginia; Temple Terrace, Florida; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1099881/principal-engineer-software-development/",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:23.232197+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1100142",
    "title": "Principal Engineer-Software Development",
    "location": "Alpharetta, Georgia; Irving, Texas; Basking Ridge, New Jersey; Temple Terrace, Florida",
    "official_url": "https://mycareer.verizon.com/jobs/r-1100142/principal-engineer-software-development/",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:23.232197+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1100363",
    "title": "Distinguished Engineer - Applied AI Solutions",
    "location": "Irving, Texas; Alpharetta, Georgia; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1100363/distinguished-engineer-applied-ai-solutions/",
    "posted_date": "2026-09-01",
    "updated_date": "",
    "fetched_at": "2026-09-15T00:32:23.232197+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.159s
- Company elapsed time: 0.178s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 20
- After US/location filtering: 9
- With trustworthy posted_date: 9
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8054682",
    "title": "Associate Marketing Operations/ Automation Manager",
    "location": "Remote - New York, NY; Remote - U.S.",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8054682",
    "posted_date": "2026-07-15",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-09-15T00:32:28.414023+00:00",
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
    "updated_date": "2026-08-21",
    "fetched_at": "2026-09-15T00:32:28.414023+00:00",
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
    "updated_date": "2026-08-17",
    "fetched_at": "2026-09-15T00:32:28.414023+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8125779",
    "title": "Platform Consultant",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8125779",
    "posted_date": "2026-08-17",
    "updated_date": "2026-08-17",
    "fetched_at": "2026-09-15T00:32:28.414023+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8138243",
    "title": "Sales Coordinator",
    "location": "London, UK; Yext UK",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8138243",
    "posted_date": "2026-08-18",
    "updated_date": "2026-08-18",
    "fetched_at": "2026-09-15T00:32:28.414023+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
