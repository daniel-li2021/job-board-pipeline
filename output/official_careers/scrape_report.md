# Official careers scrape report — 2026-08-30_0902

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or advertised total
- Pages/requests fetched: 73
- Raw jobs found: 1442
- After US/location filtering: 384
- With trustworthy posted_date: 384
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "73942314325549766",
    "title": "Senior Software Engineer, Google XR, Gaming",
    "location": "San Francisco, CA, USA; New York, NY, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/73942314325549766-senior-software-engineer-google-xr-gaming",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-30T09:02:19.265192+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "126285664877454022",
    "title": "Senior Software Engineer, AI/ML, Core",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/126285664877454022-senior-software-engineer-ai-ml-core",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-30T09:02:19.265192+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "93036433253507782",
    "title": "Software Engineer III, Infrastructure, Infra Spanner",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/93036433253507782-software-engineer-iii-infrastructure-infra-spanner",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-30T09:02:19.265192+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "109889747484058310",
    "title": "Software Engineer III, Android, Geo",
    "location": "San Francisco, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/109889747484058310-software-engineer-iii-android-geo",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-30T09:02:19.265192+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "101599343911281350",
    "title": "Software Engineer III, Infrastructure, Infra Bigtable",
    "location": "New York, NY, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/101599343911281350-software-engineer-iii-infrastructure-infra-bigtable",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-30T09:02:19.265192+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  }
]
```

## Amazon

- Status: ok
- Scraping method: HTTP GET search.json
- Search URL/API: `https://www.amazon.jobs/en/search?base_query=software+engineer&country=USA&offset=0&result_limit=10&sort=recent`
- Pagination: offset=0,20,... ; result_limit=20; stop on empty/repeat or hits
- Pages/requests fetched: 49
- Raw jobs found: 927
- After US/location filtering: 682
- With trustworthy posted_date: 682
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10517792",
    "title": "Senior Software Engineer, AWS Applied AI Solutions",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10517792/senior-software-engineer-aws-applied-ai-solutions",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-30T09:03:05.432645+00:00",
    "date_confidence": "high",
    "description": "As part of the AWS Applied AI Solutions organization, we have a vision to provide business applications, leveraging Amazon’s unique experience and expertise, that are used by milli"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10513639",
    "title": "Principal Technical Program Manager - Prime Video, PV Personalization and Discovery",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10513639/principal-technical-program-manager-prime-video-pv-personalization-and-discovery",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-30T09:03:05.432645+00:00",
    "date_confidence": "high",
    "description": "Prime Video is a first-stop entertainment destination offering customers a vast collection of premium programming in one app available across thousands of devices. Prime members ca"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10513234",
    "title": "AI/ML Engineer, Amazon Global Data Center Ops Central Insight and Analytics Team",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10513234/ai-ml-engineer-amazon-global-data-center-ops-central-insight-and-analytics-team",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-30T09:03:05.432645+00:00",
    "date_confidence": "high",
    "description": "We are looking for an **AI/ML Engineer** to build, deploy, and operate the ML/AI systems that power the agentic decision intelligence workflow we are building. You are the person w"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10515062",
    "title": "Front End Engineer, AWS Agentic AI Automated Reasoning (AR)",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10515062/front-end-engineer-aws-agentic-ai-automated-reasoning-ar",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-30T09:03:05.432645+00:00",
    "date_confidence": "high",
    "description": "We are building exciting new capabilities in the Amazon Web Services (AWS) Agentic AI Automated Reasoning group by using Automated Reasoning in new, novel and exciting ways to enha"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10515061",
    "title": "Sr. Front End Engineer, AWS Agentic AI Automated Reasoning (AR)",
    "location": "Seattle, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10515061/sr-front-end-engineer-aws-agentic-ai-automated-reasoning-ar",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-30T09:03:05.432645+00:00",
    "date_confidence": "high",
    "description": "We are building exciting new capabilities in the Amazon Web Services (AWS) Agentic AI Automated Reasoning group by using Automated Reasoning in new, novel and exciting ways to enha"
  }
]
```

## Apple

- Status: blocked
- Scraping method: apple
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ["apple network error: HTTPSConnectionPool(host='jobs.apple.com', port=443): Read timed out. (read timeout=30)"]

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: start=0,10,20,... ; num=10 (API cap); stop on empty/repeat or count
- Pages/requests fetched: 78
- Raw jobs found: 771
- After US/location filtering: 328
- With trustworthy posted_date: 328
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200052629",
    "title": "Senior Security Operations Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556983225",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:04:33.412024+00:00",
    "date_confidence": "high",
    "description": "Overview Quantum computing has the potential to massively accelerate science and technology innovation. Microsoft Discovery & Quantum group is building advanced computing platforms"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200052627",
    "title": "Principal Security Operations Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556983224",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:04:33.412024+00:00",
    "date_confidence": "high",
    "description": "Overview Quantum computing has the potential to massively accelerate science and technology innovation. Microsoft Discovery & Quantum is building advanced computing platforms, span"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200052038",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556982164",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:04:33.412024+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Research is working to transform the future of artificial intelligence by bridging the gap between cutting-edge general AI and the specialized, real-world applic"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200038101",
    "title": "Senior Firmware Development Engineer",
    "location": "United States, California, Mountain View; United States, Washington, Redmond; United States, Oregon, Hillsboro",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556868650",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:04:33.412024+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon and Cloud Hardware Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Microsof"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200046032",
    "title": "Industry Architect - Research & Development",
    "location": "United States, Multiple Locations, Multiple Locations",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556950622",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:04:33.412024+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft is helping define a new era of scientific and industrial innovation: one where agentic AI, cloud-scale computing, data, simulation, and human expertise come toge"
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 84
- Raw jobs found: 1655
- After US/location filtering: 953
- With trustworthy posted_date: 953
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2018179",
    "title": "Applied AI Engineer",
    "location": "US, CA, Remote",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Remote/Applied-AI-Engineer_JR2018179-3",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:06:37.469722+00:00",
    "date_confidence": "high",
    "description": "NVIDIA's Silicon Co-Design Group is seeking an Applied AI Engineer to innovate, develop, and integrate innovative AI solutions into the design and automation infrastructure that po"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2018178",
    "title": "Applied AI Engineer",
    "location": "US, CA, Remote",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Remote/Applied-AI-Engineer_JR2018178-3",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:06:37.469722+00:00",
    "date_confidence": "high",
    "description": "NVIDIA's Silicon Co-Design Group is seeking an Applied AI Engineer to innovate, develop, and integrate innovative AI solutions into the design and automation infrastructure that po"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2018181",
    "title": "Applied AI Engineer",
    "location": "US, CA, Remote",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Remote/Applied-AI-Engineer_JR2018181-1",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:06:37.469722+00:00",
    "date_confidence": "high",
    "description": "NVIDIA's Silicon Co-Design Group is seeking an Applied AI Engineer to innovate, develop, and integrate innovative AI solutions into the design and automation infrastructure that po"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2020962",
    "title": "Senior Platform AI Engineer",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Platform-AI-Engineer_JR2020962",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:06:37.469722+00:00",
    "date_confidence": "high",
    "description": "For over 25 years, NVIDIA has been revolutionizing computer graphics, PC gaming, and accelerated computing. It’s a unique legacy of innovation that’s fueled by great technology—and"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2021231",
    "title": "Senior Applied AI Engineer",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Applied-AI-Engineer_JR2021231-1",
    "posted_date": "2026-07-17",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:06:37.469722+00:00",
    "date_confidence": "high",
    "description": "NVIDIA has been transforming accelerated computing with innovation that’s fueled by great technology—and amazing people. As part of Nvidia's applied AI team for chip design, you wi"
  }
]
```

## Salesforce

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://salesforce.wd12.myworkdayjobs.com/External_Career_Site`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 65
- Raw jobs found: 1207
- After US/location filtering: 173
- With trustworthy posted_date: 173
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR358273",
    "title": "Technical Architect (Products, Auto, Consumer, Or Energy Industry)",
    "location": "Illinois - Chicago Metro - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Illinois---Chicago-Metro---Remote/Technical-Architect--Products--Auto--Consumer--Or-Energy-Industry-_JR358273",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:09:56.576181+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Customer Success Jo"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR355248",
    "title": "Senior Product Manager, Emerging Technology",
    "location": "New York - New York",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/New-York---New-York/Senior-Product-Manager--Emerging-Technology_JR355248",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:09:56.576181+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Product Job Details"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR336646",
    "title": "Technical Support Engineer - Agentforce & Data 360",
    "location": "Washington - Seattle",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Washington---Seattle/Agentforce---Data-360-Support-Engineer_JR336646",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:09:56.576181+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Customer Success Jo"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR351980",
    "title": "VP, Software Engineering",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/VP--Software-Engineering_JR351980",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:09:56.576181+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357121",
    "title": "Field CTO, Data Governance and MDM, Data Foundations",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Field-CTO--Data-Governance-and-MDM--Data-Foundations_JR357121",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:09:56.576181+00:00",
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
- Pages/requests fetched: 72
- Raw jobs found: 1352
- After US/location filtering: 254
- With trustworthy posted_date: 254
- Errors/403s: none

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
    "fetched_at": "2026-08-30T09:11:59.735522+00:00",
    "date_confidence": "high",
    "description": "The Opportunity We are looking for a hands-on AI Agent Engineer to develop, build, and maintain intelligent agents that drive automation and business impact across the enterprise. "
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170895",
    "title": "Senior Agentic AI Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Senior-Agentic-AI-Engineer_R170895",
    "posted_date": "2026-08-02",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:11:59.735522+00:00",
    "date_confidence": "high",
    "description": "The Opportunity Join our world-class team in San Jose, CA, where your engineering skills will flourish! In this role, you’ll help shape the future of Adobe’s next-generation agenti"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R165968",
    "title": "Senior AI Platform Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Senior-AI-Platform-Engineer_R165968-1",
    "posted_date": "2026-06-15",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:11:59.735522+00:00",
    "date_confidence": "high",
    "description": "The Opportunity Adobe empowers individuals and organizations to create exceptional content effortlessly. The AI for Engineering team builds a scalable, production-grade AI platform"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R168433",
    "title": "Staff AI VFX Engineer",
    "location": "Los Angeles",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/Los-Angeles/Staff-AI-VFX-Engineer_R168433",
    "posted_date": "2026-05-20",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:11:59.735522+00:00",
    "date_confidence": "high",
    "description": "The Opportunity As AI rapidly transforms creative industries, professional production workflows must evolve alongside it. At Firefly Foundry , we’re leading an industry-first initi"
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R168858",
    "title": "Senior Applied AI Engineer– Creative Systems & Brand Intelligence, Adobe Express",
    "location": "San Francisco",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Francisco/Senior-Applied-AI-Engineer--Creative-Systems---Brand-Intelligence--Adobe-Express_R168858",
    "posted_date": "2026-07-23",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:11:59.735522+00:00",
    "date_confidence": "high",
    "description": "The Opportunity Our pillar, Assets and Collaboration, focuses on building foundational capabilities in Adobe Express that help users create, organize, govern, and collaborate on co"
  }
]
```

## Meta

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['metacareers.com returns HTTP 400 for anonymous HTTP (WAF). Need a working search URL/HAR of the jobsearch JSON/GraphQL that a logged-out browser uses: https://www.metacareers.com/jobsearch/?q=software%20engineer&sort_by_new=true&roles[0]=Full%20time%20employment']

## TikTok

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['lifeattiktok.com/search is Next.js CSR; public job-list API returns empty/HTML. Need the XHR/fetch URL from DevTools on https://lifeattiktok.com/search?recruitment_id_list=1%2C201&keyword=software+engineer&limit=12&offset=0&location_code_list=CT_100762,CT_247,CT_1103554,CT_94,CT_103,CT_223,CT_243,CT_114,CT_203,CT_75,CT_1103355,CT_130,CT_157,CT_233']

## Uber

- Status: ok
- Scraping method: HTTP GET Oracle HCM recruitingCEJobRequisitions on iaziqy.fa.ocs.oraclecloud.com (offset pagination) + recruitingCEJobRequisitionDetails
- Search URL/API: `https://jobs.uber.com/en/jobs/?search=software%20engineer&page=1&pagesize=10`
- Pagination: HCM finder offset=(page-1)*limit ; limit=20; stop on empty/repeat or TotalJobsCount (do not stop at pages 1–7)
- Pages/requests fetched: 48
- Raw jobs found: 904
- After US/location filtering: 206
- With trustworthy posted_date: 206
- Errors/403s: none

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
    "fetched_at": "2026-08-30T09:14:53.615869+00:00",
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
    "fetched_at": "2026-08-30T09:14:53.615869+00:00",
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
    "fetched_at": "2026-08-30T09:14:53.615869+00:00",
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
    "fetched_at": "2026-08-30T09:14:53.615869+00:00",
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
    "fetched_at": "2026-08-30T09:14:53.615869+00:00",
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
- Raw jobs found: 468
- After US/location filtering: 464
- With trustworthy posted_date: 464
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-30T09:16:44.803579+00:00",
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-30T09:16:44.803579+00:00",
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-30T09:16:44.803579+00:00",
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
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-30T09:16:44.803579+00:00",
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-30T09:16:44.803579+00:00",
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
- Pages/requests fetched: 24
- Raw jobs found: 299
- After US/location filtering: 87
- With trustworthy posted_date: 87
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046467",
    "title": "Staff Machine Learning Engineer, Generative AI Modeling and Inference",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Staff-Machine-Learning-Engineer--Generative-AI-Modeling-and-Inference_R0046467",
    "posted_date": "2026-08-14",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:16:46.253474+00:00",
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
    "posted_date": "2026-07-31",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:16:46.253474+00:00",
    "date_confidence": "medium",
    "description": ""
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046612",
    "title": "Privacy Engineer, Level 4",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Privacy-Engineer--Level-4_R0046612-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:16:46.253474+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046161",
    "title": "Manager, Privacy Engineering",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Manager--Privacy-Engineering_R0046161-1",
    "posted_date": "2026-07-14",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:16:46.253474+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "H226EM8",
    "title": "Manager, Software Engineering",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Manager--Software-Engineering_H226EM8-1",
    "posted_date": "2026-07-09",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:16:46.253474+00:00",
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
- Raw jobs found: 209
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
    "fetched_at": "2026-08-30T09:17:30.768601+00:00",
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
    "fetched_at": "2026-08-30T09:17:30.768601+00:00",
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
    "updated_date": "2026-08-20",
    "fetched_at": "2026-08-30T09:17:30.768601+00:00",
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
    "fetched_at": "2026-08-30T09:17:30.768601+00:00",
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
    "fetched_at": "2026-08-30T09:17:30.768601+00:00",
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
- Raw jobs found: 389
- After US/location filtering: 304
- With trustworthy posted_date: 304
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
    "fetched_at": "2026-08-30T09:17:31.147893+00:00",
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
    "fetched_at": "2026-08-30T09:17:31.147893+00:00",
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
    "fetched_at": "2026-08-30T09:17:31.147893+00:00",
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
    "fetched_at": "2026-08-30T09:17:31.147893+00:00",
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
    "fetched_at": "2026-08-30T09:17:31.147893+00:00",
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
- Pages/requests fetched: 14
- Raw jobs found: 1032
- After US/location filtering: 269
- With trustworthy posted_date: 269
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075074",
    "title": "Sr Staff AI Engineer - Veza",
    "location": "Minneapolis, Minnesota, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146269339-sr-staff-ai-engineer-veza",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:17:31.472758+00:00",
    "date_confidence": "high",
    "description": "Veza is the pioneer in identity security, purpose-built to answer the fundamental question enterprises face: who can and should take what action on what data. Veza's Access Graph p"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074990",
    "title": "Senior Reliability Engineer",
    "location": "Minneapolis, Minnesota, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146080839-senior-reliability-engineer",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:17:31.472758+00:00",
    "date_confidence": "high",
    "description": "Veza is the pioneer in identity security, purpose-built to answer the fundamental question enterprises face: who can and should take what action on what data. Veza's Access Graph p"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074976",
    "title": "Senior Manager, Software Engineering Management - AI Experience Framework",
    "location": "San Diego, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146076439-senior-manager-software-engineering-management-ai-experience-framework",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:17:31.472758+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075039",
    "title": "Software Engineer",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146076209-software-engineer",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:17:31.472758+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074972",
    "title": "Senior Staff Data Platform Engineer - Kafka - Apache Iceberg - Apache Spark",
    "location": "San Diego, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146075679-senior-staff-data-platform-engineer-kafka-apache-iceberg-apache-spark",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:17:31.472758+00:00",
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
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['careers.linkedin.com has no public job-search API/ATS feed; Workday CXS is 401. Need the official LinkedIn-the-company engineering search URL (not linkedin.com/jobs).']

## Bloomberg

- Status: ok
- Scraping method: HTTP GET Avature SearchJobs HTML + JobDetail HTML
- Search URL/API: `https://bloomberg.avature.net/careers/SearchJobs?q=software+engineer&jobRecordsPerPage=12&jobOffset=0`
- Pagination: jobOffset=0,12,... ; stop on empty/repeat or short page
- Pages/requests fetched: 84
- Raw jobs found: 1008
- After US/location filtering: 74
- With trustworthy posted_date: 0
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21651",
    "title": "Product Manager — Terminal Controls, Compliance & Policy",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Product-Manager-Terminal-Controls-Compliance-Policy/21651",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:19:24.982378+00:00",
    "date_confidence": "unknown",
    "description": "Product Manager — Terminal Controls, Compliance & Policy"
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
    "fetched_at": "2026-08-30T09:19:24.982378+00:00",
    "date_confidence": "unknown",
    "description": "TOP & Today Editor - Los Angeles"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21640",
    "title": "White Hose Stringer - Part Time / Contract",
    "location": "Washington, District of Columbia, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/White-Hose-Stringer-Part-Time-Contract/21640",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:19:24.982378+00:00",
    "date_confidence": "unknown",
    "description": "White Hose Stringer - Part Time / Contract"
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
    "fetched_at": "2026-08-30T09:19:24.982378+00:00",
    "date_confidence": "unknown",
    "description": "Senior Financial Analyst, CFO Global Sustainability Office"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21659",
    "title": "Senior Data Management Professional - Company Financial Market Data",
    "location": "Princeton, New Jersey, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Data-Management-Professional-Company-Financial-Market-Data/21659",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:19:24.982378+00:00",
    "date_confidence": "unknown",
    "description": "Senior Data Management Professional - Company Financial Market Data"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 84
- Raw jobs found: 1680
- After US/location filtering: 542
- With trustworthy posted_date: 542
- Errors/403s: none

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
    "fetched_at": "2026-08-30T09:22:16.270507+00:00",
    "date_confidence": "high",
    "description": "Build and operate the AI toolchain that is accelerating mainframe modernization at scale. As an Sr Lead Software Engineer within Core Processing, Wealth Management Technology, you "
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
    "fetched_at": "2026-08-30T09:22:16.270507+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorgan Chase, within the Co"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210784683",
    "title": "Sr Lead Software Engineer - AI-Native Component Engineering",
    "location": "OH, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210784683",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:22:16.270507+00:00",
    "date_confidence": "high",
    "description": "Be an integral part of an agile team that's constantly pushing the envelope to enhance, build, and deliver top-notch technology products. As a Senior Lead Software Engineer at JPMo"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210785391",
    "title": "Lead Software Engineer - AI",
    "location": "OH, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210785391",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:22:16.270507+00:00",
    "date_confidence": "high",
    "description": "Build the context backbone for governed, agentic software delivery by designing secure, scalable Code Intelligence capabilities that help engineers navigate and act on code in real"
  },
  {
    "company": "JPMorgan Chase",
    "source": "jpmorgan_chase_official_careers",
    "job_id": "210775950",
    "title": "Lead Software Engineer – AI-Native Component Engineering",
    "location": "Columbus, OH, United States",
    "official_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210775950",
    "posted_date": "2026-08-21",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:22:16.270507+00:00",
    "date_confidence": "high",
    "description": "We have an opportunity to impact your career and provide an adventure where you can push the limits of what's possible. As a Lead Software Engineer at JPMorganChase within the Chie"
  }
]
```

## Capital One

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://capitalone.wd12.myworkdayjobs.com/Capital_One`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 73
- Raw jobs found: 1448
- After US/location filtering: 519
- With trustworthy posted_date: 519
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R246468",
    "title": "Manager, Product Management- Developer Experience",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Manager--Product-Management--Developer-Experience_R246468-1",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:24:34.444412+00:00",
    "date_confidence": "high",
    "description": "Manager, Product Management- Developer Experience Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, finding value creation opp"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R248104",
    "title": "Senior Manager, Product Management - Developer Experience, AI & Developer Productivity",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Manager--Product-Management---Developer-Experience--AI-Coding-Tools_R248104-1",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:24:34.444412+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Product Management - Developer Experience, AI & Developer Productivity Product Management at Capital One is a booming, vibrant craft that requires reimagining the s"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R246485",
    "title": "Senior Manager, Product Management - Developer Experience",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Manager--Product-Management----Developer-Experience_R246485",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:24:34.444412+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Product Management - Developer Experience Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, finding value crea"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999411",
    "title": "Lead Software Engineer, Backend (IC)",
    "location": "San Jose, CA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/San-Jose-CA/Lead-Software-Engineer--Backend--IC-_R999411-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:24:34.444412+00:00",
    "date_confidence": "high",
    "description": "Lead Software Engineer, Backend (IC) Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inc"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999435",
    "title": "Staff AI Engineer - Enterprise Analysis Platform (Remote Eligible)",
    "location": "San Francisco, CA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/San-Francisco--CA/Staff-AI-Engineer---Enterprise-Analysis-Platform--Remote-Eligible-_R999435-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:24:34.444412+00:00",
    "date_confidence": "high",
    "description": "Staff AI Engineer - Enterprise Analysis Platform (Remote Eligible) At Capital One, we are creating responsible and reliable AI systems, changing banking for good. For years, Capita"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 84
- Raw jobs found: 1678
- After US/location filtering: 705
- With trustworthy posted_date: 705
- Errors/403s: none

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
    "fetched_at": "2026-08-30T09:26:29.131888+00:00",
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
    "fetched_at": "2026-08-30T09:26:29.131888+00:00",
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
    "posted_date": "2026-06-10",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:26:29.131888+00:00",
    "date_confidence": "high",
    "description": "The ideal candidate is an experienced RDMA software engineer with a strong background in high-performance networking, distributed communication systems, and systems programming. Yo"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "336796",
    "title": "Senior Principal Engineer - AI Networking",
    "location": "Seattle, WA, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/336796",
    "posted_date": "2026-06-10",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:26:29.131888+00:00",
    "date_confidence": "high",
    "description": "You will work at the intersection of distributed systems, networking, and AI infrastructure, driving architecture, design, implementation, and performance optimization across softw"
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
    "fetched_at": "2026-08-30T09:26:29.131888+00:00",
    "date_confidence": "high",
    "description": "You will work at the intersection of distributed systems, networking, and AI infrastructure, driving architecture, design, implementation, and performance optimization across softw"
  }
]
```

## Walmart Global Tech

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['careers.walmart.com is a custom Next.js app; widgets/Workday CXS/JSON endpoints 404 or 422. Need the jobs search XHR URL from DevTools on a US software-engineer search.']

## Cisco

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cisco.wd5.myworkdayjobs.com/Cisco_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 59
- Raw jobs found: 1165
- After US/location filtering: 231
- With trustworthy posted_date: 231
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2021114",
    "title": "Software Engineer",
    "location": "Boulder, Colorado, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Boulder-Colorado-US/Software-Engineer_2021114-1",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:29:08.458337+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/18/2026 Meet the Team Splunk, a Cisco company, is building a safer, more resilient digital world with an end-to-end, full-stack p"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2022755",
    "title": "Engineering Product Manager",
    "location": "Houston, Texas, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Houston-Texas-US/Engineering-Product-Manager_2022755-1",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:29:08.458337+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/28/2026 Meet the Team Splunk, a Cisco company, helps the world’s most complex organizations turn machine data into action. The Da"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2019369",
    "title": "2019369 Customer Delivery Consulting Engineer - Security",
    "location": "Herndon, Virginia, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Herndon-Virginia-US/XMLNAME-2019369-Customer-Delivery-Consulting-Engineer---Security_2019369",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:29:08.458337+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/24/2026 The successful applicant will be performing work on US Government classified environments, and therefore, must be a U.S. "
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2022516",
    "title": "Technical Program Manager",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Technical-Program-Manager_2022516",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:29:08.458337+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/10/2026 Meet the Team Cisco Cloud Security Group is a leading provider of Cloud Security and DNS services, enabling the world to "
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2020847",
    "title": "Software Engineer",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Software-Engineer_2020847",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:29:08.458337+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/03/2026 Meet the team We are seeking an experienced and motivated Software Engineer to join our Service Provider High End Router "
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 47
- Raw jobs found: 1117
- After US/location filtering: 157
- With trustworthy posted_date: 0
- Errors/403s: none

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
    "fetched_at": "2026-08-30T09:31:00.896572+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1421516033",
    "title": "Forward Deployed AI Engineer",
    "location": "New York, NY, US, 10001",
    "official_url": "https://jobs.sap.com/job/New-York-Forward-Deployed-AI-Engineer-NY-10001/1421516033/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:31:00.896572+00:00",
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
    "fetched_at": "2026-08-30T09:31:00.896572+00:00",
    "date_confidence": "unknown",
    "description": "We help the world run better At SAP, we keep it simple: you bring your best to us, and we'll bring out the best in you. We're builders touching over 20 industries and 80% of global"
  },
  {
    "company": "SAP",
    "source": "sap_official_careers",
    "job_id": "1421516533",
    "title": "Forward Deployed Application/ ML Principal Engineer",
    "location": "New York, NY, US, 10001",
    "official_url": "https://jobs.sap.com/job/New-York-Forward-Deployed-Application-ML-Principal-Engineer-NY-10001/1421516533/",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:31:00.896572+00:00",
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
    "fetched_at": "2026-08-30T09:31:00.896572+00:00",
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
- Pages/requests fetched: 69
- Raw jobs found: 1313
- After US/location filtering: 284
- With trustworthy posted_date: 284
- Errors/403s: none

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
    "fetched_at": "2026-08-30T09:32:36.115562+00:00",
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
    "fetched_at": "2026-08-30T09:32:36.115562+00:00",
    "date_confidence": "high",
    "description": "Senior AI Engineer Developer This role has been designed as ‘’Onsite’ with an expectation that you will primarily work from an HPE office. Who We Are: Hewlett Packard Enterprise is"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1202624",
    "title": "AI Solution Engineer",
    "location": "All, Texas, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/All-Texas-United-States-of-America/AI-Solution-Engineer_1202624-2",
    "posted_date": "2026-02-12",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:32:36.115562+00:00",
    "date_confidence": "high",
    "description": "AI Solution Engineer This role has been designated as ‘Remote/Teleworker’, which means you will primarily work from home. Who We Are: Hewlett Packard Enterprise is the global edge-"
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1212266",
    "title": "AI Ops Engineer",
    "location": "San Juan, Puerto Rico, Puerto Rico",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/San-Juan-Puerto-Rico-Puerto-Rico/AI-Ops-Engineer_1212266",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:32:36.115562+00:00",
    "date_confidence": "high",
    "description": "AI Ops Engineer This role has been designed as 'Hybrid' with a requirement that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Packard Enterprise "
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1212264",
    "title": "AI Ops Engineer",
    "location": "San Juan, Puerto Rico, Puerto Rico",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/San-Juan-Puerto-Rico-Puerto-Rico/AI-Ops-Engineer_1212264-4",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:32:36.115562+00:00",
    "date_confidence": "high",
    "description": "AI Ops Engineer This role has been designed as 'Hybrid' with a requirement that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Packard Enterprise "
  }
]
```

## Disney

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Verified official filtered search captured; automated adapter deferred.']

## eBay

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Verified official search captured; automated adapter deferred.']

## Qualcomm

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Verified official search captured; automated adapter deferred.']

## AMD

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Verified official search captured; automated adapter deferred.']

## Zoom

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://zoom.wd5.myworkdayjobs.com/Zoom`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 17
- Raw jobs found: 203
- After US/location filtering: 47
- With trustworthy posted_date: 47
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19566",
    "title": "Lead Technical Product Manager",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Product-Architect-Lead-Product-Manager_R19566-1",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:35:27.496715+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect You will own and drive Zoom's Enterprise Infrastructure portfolio - covering data sovereignty, network resilience, and cryptographic key management for regulate"
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19366",
    "title": "AI Inference Engineer - Speech",
    "location": "Seattle (WA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/Seattle-WA/AI-Inference-Engineer---Speech_R19366-1",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:35:27.496715+00:00",
    "date_confidence": "high",
    "description": "What you can expect We are looking for an AI Inference Engineer with a solid background in speech recognition and model inference. In this role, you will develop state-of-the-art a"
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
    "fetched_at": "2026-08-30T09:35:27.496715+00:00",
    "date_confidence": "high",
    "description": "Immigration sponsorship is not available for this position What you can expect: We’re building the next-generation AI-native knowledge platform to help organizations easily access "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19452",
    "title": "Manager of Platform DevOps",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Manager-of-Platform-DevOps_R19452-1",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:35:27.496715+00:00",
    "date_confidence": "high",
    "description": "What You Can Expect You will be the leader of our Platforms DevOps team. This team is responsible for Zoom’s Kubernetes clusters in both datacenters and clouds, as well as for our "
  },
  {
    "company": "Zoom",
    "source": "zoom_official_careers",
    "job_id": "R19559",
    "title": "Software Development Engineer",
    "location": "San Jose (CA)",
    "official_url": "https://zoom.wd5.myworkdayjobs.com/Zoom/job/San-Jose-CA/Software-Development-Engineer_R19559",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-30T09:35:27.496715+00:00",
    "date_confidence": "high",
    "description": "Immigration sponsorship is not available for this position Responsibilities: Full-Stack Platform Dev. (25%): Design, dev., test, deploy, & maintain scalable, fault-tolerant distrib"
  }
]
```

## Goldman Sachs

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Verified official search captured; automated adapter deferred.']

## Pure Storage

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/purestorage/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Raw jobs found: 322
- After US/location filtering: 201
- With trustworthy posted_date: 201
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
    "fetched_at": "2026-08-30T09:36:00.291926+00:00",
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
    "fetched_at": "2026-08-30T09:36:00.291926+00:00",
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
    "fetched_at": "2026-08-30T09:36:00.291926+00:00",
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
    "fetched_at": "2026-08-30T09:36:00.291926+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p>Everpure (NYSE: P) has evolved from storage pioneer to data platform, closing fiscal 2026 with $3.7 billion in revenue, its first billion-dollar quart"
  },
  {
    "company": "Pure Storage",
    "source": "pure_storage_official_careers",
    "job_id": "8103422",
    "title": "Account Executive, SLED (TOLA)",
    "location": "Remote, Oklahoma; Oklahoma, United States",
    "official_url": "https://job-boards.greenhouse.io/purestorage/jobs/8103422",
    "posted_date": "2026-08-03",
    "updated_date": "2026-08-11",
    "fetched_at": "2026-08-30T09:36:00.291926+00:00",
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
- Raw jobs found: 856
- After US/location filtering: 489
- With trustworthy posted_date: 489
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
    "fetched_at": "2026-08-30T09:36:01.002621+00:00",
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
    "fetched_at": "2026-08-30T09:36:01.002621+00:00",
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
    "fetched_at": "2026-08-30T09:36:01.002621+00:00",
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
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-30T09:36:01.002621+00:00",
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
    "fetched_at": "2026-08-30T09:36:01.002621+00:00",
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
- Raw jobs found: 234
- After US/location filtering: 211
- With trustworthy posted_date: 211
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
    "fetched_at": "2026-08-30T09:36:02.215217+00:00",
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
    "fetched_at": "2026-08-30T09:36:02.215217+00:00",
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
    "fetched_at": "2026-08-30T09:36:02.215217+00:00",
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
    "updated_date": "2026-08-30",
    "fetched_at": "2026-08-30T09:36:02.215217+00:00",
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
    "fetched_at": "2026-08-30T09:36:02.215217+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><span style=\"font-weight: 400;\">Every day, tens of millions of people come to Roblox to explore, create, play, learn, and connect with friends in 3D i"
  }
]
```
