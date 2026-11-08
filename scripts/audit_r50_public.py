#!/usr/bin/env python3
"""Rights-safe structural source-check for 99aI R50, not a final eligibility reviewer."""
from pathlib import Path
import collections,csv,json,re
ROOT=Path(__file__).resolve().parents[1]
PRIOR=[('R41_220_provisional_decisions_PUBLICSAFE.csv','record_id',220),('R42_B04_64_provisional_decisions_PUBLICSAFE.csv','cluster_id',64),('R43_B05_120_provisional_decisions_PUBLICSAFE.csv','cluster_id',120),('R44_64_Provisional_RecallStress_PUBLICSAFE.csv','cluster_id',64),('R45_112_Provisional_Routes_PUBLICSAFE.csv','cluster_id',112),('R46_68_SourceReasons_PUBLICSAFE.csv','cluster_id',68),('R47_124_CaseText_Triage_PUBLICSAFE.csv','cluster_id',124),('R48_192_SourceTriage_PUBLICSAFE.csv','cluster_id',192),('R49_384_TitleAbstract_Provisional_Routes_PUBLICSAFE.csv','cluster_id',384)]
def read(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def audit(root=ROOT):
 root=Path(root);data=root/'data'
 old=[]
 for file,key,number in PRIOR:
  q=read(data/file)
  assert len(q)==number,(file,len(q),number)
  old.extend(r[key] for r in q)
 assert len(old)==len(set(old))==1348
 extra=read(data/'R50_96_SourceText_Triage_PUBLICSAFE.csv')
 rescue=read(data/'R50_3_New_Publisher_Rescue_Cases_PUBLICSAFE.csv')
 new=[r['cluster_id'] for r in extra+rescue]
 assert len(extra)==96 and len(rescue)==3 and len(set(new))==99
 assert not set(r['cluster_id'] for r in extra).intersection(old)
 assert set(r['cluster_id'] for r in rescue).issubset(old)
 assert set(r['cluster_id'] for r in rescue).issubset({x['record_id'] for x in read(data/'R41_220_provisional_decisions_PUBLICSAFE.csv')})
 assert all(re.fullmatch('BIB[0-9]{5}',x) for x in old+new)
 assert set(extra[0])=={'cluster_id','stratum','label','reason_code','assessment_stage','final_inclusion'}
 assert set(rescue[0])=={'cluster_id','label','reason_code','source_tier','publisher_url','supported_claim','boundary'}
 assert collections.Counter(r['stratum'] for r in extra)=={'A_TITLE_PUBLIC_AI':12,'B_TITLE_SUPPLIER_PROCUREMENT':24,'C_ABSTRACT_PUBLIC_AI_SAME_SENTENCE':36,'D_HASH_CONTROL':24}
 assert collections.Counter(r['label'] for r in extra)=={'OUTSIDE_SCOPE_TA':73,'CONTEXT_ONLY':13,'HOLD_DIRECTION_OR_UNIT':10}
 assert all(r['assessment_stage']=='AI_ASSISTED_TITLE_ABSTRACT_SOURCE_TEXT_NOT_FULLTEXT' and r['final_inclusion']=='NOT_DETERMINED' for r in extra)
 assert {r['cluster_id']:r['label'] for r in rescue}=={'BIB01200':'DIRECT_TA_POSSIBLE','BIB00196':'DIRECT_TA_POSSIBLE','BIB00229':'AI_USED_IN_PROCUREMENT_ONLY'}
 assert all(r['publisher_url'].startswith('https://') for r in rescue)
 summary=json.loads((data/'R50_progress_summary.json').read_text(encoding='utf-8'))
 assert summary['original_bibliographic_identity_groups']==2556
 assert (summary['previous_R49_nonfinal_firstpass'],summary['new_R50_provisional_title_abstract_source_text'],summary['R50_publisher_source_re_reviews_of_already_screened_R41'])==(1348,96,3)
 assert (summary['cumulative_nonfinal_firstpass'],summary['remaining_not_individually_screened'])==(1444,1112)
 assert summary['R49_inherited_fulltext_retrieval_priority_records']==104 and summary['R50_new_priority_fulltext_ids']==2 and summary['R50_priority_unique_IDs']==106
 assert summary['original_source_sha256']=='9cf7a0d07e7ebd80283437b21158c55c86559fbaa05780b4a0e6dcd58d98ce79'
 assert summary['independent_study_inclusion']=='NOT_DETERMINED' and summary['PRISMA_ScR']=='NOT_COMPLETED'
 assert summary['original_licensed_metadata_on_public_github'] is False
 priority=read(data/'R50_104_FullText_Retrieval_Status_PUBLICSAFE.csv')
 extra_priority=read(data/'R50_2_New_Fulltext_Retrieval_Leads_PUBLICSAFE.csv')
 assert len(priority)==104 and len(extra_priority)==2
 assert set(r['cluster_id'] for r in extra_priority)=={'BIB01200','BIB00196'}
 assert len({r['record_id'] for r in priority}|{r['cluster_id'] for r in extra_priority})==106
 assert all(r['fulltext_final_eligibility']=='NOT_DETERMINED' for r in priority)
 cards=read(data/'R50_20_Original_Source_ClaimBoundaries_PUBLICSAFE.csv')
 assert len(cards)==20 and len({r['record_id'] for r in cards})==20
 assert collections.Counter(r['corpus_relation'] for r in cards)=={'IN_FROZEN_2556':15,'OUTSIDE_FROZEN_SEARCH':3,'UPDATED_SEARCH_NOT_FROZEN':2}
 assert all(r['public_source_url'].startswith('https://') and r['non_inference_boundary'] for r in cards)
 gates=json.loads((data/'R50_PRISMA_GATES_NOT_FINAL.json').read_text(encoding='utf-8'))
 assert gates['status']=='NOT_COMPLETED' and gates['prisma_flow_final'] is False
 assert gates['adjudicated_unique_studies_included'] is None and gates['reports_sought_prisma'] is None
 return {'status':'PASS','nonfinal_firstpass':1444,'remaining':1112,'new_frozen_text_reads':96,'publisher_rechecks_of_R41_ids':3,'fulltext_priority_unique_ids':106,'source_cards':20,'PRISMA':'NOT_COMPLETED'}
if __name__=='__main__':print(json.dumps(audit(),indent=2))
