import csv, pathlib, shutil, sys, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_r42_direction import audit
class R42PublicAuditTests(unittest.TestCase):
    def test_valid_delta(self):
        d=audit(ROOT)
        self.assertEqual(d['status'],'PASS')
        self.assertEqual(d['remaining'],2272)
    def test_reject_fake_inclusion(self):
        with tempfile.TemporaryDirectory() as tmp:
            t=pathlib.Path(tmp);(t/'data').mkdir()
            for file in ('R41_220_provisional_decisions_PUBLICSAFE.csv','R42_B04_64_provisional_decisions_PUBLICSAFE.csv','R42_progress_summary.json'):
                shutil.copy2(ROOT/'data'/file,t/'data'/file)
            p=t/'data/R42_B04_64_provisional_decisions_PUBLICSAFE.csv'
            with p.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
            rows[0]['final_review_inclusion']='INCLUDE'
            with p.open('w',encoding='utf-8',newline='') as f:
                w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
            with self.assertRaises(AssertionError):audit(t)
if __name__=='__main__':unittest.main()
