#!/usr/bin/env python3
"""Reproducibility QA for R44 public-safe derived labels. No licensed source text needed."""
import csv,collections,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def rows(path):
 with pathlib.Path(path).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def audit(root=ROOT):
 root=pathlib.Path(root)
 prev=[r['record_id'] for r in rows(root/'data/R41_220_provisional_decisions_PUBLICSAFE.csv')]
 prev += [r['cluster_id'] for r in rows(root/'data/R42_B04_64_provisional_decisions_PUBLICSAFE.csv')]
 prev += [r['cluster_id'] for r in rows(root/'data/R43_B05_120_provisional_decisions_PUBLICSAFE.csv')]
 current=rows(root/'data/R44_64_Provisional_RecallStress_PUBLICSAFE.csv')
 info=json.loads((root/'data/R44_progress_summary.json').read_text(encoding='utf-8'))
 assert len(prev)==404 and len(set(prev))==404
 assert len(current)==64 and len({r['cluster_id'] for r in current})==64
 assert not set(prev).intersection(r['cluster_id'] for r in current)
 assert set(current[0])=={'cluster_id','r44_sequence','control_band','r44_provisional_label','r44_direction','reviewer_type','final_review_inclusion'},'licensed source columns not allowed in public'
 assert [int(r['r44_sequence']) for r in current]==list(range(1,65))
 assert all(r['reviewer_type']=='AI_ASSISTED_SINGLE_PASS' and r['final_review_inclusion']=='NOT_DETERMINED' for r in current)
 assert dict(collections.Counter(r['control_band'] for r in current))=={'LOW_SIGNAL_SAFETY_SAMPLE':32,'MID_SIGNAL_RECALL_SAMPLE':32}
 assert dict(sorted(collections.Counter(r['r44_provisional_label'] for r in current).items()))==info['new_AI_assisted_labels']
 assert [r['cluster_id'] for r in current if r['control_band']=='LOW_SIGNAL_SAFETY_SAMPLE' and r['r44_direction']=='PUBLIC_CLIENT_OF_SPYWARE_AI_FUNCTION_UNVERIFIED' and r['r44_provisional_label']=='HOLD_DIRECTION_OR_UNIT']==['BIB00433']
 assert (info['original_bibliographic_identity_groups'],info['inherited_AI_firstpass'],info['new_64_individually_read_AI_firstpass'],info['cumulative_AI_firstpass'],info['unread'])==(2556,404,64,468,2088)
 assert info['PRISMA_ScR']=='NOT_COMPLETED' and info['final_inclusion']=='NOT_DETERMINED'
 assert info['no_representative_sensitivity_claim']=='STRESSED_CONTROL_SAMPLE_NOT_POPULATION_ESTIMATE'
 linked=rows(root/'data/R44_Three_PublicSource_Gates_PUBLICSAFE.csv')
 assert len(linked)==3
 assert set(r['record_id'] for r in linked)=={'BIB00433','BIB01683','BIB01917'}
 assert all(r['final_study_inclusion']=='NOT_DETERMINED' for r in linked)
 return {'status':'PASS','first_pass_new':64,'cumulative_first_pass':468,'unread':2088,'low_signal_AIfunc_hold':'BIB00433','human_R2':False,'final_prisma':False}
if __name__=='__main__':print(json.dumps(audit(),indent=2))
