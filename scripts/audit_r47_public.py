#!/usr/bin/env python3
"""Public-only integrity checks for the R47 provisional 124-case delta."""
import pathlib,csv,json,collections,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def audit(root=ROOT):
 root=pathlib.Path(root);d=root/'data'
 p=read(d/'R47_124_CaseText_Triage_PUBLICSAFE.csv');s=json.loads((d/'R47_ProgressSummary.json').read_text())
 assert len(p)==len({r['cluster_id'] for r in p})==124
 assert set(p[0])=={'cluster_id','r47_sequence','prior_selection_stratum','provisional_label','source_reason_code','source_text_status','review_mode','final_inclusion'}
 assert all(re.fullmatch(r'BIB\d{5}',r['cluster_id']) for r in p)
 assert [int(x['r47_sequence']) for x in p]==list(range(1,125))
 assert all(x['review_mode']=='AI_ASSISTED_SOURCE_TEXT_TRIAGE_NOT_FULLTEXT' and x['final_inclusion']=='NOT_DETERMINED' for x in p)
 assert dict(sorted(collections.Counter(x['provisional_label'] for x in p).items()))==s['R47_provisional_label_counts']
 assert s['original_bibliographic_identity_groups']==2556 and s['R46_individually_reasoned_first_pass']==648
 assert s['new_R47_AI_assisted_case_text_124']==124 and s['cumulative_provisional_case_text']==772 and s['remaining_without_case_text']==1784
 assert s['PRISMA_status']=='NOT_COMPLETED' and s['final_inclusions']=='NOT_DETERMINED'
 return {'status':'PASS','new':124,'cumulative':772,'unread':1784,'source_stage':'NON_FINAL'}
if __name__=='__main__':print(json.dumps(audit(),indent=2))
