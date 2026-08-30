# Codex guidance

Optimize for focused, token-efficient changes.

## Start here
- Dashboard/display/filter changes → `dashboard.py`
- ATS / LinkedIn → `board_pipeline.py`
- Syncareer → `daily_pipeline.py`
- Big Company Official → `official_careers.py`
- Shared/company configuration → `profile/` and `source/`
- Full architecture and pipeline documentation → `README.md`

## Rules
- Start with the responsible file above, then inspect only files required by the task.
- Use targeted searches and line ranges; do not repeatedly reread whole files.
- Do not scan unrelated tests, pipelines, workflows, or configuration.
- Reuse existing output data, scores, tiers, caches, and snapshots.
- Dashboard-only changes must not rerun crawlers, pipelines, or LLM scoring.
- Do not modify scoring/ranking unless explicitly requested.
- Avoid unrelated refactors.
- Run targeted tests only; use the full suite only when necessary.
- Stop after the requested behavior is implemented and validated.
- Keep progress updates and the final summary concise.
