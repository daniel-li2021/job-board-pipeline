"""Focused evidence-reference, identity, and adapter compatibility regressions."""
import copy
import json
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import board_pipeline as board
import job_identity as identity


class RemainingTests(unittest.TestCase):


    def row(self, key, url='', **extra):
        return {'canonical_job_key': key, 'source': 'indeed', 'job_id': 'i1', 'company': 'NVIDIA',
                'official_url': url, **extra}

    def test_url_added_lost_workday_locale_and_history_keys(self):
        a = 'https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Engineer_JR2026802'
        b = a.replace('/en-US/', '/')
        rows = [self.row('old', a), self.row('new', b), self.row('id::indeed::i1')]
        before = copy.deepcopy(rows)
        groups = identity.alias_map(rows)
        self.assertIn('old', groups['new'])
        self.assertIn('id::indeed::i1', groups['old'])
        self.assertEqual(before, rows)
        self.assertEqual(identity.detail_identity(a), identity.detail_identity(b))

    def test_conflicting_requisitions_and_general_search_never_merge(self):
        url = 'https://jobs.apple.com/en-us/details/200688902/software-engineer'
        rows = [self.row('one', url), self.row('two', url.replace('200688902', '200688903'))]
        self.assertEqual({}, identity.alias_map(rows))
        self.assertEqual({}, identity.alias_map([dict(r,jd_tentative=True) for r in rows]))
        rows = [self.row(str(i), 'https://www.kforce.com/find-work/search-jobs/', job_id=str(i)) for i in range(12)]
        groups = identity.alias_map(rows)
        self.assertTrue(all(len(g) == 2 for g in groups.values()))
        self.assertFalse(identity.detail_identity('https://jobs.apple.com.evil.test/en-us/details/200688902/software-engineer'))

    def test_greenhouse_host_alias_and_distinct_stale_digest_keys(self):
        old = 'https://boards.greenhouse.io/figma/jobs/6131089004'
        new = old.replace('boards.greenhouse.io','job-boards.greenhouse.io')
        self.assertEqual(identity.detail_identity(old),identity.detail_identity(new))
        a = self.row('stale',old,tier='A')
        b = self.row('stale',new.replace('6131089004','6131089005'),job_id='i2',tier='A')
        self.assertEqual([a,b],board.digest_alert_jobs([a,b],{}))

    def test_stale_shared_key_cannot_bridge_distinct_requisitions(self):
        url = 'https://jobs.apple.com/en-us/details/200688902/software-engineer'
        rows = [self.row('url::'+url, url), self.row('url::'+url, url.replace('200688902', '200688903'), job_id='i2')]
        self.assertEqual({}, identity.alias_map(rows))
        self.assertEqual({}, identity.alias_map(rows[1:]))

    def test_apple_title_slugs_same_id_sap_host_alias(self):
        url = 'https://jobs.apple.com/en-us/details/200688902/software-engineer'
        groups = identity.alias_map([self.row('one', url), self.row('two', url+'-ase')])
        self.assertIn('two', groups['one'])
        url = 'https://careers.sap.com/job/Palo-Alto-Engineer/1234567'
        groups = identity.alias_map([self.row('sap', url)])
        self.assertIn('url::'+url.replace('careers.sap.com', 'jobs.sap.com'), groups['sap'])

    def test_durable_discovery_ledger_survives_store_expiry(self):
        old = 'https://jobs.sap.com/job/Palo-Alto-Developer/1234567'
        row = self.row('new', old.replace('jobs.sap.com', 'careers.sap.com'))
        self.assertEqual((True, '2026-10-01T00:00:00Z'), identity.discovery_alias_date(row, {'url::'+old:'2026-10-01T00:00:00Z'}))
        self.assertEqual((True, ''), identity.discovery_alias_date(row, {'url::'+old:''}))
        self.assertEqual((False, ''), identity.discovery_alias_date(row, {'url::'+old.replace('1234567','7654321'):'2026-10-01T00:00:00Z'}))

    def test_stale_primary_key_does_not_borrow_other_requisition_date(self):
        old = 'https://jobs.apple.com/en-us/details/200688902/software-engineer'
        row = self.row('url::'+old,old.replace('200688902','200688903'))
        self.assertEqual((False,''), identity.discovery_alias_date(row, {'url::'+old:'2020-01-01T00:00:00Z'}))

    def test_digest_url_identity_prevents_repeat_but_retains_b_to_a(self):
        url = 'https://lifeattiktok.com/search/7696782198126545157'
        job = self.row('new', url, tier='B')
        job['canonical_job_key'] = 'new'
        state = {'alerted_keys': ['id::indeed::i1'], 'alerted_tier': {'id::indeed::i1': 'B'}}
        self.assertEqual([], board.digest_alert_jobs([job], state))
        job['tier'] = 'A'
        self.assertEqual([job], board.digest_alert_jobs([job], state))
        state = {'alerted_keys': ['url::'+url+'?utm_source=old'], 'alerted_tier': {}}
        self.assertEqual([], board.digest_alert_jobs([job], state))


    def test_duplicate_aliases_emit_once_and_null_legacy_tier_does_not_repeat(self):
        url = 'https://jobs.apple.com/en-us/details/200688902/software-engineer'
        job = self.row('old', url, tier='B')
        peer = self.row('new', url+'-ase', job_id='i2', tier='A')
        self.assertEqual([peer], board.digest_alert_jobs([job,peer], {}))
        self.assertEqual([], board.digest_alert_jobs([job], {'alerted_keys':['id::indeed::i1'], 'alerted_tier':{'id::indeed::i1':None}}))

