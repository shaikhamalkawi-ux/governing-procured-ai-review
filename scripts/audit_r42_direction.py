#!/usr/bin/env python3
"""Validate 99aI R42 public-safe, non-final screening checkpoint (standard library)."""
import csv,json,collections,pathlib
ALLOWED={'DIRECT_TA_POSSIBLE','HOLD_DIRECTION_OR_UNIT','CONTEXT_ONLY','AI_USED_IN_PROCUREMENT_ONLY','OUTSIDE_SCOPE_TA','WRONG_TOPIC_RANDOM_CONTROL'}
def _rows(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def audit(base):
    base=pathlib.Path(base)
    prev=_rows(base/'data/R41_220_provisional_decisions_PUBLICSAFE.csv')
    delta=_rows(base/'data/R42_B04_64_provisional_decisions_PUBLICSAFE.csv')
    report=json.loads((base/'data/R42_progress_summary.json').read_text(encoding='utf-8'))
    assert len(prev)==220 and len(delta)==64
    prev_ids={r['record_id'] for r in prev}
    ids={r['cluster_id'] for r in delta}
    assert len(prev_ids)==220 and len(ids)==64 and not ids.intersection(prev_ids)
    assert [int(r['r42_sequence']) for r in delta]==list(range(1,65))
    assert all(r['cluster_id'].startswith('BIB') and r['r42_provisional_label'] in ALLOWED for r in delta)
    assert all(r['screening_mode']=='AI_ASSISTED_SINGLE_PASS' and r['final_review_inclusion']=='NOT_DETERMINED' and r['fulltext_eligibility']=='NOT_DETERMINED' for r in delta)
    counts=dict(sorted(collections.Counter(r['r42_provisional_label'] for r in delta).items()))
    assert counts==report['new_labels']
    assert report['source_universe_identity_groups']==2556
    assert report['inherited_AI_assisted_first_pass']==220
    assert report['new_AI_assisted_first_pass']==64
    assert report['cumulative_AI_assisted_first_pass']==284
    assert report['unread']==2272 and 284+2272==2556
    assert report['PRISMA_STATUS']=='NOT_FINAL' and report['final_included_studies']=='NOT_DETERMINED'
    assert report['independent_human_screen']=='NOT_PERFORMED' and report['fulltext_eligibility']=='NOT_DETERMINED'
    assert all(r['r42_direction'] for r in delta)
    return {'status':'PASS','stage':'R42_B04','new':64,'first_pass':284,'remaining':2272,'labels':counts,'scientific_status':'PROVISIONAL_ONLY'}
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--root',default=str(pathlib.Path(__file__).resolve().parents[1]))
    print(json.dumps(audit(p.parse_args().root),indent=2))
