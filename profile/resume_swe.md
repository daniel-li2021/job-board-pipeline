# Resume Profile — SWE / Backend / Full-Stack / Data Systems

## Summary
Software Engineer building production backend services and data-intensive systems, with experience taking systems from design through cloud deployment and production operations. Strong focus on reliability and engineering quality, with additional depth in full-stack development and AI/search products.

## Education
- **University of Southern California** — M.S. Computer Science, Aug 2024 — May 2026
- **University of California, Santa Barbara** — B.S. Computer Science & Applied Mathematics, Sep 2021 — Jun 2024

## Experience

### Software Engineer — VortexNet
Covina, CA | Nov 2025 — Apr 2026
- Delivered a production full-stack knowledge application for support and implementation teams using React, TypeScript, FastAPI, and Node.js, reducing repetitive document lookups by 40%.
- Engineered asynchronous REST and retrieval services with typed contracts, caching, hybrid search, and reranking, sustaining sub-second response times while increasing Recall@10 to 92%.
- Automated deployment of Dockerized FastAPI services to AWS ECS/Fargate through GitHub Actions, with health checks and staged rollouts that reduced release cycles from hours to minutes.
- Established production reliability safeguards with tracing, structured validation, and automated regression testing to catch service and response-quality failures before deployment.

### Software Engineer Intern, Digital Solutions — AptarGroup, Inc.
Crystal Lake, IL | Jun 2025 — Aug 2025
- Engineered a resilient pharmaceutical news-ingestion pipeline for Strategy & Market Intelligence teams, processing 10,000+ articles/day at 94% parsing reliability through Python extraction, browser fallback, and retry handling.
- Productionized ingestion across Dataiku and Databricks workflows with automated validation, retries, and explicit failure routing, preventing malformed or inaccessible content from silently entering daily reports.
- Diagnosed data-quality issues in a Spark/Databricks pharmaceutical risk pipeline by tracing formulation lineage and correcting normalization and join logic, reducing low-signal alerts by 20% across 10+ product lines.
- Developed a reusable automated evaluation harness that benchmarked model endpoints against versioned JSONL ground truth across a 20-category taxonomy, reaching 80%+ field-level label agreement.

### Research Software Engineer — University of Southern California
Los Angeles, CA | May 2025 — Feb 2026
- Delivered CounselReflect, a full-stack evaluation platform for mental-health support conversations, enabling researchers and therapists to analyze 10,000+ labeled samples across 81 model and rubric-based metrics.
- Built three user-facing clients on a shared backend: a React/Vite web application, Chrome MV3 extension for LLM interfaces, and Dockerized batch service, reusing the same evaluation engine across interactive and batch workflows.
- Refactored the FastAPI evaluator backend into a registry-driven architecture with typed contracts and provider abstractions, consolidating changes previously spread across 6–8 integration points.
- Strengthened platform reliability with 90+ unit/integration tests, structured-output validation, caching, and retries, supporting deployment and an N=26 human study with counseling users and therapists.

### Software Engineer Intern, AI Platform — YunXuetang
Suzhou, China | Jun 2023 — Sep 2023
- Optimized backend retrieval services for an enterprise learning platform serving 7K+ active users, reducing query latency by 54% through async batching, connection pooling, and vector-search tuning.
- Implemented and validated REST APIs for retrieval, inference, and reporting workflows, standardizing service contracts and integration testing through Postman and GitLab pipelines.
- Designed server-side long-document processing workflows with segmented chunking, staged summarization, and context management, enabling reliable processing of 30K+ token enterprise documents.

## Technical Skills
- **Languages:** Python, Java, TypeScript/JavaScript, SQL, C++, Bash
- **Core Engineering:** Data Structures & Algorithms, Object-Oriented Design, System Design, Distributed Systems, Microservices, Async Programming, Concurrency, Scalability, Reliability, Performance Optimization
- **Backend & Data:** FastAPI, Node.js/Express, Spring Boot, REST APIs, API Design, PostgreSQL, MySQL, MongoDB, Redis, Caching, Data Pipelines, Spark, Databricks
- **Frontend:** React, Next.js, Angular, Vite, TailwindCSS, Chrome Extension MV3
- **Cloud, Production & Tooling:** AWS (ECS/Fargate), GCP, Docker, Kubernetes, Terraform, GitHub Actions, CI/CD, Observability, Monitoring & Tracing, Unit/Integration/Regression Testing, Linux, Git, Postman, Cursor, Claude Code
- **AI & Search:** Information Retrieval, RAG, Hybrid Search, Reranking, LLM APIs, LLM Evaluation, MLflow, PyTorch
