#!/usr/bin/env python3
"""Rights-safe R51 integrity audit. Not a truth/eligibility audit and not a PRISMA report."""
import csv,json,collections,pathlib,re,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
PRIOR=[('R41_220_provisional_decisions_PUBLICSAFE.csv','record_id',220),('R42_B04_64_provisional_decisions_PUBLICSAFE.csv','cluster_id',64),('R43_B05_120_provisional_decisions_PUBLICSAFE.csv','cluster_id',120),('R44_64_Provisional_RecallStress_PUBLICSAFE.csv','cluster_id',64),('R45_112_Provisional_Routes_PUBLICSAFE.csv','cluster_id',112),('R46_68_SourceReasons_PUBLICSAFE.csv','cluster_id',68),('R47_124_CaseText_Triage_PUBLICSAFE.csv','cluster_id',124),('R48_192_SourceTriage_PUBLICSAFE.csv','cluster_id',192),('R49_384_TitleAbstract_Provisional_Routes_PUBLICSAFE.csv','cluster_id',384),('R50_96_SourceText_Triage_PUBLICSAFE.csv','cluster_id',96)]
ALLOWED={'AI_USED_IN_PROCUREMENT_ONLY','CONTEXT_ONLY','HOLD_DIRECTION_OR_UNIT','OUTSIDE_SCOPE_TA','DIRECT_TA_POSSIBLE'}
def get(path):
 with path.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def audit(root=ROOT):
 root=pathlib.Path(root);d=root/'data';old=[]
 for file,col,num in PRIOR:
  rows=get(d/file);assert len(rows)==num,(file,len(rows))
  old.extend(r[col] for r in rows)
 assert len(old)==len(set(old))==1444
 new=get(d/'R51_192_ProvisionalTitleAbstractRoutes_PUBLICSAFE.csv')
 assert len(new)==192 and len({r['cluster_id'] for r in new})==192
 assert len(set(old)|{r['cluster_id'] for r in new})==1636
 assert [int(r['r51_sequence']) for r in new]==list(range(1,193))
 assert all(re.fullmatch(r'BIB\d{5}',r['cluster_id']) for r in new)
 assert set(new[0])=={'cluster_id','r51_sequence','r51_stratum','provisional_label','reason_code','review_stage','final_inclusion'},'licensed titles/abstracts may not be published'
 assert all(r['provisional_label'] in ALLOWED and r['reason_code'] for r in new)
 assert all(r['review_stage']=='AI_ASSISTED_TITLE_ABSTRACT_NOT_FULLTEXT' and r['final_inclusion']=='NOT_DETERMINED' for r in new)
 s=json.loads((d/'R51_progress_summary.json').read_text(encoding='utf-8'))
 assert (s['source_identity_groups_original'],s['inherited_R50_provisional_firstpass'],s['new_R51_AI_assisted_source_text_provisional'],s['cumulative_provisional_firstpass'],s['remaining_not_yet_source_triaged'])==(2556,1444,192,1636,920)
 assert collections.Counter(r['provisional_label'] for r in new)==s['R51_new_labels']
 assert collections.Counter(r['r51_stratum'] for r in new)==s['R51_strata']
 assert s['final_inclusion']=='NOT_DETERMINED' and s['PRISMA_ScR']=='NOT_COMPLETED' and s['fulltext_admissions']=='NOT_DETERMINED' and s['independent_study_count']=='NOT_DETERMINED'
 assert s['licensed_source_released'] is False
 c=get(d/'R51_17_OriginalSource_ClaimAudit_PUBLICSAFE.csv');assert len(c)==17
 assert len(set(r['record_id'] for r in c))==17
 assert all(r['original_public_locator'].startswith('https://') and r['final_inclusion']=='NOT_DETERMINED' for r in c)
 assert set(c[0])=={'record_id','source_key','source_access_tier','original_public_locator','study_family','method_design_and_unit','what_procurement_evidence_supports','what_postaward_evidence_supports','do_not_infer','direction_scope','final_inclusion','publisher_checked_as_of'}
 q=get(d/'R51_106_FulltextRetrieval_SourceGate_PUBLICSAFE.csv');assert len(q)==106 and len({r['record_id'] for r in q})==106
 oldq=get(d/'R50_106_RetrievalPriority_IDonly_PUBLICSAFE.csv')
 assert {r['record_id'] for r in oldq}=={r['record_id'] for r in q}
 assert all(r['fulltext_final_eligibility']=='NOT_DETERMINED' for r in q)
 assert sum(r['report_identity_gate']=='CONFERENCE_PARENT_CHILD_HOLD' for r in q)==24
 assert sum(r['report_identity_gate']=='PROCEEDINGS_PAPER_VALIDATE_FULLTEXT' for r in q)==6
 assert sum(r['source_claim_card_present']=='YES' for r in q)==16
 families=get(d/'R51_ReportFamily_Holds_PUBLICSAFE.csv')
 assert len(families)==5 and all(r['decision'].startswith('HOLD') for r in families)
 assert sum(r['provisional_label']=='AI_USED_IN_PROCUREMENT_ONLY' for r in new)==3
 assert all(r['reason_code']!='AI_METHOD_USED_TO_ANALYSE_PUBLIC_PURCHASING' for r in new),'false cooccurrence not allowed'
 return {'status':'PASS','new_192':len(new),'cumulative':1636,'pending':920,'fulltext_priority':len(q),'source_cards':len(c),'conference_review_parent_holds':24,'source_checked_in_queue':16,'PRISMA':'NOT_COMPLETED'}
if __name__=='__main__':
 try:print(json.dumps(audit(),indent=2))
 except Exception as e:print('FAIL: '+repr(e),file=sys.stderr);raise
