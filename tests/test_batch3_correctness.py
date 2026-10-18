"""Batch 3 fairness, employer attribution, and non-production review boundaries."""
import copy
import json
import tempfile
import unittest
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock, patch

import board_pipeline as board
import local_sources
import recovery_policy
from sources import linkedin_local
from sources.company_aliases import recover_missing_company
from sources.linkedin_transport import LinkedInTransport
from scripts import selective_review_pilot as pilot


class Batch3Tests(unittest.TestCase):
    def card(self, **extra):
        return {'source': 'linkedin', 'job_id': '123', 'company': 'Example',
                'title': 'Software Engineer', 'location': 'Austin, TX', 'description': '',
                'first_seen': datetime.now(timezone.utc).isoformat(),
                'linkedin_detail_triage': {'needs_jd': True}, **extra}

    def test_legacy_transport_deferrals_get_only_one_bounded_opportunity(self):
        now = datetime.now(timezone.utc)
        for field, reason in [('enrichment_deferred_reason', 'linkedin_detail_cooldown'),
                              ('enrichment_failure_reason', 'linkedin_rate_limited')]:
            row = self.card(first_seen=(now-timedelta(hours=25)).isoformat(), **{field: reason})
            self.assertFalse(recovery_policy.fresh(row, now))
            self.assertTrue(local_sources._linkedin_detail_eligible(row, now))
            for bad in [dict(row, linkedin_detail_triage={'needs_jd': False}),
                        dict(row, linkedin_detail_attempted_at=now.isoformat()),
                        dict(row, first_seen=(now-timedelta(hours=72, seconds=1)).isoformat()),
                        dict(row, first_seen=(now+timedelta(seconds=1)).isoformat())]:
                self.assertFalse(local_sources._linkedin_detail_eligible(bad, now))
            boundary = dict(row, first_seen=(now-timedelta(hours=72)).isoformat())
            self.assertTrue(local_sources._linkedin_detail_eligible(boundary, now))

    def test_cooldown_persists_admitted_only_and_next_round_respects_probe_cap(self):
        now = datetime.now(timezone.utc)
        rows = [self.card(job_id=str(i), first_seen=(now-timedelta(hours=23)).isoformat()) for i in range(3)]
        rows[-1]['linkedin_detail_triage'] = {'needs_jd': False}
        dates = [r['first_seen'] for r in rows]
        with patch.object(local_sources, '_linkedin_detail_control', return_value=(0, True, False)), \
             patch.object(local_sources.recovery_ai, 'triage_linkedin_detail') as triage, \
             patch.object(linkedin_local, '_make_session') as session:
            paused = local_sources._finish_linkedin_detail(rows, [], {'cache_reused': 0}, recovery_policy.RecoveryBudget(), now)
            session.return_value.get.assert_not_called()
            triage.assert_not_called()
        self.assertEqual(0, paused['requests'])
        self.assertEqual(2, paused['protected_deferred'])
        self.assertNotIn('linkedin_detail_deferred_at', rows[-1])
        next_now = now + timedelta(hours=3)
        candidates, admission = local_sources._prepare_linkedin_detail(rows, rows, next_now)
        self.assertEqual(2, len(candidates))
        session = Mock()
        session.get.return_value = Mock(status_code=200, text='', headers={})
        with patch.object(local_sources, '_linkedin_detail_control', return_value=(1, False, True)), \
             patch.object(board, 'load_profiles', return_value={}), \
             patch.object(local_sources.recovery_ai, 'triage_linkedin_detail',
                          side_effect=lambda batch, _: {recovery_policy.identity(r): {'needs_jd': True} for r in batch}), \
             patch.object(linkedin_local, '_make_session', return_value=session), \
             patch.object(linkedin_local, '_parse_detail', return_value={'description': 'Verified JD ' * 40, 'application_url': ''}), \
             patch('sources.linkedin_transport.time.sleep'):
            budget = recovery_policy.RecoveryBudget()
            first = local_sources._finish_linkedin_detail(candidates, rows, admission, budget, next_now, transport=LinkedInTransport())
            second = local_sources._finish_linkedin_detail(candidates, rows, admission, budget, next_now, transport=LinkedInTransport())
        self.assertEqual(1, first['protected_requests'])
        self.assertEqual(1, first['protected_jds_resolved'])
        self.assertEqual(0, second['requests'])
        self.assertEqual(1, session.get.call_count)
        self.assertEqual(dates, [r['first_seen'] for r in rows])

    def test_midround_429_protects_unattempted_admitted_cards(self):
        now = datetime.now(timezone.utc)
        rows = [self.card(job_id=str(i)) for i in range(3)]
        session = Mock()
        session.get.return_value = Mock(status_code=429, text='', headers={})
        with patch.object(local_sources, '_linkedin_detail_control', return_value=(8, False, False)), \
             patch.object(board, 'load_profiles', return_value={}), \
             patch.object(local_sources.recovery_ai, 'triage_linkedin_detail',
                          side_effect=lambda batch, _: {recovery_policy.identity(r): {'needs_jd': True} for r in batch}), \
             patch.object(linkedin_local, '_make_session', return_value=session), \
             patch('sources.linkedin_transport.time.sleep'):
            detail = local_sources._finish_linkedin_detail(rows, [], {'cache_reused': 0}, recovery_policy.RecoveryBudget(), now, transport=LinkedInTransport())
        self.assertEqual(1, detail['requests'])
        self.assertEqual(2, detail['protected_deferred'])
        self.assertNotIn('linkedin_detail_deferred_at', rows[0])
        self.assertTrue(all(r.get('linkedin_detail_deferred_at') for r in rows[1:]))
        self.assertFalse(local_sources._linkedin_detail_eligible(dict(rows[0], first_seen=(now-timedelta(hours=25)).isoformat()), now))

    def test_employer_attribution_preserves_identity_score_and_evidence(self):
        profiles = [{'name': 'Example AI', 'career_board_url': 'https://jobs.ashbyhq.com/example'}]
        url = 'https://jobs.ashbyhq.com/example/48219357-056f-4089-981a-0c773b196130?source=indeed'
        row = self.card(source='indeed', company='', application_url=url, match_score=94, sponsorship='unknown')
        before, key = copy.deepcopy(row), board.dedup_key(row)
        self.assertTrue(recover_missing_company(row, profiles))
        self.assertEqual('Example AI', row['company'])
        self.assertEqual(key, board.dedup_key(row))
        self.assertEqual({k:v for k,v in before.items() if k!='company'}, {k:row[k] for k in before if k!='company'})
        self.assertNotIn('official_url', row)
        compact = board.compact_store_entry(board.build_store_entry(row, key))
        self.assertEqual('curated_ats_tenant', compact['company_identity_method'])
        self.assertEqual('https://jobs.ashbyhq.com/example', compact['company_identity_url'])
        self.assertFalse(recover_missing_company(row, profiles))
        for bad in [dict(before, company='Named'), dict(before, job_id=''),
                    dict(before, application_url=url.replace('ashbyhq.com', 'ashbyhq.com.evil.test')),
                    dict(before, application_url='https://jobs.ashbyhq.com/example'),
                    dict(before, application_url=url.replace('/example/', '/other/'))]:
            snapshot = copy.deepcopy(bad)
            self.assertFalse(recover_missing_company(bad, profiles))
            self.assertEqual(snapshot, bad)
        self.assertFalse(recover_missing_company(dict(before), profiles + [{'name': 'Other', 'career_board_url': profiles[0]['career_board_url']}]))

    def test_collector_recovers_employer_before_dedup_and_keeps_provenance(self):
        row = self.card(source='indeed', company='', application_url='https://jobs.ashbyhq.com/example/48219357-056f-4089-981a-0c773b196130')
        def snapshot(name):
            return {'jobs': [dict(row)] if name == 'indeed' else [], 'meta': {}}
        with patch.object(board, 'read_source_snapshot_payload', side_effect=snapshot), \
             patch.object(board, 'load_company_profiles', return_value=({'name': 'Example', 'career_board_url': 'https://jobs.ashbyhq.com/example'},)):
            rows, meta = board.collect_sources(Mock(), skip_network=True)
        self.assertEqual('Example', rows[0]['company'])
        self.assertEqual(1, meta['employers_recovered'])

    def test_frozen_packet_is_unique_split_and_unlabelled(self):
        packet = json.loads((pilot.ROOT / 'docs/BATCH3_PILOT.json').read_text())
        self.assertEqual(40, len(packet['cases']))
        self.assertEqual({'development':20, 'held_out':20}, dict(Counter(c['partition'] for c in packet['cases'])))
        seen = set()
        for case in packet['cases']:
            keys = set(case['job']['source_urls'])
            self.assertFalse(keys & seen)
            seen.update(keys)
            self.assertIsNone(case['human_label'])
            self.assertEqual(pilot.digest(case['job']), case['evidence_sha256'])
        self.assertFalse(packet['production_enabled'])
        self.assertFalse(pilot.identities({'url': 'https://www.kforce.com/find-work/search-jobs/', 'company':'A', 'title':'Engineer'}))

    def test_reviews_reject_fabricated_quotes_and_require_human_labels(self):
        case = {'id':'x', 'job':{'description':'Requires Python.'}, 'baseline':{'tier':'A'}}
        profiles = {'resume_swe':'Built Python APIs.', 'resume_ai':''}
        review = {'id':'x', 'tier':'B', 'eligibility':'unknown', 'evidence':[{'jd_quote':'Requires Python.', 'resume_quote':'Built Python APIs.'}]}
        self.assertTrue(pilot.validate_review(review, case, profiles))
        self.assertFalse(pilot.validate_review(dict(review, evidence=[{'jd_quote':'Requires 10 years', 'resume_quote':''}]), case, profiles))
        self.assertFalse(pilot.validate_review(dict(review, evidence=[]), case, profiles))
        packet = {'cases':[case], 'profiles':profiles}
        receipt = {'packet_sha256':pilot.digest(packet), 'batches':[{'results':[review]}]}
        self.assertEqual({}, pilot.evaluate(packet, receipt, {})['counts'])
        result = pilot.evaluate(packet, receipt, {'x':{'tier':'A', 'eligibility':'blocked'}})
        self.assertEqual(1, result['counts']['harmed_tiers'])
        self.assertEqual(1, result['counts']['blocked_high_priority_proposals'])
        self.assertFalse(result['production_enabled'])

    def test_pilot_is_development_only_and_reuses_receipts(self):
        profiles = {'resume_swe':'Python', 'resume_ai':'', 'candidate_profile':''}
        packet = {'profiles':profiles, 'cases':[
            {'id':str(i), 'partition':'development' if i<20 else 'held_out', 'job':{'description':''}}
            for i in range(40)]}
        result = lambda *a, **kw: Mock(raise_for_status=lambda: None, json=lambda: {
            'choices':[{'message':{'content':json.dumps({'results':[{'id':c['id'], 'tier':'unknown', 'eligibility':'unknown', 'evidence':[]} for c in json.loads(kw['json']['messages'][1]['content'])['cases']]})}}], 'usage':{'prompt_tokens':10}})
        with tempfile.TemporaryDirectory() as temp, patch.dict('os.environ', {'OPENAI_API_KEY':'fixture'}), \
             patch('requests.post', side_effect=result) as post:
            path = Path(temp)/'receipt.json'
            receipt = pilot.review_development(packet, path)
            self.assertEqual(2, post.call_count)
            self.assertEqual([str(i) for i in range(20)], [k for b in receipt['batches'] for k in b['case_ids']])
            with patch.dict('os.environ', {'OPENAI_API_KEY':''}):
                self.assertEqual(receipt, pilot.review_development(packet, path))
            self.assertEqual(2, post.call_count)
            with self.assertRaises(ValueError):
                pilot.review_development(dict(packet, policy='changed'), path)
