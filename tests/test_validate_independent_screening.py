import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_independent_screening import analyze


def vote(record='BIB00001', reviewer='A', kind='HUMAN', decision='INCLUDE_CANDIDATE', level='TITLE_ABSTRACT'):
    return {'record_id': record, 'reviewer_id': reviewer, 'reviewer_kind': kind,
            'decision': decision, 'reason_code': 'PCC_IN_SCOPE', 'evidence_level': level}


class IndependentScreenTests(unittest.TestCase):
    def test_two_independent_agreements_remain_provisional(self):
        out = analyze([vote(reviewer='A'), vote(reviewer='B')], {'BIB00001', 'BIB00002'})
        self.assertTrue(out['valid'])
        self.assertEqual(out['states']['AGREED_PROVISIONAL_INCLUDE_CANDIDATE'], 1)
        self.assertEqual(out['states']['NOT_YET_SCREENED_IN_THIS_INPUT'], 1)
        self.assertEqual(out['final_study_inclusion'], 'NOT_DETERMINED')
    def test_disagreement_requires_reconciliation(self):
        out = analyze([vote(reviewer='A'), vote(reviewer='B', decision='HOLD')])
        self.assertTrue(out['valid'])
        self.assertEqual(out['states']['DISAGREEMENT_RECONCILIATION_REQUIRED'], 1)
    def test_ai_as_human_rejected(self):
        self.assertFalse(analyze([vote(kind='AI')])['valid'])
    def test_same_reviewer_twice_rejected(self):
        self.assertFalse(analyze([vote(), vote()])['valid'])
    def test_mismatched_level_requires_reconciliation(self):
        out = analyze([vote(reviewer='A'), vote(reviewer='B', level='FULL_TEXT')])
        self.assertEqual(out['states']['DIFFERENT_EVIDENCE_LEVELS_RECONCILIATION_REQUIRED'], 1)
    def test_outside_universe_rejected(self):
        self.assertFalse(analyze([vote()], {'BIB00003'})['valid'])
    def test_missing_fields_rejected(self):
        t = vote(); t['reason_code'] = ''
        self.assertFalse(analyze([t])['valid'])

if __name__ == '__main__':
    unittest.main()
