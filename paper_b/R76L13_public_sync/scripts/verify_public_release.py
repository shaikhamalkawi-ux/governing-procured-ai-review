#!/usr/bin/env python3
"""Arithmetic, lineage and file-integrity checks for Paper B R76L13 public-safe files.

This does NOT validate original papers, original contract terms, the completion of
systematic review screening, the real-world performance of AI systems, or a
causal effect. It is a deterministic package check only.
"""
import csv
import hashlib
import json
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ROLE_COUNTS = {
    'official / public administrative evidence': 34,
    'observed / empirical research': 25,
    'legal / doctrinal': 16,
    'standard / methods': 9,
    'review / methodology': 6,
    'other scholarship / sector evidence': 3,
}
EXPECTED_FIGURES = [
    'Figure1_Auditor_Evidence_Chain.pdf',
    'Figure2_State_AI_Contract_Clauses.pdf',
    'Figure3_OECD_National_Indicators.pdf',
    'Figure4_GOV_Voice_Weights.pdf',
    'SupplementaryFigureS1_Source_Roles.pdf',
]


def read_csv(filename):
    with (ROOT/'data'/filename).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))


def sha256(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()


def validate():
    ids=read_csv('source_identity_register_93.csv')
    assert len(ids)==93, f'Expected 93 cited identities, found {len(ids)}'
    assert [r['id'] for r in ids]==[f'R{i:02d}' for i in range(1,94)], 'Not contiguous R01-R93'
    assert all(r['cited_in_main']=='YES' for r in ids), 'A bibliography item is not marked cited'
    counts=Counter(r['classification_for_inference'] for r in ids)
    assert dict(counts)==EXPECTED_ROLE_COUNTS, f'Source roles changed: {counts}'
    assert sum(counts.values())==93

    led=read_csv('source_selection_ledger_93.csv')
    assert len(led)==93
    assert [r['ref_id'] for r in led]==[r['id'] for r in ids]
    assert all(r['not_a_systematic_inclusion']=='YES' for r in led)
    recent=read_csv('literature_update_2021_2026_9_sources.csv')
    assert len(recent)==9
    assert {r['id'] for r in recent}=={f'R{i:02d}' for i in range(85,94)}
    search=read_csv('targeted_search_log_20261121.csv')
    assert len(search)==10
    assert {r['execution_date'] for r in search}=={'2026-11-21'}

    data=json.loads((ROOT/'data'/'figure_data_manifest.json').read_text())
    core=data['counts']
    assert core['total']==93
    assert core['source_roles']==[34,25,16,9,6,3]
    assert core['oecd']=={'n':36,'support':21,'audit':11,'impact':10}
    assert core['state_contracts']==215
    assert core['state_provisions']==3771
    assert core['clause_proportions']==[77.0,5.3,3.0,2.4]
    assert core['govvoice_quality']==70 and core['govvoice_commercial']==30
    assert core['govvoice_quality_subweights']==[60,30,10]
    assert [70*n//100 for n in [60,30,10]]+[30]==[42,21,7,30]
    assert core['govvoice_derived']==[42,21,7,30]
    assert sum(core['govvoice_derived'])==100
    for n,expected in ((21,'58.3'),(11,'30.6'),(10,'27.8')):
        reported=(Decimal(100*n)/Decimal(36)).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP)
        assert str(reported)==expected

    for f in EXPECTED_FIGURES:
        target=ROOT/'figures'/f
        assert target.is_file() and target.stat().st_size>2000, f'Missing PDF figure {f}'
        assert target.read_bytes()[:5]==b'%PDF-'
    manifest=ROOT/'RELEASE_SHA256SUMS.txt'
    checksum_rows=[]
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'): continue
        digest,relative=line.split('  ',1)
        assert sha256(ROOT/relative)==digest, f'Hash mismatch: {relative}'
        checksum_rows.append(relative)
    expected_files={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p.name != 'RELEASE_SHA256SUMS.txt' and '__pycache__' not in p.parts and 'rebuild_figures' not in p.parts and p.suffix != '.pyc'}
    assert set(checksum_rows)==expected_files, (len(checksum_rows),len(expected_files),sorted(expected_files-set(checksum_rows)))
    print('PASS: 93 sources, six roles, 9 new sources, 10 logged searches,')
    print('five inherited figures, source percentages, GOV Voice arithmetic,')
    print(f'and {len(checksum_rows)} public release file hashes.')
    print('LIMIT: Arithmetic and file integrity are not scientific source validation.')


if __name__=='__main__':
    validate()
