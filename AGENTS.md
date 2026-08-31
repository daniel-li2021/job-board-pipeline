# Codex guidance

Optimize for focused, token-efficient changes and keep Git state easy to reason about.

## Start here
- Dashboard/display/filter changes → `dashboard.py`
- ATS / LinkedIn → `board_pipeline.py`
- Syncareer → `daily_pipeline.py`
- Big Company Official → `official_careers.py`
- Shared job schema / normalization → `sources/schema.py`
- Shared/company configuration → `profile/` and `source/`
- Full architecture and pipeline documentation → `README.md`

## Rules
- Before editing, run `git fetch origin`, inspect `git status --short`, and compare `HEAD...origin/main`.
- If the current checkout is clean and only behind `origin/main`, fast-forward it with `git pull --ff-only`; do not create a new worktree just because automation advanced `main`.
- If the checkout is dirty or diverged, preserve it and create a clean `codex/<task>` branch/worktree from current `origin/main`. Never reset, clean, merge, or rebase unknown local changes.
- A dirty checkout during active editing is normal; do not leave stale uncommitted changes or temporary worktrees after the task is finished.
- Start new code changes from current `origin/main`, not from an old reused task branch.
- After the requested behavior is implemented and targeted validation passes, commit it and publish it to the latest `origin/main` by default without waiting for confirmation. Only stop before publishing for conflicts, failing tests, uncertain local changes, or another real safety issue.
- If a temporary task branch/worktree was used, integrate the validated commit into the latest `main`, push `main`, verify the remote commit, then remove the temporary local/remote task branch and worktree when no longer needed.
- Start with the responsible file above, then inspect only files required by the task.
- Use targeted searches and line ranges; do not repeatedly reread whole files.
- Reuse existing output data, scores, tiers, caches, and snapshots.
- Dashboard-only changes must not rerun crawlers, pipelines, or LLM scoring.
- Do not modify scoring/ranking unless explicitly requested.
- Avoid unrelated refactors and generated-output churn.
- Run targeted tests only; use the full suite only when necessary.
- Stop after the requested behavior is implemented, validated, published, and Git cleanup is complete.
- Keep progress updates and the final summary concise.
