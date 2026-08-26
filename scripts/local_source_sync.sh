#!/usr/bin/env bash
#
# Local source sync: scrape LinkedIn + Glassdoor, then commit/push ONLY the
# source snapshots if they changed. Intended to be driven by launchd every
# 2-3 hours (see scripts/macos/). Safe to run manually for testing.
#
# Guarantees per plan:
#   - Only `output/sources/*.json` is staged. Never `git add -A`.
#   - jobs.json / latest.md are GitHub-Actions-owned; this script never touches them.
#   - No commit is created when nothing changed.
#   - Never edits git config; relies on existing SSH / gh credentials.
#
# Env:
#   PYTHON_BIN   python interpreter (default: python3)
#   SKIP_PUSH=1  commit locally but do not push (useful for first-time testing)
#   NO_GIT=1     run the scrape only; skip all git operations
#
set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR" || exit 1

PYTHON_BIN="${PYTHON_BIN:-python3}"
LOG_DIR="$REPO_DIR/output/logs"
mkdir -p "$LOG_DIR"
STAMP="$(date +%Y-%m-%d_%H%M)"

# Load .env WITHOUT echoing secrets and WITHOUT executing file contents.
# Parses KEY=VALUE lines, tolerating spaces around '=' and surrounding quotes.
if [ -f "$REPO_DIR/.env" ]; then
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in
      ''|'#'*) continue ;;
    esac
    key="${line%%=*}"
    val="${line#*=}"
    # Trim surrounding whitespace.
    key="$(printf '%s' "$key" | tr -d '[:space:]')"
    val="${val#"${val%%[![:space:]]*}"}"
    val="${val%"${val##*[![:space:]]}"}"
    # Strip matching surrounding quotes.
    case "$val" in
      \"*\") val="${val%\"}"; val="${val#\"}" ;;
      \'*\') val="${val%\'}"; val="${val#\'}" ;;
    esac
    [ -n "$key" ] && export "$key=$val"
  done < "$REPO_DIR/.env"
fi

echo "[$STAMP] scraping local sources..."
"$PYTHON_BIN" local_sources.py
SCRAPE_RC=$?
if [ $SCRAPE_RC -ne 0 ]; then
  echo "[$STAMP] scrape exited $SCRAPE_RC (continuing to git step; snapshots preserved)"
fi

if [ "${NO_GIT:-0}" = "1" ]; then
  echo "[$STAMP] NO_GIT=1 set; skipping git sync."
  exit 0
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[$STAMP] not a git repo; skipping git sync. Initialize a repo + remote to enable auto-push."
  exit 0
fi

# Stage ONLY the source snapshots.
git add output/sources/linkedin.json output/sources/glassdoor.json 2>/dev/null

if git diff --staged --quiet; then
  echo "[$STAMP] no source changes; nothing to commit."
  exit 0
fi

git commit -m "chore: local job sources ${STAMP}" || {
  echo "[$STAMP] commit failed."
  exit 1
}

if [ "${SKIP_PUSH:-0}" = "1" ]; then
  echo "[$STAMP] SKIP_PUSH=1 set; committed locally, not pushing."
  exit 0
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"
echo "[$STAMP] pushing ${BRANCH}..."
if git push origin "HEAD:${BRANCH}"; then
  echo "[$STAMP] pushed. GitHub Actions will ingest the updated sources."
else
  echo "[$STAMP] push failed (commit is saved locally; will push next run)."
  exit 1
fi
