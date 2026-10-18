"""SAP linked legacy public-interface regression."""
import unittest
from unittest.mock import Mock
from sources.careers import sap


class SAPCompatibilityTests(unittest.TestCase):
    def test_sap_uses_linked_legacy_careers_interface(self):
        html = '<tr><td><a class="jobTitle-link" href="/job/Palo-Alto-Developer/1234567/">Developer</a></td><td class="jobLocation">Palo Alto, CA, US</td></tr>'
        response = Mock(status_code=200, text=html)
        session = Mock(); session.get.return_value = response
        result = sap.scrape_sap(session, queries=['software engineer'], max_pages=1, fetch_details=False)
        self.assertEqual(1, len(result['jobs']))
        self.assertEqual('https://careers.sap.com/search/', session.get.call_args.args[0])
        self.assertTrue(result['jobs'][0]['official_url'].startswith('https://careers.sap.com/job/'))


    def test_redirect_contract_change_and_missing_detail_do_not_become_successful_jds(self):
        from sources.schema import SourceUnavailable
        session = Mock()
        session.get.return_value = Mock(status_code=200, url='https://jobs.sap.com/en/jobs/', text='<main>New careers interface</main>')
        with self.assertRaisesRegex(SourceUnavailable, 'redirected outside'):
            sap.scrape_sap(session, queries=['software engineer'], max_pages=1)
        search = Mock(status_code=200, text='<tr><td><a href="/job/Palo-Alto-Developer/1234567/">Developer</a></td><td class="jobLocation">Palo Alto, CA, US</td></tr>')
        detail = Mock(status_code=200, text='<main>Navigation and company information only</main>')
        session.get.side_effect = [search, detail]
        result = sap.scrape_sap(session, queries=['software engineer'], max_pages=1)
        self.assertEqual('', result['jobs'][0]['description'])
        self.assertEqual(0, result['detail_fetches'])
        self.assertIn('missing job description', result['errors'][0])

    def test_official_match_preserves_discovery_after_legacy_url_row_expired(self):
        from argparse import Namespace
        from unittest.mock import patch
        import official_careers as official
        import board_pipeline as board
        old = 'https://jobs.sap.com/job/Palo-Alto-Developer/1234567'
        row = {'source':'sap_official_careers','job_id':'1234567','company':'SAP','title':'Software Engineer I',
               'location':'Palo Alto, CA, US','official_url':old.replace('jobs.sap.com','careers.sap.com'),
               'description':'Build software services using Python and REST APIs. '*10}
        class ReachedScoring(Exception): pass
        def inspect(rows, *_args, **_kwargs):
            self.assertEqual('2026-10-01T00:00:00Z',rows[0]['first_seen'])
            raise ReachedScoring()
        with patch.object(official,'load_careers_store',return_value={}), \
             patch.object(board,'load_seen_jobs_path',return_value={'url::'+old:'2026-10-01T00:00:00Z'}), \
             patch.object(board,'load_profiles',return_value={}), \
             patch.object(board,'load_store_path',return_value={}), \
             patch.object(board,'load_syncareer_peer_store',return_value={}), \
             patch.object(board,'enrich_from_exact_peers',return_value=0), \
             patch.object(official.remote_recovery,'write_snapshot'), \
             patch.object(board,'score_survivors',side_effect=inspect):
            with self.assertRaises(ReachedScoring): official.cmd_match(Namespace(no_llm=True),[row])
