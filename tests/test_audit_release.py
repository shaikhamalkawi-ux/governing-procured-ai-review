import unittest,tempfile,shutil,json,csv,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_release import audit

class PublicCheckpointTests(unittest.TestCase):
    def test_original_release(self):
        q=audit(ROOT)
        self.assertEqual(q['status'],'PASS')
        self.assertEqual(q['unread'],2336)
    def test_duplicate_record_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            t=Path(t);(t/'data').mkdir()
            for name in ['R41_progress_summary.json','R41_220_provisional_decisions_PUBLICSAFE.csv','R40_14_sources_evidence_chart_PUBLICSAFE.csv']:
                shutil.copy2(ROOT/'data'/name,t/'data'/name)
            p=t/'data/R41_220_provisional_decisions_PUBLICSAFE.csv'
            with p.open(encoding='utf-8',newline='') as f:r=list(csv.reader(f))
            r[-1][0]=r[1][0]
            with p.open('w',encoding='utf-8',newline='') as f:csv.writer(f).writerows(r)
            with self.assertRaises(AssertionError):audit(t)
    def test_fake_completed_prisma_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            t=Path(t);(t/'data').mkdir()
            for name in ['R41_progress_summary.json','R41_220_provisional_decisions_PUBLICSAFE.csv','R40_14_sources_evidence_chart_PUBLICSAFE.csv']:
                shutil.copy2(ROOT/'data'/name,t/'data'/name)
            p=t/'data/R41_progress_summary.json';r=json.loads(p.read_text());r['PRISMA_ScR']='COMPLETED';p.write_text(json.dumps(r))
            with self.assertRaises(AssertionError):audit(t)

if __name__=='__main__':unittest.main()
