#!/usr/bin/env python3
"""Read-only alias migration rehearsal over a pinned local backup; no network/writes."""
import argparse
import hashlib
import json
import sys
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from job_identity import alias_groups
from scripts.preview_batch2_migration import normalized_key


def rehearse(backup):
    manifest = json.loads((backup / 'manifest.json').read_text())
    checksums = dict(manifest['files'], **{'supabase.json': manifest['sha256']})
    for rel, expected in checksums.items():
        if hashlib.sha256((backup / rel).read_bytes()).hexdigest() != expected:
            raise ValueError('Backup hash mismatch: ' + rel)
    rows, changes = [], []
    for pipeline, directory in [('board', 'board'), ('syncareer', 'syncareer'), ('official', 'official_careers')]:
        for row in json.loads((backup / 'output' / directory / 'jobs.json').read_text())['entries']:
            row = dict(row, source_pipeline=pipeline)
            key = row.get('canonical_job_key') or row.get('key') or ''
            proposed = normalized_key(row, pipeline)
            rows.append(row)
            if proposed != key:
                changes.append((key, proposed))
    groups = alias_groups(rows)
    aliases = {key: g for g in groups for key in g}
    remote = json.loads((backup / 'supabase.json').read_text())
    local = json.loads((backup / 'profile/review_state.json').read_text()).get('jobs', {})
    # Rehearse an additive view only. Original records/events/keys never disappear.
    before = json.dumps({'remote': remote, 'local': local, 'rows': rows}, sort_keys=True)
    conflicts = 0
    for group in groups:
        states = [r for r in remote if r['canonical_job_key'] in group]
        if len({(r['status'], r['deleted']) for r in states}) > 1:
            conflicts += 1
    runtime_rows = [{**r, 'pipeline': r['source_pipeline'], 'url': r.get('official_url') or r.get('job_url') or r.get('url') or '',
                     'score':r.get('match_score', r.get('fit_score',''))} for r in rows]
    history = {r.get('canonical_job_key') or r.get('key'): [r['pipeline'],r.get('company',''),r.get('title',''),r.get('location',''),r['url'],r.get('tier','-'),r['score']] for r in runtime_rows}
    runtime = json.loads(subprocess.check_output(['node', str(ROOT/'scripts/rehearse_identity_browser.js')], cwd=ROOT,
        input=json.dumps({'groups':groups,'rows':runtime_rows,'history':history,'remote':remote}), text=True))
    archives = [json.loads(r['canonical_job_key'][len('applied-archive::'):]) for r in remote if r['canonical_job_key'].startswith('applied-archive::')]
    preservation = before == json.dumps({'remote': remote, 'local': local, 'rows': rows}, sort_keys=True)
    covered = sum(new in aliases.get(old, []) for old, new in changes)
    ledgers = {}
    for rel in checksums:
        if any(name in rel for name in ['seen_jobs', 'digest_state', 'alert_history', 'notification_outbox']):
            value = json.dumps(json.loads((backup / rel).read_text()))
            ledgers[rel] = {'sha256': checksums[rel], 'alias_keys_referenced': sum(json.dumps(k) in value for k in aliases), 'retained_verbatim': True}
    return {'mode': 'additive_alias_dry_run', 'applied': False, 'backup_sha256': manifest['sha256'],
            'backup_rows': len(remote), 'local_review_keys':len(local), 'stored_records': len(rows), 'proposed_key_changes': len(changes),
            'key_changes_covered_by_safe_aliases': covered, 'key_changes_deferred': len(changes)-covered,
            'alias_groups': len(groups), 'alias_keys': len(aliases),
            'remote_direct_statuses_by_state': dict(Counter((r['status'] + (' deleted' if r['deleted'] else '')) for r in remote if not r['canonical_job_key'].startswith('applied-archive::'))),
            'remote_alias_keys_present': sum(r['canonical_job_key'] in aliases for r in remote),
            'groups_with_different_saved_statuses': conflicts,
            'all_original_records_keys_statuses_dates_preserved': preservation,
            'browser_runtime_rehearsal':runtime, 'archived_metadata_records_retained':len(archives),
            'archive_application_dates_retained':sum(bool(a.get('applied')) for a in archives),
            'first_seen_policy': 'Stored first_seen remains untouched; new source-ID/URL aliases inherit prior discovery date.',
            'ledgers': ledgers, 'browser_pending_edits_inspected': False,
            'rollback': 'Remove additive aliases; restore no database rows because no database mutation occurs.',
            'blocking_limits': ['Unrecognized posting URLs remain separate; no mass rekey.',
                                'Public REST export is paginated and not a transactional database backup.',
                                'Browser-only pending edits and historical status events absent from the table cannot be exported here.',
                                'Live rekey/merge requires owner approval and a consistent database backup.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--backup', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(rehearse(args.backup), indent=2))
