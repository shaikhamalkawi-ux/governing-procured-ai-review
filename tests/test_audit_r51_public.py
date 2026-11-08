import csv,shutil,json,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_r51_public import audit,PRIOR
FILES=[x[0] for x in PRIOR]+['R51_192_ProvisionalTitleAbstractRoutes_PUBLICSAFE.csv','R51_progress_summary.json','R51_17_OriginalSource_ClaimAudit_PUBLICSAFE.csv','R51_106_FulltextRetrieval_SourceGate_PUBLICSAFE.csv','R50_106_RetrievalPriority_IDonly_PUBLICSAFE.csv','R51_ReportFamily_Holds_PUBLICSAFE.csv']
class TestR51Conservation(unittest.TestCase):
 def copy(self):
  tmp=tempfile.TemporaryDirectory();t=Path(tmp.name);(t/'data').mkdir()
  for f in FILES:shutil.copy2(ROOT/'data'/f,t/'data'/f)
  return tmp,t
 def mutate(self,t,file,fn):
  p=t/'data'/file
  with p.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
  fn(rows)
  with p.open('w',encoding='utf-8',newline='') as f:
   writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
 def test_valid(self):self.assertEqual(audit(ROOT)['status'],'PASS')
 def test_prior_overlap_rejected(self):
  x,t=self.copy()
  with x:
   self.mutate(t,'R51_192_ProvisionalTitleAbstractRoutes_PUBLICSAFE.csv',lambda r:r[0].update(cluster_id='BIB00001'))
   with self.assertRaises(AssertionError):audit(t)
 def test_fake_final_admission_rejected(self):
  x,t=self.copy()
  with x:
   self.mutate(t,'R51_192_ProvisionalTitleAbstractRoutes_PUBLICSAFE.csv',lambda r:r[0].update(final_inclusion='INCLUDE'))
   with self.assertRaises(AssertionError):audit(t)
 def test_abstract_license_leak_rejected(self):
  x,t=self.copy()
  with x:
   self.mutate(t,'R51_192_ProvisionalTitleAbstractRoutes_PUBLICSAFE.csv',lambda r:r[0].update(abstract_PRIVATE='must_not_ship'))
   with self.assertRaises(AssertionError):audit(t)
 def test_conference_container_mislabel_rejected(self):
  x,t=self.copy()
  with x:
   self.mutate(t,'R51_106_FulltextRetrieval_SourceGate_PUBLICSAFE.csv',lambda r:next(z for z in r if z['report_identity_gate']=='CONFERENCE_PARENT_CHILD_HOLD').update(report_identity_gate='CONFIRMED_INDEPENDENT_STUDY'))
   with self.assertRaises(AssertionError):audit(t)
 def test_false_fulltext_inclusion_rejected(self):
  x,t=self.copy()
  with x:
   self.mutate(t,'R51_106_FulltextRetrieval_SourceGate_PUBLICSAFE.csv',lambda r:r[0].update(fulltext_final_eligibility='INCLUDED'))
   with self.assertRaises(AssertionError):audit(t)
 def test_source_card_url_gate(self):
  x,t=self.copy()
  with x:
   self.mutate(t,'R51_17_OriginalSource_ClaimAudit_PUBLICSAFE.csv',lambda r:r[0].update(original_public_locator='file:///private'))
   with self.assertRaises(AssertionError):audit(t)
 def test_summary_prisma_falsification_rejected(self):
  x,t=self.copy()
  with x:
   p=t/'data/R51_progress_summary.json';j=json.loads(p.read_text());j['PRISMA_ScR']='COMPLETED';p.write_text(json.dumps(j))
   with self.assertRaises(AssertionError):audit(t)
 def test_report_family_not_automerged(self):
  x,t=self.copy()
  with x:
   self.mutate(t,'R51_ReportFamily_Holds_PUBLICSAFE.csv',lambda r:r[0].update(decision='AUTO_MERGED'))
   with self.assertRaises(AssertionError):audit(t)
if __name__=='__main__':unittest.main()
