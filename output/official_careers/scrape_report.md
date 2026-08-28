# Official careers scrape report — 2026-08-28_0015

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Software+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or advertised total
- Pages/requests fetched: 30
- Raw jobs found: 589
- After US/location filtering: 334
- With trustworthy posted_date: 334
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "96193079597245126",
    "title": "Senior Software Engineer, AI/ML, Google Cloud Networking",
    "location": "New York, NY, USA; Seattle, WA, USA; San Jose, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/96193079597245126-senior-software-engineer-ai-ml-google-cloud-networking",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-28T00:15:54.603365+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "88630088865587910",
    "title": "Software Engineer III, Infrastructure, AI and Infrastructure",
    "location": "Kirkland, WA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/88630088865587910-software-engineer-iii-infrastructure-ai-and-infrastructure",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-28T00:15:54.603365+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "72980190111638214",
    "title": "Software Engineer III, AI/ML GenAI, Google Ads",
    "location": "Los Angeles, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/72980190111638214-software-engineer-iii-ai-ml-genai-google-ads",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-28T00:15:54.603365+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "91776684985852614",
    "title": "Software Engineer, Cloud Bigtable SQL and Analytics",
    "location": "New York, NY, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/91776684985852614-software-engineer-cloud-bigtable-sql-and-analytics",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-28T00:15:54.603365+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "102022632265654982",
    "title": "Software Engineer III, Infrastructure, Core",
    "location": "Pittsburgh, PA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/102022632265654982-software-engineer-iii-infrastructure-core",
    "posted_date": "2026-08-21",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-28T00:15:54.603365+00:00",
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
- After US/location filtering: 1204
- With trustworthy posted_date: 1204
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
    "fetched_at": "2026-08-28T00:16:14.826401+00:00",
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
    "fetched_at": "2026-08-28T00:16:14.826401+00:00",
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
    "fetched_at": "2026-08-28T00:16:14.826401+00:00",
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
    "fetched_at": "2026-08-28T00:16:14.826401+00:00",
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
    "fetched_at": "2026-08-28T00:16:14.826401+00:00",
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
- Raw jobs found: 2538
- After US/location filtering: 1482
- With trustworthy posted_date: 1482
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200671418-3956",
    "title": "Front End Engineer - Retail and Marcom Engineering'",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200671418/front-end-engineer-retail-and-marcom-engineering",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:17:14.143518+00:00",
    "date_confidence": "high",
    "description": "Do you want to help build some of the largest and most consequential enterprise and customer technology systems in the world? Join Apple’s Information Systems and Technology (IS&T)"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200679044-3337",
    "title": "Engineering Program Manager, Data Privacy and Compliance, Apple Services Engineering",
    "location": "Seattle, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200679044/engineering-program-manager-data-privacy-and-compliance-apple-services-engineering",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:17:14.143518+00:00",
    "date_confidence": "high",
    "description": "At Apple, we believe in the power of innovation to improve lives. Here, your ideas can quickly become impactful products, services, and customer experiences."
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680492-3337",
    "title": "Visual Generation Framework Software Engineer - Proactive",
    "location": "Seattle, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680492/visual-generation-framework-software-engineer-proactive",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:17:14.143518+00:00",
    "date_confidence": "high",
    "description": "The Visual Generation Framework team is seeking a senior engineer in ML software engineering. The primary responsibilities associated with this position include integration of rese"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680270-3956",
    "title": "Senior Hardware Systems Engineer– Data Center HWE",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680270/senior-hardware-systems-engineer-data-center-hwe",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:17:14.143518+00:00",
    "date_confidence": "high",
    "description": "Apple's Data Center Hardware Engineering team builds the custom compute platforms behind Apple's services. We design circuits and boards, own rack integration, and deliver complete"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200660665-0836",
    "title": "Sr Machine Learning Engineer, Proactive - ML Systems Engineering",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200660665/sr-machine-learning-engineer-proactive-ml-systems-engineering",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:17:14.143518+00:00",
    "date_confidence": "high",
    "description": "Apple’s products combine the best hardware and incredible software to deliver magical experiences to our customers. The Proactive Intelligence team builds features that anticipate "
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: start=0,10,20,... ; num=10 (API cap); stop on empty/repeat or count
- Pages/requests fetched: 82
- Raw jobs found: 815
- After US/location filtering: 613
- With trustworthy posted_date: 613
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200050042",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556978134",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:20:40.488951+00:00",
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
    "fetched_at": "2026-08-28T00:20:40.488951+00:00",
    "date_confidence": "high",
    "description": "Overview Join the team building the future of AI at Microsoft. Are you passionate about creating the next generation of Agent Building experiences? The Microsoft Foundry team withi"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200050407",
    "title": "Senior Software Engineer - CoreAI",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556979144",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:20:40.488951+00:00",
    "date_confidence": "high",
    "description": "Overview We are looking for a Senior Software Engineer – to design, build and operate scalable data pipelines that power GitHub Copilot and related model’s growing data needs. You’"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200050383",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond; United States, Oregon, Hillsboro; United States, California, Mountain View; United States, Texas, Austin; United States, North Carolina, Raleigh",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556979077",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:20:40.488951+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200049541",
    "title": "Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556972217",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:20:40.488951+00:00",
    "date_confidence": "high",
    "description": "Overview Security represents the most critical priorities for our customers in a world awash in digital threats, regulatory scrutiny, and estate complexity. Microsoft Security aspi"
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
- With trustworthy posted_date: 1081
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
    "fetched_at": "2026-08-28T00:22:35.556079+00:00",
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
    "fetched_at": "2026-08-28T00:22:35.556079+00:00",
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
    "fetched_at": "2026-08-28T00:22:35.556079+00:00",
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
    "fetched_at": "2026-08-28T00:22:35.556079+00:00",
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
    "fetched_at": "2026-08-28T00:22:35.556079+00:00",
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
- Raw jobs found: 615
- After US/location filtering: 243
- With trustworthy posted_date: 243
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR350380",
    "title": "Senior Software Development Engineer in Test - AI Tooling & Automation",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Software-Engineering-SMTS_JR350380",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:25:45.611656+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357806",
    "title": "Lead Software Development Engineer in Test - AI Tooling & Automation",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Software-Engineering-LMTS_JR357806",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:25:45.611656+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR345537",
    "title": "Software Engineer MTS — Automation & MuleSoft Agentic Cloud Services",
    "location": "Washington - Bellevue",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Washington---Bellevue/Software-Engineer-MTS---Automation---MuleSoft-Agentic-Cloud-Services_JR345537",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:25:45.611656+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR336646",
    "title": "Technical Support Engineer - Agentforce & Data 360",
    "location": "Washington - Seattle",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Washington---Seattle/Agentforce---Data-360-Support-Engineer_JR336646",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:25:45.611656+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Customer Success Jo"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357821",
    "title": "Software Engineering PMTS",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Software-Engineering-PMTS_JR357821",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:25:45.611656+00:00",
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
- Pages/requests fetched: 24
- Raw jobs found: 417
- After US/location filtering: 310
- With trustworthy posted_date: 310
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
    "fetched_at": "2026-08-28T00:27:40.968270+00:00",
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
    "fetched_at": "2026-08-28T00:27:40.968270+00:00",
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
    "fetched_at": "2026-08-28T00:27:40.968270+00:00",
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
    "fetched_at": "2026-08-28T00:27:40.968270+00:00",
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
    "fetched_at": "2026-08-28T00:27:40.968270+00:00",
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
- Raw jobs found: 198
- After US/location filtering: 137
- With trustworthy posted_date: 137
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "157628",
    "title": "Enterprise Applications Developer",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/157628",
    "posted_date": "2026-06-19",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:30:24.037692+00:00",
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
    "fetched_at": "2026-08-28T00:30:24.037692+00:00",
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
    "fetched_at": "2026-08-28T00:30:24.037692+00:00",
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
    "fetched_at": "2026-08-28T00:30:24.037692+00:00",
    "date_confidence": "high",
    "description": "About the role and team The FinTech team, part of the CFO’s organization, is responsible for innovating and building the best financial products and systems in the world. We are ob"
  },
  {
    "company": "Uber",
    "source": "uber_official_careers",
    "job_id": "301364",
    "title": "Sr Applications Developer, EPM",
    "location": "San Francisco, CA, United States",
    "official_url": "https://jobs.uber.com/en/jobs/301364",
    "posted_date": "2026-08-12",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:30:24.037692+00:00",
    "date_confidence": "high",
    "description": "About the Role The FinTech team, part of the CFO’s organization, is responsible for innovating and building the best financial products and systems in the world. We are obsessed wi"
  }
]
```

## DoorDash

- Status: ok
- Scraping method: HTTP GET Greenhouse boards-api /v1/boards/{token}/jobs?content=true
- Search URL/API: `https://boards-api.greenhouse.io/v1/boards/doordashusa/jobs`
- Pagination: single JSON payload (no paging)
- Pages/requests fetched: 1
- Raw jobs found: 467
- After US/location filtering: 463
- With trustworthy posted_date: 463
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
    "fetched_at": "2026-08-28T00:31:20.790849+00:00",
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
    "fetched_at": "2026-08-28T00:31:20.790849+00:00",
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
    "fetched_at": "2026-08-28T00:31:20.790849+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "7592588",
    "title": "Account Manager, CPG",
    "location": "New York, NY; Los Angeles, CA; Atlanta, GA; Chicago, IL; San Francisco, CA; New York",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/7592588",
    "posted_date": "2026-02-06",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-28T00:31:20.790849+00:00",
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
    "fetched_at": "2026-08-28T00:31:20.790849+00:00",
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
    "fetched_at": "2026-08-28T00:31:22.083799+00:00",
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
    "fetched_at": "2026-08-28T00:31:22.083799+00:00",
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
    "fetched_at": "2026-08-28T00:31:22.083799+00:00",
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
    "fetched_at": "2026-08-28T00:31:22.083799+00:00",
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
    "fetched_at": "2026-08-28T00:31:22.083799+00:00",
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
- Raw jobs found: 215
- After US/location filtering: 165
- With trustworthy posted_date: 165
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
    "fetched_at": "2026-08-28T00:31:48.403196+00:00",
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
    "fetched_at": "2026-08-28T00:31:48.403196+00:00",
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
    "fetched_at": "2026-08-28T00:31:48.403196+00:00",
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
    "fetched_at": "2026-08-28T00:31:48.403196+00:00",
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
    "fetched_at": "2026-08-28T00:31:48.403196+00:00",
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
- Raw jobs found: 386
- After US/location filtering: 302
- With trustworthy posted_date: 302
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
    "fetched_at": "2026-08-28T00:31:48.851668+00:00",
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
    "fetched_at": "2026-08-28T00:31:48.851668+00:00",
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
    "fetched_at": "2026-08-28T00:31:48.851668+00:00",
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
    "fetched_at": "2026-08-28T00:31:48.851668+00:00",
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
    "fetched_at": "2026-08-28T00:31:48.851668+00:00",
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
    "fetched_at": "2026-08-28T00:31:49.223260+00:00",
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
    "fetched_at": "2026-08-28T00:31:49.223260+00:00",
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
    "fetched_at": "2026-08-28T00:31:49.223260+00:00",
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
    "fetched_at": "2026-08-28T00:31:49.223260+00:00",
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
    "fetched_at": "2026-08-28T00:31:49.223260+00:00",
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
- Raw jobs found: 758
- After US/location filtering: 212
- With trustworthy posted_date: 0
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21660",
    "title": "Senior Financial Analyst, CFO Global Sustainability Office",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Financial-Analyst-CFO-Global-Sustainability-Office/21660",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:33:42.727720+00:00",
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
    "fetched_at": "2026-08-28T00:33:42.727720+00:00",
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
    "fetched_at": "2026-08-28T00:33:42.727720+00:00",
    "date_confidence": "unknown",
    "description": "Vertical Video Producer/Editor, Bloomberg Opinion – 12 Month Contract"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21639",
    "title": "Senior Financial Analyst - Workplace Operations - Finance & Administration",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Financial-Analyst-Workplace-Operations-Finance-Administration/21639",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:33:42.727720+00:00",
    "date_confidence": "unknown",
    "description": "Senior Financial Analyst - Workplace Operations - Finance & Administration"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21622",
    "title": "Director, Product Marketing (Audience, Data & Emerging)",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Director-Product-Marketing-Audience-Data-Emerging/21622",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:33:42.727720+00:00",
    "date_confidence": "unknown",
    "description": "Director, Product Marketing (Audience, Data & Emerging)"
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
- After US/location filtering: 955
- With trustworthy posted_date: 955
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
    "fetched_at": "2026-08-28T00:38:30.744408+00:00",
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
    "fetched_at": "2026-08-28T00:38:30.744408+00:00",
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
    "fetched_at": "2026-08-28T00:38:30.744408+00:00",
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
    "fetched_at": "2026-08-28T00:38:30.744408+00:00",
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
    "fetched_at": "2026-08-28T00:38:30.744408+00:00",
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
- Raw jobs found: 1350
- After US/location filtering: 954
- With trustworthy posted_date: 954
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999361",
    "title": "Senior Lead AI Engineer (GenAI Platform Services, Agentic Platform)",
    "location": "San Jose, CA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/San-Jose-CA/Senior-Lead-AI-Engineer--GenAI-Platform-Services--Agentic-Platform-_R999361-1",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:40:52.211223+00:00",
    "date_confidence": "high",
    "description": "Senior Lead AI Engineer (GenAI Platform Services, Agentic Platform) Overview: At Capital One, we are creating responsible and reliable AI systems, changing banking for good. For ye"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R238979",
    "title": "Sr. Business Analyst - US Card",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Sr-Business-Analyst---US-Card_R238979-1",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:40:52.211223+00:00",
    "date_confidence": "high",
    "description": "Sr. Business Analyst - US Card Summary: As a Senior Business Analyst at Capital One, you will apply your strategic and analytical skills to major company challenges. You will team "
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R244058",
    "title": "Lead Software Engineer, Messaging Dispatch",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Lead-Software-Engineer--Messaging-Dispatch_R244058-1",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:40:52.211223+00:00",
    "date_confidence": "high",
    "description": "Lead Software Engineer, Messaging Dispatch Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborativ"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R235046",
    "title": "Director, Staff Engineer - Marketing & Sales",
    "location": "Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Richmond-VA/Distinguished-Engineer_R235046",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:40:52.211223+00:00",
    "date_confidence": "high",
    "description": "Director, Staff Engineer - Marketing & Sales As a Director, Staff Engineer at Capital One, you will be a part of a community of technical experts working to define the future of ba"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R243350",
    "title": "Sr Director, AI Engineering",
    "location": "San Francisco, CA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/San-Francisco--CA/Sr-Director--AI-Engineering_R243350-1",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:40:52.211223+00:00",
    "date_confidence": "high",
    "description": "Sr Director, AI Engineering Overview: At Capital One, we are creating responsible and reliable AI systems, changing banking for good. For years, Capital One has been an industry le"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 71
- Raw jobs found: 1404
- After US/location filtering: 851
- With trustworthy posted_date: 851
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "338844",
    "title": "Senior Software Development Engineer",
    "location": "United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/338844",
    "posted_date": "2026-07-13",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:42:30.870866+00:00",
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
    "fetched_at": "2026-08-28T00:42:30.870866+00:00",
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
    "fetched_at": "2026-08-28T00:42:30.870866+00:00",
    "date_confidence": "high",
    "description": "Oracle Cloud Infrastructure (OCI) delivers mission-critical applications for leading enterprises worldwide. Our cloud offers hyper-scale, multi-tenant services deployed across more"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "341640",
    "title": "Senior Platform Software Engineer",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/341640",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:42:30.870866+00:00",
    "date_confidence": "high",
    "description": "As a Senior Software Development Engineer, you will own the design and development of major components that improve the developer experience for software teams building Oracle Clou"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "343994",
    "title": "Senior Software Development Engineer - Core Infrastructure",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/343994",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:42:30.870866+00:00",
    "date_confidence": "high",
    "description": "Design, implement, and optimize components of highly distributed systems with a focus on scalability, reliability, availability, security, and operability. Build and test high-scal"
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
- Raw jobs found: 658
- After US/location filtering: 225
- With trustworthy posted_date: 225
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2023876",
    "title": "Software Engineer - Mobile",
    "location": "Bratislava, Slovakia",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Bratislava-Slovakia/Software-Engineer---Mobile_2023876",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:44:43.097952+00:00",
    "date_confidence": "high",
    "description": "Meet the Team Cisco's Webex Engineering Group is redefining the future of collaboration. We're building a world where people connect effortlessly to enjoy modern, uncompromised col"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2010405",
    "title": "Senior QA Automation Engineer - Networking L2/L3",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Senior-QA-Automation-Engineer---Networking-L2-L3_2010405",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:44:43.097952+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/27/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Job"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2023141",
    "title": "Senior Software Engineer - Backend & AI",
    "location": "Austin, Texas, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Austin-Texas-US/Senior-Software-Engineer---Backend---AI_2023141-1",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-28T00:44:43.097952+00:00",
    "date_confidence": "high",
    "description": "Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Meet the Team Software is a team sport. The core of this team "
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
    "fetched_at": "2026-08-28T00:44:43.097952+00:00",
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
    "fetched_at": "2026-08-28T00:44:43.097952+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/29/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Mee"
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 16
- Raw jobs found: 361
- After US/location filtering: 169
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
    "fetched_at": "2026-08-28T00:46:12.114774+00:00",
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
    "fetched_at": "2026-08-28T00:46:12.114774+00:00",
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
    "fetched_at": "2026-08-28T00:46:12.114774+00:00",
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
    "fetched_at": "2026-08-28T00:46:12.114774+00:00",
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
    "fetched_at": "2026-08-28T00:46:12.114774+00:00",
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
- Pages/requests fetched: 32
- Raw jobs found: 588
- After US/location filtering: 248
- With trustworthy posted_date: 248
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
    "fetched_at": "2026-08-28T00:48:00.147471+00:00",
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
    "fetched_at": "2026-08-28T00:48:00.147471+00:00",
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
    "fetched_at": "2026-08-28T00:48:00.147471+00:00",
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
    "fetched_at": "2026-08-28T00:48:00.147471+00:00",
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
    "fetched_at": "2026-08-28T00:48:00.147471+00:00",
    "date_confidence": "medium",
    "description": ""
  }
]
```
