"""Additive, conservative identity aliases. Never rekeys or mutates saved state."""
import re
from collections import defaultdict
from urllib.parse import urlsplit
from sources.schema import normalize_job_url


def detail_identity(url):
    """Recognize explicit posting IDs, never arbitrary equal URLs/search pages."""
    u = urlsplit(str(url or ''))
    host, path = (u.hostname or '').lower(), u.path.rstrip('/')
    if u.scheme != 'https':
        return ''
    patterns = [
        (host in {'boards.greenhouse.io', 'job-boards.greenhouse.io'}, r'/([^/]+)/jobs/(\d+)'),
        (host == 'jobs.ashbyhq.com', r'/([^/]+)/([0-9a-fA-F-]{36})'),
        (host == 'jobs.lever.co', r'/([^/]+)/([0-9a-fA-F-]{36})'),
        (host == 'jobs.apple.com', r'/[^/]+/details/(\d+)(?:/[^/]+)?'),
        (host in {'www.metacareers.com', 'metacareers.com'}, r'/(?:jobs|profile/job_details)/(\d+)'),
        (host == 'lifeattiktok.com', r'/search/(\d+)'),
        (host.endswith('.myworkdayjobs.com'), r'/(?:[^/]+/)*job/[^/]+/[^/]*_([A-Za-z]+\d+(?:-\d+)?)'),
        (host in {'careers.sap.com', 'jobs.sap.com'}, r'/job/[^/]+/(\d+)'),
    ]
    for enabled, pattern in patterns:
        match = re.fullmatch(pattern, path)
        if enabled and match:
            namespace = 'job-boards.greenhouse.io' if host in {'boards.greenhouse.io', 'job-boards.greenhouse.io'} else host
            if host in {'jobs.sap.com', 'careers.sap.com'}:
                namespace = 'careers.sap.com'
            # Workday site is part of employer identity; locale is presentation only.
            if host.endswith('.myworkdayjobs.com'):
                namespace += '/' + path.split('/job/')[0].split('/')[-1]
            return namespace + ':' + ':'.join(match.groups())
    return ''


def alias_groups(rows):
    """Group verified detail identities or consistent exact source IDs; retain every key."""
    records, by_id, by_detail = [], defaultdict(list), defaultdict(list)
    unsafe_keys = set()
    for row in rows:
        key = str(row.get('canonical_job_key') or row.get('key') or '')
        source = str(row.get('source') or row.get('source_pipeline') or row.get('pipeline') or '')
        job_id = str(row.get('job_id') or '')
        url = row.get('official_url') or row.get('job_url') or row.get('url') or row.get('source_url') or ''
        token = detail_identity(url)
        verified_url = bool(token and not row.get('jd_tentative'))
        company = str(row.get('company') or '').strip().casefold()
        if not key:
            continue
        keys = {key}
        if source and job_id:
            keys.add(f'id::{source}::{job_id}')
        if verified_url:
            keys.add('url::' + normalize_job_url(url))
            if urlsplit(str(url)).hostname in {'jobs.sap.com', 'careers.sap.com'}:
                keys.add('url::' + normalize_job_url(str(url).replace('careers.sap.com', 'jobs.sap.com')))
        key_token = detail_identity(key.removeprefix("url::")) if key.startswith("url::") else ""
        if token and key_token and token != key_token:
            unsafe_keys.update(keys)
        record = (keys, token, company)
        records.append(record)
        if source and job_id:
            by_id[(source, job_id)].append(record)
        if verified_url and company:
            by_detail[(company, token)].append(record)
    candidates = []
    for members in [*by_id.values(), *by_detail.values()]:
        tokens = {r[1] for r in members if r[1]}
        companies = {r[2] for r in members if r[2]}
        if len(tokens) <= 1 and len(companies) <= 1:
            candidates.append(set().union(*(r[0] for r in members)))
    # A conflicting source-ID must not bridge distinct requisitions through a shared key.
    unsafe = unsafe_keys
    for members in by_id.values():
        if len({r[1] for r in members if r[1]}) > 1 or len({r[2] for r in members if r[2]}) > 1:
            unsafe.update(set().union(*(r[0] for r in members)))
    parent = {}
    def root(key):
        parent.setdefault(key, key)
        while parent[key] != key:
            parent[key] = parent[parent[key]]
            key = parent[key]
        return key
    for keys in candidates:
        if keys & unsafe or len(keys) < 2:
            continue
        first = min(keys)
        for key in keys:
            parent[root(key)] = root(first)
    grouped = defaultdict(list)
    for key in parent:
        grouped[root(key)].append(key)
    result = []
    for group in grouped.values():
        members = [r for r in records if r[0].intersection(group)]
        if len({r[1] for r in members if r[1]}) > 1 or len({r[2] for r in members if r[2]}) > 1:
            continue
        if len(group) > 1:
            result.append(sorted(group))
    return sorted(result)


def alias_map(rows):
    return {key: group for group in alias_groups(rows) for key in group}


def discovery_alias_date(row, ledger):
    """Look through durable discovery keys after the retained job row has expired."""
    from sources.schema import parse_datetime
    keys = set()
    if row.get('source') and row.get('job_id'):
        keys.add(f"id::{row['source']}::{row['job_id']}")
    token = detail_identity(row.get('official_url') or '')
    dates = [value for key, value in ledger.items() if key in keys or (
        token and str(key).startswith('url::') and detail_identity(key[5:]) == token)]
    valid = [value for value in dates if parse_datetime(value)]
    return bool(dates), min(valid, key=parse_datetime) if valid else ''
