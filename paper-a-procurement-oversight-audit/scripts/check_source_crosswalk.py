#!/usr/bin/env python3
"""Check publicly deposited 33-row source-role crosswalk against frozen derived R76 cohorts.
This is a structural/source-addendum consistency test, not independent human coding or government-source fact validation.
Python 3.10+; standard library only. Run from any working directory after a full clone.
"""
from __future__ import annotations
import collections, csv, hashlib, json
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
DATA = HERE / 'data'

def read(filename):
    with (DATA / filename).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def main():
    cross = read('source_to_role_crosswalk_33.csv')
    local = {r['record_id']:r for r in read('local_authority_13_derived_R76.csv')}
    ministerial = {r['record_id']:r for r in read('ministerial_20_derived_R76.csv')}
    assert len(cross)==33 and len(local)==13 and len(ministerial)==20
    assert len({r['id'] for r in cross}) == 33
    assert {r['id'] for r in cross} == set(local)|set(ministerial)
    n_author_review=0
    for r in cross:
        assert r['original_R76_pdf_page'].isdigit()
        assert r['source_classification_agreement']=='PASS'
        assert r['official_source_url'].startswith('https://www.gov.uk/algorithmic-transparency-records/')
        if r['id'] in local:
            s=local[r['id']]
            assert r['A_frozen_role_code']==s['source_scope_reconstructed']==r['B_source_read_role']
            assert r['A_third_party_field']==s['third_party_declared']
            assert r['A_technology_code']=='NOT_CODED_IN_LOCAL_COHORT'
        else:
            s=ministerial[r['id']]
            assert r['A_frozen_role_code']==s['supplier_relationship_reconstructed']==r['B_source_read_role']
            assert r['A_technology_code']==s['technology_source_code']==r['B_technology_code']
            assert r['A_third_party_field']==s['third_party_declared']
        if r['latest_direct_official_page_check']=='NOT_RECHECKED_LIVE_IN_G9': n_author_review+=1
    print(json.dumps({'status':'PASS','source_rows_33':33,'local_13':13,'ministerial_20':20,
       'all_record_IDs_and_roles_match_frozen_public_dataset':True,'not_live_rechecked_count':n_author_review,
       'original_R65_R66_R75_machine_ledgers_not_recovered':True,
       'claim_limit':'INTERNAL CONSISTENCY only; no independent human recoding, contract authentication or national inference'},indent=2))
    return 0
if __name__=='__main__':
    try: raise SystemExit(main())
    except Exception as exc:
        print('FAIL:',repr(exc));raise SystemExit(1)
