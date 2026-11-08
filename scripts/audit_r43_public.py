#!/usr/bin/env python3
"""Public-safe R43 provenance audit. Standard library only, NOT eligibility."""
import csv,json,collections,pathlib,re
BASE=pathlib.Path(__file__).resolve().parents[1]
WHITELIST={'DIRECT_TA_POSSIBLE','HOLD_DIRECTION_OR_UNIT','CONTEXT_ONLY','AI_USED_IN_PROCUREMENT_ONLY','OUTSIDE_SCOPE_TA','WRONG_TOPIC_RANDOM_CONTROL'}
def load(p):
    with pathlib.Path(p).open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def audit(root):
    root=pathlib.Path(root)
    old=load(root/'data/R41_220_provisional_decisions_PUBLICSAFE.csv')
    mid=load(root/'data/R42_B04_64_provisional_decisions_PUBLICSAFE.csv')
    new=load(root/'data/R43_B05_120_provisional_decisions_PUBLICSAFE.csv')
    stat=json.loads((root/'data/R43_progress_summary.json').read_text(encoding='utf-8'))
    assert (len(old),len(mid),len(new))==(220,64,120)
    assert len({r['record_id'] for r in old})==220
    assert len({r['cluster_id'] for r in mid})==64
    assert len({r['cluster_id'] for r in new})==120
    ids=[r['record_id'] for r in old]+[r['cluster_id'] for r in mid+new]
    assert len(set(ids))==404
    assert [int(r['r43_sequence']) for r in new]==list(range(1,121))
    assert all(re.fullmatch(r'BIB\d{5}',k) for k in ids)
    assert all(r['r43_provisional_label'] in WHITELIST and r['r43_direction'] for r in new)
    assert all(r['screening_mode']=='AI_ASSISTED_SINGLE_PASS' and r['final_review_inclusion']=='NOT_DETERMINED' and r['fulltext_eligibility']=='NOT_DETERMINED' for r in new)
    assert set(new[0])=={'cluster_id','r43_sequence','r43_provisional_label','r43_direction','screening_mode','fulltext_eligibility','final_review_inclusion'},'unexpected licensed metadata in public CSV'
    assert stat['record_universe']==2556 and stat['cumulative_AI_assisted_single_pass']==404 and stat['unread']==2152
    assert stat['previous_single_pass_covered']==284 and stat['new_AI_assisted_source_reads']==120
    assert stat['PRISMA_ScR']=='NOT_COMPLETED' and stat['independent_human_screen']=='NOT_PERFORMED' and stat['new_final_included']=='NOT_DETERMINED'
    assert dict(sorted(collections.Counter(r['r43_provisional_label'] for r in new).items()))==stat['new_provisional_labels']
    sources=load(root/'data/R43_Original_Source_Verification_PublicSafe.csv')
    assert len(sources)==7 and len({r['record_id'] for r in sources})==7
    assert all(r['public_url'].startswith('https://') and r['final_study_decision']=='NOT_DETERMINED' for r in sources)
    return {'status':'PASS','prior':284,'new':120,'cumulative':404,'unread':2152,'source_url_checks':7,'final_studies':'NOT_DETERMINED','human_R2':'NOT_PERFORMED'}
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--root',default=str(BASE));print(json.dumps(audit(p.parse_args().root),indent=2))
