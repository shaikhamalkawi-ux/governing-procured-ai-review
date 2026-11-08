import csv,pathlib,shutil,sys,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_r44_public import audit
PUBLIC_FILES=['R41_220_provisional_decisions_PUBLICSAFE.csv','R42_B04_64_provisional_decisions_PUBLICSAFE.csv','R43_B05_120_provisional_decisions_PUBLICSAFE.csv','R44_64_Provisional_RecallStress_PUBLICSAFE.csv','R44_progress_summary.json','R44_Three_PublicSource_Gates_PUBLICSAFE.csv']
class R44ControlTests(unittest.TestCase):
 def test_valid_stress_sample(self):self.assertEqual(audit(ROOT)['status'],'PASS')
 def copy(self):
  temp=tempfile.TemporaryDirectory();p=pathlib.Path(temp.name);(p/'data').mkdir()
  for name in PUBLIC_FILES:shutil.copy2(ROOT/'data'/name,p/'data'/name)
  return temp,p
 def edit(self,p,func):
  q=p/'data/R44_64_Provisional_RecallStress_PUBLICSAFE.csv'
  with q.open(encoding='utf-8',newline='') as f:rr=list(csv.DictReader(f))
  func(rr)
  with q.open('w',encoding='utf-8',newline='') as f:
   w=csv.DictWriter(f,fieldnames=rr[0].keys());w.writeheader();w.writerows(rr)
 def test_reject_duplicate_earlier(self):
  t,p=self.copy()
  with t:
   self.edit(p,lambda rr:rr[0].update({'cluster_id':'BIB00433'}))
   with self.assertRaises(AssertionError):audit(p)
 def test_reject_fake_finality(self):
  t,p=self.copy()
  with t:
   self.edit(p,lambda rr:rr[0].update({'final_review_inclusion':'INCLUDE'}))
   with self.assertRaises(AssertionError):audit(p)
 def test_reject_licensed_title_column(self):
  t,p=self.copy()
  with t:
   self.edit(p,lambda rr:rr[0].update({'title':'private indexed metadata'}))
   with self.assertRaises(AssertionError):audit(p)
 def test_reject_low_signal_hold_erasure(self):
  t,p=self.copy()
  with t:
   self.edit(p,lambda rr:rr[1].update({'r44_provisional_label':'OUTSIDE_SCOPE_TA'}))
   with self.assertRaises(AssertionError):audit(p)
if __name__=='__main__':unittest.main()
