import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build_fulltext_queue import make_queue

class FulltextQueueTests(unittest.TestCase):
 def test_candidate_order_and_scope(self):
  sample=[{'cluster_id':'BIB00010','R41_TA_label':'HOLD_DIRECTION_OR_UNIT'},
          {'cluster_id':'BIB00009','R41_TA_label':'DIRECT_TA_POSSIBLE'},
          {'cluster_id':'BIB00008','R41_TA_label':'AI_USED_IN_PROCUREMENT_ONLY'}]
  result=make_queue(sample)
  self.assertEqual([x['cluster_id'] for x in result],['BIB00009','BIB00010'])
  self.assertTrue(all(x['fulltext_eligibility']=='NOT_DETERMINED' for x in result))
 def test_duplicates_rejected(self):
  sample=[{'cluster_id':'BIB00010','R41_TA_label':'HOLD_DIRECTION_OR_UNIT'}]*2
  with self.assertRaises(ValueError): make_queue(sample)
if __name__=='__main__':unittest.main()
