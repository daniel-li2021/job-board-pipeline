#!/usr/bin/env bash
#
# Local source sync: scrape local job boards, then commit/push ONLY the
# source snapshots if they changed. The Mac gate controls launch times.
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

if [ -z "${PYTHON_BIN:-}" ] && [ -x "$REPO_DIR/.venv/bin/python3" ]; then
  PYTHON_BIN="$REPO_DIR/.venv/bin/python3"
else
  PYTHON_BIN="${PYTHON_BIN:-python3}"
fi
LOG_DIR="$REPO_DIR/output/logs"
# Durable allowance survives discarded collector worktrees and failed publication.
export LINKEDIN_TRANSPORT_STATE_PATH="${LINKEDIN_TRANSPORT_STATE_PATH:-$LOG_DIR/linkedin_transport.json}"
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

# Use the repository owner's SSH credential even when the wrapper is run
# manually outside the launchd environment. Leave non-production remotes alone.
# Bash 3.2 needs the guarded array expansions below under set -u.
FETCH_ARGS=()
case "$(git remote get-url origin 2>/dev/null)" in
  *github.com/daniel-li2021/job-board-pipeline*)
    # This public repository needs no credential helper for read-only fetches.
    FETCH_ARGS=(-c credential.helper=)
    export GIT_CONFIG_COUNT="${GIT_CONFIG_COUNT:-1}"
    export GIT_CONFIG_KEY_0="${GIT_CONFIG_KEY_0:-remote.origin.pushurl}"
    export GIT_CONFIG_VALUE_0="${GIT_CONFIG_VALUE_0:-git@github.com:daniel-li2021/job-board-pipeline.git}"
    export GIT_SSH_COMMAND="${GIT_SSH_COMMAND:-/usr/bin/ssh -o BatchMode=yes}"
    export GIT_TERMINAL_PROMPT="${GIT_TERMINAL_PROMPT:-0}"
    ;;
esac

# Keep the bootstrap self-contained: a stale checkout need not contain a new helper module.
git_network() {
  "$PYTHON_BIN" - "$LOG_DIR/git_network_latest.json" "$@" <<'PY_GIT_NETWORK'
import json
import os
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

TRANSIENT = ("could not resolve", "timed out", "failed to connect", "connection reset",
             "connection refused", "recv failure", "early eof", "unexpected disconnect",
             "remote end hung up", "tls connection", "error: 502", "error: 503", "error: 504")


def save_receipt(path, receipt):
    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as out:
        json.dump(receipt, out, indent=2)
        out.write("\n")
    os.replace(out.name, path)


def run(path, stage, args):
    started = time.monotonic()
    started_at = datetime.now(timezone.utc).isoformat()
    for attempt in range(1, 4):
        proc = subprocess.Popen(["git", *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, start_new_session=True)
        timed_out = False
        try:
            stdout, stderr = proc.communicate(timeout=45)
        except subprocess.TimeoutExpired:
            timed_out = True
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            stdout, stderr = proc.communicate()
        sys.stdout.write(stdout)
        sys.stderr.write(stderr)
        code = 124 if timed_out else proc.returncode
        reason = ("timeout" if timed_out else "transient_network" if code and any(
            text in stderr.lower() for text in TRANSIENT) else "git_failed" if code else "")
        receipt = {"stage": stage, "status": "failed" if code else "success", "reason": reason,
                   "attempts": attempt, "exit_code": code, "started_at": started_at,
                   "finished_at": datetime.now(timezone.utc).isoformat(),
                   "elapsed_seconds": round(time.monotonic() - started, 3)}
        save_receipt(path, receipt)
        if not code:
            return 0
        if attempt == 3 or reason == "git_failed":
            save_receipt(path.with_name("git_network_last_failure.json"), receipt)
            return code
        print(f"Git {stage}: {reason}; retry {attempt + 1}/3", file=sys.stderr, flush=True)
        time.sleep(5 * attempt)


if __name__ == "__main__":
    raise SystemExit(run(Path(sys.argv[1]), sys.argv[2], sys.argv[3:]))
PY_GIT_NETWORK
}

TARGET_BRANCH="${TARGET_BRANCH:-main}"
# Bootstrap the runner itself from the fetched target. The long-lived checkout
# may be stale or dirty; neither its runner nor its collector code should run.
if [ "${LOCAL_SOURCE_BOOTSTRAPPED:-0}" != "1" ]; then
  if ! git_network fetch ${FETCH_ARGS[@]+"${FETCH_ARGS[@]}"} fetch origin "$TARGET_BRANCH"; then
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
  git_network fetch ${FETCH_ARGS[@]+"${FETCH_ARGS[@]}"} fetch origin "$TARGET_BRANCH" || exit 1
  TARGET_COMMIT="$(git rev-parse "origin/$TARGET_BRANCH")" || exit 1
fi

# A public fetch can succeed with the wrong cached GitHub account. Check write
# authentication before spending several minutes scraping.
if [ "${SKIP_PUSH:-0}" != "1" ] && ! git_network push_preflight push --dry-run origin "origin/$TARGET_BRANCH:$TARGET_BRANCH" >/dev/null; then
  echo "[$STAMP] Git push preflight failed before collection; see output/logs/git_network_latest.json."
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

finish_publication() {
  if [ -n "${LOCAL_SOURCE_RESULT_PATH:-}" ] && [ -f "$SYNC_TREE/output/logs/local_sources_latest.json" ]; then
    cp "$SYNC_TREE/output/logs/local_sources_latest.json" "$LOCAL_SOURCE_RESULT_PATH" || return 1
  fi
  if [ "${COLLECTOR_DEGRADED:-0}" = "1" ]; then
    echo "[$STAMP] all required sources failed; health published, last-good data retained."
    return 1
  fi
  return 0
}

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
    if [ "${LOCAL_SOURCE_PROFILE:-}" != "mac" ]; then
      echo "[$STAMP] collector exited $SCRAPE_RC; snapshots remain unchanged."
      exit $SCRAPE_RC
    fi
    echo "[$STAMP] collector degraded ($SCRAPE_RC); publishing health/last-good state."
    COLLECTOR_DEGRADED=1
  fi
fi

staged_any=0
for source_name in linkedin glassdoor remote_recovery health; do
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
  if [ "${LOCAL_SOURCE_PROFILE:-}" = "mac" ] && [ "${SKIP_PUSH:-0}" != "1" ]; then
    # A successful no-change Mac round still needs a meaningful health receipt
    # on main so the existing source push -> Board -> Pages chain runs once.
    (
      cd "$SYNC_TREE" || exit 1
      "$PYTHON_BIN" -c 'import json, sys; from datetime import datetime, timezone; from pathlib import Path; from state_io import atomic_write; p=Path(sys.argv[1]); data=json.loads(p.read_text(encoding="utf-8")); data["mac_no_change_round_at"]=datetime.now(timezone.utc).isoformat(); atomic_write(p, (json.dumps(data, indent=2, ensure_ascii=False)+"\n").encode("utf-8"))' output/sources/health.json
    ) || exit 1
    git -C "$SYNC_TREE" add output/sources/health.json || exit 1
    echo "[$STAMP] no changed jobs; publishing Mac health receipt for Board refresh."
  else
    echo "[$STAMP] no source changes versus origin/$TARGET_BRANCH; nothing to commit."
    exit 0
  fi
fi
if [ "${SKIP_PUSH:-0}" = "1" ]; then
  echo "[$STAMP] SKIP_PUSH=1 set; source diff verified, not committed or pushed."
  exit 0
fi

if ! (cd "$SYNC_TREE" && "$PYTHON_BIN" scripts/guard_github_blob_size.py); then
  echo "[$STAMP] source blob size guard failed."
  exit 1
fi

git -C "$SYNC_TREE" commit -m "chore: local job sources ${STAMP}" || {
  echo "[$STAMP] isolated source commit failed."
  exit 1
}

echo "[$STAMP] pushing source-only commit to ${TARGET_BRANCH}..."
if git_network publish -C "$SYNC_TREE" push origin "HEAD:${TARGET_BRANCH}"; then
  echo "[$STAMP] pushed. GitHub Actions will ingest the updated sources."
  finish_publication
  exit $?
fi

# Re-scrape once if main advanced. Rebasing would publish artifacts produced by
# old code alongside newer code, recreating the provenance bug.
git_network fetch -C "$SYNC_TREE" ${FETCH_ARGS[@]+"${FETCH_ARGS[@]}"} fetch origin "$TARGET_BRANCH" || exit 1
LATEST_TARGET="$(git -C "$SYNC_TREE" rev-parse "origin/$TARGET_BRANCH")"
if [ "$LATEST_TARGET" != "$COLLECTOR_COMMIT" ] && [ "${LOCAL_SOURCE_RETRY:-0}" != "1" ]; then
  echo "[$STAMP] main advanced during collection; restarting once on $LATEST_TARGET."
  cleanup_sync_tree
  trap - EXIT
  LOCAL_SOURCE_RETRY=1 LOCAL_SOURCE_BOOTSTRAPPED=0 LOCAL_SOURCE_TARGET_COMMIT= exec /bin/bash "$0"
fi
echo "[$STAMP] push failed; snapshots remain on origin/$TARGET_BRANCH and will retry next run."
exit 1
