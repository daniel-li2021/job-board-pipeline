# Resume Profile — AI Engineer / Applied AI / AI Platform / LLM Systems

## Summary
AI Engineer building production LLM and agent systems for enterprise knowledge and evaluation products. Experienced owning the full AI lifecycle—from multimodal ingestion and hybrid retrieval through agent orchestration, model serving, evaluation and observability, and cloud deployment—with a focus on reliable, cost-efficient AI in production.

## Education
- **University of Southern California** — M.S. Computer Science, Aug 2024 — May 2026
- **University of California, Santa Barbara** — B.S. Computer Science & Applied Mathematics, Sep 2021 — Jun 2024

## Experience

### AI Engineer — VortexNet
Covina, CA | Nov 2025 — Apr 2026
- Delivered an enterprise knowledge agent for support and implementation teams, using LangChain/LangGraph, MCP tool calling, and memory to ground answers across enterprise documentation, reducing lookups by 40%.
- Improved retrieval over complex enterprise PDFs using structure-aware parsing, VLM captions for tables/charts, and parent-child chunking, raising context precision from 0.48 to 0.85 on an internal QA benchmark.
- Diagnosed dense-only failures on IDs, error codes, and versions using a 120-query golden set; implemented hybrid retrieval with BM25+dense search, RRF, reranking, and version filters, lifting Recall@10 from 74% to 92%.
- Fine-tuned and served a Qwen3-class model with QLoRA/PEFT and vLLM for high-volume requests, routing complex queries to frontier fallbacks and cutting inference cost by 60% while staying within 2 points of baseline quality.
- Deployed Dockerized FastAPI services on AWS via CI/CD, cutting release cycles from hours to minutes; added LangSmith tracing, Ragas evals, and regression gates with structured-output validation and safety guardrails to catch retrieval and generation failures before release.

### Software Engineer Intern, Applied AI & Digital Solutions — AptarGroup, Inc.
Jun 2025 — Aug 2025
- Automated a pharmaceutical news intelligence workflow for Strategy & Market Intelligence using Dataiku agents for screening/extraction and LLM summaries with human review, cutting newsletter preparation time by 45%.
- Engineered a resilient Python ingestion pipeline with requests, Selenium fallback, content validation, retries, and categorized error handling, processing 10,000+ articles/day with 94% parsing success across supported pages.
- Implemented a KIE evaluation framework for beauty reviews, standardizing JSONL ground truth across a 20-category taxonomy, creating train/test splits, and benchmarking model predictions with 80%+ field-level agreement.
- Reduced false-positive nitrosamine risk alerts by 20% across 10+ product lines by tracing formulation lineage and adding ingredient/unit normalization, version-aware joins, and deduplication in Spark/Databricks.

### AI Research Engineer, LLM Evaluation — University of Southern California
May 2025 — Feb 2026
- Developed CounselReflect, an LLM conversation-evaluation platform spanning 12 model-trained metrics, 69 rubric-based metrics, and 10,000+ labeled samples across 8+ public dialogue datasets.
- Unified a React web app, Chrome extension, and FastAPI batch service behind a shared evaluation engine, standardizing turn- and session-level analysis across ChatGPT, Gemini, Claude, and offline workflows.
- Refactored the evaluator backend with typed schemas, provider abstractions, structured outputs, caching, and retries, reducing new-evaluator integration touchpoints from 6–8 to 2–3, backed by 90+ unit/integration tests.
- Validated platform effectiveness through an N=26 human study with counseling users and therapists, measuring usability, trust, authenticity, and satisfaction to support academic publication and deployment.

### AI Platform Engineer Intern — YunXuetang
Suzhou, China | Jun 2023 — Sep 2023
- Optimized vector retrieval for an enterprise learning platform serving 7K+ active users through batched embeddings, connection pooling, metadata-aware retrieval, and vector-search tuning, cutting query latency by 54%.
- Designed long-document processing workflows with hierarchical chunking, staged summarization, and context-window management, enabling reliable processing of 30K+ token enterprise documents.
- Implemented a learner-engagement risk prediction pipeline using behavioral feature engineering, class balancing, and baseline ML models, improving macro-F1 from 0.74 to 0.84 while automating at-risk learner reporting.

## Technical Skills
- **Programming & Backend:** Python, SQL, TypeScript/JavaScript, Java, C++, Bash, FastAPI, Node.js, REST APIs, System Design, Microservices, Async Programming, Streaming APIs/SSE, Redis
- **AI Engineering:** Production AI Systems, RAG, Retrieval Systems, AI Agents, Agent Orchestration, MCP, Tool Calling, Multimodal AI, LLM Evaluation, Fine-tuning, Guardrails, LangChain/LangGraph, Cursor, Claude Code
- **MLOps & Reliability:** Observability, LangSmith, MLflow, Regression Testing, GitHub Actions, CI/CD, Kubernetes
- **Data & Cloud:** Data Pipelines, Spark, Databricks, PostgreSQL, Vector Databases, AWS, GCP, Docker, Terraform
