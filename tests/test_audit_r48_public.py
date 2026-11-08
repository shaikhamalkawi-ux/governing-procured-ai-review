import csv, json, pathlib, sys, tempfile, shutil, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_r48_public import audit,STAGES
class R48SourceSafetyTests(unittest.TestCase):
    def stage(self):
        td=tempfile.TemporaryDirectory(); r=pathlib.Path(td.name); (r/'data').mkdir()
        for n,_,_ in STAGES:shutil.copy2(ROOT/'data'/n,r/'data'/n)
        for n in ['R48_progress_summary_PUBLICSAFE.json','R48_12_OriginalSource_EvidenceBoundary_PublicSafe.csv','R48_Family_Holds_PublicSafe.csv']:
            shutil.copy2(ROOT/'data'/n,r/'data'/n)
        return td,r
    def alter(self, r, fn):
        p=r/'data/R48_192_SourceTriage_PUBLICSAFE.csv'
        with p.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
        fn(rows)
        with p.open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    def test_original(self):
        self.assertEqual(audit(ROOT)['result'],'PASS')
    def test_duplicate_old_id_rejected(self):
        t,r=self.stage()
        with t:
            self.alter(r,lambda x:x[0].update({'cluster_id':'BIB00001'}))
            with self.assertRaises(AssertionError):audit(r)
    def test_duplicate_new_id_rejected(self):
        t,r=self.stage()
        with t:
            self.alter(r,lambda x:x[0].update({'cluster_id':x[1]['cluster_id']}))
            with self.assertRaises(AssertionError):audit(r)
    def test_fake_final_inclusion_rejected(self):
        t,r=self.stage()
        with t:
            self.alter(r,lambda x:x[0].update({'final_inclusion':'INCLUDE'}))
            with self.assertRaises(AssertionError):audit(r)
    def test_fake_fulltext_rejected(self):
        t,r=self.stage()
        with t:
            self.alter(r,lambda x:x[0].update({'fulltext_status':'ASSESSED'}))
            with self.assertRaises(AssertionError):audit(r)
    def test_license_leak_column_rejected(self):
        t,r=self.stage()
        with t:
            self.alter(r,lambda x:x[0].update({'original_abstract':'Restricted-index text'}))
            with self.assertRaises(AssertionError):audit(r)
    def test_missing_stratum_rejected(self):
        t,r=self.stage()
        with t:
            self.alter(r,lambda x:x[0].update({'r48_stratum':'ARTIFICIAL_EXTRA'}))
            with self.assertRaises(AssertionError):audit(r)
    def test_false_eligibility_totals_rejected(self):
        t,r=self.stage()
        with t:
            f=r/'data/R48_progress_summary_PUBLICSAFE.json';j=json.loads(f.read_text(encoding='utf-8'));j['pending_individual_firstpass']=0;f.write_text(json.dumps(j))
            with self.assertRaises(AssertionError):audit(r)
    def test_source_card_misrepresentation_rejected(self):
        t,r=self.stage()
        with t:
            p=r/'data/R48_12_OriginalSource_EvidenceBoundary_PublicSafe.csv'
            with p.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
            for row in rows:
                if row['source_id']=='BIB02569':row['source_access_tier']='AI_INVENTED'
            with p.open('w',encoding='utf-8',newline='') as f:
                w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
            with self.assertRaises(AssertionError):audit(r)
if __name__=='__main__':unittest.main()
