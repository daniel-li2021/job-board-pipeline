"""Import curated companies and enrich profiles/pending from local USCIS, DOL, SEC files.

Run offline: python3 scripts/enrich_company_profiles.py --findings path/to/clean.json
    --data-dir path/to/downloads --apply
Without --apply, print counts only. Raw datasets are never copied into the repo.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import zipfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from sources.company_pending import SCREENING_FIELDS, company_key, pending_entry  # noqa: E402
from sources.schema import normalize_company_key  # noqa: E402
from state_io import atomic_write  # noqa: E402

KEEP_TAGS = {
    "staffing", "defense", "clearance_heavy", "tech_service",
    "cybersecurity", "government", "government_contracting", "clearance_risk",
}
SIZES = {"unknown", "<50", "50-200", "200-1k", "1k-5k", "5k-20k", "20k+"}
MATURITIES = {"unknown", "early_startup", "growth", "established"}
SPONSORS = {"unknown", "likely", "unlikely"}
TYPES = {"unknown", "tech", "industrial", "healthcare", "finance", "consulting", "retail", "government", "other"}
MAIN_NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
LCA_FILES = (
    ("LCA_Disclosure_Data_FY2024_Q4.xlsx", 2024),
    ("LCA_Disclosure_Data_FY2025_Q4.xlsx", 2025),
    ("LCA_Disclosure_Data_FY2026_Q3.xlsx", 2026),
)


def names_index(entries: list[dict]) -> dict[str, set[str]]:
    index: dict[str, set[str]] = defaultdict(set)
    for entry in entries:
        for name in [entry["name"], *entry.get("aliases", [])]:
            exact, legal = normalize_company_key(name), company_key(name)
            if exact:
                index[exact].add(entry["name"])
            # ponytail: short stripped keys collide easily; use only full exact names there.
            if len(legal) >= 4:
                index[legal].add(entry["name"])
    return index


def resolve(name: str, index: dict[str, set[str]]) -> set[str]:
    exact = index.get(normalize_company_key(name), set())
    return exact or (index.get(company_key(name), set()) if len(company_key(name)) >= 4 else set())


def review_item(review: list[dict], name: str, field: str, existing: str, candidate: str, reason: str) -> None:
    review.append({"name": name, "field": field, "existing": existing, "candidate": candidate, "reason": reason})


def validate_findings(payload: dict) -> list[dict]:
    entries = payload.get("companies")
    stated_count = payload.get("count", payload.get("canonical_profile_count"))
    if not isinstance(entries, list) or stated_count != len(entries):
        raise ValueError("findings companies/count mismatch")
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict) or not str(entry.get("name") or "").strip():
            raise ValueError("finding missing company name")
        key = normalize_company_key(entry["name"])
        if key in seen:
            raise ValueError(f"duplicate finding: {entry['name']}")
        seen.add(key)
        if not isinstance(entry.get("aliases"), list) or not isinstance(entry.get("tags"), list):
            raise ValueError(f"bad aliases/tags: {entry['name']}")
        for field, allowed in (("size", SIZES), ("maturity", MATURITIES), ("sponsor", SPONSORS), ("type", TYPES)):
            if entry.get(field) not in allowed:
                raise ValueError(f"invalid {field}: {entry['name']}")
    return entries


def import_findings(profiles: list[dict], findings: list[dict], review: list[dict]) -> Counter:
    counts = Counter()
    by_name = {entry["name"]: entry for entry in profiles}
    for incoming in findings:
        name = incoming["name"]
        matches = resolve(name, names_index(profiles))
        if not matches and len(company_key(name)) < 4:
            matches = {entry["name"] for entry in profiles if company_key(entry["name"]) == company_key(name)}
        if len(matches) > 1:
            review_item(review, name, "identity", "", ", ".join(sorted(matches)), "multiple existing profiles")
            counts["review_identity"] += 1
            continue
        if matches:
            target = by_name[next(iter(matches))]
            if company_key(target["name"]) != company_key(name):
                review_item(review, name, "identity", target["name"], name, "alias may denote a different legal entity")
                counts["review_identity"] += 1
                continue
            aliases = target.setdefault("aliases", [])
            for alias in [name, *incoming["aliases"]]:
                if alias != target["name"] and normalize_company_key(alias) not in {
                    normalize_company_key(value) for value in aliases
                }:
                    aliases.append(alias)
            for field in SCREENING_FIELDS:
                old, new = target.get(field, "unknown"), incoming[field]
                if old == "unknown" and new != "unknown":
                    target[field] = new
                elif new != "unknown" and old != new:
                    review_item(review, target["name"], field, old, new, "curated finding conflicts with existing profile")
            target["tags"] = sorted(set(target.get("tags", [])) | (set(incoming["tags"]) & KEEP_TAGS))
            counts["existing_matched"] += 1
        else:
            entry = {field: incoming[field] for field in ("name", "aliases", *SCREENING_FIELDS)}
            entry["tags"] = sorted(set(incoming["tags"]) & KEEP_TAGS)
            entry["priority"] = "normal"  # Existing ranking still consumes priority; do not infer it.
            entry["last_verified"] = incoming.get("last_verified") or date.today().isoformat()
            if incoming.get("notes"):
                entry["notes"] = incoming["notes"]
            profiles.append(entry)
            by_name[name] = entry
            counts["added"] += 1
    return counts


def load_pending(path: Path, profiles: list[dict]) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    entries = payload.get("companies")
    if not isinstance(entries, list):
        raise ValueError("pending companies must be a list")
    profile_index = names_index(profiles)
    pending: dict[str, dict] = {}
    for raw in entries:
        entry = pending_entry(raw)
        if not entry:
            raise ValueError("invalid pending company")
        if any(resolve(alias, profile_index) for alias in [entry["name"], *entry["aliases"]]):
            continue
        key = company_key(entry["name"])
        old = pending.get(key)
        if old:
            for field in SCREENING_FIELDS:
                if old[field] == "unknown":
                    old[field] = entry[field]
            old["seen_job_keys"] = sorted(set(old["seen_job_keys"] + entry["seen_job_keys"]))
            old["seen_count"] = max(1, len(old["seen_job_keys"]))
            old["aliases"] = sorted(set(old["aliases"] + entry["aliases"] + [entry["name"]]) - {old["name"]})
        else:
            pending[key] = entry
    return sorted(pending.values(), key=lambda entry: entry["name"].casefold())


def source_index(profiles: list[dict], pending: list[dict], review: list[dict]) -> dict[str, set[str]]:
    entries = [*profiles, *pending]
    index = names_index(entries)
    for key, matches in index.items():
        if len(matches) > 1:
            review_item(review, ", ".join(sorted(matches)), "identity", "", key, "ambiguous normalized name/alias")
    return index


def read_uscis(path: Path, index: dict[str, set[str]]) -> tuple[Counter, dict[str, Counter]]:
    approvals = Counter()
    industries: dict[str, Counter] = defaultdict(Counter)
    with path.open(encoding="utf-16", newline="") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            if row["Fiscal Year   "].strip() not in {"2025", "2026"}:
                continue
            names = resolve(row["Employer (Petitioner) Name"], index)
            if len(names) != 1:
                continue
            name = next(iter(names))
            approvals[name] += sum(int((row.get(column) or "0").replace(",", "")) for column in (
                "New Employment Approval", "Continuation Approval",
                "Change with Same Employer Approval", "New Concurrent Approval",
                "Change of Employer Approval", "Amended Approval",
            ))
            category = row["Industry (NAICS) Code"].split(" - ", 1)[0].strip()
            if category:
                industries[name][category] += 1
    return approvals, industries


def lca_shared_strings(archive: zipfile.ZipFile, index: dict[str, set[str]]) -> tuple[dict[int, str], set[int], set[int], dict[int, str]]:
    employers: dict[int, str] = {}
    certified, h1b = set(), set()
    headers: dict[int, str] = {}
    with archive.open("xl/sharedStrings.xml") as stream:
        parser = ElementTree.iterparse(stream, events=("start", "end"))
        root = next(parser)[1]
        number = 0
        for event, elem in parser:
            if event != "end" or elem.tag != MAIN_NS + "si":
                continue
            value = "".join(node.text or "" for node in elem.iter(MAIN_NS + "t")).strip()
            if number < 120:
                headers[number] = value
            if value.casefold() == "certified":
                certified.add(number)
            elif value.upper() == "H-1B":
                h1b.add(number)
            match = resolve(value, index)
            if len(match) == 1:
                employers[number] = next(iter(match))
            number += 1
            elem.clear()
            if number % 1000 == 0:
                root.clear()
    return employers, certified, h1b, headers


def read_lca(path: Path, index: dict[str, set[str]]) -> Counter:
    counts = Counter()
    with zipfile.ZipFile(path) as archive:
        employers, certified, h1b, strings = lca_shared_strings(archive, index)
        with archive.open("xl/worksheets/sheet1.xml") as stream:
            parser = ElementTree.iterparse(stream, events=("start", "end"))
            root = next(parser)[1]
            sheet_data = None
            columns = {}
            for event, elem in parser:
                if event == "start" and elem.tag == MAIN_NS + "sheetData":
                    sheet_data = elem
                if event != "end" or elem.tag != MAIN_NS + "row":
                    continue
                values = {}
                for cell in elem:
                    ref = cell.get("r", "")
                    if len(ref) < 2 or ref[0] not in "BFT" or not ref[1].isdigit():
                        continue
                    value = cell.find(MAIN_NS + "v")
                    if value is not None and value.text is not None:
                        values[ref[0]] = int(value.text) if cell.get("t") == "s" else value.text
                if elem.get("r") == "1":
                    columns = {strings.get(value): col for col, value in values.items()}
                    if not {"CASE_STATUS", "VISA_CLASS", "EMPLOYER_NAME"} <= columns.keys():
                        raise ValueError(f"unexpected LCA header: {path}")
                elif (values.get(columns["CASE_STATUS"]) in certified
                      and values.get(columns["VISA_CLASS"]) in h1b):
                    company = employers.get(values.get(columns["EMPLOYER_NAME"]))
                    if company:
                        counts[company] += 1
                row_number = int(elem.get("r", "0"))
                elem.clear()
                if sheet_data is not None and row_number % 1000 == 0:
                    sheet_data.clear()
                    root.clear()
    return counts


def read_sec(path: Path, index: dict[str, set[str]], review: list[dict]) -> set[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    ciks: dict[str, set[int]] = defaultdict(set)
    for row in payload.values():
        names = resolve(str(row.get("title") or ""), index)
        if len(names) == 1:
            ciks[next(iter(names))].add(int(row["cik_str"]))
    matched = set()
    for name, ids in ciks.items():
        if len(ids) == 1:
            matched.add(name)
        else:
            review_item(review, name, "maturity", "unknown", "established", "SEC name maps to multiple CIKs")
    return matched


def apply_evidence(profiles: list[dict], pending: list[dict], approvals: Counter,
                   industries: dict[str, Counter], lca: dict[int, Counter],
                   public: set[str], review: list[dict]) -> Counter:
    counts = Counter()
    for entry in [*profiles, *pending]:
        name = entry["name"]
        recent = lca[2025][name] + lca[2026][name]
        strong = approvals[name] >= 3 or recent >= 3 or (approvals[name] >= 1 and recent >= 2)
        if strong:
            if entry["sponsor"] == "unknown":
                entry["sponsor"] = "likely"
                counts["sponsor_likely"] += 1
            elif entry["sponsor"] == "unlikely":
                review_item(review, name, "sponsor", "unlikely", "likely", f"recent USCIS approvals={approvals[name]}, certified LCAs={recent}")
        elif entry["sponsor"] == "unknown" and lca[2024][name] >= 3:
            review_item(review, name, "sponsor", "unknown", "likely", "2024-only LCA history is not recent evidence")
        if name in public:
            if entry["maturity"] == "unknown":
                entry["maturity"] = "established"
                counts["maturity_established"] += 1
            elif entry["maturity"] != "established":
                review_item(review, name, "maturity", entry["maturity"], "established", "exact SEC company-title match")
        industry = industries.get(name, Counter())
        if sum(industry.values()) >= 2:
            category = industry.most_common(1)[0][0]
            mapped = {
                "31-33": "industrial", "44-45": "retail", "52": "finance", "62": "healthcare",
            }.get(category)
            if mapped and len(industry) == 1:
                if entry["type"] == "unknown":
                    entry["type"] = mapped
                    counts["type_filled"] += 1
                elif entry["type"] != mapped:
                    review_item(review, name, "type", entry["type"], mapped, "USCIS NAICS conflicts with profile")
    return counts


def json_bytes(value: dict) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def prune_profile_tags(profiles: list[dict]) -> int:
    changed = 0
    for entry in profiles:
        kept = sorted(set(entry.get("tags", [])) & KEEP_TAGS)
        if kept != entry.get("tags", []):
            entry["tags"] = kept
            changed += 1
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--findings", type=Path, action="append", default=[], help="Curated company JSON; repeat for multiple batches")
    parser.add_argument("--data-dir", type=Path, help="Optional USCIS CSV, DOL XLSX, and SEC tickers directory")
    parser.add_argument("--profiles", type=Path, default=ROOT / "profile/company_profiles.json")
    parser.add_argument("--pending", type=Path, default=ROOT / "profile/company_profiles_pending.json")
    parser.add_argument("--review", type=Path, default=ROOT / "profile/company_profiles_manual_review.json")
    parser.add_argument("--apply", action="store_true", help="Atomically save profile, pending, and review JSON")
    args = parser.parse_args()
    if not args.findings and not args.data_dir:
        parser.error("provide --findings and/or --data-dir")
    data_paths = ([args.data_dir / "Employer Information.csv", args.data_dir / "company_tickers.json",
                   *(args.data_dir / name for name, _ in LCA_FILES)] if args.data_dir else [])
    for path in [args.profiles, args.pending, *args.findings, *data_paths]:
        if not path.is_file():
            parser.error(f"missing input: {path}")
    profiles_payload = json.loads(args.profiles.read_text(encoding="utf-8"))
    profiles = profiles_payload["companies"]
    review: list[dict] = []
    stats = Counter()
    for finding_path in args.findings:
        stats.update(import_findings(profiles, validate_findings(json.loads(finding_path.read_text(encoding="utf-8"))), review))
    pending = load_pending(args.pending, profiles)
    if args.data_dir:
        index = source_index(profiles, pending, review)
        approvals, industries = read_uscis(args.data_dir / "Employer Information.csv", index)
        lca = {year: read_lca(args.data_dir / filename, index) for filename, year in LCA_FILES}
        public = read_sec(args.data_dir / "company_tickers.json", index, review)
        stats.update(apply_evidence(profiles, pending, approvals, industries, lca, public, review))
    stats["tags_simplified"] = prune_profile_tags(profiles)
    profiles_payload["_meta"]["company_count"] = len(profiles)
    profiles_payload["_meta"]["generated"] = date.today().isoformat()
    sources = profiles_payload["_meta"].setdefault("source_scope", [])
    for source in (["curated company findings"] if args.findings else []) + (["local USCIS, DOL, and SEC datasets"] if args.data_dir else []):
        if source not in sources:
            sources.append(source)
    profiles_payload["_meta"]["classification_notes"]["sponsor"] = (
        "Likely requires strong recent USCIS/DOL evidence or curated evidence; missing records stay unknown. "
        "Job-description evidence always overrides this company-level signal."
    )
    pending_payload = {"generated_at": date.today().isoformat(), "count": len(pending), "companies": pending}
    old_review = json.loads(args.review.read_text(encoding="utf-8")) if args.review.exists() else {}
    prior_items = old_review.get("items", []) if isinstance(old_review, dict) else []
    if not isinstance(prior_items, list):
        raise ValueError("manual review items must be a list")
    review = list({json.dumps(item, sort_keys=True): item for item in [*prior_items, *review]}.values())
    review_payload = {"generated_at": date.today().isoformat(), "count": len(review),
                      "summary": dict(stats), "items": sorted(review, key=lambda row: (row["name"].casefold(), row["field"], row["reason"]))}
    if args.apply:
        for path, payload in ((args.profiles, profiles_payload), (args.pending, pending_payload), (args.review, review_payload)):
            atomic_write(path, json_bytes(payload))
    print(json.dumps({"profile_count": len(profiles), "pending_count": len(pending), "review_count": len(review),
                      **stats, "saved": args.apply}, sort_keys=True))


if __name__ == "__main__":
    main()
