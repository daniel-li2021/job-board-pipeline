# Candidate Search & Matching Profile

## Goal
Use broad recall at discovery time, then rank precisely using job title, job description, seniority, hard constraints, and the most relevant resume profile.

Do not require a job to match many keywords simultaneously. A role should enter the candidate pool if its core responsibilities clearly align with either:
1. backend / software systems / platform engineering, or
2. production AI / ML / LLM systems.

## Priority Role Families

### Software / Backend / Platform
- Software Engineer
- Software Development Engineer
- SWE
- Backend Engineer
- Backend Software Engineer
- Full Stack Engineer
- Full-Stack Software Engineer
- Platform Engineer
- Software Platform Engineer
- Infrastructure Engineer
- Software Infrastructure Engineer
- Cloud Software Engineer
- Distributed Systems Engineer
- Data Platform Engineer
- Data Engineer, when software/platform-oriented

### AI / ML / Applied AI
- AI Engineer
- Applied AI Engineer
- ML Engineer
- Machine Learning Engineer
- AI Platform Engineer
- ML Platform Engineer
- LLM Engineer
- Generative AI Engineer
- AI Infrastructure Engineer
- ML Infrastructure Engineer
- Retrieval Engineer
- Search Engineer
- Agent Engineer
- Agentic AI Engineer
- Forward Deployed Engineer, when software / AI implementation-oriented

## Positive Matching Signals

### Backend / SWE
`Python`, `Java`, `TypeScript`, `JavaScript`, `SQL`, `FastAPI`, `Node.js`, `Spring Boot`, `REST API`, `microservices`, `distributed systems`, `async`, `concurrency`, `backend`, `data pipelines`, `Spark`, `Databricks`, `PostgreSQL`, `Redis`, `AWS`, `Docker`, `Kubernetes`, `CI/CD`, `reliability`, `scalability`, `system design`.

### AI / Applied AI
`LLM`, `RAG`, `retrieval`, `information retrieval`, `hybrid search`, `reranking`, `AI agents`, `agent orchestration`, `MCP`, `tool calling`, `LangChain`, `LangGraph`, `LLM evaluation`, `fine-tuning`, `model serving`, `vLLM`, `PyTorch`, `MLflow`, `LangSmith`, `vector database`, `multimodal`, `guardrails`, `AI platform`.

## Seniority Preference
Prioritize:
- New Grad
- Early Career
- Entry Level
- Software Engineer I
- Engineer I
- Associate
- 0–3 years

Do **not** automatically reject 3–5 years. Keep the role if responsibilities and skill alignment are strong.

Strongly down-rank or reject:
- Senior
- Staff
- Principal
- Lead
- Roles that explicitly require 5–7+ years and do not otherwise look early-career compatible

## Hard Constraints
Reject or heavily down-rank:
- U.S. Citizen-only requirements
- Security clearance requirements
- Roles restricted to candidates who already hold a clearance
- Non-U.S. roles when the pipeline is configured for U.S.-only search
- Clearly hardware-first roles such as FPGA / RTL / ASIC / board design / electrical engineering, unless the actual role is clearly software/platform-focused

## Resume Routing
Use the most relevant resume profile for LLM matching:

- **SWE / Backend / Full Stack / Platform / Infrastructure / Data Platform** → `resume_swe.md`
- **AI Engineer / Applied AI / LLM / RAG / ML Platform / AI Infrastructure / Retrieval / Agentic AI** → `resume_ai.md`
- **Mixed or ambiguous role** → consider both profiles and use whichever yields the stronger evidence-based match

## Matching Philosophy
- Optimize discovery for **recall**, not precision.
- Do not over-filter based on title alone.
- Use title + responsibilities + required qualifications together.
- Skills in the job description are signals, not mandatory keyword checkboxes.
- Prefer evidence from actual experience over superficial keyword overlap.
- Prefer recent postings and roles with clear requirements.
- Verified official job URLs should rank above unverified third-party listings when other factors are similar.

## Search vs Match Separation
ATS sources such as Greenhouse, Lever, and Ashby should generally pull the configured company's available job list once per run rather than issuing separate API requests for each keyword.

After ingestion:
1. Normalize jobs.
2. Apply hard filters.
3. Detect likely role family.
4. Route to the relevant resume profile.
5. Apply rule-based scoring.
6. Run LLM matching only on new jobs that survive hard filtering.
7. Cache the result so unchanged jobs are not repeatedly re-scored.

## Suggested LLM Output
For each surviving job, return:
- `role_family`
- `resume_profile_used`
- `match_score` (0–100)
- `tier` (`A`, `B`, `C`)
- `top_match_reasons` (2–4 concise reasons)
- `main_gaps` (0–3 concise gaps)
- `seniority_fit`
- `hard_constraint_status`
- `recommended_action` (`referral_now`, `apply_now`, `apply_if_time`, `skip`)

## Tier Guidance
- **Tier A:** Strong fit + recent + requirements are realistic; worth immediate application or referral.
- **Tier B:** Good fit with manageable gaps; worth applying.
- **Tier C:** Weak/uncertain fit, older, unverified, or meaningful seniority mismatch.

## Operational Note
The semantic search/matching policy belongs in this file. Scheduling cadence and workflow behavior should live in pipeline config / GitHub Actions rather than being treated as candidate attributes.

Recommended operational behavior:
- ATS / official discovery: every 2–3 hours
- Rule filtering: every run
- LLM scoring: new + changed surviving jobs only
- Digest / Issue alert: twice daily
