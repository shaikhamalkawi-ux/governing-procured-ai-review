#!/usr/bin/env python3
"""R45 public checkpoint integrity only; NO source validation, human review or PRISMA.
Runs without access to licensed Scopus/Web of Science exports.
"""
from pathlib import Path
import csv,collections,json,re
BASE=Path(__file__).resolve().parents[1]
def load(path):
 with path.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def audit(root=BASE):
 root=Path(root);d=root/'data'
 stages=[
  (load(d/'R41_220_provisional_decisions_PUBLICSAFE.csv'),'record_id',220),
  (load(d/'R42_B04_64_provisional_decisions_PUBLICSAFE.csv'),'cluster_id',64),
  (load(d/'R43_B05_120_provisional_decisions_PUBLICSAFE.csv'),'cluster_id',120),
  (load(d/'R44_64_Provisional_RecallStress_PUBLICSAFE.csv'),'cluster_id',64),
  (load(d/'R45_112_Provisional_Routes_PUBLICSAFE.csv'),'cluster_id',112),
 ]
 all_ids=[]
 for rows,k,n in stages:
  assert len(rows)==n
  assert all(re.fullmatch(r'BIB\d{5}',r[k]) for r in rows)
  all_ids.extend(r[k] for r in rows)
 assert len(all_ids)==len(set(all_ids))==580
 new=stages[-1][0];s=json.loads((d/'R45_Public_ProgressSummary.json').read_text(encoding='utf-8'))
 assert set(new[0])=={'cluster_id','r45_sequence','sample_stratum','r45_provisional_label','r45_direction','reviewer_type','final_inclusion'},'unexpected licensed provider metadata column'
 assert [int(x['r45_sequence']) for x in new]==list(range(1,113))
 assert all(x['reviewer_type']=='AI_ASSISTED_SINGLE_PASS' and x['final_inclusion']=='NOT_DETERMINED' and x['r45_direction'] for x in new)
 assert dict(collections.Counter(x['sample_stratum'] for x in new))=={'HIGH_TOP32':32,'MID_HASH32':32,'LOW_HASH32':32,'VENDOR_ENRICH16':16}
 labels=dict(sorted(collections.Counter(x['r45_provisional_label'] for x in new).items()))
 assert labels==s['new_R45_provisional_label_counts']
 assert s['provisional_bibliographic_identity_groups']==2556 and s['new_R45_AI_assisted_first_pass']==112
 assert s['inherited_previous_AI_assisted_first_pass']==468 and s['cumulative_AI_assisted_first_pass']==580
 assert s['individual_first_pass_unread']==1976 and 580+1976==2556
 assert s['PRISMA_ScR']=='NOT_COMPLETED' and s['final_fulltext_inclusion']=='NOT_DETERMINED' and s['new_fulltext_admissions']==0
 assert s['independent_human_second_screen']=='NOT_PERFORMED' and s['automated_signals_are_eligibility_decisions'] is False
 chart=load(d/'R45_13_PublicSource_ClaimBoundaries.csv')
 assert len(chart)==13 and len(set(x['source_family_id'] for x in chart))==7
 assert set(chart[0])=={'original_record_id','source_family_id','evidence_tier','primary_public_url','supportable_proposition','evidence_role','strict_inference_boundary','independent_contract_enforcement_verified','final_fulltext_inclusion'}
 assert all(x['primary_public_url'].startswith('https://') and x['final_fulltext_inclusion']=='NOT_DETERMINED' and x['independent_contract_enforcement_verified']=='NO' for x in chart)
 holds=load(d/'R45_Identity_Holds_IDonly_PUBLICSAFE.csv')
 exact={tuple(sorted([x['cluster_id']]+x['possible_family_members'].split(';'))) for x in holds if x['flag_type']=='EXACT_TITLE_ABSTRACT'}
 assert len(exact)==7 and len({i for group in exact for i in group})==17
 assert s['possible_exact_title_abstract_groups']==7
 assert all(x['identity_decision']=='HOLD_NOT_AUTOMERGED' for x in holds)
 return {'status':'PASS','public_records_firstpass':580,'added_R45':112,'unread':1976,'source_claim_cells':13,'source_families':7,'identity_groups_hold':7,'stage':'AI_PROVISIONAL_NO_ELIGIBILITY'}
if __name__=='__main__':print(json.dumps(audit(),indent=2))
