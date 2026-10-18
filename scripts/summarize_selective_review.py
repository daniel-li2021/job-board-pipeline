#!/usr/bin/env python3
"""Audited offline metrics; leaves the frozen request policy/runner unchanged."""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.selective_review_pilot import digest


def summarize(packet, receipt, assessment):
    if receipt['packet_sha256'] != digest(packet) or assessment['packet_sha256'] != digest(packet):
        raise ValueError('Packet fingerprint mismatch')
    if assessment['partition'] != receipt['partition'] or assessment['human_verified'] is not False:
        raise ValueError('Assessment provenance/partition mismatch')
    reviews = {r['id']: r for b in receipt['batches'] for r in b['results']}
    counts, cases = Counter(), []
    for case in packet['cases']:
        if case['partition'] != receipt['partition']:
            continue
        label = assessment['labels'][case['id']]
        review = reviews.get(case['id'])
        before, expected, after = case['baseline'].get('tier'), label['tier'], (review or {}).get('tier')
        counts['cases'] += 1
        counts['valid_reviews'] += review is not None
        counts['review_missing'] += review is None
        counts['assessment_unknown'] += expected == 'unknown'
        counts['baseline_tier_missing'] += before not in {'A', 'B', 'C'}
        counts['review_abstentions'] += after == 'unknown'
        known = expected in {'A', 'B', 'C'}
        comparable = known and before in {'A', 'B', 'C'} and after in {'A', 'B', 'C'}
        counts['baseline_assessable'] += known and before in {'A', 'B', 'C'}
        counts['review_assessable'] += known and after in {'A', 'B', 'C'}
        counts['baseline_false_positives'] += known and expected == 'C' and before in {'A', 'B'}
        counts['review_false_positives'] += known and expected == 'C' and after in {'A', 'B'}
        counts['comparable_tiers'] += comparable
        counts['corrected_tiers'] += comparable and before != expected and after == expected
        counts['harmed_tiers'] += comparable and before == expected and after != expected
        counts['rescued_opportunities'] += comparable and before == 'C' and after in {'A', 'B'} and expected in {'A', 'B'}
        counts['lost_opportunities'] += comparable and before in {'A', 'B'} and after == 'C' and expected in {'A', 'B'}
        counts['eligibility_assessable'] += label['eligibility'] in {'supported', 'blocked'} and review is not None
        counts['eligibility_errors'] += label['eligibility'] in {'supported', 'blocked'} and review is not None and review['eligibility'] != label['eligibility']
        counts['unsupported_eligibility_claims'] += label['eligibility'] == 'unknown' and review is not None and review['eligibility'] != 'unknown'
        counts['blocked_review_priorities'] += label['eligibility'] == 'blocked' and after in {'A', 'B'}
        cases.append({'id': case['id'], 'baseline_tier': before, 'review_tier': after, 'assessment_tier': expected,
                      'eligibility_assessment': label['eligibility'], 'comparable': comparable})
    fields = ['prompt_tokens', 'completion_tokens', 'total_tokens']
    usage = {k: sum(b['usage'].get(k, 0) for b in receipt['batches']) for k in fields}
    return {'partition': receipt['partition'], 'basis': 'AI silver assessment; no verified human ground truth',
            'counts': dict(counts), 'usage': usage, 'requests': len(receipt['batches']),
            'first_attempt_valid': sum(len(b['results']) for b in receipt['batches'] if b['tag'].endswith(':0')),
            'eligibility_error_rate': counts['eligibility_errors']/counts['eligibility_assessable'] if counts['eligibility_assessable'] else None,
            'precision_at_10': None, 'ranking_limit': 'Purposive small case packet; missing comparable tiers and no complete production ranking or human relevance judgments',
            'production_enabled': False, 'recommendation': 'Do not integrate: benefit is promising but insufficiently established; human adjudication and eligibility evidence required',
            'cases': cases}


if __name__ == '__main__':
    partition = sys.argv[1]
    suffix = 'DEV' if partition == 'development' else 'HELD_OUT'
    packet = json.loads((ROOT/'docs/BATCH3_PILOT.json').read_text())
    receipt = json.loads((ROOT/f'docs/SELECTIVE_V2_{suffix}.json').read_text())
    assessment = json.loads((ROOT/f'docs/SELECTIVE_{suffix}_ASSESSMENT.json').read_text())
    print(json.dumps(summarize(packet, receipt, assessment), indent=2))
