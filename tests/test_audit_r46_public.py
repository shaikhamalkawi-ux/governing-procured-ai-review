"""Mutation guards for the R46 public-safe checkpoint."""
import csv,json,pathlib,shutil,sys,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_r46_public import audit
FILES=[
'R41_220_provisional_decisions_PUBLICSAFE.csv','R42_B04_64_provisional_decisions_PUBLICSAFE.csv','R43_B05_120_provisional_decisions_PUBLICSAFE.csv',
'R44_64_Provisional_RecallStress_PUBLICSAFE.csv','R45_112_Provisional_Routes_PUBLICSAFE.csv',
'R46_All1976_IDOnly_MachineRoutes_PUBLICSAFE.csv','R46_68_SourceReasons_PUBLICSAFE.csv',
'R46_100_RetrievalPriority_IDonly_PUBLICSAFE.csv','R46_4_OriginalSource_Verification_PUBLICSAFE.csv',
'R46_8_FurtherPublisherBoundaries_PUBLICSAFE.csv','R46_Seven_Exact_TextIdentity_IDonly_PUBLICSAFE.csv','R46_ProgressSummary_PublicSafe.json']
class R46PublicTests(unittest.TestCase):
    def test_pristine_public_release(self):self.assertEqual(audit(ROOT)['status'],'PASS')
    def _temp(self):
        z=tempfile.TemporaryDirectory();base=pathlib.Path(z.name);(base/'data').mkdir()
        for f in FILES:shutil.copy2(ROOT/'data'/f,base/'data'/f)
        return z,base
    @staticmethod
    def _mutate_csv(p,fn):
        with p.open(encoding='utf-8',newline='') as f:r=list(csv.DictReader(f))
        fn(r)
        with p.open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(r[0]));w.writeheader();w.writerows(r)
    def test_duplicate_unread_record_rejected(self):
        z,b=self._temp()
        with z:
            p=b/'data/R46_All1976_IDOnly_MachineRoutes_PUBLICSAFE.csv'
            self._mutate_csv(p,lambda r:r[0].update({'cluster_id':r[1]['cluster_id']}))
            with self.assertRaises(AssertionError):audit(b)
    def test_case_not_in_unread_rejected(self):
        z,b=self._temp()
        with z:
            p=b/'data/R46_68_SourceReasons_PUBLICSAFE.csv'
            self._mutate_csv(p,lambda r:r[0].update({'cluster_id':'BIB00001'}))
            with self.assertRaises(AssertionError):audit(b)
    def test_fake_final_inclusion_rejected(self):
        z,b=self._temp()
        with z:
            p=b/'data/R46_68_SourceReasons_PUBLICSAFE.csv'
            self._mutate_csv(p,lambda r:r[0].update({'final_inclusion':'INCLUDE'}))
            with self.assertRaises(AssertionError):audit(b)
    def test_fake_machine_individual_read_rejected(self):
        z,b=self._temp()
        with z:
            p=b/'data/R46_All1976_IDOnly_MachineRoutes_PUBLICSAFE.csv'
            self._mutate_csv(p,lambda r:r[0].update({'review_stage':'INDIVIDUAL_FULLTEXT_READ'}))
            with self.assertRaises(AssertionError):audit(b)
    def test_leaked_abstract_column_rejected(self):
        z,b=self._temp()
        with z:
            p=b/'data/R46_68_SourceReasons_PUBLICSAFE.csv'
            self._mutate_csv(p,lambda r:r[0].update({'abstract':'licensed original text'}))
            with self.assertRaises(AssertionError):audit(b)
    def test_mutated_denominator_rejected(self):
        z,b=self._temp()
        with z:
            p=b/'data/R46_ProgressSummary_PublicSafe.json'
            data=json.loads(p.read_text(encoding='utf-8'));data['cumulative_individually_reasoned_firstpass']=2556;p.write_text(json.dumps(data))
            with self.assertRaises(AssertionError):audit(b)
    def test_unresolved_family_removed_rejected(self):
        z,b=self._temp()
        with z:
            p=b/'data/R46_Seven_Exact_TextIdentity_IDonly_PUBLICSAFE.csv'
            self._mutate_csv(p,lambda r:r[0].update({'identity_action':'MERGED_FINAL'}))
            with self.assertRaises(AssertionError):audit(b)
if __name__=='__main__':unittest.main()
