"""Negative controls ensure fabricated human/final status, duplicated IDs and licensed fields fail."""
from pathlib import Path
import unittest,tempfile,shutil,sys,csv,json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_r45_public import audit
FILES=['R41_220_provisional_decisions_PUBLICSAFE.csv','R42_B04_64_provisional_decisions_PUBLICSAFE.csv','R43_B05_120_provisional_decisions_PUBLICSAFE.csv','R44_64_Provisional_RecallStress_PUBLICSAFE.csv','R45_112_Provisional_Routes_PUBLICSAFE.csv','R45_Public_ProgressSummary.json','R45_13_PublicSource_ClaimBoundaries.csv','R45_Identity_Holds_IDonly_PUBLICSAFE.csv']
class TestR45Audit(unittest.TestCase):
 def test_normal(self):self.assertEqual(audit(ROOT)['status'],'PASS')
 def setup(self):
  td=tempfile.TemporaryDirectory();root=Path(td.name);(root/'data').mkdir()
  for f in FILES:shutil.copyfile(ROOT/'data'/f,root/'data'/f)
  return td,root
 def mutate(self,root,fn):
  path=root/'data/R45_112_Provisional_Routes_PUBLICSAFE.csv'
  with path.open(encoding='utf-8',newline='') as f:records=list(csv.DictReader(f))
  fn(records)
  with path.open('w',encoding='utf-8',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
 def test_duplicate_rejected(self):
  t,p=self.setup()
  with t:
   self.mutate(p,lambda r:r[0].update({'cluster_id':r[1]['cluster_id']}))
   with self.assertRaises(AssertionError):audit(p)
 def test_final_inclusion_rejected(self):
  t,p=self.setup()
  with t:
   self.mutate(p,lambda r:r[0].update({'final_inclusion':'INCLUDE'}))
   with self.assertRaises(AssertionError):audit(p)
 def test_license_leak_column_rejected(self):
  t,p=self.setup()
  with t:
   self.mutate(p,lambda r:r[0].update({'abstract':'copyrighted database export'}))
   with self.assertRaises(AssertionError):audit(p)
 def test_fabricated_human_R2_rejected(self):
  t,p=self.setup()
  with t:
   self.mutate(p,lambda r:r[0].update({'reviewer_type':'HUMAN_R2'}))
   with self.assertRaises(AssertionError):audit(p)
 def test_claim_enforcement_misrepresentation_rejected(self):
  t,p=self.setup()
  with t:
   path=p/'data/R45_13_PublicSource_ClaimBoundaries.csv'
   with path.open(encoding='utf-8',newline='') as f:r=list(csv.DictReader(f))
   r[0]['independent_contract_enforcement_verified']='YES'
   with path.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(r[0]));w.writeheader();w.writerows(r)
   with self.assertRaises(AssertionError):audit(p)
if __name__=='__main__':unittest.main()
