# Official careers scrape report — 2026-08-30_1821

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Ai+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or advertised total
- Pages/requests fetched: 86
- Raw jobs found: 1685
- After US/location filtering: 385
- With trustworthy posted_date: 385
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
    "fetched_at": "2026-08-30T18:21:19.426359+00:00",
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
    "fetched_at": "2026-08-30T18:21:19.426359+00:00",
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
    "fetched_at": "2026-08-30T18:21:19.426359+00:00",
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
    "fetched_at": "2026-08-30T18:21:19.426359+00:00",
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
    "fetched_at": "2026-08-30T18:21:19.426359+00:00",
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
- Pages/requests fetched: 65
- Raw jobs found: 1238
- After US/location filtering: 984
- With trustworthy posted_date: 984
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
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-30T18:22:16.228333+00:00",
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
    "fetched_at": "2026-08-30T18:22:16.228333+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-30T18:22:16.228333+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-30T18:22:16.228333+00:00",
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
    "updated_date": "2026-08-25",
    "fetched_at": "2026-08-30T18:22:16.228333+00:00",
    "date_confidence": "high",
    "description": "We are building exciting new capabilities in the Amazon Web Services (AWS) Agentic AI Automated Reasoning group by using Automated Reasoning in new, novel and exciting ways to enha"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=ai+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or totalRecords
- Pages/requests fetched: 120
- Raw jobs found: 2400
- After US/location filtering: 583
- With trustworthy posted_date: 583
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200679583-0157",
    "title": "Sr. Engineering Program Manager - Customer Systems",
    "location": "Austin, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200679583/sr-engineering-program-manager-customer-systems",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:22:51.496443+00:00",
    "date_confidence": "high",
    "description": "Do you want to help build some of the largest and most consequential enterprise and customer technology systems in the world? Join Apple’s Information Systems and Technology (IS&T)"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200670204-0836",
    "title": "RF System Integration Engineer (Instrument Engineering)",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200670204/rf-system-integration-engineer-instrument-engineering",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:22:51.496443+00:00",
    "date_confidence": "high",
    "description": "Join our Wireless team and build the technology that makes every Apple radio possible. We're looking for engineers with strong fundamentals in RF, communication, software and signa"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200677500-0157",
    "title": "Product RF Design Engineer",
    "location": "Austin, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200677500/product-rf-design-engineer",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:22:51.496443+00:00",
    "date_confidence": "high",
    "description": "You will have a once-in-a-lifetime opportunity to deliver outstanding performance for wireless products. As a member of the Product RF Design team, you will be at the forefront of "
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680059-3956",
    "title": "Applied Data Scientist and Visualization Specialist - Hardware Engineering Product Design",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680059/applied-data-scientist-and-visualization-specialist-hardware-engineering-product-design",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:22:51.496443+00:00",
    "date_confidence": "high",
    "description": "The Data Science and Visualization (DataViz) team in Hardware Engineering at Apple is seeking an enthusiastic team player to join us as an Applied Data Scientist and Visualization "
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200675258-0836",
    "title": "Software Development Engineer - Cellular (Instrument Engineering)",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200675258/software-development-engineer-cellular-instrument-engineering",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:22:51.496443+00:00",
    "date_confidence": "high",
    "description": "Join this small team of extraordinary engineers that designs and produces precision protocol, RF and Analog Test Equipment for use in calibrating and testing 4G, 5G, WiFi, BT, mmWa"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: start=0,10,20,... ; num=10 (API cap); stop on empty/repeat or count
- Pages/requests fetched: 94
- Raw jobs found: 931
- After US/location filtering: 434
- With trustworthy posted_date: 434
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
    "fetched_at": "2026-08-30T18:24:15.601338+00:00",
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
    "fetched_at": "2026-08-30T18:24:15.601338+00:00",
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
    "fetched_at": "2026-08-30T18:24:15.601338+00:00",
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
    "fetched_at": "2026-08-30T18:24:15.601338+00:00",
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
    "fetched_at": "2026-08-30T18:24:15.601338+00:00",
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
- Pages/requests fetched: 101
- Raw jobs found: 1967
- After US/location filtering: 1034
- With trustworthy posted_date: 1034
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
    "fetched_at": "2026-08-30T18:26:42.200150+00:00",
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
    "fetched_at": "2026-08-30T18:26:42.200150+00:00",
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
    "fetched_at": "2026-08-30T18:26:42.200150+00:00",
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
    "fetched_at": "2026-08-30T18:26:42.200150+00:00",
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
    "fetched_at": "2026-08-30T18:26:42.200150+00:00",
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
- Pages/requests fetched: 80
- Raw jobs found: 1476
- After US/location filtering: 204
- With trustworthy posted_date: 204
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
    "fetched_at": "2026-08-30T18:30:17.552139+00:00",
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
    "fetched_at": "2026-08-30T18:30:17.552139+00:00",
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
    "fetched_at": "2026-08-30T18:30:17.552139+00:00",
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
    "fetched_at": "2026-08-30T18:30:17.552139+00:00",
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
    "fetched_at": "2026-08-30T18:30:17.552139+00:00",
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
- Pages/requests fetched: 88
- Raw jobs found: 1604
- After US/location filtering: 284
- With trustworthy posted_date: 284
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
    "fetched_at": "2026-08-30T18:32:37.336979+00:00",
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
    "fetched_at": "2026-08-30T18:32:37.336979+00:00",
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
    "fetched_at": "2026-08-30T18:32:37.336979+00:00",
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
    "fetched_at": "2026-08-30T18:32:37.336979+00:00",
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
    "fetched_at": "2026-08-30T18:32:37.336979+00:00",
    "date_confidence": "high",
    "description": "The Opportunity Our pillar, Assets and Collaboration, focuses on building foundational capabilities in Adobe Express that help users create, organize, govern, and collaborate on co"
  }
]
```

## Meta

- Status: ok
- Scraping method: HTTP POST Meta Relay GraphQL; dynamic LSD and doc_id discovery
- Search URL/API: `https://www.metacareers.com/jobsearch/`
- Pagination: one complete Relay payload per role query
- Pages/requests fetched: 9
- Raw jobs found: 1678
- After US/location filtering: 526
- With trustworthy posted_date: 0
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1719639269238156",
    "title": "Product Manager, Platform",
    "location": "Menlo Park, CA; New York, NY",
    "official_url": "https://www.metacareers.com/jobs/1719639269238156",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:36:04.293434+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1275537681223900",
    "title": "Software Engineering Manager - Neural Interface ML Infra",
    "location": "Redmond, WA; Menlo Park, CA; Burlingame, CA; New York, NY",
    "official_url": "https://www.metacareers.com/jobs/1275537681223900",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:36:04.293434+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2412478939225801",
    "title": "Supply Chain Capacity Engineer",
    "location": "Menlo Park, CA; Fremont, CA",
    "official_url": "https://www.metacareers.com/jobs/2412478939225801",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:36:04.293434+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "1058967853284174",
    "title": "Technical Program Manager, Wearables AI",
    "location": "Sunnyvale, CA",
    "official_url": "https://www.metacareers.com/jobs/1058967853284174",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:36:04.293434+00:00",
    "date_confidence": "unknown",
    "description": ""
  },
  {
    "company": "Meta",
    "source": "meta_official_careers",
    "job_id": "2795485777493552",
    "title": "Network Production Engineering, Infrastructure",
    "location": "Menlo Park, CA",
    "official_url": "https://www.metacareers.com/jobs/2795485777493552",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:36:04.293434+00:00",
    "date_confidence": "unknown",
    "description": ""
  }
]
```

## TikTok

- Status: ok
- Scraping method: HTTP POST LifeAtTikTok public supplier /search/job/posts
- Search URL/API: `https://api.lifeattiktok.com/api/v1/public/supplier/search/job/posts`
- Pagination: offset=0,50,...; limit=50; US city filter
- Pages/requests fetched: 31
- Raw jobs found: 1394
- After US/location filtering: 642
- With trustworthy posted_date: 0
- Errors/403s: none

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
    "fetched_at": "2026-08-30T18:36:11.124876+00:00",
    "date_confidence": "unknown",
    "description": "Our team focuses on the R&D of algorithm for TikTok international advertising customer growth. We leverage deep learning and large language model technologies to build an algorithm"
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
    "fetched_at": "2026-08-30T18:36:11.124876+00:00",
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
    "fetched_at": "2026-08-30T18:36:11.124876+00:00",
    "date_confidence": "unknown",
    "description": "TikTok’s Web Architecture team is looking for a visionary Frontend Infrastructure Engineer (AI Tooling) to shape the future of AI-driven frontend engineering. You will work on the "
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
    "fetched_at": "2026-08-30T18:36:11.124876+00:00",
    "date_confidence": "unknown",
    "description": "The AIGE (AI-Generated Effects) team is building AI-native creative tools that enable TikTok creators to turn natural-language and multimodal ideas into high-quality, interactive e"
  },
  {
    "company": "TikTok",
    "source": "tiktok_official_careers",
    "job_id": "7663036952090347829",
    "title": "Backend Software Engineer Graduate (Emerging Products & AI Safety) - 2027 Start",
    "location": "San Jose, California, United States of America",
    "official_url": "https://lifeattiktok.com/search/7663036952090347829",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:36:11.124876+00:00",
    "date_confidence": "unknown",
    "description": "The Trust and Safety(TnS) engineering team is responsible for protecting our users from harmful content and abusive behaviors. With the continuous efforts of our trust and safety e"
  }
]
```

## Uber

- Status: ok
- Scraping method: HTTP GET Oracle HCM recruitingCEJobRequisitions on iaziqy.fa.ocs.oraclecloud.com (offset pagination) + recruitingCEJobRequisitionDetails
- Search URL/API: `https://jobs.uber.com/en/jobs/?search=software%20engineer&page=1&pagesize=10`
- Pagination: HCM finder offset=(page-1)*limit ; limit=20; stop on empty/repeat or TotalJobsCount (do not stop at pages 1–7)
- Pages/requests fetched: 52
- Raw jobs found: 976
- After US/location filtering: 207
- With trustworthy posted_date: 207
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
    "fetched_at": "2026-08-30T18:36:37.736785+00:00",
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
    "fetched_at": "2026-08-30T18:36:37.736785+00:00",
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
    "fetched_at": "2026-08-30T18:36:37.736785+00:00",
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
    "fetched_at": "2026-08-30T18:36:37.736785+00:00",
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
    "fetched_at": "2026-08-30T18:36:37.736785+00:00",
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
    "fetched_at": "2026-08-30T18:38:36.773272+00:00",
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
    "fetched_at": "2026-08-30T18:38:36.773272+00:00",
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
    "fetched_at": "2026-08-30T18:38:36.773272+00:00",
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
    "fetched_at": "2026-08-30T18:38:36.773272+00:00",
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
    "fetched_at": "2026-08-30T18:38:36.773272+00:00",
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
- Pages/requests fetched: 28
- Raw jobs found: 333
- After US/location filtering: 88
- With trustworthy posted_date: 88
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
    "fetched_at": "2026-08-30T18:38:37.987963+00:00",
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
    "fetched_at": "2026-08-30T18:38:37.987963+00:00",
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
    "fetched_at": "2026-08-30T18:38:37.987963+00:00",
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
    "fetched_at": "2026-08-30T18:38:37.987963+00:00",
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
    "fetched_at": "2026-08-30T18:38:37.987963+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.518428+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.518428+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.518428+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.518428+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.518428+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.830901+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.830901+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.830901+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.830901+00:00",
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
    "fetched_at": "2026-08-30T18:39:23.830901+00:00",
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
- Pages/requests fetched: 19
- Raw jobs found: 1394
- After US/location filtering: 320
- With trustworthy posted_date: 320
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074847",
    "title": "Director, Software Engineering Management",
    "location": "Santa Clara, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146344019-director-software-engineering-management",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:39:24.175307+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075074",
    "title": "Sr Staff AI Engineer - Veza",
    "location": "Minneapolis, Minnesota, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146269339-sr-staff-ai-engineer-veza",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:39:24.175307+00:00",
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
    "fetched_at": "2026-08-30T18:39:24.175307+00:00",
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
    "fetched_at": "2026-08-30T18:39:24.175307+00:00",
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
    "fetched_at": "2026-08-30T18:39:24.175307+00:00",
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
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['LinkedIn company guest search blocked with HTTP 429']

## Bloomberg

- Status: ok
- Scraping method: HTTP GET Avature SearchJobs HTML + JobDetail HTML
- Search URL/API: `https://bloomberg.avature.net/careers/SearchJobs?q=software+engineer&jobRecordsPerPage=12&jobOffset=0`
- Pagination: jobOffset=0,12,... ; stop on empty/repeat or short page
- Pages/requests fetched: 108
- Raw jobs found: 1296
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
    "fetched_at": "2026-08-30T18:41:25.498130+00:00",
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
    "fetched_at": "2026-08-30T18:41:25.498130+00:00",
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
    "fetched_at": "2026-08-30T18:41:25.498130+00:00",
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
    "fetched_at": "2026-08-30T18:41:25.498130+00:00",
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
    "fetched_at": "2026-08-30T18:41:25.498130+00:00",
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
- Pages/requests fetched: 103
- Raw jobs found: 2045
- After US/location filtering: 667
- With trustworthy posted_date: 667
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
    "fetched_at": "2026-08-30T18:44:45.177998+00:00",
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
    "fetched_at": "2026-08-30T18:44:45.177998+00:00",
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
    "fetched_at": "2026-08-30T18:44:45.177998+00:00",
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
    "fetched_at": "2026-08-30T18:44:45.177998+00:00",
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
    "fetched_at": "2026-08-30T18:44:45.177998+00:00",
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
- Pages/requests fetched: 96
- Raw jobs found: 1895
- After US/location filtering: 668
- With trustworthy posted_date: 668
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R247523",
    "title": "Senior Associate, Product Manager, Small Business Bank Fraud Decisioning",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Associate--Product-Manager--Small-Business-Bank-Fraud-Decisioning_R247523-1",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:47:13.902179+00:00",
    "date_confidence": "high",
    "description": "Senior Associate, Product Manager, Small Business Bank Fraud Decisioning Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, fin"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R249580",
    "title": "Manager, Product Manager- Move & Manage Decisioning",
    "location": "New York, NY",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/New-York-NY/Manager--Product-Manager--Move---Manage-Decisioning_R249580-1",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:47:13.902179+00:00",
    "date_confidence": "high",
    "description": "Manager, Product Manager- Move & Manage Decisioning At Capital One, we believe great products begin with a deep understanding of our customers. From our earliest days, we pioneered"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R246468",
    "title": "Manager, Product Management- Developer Experience",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Manager--Product-Management--Developer-Experience_R246468-1",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:47:13.902179+00:00",
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
    "fetched_at": "2026-08-30T18:47:13.902179+00:00",
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
    "fetched_at": "2026-08-30T18:47:13.902179+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Product Management - Developer Experience Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, finding value crea"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 100
- Raw jobs found: 1979
- After US/location filtering: 798
- With trustworthy posted_date: 798
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
    "fetched_at": "2026-08-30T18:49:18.411409+00:00",
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
    "fetched_at": "2026-08-30T18:49:18.411409+00:00",
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
    "fetched_at": "2026-08-30T18:49:18.411409+00:00",
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
    "fetched_at": "2026-08-30T18:49:18.411409+00:00",
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
    "fetched_at": "2026-08-30T18:49:18.411409+00:00",
    "date_confidence": "high",
    "description": "You will work at the intersection of distributed systems, networking, and AI infrastructure, driving architecture, design, implementation, and performance optimization across softw"
  }
]
```

## Walmart Global Tech

- Status: ok
- Scraping method: HTTP POST Walmart combined hybrid-search
- Search URL/API: `https://careers.walmart.com/api/ai/search-ai/api/v1/combined/hybrid-search`
- Pagination: page=0,1,...; size=25; bounded per query
- Pages/requests fetched: 36
- Raw jobs found: 900
- After US/location filtering: 229
- With trustworthy posted_date: 229
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Walmart Global Tech",
    "source": "walmart_official_careers",
    "job_id": "R-2451270",
    "title": "Distinguished, Software Engineer -AI/ML Engineer – Agentic Systems",
    "location": "SUNNYVALE, CA, US",
    "official_url": "https://careers.walmart.com/job/R-2451270",
    "posted_date": "2026-03-19",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:52:12.641172+00:00",
    "date_confidence": "high",
    "description": "Job Posting Title: Distinguished, Software Engineer -AI/ML Engineer – Agentic Systems Job Posting Description: Position Summary... What you'll do... As a Distinguished AI/ML Engine"
  },
  {
    "company": "Walmart Global Tech",
    "source": "walmart_official_careers",
    "job_id": "R-2533229",
    "title": "(USA) Distinguished, Software Engineer-AI/ML Engineer - Agentic Systems & Site Reliability Engineering",
    "location": "SUNNYVALE, CA, US",
    "official_url": "https://careers.walmart.com/job/R-2533229",
    "posted_date": "2026-06-25",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:52:12.641172+00:00",
    "date_confidence": "high",
    "description": "Job Posting Title: (USA) Distinguished, Software Engineer-AI/ML Engineer - Agentic Systems & Site Reliability Engineering Job Summary: As a Distinguished AI/ML Engineer within Walm"
  },
  {
    "company": "Walmart Global Tech",
    "source": "walmart_official_careers",
    "job_id": "R-2445762",
    "title": "Software Engineer III– AI Systems",
    "location": "BENTONVILLE, AR, US",
    "official_url": "https://careers.walmart.com/job/R-2445762",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:52:12.641172+00:00",
    "date_confidence": "high",
    "description": "Job Posting Title: Software Engineer III– AI Systems Job Summary: We’re seeking a Software Engineer to design and build AI-first systems with a focus on agentic AI, high performanc"
  },
  {
    "company": "Walmart Global Tech",
    "source": "walmart_official_careers",
    "job_id": "R-2590928",
    "title": "Staff, Software Engineer - Gen AI / Backend",
    "location": "SUNNYVALE, CA, US",
    "official_url": "https://careers.walmart.com/job/R-2590928",
    "posted_date": "2026-08-13",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:52:12.641172+00:00",
    "date_confidence": "high",
    "description": "Job Posting Title: Staff, Software Engineer - Gen AI / Backend Job Posting Description: Position Summary... What you'll do... Role summary: The (USA) Staff, Software Engineer plays"
  },
  {
    "company": "Walmart Global Tech",
    "source": "walmart_official_careers",
    "job_id": "R-2610003",
    "title": "Principal, Software Engineer",
    "location": "SUNNYVALE, CA, US",
    "official_url": "https://careers.walmart.com/job/R-2610003",
    "posted_date": "2026-08-20",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:52:12.641172+00:00",
    "date_confidence": "high",
    "description": "Job Posting Title: Principal, Software Engineer Job Posting Description: Position Summary... What you'll do... Role summary: The Principal Software Engineer leads platform engineer"
  }
]
```

## Cisco

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cisco.wd5.myworkdayjobs.com/Cisco_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 72
- Raw jobs found: 1425
- After US/location filtering: 245
- With trustworthy posted_date: 245
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2004763",
    "title": "Hardware Systems Engineering Technical Leader",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Hardware-Systems-Engineering-Technical-Lead---Milpitas-San-Jose--CA_2004763",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:53:11.959386+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/29/2026 This is an onsite position and requires the employee to work out the Milpitas, CA location. Meet the Team The Common Hard"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2013117",
    "title": "Hardware Design Engineer",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Hardware-Design-Engineer_2013117",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-30T18:53:11.959386+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/29/2026 This role requires the employee to work onsite at the San Jose, CA office location. Meet the Team The Common Hardware Gro"
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
    "fetched_at": "2026-08-30T18:53:11.959386+00:00",
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
    "fetched_at": "2026-08-30T18:53:11.959386+00:00",
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
    "fetched_at": "2026-08-30T18:53:11.959386+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/24/2026 The successful applicant will be performing work on US Government classified environments, and therefore, must be a U.S. "
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 60
- Raw jobs found: 1408
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
    "fetched_at": "2026-08-30T18:55:09.872567+00:00",
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
    "fetched_at": "2026-08-30T18:55:09.872567+00:00",
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
    "fetched_at": "2026-08-30T18:55:09.872567+00:00",
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
    "fetched_at": "2026-08-30T18:55:09.872567+00:00",
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
    "fetched_at": "2026-08-30T18:55:09.872567+00:00",
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
- Pages/requests fetched: 84
- Raw jobs found: 1585
- After US/location filtering: 301
- With trustworthy posted_date: 301
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
    "fetched_at": "2026-08-30T18:56:54.488624+00:00",
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
    "fetched_at": "2026-08-30T18:56:54.488624+00:00",
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
    "fetched_at": "2026-08-30T18:56:54.488624+00:00",
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
    "fetched_at": "2026-08-30T18:56:54.488624+00:00",
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
    "fetched_at": "2026-08-30T18:56:54.488624+00:00",
    "date_confidence": "high",
    "description": "AI Ops Engineer This role has been designed as 'Hybrid' with a requirement that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Packard Enterprise "
  }
]
```

## Disney

- Status: ok
- Scraping method: HTTP GET Disney server-rendered US search results
- Search URL/API: `https://www.disneycareers.com/en/search-jobs/software%20engineer/United%20States/391/1/2/6252001/39x76/-98x5/100/2`
- Pagination: ?p=1,2,3 per role query (intentional request cap)
- Pages/requests fetched: 27
- Raw jobs found: 270
- After US/location filtering: 130
- With trustworthy posted_date: 0
- Errors/403s: none

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
    "fetched_at": "2026-08-30T19:00:34.728400+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10146000",
    "title": "Lead Frontend Software Engineer - AI Assisted Engineering Practices",
    "location": "Celebration, Florida",
    "official_url": "https://www.disneycareers.com/en/job/celebration/lead-frontend-software-engineer-ai-assisted-engineering-practices/391/94498288272",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:00:34.728400+00:00",
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
    "fetched_at": "2026-08-30T19:00:34.728400+00:00",
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
    "fetched_at": "2026-08-30T19:00:34.728400+00:00",
    "date_confidence": "high",
    "description": ""
  },
  {
    "company": "Disney",
    "source": "disney_official_careers",
    "job_id": "10157864",
    "title": "Director, Software Engineering",
    "location": "Glendale, California / Orlando, Florida",
    "official_url": "https://www.disneycareers.com/en/job/glendale/director-software-engineering/391/99718739296",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:00:34.728400+00:00",
    "date_confidence": "high",
    "description": ""
  }
]
```

## eBay

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Phenom renders results through a site-specific /widgets payload; keep the verified official link instead of adding brittle browser emulation.']

## Qualcomm

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://careers.qualcomm.com/api/pcsx/search?domain=qualcomm.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: start=0,10,20,... ; num=10 (API cap); stop on empty/repeat or count
- Pages/requests fetched: 26
- Raw jobs found: 255
- After US/location filtering: 115
- With trustworthy posted_date: 115
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3080335",
    "title": "Mixed Signal SVE Engineer",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446715137477",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:00:58.142085+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > ASICS Engineering General Summary: Qualcomm is a company of inventors that unlocked 5G - usher"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3091566",
    "title": "CPU RTL/AI Micro-Architect - AI Development",
    "location": "Austin, Texas, United States of America; Santa Clara, CA, USA",
    "official_url": "https://careers.qualcomm.com/careers/job/446718779461",
    "posted_date": "2026-08-30",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:00:58.142085+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > CPU Engineering General Summary: Qualcomm is a company of inventors pushing the boundaries of "
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095336",
    "title": "Wireless Software Engineer",
    "location": "Santa Clara, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720729799",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:00:58.142085+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Atheros, Inc. Job Area: Engineering Group, Engineering Group > Systems Test Engineering General Summary: ** This position is not eligible for Qualcomm immigration"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095794",
    "title": "Staff Program Manager, Camera Processors Software",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720810805",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:00:58.142085+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Services Group, Engineering Services Group > Program Management General Summary: Develops, defines, and executes plans of"
  },
  {
    "company": "Qualcomm",
    "source": "qualcomm_official_careers",
    "job_id": "3095893",
    "title": "Modem RF Software Integration and Test Engineer (Automation /AI/ML)",
    "location": "San Diego, California, United States of America",
    "official_url": "https://careers.qualcomm.com/careers/job/446720834667",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:00:58.142085+00:00",
    "date_confidence": "high",
    "description": "Company: Qualcomm Technologies, Inc. Job Area: Engineering Group, Engineering Group > Cellular System Test Engineering General Summary: As a Modem RFSW Integration & Test Engineer "
  }
]
```

## AMD

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · careers.amd.com returns HTTP 403 to anonymous automation; keep the verified official search link.']

## Zoom

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://zoom.wd5.myworkdayjobs.com/Zoom`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 21
- Raw jobs found: 239
- After US/location filtering: 48
- With trustworthy posted_date: 48
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
    "fetched_at": "2026-08-30T19:01:57.316003+00:00",
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
    "fetched_at": "2026-08-30T19:01:57.316003+00:00",
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
    "fetched_at": "2026-08-30T19:01:57.316003+00:00",
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
    "fetched_at": "2026-08-30T19:01:57.316003+00:00",
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
    "fetched_at": "2026-08-30T19:01:57.316003+00:00",
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
- Errors/403s: ['Tier B · higher.gs.com uses a custom GraphQL schema; keep the verified official link until a stable filtered role-search query is available.']

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
    "fetched_at": "2026-08-30T19:02:34.356124+00:00",
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
    "fetched_at": "2026-08-30T19:02:34.356124+00:00",
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
    "fetched_at": "2026-08-30T19:02:34.356124+00:00",
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
    "fetched_at": "2026-08-30T19:02:34.356124+00:00",
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
    "fetched_at": "2026-08-30T19:02:34.356124+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.046373+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.046373+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.046373+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.046373+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.046373+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.971114+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.971114+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.971114+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.971114+00:00",
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
    "fetched_at": "2026-08-30T19:02:35.971114+00:00",
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
- Raw jobs found: 170
- After US/location filtering: 97
- With trustworthy posted_date: 97
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
    "fetched_at": "2026-08-30T19:02:36.297688+00:00",
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
    "fetched_at": "2026-08-30T19:02:36.297688+00:00",
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
    "fetched_at": "2026-08-30T19:02:36.297688+00:00",
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
    "fetched_at": "2026-08-30T19:02:36.297688+00:00",
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
    "fetched_at": "2026-08-30T19:02:36.297688+00:00",
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
- Raw jobs found: 571
- After US/location filtering: 453
- With trustworthy posted_date: 453
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
    "fetched_at": "2026-08-30T19:02:36.530760+00:00",
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
    "fetched_at": "2026-08-30T19:02:36.530760+00:00",
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
    "fetched_at": "2026-08-30T19:02:36.530760+00:00",
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
    "fetched_at": "2026-08-30T19:02:36.530760+00:00",
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
    "fetched_at": "2026-08-30T19:02:36.530760+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><h2><strong>About Anthropic</strong></h2> <p>Anthropic’s mission is to create reliable, interpretable, and steerable AI systems. We want AI to be safe an"
  }
]
```

## AppLovin

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · High-value engineering employer; page loads job listings dynamically; inspect XHR.']

## ByteDance

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · High-value; likely shares patterns with TikTok but treat search surface separately until verified.']

## Chime

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · High-value fintech; official search supports keyword/team/location filters.']

## Citadel

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
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
- Raw jobs found: 41
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
    "fetched_at": "2026-08-30T19:02:37.493259+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.493259+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.493259+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.493259+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.493259+00:00",
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
- Raw jobs found: 123
- After US/location filtering: 107
- With trustworthy posted_date: 107
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
    "fetched_at": "2026-08-30T19:02:37.622823+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.622823+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.622823+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.622823+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.622823+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><strong>We're transforming the grocery industry</strong></p> <p><span class=\"im\">At Instacart, we invite the world to share love through food because "
  }
]
```

## Intel

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Large engineering employer; inspect ATS, filter US software.']

## MathWorks

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
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
- Raw jobs found: 407
- After US/location filtering: 260
- With trustworthy posted_date: 260
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7318466",
    "title": "Account Development Representative",
    "location": "Bengaluru; Bengaluru, Karnataka, India",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7318466",
    "posted_date": "2026-07-22",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-30T19:02:37.823533+00:00",
    "date_confidence": "high",
    "description": "<p>An Account Development Representative at MongoDB is the starting point for building a serious career in technology sales.&nbsp;</p> <p>This role is the foundation of our sales o"
  },
  {
    "company": "MongoDB",
    "source": "mongodb_official_careers",
    "job_id": "7318558",
    "title": "Account Development Representative",
    "location": "Gurugram; Gurugram, Haryana, India",
    "official_url": "https://www.mongodb.com/careers/job/?gh_jid=7318558",
    "posted_date": "2026-07-27",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-30T19:02:37.823533+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.823533+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.823533+00:00",
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
    "fetched_at": "2026-08-30T19:02:37.823533+00:00",
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
    "fetched_at": "2026-08-30T19:02:38.262173+00:00",
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
    "fetched_at": "2026-08-30T19:02:38.262173+00:00",
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
    "fetched_at": "2026-08-30T19:02:38.262173+00:00",
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
    "fetched_at": "2026-08-30T19:02:38.262173+00:00",
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
    "fetched_at": "2026-08-30T19:02:38.262173+00:00",
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
- Raw jobs found: 307
- After US/location filtering: 240
- With trustworthy posted_date: 240
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
    "fetched_at": "2026-08-30T19:02:38.875026+00:00",
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
    "fetched_at": "2026-08-30T19:02:38.875026+00:00",
    "date_confidence": "high",
    "description": "Own calendar management and deconfliction across multiple workstream leads — onsites, supplier visits, internal syncs, and Navy stakeholder meetings Schedule and track supplier eng"
  },
  {
    "company": "Palantir",
    "source": "palantir_official_careers",
    "job_id": "0ccbe620-a3ef-41d1-a5c4-68e56b3c91d0",
    "title": "American Tech Fellowship",
    "location": "North America",
    "official_url": "https://jobs.lever.co/palantir/0ccbe620-a3ef-41d1-a5c4-68e56b3c91d0",
    "posted_date": "2025-06-17",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:02:38.875026+00:00",
    "date_confidence": "high",
    "description": ""
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
    "fetched_at": "2026-08-30T19:02:38.875026+00:00",
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
    "fetched_at": "2026-08-30T19:02:38.875026+00:00",
    "date_confidence": "high",
    "description": "Build for high-scale, collaborative, geospatial workflows ( Gaia ) Design sophisticated frameworks to enable complex workflows across applications in a single workspace Develop the"
  }
]
```

## PayPal

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
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
- Raw jobs found: 153
- After US/location filtering: 135
- With trustworthy posted_date: 135
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
    "fetched_at": "2026-08-30T19:02:40.506702+00:00",
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
    "updated_date": "2026-08-30",
    "fetched_at": "2026-08-30T19:02:40.506702+00:00",
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
    "fetched_at": "2026-08-30T19:02:40.506702+00:00",
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
    "fetched_at": "2026-08-30T19:02:40.506702+00:00",
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
    "updated_date": "2026-08-30",
    "fetched_at": "2026-08-30T19:02:40.506702+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><div class=\"c-message_kit__blocks c-message_kit__blocks--rich_text\"> <div class=\"c-message__message_blocks c-message__message_blocks--rich_text\" data-qa="
  }
]
```

## Red Hat

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong software/platform employer; inspect underlying ATS.']

## Roku

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong SWE hiring; structured search page, inspect API.']

## Block / Square

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/block/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Raw jobs found: 193
- After US/location filtering: 182
- With trustworthy posted_date: 182
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
    "fetched_at": "2026-08-30T19:02:40.776865+00:00",
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
    "fetched_at": "2026-08-30T19:02:40.776865+00:00",
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
    "fetched_at": "2026-08-30T19:02:40.776865+00:00",
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
    "fetched_at": "2026-08-30T19:02:40.776865+00:00",
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
    "fetched_at": "2026-08-30T19:02:40.776865+00:00",
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
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · High-value SWE/quant; identify direct openings/search endpoint.']

## Verkada

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong SWE/AI/hardware-software employer; inspect job board.']

## Visa

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Large technology org; identify direct search backend.']

## WeRide

- Status: ok
- Scraping method: HTTP GET Lever /v0/postings/{token}?mode=json
- Search URL/API: `https://api.lever.co/v0/postings/weride`
- Pagination: single JSON payload
- Pages/requests fetched: 1
- Raw jobs found: 30
- After US/location filtering: 23
- With trustworthy posted_date: 23
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
    "fetched_at": "2026-08-30T19:02:41.147905+00:00",
    "date_confidence": "high",
    "description": "Role Responsibilities: System Bringup & Deployment Deploy and integrate autonomous driving software onto vehicle platforms and embedded computing systems. Validate system functiona"
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
    "fetched_at": "2026-08-30T19:02:41.147905+00:00",
    "date_confidence": "high",
    "description": "Thoroughly understand how our self-driving technology works. Stay on top of countless daily changes, both big and small. Safely operate test vehicles for up to 8 hours a day to eva"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "8b43a662-fd58-45e0-9087-36c00ed82ff7",
    "title": "Data Annotator",
    "location": "Bangsar South, Kuala Lumpur",
    "official_url": "https://jobs.lever.co/weride/8b43a662-fd58-45e0-9087-36c00ed82ff7",
    "posted_date": "2025-12-21",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:02:41.147905+00:00",
    "date_confidence": "high",
    "description": "Accurately label and categorize large datasets, including text, audio, images, and video. Review and correct data annotations to ensure quality and consistency. Work closely with t"
  },
  {
    "company": "WeRide",
    "source": "weride_official_careers",
    "job_id": "3da6e841-eac2-4dd7-8fa9-934c42f63d1f",
    "title": "Driving Safety Operator - Singapore",
    "location": "One-north",
    "official_url": "https://jobs.lever.co/weride/3da6e841-eac2-4dd7-8fa9-934c42f63d1f",
    "posted_date": "2024-12-11",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:02:41.147905+00:00",
    "date_confidence": "high",
    "description": "Operational Oversight: Sit in the driver’s seat, ready to take control of the autonomous vehicle at any moment, ensuring the safety of all passengers, road users, and the vehicle. "
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
    "fetched_at": "2026-08-30T19:02:41.147905+00:00",
    "date_confidence": "high",
    "description": "Act as a frontline technical owner for the deployment and operation of L4 autonomous driving systems in real-world environments Lead and execute system-level testing and validation"
  }
]
```

## Workday

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong enterprise SWE employer; identify its external recruiting site.']

## Zillow

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong product/software hiring; locate direct search feed.']

## Zscaler

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier A · Strong cloud/security software employer; inspect search backend.']

## Chewy

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Worth adding if generic ATS; good SWE volume.']

## CVS Health

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Large employer; lower SWE density, implement only if cheap.']

## Duolingo

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · High-quality but smaller volume; implement if ATS is easy.']

## Equinix

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Good infra/software relevance; inspect ATS.']

## F5

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Good systems/security relevance; implement if generic.']

## IXL Learning

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier B · Relevant SWE employer; smaller volume, easy-only.']

## Wayfair

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
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
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Interesting SWE roles but lower volume; easy-only.']

## Flex

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Lower SWE signal; easy-only.']

## IQVIA

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Large but mixed roles; easy-only with software filters.']

## Johnson & Johnson

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Large mixed-role employer; only if generic and cheap.']

## Nasdaq

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Some strong tech roles but lower volume; easy-only.']

## PointClickCare

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Relevant SaaS/healthtech; easy-only.']

## Stryker

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Mixed hardware/software; lower priority.']

## TransUnion

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://transunion.wd5.myworkdayjobs.com/TransUnion`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 26
- Raw jobs found: 291
- After US/location filtering: 63
- With trustworthy posted_date: 63
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19041664",
    "title": "Advisor -AI Security Engineer",
    "location": "Bengaluru",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Bengaluru/Advisor--AI-Security-Engineer_19041664",
    "posted_date": "2026-08-17",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:02:41.257555+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Team Overview At TransUnion, we have a welcoming and energetic environment that encourages collaboration and innovation – we’re consistent"
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19042097",
    "title": "AI Research & Innovation Lead",
    "location": "Chicago, Illinois",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Chicago-Illinois/AI-Research---Innovation-Lead_19042097",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:02:41.257555+00:00",
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
    "fetched_at": "2026-08-30T19:02:41.257555+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The Global Infrastructure, Engineering & Operations (GIO) organization "
  },
  {
    "company": "TransUnion",
    "source": "transunion_official_careers",
    "job_id": "19041566",
    "title": "Data Engineer",
    "location": "Bengaluru",
    "official_url": "https://transunion.wd5.myworkdayjobs.com/TransUnion/job/Bengaluru/Data-Engineer_19041566",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-30T19:02:41.257555+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Team Overview The Argus Data Engineering Team, part of the Global Technology (GT) organization, is responsible for designing, developing, "
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
    "fetched_at": "2026-08-30T19:02:41.257555+00:00",
    "date_confidence": "high",
    "description": "TransUnion's Job Applicant Privacy Notice Personal Information We Collect Your Privacy Choices Team Overview The Global Infrastructure, Engineering & Operations (GIO) organization "
  }
]
```

## Travelers

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Mixed-role employer; easy-only.']

## Verizon

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Large tech org but noisy; easy-only.']

## Yext

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Tier C · Relevant SaaS; smaller hiring volume, easy-only.']
