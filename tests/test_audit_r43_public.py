import csv,json,pathlib,sys,shutil,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_r43_public import audit
FILES=['R41_220_provisional_decisions_PUBLICSAFE.csv','R42_B04_64_provisional_decisions_PUBLICSAFE.csv','R43_B05_120_provisional_decisions_PUBLICSAFE.csv','R43_progress_summary.json','R43_Original_Source_Verification_PublicSafe.csv']
class R43AuditTests(unittest.TestCase):
 def test_original(self):
    self.assertEqual(audit(ROOT)['status'],'PASS')
 def _clone(self):
    tmp=tempfile.TemporaryDirectory();t=pathlib.Path(tmp.name);(t/'data').mkdir()
    for f in FILES:shutil.copy2(ROOT/'data'/f,t/'data'/f)
    return tmp,t
 def test_fake_final_inclusion_rejected(self):
    t,p=self._clone()
    with t:
      f=p/'data/R43_B05_120_provisional_decisions_PUBLICSAFE.csv'
      with f.open(encoding='utf-8',newline='') as h:rows=list(csv.DictReader(h))
      rows[0]['final_review_inclusion']='INCLUDE'
      with f.open('w',encoding='utf-8',newline='') as h:
        w=csv.DictWriter(h,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
      with self.assertRaises(AssertionError):audit(p)
 def test_old_row_duplication_rejected(self):
    t,p=self._clone()
    with t:
      f=p/'data/R43_B05_120_provisional_decisions_PUBLICSAFE.csv'
      with f.open(encoding='utf-8',newline='') as h:rows=list(csv.DictReader(h))
      rows[0]['cluster_id']='BIB00269'
      with f.open('w',encoding='utf-8',newline='') as h:
        w=csv.DictWriter(h,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
      with self.assertRaises(AssertionError):audit(p)
 def test_unlicensed_abstract_column_rejected(self):
    t,p=self._clone()
    with t:
      f=p/'data/R43_B05_120_provisional_decisions_PUBLICSAFE.csv'
      with f.open(encoding='utf-8',newline='') as h:rows=list(csv.DictReader(h))
      rows[0]['abstract']='SHOULD_NOT_BE_PUBLIC'
      with f.open('w',encoding='utf-8',newline='') as h:
        w=csv.DictWriter(h,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
      with self.assertRaises(AssertionError):audit(p)
if __name__=='__main__':unittest.main()
