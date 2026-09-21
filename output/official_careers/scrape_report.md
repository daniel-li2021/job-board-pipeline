# Official careers scrape report — 2026-09-21_0021

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Runtime metrics

- Wall time: 806.477s
- HTTP requests/cumulative request time: 7271 / 2838.287s
- Listing pages/detail fetched/cache reused/prefilter skipped: 1305 / 5924 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 265, 'fetched:new': 5464}

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 47
- HTTP requests/cumulative request time: 47 / 11.191s
- Company elapsed time: 27.854s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 888
- After US/location filtering: 317
- With trustworthy posted_date: 317
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.059, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "\"Ai Engineer\"", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 1.889, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Machine Learning Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.833, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Data Scientist\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.249, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "\"Solutions Architect\"", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.174, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "\"Data Engineer\"", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 1.988, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "\"Platform Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.024, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Full Stack Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.988, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "\"Forward Deployed Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.903, "first_pass_survivors": 136, "group": "official", "jds_resolved": 136, "original_postings_resolved": 136, "page_budget": 12, "pages_fetched": 12, "query": "\"Software Engineer\"", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 136, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.821, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "\"Infrastructure Engineer\"", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.668, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 5, "pages_fetched": 5, "query": "\"Software Engineer III\"", "raw_jobs": 86, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 86}
- Query diagnostic: {"elapsed_seconds": 1.282, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 2, "query": "\"Web Solutions Engineer\"", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 40}
- Query diagnostic: {"elapsed_seconds": 0.976, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 2, "pages_fetched": 2, "query": "\"DeepMind\"", "raw_jobs": 38, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 38}

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "76331955745891014",
    "title": "Software Engineer III, AI/ML, Google Ads",
    "location": "Irvine, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/76331955745891014-software-engineer-iii-ai-ml-google-ads",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:21:09.848769+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "112803830181044934",
    "title": "Senior Software Engineer, Gemini Enterprise Mobile (iOS",
    "location": "Sunnyvale, CA, USA; New York, NY, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/112803830181044934-senior-software-engineer-gemini-enterprise-mobile-ios",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:21:09.848769+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "116667514041049798",
    "title": "Software Engineer III, Search Data and ML Platform",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/116667514041049798-software-engineer-iii-search-data-and-ml-platform",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:21:09.848769+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "86584875905098438",
    "title": "Software Engineer, Core Runtime, BigQuery",
    "location": "Kirkland, WA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/86584875905098438-software-engineer-core-runtime-bigquery",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:21:09.848769+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "108518356373381830",
    "title": "Senior Software Engineer, Mobile (iOS), YouTube",
    "location": "San Bruno, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/108518356373381830-senior-software-engineer-mobile-ios-youtube",
    "posted_date": "2026-07-28",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:21:09.848769+00:00",
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
- Pages/requests fetched: 43
- HTTP requests/cumulative request time: 43 / 14.534s
- Company elapsed time: 26.234s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 805
- After US/location filtering: 696
- With trustworthy posted_date: 696
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.311, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 1.022, "first_pass_survivors": 36, "group": "official", "jds_resolved": 36, "original_postings_resolved": 36, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 38, "stop_reason": "early_stop", "unique_contribution": 36, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 1.99, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.109, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.895, "first_pass_survivors": 57, "group": "official", "jds_resolved": 57, "original_postings_resolved": 57, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 57, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.709, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 0.25, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.283, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 7.578, "first_pass_survivors": 213, "group": "official", "jds_resolved": 213, "original_postings_resolved": 213, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 213, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 1.681, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.821, "first_pass_survivors": 55, "group": "official", "jds_resolved": 55, "original_postings_resolved": 55, "page_budget": 3, "pages_fetched": 3, "query": "systems development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 55, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.394, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "site reliability engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.189, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 2, "pages_fetched": 2, "query": "applied scientist", "raw_jobs": 40, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 40}

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10543908",
    "title": "AI Platform Data Engineer, Ring Decision Science, Ring Decision Science",
    "location": "Hawthorne, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10543908/ai-platform-data-engineer-ring-decision-science-ring-decision-science",
    "posted_date": "2026-09-15",
    "updated_date": "2026-09-20",
    "fetched_at": "2026-09-21T00:21:09.849588+00:00",
    "date_confidence": "high",
    "description": "We seek an AI Platform Builder—a Data Engineer focused on developing Platforms and Agentic AI solution—who embraces prompt-driven development with strong technical, analytical, com"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10547170",
    "title": "Software Development Engineer, Specialist AI Tooling, Specialist Technology Team",
    "location": "Austin, Texas, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10547170/software-development-engineer-specialist-ai-tooling-specialist-technology-team",
    "posted_date": "2026-09-16",
    "updated_date": "2026-09-21",
    "fetched_at": "2026-09-21T00:21:09.849588+00:00",
    "date_confidence": "high",
    "description": "AWS Specialist Technology Team (STT) is seeking a Software Development Engineer to join the Specialist AI Tooling engineering team - the group building AI-native, agentic solutions"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10545829",
    "title": "Software Development Engineer, Agentic AI, Velocity Labs",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10545829/software-development-engineer-agentic-ai-velocity-labs",
    "posted_date": "2026-09-16",
    "updated_date": "2026-09-21",
    "fetched_at": "2026-09-21T00:21:09.849588+00:00",
    "date_confidence": "high",
    "description": "The Velocity Labs team mission is to think beyond the confines of the normal product-orientated approach and to discover new ways to apply and embrace agentic AI. We have noticed h"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10545820",
    "title": "Software Development Engineer, Agentic AI, Velocity Labs",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10545820/software-development-engineer-agentic-ai-velocity-labs",
    "posted_date": "2026-09-16",
    "updated_date": "2026-09-20",
    "fetched_at": "2026-09-21T00:21:09.849588+00:00",
    "date_confidence": "high",
    "description": "The Velocity Labs team mission is to think beyond the confines of the normal product-orientated approach and to discover new ways to apply and embrace agentic AI. We have noticed h"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10545408",
    "title": "Sr. Software Development Engineer, Agentic AI, Velocity Labs",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10545408/sr-software-development-engineer-agentic-ai-velocity-labs",
    "posted_date": "2026-09-16",
    "updated_date": "2026-09-21",
    "fetched_at": "2026-09-21T00:21:09.849588+00:00",
    "date_confidence": "high",
    "description": "The Velocity Labs team mission is to think beyond the confines of the normal product-orientated approach and to discover new ways to apply and embrace agentic AI. We have noticed h"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=ai+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 42
- HTTP requests/cumulative request time: 42 / 16.441s
- Company elapsed time: 31.462s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 840
- After US/location filtering: 287
- With trustworthy posted_date: 287
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.446, "first_pass_survivors": 120, "group": "official", "jds_resolved": 120, "original_postings_resolved": 120, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 120, "unique_jobs": 120}
- Query diagnostic: {"elapsed_seconds": 2.141, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.158, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.092, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.206, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.078, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.166, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.746, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.785, "first_pass_survivors": 122, "group": "official", "jds_resolved": 122, "original_postings_resolved": 122, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 240, "stop_reason": "page_budget", "unique_contribution": 122, "unique_jobs": 240}
- Query diagnostic: {"elapsed_seconds": 2.644, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "apps-and-frameworks-SFTWR-AF", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200683893-3956",
    "title": "AI Data & Infrastructure Engineer",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200683893/ai-data-infrastructure-engineer",
    "posted_date": "2026-09-20",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.851388+00:00",
    "date_confidence": "high",
    "description": "Imagine what you could do here. At Apple, we believe new insights have a way of becoming excellent products, services, and customer experiences very quickly. Bring passion and dedi"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200683922-3401",
    "title": "Thin-Film/ALD Engineer",
    "location": "San Francisco Bay Area, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200683922/thin-film-ald-engineer",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.851388+00:00",
    "date_confidence": "high",
    "description": "We are seeking an experienced and knowledgeable Thin-film /ALD Engineer with a strong background in vacuum systems to lead technical initiatives and process improvements as related"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200683324-3337",
    "title": "Senior Graphics Software Engineer",
    "location": "Seattle, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200683324/senior-graphics-software-engineer",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.851388+00:00",
    "date_confidence": "high",
    "description": "Summary: Apple's ProVideo Software team pushes the boundaries of what's possible in image and video processing, delivering breakthrough visual experiences to hundreds of millions o"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200683324-0670",
    "title": "Senior Graphics Software Engineer",
    "location": "Culver City, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200683324/senior-graphics-software-engineer",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.851388+00:00",
    "date_confidence": "high",
    "description": "Summary: Apple's ProVideo Software team pushes the boundaries of what's possible in image and video processing, delivering breakthrough visual experiences to hundreds of millions o"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200683324-3543",
    "title": "Senior Graphics Software Engineer",
    "location": "San Diego, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200683324/senior-graphics-software-engineer",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.851388+00:00",
    "date_confidence": "high",
    "description": "Summary: Apple's ProVideo Software team pushes the boundaries of what's possible in image and video processing, delivering breakthrough visual experiences to hundreds of millions o"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 39
- HTTP requests/cumulative request time: 233 / 58.268s
- Company elapsed time: 92.002s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 193 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 14, 'fetched:new': 179}
- Raw jobs found: 390
- After US/location filtering: 193
- With trustworthy posted_date: 193
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 26.611, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 6, "pages_fetched": 6, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.269, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 11.012, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 6.83, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.274, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.697, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.572, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 7.727, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 25.497, "first_pass_survivors": 49, "group": "official", "jds_resolved": 49, "original_postings_resolved": 49, "page_budget": 12, "pages_fetched": 12, "query": "software engineer", "raw_jobs": 120, "stop_reason": "page_budget", "unique_contribution": 49, "unique_jobs": 120}

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200055918",
    "title": "Software Engineer II - Full Stack",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556999241",
    "posted_date": "2026-09-20",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.852511+00:00",
    "date_confidence": "high",
    "description": "Overview Are you a customer-obsessed, AI-curious problem-solver who thrives in an inclusive, collaborative global team? Join Engineering Operations (EngOps) – the organization driv"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200052807",
    "title": "Solution Engineer - AI Business Process",
    "location": "United States, Multiple Locations, Multiple Locations",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556984043",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.852511+00:00",
    "date_confidence": "high",
    "description": "Overview Our purpose is to empower organizations to transform the way they work by harnessing the full potential of artificial intelligence. We guide customers through the evolving"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200057051",
    "title": "Hardware Engineering Internship (6-Month Program)",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557002608",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.852511+00:00",
    "date_confidence": "high",
    "description": "Overview Come build community, explore your passions and do your best work at Microsoft with thousands of University interns from every corner of the world. This opportunity will a"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200056606",
    "title": "Software Engineer II - Excel Team",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557001308",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.852511+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Excel is where hundreds of millions of people bring data, decisions, and work together. The Excel team is building the next generation of AI-powered spreadsheet "
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200056381",
    "title": "Principal Software Engineer, Minecaft Creator - Minecraft",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393557000669",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:09.852511+00:00",
    "date_confidence": "high",
    "description": "Overview At Mojang Studios, the creators of Minecraft, we are on a mission to build a better world through the power of play. Why play? Well, play is at the heart of everything we "
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 511 / 229.986s
- Company elapsed time: 296.845s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 478 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 4, 'fetched:new': 474}
- Raw jobs found: 640
- After US/location filtering: 478
- With trustworthy posted_date: 478
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 50.405, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 35.869, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 29.838, "first_pass_survivors": 47, "group": "official", "jds_resolved": 47, "original_postings_resolved": 47, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 47, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 32.367, "first_pass_survivors": 49, "group": "official", "jds_resolved": 49, "original_postings_resolved": 49, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 49, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 27.47, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 26.173, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 26.176, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 19.775, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 28.834, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 18.421, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}

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
    "fetched_at": "2026-09-21T00:21:09.853278+00:00",
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
    "fetched_at": "2026-09-21T00:21:09.853278+00:00",
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
    "fetched_at": "2026-09-21T00:21:09.853278+00:00",
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
    "fetched_at": "2026-09-21T00:21:09.853278+00:00",
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
    "fetched_at": "2026-09-21T00:21:09.853278+00:00",
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
- HTTP requests/cumulative request time: 188 / 57.794s
- Company elapsed time: 83.088s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 163 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 7, 'fetched:new': 156}
- Raw jobs found: 433
- After US/location filtering: 163
- With trustworthy posted_date: 163
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 33.36, "first_pass_survivors": 78, "group": "official", "jds_resolved": 78, "original_postings_resolved": 78, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 78, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 5.655, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 3.864, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 11.496, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.183, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.219, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.538, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 29, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 29}
- Query diagnostic: {"elapsed_seconds": 5.148, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 6.796, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 1.24, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "software engineering mts", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 10}

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR360326",
    "title": "Senior backend Engineer - Java",
    "location": "California - San Francisco; California - Palo Alto",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Senior-backend-Engineer---Java_JR360326",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:36.083924+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR360316",
    "title": "Senior Software Engineer",
    "location": "California - Palo Alto; Washington - Seattle; Washington - Bellevue; California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---Palo-Alto/Senior-Software-Engineer_JR360316",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:36.083924+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR358761",
    "title": "Senior Cloud Platform Engineer (SMTS)",
    "location": "Washington - Bellevue; California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Washington---Bellevue/Senior-Cloud-Platform-Engineer--SMTS-_JR358761",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:36.083924+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR351123",
    "title": "Security Practices Director",
    "location": "California - Remote; Arizona - Remote; New Jersey - Remote; Washington - Remote; New York - Remote; Virginia - Remote; Texas - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---Remote/Services-Practices-Director_JR351123",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:36.083924+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Customer Success Jo"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR355122",
    "title": "Manager, Compliance - Public Sector Contracts",
    "location": "Virginia - Mclean; District of Columbia - Washington; Illinois - Chicago; Georgia - Atlanta; Indiana - Indianapolis; Texas - Austin",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Virginia---Mclean/Manager--Compliance---Public-Sector-Contracts_JR355122",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:36.083924+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Global Affairs Job "
  }
]
```

## Adobe

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://adobe.wd5.myworkdayjobs.com/external_experienced`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 261 / 122.508s
- Company elapsed time: 159.218s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 228 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 5, 'fetched:new': 223}
- Raw jobs found: 616
- After US/location filtering: 228
- With trustworthy posted_date: 228
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 59.468, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 14.767, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.024, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 23.437, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.411, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.426, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.977, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 3.999, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.892, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 5.025, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "software development engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}

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
    "fetched_at": "2026-09-21T00:21:37.703477+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are looking for a hands-on AI Agent Engineer to develop, build, and maintain intelligent agents that drive automation and business impact across the enterprise. "
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
    "fetched_at": "2026-09-21T00:21:37.703477+00:00",
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
    "fetched_at": "2026-09-21T00:21:37.703477+00:00",
    "date_confidence": "high",
    "description": "Senior SRE — RTCDP Datastores & AI/ML Ops Adobe’s Real-Time Customer Data Platform (RTCDP) powers personalized experiences for some of the world’s largest brands. As a Senior SRE o"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R168858",
    "title": "Senior Applied AI Engineer– Creative Systems & Brand Intelligence, Adobe Express",
    "location": "San Francisco; San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Francisco/Senior-Applied-AI-Engineer--Creative-Systems---Brand-Intelligence--Adobe-Express_R168858",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:37.703477+00:00",
    "date_confidence": "high",
    "description": "The Opportunity Our pillar, Assets and Collaboration, focuses on building foundational capabilities in Adobe Express that help users create, organize, govern, and collaborate on co"
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
    "fetched_at": "2026-09-21T00:21:37.703477+00:00",
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
- HTTP requests/cumulative request time: 15 / 4.837s
- Company elapsed time: 5.777s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 1971
- After US/location filtering: 603
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.668, "first_pass_survivors": 362, "group": "official", "jds_resolved": 0, "original_postings_resolved": 362, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 450, "stop_reason": "page_budget", "unique_contribution": 362, "unique_jobs": 450}
- Query diagnostic: {"elapsed_seconds": 0.424, "first_pass_survivors": 18, "group": "official", "jds_resolved": 0, "original_postings_resolved": 18, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 0.371, "first_pass_survivors": 33, "group": "official", "jds_resolved": 0, "original_postings_resolved": 33, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 106, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 106}
- Query diagnostic: {"elapsed_seconds": 0.459, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 148, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 148}
- Query diagnostic: {"elapsed_seconds": 0.554, "first_pass_survivors": 127, "group": "official", "jds_resolved": 0, "original_postings_resolved": 127, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 526, "stop_reason": "page_budget", "unique_contribution": 127, "unique_jobs": 526}
- Query diagnostic: {"elapsed_seconds": 0.447, "first_pass_survivors": 22, "group": "official", "jds_resolved": 0, "original_postings_resolved": 22, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 309, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 309}
- Query diagnostic: {"elapsed_seconds": 0.449, "first_pass_survivors": 1, "group": "official", "jds_resolved": 0, "original_postings_resolved": 1, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 0.404, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 18, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 0.756, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 293, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 293}

Sample normalized records:

```json
[
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2129036344653746",
    "title": "Program Management Manager, Fleet Health, Reliability, and Central Engineering",
    "location": "Menlo Park, CA; Remote, US",
    "official_url": "https://www.metacareers.com/jobs/2129036344653746",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:41.314072+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1809721810184545",
    "title": "Software Engineer - Host Networking",
    "location": "Bellevue, WA; Menlo Park, CA; New York, NY",
    "official_url": "https://www.metacareers.com/jobs/1809721810184545",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:41.314072+00:00",
    "date_confidence": "unknown",
    "description": ""
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
    "fetched_at": "2026-09-21T00:21:41.314072+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1050754181130466",
    "title": "Software Engineering Manager",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/1050754181130466",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:41.314072+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1031032768371242",
    "title": "Production Engineer",
    "location": "Remote, US; Bellevue, WA; Menlo Park, CA; Seattle, WA; Burlingame, CA; Boston, MA; New York, NY; Fremont, CA",
    "official_url": "https://www.metacareers.com/jobs/1031032768371242",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:41.314072+00:00",
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
- HTTP requests/cumulative request time: 26 / 23.226s
- Company elapsed time: 27.453s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 1241
- After US/location filtering: 723
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.818, "first_pass_survivors": 200, "group": "official", "jds_resolved": 200, "original_postings_resolved": 200, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 200, "unique_jobs": 200}
- Query diagnostic: {"elapsed_seconds": 2.884, "first_pass_survivors": 132, "group": "official", "jds_resolved": 132, "original_postings_resolved": 132, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 132, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.274, "first_pass_survivors": 114, "group": "official", "jds_resolved": 114, "original_postings_resolved": 114, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 114, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.845, "first_pass_survivors": 84, "group": "official", "jds_resolved": 84, "original_postings_resolved": 84, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 84, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 4.023, "first_pass_survivors": 64, "group": "official", "jds_resolved": 64, "original_postings_resolved": 64, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 64, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.769, "first_pass_survivors": 63, "group": "official", "jds_resolved": 63, "original_postings_resolved": 63, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 63, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 1.574, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 90, "stop_reason": "early_stop", "unique_contribution": 22, "unique_jobs": 90}
- Query diagnostic: {"elapsed_seconds": 0.624, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 4.641, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 200, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 200}

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
    "fetched_at": "2026-09-21T00:21:47.092611+00:00",
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
    "fetched_at": "2026-09-21T00:21:47.092611+00:00",
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
    "fetched_at": "2026-09-21T00:21:47.092611+00:00",
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
    "fetched_at": "2026-09-21T00:21:47.092611+00:00",
    "date_confidence": "unknown",
    "description": "The Commercial AI-CRM and Transaction team focuses on TikTok advertiser growth algorithms. Leveraging deep learning and large language model technologies, the team builds an algori"
  },
  {
    "company": "TikTok",
    "source": "tiktok_official_careers",
    "job_id": "7667934792727906565",
    "title": "Research Engineer Intern, Agentic Systems & AI Infrastructure (TikTok-Generalized Arch) - 2027 Summer",
    "location": "Seattle, Washington, United States of America",
    "official_url": "https://lifeattiktok.com/search/7667934792727906565",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:21:47.092611+00:00",
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
- HTTP requests/cumulative request time: 157 / 47.663s
- Company elapsed time: 69.489s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 130 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 128}
- Raw jobs found: 502
- After US/location filtering: 130
- With trustworthy posted_date: 130
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.691, "first_pass_survivors": 62, "group": "official", "jds_resolved": 62, "original_postings_resolved": 62, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 69, "stop_reason": "page_budget", "unique_contribution": 62, "unique_jobs": 69}
- Query diagnostic: {"elapsed_seconds": 8.926, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.546, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 7.857, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 8.72, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.044, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.569, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.826, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 4.309, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 80}

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
    "fetched_at": "2026-09-21T00:22:14.546380+00:00",
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
    "fetched_at": "2026-09-21T00:22:14.546380+00:00",
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
    "fetched_at": "2026-09-21T00:22:14.546380+00:00",
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
    "fetched_at": "2026-09-21T00:22:14.546380+00:00",
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
    "fetched_at": "2026-09-21T00:22:14.546380+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.547s
- Company elapsed time: 2.519s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 462
- After US/location filtering: 460
- With trustworthy posted_date: 460
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
    "updated_date": "2026-09-17",
    "fetched_at": "2026-09-21T00:22:41.855419+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8068432",
    "title": "Account Executive, Emerging Markets",
    "location": "Atlanta, GA; Tempe, AZ; Tampa, FL; Raleigh, NC; Nashville, TN; Las Vegas, NV; Dallas, TX; Houston, TX; Tempe, AZ",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8068432",
    "posted_date": "2026-07-15",
    "updated_date": "2026-09-17",
    "fetched_at": "2026-09-21T00:22:41.855419+00:00",
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
    "updated_date": "2026-09-17",
    "fetched_at": "2026-09-21T00:22:41.855419+00:00",
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
    "updated_date": "2026-09-17",
    "fetched_at": "2026-09-21T00:22:41.855419+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8114531",
    "title": "Account Manager, CPG Enterprise Ad Sales",
    "location": "Chicago, IL",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8114531",
    "posted_date": "2026-08-10",
    "updated_date": "2026-09-17",
    "fetched_at": "2026-09-21T00:22:41.855419+00:00",
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
- HTTP requests/cumulative request time: 117 / 40.145s
- Company elapsed time: 56.038s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 93 / 0 / 0
- Detail cache statuses: {'fetched:new': 93}
- Raw jobs found: 328
- After US/location filtering: 93
- With trustworthy posted_date: 93
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 22.669, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.514, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 0.656, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 5.008, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 6.145, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.562, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.08, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.696, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 5.975, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 74, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 74}

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
    "posted_date": "2026-06-23",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:22:44.374838+00:00",
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
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:22:44.374838+00:00",
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
    "fetched_at": "2026-09-21T00:22:44.374838+00:00",
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
    "fetched_at": "2026-09-21T00:22:44.374838+00:00",
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
    "fetched_at": "2026-09-21T00:22:44.374838+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.184s
- Company elapsed time: 0.607s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 161
- After US/location filtering: 116
- With trustworthy posted_date: 116
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:22:59.173220+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8089344",
    "title": "Agency Lead, Independents",
    "location": "Los Angeles, CA, US; Chicago, IL, US; New York, NY, US; New York, NY, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8089344",
    "posted_date": "2026-08-14",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:22:59.173220+00:00",
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
    "updated_date": "2026-09-17",
    "fetched_at": "2026-09-21T00:22:59.173220+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:22:59.173220+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:22:59.173220+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.297s
- Company elapsed time: 0.709s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 345
- After US/location filtering: 258
- With trustworthy posted_date: 258
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
    "fetched_at": "2026-09-21T00:22:59.780526+00:00",
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
    "fetched_at": "2026-09-21T00:22:59.780526+00:00",
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
    "fetched_at": "2026-09-21T00:22:59.780526+00:00",
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
    "fetched_at": "2026-09-21T00:22:59.780526+00:00",
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
    "fetched_at": "2026-09-21T00:22:59.780526+00:00",
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
- HTTP requests/cumulative request time: 393 / 160.621s
- Company elapsed time: 209.299s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 373 / 0 / 0
- Detail cache statuses: {'fetched:new': 373}
- Raw jobs found: 1631
- After US/location filtering: 373
- With trustworthy posted_date: 373
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 144.979, "first_pass_survivors": 268, "group": "official", "jds_resolved": 268, "original_postings_resolved": 268, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 268, "stop_reason": "early_stop", "unique_contribution": 268, "unique_jobs": 268}
- Query diagnostic: {"elapsed_seconds": 0.399, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 93, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 93}
- Query diagnostic: {"elapsed_seconds": 8.424, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 160, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 160}
- Query diagnostic: {"elapsed_seconds": 48.286, "first_pass_survivors": 88, "group": "official", "jds_resolved": 88, "original_postings_resolved": 88, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 249, "stop_reason": "page_budget", "unique_contribution": 88, "unique_jobs": 249}
- Query diagnostic: {"elapsed_seconds": 1.595, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 258, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 258}
- Query diagnostic: {"elapsed_seconds": 2.696, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 265, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 265}
- Query diagnostic: {"elapsed_seconds": 0.397, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 57, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 57}
- Query diagnostic: {"elapsed_seconds": 0.39, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 51, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 51}
- Query diagnostic: {"elapsed_seconds": 2.132, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 230, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 230}

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075536",
    "title": "Staff Inbound Product Manager - ServiceNow University",
    "location": "San Diego, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000150513709-staff-inbound-product-manager-servicenow-university",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:00.493109+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075253",
    "title": "Staff Software Engineer - AI Search",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000150494819-staff-software-engineer-ai-search",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:00.493109+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074848",
    "title": "Senior Manager - Machine Learning Engineering",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000150494699-senior-manager-machine-learning-engineering",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:00.493109+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075429",
    "title": "Principal Technical Program Manager",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000150471979-principal-technical-program-manager",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:00.493109+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075440",
    "title": "Senior Staff Strategic Operations",
    "location": "San Diego, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000150471599-senior-staff-strategic-operations",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:00.493109+00:00",
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
- HTTP requests/cumulative request time: 6 / 1.570s
- Company elapsed time: 2.615s
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
- HTTP requests/cumulative request time: 54 / 51.371s
- Company elapsed time: 63.823s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 25 / 0 / 0
- Detail cache statuses: {'fetched:new': 25}
- Raw jobs found: 348
- After US/location filtering: 25
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.569, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 47}
- Query diagnostic: {"elapsed_seconds": 4.099, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 4.148, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 4.147, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 4.137, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 4.053, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 4.136, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 4.075, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 5.459, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 48, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 47}

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22196",
    "title": "Subscriptions Editor",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Subscriptions-Editor/22196",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:26.651935+00:00",
    "date_confidence": "unknown",
    "description": "Subscriptions Editor"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22190",
    "title": "Head of Benefits, Americas, Team Leader",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Head-of-Benefits-Americas-Team-Leader/22190",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:26.651935+00:00",
    "date_confidence": "unknown",
    "description": "Head of Benefits, Americas, Team Leader"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22182",
    "title": "Accounting Analyst, ESG Controller - Chief Accounting Office",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Accounting-Analyst-ESG-Controller-Chief-Accounting-Office/22182",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:26.651935+00:00",
    "date_confidence": "unknown",
    "description": "Accounting Analyst, ESG Controller - Chief Accounting Office"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22189",
    "title": "Product Manager, Alternative Data - Data Evaluations and Onboarding",
    "location": "San Francisco, California, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Product-Manager-Alternative-Data-Data-Evaluations-and-Onboarding/22189",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:26.651935+00:00",
    "date_confidence": "unknown",
    "description": "Product Manager, Alternative Data - Data Evaluations and Onboarding"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "22187",
    "title": "Product Manager, Alternative Data - Data Evaluations and Onboarding",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Product-Manager-Alternative-Data-Data-Evaluations-and-Onboarding/22187",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:26.651935+00:00",
    "date_confidence": "unknown",
    "description": "Product Manager, Alternative Data - Data Evaluations and Onboarding"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 64
- HTTP requests/cumulative request time: 599 / 128.938s
- Company elapsed time: 210.552s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 535 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 25, 'fetched:new': 509}
- Raw jobs found: 1273
- After US/location filtering: 534
- With trustworthy posted_date: 534
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 18.26, "first_pass_survivors": 51, "group": "official", "jds_resolved": 51, "original_postings_resolved": 51, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 51, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 13.626, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.557, "first_pass_survivors": 38, "group": "official", "jds_resolved": 38, "original_postings_resolved": 38, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 38, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 14.603, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.019, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.305, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.704, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.999, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.778, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 12.257, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "full stack", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.938, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "python react", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.721, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "pyspark databricks", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 8.679, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "experienced software engineer java python", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.655, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "agentic ai", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.015, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.913, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "software engineer ii", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.705, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "infrastructure engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.325, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "security engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.768, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "quantitative developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.829, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "software engineer java spring", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.535, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "software engineer python authe", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 1.481, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "aws data platform engineer", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.398, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "data engineer applied ai", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 3.479, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 1, "pages_fetched": 1, "query": "asset management technology", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 20}

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
    "fetched_at": "2026-09-21T00:23:40.413960+00:00",
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
    "fetched_at": "2026-09-21T00:23:40.413960+00:00",
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
    "fetched_at": "2026-09-21T00:23:40.413960+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorgan Chase, within the Co"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210787972",
    "title": "Sr Lead Software Engineer - AI Engineer",
    "location": "Columbus, OH, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210787972",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:23:40.413960+00:00",
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
    "fetched_at": "2026-09-21T00:23:40.413960+00:00",
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
- HTTP requests/cumulative request time: 155 / 40.610s
- Company elapsed time: 63.102s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 127 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 42, 'fetched:new': 85}
- Raw jobs found: 527
- After US/location filtering: 127
- With trustworthy posted_date: 127
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 31.148, "first_pass_survivors": 74, "group": "official", "jds_resolved": 74, "original_postings_resolved": 74, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 74, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.379, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.937, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.364, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.513, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.297, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.522, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.851, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 2.768, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 80}

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001157",
    "title": "Capital One Shopping Tech, Staff Full Stack Engineer, Technical Chief of Staff (Remote - Eligible)",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Capital-One-Shopping-Tech--Staff-Full-Stack-Engineer--Technical-Chief-of-Staff--Remote---Eligible-_R1001157",
    "posted_date": "2026-09-20",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:24:16.922012+00:00",
    "date_confidence": "high",
    "description": "Capital One Shopping Tech, Staff Full Stack Engineer, Technical Chief of Staff (Remote - Eligible) Capital One Shopping is a product organization that operates autonomously within "
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001236",
    "title": "Full-stack Engineer 4 (Manager, IC)",
    "location": "Richmond, VA; McLean, VA; Cambridge, MA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Richmond-VA/Full-stack-Engineer-4--Manager--IC-_R1001236-1",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:24:16.922012+00:00",
    "date_confidence": "high",
    "description": "Full-stack Engineer 4 (Manager, IC) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, incl"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001234",
    "title": "Full-stack Engineer 5 (Senior Manager, IC)",
    "location": "Richmond, VA; McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Richmond-VA/Full-stack-Engineer-5--Senior-Manager--IC-_R1001234-1",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:24:16.922012+00:00",
    "date_confidence": "high",
    "description": "Full-stack Engineer 5 (Senior Manager, IC) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborativ"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001230",
    "title": "Data Engineer 4 (Manager, IC)",
    "location": "Richmond, VA; McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Richmond-VA/Data-Engineer-4--Manager--IC-_R1001230-1",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:24:16.922012+00:00",
    "date_confidence": "high",
    "description": "Data Engineer 4 (Manager, IC) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclusive "
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R1001226",
    "title": "Full-stack Engineer 5 (Senior Manager, IC)",
    "location": "McLean, VA; Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Full-stack-Engineer-5--Senior-Manager--IC-_R1001226-2",
    "posted_date": "2026-09-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:24:16.922012+00:00",
    "date_confidence": "high",
    "description": "Full-stack Engineer 5 (Senior Manager, IC) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborativ"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 41
- HTTP requests/cumulative request time: 518 / 119.621s
- Company elapsed time: 189.601s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 477 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 7, 'fetched:new': 470}
- Raw jobs found: 817
- After US/location filtering: 477
- With trustworthy posted_date: 477
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 27.818, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 76, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 13.807, "first_pass_survivors": 35, "group": "official", "jds_resolved": 35, "original_postings_resolved": 35, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 35, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.344, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 15.465, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.11, "first_pass_survivors": 50, "group": "official", "jds_resolved": 50, "original_postings_resolved": 50, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 50, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.792, "first_pass_survivors": 48, "group": "official", "jds_resolved": 48, "original_postings_resolved": 48, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 48, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.3, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 10.735, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 13.606, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 79, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 79}
- Query diagnostic: {"elapsed_seconds": 15.879, "first_pass_survivors": 43, "group": "official", "jds_resolved": 43, "original_postings_resolved": 43, "page_budget": 3, "pages_fetched": 3, "query": "core infrastructure", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 43, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 13.364, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 3, "pages_fetched": 3, "query": "cleared site reliability engineer database", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.922, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "software developer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 15.459, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "applications developer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 60}

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
    "fetched_at": "2026-09-21T00:24:30.476173+00:00",
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
    "fetched_at": "2026-09-21T00:24:30.476173+00:00",
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
    "fetched_at": "2026-09-21T00:24:30.476173+00:00",
    "date_confidence": "high",
    "description": "As a Senior Software Engineer within Oracle Cloud Infrastructure (OCI), you’ll have the opportunity to solve large-scale, mission-critical engineering challenges with broad technic"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "336161",
    "title": "Senior Principal AI Agent / ML Engineer (OCI)",
    "location": "Seattle, WA, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/336161",
    "posted_date": "2026-06-11",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:24:30.476173+00:00",
    "date_confidence": "high",
    "description": "The Senior Principal AI Agent / ML Software Engineer is a Senior Staff-level, hands-on technical leadership role responsible for defining, building, and operating next-generation A"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "342714",
    "title": "Principal Platform Software Engineer, AI",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/342714",
    "posted_date": "2026-08-14",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:24:30.476173+00:00",
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
- HTTP requests/cumulative request time: 400 / 250.708s
- Company elapsed time: 304.980s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 371 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 44, 'fetched:new': 327}
- Raw jobs found: 547
- After US/location filtering: 371
- With trustworthy posted_date: 371
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 55.485, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 34.083, "first_pass_survivors": 49, "group": "official", "jds_resolved": 49, "original_postings_resolved": 49, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 49, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 39.803, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 54.38, "first_pass_survivors": 42, "group": "official", "jds_resolved": 42, "original_postings_resolved": 42, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 42, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 21.131, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 31.72, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 33.8, "first_pass_survivors": 39, "group": "official", "jds_resolved": 39, "original_postings_resolved": 39, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 39, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.838, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 18.733, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 9.998, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 1, "pages_fetched": 1, "query": "usa software engineer ii", "raw_jobs": 20, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 20}

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
    "fetched_at": "2026-09-21T00:25:20.025234+00:00",
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
    "fetched_at": "2026-09-21T00:25:20.025234+00:00",
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
    "fetched_at": "2026-09-21T00:25:20.025234+00:00",
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
    "fetched_at": "2026-09-21T00:25:20.025234+00:00",
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
    "fetched_at": "2026-09-21T00:25:20.025234+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.348s
- Company elapsed time: 1.428s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 379
- After US/location filtering: 375
- With trustworthy posted_date: 375
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
    "fetched_at": "2026-09-21T00:26:06.699541+00:00",
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
    "updated_date": "2026-09-15",
    "fetched_at": "2026-09-21T00:26:06.699541+00:00",
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
    "fetched_at": "2026-09-21T00:26:06.699541+00:00",
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
    "fetched_at": "2026-09-21T00:26:06.699541+00:00",
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
    "fetched_at": "2026-09-21T00:26:06.699541+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.264s
- Company elapsed time: 1.102s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 665
- After US/location filtering: 390
- With trustworthy posted_date: 390
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
    "fetched_at": "2026-09-21T00:26:08.127928+00:00",
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
    "fetched_at": "2026-09-21T00:26:08.127928+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:26:08.127928+00:00",
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
    "updated_date": "2026-09-15",
    "fetched_at": "2026-09-21T00:26:08.127928+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s largest enterprises to the most am"
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
    "fetched_at": "2026-09-21T00:26:08.127928+00:00",
    "date_confidence": "high",
    "description": "<h2>Who we are</h2> <h3>About Stripe</h3> <p><span style=\"font-weight: 400;\">Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s la"
  }
]
```

## Coinbase

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/coinbase/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.139s
- Company elapsed time: 0.684s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 217
- After US/location filtering: 183
- With trustworthy posted_date: 183
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
    "fetched_at": "2026-09-21T00:26:09.230972+00:00",
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
    "fetched_at": "2026-09-21T00:26:09.230972+00:00",
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
    "fetched_at": "2026-09-21T00:26:09.230972+00:00",
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
    "fetched_at": "2026-09-21T00:26:09.230972+00:00",
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
    "fetched_at": "2026-09-21T00:26:09.230972+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.198s
- Company elapsed time: 0.722s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 157
- After US/location filtering: 144
- With trustworthy posted_date: 144
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
    "fetched_at": "2026-09-21T00:26:09.915977+00:00",
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
    "fetched_at": "2026-09-21T00:26:09.915977+00:00",
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
    "fetched_at": "2026-09-21T00:26:09.915977+00:00",
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
    "fetched_at": "2026-09-21T00:26:09.915977+00:00",
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
    "updated_date": "2026-09-14",
    "fetched_at": "2026-09-21T00:26:09.915977+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.183s
- Company elapsed time: 0.548s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 152
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
    "fetched_at": "2026-09-21T00:26:10.640558+00:00",
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
    "fetched_at": "2026-09-21T00:26:10.640558+00:00",
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
    "fetched_at": "2026-09-21T00:26:10.640558+00:00",
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
    "fetched_at": "2026-09-21T00:26:10.640558+00:00",
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
    "fetched_at": "2026-09-21T00:26:10.640558+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.288s
- Company elapsed time: 0.800s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 216
- After US/location filtering: 122
- With trustworthy posted_date: 122
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
    "fetched_at": "2026-09-21T00:26:11.187057+00:00",
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
    "fetched_at": "2026-09-21T00:26:11.187057+00:00",
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
    "fetched_at": "2026-09-21T00:26:11.187057+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational e"
  },
  {
    "company": "GitLab",
    "source": "gitlab_official_careers",
    "job_id": "8808115002",
    "title": "Associate Revenue Operations Analyst, Policy & Rules of Engagement",
    "location": "Remote, United States; Canada; United States of America",
    "official_url": "https://job-boards.greenhouse.io/gitlab/jobs/8808115002",
    "posted_date": "2026-09-16",
    "updated_date": "2026-09-17",
    "fetched_at": "2026-09-21T00:26:11.187057+00:00",
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
    "fetched_at": "2026-09-21T00:26:11.187057+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.120s
- Company elapsed time: 0.234s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 47
- After US/location filtering: 47
- With trustworthy posted_date: 47
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
    "fetched_at": "2026-09-21T00:26:11.987905+00:00",
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
    "fetched_at": "2026-09-21T00:26:11.987905+00:00",
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
    "fetched_at": "2026-09-21T00:26:11.987905+00:00",
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
    "fetched_at": "2026-09-21T00:26:11.987905+00:00",
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
    "fetched_at": "2026-09-21T00:26:11.987905+00:00",
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
- HTTP requests/cumulative request time: 1 / 7.055s
- Company elapsed time: 7.342s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 103
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
    "updated_date": "2026-09-15",
    "fetched_at": "2026-09-21T00:26:12.222217+00:00",
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
    "fetched_at": "2026-09-21T00:26:12.222217+00:00",
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
    "fetched_at": "2026-09-21T00:26:12.222217+00:00",
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
    "updated_date": "2026-09-15",
    "fetched_at": "2026-09-21T00:26:12.222217+00:00",
    "date_confidence": "high",
    "description": "<p>The Asana Marketing team is responsible for fueling business growth and building a brand customers love. We create campaigns and content to attract new accounts and inspire curr"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8194305",
    "title": "Channel Partner Manager",
    "location": "Chicago",
    "official_url": "https://www.asana.com/jobs/apply/8194305?gh_jid=8194305",
    "posted_date": "2026-09-15",
    "updated_date": "2026-09-15",
    "fetched_at": "2026-09-21T00:26:12.222217+00:00",
    "date_confidence": "high",
    "description": "<p id=\"p-rc_36ffeb718aae9af3-231\" data-path-to-node=\"4\"><span data-path-to-node=\"4,0\">The Channel and Ecosystems team is dedicated to accelerating Asana's growth and market reach t"
  }
]
```

## Brex

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/brex/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.218s
- Company elapsed time: 0.902s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 251
- After US/location filtering: 247
- With trustworthy posted_date: 247
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8688110002",
    "title": "Account Executive, Small Business",
    "location": "New York, New York, United States; Salt Lake City, Utah, United States; San Francisco, California, United States",
    "official_url": "https://www.brex.com/careers/8688110002?gh_jid=8688110002",
    "posted_date": "2026-08-06",
    "updated_date": "2026-08-19",
    "fetched_at": "2026-09-21T00:26:19.565372+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8686667002",
    "title": "Account Executive, Small Business",
    "location": "San Francisco, California, United States; New York, New York, United States; Salt Lake City, Utah, United States; São Paulo, São Paulo, Brazil",
    "official_url": "https://www.brex.com/careers/8686667002?gh_jid=8686667002",
    "posted_date": "2026-08-06",
    "updated_date": "2026-08-19",
    "fetched_at": "2026-09-21T00:26:19.565372+00:00",
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
    "fetched_at": "2026-09-21T00:26:19.565372+00:00",
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
    "fetched_at": "2026-09-21T00:26:19.565372+00:00",
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
    "fetched_at": "2026-09-21T00:26:19.565372+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.207s
- Company elapsed time: 1.158s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 273
- After US/location filtering: 215
- With trustworthy posted_date: 215
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:26:20.469001+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:26:20.469001+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:26:20.469001+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:26:20.469001+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:26:20.469001+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.188s
- Company elapsed time: 0.463s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 176
- After US/location filtering: 100
- With trustworthy posted_date: 100
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
    "fetched_at": "2026-09-21T00:26:21.627242+00:00",
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
    "fetched_at": "2026-09-21T00:26:21.627242+00:00",
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
    "fetched_at": "2026-09-21T00:26:21.627242+00:00",
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
    "fetched_at": "2026-09-21T00:26:21.627242+00:00",
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
    "fetched_at": "2026-09-21T00:26:21.627242+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.672s
- Company elapsed time: 0.759s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 71
- After US/location filtering: 57
- With trustworthy posted_date: 57
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
    "fetched_at": "2026-09-21T00:26:22.091646+00:00",
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
    "fetched_at": "2026-09-21T00:26:22.091646+00:00",
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
    "fetched_at": "2026-09-21T00:26:22.091646+00:00",
    "date_confidence": "high",
    "description": "Identify and evaluate audiobook catalogs from independent authors, hybrid publishers, independent presses, and distribution partners that will resonate with Spotify listeners. Nego"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "318f73b5-6a78-49c7-b625-ecb1481042b9",
    "title": "Backend Engineer, Personalization",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/318f73b5-6a78-49c7-b625-ecb1481042b9",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:22.091646+00:00",
    "date_confidence": "high",
    "description": "Build, maintain, and evolve backend systems that support personalization and recommendations at Spotify scale. Develop infrastructure that enables efficient retrieval, ranking, and"
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
    "fetched_at": "2026-09-21T00:26:22.091646+00:00",
    "date_confidence": "high",
    "description": "Identify, structure, negotiate, amend, close, and manage strategic distribution partnerships across APAC that advance Spotify’s growth and long‑term vision. Develop and refine part"
  }
]
```

## Ramp

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/ramp`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.136s
- Company elapsed time: 0.398s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 148
- After US/location filtering: 131
- With trustworthy posted_date: 131
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
    "fetched_at": "2026-09-21T00:26:22.851625+00:00",
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
    "fetched_at": "2026-09-21T00:26:22.851625+00:00",
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
    "fetched_at": "2026-09-21T00:26:22.851625+00:00",
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
    "fetched_at": "2026-09-21T00:26:22.851625+00:00",
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
    "fetched_at": "2026-09-21T00:26:22.851625+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.156s
- Company elapsed time: 0.340s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 128
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
    "title": "Software Engineer, Developer Platform",
    "location": "San Francisco, California; San Francisco, California, United States; New York, New York; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/notion/1fc309c8-da20-4ff2-84c7-8b863ece2b0a",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:23.254054+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.254054+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.254054+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.254054+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.254054+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.081s
- Company elapsed time: 0.130s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 32
- After US/location filtering: 30
- With trustworthy posted_date: 30
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
    "fetched_at": "2026-09-21T00:26:23.592101+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.592101+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.592101+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.592101+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.592101+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.161s
- Company elapsed time: 0.404s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 142
- After US/location filtering: 117
- With trustworthy posted_date: 117
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
    "fetched_at": "2026-09-21T00:26:23.722185+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.722185+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.722185+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.722185+00:00",
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
    "fetched_at": "2026-09-21T00:26:23.722185+00:00",
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
- Pages/requests fetched: 43
- HTTP requests/cumulative request time: 220 / 60.983s
- Company elapsed time: 92.724s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 177 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 31, 'fetched:new': 145}
- Raw jobs found: 833
- After US/location filtering: 176
- With trustworthy posted_date: 176
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 19.998, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 9.627, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.041, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.092, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.659, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.775, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.539, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.369, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 2, "query": "forward deployed engineer", "raw_jobs": 33, "stop_reason": "early_stop", "unique_contribution": 16, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 5.031, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 1.258, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 2, "query": "full stack backend", "raw_jobs": 38, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 38}
- Query diagnostic: {"elapsed_seconds": 9.113, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "site reliability engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.957, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "cloud engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.906, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "security engineer remote", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.804, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 2, "query": "software engineer collaboration devices", "raw_jobs": 35, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 2.472, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "splunk engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.083, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "software engineer solution test iq platform", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 7}

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2024152",
    "title": "Senior Product Designer -- Hypershield",
    "location": "San Jose, California, US; Remote - North Dakota, USA; Remote - Montana, USA; Remote - Maine, USA; Remote - Ohio, USA; Remote - Nebraska, USA; Remote - Louisiana, USA; Remote - Texas, USA; Remote - Nevada, USA; Remote - Hawaii, USA; Remote - Georgia, USA; Remote - Mississippi, USA; Remote - Connecticut, USA; Remote - Colorado, USA; Remote - Wyoming, USA; Remote - Wisconsin, USA; Remote - West Virginia, USA; Remote - Maryland, USA; Remote - California, USA; Remote - Vermont, USA; Remote - New York, USA; Remote - New Jersey, USA; Remote - Arkansas, USA; Remote - South Dakota, USA; Remote - Pennsylvania, USA; Remote - Michigan, USA; Remote - Indiana, USA; Remote - Idaho, USA; Remote - Arizona, USA; Remote - New Mexico, USA; Remote - New Hampshire, USA; Remote - Kentucky, USA; Remote - Alabama, USA; Remote - South Carolina, USA; Remote - Illinois, USA; Remote - Missouri, USA; Remote - Massachusetts, USA; Remote - Iowa, USA; Remote - Tennessee, USA; Remote - North Carolina, USA; Remote - Minnesota, USA; Remote - Kansas, USA; Remote - Alaska, USA; Remote - Rhode Island, USA; Remote - Delaware, USA; Remote - Washington, USA; Remote - Virginia, USA; Remote - Utah, USA; Remote - Oregon, USA; Remote - Florida, USA; Remote - Oklahoma, USA",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Senior-Product-Designer----Hypershield_2024152",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:24.126299+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/21/2026 Meet the Team Isovalent , now part of Cisco, is the company founded by the creators of Cilium and eBPF . Cisco Isovalent "
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2024153",
    "title": "Product Designer -- Hypershield",
    "location": "San Jose, California, US; Remote - North Dakota, USA; Remote - Montana, USA; Remote - Maine, USA; Remote - Ohio, USA; Remote - Nebraska, USA; Remote - Louisiana, USA; Remote - Texas, USA; Remote - Nevada, USA; Remote - Hawaii, USA; Remote - Georgia, USA; Remote - Mississippi, USA; Remote - Connecticut, USA; Remote - Colorado, USA; Remote - Wyoming, USA; Remote - Wisconsin, USA; Remote - West Virginia, USA; Remote - Maryland, USA; Remote - California, USA; Remote - Vermont, USA; Remote - New York, USA; Remote - New Jersey, USA; Remote - Arkansas, USA; Remote - South Dakota, USA; Remote - Pennsylvania, USA; Remote - Michigan, USA; Remote - Indiana, USA; Remote - Idaho, USA; Remote - Arizona, USA; Remote - New Mexico, USA; Remote - New Hampshire, USA; Remote - Kentucky, USA; Remote - Alabama, USA; Remote - South Carolina, USA; Remote - Illinois, USA; Remote - Missouri, USA; Remote - Massachusetts, USA; Remote - Iowa, USA; Remote - Tennessee, USA; Remote - North Carolina, USA; Remote - Minnesota, USA; Remote - Kansas, USA; Remote - Alaska, USA; Remote - Rhode Island, USA; Remote - Delaware, USA; Remote - Washington, USA; Remote - Virginia, USA; Remote - Utah, USA; Remote - Oregon, USA; Remote - Florida, USA; Remote - Oklahoma, USA",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Product-Designer----Hypershield_2024153",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:24.126299+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/21/2026 Meet the Team Isovalent , now part of Cisco, is the company founded by the creators of Cilium and eBPF . Cisco Isovalent "
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2024998",
    "title": "AI Security Engineer",
    "location": "RTP, North Carolina, US; San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/RTP-North-Carolina-US/AI-Security-Engineer_2024998",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:24.126299+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/29/2026 Meet the Team Join Cisco’s Enterprise AI team, the core group enabling Generative AI powered experiences across Cisco. Ou"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2024999",
    "title": "AI Application Security Engineer",
    "location": "RTP, North Carolina, US; San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/RTP-North-Carolina-US/AI-Application-Security-Engineer_2024999",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:24.126299+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/29/2026 Meet the Team Join Cisco’s Enterprise AI team, the core group enabling Generative AI powered experiences across Cisco. Ou"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2011083",
    "title": "IC Package Design Engineer",
    "location": "San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/IC-Package-Design-Engineer_2011083",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:24.126299+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 11/29/2026 Meet the Team The Common Hardware Group (CHG) creates innovative hardware platforms central to the AI era, powering Cisco"
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 32
- HTTP requests/cumulative request time: 185 / 65.271s
- Company elapsed time: 99.174s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 153 / 0 / 0
- Detail cache statuses: {'fetched:new': 153}
- Raw jobs found: 800
- After US/location filtering: 153
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 53.655, "first_pass_survivors": 100, "group": "official", "jds_resolved": 100, "original_postings_resolved": 100, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 100, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 5.41, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 10.922, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 13.558, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.012, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.082, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.493, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 2.105, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 75}
- Query diagnostic: {"elapsed_seconds": 3.316, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 100, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 100}
- Query diagnostic: {"elapsed_seconds": 3.62, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "cloud developer", "raw_jobs": 75, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 75}

Sample normalized records:

```json
[
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1411898433",
    "title": "Senior Product Manager - Application AI",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://jobs.sap.com/job/Palo-Alto-Senior-Product-Manager-Application-AI-CA-94304/1411898433/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:29.792868+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1421516633",
    "title": "Forward Deployed Senior AI Engineer",
    "location": "New York, NY, US, 10001",
    "official_url": "https://jobs.sap.com/job/New-York-Forward-Deployed-Senior-AI-Engineer-NY-10001/1421516633/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:29.792868+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1438239233",
    "title": "Senior Machine Learning Engineer - Research & Innovation Team",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://jobs.sap.com/job/Palo-Alto-Senior-Machine-Learning-Engineer-Research-&-Innovation-Team-CA-94304/1438239233/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:29.792868+00:00",
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
    "fetched_at": "2026-09-21T00:26:29.792868+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1424890833",
    "title": "Senior Full Stack Developer",
    "location": "Bellevue, WA, US, 98004",
    "official_url": "https://jobs.sap.com/job/Bellevue-Senior-Full-Stack-Developer-WA-98004/1424890833/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:26:29.792868+00:00",
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
- HTTP requests/cumulative request time: 254 / 120.003s
- Company elapsed time: 154.663s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 227 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 11, 'fetched:new': 216}
- Raw jobs found: 473
- After US/location filtering: 227
- With trustworthy posted_date: 227
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 53.346, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 16.984, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 43, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 43}
- Query diagnostic: {"elapsed_seconds": 1.438, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 21.03, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 19.617, "first_pass_survivors": 31, "group": "official", "jds_resolved": 31, "original_postings_resolved": 31, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 31, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.883, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.261, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.251, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 10.203, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 2.038, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "ai workflow specialist", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 6}

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
    "fetched_at": "2026-09-21T00:27:10.966639+00:00",
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
    "fetched_at": "2026-09-21T00:27:10.966639+00:00",
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
    "fetched_at": "2026-09-21T00:27:10.966639+00:00",
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
    "fetched_at": "2026-09-21T00:27:10.966639+00:00",
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
    "fetched_at": "2026-09-21T00:27:10.966639+00:00",
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
- HTTP requests/cumulative request time: 27 / 18.184s
- Company elapsed time: 25.019s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 270
- After US/location filtering: 130
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 2.751, "first_pass_survivors": 30, "group": "official", "jds_resolved": 0, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.431, "first_pass_survivors": 16, "group": "official", "jds_resolved": 0, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.225, "first_pass_survivors": 22, "group": "official", "jds_resolved": 0, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.337, "first_pass_survivors": 21, "group": "official", "jds_resolved": 0, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.201, "first_pass_survivors": 4, "group": "official", "jds_resolved": 0, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.336, "first_pass_survivors": 14, "group": "official", "jds_resolved": 0, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 5.39, "first_pass_survivors": 9, "group": "official", "jds_resolved": 0, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.342, "first_pass_survivors": 9, "group": "official", "jds_resolved": 0, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.005, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 30}

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
    "fetched_at": "2026-09-21T00:27:40.078056+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10148555",
    "title": "Software Engineer II, AI Performance",
    "location": "New York, New York",
    "official_url": "https://www.disneycareers.com/en/job/new-york/software-engineer-ii-ai-performance/391/100828809776",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:27:40.078056+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10148557",
    "title": "Software Engineer II, AI Insights",
    "location": "New York, New York",
    "official_url": "https://www.disneycareers.com/en/job/new-york/software-engineer-ii-ai-insights/391/100828809312",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:27:40.078056+00:00",
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
    "fetched_at": "2026-09-21T00:27:40.078056+00:00",
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
    "fetched_at": "2026-09-21T00:27:40.078056+00:00",
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
- HTTP requests/cumulative request time: 74 / 34.462s
- Company elapsed time: 44.246s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 55 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 5, 'fetched:new': 50}
- Raw jobs found: 261
- After US/location filtering: 55
- With trustworthy posted_date: 55
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.573, "first_pass_survivors": 52, "group": "official", "jds_resolved": 52, "original_postings_resolved": 52, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 52, "stop_reason": "page_budget", "unique_contribution": 52, "unique_jobs": 52}
- Query diagnostic: {"elapsed_seconds": 0.775, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 0.737, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 2.093, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 2.861, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 2.818, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 2.812, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 53, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 53}
- Query diagnostic: {"elapsed_seconds": 0.767, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.773, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 20}

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
    "fetched_at": "2026-09-21T00:27:56.851725+00:00",
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
    "fetched_at": "2026-09-21T00:27:56.851725+00:00",
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
    "fetched_at": "2026-09-21T00:27:56.851725+00:00",
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
    "fetched_at": "2026-09-21T00:27:56.851725+00:00",
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
    "fetched_at": "2026-09-21T00:27:56.851725+00:00",
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
- HTTP requests/cumulative request time: 138 / 50.085s
- Company elapsed time: 70.272s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 111 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 17, 'fetched:new': 94}
- Raw jobs found: 260
- After US/location filtering: 111
- With trustworthy posted_date: 111
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 14.016, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.158, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 8.344, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 17, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 16.555, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 24, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 3.322, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.96, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.996, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.979, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.472, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095379",
    "title": "SOC Design Verification Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720709639",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:05.097575+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > ASICS Engineering General Summary: We are seeking highly motivated and experienced Design Veri"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095749",
    "title": "Security (Product, Systems, Cyber) Engineering Internship - Summer 2027",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720740636",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:05.097575+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Interns Group, Interns Group > Interim Engineering Intern - SW General Summary: About Qualcomm Qualcomm relentlessly innovates transf"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095751",
    "title": "Multimedia Engineering Internship – Summer 2027",
    "location": "San Diego, California, United States of America; Santa Clara, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720740640",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:05.097575+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Interns Group, Interns Group > Interim Engineering Intern - Systems General Summary: About Qualcomm Qualcomm relentlessly innovates t"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095752",
    "title": "Hardware (CPU, GPU, SoC, Digital Design, DV) Engineering Internship – Summer 2027",
    "location": "San Diego, California, United States of America; Austin, Texas, United States of America; Boxborough, Massachusetts, United States of America; Tempe, Arizona, United States of America; Santa Clara, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720740649",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:05.097575+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Interns Group, Interns Group > Interim Engineering Intern - HW General Summary: About Qualcomm Qualcomm relentlessly innovates transf"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095760",
    "title": "IT Infrastructure & Cloud Engineering Internship – Summer 2027",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720741668",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:05.097575+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Incorporated Job Area: Interns Group, Interns Group > Interim Intern General Summary: About Qualcomm Qualcomm relentlessly innovates transforming businesses, enri"
  }
]
```

## AMD

- Status: ok
- Scraping method: HTTP GET public Jibe/iCIMS jobs JSON
- Search URL/API: `https://careers.amd.com/api/jobs`
- Pagination: page=1,2,... per role query; stop on total/empty/repeat/short page
- Pages/requests fetched: 14
- HTTP requests/cumulative request time: 14 / 9.469s
- Company elapsed time: 11.225s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 1251
- After US/location filtering: 472
- With trustworthy posted_date: 472
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 3.61, "first_pass_survivors": 330, "group": "official", "jds_resolved": 330, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 330, "stop_reason": "page_budget", "unique_contribution": 330, "unique_jobs": 330}
- Query diagnostic: {"elapsed_seconds": 0.641, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning", "raw_jobs": 86, "stop_reason": "early_stop", "unique_contribution": 21, "unique_jobs": 86}
- Query diagnostic: {"elapsed_seconds": 2.462, "first_pass_survivors": 76, "group": "official", "jds_resolved": 76, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 76, "unique_jobs": 300}
- Query diagnostic: {"elapsed_seconds": 2.183, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "AI research", "raw_jobs": 235, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 235}
- Query diagnostic: {"elapsed_seconds": 2.329, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 300, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 300}

Sample normalized records:

```json
[
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "78259",
    "title": "Principal Software Engineer – PyTorch Training Frameworks",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-02-26",
    "updated_date": "2026-09-19",
    "fetched_at": "2026-09-21T00:28:08.968461+00:00",
    "date_confidence": "high",
    "description": "WHAT YOU DO AT AMD CHANGES EVERYTHING At AMD, our mission is to build great products that accelerate next-generation computing experiences—from AI and data centers, to PCs, gaming "
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "88472",
    "title": "Sr. Software Development Engineer - Adaptive and Embedded Group",
    "location": "San Jose, California",
    "official_url": "",
    "posted_date": "2026-07-10",
    "updated_date": "2026-09-19",
    "fetched_at": "2026-09-21T00:28:08.968461+00:00",
    "date_confidence": "high",
    "description": "WHAT YOU DO AT AMD CHANGES EVERYTHING At AMD, our mission is to build great products that accelerate next-generation computing experiences—from AI and data centers, to PCs, gaming "
  },
  {
    "company": "AMD",
    "source": "amd_official_careers",
    "job_id": "91897",
    "title": "Principal Software Development Engineer",
    "location": "Santa Clara, California",
    "official_url": "",
    "posted_date": "2026-09-08",
    "updated_date": "2026-09-19",
    "fetched_at": "2026-09-21T00:28:08.968461+00:00",
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
    "updated_date": "2026-09-19",
    "fetched_at": "2026-09-21T00:28:08.968461+00:00",
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
    "fetched_at": "2026-09-21T00:28:08.968461+00:00",
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
- HTTP requests/cumulative request time: 62 / 21.964s
- Company elapsed time: 30.177s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 42 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 40}
- Raw jobs found: 185
- After US/location filtering: 42
- With trustworthy posted_date: 42
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 12.293, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 26, "stop_reason": "early_stop", "unique_contribution": 26, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 1.235, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 0.492, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 5.636, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 23, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 4.082, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 41, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 41}
- Query diagnostic: {"elapsed_seconds": 2.729, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 42, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 42}
- Query diagnostic: {"elapsed_seconds": 0.5, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.489, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 2.083, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 29, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 29}

Sample normalized records:

```json
[
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19654",
    "title": "Senior Solutions Engineer - Upmarket West",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Senior-Solutions-Engineer---Upmarket-West_R19654",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:20.194840+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect You will serve as the lead technical advocate for our customers, helping them understand and leverage Zoom's architectural advantages while partnering closely w"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19452",
    "title": "Manager of Platform DevOps",
    "location": "San Jose (CA); Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Manager-of-Platform-DevOps_R19452-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:20.194840+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect You will be the leader of our Platforms DevOps team. This team is responsible for Zoom’s Kubernetes clusters in both datacenters and clouds, as well as for our "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R17675",
    "title": "Principal DevOps Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Principal-DevOps-Engineer_R17675",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:20.194840+00:00",
    "date_confidence": "high",
    "description": "We are seeking a Principal DevOps Engineer who combines deep technical expertise with broad system understanding. This engineer should be capable of diving into a wide range of ser"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19426",
    "title": "Software Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Software-Engineer_R19426-1",
    "posted_date": "2026-09-04",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:20.194840+00:00",
    "date_confidence": "high",
    "description": "What you can expect Design, build, and own the data pipelines, models, and products that power sales, customer success, and revenue analytics for Zoom's Go-To-Market organization. "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19366",
    "title": "AI Inference Engineer - Speech",
    "location": "Seattle (WA); San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Seattle-WA/AI-Inference-Engineer---Speech_R19366-1",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:20.194840+00:00",
    "date_confidence": "high",
    "description": "What you can expect We are looking for an AI Inference Engineer with a solid background in speech recognition and model inference. In this role, you will develop state-of-the-art a"
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
- HTTP requests/cumulative request time: 1 / 0.508s
- Company elapsed time: 1.199s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 354
- After US/location filtering: 205
- With trustworthy posted_date: 205
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
    "fetched_at": "2026-09-21T00:28:41.098512+00:00",
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
    "fetched_at": "2026-09-21T00:28:41.098512+00:00",
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
    "fetched_at": "2026-09-21T00:28:41.098512+00:00",
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
    "fetched_at": "2026-09-21T00:28:41.098512+00:00",
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
    "fetched_at": "2026-09-21T00:28:41.098512+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.424s
- Company elapsed time: 2.059s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 875
- After US/location filtering: 485
- With trustworthy posted_date: 485
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
    "fetched_at": "2026-09-21T00:28:42.298468+00:00",
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
    "fetched_at": "2026-09-21T00:28:42.298468+00:00",
    "date_confidence": "high",
    "description": "<p><strong>AI Engineer - FDE (Forward Deployed Engineer) (ALL LEVELS)</strong></p> <p><strong>CSQ327R177</strong></p> <p><strong>Mission</strong></p> <p>The AI Forward Deployed Eng"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8760167002",
    "title": "AI Engineer – Forward Deployed Engineering, U.S. Public Sector (Federal Focus)",
    "location": "Maryland; Virginia; Washington, D.C.; Remote - Washington D.C.",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8760167002",
    "posted_date": "2026-08-28",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:28:42.298468+00:00",
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
    "fetched_at": "2026-09-21T00:28:42.298468+00:00",
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
    "fetched_at": "2026-09-21T00:28:42.298468+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.175s
- Company elapsed time: 0.765s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 243
- After US/location filtering: 225
- With trustworthy posted_date: 225
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
    "fetched_at": "2026-09-21T00:28:44.358977+00:00",
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
    "fetched_at": "2026-09-21T00:28:44.358977+00:00",
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
    "fetched_at": "2026-09-21T00:28:44.358977+00:00",
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
    "updated_date": "2026-09-20",
    "fetched_at": "2026-09-21T00:28:44.358977+00:00",
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
    "updated_date": "2026-09-20",
    "fetched_at": "2026-09-21T00:28:44.358977+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.170s
- Company elapsed time: 0.565s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 168
- After US/location filtering: 96
- With trustworthy posted_date: 96
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8214444",
    "title": "Business Systems Engineer, Tech Foundations",
    "location": "San Francisco, CA; United States",
    "official_url": "https://careers.airbnb.com/positions/8214444?gh_jid=8214444",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:28:45.125288+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:28:45.125288+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:28:45.125288+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:28:45.125288+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:28:45.125288+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.314s
- Company elapsed time: 2.340s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 611
- After US/location filtering: 499
- With trustworthy posted_date: 499
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5421031008",
    "title": "Accommodations Partner",
    "location": "San Francisco, CA | Seattle, WA; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5421031008",
    "posted_date": "2026-09-17",
    "updated_date": "2026-09-17",
    "fetched_at": "2026-09-21T00:28:45.691696+00:00",
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
    "fetched_at": "2026-09-21T00:28:45.691696+00:00",
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
    "fetched_at": "2026-09-21T00:28:45.691696+00:00",
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
    "fetched_at": "2026-09-21T00:28:45.691696+00:00",
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
    "fetched_at": "2026-09-21T00:28:45.691696+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.163s
- Company elapsed time: 0.263s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 35
- After US/location filtering: 24
- With trustworthy posted_date: 24
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
    "fetched_at": "2026-09-21T00:28:48.032812+00:00",
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
    "fetched_at": "2026-09-21T00:28:48.032812+00:00",
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
    "fetched_at": "2026-09-21T00:28:48.032812+00:00",
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
    "fetched_at": "2026-09-21T00:28:48.032812+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4706446006",
    "title": "Content Marketing Manager",
    "location": "Palo Alto, CA",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4706446006?gh_jid=4706446006",
    "posted_date": "2026-08-19",
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:28:48.032812+00:00",
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
- HTTP requests/cumulative request time: 24 / 24.852s
- Company elapsed time: 28.414s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 1066
- After US/location filtering: 449
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.033, "first_pass_survivors": 142, "group": "official", "jds_resolved": 142, "original_postings_resolved": 142, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 142, "unique_jobs": 147}
- Query diagnostic: {"elapsed_seconds": 3.501, "first_pass_survivors": 104, "group": "official", "jds_resolved": 104, "original_postings_resolved": 104, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 104, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.134, "first_pass_survivors": 56, "group": "official", "jds_resolved": 56, "original_postings_resolved": 56, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 105, "stop_reason": "page_budget", "unique_contribution": 56, "unique_jobs": 105}
- Query diagnostic: {"elapsed_seconds": 3.528, "first_pass_survivors": 58, "group": "official", "jds_resolved": 58, "original_postings_resolved": 58, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 58, "unique_jobs": 149}
- Query diagnostic: {"elapsed_seconds": 3.406, "first_pass_survivors": 53, "group": "official", "jds_resolved": 53, "original_postings_resolved": 53, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 53, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 3.297, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 150}
- Query diagnostic: {"elapsed_seconds": 2.107, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 58, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 0.93, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 3.478, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 150, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 150}

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
    "fetched_at": "2026-09-21T00:28:48.296781+00:00",
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
    "fetched_at": "2026-09-21T00:28:48.296781+00:00",
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
    "fetched_at": "2026-09-21T00:28:48.296781+00:00",
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
    "fetched_at": "2026-09-21T00:28:48.296781+00:00",
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
    "fetched_at": "2026-09-21T00:28:48.296781+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.231s
- Company elapsed time: 0.515s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 67
- After US/location filtering: 67
- With trustworthy posted_date: 67
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
    "fetched_at": "2026-09-21T00:28:50.372318+00:00",
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
    "fetched_at": "2026-09-21T00:28:50.372318+00:00",
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
    "fetched_at": "2026-09-21T00:28:50.372318+00:00",
    "date_confidence": "high",
    "description": "<h2>About the role</h2> <p>Chime is looking for a Creative Director to shape what our brand looks, sounds and feels like — and to turn that into work people actually talk about.</p"
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
    "fetched_at": "2026-09-21T00:28:50.372318+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\"><strong>About the role</strong></span></h2> <p class=\"p2\">We're looking for a Growth Product Scientist to partner with "
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8694634002",
    "title": "Design Director",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8694634002?gh_jid=8694634002",
    "posted_date": "2026-08-13",
    "updated_date": "2026-09-09",
    "fetched_at": "2026-09-21T00:28:50.372318+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\">About the role</span></h2> <p class=\"isSelectedEnd\">We’re hiring a Design Director to lead Product Design across our Sp"
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
- Pages/requests fetched: 25
- HTTP requests/cumulative request time: 127 / 36.181s
- Company elapsed time: 54.552s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 102 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 4, 'fetched:new': 98}
- Raw jobs found: 481
- After US/location filtering: 102
- With trustworthy posted_date: 102
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.768, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.355, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.001, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 11.597, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.083, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.879, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.584, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.722, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 47, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 47}
- Query diagnostic: {"elapsed_seconds": 3.563, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "295755",
    "title": "Senior Principal Systems Thermal Engineer AI Infrastructure",
    "location": "Austin, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/295755",
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:50.888309+00:00",
    "date_confidence": "high",
    "description": "Infrastructure Solutions Group (ISG) builds the products that power infrastructure, solutions, and data management our customers need most. Our teams design and develop the hardwar"
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
    "fetched_at": "2026-09-21T00:28:50.888309+00:00",
    "date_confidence": "high",
    "description": "SUMMARY Agentic Context Engineering Architect & AI Practitioner Join us to do the best work of your career and make a profound social impact as an Agentic Context Engineering Archi"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "298037",
    "title": "Technical Support Engineer 2 - AI Networking",
    "location": "Round Rock, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/298037",
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:50.888309+00:00",
    "date_confidence": "high",
    "description": "Tec Technical Support Engineer 2 – Dell & Nvidia AI Networking At Dell Technologies, world-class service doesn’t end when a customer purchases our innovative products. Our Technica"
  },
  {
    "company": "Dell",
    "source": "dell_official_careers",
    "job_id": "298110",
    "title": "Technical Support Engineer 2 - AI Networking",
    "location": "Round Rock, TX, United States",
    "official_url": "https://enterpriseplatform.dell.com/hcmUI/CandidateExperience/en/sites/careers/job/298110",
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:28:50.888309+00:00",
    "date_confidence": "high",
    "description": "Technical Support Engineer 2 – Dell & Nvidia AI Networking At Dell Technologies, world-class service doesn’t end when a customer purchases our innovative products. Our Technical Su"
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
    "fetched_at": "2026-09-21T00:28:50.888309+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.125s
- Company elapsed time: 0.264s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 44
- After US/location filtering: 35
- With trustworthy posted_date: 35
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
    "fetched_at": "2026-09-21T00:29:15.370903+00:00",
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
    "fetched_at": "2026-09-21T00:29:15.370903+00:00",
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
    "fetched_at": "2026-09-21T00:29:15.370903+00:00",
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
    "fetched_at": "2026-09-21T00:29:15.370903+00:00",
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
    "fetched_at": "2026-09-21T00:29:15.370903+00:00",
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
- Pages/requests fetched: 22
- HTTP requests/cumulative request time: 80 / 22.488s
- Company elapsed time: 34.235s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 58 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 8, 'fetched:new': 50}
- Raw jobs found: 388
- After US/location filtering: 58
- With trustworthy posted_date: 58
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 15.362, "first_pass_survivors": 33, "group": "official", "jds_resolved": 33, "original_postings_resolved": 33, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 33, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.659, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 50, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 50}
- Query diagnostic: {"elapsed_seconds": 0.698, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 3.485, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.464, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.808, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 1.623, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.21, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.925, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109347",
    "title": "Machine Learning Scientist II",
    "location": "Austin Domain 11 - HomeAway; Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Austin-Domain-11---HomeAway/Machine-Learning-Scientist-II_R-109347-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:15.635204+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109458",
    "title": "Principal Program Manager",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Principal-Program-Manager_R-109458-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:15.635204+00:00",
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
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:15.635204+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-109895",
    "title": "Product Manager III, Rapid API - Post-Booking",
    "location": "USA - Illinois - Chicago",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/USA---Illinois---Chicago/Product-Manager-III--Rapid-API---Post-Booking_R-109895-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:15.635204+00:00",
    "date_confidence": "high",
    "description": "At Expedia Group, we help travelers explore the world, one journey at a time. As a global travel company powered by passionate people, trusted partnerships, and leading technology,"
  },
  {
    "company": "Expedia Group",
    "source": "expedia_group_official_careers",
    "job_id": "R-108467",
    "title": "Senior Machine Learning Engineer",
    "location": "Washington - Seattle Campus",
    "official_url": "https://expedia.wd108.myworkdayjobs.com/search/job/Washington---Seattle-Campus/Senior-Machine-Learning-Engineer_R-108467",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:15.635204+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.170s
- Company elapsed time: 0.312s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 138
- After US/location filtering: 31
- With trustworthy posted_date: 31
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
    "fetched_at": "2026-09-21T00:29:16.712159+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:29:16.712159+00:00",
    "date_confidence": "high",
    "description": "<p><strong>***Now accepting applications for a November 3rd, 2026 start date***</strong></p> <p>As an Account Executive on the Small Business sales team, you will identify, source,"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8164700",
    "title": "Lead Marketer, AI Usage Automation",
    "location": "Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8164700?gh_jid=8164700",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:29:16.712159+00:00",
    "date_confidence": "high",
    "description": "<h3>Role Summary</h3> <p>Our mission at HubSpot is to help millions of organizations grow better. As Lead Marketer, AI Usage Automation, you’ll define how we use data, AI, and digi"
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
    "fetched_at": "2026-09-21T00:29:16.712159+00:00",
    "date_confidence": "high",
    "description": "<p><strong>POS-33330</strong></p> <hr> <p><strong>Manager, Analytics Engineering, Data &amp; AI Foundations</strong></p> <p>HubSpot's mission is to Help Millions of Organizations G"
  },
  {
    "company": "HubSpot",
    "source": "hubspot_official_careers",
    "job_id": "8035238",
    "title": "Outbound Business Development Representative (BDR)",
    "location": "Cambridge, MA, USA; Remote - USA",
    "official_url": "https://www.hubspot.com/careers/jobs/8035238?gh_jid=8035238",
    "posted_date": "2026-06-29",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:29:16.712159+00:00",
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
- Company elapsed time: 0.449s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 108
- After US/location filtering: 92
- With trustworthy posted_date: 92
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
    "fetched_at": "2026-09-21T00:29:17.025301+00:00",
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
    "fetched_at": "2026-09-21T00:29:17.025301+00:00",
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
    "fetched_at": "2026-09-21T00:29:17.025301+00:00",
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
    "fetched_at": "2026-09-21T00:29:17.025301+00:00",
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
    "fetched_at": "2026-09-21T00:29:17.025301+00:00",
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
- HTTP requests/cumulative request time: 174 / 88.601s
- Company elapsed time: 112.792s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 148 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 5, 'fetched:new': 143}
- Raw jobs found: 485
- After US/location filtering: 148
- With trustworthy posted_date: 148
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.085, "first_pass_survivors": 45, "group": "official", "jds_resolved": 45, "original_postings_resolved": 45, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 45, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 20.364, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.458, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 12.538, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 12.486, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 11.954, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 18.85, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 59}
- Query diagnostic: {"elapsed_seconds": 0.854, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 6.273, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 78}

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
    "fetched_at": "2026-09-21T00:29:17.474854+00:00",
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
    "fetched_at": "2026-09-21T00:29:17.474854+00:00",
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
    "fetched_at": "2026-09-21T00:29:17.474854+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Intel Foundry Automation - Data Analytics and Process Group is seeking a motivated and technically curious intern to join our Manufacturing Automation"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0286502",
    "title": "Operations Research, Engineering Analytics Graduate Intern",
    "location": "US, Arizona, Phoenix",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Arizona-Phoenix/Operations-Research--Engineering-Analytics-Graduate-Intern_JR0286502",
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:17.474854+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: This internship is intended for Industrial Engineering graduate students with a focus on Operations Research, simulation, analytics, and optimization."
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
    "fetched_at": "2026-09-21T00:29:17.474854+00:00",
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
- HTTP requests/cumulative request time: 44 / 10.835s
- Company elapsed time: 12.298s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 34 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 86
- After US/location filtering: 34
- With trustworthy posted_date: 34
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 4.138, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 13, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.486, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 1.022, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 1.906, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.539, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 6, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.624, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 0.316, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.438, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 1.829, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 22, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 22}

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
    "fetched_at": "2026-09-21T00:29:45.441493+00:00",
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
    "fetched_at": "2026-09-21T00:29:45.441493+00:00",
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
    "fetched_at": "2026-09-21T00:29:45.441493+00:00",
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
    "fetched_at": "2026-09-21T00:29:45.441493+00:00",
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
    "fetched_at": "2026-09-21T00:29:45.441493+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.290s
- Company elapsed time: 1.108s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 401
- After US/location filtering: 255
- With trustworthy posted_date: 255
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:29:45.630313+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:29:45.630313+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:29:45.630313+00:00",
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
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:29:45.630313+00:00",
    "date_confidence": "high",
    "description": "<p>We’re looking for a hardworking, driven individual with superb energy, passion and initiative for new business acquisition. The Enterprise Account Executive role focuses exclusi"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "6531094",
    "title": "Account Executive, Growth",
    "location": "São Paulo; São Paulo, São Paulo, Brazil",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=6531094",
    "posted_date": "2026-04-30",
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:29:45.630313+00:00",
    "date_confidence": "high",
    "description": "<p>MongoDB is always developing and innovating — not only in our technology, but also in our sales go-to-market strategy. Our sales leadership is committed to building the best sal"
  }
]
```

## Morgan Stanley

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://morganstanley.eightfold.ai/api/pcsx/search?domain=morganstanley.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 130 / 46.046s
- Company elapsed time: 64.436s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 105 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1, 'fetched:new': 104}
- Raw jobs found: 226
- After US/location filtering: 105
- With trustworthy posted_date: 105
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 16.229, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 12.41, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.75, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 2, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 7.823, "first_pass_survivors": 13, "group": "official", "jds_resolved": 13, "original_postings_resolved": 13, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 13, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 4.641, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 2.945, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 12.442, "first_pass_survivors": 23, "group": "official", "jds_resolved": 23, "original_postings_resolved": 23, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 23, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 0.387, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 2.292, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR041494",
    "title": "Generative AI, Backend Engineer",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549799388181",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:46.741046+00:00",
    "date_confidence": "high",
    "description": "In the Technology division, we leverage innovation to build the connections and capabilities that power our Firm, enabling our clients and colleagues to redefine markets and shape "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR043623",
    "title": "Global Portfolio Analysis and Reporting Director",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800248228",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:46.741046+00:00",
    "date_confidence": "high",
    "description": "DEPARTMENT OVERVIEW The Global Portfolio Analysis and Reporting (GPAR) team at MSIM is responsible for delivering performance, attribution, and portfolio analytics to internal and "
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR044171",
    "title": "Lead Software Engineer - Parametric",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549800376380",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:46.741046+00:00",
    "date_confidence": "high",
    "description": "ABOUT MORGAN STANLEY Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, wealth management and investment managemen"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR038386",
    "title": "Senior Software Engineer (Java) - Parametric",
    "location": "Alpharetta, Georgia, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549798043626",
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:46.741046+00:00",
    "date_confidence": "high",
    "description": "Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, wealth management and investment management services. With offi"
  },
  {
    "company": "Morgan Stanley",
    "source": "morgan_stanley_official_careers",
    "job_id": "PT-JR042095",
    "title": "AI Platform Engineer / Architect - VP",
    "location": "New York, New York, United States of America",
    "official_url": "https://morganstanley.eightfold.ai/careers/job/549799536458",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:29:46.741046+00:00",
    "date_confidence": "high",
    "description": "Our mission is to develop a firmwide Artificial Intelligence (AI) Development Platform that aligns with the firm's Technology principles and drives efficiency and consistency, cont"
  }
]
```

## NetApp

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.netapp.com/en/search-jobs`
- Pagination: p=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 29
- HTTP requests/cumulative request time: 118 / 33.333s
- Company elapsed time: 51.645s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 89 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 435
- After US/location filtering: 89
- With trustworthy posted_date: 89
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 16.825, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.807, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 12, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.789, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 6.689, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 14, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 2.475, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 5.617, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 4.032, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 3.415, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 45}
- Query diagnostic: {"elapsed_seconds": 1.995, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 60}

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
    "fetched_at": "2026-09-21T00:29:49.871167+00:00",
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
    "fetched_at": "2026-09-21T00:29:49.871167+00:00",
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
    "fetched_at": "2026-09-21T00:29:49.871167+00:00",
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
    "fetched_at": "2026-09-21T00:29:49.871167+00:00",
    "date_confidence": "high",
    "description": "Job Summary As Director, Data & AI readiness you will own the strategy to enable data & intelligence layer powering NetApp’s most critical corporate functions — Sales, HR, Finance,"
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
    "fetched_at": "2026-09-21T00:29:49.871167+00:00",
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
- HTTP requests/cumulative request time: 9 / 3.735s
- Company elapsed time: 4.736s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 90
- After US/location filtering: 58
- With trustworthy posted_date: 58
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.658, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.571, "first_pass_survivors": 10, "group": "official", "jds_resolved": 0, "original_postings_resolved": 10, "page_budget": 1, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.464, "first_pass_survivors": 6, "group": "official", "jds_resolved": 0, "original_postings_resolved": 6, "page_budget": 1, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.999, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.432, "first_pass_survivors": 8, "group": "official", "jds_resolved": 0, "original_postings_resolved": 8, "page_budget": 1, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.377, "first_pass_survivors": 7, "group": "official", "jds_resolved": 0, "original_postings_resolved": 7, "page_budget": 1, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.367, "first_pass_survivors": 5, "group": "official", "jds_resolved": 0, "original_postings_resolved": 5, "page_budget": 1, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.452, "first_pass_survivors": 2, "group": "official", "jds_resolved": 0, "original_postings_resolved": 2, "page_budget": 1, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.414, "first_pass_survivors": 3, "group": "official", "jds_resolved": 0, "original_postings_resolved": 3, "page_budget": 1, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 10, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 10}

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
    "updated_date": "2026-05-19",
    "fetched_at": "2026-09-21T00:29:57.740593+00:00",
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
    "fetched_at": "2026-09-21T00:29:57.740593+00:00",
    "date_confidence": "high",
    "description": ""
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
    "fetched_at": "2026-09-21T00:29:57.740593+00:00",
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
    "fetched_at": "2026-09-21T00:29:57.740593+00:00",
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
    "fetched_at": "2026-09-21T00:29:57.740593+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.657s
- Company elapsed time: 2.128s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 817
- After US/location filtering: 674
- With trustworthy posted_date: 674
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
    "fetched_at": "2026-09-21T00:30:02.477259+00:00",
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
    "fetched_at": "2026-09-21T00:30:02.477259+00:00",
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
    "fetched_at": "2026-09-21T00:30:02.477259+00:00",
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
    "fetched_at": "2026-09-21T00:30:02.477259+00:00",
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
    "fetched_at": "2026-09-21T00:30:02.477259+00:00",
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
- HTTP requests/cumulative request time: 1 / 1.188s
- Company elapsed time: 1.508s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 313
- After US/location filtering: 243
- With trustworthy posted_date: 243
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
    "fetched_at": "2026-09-21T00:30:04.611277+00:00",
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
    "fetched_at": "2026-09-21T00:30:04.611277+00:00",
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
    "fetched_at": "2026-09-21T00:30:04.611277+00:00",
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
    "fetched_at": "2026-09-21T00:30:04.611277+00:00",
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
    "fetched_at": "2026-09-21T00:30:04.611277+00:00",
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
- HTTP requests/cumulative request time: 71 / 25.302s
- Company elapsed time: 34.971s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 51 / 0 / 0
- Detail cache statuses: {'fetched:new': 51}
- Raw jobs found: 156
- After US/location filtering: 51
- With trustworthy posted_date: 51
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.421, "first_pass_survivors": 21, "group": "official", "jds_resolved": 21, "original_postings_resolved": 21, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 21, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 1.672, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 1.981, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 4.447, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 6.02, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 9, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.986, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 1.451, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.225, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 2.253, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 30}

Sample normalized records:

```json
[
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137389",
    "title": "Sr. Staff, Cybersecurity Risk",
    "location": "Chicago, Illinois, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922258278",
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:06.120478+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137881",
    "title": "Data Scientist",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922421821",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:06.120478+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137866",
    "title": "Sr. Staff, Cybersecurity Engineering",
    "location": "Scottsdale, Arizona, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922421842",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:06.120478+00:00",
    "date_confidence": "high",
    "description": "The Company PayPal has been revolutionizing commerce globally for more than 25 years. Creating innovative experiences that make moving money, selling, and shopping simple, personal"
  },
  {
    "company": "PayPal",
    "source": "paypal_official_careers",
    "job_id": "R0137880",
    "title": "Principal Agentic Engineer",
    "location": "San Jose, California, United States of America",
    "official_url": "https://paypal.eightfold.ai/careers/job/274922421877",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:06.120478+00:00",
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
    "fetched_at": "2026-09-21T00:30:06.120478+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.177s
- Company elapsed time: 0.736s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 156
- After US/location filtering: 139
- With trustworthy posted_date: 139
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
    "updated_date": "2026-09-20",
    "fetched_at": "2026-09-21T00:30:25.005895+00:00",
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
    "fetched_at": "2026-09-21T00:30:25.005895+00:00",
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
    "fetched_at": "2026-09-21T00:30:25.005895+00:00",
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
    "fetched_at": "2026-09-21T00:30:25.005895+00:00",
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
    "updated_date": "2026-09-20",
    "fetched_at": "2026-09-21T00:30:25.005895+00:00",
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
- HTTP requests/cumulative request time: 54 / 21.620s
- Company elapsed time: 27.625s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 40 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 4, 'fetched:new': 36}
- Raw jobs found: 95
- After US/location filtering: 40
- With trustworthy posted_date: 40
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 6.635, "first_pass_survivors": 12, "group": "official", "jds_resolved": 12, "original_postings_resolved": 12, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 12, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.438, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.584, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 13.798, "first_pass_survivors": 25, "group": "official", "jds_resolved": 25, "original_postings_resolved": 25, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 32, "stop_reason": "page_budget", "unique_contribution": 25, "unique_jobs": 32}
- Query diagnostic: {"elapsed_seconds": 0.436, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 0.816, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.408, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.403, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.51, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 21}

Sample normalized records:

```json
[
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059025",
    "title": "Global Specialist Solution Architect - Lightwell",
    "location": "Boston; Remote US VA; Remote US SC; Remote US NC; Remote US TX; Remote US FL; Remote US CA; Remote US GA",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Boston/Global-Specialist-Solution-Architect---Lightwell_R-059025-1",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:25.742530+00:00",
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
    "fetched_at": "2026-09-21T00:30:25.742530+00:00",
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
    "fetched_at": "2026-09-21T00:30:25.742530+00:00",
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
    "fetched_at": "2026-09-21T00:30:25.742530+00:00",
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
    "fetched_at": "2026-09-21T00:30:25.742530+00:00",
    "date_confidence": "high",
    "description": "About the Role Do you love learning how technology works and then figuring out the best way to explain its value to others? As a Technical Product Intern, you'll get hands-on exper"
  }
]
```

## Roku

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roku/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- HTTP requests/cumulative request time: 1 / 0.275s
- Company elapsed time: 1.114s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 254
- After US/location filtering: 194
- With trustworthy posted_date: 194
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
    "updated_date": "2026-09-20",
    "fetched_at": "2026-09-21T00:30:41.092668+00:00",
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
    "updated_date": "2026-09-20",
    "fetched_at": "2026-09-21T00:30:41.092668+00:00",
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
    "updated_date": "2026-09-20",
    "fetched_at": "2026-09-21T00:30:41.092668+00:00",
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
    "fetched_at": "2026-09-21T00:30:41.092668+00:00",
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
    "fetched_at": "2026-09-21T00:30:41.092668+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.724s
- Company elapsed time: 1.523s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 221
- After US/location filtering: 204
- With trustworthy posted_date: 204
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
    "fetched_at": "2026-09-21T00:30:41.521895+00:00",
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
    "fetched_at": "2026-09-21T00:30:41.521895+00:00",
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
    "fetched_at": "2026-09-21T00:30:41.521895+00:00",
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
    "fetched_at": "2026-09-21T00:30:41.521895+00:00",
    "date_confidence": "high",
    "description": "<p><strong>Team:</strong> Apollo — Block Applied R&amp;D<br><strong>Location:</strong> Remote (US / Canada)<br><strong>Duration:</strong> Fall/Winter 2026 co-op — 8 months, flexibl"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5234092008",
    "title": "Bilingual Strategic Account Manager",
    "location": "Miami, FL, United States of America; US - NC - Remote",
    "official_url": "http://block.xyz/careers/jobs/5234092008?gh_jid=5234092008",
    "posted_date": "2026-05-28",
    "updated_date": "2026-09-16",
    "fetched_at": "2026-09-21T00:30:41.521895+00:00",
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
- Pages/requests fetched: 16
- HTTP requests/cumulative request time: 55 / 60.083s
- Company elapsed time: 68.184s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 39 / 0 / 0
- Detail cache statuses: {'fetched:new': 39}
- Raw jobs found: 104
- After US/location filtering: 39
- With trustworthy posted_date: 0
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 15.965, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 10.843, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 3.6, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 5.66, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 18.105, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.956, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 1.137, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.973, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 6.945, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 27}

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
    "fetched_at": "2026-09-21T00:30:42.208150+00:00",
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
    "fetched_at": "2026-09-21T00:30:42.208150+00:00",
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
    "fetched_at": "2026-09-21T00:30:42.208150+00:00",
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
    "fetched_at": "2026-09-21T00:30:42.208150+00:00",
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
    "fetched_at": "2026-09-21T00:30:42.208150+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.175s
- Company elapsed time: 0.812s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 297
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
    "fetched_at": "2026-09-21T00:30:43.045742+00:00",
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
    "fetched_at": "2026-09-21T00:30:43.045742+00:00",
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
    "fetched_at": "2026-09-21T00:30:43.045742+00:00",
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
    "fetched_at": "2026-09-21T00:30:43.045742+00:00",
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
    "fetched_at": "2026-09-21T00:30:43.045742+00:00",
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
- HTTP requests/cumulative request time: 138 / 53.022s
- Company elapsed time: 71.490s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 118 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 5, 'fetched:new': 113}
- Raw jobs found: 343
- After US/location filtering: 118
- With trustworthy posted_date: 118
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 29.874, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.344, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 8, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 1.662, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 15}
- Query diagnostic: {"elapsed_seconds": 15.486, "first_pass_survivors": 27, "group": "official", "jds_resolved": 27, "original_postings_resolved": 27, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 27, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.097, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.911, "first_pass_survivors": 8, "group": "official", "jds_resolved": 8, "original_postings_resolved": 8, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 8, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.552, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 13, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 13}
- Query diagnostic: {"elapsed_seconds": 0.68, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 4.147, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 3, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF087977W",
    "title": "Staff Software Engineer, AI Solutions",
    "location": "US - Denver, CO",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Denver-CO/Staff-Software-Engineer--AI-Solutions_REF087977W-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:43.858154+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088214W",
    "title": "Director, Product Builder",
    "location": "US - Foster City, CA; US - Austin, TX",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Director--Product-Builder_REF088214W",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:43.858154+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF085181W",
    "title": "Staff SW Engineer",
    "location": "US - Foster City, CA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Staff-SW-Engineer_REF085181W-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:43.858154+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF088621W",
    "title": "SW Engineer - Cyber (does not qualify for immigration support)",
    "location": "US - Foster City, CA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/SW-Engineer---Cyber--does-not-qualify-for-immigration-support-_REF088621W",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:43.858154+00:00",
    "date_confidence": "high",
    "description": "About Us Visa is a world leader in payments technology, facilitating transactions between consumers, merchants, financial institutions and government entities across more than 200 "
  },
  {
    "company": "Visa",
    "source": "visa_official_careers",
    "job_id": "REF082660W",
    "title": "Senior Software Engineer - Full Stack",
    "location": "US - Foster City, CA",
    "official_url": "https://visa.wd5.myworkdayjobs.com/Visa/job/US---Foster-City-CA/Senior-Software-Engineer---Full-Stack_REF082660W-2",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:43.858154+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.444s
- Company elapsed time: 0.457s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 16
- After US/location filtering: 12
- With trustworthy posted_date: 12
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
    "fetched_at": "2026-09-21T00:30:51.178554+00:00",
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
    "fetched_at": "2026-09-21T00:30:51.178554+00:00",
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
    "fetched_at": "2026-09-21T00:30:51.178554+00:00",
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
    "fetched_at": "2026-09-21T00:30:51.178554+00:00",
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
    "fetched_at": "2026-09-21T00:30:51.178554+00:00",
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
- HTTP requests/cumulative request time: 145 / 92.613s
- Company elapsed time: 112.835s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 121 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 119}
- Raw jobs found: 440
- After US/location filtering: 121
- With trustworthy posted_date: 121
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 50.545, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 4.53, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 20}
- Query diagnostic: {"elapsed_seconds": 2.395, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 16.984, "first_pass_survivors": 22, "group": "official", "jds_resolved": 22, "original_postings_resolved": 22, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 22, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.659, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.724, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 7.359, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.478, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 8.948, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 80}

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
    "fetched_at": "2026-09-21T00:30:51.635849+00:00",
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
    "fetched_at": "2026-09-21T00:30:51.635849+00:00",
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
    "fetched_at": "2026-09-21T00:30:51.635849+00:00",
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
    "fetched_at": "2026-09-21T00:30:51.635849+00:00",
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
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:51.635849+00:00",
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
- HTTP requests/cumulative request time: 53 / 29.246s
- Company elapsed time: 35.389s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 37 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1, 'fetched:new': 36}
- Raw jobs found: 158
- After US/location filtering: 37
- With trustworthy posted_date: 37
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 18.577, "first_pass_survivors": 30, "group": "official", "jds_resolved": 30, "original_postings_resolved": 30, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 0.914, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.8, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 10, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 10}
- Query diagnostic: {"elapsed_seconds": 2.633, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 9, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 9}
- Query diagnostic: {"elapsed_seconds": 4.221, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 31, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 31}
- Query diagnostic: {"elapsed_seconds": 4.268, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 36, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 36}
- Query diagnostic: {"elapsed_seconds": 1.03, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 1.02, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.866, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 15, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 15}

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
    "fetched_at": "2026-09-21T00:30:53.368575+00:00",
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
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:53.368575+00:00",
    "date_confidence": "high",
    "description": "About the team The Agentic AI team at Zillow is at the forefront of transforming the real estate industry by helping millions of people use AI technologies to find their next home."
  },
  {
    "company": "Zillow",
    "source": "zillow_official_careers",
    "job_id": "P748682",
    "title": "Principal Machine Learning Engineer, Agentic AI",
    "location": "Remote-USA",
    "official_url": "https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Principal-Machine-Learning-Engineer--Agentic-AI_P748682-2",
    "posted_date": "2026-09-15",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:30:53.368575+00:00",
    "date_confidence": "high",
    "description": "About the team The Agentic AI team at Zillow is at the forefront of transforming the real estate industry by helping millions of people use AI assistants to find their next home. W"
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
    "fetched_at": "2026-09-21T00:30:53.368575+00:00",
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
    "fetched_at": "2026-09-21T00:30:53.368575+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.372s
- Company elapsed time: 1.232s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 370
- After US/location filtering: 227
- With trustworthy posted_date: 227
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:31:10.268621+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:31:10.268621+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:31:10.268621+00:00",
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
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:31:10.268621+00:00",
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
    "fetched_at": "2026-09-21T00:31:10.268621+00:00",
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
- HTTP requests/cumulative request time: 12 / 5.751s
- Company elapsed time: 6.000s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 2 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1, 'fetched:new': 1}
- Raw jobs found: 9
- After US/location filtering: 2
- With trustworthy posted_date: 2
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.775, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.787, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.417, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.425, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.744, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.41, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 0.769, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.58, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.466, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}

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
    "fetched_at": "2026-09-21T00:31:11.501821+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity Chewy is growing! We're looking for a Software Engineer III to help define and scale the frontend foundations that power consistent, accessible, an"
  },
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R30459",
    "title": "Machine Learning Engineer II",
    "location": "Richardson, TX; USA - MA - Boston - BOS1; USA - FL - Plantation - FLL7; Bellevue, WA",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/Richardson-TX/Machine-Learning-Engineer-II_R30459-1",
    "posted_date": "2026-09-13",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:11.501821+00:00",
    "date_confidence": "high",
    "description": "Job Description: Summary: We are seeking a talented and passionate Machine Learning Engineer II to join our growing team. In this role, you will play a crucial part in building and"
  }
]
```

## CVS Health

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 142 / 74.769s
- Company elapsed time: 94.040s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 120 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 118}
- Raw jobs found: 365
- After US/location filtering: 120
- With trustworthy posted_date: 120
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 52.799, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.626, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 2, "query": "machine learning engineer", "raw_jobs": 23, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 23}
- Query diagnostic: {"elapsed_seconds": 1.252, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 11.313, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 6.842, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.35, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 5.85, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 33, "stop_reason": "early_stop", "unique_contribution": 10, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 0.217, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 6.468, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1029588",
    "title": "Lead Director - Security Operations Center (SOC)",
    "location": "NY - New York",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/NY---New-York/Lead-Director---Security-Operations-Center--SOC-_R1029588",
    "posted_date": "2026-09-20",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:17.502849+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R0821040",
    "title": "Lead Java Software Engineer",
    "location": "Work At Home-Connecticut; Work At Home-Ohio; Work At Home-Texas; Work At Home-Georgia; Work At Home-Massachusetts; Work At Home-Minnesota; Work At Home-Alabama; Work At Home-Missouri; Work At Home-Michigan; Work At Home-Virginia; Work At Home-Illinois; Work At Home-North Carolina; Work At Home-Kansas; Work At Home-Colorado; Work At Home-Florida; Work At Home-Indiana; Work At Home-Kentucky; Work At Home-Tennessee",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/Work-At-Home-Connecticut/Staff-Software-Development-Engineer_R0821040",
    "posted_date": "2026-09-20",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:17.502849+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1008983",
    "title": "Manager, AI Search Strategy and Customer Experience",
    "location": "RI - Work from home",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/RI---Work-from-home/Manager--AI-search-Strategy-and-Customer-Experience_R1008983-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:17.502849+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R1037882",
    "title": "Senior Manager - Software Development Engineering",
    "location": "Work At Home-Colorado",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/Work-At-Home-Colorado/Senior-Manager---Software-Development-Engineering_R1037882-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:17.502849+00:00",
    "date_confidence": "high",
    "description": "We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passion"
  },
  {
    "company": "CVS Health",
    "source": "cvs_health_official_careers",
    "job_id": "R0954957",
    "title": "Software Engineer - Search and Personalization",
    "location": "",
    "official_url": "https://cvshealth.wd1.myworkdayjobs.com/CVS_Health_Careers/job/Software-Engineer---Search-and-Personalization_R0954957",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:17.502849+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.165s
- Company elapsed time: 0.384s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 81
- After US/location filtering: 73
- With trustworthy posted_date: 73
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8705196002",
    "title": "Ad Sales Lead - West",
    "location": "Remote - California; Remote",
    "official_url": "https://careers.duolingo.com/jobs/8705196002?gh_jid=8705196002",
    "posted_date": "2026-08-13",
    "updated_date": "2026-09-03",
    "fetched_at": "2026-09-21T00:31:28.758632+00:00",
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
    "fetched_at": "2026-09-21T00:31:28.758632+00:00",
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
    "fetched_at": "2026-09-21T00:31:28.758632+00:00",
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
    "fetched_at": "2026-09-21T00:31:28.758632+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8658654002",
    "title": "Creative Sourcer",
    "location": "Pittsburgh, PA; Pittsburgh, Pennsylvania, United States",
    "official_url": "https://careers.duolingo.com/jobs/8658654002?gh_jid=8658654002",
    "posted_date": "2026-07-30",
    "updated_date": "2026-08-20",
    "fetched_at": "2026-09-21T00:31:28.758632+00:00",
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
- HTTP requests/cumulative request time: 40 / 5.129s
- Company elapsed time: 8.620s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 30 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 30
- After US/location filtering: 30
- With trustworthy posted_date: 6
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 8.459, "first_pass_survivors": 30, "group": "official", "jds_resolved": 6, "original_postings_resolved": 30, "page_budget": 2, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 30, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 0.02, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.019, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.019, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.019, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.019, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.024, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.02, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.021, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 2, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}

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
    "fetched_at": "2026-09-21T00:31:29.143048+00:00",
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
    "fetched_at": "2026-09-21T00:31:29.143048+00:00",
    "date_confidence": "high",
    "description": "Who are we? Equinix is the world’s digital infrastructure company®, shortening the path to connectivity to enable the innovations that enrich our work, life and planet. A place whe"
  },
  {
    "company": "Equinix",
    "source": "equinix_official_careers",
    "job_id": "JR-163188",
    "title": "Senior Principal Engineer, Enterprise Networking Architecture, Automation and AI",
    "location": "Toronto, Ontario, Canada; Redwood City, California, United States; Dallas, Texas, United States",
    "official_url": "https://careers.equinix.com/jobs/senior-principal-engineer-enterprise-networking-architecture-automation-and-ai-dallas-texas-united-states-redwood-city-california-toronto-ontario-canada",
    "posted_date": "2026-09-10",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:29.143048+00:00",
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
    "fetched_at": "2026-09-21T00:31:29.143048+00:00",
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
    "fetched_at": "2026-09-21T00:31:29.143048+00:00",
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
- HTTP requests/cumulative request time: 16 / 7.453s
- Company elapsed time: 8.832s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 1 / 0 / 0
- Detail cache statuses: {'fetched:new': 1}
- Raw jobs found: 111
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 1.859, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 2, "query": "ai engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.445, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.456, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.134, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "solutions architect", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.145, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "data engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.157, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 2, "query": "platform engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.485, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.442, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.134, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 2, "query": "software engineer", "raw_jobs": 20, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}

Sample normalized records:

```json
[
  {
    "company": "F5",
    "source": "f5_official_careers",
    "job_id": "RP1038786",
    "title": "Sr. People Analytics Solutions Consultant",
    "location": "Seattle; San Jose",
    "official_url": "https://ffive.wd5.myworkdayjobs.com/f5jobs/job/Seattle/Sr-People-Analytics-Solutions-Consultant_RP1038786",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:37.764010+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.150s
- Company elapsed time: 0.362s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 111
- After US/location filtering: 100
- With trustworthy posted_date: 100
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
    "fetched_at": "2026-09-21T00:31:46.597111+00:00",
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
    "fetched_at": "2026-09-21T00:31:46.597111+00:00",
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
    "fetched_at": "2026-09-21T00:31:46.597111+00:00",
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
    "fetched_at": "2026-09-21T00:31:46.597111+00:00",
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
    "fetched_at": "2026-09-21T00:31:46.597111+00:00",
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
- Pages/requests fetched: 19
- HTTP requests/cumulative request time: 111 / 53.852s
- Company elapsed time: 68.989s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 91 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1, 'fetched:new': 90}
- Raw jobs found: 324
- After US/location filtering: 91
- With trustworthy posted_date: 91
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 32.823, "first_pass_survivors": 56, "group": "official", "jds_resolved": 56, "original_postings_resolved": 56, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 56, "stop_reason": "page_budget", "unique_contribution": 56, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 2.538, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 19, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 19}
- Query diagnostic: {"elapsed_seconds": 0.943, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 13.71, "first_pass_survivors": 19, "group": "official", "jds_resolved": 19, "original_postings_resolved": 19, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 19, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.849, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.573, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 0.985, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.954, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 3.442, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 60}

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
    "fetched_at": "2026-09-21T00:31:46.960098+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Principal AI Engineer to join the CCIBT Gen AI team, which is responsible for building AI frameworks, intelligent agents, and technology p"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-576430",
    "title": "Principal Engineer (AI Engineering)",
    "location": "COLUMBUS, OH",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/COLUMBUS-OH/Principal-Engineer--AI-Engineering-_R-576430",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:46.960098+00:00",
    "date_confidence": "high",
    "description": "About this role: Wells Fargo is seeking a Principal Engineer (AI Engineering Productivity & Enablement) within Technology as part of COO (Chief Operating Office) Technology's Engin"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-573422",
    "title": "Senior Lead Technology Risk Officer (Application Domain, SDLC, DevOps and AI)",
    "location": "CHARLOTTE, NC; IRVING, TX",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/CHARLOTTE-NC/Senior-Lead-Technology-Risk-Officer--Application-Domain--SDLC--DevOps-and-AI-_R-573422-1",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:46.960098+00:00",
    "date_confidence": "high",
    "description": "About this role: The Application Risk Domain Officer operates within Technology Risk Management (TRM), part of Corporate Risk, providing independent second line oversight across ap"
  },
  {
    "company": "Wells Fargo",
    "source": "wells_fargo_official_careers",
    "job_id": "R-564887",
    "title": "Principal Engineer Automation",
    "location": "IRVING, TX; CHANDLER, AZ; CHARLOTTE, NC",
    "official_url": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs/job/IRVING-TX/Principal-Engineer-Automation_R-564887",
    "posted_date": "2026-09-17",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:31:46.960098+00:00",
    "date_confidence": "high",
    "description": "In This Role, You Will Software Architecture and Engineering Act as a trusted technical advisor to senior leadership, influencing the architecture and development of applications, "
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
    "fetched_at": "2026-09-21T00:31:46.960098+00:00",
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
- Pages/requests fetched: 21
- HTTP requests/cumulative request time: 92 / 42.428s
- Company elapsed time: 54.930s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 70 / 0 / 0
- Detail cache statuses: {'fetched:new': 70}
- Raw jobs found: 290
- After US/location filtering: 70
- With trustworthy posted_date: 70
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 33.858, "first_pass_survivors": 60, "group": "official", "jds_resolved": 60, "original_postings_resolved": 60, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 60, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.627, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 1.544, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 5.238, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 33, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 33}
- Query diagnostic: {"elapsed_seconds": 3.6, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.328, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 58, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 58}
- Query diagnostic: {"elapsed_seconds": 0.677, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 12, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 12}
- Query diagnostic: {"elapsed_seconds": 0.644, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 2.61, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 31, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 31}

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
    "fetched_at": "2026-09-21T00:31:50.392891+00:00",
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
    "fetched_at": "2026-09-21T00:31:50.392891+00:00",
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
    "fetched_at": "2026-09-21T00:31:50.392891+00:00",
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
    "fetched_at": "2026-09-21T00:31:50.392891+00:00",
    "date_confidence": "high",
    "description": "Yahoo serves as a trusted guide for hundreds of millions of people globally, helping them achieve their goals online through our portfolio of iconic products. For advertisers, Yaho"
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
    "fetched_at": "2026-09-21T00:31:50.392891+00:00",
    "date_confidence": "high",
    "description": "It takes powerful technology to connect our brands and partners with an audience of hundreds of millions of people. Whether you’re looking to write mobile app code, engineer the se"
  }
]
```

## Ansys

- Status: ok
- Scraping method: HTTP GET server-rendered Radancy/TalentBrew search + JobPosting JSON-LD
- Search URL/API: `https://careers.synopsys.com/search-jobs`
- Pagination: p=1,2,...; stop on empty/repeat/short page
- Pages/requests fetched: 3
- HTTP requests/cumulative request time: 29 / 8.562s
- Company elapsed time: 12.437s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 26 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 45
- After US/location filtering: 26
- With trustworthy posted_date: 26
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 12.437, "first_pass_survivors": 26, "group": "official", "jds_resolved": 26, "original_postings_resolved": 26, "page_budget": 3, "pages_fetched": 3, "query": "Ansys", "raw_jobs": 45, "stop_reason": "page_budget", "unique_contribution": 26, "unique_jobs": 45}

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
    "fetched_at": "2026-09-21T00:31:55.349511+00:00",
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
    "fetched_at": "2026-09-21T00:31:55.349511+00:00",
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
    "fetched_at": "2026-09-21T00:31:55.349511+00:00",
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
    "fetched_at": "2026-09-21T00:31:55.349511+00:00",
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
    "fetched_at": "2026-09-21T00:31:55.349511+00:00",
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
- HTTP requests/cumulative request time: 191 / 75.914s
- Company elapsed time: 100.573s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 169 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 167}
- Raw jobs found: 325
- After US/location filtering: 169
- With trustworthy posted_date: 169
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 39.362, "first_pass_survivors": 80, "group": "official", "jds_resolved": 80, "original_postings_resolved": 80, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 80, "unique_jobs": 80}
- Query diagnostic: {"elapsed_seconds": 6.87, "first_pass_survivors": 14, "group": "official", "jds_resolved": 14, "original_postings_resolved": 14, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 14, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 1.011, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 8.286, "first_pass_survivors": 10, "group": "official", "jds_resolved": 10, "original_postings_resolved": 10, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 10, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 14.955, "first_pass_survivors": 29, "group": "official", "jds_resolved": 29, "original_postings_resolved": 29, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 29, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 8.065, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 35, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 5.947, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 1.039, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 13.283, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 80, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 80}

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
    "fetched_at": "2026-09-21T00:32:07.787509+00:00",
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
    "fetched_at": "2026-09-21T00:32:07.787509+00:00",
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
    "fetched_at": "2026-09-21T00:32:07.787509+00:00",
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
    "fetched_at": "2026-09-21T00:32:07.787509+00:00",
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
    "fetched_at": "2026-09-21T00:32:07.787509+00:00",
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
- HTTP requests/cumulative request time: 45 / 20.808s
- Company elapsed time: 25.390s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 33 / 0 / 0
- Detail cache statuses: {'fetched:new': 33}
- Raw jobs found: 82
- After US/location filtering: 33
- With trustworthy posted_date: 33
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 5.657, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 11, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 1.173, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 3.04, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 3.027, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 7, "stop_reason": "early_stop", "unique_contribution": 5, "unique_jobs": 7}
- Query diagnostic: {"elapsed_seconds": 8.043, "first_pass_survivors": 11, "group": "official", "jds_resolved": 11, "original_postings_resolved": 11, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 25, "stop_reason": "page_budget", "unique_contribution": 11, "unique_jobs": 25}
- Query diagnostic: {"elapsed_seconds": 0.762, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 0.8, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.802, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 1.149, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 16}

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
    "fetched_at": "2026-09-21T00:32:44.472111+00:00",
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
    "fetched_at": "2026-09-21T00:32:44.472111+00:00",
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
    "fetched_at": "2026-09-21T00:32:44.472111+00:00",
    "date_confidence": "high",
    "description": "We are seeking Manager for our Laboratory Automation & AI Transformation Lab to join IQVIA Laboratories at Durham, NC . We hire passionate innovators who drive healthcare forward t"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1548171",
    "title": "Associate Director, Product Management – AIM XR (IQVIA Digital)",
    "location": "Parsippany, New Jersey, United States of America; Washington, DC; Atlanta, GA; Hartford, CT; Boston, MA; Miami, FL; Philadelphia, PA; Newark, NJ; Austin, TX; New York, NY",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Parsippany-New-Jersey-United-States-of-America/Personalization-Science-Product-Leader--IQVIA-Digital_R1548171",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:32:44.472111+00:00",
    "date_confidence": "high",
    "description": "IQVIA Digital Overview: IQVIA Digital powers exceptional brand experiences, delivering innovative solutions based on a customer-first, insights-driven, and integrated omnichannel v"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1526366",
    "title": "Senior Software Engineer (React), IQVIA Digital",
    "location": "Red Bank, NJ, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Red-Bank-NJ-United-States-of-America/Senior-Software-Engineer_R1526366",
    "posted_date": "2026-08-19",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:32:44.472111+00:00",
    "date_confidence": "high",
    "description": "IQVIA Digital Overview: IQVIA Digital powers exceptional brand experiences, delivering innovative solutions based on a customer-first, insights-driven, and integrated omnichannel v"
  }
]
```

## Johnson & Johnson

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://jj.wd5.myworkdayjobs.com/JJ`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 24
- HTTP requests/cumulative request time: 213 / 82.183s
- Company elapsed time: 110.961s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 188 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 8, 'fetched:new': 180}
- Raw jobs found: 432
- After US/location filtering: 188
- With trustworthy posted_date: 188
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 33.726, "first_pass_survivors": 59, "group": "official", "jds_resolved": 59, "original_postings_resolved": 59, "page_budget": 3, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 59, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 17.762, "first_pass_survivors": 32, "group": "official", "jds_resolved": 32, "original_postings_resolved": 32, "page_budget": 3, "pages_fetched": 3, "query": "machine learning engineer", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 32, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 22.331, "first_pass_survivors": 40, "group": "official", "jds_resolved": 40, "original_postings_resolved": 40, "page_budget": 3, "pages_fetched": 3, "query": "data scientist", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 40, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 12.686, "first_pass_survivors": 20, "group": "official", "jds_resolved": 20, "original_postings_resolved": 20, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 20, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 9.767, "first_pass_survivors": 16, "group": "official", "jds_resolved": 16, "original_postings_resolved": 16, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 16, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 3.605, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 4, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.796, "first_pass_survivors": 9, "group": "official", "jds_resolved": 9, "original_postings_resolved": 9, "page_budget": 3, "pages_fetched": 2, "query": "full stack engineer", "raw_jobs": 27, "stop_reason": "early_stop", "unique_contribution": 9, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 0.822, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 5.094, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 7, "unique_jobs": 60}

Sample normalized records:

```json
[
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-099961",
    "title": "Senior Ontologist, Biologics Discovery",
    "location": "Spring House, Pennsylvania, United States of America; Raritan, New Jersey, United States of America; Titusville, New Jersey, United States of America; Madrid, Spain; Beerse, Antwerp, Belgium",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Spring-House-Pennsylvania-United-States-of-America/Senior-Ontologist--Biologics-Discovery_R-099961-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:32:45.324437+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-099955",
    "title": "Principal Data Engineer, Biologics Discovery",
    "location": "Spring House, Pennsylvania, United States of America; Raritan, New Jersey, United States of America; Titusville, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Spring-House-Pennsylvania-United-States-of-America/Principal-Data-Engineer--Biologics-Discovery_R-099955-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:32:45.324437+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-099962",
    "title": "Senior Machine Learning Engineer, Biologics Discovery",
    "location": "Spring House, Pennsylvania, United States of America; Raritan, New Jersey, United States of America; Titusville, New Jersey, United States of America; Madrid, Spain; Beerse, Antwerp, Belgium",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Spring-House-Pennsylvania-United-States-of-America/Senior-Machine-Learning-Engineer--Biologics-Discovery_R-099962-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:32:45.324437+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-100342",
    "title": "Senior AI Engineer",
    "location": "Titusville, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Titusville-New-Jersey-United-States-of-America/Senior-AI-Engineer_R-100342",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:32:45.324437+00:00",
    "date_confidence": "high",
    "description": "At Johnson & Johnson, we believe health is everything. Our strength in healthcare innovation empowers us to build a world where complex diseases are prevented, treated, and cured, "
  },
  {
    "company": "Johnson & Johnson",
    "source": "johnson_&_johnson_official_careers",
    "job_id": "R-095200",
    "title": "Senior Director, Global Commercial Data Platforms & AI Engineering",
    "location": "Raritan, New Jersey, United States of America",
    "official_url": "https://jj.wd5.myworkdayjobs.com/JJ/job/Raritan-New-Jersey-United-States-of-America/Senior-Director--Global-Commercial-Data-Platforms---AI-Engineering_R-095200-1",
    "posted_date": "2026-09-18",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:32:45.324437+00:00",
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
- HTTP requests/cumulative request time: 43 / 18.142s
- Company elapsed time: 22.991s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 27 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1, 'fetched:new': 26}
- Raw jobs found: 109
- After US/location filtering: 27
- With trustworthy posted_date: 27
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 7.749, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 4, "pages_fetched": 1, "query": "ai engineer", "raw_jobs": 17, "stop_reason": "early_stop", "unique_contribution": 17, "unique_jobs": 17}
- Query diagnostic: {"elapsed_seconds": 0.578, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.705, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 2.439, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 11, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 11}
- Query diagnostic: {"elapsed_seconds": 4.937, "first_pass_survivors": 6, "group": "official", "jds_resolved": 6, "original_postings_resolved": 6, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 26, "stop_reason": "page_budget", "unique_contribution": 6, "unique_jobs": 26}
- Query diagnostic: {"elapsed_seconds": 2.326, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 21, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 21}
- Query diagnostic: {"elapsed_seconds": 0.554, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}
- Query diagnostic: {"elapsed_seconds": 0.555, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 2.484, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 3, "query": "software engineer", "raw_jobs": 21, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 21}

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
    "fetched_at": "2026-09-21T00:32:51.543633+00:00",
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
    "fetched_at": "2026-09-21T00:32:51.543633+00:00",
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
    "fetched_at": "2026-09-21T00:32:51.543633+00:00",
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
    "fetched_at": "2026-09-21T00:32:51.543633+00:00",
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
    "fetched_at": "2026-09-21T00:32:51.543633+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.915s
- Company elapsed time: 0.960s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 86
- After US/location filtering: 79
- With trustworthy posted_date: 79
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
    "fetched_at": "2026-09-21T00:32:55.950112+00:00",
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
    "fetched_at": "2026-09-21T00:32:55.950112+00:00",
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
    "fetched_at": "2026-09-21T00:32:55.950112+00:00",
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
    "fetched_at": "2026-09-21T00:32:55.950112+00:00",
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
    "fetched_at": "2026-09-21T00:32:55.950112+00:00",
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
- Pages/requests fetched: 20
- HTTP requests/cumulative request time: 152 / 45.130s
- Company elapsed time: 64.642s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 131 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1, 'fetched:new': 130}
- Raw jobs found: 222
- After US/location filtering: 131
- With trustworthy posted_date: 131
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 15.307, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 35, "stop_reason": "early_stop", "unique_contribution": 34, "unique_jobs": 35}
- Query diagnostic: {"elapsed_seconds": 0.64, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 1.345, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 2, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 2}
- Query diagnostic: {"elapsed_seconds": 8.074, "first_pass_survivors": 15, "group": "official", "jds_resolved": 15, "original_postings_resolved": 15, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 15, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 17.125, "first_pass_survivors": 41, "group": "official", "jds_resolved": 41, "original_postings_resolved": 41, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 41, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 4.396, "first_pass_survivors": 5, "group": "official", "jds_resolved": 5, "original_postings_resolved": 5, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 27, "stop_reason": "page_budget", "unique_contribution": 5, "unique_jobs": 27}
- Query diagnostic: {"elapsed_seconds": 0.628, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "full stack engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 0.61, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 1, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 1}
- Query diagnostic: {"elapsed_seconds": 15.753, "first_pass_survivors": 34, "group": "official", "jds_resolved": 34, "original_postings_resolved": 34, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 72, "stop_reason": "page_budget", "unique_contribution": 34, "unique_jobs": 72}

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
    "fetched_at": "2026-09-21T00:32:56.910796+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid We're hiring a Staff AI Engineer to build GenAI and voice agents for medical devices, deployed both on-device and in the cloud. You'll own the technical di"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R570975",
    "title": "Senior Principal Engineer, Innovation Lab (Remote)",
    "location": "Kalamazoo, Michigan; Flower Mound, Texas; Mahwah, New Jersey",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Kalamazoo-Michigan/Senior-Principal-Engineer--Innovation-Lab--Remote-_R570975-1",
    "posted_date": "2026-09-16",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:32:56.910796+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Remote or Hybrid or Onsite What you will do: As our Senior Principal Engineer, you will serve as the Enterprise Digital Technology Innovation Lab's lead software "
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
    "fetched_at": "2026-09-21T00:32:56.910796+00:00",
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
    "fetched_at": "2026-09-21T00:32:56.910796+00:00",
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
    "fetched_at": "2026-09-21T00:32:56.910796+00:00",
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
- HTTP requests/cumulative request time: 44 / 15.518s
- Company elapsed time: 20.255s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 30 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 1, 'fetched:new': 29}
- Raw jobs found: 116
- After US/location filtering: 30
- With trustworthy posted_date: 30
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 11.52, "first_pass_survivors": 24, "group": "official", "jds_resolved": 24, "original_postings_resolved": 24, "page_budget": 4, "pages_fetched": 3, "query": "ai engineer", "raw_jobs": 24, "stop_reason": "early_stop", "unique_contribution": 24, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 0.496, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 1.217, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 2.004, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "solutions architect", "raw_jobs": 14, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 14}
- Query diagnostic: {"elapsed_seconds": 0.488, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "data engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 0.489, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "platform engineer", "raw_jobs": 16, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 16}
- Query diagnostic: {"elapsed_seconds": 2.099, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 24, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 24}
- Query diagnostic: {"elapsed_seconds": 0.69, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "forward deployed engineer", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.469, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 4, "pages_fetched": 1, "query": "software engineer", "raw_jobs": 8, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 8}

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
    "fetched_at": "2026-09-21T00:33:09.863143+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview This role reports directly to Senior Manager, Data Science & Analytics "
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
    "fetched_at": "2026-09-21T00:33:09.863143+00:00",
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
    "fetched_at": "2026-09-21T00:33:09.863143+00:00",
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
    "fetched_at": "2026-09-21T00:33:09.863143+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The Global Infrastructure, Engineering & Operations (GIO) organization "
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042363",
    "title": "Staff Site Reliability Engineer",
    "location": "Chicago, Illinois; Reston, Virginia; Crum Lynne, Pennsylvania; Boca Raton, Florida; White Plains, New York",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Staff-Site-Reliability-Engineer_19042363",
    "posted_date": "2026-09-11",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:33:09.863143+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview At TransUnion, this role will report to a DevOps Director. The Site Rel"
  }
]
```

## Travelers

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://travelers.wd5.myworkdayjobs.com/External`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 25
- HTTP requests/cumulative request time: 118 / 51.257s
- Company elapsed time: 67.609s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 92 / 0 / 0
- Detail cache statuses: {'fetched:missing_detail': 2, 'fetched:new': 90}
- Raw jobs found: 349
- After US/location filtering: 92
- With trustworthy posted_date: 92
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 25.376, "first_pass_survivors": 44, "group": "official", "jds_resolved": 44, "original_postings_resolved": 44, "page_budget": 4, "pages_fetched": 4, "query": "ai engineer", "raw_jobs": 44, "stop_reason": "page_budget", "unique_contribution": 44, "unique_jobs": 44}
- Query diagnostic: {"elapsed_seconds": 3.805, "first_pass_survivors": 7, "group": "official", "jds_resolved": 7, "original_postings_resolved": 7, "page_budget": 3, "pages_fetched": 1, "query": "machine learning engineer", "raw_jobs": 18, "stop_reason": "early_stop", "unique_contribution": 7, "unique_jobs": 18}
- Query diagnostic: {"elapsed_seconds": 2.596, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "data scientist", "raw_jobs": 4, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 4}
- Query diagnostic: {"elapsed_seconds": 11.156, "first_pass_survivors": 17, "group": "official", "jds_resolved": 17, "original_postings_resolved": 17, "page_budget": 3, "pages_fetched": 3, "query": "solutions architect", "raw_jobs": 56, "stop_reason": "page_budget", "unique_contribution": 17, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 11.199, "first_pass_survivors": 18, "group": "official", "jds_resolved": 18, "original_postings_resolved": 18, "page_budget": 3, "pages_fetched": 3, "query": "data engineer", "raw_jobs": 60, "stop_reason": "page_budget", "unique_contribution": 18, "unique_jobs": 60}
- Query diagnostic: {"elapsed_seconds": 2.81, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 3, "query": "platform engineer", "raw_jobs": 56, "stop_reason": "page_budget", "unique_contribution": 1, "unique_jobs": 56}
- Query diagnostic: {"elapsed_seconds": 2.539, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "full stack engineer", "raw_jobs": 22, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 22}
- Query diagnostic: {"elapsed_seconds": 2.604, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 3, "query": "forward deployed engineer", "raw_jobs": 30, "stop_reason": "page_budget", "unique_contribution": 0, "unique_jobs": 30}
- Query diagnostic: {"elapsed_seconds": 4.702, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 4, "pages_fetched": 4, "query": "software engineer", "raw_jobs": 59, "stop_reason": "page_budget", "unique_contribution": 2, "unique_jobs": 59}

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
    "fetched_at": "2026-09-21T00:33:14.535442+00:00",
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
    "fetched_at": "2026-09-21T00:33:14.535442+00:00",
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
    "fetched_at": "2026-09-21T00:33:14.535442+00:00",
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
    "fetched_at": "2026-09-21T00:33:14.535442+00:00",
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
    "fetched_at": "2026-09-21T00:33:14.535442+00:00",
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
- HTTP requests/cumulative request time: 20 / 3.281s
- Company elapsed time: 3.482s
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused/prefilter skipped: 14 / 0 / 0
- Detail cache statuses: none
- Raw jobs found: 25
- After US/location filtering: 14
- With trustworthy posted_date: 14
- Errors/403s: none

- Query diagnostic: {"elapsed_seconds": 0.741, "first_pass_survivors": 3, "group": "official", "jds_resolved": 3, "original_postings_resolved": 3, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 3, "stop_reason": "early_stop", "unique_contribution": 3, "unique_jobs": 3}
- Query diagnostic: {"elapsed_seconds": 0.371, "first_pass_survivors": 1, "group": "official", "jds_resolved": 1, "original_postings_resolved": 1, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 1, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.37, "first_pass_survivors": 2, "group": "official", "jds_resolved": 2, "original_postings_resolved": 2, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 6, "stop_reason": "early_stop", "unique_contribution": 2, "unique_jobs": 6}
- Query diagnostic: {"elapsed_seconds": 0.821, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}
- Query diagnostic: {"elapsed_seconds": 0.212, "first_pass_survivors": 0, "group": "official", "jds_resolved": 0, "original_postings_resolved": 0, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 0, "stop_reason": "early_stop", "unique_contribution": 0, "unique_jobs": 0}
- Query diagnostic: {"elapsed_seconds": 0.966, "first_pass_survivors": 4, "group": "official", "jds_resolved": 4, "original_postings_resolved": 4, "page_budget": 3, "pages_fetched": 1, "query": "", "raw_jobs": 5, "stop_reason": "early_stop", "unique_contribution": 4, "unique_jobs": 5}

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
    "fetched_at": "2026-09-21T00:33:30.118600+00:00",
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
    "fetched_at": "2026-09-21T00:33:30.118600+00:00",
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
    "fetched_at": "2026-09-21T00:33:30.118600+00:00",
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
    "fetched_at": "2026-09-21T00:33:30.118600+00:00",
    "date_confidence": "high",
    "description": "When you join Verizon You want more out of a career. A place to share your ideas freely — even if they’re daring or different. Where the true you can learn, grow, and thrive. At Ve"
  },
  {
    "company": "Verizon",
    "source": "verizon_official_careers",
    "job_id": "r-1099596",
    "title": "Principal Data Scientist",
    "location": "Basking Ridge, New Jersey; Alpharetta, Georgia; Irving, Texas",
    "official_url": "https://mycareer.verizon.com/jobs/r-1099596/principal-data-scientist/",
    "posted_date": "2026-09-03",
    "updated_date": "",
    "fetched_at": "2026-09-21T00:33:30.118600+00:00",
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
- HTTP requests/cumulative request time: 1 / 0.307s
- Company elapsed time: 0.347s
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused/prefilter skipped: 0 / 0 / 0
- Detail cache statuses: none
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
    "job_id": "8054682",
    "title": "Associate Marketing Operations/ Automation Manager",
    "location": "Remote - New York, NY; Remote - U.S.",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8054682",
    "posted_date": "2026-07-15",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-09-21T00:33:33.601004+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "8046381",
    "title": "Customer Success Manager, Enterprise",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/8046381",
    "posted_date": "2026-09-18",
    "updated_date": "2026-09-18",
    "fetched_at": "2026-09-21T00:33:33.601004+00:00",
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
    "fetched_at": "2026-09-21T00:33:33.601004+00:00",
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
    "fetched_at": "2026-09-21T00:33:33.601004+00:00",
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
    "fetched_at": "2026-09-21T00:33:33.601004+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
