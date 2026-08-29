# Official careers scrape report — 2026-08-29_1806

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Software+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or advertised total
- Pages/requests fetched: 30
- Raw jobs found: 580
- After US/location filtering: 328
- With trustworthy posted_date: 328
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
    "fetched_at": "2026-08-29T18:06:44.687736+00:00",
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
    "fetched_at": "2026-08-29T18:06:44.687736+00:00",
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
    "fetched_at": "2026-08-29T18:06:44.687736+00:00",
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
    "fetched_at": "2026-08-29T18:06:44.687736+00:00",
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
    "fetched_at": "2026-08-29T18:06:44.687736+00:00",
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
- After US/location filtering: 1201
- With trustworthy posted_date: 1201
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10519775",
    "title": "Software Development Manager, Amazon Leo Data Platform",
    "location": "Redmond, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10519775/software-development-manager-amazon-leo-data-platform",
    "posted_date": "2026-08-28",
    "updated_date": "2026-08-28",
    "fetched_at": "2026-08-29T18:07:03.909599+00:00",
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
    "fetched_at": "2026-08-29T18:07:03.909599+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon’s low Earth orbit satellite network. Our mission is to deliver fast, reliable internet connectivity to customers beyond the reach of existing networks. From in"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10517605",
    "title": "Sr. Technical Full Life Cycle Recruiter, Amazon Stores",
    "location": "New York, New York, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10517605/sr-technical-full-life-cycle-recruiter-amazon-stores",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-29",
    "fetched_at": "2026-08-29T18:07:03.909599+00:00",
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
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-29T18:07:03.909599+00:00",
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
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-29T18:07:03.909599+00:00",
    "date_confidence": "high",
    "description": "A Forward Deployed Engineering Manager (FDE Manager) leads a pod of FDEs embedded within strategic enterprise customers, owning delivery execution, engineering quality, and team de"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=software+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or totalRecords
- Pages/requests fetched: 128
- Raw jobs found: 2557
- After US/location filtering: 1486
- With trustworthy posted_date: 1486
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200670204-0836",
    "title": "RF System Integration Engineer (Instrument Engineering)",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200670204/rf-system-integration-engineer-instrument-engineering",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:08:06.499941+00:00",
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
    "fetched_at": "2026-08-29T18:08:06.499941+00:00",
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
    "fetched_at": "2026-08-29T18:08:06.499941+00:00",
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
    "fetched_at": "2026-08-29T18:08:06.499941+00:00",
    "date_confidence": "high",
    "description": "Join this small team of extraordinary engineers that designs and produces precision protocol, RF and Analog Test Equipment for use in calibrating and testing 4G, 5G, WiFi, BT, mmWa"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200670199-0836",
    "title": "GUI Software Lead (SwiftUI)",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200670199/gui-software-lead-swiftui",
    "posted_date": "2026-08-29",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:08:06.499941+00:00",
    "date_confidence": "high",
    "description": "Join Apple’s Instrument Engineering team, where we design and build the custom RF test instruments that help deliver world-leading products to our customers. As GUI Software Lead, "
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: start=0,10,20,... ; num=10 (API cap); stop on empty/repeat or count
- Pages/requests fetched: 80
- Raw jobs found: 783
- After US/location filtering: 590
- With trustworthy posted_date: 590
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
    "fetched_at": "2026-08-29T18:09:39.252542+00:00",
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
    "fetched_at": "2026-08-29T18:09:39.252542+00:00",
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
    "fetched_at": "2026-08-29T18:09:39.252542+00:00",
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
    "fetched_at": "2026-08-29T18:09:39.252542+00:00",
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
    "fetched_at": "2026-08-29T18:09:39.252542+00:00",
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
- Pages/requests fetched: 68
- Raw jobs found: 1323
- After US/location filtering: 1096
- With trustworthy posted_date: 1096
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
    "fetched_at": "2026-08-29T18:11:58.892310+00:00",
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
    "fetched_at": "2026-08-29T18:11:58.892310+00:00",
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
    "fetched_at": "2026-08-29T18:11:58.892310+00:00",
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
    "fetched_at": "2026-08-29T18:11:58.892310+00:00",
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
    "fetched_at": "2026-08-29T18:11:58.892310+00:00",
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
- Pages/requests fetched: 33
- Raw jobs found: 602
- After US/location filtering: 221
- With trustworthy posted_date: 221
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR355248",
    "title": "Senior Product Manager, Emerging Technology",
    "location": "New York - New York",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/New-York---New-York/Senior-Product-Manager--Emerging-Technology_JR355248",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:14:42.848555+00:00",
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
    "fetched_at": "2026-08-29T18:14:42.848555+00:00",
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
    "fetched_at": "2026-08-29T18:14:42.848555+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR346498",
    "title": "Enterprise Tableau Account Director, State and Local Gov",
    "location": "Virginia - Mclean",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Virginia---Mclean/Tableau-Account-Director--SLG_JR346498",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:14:42.848555+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR333757",
    "title": "Pre-Sales Data and AI Architect - Solution Engineering (United States)",
    "location": "New York - New York",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/New-York---New-York/Pre-Sales-Data-and-AI-Architect---Solution-Engineering--United-States-_JR333757",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:14:42.848555+00:00",
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
- Pages/requests fetched: 24
- Raw jobs found: 412
- After US/location filtering: 232
- With trustworthy posted_date: 232
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
    "posted_date": "2026-07-30",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:16:27.467800+00:00",
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
    "fetched_at": "2026-08-29T18:16:27.467800+00:00",
    "date_confidence": "high",
    "description": "About the Role We are seeking a highly motivated Lead Software Engineer to join the new Project Graph team at Adobe. Project Graph is a new creative system that lets you combine fi"
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
    "fetched_at": "2026-08-29T18:16:27.467800+00:00",
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
    "fetched_at": "2026-08-29T18:16:27.467800+00:00",
    "date_confidence": "high",
    "description": "The Adobe Risk Platform (ARP) is Adobe's centralized fraud prevention and risk-decisioning platform, protecting surfaces like Commerce, Stock, and Firefly with real-time decisions "
  },
  {
    "company": "Adobe",
    "source": "adobe_official_careers",
    "job_id": "R147125",
    "title": "Senior Software Engineer",
    "location": "San Jose",
    "official_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/Senior-Software-Engineer_R147125-1",
    "posted_date": "2026-07-30",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:16:27.467800+00:00",
    "date_confidence": "medium",
    "description": ""
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
- Raw jobs found: 195
- After US/location filtering: 136
- With trustworthy posted_date: 136
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
    "fetched_at": "2026-08-29T18:18:24.948045+00:00",
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
    "fetched_at": "2026-08-29T18:18:24.948045+00:00",
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
    "fetched_at": "2026-08-29T18:18:24.948045+00:00",
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
    "fetched_at": "2026-08-29T18:18:24.948045+00:00",
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
    "fetched_at": "2026-08-29T18:18:24.948045+00:00",
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
    "fetched_at": "2026-08-29T18:19:26.754541+00:00",
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
    "fetched_at": "2026-08-29T18:19:26.754541+00:00",
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
    "fetched_at": "2026-08-29T18:19:26.754541+00:00",
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
    "fetched_at": "2026-08-29T18:19:26.754541+00:00",
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
    "fetched_at": "2026-08-29T18:19:26.754541+00:00",
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
- Raw jobs found: 90
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
    "fetched_at": "2026-08-29T18:19:28.216124+00:00",
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
    "fetched_at": "2026-08-29T18:19:28.216124+00:00",
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
    "fetched_at": "2026-08-29T18:19:28.216124+00:00",
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
    "fetched_at": "2026-08-29T18:19:28.216124+00:00",
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
    "posted_date": "2026-07-30",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:19:28.216124+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.077274+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.077274+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.077274+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.077274+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.077274+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.449260+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.449260+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.449260+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.449260+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.449260+00:00",
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
    "job_id": "JB0075074",
    "title": "Sr Staff AI Engineer - Veza",
    "location": "Minneapolis, Minnesota, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000146269339-sr-staff-ai-engineer-veza",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:19:52.780113+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.780113+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.780113+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.780113+00:00",
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
    "fetched_at": "2026-08-29T18:19:52.780113+00:00",
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
- Raw jobs found: 760
- After US/location filtering: 199
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
    "fetched_at": "2026-08-29T18:21:37.475538+00:00",
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
    "fetched_at": "2026-08-29T18:21:37.475538+00:00",
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
    "fetched_at": "2026-08-29T18:21:37.475538+00:00",
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
    "fetched_at": "2026-08-29T18:21:37.475538+00:00",
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
    "fetched_at": "2026-08-29T18:21:37.475538+00:00",
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
- Pages/requests fetched: 100
- Raw jobs found: 1999
- After US/location filtering: 938
- With trustworthy posted_date: 938
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
    "fetched_at": "2026-08-29T18:25:49.441862+00:00",
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
    "fetched_at": "2026-08-29T18:25:49.441862+00:00",
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
    "fetched_at": "2026-08-29T18:25:49.441862+00:00",
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
    "fetched_at": "2026-08-29T18:25:49.441862+00:00",
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
    "fetched_at": "2026-08-29T18:25:49.441862+00:00",
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
- Raw jobs found: 1363
- After US/location filtering: 965
- With trustworthy posted_date: 965
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999411",
    "title": "Lead Software Engineer, Backend (IC)",
    "location": "San Jose, CA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/San-Jose-CA/Lead-Software-Engineer--Backend--IC-_R999411-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:28:12.738767+00:00",
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
    "fetched_at": "2026-08-29T18:28:12.738767+00:00",
    "date_confidence": "high",
    "description": "Staff AI Engineer - Enterprise Analysis Platform (Remote Eligible) At Capital One, we are creating responsible and reliable AI systems, changing banking for good. For years, Capita"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999423",
    "title": "Manager, Product Management - IVR Customer Experience",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Manager--Product-Management---IVR-Customer-Experience_R999423-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:28:12.738767+00:00",
    "date_confidence": "high",
    "description": "Manager, Product Management - IVR Customer Experience Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, finding value creation"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999456",
    "title": "Senior Manager, Product Management - Workforce Management Tools",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Manager--Product-Management---Workforce-Management-Tools_R999456-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:28:12.738767+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Product Management - Workforce Management Tools Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, finding valu"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999460",
    "title": "Lead AI Engineer (Gen AI Platform Services: Agentic AI, Agent Guardrails, Agent Evaluation, Agent Memory)",
    "location": "San Francisco, CA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/San-Francisco--CA/Lead-AI-Engineer--Gen-AI-Platform-Services--Agentic-AI--Agent-Guardrails--Agent-Evaluation--Agent-Memory-_R999460-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:28:12.738767+00:00",
    "date_confidence": "high",
    "description": "Lead AI Engineer (Gen AI Platform Services: Agentic AI, Agent Guardrails, Agent Evaluation, Agent Memory) Overview At Capital One, we are creating responsible and reliable AI syste"
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 72
- Raw jobs found: 1422
- After US/location filtering: 869
- With trustworthy posted_date: 869
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
    "fetched_at": "2026-08-29T18:30:05.803957+00:00",
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
    "fetched_at": "2026-08-29T18:30:05.803957+00:00",
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
    "fetched_at": "2026-08-29T18:30:05.803957+00:00",
    "date_confidence": "high",
    "description": "Oracle Cloud Infrastructure (OCI) delivers mission-critical applications for leading enterprises worldwide. Our cloud offers hyper-scale, multi-tenant services deployed across more"
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
    "fetched_at": "2026-08-29T18:30:05.803957+00:00",
    "date_confidence": "high",
    "description": "Design, implement, and optimize components of highly distributed systems with a focus on scalability, reliability, availability, security, and operability. Build and test high-scal"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "339707",
    "title": "Software Developer 4",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/339707",
    "posted_date": "2026-07-16",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:30:05.803957+00:00",
    "date_confidence": "high",
    "description": "The Oracle Cloud Infrastructure (OCI) team can provide you the opportunity to build and operate a suite of massive scale, integrated cloud services in a broadly distributed, multi-"
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
- Raw jobs found: 654
- After US/location filtering: 192
- With trustworthy posted_date: 192
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
    "fetched_at": "2026-08-29T18:32:32.778661+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/18/2026 Meet the Team Splunk, a Cisco company, is building a safer, more resilient digital world with an end-to-end, full-stack p"
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
    "fetched_at": "2026-08-29T18:32:32.778661+00:00",
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
    "fetched_at": "2026-08-29T18:32:32.778661+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/03/2026 Meet the team We are seeking an experienced and motivated Software Engineer to join our Service Provider High End Router "
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2010405",
    "title": "Senior QA Automation Engineer - Networking L2/L3",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Senior-QA-Automation-Engineer---Networking-L2-L3_2010405",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:32:32.778661+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/26/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Thi"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2023141",
    "title": "Senior Software Engineer - Backend & AI",
    "location": "Austin, Texas, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Austin-Texas-US/Senior-Software-Engineer---Backend---AI_2023141-1",
    "posted_date": "2026-08-28",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:32:32.778661+00:00",
    "date_confidence": "high",
    "description": "Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Hybrid role, located in Austin, Texas Meet the Team Software i"
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 14
- Raw jobs found: 337
- After US/location filtering: 157
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
    "fetched_at": "2026-08-29T18:34:00.526600+00:00",
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
    "fetched_at": "2026-08-29T18:34:00.526600+00:00",
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
    "fetched_at": "2026-08-29T18:34:00.526600+00:00",
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
    "fetched_at": "2026-08-29T18:34:00.526600+00:00",
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
    "fetched_at": "2026-08-29T18:34:00.526600+00:00",
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
- Raw jobs found: 602
- After US/location filtering: 239
- With trustworthy posted_date: 239
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
    "fetched_at": "2026-08-29T18:35:17.521266+00:00",
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
    "posted_date": "2026-07-30",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:35:17.521266+00:00",
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
    "posted_date": "2026-07-30",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:35:17.521266+00:00",
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
    "fetched_at": "2026-08-29T18:35:17.521266+00:00",
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
    "posted_date": "2026-07-30",
    "updated_date": "",
    "fetched_at": "2026-08-29T18:35:17.521266+00:00",
    "date_confidence": "medium",
    "description": ""
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

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Verified official Workday search captured; adapter configuration deferred.']

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

- Status: blocked
- Scraping method: skip
- Search URL/API: `-`
- Pagination: -
- Pages/requests fetched: 0
- Raw jobs found: 0
- After US/location filtering: 0
- With trustworthy posted_date: 0
- Errors/403s: ['Verified official Greenhouse board captured; query-specific adapter deferred.']
