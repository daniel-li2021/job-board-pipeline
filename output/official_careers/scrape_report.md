# Official careers scrape report — 2026-08-31_1758

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Software+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 23
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 433
- After US/location filtering: 228
- With trustworthy posted_date: 228
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "77161400903836358",
    "title": "Software Engineer, Embedded Systems/Firmware, Platforms and Devices",
    "location": "San Jose, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/77161400903836358-software-engineer-embedded-systems-firmware-platforms-and-devices",
    "posted_date": "2026-08-31",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T17:58:57.078495+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "96263216413188806",
    "title": "Senior Software Engineer, Generative AI, Shopping Product Graph, Commerce",
    "location": "Pittsburgh, PA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/96263216413188806-senior-software-engineer-generative-ai-shopping-product-graph-commerce",
    "posted_date": "2026-08-31",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T17:58:57.078495+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "83915700833264326",
    "title": "Software Engineer",
    "location": "Pittsburgh, PA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/83915700833264326-software-engineer",
    "posted_date": "2026-08-31",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T17:58:57.078495+00:00",
    "date_confidence": "high",
    "description": "The US base salary range for this full-time position is $147,000 - $211,000 + 15% bonus target + equity + benefits determined by role, level, and location. Individual pay is determ"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "106684387621249734",
    "title": "Software Engineer",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/106684387621249734-software-engineer",
    "posted_date": "2026-08-31",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T17:58:57.078495+00:00",
    "date_confidence": "high",
    "description": "Artificial intelligence will be one of humanity’s most transformative inventions. At Google DeepMind, we are a pioneering AI lab with exceptional interdisciplinary teams focused on"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "140763200768352966",
    "title": "Software Engineer, Generative AI, Shopping on Gemini",
    "location": "Pittsburgh, PA, USA; Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/140763200768352966-software-engineer-generative-ai-shopping-on-gemini",
    "posted_date": "2026-08-31",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T17:58:57.078495+00:00",
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
- Pages/requests fetched: 35
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 678
- After US/location filtering: 464
- With trustworthy posted_date: 464
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10522267",
    "title": "Software Development Engineer, AWS OpenSearch Service",
    "location": "Austin, Texas, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10522267/software-development-engineer-aws-opensearch-service",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T17:59:12.358841+00:00",
    "date_confidence": "high",
    "description": "Imagine running search and analytics at any scale without thinking about clusters, capacity, or version upgrades. Where your queries return in milliseconds whether you're indexing "
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10522049",
    "title": "Software Development Engineer , Cryptography and Identity Management",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10522049/software-development-engineer-cryptography-and-identity-management",
    "posted_date": "2026-08-31",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T17:59:12.358841+00:00",
    "date_confidence": "high",
    "description": "We are currently looking for a Software Development Engineer to join our systems organization. You love to work with internal and external customers to execute projects and resolve"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10522051",
    "title": "Software Dev Engineer II, Atlas Telemetry",
    "location": "Redmond, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10522051/software-dev-engineer-ii-atlas-telemetry",
    "posted_date": "2026-08-31",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T17:59:12.358841+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon’s low Earth orbit satellite network. Our mission is to deliver fast, reliable internet connectivity to customers beyond the reach of existing networks. From in"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10519775",
    "title": "Software Development Manager, Amazon Leo Data Platform",
    "location": "Redmond, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10519775/software-development-manager-amazon-leo-data-platform",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-31T17:59:12.358841+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon’s low Earth orbit satellite network. Our mission is to deliver fast, reliable internet connectivity to customers beyond the reach of existing networks. From in"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10521254",
    "title": "Senior Software Development Engineer, Amazon Leo - Developer Productivity, AI, Test and Simulation",
    "location": "Redmond, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10521254/senior-software-development-engineer-amazon-leo-developer-productivity-ai-test-and-simulation",
    "posted_date": "2026-08-29",
    "updated_date": "2026-08-29",
    "fetched_at": "2026-08-31T17:59:12.358841+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon’s low Earth orbit satellite network. Our mission is to deliver fast, reliable internet connectivity to customers beyond the reach of existing networks. From in"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=software+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise total/cap
- Pages/requests fetched: 34
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 680
- After US/location filtering: 397
- With trustworthy posted_date: 397
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200641998-0836",
    "title": "AIML - Machine Learning Researcher, Foundation Models",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200641998/aiml-machine-learning-researcher-foundation-models",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T17:59:36.043067+00:00",
    "date_confidence": "high",
    "description": "We build frontier foundation models that power intelligent experiences at Apple. Our team works across the full training lifecycle: including pre-training foundation models, and de"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200641998-2459",
    "title": "AIML - Machine Learning Researcher, Foundation Models",
    "location": "New York City, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200641998/aiml-machine-learning-researcher-foundation-models",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T17:59:36.043067+00:00",
    "date_confidence": "high",
    "description": "We build frontier foundation models that power intelligent experiences at Apple. Our team works across the full training lifecycle: including pre-training foundation models, and de"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680978-3401",
    "title": "AIML - Staff ML Infrastructure Engineer, ML Platform & Technology - Pre-training Infrastructure",
    "location": "San Francisco Bay Area, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680978/aiml-staff-ml-infrastructure-engineer-ml-platform-technology-pre-training-infrastructure",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T17:59:36.043067+00:00",
    "date_confidence": "high",
    "description": "Apple is where individual imaginations gather together, committing to the values that lead to great work. Every new product we build, service we create, or Apple Store experience w"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680258-0836",
    "title": "AV Project Manager, SWE Employee Experience",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680258/av-project-manager-swe-employee-experience",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T17:59:36.043067+00:00",
    "date_confidence": "high",
    "description": "SWE Employee Experience and Event Operations brings people together, tells impactful stories, and delivers best-in-class experiences across Software Engineering (SWE). Our team pro"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200673911-3337",
    "title": "Service Reliability Engineer (SRE)",
    "location": "Seattle, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200673911/service-reliability-engineer-sre",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T17:59:36.043067+00:00",
    "date_confidence": "high",
    "description": "The Apple Services Engineering team (ASE) is one of the most exciting examples of Apple’s long-held passion for combining art and technology. These are the people who power the App"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: newest-first; minimum 2 pages, then two seen pages + one overlap page; otherwise count/cap
- Pages/requests fetched: 21
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 168 / 0
- Raw jobs found: 210
- After US/location filtering: 168
- With trustworthy posted_date: 168
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200052256",
    "title": "App Innovation Senior Cloud Solution Architect - CTJ - Top Secret",
    "location": "United States, District of Columbia, Washington D.C.; United States, Virginia, Reston; United States, Virginia, Arlington",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556982609",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:00:05.551109+00:00",
    "date_confidence": "high",
    "description": "Overview We are seeking a App Innovation Senior Cloud Solution Architect (GitHub Engineer) with deep expertise designing, implementing, and operating enterprise-scale GitHub platfo"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200049773",
    "title": "Senior Software Engineer (Windows ML MLIR Platform)",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556972729",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:00:05.551109+00:00",
    "date_confidence": "high",
    "description": "Overview Help define how AI runs on Windows at global scale. The Windows AI Platform & Tools Team is building the foundational software that turns rapidly advancing models and sili"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200052287",
    "title": "Principal Software Engineer - CoreAI (Foundry Observability)",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556982631",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:00:05.551109+00:00",
    "date_confidence": "high",
    "description": "Overview Core AI is at the forefront of Microsoft’s mission to redefine how software is built and experienced. We are responsible for building the foundational platforms, services,"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200047662",
    "title": "Principal UX Engineering Lead",
    "location": "United States, Washington, Redmond; United States, California, San Francisco; United States, Illinois, Chicago; United States, Georgia, Atlanta; United States, New York, New York; United States, California, Los Angeles; United States, North Carolina, Charlotte; United States, Texas, Dallas; United States, Texas, Austin; United States, North Carolina, Raleigh; United States, Massachusetts, Boston",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556958757",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:00:05.551109+00:00",
    "date_confidence": "high",
    "description": "Overview MCAPS-Core accelerates customer outcomes and business growth. By uniting product, engineering, marketing, sales, customer success, and partners around a common customer mi"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200052206",
    "title": "Critical Environment Field Service Engineer",
    "location": "United States, Virginia, Richmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556982498",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:00:05.551109+00:00",
    "date_confidence": "high",
    "description": "Overview In alignment with our Microsoft values, we are committed to cultivating an inclusive work environment for all employees to positively impact our culture every day and we n"
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 14
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 200 / 0
- Raw jobs found: 280
- After US/location filtering: 264
- With trustworthy posted_date: 264
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2020825",
    "title": "Software Engineer, OpenShell",
    "location": "US, Remote",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-Remote/Software-Engineer--OpenShell_JR2020825",
    "posted_date": "2026-07-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:01:42.277991+00:00",
    "date_confidence": "high",
    "description": "Are you ready to translate groundbreaking AI research into secure, production-grade systems? Want to shape the next generation of AI agent infrastructure? Join us! At NVIDIA OpenSh"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2023825",
    "title": "Director, Software Engineering",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Director--Software-Engineering_JR2023825",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:01:42.277991+00:00",
    "date_confidence": "high",
    "description": "In this role, you will own the enterprise platforms that enable the development, deployment, operation, and scaling of AI agents and GPU-accelerated workloads for NVIDIA employees."
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2024363",
    "title": "Principal Software Engineer",
    "location": "US, CA, Santa Clara; US, OR, Hillsboro; US, WA, Redmond",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Principal-Software-Engineer_JR2024363",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:01:42.277991+00:00",
    "date_confidence": "high",
    "description": "NVIDIA has been transforming computer graphics, PC gaming, and accelerated computing for more than 25 years. It’s a unique legacy of innovation that’s fueled by great technology—an"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2015068",
    "title": "Senior Software Engineer, Networking",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Linux-Kernel-Software-Engineer_JR2015068",
    "posted_date": "2026-08-07",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:01:42.277991+00:00",
    "date_confidence": "high",
    "description": "At NVIDIA, we are redefining the future of technology, and our Senior Software Engineer, Networking role offers a uniquely ambitious opportunity to contribute to world-class innova"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2018245",
    "title": "Senior Software Engineer, Security",
    "location": "US, CA, Santa Clara; US, CA, Remote",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Security-Architect_JR2018245",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:01:42.277991+00:00",
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
- Pages/requests fetched: 13
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 65 / 0
- Raw jobs found: 187
- After US/location filtering: 66
- With trustworthy posted_date: 66
- Errors/403s: ['detail JR353388: Salesforce workday detail HTTP 504']

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357997",
    "title": "Software Engineering AMTS, Office of the CEO",
    "location": "California - San Francisco; New York - New York",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Software-Engineering-AMTS--Office-of-the-CEO_JR357997-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:04:10.156747+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. About Futureforce University Rec"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR352645",
    "title": "Account Partner - Public Sector NGO/ Non-Profit",
    "location": "Virginia - Remote; Maryland - Remote; District of Columbia - Washington; Texas - Remote; California - Remote; Illinois - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Virginia---Remote/Account-Partner---Public-Sector-NGO--Non-Profit_JR352645",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:04:10.156747+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Customer Success Jo"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR342037",
    "title": "Senior Technical Support Engineer",
    "location": "Washington - Seattle",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Washington---Seattle/Sr-Technical-Support-Engineer_JR342037",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:04:10.156747+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Customer Success Jo"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR346498",
    "title": "Enterprise Tableau Account Director, State and Local Gov",
    "location": "Virginia - Mclean",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Virginia---Mclean/Tableau-Account-Director--SLG_JR346498",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:04:10.156747+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR355248",
    "title": "Senior Product Manager, Emerging Technology",
    "location": "New York - New York; Indiana - Indianapolis; California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/New-York---New-York/Senior-Product-Manager--Emerging-Technology_JR355248",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:04:10.156747+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Product Job Details"
  }
]
```

## Adobe

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://adobe.wd5.myworkdayjobs.com/external_experienced`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 14
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 175 / 0
- Raw jobs found: 280
- After US/location filtering: 175
- With trustworthy posted_date: 175
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R165261",
    "title": "Sr. Software Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Sr-Software-Engineer_R165261",
    "posted_date": "2026-03-16",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:05:32.313811+00:00",
    "date_confidence": "high",
    "description": "Our Team Join the Adobe Journey Optimizer B2B Insights and Analytics team and be at the forefront of transforming how businesses derive insights from customer data. We are pioneeri"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R169956",
    "title": "Lead Software Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Sr-Software-Engineer--UI_R169956",
    "posted_date": "2026-08-04",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:05:32.313811+00:00",
    "date_confidence": "high",
    "description": "About the Role We are seeking a highly motivated Lead Software Engineer to join the new Project Graph team at Adobe. Project Graph is a new creative system that lets you combine fi"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170402",
    "title": "Senior Software Engineer",
    "location": "Basel",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/Basel/Senior-Software-Engineer_R170402",
    "posted_date": "2026-07-10",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:05:32.313811+00:00",
    "date_confidence": "high",
    "description": "THE OPPORTUNITY Are you an AI-native software engineer ready to shape how enterprise brands appear in AI? The Adobe Brand Visibility team builds the systems that determine how ente"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170546",
    "title": "Senior Software Engineer",
    "location": "San Jose; San Francisco",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Senior-Software-Engineer_R170546-1",
    "posted_date": "2026-07-23",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:05:32.313811+00:00",
    "date_confidence": "high",
    "description": "The Opportunity Come join the Adobe Cloud Platform & Collaboration (ACPC) experiences engineering team, one of the most dynamic, fun, and agile teams at Adobe! You'll help build ou"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170582",
    "title": "Senior Software Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Senior-Software-Engineer_R170582",
    "posted_date": "2026-08-04",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:05:32.313811+00:00",
    "date_confidence": "high",
    "description": "The Adobe Risk Platform (ARP) is Adobe's centralized fraud prevention and risk-decisioning platform, protecting surfaces like Commerce, Stock, and Firefly with real-time decisions "
  }
]
```

## Meta

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · WAF/browser-only today. Keep official link; investigate browser XHR/HAR later.']

## TikTok

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · custom CSR/API. Keep official link; investigate XHR later.']

## Uber

- Status: ok
- Scraping method: HTTP GET Oracle HCM recruitingCEJobRequisitions on iaziqy.fa.ocs.oraclecloud.com (offset pagination) + recruitingCEJobRequisitionDetails
- Search URL/API: `https://jobs.uber.com/en/jobs/?search=software%20engineer&page=1&pagesize=10`
- Pagination: HCM finder offset=(page-1)*limit ; limit=20; stop on empty/repeat or TotalJobsCount (do not stop at pages 1–7)
- Pages/requests fetched: 8
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 10 / 105
- Raw jobs found: 160
- After US/location filtering: 115
- With trustworthy posted_date: 115
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "301389",
    "title": "Applications Developer II",
    "location": "New York City, NY, United States",
    "official_url": "https://jobs.uber.com/en/jobs/301389",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:07:22.711063+00:00",
    "date_confidence": "high",
    "description": "About the role and team Working at Uber means solving hard problems in a high-stakes, fast-moving environment. As an Application Developer, you will design, develop, and maintain t"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "157628",
    "title": "Enterprise Applications Developer",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/157628",
    "posted_date": "2026-06-19",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:07:22.711063+00:00",
    "date_confidence": "high",
    "description": "Uber Engineering is a high-performance culture marked by perseverance and hyperproductivity. We’re looking for team players with natural customer service intuition who can work har"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "300877",
    "title": "Sr Applications Developer",
    "location": "Dallas, TX, United States",
    "official_url": "https://jobs.uber.com/en/jobs/300877",
    "posted_date": "2026-08-18",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:07:22.711063+00:00",
    "date_confidence": "high",
    "description": "About the role and team Working at Uber means solving hard problems in a high-stakes, fast-moving environment. As a Senior Application Developer, you will be a technical leader and"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "154758",
    "title": "Applications Developer II - ServiceNow",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/154758",
    "posted_date": "2026-06-19",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:07:22.711063+00:00",
    "date_confidence": "high",
    "description": "About the Role The Application Developer, ServiceNow Platform is responsible for designing, developing, configuring, and supporting scalable ServiceNow solutions that meet complex "
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "300543",
    "title": "Senior Integrations Application Developer",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/300543",
    "posted_date": "2026-07-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:07:22.711063+00:00",
    "date_confidence": "high",
    "description": "About the role and team The FinTech team, part of the CFO’s organization, is responsible for innovating and building the best financial products and systems in the world. We are ob"
  }
]
```

## DoorDash

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/doordashusa/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 469
- After US/location filtering: 465
- With trustworthy posted_date: 465
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:07:33.437478+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:07:33.437478+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:07:33.437478+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:07:33.437478+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8077011",
    "title": "Account Manager, CPG",
    "location": "New York, NY; San Francisco, CA; Los Angeles, CA; Chicago, IL; Atlanta, GA; San Francisco",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8077011",
    "posted_date": "2026-07-22",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:07:33.437478+00:00",
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
- Pages/requests fetched: 10
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 76 / 0
- Raw jobs found: 149
- After US/location filtering: 76
- With trustworthy posted_date: 76
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "H226EM8",
    "title": "Manager, Software Engineering",
    "location": "Los Angeles, California; New York - 229 W 43rd St; Bellevue - 110 110th Ave NE; Seattle - 2025 1st Avenue; San Francisco - 1160 Battery St; Palo Alto - 395 Page Mill Rd",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Manager--Software-Engineering_H226EM8-1",
    "posted_date": "2026-07-09",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:07:37.845103+00:00",
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
    "posted_date": "2026-07-21",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:07:37.845103+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046369",
    "title": "Manager, Software Engineering, Maps",
    "location": "New York, New York; Seattle, Washington; San Francisco, California; Palo Alto, California; Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/New-York-New-York/Manager--Software-Engineering--Maps_R0046369-1",
    "posted_date": "2026-08-04",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:07:37.845103+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "Q326SWE",
    "title": "Software Engineer, Level 3",
    "location": "Los Angeles, California; New York - 229 W 43rd St; Seattle - 2025 1st Avenue; San Francisco - 1160 Battery St; Bellevue, Washington; Palo Alto - 395 Page Mill Rd",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Software-Engineer--Level-3_Q326SWE-1",
    "posted_date": "2026-08-18",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:07:37.845103+00:00",
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
    "fetched_at": "2026-08-31T18:07:37.845103+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 208
- After US/location filtering: 155
- With trustworthy posted_date: 155
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
    "updated_date": "2026-08-20",
    "fetched_at": "2026-08-31T18:08:39.378519+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8022863",
    "title": "Agency Lead",
    "location": "New York, NY, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8022863",
    "posted_date": "2026-08-03",
    "updated_date": "2026-08-20",
    "fetched_at": "2026-08-31T18:08:39.378519+00:00",
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
    "updated_date": "2026-08-20",
    "fetched_at": "2026-08-31T18:08:39.378519+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8081337",
    "title": "Client Account Manager II",
    "location": "São Paulo, BR",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8081337",
    "posted_date": "2026-07-30",
    "updated_date": "2026-08-20",
    "fetched_at": "2026-08-31T18:08:39.378519+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>About Pinterest:</strong></p> <p>Millions of people around the world come to our platform to find creative ideas, dream about new possibilitie"
  },
  {
    "company": "Pinterest",
    "source": "pinterest_official_careers",
    "job_id": "8055301",
    "title": "Client Account Manager II, Fashion & Apparel",
    "location": "New York, NY, US",
    "official_url": "https://www.pinterestcareers.com/jobs/?gh_jid=8055301",
    "posted_date": "2026-07-15",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-08-31T18:08:39.378519+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 386
- After US/location filtering: 299
- With trustworthy posted_date: 299
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Snowflake",
    "source": "snowflake_official_careers",
    "job_id": "02b4dbeb-2fef-4838-9d79-922330f08d58",
    "title": "Senior Data Scientist",
    "location": "US-CA-Menlo Park; Menlo Park, California, United States; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/snowflake/02b4dbeb-2fef-4838-9d79-922330f08d58",
    "posted_date": "2026-03-20",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:08:39.712949+00:00",
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
    "fetched_at": "2026-08-31T18:08:39.712949+00:00",
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
    "fetched_at": "2026-08-31T18:08:39.712949+00:00",
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
    "fetched_at": "2026-08-31T18:08:39.712949+00:00",
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
    "fetched_at": "2026-08-31T18:08:39.712949+00:00",
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
- Pages/requests fetched: 3
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 192 / 0
- Raw jobs found: 261
- After US/location filtering: 192
- With trustworthy posted_date: 192
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075020",
    "title": "Senior Manager - Software Engineering Management - AI Engineering",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146526999-senior-manager-software-engineering-management-ai-engineering",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:08:40.227211+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074763",
    "title": "Partner Technology Architect",
    "location": "Austin, Texas , United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146512627-partner-technology-architect-",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:08:40.227211+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074963",
    "title": "Principal Customer Success Executive - Manufacturing Vertical",
    "location": "Austin, TEXAS, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146496819-principal-customer-success-executive-manufacturing-vertical-",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:08:40.227211+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074458",
    "title": "Staff Reliability Engineer",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146495429-staff-reliability-engineer",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:08:40.227211+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074847",
    "title": "Director, Software Engineering Management",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146344019-director-software-engineering-management",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:08:40.227211+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  }
]
```

## LinkedIn

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · official company jobs page captured; scraper/API still unresolved.']

## Bloomberg

- Status: ok
- Scraping method: HTTP GET Avature SearchJobs HTML + JobDetail HTML
- Search URL/API: `https://bloomberg.avature.net/careers/SearchJobs?q=software+engineer&jobRecordsPerPage=12&jobOffset=0`
- Pagination: jobOffset=0,12,... ; stop on empty/repeat or short page
- Pages/requests fetched: 8
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 13 / 13
- Raw jobs found: 96
- After US/location filtering: 26
- With trustworthy posted_date: 0
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21640",
    "title": "White House Stringer - Part Time / Contract",
    "location": "Washington, District of Columbia, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/White-House-Stringer-Part-Time-Contract/21640",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:10:45.886733+00:00",
    "date_confidence": "unknown",
    "description": "White House Stringer - Part Time / Contract"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21249",
    "title": "TOP & Today Editor - Los Angeles",
    "location": "Los Angeles, California, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/TOP-Today-Editor-Los-Angeles/21249",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:10:45.886733+00:00",
    "date_confidence": "unknown",
    "description": "TOP & Today Editor - Los Angeles"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21651",
    "title": "Product Manager — Terminal Controls, Compliance & Policy",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Product-Manager-Terminal-Controls-Compliance-Policy/21651",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:10:45.886733+00:00",
    "date_confidence": "unknown",
    "description": "Product Manager — Terminal Controls, Compliance & Policy"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21667",
    "title": "Senior Data Management Professional - Data Engineering - Sustainable Fixed Income Data, Hong Kong",
    "location": "Hong Kong, Hong Kong",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Data-Management-Professional-Data-Engineering-Sustainable-Fixed-Income-Data-Hong-Kong/21667",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:10:45.886733+00:00",
    "date_confidence": "unknown",
    "description": "Senior Data Management Professional - Data Engineering - Sustainable Fixed Income Data, Hong Kong"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21660",
    "title": "Senior Financial Analyst, CFO Global Sustainability Office",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Financial-Analyst-CFO-Global-Sustainability-Office/21660",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:10:45.886733+00:00",
    "date_confidence": "unknown",
    "description": "Senior Financial Analyst, CFO Global Sustainability Office"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 17
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 34 / 150
- Raw jobs found: 340
- After US/location filtering: 184
- With trustworthy posted_date: 184
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210748454",
    "title": "FircoSoft Application Developer - Software Engineer III",
    "location": "Tampa, FL, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210748454",
    "posted_date": "2026-08-02",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:14.927583+00:00",
    "date_confidence": "high",
    "description": "We have an exciting and rewarding opportunity for you to take your software engineering career to the next level. As a FircoSoft Application Developer – Software Engineer III at JP"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210722255",
    "title": "Lead Software Engineer-Security/Application Development",
    "location": "Plano, TX, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210722255",
    "posted_date": "2026-07-10",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:14.927583+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer-Security/Application Development"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210760337",
    "title": "Lead Software Engineer - Full Stack Engineer",
    "location": "New York, NY, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210760337",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:14.927583+00:00",
    "date_confidence": "high",
    "description": "As a Lead Software Engineer at JPMorgan Chase in Connected Banking - Personal Financial Management, you’ll lead engineering innovation through the architecture, development, and ev"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210760528",
    "title": "Lead Software Engineer - Full Stack Engineer",
    "location": "New York, NY, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210760528",
    "posted_date": "2026-07-21",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:14.927583+00:00",
    "date_confidence": "high",
    "description": "As a Lead Software Engineer at JPMorgan Chase in Connected Banking - Personal Financial Management, you’ll lead engineering innovation through the architecture, development, and ev"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210724892",
    "title": "Lead Software Engineer - Java Full Stack Engineering",
    "location": "Chicago, IL, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210724892",
    "posted_date": "2026-08-14",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:14.927583+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorganChase within the Corp"
  }
]
```

## Capital One

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://capitalone.wd12.myworkdayjobs.com/Capital_One`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 11
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 132 / 0
- Raw jobs found: 220
- After US/location filtering: 133
- With trustworthy posted_date: 132
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R248687",
    "title": "Lead Software Engineer, Full Stack (Golang, Python, Java, AWS)",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Lead-Software-Engineer--Full-Stack--Golang--Python--Java--AWS-_R248687-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:42.811069+00:00",
    "date_confidence": "high",
    "description": "Lead Software Engineer, Full Stack (Golang, Python, Java, AWS) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R248352",
    "title": "Lead Software Engineer, Full Stack (Python, Java, PySpark/Spark, AWS)",
    "location": "Plano, TX",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Plano-TX/Lead-Software-Engineer--Full-Stack--Python--Java--PySpark-Spark--AWS-_R248352-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:42.811069+00:00",
    "date_confidence": "high",
    "description": "Lead Software Engineer, Full Stack (Python, Java, PySpark/Spark, AWS) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999400",
    "title": "Director, Customer Solutions Architecture- Capital One Software, Databolt (Remote)",
    "location": "Richmond, VA; US Remote",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Richmond-VA/Director--Customer-Solutions-Architecture--Capital-One-Software--Databolt--Remote-_R999400-2",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:42.811069+00:00",
    "date_confidence": "high",
    "description": "Director, Customer Solutions Architecture- Capital One Software, Databolt (Remote) Ever since our first credit card customer in 1994, Capital One has recognized that technology and"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R248340",
    "title": "Business Manager - US Card",
    "location": "McLean, VA; Richmond, VA; Chicago, IL; New York, NY",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Business-Manager---US-Card_R248340-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:42.811069+00:00",
    "date_confidence": "high",
    "description": "Business Manager - US Card Summary: As a Business Analysis Manager at Capital One, you will apply your strategic and analytical skills to major company challenges. You'll team with"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999432",
    "title": "Lead Software Engineer (Python, AWS)",
    "location": "San Francisco, CA; New York, NY",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/San-Francisco--CA/Lead-Software-Engineer--Python--AWS-_R999432-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:11:42.811069+00:00",
    "date_confidence": "high",
    "description": "Lead Software Engineer (Python, AWS) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inc"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 11
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 62 / 111
- Raw jobs found: 219
- After US/location filtering: 173
- With trustworthy posted_date: 173
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "342800",
    "title": "Principal Platform Software Engineer",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/342800",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:12:42.266759+00:00",
    "date_confidence": "high",
    "description": "Join the team building Oracle Cloud Infrastructure's state of the art observability platform, powering visibility and operational intelligence for both OCI's internal cloud service"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "342801",
    "title": "Lead Principal Platform Software Engineer",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/342801",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:12:42.266759+00:00",
    "date_confidence": "high",
    "description": "Join the team building Oracle Cloud Infrastructure's state of the art observability platform, powering visibility and operational intelligence for both OCI's internal cloud service"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "338844",
    "title": "Senior Software Development Engineer",
    "location": "United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/338844",
    "posted_date": "2026-07-13",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:12:42.266759+00:00",
    "date_confidence": "high",
    "description": "As a Senior Software Development Engineer in the Oracle Cloud Infrastructure (OCI) Security Platform division, you will help build and operate OCI’s Key Management Service (KMS), a"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "338704",
    "title": "Senior Software Developer",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/338704",
    "posted_date": "2026-07-01",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:12:42.266759+00:00",
    "date_confidence": "high",
    "description": "Oracle Cloud Infrastructure (OCI) delivers mission-critical applications for leading enterprises worldwide. Our cloud offers hyper-scale, multi-tenant services deployed across more"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "338705",
    "title": "Senior Software Developer",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/338705",
    "posted_date": "2026-07-01",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:12:42.266759+00:00",
    "date_confidence": "high",
    "description": "Oracle Cloud Infrastructure (OCI) delivers mission-critical applications for leading enterprises worldwide. Our cloud offers hyper-scale, multi-tenant services deployed across more"
  }
]
```

## Walmart Global Tech

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · custom Next.js/API. Search link works; XHR reverse-engineering in progress/deferred.']

## Cloudflare

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/cloudflare/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 307
- After US/location filtering: 301
- With trustworthy posted_date: 301
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:15.117647+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:15.117647+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:15.117647+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:15.117647+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:15.117647+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 568
- After US/location filtering: 370
- With trustworthy posted_date: 370
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "7532733",
    "title": "Account Executive, AI Sales",
    "location": "San Francisco, CA; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=7532733",
    "posted_date": "2026-02-03",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:16.287327+00:00",
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
    "updated_date": "2026-08-19",
    "fetched_at": "2026-08-31T18:13:16.287327+00:00",
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
    "updated_date": "2026-08-18",
    "fetched_at": "2026-08-31T18:13:16.287327+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>Who we are </strong></h2> <h3><strong>About Stripe</strong></h3> <p><span style=\"font-weight: 400;\">Stripe is a financial infrastructure platform for businesses. Millio"
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "8123027",
    "title": "Account Executive, Commercial (Grower)",
    "location": "Chicago; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=8123027",
    "posted_date": "2026-08-11",
    "updated_date": "2026-08-18",
    "fetched_at": "2026-08-31T18:13:16.287327+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>Who we are</strong></h2> <h3><strong>About Stripe</strong></h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s "
  },
  {
    "company": "Stripe",
    "source": "stripe_official_careers",
    "job_id": "7993151",
    "title": "Account Executive - Enterprise, Grower",
    "location": "US-Remote, US-San Francisco, US-Chicago, US-New York, US-Seattle, US-Texas; US",
    "official_url": "https://stripe.com/jobs/search?gh_jid=7993151",
    "posted_date": "2026-06-09",
    "updated_date": "2026-08-18",
    "fetched_at": "2026-08-31T18:13:16.287327+00:00",
    "date_confidence": "high",
    "description": "<h2><strong>Who we are</strong></h2> <h3><strong>About Stripe</strong></h3> <p>Stripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s "
  }
]
```

## Coinbase

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/coinbase/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 189
- After US/location filtering: 150
- With trustworthy posted_date: 150
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8053751",
    "title": "Accountant, Cyprus",
    "location": "Remote - Cyprus",
    "official_url": "https://www.coinbase.com/careers/positions/8053751?gh_jid=8053751",
    "posted_date": "2026-07-09",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-31T18:13:16.753127+00:00",
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
    "fetched_at": "2026-08-31T18:13:16.753127+00:00",
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
    "updated_date": "2026-08-24",
    "fetched_at": "2026-08-31T18:13:16.753127+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? At&nbsp;<a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sou"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "8164862",
    "title": "Accounting Manager, Tokenized Equities",
    "location": "Remote - Abu Dhabi; Abu Dhabi, United Arab Emirates",
    "official_url": "https://www.coinbase.com/careers/positions/8164862?gh_jid=8164862",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-31T18:13:16.753127+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Ready to do the most impactful work of your career? At&nbsp;<a href=\"https://www.coinbase.com/?utm_campaign=mt_o_m_w_m_m__coi_0_jd-onchain&amp;utm_sou"
  },
  {
    "company": "Coinbase",
    "source": "coinbase_official_careers",
    "job_id": "7942306",
    "title": "AMLCO & Senior Compliance Associate",
    "location": "Remote - Cyprus",
    "official_url": "https://www.coinbase.com/careers/positions/7942306?gh_jid=7942306",
    "posted_date": "2026-06-10",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-08-31T18:13:16.753127+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 128
- After US/location filtering: 120
- With trustworthy posted_date: 120
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8114351",
    "title": "Account Maintenance Associate",
    "location": "Clearwater, FL",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8114351?t=gh_src=&gh_jid=8114351",
    "posted_date": "2026-08-07",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:17.694738+00:00",
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
    "fetched_at": "2026-08-31T18:13:17.694738+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:17.694738+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:17.694738+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2>Join us in building the future of finance.</h2> <p>Our mission is to democratize finance for all. <a href=\"https://www.cerulli.com/press-releases/cer"
  },
  {
    "company": "Robinhood",
    "source": "robinhood_official_careers",
    "job_id": "8003458",
    "title": "Assistant General Counsel, Regulatory",
    "location": "Menlo Park, CA; New York, NY; Washington, DC; Menlo Park, CA; New York, NY; Washington, DC",
    "official_url": "https://boards.greenhouse.io/robinhood/jobs/8003458?t=gh_src=&gh_jid=8003458",
    "posted_date": "2026-06-18",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:13:17.694738+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 160
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
    "location": "San Francisco, CA • New York, NY • United States; US",
    "official_url": "https://boards.greenhouse.io/figma/jobs/5426468004?gh_jid=5426468004",
    "posted_date": "2025-01-28",
    "updated_date": "2026-07-22",
    "fetched_at": "2026-08-31T18:13:17.917335+00:00",
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
    "fetched_at": "2026-08-31T18:13:17.917335+00:00",
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
    "fetched_at": "2026-08-31T18:13:17.917335+00:00",
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
    "fetched_at": "2026-08-31T18:13:17.917335+00:00",
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
    "fetched_at": "2026-08-31T18:13:17.917335+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 220
- After US/location filtering: 123
- With trustworthy posted_date: 123
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.107178+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.107178+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.107178+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.107178+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.107178+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
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
    "job_id": "8599937002",
    "title": "Account Manager, Advertising Solutions",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8599937002",
    "posted_date": "2026-06-23",
    "updated_date": "2026-08-06",
    "fetched_at": "2026-08-31T18:13:18.407258+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8686353002",
    "title": "Advertising Operations Manager",
    "location": "San Francisco Bay Area or New York (Remote); New York, New York, United States; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8686353002",
    "posted_date": "2026-08-06",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-08-31T18:13:18.407258+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8625545002",
    "title": "Associate Product Counsel, Safety",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8625545002",
    "posted_date": "2026-07-13",
    "updated_date": "2026-07-31",
    "fetched_at": "2026-08-31T18:13:18.407258+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Discord has a highly engaged community of millions of daily active users who use the platform for many different reasons, but there’s one thing that n"
  },
  {
    "company": "Discord",
    "source": "discord_official_careers",
    "job_id": "8680047002",
    "title": "Commercial Policy Lead, Brand Safety & Malware",
    "location": "San Francisco Bay Area; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/discord/jobs/8680047002",
    "posted_date": "2026-08-05",
    "updated_date": "2026-08-05",
    "fetched_at": "2026-08-31T18:13:18.407258+00:00",
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
    "updated_date": "2026-07-31",
    "fetched_at": "2026-08-31T18:13:18.407258+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 120
- After US/location filtering: 93
- With trustworthy posted_date: 93
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.952959+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.952959+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.952959+00:00",
    "date_confidence": "high",
    "description": "<p id=\"p-rc_10838ec6a95bc2d4-72\" data-path-to-node=\"3\"><span data-path-to-node=\"3,0\">We are looking for a detail-oriented, strategic team player to join as a Benefits Manager on As"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8075658",
    "title": "Chief Accounting Officer",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://www.asana.com/jobs/apply/8075658?gh_jid=8075658",
    "posted_date": "2026-07-20",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.952959+00:00",
    "date_confidence": "high",
    "description": "<p>We’re looking for a strategic and collaborative leader to join Asana as our Chief Accounting Officer. In this pivotal role, you will guide our global financial operations, overs"
  },
  {
    "company": "Asana",
    "source": "asana_official_careers",
    "job_id": "8052235",
    "title": "Chief of Staff",
    "location": "San Francisco; San Francisco, California, United States",
    "official_url": "https://www.asana.com/jobs/apply/8052235?gh_jid=8052235",
    "posted_date": "2026-07-21",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:18.952959+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 294
- After US/location filtering: 288
- With trustworthy posted_date: 288
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
    "fetched_at": "2026-08-31T18:13:19.160226+00:00",
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
    "fetched_at": "2026-08-31T18:13:19.160226+00:00",
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
    "fetched_at": "2026-08-31T18:13:19.160226+00:00",
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
    "fetched_at": "2026-08-31T18:13:19.160226+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>Why join us</strong></p> <p>Brex is the intelligent finance platform that enables companies to spend smarter and move faster in more than 200 "
  },
  {
    "company": "Brex",
    "source": "brex_official_careers",
    "job_id": "8387049002",
    "title": "Account Manager",
    "location": "San Francisco, California, United States; New York, New York, United States; Vancouver, British Columbia, Canada",
    "official_url": "https://www.brex.com/careers/8387049002?gh_jid=8387049002",
    "posted_date": "2026-01-28",
    "updated_date": "2026-08-19",
    "fetched_at": "2026-08-31T18:13:19.160226+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 243
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
    "location": "Atlanta, Georgia, United States; Phoenix, Arizona, United States; Atlanta, Georgia, United States",
    "official_url": "https://www.samsara.com/company/careers/roles/8094367?gh_jid=8094367",
    "posted_date": "2026-08-12",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:19.437566+00:00",
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
    "updated_date": "2026-08-21",
    "fetched_at": "2026-08-31T18:13:19.437566+00:00",
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
    "updated_date": "2026-08-21",
    "fetched_at": "2026-08-31T18:13:19.437566+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "7612462",
    "title": "Account Executive, Commercial",
    "location": "Remote - US",
    "official_url": "https://www.samsara.com/company/careers/roles/7612462?gh_jid=7612462",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:13:19.437566+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: arial, helvetica, sans-serif;\"><strong>Who we are</strong></span></p> <p><span style=\"font-weight: 300; font-family: arial, "
  },
  {
    "company": "Samsara",
    "source": "samsara_official_careers",
    "job_id": "6605599",
    "title": "Account Executive, Commercial",
    "location": "Remote - US",
    "official_url": "https://www.samsara.com/company/careers/roles/6605599?gh_jid=6605599",
    "posted_date": "2025-02-19",
    "updated_date": "2026-08-20",
    "fetched_at": "2026-08-31T18:13:19.437566+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 171
- After US/location filtering: 102
- With trustworthy posted_date: 102
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8577546002",
    "title": "Account Manager, Strategic Healthcare Partnerships",
    "location": "New York, NY; New York, New York, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8577546002?gh_jid=8577546002",
    "posted_date": "2026-06-04",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:13:19.929075+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>L"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8576942002",
    "title": "Account Manager, Strategic Healthcare Partnerships",
    "location": "San Francisco, CA; New York, New York, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8576942002?gh_jid=8576942002",
    "posted_date": "2026-06-04",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:13:19.929075+00:00",
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:13:19.929075+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
  },
  {
    "company": "Lyft",
    "source": "lyft_official_careers",
    "job_id": "8737764002",
    "title": "Analytics Lead, Safety Reporting",
    "location": "San Francisco, CA; Florida, United States",
    "official_url": "https://app.careerpuck.com/job-board/lyft/job/8737764002?gh_jid=8737764002",
    "posted_date": "2026-08-21",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:13:19.929075+00:00",
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:13:19.929075+00:00",
    "date_confidence": "high",
    "description": "<p>At Lyft, our purpose is to serve and connect. We aim to achieve this by cultivating a work environment where all team members belong and have the opportunity to thrive.</p> <p>T"
  }
]
```

## Spotify

- Status: ok
- Scraping method: HTTP GET shared Lever postings API /v0/postings/{token}
- Search URL/API: `https://jobs.lever.co/spotify`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 33
- After US/location filtering: 33
- With trustworthy posted_date: 33
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "a0fa7da3-4c3c-4fa2-97bd-7d6eb01eb9e5",
    "title": "Android Engineer - Advertising",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/a0fa7da3-4c3c-4fa2-97bd-7d6eb01eb9e5",
    "posted_date": "2026-03-18",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "Our mission on the Advertising Product & Technology team is to build a next generation advertising platform that aligns with our unique value proposition for audio and video. We wo"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "1bbaf909-5ff3-4ed6-87ca-f7ff007a169c",
    "title": "Data Scientist - Music Mission",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/1bbaf909-5ff3-4ed6-87ca-f7ff007a169c",
    "posted_date": "2026-06-22",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "The Music Mission enables music creators to grow, engage, and monetize their fan bases on Spotify. Central to the Music Mission's vision is the development of promotional tools for"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "600a4ac7-6ffa-4ced-8d34-253d00147aa9",
    "title": "Director of ML Engineering, Conversation Product Area",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/600a4ac7-6ffa-4ced-8d34-253d00147aa9",
    "posted_date": "2026-08-06",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "The Personalization team makes deciding what to play next easier and more enjoyable for every listener. From Blend to Discover Weekly, we're behind some of Spotify's most-loved fea"
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "7aeec299-4653-4c5d-aafb-d537e1232208",
    "title": "Director, Portfolio & Monetization Architecture",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/7aeec299-4653-4c5d-aafb-d537e1232208",
    "posted_date": "2026-06-23",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "Spotify's growth depends on offering the right thing to the right listener at the right price, moving beyond one-size-fits-all packaging toward a portfolio where listeners can mix "
  },
  {
    "company": "Spotify",
    "source": "spotify_official_careers",
    "job_id": "f45de8ee-8f32-4e19-9163-eddf7a018337",
    "title": "Engineering Manager - Music",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/spotify/f45de8ee-8f32-4e19-9163-eddf7a018337",
    "posted_date": "2026-08-14",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "The Rights Systems team is driving the technical foundations of a step-change for Spotify’s business by enabling the distribution of new forms of content across the platform. This "
  }
]
```

## Ramp

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/ramp`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 137
- After US/location filtering: 121
- With trustworthy posted_date: 121
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
    "fetched_at": "2026-08-31T18:13:21.405852+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.405852+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.405852+00:00",
    "date_confidence": "high",
    "description": "ABOUT RAMP Ramp is building the smart infrastructure for finance teams, embedded in the transaction flow of every dollar a business spends. We automate how over $200B in annualized"
  },
  {
    "company": "Ramp",
    "source": "ramp_official_careers",
    "job_id": "1db75064-e38c-4b21-8310-21471943d0be",
    "title": "Technical Program Manager",
    "location": "New York, NY (HQ); New York City, NY, USA; Remote, USA",
    "official_url": "https://jobs.ashbyhq.com/ramp/1db75064-e38c-4b21-8310-21471943d0be",
    "posted_date": "2026-05-22",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:13:21.405852+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.405852+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 132
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
    "fetched_at": "2026-08-31T18:13:21.559480+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.559480+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.559480+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.559480+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.559480+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 28
- After US/location filtering: 26
- With trustworthy posted_date: 26
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
    "fetched_at": "2026-08-31T18:13:21.988363+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.988363+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.988363+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.988363+00:00",
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
    "fetched_at": "2026-08-31T18:13:21.988363+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 144
- After US/location filtering: 122
- With trustworthy posted_date: 122
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
    "fetched_at": "2026-08-31T18:13:22.047842+00:00",
    "date_confidence": "high",
    "description": "Who are we? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  },
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "0183bddd-f845-4e7e-af69-e6178cdc32be",
    "title": "Senior HR Business Partner",
    "location": "New York; New York, New York, United States; London; United States; Toronto; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/cohere/0183bddd-f845-4e7e-af69-e6178cdc32be",
    "posted_date": "2026-08-20",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:13:22.047842+00:00",
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
    "fetched_at": "2026-08-31T18:13:22.047842+00:00",
    "date_confidence": "high",
    "description": "Who are we? Cohere is the leading security-first enterprise AI company. We build cutting-edge foundation AI models and end-to-end products that are designed to solve real-world bus"
  },
  {
    "company": "Cohere",
    "source": "cohere_official_careers",
    "job_id": "acec6038-117b-400b-92e3-0745fbb4cf53",
    "title": "Data Annotation Specialist - German Writer/Translator",
    "location": "Canada; Calgary; Boston; Nashville; Richmond, VA; Phoenix; Seattle; United States; Vancouver; North America | Utah; Ottawa; Toronto; Montreal; Remote, Canada",
    "official_url": "https://jobs.ashbyhq.com/cohere/acec6038-117b-400b-92e3-0745fbb4cf53",
    "posted_date": "2026-02-20",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:13:22.047842+00:00",
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
    "fetched_at": "2026-08-31T18:13:22.047842+00:00",
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
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 91 / 0
- Raw jobs found: 250
- After US/location filtering: 91
- With trustworthy posted_date: 91
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2022599",
    "title": "Principal Software Engineer - Cisco IQ Validation (Hybrid)",
    "location": "RTP, North Carolina, US; San Jose, California, US; Richardson, Texas, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/RTP-North-Carolina-US/Principal-Engineer---Cisco-IQ-Validation_2022599",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:13:22.246953+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/29/2026 Meet the Team At Cisco, we are redefining the customer experience through the power of Cisco IQ Services and Applications"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2014522",
    "title": "Hardware Design Engineer Technical Lead",
    "location": "San Jose, California, US; San Francisco, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Hardware-Design-Engineer-Technical-Lead_2014522-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:13:22.246953+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/29/2026 Meet the Team The Common Hardware Group (CHG) creates innovative hardware platforms central to the AI era, powering Cisco"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2004763",
    "title": "Hardware Systems Engineering Technical Leader",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Hardware-Systems-Engineering-Technical-Lead---Milpitas-San-Jose--CA_2004763",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:13:22.246953+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/29/2026 This is an onsite position and requires the employee to work out the Milpitas, CA location. Meet the Team The Common Hard"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2021114",
    "title": "Software Engineer",
    "location": "Boulder, Colorado, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Boulder-Colorado-US/Software-Engineer_2021114-1",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:13:22.246953+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/18/2026 Meet the Team Splunk, a Cisco company, is building a safer, more resilient digital world with an end-to-end, full-stack p"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2022516",
    "title": "Technical Program Manager",
    "location": "Milpitas, California, US; San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Technical-Program-Manager_2022516",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:13:22.246953+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/10/2026 Meet the Team Cisco Cloud Security Group is a leading provider of Cloud Security and DNS services, enabling the world to "
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 14
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 28 / 103
- Raw jobs found: 350
- After US/location filtering: 131
- With trustworthy posted_date: 0
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1426322133",
    "title": "Principal Software Engineer - Identity & Access Management",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://jobs.sap.com/job/Palo-Alto-Principal-Software-Engineer-Identity-&-Access-Management-CA-94304/1426322133/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:14:18.570283+00:00",
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
    "fetched_at": "2026-08-31T18:14:18.570283+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1429414433",
    "title": "Principal Software Engineer - Platform Engineering",
    "location": "Palo Alto, CA, US, 94304",
    "official_url": "https://jobs.sap.com/job/Palo-Alto-Principal-Software-Engineer-Platform-Engineering-CA-94304/1429414433/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:14:18.570283+00:00",
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
    "fetched_at": "2026-08-31T18:14:18.570283+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1408906233",
    "title": "Expert DevOps Engineer",
    "location": "Reston, VA, US, 20191",
    "official_url": "https://jobs.sap.com/job/Reston-Expert-DevOps-Engineer-VA-20191/1408906233/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:14:18.570283+00:00",
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
- Pages/requests fetched: 11
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 99 / 0
- Raw jobs found: 220
- After US/location filtering: 100
- With trustworthy posted_date: 100
- Errors/403s: ['detail 1210651: HPE workday detail HTTP 504']

Sample normalized records:

```json
[
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1208691",
    "title": "Software Engineer",
    "location": "Westford, Massachusetts, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Westford-Massachusetts-United-States-of-America/Software-Engineer_1208691-2",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:14:50.468427+00:00",
    "date_confidence": "high",
    "description": "Software Engineer This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enterprise is the global"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1202357",
    "title": "Principal Software Engineer",
    "location": "Cupertino, California, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Cupertino-California-United-States-of-America/Principal-Software-Engineer_1202357-2",
    "posted_date": "2026-05-12",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:14:50.468427+00:00",
    "date_confidence": "high",
    "description": "Principal Software Engineer This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enterprise is "
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1203998",
    "title": "System Software Engineer",
    "location": "Sunnyvale, California, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Sunnyvale-California-United-States-of-America/System-Software-Engineer_1203998-2",
    "posted_date": "2026-06-10",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:14:50.468427+00:00",
    "date_confidence": "high",
    "description": "System Software Engineer This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enterprise is the"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1206283",
    "title": "Systems/Software Engineer",
    "location": "Roseville, California, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Roseville-California-United-States-of-America/Systems-Software-Engineer_1206283-1",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:14:50.468427+00:00",
    "date_confidence": "high",
    "description": "Systems/Software Engineer This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enterprise is th"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1207779",
    "title": "Systems/Software Engineer",
    "location": "Sunnyvale, California, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Sunnyvale-California-United-States-of-America/Systems-Software-Engineer_1207779-2",
    "posted_date": "2026-06-17",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:14:50.468427+00:00",
    "date_confidence": "high",
    "description": "Systems/Software Engineer This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enterprise is th"
  }
]
```

## Disney

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · verified official filtered search captured; adapter deferred.']

## eBay

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ebay.wd5.myworkdayjobs.com/apply`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 10
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 23 / 0
- Raw jobs found: 165
- After US/location filtering: 23
- With trustworthy posted_date: 23
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0076678",
    "title": "Software Engineer 2",
    "location": "San Jose",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/San-Jose/Software-Engineer-2_R0076678",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:16:47.239517+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0076679",
    "title": "Software Engineer 3",
    "location": "San Jose",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/San-Jose/Software-Engineer-3_R0076679",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:16:47.239517+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0076414",
    "title": "MTS1 Software Engineer, Android",
    "location": "Portland",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/Portland/MTS1-Software-Engineer--Android_R0076414",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:16:47.239517+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0075377",
    "title": "Sr. MTS Software Engineer - Identity",
    "location": "San Jose",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/San-Jose/Sr-MTS-Software-Engineer---Identity_R0075377",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:16:47.239517+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  },
  {
    "company": "eBay",
    "source": "ebay_official_careers",
    "job_id": "R0069694",
    "title": "Sr. MTS iOS Engineer, eBay Live",
    "location": "San Jose",
    "official_url": "https://ebay.wd5.myworkdayjobs.com/apply/job/San-Jose/Senior-Software-Engineer--iOS-_R0069694",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:16:47.239517+00:00",
    "date_confidence": "high",
    "description": "At eBay, we're more than a global ecommerce leader — we’re changing the way the world shops and sells. Our platform empowers millions of buyers and sellers in more than 190 markets"
  }
]
```

## Qualcomm

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · verified official search captured; adapter deferred.']

## AMD

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · verified official search captured; adapter deferred.']

## Zoom

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://zoom.wd5.myworkdayjobs.com/Zoom`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 7
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 45 / 0
- Raw jobs found: 103
- After US/location filtering: 45
- With trustworthy posted_date: 45
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19356",
    "title": "Video AI Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Video-AI-Engineer_R19356-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:22.365010+00:00",
    "date_confidence": "high",
    "description": "What you can expect As a Video AI Engineer, you'll enhance video codec standards to improve real-time video quality and performance in Zoom products. Work across our stack, develop"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19591",
    "title": "Audio Software Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Audio-Software-Engineer_R19591",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:22.365010+00:00",
    "date_confidence": "high",
    "description": "Immigration sponsorship is not available for this position What you can expect: We are seeking a highly skilled and motivated Audio Software Engineer to join our team. The successf"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19597",
    "title": "Software Developer Engineer",
    "location": "Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Seattle-WA/Software-Developer-Engineer_R19597",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:22.365010+00:00",
    "date_confidence": "high",
    "description": "Immigration sponsorship is not available for this position What you can expect We are seeking a talented engineer to join our AI Agent Experience team to help build the next-genera"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19467",
    "title": "Security DevOps Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Security-DevOps-Engineer_R19467-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:22.365010+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect As a DevOps Engineer on Zoom’s Security DevOps team, you will work on high-impact infrastructure initiatives that power some of Zoom’s most security-critical pr"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19581",
    "title": "Software Engineer",
    "location": "Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Seattle-WA/Software-Engineer_R19581",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:22.365010+00:00",
    "date_confidence": "high",
    "description": "Immigration sponsorship is not available for this position What you can expect: We’re building the next-generation AI-native knowledge platform to help organizations easily access "
  }
]
```

## Goldman Sachs

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · verified official search captured; adapter deferred.']

## Pure Storage

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/purestorage/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 322
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
    "fetched_at": "2026-08-31T18:17:53.655687+00:00",
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
    "fetched_at": "2026-08-31T18:17:53.655687+00:00",
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
    "fetched_at": "2026-08-31T18:17:53.655687+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8081943",
    "title": "Account Executive, Federal (Washington, DC)",
    "location": "Remote, Maryland; Remote, Virginia; Remote, Washington D.C.; Maryland, United States; Virginia, United States; Washington, D.C., United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8081943",
    "posted_date": "2026-07-23",
    "updated_date": "2026-07-23",
    "fetched_at": "2026-08-31T18:17:53.655687+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8119401",
    "title": "Account Executive, FSI, South Africa",
    "location": "Johannesburg, South Africa",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8119401",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:17:53.655687+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 853
- After US/location filtering: 500
- With trustworthy posted_date: 500
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
    "fetched_at": "2026-08-31T18:17:54.584035+00:00",
    "date_confidence": "high",
    "description": "<p class=\"p1\">As we continue to increase our presence in the world of Unified Data Analytics and AI, we're looking for a creative, driven, and execution-oriented Enterprise Account"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8604614002",
    "title": "Accounting Manager",
    "location": "San Francisco, California",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8604614002",
    "posted_date": "2026-07-01",
    "updated_date": "2026-08-18",
    "fetched_at": "2026-08-31T18:17:54.584035+00:00",
    "date_confidence": "high",
    "description": "<p data-pm-slice=\"1 1 []\">GAQ327R255</p> <p data-renderer-start-pos=\"1648\">While candidates in the listed location(s) are encouraged for this role, candidates in other locations wi"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8546367002",
    "title": "AI Engineer - FDE (Forward Deployed Engineer)",
    "location": "United States; Remote - California",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8546367002",
    "posted_date": "2026-05-13",
    "updated_date": "2026-08-18",
    "fetched_at": "2026-08-31T18:17:54.584035+00:00",
    "date_confidence": "high",
    "description": "<p><strong>AI Engineer - FDE (Forward Deployed Engineer) (ALL LEVELS)</strong></p> <p><strong>CSQ327R177</strong></p> <p><strong>Mission</strong></p> <p>The AI Forward Deployed Eng"
  },
  {
    "company": "Databricks",
    "source": "databricks_official_careers",
    "job_id": "8638847002",
    "title": "AI Engineer — GTM Analytics",
    "location": "United States; Remote - Illinois",
    "official_url": "https://databricks.com/company/careers/open-positions/job?gh_jid=8638847002",
    "posted_date": "2026-07-30",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:17:54.584035+00:00",
    "date_confidence": "high",
    "description": "<p data-pm-slice=\"1 1 []\"><span style=\"font-family: helvetica, arial, sans-serif;\">SLSQ327R637</span></p> <p><span style=\"font-family: helvetica, arial, sans-serif;\">At Databricks,"
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
    "fetched_at": "2026-08-31T18:17:54.584035+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 231
- After US/location filtering: 208
- With trustworthy posted_date: 208
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
    "fetched_at": "2026-08-31T18:17:55.491016+00:00",
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
    "fetched_at": "2026-08-31T18:17:55.491016+00:00",
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
    "fetched_at": "2026-08-31T18:17:55.491016+00:00",
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
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:17:55.491016+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  },
  {
    "company": "Roblox",
    "source": "roblox_official_careers",
    "job_id": "8054257",
    "title": "3D Animator (Short Term)",
    "location": "San Mateo, CA, United States",
    "official_url": "https://careers.roblox.com/jobs/8054257?gh_jid=8054257",
    "posted_date": "2026-07-10",
    "updated_date": "2026-08-17",
    "fetched_at": "2026-08-31T18:17:55.491016+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 169
- After US/location filtering: 100
- With trustworthy posted_date: 100
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "7834481",
    "title": "Business Operations and Growth Lead",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/7834481?gh_jid=7834481",
    "posted_date": "2026-04-21",
    "updated_date": "2026-07-23",
    "fetched_at": "2026-08-31T18:17:55.730025+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8144691",
    "title": "Community & Culture Program Manager",
    "location": "United States",
    "official_url": "https://careers.airbnb.com/positions/8144691?gh_jid=8144691",
    "posted_date": "2026-08-20",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-08-31T18:17:55.730025+00:00",
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
    "updated_date": "2026-04-24",
    "fetched_at": "2026-08-31T18:17:55.730025+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">Airbnb was born in 2007 when two hosts welcomed three guests to their San Fr"
  },
  {
    "company": "Airbnb",
    "source": "airbnb_official_careers",
    "job_id": "8104102",
    "title": "Compensation Partner",
    "location": "San Francisco, United States; San Francisco, CA",
    "official_url": "https://careers.airbnb.com/positions/8104102?gh_jid=8104102",
    "posted_date": "2026-08-03",
    "updated_date": "2026-08-03",
    "fetched_at": "2026-08-31T18:17:55.730025+00:00",
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
    "fetched_at": "2026-08-31T18:17:55.730025+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 570
- After US/location filtering: 454
- With trustworthy posted_date: 454
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
    "fetched_at": "2026-08-31T18:17:55.940696+00:00",
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
    "fetched_at": "2026-08-31T18:17:55.940696+00:00",
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
    "fetched_at": "2026-08-31T18:17:55.940696+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5390966008",
    "title": "AI Engineer, GTM Claudification",
    "location": "Remote-Friendly (Travel-Required) | San Francisco, CA | Seattle, WA; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5390966008",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:17:55.940696+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  },
  {
    "company": "Anthropic",
    "source": "anthropic_official_careers",
    "job_id": "5383242008",
    "title": "AI Fluency Education Lead",
    "location": "San Francisco, CA | New York City, NY; San Francisco, California, United States",
    "official_url": "https://job-boards.greenhouse.io/anthropic/jobs/5383242008",
    "posted_date": "2026-08-07",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-08-31T18:17:55.940696+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 34
- After US/location filtering: 24
- With trustworthy posted_date: 24
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4705312006",
    "title": "Account Executive",
    "location": "Toronto; Remote - United States",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4705312006?gh_jid=4705312006",
    "posted_date": "2026-08-14",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:17:56.694574+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4703378006",
    "title": "Account Executive",
    "location": "New York City, NY; Remote - United States",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4703378006?gh_jid=4703378006",
    "posted_date": "2026-08-07",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:17:56.694574+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  },
  {
    "company": "AppLovin",
    "source": "applovin_official_careers",
    "job_id": "4700129006",
    "title": "Agency Growth Lead",
    "location": "Los Angeles/Santa Monica, CA; Remote - United States",
    "official_url": "https://boards.greenhouse.io/applovin/jobs/4700129006?gh_jid=4700129006",
    "posted_date": "2026-07-28",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:17:56.694574+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:17:56.694574+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:17:56.694574+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><span style=\"font-weight: 400;\"><strong>About AppLovin</strong></span></h3> <p><a href=\"https://cts.businesswire.com/ct/CT?id=smartlink&amp;url=http%"
  }
]
```

## ByteDance

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · High-value; likely shares patterns with TikTok but treat search surface separately until verified.']

## Chime

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/chime/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 64
- After US/location filtering: 64
- With trustworthy posted_date: 64
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8609153002",
    "title": "Analyst, Investor Relations",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8609153002?gh_jid=8609153002",
    "posted_date": "2026-07-22",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-31T18:17:56.814310+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\"><strong>About the Role</strong></span></h2> <p><span style=\"font-family: helvetica, arial, sans-serif;\">Chime is lookin"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8684363002",
    "title": "Associate Creative Director, Growth Marketing",
    "location": "San Francisco, CA, USA; San Francisco, California, United States",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8684363002?gh_jid=8684363002",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:17:56.814310+00:00",
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
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-31T18:17:56.814310+00:00",
    "date_confidence": "high",
    "description": "<h2>About the Role</h2> <p>We are hiring a Chief of Staff / Head of Legal Operations to join our growing Legal team. This role sits at the intersection of executive strategy and le"
  },
  {
    "company": "Chime",
    "source": "chime_official_careers",
    "job_id": "8564916002",
    "title": "CX Partner Manager",
    "location": "Remote, USA; Remote - US",
    "official_url": "https://boards.greenhouse.io/chime/jobs/8564916002?gh_jid=8564916002",
    "posted_date": "2026-05-29",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-31T18:17:56.814310+00:00",
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
    "updated_date": "2026-06-29",
    "fetched_at": "2026-08-31T18:17:56.814310+00:00",
    "date_confidence": "high",
    "description": "<h2><span style=\"font-family: helvetica, arial, sans-serif;\"><strong>About the role</strong></span></h2> <p class=\"p2\">We're looking for a Growth Product Scientist to partner with "
  }
]
```

## Citadel

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · High-value SWE/quant; inspect search feed. Some roles may have restrictions but not blanket US-person-only.']

## Dell

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Large SWE employer; inspect ATS before custom work.']

## Dropbox

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/dropbox/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 42
- After US/location filtering: 34
- With trustworthy posted_date: 34
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8107794",
    "title": "Account Executive",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8107794?gh_jid=8107794",
    "posted_date": "2026-08-07",
    "updated_date": "2026-08-07",
    "fetched_at": "2026-08-31T18:17:57.225275+00:00",
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
    "updated_date": "2026-08-05",
    "fetched_at": "2026-08-31T18:17:57.225275+00:00",
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
    "updated_date": "2026-08-05",
    "fetched_at": "2026-08-31T18:17:57.225275+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-1gg9uz65z1iz85zgdz68zmqkz84zo2qowz80zsz81z8nqz122zdfz68z5coz87zsz73zz76zipqu3z86zmz88zz81zcth"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8126572",
    "title": "Data Analytics Partner, People Analytics",
    "location": "Remote - US: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8126572?gh_jid=8126572",
    "posted_date": "2026-08-18",
    "updated_date": "2026-08-18",
    "fetched_at": "2026-08-31T18:17:57.225275+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9yz88zz69zpz75zz65zpcz87zkdtuz90zz88zz87z4ez"
  },
  {
    "company": "Dropbox",
    "source": "dropbox_official_careers",
    "job_id": "8126575",
    "title": "Data Analytics Partner, People Analytics",
    "location": "Remote - Canada: Select locations; Canada; US",
    "official_url": "https://jobs.dropbox.com/listing/8126575?gh_jid=8126575",
    "posted_date": "2026-08-18",
    "updated_date": "2026-08-18",
    "fetched_at": "2026-08-31T18:17:57.225275+00:00",
    "date_confidence": "high",
    "description": "<h2 class=\"p1\"><span class=\"s1\">Role Description</span></h2> <p><span class=\" author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9yz88zz69zpz75zz65zpcz87zkdtuz90zz88zz87z4ez"
  }
]
```

## Expedia Group

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Large software hiring volume; inspect search API.']

## HubSpot

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong SWE/product employer; inspect ATS/feed.']

## Instacart

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/instacart/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 118
- After US/location filtering: 102
- With trustworthy posted_date: 102
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
    "fetched_at": "2026-08-31T18:17:57.388090+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  },
  {
    "company": "Instacart",
    "source": "instacart_official_careers",
    "job_id": "7495338",
    "title": "Ads AI Analytics Lead II",
    "location": "United States - Remote; Remote - Canada",
    "official_url": "https://instacart.careers/job/?gh_jid=7495338",
    "posted_date": "2025-12-23",
    "updated_date": "2026-08-24",
    "fetched_at": "2026-08-31T18:17:57.388090+00:00",
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
    "fetched_at": "2026-08-31T18:17:57.388090+00:00",
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
    "fetched_at": "2026-08-31T18:17:57.388090+00:00",
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
    "fetched_at": "2026-08-31T18:17:57.388090+00:00",
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
- Pages/requests fetched: 11
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 103 / 0
- Raw jobs found: 220
- After US/location filtering: 103
- With trustworthy posted_date: 103
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0282641",
    "title": "AI Software Engineering Intern",
    "location": "US, Arizona, Phoenix",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Arizona-Phoenix/AI-Software-Engineering-Intern_JR0282641",
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:57.578267+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Contributes to the design, development, and optimization of AI software solutions including algorithms, frameworks, and AI software architectures acro"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0285371",
    "title": "Software Engineering Leader",
    "location": "US, Oregon, Hillsboro; US, California, Folsom; US, California, Santa Clara; US, Texas, Austin; US, Arizona, Phoenix",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/Software-Engineering-Leader_JR0285371-1",
    "posted_date": "2026-07-23",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:57.578267+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: We are seeking an innovative and experienced engineering leader to join our developer software team. In this pivotal role, you will be responsible for"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0285035",
    "title": "System Software Engineer",
    "location": "US, Arizona, Phoenix",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Arizona-Phoenix/System-Software-Engineer_JR0285035-1",
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:57.578267+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Join Intel as a System Software Engineer, where you will play a pivotal role in designing, developing, and optimizing software solutions across Intel'"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0285033",
    "title": "System Software Engineer",
    "location": "US, Arizona, Phoenix",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Arizona-Phoenix/System-Software-Engineer_JR0285033",
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:57.578267+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Join Intel as a System Software Engineer, where you will play a pivotal role in designing, developing, and optimizing software solutions across Intel'"
  },
  {
    "company": "Intel",
    "source": "intel_official_careers",
    "job_id": "JR0285048",
    "title": "System Software Engineer",
    "location": "US, Oregon, Hillsboro",
    "official_url": "https://intel.wd1.myworkdayjobs.com/External/job/US-Oregon-Hillsboro/System-Software-Engineer_JR0285048",
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:17:57.578267+00:00",
    "date_confidence": "high",
    "description": "Job Details: Job Description: Join Intel as a System Software Engineer, where you will play a pivotal role in designing, developing, and optimizing software solutions across Intel'"
  }
]
```

## MathWorks

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong technical hiring; official searchable page.']

## MongoDB

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/mongodb/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 412
- After US/location filtering: 265
- With trustworthy posted_date: 265
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:19:47.109231+00:00",
    "date_confidence": "high",
    "description": "<p>An Account Development Representative at MongoDB is the starting point for building a serious career in technology sales.&nbsp;</p> <p>This role is the foundation of our sales o"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7318466",
    "title": "Account Development Representative",
    "location": "Bengaluru; Bengaluru, Karnataka, India",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7318466",
    "posted_date": "2026-07-22",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:19:47.109231+00:00",
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
    "updated_date": "2026-08-21",
    "fetched_at": "2026-08-31T18:19:47.109231+00:00",
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:19:47.109231+00:00",
    "date_confidence": "high",
    "description": "<p>At MongoDB, our Account Development team works closely with our partners in both Sales and Marketing to build fanatical customer enthusiasm around MongoDB. ADR reps are responsi"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7566671",
    "title": "Account Development Representative - Mandarin Speaking",
    "location": "Kuala Lumpur; MYS_KualaLumpur",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7566671",
    "posted_date": "2026-04-02",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-31T18:19:47.109231+00:00",
    "date_confidence": "high",
    "description": "<p>An Account Development Representative at MongoDB is the starting point for building a serious career in technology sales.&nbsp;</p> <p>This role is the foundation of our sales o"
  }
]
```

## Morgan Stanley

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Large technology org; filter aggressively to SWE/AI.']

## NetApp

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong systems/software employer; inspect ATS.']

## Netflix

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · High-value; inspect jobs search API/feed.']

## OpenAI

- Status: ok
- Scraping method: HTTP GET Ashby posting-api/job-board/{token}
- Search URL/API: `https://api.ashbyhq.com/posting-api/job-board/openai`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 755
- After US/location filtering: 642
- With trustworthy posted_date: 642
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
    "fetched_at": "2026-08-31T18:19:47.772254+00:00",
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
    "fetched_at": "2026-08-31T18:19:47.772254+00:00",
    "date_confidence": "high",
    "description": "By applying to this role, you will be considered for Research Engineer roles across all teams at OpenAI. About the Role As a Research Engineer here, you will be responsible for bui"
  },
  {
    "company": "OpenAI",
    "source": "openai_official_careers",
    "job_id": "13995549-e8cc-498f-9eaa-1869067ac35b",
    "title": "Software Engineer, RL Training Infra",
    "location": "San Francisco; San Francisco, California, United States; Remote, United States",
    "official_url": "https://jobs.ashbyhq.com/openai/13995549-e8cc-498f-9eaa-1869067ac35b",
    "posted_date": "2026-05-23",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:19:47.772254+00:00",
    "date_confidence": "high",
    "description": "ABOUT THE TEAM The Post-Training Frontiers team is responsible for training the frontier agents OpenAI ships to the world (GPT-Next). We train the flagship agentic models behind Co"
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
    "fetched_at": "2026-08-31T18:19:47.772254+00:00",
    "date_confidence": "high",
    "description": "About the Team We bring OpenAI's technology to the world through products like ChatGPT and the OpenAI API. We seek to learn from deployment and distribute the benefits of AI, while"
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
    "fetched_at": "2026-08-31T18:19:47.772254+00:00",
    "date_confidence": "high",
    "description": "ABOUT THE TEAM The Safety Systems team https://openai.com/safety/safety-systems is responsible for various safety work to ensure our best models can be safely deployed to the real "
  }
]
```

## Palantir

- Status: ok
- Scraping method: HTTP GET shared Lever postings API /v0/postings/{token}
- Search URL/API: `https://jobs.lever.co/palantir`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 162
- After US/location filtering: 162
- With trustworthy posted_date: 162
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "a5f93bb6-4f13-4451-80a4-f63090830269",
    "title": "Administrative Business Partner - ShipOS",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/palantir/a5f93bb6-4f13-4451-80a4-f63090830269",
    "posted_date": "2026-06-18",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "A World-Changing Company Palantir builds the world’s leading software for data-driven decisions and operations. By bringing the right data to the people who need it, our platforms "
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
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "A World-Changing Company Palantir builds the world’s leading software for data-driven decisions and operations. By bringing the right data to the people who need it, our platforms "
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
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "A World-Changing Company Palantir builds the world’s leading software for data-driven decisions and operations. By bringing the right data to the people who need it, our platforms "
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
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "A World-Changing Company Palantir builds the world’s leading software for data-driven decisions and operations. By bringing the right data to the people who need it, our platforms "
  },
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "6fe5515f-f677-4d98-8ac2-1775a425f5e7",
    "title": "Backend Software Engineer - Infrastructure",
    "location": "New York, NY",
    "official_url": "https://jobs.lever.co/palantir/6fe5515f-f677-4d98-8ac2-1775a425f5e7",
    "posted_date": "2025-08-06",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "A World-Changing Company Palantir builds the world’s leading software for data-driven decisions and operations. By bringing the right data to the people who need it, our platforms "
  }
]
```

## PayPal

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Large fintech SWE employer; inspect ATS/search endpoint.']

## Reddit

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/reddit/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 155
- After US/location filtering: 137
- With trustworthy posted_date: 137
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "7617155",
    "title": "3rd Party Partnerships Manager - Commerce",
    "location": "New York City, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/7617155",
    "posted_date": "2026-02-27",
    "updated_date": "2026-08-06",
    "fetched_at": "2026-08-31T18:19:55.227532+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8089959",
    "title": "3rd Party Partnerships Manager - Signals",
    "location": "New York City, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8089959",
    "posted_date": "2026-07-29",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:19:55.227532+00:00",
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
    "fetched_at": "2026-08-31T18:19:55.227532+00:00",
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
    "fetched_at": "2026-08-31T18:19:55.227532+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  },
  {
    "company": "Reddit",
    "source": "reddit_official_careers",
    "job_id": "8114666",
    "title": "Client Partner, Mid-Market Sales (Services - Acquisitions)",
    "location": "New York City, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/reddit/jobs/8114666",
    "posted_date": "2026-08-10",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:19:55.227532+00:00",
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
- Pages/requests fetched: 8
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 29 / 0
- Raw jobs found: 145
- After US/location filtering: 29
- With trustworthy posted_date: 29
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-058865",
    "title": "Associate Consultant - OpenShift",
    "location": "Mumbai",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Mumbai/Associate-Consultant---OpenShift_R-058865-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:19:55.742758+00:00",
    "date_confidence": "high",
    "description": "About the Job: The Associate Consultant exercises judgment when following general instructions and is responsible for working independently to support complex consulting engagement"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-058970",
    "title": "Consultant - Openshift",
    "location": "New Delhi",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/New-Delhi/Consultant---Openshift_R-058970-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:19:55.742758+00:00",
    "date_confidence": "high",
    "description": "About The Job: The Consultant exercises good judgment and is responsible for working independently with minimal instruction whilst making sound decisions to resolve moderately comp"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-055739",
    "title": "Principal Software Engineer - OpenShift Virtualization Windows Guests",
    "location": "Raanana",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Raanana/Principal-Software-Engineer---OpenShift-Virtualization-Windows-Guests_R-055739-1",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:19:55.742758+00:00",
    "date_confidence": "high",
    "description": "Job Summary: The Red Hat Virtualization team is seeking a Principal Software Engineer to help define and build the next generation of solutions for running Microsoft Windows as a g"
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-058514",
    "title": "Sr. Platform Partner Technical Account Manager (PTAM)",
    "location": "Remote US NC; Remote US MA",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Remote-US-NC/Sr-Platform-Partner-Technical-Account-Manager--PTAM-_R-058514-1",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:19:55.742758+00:00",
    "date_confidence": "high",
    "description": "About the role: In this role, you will collaborate with a dedicated team of Red Hatters supporting our partners. You will provide hands-on technical and architectural guidance for "
  },
  {
    "company": "Red Hat",
    "source": "red_hat_official_careers",
    "job_id": "R-059006",
    "title": "Senior Software Engineer",
    "location": "Raleigh",
    "official_url": "https://redhat.wd5.myworkdayjobs.com/jobs/job/Raleigh/Senior-Software-Engineer_R-059006",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:19:55.742758+00:00",
    "date_confidence": "high",
    "description": "*Telecommuting permitted: work may be performed within normal commuting distance from the Red Hat, LLC office in Raleigh, NC. Own the implementation of security remediation and com"
  }
]
```

## Roku

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/roku/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 250
- After US/location filtering: 233
- With trustworthy posted_date: 233
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8051546",
    "title": "Account Executive",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8051546?gh_jid=8051546",
    "posted_date": "2026-07-08",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:20:43.479435+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "7874146",
    "title": "Account Executive, Ads Manager",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/7874146?gh_jid=7874146",
    "posted_date": "2026-05-01",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:20:43.479435+00:00",
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
    "fetched_at": "2026-08-31T18:20:43.479435+00:00",
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
    "fetched_at": "2026-08-31T18:20:43.479435+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2 style=\"font-family: GothamBold,Helvetica,Arial,sans-serif; color: #662d91;\">Teamwork makes the stream work.</h2> <p>&nbsp;</p> <h3 style=\"font-family"
  },
  {
    "company": "Roku",
    "source": "roku_official_careers",
    "job_id": "8119497",
    "title": "Ad Measurement Manager",
    "location": "New York, New York; New York, New York, U.S.",
    "official_url": "https://www.weareroku.com/jobs/8119497?gh_jid=8119497",
    "posted_date": "2026-08-10",
    "updated_date": "2026-08-31",
    "fetched_at": "2026-08-31T18:20:43.479435+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 192
- After US/location filtering: 181
- With trustworthy posted_date: 181
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
    "fetched_at": "2026-08-31T18:20:44.194521+00:00",
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
    "fetched_at": "2026-08-31T18:20:44.194521+00:00",
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
    "fetched_at": "2026-08-31T18:20:44.194521+00:00",
    "date_confidence": "high",
    "description": "<p>Since we opened our doors in 2009, the world of commerce has evolved immensely, and so has Square. After enabling anyone to take payments and never miss a sale, we saw sellers s"
  },
  {
    "company": "Block / Square",
    "source": "block_/_square_official_careers",
    "job_id": "5367290008",
    "title": "AI Legal Program Manager",
    "location": "Bay Area, CA, United States of America; US - CA - San Francisco City - Remote",
    "official_url": "http://block.xyz/careers/jobs/5367290008?gh_jid=5367290008",
    "posted_date": "2026-07-28",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:20:44.194521+00:00",
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
    "fetched_at": "2026-08-31T18:20:44.194521+00:00",
    "date_confidence": "high",
    "description": "<p><strong>Team:</strong> Apollo — Block Applied R&amp;D<br><strong>Location:</strong> Remote (US / Canada)<br><strong>Duration:</strong> Fall/Winter 2026 co-op — 8 months, flexibl"
  }
]
```

## Tesla

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Large software/AI hiring; filter out export-controlled/restricted roles individually.']

## Two Sigma

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · High-value SWE/quant; identify direct openings/search endpoint.']

## Verkada

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/verkada/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 282
- After US/location filtering: 228
- With trustworthy posted_date: 228
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
    "updated_date": "2026-08-19",
    "fetched_at": "2026-08-31T18:20:44.509456+00:00",
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
    "updated_date": "2026-08-19",
    "fetched_at": "2026-08-31T18:20:44.509456+00:00",
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
    "updated_date": "2026-08-24",
    "fetched_at": "2026-08-31T18:20:44.509456+00:00",
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
    "updated_date": "2026-08-24",
    "fetched_at": "2026-08-31T18:20:44.509456+00:00",
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
    "updated_date": "2026-08-19",
    "fetched_at": "2026-08-31T18:20:44.509456+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h3><strong>Who We Are</strong></h3> <p>Verkada is transforming how organizations protect their people and places with an integrated, privacy-sensitive A"
  }
]
```

## Visa

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Large technology org; identify direct search backend.']

## WeRide

- Status: ok
- Scraping method: HTTP GET shared Lever postings API /v0/postings/{token}
- Search URL/API: `https://jobs.lever.co/weride`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 13
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
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "Established in 2017, WeRide (NASDAQ: WRD) is a leading global commercial-stage company that develops autonomous driving technologies from Level 2 to Level 4 and is the world's firs"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "67194770-ca27-4291-82ac-a90e58967e29",
    "title": "Contract Vehicle Operations Specialist (Bilingual Spanish)",
    "location": "San Jose, CA",
    "official_url": "https://jobs.lever.co/weride/67194770-ca27-4291-82ac-a90e58967e29",
    "posted_date": "2026-07-06",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "WeRide is a smart mobility start-up whose mission is to transform mobility with autonomous driving. We are committed to build better transportation experience that’s safe, efficien"
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
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "Established in 2017, WeRide (NASDAQ: WRD) is a leading global commercial-stage company that develops autonomous driving technologies from Level 2 to Level 4 and is the world's firs"
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
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "Established in 2017, WeRide (NASDAQ: WRD) is a leading global commercial-stage company that develops autonomous driving technologies from Level 2 to Level 4 and is the world's firs"
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
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "Established in 2017, WeRide (NASDAQ: WRD) is a leading global commercial-stage company that develops autonomous driving technologies from Level 2 to Level 4 and is the world's firs"
  }
]
```

## Workday

- Status: error
- Scraping method: workday
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['JSONDecodeError: Expecting value: line 1 column 1 (char 0)']

## Zillow

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong product/software hiring; locate direct search feed.']

## Zscaler

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/zscaler/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 338
- After US/location filtering: 229
- With trustworthy posted_date: 229
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
    "fetched_at": "2026-08-31T18:21:02.182487+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>About <strong>Zscaler</strong></p> <p>Zscaler accelerates digital transformation to ensure our customers can be more agile, efficient, resilient, and "
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
    "fetched_at": "2026-08-31T18:21:02.182487+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>About <strong>Zscaler</strong></p> <p>Zscaler accelerates digital transformation to ensure our customers can be more agile, efficient, resilient, and "
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5159494007",
    "title": "Account Executive, Commercial (West)",
    "location": "Remote - Ôsaka, Japan; Osaka, JPN",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5159494007",
    "posted_date": "2026-07-13",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:21:02.182487+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>About <strong>Zscaler</strong></p> <p>Zscaler accelerates digital transformation to ensure our customers can be more agile, efficient, resilient, and "
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5179814007",
    "title": "Account Executive, Commercial (West)",
    "location": "Remote - Ôsaka, Japan; Osaka, JPN",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5179814007",
    "posted_date": "2026-07-13",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:21:02.182487+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>About <strong>Zscaler</strong></p> <p>Zscaler accelerates digital transformation to ensure our customers can be more agile, efficient, resilient, and "
  },
  {
    "company": "Zscaler",
    "source": "zscaler_official_careers",
    "job_id": "5199289007",
    "title": "Account Executive, Data Security",
    "location": "City of London Corporation, GBR; Remote - UK",
    "official_url": "https://job-boards.greenhouse.io/zscaler/jobs/5199289007",
    "posted_date": "2026-08-07",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-31T18:21:02.182487+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>About <strong>Zscaler</strong></p> <p>Zscaler accelerates digital transformation to ensure our customers can be more agile, efficient, resilient, and "
  }
]
```

## Chewy

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://wd5.myworkdaysite.com/recruiting/chewy/External`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 5
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 30 / 0
- Raw jobs found: 46
- After US/location filtering: 30
- With trustworthy posted_date: 30
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R29873",
    "title": "Software Engineer II",
    "location": "Minneapolis, MN; Boston, MA",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/Minneapolis-MN/Software-Engineer-II_R29873",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:02.606817+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Team: The Cart & Checkout Engineering team is responsible for building and operating the services that orchestrate the end-to-end checkout experience across mu"
  },
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R29953",
    "title": "Software Engineer III",
    "location": "Bellevue, WA; Boston, MA",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/Bellevue-WA/Software-Engineer-III_R29953",
    "posted_date": "2026-08-05",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:02.606817+00:00",
    "date_confidence": "high",
    "description": "Job Description: We are hiring amazing humans, and we hope that includes you! Are you looking for more than just a job? At Chewy, you’ll find yourself on a career path with other o"
  },
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R30410",
    "title": "Staff Software Engineer",
    "location": "Bellevue, WA; Boston, MA",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/Bellevue-WA/Staff-Software-Engineer_R30410",
    "posted_date": "2026-08-05",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:02.606817+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity: Chewy is hiring a Staff Software Engineer to lead the technical direction of Chewy’s Discovery Experience platform in Bellevue, WA. The Discovery "
  },
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R30754",
    "title": "Software Engineer II",
    "location": "Boston, MA",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/Boston-MA/Software-Engineer-II_R30754",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:02.606817+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Opportunity: We are hiring a Software Engineer II to join the Developer Experience team in Boston, MA . At Chewy, it is our mission to be the most trusted and "
  },
  {
    "company": "Chewy",
    "source": "chewy_official_careers",
    "job_id": "R29253",
    "title": "Software Engineer II - Frontend",
    "location": "Boston, MA",
    "official_url": "https://wd5.myworkdaysite.com/recruiting/chewy/External/job/Boston-MA/Software-Engineer-II---Frontend_R29253",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:02.606817+00:00",
    "date_confidence": "high",
    "description": "Job Description: Our Team: The Chewy+ Loyalty team builds customer-facing membership experiences that help pet parents discover value, manage their plan, earn and use rewards, and "
  }
]
```

## CVS Health

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Large employer; lower SWE density, implement only if cheap.']

## Duolingo

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/duolingo/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 87
- After US/location filtering: 75
- With trustworthy posted_date: 75
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
    "fetched_at": "2026-08-31T18:21:48.790752+00:00",
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
    "updated_date": "2026-08-13",
    "fetched_at": "2026-08-31T18:21:48.790752+00:00",
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
    "fetched_at": "2026-08-31T18:21:48.790752+00:00",
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
    "fetched_at": "2026-08-31T18:21:48.790752+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  },
  {
    "company": "Duolingo",
    "source": "duolingo_official_careers",
    "job_id": "8442932002",
    "title": "Creative Director, Marketing",
    "location": "New York, NY; London, England, United Kingdom; New York, New York, United States",
    "official_url": "https://careers.duolingo.com/jobs/8442932002?gh_jid=8442932002",
    "posted_date": "2026-02-27",
    "updated_date": "2026-08-06",
    "fetched_at": "2026-08-31T18:21:48.790752+00:00",
    "date_confidence": "high",
    "description": "<p>Our mission at Duolingo is to develop the best education in the world and make it universally available. It’s a big mission, and that’s where you come in!</p> <p>At Duolingo, yo"
  }
]
```

## Equinix

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Good infra/software relevance; inspect ATS.']

## F5

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://ffive.wd5.myworkdayjobs.com/f5jobs`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 5
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 1 / 0
- Raw jobs found: 50
- After US/location filtering: 1
- With trustworthy posted_date: 1
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "F5",
    "source": "f5_official_careers",
    "job_id": "RP1038531",
    "title": "Sr. Software Development Engineer",
    "location": "F5 Tower; San Jose; Spokane Valley",
    "official_url": "https://ffive.wd5.myworkdayjobs.com/f5jobs/job/F5-Tower/Sr-Software-Development-Engineer_RP1038531",
    "posted_date": "2026-08-31",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:48.992376+00:00",
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
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 109
- After US/location filtering: 99
- With trustworthy posted_date: 99
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8726150002",
    "title": "Account Executive, Rosetta Stone Latin America",
    "location": "Bogotá, Colombia; Bogotá, Bogota D.C., Colombia",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8726150002",
    "posted_date": "2026-08-18",
    "updated_date": "2026-08-19",
    "fetched_at": "2026-08-31T18:21:55.211724+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is seeking an Account Executive to join our Rosetta Stone Latin America (LATAM) te"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8642613002",
    "title": "Account Manager, K-12",
    "location": "Raleigh, NC; Morrisville, North Carolina, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8642613002",
    "posted_date": "2026-07-21",
    "updated_date": "2026-07-21",
    "fetched_at": "2026-08-31T18:21:55.211724+00:00",
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
    "fetched_at": "2026-08-31T18:21:55.211724+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is looking for an Administrative Assistant to support IXL’s RFP and proposals stra"
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
    "fetched_at": "2026-08-31T18:21:55.211724+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is seeking an Associate Curriculum Alignment Specialist to join our curriculum dev"
  },
  {
    "company": "IXL Learning",
    "source": "ixl_learning_official_careers",
    "job_id": "8577706002",
    "title": "Associate Customer Support Analyst, Teachers Pay Teachers (TPT)",
    "location": "Raleigh, NC; Morrisville, North Carolina, United States",
    "official_url": "https://www.ixl.com/company/jobs?gh_jid=8577706002",
    "posted_date": "2026-06-05",
    "updated_date": "2026-08-20",
    "fetched_at": "2026-08-31T18:21:55.211724+00:00",
    "date_confidence": "high",
    "description": "<p>IXL Learning, developer of personalized learning products used by millions of people globally, is seeking a driven, customer-focused, and analytical individual to join our Teach"
  }
]
```

## Wayfair

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Good SWE volume; inspect backend.']

## Wells Fargo

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Huge feed but low SWE density; only add with strong filters.']

## Yahoo

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Relevant software employer; implement if easy.']

## Ansys

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Technical employer but lower priority; implement only if near-zero incremental cost.']

## Blizzard Entertainment

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Interesting SWE roles but lower volume; easy-only.']

## Flex

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://flextronics.wd1.myworkdayjobs.com/Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 10
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 43 / 0
- Raw jobs found: 179
- After US/location filtering: 43
- With trustworthy posted_date: 43
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD227317",
    "title": "Software Development Engineer",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Software-Development-Engineer_WD227317",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:55.639006+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD228034",
    "title": "ICT Engineer",
    "location": "USA, TX, Austin",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/ICT-Engineer_WD228034",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:55.639006+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD228088",
    "title": "Test Engineering Manager",
    "location": "USA, SC, Columbia",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-SC-Columbia/Test-Engineering-Manager_WD228088",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:55.639006+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
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
    "fetched_at": "2026-08-31T18:21:55.639006+00:00",
    "date_confidence": "high",
    "description": "Flex is the diversified manufacturing partner of choice that helps market-leading brands design, build and deliver innovative products that improve the world. A career at Flex offe"
  },
  {
    "company": "Flex",
    "source": "flex_official_careers",
    "job_id": "WD225959",
    "title": "Engineering Technician",
    "location": "USA, TN, Memphis",
    "official_url": "https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TN-Memphis/Engineering-Technician_WD225959",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:21:55.639006+00:00",
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
- Pages/requests fetched: 10
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 39 / 0
- Raw jobs found: 161
- After US/location filtering: 38
- With trustworthy posted_date: 38
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1526366",
    "title": "Senior Software Engineer (React), IQVIA Digital",
    "location": "Red Bank, NJ, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Red-Bank-NJ-United-States-of-America/Senior-Software-Engineer_R1526366",
    "posted_date": "2026-08-19",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:22:34.927684+00:00",
    "date_confidence": "high",
    "description": "IQVIA Digital Overview: IQVIA Digital powers exceptional brand experiences, delivering innovative solutions based on a customer-first, insights-driven, and integrated omnichannel v"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1548888",
    "title": "Sr Software Development Engineer",
    "location": "Houston, Texas, United States of America; Greenwich, CT, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Houston-Texas-United-States-of-America/Sr-Software-Development-Engineer_R1548888",
    "posted_date": "2026-06-29",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:22:34.927684+00:00",
    "date_confidence": "high",
    "description": "About Cedar Gate Technologies Cedar Gate Technologies, an IQVIA business, enables payers, providers, employers, and service administrators to excel at value-based care with a unifi"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1320047",
    "title": "Sr. Software Developer",
    "location": "Bogota, Colombia",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Bogota-Colombia/XMLNAME-40842---Software-Devl-Analyst-2_R1320047",
    "posted_date": "2022-12-14",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:22:34.927684+00:00",
    "date_confidence": "high",
    "description": "Job Overview Under broad guidance, performs activities related to the analysis, design, programming, debugging, modification, and maintenance of web enhancements and/or new product"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1554802",
    "title": "Development Manager",
    "location": "Greenwich, CT, United States of America; Burlington, MA, United States of America",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Greenwich-CT-United-States-of-America/Development-Manager_R1554802",
    "posted_date": "2026-08-05",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:22:34.927684+00:00",
    "date_confidence": "high",
    "description": "About Cedar Gate Technologies Cedar Gate Technologies, an IQVIA business, enables payers, providers, employers, and service administrators to excel at value-based care with a unifi"
  },
  {
    "company": "IQVIA",
    "source": "iqvia_official_careers",
    "job_id": "R1320054",
    "title": "Sr. Software Developer",
    "location": "Bogota, Colombia",
    "official_url": "https://iqvia.wd1.myworkdayjobs.com/IQVIA/job/Bogota-Colombia/Sr-Software-Developer_R1320054",
    "posted_date": "2022-09-05",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:22:34.927684+00:00",
    "date_confidence": "high",
    "description": "Job Overview Under broad guidance, performs activities related to the analysis, design, programming, debugging, modification, and maintenance of software enhancements and/or new pr"
  }
]
```

## Johnson & Johnson

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Large mixed-role employer; only if generic and cheap.']

## Nasdaq

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 8
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 37 / 0
- Raw jobs found: 143
- After US/location filtering: 37
- With trustworthy posted_date: 37
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026302",
    "title": "Software Engineer",
    "location": "Lithuania - Vilnius",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/Lithuania---Vilnius/Software-Engineer_R0026302",
    "posted_date": "2026-06-19",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:18.952549+00:00",
    "date_confidence": "high",
    "description": "As a Software Engineer reporting to Senior Director, you'll play a critical role in designing, developing, and delivering software solutions that power Nasdaq's technology platform"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026396",
    "title": "Senior Software Engineer",
    "location": "CA-Toronto-York St 24/25",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/CA-Toronto-York-St-2425/Senior-Software-Engineer_R0026396",
    "posted_date": "2026-07-07",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:18.952549+00:00",
    "date_confidence": "high",
    "description": "As a Senior Software Engineer reporting to the Sr. Director of Software Development, you'll play a critical role in building the next generation of market data streaming products t"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026607",
    "title": "Lead Software Engineer",
    "location": "USA - Philadelphia - Pennsylvania",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---Philadelphia---Pennsylvania/Lead-Software-Engineer_R0026607",
    "posted_date": "2026-08-04",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:18.952549+00:00",
    "date_confidence": "high",
    "description": "As a Lead Software Engineer reporting to the VP - Software Engineering, you'll play a critical role in developing and maintaining the technology that powers Nasdaq's Derivatives Ma"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026685",
    "title": "Principal Software Engineer",
    "location": "USA - Atlanta - Georgia",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---Atlanta---Georgia/Principal-Software-Engineer_R0026685-1",
    "posted_date": "2026-08-18",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:18.952549+00:00",
    "date_confidence": "high",
    "description": "As a Principal Software Engineer, you'll play a defining role in shaping the technical direction of the platforms that power the institutional investing marketplace. You'll operate"
  },
  {
    "company": "Nasdaq",
    "source": "nasdaq_official_careers",
    "job_id": "R0026675",
    "title": "Software Engineer Specialist",
    "location": "USA - New York City - New York",
    "official_url": "https://nasdaq.wd1.myworkdayjobs.com/Global_External_Site/job/USA---New-York-City---New-York/Software-Engineer--Specialist_R0026675",
    "posted_date": "2026-08-20",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:18.952549+00:00",
    "date_confidence": "high",
    "description": "The Role As a Software Engineer Specialist reporting to th e Director - Software Engineering , you'll play a critical role in building and maintaining the technology platforms that"
  }
]
```

## PointClickCare

- Status: ok
- Scraping method: HTTP GET shared Lever postings API /v0/postings/{token}
- Search URL/API: `https://jobs.lever.co/pointclickcare`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 59
- After US/location filtering: 59
- With trustworthy posted_date: 59
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "30417b22-fd9a-4ff2-bc8d-5689401063b7",
    "title": "(Canada) Commercial Services Representative (6 month secondment)",
    "location": "Remote or Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/30417b22-fd9a-4ff2-bc8d-5689401063b7",
    "posted_date": "2026-08-17",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "At PointClickCare our mission is simple: to help providers deliver exceptional care. And that starts with our people. As a leading health tech company that’s founder-led and privat"
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
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "At PointClickCare our mission is simple: to help providers deliver exceptional care. And that starts with our people. As a leading health tech company that’s founder-led and privat"
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
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "We are seeking a dynamic and results-oriented Named Regional Account Executive to join our high-performing team. This role is responsible for driving revenue growth through strateg"
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "5fb4a010-9087-45ac-b49a-631cfdb0b2c8",
    "title": "(Canada) Solutions Analyst- Pharmacy",
    "location": "Remote or Mississauga",
    "official_url": "https://jobs.lever.co/pointclickcare/5fb4a010-9087-45ac-b49a-631cfdb0b2c8",
    "posted_date": "2026-08-05",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "At PointClickCare our mission is simple: to help providers deliver exceptional care. And that starts with our people. As a leading health tech company that’s founder-led and privat"
  },
  {
    "company": "PointClickCare",
    "source": "pointclickcare_official_careers",
    "job_id": "efcc56c5-ba22-416a-bff2-5f04ea1579ee",
    "title": "(US) Commercial Services Representative (6 month contract)",
    "location": "Remote or In Office",
    "official_url": "https://jobs.lever.co/pointclickcare/efcc56c5-ba22-416a-bff2-5f04ea1579ee",
    "posted_date": "2026-08-17",
    "updated_date": "",
    "fetched_at": "",
    "date_confidence": "medium",
    "description": "At PointClickCare our mission is simple: to help providers deliver exceptional care. And that starts with our people. As a leading health tech company that’s founder-led and privat"
  }
]
```

## Stryker

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://stryker.wd1.myworkdayjobs.com/StrykerCareers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 8
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 37 / 0
- Raw jobs found: 156
- After US/location filtering: 37
- With trustworthy posted_date: 37
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R565692",
    "title": "Staff Software Engineer",
    "location": "San Jose, California",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/San-Jose-California/Staff-Software-Engineer_R565692-1",
    "posted_date": "2026-08-04",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:53.457260+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid or Onsite Stryker is seeking a Staff Software Engineer to join our Endoscopy division. This role will lead the design and development of Windows-based soft"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R570033",
    "title": "Associate Manager, Software Engineering",
    "location": "Portage, Michigan",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Portage-Michigan/Associate-Manager--Software-Engineering_R570033",
    "posted_date": "2026-08-18",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:53.457260+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid Join a leadership team focused on advancing software quality, verification, and test excellence across a portfolio of regulated products. In this role, you"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R570625",
    "title": "Salesforce Software Engineer (Remote)",
    "location": "Portage, Michigan; Atlanta, Georgia; Dallas, Texas; Chicago, Illinois; Indianapolis, Indiana",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Portage-Michigan/Salesforce-Software-Engineer--Remote-_R570625",
    "posted_date": "2026-08-20",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:53.457260+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Remote As a Salesforce Software Engineer, you will play a key role in shaping how our U.S. commercial organization leverages Salesforce to manage accounts, streng"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R570077",
    "title": "Senior Embedded Software Engineer",
    "location": "Portage, Michigan",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Portage-Michigan/Senior-Embedded-Software-Engineer_R570077",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:53.457260+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid What You Will Do: We are looking for a collaborative Senior Software Engineer who enjoys solving complex technical challenges and driving continuous improv"
  },
  {
    "company": "Stryker",
    "source": "stryker_official_careers",
    "job_id": "R569978",
    "title": "Staff Software Engineer, R&D",
    "location": "Portage, Michigan",
    "official_url": "https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Portage-Michigan/Staff-Software-Engineer--R-D_R569978",
    "posted_date": "2026-08-05",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:23:53.457260+00:00",
    "date_confidence": "high",
    "description": "Work Flexibility: Hybrid Join a team developing embedded software for advanced electromechanical medical devices within Stryker's Orthopaedic Instruments business. In this role, yo"
  }
]
```

## TransUnion

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://transunion.wd5.myworkdayjobs.com/TransUnion`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 7
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 55 / 0
- Raw jobs found: 84
- After US/location filtering: 55
- With trustworthy posted_date: 55
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19041752",
    "title": "Directors, Software Engineering",
    "location": "Chicago, Illinois",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/Directors--Software-Engineering_19041752",
    "posted_date": "2026-08-06",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:24:25.602362+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview Directors, Software Engineering for Chicago IL, location. Provide strat"
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19041696",
    "title": "Software Engineer II - DevOps",
    "location": "Bengaluru",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Bengaluru/Software-Engineer-II---DevOps_19041696",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:24:25.602362+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Team Overview Sr. Devops Engineer for Fraud Solutions products to handle Production, pre-production environments , automation , monitoring"
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19040961",
    "title": "Senior Developer Software",
    "location": "Bengaluru; Chennai",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Bengaluru/Senior-Developer-Software_19040961",
    "posted_date": "2026-08-02",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:24:25.602362+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Team Overview As a Software Engineer (Java Backend), you will design and develop scalable, cloud-ready backend services that power fraud p"
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19041173",
    "title": "Senior .NET Developer",
    "location": "Lagunilla de Heredia; Remote - Costa Rica",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Lagunilla-de-Heredia/Senior-NET-Developer_19041173",
    "posted_date": "2026-07-20",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:24:25.602362+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Team Overview The DHI Information Technology Online Scrum Team supports TransUnion’s DHI business unit by building, maintaining, and moder"
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
    "fetched_at": "2026-08-31T18:24:25.602362+00:00",
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
- Pages/requests fetched: 8
- Incremental mode/page cap: incremental / 4
- Detail pages fetched/cache reused: 72 / 0
- Raw jobs found: 139
- After US/location filtering: 72
- With trustworthy posted_date: 72
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51277",
    "title": "Software Engineer II",
    "location": "CT - Hartford; GA - Atlanta; MN - St. Paul; MD - Hunt Valley",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Software-Engineer-II_R-51277",
    "posted_date": "2026-06-30",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:24:58.554643+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51279",
    "title": "Director, Software Engineering",
    "location": "CT - Hartford; GA - Atlanta; MN - St. Paul; MD - Hunt Valley",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Director--Software-Engineering_R-51279",
    "posted_date": "2026-08-20",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:24:58.554643+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51276",
    "title": "Software Engineer I",
    "location": "CT - Hartford; GA - Atlanta; MN - St. Paul; MD - Hunt Valley",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Software-Engineer-I_R-51276-1",
    "posted_date": "2026-06-30",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:24:58.554643+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51345",
    "title": "Sr Software Engineer",
    "location": "CT - Hartford; MN - St. Paul",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Sr-Software-Engineer_R-51345",
    "posted_date": "2026-07-10",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:24:58.554643+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  },
  {
    "company": "Travelers",
    "source": "travelers_official_careers",
    "job_id": "R-51974",
    "title": "Director, Software Engineer (Circle Engineer)",
    "location": "CT - Hartford; MN - St. Paul",
    "official_url": "https://travelers.wd5.myworkdayjobs.com/External/job/CT---Hartford/Director--Software-Engineer--Circle-Engineer-_R-51974-1",
    "posted_date": "2026-08-18",
    "updated_date": "",
    "fetched_at": "2026-08-31T18:24:58.554643+00:00",
    "date_confidence": "high",
    "description": "Who Are We? Taking care of our customers, our communities and each other. That’s the Travelers Promise. By honoring this commitment, we have maintained our reputation as one of the"
  }
]
```

## Verizon

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Incremental mode/page cap: - / -
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Large tech org but noisy; easy-only.']

## Yext

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/yext/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Incremental mode/page cap: incremental / 12
- Detail pages fetched/cache reused: 0 / 0
- Raw jobs found: 23
- After US/location filtering: 12
- With trustworthy posted_date: 12
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
    "fetched_at": "2026-08-31T18:25:45.271798+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "7731837",
    "title": "Associate Technical Partner Manager",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/7731837",
    "posted_date": "2026-03-27",
    "updated_date": "2026-08-21",
    "fetched_at": "2026-08-31T18:25:45.271798+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "7766556",
    "title": "Customer Success Manager, Enterprise - Financial Services",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/7766556",
    "posted_date": "2026-04-07",
    "updated_date": "2026-08-17",
    "fetched_at": "2026-08-31T18:25:45.271798+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  },
  {
    "company": "Yext",
    "source": "yext_official_careers",
    "job_id": "7989162",
    "title": "Director Financial Systems & Integrations",
    "location": "New York, NY; New York, NY, United States",
    "official_url": "https://job-boards.greenhouse.io/yext/jobs/7989162",
    "posted_date": "2026-06-10",
    "updated_date": "2026-08-17",
    "fetched_at": "2026-08-31T18:25:45.271798+00:00",
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
    "fetched_at": "2026-08-31T18:25:45.271798+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Yext (NYSE: YEXT) is the enterprise agentic marketing platform. Built on the world's most comprehensive structured data platform for local businesses,"
  }
]
```
