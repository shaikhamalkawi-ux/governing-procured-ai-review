import pathlib,sys,unittest,shutil,tempfile,csv,json
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from audit_r50_public import audit
class R50Tests(unittest.TestCase):
 def test_clean(self):self.assertEqual(audit(ROOT)['status'],'PASS')
 def clone(self):
  td=tempfile.TemporaryDirectory();root=pathlib.Path(td.name);shutil.copytree(ROOT/'data',root/'data');return td,root
 def mutate_rows(self,root,name,mutator):
  p=root/'data'/name
  with p.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
  mutator(rows)
  with p.open('w',encoding='utf-8',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 def test_fake_inclusion_rejected(self):
  td,r=self.clone()
  with td:
   self.mutate_rows(r,'R50_96_SourceText_Triage_PUBLICSAFE.csv',lambda rows:rows[0].update({'final_inclusion':'INCLUDE'}))
   with self.assertRaises(AssertionError):audit(r)
 def test_prior_id_duplicate_rejected(self):
  td,r=self.clone()
  with td:
   self.mutate_rows(r,'R50_96_SourceText_Triage_PUBLICSAFE.csv',lambda rows:rows[0].update({'cluster_id':'BIB00336'}))
   with self.assertRaises(AssertionError):audit(r)
 def test_licensed_column_rejected(self):
  td,r=self.clone()
  with td:
   self.mutate_rows(r,'R50_96_SourceText_Triage_PUBLICSAFE.csv',lambda rows:rows[0].update({'abstract':'licensed text'}))
   with self.assertRaises(AssertionError):audit(r)
 def test_spurious_fulltext_inclusion_rejected(self):
  td,r=self.clone()
  with td:
   self.mutate_rows(r,'R50_104_FullText_Retrieval_Status_PUBLICSAFE.csv',lambda rows:rows[0].update({'fulltext_final_eligibility':'INCLUDE'}))
   with self.assertRaises(AssertionError):audit(r)
 def test_misclassified_rescue_rejected(self):
  td,r=self.clone()
  with td:
   self.mutate_rows(r,'R50_3_New_Publisher_Rescue_Cases_PUBLICSAFE.csv',lambda rows:rows[2].update({'label':'DIRECT_TA_POSSIBLE'}))
   with self.assertRaises(AssertionError):audit(r)
 def test_fake_prisma_rejected(self):
  td,r=self.clone()
  with td:
   f=r/'data/R50_PRISMA_GATES_NOT_FINAL.json';j=json.loads(f.read_text());j['prisma_flow_final']=True;f.write_text(json.dumps(j))
   with self.assertRaises(AssertionError):audit(r)
if __name__=='__main__':unittest.main()
