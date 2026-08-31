# AI / Applied AI / LLM Systems Evidence

## Education
USC — M.S. Computer Science, Aug 2024–May 2026
UCSB — B.S. Computer Science & Applied Mathematics, Sep 2021–Jun 2024

## Experience

### VortexNet — AI Engineer | Nov 2025–Apr 2026
- Built production enterprise knowledge agent for support/implementation teams using LangChain/LangGraph, MCP tool calling, memory; reduced repetitive lookups 40%.
- Complex-document RAG: structure-aware parsing, VLM table/chart captions, parent-child chunking; context precision 0.48→0.85.
- Diagnosed retrieval failures with 120-query golden set; BM25+dense retrieval, RRF, reranking, version filters improved Recall@10 74%→92%.
- Fine-tuned Qwen3-class model with QLoRA/PEFT; served via vLLM with frontier fallback routing, cutting inference cost 60% while staying within ~2 points of baseline quality.
- Productionized Dockerized FastAPI on AWS via CI/CD; LangSmith tracing, Ragas evaluation, structured-output validation, regression gates, guardrails.

### AptarGroup — Software Engineer Intern, Applied AI & Digital Solutions | Jun–Aug 2025
- Automated pharmaceutical news-intelligence workflow using Dataiku agents for screening/extraction and LLM summaries with human review; reduced newsletter preparation time 45%.
- Built resilient Python ingestion with requests, Selenium fallback, validation, retries, categorized errors; 10K+ articles/day, 94% parsing success.
- Built KIE evaluation framework with versioned JSONL ground truth, train/test splits, 20-category taxonomy; 80%+ field-level agreement.
- Reduced nitrosamine-risk false positives 20% across 10+ product lines via formulation lineage analysis, normalization, version-aware joins, deduplication in Spark/Databricks.

### USC — AI Research Engineer, LLM Evaluation | May 2025–Feb 2026
- Built CounselReflect LLM evaluation platform: 12 model-trained + 69 rubric metrics, 10K+ labeled samples across 8+ public dialogue datasets.
- Unified React web app, Chrome extension, and FastAPI batch service behind shared evaluation engine for ChatGPT, Gemini, Claude, and offline workflows.
- Built typed schemas, provider abstractions, structured outputs, caching, retries; reduced new-evaluator integration touchpoints 6–8→2–3; backed by 90+ unit/integration tests.
- Validated platform through N=26 human study with counseling users and therapists.

### YunXuetang — AI Platform Engineer Intern | Jun–Sep 2023
- Optimized vector retrieval for enterprise learning platform serving 7K+ active users using batched embeddings, connection pooling, metadata-aware retrieval, vector-search tuning; query latency -54%.
- Built long-document workflows for 30K+ token documents with hierarchical chunking, staged summarization, context-window management.
- Built learner-risk ML pipeline with feature engineering/class balancing/baseline models; macro-F1 0.74→0.84.

## Skills
Programming/Backend: Python, SQL, TypeScript/JavaScript, Java, C++, Bash, FastAPI, Node.js, REST APIs, microservices, async programming, SSE, Redis
AI: production LLM systems, RAG, retrieval, hybrid search, reranking, AI agents, LangChain/LangGraph, MCP, tool calling, multimodal AI, fine-tuning, QLoRA/PEFT, vLLM, guardrails
Evaluation/MLOps: LLM evaluation, Ragas, LangSmith, MLflow, structured outputs, regression testing, observability, GitHub Actions, CI/CD, Kubernetes
Data/Cloud: Spark, Databricks, PostgreSQL, vector databases, AWS, GCP, Docker, Terraform