#!/usr/bin/env python3
"""Make a full-text retrieval queue from a PRIVATE 99aI status CSV.

This utility does not decide inclusion, does not redistribute source metadata,
and does not use titles/abstracts for automated exclusion. The caller controls
where the PRIVATE output is stored. It is deliberately not called by CI.
"""
from __future__ import annotations
import argparse,csv,collections,hashlib,json,pathlib,sys
CATEGORIES={'DIRECT_TA_POSSIBLE':1,'HOLD_DIRECTION_OR_UNIT':2}
FIELD=['review_priority','cluster_id','provisional_label','title','doi','year','source_url','database_flags','fulltext_eligibility','independent_human_review','publication_family_check','source_licence']

def read_table(path):
    with pathlib.Path(path).open('r',encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def make_queue(records):
    result=[]
    seen=set()
    for x in records:
        label=x.get('R41_TA_label','')
        if label not in CATEGORIES:continue
        ident=x.get('cluster_id')
        if not ident or ident in seen:raise ValueError('missing or duplicate ID in candidate queue: '+str(ident))
        seen.add(ident)
        result.append({'review_priority':str(CATEGORIES[label]),'cluster_id':ident,'provisional_label':label,
                       'title':x.get('title',''),'doi':x.get('doi',''),'year':x.get('year',''),
                       'source_url':x.get('source_url',''),'database_flags':x.get('database_flags',''),
                       'fulltext_eligibility':'NOT_DETERMINED','independent_human_review':'NOT_PERFORMED',
                       'publication_family_check':'PENDING','source_licence':'PRIVATE_DATABASE_METADATA'})
    return sorted(result,key=lambda x:(int(x['review_priority']),x['cluster_id']))

def main():
    p=argparse.ArgumentParser(description='Private fulltext retrieval queue: no eligibility screening')
    p.add_argument('--input-private',required=True)
    p.add_argument('--output-private',required=True)
    a=p.parse_args()
    records=read_table(a.input_private)
    queue=make_queue(records)
    out=pathlib.Path(a.output_private)
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,FIELD);w.writeheader();w.writerows(queue)
    print(json.dumps({'status':'QUEUED_NOT_ELIGIBILITY','records':len(queue),'by_provisional_label':dict(collections.Counter(x['provisional_label'] for x in queue)),'private_output':str(out)},indent=2))
if __name__=='__main__':main()
