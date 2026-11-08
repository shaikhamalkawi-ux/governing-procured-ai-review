#!/usr/bin/env python3
"""Validate double-screening handoffs without making eligibility decisions.

Accepted inputs must be completed by distinct human reviewers. AI pre-screen labels
must never be passed as human judgments. This script reports matched votes,
disagreements and pending reviews; it never computes final PRISMA counts.
"""
import argparse
import collections
import csv
import json
from pathlib import Path

FIELDS = ('record_id', 'reviewer_id', 'reviewer_kind', 'decision', 'reason_code', 'evidence_level')
DECISIONS = {'INCLUDE_CANDIDATE', 'EXCLUDE_CANDIDATE', 'HOLD'}
REASONS = {'PCC_IN_SCOPE', 'NOT_PUBLIC_SECTOR', 'NOT_PROCURED_AI', 'AI_USED_IN_PROCUREMENT_ONLY',
           'NO_ACCOUNTABILITY_EVIDENCE', 'WRONG_PUBLICATION_UNIT', 'INSUFFICIENT_METADATA',
           'OTHER_DOCUMENTED'}
EVIDENCE = {'TITLE_ABSTRACT', 'FULL_TEXT'}


def analyze(rows, expected_ids=None):
    expected_ids = set(expected_ids) if expected_ids is not None else None
    grouped = collections.defaultdict(list)
    errors = []
    for index, item in enumerate(rows, start=2):
        missing = [field for field in FIELDS if not item.get(field, '').strip()]
        if missing:
            errors.append(f'row {index}: missing {missing}')
            continue
        record = item['record_id'].strip()
        if not record.startswith('BIB') or not record[3:].isdigit():
            errors.append(f'row {index}: invalid record_id')
        if expected_ids is not None and record not in expected_ids:
            errors.append(f'row {index}: record not in authorized record universe')
        if item['reviewer_kind'].strip() != 'HUMAN':
            errors.append(f'row {index}: reviewer_kind must be HUMAN (AI labels are not human votes)')
        if item['decision'].strip() not in DECISIONS:
            errors.append(f'row {index}: unknown decision')
        if item['reason_code'].strip() not in REASONS:
            errors.append(f'row {index}: unknown reason_code')
        if item['evidence_level'].strip() not in EVIDENCE:
            errors.append(f'row {index}: unknown evidence_level')
        grouped[record].append(item)
    state_counts = collections.Counter()
    for record, votes in grouped.items():
        reviewers = [r['reviewer_id'].strip() for r in votes]
        if len(votes) > 2 or len(reviewers) != len(set(reviewers)):
            errors.append(f'{record}: >2 votes or duplicate reviewer')
            continue
        if len(votes) == 1:
            state_counts['AWAITING_SECOND_INDEPENDENT_HUMAN'] += 1
            continue
        if votes[0]['evidence_level'] != votes[1]['evidence_level']:
            state_counts['DIFFERENT_EVIDENCE_LEVELS_RECONCILIATION_REQUIRED'] += 1
        elif votes[0]['decision'] != votes[1]['decision']:
            state_counts['DISAGREEMENT_RECONCILIATION_REQUIRED'] += 1
        else:
            state_counts['AGREED_PROVISIONAL_' + votes[0]['decision']] += 1
    if expected_ids is not None:
        state_counts['NOT_YET_SCREENED_IN_THIS_INPUT'] = len(expected_ids - set(grouped))
    return {
        'valid': not errors,
        'errors': errors,
        'records_with_votes': len(grouped),
        'states': dict(sorted(state_counts.items())),
        'final_study_inclusion': 'NOT_DETERMINED',
        'PRISMA_ScR': 'NOT_COMPLETED',
        'notice': 'Agreement at title/abstract stage is not final full-text eligibility.'
    }


def load_ids(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as f:
        records = list(csv.DictReader(f))
    if not records or 'record_id' not in records[0]:
        raise ValueError('Universe CSV needs record_id column')
    ids = [x['record_id'].strip() for x in records]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate IDs in universe')
    return ids


def main():
    p = argparse.ArgumentParser(description='Audit independently entered human votes; no eligibility conclusion')
    p.add_argument('--votes', required=True, help='PRIVATE human-vote CSV')
    p.add_argument('--universe', help='CSV of authorized record_id values')
    p.add_argument('--report', help='PRIVATE JSON report destination')
    a = p.parse_args()
    with Path(a.votes).open(encoding='utf-8-sig', newline='') as f:
        items = list(csv.DictReader(f))
    result = analyze(items, load_ids(a.universe) if a.universe else None)
    output = json.dumps(result, indent=2, ensure_ascii=False)
    if a.report:
        Path(a.report).write_text(output + '\n', encoding='utf-8')
    print(output)
    if not result['valid']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
