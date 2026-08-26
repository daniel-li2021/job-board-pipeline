# Official careers scrape report — 2026-08-26_1623

Discovery only. Matching/ranking is applied afterwards by the shared board pipeline.

## Google

- Status: ok
- Scraping method: HTTP GET HTML + AF_initDataCallback ds:1 JSON
- Search URL/API: `https://www.google.com/about/careers/applications/jobs/results?sort_by=date&q=%22Software+Engineer%22&location=United+States&page=1&target_level=MID&target_level=EARLY&target_level=INTERN_AND_APPRENTICE`
- Pagination: page=1,2,... (20 jobs/page); stop on empty/repeat or advertised total
- Pages/requests fetched: 30
- Raw jobs found: 568
- After US/location filtering: 326
- With trustworthy posted_date: 326
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "84680705375642310",
    "title": "Software Engineer, Infrastructure, PhD, Early Career, 2027 Start",
    "location": "Sunnyvale, CA, USA; Atlanta, GA, USA; Austin, TX, USA; Kirkland, WA, USA; Los Angeles, CA, USA; Madison, WI, USA; Mountain View, CA, USA; New York, NY, USA; Raleigh, NC, USA; Durham, NC, USA; San Bruno, CA, USA; Seattle, WA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/84680705375642310-software-engineer-infrastructure-phd-early-career-2027-start",
    "posted_date": "2026-08-24",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-26T16:23:41.572690+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "120482975081996998",
    "title": "Senior Software Engineer, Embedded Systems, Health and Home",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/120482975081996998-senior-software-engineer-embedded-systems-health-and-home",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-26T16:23:41.572690+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "127944260988084934",
    "title": "Software Engineer, AI/ML, Google Research",
    "location": "Mountain View, CA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/127944260988084934-software-engineer-ai-ml-google-research",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-26T16:23:41.572690+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "130737570278449862",
    "title": "Software Engineer, Search, AI/ML",
    "location": "Cambridge, MA, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/130737570278449862-software-engineer-search-ai-ml",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-26T16:23:41.572690+00:00",
    "date_confidence": "high",
    "description": "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products"
  },
  {
    "company": "Google",
    "source": "google_official_careers",
    "job_id": "141934996695720646",
    "title": "Senior Software Engineer, Search Personalization Quality",
    "location": "New York, NY, USA",
    "official_url": "https://www.google.com/about/careers/applications/jobs/results/141934996695720646-senior-software-engineer-search-personalization-quality",
    "posted_date": "2026-08-26",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-26T16:23:41.572690+00:00",
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
- Raw jobs found: 2035
- After US/location filtering: 1205
- With trustworthy posted_date: 1205
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
    "fetched_at": "2026-08-26T16:24:15.232156+00:00",
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
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-26T16:24:15.232156+00:00",
    "date_confidence": "high",
    "description": "Amazon Leo is Amazon’s low Earth orbit satellite network. Our mission is to deliver fast, reliable internet connectivity to customers beyond the reach of existing networks. From in"
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
    "fetched_at": "2026-08-26T16:24:15.232156+00:00",
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
    "fetched_at": "2026-08-26T16:24:15.232156+00:00",
    "date_confidence": "high",
    "description": "If you are interested in this position, please apply on Twitch's Career site https://www.twitch.tv/jobs/en/ About Us: Twitch is the world’s biggest live streaming service, with glo"
  },
  {
    "company": "Amazon",
    "source": "amazon_official_careers",
    "job_id": "10514554",
    "title": "Software Engineer II, Fintech",
    "location": "San Francisco, California, USA",
    "official_url": "https://www.amazon.jobs/en/jobs/10514554/software-engineer-ii-fintech",
    "posted_date": "2026-08-25",
    "updated_date": "2026-08-26",
    "fetched_at": "2026-08-26T16:24:15.232156+00:00",
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
- Raw jobs found: 2536
- After US/location filtering: 1484
- With trustworthy posted_date: 1484
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680022-1435",
    "title": "Senior Backend Software Engineer, Apple Pay",
    "location": "Cary, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680022/senior-backend-software-engineer-apple-pay",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:25:18.016759+00:00",
    "date_confidence": "high",
    "description": "Imagine what you could do here! At Apple, great ideas have a way of becoming phenomenal products, services, and customer experiences very quickly. Are you passionate about building"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200679728-2502",
    "title": "US-Technical Specialist",
    "location": "Pentagon City, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200679728/us-technical-specialist",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:25:18.016759+00:00",
    "date_confidence": "high",
    "description": "Apple Retail is where the best of Apple comes together. We bring our expertise to help people do what they love, delivering an only-at-Apple experience. At Apple, we believe inclus"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200680118-2926",
    "title": "US-Technical Specialist",
    "location": "Pittsburgh, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200680118/us-technical-specialist",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:25:18.016759+00:00",
    "date_confidence": "high",
    "description": "Apple Retail is where the best of Apple comes together. We bring our expertise to help people do what they love, delivering an only-at-Apple experience. At Apple, we believe inclus"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200679909-3956",
    "title": "Software Engineer - VE",
    "location": "Sunnyvale, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200679909/software-engineer-ve",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:25:18.016759+00:00",
    "date_confidence": "high",
    "description": "The people here at Apple don't just create products, they create the kind of wonder that's revolutionized entire industries. It's the diversity of those people and their ideas that"
  },
  {
    "company": "Apple",
    "source": "apple_official_careers",
    "job_id": "200679909-0836",
    "title": "Software Engineer - VE",
    "location": "Cupertino, United States of America",
    "official_url": "https://jobs.apple.com/en-us/details/200679909/software-engineer-ve",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:25:18.016759+00:00",
    "date_confidence": "high",
    "description": "The people here at Apple don't just create products, they create the kind of wonder that's revolutionized entire industries. It's the diversity of those people and their ideas that"
  }
]
```

## Microsoft

- Status: ok
- Scraping method: HTTP GET Eightfold PCSX /api/pcsx/search (+ optional position_details)
- Search URL/API: `https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=software+engineer&location=United+States&sort_by=timestamp&start=0&num=10`
- Pagination: start=0,10,20,... ; num=10 (API cap); stop on empty/repeat or count
- Pages/requests fetched: 81
- Raw jobs found: 795
- After US/location filtering: 595
- With trustworthy posted_date: 595
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200049409",
    "title": "Principal Software Engineer for Copilot Evals",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556971984",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:26:50.929068+00:00",
    "date_confidence": "high",
    "description": "Overview CADET (Customer and Analytics Driven Evals Team) is building a customer-grounded quality system for Copilot. Our mission is to rapidly identify the customer scenarios that"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200045858",
    "title": "Principal Software Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556948011",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:26:50.929068+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft 365 and Copilot run on Substrate & Work IQ (SWIQ) — the trusted data and intelligence platform behind Microsoft 365. In plain terms, SWIQ is the secure foundatio"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200043370",
    "title": "Principal Platform Power and Performance Engineer",
    "location": "United States, Washington, Redmond; United States, Oregon, Hillsboro; United States, California, Mountain View",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556929417",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:26:50.929068+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200051594",
    "title": "Firmware Engineer",
    "location": "United States, Washington, Redmond; United States, California, Mountain View; United States, Texas, Austin; United States, North Carolina, Raleigh; United States, Oregon, Hillsboro",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556981432",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:26:50.929068+00:00",
    "date_confidence": "high",
    "description": "Overview Microsoft Silicon, Cloud Hardware, and Infrastructure Engineering (SCHIE) is the team behind Microsoft’s expanding Cloud Infrastructure and responsible for powering Micros"
  },
  {
    "company": "Microsoft",
    "source": "microsoft_official_careers",
    "job_id": "200046664",
    "title": "Principal Hardware Security & Platform Engineer",
    "location": "United States, Washington, Redmond",
    "official_url": "https://apply.careers.microsoft.com/careers/job/1970393556955543",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:26:50.929068+00:00",
    "date_confidence": "high",
    "description": "Overview Do you want to be at the forefront of innovating the latest hardware designs to propel Microsoft’s cloud growth? Are you seeking a unique career opportunity that combines "
  }
]
```

## NVIDIA

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 68
- Raw jobs found: 1294
- After US/location filtering: 1070
- With trustworthy posted_date: 1070
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
    "fetched_at": "2026-08-26T16:28:53.655155+00:00",
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
    "fetched_at": "2026-08-26T16:28:53.655155+00:00",
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
    "fetched_at": "2026-08-26T16:28:53.655155+00:00",
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
    "fetched_at": "2026-08-26T16:28:53.655155+00:00",
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
    "fetched_at": "2026-08-26T16:28:53.655155+00:00",
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
- Raw jobs found: 613
- After US/location filtering: 242
- With trustworthy posted_date: 241
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357686",
    "title": "RVP, Sales",
    "location": "Ontario - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Ontario---Remote/RVP--Sales_JR357686",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:32:36.446628+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR356261",
    "title": "Senior/Lead Software Engineer, Developer Productivity (AI Tooling)",
    "location": "California - San Francisco",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/California---San-Francisco/Senior-Lead-Software-Engineer--Developer-Productivity--AI-Tooling-_JR356261",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:32:36.446628+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR357685",
    "title": "RVP, Sales",
    "location": "British Columbia - Remote",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/British-Columbia---Remote/RVP--Sales_JR357685",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:32:36.446628+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Sales Job Details A"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR355969",
    "title": "Senior Staff, Software Engineer - Slack Front End Infrastructure",
    "location": "Georgia - Atlanta",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Georgia---Atlanta/Senior-Staff--Software-Engineer---Slack-Front-End-Infrastructure_JR355969-1",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:32:36.446628+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Software Engineerin"
  },
  {
    "company": "Salesforce",
    "source": "salesforce_official_careers",
    "job_id": "JR355119",
    "title": "Sr. DNS Engineer",
    "location": "Washington - Bellevue",
    "official_url": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Washington---Bellevue/Sr-DNS-Engineer_JR355119",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:32:36.446628+00:00",
    "date_confidence": "high",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months to ensure you are not duplicating efforts. Job Category Enterprise Technolo"
  }
]
```

## Adobe

- Status: ok
- Scraping method: HTTP POST Workday CXS /wday/cxs/{tenant}/{site}/jobs (+ optional job detail GET)
- Search URL/API: `https://adobe.wd5.myworkdayjobs.com/external_experienced`
- Pagination: offset=0,20,40,... ; limit=20; stop on empty/repeat or total
- Pages/requests fetched: 25
- Raw jobs found: 427
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
    "posted_date": "2026-07-27",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:34:50.135994+00:00",
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
    "fetched_at": "2026-08-26T16:34:50.135994+00:00",
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
    "posted_date": "2026-07-27",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:34:50.135994+00:00",
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
    "fetched_at": "2026-08-26T16:34:50.135994+00:00",
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
    "fetched_at": "2026-08-26T16:34:50.135994+00:00",
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
- Pages/requests fetched: 13
- Raw jobs found: 225
- After US/location filtering: 157
- With trustworthy posted_date: 157
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
    "fetched_at": "2026-08-26T16:36:59.372318+00:00",
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
    "fetched_at": "2026-08-26T16:36:59.372318+00:00",
    "date_confidence": "high",
    "description": "About the role and team Working at Uber means solving hard problems in a high-stakes, fast-moving environment. As a Senior Application Developer, you will be a technical leader and"
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
    "fetched_at": "2026-08-26T16:36:59.372318+00:00",
    "date_confidence": "high",
    "description": "About the Role The FinTech team, part of the CFO’s organization, is responsible for innovating and building the best financial products and systems in the world. We are obsessed wi"
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
    "fetched_at": "2026-08-26T16:36:59.372318+00:00",
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
    "fetched_at": "2026-08-26T16:36:59.372318+00:00",
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
    "fetched_at": "2026-08-26T16:38:07.097438+00:00",
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
    "fetched_at": "2026-08-26T16:38:07.097438+00:00",
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
    "fetched_at": "2026-08-26T16:38:07.097438+00:00",
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
    "fetched_at": "2026-08-26T16:38:07.097438+00:00",
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
    "fetched_at": "2026-08-26T16:38:07.097438+00:00",
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
- Raw jobs found: 91
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
    "fetched_at": "2026-08-26T16:38:08.408434+00:00",
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
    "fetched_at": "2026-08-26T16:38:08.408434+00:00",
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
    "fetched_at": "2026-08-26T16:38:08.408434+00:00",
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
    "fetched_at": "2026-08-26T16:38:08.408434+00:00",
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
    "posted_date": "2026-07-27",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:38:08.408434+00:00",
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
- Raw jobs found: 216
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
    "fetched_at": "2026-08-26T16:38:36.836999+00:00",
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
    "fetched_at": "2026-08-26T16:38:36.836999+00:00",
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
    "fetched_at": "2026-08-26T16:38:36.836999+00:00",
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
    "fetched_at": "2026-08-26T16:38:36.836999+00:00",
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
    "fetched_at": "2026-08-26T16:38:36.836999+00:00",
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
- Raw jobs found: 384
- After US/location filtering: 305
- With trustworthy posted_date: 305
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
    "fetched_at": "2026-08-26T16:38:37.260140+00:00",
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
    "fetched_at": "2026-08-26T16:38:37.260140+00:00",
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
    "fetched_at": "2026-08-26T16:38:37.260140+00:00",
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
    "fetched_at": "2026-08-26T16:38:37.260140+00:00",
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
    "fetched_at": "2026-08-26T16:38:37.260140+00:00",
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
- Raw jobs found: 256
- After US/location filtering: 190
- With trustworthy posted_date: 190
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0075001",
    "title": "Senior Staff Software Engineer – SRE & AIOps",
    "location": "Santa Clara, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145786989-senior-staff-software-engineer-sre-aiops",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:38:37.710930+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074985",
    "title": "Global Director, Global Technology Partnerships",
    "location": "San Diego, California, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145585164-global-director-global-technology-partnerships-",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:38:37.710930+00:00",
    "date_confidence": "high",
    "description": "It all started when engineer Fred Luddy wrote code that automated a tedious task for his coworker, Phyllis. She cried tears of joy. That moment inspired Fred to build a company tha"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0070796",
    "title": "Senior Software Engineer, Core Infrastructure - Moveworks",
    "location": "Mountain View, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145579989-senior-software-engineer-core-infrastructure-moveworks",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:38:37.710930+00:00",
    "date_confidence": "high",
    "description": "It all started in sunny San Diego, California in 2004 when a visionary engineer, Fred Luddy, saw the potential to transform how we work. Fast forward to today — ServiceNow stands a"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0072947",
    "title": "Director, Data Strategy & Services",
    "location": "Santa Clara, California , United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145574214-director-data-strategy-services-",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:38:37.710930+00:00",
    "date_confidence": "high",
    "description": "It all started in sunny San Diego, California in 2004 when a visionary engineer, Fred Luddy, saw the potential to transform how we work. Fast forward to today — ServiceNow stands a"
  },
  {
    "company": "ServiceNow",
    "source": "servicenow_official_careers",
    "job_id": "JB0074540",
    "title": "Senior Software Engineer - Data Platform - Kubernetes - Federal",
    "location": "San Diego, CALIFORNIA, United States",
    "official_url": "https://jobs.smartrecruiters.com/ServiceNow/744000145410729-senior-software-engineer-data-platform-kubernetes-federal",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:38:37.710930+00:00",
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
- Raw jobs found: 746
- After US/location filtering: 211
- With trustworthy posted_date: 0
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21620",
    "title": "Director, Product Marketing (Core Media)",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Director-Product-Marketing-Core-Media/21620",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:40:27.819641+00:00",
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
    "fetched_at": "2026-08-26T16:40:27.819641+00:00",
    "date_confidence": "unknown",
    "description": "Director, Product Marketing (Audience, Data & Emerging)"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21591",
    "title": "BNEF Account Manager, Financial Solutions",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/BNEF-Account-Manager-Financial-Solutions/21591",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:40:27.819641+00:00",
    "date_confidence": "unknown",
    "description": "BNEF Account Manager, Financial Solutions"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21596",
    "title": "Senior Account Executive - Financial Services",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Senior-Account-Executive-Financial-Services/21596",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:40:27.819641+00:00",
    "date_confidence": "unknown",
    "description": "Senior Account Executive - Financial Services"
  },
  {
    "company": "Bloomberg",
    "source": "bloomberg_official_careers",
    "job_id": "21578",
    "title": "Service Specialist, Employee Technology Support",
    "location": "New York, New York, United States of America",
    "official_url": "https://bloomberg.avature.net/careers/JobDetail/Service-Specialist-Employee-Technology-Support/21578",
    "posted_date": "",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:40:27.819641+00:00",
    "date_confidence": "unknown",
    "description": "Service Specialist, Employee Technology Support"
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
- After US/location filtering: 943
- With trustworthy posted_date: 943
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
    "fetched_at": "2026-08-26T16:45:24.567351+00:00",
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
    "fetched_at": "2026-08-26T16:45:24.567351+00:00",
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
    "fetched_at": "2026-08-26T16:45:24.567351+00:00",
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
    "fetched_at": "2026-08-26T16:45:24.567351+00:00",
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
    "fetched_at": "2026-08-26T16:45:24.567351+00:00",
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
- Raw jobs found: 1360
- After US/location filtering: 967
- With trustworthy posted_date: 967
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999221",
    "title": "Senior Manager, Risk Data Product Manager",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Manager---Risk-Data-Product-Manager_R999221-1",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:47:50.593840+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Risk Data Product Manager Product Management at Capital One is a booming, vibrant craft that requires reimagining the status quo, finding value creation opportuniti"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999164",
    "title": "Lead Software Engineer, Full Stack",
    "location": "Boston, MA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Boston-MA/Lead-Software-Engineer--Full-Stack_R999164-1",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:47:50.593840+00:00",
    "date_confidence": "high",
    "description": "Lead Software Engineer, Full Stack Do you love building and pioneering in the technology space? Do you enjoy solving complex business problems in a fast-paced, collaborative, inclu"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999098",
    "title": "Senior Associate Product Management - Authorizations Data Platform",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Senior-Associate-Product-Management---Authorizations-Data-Platform_R999098-1",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:47:50.593840+00:00",
    "date_confidence": "high",
    "description": "Senior Associate Product Management - Authorizations Data Platform Product Management Product Management at Capital One is a booming, vibrant craft that requires reimagining the st"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R999188",
    "title": "Senior Manager, Technical Program Management",
    "location": "Chicago, IL",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/Chicago-IL/Senior-Manager--Technical-Program-Management_R999188-1",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:47:50.593840+00:00",
    "date_confidence": "high",
    "description": "Senior Manager, Technical Program Management Are you interested in leading programs that deliver on critical business goals and build large scale products & platforms? At Capital O"
  },
  {
    "company": "Capital One",
    "source": "capital_one_official_careers",
    "job_id": "R248338",
    "title": "Sr. Business Analyst - US Card",
    "location": "McLean, VA",
    "official_url": "https://capitalone.wd12.myworkdayjobs.com/Capital_One/job/McLean-VA/Sr-Business-Analyst---US-Card_R248338-1",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:47:50.593840+00:00",
    "date_confidence": "high",
    "description": "Sr. Business Analyst - US Card Summary: As a Senior Business Analyst at Capital One, you will apply your strategic and analytical skills to major company challenges. You will team "
  }
]
```

## Oracle

- Status: ok
- Scraping method: HTTP GET Oracle Cloud HCM recruitingCEJobRequisitions (+ details)
- Search URL/API: `https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_45001/requisitions?keyword=software+engineer`
- Pagination: finder offset=0,20,... ; limit=20; stop on empty/repeat or TotalJobsCount
- Pages/requests fetched: 66
- Raw jobs found: 1308
- After US/location filtering: 773
- With trustworthy posted_date: 773
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "342728",
    "title": "Senior Platform Software Engineer",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/342728",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:49:33.456244+00:00",
    "date_confidence": "high",
    "description": "As a Senior Software Development Engineer on OCI Build, you will independently design, build, and operate components of a critical OCI developer infrastructure platform. You will s"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "342348",
    "title": "Software Engineer, Core Infrastructure",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/342348",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:49:33.456244+00:00",
    "date_confidence": "high",
    "description": "Join Oracle Cloud Infrastructure (OCI) as a Senior Core Infrastructure Engineer and play a pivotal role in shaping the future of cloud computing. In this role, you will lead the de"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "341412",
    "title": "Director, Platform Software Engineering",
    "location": "United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/341412",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:49:33.456244+00:00",
    "date_confidence": "high",
    "description": "Leads a platform group; develops strategies and plans that standardize runtimes, APIs, and SDKs across several teams. Accountable for group results and governance adherence; makes "
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "343031",
    "title": "Senior Engineer, Core Infrastructure",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/343031",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:49:33.456244+00:00",
    "date_confidence": "high",
    "description": "Within OCI, the Technical Strategy & Oversight organization builds foundational systems for OCI’s most demanding services. One of its boldest initiatives is Autonomous OCI: a green"
  },
  {
    "company": "Oracle",
    "source": "oracle_official_careers",
    "job_id": "343034",
    "title": "Senior Engineer, Core Infrastructure",
    "location": "Nashville, TN, United States",
    "official_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/343034",
    "posted_date": "2026-08-26",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:49:33.456244+00:00",
    "date_confidence": "high",
    "description": "Within OCI, the Technical Strategy & Oversight organization builds foundational systems for OCI’s most demanding services. One of its boldest initiatives is Autonomous OCI: a green"
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
- Raw jobs found: 647
- After US/location filtering: 212
- With trustworthy posted_date: 212
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2020847",
    "title": "Software Engineer",
    "location": "Milpitas, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/Milpitas-California-US/Software-Engineer_2020847",
    "posted_date": "2026-08-25",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:51:54.430131+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 08/26/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Mee"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2023592",
    "title": "Software Engineer",
    "location": "San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Software-Engineer_2023592-1",
    "posted_date": "2026-08-24",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:51:54.430131+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/23/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Mee"
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
    "fetched_at": "2026-08-26T16:51:54.430131+00:00",
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
    "fetched_at": "2026-08-26T16:51:54.430131+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/29/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Thi"
  },
  {
    "company": "Cisco",
    "source": "cisco_official_careers",
    "job_id": "2021192",
    "title": "Engineering Program Manager",
    "location": "San Jose, California, US",
    "official_url": "https://cisco.wd5.myworkdayjobs.com/Cisco_Careers/job/San-Jose-California-US/Engineering-Program-Manager_2021192-1",
    "posted_date": "2026-08-21",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:51:54.430131+00:00",
    "date_confidence": "high",
    "description": "The application window is expected to close on: 09/20/2026 Job posting may be removed earlier if the position is filled or if a sufficient number of applications are received . Mee"
  }
]
```

## SAP

- Status: ok
- Scraping method: HTTP GET jobs.sap.com/search HTML + job detail HTML
- Search URL/API: `https://jobs.sap.com/search/?q=software+engineer&locationsearch=United+States`
- Pagination: startrow=0,25,... ; stop on empty/repeat or short page
- Pages/requests fetched: 16
- Raw jobs found: 364
- After US/location filtering: 171
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
    "fetched_at": "2026-08-26T16:53:32.667853+00:00",
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
    "fetched_at": "2026-08-26T16:53:32.667853+00:00",
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
    "fetched_at": "2026-08-26T16:53:32.667853+00:00",
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
    "fetched_at": "2026-08-26T16:53:32.667853+00:00",
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
    "fetched_at": "2026-08-26T16:53:32.667853+00:00",
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
- Raw jobs found: 576
- After US/location filtering: 234
- With trustworthy posted_date: 234
- Errors/403s: none

Sample normalized records:

```json
[
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1202357",
    "title": "Principal Software Engineer",
    "location": "Cupertino, California, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Cupertino-California-United-States-of-America/Principal-Software-Engineer_1202357-2",
    "posted_date": "2026-07-27",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:55:20.751642+00:00",
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
    "posted_date": "2026-07-27",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:55:20.751642+00:00",
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
    "fetched_at": "2026-08-26T16:55:20.751642+00:00",
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
    "posted_date": "2026-07-27",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:55:20.751642+00:00",
    "date_confidence": "medium",
    "description": ""
  },
  {
    "company": "HPE",
    "source": "hpe_official_careers",
    "job_id": "1207852",
    "title": "Software Engineer II",
    "location": "Roseville, California, United States of America",
    "official_url": "https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Roseville-California-United-States-of-America/Software-Engineer-II_1207852-2",
    "posted_date": "2026-08-03",
    "updated_date": "",
    "fetched_at": "2026-08-26T16:55:20.751642+00:00",
    "date_confidence": "high",
    "description": "Software Engineer II This role has been designed as 'Hybrid' with a requirement that you will work on average 2 days per week from an HPE office. Who We Are: Hewlett Packard Enterp"
  }
]
```
