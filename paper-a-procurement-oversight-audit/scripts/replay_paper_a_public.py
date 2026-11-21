#!/usr/bin/env python3
"""Replay locked source-description counts for 99aiA Paper A (public-safe).
No packages beyond Python's standard library. No new scientific coding.
Run from any working directory after cloning the complete repository.
"""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import csv, hashlib, json, sys
HERE = Path(__file__).resolve().parent.parent
ROOT = HERE.parent
DATA = HERE / "data"

def read_csv(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def check(condition, message):
    if not condition: raise AssertionError(message)

def main():
    local = read_csv("local_authority_13_derived_R76.csv")
    ministerial = read_csv("ministerial_20_derived_R76.csv")
    with (ROOT / "data" / "documentary" / "R29_28Event_CXSM_A_SourceLedger.csv").open(encoding="utf-8-sig", newline="") as f:
        historical = list(csv.DictReader(f))
    check(len(local) == 13, "Local cohort is not 13")
    check(len(ministerial) == 20, "Ministerial cohort is not 20")
    check(len(historical) == 28, "Historical descriptions are not 28")
    check(len(set(r["record_id"] for r in local)) == 13, "Duplicate local IDs")
    check(len(set(r["record_id"] for r in ministerial)) == 20, "Duplicate ministerial IDs")
    check(len(set(r["case_id"] for r in historical)) == 9, "Historical programmes are not 9")
    for r in local + ministerial:
        check(r["official_url"].startswith("https://www.gov.uk/algorithmic-transparency-records/"), "Invalid official locator")
    local_values = {
        "outside_yes": sum(r["third_party_declared"] == "Yes" for r in local),
        "procurement_connected": sum(r["broad_procurement_connected"] == "1" for r in local),
        "direct_commercial_AI_desc": sum(r["direct_commercial_AI_use"] == "1" for r in local)
    }
    check(local_values == {"outside_yes":12,"procurement_connected":7,"direct_commercial_AI_desc":2}, "Local source-role totals drift")
    ministerial_values = {
        "outside_yes": sum(r["third_party_declared"] == "Yes" for r in ministerial),
        "outside_no": sum(r["third_party_declared"] == "No" for r in ministerial),
        "tech":dict(Counter(r["technology_source_code"] for r in ministerial)),
        "AI_no_outside_supplier":sum(r["third_party_declared"] == "No" and r["technology_source_code"] == "AI_CONFIRMED" for r in ministerial),
        "supplier_roles":dict(Counter(r["supplier_relationship_reconstructed"] for r in ministerial))
    }
    check(ministerial_values["outside_yes"] == 14 and ministerial_values["outside_no"] == 6, "Outside flags drift")
    check(ministerial_values["tech"] == {"AI_CONFIRMED":13, "EXPLICIT_NO_AI_ML":3,"TECH_SCOPE_HOLD":4}, "Technology-code totals drift")
    check(ministerial_values["AI_no_outside_supplier"] == 5, "No-outside AI count drift")
    check(ministerial_values["supplier_roles"] == {"COMMISSIONED_CUSTOM_DEVELOPMENT":10,"NO_THIRD_PARTY_DECLARED":6,"DIRECT_TOOL_ACCESS_DECLARED":2,"IN_HOUSE_TOOL_WITH_EXTERNAL_COMPONENTS":1,"DIRECT_SUPPLIER_AI_COMPONENT_DECLARED":1}, "Supplier role counts drift")
    CATEGORIES = ("DOCUMENTED", "REPORTED_ONLY", "NOT_ESTABLISHED", "NOT_APPLICABLE")
    fields = ["C_contract_entitlement", "X_exercised_oversight", "S_supplier_action", "M_relevant_measurement", "A_causal_attribution"]
    expected = [[3,4,7,14],[7,7,1,13],[3,1,8,16],[2,5,9,12],[0,0,15,13]]
    historical_values = {}
    for field,values in zip(fields,expected):
        v = [sum(r[field] == category for r in historical) for category in CATEGORIES]
        check(v == values, f"Historical counts drift for {field}: {v}")
        historical_values[field] = dict(zip(CATEGORIES,v))
    noncontractual = [r for r in historical if r["cross_link_X_to_S"].startswith("DOCUMENTED_NONCONTRACTUAL_") or r["cross_link_X_to_S"].startswith("DOCUMENTED_STATUTORY_")]
    check(len(noncontractual)==2, "Two recorded noncontractual response links not found")
    check(all(r["A_causal_attribution"] != "DOCUMENTED" for r in historical), "Unexpected causal documented claim")
    with (DATA / "omilia_selected_six_payments.csv").open(encoding="utf-8", newline="") as f: payments = list(csv.DictReader(f))
    with (DATA / "ontario_reported_two_site_differences.csv").open(encoding="utf-8", newline="") as f: sites = list(csv.DictReader(f))
    check(len(payments)==6 and [float(r["amount_GBP"]) for r in payments] == [236660.0,236660.0,236660.0,216742.5,144495.0,72248.0], "Selected payment points drift")
    check(len(sites)==2 and [(r["site"],float(r["reported_mean_documentation_time_difference_minutes"])) for r in sites]==[("SMDHU",-12.9),("WDGPH",10.3)], "Ontario points drift")
    manifest = DATA / "SHA256SUMS.txt"
    pairs = [line.split(None,1) for line in manifest.read_text(encoding="ascii").splitlines() if line.strip()]
    for sha,filename in pairs:
        file = DATA / filename.strip().lstrip("*")
        check(file.is_file(),"Missing pinned file: "+str(file))
        check(hashlib.sha256(file.read_bytes()).hexdigest()==sha,"SHA256 mismatch: "+filename)
    out={"status":"PASS", "scientific_analyses_rerun":False, "rechecked_structural_claims_only":True, "local_13":local_values, "ministerial_20":ministerial_values, "historical_28":historical_values, "historical_programmes":9, "noncontractual_X_to_S":2,"documented_contract_remedy_causal_benefit_chain":0,"selected_payment_entries":6,"reported_ontario_site_differences":[-12.9,10.3],"sha256_files_verified":len(pairs),"no_independent_human_coding":True}
    print(json.dumps(out,sort_keys=True,indent=2))
    return 0

if __name__ == "__main__":
    try:sys.exit(main())
    except Exception as e:
        print("FAIL: "+str(e),file=sys.stderr)
        sys.exit(1)
