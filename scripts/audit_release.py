#!/usr/bin/env python3
"""Portable checks on the public-safe 99aI research checkpoint.

No external packages and no institutional database records are needed.
This does not make PRISMA decisions or validate source-level evidence.
"""
import argparse,csv,json,collections,pathlib,sys,hashlib

ALLOWED={'DIRECT_TA_POSSIBLE','HOLD_DIRECTION_OR_UNIT','CONTEXT_ONLY','AI_USED_IN_PROCUREMENT_ONLY','OUTSIDE_SCOPE_TA','WRONG_TOPIC_RANDOM_CONTROL'}

def rows(path):
    with open(path,'r',encoding='utf-8-sig',newline='') as stream:
        return list(csv.DictReader(stream))

def audit(base):
    base=pathlib.Path(base)
    s=json.loads((base/'data/R41_progress_summary.json').read_text(encoding='utf-8'))
    read=rows(base/'data/R41_220_provisional_decisions_PUBLICSAFE.csv')
    chart=rows(base/'data/R40_14_sources_evidence_chart_PUBLICSAFE.csv')
    assert s['provisional_bibliographic_identities']==2556
    assert s['AI_assisted_first_pass_read']==len(read)==220
    assert s['unread']==2336
    assert s['AI_assisted_first_pass_read']+s['unread']==s['provisional_bibliographic_identities']
    assert len({x['record_id'] for x in read})==len(read)
    assert all(x['record_id'].startswith('BIB') for x in read)
    assert all(x['provisional_label'] in ALLOWED for x in read)
    assert all(x['screening_mode']=='AI_ASSISTED_SINGLE_PASS' and x['final_inclusion']=='NOT_DETERMINED' for x in read)
    counts=dict(sorted(collections.Counter(x['provisional_label'] for x in read).items()))
    assert counts==s['read_provisional_label_counts'],(counts,s['read_provisional_label_counts'])
    assert len(chart)==s['public_evidence_chart_source_count']==14
    assert len({x['source_id'] for x in chart})==len(chart)
    assert s['PRISMA_ScR']=='NOT_COMPLETED'
    assert s['independent_human_title_abstract_screen']=='NOT_PERFORMED'
    assert s['full_text_final_inclusion']=='NOT_DETERMINED'
    return {'status':'PASS','reviewed':len(read),'unread':s['unread'],'evidence_chart_sources':len(chart),'labels':counts,'scientific_status':'PRELIMINARY_ONLY'}

def main():
    p=argparse.ArgumentParser(description='Audit public-safe screening checkpoint, not eligibility')
    p.add_argument('--root',default=str(pathlib.Path(__file__).resolve().parents[1]))
    a=p.parse_args()
    try: print(json.dumps(audit(a.root),indent=2))
    except Exception as ex:
        print('Audit FAIL: %s'%ex,file=sys.stderr);raise SystemExit(1)

if __name__=='__main__':main()
