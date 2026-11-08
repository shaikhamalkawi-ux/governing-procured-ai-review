#!/usr/bin/env python3
"""Public integrity audit only. Cannot prove original source truth or final eligibility."""
import csv,collections,json,pathlib,re
BASE=pathlib.Path(__file__).resolve().parents[1]
PREDECESSORS=(('R41_220_provisional_decisions_PUBLICSAFE.csv','record_id',220),('R42_B04_64_provisional_decisions_PUBLICSAFE.csv','cluster_id',64),('R43_B05_120_provisional_decisions_PUBLICSAFE.csv','cluster_id',120),('R44_64_Provisional_RecallStress_PUBLICSAFE.csv','cluster_id',64),('R45_112_Provisional_Routes_PUBLICSAFE.csv','cluster_id',112),('R46_68_SourceReasons_PUBLICSAFE.csv','cluster_id',68),('R47_124_CaseText_Triage_PUBLICSAFE.csv','cluster_id',124),('R48_192_SourceTriage_PUBLICSAFE.csv','cluster_id',192))
LABELS={'AI_USED_IN_PROCUREMENT_ONLY','CONTEXT_ONLY','DIRECT_TA_POSSIBLE','HOLD_DIRECTION_OR_UNIT','OUTSIDE_SCOPE_TA'}
def rows(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def audit(root=BASE):
 root=pathlib.Path(root);d=root/'data'; ids=[]
 for file,col,n in PREDECESSORS:
  a=rows(d/file);assert len(a)==n,(file,len(a));ids.extend(x[col] for x in a)
 assert len(ids)==964 and len(set(ids))==964
 r=rows(d/'R49_384_TitleAbstract_Provisional_Routes_PUBLICSAFE.csv')
 assert len(r)==384 and len(set(x['cluster_id'] for x in r))==384
 assert set(r[0])=={'cluster_id','r49_sequence','r49_stratum','provisional_label','reason_code','assessment_type','final_study_inclusion'},'provider copyright fields not allowed'
 assert not set(ids)&{x['cluster_id'] for x in r}
 assert len(set(ids+[x['cluster_id'] for x in r]))==1348
 assert [int(x['r49_sequence']) for x in r]==list(range(1,385))
 assert all(re.fullmatch(r'BIB\d{5}',x['cluster_id']) for x in r)
 assert all(x['provisional_label'] in LABELS and x['reason_code'] and x['final_study_inclusion']=='NOT_DETERMINED' for x in r)
 assert all(x['assessment_type'] in {'AI_ASSISTED_RULE_GATED_SOURCE_TEXT_BRIEF_NOT_FULLTEXT','AI_ASSISTED_CASE_SPECIFIC_SOURCE_SUBJECT_RECHECK_NOT_FULLTEXT'} for x in r)
 assert sum(x['assessment_type']=='AI_ASSISTED_CASE_SPECIFIC_SOURCE_SUBJECT_RECHECK_NOT_FULLTEXT' for x in r)==48
 strata=dict(sorted(collections.Counter(x['r49_stratum'] for x in r).items()))
 assert len(strata)==6 and set(strata.values())=={64}
 counts=dict(sorted(collections.Counter(x['provisional_label'] for x in r).items()))
 assert counts=={'AI_USED_IN_PROCUREMENT_ONLY':2,'CONTEXT_ONLY':80,'DIRECT_TA_POSSIBLE':1,'HOLD_DIRECTION_OR_UNIT':14,'OUTSIDE_SCOPE_TA':287}
 for i,category in [('BIB00634','DIRECT_TA_POSSIBLE'),('BIB00146','HOLD_DIRECTION_OR_UNIT'),('BIB00099','HOLD_DIRECTION_OR_UNIT')]:
  assert next(x for x in r if x['cluster_id']==i)['provisional_label']==category
 s=json.loads((d/'R49_progress_summary_PUBLICSAFE.json').read_text(encoding='utf-8'))
 assert (s['original_bibliographic_identity_groups'],s['previous_nonfinal_firstpass_routes'],s['new_R49_nonfinal_firstpass_routes'],s['cumulative_nonfinal_firstpass_routes'],s['pending_original_source_identities'])==(2556,964,384,1348,1208)
 assert s['frozen_R49_strata']==strata and s['R49_provisional_source_routes']==counts
 assert s['original_fulltext_eligibility']=='NOT_DETERMINED' and s['PRISMA_ScR']=='NOT_COMPLETED'
 assert s['source_provider_data_in_public_release'] is False and s['is_representative_sensitivity_estimate'] is False
 corrections=rows(d/'R49_6_Semantic_Falsification_Corrections_PUBLICSAFE.csv');assert len(corrections)==6
 assert set(x['cluster_id'] for x in corrections)=={'BIB00634','BIB00146','BIB00099','BIB00241','BIB02535','BIB00224'}
 assert all(x['fulltext_eligibility']=='NOT_DETERMINED' for x in corrections)
 assert all(x['updated_label']==next(y['provisional_label'] for y in r if y['cluster_id']==x['cluster_id']) for x in corrections)
 checks=rows(d/'R49_3_Hidden_SourceCandidateChecks_PUBLICSAFE.csv');assert len(checks)==3
 assert {x['cluster_id'] for x in checks}=={'BIB00634','BIB00146','BIB00099'}
 assert all(x['contract_enforcement_gate'].startswith('NO_') for x in checks)
 orig_source_chart=rows(d/'R49_18_SourceClaimEvidenceRoles_PUBLICSAFE.csv');assert len(orig_source_chart)==18
 assert len({x['source_id'] for x in orig_source_chart})==18
 assert [x['source_id'] for x in orig_source_chart if x['C_contract_instrument']=='Y']==['DOC_NNC_2025']
 assert not any(x['X_attributed_contract_remedy_outcome']=='Y' for x in orig_source_chart)
 assert all(x['final_review_inclusion']=='NOT_DETERMINED' for x in orig_source_chart)
 oldqueue=rows(d/'R46_100_RetrievalPriority_IDonly_PUBLICSAFE.csv');assert len(oldqueue)==100
 q=rows(d/'R49_104_RetrievalPriorities_IDOnly_PUBLICSAFE.csv');assert len(q)==104
 assert len({x['cluster_id'] for x in q})==104
 assert set(x['cluster_id'] for x in oldqueue).issubset({x['cluster_id'] for x in q})
 assert {x['cluster_id'] for x in q if x['priority_batch']=='R49_ADDED'}=={'BIB00634','BIB00146','BIB00099'}
 assert {x['cluster_id'] for x in q if x['priority_batch']=='R48_ADDED'}=={'BIB02569'}
 assert all(x['final_inclusion']=='NOT_DETERMINED' for x in q)
 cross=rows(d/'R49_US_FederalAI_Award_vs_Oversight_Nonjoin_Control_PUBLICSAFE.csv')
 assert len(cross)==3 and len({x['source_id'] for x in cross})==3
 award=next(x for x in cross if x['source_id']=='EXT_USASPENDING_CLEARVIEW_2021')
 gao=next(x for x in cross if x['source_id']=='EXT_GAO_CLEARVIEW_USERACCESS_2023_2024')
 faception=next(x for x in cross if x['source_id']=='EXT_FACEPTION_MEDIA_2016')
 assert award['vendor_legal_or_brand']=='CLEARVIEW AI INC' and award['award_or_contract_identifier']=='70CMSD21P00000127'
 assert gao['award_or_contract_identifier']=='UNLINKED_TO_USASPENDING_AWARD_ID' and 'TRAINING' in gao['supported_evidence_stage']
 assert 'Faception' in faception['vendor_legal_or_brand'] and 'FACEPTION' in faception['source_id'] and faception['vendor_legal_or_brand']!=award['vendor_legal_or_brand']
 return {'PASS':True,'R49_new':384,'firstpass_cumulative':1348,'remaining':1208,'original_source_cards':18,'falsification_cases':6,'retrieval_queue':104,'final_included':None,'PRISMA':'OPEN'}
if __name__=='__main__':print(json.dumps(audit(),indent=2))
