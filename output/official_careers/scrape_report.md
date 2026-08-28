# Official careers scrape report — 2026-08-28_1442

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Software+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or advertised total
- Pages/requests fetched: 30
- Raw jobs found: 586
- After US/location filtering: 332
- With trustworthy posted_date: 332
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "101599343911281350",
    "title": "Software Engineer III, Infrastructure, Infra Bigtable",
    "location": "New York, NY, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/101599343911281350-software-engineer-iii-infrastructure-infra-bigtable",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:23.197758+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "123776167026008774",
    "title": "Senior Software Engineer, XR, Platforms and Devices",
    "location": "San Jose, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/123776167026008774-senior-software-engineer-xr-platforms-and-devices",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:23.197758+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "141965593505866438",
    "title": "Software Engineer III, Cloud Security, Identity and Access Management",
    "location": "San Francisco, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/141965593505866438-software-engineer-iii-cloud-security-identity-and-access-management",
    "posted_date": "2026-06-19",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:23.197758+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "120397962646823622",
    "title": "Senior Software Engineer, Engineering Productivity, Cloud Learning Services",
    "location": "Boulder, CO, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/120397962646823622-senior-software-engineer-engineering-productivity-cloud-learning-services",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:23.197758+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "81105770019463878",
    "title": "Software Engineer III, Google Distributed Cloud AI Storage",
    "location": "Sunnyvale, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/81105770019463878-software-engineer-iii-google-distributed-cloud-ai-storage",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:23.197758+00:00",
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
- Pages/requests fetched: 102
- Raw jobs found: 2036
- After US/location filtering: 1206
- With trustworthy posted_date: 1206
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10517605",
    "title": "Sr. Technical Full Life Cycle Recruiter, Amazon Stores",
    "location": "New York, New York, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10517605/sr-technical-full-life-cycle-recruiter-amazon-stores",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:41.520405+00:00",
    "date_confidence": "high",
    "description": "Amazon's mission is to be Earth's most customer-centric company and to get there, customer obsessed, talented, and driven individuals are needed. Americas Stores Tech Talent Acquis"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10517567",
    "title": "Software Development Engineer Intern, Annapurna Labs - 2027",
    "location": "Cupertino, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10517567/software-development-engineer-intern-annapurna-labs-2027",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:41.520405+00:00",
    "date_confidence": "high",
    "description": "At Amazon, our tech isn't just a tool, it's your playground. Our engineers work on scalable systems, cloud services, and customer-facing products that operate at global scale. This"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10517532",
    "title": "Forward Deployed Engineering Manager, AWS Forward Deployed Engineering",
    "location": "New York, New York, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10517532/forward-deployed-engineering-manager-aws-forward-deployed-engineering",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:41.520405+00:00",
    "date_confidence": "high",
    "description": "A Forward Deployed Engineering Manager (FDE Manager) leads a pod of FDEs embedded within strategic enterprise customers, owning delivery execution, engineering quality, and team de"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10517535",
    "title": "ASIC Engineer Intern, Annapurna Labs - 2027",
    "location": "Cupertino, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10517535/asic-engineer-intern-annapurna-labs-2027",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:41.520405+00:00",
    "date_confidence": "high",
    "description": "At Amazon, our tech isn't just a tool, it's your playground. Our engineers work on scalable systems, cloud services, and customer-facing products that operate at global scale. This"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10517149",
    "title": "Robotics - Software Development Engineer Fall Intern/Co-op - 2026",
    "location": "Westboro, Wisconsin, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10517149/robotics-software-development-engineer-fall-intern-co-op-2026",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-28T14:42:41.520405+00:00",
    "date_confidence": "high",
    "description": "Do you want to solve real customer problems through innovative technology? Do you enjoy working on scalable services in a collaborative team environment? Do you want to see your co"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=software+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or totalRecords
- Pages/requests fetched: 127
- Raw jobs found: 2537
- After US/location filtering: 1483
- With trustworthy posted_date: 1483
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680542-3956",
    "title": "ASIC Design Engineer — Pixel IP",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680542/asic-design-engineer-pixel-ip",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:43:47.799812+00:00",
    "date_confidence": "high",
    "description": "Do you love creating elegant solutions to highly complex challenges? As part of our Hardware Technologies group, you’ll help design our next-generation, high-performance, power-eff"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680547-3956",
    "title": "ASIC Design Engineer — Pixel IP",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680547/asic-design-engineer-pixel-ip",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:43:47.799812+00:00",
    "date_confidence": "high",
    "description": "Do you love creating elegant solutions to highly complex challenges? As part of our Hardware Technologies group, you’ll help design our next-generation, high-performance, power-eff"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680548-3956",
    "title": "ASIC Design Engineer — Pixel IP",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680548/asic-design-engineer-pixel-ip",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:43:47.799812+00:00",
    "date_confidence": "high",
    "description": "Do you love creating elegant solutions to highly complex challenges? As part of our Hardware Technologies group, you’ll help design our next-generation, high-performance, power-eff"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680522-0836",
    "title": "Modeling & Simulation Engineer",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680522/modeling-simulation-engineer",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:43:47.799812+00:00",
    "date_confidence": "high",
    "description": "Apple is a place where extraordinary people team up to do their best work. Together we build products and experiences people once couldn't have envisioned - and now can't imagine l"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680331-0836",
    "title": "Software Quality Test Manager, Sensing & Connectivity",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680331/software-quality-test-manager-sensing-connectivity",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:43:47.799812+00:00",
    "date_confidence": "high",
    "description": "Join the Sensing and Connectivity - Location Context team that powers critical experiences in Apple products. Our team works on providing personalized insights from users' daily pa"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: start=0,10,20,... ; num=10 (API cap); stop on empty/repeat or count
- Pages/requests fetched: 82
- Raw jobs found: 808
- After US/location filtering: 604
- With trustworthy posted_date: 604
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200043510",
    "title": "Senior Silicon Engineer",
    "location": "United States, California, Santa Clara",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556933263",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:45:19.153904+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200045266",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556943806",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:45:19.153904+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft’s Azure Data engineering team is leading the transformation of analytics in the world of data with products like databases, data integration, big data analytics,"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200044674",
    "title": "Principal Azure Customer Engineer (ACE) Manager",
    "location": "United States, Georgia, Atlanta",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556941526",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:45:19.153904+00:00",
    "date_confidence": "high",
    "description": "Overview Are you interested in working for one of the most exciting teams in Microsoft, relentlessly focused on customer needs and advancing Microsoft's cloud first strategy? Inter"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200050042",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556978134",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:45:19.153904+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Rewards is Microsoft's loyalty platform that powers engagement experiences across Bing, Edge, Xbox, Microsoft Store, and other Microsoft products. We are seeking"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200027347",
    "title": "Principal Software Engineer (CoreAI)",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556754609",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:45:19.153904+00:00",
    "date_confidence": "high",
    "description": "Overview Join the team building the future of AI at Microsoft. Are you passionate about creating the next generation of Agent Building experiences? The Microsoft Foundry team withi"
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 68
- Raw jobs found: 1307
- After US/location filtering: 1082
- With trustworthy posted_date: 1082
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
    "fetched_at": "2026-08-28T14:47:31.745110+00:00",
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
    "fetched_at": "2026-08-28T14:47:31.745110+00:00",
    "date_confidence": "high",
    "description": "In this role, you will own the enterprise platforms that enable the development, deployment, operation, and scaling of AI agents and GPU-accelerated workloads for NVIDIA employees."
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2024363",
    "title": "Principal Software Engineer",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Principal-Software-Engineer_JR2024363",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:47:31.745110+00:00",
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
    "fetched_at": "2026-08-28T14:47:31.745110+00:00",
    "date_confidence": "high",
    "description": "At NVIDIA, we are redefining the future of technology, and our Senior Software Engineer, Networking role offers a uniquely ambitious opportunity to contribute to world-class innova"
  },
  {
    "company": "NVIDIA",
    "source": "nvidia_official_careers",
    "job_id": "JR2018245",
    "title": "Senior Software Engineer, Security",
    "location": "US, CA, Santa Clara",
    "official_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Security-Architect_JR2018245",
    "posted_date": "2026-08-16",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:47:31.745110+00:00",
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
- Pages/requests fetched: 34
- Raw jobs found: 612
- After US/location filtering: 244
- With trustworthy posted_date: 244
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357991",
    "title": "Associate Data Scientist — AI Strategy & Governance",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Associate-Data-Scientist---AI-Strategy---Governance_JR357991",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:51:01.145525+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. About Futureforce University Rec"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR347097",
    "title": "SMB Account Executive - Data Foundation (Informatica + MuleSoft)",
    "location": "New York - New York",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/New-York---New-York/SMB-Account-Executive-Data-Foundations--Informatica---MuleSoft-_JR347097",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:51:01.145525+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR347125",
    "title": "SMB Account Executive Data Foundation (Informatica + MuleSoft)",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/SMB-Account-Executive-Data-Foundations--Informatica---MuleSoft-_JR347125",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:51:01.145525+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR354027",
    "title": "Principal Data Platform Engineer",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Principal-Data-Platform-Engineer_JR354027",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:51:01.145525+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR340771",
    "title": "Summer 2027 Intern - Software Engineer",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Summer-2027-Intern---Software-Engineer_JR340771-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:51:01.145525+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. About Futureforce University Rec"
  }
]
```

## Adobe

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://adobe.wd5.myworkdayjobs.com/external_experienced`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 24
- Raw jobs found: 418
- After US/location filtering: 312
- With trustworthy posted_date: 312
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
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:53:30.550310+00:00",
    "date_confidence": "medium",
    "description": ""
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
    "fetched_at": "2026-08-28T14:53:30.550310+00:00",
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
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:53:30.550310+00:00",
    "date_confidence": "medium",
    "description": ""
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R170546",
    "title": "Senior Software Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Senior-Software-Engineer_R170546-1",
    "posted_date": "2026-07-23",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:53:30.550310+00:00",
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
    "fetched_at": "2026-08-28T14:53:30.550310+00:00",
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
- Pages/requests fetched: 11
- Raw jobs found: 201
- After US/location filtering: 139
- With trustworthy posted_date: 139
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
    "fetched_at": "2026-08-28T14:56:06.859113+00:00",
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
    "fetched_at": "2026-08-28T14:56:06.859113+00:00",
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
    "fetched_at": "2026-08-28T14:56:06.859113+00:00",
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
    "fetched_at": "2026-08-28T14:56:06.859113+00:00",
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
    "fetched_at": "2026-08-28T14:56:06.859113+00:00",
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
- Raw jobs found: 473
- After US/location filtering: 469
- With trustworthy posted_date: 469
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
    "fetched_at": "2026-08-28T14:57:07.828469+00:00",
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
    "fetched_at": "2026-08-28T14:57:07.828469+00:00",
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
    "fetched_at": "2026-08-28T14:57:07.828469+00:00",
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
    "fetched_at": "2026-08-28T14:57:07.828469+00:00",
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
    "fetched_at": "2026-08-28T14:57:07.828469+00:00",
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
- Pages/requests fetched: 8
- Raw jobs found: 88
- After US/location filtering: 58
- With trustworthy posted_date: 58
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "H226EM8",
    "title": "Manager, Software Engineering",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Manager--Software-Engineering_H226EM8-1",
    "posted_date": "2026-07-09",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:57:08.837523+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "H226PE10",
    "title": "Principal Software Engineer",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Principal-Software-Engineer_H226PE10",
    "posted_date": "2026-07-21",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:57:08.837523+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "R0046369",
    "title": "Manager, Software Engineering, Maps",
    "location": "New York, New York",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/New-York-New-York/Manager--Software-Engineering--Maps_R0046369-1",
    "posted_date": "2026-08-04",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:57:08.837523+00:00",
    "date_confidence": "high",
    "description": "Snap Inc is a technology company. We believe the camera presents the greatest opportunity to improve the way people live and communicate. Snap contributes to human progress by empo"
  },
  {
    "company": "Snap",
    "source": "snap_official_careers",
    "job_id": "Q326SWE",
    "title": "Software Engineer, Level 3",
    "location": "Los Angeles, California",
    "official_url": "https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Software-Engineer--Level-3_Q326SWE-1",
    "posted_date": "2026-08-18",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:57:08.837523+00:00",
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
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:57:08.837523+00:00",
    "date_confidence": "medium",
    "description": ""
  }
]
```

## Pinterest

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/pinterest/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Raw jobs found: 214
- After US/location filtering: 164
- With trustworthy posted_date: 164
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
    "fetched_at": "2026-08-28T14:57:35.367721+00:00",
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
    "fetched_at": "2026-08-28T14:57:35.367721+00:00",
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
    "fetched_at": "2026-08-28T14:57:35.367721+00:00",
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
    "fetched_at": "2026-08-28T14:57:35.367721+00:00",
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
    "fetched_at": "2026-08-28T14:57:35.367721+00:00",
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
- Raw jobs found: 387
- After US/location filtering: 301
- With trustworthy posted_date: 301
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
    "fetched_at": "2026-08-28T14:57:35.669553+00:00",
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
    "fetched_at": "2026-08-28T14:57:35.669553+00:00",
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
    "fetched_at": "2026-08-28T14:57:35.669553+00:00",
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
    "fetched_at": "2026-08-28T14:57:35.669553+00:00",
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
    "fetched_at": "2026-08-28T14:57:35.669553+00:00",
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
- Raw jobs found: 263
- After US/location filtering: 193
- With trustworthy posted_date: 193
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074990",
    "title": "Senior Reliability Engineer",
    "location": "Minneapolis, Minnesota, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146080839-senior-reliability-engineer",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:57:36.007440+00:00",
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
    "fetched_at": "2026-08-28T14:57:36.007440+00:00",
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
    "fetched_at": "2026-08-28T14:57:36.007440+00:00",
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
    "fetched_at": "2026-08-28T14:57:36.007440+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074969",
    "title": "Senior Staff Data Platform Engineer - Data Access Team",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146075479-senior-staff-data-platform-engineer-data-access-team",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:57:36.007440+00:00",
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
- Pages/requests fetched: 64
- Raw jobs found: 756
- After US/location filtering: 213
- With trustworthy posted_date: 0
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21249",
    "title": "TOP & Today Editor - Los Angeles",
    "location": "Los Angeles, California, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/TOP-Today-Editor-Los-Angeles/21249",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:59:22.813639+00:00",
    "date_confidence": "unknown",
    "description": "TOP & Today Editor - Los Angeles"
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
    "fetched_at": "2026-08-28T14:59:22.813639+00:00",
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
    "fetched_at": "2026-08-28T14:59:22.813639+00:00",
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
    "fetched_at": "2026-08-28T14:59:22.813639+00:00",
    "date_confidence": "unknown",
    "description": "Senior Data Management Professional - Company Financial Market Data"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21638",
    "title": "Vertical Video Producer/Editor, Bloomberg Opinion – 12 Month Contract",
    "location": "Washington, District of Columbia, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Vertical-Video-Producer-Editor-Bloomberg-Opinion-12-Month-Contract/21638",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-28T14:59:22.813639+00:00",
    "date_confidence": "unknown",
    "description": "Vertical Video Producer/Editor, Bloomberg Opinion – 12 Month Contract"
  }
]
```

## JPMorgan Chase

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 100
- Raw jobs found: 1999
- After US/location filtering: 951
- With trustworthy posted_date: 951
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
    "fetched_at": "2026-08-28T15:04:06.966375+00:00",
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
    "fetched_at": "2026-08-28T15:04:06.966375+00:00",
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
    "fetched_at": "2026-08-28T15:04:06.966375+00:00",
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
    "fetched_at": "2026-08-28T15:04:06.966375+00:00",
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
    "fetched_at": "2026-08-28T15:04:06.966375+00:00",
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
- Pages/requests fetched: 69
- Raw jobs found: 1355
- After US/location filtering: 959
- With trustworthy posted_date: 958
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R246832",
    "title": "Staff Software Engineer, Full Stack (Remote Eligible)",
    "location": "Cambridge, MA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Cambridge-MA/Distinguished-Engineer--Back-End--Remote-Eligibe-_R246832-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:06:38.228869+00:00",
    "date_confidence": "high",
    "description": "Staff Software Engineer, Full Stack (Remote Eligible) As a Staff Software Engineer at Capital One, you will be a part of a community of technical experts working to define the futu"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999218",
    "title": "Lead Software Engineer, Server-Driven UI (SDUI) platform",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Lead-Software-Engineer--Server-Driven-UI--SDUI--platform_R999218-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:06:38.228869+00:00",
    "date_confidence": "high",
    "description": "Lead Software Engineer, Server-Driven UI (SDUI) platform Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R248338",
    "title": "Sr. Business Analyst - US Card",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Sr-Business-Analyst---US-Card_R248338-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:06:38.228869+00:00",
    "date_confidence": "high",
    "description": "Sr. Business Analyst - US Card Summary: As a Senior Business Analyst at Capital One, you will apply your strategic and analytical skills to major company challenges. You will team "
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R246011",
    "title": "Business Manager-Customer Experience",
    "location": "Chicago, IL",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Chicago-IL/Business-Manager-Customer-Experience_R246011-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:06:38.228869+00:00",
    "date_confidence": "high",
    "description": "Business Manager-Customer Experience Summary: As a Business Analysis Manager at Capital One, you will apply your strategic and analytical skills to major company challenges. You'll"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R235046",
    "title": "Director, Staff Engineer - Marketing & Sales",
    "location": "Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Richmond-VA/Distinguished-Engineer_R235046",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:06:38.228869+00:00",
    "date_confidence": "high",
    "description": "Director, Staff Engineer - Marketing & Sales As a Director, Staff Engineer at Capital One, you will be a part of a community of technical experts working to define the future of ba"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 71
- Raw jobs found: 1393
- After US/location filtering: 852
- With trustworthy posted_date: 852
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "342903",
    "title": "Principal Core Infrastructure Engineer- Nashville,TN",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/342903",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:08:41.204290+00:00",
    "date_confidence": "high",
    "description": "Leads development and begins architecting components of scalable, elastic distributed systems for the Network Automation Team. Defines and enforces scalability requirements for own"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "323426",
    "title": "Principal Software Developer",
    "location": "Austin, TX, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/323426",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:08:41.204290+00:00",
    "date_confidence": "high",
    "description": "Oracle Cloud Infrastructure (OCI) delivers mission-critical applications for leading enterprises worldwide. Our cloud offers hyper-scale, multi-tenant services deployed across more"
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
    "fetched_at": "2026-08-28T15:08:41.204290+00:00",
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
    "fetched_at": "2026-08-28T15:08:41.204290+00:00",
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
    "fetched_at": "2026-08-28T15:08:41.204290+00:00",
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
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['careers.walmart.com is a custom Next.js app; widgets/Workday CXS/JSON endpoints 404 or 422. Need the jobs search XHR URL from DevTools on a US software-engineer search.']

## Cisco

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://cisco.wd5.myworkdayjobs.com/Cisco_Careers`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 33
- Raw jobs found: 641
- After US/location filtering: 208
- With trustworthy posted_date: 208
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2023141",
    "title": "Senior Software Engineer - Backend & AI",
    "location": "Austin, Texas, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Austin-Texas-US/Senior-Software-Engineer---Backend---AI_2023141-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:11:15.512761+00:00",
    "date_confidence": "high",
    "description": "Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Hybrid role, located in Austin, Texas Meet the Team Software i"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2023876",
    "title": "Software Engineer - Mobile",
    "location": "Bratislava, Slovakia",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Bratislava-Slovakia/Software-Engineer---Mobile_2023876",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:11:15.512761+00:00",
    "date_confidence": "high",
    "description": "Meet the Team Cisco's Webex Engineering Group is redefining the future of collaboration. We're building a world where people connect effortlessly to enjoy modern, uncompromised col"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2021765",
    "title": "Software Engineering Technical Leader, Backend (Hybrid)",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Software-Engineering-Technical-Leader--Backend--Hybrid-_2021765",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:11:15.512761+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 08/30/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Thi"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2022599",
    "title": "Principal Software Engineer - Cisco IQ Validation",
    "location": "RTP, North Carolina, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/RTP-North-Carolina-US/Principal-Engineer---Cisco-IQ-Validation_2022599",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:11:15.512761+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/29/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Mee"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2022586",
    "title": "Distinguished Software Engineer, AI Software & Platform (Hybrid)",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Distinguished-Software-Engineer--AI-Software---Platform--Hybrid-_2022586",
    "posted_date": "2026-08-21",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:11:15.512761+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/29/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Thi"
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 16
- Raw jobs found: 355
- After US/location filtering: 166
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
    "fetched_at": "2026-08-28T15:12:56.229570+00:00",
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
    "fetched_at": "2026-08-28T15:12:56.229570+00:00",
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
    "fetched_at": "2026-08-28T15:12:56.229570+00:00",
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
    "fetched_at": "2026-08-28T15:12:56.229570+00:00",
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
    "fetched_at": "2026-08-28T15:12:56.229570+00:00",
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
- Pages/requests fetched: 33
- Raw jobs found: 599
- After US/location filtering: 254
- With trustworthy posted_date: 254
- Errors/403s: none

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
    "fetched_at": "2026-08-28T15:14:31.280399+00:00",
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
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:14:31.280399+00:00",
    "date_confidence": "medium",
    "description": ""
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1203998",
    "title": "System Software Engineer",
    "location": "Sunnyvale, California, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Sunnyvale-California-United-States-of-America/System-Software-Engineer_1203998-2",
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:14:31.280399+00:00",
    "date_confidence": "medium",
    "description": ""
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
    "fetched_at": "2026-08-28T15:14:31.280399+00:00",
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
    "posted_date": "2026-07-29",
    "updated_date": "",
    "fetched_at": "2026-08-28T15:14:31.280399+00:00",
    "date_confidence": "medium",
    "description": ""
  }
]
```
