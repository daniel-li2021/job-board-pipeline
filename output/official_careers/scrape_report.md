# Official careers scrape report — 2026-11-25_1531

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Runtime metrics

- Wall time: 392.041s
- HTTP requests/cumulative request time: 3469 / 1220.645s
- Listing pages/detail fetched/cache reused/prefilter skipped: 717 / 2659 / 50 / 266
- Detail cache statuses: {'fetched:changed': 3, 'fetched:missing_detail': 115, 'fetched:new': 2343, 'reuse_after_error:stale': 19, 'reused': 29}
- Relevant JD coverage: 4222 / 4238; added detail requests 18 / 150; deferred 0

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 12.443s
- Company elapsed time: 27.280s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 121, 'usable_jd': 121}
- Raw jobs found: 788
- After US/location filtering: 255
- With trustworthy posted_date: 255
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.381, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "\"Ai Engineer\"", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.062, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Machine Learning Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.421, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Data Scientist\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.248, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Solutions Architect\"", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.245, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "\"Data Engineer\"", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 2.003, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "\"Platform Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.074, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Full Stack Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.015, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "\"Forward Deployed Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.888, "first_pass_survivors": 77, "group": "official", "jds_resolved": 77, "original_postings_resolved": 77, "page_budget": 12, "pages_fetched": 8, "query": "\"Software Engineer\"", "raw_jobs": 160, "stop_reason": "early_stop", "unique_contribution": 77, "unique_jobs": 160}
- Query diagnostic: {"elapsed_seconds": 2.097, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Infrastructure Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.173, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 5, "pages_fetched": 4, "query": "\"Software Engineer III\"", "raw_jobs": 63, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 63}
- Query diagnostic: {"elapsed_seconds": 1.327, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "\"Web Solutions Engineer\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 1.344, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 2, "pages_fetched": 2, "query": "\"DeepMind\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "93758412692562630",
    "title": "Senior Business and Marketing Data Scientist I",
    "location": "Kirkland, WA, USA; New York, NY, USA; Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/93758412692562630-senior-business-and-marketing-data-scientist-i",
    "posted_date": "2026-11-25",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:31:22.361310+00:00",
    "date_confidence": "high",
    "description": "Google's leadership team hand-picks thorny business challenges, and members of BizOps work in small teams to find solutions. As part of this team you fully immerse yourself in data"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "138280387280282310",
    "title": "Technical Solutions Engineer I, Infrastructure, Compute, Google Cloud",
    "location": "Kirkland, WA, USA; Austin, TX, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/138280387280282310-technical-solutions-engineer-i-infrastructure-compute-google-cloud",
    "posted_date": "2026-11-25",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:31:22.361310+00:00",
    "date_confidence": "high",
    "description": "The Google Cloud Platform team helps customers transform and build what's next for their business — all with technology built in the cloud. Our products are developed for security,"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "120425692834734790",
    "title": "Senior Business Data Scientist, Ads Finance",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/120425692834734790-senior-business-data-scientist-ads-finance",
    "posted_date": "2026-11-25",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:31:22.361310+00:00",
    "date_confidence": "high",
    "description": "The Knowledge and Information (K&I) Finance team provides strategic analysis and forecasting of Google’s revenue-generating products to executive audiences. As part of this team, y"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "76577718874841798",
    "title": "Research Scientist",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/76577718874841798-research-scientist",
    "posted_date": "2026-11-25",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:31:22.361310+00:00",
    "date_confidence": "high",
    "description": "As an organization, Google maintains a portfolio of research projects driven by fundamental research, new product innovation, product contribution and infrastructure goals, while p"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "130382870135874246",
    "title": "Senior Research Data Scientist, Consumer Shopping",
    "location": "Mountain View, CA, USA; Kirkland, WA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/130382870135874246-senior-research-data-scientist-consumer-shopping",
    "posted_date": "2026-11-25",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:31:22.361310+00:00",
    "date_confidence": "high",
    "description": "Google Shopping is a comprehensive product search engine, a fast-growing product ads business, and an everyday essentials marketplace. We aim to revolutionize shopping by building "
  }
]
```

## Amazon

- Status: ok
- Scraping method: HTTP GET search.json
- Search URL/API: `https://www.amazon.jobs/en/search?base_query=software+engineer&country=USA&offset=0&result_limit=10&sort=recent`
- Pagination: newest-first offset by 20; minimum 2 pages, then two seen pages + one overlap page; otherwise hits/cap
- Pages/requests fetched: 46
- HTTP requests/cumulative request time: 46 / 12.089s
- Company elapsed time: 24.331s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 491, 'usable_jd': 491}
- Raw jobs found: 872
- After US/location filtering: 754
- With trustworthy posted_date: 754
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.506, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 1.312, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 55, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 55}
- Query diagnostic: {"elapsed_seconds": 1.623, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.692, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.666, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.417, "first_pass_survivors": 49, "group": "official", "jds_resolved": 49, "original_postings_resolved": 49, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 52, "stop_reason": "page_budget", "unique_contribution": 49, "unique_jobs": 52}
- Query diagnostic: {"elapsed_seconds": 0.219, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 1.361, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 54, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 54}
- Query diagnostic: {"elapsed_seconds": 6.934, "first_pass_survivors": 212, "group": "official", "jds_resolved": 212, "original_postings_resolved": 212, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 212, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.62, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.726, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 3, "pages_fetched": 3, "query": "systems development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.193, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.063, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 2, "pages_fetched": 2, "query": "applied scientist", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10612960",
    "title": "Senior Software Development Engineer, Leo AI Foundations",
    "location": "Redmond, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10612960/senior-software-development-engineer-leo-ai-foundations",
    "posted_date": "2026-11-24",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:31:22.362052+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon’s low Earth orbit satellite network. Our mission is to deliver fast, reliable internet connectivity to customers beyond the reach of existing networks. From in"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10613799",
    "title": "Software Dev Engineer II, GenAIUX",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10613799/software-dev-engineer-ii-genaiux",
    "posted_date": "2026-11-25",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:31:22.362052+00:00",
    "date_confidence": "high",
    "description": "Help shape new Generative AIUX products for AWS customers Our team builds Generative AIUX products that transform the way customers design. We are focused on the future of design d"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10611672",
    "title": "Sr. Software Development Engineer – AI/ML Networking Disaggregated Inference, Annapurna Labs, Annapurna Labs",
    "location": "Cupertino, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10611672/sr-software-development-engineer-ai-ml-networking-disaggregated-inference-annapurna-labs-annapurna-labs",
    "posted_date": "2026-11-23",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:31:22.362052+00:00",
    "date_confidence": "high",
    "description": "Every token a large language model generates depends on data reaching the right accelerator at the right moment. As AI models outgrow any single chip, the network between accelerat"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10609661",
    "title": "Software Development Engineer, Autonomous AI Security",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10609661/software-development-engineer-autonomous-ai-security",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-24",
    "fetched_at": "2026-11-25T15:31:22.362052+00:00",
    "date_confidence": "high",
    "description": "At Amazon, security is central to maintaining customer trust and delivering delightful customer experiences. Our organization is responsible for creating and maintaining a high bar"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10607721",
    "title": "Software Engineer II, Fintech",
    "location": "San Francisco, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10607721/software-engineer-ii-fintech",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-18",
    "fetched_at": "2026-11-25T15:31:22.362052+00:00",
    "date_confidence": "high",
    "description": "If you are interested in this position, please apply on Twitch's Career site https://www.twitch.tv/jobs/en/ About Us: Twitch is the world’s biggest live streaming service, with glo"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=ai+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 43 / 24.159s
- Company elapsed time: 39.221s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 166, 'ai_recover': 1, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 165}
- Raw jobs found: 840
- After US/location filtering: 277
- With trustworthy posted_date: 277
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.338, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.162, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.446, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.299, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.255, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.221, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.494, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.692, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.646, "first_pass_survivors": 118, "group": "official", "jds_resolved": 118, "original_postings_resolved": 118, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 118, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.906, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "apps-and-frameworks-SFTWR-AF", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200696384-3956",
    "title": "AR/VR Software Engineer, Siri and Visual Intelligence - Vision Products Software",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200696384/ar-vr-software-engineer-siri-and-visual-intelligence-vision-products-software",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.363358+00:00",
    "date_confidence": "high",
    "description": "Would you like to help define how people interact with intelligence in spatial computing? Join the team that brings Siri and Visual Intelligence to Apple Vision Pro and visionOS. W"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200695852-3749",
    "title": "Retail Facilities Manager",
    "location": "San Jose, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200695852/retail-facilities-manager",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.363358+00:00",
    "date_confidence": "high",
    "description": "In Places, we don't sit back and let things happen — we make things happen, and we do it in service to every Apple employee and customer. Our team is a diverse, nimble group respon"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200695848-1124",
    "title": "Retail Facilities Manager",
    "location": "Dallas, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200695848/retail-facilities-manager",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.363358+00:00",
    "date_confidence": "high",
    "description": "In Places, we don't sit back and let things happen — we make things happen, and we do it in service to every Apple employee and customer. Our team is a diverse, nimble group respon"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200695068-3749",
    "title": "Business Intelligence and Reporting Program Manager, Places",
    "location": "San Jose, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200695068/business-intelligence-and-reporting-program-manager-places",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.363358+00:00",
    "date_confidence": "high",
    "description": "In Places, we don’t sit back and let things happen, we make things happen, and we do this in service to all Apple employees and customers. Our team is a diverse and nimble group th"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200696418-3337",
    "title": "CV/ML Systems Integration Engineer",
    "location": "Seattle, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200696418/cv-ml-systems-integration-engineer",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.363358+00:00",
    "date_confidence": "high",
    "description": "At Apple, we're on the cutting edge of delivering transformative experiences. If you are passionate about pushing the limits of technology to bring delight to a large user base, we"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 249 / 60.041s
- Company elapsed time: 95.831s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 209 / 0 / 0
- Detail cache statuses: {'fetched:new': 192, 'fetched:missing_detail': 17}
- Relevant JD recovery: {'eligible': 41, 'usable_jd': 41}
- Raw jobs found: 390
- After US/location filtering: 209
- With trustworthy posted_date: 209
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.287, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.914, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 11.773, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.924, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.097, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 1.459, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.524, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.435, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 24.097, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 118}

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200068561",
    "title": "Senior Hardware Test Engineer",
    "location": "United States, California, Mountain View",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557078619",
    "posted_date": "2026-11-25",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.365070+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft's expanding cloud infrastructure and is responsible for powering Mic"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200060075",
    "title": "Principal Cloud Network Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557025705",
    "posted_date": "2026-11-25",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.365070+00:00",
    "date_confidence": "high",
    "description": "Overview At Microsoft, our mission is to empower every person and every organization on the planet to achieve more, with Azure serving as the physical platform that underpins this "
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200055886",
    "title": "Software Engineer II- CTJ- POLY",
    "location": "United States, Virginia, Reston; United States, Washington, Redmond; United States, Maryland, Annapolis Junction",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556999153",
    "posted_date": "2026-11-25",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.365070+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft has an exciting opportunity for a Software Engineer II in the Cloud+AI Azure Data team. As part of a core product engineering group, you will develop features, i"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200068553",
    "title": "Director, Solution Engineering Management",
    "location": "United States, California, San Francisco; United States, California, Los Angeles; United States, Washington, Seattle; United States, Colorado, Denver",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557078600",
    "posted_date": "2026-11-25",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.365070+00:00",
    "date_confidence": "high",
    "description": "Overview Are you passionate about leading high-performing technical teams and helping some of the world's most innovative software and digital platform companies build, innovate, a"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200067801",
    "title": "Software Engineer II",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557075113",
    "posted_date": "2026-11-25",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:22.365070+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft's mission is to empower every person and every organization on the planet to achieve more. As employees we come together with a growth mindset, innovate to empow"
  }
]
```

## NVIDIA

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.098s
- Company elapsed time: 0.098s
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
- HTTP requests/cumulative request time: 1 / 0.047s
- Company elapsed time: 0.047s
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
- HTTP requests/cumulative request time: 1 / 0.172s
- Company elapsed time: 0.173s
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
- HTTP requests/cumulative request time: 11 / 2.060s
- Company elapsed time: 2.071s
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
- HTTP requests/cumulative request time: 26 / 23.821s
- Company elapsed time: 27.977s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 420, 'usable_jd': 420}
- Raw jobs found: 1236
- After US/location filtering: 704
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.963, "first_pass_survivors": 199, "group": "official", "jds_resolved": 199, "original_postings_resolved": 199, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 199, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 2.762, "first_pass_survivors": 129, "group": "official", "jds_resolved": 129, "original_postings_resolved": 129, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 129, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.363, "first_pass_survivors": 109, "group": "official", "jds_resolved": 109, "original_postings_resolved": 109, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 109, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.868, "first_pass_survivors": 78, "group": "official", "jds_resolved": 78, "original_postings_resolved": 78, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 78, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.648, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.56, "first_pass_survivors": 61, "group": "official", "jds_resolved": 61, "original_postings_resolved": 61, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 61, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.09, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 82, "stop_reason": "early_stop", "unique_contribution": 25, "unique_jobs": 82}
- Query diagnostic: {"elapsed_seconds": 0.629, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 5.093, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 200}

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
    "fetched_at": "2026-11-25T15:31:24.756591+00:00",
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
    "fetched_at": "2026-11-25T15:31:24.756591+00:00",
    "date_confidence": "unknown",
    "description": "Team Introduction: The AIGE (AI-Generated Effects) team is building AI-native creative tools that enable TikTok creators to turn natural-language and multimodal ideas into high-qua"
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
    "fetched_at": "2026-11-25T15:31:24.756591+00:00",
    "date_confidence": "unknown",
    "description": "The Commercial AI-CRM and Transaction team focuses on TikTok advertiser growth algorithms. Leveraging deep learning and large language model technologies, the team builds an algori"
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
    "fetched_at": "2026-11-25T15:31:24.756591+00:00",
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
    "fetched_at": "2026-11-25T15:31:24.756591+00:00",
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
- Pages/requests fetched: 29
- HTTP requests/cumulative request time: 216 / 58.137s
- Company elapsed time: 88.085s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 187 / 0 / 0
- Detail cache statuses: {'fetched:new': 183, 'fetched:missing_detail': 4}
- Relevant JD recovery: {'eligible': 29, 'usable_jd': 29}
- Raw jobs found: 553
- After US/location filtering: 187
- With trustworthy posted_date: 187
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 24.824, "first_pass_survivors": 61, "group": "official", "jds_resolved": 61, "original_postings_resolved": 61, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 61, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 11.654, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.196, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 11.268, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 50, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 50}
- Query diagnostic: {"elapsed_seconds": 5.935, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.771, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.651, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.996, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.79, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 80}

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
    "fetched_at": "2026-11-25T15:31:46.694251+00:00",
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
    "fetched_at": "2026-11-25T15:31:46.694251+00:00",
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
    "fetched_at": "2026-11-25T15:31:46.694251+00:00",
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
    "fetched_at": "2026-11-25T15:31:46.694251+00:00",
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
    "fetched_at": "2026-11-25T15:31:46.694251+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.223s
- Company elapsed time: 1.740s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 91, 'usable_jd': 91}
- Raw jobs found: 399
- After US/location filtering: 398
- With trustworthy posted_date: 398
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
    "fetched_at": "2026-11-25T15:31:49.641703+00:00",
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
    "fetched_at": "2026-11-25T15:31:49.641703+00:00",
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
    "fetched_at": "2026-11-25T15:31:49.641703+00:00",
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
    "fetched_at": "2026-11-25T15:31:49.641703+00:00",
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
    "fetched_at": "2026-11-25T15:31:49.641703+00:00",
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
- HTTP requests/cumulative request time: 119 / 47.564s
- Company elapsed time: 63.938s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 95 / 0 / 0
- Detail cache statuses: {'fetched:new': 95}
- Relevant JD recovery: {'eligible': 16, 'usable_jd': 16}
- Raw jobs found: 345
- After US/location filtering: 95
- With trustworthy posted_date: 95
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 28.587, "first_pass_survivors": 55, "group": "official", "jds_resolved": 55, "original_postings_resolved": 55, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 69, "stop_reason": "page_budget", "unique_contribution": 55, "unique_jobs": 69}
- Query diagnostic: {"elapsed_seconds": 4.432, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 29, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 0.624, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 6.193, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 8.803, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.443, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.971, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.671, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 6.318, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 76, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 76}

Sample normalized records:

```json
[
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046612",
    "title": "Privacy Engineer, Level 4",
    "location": "Los Angeles, California; Sunnyvale, California; New York, New York; Bellevue, Washington",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Privacy-Engineer--Level-4_R0046612-1",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:51.382495+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0047426",
    "title": "Application Engineer, CRM Technology, Level 4",
    "location": "Los Angeles, California; Sunnyvale, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Application-Engineer--CRM-Technology--Level-4_R0047426-1",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:51.382495+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "H226EM8",
    "title": "Manager, Software Engineering",
    "location": "Los Angeles, California; New York - 229 W 43rd St; Bellevue - 110 110th Ave NE; Sunnyvale, California; San Francisco - 1160 Battery St",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Manager--Software-Engineering_H226EM8-1",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:51.382495+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "H226PE10",
    "title": "Principal Software Engineer",
    "location": "Los Angeles, California; New York - 229 W 43rd St; Bellevue - 110 110th Ave NE; Sunnyvale, California; San Francisco - 1160 Battery St",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Principal-Software-Engineer_H226PE10",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:51.382495+00:00",
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
    "fetched_at": "2026-11-25T15:31:51.382495+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.113s
- Company elapsed time: 0.511s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 25, 'usable_jd': 25}
- Raw jobs found: 166
- After US/location filtering: 130
- With trustworthy posted_date: 130
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8396724",
    "title": "Administrative Business Partner I - Engineering, Product and Design",
    "location": "San Francisco, CA, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8396724",
    "posted_date": "2026-11-17",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-25T15:31:52.735245+00:00",
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
    "fetched_at": "2026-11-25T15:31:52.735245+00:00",
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
    "fetched_at": "2026-11-25T15:31:52.735245+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8349975",
    "title": "Compliance Specialist II",
    "location": "São Paulo, BR",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8349975",
    "posted_date": "2026-11-23",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:31:52.735245+00:00",
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
    "fetched_at": "2026-11-25T15:31:52.735245+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.205s
- Company elapsed time: 0.610s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 47, 'usable_jd': 47}
- Raw jobs found: 369
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
    "fetched_at": "2026-11-25T15:31:53.247704+00:00",
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
    "fetched_at": "2026-11-25T15:31:53.247704+00:00",
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
    "fetched_at": "2026-11-25T15:31:53.247704+00:00",
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
    "fetched_at": "2026-11-25T15:31:53.247704+00:00",
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
    "fetched_at": "2026-11-25T15:31:53.247704+00:00",
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
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 538 / 249.461s
- Company elapsed time: 317.228s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 514 / 0 / 0
- Detail cache statuses: {'fetched:new': 513, 'fetched:changed': 1}
- Relevant JD recovery: {'eligible': 81, 'usable_jd': 81}
- Raw jobs found: 2005
- After US/location filtering: 514
- With trustworthy posted_date: 514
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 206.927, "first_pass_survivors": 347, "group": "official", "jds_resolved": 347, "original_postings_resolved": 347, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 347, "stop_reason": "page_budget", "unique_contribution": 347, "unique_jobs": 347}
- Query diagnostic: {"elapsed_seconds": 1.061, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 113, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 113}
- Query diagnostic: {"elapsed_seconds": 10.977, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 204, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 204}
- Query diagnostic: {"elapsed_seconds": 86.179, "first_pass_survivors": 143, "group": "official", "jds_resolved": 143, "original_postings_resolved": 143, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 143, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 1.976, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 5.539, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 1.131, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 72, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 72}
- Query diagnostic: {"elapsed_seconds": 0.486, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 66, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 66}
- Query diagnostic: {"elapsed_seconds": 2.949, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 303, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 303}

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0077336",
    "title": "Senior Application Engineer",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162883203-senior-application-engineer",
    "posted_date": "2026-11-21",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:53.858145+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0077337",
    "title": "Staff Application Engineer",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162891903-staff-application-engineer",
    "posted_date": "2026-11-21",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:53.858145+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0077338",
    "title": "Senior Staff Application Engineer",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162891739-senior-staff-application-engineer",
    "posted_date": "2026-11-21",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:53.858145+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0078079",
    "title": "Sr Software Engineer",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162883690-sr-software-engineer",
    "posted_date": "2026-11-21",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:53.858145+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0077342",
    "title": "Sr Software Engineer",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000162878715-sr-software-engineer",
    "posted_date": "2026-11-21",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:53.858145+00:00",
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
- HTTP requests/cumulative request time: 49 / 60.049s
- Company elapsed time: 72.083s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 20 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 20}
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 348
- After US/location filtering: 20
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 31.676, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 4.879, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.7, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.797, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.767, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.896, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.816, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 4.964, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 6.588, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 48}

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46299",
    "title": "Legal Data Analyst - Tax & Transactional",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Legal-Data-Analyst-Tax-Transactional/46299",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:58.821910+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Thinking about an alternative legal career? Our Data team supports the Bloomberg Industry Group (INDG) business, which offers outstanding tools, search, "
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46290",
    "title": "AMER Warehouse Representative",
    "location": "Middle Village, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/AMER-Warehouse-Representative/46290",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:58.821910+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Position Summary We are seeking a highly motivated Warehouse Representative to join our AMER Supply Chain team This role is responsible for executing dai"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46255",
    "title": "Senior Researcher, Consumer Insights - Contract",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Researcher-Consumer-Insights-Contract/46255",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:58.821910+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Smarter, Faster, and as always - First. That's our philosophy. Bloomberg Media empowers global business leaders with breaking news, expert opinion, and p"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46252",
    "title": "BVAL (Bloomberg Evaluated Pricing) Evaluator - CLO",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/BVAL-Bloomberg-Evaluated-Pricing-Evaluator-CLO/46252",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:58.821910+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements Bloomberg’s BVAL (Bloomberg Evaluated Pricing) group is a market leader in fixed income pricing and the pricing provider to the Bloomberg Indices. BVAL p"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "46236",
    "title": "Technology Finance- Finance Transformation",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Technology-Finance-Finance-Transformation/46236",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:31:58.821910+00:00",
    "date_confidence": "unknown",
    "description": "Description & Requirements The energy of a newsroom, the pace of a trading floor, the buzz of a recent tech breakthrough; we work hard, and we work fast - while keeping up the qual"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 64
- HTTP requests/cumulative request time: 595 / 129.746s
- Company elapsed time: 211.424s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 531 / 0 / 0
- Detail cache statuses: {'fetched:new': 517, 'fetched:missing_detail': 14}
- Relevant JD recovery: {'eligible': 116, 'usable_jd': 116}
- Raw jobs found: 1262
- After US/location filtering: 531
- With trustworthy posted_date: 531
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 19.324, "first_pass_survivors": 54, "group": "official", "jds_resolved": 54, "original_postings_resolved": 54, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 54, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 15.593, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.484, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 36, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.838, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.846, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.24, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.741, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.129, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.568, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 15.181, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 3, "pages_fetched": 3, "query": "full stack", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.699, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "python react", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.694, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "pyspark databricks", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 6.684, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "experienced software engineer java python", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 9.178, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "agentic ai", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.378, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.288, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "software engineer ii", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.748, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 5.924, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "security engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.999, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "quantitative developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.414, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 1, "pages_fetched": 1, "query": "software engineer java spring", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.006, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "software engineer python authe", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.172, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "aws data platform engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.302, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data engineer applied ai", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.992, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "asset management technology", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 20}

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
    "posted_date": "2026-11-19",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:32:55.321566+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Senior Lead Software Engineer at JPMorgan Chase, within"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210807023",
    "title": "Lead Software Engineer- AI Engineer (AI Tool & Framework Development)",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210807023",
    "posted_date": "2026-11-20",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:32:55.321566+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorganChase within the Cons"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210788451",
    "title": "Senior Lead Software Engineer - AI/ML Engineering, GPU ML Serving",
    "location": "Seattle, WA, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210788451",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:32:55.321566+00:00",
    "date_confidence": "high",
    "description": "We have an exciting and rewarding opportunity for you to take your software engineering career to the next level. As a Lead Software Engineer at JPMorgan Chase within the Commercia"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210778106",
    "title": "Lead Software Engineer - Agentic AI",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210778106",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:32:55.321566+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorganChase with in Enterpr"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210770041",
    "title": "Principal Architect, AI-Native Engineering",
    "location": "Jersey City, NJ, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210770041",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:32:55.321566+00:00",
    "date_confidence": "high",
    "description": "If you are excited about shaping the future of technology and driving significant business impact in financial services, we are looking for people just like you. Join our team and "
  }
]
```

## Capital One

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
- Errors/403s: ['Capital One workday probe blocked with HTTP 429']

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 41
- HTTP requests/cumulative request time: 492 / 161.286s
- Company elapsed time: 228.386s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 451 / 0 / 0
- Detail cache statuses: {'fetched:new': 443, 'fetched:missing_detail': 8}
- Relevant JD recovery: {'eligible': 65, 'usable_jd': 65}
- Raw jobs found: 818
- After US/location filtering: 451
- With trustworthy posted_date: 451
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 31.811, "first_pass_survivors": 63, "group": "official", "jds_resolved": 63, "original_postings_resolved": 63, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 63, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 21.074, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.801, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.335, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 24.728, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.43, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.41, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 16.917, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 16.048, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 19.251, "first_pass_survivors": 37, "group": "official", "jds_resolved": 37, "original_postings_resolved": 37, "page_budget": 3, "pages_fetched": 3, "query": "core infrastructure", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 37, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 19.468, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "cleared site reliability engineer database", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.493, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "software developer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 10.618, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "applications developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "341967",
    "title": "Senior AI Agent Engineer",
    "location": "United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/341967",
    "posted_date": "2026-08-12",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:32:58.241254+00:00",
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
    "fetched_at": "2026-11-25T15:32:58.241254+00:00",
    "date_confidence": "high",
    "description": "Oracle Health is seeking a Senior AI Agent Engineer to build production AI agents and workflow automation capabilities that accelerate analytics delivery, improve insight generatio"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "342720",
    "title": "Senior Platform Software Engineer, AI",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/342720",
    "posted_date": "2026-11-20",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:32:58.241254+00:00",
    "date_confidence": "high",
    "description": "Oracle Cloud Infrastructure’s (OCI) Developer Platform Tools and Services organisation builds the next generation of developer productivity platforms, intelligent development workf"
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
    "fetched_at": "2026-11-25T15:32:58.241254+00:00",
    "date_confidence": "high",
    "description": "You will work at the intersection of distributed systems, networking, and AI infrastructure, driving architecture, design, implementation, and performance optimization across softw"
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
    "fetched_at": "2026-11-25T15:32:58.241254+00:00",
    "date_confidence": "high",
    "description": "We are looking for an experienced, hands-on engineer to lead the architecture and technical direction of NetSuite’s Mobile team across our applications and supporting services. You"
  }
]
```

## Walmart Global Tech

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
- Errors/403s: ['Walmart Global Tech workday probe blocked with HTTP 429']

## Cloudflare

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/cloudflare/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.311s
- Company elapsed time: 1.706s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 112, 'usable_jd': 112}
- Raw jobs found: 518
- After US/location filtering: 515
- With trustworthy posted_date: 515
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
    "updated_date": "2026-11-24",
    "fetched_at": "2026-11-25T15:33:10.957078+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3>About Us</h3> <p>At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that "
  },
  {
    "company": "Cloudflare",
    "source": "cloudflare_official_careers",
    "job_id": "8392878",
    "title": "Account Executive, Start Ups",
    "location": "Hybrid; München, Bayern, Germany",
    "official_url": "https://boards.greenhouse.io/cloudflare/jobs/8392878?gh_jid=8392878",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:10.957078+00:00",
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
    "fetched_at": "2026-11-25T15:33:10.957078+00:00",
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
    "fetched_at": "2026-11-25T15:33:10.957078+00:00",
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
    "fetched_at": "2026-11-25T15:33:10.957078+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.211s
- Company elapsed time: 1.028s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 136, 'usable_jd': 136}
- Raw jobs found: 771
- After US/location filtering: 406
- With trustworthy posted_date: 406
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:12.664168+00:00",
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:12.664168+00:00",
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:12.664168+00:00",
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:12.664168+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s largest enterprises to the most am"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8274927",
    "title": "Account Executive, Amer Platform (Growth Velocity)",
    "location": "Chicago, San Francisco, New York; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8274927",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:12.664168+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About Stripe</strong></h2> <div>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s largest enterprises to the most amb"
  }
]
```

## Coinbase

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/coinbase/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.151s
- Company elapsed time: 0.730s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 58, 'usable_jd': 58}
- Raw jobs found: 246
- After US/location filtering: 210
- With trustworthy posted_date: 210
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
    "fetched_at": "2026-11-25T15:33:13.694880+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? <span><a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sourc"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8173991",
    "title": "Accounting Intern",
    "location": "Hybrid - New York, NY; US - Remote Zone 1 (Job Requisitions Only)",
    "official_url": "https://www.coinbase.com/careers/positions/8173991?gh_jid=8173991",
    "posted_date": "2026-09-08",
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:13.694880+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? <span><a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sourc"
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
    "fetched_at": "2026-11-25T15:33:13.694880+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? <span><a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sourc"
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
    "fetched_at": "2026-11-25T15:33:13.694880+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? <span><a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sourc"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8175471",
    "title": "Analytics Engineer Intern",
    "location": "Hybrid - New York, NY; US - Remote Zone 1 (Job Requisitions Only)",
    "official_url": "https://www.coinbase.com/careers/positions/8175471?gh_jid=8175471",
    "posted_date": "2026-09-08",
    "updated_date": "2026-10-30",
    "fetched_at": "2026-11-25T15:33:13.694880+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? <span><a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sourc"
  }
]
```

## Robinhood

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/robinhood/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.336s
- Company elapsed time: 0.858s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 39, 'usable_jd': 39}
- Raw jobs found: 161
- After US/location filtering: 151
- With trustworthy posted_date: 151
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
    "fetched_at": "2026-11-25T15:33:14.426919+00:00",
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
    "fetched_at": "2026-11-25T15:33:14.426919+00:00",
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
    "fetched_at": "2026-11-25T15:33:14.426919+00:00",
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
    "fetched_at": "2026-11-25T15:33:14.426919+00:00",
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
    "fetched_at": "2026-11-25T15:33:14.426919+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.528s
- Company elapsed time: 0.862s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 38, 'usable_jd': 38}
- Raw jobs found: 145
- After US/location filtering: 96
- With trustworthy posted_date: 96
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Figma",
    "source": "figma_official_careers",
    "job_id": "5426468004",
    "title": "Account Executive, Enterprise",
    "location": "San Francisco, CA • New York, NY • United States; Canada; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/5426468004?gh_jid=5426468004",
    "posted_date": "2025-01-28",
    "updated_date": "2026-10-27",
    "fetched_at": "2026-11-25T15:33:14.792245+00:00",
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:14.792245+00:00",
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
    "fetched_at": "2026-11-25T15:33:14.792245+00:00",
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
    "fetched_at": "2026-11-25T15:33:14.792245+00:00",
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
    "fetched_at": "2026-11-25T15:33:14.792245+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.525s
- Company elapsed time: 1.041s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 20, 'usable_jd': 20}
- Raw jobs found: 247
- After US/location filtering: 136
- With trustworthy posted_date: 136
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8771512002",
    "title": "Backend Engineer, GitLab Orbit",
    "location": "Remote, Canada; Remote, United States; United States of America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8771512002",
    "posted_date": "2026-10-23",
    "updated_date": "2026-11-20",
    "fetched_at": "2026-11-25T15:33:15.284433+00:00",
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
    "fetched_at": "2026-11-25T15:33:15.284433+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8950909002",
    "title": "Business Development Representative, Japan",
    "location": "Remote; Japan",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8950909002",
    "posted_date": "2026-11-23",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:33:15.284433+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8932282002",
    "title": "Business Development Representative, SLED - West",
    "location": "Remote, United States; United States of America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8932282002",
    "posted_date": "2026-11-09",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-25T15:33:15.284433+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8782471002",
    "title": "Candidate Experience Specialist, Contractor (AMER)",
    "location": "Remote, United States; United States of America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8782471002",
    "posted_date": "2026-09-08",
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:15.284433+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.071s
- Company elapsed time: 0.149s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 3, 'usable_jd': 3}
- Raw jobs found: 29
- After US/location filtering: 29
- With trustworthy posted_date: 29
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8945798002",
    "title": "Account Executive, Media & Entertainment",
    "location": "Los Angeles Metropolitan Area or New York City Metropolitan Area; Los Angeles, California, United States; New York, New York, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8945798002",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:15.649043+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8927168002",
    "title": "Account Executive, Mobile Gaming & Apps",
    "location": "San Francisco Bay Area, Los Angeles; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8927168002",
    "posted_date": "2026-11-13",
    "updated_date": "2026-11-17",
    "fetched_at": "2026-11-25T15:33:15.649043+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8917177002",
    "title": "Associate Commercial Counsel",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8917177002",
    "posted_date": "2026-11-03",
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:33:15.649043+00:00",
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
    "fetched_at": "2026-11-25T15:33:15.649043+00:00",
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
    "fetched_at": "2026-11-25T15:33:15.649043+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.596s
- Company elapsed time: 0.879s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 13, 'usable_jd': 13}
- Raw jobs found: 111
- After US/location filtering: 75
- With trustworthy posted_date: 75
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
    "fetched_at": "2026-11-25T15:33:15.799466+00:00",
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
    "fetched_at": "2026-11-25T15:33:15.799466+00:00",
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
    "fetched_at": "2026-11-25T15:33:15.799466+00:00",
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
    "fetched_at": "2026-11-25T15:33:15.799466+00:00",
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
    "fetched_at": "2026-11-25T15:33:15.799466+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.416s
- Company elapsed time: 1.064s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 50, 'usable_jd': 50}
- Raw jobs found: 256
- After US/location filtering: 250
- With trustworthy posted_date: 250
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8688112002",
    "title": "Account Executive, Small Business",
    "location": "Salt Lake City, Utah, United States; New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8688112002?gh_jid=8688112002",
    "posted_date": "2026-08-06",
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-25T15:33:16.326263+00:00",
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
    "fetched_at": "2026-11-25T15:33:16.326263+00:00",
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
    "fetched_at": "2026-11-25T15:33:16.326263+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8950778002",
    "title": "Accounting Partnerships Manager",
    "location": "New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8950778002?gh_jid=8950778002",
    "posted_date": "2026-11-18",
    "updated_date": "2026-11-18",
    "fetched_at": "2026-11-25T15:33:16.326263+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8950781002",
    "title": "Accounting Partnerships Manager",
    "location": "San Francisco, California, United States; New York, New York, United States",
    "official_url": "https://www.brex.com/careers/8950781002?gh_jid=8950781002",
    "posted_date": "2026-11-18",
    "updated_date": "2026-11-18",
    "fetched_at": "2026-11-25T15:33:16.326263+00:00",
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
- HTTP requests/cumulative request time: 1 / 1.046s
- Company elapsed time: 2.176s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 49, 'usable_jd': 49}
- Raw jobs found: 295
- After US/location filtering: 248
- With trustworthy posted_date: 248
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
    "fetched_at": "2026-11-25T15:33:16.680040+00:00",
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
    "fetched_at": "2026-11-25T15:33:16.680040+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:33:16.680040+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:33:16.680040+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:33:16.680040+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.110s
- Company elapsed time: 0.304s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 16, 'usable_jd': 16}
- Raw jobs found: 144
- After US/location filtering: 73
- With trustworthy posted_date: 73
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
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-25T15:33:17.391388+00:00",
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
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-25T15:33:17.391388+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8952328002",
    "title": "Account Manager, Lyft Ads",
    "location": "San Francisco, CA; San Francisco, California, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8952328002?gh_jid=8952328002",
    "posted_date": "2026-11-20",
    "updated_date": "2026-11-20",
    "fetched_at": "2026-11-25T15:33:17.391388+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
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
    "fetched_at": "2026-11-25T15:33:17.391388+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
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
    "fetched_at": "2026-11-25T15:33:17.391388+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.660s
- Company elapsed time: 0.918s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 15, 'usable_jd': 15}
- Raw jobs found: 92
- After US/location filtering: 71
- With trustworthy posted_date: 71
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
    "fetched_at": "2026-11-25T15:33:17.696036+00:00",
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
    "fetched_at": "2026-11-25T15:33:17.696036+00:00",
    "date_confidence": "high",
    "description": "• Identify and pursue new business opportunities with organizations of 1,000+ employees. This is a “Hunter” role with significant inbound and SDR support. • Research and prospect i"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "b24fe5e5-dcb2-4238-a883-5fdb6bd404db",
    "title": "Accounting Analyst, Content Accounting",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/b24fe5e5-dcb2-4238-a883-5fdb6bd404db",
    "posted_date": "2026-11-13",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:17.696036+00:00",
    "date_confidence": "high",
    "description": "Execute the monthly global content accounting close, delivering accurate results on time for reporting, including account reconciliations, roll-forward analyses, and insight-driven"
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
    "fetched_at": "2026-11-25T15:33:17.696036+00:00",
    "date_confidence": "high",
    "description": "Build a deep understanding of Spotify’s label, publishing, lyrics, and audiobook contracts, how they’re implemented in our royalty systems, and how they flow into royalty calculati"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "77d3435e-569e-4644-876d-afc960da8d0a",
    "title": "Associate Artist Label Partnerships Manager, South Korea",
    "location": "Seoul",
    "official_url": "https://jobs.lever.co/spotify/77d3435e-569e-4644-876d-afc960da8d0a",
    "posted_date": "2026-11-17",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:17.696036+00:00",
    "date_confidence": "high",
    "description": "Manage a portfolio of artist and label relationships. Serve as the day-to-day contact for selected labels, distributors and artist teams. Stay close to their release plans and foll"
  }
]
```

## Ramp

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/ramp`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.234s
- Company elapsed time: 0.568s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 69, 'usable_jd': 69}
- Raw jobs found: 182
- After US/location filtering: 170
- With trustworthy posted_date: 170
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
    "fetched_at": "2026-11-25T15:33:18.642490+00:00",
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
    "fetched_at": "2026-11-25T15:33:18.642490+00:00",
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
    "fetched_at": "2026-11-25T15:33:18.642490+00:00",
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
    "fetched_at": "2026-11-25T15:33:18.642490+00:00",
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
    "fetched_at": "2026-11-25T15:33:18.642490+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.366s
- Company elapsed time: 0.547s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 40, 'usable_jd': 40}
- Raw jobs found: 173
- After US/location filtering: 84
- With trustworthy posted_date: 84
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
    "fetched_at": "2026-11-25T15:33:18.857713+00:00",
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
    "fetched_at": "2026-11-25T15:33:18.857713+00:00",
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
    "fetched_at": "2026-11-25T15:33:18.857713+00:00",
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
    "fetched_at": "2026-11-25T15:33:18.857713+00:00",
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
    "fetched_at": "2026-11-25T15:33:18.857713+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.206s
- Company elapsed time: 0.243s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 10, 'usable_jd': 10}
- Raw jobs found: 30
- After US/location filtering: 22
- With trustworthy posted_date: 22
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
    "fetched_at": "2026-11-25T15:33:19.202367+00:00",
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
    "fetched_at": "2026-11-25T15:33:19.202367+00:00",
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
    "fetched_at": "2026-11-25T15:33:19.202367+00:00",
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
    "fetched_at": "2026-11-25T15:33:19.202367+00:00",
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
    "fetched_at": "2026-11-25T15:33:19.202367+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.127s
- Company elapsed time: 0.319s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 32, 'usable_jd': 32}
- Raw jobs found: 122
- After US/location filtering: 99
- With trustworthy posted_date: 99
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
    "fetched_at": "2026-11-25T15:33:19.406673+00:00",
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
    "fetched_at": "2026-11-25T15:33:19.406673+00:00",
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
    "fetched_at": "2026-11-25T15:33:19.406673+00:00",
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
    "fetched_at": "2026-11-25T15:33:19.406673+00:00",
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
    "fetched_at": "2026-11-25T15:33:19.406673+00:00",
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
- HTTP requests/cumulative request time: 13 / 2.209s
- Company elapsed time: 2.842s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Cisco workday blocked with HTTP 429']

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://careers.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 135 / 54.801s
- Company elapsed time: 80.546s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 103 / 0 / 0
- Detail cache statuses: {'fetched:new': 103}
- Relevant JD recovery: {'eligible': 29, 'usable_jd': 29}
- Raw jobs found: 800
- After US/location filtering: 103
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 57.171, "first_pass_survivors": 97, "group": "official", "jds_resolved": 97, "original_postings_resolved": 97, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 97, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.158, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 3.266, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 3.662, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.129, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.153, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.149, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.849, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.895, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 2.113, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "cloud developer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}

Sample normalized records:

```json
[
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1450984933",
    "title": "Forward Deployed Chief AI Engineering Expert",
    "location": "New York, NY, US, 10001",
    "official_url": "https://careers.sap.com/job/New-York-Forward-Deployed-Chief-AI-Engineering-Expert-NY-10001/1450984933/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:19.726644+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1431260733",
    "title": "Principal Data and Applied Scientist, Finance and Spend Autonomous Suite, Palo Alto",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://careers.sap.com/job/Palo-Alto-Principal-Data-and-Applied-Scientist%2C-Finance-and-Spend-Autonomous-Suite%2C-Palo-Alto-CA-94304/1431260733/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:19.726644+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1431253733",
    "title": "Senior Data and Applied Scientist, HCM Autonomous Suite, Palo Alto",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://careers.sap.com/job/Palo-Alto-Senior-Data-and-Applied-Scientist%2C-HCM-Autonomous-Suite%2C-Palo-Alto-CA-94304/1431253733/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:19.726644+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1443337833",
    "title": "Principal AI Developer, Industry AI",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://careers.sap.com/job/Palo-Alto-Principal-AI-Developer%2C-Industry-AI-CA-94304/1443337833/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:19.726644+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1421516633",
    "title": "Forward Deployed Senior AI Engineer",
    "location": "New York, NY, US, 10001",
    "official_url": "https://careers.sap.com/job/New-York-Forward-Deployed-Senior-AI-Engineer-NY-10001/1421516633/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:19.726644+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  }
]
```

## HPE

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.172s
- Company elapsed time: 0.173s
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
- HTTP requests/cumulative request time: 41 / 25.048s
- Company elapsed time: 31.456s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 14 / 4 / 97
- Detail cache statuses: {'reused': 4}
- Relevant JD recovery: {'deterministic_skip': 93, 'cache_reused': 4, 'eligible': 18, 'ai_skip': 4, 'ai_recover': 4, 'detail_requests': 14, 'detail_failure': 14, 'budget_deferred': 0, 'usable_jd': 4}
- Raw jobs found: 270
- After US/location filtering: 115
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.015, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.715, "first_pass_survivors": 17, "group": "official", "jds_resolved": 0, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.957, "first_pass_survivors": 20, "group": "official", "jds_resolved": 0, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.751, "first_pass_survivors": 18, "group": "official", "jds_resolved": 0, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.549, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.276, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.679, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.235, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.611, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "103118491568",
    "title": "Lead Software Engineer (Java/AI)",
    "location": "Orlando, Florida",
    "official_url": "https://www.disneycareers.com/en/job/orlando/lead-software-engineer-java-ai/391/103118491568",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:22.462001+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "103169129808",
    "title": "Software Engineer II - AI Performance",
    "location": "New York, New York",
    "official_url": "https://www.disneycareers.com/en/job/new-york/software-engineer-ii-ai-performance/391/103169129808",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:22.462001+00:00",
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
    "fetched_at": "2026-11-25T15:33:22.462001+00:00",
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
    "fetched_at": "2026-11-25T15:33:22.462001+00:00",
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
    "fetched_at": "2026-11-25T15:33:22.462001+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.066s
- Company elapsed time: 0.066s
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
- HTTP requests/cumulative request time: 154 / 22.098s
- Company elapsed time: 44.369s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 127 / 0 / 0
- Detail cache statuses: {'fetched:new': 117, 'fetched:missing_detail': 10}
- Relevant JD recovery: {'eligible': 47, 'usable_jd': 47}
- Raw jobs found: 254
- After US/location filtering: 127
- With trustworthy posted_date: 127
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.958, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.712, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.914, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 8.614, "first_pass_survivors": 28, "group": "official", "jds_resolved": 28, "original_postings_resolved": 28, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 28, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.773, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.942, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.978, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.788, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.47, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3084018",
    "title": "Sr. ADAS Software Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446716245843",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:47.318383+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > ADAS R&D Software General Summary: At Qualcomm, we are advancing the automotive industry throu"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095879",
    "title": "Modem Hardware Design Verification Engineer – AI Driven Next Gen Modem Hardware Development, Staff",
    "location": "Boxborough, Massachusetts, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720926576",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:47.318383+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Modem Technologies General Summary: Qualcomm is the world’s largest fabless semiconductor comp"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3099231",
    "title": "EVA Implementation/Synthesis Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446722078669",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:47.318383+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Video Systems, HW Architecture General Summary: The EVA synthesis/implementation engineer will"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3098602",
    "title": "Automation Developer Engineer",
    "location": "San Diego, California, United States of America; Boulder, Colorado, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446721803210",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:47.318383+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Cellular System Test Engineering General Summary: About the Team Qualcomm's Wireless R&D group"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3099586",
    "title": "IT Program Manager, Staff",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446722225436",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:33:47.318383+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Incorporated Job Area: Information Technology Group, Information Technology Group > IT Program Management General Summary: The IT Program Manager, Staff will serv"
  }
]
```

## AMD

- Status: ok
- Scraping method: HTTP GET public Jibe/iCIMS jobs JSON
- Search URL/API: `https://careers.amd.com/api/jobs`
- Pagination: page=1,2,... per role query; stop on total/empty/repeat/short page
- Pages/requests fetched: 13
- HTTP requests/cumulative request time: 13 / 9.849s
- Company elapsed time: 11.473s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 181, 'usable_jd': 181}
- Raw jobs found: 1171
- After US/location filtering: 463
- With trustworthy posted_date: 463
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.746, "first_pass_survivors": 293, "group": "official", "jds_resolved": 293, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 293, "stop_reason": "early_stop", "unique_contribution": 293, "unique_jobs": 293}
- Query diagnostic: {"elapsed_seconds": 0.57, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning", "raw_jobs": 68, "stop_reason": "early_stop", "unique_contribution": 27, "unique_jobs": 68}
- Query diagnostic: {"elapsed_seconds": 2.474, "first_pass_survivors": 86, "group": "official", "jds_resolved": 86, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 86, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 1.99, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "AI research", "raw_jobs": 210, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 210}
- Query diagnostic: {"elapsed_seconds": 3.692, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 300}

Sample normalized records:

```json
[
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "96190",
    "title": "Software Engineer – AI Inference and Performance Optimization",
    "location": "Austin, Texas",
    "official_url": "",
    "posted_date": "2026-11-10",
    "updated_date": "2026-11-21",
    "fetched_at": "2026-11-25T15:34:31.688636+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92051",
    "title": "Software Development Engineer — GPU Fleet Management & AI Infrastructure",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-09-10",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:34:31.688636+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "97772",
    "title": "Software Development Test Engineer Lead AI Platform",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-11-11",
    "updated_date": "2026-11-21",
    "fetched_at": "2026-11-25T15:34:31.688636+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "92605",
    "title": "Software Development Engineer - GPU Interconnects and Ethernet AI",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-11-02",
    "updated_date": "2026-11-21",
    "fetched_at": "2026-11-25T15:34:31.688636+00:00",
    "date_confidence": "high",
    "description": "ADVANCE YOUR CAREER. ADVANCE THE WORLD. At AMD, we believe technology has the power to solve the world’s most important challenges. From advancing healthcare and scientific discove"
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "96895",
    "title": "Fellow, Agentic AI Software",
    "location": "Austin, Texas",
    "official_url": "",
    "posted_date": "2026-11-06",
    "updated_date": "2026-11-21",
    "fetched_at": "2026-11-25T15:34:31.688636+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.055s
- Company elapsed time: 0.056s
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
- HTTP requests/cumulative request time: 1 / 0.197s
- Company elapsed time: 0.971s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 59, 'usable_jd': 59}
- Raw jobs found: 390
- After US/location filtering: 242
- With trustworthy posted_date: 242
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
    "fetched_at": "2026-11-25T15:34:40.329833+00:00",
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
    "fetched_at": "2026-11-25T15:34:40.329833+00:00",
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
    "fetched_at": "2026-11-25T15:34:40.329833+00:00",
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
    "fetched_at": "2026-11-25T15:34:40.329833+00:00",
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
    "fetched_at": "2026-11-25T15:34:40.329833+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.296s
- Company elapsed time: 1.833s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 84, 'usable_jd': 84}
- Raw jobs found: 875
- After US/location filtering: 486
- With trustworthy posted_date: 486
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:34:41.301561+00:00",
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:34:41.301561+00:00",
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:34:41.301561+00:00",
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:34:41.301561+00:00",
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
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:34:41.301561+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.135s
- Company elapsed time: 0.715s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 30, 'usable_jd': 30}
- Raw jobs found: 255
- After US/location filtering: 236
- With trustworthy posted_date: 236
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
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:34:43.136203+00:00",
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
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:34:43.136203+00:00",
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
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:34:43.136203+00:00",
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
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:34:43.136203+00:00",
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
    "updated_date": "2026-11-04",
    "fetched_at": "2026-11-25T15:34:43.136203+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.889s
- Company elapsed time: 1.286s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 6, 'usable_jd': 6}
- Raw jobs found: 198
- After US/location filtering: 100
- With trustworthy posted_date: 100
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8381807",
    "title": "Category Lead, Airbnb Services",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8381807?gh_jid=8381807",
    "posted_date": "2026-11-12",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-25T15:34:43.162642+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8385577",
    "title": "Communications Manager, Trust",
    "location": "San Francisco, United States; San Francisco, CA",
    "official_url": "https://careers.airbnb.com/positions/8385577?gh_jid=8385577",
    "posted_date": "2026-11-18",
    "updated_date": "2026-11-18",
    "fetched_at": "2026-11-25T15:34:43.162642+00:00",
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
    "fetched_at": "2026-11-25T15:34:43.162642+00:00",
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
    "fetched_at": "2026-11-25T15:34:43.162642+00:00",
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
    "updated_date": "2026-11-10",
    "fetched_at": "2026-11-25T15:34:43.162642+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.666s
- Company elapsed time: 2.718s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 154, 'usable_jd': 154}
- Raw jobs found: 635
- After US/location filtering: 503
- With trustworthy posted_date: 503
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
    "fetched_at": "2026-11-25T15:34:43.856988+00:00",
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
    "fetched_at": "2026-11-25T15:34:43.856988+00:00",
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
    "fetched_at": "2026-11-25T15:34:43.856988+00:00",
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
    "fetched_at": "2026-11-25T15:34:43.856988+00:00",
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
    "updated_date": "2026-11-24",
    "fetched_at": "2026-11-25T15:34:43.856988+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.676s
- Company elapsed time: 0.893s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
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
    "job_id": "4568195006",
    "title": "Account Executive - New Business",
    "location": "New York City, NY",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4568195006?gh_jid=4568195006",
    "posted_date": "2025-07-22",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:34:44.450192+00:00",
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
    "fetched_at": "2026-11-25T15:34:44.450192+00:00",
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
    "fetched_at": "2026-11-25T15:34:44.450192+00:00",
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
    "updated_date": "2026-11-20",
    "fetched_at": "2026-11-25T15:34:44.450192+00:00",
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
    "fetched_at": "2026-11-25T15:34:44.450192+00:00",
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
- Pages/requests fetched: 23
- HTTP requests/cumulative request time: 23 / 31.234s
- Company elapsed time: 34.600s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 235, 'usable_jd': 235}
- Raw jobs found: 1064
- After US/location filtering: 453
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 6.434, "first_pass_survivors": 143, "group": "official", "jds_resolved": 143, "original_postings_resolved": 143, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 143, "unique_jobs": 148}
- Query diagnostic: {"elapsed_seconds": 3.907, "first_pass_survivors": 100, "group": "official", "jds_resolved": 100, "original_postings_resolved": 100, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 100, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 4.455, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 106, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 105}
- Query diagnostic: {"elapsed_seconds": 4.835, "first_pass_survivors": 66, "group": "official", "jds_resolved": 66, "original_postings_resolved": 66, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 66, "unique_jobs": 149}
- Query diagnostic: {"elapsed_seconds": 4.537, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.677, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 149}
- Query diagnostic: {"elapsed_seconds": 1.817, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 48, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 48}
- Query diagnostic: {"elapsed_seconds": 0.889, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 4.048, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 148}

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
    "fetched_at": "2026-11-25T15:34:45.343941+00:00",
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
    "fetched_at": "2026-11-25T15:34:45.343941+00:00",
    "date_confidence": "unknown",
    "description": "About the Team Join ByteDance’s database R&D team, where you’ll build and own cutting-edge database products supporting ByteDance’s global infrastructure. Our diverse portfolio inc"
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
    "fetched_at": "2026-11-25T15:34:45.343941+00:00",
    "date_confidence": "unknown",
    "description": "We are building the dedicated AI Agent infrastructure and product platform for the Security organization, enabling different business teams to rapidly build, deploy, and scale AI A"
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
    "fetched_at": "2026-11-25T15:34:45.343941+00:00",
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
    "fetched_at": "2026-11-25T15:34:45.343941+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.106s
- Company elapsed time: 0.422s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 78
- After US/location filtering: 78
- With trustworthy posted_date: 78
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
    "fetched_at": "2026-11-25T15:34:46.576453+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role</h2> <p>Chime's Data Science &amp; Machine Learning team builds the models, services, and platforms behind how millions of members manage and grow their financia"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8904561002",
    "title": "Associate, Assurance & Testing",
    "location": "Chicago, IL, USA; New York, NY, USA; San Francisco, CA, USA; Chicago, Illinois, United States; New York Office; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8904561002?gh_jid=8904561002",
    "posted_date": "2026-11-18",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:34:46.576453+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role&nbsp;</h2> <p>We are hiring an Associate on Chime’s Compliance Assurance &amp; Testing team. You will assess Chime’s compliance with regulatory requirements and "
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
    "fetched_at": "2026-11-25T15:34:46.576453+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the role</strong></h2> <p>We are hiring for a Director, Strategy and Growth Initiatives to help define and drive the long-term strategy and growth of the company."
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8765690002",
    "title": "Director, Data Engineering",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8765690002?gh_jid=8765690002",
    "posted_date": "2026-11-12",
    "updated_date": "2026-11-12",
    "fetched_at": "2026-11-25T15:34:46.576453+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\">About the role</span></h2> <p><span style=\"font-family: helvetica, arial, sans-serif;\">Data Engineering sits at the hea"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8932546002",
    "title": "Director, Incident & Availability Engineering",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8932546002?gh_jid=8932546002",
    "posted_date": "2026-11-16",
    "updated_date": "2026-11-16",
    "fetched_at": "2026-11-25T15:34:46.576453+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>About the role</strong></h2> <p>Availability and resilience are core to keeping Chime reliable for millions of members who count on us for their everyday financial live"
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

- Status: blocked
- Scraping method: oracle_hcm
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.309s
- Company elapsed time: 0.309s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Dell oracle hcm HTTP 502']

## Dropbox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/dropbox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.102s
- Company elapsed time: 0.223s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 11, 'usable_jd': 11}
- Raw jobs found: 51
- After US/location filtering: 36
- With trustworthy posted_date: 36
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
    "fetched_at": "2026-11-25T15:34:47.310037+00:00",
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
    "fetched_at": "2026-11-25T15:34:47.310037+00:00",
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
    "fetched_at": "2026-11-25T15:34:47.310037+00:00",
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
    "fetched_at": "2026-11-25T15:34:47.310037+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qotuz85z92z66zpz73zz122zz67z0z78zz78zgz85z5f2sngz82zz65z4z69zm6"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8048844",
    "title": "Director, Strategic AI Partnerships",
    "location": "Remote - US: San Francisco, CA; US",
    "official_url": "https://jobs.dropbox.com/listing/8048844?gh_jid=8048844",
    "posted_date": "2026-11-18",
    "updated_date": "2026-11-18",
    "fetched_at": "2026-11-25T15:34:47.310037+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qowz80zsz81z8nqz122zdfz68z5coz87zsz73zz76zipqu3z86zmz88zz81zcth"
  }
]
```

## Expedia Group

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.044s
- Company elapsed time: 0.045s
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
- HTTP requests/cumulative request time: 1 / 0.128s
- Company elapsed time: 0.204s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 1, 'usable_jd': 1}
- Raw jobs found: 141
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
    "fetched_at": "2026-11-25T15:34:47.579339+00:00",
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
    "fetched_at": "2026-11-25T15:34:47.579339+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:34:47.579339+00:00",
    "date_confidence": "high",
    "description": "<p><strong>***Now accepting applications for a January 5th, 2027 start date***</strong></p> <p>As an Account Executive on the Small Business sales team, you will identify, source, "
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8044961",
    "title": "Associate, Corporate Development",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8044961?gh_jid=8044961",
    "posted_date": "2026-10-02",
    "updated_date": "2026-11-18",
    "fetched_at": "2026-11-25T15:34:47.579339+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-24470</strong></p> <hr> <h2>About The Team</h2> <p>HubSpot’s mission is to help millions of organizations grow better.</p> <p>At HubSpot, strategy isn’t just a plan "
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
    "fetched_at": "2026-11-25T15:34:47.579339+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-34030</strong></p> <p><strong>Application deadline: </strong>Monday, November 30th at 9am ET</p> <hr> <p>&nbsp;</p> <h2><strong>Role Summary</strong></h2> <p>Our mis"
  }
]
```

## Instacart

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/instacart/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.103s
- Company elapsed time: 0.365s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 7, 'usable_jd': 7}
- Raw jobs found: 98
- After US/location filtering: 88
- With trustworthy posted_date: 88
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
    "fetched_at": "2026-11-25T15:34:47.784638+00:00",
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
    "fetched_at": "2026-11-25T15:34:47.784638+00:00",
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
    "fetched_at": "2026-11-25T15:34:47.784638+00:00",
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
    "fetched_at": "2026-11-25T15:34:47.784638+00:00",
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
    "updated_date": "2026-11-18",
    "fetched_at": "2026-11-25T15:34:47.784638+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.045s
- Company elapsed time: 0.046s
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
- Pages/requests fetched: 12
- HTTP requests/cumulative request time: 52 / 17.276s
- Company elapsed time: 18.996s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 40 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 14, 'usable_jd': 14}
- Raw jobs found: 120
- After US/location filtering: 40
- With trustworthy posted_date: 40
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 7.752, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 22, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 1.106, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 0.879, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 2.789, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 2.609, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 1.088, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 0.512, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.484, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.777, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 30, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 30}

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
    "fetched_at": "2026-11-25T15:34:48.196723+00:00",
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
    "fetched_at": "2026-11-25T15:34:48.196723+00:00",
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
    "fetched_at": "2026-11-25T15:34:48.196723+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37817",
    "title": "Software Engineer in Test - EDG (Graduate Engineers)",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37817-software-engineer-in-test-edg-graduate-engineers?keywords=ai+engineer",
    "posted_date": "2026-10-08",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:34:48.196723+00:00",
    "date_confidence": "high",
    "description": "<p>Job Summary</p> &lt;p&gt;MathWorks has a hybrid work model that enables staff members to split their time between office and home. The hybrid model provides the advantage of hav"
  },
  {
    "company": "MathWorks",
    "source": "mathworks_official_careers",
    "job_id": "37914",
    "title": "Software Engineer in Test",
    "location": "US-MA-Natick",
    "official_url": "https://www.mathworks.com/company/jobs/opportunities/37914-software-engineer-in-test?keywords=ai+engineer",
    "posted_date": "2026-11-20",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:34:48.196723+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.192s
- Company elapsed time: 0.945s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 43, 'usable_jd': 43}
- Raw jobs found: 420
- After US/location filtering: 265
- With trustworthy posted_date: 265
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "8346138",
    "title": "2027 - AI and People Transformation Intern, NYC",
    "location": "New York City; New York, NY, United States",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=8346138",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:35:07.195676+00:00",
    "date_confidence": "high",
    "description": "<p>We’re seeking AI &amp; People Transformation Interns to help reimagine how our People teams work. You’ll examine how process design, data, and emerging AI tools can help simplif"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "8346144",
    "title": "2027 - Finance Intern, San Francisco",
    "location": "San Francisco; San Francisco, CA, United States",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=8346144",
    "posted_date": "2026-11-20",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:35:07.195676+00:00",
    "date_confidence": "high",
    "description": "<p>We’re seeking a curious, analytical intern who brings a fresh perspective and is eager to help the Financial Planning &amp; Analysis team identify ways to improve. As a Financia"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "8209134",
    "title": "2027 - Software Engineering Intern, AMER",
    "location": "Austin; New York City; San Francisco; Austin, TX, United States; New York, NY, United States; San Francisco, CA, United States",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=8209134",
    "posted_date": "2026-10-23",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:35:07.195676+00:00",
    "date_confidence": "high",
    "description": "<p>We’re seeking curious minds like yours to collaborate with full-time engineers and cross functional teammates, learn development standard methodologies, and gain practical softw"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "8301842",
    "title": "2027 - Tax Intern, New York City",
    "location": "New York City; New York, NY, United States",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=8301842",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:35:07.195676+00:00",
    "date_confidence": "high",
    "description": "<p>We're seeking someone who's curious, detail-oriented, and excited to learn how a modern tax department operates from the inside out. As a MongoDB Tax Intern, you’ll get hands-on"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7669637",
    "title": "Account Development Representative",
    "location": "Tysons; Tysons, Virginia, United States",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7669637",
    "posted_date": "2026-03-03",
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:35:07.195676+00:00",
    "date_confidence": "high",
    "description": "<p>Headquartered in New York, MongoDB’s mission is to empower innovators to create, transform, and disrupt industries with software. MongoDB’s unified database platform was built t"
  }
]
```

## Morgan Stanley

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://morganstanley.eightfold.ai/api/pcsx/search?domain=morganstanley.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 135 / 21.375s
- Company elapsed time: 40.268s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 110 / 0 / 0
- Detail cache statuses: {'fetched:new': 110}
- Relevant JD recovery: {'eligible': 33, 'usable_jd': 33}
- Raw jobs found: 220
- After US/location filtering: 110
- With trustworthy posted_date: 110
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 9.156, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.43, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.838, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 4.872, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 3.18, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.626, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.536, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 0.723, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 1.659, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR046701",
    "title": "Lead Cryptography Engineering and Development",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549801331743",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:08.142145+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR046542",
    "title": "Senior AI Development Platform Engineer",
    "location": "Alpharetta, Georgia, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549801310855",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:08.142145+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR044760",
    "title": "Senior L3 Network Operation Engineer - Vice President",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800457371",
    "posted_date": "2026-11-22",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:08.142145+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR046722",
    "title": "Mainframe Network Engineer",
    "location": "Atlanta, Georgia, United States of America; Birmingham, Alabama, United States of America; Little Rock, Arkansas, United States of America; Scottsdale, Arizona, United States of America; Greenwood Village, Colorado, United States of America; Greenwich, Connecticut, United States of America; Wilmington, Delaware, United States of America; Miami, Florida, United States of America; Davenport, Iowa, United States of America; Boise, Idaho, United States of America; Chicago, Illinois, United States of America; Indianapolis, Indiana, United States of America; Leawood, Kansas, United States of America; Louisville, Kentucky, United States of America; New Orleans, Louisiana, United States of America; Boston, Massachusetts, United States of America; Baltimore, Maryland, United States of America; Portland, Maine, United States of America; Birmingham, Michigan, United States of America; Minneapolis, Minnesota, United States of America; Clayton, Missouri, United States of America; Jackson, Mississippi, United States of America; Billings, Montana, United States of America; Charlotte, North Carolina, United States of America; Fargo, North Dakota, United States of America; Omaha, Nebraska, United States of America; Manchester, New Hampshire, United States of America; Albuquerque, New Mexico, United States of America; Reno, Nevada, United States of America; Columbus, Ohio, United States of America; Tulsa, Oklahoma, United States of America; Portland, Oregon, United States of America; West Conshohocken, Pennsylvania, United States of America; Providence, Rhode Island, United States of America; Charleston, South Carolina, United States of America; Sioux City, South Dakota, United States of America; Knoxville, Tennessee, United States of America; Houston, Texas, United States of America; South Jordan, Utah, United States of America; Mclean, Virginia, United States of America; Burlington, Vermont, United States of America; Bellevue, Washington, United States of America; Wauwatosa, Wisconsin, United States of America; Charleston, West Virginia, United States of America; Sheridan, Wyoming, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549801333393",
    "posted_date": "2026-11-19",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:08.142145+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR043786",
    "title": "Senior Platform Engineer - Parametric",
    "location": "Seattle, Washington, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800280238",
    "posted_date": "2026-11-18",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:08.142145+00:00",
    "date_confidence": "high",
    "description": "ABOUT MORGAN STANLEY Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, wealth management and investment managemen"
  }
]
```

## NetApp

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.netapp.com/en/search-jobs`
- Pagination: p=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 29
- HTTP requests/cumulative request time: 125 / 38.813s
- Company elapsed time: 57.770s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 96 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 42, 'usable_jd': 42}
- Raw jobs found: 435
- After US/location filtering: 96
- With trustworthy posted_date: 96
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 17.924, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.945, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 6.515, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 7.572, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 3.178, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.916, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.514, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.448, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.758, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

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
    "fetched_at": "2026-11-25T15:35:19.945214+00:00",
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
    "fetched_at": "2026-11-25T15:35:19.945214+00:00",
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
    "fetched_at": "2026-11-25T15:35:19.945214+00:00",
    "date_confidence": "high",
    "description": "Job Summary Distinguished Engineer - AI Infrastructure We are seeking a Distinguished Engineer with unrivaled depth in AI/ML inferencing at scale and the distributed systems founda"
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
    "fetched_at": "2026-11-25T15:35:19.945214+00:00",
    "date_confidence": "high",
    "description": "Job Summary As Director, Data & AI readiness you will own the strategy to enable data & intelligence layer powering NetApp’s most critical corporate functions — Sales, HR, Finance,"
  },
  {
    "company": "NetApp",
    "source": "netapp_official_careers",
    "job_id": "103118417344",
    "title": "Software Engineer - Cloud & AI Systems",
    "location": "Morrisville, North Carolina, United States; United States",
    "official_url": "https://careers.netapp.com/en/job/morrisville/software-engineer-cloud-and-ai-systems/27600/103118417344",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:19.945214+00:00",
    "date_confidence": "high",
    "description": "Job Summary As a Software Engineer in NetApp’s CPTO organization, you’ll contribute to solving complex engineering challenges and building scalable, reliable solutions for enterpri"
  }
]
```

## Netflix

- Status: ok
- Scraping method: HTTP GET Eightfold server HTML + embedded smartApplyData positions
- Search URL/API: `https://explore.jobs.netflix.net/careers`
- Pagination: first 10 embedded positions per focused role query; PCSX remains disabled
- Pages/requests fetched: 9
- HTTP requests/cumulative request time: 11 / 2.977s
- Company elapsed time: 3.967s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 2 / 31 / 42
- Detail cache statuses: {'fetched:changed': 2, 'reuse_after_error:stale': 17, 'reused': 12}
- Relevant JD recovery: {'cache_reused': 31, 'deterministic_skip': 11, 'eligible': 14, 'ai_skip': 31, 'ai_recover': 1, 'detail_requests': 2, 'detail_success': 2, 'budget_deferred': 0, 'usable_jd': 14}
- Raw jobs found: 90
- After US/location filtering: 56
- With trustworthy posted_date: 56
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.541, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.291, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.301, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.367, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.348, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.65, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.309, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.308, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.282, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}

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
    "fetched_at": "2026-11-25T15:35:48.412227+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR43427",
    "title": "AI Software Engineer (L5) - Machine Learning",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790319332434",
    "posted_date": "2026-11-24",
    "updated_date": "2026-11-24",
    "fetched_at": "2026-11-25T15:35:48.412227+00:00",
    "date_confidence": "high",
    "description": "At Netflix, our mission is to entertain the world. Together, we are writing the next episode - pushing the boundaries of storytelling, global fandom and making the unimaginable a r"
  },
  {
    "company": "Netflix",
    "source": "netflix_official_careers",
    "job_id": "JR43763",
    "title": "Software Engineer 5, AI Observability",
    "location": "Remote, United States",
    "official_url": "https://explore.jobs.netflix.net/careers/job/790319610169",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:35:48.412227+00:00",
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
    "fetched_at": "2026-11-25T15:35:48.412227+00:00",
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
    "fetched_at": "2026-11-25T15:35:48.412227+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.418s
- Company elapsed time: 1.865s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 360, 'usable_jd': 360}
- Raw jobs found: 876
- After US/location filtering: 686
- With trustworthy posted_date: 686
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
    "fetched_at": "2026-11-25T15:35:51.810781+00:00",
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
    "fetched_at": "2026-11-25T15:35:51.810781+00:00",
    "date_confidence": "high",
    "description": "By applying to this role, you will be considered for Research Engineer roles across all teams at OpenAI. About the Role As a Research Engineer here, you will be responsible for bui"
  },
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "2560ed50-5535-42b8-b069-9ebc28ce7493",
    "title": "Researcher, Safety Training",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://jobs.ashbyhq.com/openai/2560ed50-5535-42b8-b069-9ebc28ce7493",
    "posted_date": "2023-05-25",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:51.810781+00:00",
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
    "fetched_at": "2026-11-25T15:35:51.810781+00:00",
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
    "fetched_at": "2026-11-25T15:35:51.810781+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.135s
- Company elapsed time: 0.408s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 2 / 2
- Detail cache statuses: {'reuse_after_error:stale': 2}
- Relevant JD recovery: {'eligible': 180, 'cache_reused': 2, 'ai_skip': 2, 'usable_jd': 180}
- Raw jobs found: 305
- After US/location filtering: 241
- With trustworthy posted_date: 241
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
    "fetched_at": "2026-11-25T15:35:53.677495+00:00",
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
    "fetched_at": "2026-11-25T15:35:53.677495+00:00",
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
    "fetched_at": "2026-11-25T15:35:53.677495+00:00",
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
    "fetched_at": "2026-11-25T15:35:53.677495+00:00",
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
    "fetched_at": "2026-11-25T15:35:53.677495+00:00",
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
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 94 / 15.011s
- Company elapsed time: 28.751s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 69 / 0 / 0
- Detail cache statuses: {'fetched:new': 68, 'fetched:missing_detail': 1}
- Relevant JD recovery: {'eligible': 8, 'usable_jd': 8}
- Raw jobs found: 220
- After US/location filtering: 69
- With trustworthy posted_date: 69
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.073, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.317, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.105, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 3.766, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 2.325, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.556, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.539, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 1.333, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 1.412, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139250",
    "title": "Sr Staff Machine Learning Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923558936",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:54.086510+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139369",
    "title": "Senior Analyst, Data Operations - PayPal Ads",
    "location": "New York City, New York, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923559012",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:54.086510+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139235",
    "title": "Staff Data Scientist",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923558960",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:54.086510+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139121",
    "title": "Senior Manager, Performance Consulting",
    "location": "New York City, New York, United States of America; San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923641918",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:54.086510+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0139248",
    "title": "Machine Learning Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274923558924",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:35:54.086510+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.147s
- Company elapsed time: 0.578s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 13, 'usable_jd': 13}
- Raw jobs found: 146
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
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:36:17.717147+00:00",
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
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:36:17.717147+00:00",
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
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:36:17.717147+00:00",
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
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:36:17.717147+00:00",
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
    "updated_date": "2026-11-25",
    "fetched_at": "2026-11-25T15:36:17.717147+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.057s
- Company elapsed time: 0.058s
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
- HTTP requests/cumulative request time: 1 / 0.115s
- Company elapsed time: 0.450s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 9, 'usable_jd': 9}
- Raw jobs found: 91
- After US/location filtering: 76
- With trustworthy posted_date: 76
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:18.354035+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:18.354035+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:18.354035+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:18.354035+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8265661",
    "title": "Creative Director, Filmmaker for Brand Storytelling",
    "location": "Santa Monica, California; Santa Monica, California, United States",
    "official_url": "https://www.weareroku.com/jobs/8265661?gh_jid=8265661",
    "posted_date": "2026-10-12",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:18.354035+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.149s
- Company elapsed time: 0.744s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 19, 'usable_jd': 19}
- Raw jobs found: 182
- After US/location filtering: 163
- With trustworthy posted_date: 163
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:18.805514+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>The Role</strong></h2> <p>As a Sales Manager, you'll lead a team of Account Executives and own one of our most critical growth levers in-market: developing talent that "
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5317296008",
    "title": "Account Manager, SMB",
    "location": "Sydney, Australia; AU - NSW - Remote",
    "official_url": "http://block.xyz/careers/jobs/5317296008?gh_jid=5317296008",
    "posted_date": "2026-07-09",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:18.805514+00:00",
    "date_confidence": "high",
    "description": "<p>Since we opened our doors in 2009, the world of commerce has evolved immensely, and so has Square. After enabling anyone to take payments and never miss a sale, we saw sellers s"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5490210008",
    "title": "Account Manager, SMB",
    "location": "Sydney, Australia; AU - NSW - Remote",
    "official_url": "http://block.xyz/careers/jobs/5490210008?gh_jid=5490210008",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:18.805514+00:00",
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
    "updated_date": "2026-11-18",
    "fetched_at": "2026-11-25T15:36:18.805514+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:18.805514+00:00",
    "date_confidence": "high",
    "description": "<p>Block is building a new generation of AI-powered products with the potential to create entirely new ways for businesses to operate, engage with customers, and grow. We are looki"
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
- HTTP requests/cumulative request time: 58 / 74.493s
- Company elapsed time: 83.834s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 41 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 41}
- Relevant JD recovery: {'eligible': 36, 'usable_jd': 36}
- Raw jobs found: 116
- After US/location filtering: 41
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 21.415, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 12.503, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 2.847, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 7.12, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 22.871, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.522, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.174, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.769, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 6.611, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 32}

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
    "fetched_at": "2026-11-25T15:36:19.550646+00:00",
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
    "fetched_at": "2026-11-25T15:36:19.550646+00:00",
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
    "fetched_at": "2026-11-25T15:36:19.550646+00:00",
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
    "fetched_at": "2026-11-25T15:36:19.550646+00:00",
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
    "fetched_at": "2026-11-25T15:36:19.550646+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.162s
- Company elapsed time: 0.863s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 50, 'usable_jd': 50}
- Raw jobs found: 352
- After US/location filtering: 280
- With trustworthy posted_date: 280
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:22.839349+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:22.839349+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:22.839349+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:22.839349+00:00",
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
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:22.839349+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.054s
- Company elapsed time: 0.055s
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
- HTTP requests/cumulative request time: 1 / 0.523s
- Company elapsed time: 0.529s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 8
- After US/location filtering: 6
- With trustworthy posted_date: 6
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
    "fetched_at": "2026-11-25T15:36:23.759549+00:00",
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
    "fetched_at": "2026-11-25T15:36:23.759549+00:00",
    "date_confidence": "high",
    "description": "BS/MS/PhD degree in Robotics, Computer Science, Electrical Engineering or equivalent practical experience. Experience in data structures and advanced algorithms Experience programm"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "628b7118-d946-47a2-a03b-ac034622d908",
    "title": "Perception Engineer – ML/CV and Algorithms",
    "location": "San Jose, CA",
    "official_url": "https://jobs.lever.co/weride/628b7118-d946-47a2-a03b-ac034622d908",
    "posted_date": "2020-05-02",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:23.759549+00:00",
    "date_confidence": "high",
    "description": "Research and develop efficient, end-to-end ML solutions for Perception with sensor fusion, including but not limited: Obstacle detection and understanding (e.g. obstacles’ 3D locat"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "0f19452c-ba1b-4d94-ae6d-53ac530bd820",
    "title": "Public Policy & Government Affairs Senior Manager — EU",
    "location": "Europe",
    "official_url": "https://jobs.lever.co/weride/0f19452c-ba1b-4d94-ae6d-53ac530bd820",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:23.759549+00:00",
    "date_confidence": "high",
    "description": "Lead WeRide’s EU public policy and government affairs strategy. Build and manage relationships with the European Commission, European Parliament, EU agencies, Member State governme"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "752dee2b-50d8-4276-97cc-ec1e1f0e1fb7",
    "title": "Senior Software Engineer - Cloud Infrastructure",
    "location": "San Jose, CA",
    "official_url": "https://jobs.lever.co/weride/752dee2b-50d8-4276-97cc-ec1e1f0e1fb7",
    "posted_date": "2023-08-02",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:23.759549+00:00",
    "date_confidence": "high",
    "description": "Architect and develop scalable and reliable PaaS and IaaS platforms to serve the whole company to meet our growing business needs. Architect and develop high performance and scalab"
  }
]
```

## Workday

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.055s
- Company elapsed time: 0.056s
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
- HTTP requests/cumulative request time: 23 / 6.906s
- Company elapsed time: 8.554s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Zillow workday blocked with HTTP 429']

## Zscaler

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/zscaler/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.185s
- Company elapsed time: 1.006s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 20, 'usable_jd': 20}
- Raw jobs found: 396
- After US/location filtering: 236
- With trustworthy posted_date: 236
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
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-25T15:36:26.747524+00:00",
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
    "fetched_at": "2026-11-25T15:36:26.747524+00:00",
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
    "fetched_at": "2026-11-25T15:36:26.747524+00:00",
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
    "updated_date": "2026-10-29",
    "fetched_at": "2026-11-25T15:36:26.747524+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p data-pm-slice=\"1 1 []\">Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and secure. The Z"
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5244297007",
    "title": "Account Executive - DoW - DISA/Fourth Estate",
    "location": "Remote - D.C., USA",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5244297007",
    "posted_date": "2026-10-08",
    "updated_date": "2026-11-11",
    "fetched_at": "2026-11-25T15:36:26.747524+00:00",
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
- HTTP requests/cumulative request time: 12 / 5.753s
- Company elapsed time: 6.001s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 2 / 0 / 0
- Detail cache statuses: {'fetched:new': 2}
- Relevant JD recovery: {'eligible': 2, 'usable_jd': 2}
- Raw jobs found: 8
- After US/location filtering: 2
- With trustworthy posted_date: 2
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.29, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.495, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.536, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.439, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.455, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.503, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.594, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.48, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.568, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

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
    "fetched_at": "2026-11-25T15:36:27.755008+00:00",
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
    "fetched_at": "2026-11-25T15:36:27.755008+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity Chewy's IAM team keeps the right people, services, and AI agents connected to the right access, from someone's first day to their last. As an IAM E"
  }
]
```

## CVS Health

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.049s
- Company elapsed time: 0.050s
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
- HTTP requests/cumulative request time: 1 / 0.087s
- Company elapsed time: 0.215s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 53
- After US/location filtering: 45
- With trustworthy posted_date: 45
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
    "fetched_at": "2026-11-25T15:36:32.950294+00:00",
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
    "fetched_at": "2026-11-25T15:36:32.950294+00:00",
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
    "fetched_at": "2026-11-25T15:36:32.950294+00:00",
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
    "fetched_at": "2026-11-25T15:36:32.950294+00:00",
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
    "fetched_at": "2026-11-25T15:36:32.950294+00:00",
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
- HTTP requests/cumulative request time: 22 / 20.698s
- Company elapsed time: 45.270s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 7 / 74
- Detail cache statuses: {'reused': 7}
- Relevant JD recovery: {'deterministic_skip': 52, 'cache_reused': 7, 'eligible': 7, 'ai_skip': 22, 'usable_jd': 7}
- Raw jobs found: 352
- After US/location filtering: 81
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.25, "first_pass_survivors": 46, "group": "official", "jds_resolved": 0, "original_postings_resolved": 46, "page_budget": 2, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 46, "stop_reason": "page_budget", "unique_contribution": 46, "unique_jobs": 46}
- Query diagnostic: {"elapsed_seconds": 3.202, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 1.552, "first_pass_survivors": 17, "group": "official", "jds_resolved": 0, "original_postings_resolved": 17, "page_budget": 2, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 24, "stop_reason": "early_stop", "unique_contribution": 17, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 1.087, "first_pass_survivors": 11, "group": "official", "jds_resolved": 0, "original_postings_resolved": 11, "page_budget": 2, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 23.902, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 3.66, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 2, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 2.769, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 3.375, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 2.473, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 2, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 43}

Sample normalized records:

```json
[
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164772",
    "title": "Principal AI Engineer, Trust & Evaluation",
    "location": "Toronto, Ontario, Canada; Redwood City, California, United States",
    "official_url": "https://careers.equinix.com/jobs/principal-ai-engineer-trust-evaluation-toronto-ontario-canada-redwood-city-california-united-states",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:33.166449+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164654",
    "title": "Senior AI Engineer. Innovation and R&D",
    "location": "Toronto, Ontario, Canada; Redwood City, California, United States",
    "official_url": "https://careers.equinix.com/jobs/senior-ai-engineer-innovation-and-r-d-toronto-ontario-canada-redwood-city-california-united-states",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:33.166449+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-164652",
    "title": "AI/Machine Learning Experience Engineer",
    "location": "Toronto, Ontario, Canada; Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/ai-machine-learning-experience-engineer-dallas-texas-united-states-toronto-ontario-canada",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:33.166449+00:00",
    "date_confidence": "unknown",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
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
    "fetched_at": "2026-11-25T15:36:33.166449+00:00",
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
    "fetched_at": "2026-11-25T15:36:33.166449+00:00",
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
- HTTP requests/cumulative request time: 10 / 4.340s
- Company elapsed time: 5.216s
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'usable_jd': 0}
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['F5 workday blocked with HTTP 429']

## IXL Learning

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/ixllearning/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.116s
- Company elapsed time: 0.311s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 54, 'usable_jd': 54}
- Raw jobs found: 112
- After US/location filtering: 100
- With trustworthy posted_date: 100
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
    "fetched_at": "2026-11-25T15:36:38.972829+00:00",
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
    "fetched_at": "2026-11-25T15:36:38.972829+00:00",
    "date_confidence": "high",
    "description": "<p><span style=\"font-weight: 400;\">IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide, is seeking a US English Language"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8952868002",
    "title": "Associate Customer Support Analyst, New Grad",
    "location": "Raleigh, NC; Morrisville, North Carolina, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8952868002",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:36:38.972829+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide, is seeking an upbeat, customer-focused, and analytical individua"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8953765002",
    "title": "Associate Customer Support Analyst, New Grad",
    "location": "San Mateo, CA; San Mateo, California, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8953765002",
    "posted_date": "2026-11-19",
    "updated_date": "2026-11-19",
    "fetched_at": "2026-11-25T15:36:38.972829+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, a global edtech leader with personalized learning products used by millions of students worldwide, is seeking an upbeat, customer-focused, and analytical individua"
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
    "fetched_at": "2026-11-25T15:36:38.972829+00:00",
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

- Status: blocked
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- HTTP requests/cumulative request time: 1 / 0.058s
- Company elapsed time: 0.059s
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
- HTTP requests/cumulative request time: 1 / 0.061s
- Company elapsed time: 0.061s
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
- HTTP requests/cumulative request time: 23 / 7.107s
- Company elapsed time: 10.227s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 20 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 5, 'usable_jd': 5}
- Raw jobs found: 45
- After US/location filtering: 20
- With trustworthy posted_date: 20
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 10.227, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "Ansys", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 45}

Sample normalized records:

```json
[
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "103700873856",
    "title": "Professional Services Consulting, Staff Consultant",
    "location": "United States Off-site",
    "official_url": "https://careers.synopsys.com/job/ohio/professional-services-consulting-staff-consultant/44408/103700873856",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:39.404876+00:00",
    "date_confidence": "high",
    "description": "We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling customers to rapidly innovate AI-powered products. We deliver industry-leading silicon desi"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "103259314912",
    "title": "Applications Engineer, Aerospace & Defense",
    "location": "",
    "official_url": "https://careers.synopsys.com/job/united-states/applications-engineer-aerospace-and-defense/44408/103259314912",
    "posted_date": "2026-11-09",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:39.404876+00:00",
    "date_confidence": "high",
    "description": "Must be Based in Hunstville, AL, the surrounding areas, or willing to relocate We Are Synopsys is the leader in engineering solutions from silicon to systems, enabling customers to"
  },
  {
    "company": "Ansys",
    "source": "ansys_official_careers",
    "job_id": "103724938144",
    "title": "Staff Applications Engineer, Electromagnetics",
    "location": "United States Off-site",
    "official_url": "https://careers.synopsys.com/job/michigan/staff-applications-engineer-electromagnetics/44408/103724938144",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:39.404876+00:00",
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
    "fetched_at": "2026-11-25T15:36:39.404876+00:00",
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
    "fetched_at": "2026-11-25T15:36:39.404876+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.044s
- Company elapsed time: 0.044s
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
- HTTP requests/cumulative request time: 1 / 0.061s
- Company elapsed time: 0.061s
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
- HTTP requests/cumulative request time: 1 / 0.052s
- Company elapsed time: 0.053s
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
- HTTP requests/cumulative request time: 1 / 0.043s
- Company elapsed time: 0.043s
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
- HTTP requests/cumulative request time: 2 / 0.280s
- Company elapsed time: 0.315s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 1 / 6 / 51
- Detail cache statuses: {'reused': 6}
- Relevant JD recovery: {'deterministic_skip': 39, 'eligible': 9, 'cache_reused': 6, 'ai_skip': 12, 'detail_requests': 1, 'detail_failure': 1, 'budget_deferred': 0, 'usable_jd': 8}
- Raw jobs found: 83
- After US/location filtering: 76
- With trustworthy posted_date: 76
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
    "fetched_at": "2026-11-25T15:36:46.830819+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "6526fc85-7320-4d6d-adce-5be5e1c1e198",
    "title": "(Canada) Manager, Professional Services",
    "location": "Mississauga, Ontario",
    "official_url": "https://jobs.lever.co/pointclickcare/6526fc85-7320-4d6d-adce-5be5e1c1e198",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:46.830819+00:00",
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
    "fetched_at": "2026-11-25T15:36:46.830819+00:00",
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
    "fetched_at": "2026-11-25T15:36:46.830819+00:00",
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
    "fetched_at": "2026-11-25T15:36:46.830819+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.039s
- Company elapsed time: 0.039s
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
- HTTP requests/cumulative request time: 1 / 0.054s
- Company elapsed time: 0.055s
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
- HTTP requests/cumulative request time: 1 / 0.063s
- Company elapsed time: 0.064s
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
- HTTP requests/cumulative request time: 32 / 5.689s
- Company elapsed time: 6.082s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 26 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 12, 'usable_jd': 12}
- Raw jobs found: 57
- After US/location filtering: 26
- With trustworthy posted_date: 26
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.989, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 1.454, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.482, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.541, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 0.863, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 0.752, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}

Sample normalized records:

```json
[
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1104182",
    "title": "Engineer III - Software Engineer",
    "location": "Irving, Texas; Alpharetta, Georgia; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1104182/engineer-iii-software-engineer/",
    "posted_date": "2026-11-23",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:47.139759+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1103683",
    "title": "Java Full Stack Developer",
    "location": "Temple Terrace, Florida",
    "official_url": "https://mycareer.verizon.com/jobs/r-1103683/java-full-stack-developer/",
    "posted_date": "2026-11-10",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:47.139759+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1104308",
    "title": "Associate Director, AI Center",
    "location": "Alpharetta, Georgia; Irving, Texas; Basking Ridge, New Jersey",
    "official_url": "https://mycareer.verizon.com/jobs/r-1104308/associate-director-ai-center/",
    "posted_date": "2026-11-24",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:47.139759+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1102337",
    "title": "Forward Deployed AI Engineer",
    "location": "Basking Ridge, New Jersey; Alpharetta, Georgia",
    "official_url": "https://mycareer.verizon.com/jobs/r-1102337/forward-deployed-ai-engineer/",
    "posted_date": "2026-11-20",
    "updated_date": "",
    "fetched_at": "2026-11-25T15:36:47.139759+00:00",
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
    "fetched_at": "2026-11-25T15:36:47.139759+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.078s
- Company elapsed time: 0.144s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Relevant JD recovery: {'eligible': 4, 'usable_jd': 4}
- Raw jobs found: 37
- After US/location filtering: 21
- With trustworthy posted_date: 21
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
    "fetched_at": "2026-11-25T15:36:49.632924+00:00",
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
    "fetched_at": "2026-11-25T15:36:49.632924+00:00",
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
    "fetched_at": "2026-11-25T15:36:49.632924+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8046381",
    "title": "Customer Success Manager, Enterprise - Healthcare",
    "location": "Remote - U.S.",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8046381",
    "posted_date": "2026-09-18",
    "updated_date": "2026-11-23",
    "fetched_at": "2026-11-25T15:36:49.632924+00:00",
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
    "fetched_at": "2026-11-25T15:36:49.632924+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
