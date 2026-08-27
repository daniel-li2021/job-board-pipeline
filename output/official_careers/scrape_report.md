# Official careers scrape report — 2026-08-27_1319

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Software+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or advertised total
- Pages/requests fetched: 30
- Raw jobs found: 583
- After US/location filtering: 332
- With trustworthy posted_date: 332
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "131789837265969862",
    "title": "Senior Software Engineer, Full Stack",
    "location": "Boulder, CO, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/131789837265969862-senior-software-engineer-full-stack",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-27T13:19:43.120699+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "140223091451011782",
    "title": "Software Engineer III, Full Stack",
    "location": "Raleigh, NC, USA; Durham, NC, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/140223091451011782-software-engineer-iii-full-stack",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-27T13:19:43.120699+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "124708982383092422",
    "title": "Senior Software Engineer, Mobile (Android), Navigation Experiences",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/124708982383092422-senior-software-engineer-mobile-android-navigation-experiences",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-27T13:19:43.120699+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "77801617318912710",
    "title": "Senior Software Engineer",
    "location": "Boulder, CO, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/77801617318912710-senior-software-engineer",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-27T13:19:43.120699+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "91079319735935686",
    "title": "Senior Software Engineer, Full Stack",
    "location": "Atlanta, GA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/91079319735935686-senior-software-engineer-full-stack",
    "posted_date": "2026-08-27",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-27T13:19:43.120699+00:00",
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
- After US/location filtering: 1207
- With trustworthy posted_date: 1207
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10515122",
    "title": "Software Engineer II - Embedded Networking, Amazon Leo",
    "location": "Sunnyvale, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10515122/software-engineer-ii-embedded-networking-amazon-leo",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-27T13:20:02.892791+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon’s low Earth orbit satellite network. Our mission is to deliver fast, reliable internet connectivity to customers beyond the reach of existing networks. From in"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10515667",
    "title": "Software Development Engineer, GNC Software, Amazon Leo",
    "location": "Redmond, Washington, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10515667/software-development-engineer-gnc-software-amazon-leo",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-27T13:20:02.892791+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon’s low Earth orbit satellite network. Our mission is to deliver fast, reliable internet connectivity to customers beyond the reach of existing networks. From in"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10515912",
    "title": "Software Engineer I, Memberships",
    "location": "San Francisco, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10515912/software-engineer-i-memberships",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-27",
    "fetched_at": "2026-08-27T13:20:02.892791+00:00",
    "date_confidence": "high",
    "description": "If you are interested in this position, please apply on Twitch's Career site https://www.twitch.tv/jobs/en/ About Us Twitch is the world’s biggest live streaming service, with glob"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10514583",
    "title": "Software Engineer, XR , Fauna",
    "location": "New York, New York, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10514583/software-engineer-xr-fauna",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-27T13:20:02.892791+00:00",
    "date_confidence": "high",
    "description": "We are seeking a Software Engineer to contribute to the development of XR applications for teleoperating Fauna robots. You will work at the intersection of XR engineering and real-"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10514569",
    "title": "Software Engineer, Browser Client",
    "location": "San Francisco, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10514569/software-engineer-browser-client",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-27T13:20:02.892791+00:00",
    "date_confidence": "high",
    "description": "If you are interested in this position, please apply on Twitch's Career site https://www.twitch.tv/jobs/en/ About Us: Twitch is the world’s biggest live streaming service, with glo"
  }
]
```

## Apple

- Status: ok
- Scraping method: HTTP GET HTML + __staticRouterHydrationData JSON
- Search URL/API: `https://jobs.apple.com/en-us/search?search=software+engineer&location=united-states-USA&sort=newest&page=1`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or totalRecords
- Pages/requests fetched: 127
- Raw jobs found: 2535
- After US/location filtering: 1485
- With trustworthy posted_date: 1485
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200679879-0836",
    "title": "Places Data and ML Director",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200679879/places-data-and-ml-director",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:21:04.868816+00:00",
    "date_confidence": "high",
    "description": "Apple Maps enables millions of delightful user experiences every day across the world. Places data is where the Maps experience truly comes to life, whether someone is trying to di"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200667030-0157",
    "title": "Software Engineer (Framework Solutions), AI & Data Platforms (AiDP)",
    "location": "Austin, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200667030/software-engineer-framework-solutions-ai-data-platforms-aidp",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:21:04.868816+00:00",
    "date_confidence": "high",
    "description": "Do you want to help build some of the largest and most consequential enterprise and customer technology systems in the world? Join Apple’s Information Systems and Technology (IS&T)"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200667030-3956",
    "title": "Software Engineer (Framework Solutions), AI & Data Platforms (AiDP)",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200667030/software-engineer-framework-solutions-ai-data-platforms-aidp",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:21:04.868816+00:00",
    "date_confidence": "high",
    "description": "Do you want to help build some of the largest and most consequential enterprise and customer technology systems in the world? Join Apple’s Information Systems and Technology (IS&T)"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680039-3956",
    "title": "Solutions Lead, Regulatory Projects, BPR: Supply Chain",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680039/solutions-lead-regulatory-projects-bpr-supply-chain",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:21:04.868816+00:00",
    "date_confidence": "high",
    "description": "Imagine what you could do here. At Apple, great ideas have a way of becoming great products, services, and customer experiences very quickly. Bring passion and dedication to your j"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680036-3956",
    "title": "Program Manager, Quality Data & Testing Lead, BPR: Supply Chain",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680036/program-manager-quality-data-testing-lead-bpr-supply-chain",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:21:04.868816+00:00",
    "date_confidence": "high",
    "description": "Imagine what you could do here. At Apple, great ideas have a way of becoming great products, services, and customer experiences very quickly. Bring passion and dedication to your j"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: start=0,10,20,... ; num=10 (API cap); stop on empty/repeat or count
- Pages/requests fetched: 79
- Raw jobs found: 784
- After US/location filtering: 590
- With trustworthy posted_date: 590
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200045052",
    "title": "Software Engineer (CEAI)",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556943247",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:22:40.450124+00:00",
    "date_confidence": "high",
    "description": "Overview Commercial Engineering & AI (CEAI) partners closely with stakeholders to accelerate the transformation of Microsoft’s commercial business into a frontier organization. We "
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200017732",
    "title": "Service Engineer II",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556650636",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:22:40.450124+00:00",
    "date_confidence": "high",
    "description": "Overview Are you a customer-obsessed, AI-curious problem-solver who thrives in an inclusive, collaborative global team? Join Engineering Operations (EngOps) – the organization driv"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200031149",
    "title": "Service Engineer",
    "location": "United States, Washington, Redmond; United States, Georgia, Atlanta",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556833996",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:22:40.450124+00:00",
    "date_confidence": "high",
    "description": "Overview Are you a customer-obsessed, AI-curious problem-solver who thrives in an inclusive, collaborative global team? Join Engineering Operations (EngOps) – the organization driv"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200051314",
    "title": "Data Scientist II",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556980966",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:22:40.450124+00:00",
    "date_confidence": "high",
    "description": "Overview As Microsoft continues to lead the way in AI innovation, Clipchamp is transforming how people create, edit, and share video content. With nearly 100 million registered use"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200041036",
    "title": "Senior SoC HW (PnP/Functional) Validation Engineer",
    "location": "United States, Oregon, Hillsboro",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556899532",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:22:40.450124+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 68
- Raw jobs found: 1289
- After US/location filtering: 1067
- With trustworthy posted_date: 1067
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
    "fetched_at": "2026-08-27T13:24:48.756865+00:00",
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
    "fetched_at": "2026-08-27T13:24:48.756865+00:00",
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
    "fetched_at": "2026-08-27T13:24:48.756865+00:00",
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
    "fetched_at": "2026-08-27T13:24:48.756865+00:00",
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
    "fetched_at": "2026-08-27T13:24:48.756865+00:00",
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
- After US/location filtering: 242
- With trustworthy posted_date: 242
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357685",
    "title": "RVP, Sales - Public Sector",
    "location": "British Columbia - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/British-Columbia---Remote/RVP--Sales_JR357685",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:28:10.279426+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357686",
    "title": "RVP, Sales - Public Sector",
    "location": "Ontario - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Ontario---Remote/RVP--Sales_JR357686",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:28:10.279426+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357221",
    "title": "Solution Engineer - Federal Civilian",
    "location": "Virginia - Mclean",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Virginia---Mclean/Solution-Engineer---Federal-Civilian_JR357221",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:28:10.279426+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR351110",
    "title": "Senior Software Engineer, Event Technology",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Senior-Software-Engineer--Event-Technology_JR351110",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:28:10.279426+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR355645",
    "title": "Lead Software Engineer - Enterprise Agents",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Lead-Software-Engineer---Enterprise-Agents_JR355645",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:28:10.279426+00:00",
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
- Pages/requests fetched: 25
- Raw jobs found: 426
- After US/location filtering: 318
- With trustworthy posted_date: 318
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
    "posted_date": "2026-07-28",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:30:15.417336+00:00",
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
    "fetched_at": "2026-08-27T13:30:15.417336+00:00",
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
    "posted_date": "2026-07-28",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:30:15.417336+00:00",
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
    "fetched_at": "2026-08-27T13:30:15.417336+00:00",
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
    "fetched_at": "2026-08-27T13:30:15.417336+00:00",
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
- Raw jobs found: 218
- After US/location filtering: 152
- With trustworthy posted_date: 152
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
    "fetched_at": "2026-08-27T13:32:34.164037+00:00",
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
    "fetched_at": "2026-08-27T13:32:34.164037+00:00",
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
    "fetched_at": "2026-08-27T13:32:34.164037+00:00",
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
    "fetched_at": "2026-08-27T13:32:34.164037+00:00",
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
    "fetched_at": "2026-08-27T13:32:34.164037+00:00",
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
- Raw jobs found: 472
- After US/location filtering: 467
- With trustworthy posted_date: 467
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
    "fetched_at": "2026-08-27T13:33:29.530065+00:00",
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
    "fetched_at": "2026-08-27T13:33:29.530065+00:00",
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
    "fetched_at": "2026-08-27T13:33:29.530065+00:00",
    "date_confidence": "high",
    "description": "<div class=\"content-intro\"><p><img style=\"display: none; max-width: 100%;\" src=\"https://click.appcast.io/greenhouse-te8/a31.png?ent=34&amp;e=22630&amp;t=1701374353806\" width=\"1px\">"
  },
  {
    "company": "DoorDash",
    "source": "doordash_official_careers",
    "job_id": "8119389",
    "title": "Account Executive - New Verticals, Enterprise Ad Sales",
    "location": "New York, NY; San Francisco, CA; Los Angeles, CA; Chicago, IL; Atlanta, GA; San Francisco",
    "official_url": "https://job-boards.greenhouse.io/doordashusa/jobs/8119389",
    "posted_date": "2026-08-10",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-27T13:33:29.530065+00:00",
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-27T13:33:29.530065+00:00",
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
- After US/location filtering: 59
- With trustworthy posted_date: 59
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
    "fetched_at": "2026-08-27T13:33:30.613834+00:00",
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
    "fetched_at": "2026-08-27T13:33:30.613834+00:00",
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
    "fetched_at": "2026-08-27T13:33:30.613834+00:00",
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
    "fetched_at": "2026-08-27T13:33:30.613834+00:00",
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
    "posted_date": "2026-07-28",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:33:30.613834+00:00",
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
    "fetched_at": "2026-08-27T13:33:58.017920+00:00",
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
    "fetched_at": "2026-08-27T13:33:58.017920+00:00",
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
    "fetched_at": "2026-08-27T13:33:58.017920+00:00",
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
    "fetched_at": "2026-08-27T13:33:58.017920+00:00",
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
    "fetched_at": "2026-08-27T13:33:58.017920+00:00",
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
- Raw jobs found: 385
- After US/location filtering: 303
- With trustworthy posted_date: 303
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
    "fetched_at": "2026-08-27T13:33:58.364125+00:00",
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
    "fetched_at": "2026-08-27T13:33:58.364125+00:00",
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
    "fetched_at": "2026-08-27T13:33:58.364125+00:00",
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
    "fetched_at": "2026-08-27T13:33:58.364125+00:00",
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
    "fetched_at": "2026-08-27T13:33:58.364125+00:00",
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
- Raw jobs found: 254
- After US/location filtering: 188
- With trustworthy posted_date: 188
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074972",
    "title": "Senior Staff Data Platform Engineer - Kafka - Apache Iceberg - Apache Spark",
    "location": "San Diego, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145885859-senior-staff-data-platform-engineer-kafka-apache-iceberg-apache-spark",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:33:58.793343+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075080",
    "title": "Senior Staff Software Engineer, Agentic Systems - Moveworks",
    "location": "Mountain View, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145848949-senior-staff-software-engineer-agentic-systems-moveworks",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:33:58.793343+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075079",
    "title": "Senior Staff Machine Learning Engineer, Agentic Systems - Moveworks",
    "location": "Mountain View, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145848354-senior-staff-machine-learning-engineer-agentic-systems-moveworks",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:33:58.793343+00:00",
    "date_confidence": "high",
    "description": "Who we are Moveworks is the Agentic AI Assistant platform that empowers the entire workforce. Our platform enables employees to converse with all of their business systems through "
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075076",
    "title": "Tech Lead, Agent Eval Platform",
    "location": "Mountain View, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145846689-tech-lead-agent-eval-platform",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:33:58.793343+00:00",
    "date_confidence": "high",
    "description": "Who we are Moveworks: the Agentic AI Assistant platform that empowers the entire workforce. Our platform enables employees to converse with all of their business systems through na"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075073",
    "title": "Staff Machine Learning Engineer, Agent Eval Platform",
    "location": "Mountain View, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145845739-staff-machine-learning-engineer-agent-eval-platform",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:33:58.793343+00:00",
    "date_confidence": "high",
    "description": "Who we are Moveworks: the Agentic AI Assistant platform that empowers the entire workforce. Our platform enables employees to converse with all of their business systems through na"
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
- Pages/requests fetched: 66
- Raw jobs found: 772
- After US/location filtering: 211
- With trustworthy posted_date: 0
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21638",
    "title": "Vertical Video Producer/Editor, Bloomberg Opinion – 12 Month Contract",
    "location": "Washington, District of Columbia, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Vertical-Video-Producer-Editor-Bloomberg-Opinion-12-Month-Contract/21638",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:35:52.715503+00:00",
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
    "fetched_at": "2026-08-27T13:35:52.715503+00:00",
    "date_confidence": "unknown",
    "description": "Senior Financial Analyst - Workplace Operations - Finance & Administration"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21620",
    "title": "Director, Product Marketing (Core Media)",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Director-Product-Marketing-Core-Media/21620",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:35:52.715503+00:00",
    "date_confidence": "unknown",
    "description": "Director, Product Marketing (Core Media)"
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
    "fetched_at": "2026-08-27T13:35:52.715503+00:00",
    "date_confidence": "unknown",
    "description": "Director, Product Marketing (Audience, Data & Emerging)"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21603",
    "title": "Data Quality Analyst – Enterprise Data",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Data-Quality-Analyst-Enterprise-Data/21603",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:35:52.715503+00:00",
    "date_confidence": "unknown",
    "description": "Data Quality Analyst – Enterprise Data"
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
    "fetched_at": "2026-08-27T13:40:52.550100+00:00",
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
    "fetched_at": "2026-08-27T13:40:52.550100+00:00",
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
    "fetched_at": "2026-08-27T13:40:52.550100+00:00",
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
    "fetched_at": "2026-08-27T13:40:52.550100+00:00",
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
    "fetched_at": "2026-08-27T13:40:52.550100+00:00",
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
- Raw jobs found: 1353
- After US/location filtering: 959
- With trustworthy posted_date: 958
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R237511",
    "title": "Lead Software Development Engineer - Shared Platforms",
    "location": "Nottingham, Eng",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Nottingham--Eng/Lead-Software-Development-Engineer---Shared-Platforms_R237511-1",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:43:16.733862+00:00",
    "date_confidence": "high",
    "description": "Nottingham Trent House (95002), United Kingdom, Nottingham, Nottinghamshire Lead Software Development Engineer - Shared Platforms About this role Capital One’s mission is to change"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999269",
    "title": "Technology Summer Internship",
    "location": "Nottingham, Eng",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Nottingham--Eng/Technology-Summer-Internship_R999269",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:43:16.733862+00:00",
    "date_confidence": "high",
    "description": "Nottingham Trent House (95002), United Kingdom, Nottingham, Nottinghamshire Technology Summer Internship Application Information Salary: £46,500 (pro rata) plus a £1,000 joining bo"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999267",
    "title": "Technology Graduate",
    "location": "Nottingham, Eng",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Nottingham--Eng/Technology-Graduate_R999267",
    "posted_date": "2026-08-27",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:43:16.733862+00:00",
    "date_confidence": "high",
    "description": "Nottingham Trent House (95002), United Kingdom, Nottingham, Nottinghamshire Technology Graduate Application Information Salary: £46,500 in Nottingham / £55,500 in London plus a £5,"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R248576",
    "title": "Senior Platform Engineer",
    "location": "Richmond, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Richmond-VA/Senior-Platform-Engineer_R248576-1",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:43:16.733862+00:00",
    "date_confidence": "high",
    "description": "Senior Platform Engineer Do you love building and pioneering in the technology space? Do you enjoy solving complex technical problems in a fast-paced, collaborative, inclusive, and"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R244715",
    "title": "Senior Cyber Program Manager",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Cyber-Program-Manager_R244715-2",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:43:16.733862+00:00",
    "date_confidence": "high",
    "description": "Senior Cyber Program Manager Do you have a passion for technology, influencing at all levels, and leading change for the better? If so, we have an exciting opportunity as a Senior "
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 70
- Raw jobs found: 1388
- After US/location filtering: 841
- With trustworthy posted_date: 841
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
    "fetched_at": "2026-08-27T13:45:10.186623+00:00",
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
    "fetched_at": "2026-08-27T13:45:10.186623+00:00",
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
    "fetched_at": "2026-08-27T13:45:10.186623+00:00",
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
    "fetched_at": "2026-08-27T13:45:10.186623+00:00",
    "date_confidence": "high",
    "description": "As a Senior Software Development Engineer, you will own the design and development of major components that improve the developer experience for software teams building Oracle Clou"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "342728",
    "title": "Senior Platform Software Engineer",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/342728",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:45:10.186623+00:00",
    "date_confidence": "high",
    "description": "As a Senior Software Development Engineer on OCI Build, you will independently design, build, and operate components of a critical OCI developer infrastructure platform. You will s"
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
- Raw jobs found: 651
- After US/location filtering: 217
- With trustworthy posted_date: 217
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
    "fetched_at": "2026-08-27T13:47:26.705648+00:00",
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
    "fetched_at": "2026-08-27T13:47:26.705648+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 10/27/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Job"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2024063",
    "title": "Cloud Engineer",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Cloud-Engineer_2024063",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:47:26.705648+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 08/27/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Mee"
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
    "fetched_at": "2026-08-27T13:47:26.705648+00:00",
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
    "fetched_at": "2026-08-27T13:47:26.705648+00:00",
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
- Raw jobs found: 376
- After US/location filtering: 177
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
    "fetched_at": "2026-08-27T13:49:00.662998+00:00",
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
    "fetched_at": "2026-08-27T13:49:00.662998+00:00",
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
    "fetched_at": "2026-08-27T13:49:00.662998+00:00",
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
    "fetched_at": "2026-08-27T13:49:00.662998+00:00",
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
    "fetched_at": "2026-08-27T13:49:00.662998+00:00",
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
- Raw jobs found: 588
- After US/location filtering: 246
- With trustworthy posted_date: 246
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
    "fetched_at": "2026-08-27T13:50:48.218519+00:00",
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
    "posted_date": "2026-07-28",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:50:48.218519+00:00",
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
    "posted_date": "2026-07-28",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:50:48.218519+00:00",
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
    "fetched_at": "2026-08-27T13:50:48.218519+00:00",
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
    "posted_date": "2026-07-28",
    "updated_date": "",
    "fetched_at": "2026-08-27T13:50:48.218519+00:00",
    "date_confidence": "medium",
    "description": ""
  }
]
```
