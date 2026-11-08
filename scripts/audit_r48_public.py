#!/usr/bin/env python3
"""Source identity and R48 public-release integrity. No eligibility judgments."""
import collections, csv, json, pathlib
BASE = pathlib.Path(__file__).resolve().parents[1]
STAGES = [
    ("R41_220_provisional_decisions_PUBLICSAFE.csv","record_id",220),
    ("R42_B04_64_provisional_decisions_PUBLICSAFE.csv","cluster_id",64),
    ("R43_B05_120_provisional_decisions_PUBLICSAFE.csv","cluster_id",120),
    ("R44_64_Provisional_RecallStress_PUBLICSAFE.csv","cluster_id",64),
    ("R45_112_Provisional_Routes_PUBLICSAFE.csv","cluster_id",112),
    ("R46_68_SourceReasons_PUBLICSAFE.csv","cluster_id",68),
    ("R47_124_CaseText_Triage_PUBLICSAFE.csv","cluster_id",124),
    ("R48_192_SourceTriage_PUBLICSAFE.csv","cluster_id",192),
]
STAGE_CATEGORIES = {
    "AI_USED_IN_PROCUREMENT_ONLY":2,"CONTEXT_ONLY":38,
    "DIRECT_TA_POSSIBLE":1,"HOLD_DIRECTION_OR_UNIT":4,"OUTSIDE_SCOPE_TA":147,
}
STRATA = {
    "PUBLIC_AI_PURCHASE_DIRECTION", "EXTERNAL_SUPPLIER_RELATION",
    "PUBLIC_BUYER_UNVERIFIED", "PUBLIC_AI_DEPLOYMENT",
    "UNRELIABLE_AI_LEXICAL_SIGNAL", "GENERAL_POLICY_AND_USE"
}
def load(path):
    with pathlib.Path(path).open(encoding="utf-8-sig", newline="") as h:
        return list(csv.DictReader(h))
def audit(root=BASE):
    root=pathlib.Path(root); dat=root/"data"
    stages=[]; cumulative=[]
    for name,col,expected in STAGES:
        rows=load(dat/name)
        assert len(rows)==expected,(name,len(rows),expected)
        assert all(r[col].startswith("BIB") and len(r[col])==8 and r[col][3:].isdigit() for r in rows)
        ids=[r[col] for r in rows]
        assert len(set(ids))==len(ids),name
        cumulative.extend(ids);stages.append(rows)
    assert len(set(cumulative))==len(cumulative)==964,'Stage overlap or missing records'
    new=stages[-1]
    expected_columns={'cluster_id','r48_sequence','r48_stratum','r48_preliminary_label','r48_reason_code','abstract_status','assessment_type','fulltext_status','final_inclusion'}
    assert set(new[0])==expected_columns,'Unexpected source-licensed field in public release'
    assert [int(x['r48_sequence']) for x in new]==list(range(1,193))
    assert all(x['assessment_type']=='TITLE_AND_ABSTRACT_BRIEF_AI_ASSISTED_PROVISIONAL' and x['final_inclusion']=='NOT_DETERMINED' and x['fulltext_status']=='NOT_REVIEWED_IN_THIS_BATCH' and x['r48_reason_code'] for x in new)
    dist=dict(collections.Counter(r['r48_preliminary_label'] for r in new))
    assert dist==STAGE_CATEGORIES,dist
    stratum_counts=collections.Counter(x['r48_stratum'] for x in new)
    assert set(stratum_counts)==STRATA and all(v==32 for v in stratum_counts.values())
    summary=json.loads((dat/'R48_progress_summary_PUBLICSAFE.json').read_text(encoding='utf-8'))
    assert summary['original_bibliographic_identity_groups']==2556
    assert summary['baseline_R46_individual_firstpass']==648 and summary['baseline_R47_additional_case_text']==124
    assert summary['R48_additional_source_excerpt_firstpass']==192 and summary['cumulative_provisional_firstpass']==964
    assert summary['pending_individual_firstpass']==1592 and 964+1592==2556
    assert summary['new_R48_labels']==STAGE_CATEGORIES
    assert summary['final_study_selection']=='NOT_DETERMINED' and summary['PRISMA_ScR_flow']=='NOT_COMPLETED'
    assert summary['fulltext_queue_from_R46']=='100_POTENTIAL_RETRIEVAL_NOT_FINAL'
    assert summary['new_fulltext_retrieval_candidate']=='BIB02569'
    assert summary['not_a_prevalence_estimate'] is True
    cards=load(dat/'R48_12_OriginalSource_EvidenceBoundary_PublicSafe.csv')
    assert len(cards)==12 and len({c['source_id'] for c in cards})==12
    assert collections.Counter(c['in_frozen_2556'] for c in cards)=={'YES':11,'NO':1}
    assert all(c['official_or_author_url'].startswith('https://') for c in cards)
    assert any(c['source_id']=='BIB02569' and c['source_access_tier']=='PRIMARY_PUBLISHED_FULL_HTML' for c in cards)
    hold=load(dat/'R48_Family_Holds_PublicSafe.csv')
    assert len(hold)==2 and all(r['status']=='HOLD_DO_NOT_MERGE' for r in hold)
    assert len({r['family_id'] for r in hold})==2
    return {'result':'PASS','bibliographic_groups':2556,'screened_provisionally':964,'awaiting_individual_reading':1592,'R48_delta':192,'source_claim_cards':12,'family_holds':2,'fulltext_candidates_inherited':100,'new_extra_candidate':'BIB02569','eligibility':'NOT_DETERMINED'}
if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument('--root',default=str(BASE))
    print(json.dumps(audit(p.parse_args().root),ensure_ascii=False,indent=2))
