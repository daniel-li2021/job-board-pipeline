#!/usr/bin/env bash
#
# Local source sync: scrape local job boards, then commit/push ONLY the
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
#   PYTHON_BIN   interpreter with requirements-local.txt installed (default: python3)
#   TARGET_BRANCH remote branch to update (default: main)
#   SKIP_SCRAPE=1 sync the last good snapshots without scraping again
#   SKIP_PUSH=1  verify the remote-main diff but do not commit or push
#   NO_GIT=1     run the scrape only; skip all git operations
#
set -uo pipefail

REPO_DIR="${LOCAL_SOURCE_REPO_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_DIR" || exit 1

PYTHON_BIN="${PYTHON_BIN:-python3}"
LOG_DIR="$REPO_DIR/output/logs"
mkdir -p "$LOG_DIR"
STAMP="$(date +%Y-%m-%d_%H%M)"
if ! [ -x "$PYTHON_BIN" ] && ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "[$STAMP] Python interpreter is unavailable: $PYTHON_BIN"
  exit 1
fi

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

if [ "${NO_GIT:-0}" = "1" ]; then
  echo "[$STAMP] NO_GIT=1 set; scraping the current checkout without git sync."
  [ "${SKIP_SCRAPE:-0}" = "1" ] || "$PYTHON_BIN" local_sources.py
  exit $?
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[$STAMP] not a git repo; skipping git sync. Initialize a repo + remote to enable auto-push."
  exit 0
fi

TARGET_BRANCH="${TARGET_BRANCH:-main}"
# Bootstrap the runner itself from the fetched target. The long-lived checkout
# may be stale or dirty; neither its runner nor its collector code should run.
if [ "${LOCAL_SOURCE_BOOTSTRAPPED:-0}" != "1" ]; then
  if ! git fetch origin "$TARGET_BRANCH"; then
    echo "[$STAMP] fetch failed; snapshots remain local and will retry next run."
    exit 1
  fi
  RUNNER_COMMIT="$(git rev-parse "origin/$TARGET_BRANCH")" || exit 1
  RUNNER_TMP="$(mktemp "${TMPDIR:-/tmp}/jobboard-source-runner.XXXXXX")" || exit 1
  cleanup_runner() { rm -f "$RUNNER_TMP"; }
  trap cleanup_runner EXIT
  if ! git show "$RUNNER_COMMIT:scripts/local_source_sync.sh" > "$RUNNER_TMP"; then
    echo "[$STAMP] could not load runner from $RUNNER_COMMIT; will retry next run."
    exit 1
  fi
  LOCAL_SOURCE_BOOTSTRAPPED=1 LOCAL_SOURCE_REPO_DIR="$REPO_DIR" \
    LOCAL_SOURCE_TARGET_COMMIT="$RUNNER_COMMIT" /bin/bash "$RUNNER_TMP"
  exit $?
fi
TARGET_COMMIT="${LOCAL_SOURCE_TARGET_COMMIT:-}"
if [ -z "$TARGET_COMMIT" ]; then
  git fetch origin "$TARGET_BRANCH" || exit 1
  TARGET_COMMIT="$(git rev-parse "origin/$TARGET_BRANCH")" || exit 1
fi

# A public fetch can succeed with the wrong cached GitHub account. Check write
# authentication before spending several minutes scraping.
if [ "${SKIP_PUSH:-0}" != "1" ] && ! git push --dry-run origin "origin/$TARGET_BRANCH:$TARGET_BRANCH" >/dev/null; then
  echo "[$STAMP] Git push authentication failed before collection; fix the credential for this repo owner."
  exit 1
fi

SYNC_PARENT="$(mktemp -d "${TMPDIR:-/tmp}/jobboard-source-sync.XXXXXX")"
SYNC_TREE="$SYNC_PARENT/tree"
cleanup_sync_tree() {
  git -C "$REPO_DIR" worktree remove --force "$SYNC_TREE" >/dev/null 2>&1 || true
  rmdir "$SYNC_PARENT" >/dev/null 2>&1 || true
}
trap cleanup_sync_tree EXIT

if ! git worktree add --detach "$SYNC_TREE" "$TARGET_COMMIT" >/dev/null; then
  echo "[$STAMP] could not create isolated sync worktree; will retry next run."
  exit 1
fi

COLLECTOR_COMMIT="$(git -C "$SYNC_TREE" rev-parse HEAD)"
echo "[$STAMP] collector commit: $COLLECTOR_COMMIT"
if [ "${SKIP_SCRAPE:-0}" = "1" ]; then
  echo "[$STAMP] SKIP_SCRAPE=1 set; using snapshots already on origin/$TARGET_BRANCH."
else
  (
    cd "$SYNC_TREE" || exit 1
    COLLECTOR_COMMIT="$COLLECTOR_COMMIT" COLLECTOR_DIRTY=0 "$PYTHON_BIN" local_sources.py
  )
  SCRAPE_RC=$?
  if [ $SCRAPE_RC -ne 0 ]; then
    echo "[$STAMP] collector exited $SCRAPE_RC; snapshots remain unchanged."
    exit $SCRAPE_RC
  fi
fi

staged_any=0
for source_name in linkedin indeed glassdoor health; do
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

# Re-scrape once if main advanced. Rebasing would publish artifacts produced by
# old code alongside newer code, recreating the provenance bug.
git -C "$SYNC_TREE" fetch origin "$TARGET_BRANCH" || exit 1
LATEST_TARGET="$(git -C "$SYNC_TREE" rev-parse "origin/$TARGET_BRANCH")"
if [ "$LATEST_TARGET" != "$COLLECTOR_COMMIT" ] && [ "${LOCAL_SOURCE_RETRY:-0}" != "1" ]; then
  echo "[$STAMP] main advanced during collection; restarting once on $LATEST_TARGET."
  cleanup_sync_tree
  trap - EXIT
  LOCAL_SOURCE_RETRY=1 LOCAL_SOURCE_BOOTSTRAPPED=0 LOCAL_SOURCE_TARGET_COMMIT= exec /bin/bash "$0"
fi
echo "[$STAMP] push failed; snapshots remain on origin/$TARGET_BRANCH and will retry next run."
exit 1
