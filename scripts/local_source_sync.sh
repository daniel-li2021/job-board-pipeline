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
#   TARGET_BRANCH remote branch to update (default: main)
#   SKIP_SCRAPE=1 sync the last good snapshots without scraping again
#   SKIP_PUSH=1  verify the remote-main diff but do not commit or push
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
if [ "${SKIP_SCRAPE:-0}" = "1" ]; then
  echo "[$STAMP] SKIP_SCRAPE=1 set; using the last good snapshots."
else
  "$PYTHON_BIN" local_sources.py
  SCRAPE_RC=$?
  if [ $SCRAPE_RC -ne 0 ]; then
    echo "[$STAMP] scrape exited $SCRAPE_RC (continuing to git step; snapshots preserved)"
  fi
fi

if [ "${NO_GIT:-0}" = "1" ]; then
  echo "[$STAMP] NO_GIT=1 set; skipping git sync."
  exit 0
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[$STAMP] not a git repo; skipping git sync. Initialize a repo + remote to enable auto-push."
  exit 0
fi

# Never commit from the developer's current branch. The repo may be on a
# feature branch (or dirty), which previously left main's LinkedIn snapshot
# stale while launchd misleadingly reported success. Build the source-only
# commit in a temporary detached worktree based on origin/main instead.
TARGET_BRANCH="${TARGET_BRANCH:-main}"
if ! git fetch origin "$TARGET_BRANCH"; then
  echo "[$STAMP] fetch failed; snapshots remain local and will retry next run."
  exit 1
fi

SYNC_PARENT="$(mktemp -d "${TMPDIR:-/tmp}/jobboard-source-sync.XXXXXX")"
SYNC_TREE="$SYNC_PARENT/tree"
cleanup_sync_tree() {
  git -C "$REPO_DIR" worktree remove --force "$SYNC_TREE" >/dev/null 2>&1 || true
  rmdir "$SYNC_PARENT" >/dev/null 2>&1 || true
}
trap cleanup_sync_tree EXIT

if ! git worktree add --detach "$SYNC_TREE" "origin/$TARGET_BRANCH" >/dev/null; then
  echo "[$STAMP] could not create isolated sync worktree; will retry next run."
  exit 1
fi

mkdir -p "$SYNC_TREE/output/sources"
for source_name in linkedin glassdoor; do
  source_path="$REPO_DIR/output/sources/${source_name}.json"
  if [ -f "$source_path" ]; then
    cp "$source_path" "$SYNC_TREE/output/sources/${source_name}.json"
  fi
done

staged_any=0
for source_name in linkedin glassdoor; do
  relative_path="output/sources/${source_name}.json"
  if [ -f "$SYNC_TREE/$relative_path" ]; then
    git -C "$SYNC_TREE" add "$relative_path" || {
      echo "[$STAMP] staging $relative_path failed."
      exit 1
    }
    staged_any=1
  fi
done
if [ "$staged_any" -ne 1 ]; then
  echo "[$STAMP] no source snapshots exist; nothing to sync."
  exit 0
fi
if git -C "$SYNC_TREE" diff --staged --quiet; then
  echo "[$STAMP] no source changes versus origin/$TARGET_BRANCH; nothing to commit."
  exit 0
fi
if [ "${SKIP_PUSH:-0}" = "1" ]; then
  echo "[$STAMP] SKIP_PUSH=1 set; source diff verified, not committed or pushed."
  exit 0
fi

git -C "$SYNC_TREE" commit -m "chore: local job sources ${STAMP}" || {
  echo "[$STAMP] isolated source commit failed."
  exit 1
}

echo "[$STAMP] pushing source-only commit to ${TARGET_BRANCH}..."
if git -C "$SYNC_TREE" push origin "HEAD:${TARGET_BRANCH}"; then
  echo "[$STAMP] pushed. GitHub Actions will ingest the updated sources."
  exit 0
fi

# One bounded race retry if another Action committed to main meanwhile.
echo "[$STAMP] main advanced during sync; rebasing once and retrying."
git -C "$SYNC_TREE" fetch origin "$TARGET_BRANCH" || exit 1
git -C "$SYNC_TREE" rebase "origin/$TARGET_BRANCH" || exit 1
git -C "$SYNC_TREE" push origin "HEAD:${TARGET_BRANCH}" || {
  echo "[$STAMP] push retry failed; local snapshot is preserved for the next run."
  exit 1
}
echo "[$STAMP] pushed after rebase. GitHub Actions will ingest the updated sources."
