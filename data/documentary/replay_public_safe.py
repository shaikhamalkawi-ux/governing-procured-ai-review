#!/usr/bin/env python3
"""Replay R29 proposition certificates from the frozen public-safe 28-event matrix.
No database exports, external network, human coding or access tokens required.
Determinism does not scientifically validate source interpretation.
"""
from pathlib import Path
import csv,hashlib,json,sys
HERE=Path(__file__).resolve().parent

def read(name):
 with (HERE/name).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
D='DOCUMENTED'
def cert_release(e):
 return ('SUPPORTED','Supplier implemented new AI software version') if (e['S_supplier_action']==D and e['specific_event_type']=='ALL_CAMERA_MODEL_ROLLOUT' and e['locator_verification']=='OFFICIAL_HTML_LOCATOR_ATTRIBUTED') else ('NOT_CERTIFIED','No verified supplier model release in this event')
def cert_arch(e):
 return ('SUPPORTED','Statutory-audit response; NOT contractual model remedy') if (e['S_supplier_action']==D and e['specific_event_type']=='ARCHIVE_RETENTION_CORRECTION' and e['authority_mechanism']=='STATUTORY_AUDIT_COMPLIANCE') else ('NOT_CERTIFIED','Not an independently audited archive correction')
def cert_enforce(e):
 return ('SUPPORTED','Contract authority and exercise linked') if (e['C_contract_entitlement']==D and e['X_exercised_oversight']==D and e['authority_mechanism']=='CONTRACT_ENFORCEMENT_EXPLICIT' and e['cross_link_C_to_X']==D) else ('NOT_CERTIFIED','No source-specific contract right exercised with a documented C->X link')
def cert_causal(e):
 ok=(all(e[k]==D for k in ['C_contract_entitlement','X_exercised_oversight','S_supplier_action','M_relevant_measurement','A_causal_attribution']) and all(e[k]==D for k in ['cross_link_C_to_X','cross_link_X_to_S','cross_link_S_to_M','cross_link_M_to_A']) and e['authority_mechanism']=='CONTRACT_ENFORCEMENT_EXPLICIT')
 return ('SUPPORTED','All five domains and four causal/provenance links documented') if ok else ('NOT_CERTIFIED','At least one necessary contract/oversight/remedy/outcome/attribution link missing')
def cert_retirement(e):
 return ('REPORTED_BY_AGENCY_IN_AUDIT','Programme retirement is NOT supplier sanction') if e['specific_event_type'] in ('PROGRAMME_RETIRED','PREPRODUCTION_RETIRED') else ('NOT_CERTIFIED','Event not a programme retirement')
RULES=[('SUPPLIER_MODEL_RELEASE',cert_release),('SUPPLIER_ARCHIVE_COMPLIANCE_FIX',cert_arch),('CONTRACTUAL_ENFORCEMENT_EXERCISED',cert_enforce),('REMEDY_CAUSED_PUBLIC_BENEFIT',cert_causal),('PROGRAMME_RETIREMENT',cert_retirement)]
def main():
 evidence=read('R29_28Event_CXSM_A_SourceLedger.csv'); locked=read('R29_140Claim_SupportCertificates.csv'); assert len(evidence)==28 and len(locked)==140
 result=[]
 for e in evidence:
  for claim,fn in RULES:
   verdict,why=fn(e)
   result.append(dict(fact_id=e['fact_id'],case_id=e['case_id'],claim_id=claim,verdict=verdict,reason=why,source_url=e['source_url'],source_locator=e['source_locator']))
 assert result==locked,'FAIL: proposition outcomes differ from frozen expected certificates'
 assert sum(x['verdict']=='SUPPORTED' and x['claim_id']=='SUPPLIER_MODEL_RELEASE' for x in result)==1
 assert sum(x['verdict']=='SUPPORTED' and x['claim_id']=='SUPPLIER_ARCHIVE_COMPLIANCE_FIX' for x in result)==1
 assert sum(x['verdict']=='SUPPORTED' and x['claim_id']=='CONTRACTUAL_ENFORCEMENT_EXERCISED' for x in result)==0
 assert sum(x['verdict']=='SUPPORTED' and x['claim_id']=='REMEDY_CAUSED_PUBLIC_BENEFIT' for x in result)==0
 assert sum(x['verdict']=='REPORTED_BY_AGENCY_IN_AUDIT' and x['claim_id']=='PROGRAMME_RETIREMENT' for x in result)==3
 vic=next(x for x in evidence if x['fact_id']=='VIC-02')
 assert cert_release(vic)[0]=='SUPPORTED' and cert_causal(vic)[0]!='SUPPORTED'
 assert cert_release({**vic,'locator_verification':'MISSING'})[0]!='SUPPORTED'
 assert cert_release({**vic,'specific_event_type':'WRONG_VENDOR'})[0]!='SUPPORTED'
 assert cert_enforce({**vic,'C_contract_entitlement':'REPORTED_ONLY'})[0]!='SUPPORTED'
 assert cert_causal({**vic,'M_relevant_measurement':'NOT_ESTABLISHED'})[0]!='SUPPORTED'
 for r in read('R29_4Document_RetrospectiveSelection.csv'):assert r['source_id'] in {x['source_id'] for x in evidence}
 print(json.dumps({'status':'PASS','frozen_facts':len(evidence),'reproduced_claim_checks':len(result),'reproduced_exactly':True,'model': 'frozen deterministic rules; no independent human validation'},indent=2))
if __name__=='__main__':main()
