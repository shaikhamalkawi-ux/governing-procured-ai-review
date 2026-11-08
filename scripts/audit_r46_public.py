#!/usr/bin/env python3
"""Non-final public-file integrity audit for R46. No licensed input or scoring claims."""
from collections import Counter
from pathlib import Path
import csv, json, re
ROOT = Path(__file__).resolve().parents[1]

def read(path):
    with Path(path).open('r',encoding='utf-8-sig',newline='') as h:
        return list(csv.DictReader(h))

def audit(root=ROOT):
    root=Path(root); d=root/'data'
    historical=[
        (read(d/'R41_220_provisional_decisions_PUBLICSAFE.csv'),'record_id',220),
        (read(d/'R42_B04_64_provisional_decisions_PUBLICSAFE.csv'),'cluster_id',64),
        (read(d/'R43_B05_120_provisional_decisions_PUBLICSAFE.csv'),'cluster_id',120),
        (read(d/'R44_64_Provisional_RecallStress_PUBLICSAFE.csv'),'cluster_id',64),
        (read(d/'R45_112_Provisional_Routes_PUBLICSAFE.csv'),'cluster_id',112),
    ]
    ids=[]
    for r,key,n in historical:
        assert len(r)==n,(key,len(r))
        ids.extend(x[key] for x in r)
    assert len(ids)==len(set(ids))==580
    machine=read(d/'R46_All1976_IDOnly_MachineRoutes_PUBLICSAFE.csv')
    case=read(d/'R46_68_SourceReasons_PUBLICSAFE.csv')
    queue=read(d/'R46_100_RetrievalPriority_IDonly_PUBLICSAFE.csv')
    source4=read(d/'R46_4_OriginalSource_Verification_PUBLICSAFE.csv')
    source8=read(d/'R46_8_FurtherPublisherBoundaries_PUBLICSAFE.csv')
    families=read(d/'R46_Seven_Exact_TextIdentity_IDonly_PUBLICSAFE.csv')
    status=json.loads((d/'R46_ProgressSummary_PublicSafe.json').read_text(encoding='utf-8'))
    mid=[x['cluster_id'] for x in machine]
    caseids=[x['cluster_id'] for x in case]
    assert len(mid)==len(set(mid))==1976
    assert len(caseids)==len(set(caseids))==68
    assert not set(ids).intersection(mid)
    assert set(caseids).issubset(set(mid))
    assert len(ids)+len(mid)==2556
    assert [int(x['sequence']) for x in case]==list(range(1,69))
    assert all(re.fullmatch(r'BIB\d{5}',id) for id in ids+mid)
    forbidden={'title','abstract','doi','source_title','source_abstract','license_fulltext','title_private','abstract_private'}
    for r in [machine,case,queue]:
        assert not {x.lower() for x in r[0]}.intersection(forbidden),'Provider metadata leaked as CSV field'
    assert all(x['review_stage']=='DETERMINISTIC_MACHINE_TEXT_ROUTING_NOT_INDIVIDUAL_SOURCE_READING' and x['final_eligibility']=='NOT_DETERMINED' for x in machine)
    assert all(x['review_stage']=='AI_ASSISTED_CASE_BY_CASE_TITLE_ABSTRACT_NOT_FINAL' and x['final_inclusion']=='NOT_DETERMINED' and x['R46_specific_source_reason'].strip() for x in case)
    assert dict(sorted(Counter(x['R46_provisional_label'] for x in case).items()))==status['new_R46_case_label_counts']
    assert all(x['final_inclusion']=='NOT_DETERMINED' for x in queue)
    assert len(queue)==len(set(x['cluster_id'] for x in queue))==100
    assert len(source4)==4 and len(source8)==8
    assert len(set(x['cluster_id'] for x in source4+source8))==12
    assert all(x['full_text_eligibility']=='NOT_DETERMINED' for x in source4) and all(x['final_eligibility']=='NOT_DETERMINED' for x in source8)
    assert len(families)==7 and sum(int(x['source_record_count']) for x in families)==17
    assert all(x['identity_action']=='HOLD_PUBLISHER_VERSION_OR_PROCEEDINGS_CHECK' for x in families)
    assert (status['original_provisional_bibliographic_identities'],status['cumulative_individually_reasoned_firstpass'],status['remaining_without_individual_source_review'],status['all_previous_1976_machine_text_routed'],status['fulltext_retrieval_leads'])==(2556,648,1908,1976,100)
    assert status['R45_AI_assisted_individual_firstpass']==580 and status['R46_new_AI_assisted_case_reads']==68
    assert status['R46_original_source_checks_total']==12 and status['R46_secondary_abstract_only_checks_total']==1
    assert status['final_study_inclusions']=='NOT_DETERMINED' and status['final_study_exclusions']=='NOT_DETERMINED' and status['PRISMA_ScR']=='NOT_COMPLETED'
    return {'status':'PASS','record_universe':2556,'previous_case_reads':580,'new_case_reads':68,'cumulative_case_reads':648,'machine_parsed':1976,'individual_unread':1908,'fulltext_retrieval_leads':100,'source_cards':12,'identity_groups_held':7,'final_eligibility':'NOT_DETERMINED'}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--root',default=str(ROOT));print(json.dumps(audit(p.parse_args().root),indent=2))
