"""Positive and negative controls for R49 release integrity (not source correctness)."""
import csv,pathlib,shutil,sys,tempfile,unittest,json
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_r49_public import audit,PREDECESSORS
F=[name for name,*_ in PREDECESSORS]+['R49_384_TitleAbstract_Provisional_Routes_PUBLICSAFE.csv','R49_progress_summary_PUBLICSAFE.json','R49_6_Semantic_Falsification_Corrections_PUBLICSAFE.csv','R49_3_Hidden_SourceCandidateChecks_PUBLICSAFE.csv','R49_18_SourceClaimEvidenceRoles_PUBLICSAFE.csv','R46_100_RetrievalPriority_IDonly_PUBLICSAFE.csv','R49_104_RetrievalPriorities_IDOnly_PUBLICSAFE.csv','R49_US_FederalAI_Award_vs_Oversight_Nonjoin_Control_PUBLICSAFE.csv']
class TestR49Public(unittest.TestCase):
 def copy(self):
  td=tempfile.TemporaryDirectory();t=pathlib.Path(td.name);(t/'data').mkdir()
  for name in F:shutil.copy2(ROOT/'data'/name,t/'data'/name)
  return td,t
 def modify(self,root,filename,callback):
  p=root/'data'/filename
  with p.open(encoding='utf-8',newline='') as f:rr=list(csv.DictReader(f))
  callback(rr)
  with p.open('w',encoding='utf-8',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(rr[0]));w.writeheader();w.writerows(rr)
 def test_release(self):self.assertTrue(audit(ROOT)['PASS'])
 def test_reject_old_id_collision(self):
  td,t=self.copy()
  with td:
   self.modify(t,'R49_384_TitleAbstract_Provisional_Routes_PUBLICSAFE.csv',lambda x:x[0].update(cluster_id='BIB00001'))
   with self.assertRaises(AssertionError):audit(t)
 def test_reject_final_inclusion(self):
  td,t=self.copy()
  with td:
   self.modify(t,'R49_384_TitleAbstract_Provisional_Routes_PUBLICSAFE.csv',lambda x:x[0].update(final_study_inclusion='INCLUDE'))
   with self.assertRaises(AssertionError):audit(t)
 def test_reject_licensed_abstract(self):
  td,t=self.copy()
  with td:
   self.modify(t,'R49_384_TitleAbstract_Provisional_Routes_PUBLICSAFE.csv',lambda x:x[0].update(abstract_PRIVATE='Restricted input'))
   with self.assertRaises(AssertionError):audit(t)
 def test_reject_fake_coverage(self):
  td,t=self.copy()
  with td:
   p=t/'data/R49_progress_summary_PUBLICSAFE.json';d=json.loads(p.read_text());d['pending_original_source_identities']=0;p.write_text(json.dumps(d))
   with self.assertRaises(AssertionError):audit(t)
 def test_reject_supplier_enforcement_claim(self):
  td,t=self.copy()
  with td:
   self.modify(t,'R49_18_SourceClaimEvidenceRoles_PUBLICSAFE.csv',lambda x:x[0].update(X_attributed_contract_remedy_outcome='Y'))
   with self.assertRaises(AssertionError):audit(t)
 def test_reject_missing_hold(self):
  td,t=self.copy()
  with td:
   self.modify(t,'R49_384_TitleAbstract_Provisional_Routes_PUBLICSAFE.csv',lambda x:next(y for y in x if y['cluster_id']=='BIB00146').update(provisional_label='OUTSIDE_SCOPE_TA'))
   with self.assertRaises(AssertionError):audit(t)
 def test_reject_wrong_vendor_merge(self):
  td,t=self.copy()
  with td:
   self.modify(t,'R49_US_FederalAI_Award_vs_Oversight_Nonjoin_Control_PUBLICSAFE.csv',lambda x:next(y for y in x if y['source_id']=='EXT_FACEPTION_MEDIA_2016').update(vendor_legal_or_brand='CLEARVIEW AI INC'))
   with self.assertRaises(AssertionError):audit(t)
 def test_reject_extra_queue_record(self):
  td,t=self.copy()
  with td:
   self.modify(t,'R49_104_RetrievalPriorities_IDOnly_PUBLICSAFE.csv',lambda x:x[0].update(cluster_id='BIB99999'))
   with self.assertRaises(AssertionError):audit(t)
if __name__=='__main__':unittest.main()
