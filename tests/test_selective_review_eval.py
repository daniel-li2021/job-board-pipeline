"""Frozen experiment boundaries and audited metric denominators."""
import copy
import unittest
from pathlib import Path
from scripts import selective_review_eval as review


class SelectiveReviewTests(unittest.TestCase):
    def test_evidence_references_are_exact_and_fail_closed(self):
        text = 'Untrusted "quotes" and Unicode — Python.\n' * 40
        self.assertEqual(text, ''.join(review.units(text)))
        case = {'id': 'x', 'job': {'description': text}}
        profiles = {'resume_swe': 'Built Python services.', 'resume_ai': ''}
        item = {'id': 'x', 'tier': 'A', 'eligibility': 'unknown', 'evidence': [
            {'jd_ref': 0, 'resume_ref': 0, 'assessment': 'Python services overlap.'}]}
        self.assertTrue(review.resolve(item, case, profiles))
        for field, value in [('jd_ref', True), ('jd_ref', -1), ('resume_ref', 999), ('assessment', '')]:
            bad = copy.deepcopy(item); bad['evidence'][0][field] = value
            self.assertIsNone(review.resolve(bad, case, profiles))
        item['evidence'][0]['resume_ref'] = None
        self.assertIsNone(review.resolve(item, case, profiles))


    def test_held_out_requires_frozen_policy_before_network(self):
        with self.assertRaisesRegex(ValueError, 'matching frozen'):
            review.run({'cases': []}, 'held_out', Path('/tmp/unused-receipt'), None)


    def test_metrics_count_baseline_false_positive_when_review_abstains(self):
        from scripts.summarize_selective_review import summarize
        from scripts.selective_review_pilot import digest
        packet = {'cases':[{'id':'x','partition':'development','baseline':{'tier':'A'}}]}
        receipt = {'packet_sha256':digest(packet),'partition':'development','batches':[{'tag':'0:0','usage':{},'results':[{'id':'x','tier':'unknown','eligibility':'unknown'}]}]}
        assessment = {'packet_sha256':digest(packet),'partition':'development','human_verified':False,'labels':{'x':{'tier':'C','eligibility':'unknown'}}}
        metrics = summarize(packet, receipt, assessment)
        self.assertEqual(1, metrics['counts']['baseline_false_positives'])
        self.assertEqual(0, metrics['counts']['comparable_tiers'])
        self.assertIsNone(metrics['eligibility_error_rate'])
        assessment['packet_sha256']='wrong'
        with self.assertRaises(ValueError): summarize(packet, receipt, assessment)

