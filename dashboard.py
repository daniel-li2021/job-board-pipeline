#!/usr/bin/env python3
"""Generate the read-only GitHub Pages job dashboard."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from zoneinfo import ZoneInfo

import coverage_reconcile
from sources.company_aliases import load_alias_file, match_company_alias
from sources.schema import classify_location_bucket

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"
DASHBOARD_JSON = PUBLIC_DIR / "dashboard.json"
DASHBOARD_HTML = PUBLIC_DIR / "index.html"
REPO_URL = "https://github.com/daniel-li2021/job-board-pipeline"
PAGES_URL = "https://daniel-li2021.github.io/job-board-pipeline/"
PACIFIC = ZoneInfo("America/Los_Angeles")
REFERRAL_PATH = BASE_DIR / "source" / "target_companies.json"
REVIEW_PATH = BASE_DIR / "profile" / "review_state.json"
OFFICIAL_REGISTRY_PATH = BASE_DIR / "source" / "official_careers.json"
INACTIVE_STATUSES = {"completed", "dismissed"}

STORE_PATHS = {
    "board": BASE_DIR / "output" / "board" / "jobs.json",
    "official": BASE_DIR / "output" / "official_careers" / "jobs.json",
    "syncareer": BASE_DIR / "output" / "syncareer" / "watchlist.json",
}
REPORT_PATHS = {
    "board": "output/board/inbox.md",
    "official": "output/official_careers/inbox.md",
    "syncareer": "output/syncareer/inbox.md",
}


def read_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def parse_dt(value: Any) -> Optional[datetime]:
    return coverage_reconcile.parse_datetime(value)


def _load_entries(path: Path) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    payload = read_json(path, {})
    if not isinstance(payload, dict):
        return {}, []
    entries = payload.get("entries", [])
    return payload, [dict(entry) for entry in entries if isinstance(entry, dict)]


def _age_bucket(age_hours: Optional[float]) -> str:
    if age_hours is None:
        return "unknown"
    if age_hours < 3:
        return "lt3h"
    if age_hours < 24:
        return "3to24h"
    if age_hours <= 72:
        return "1to3d"
    if age_hours <= 168:
        return "3to7d"
    return "gt7d"


def _age_hours(value: Optional[datetime], now: datetime) -> Optional[float]:
    return round(max(0.0, (now - value).total_seconds() / 3600), 2) if value else None


def recency(job: Dict[str, Any], now: datetime) -> Dict[str, Any]:
    """Expose posting recency and discovery activity as separate signals."""
    confidence = str(job.get("date_confidence") or "unknown").lower()
    posted_raw = str(job.get("posted_date") or job.get("posting_date") or "").strip()
    posted = parse_dt(posted_raw)
    first_seen = parse_dt(job.get("first_seen"))
    trusted = confidence in {"high", "medium"} and posted is not None
    date_only = bool(posted_raw) and len(posted_raw) == 10
    posted_age = _age_hours(posted, now) if trusted else None
    discovered_age = _age_hours(first_seen, now)
    posted_bucket = _age_bucket(posted_age)
    discovered_bucket = _age_bucket(discovered_age)

    if trusted:
        bucket = posted_bucket
        kind = "confirmed_posted_date_only" if date_only else "confirmed_posted"
        reference_at = posted.isoformat() if posted else ""
        age_hours = posted_age
    elif first_seen:
        bucket = "newly_discovered" if (discovered_age or 0) <= 72 else discovered_bucket
        kind = "newly_discovered"
        reference_at = first_seen.isoformat()
        age_hours = discovered_age
    else:
        bucket, kind, reference_at, age_hours = "unknown", "unknown", "", None
    return {
        "bucket": bucket,
        "kind": kind,
        "age_hours": age_hours,
        "reference_at": reference_at,
        "posted": {"bucket": posted_bucket, "age_hours": posted_age, "at": posted.isoformat() if posted and trusted else "", "date_only": date_only, "trusted": trusted},
        "discovered": {"bucket": discovered_bucket, "age_hours": discovered_age, "at": first_seen.isoformat() if first_seen else ""},
        # Dashboard windows intentionally follow discovery/Issue activity, not
        # the employer's posting date. posted_date remains reference metadata.
        "fresh_activity": discovered_age is not None and discovered_age <= 24,
        "rolling_activity": discovered_age is not None and discovered_age <= 72,
    }


def review_map() -> Dict[str, Any]:
    payload = read_json(REVIEW_PATH, {})
    jobs = payload.get("jobs", {}) if isinstance(payload, dict) else {}
    return jobs if isinstance(jobs, dict) else {}


def normalize_row(
    entry: Dict[str, Any],
    pipeline: str,
    now: datetime,
    referrals: List[Dict[str, Any]],
    review: Dict[str, Any],
    coverage_by_key: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    if pipeline == "syncareer":
        entry.setdefault("source_url", entry.get("job_url") or entry.get("url") or "")
        entry.setdefault("official_url", entry.get("job_url") or entry.get("url") or "")
        entry.setdefault("posted_date", entry.get("posting_date") or "")
        entry.setdefault("date_confidence", "medium")
        entry.setdefault("filter_status", "kept" if str(entry.get("kept", "")).lower() in {"yes", "true", "1"} else "dropped")
        entry.setdefault("tier", entry.get("tier") or "-")
    key = entry.get("canonical_job_key") or coverage_reconcile.canonical_job_key(entry)
    audit = coverage_by_key.get(key, {})
    state = review.get(key, {}) if isinstance(review.get(key, {}), dict) else {}
    referral = entry.get("referral_name") or entry.get("target_company_match") or match_company_alias(str(entry.get("company") or ""), referrals) or ""
    freshness = recency(entry, now)
    return {
        "canonical_job_key": key,
        "pipeline": pipeline,
        "source": entry.get("source") or pipeline,
        "company": entry.get("company", ""),
        "title": entry.get("title", ""),
        "location": entry.get("location", ""),
        "posted_date": entry.get("posted_date") or entry.get("posting_date") or "",
        "first_seen": entry.get("first_seen", ""),
        "date_confidence": entry.get("date_confidence", "unknown"),
        "freshness": freshness,
        "tier": entry.get("tier") or "-",
        "score": entry.get("match_score") if entry.get("match_score") is not None else entry.get("fit_score", ""),
        "referral": referral,
        "review_status": state.get("status", "unreviewed"),
        "coverage_status": audit.get("coverage_status") or entry.get("coverage_status") or ("official_canonical" if pipeline == "official" else "not_reconciled"),
        "canonical_source": audit.get("canonical_source") or entry.get("canonical_source") or pipeline,
        "duplicate_of": audit.get("duplicate_of") or entry.get("duplicate_of") or "",
        "url": entry.get("official_url") or entry.get("source_url") or entry.get("job_url") or entry.get("url") or "",
        "filter_status": entry.get("filter_status", "kept"),
        "suppress_alert": bool(audit.get("suppress_alert") or entry.get("suppress_alert")),
    }


def visible_candidate(row: Dict[str, Any]) -> bool:
    if row.get("filter_status") not in {"kept", ""}:
        return False
    if row.get("suppress_alert"):
        return False
    if classify_location_bucket(str(row.get("location") or "")) == "non_us":
        return False
    tier = str(row.get("tier") or "-")
    return tier in {"A", "B", "1", "2", "-"}


def _sort_rows(rows: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    bucket_rank = {"lt3h": 0, "3to24h": 1, "1to3d": 2, "newly_discovered": 3, "3to7d": 4, "gt7d": 5, "unknown": 6}
    tier_rank = {"A": 0, "1": 0, "B": 1, "2": 1, "-": 2}
    return sorted(
        rows,
        key=lambda row: (
            tier_rank.get(str(row.get("tier") or "-"), 3),
            -float(row.get("score") or 0),
            row["freshness"]["discovered"]["age_hours"] if row["freshness"]["discovered"]["age_hours"] is not None else 999999,
            bucket_rank.get(row["freshness"]["posted"]["bucket"], 9),
            str(row.get("company") or "").lower(),
        ),
    )


def official_search_catalog() -> List[Dict[str, Any]]:
    registry = read_json(OFFICIAL_REGISTRY_PATH, {})
    companies: List[Dict[str, Any]] = []
    for company in registry.get("companies", []) if isinstance(registry, dict) else []:
        if not isinstance(company, dict) or not company.get("enabled"):
            continue
        links = company.get("search_links") or []
        if isinstance(links, str):
            links = [{"label": "Official search", "url": links}]
        companies.append({
            "id": company.get("id", ""),
            "name": company.get("name", ""),
            "adapter": company.get("adapter", ""),
            "automation": "active" if company.get("adapter") != "skip" else "search_link_only",
            "search_links": [link for link in links if isinstance(link, dict) and link.get("url")],
            "note": company.get("skip_reason", "") if company.get("adapter") == "skip" else "",
        })
    return sorted(companies, key=lambda item: (item["automation"] != "active", str(item["name"]).lower()))


def build_payload(now: Optional[datetime] = None) -> Dict[str, Any]:
    now = now or datetime.now(timezone.utc)
    referrals = load_alias_file(REFERRAL_PATH)
    review = review_map()
    coverage = coverage_reconcile.build_coverage_payload(now)
    coverage_by_key = {record.get("canonical_job_key", ""): record for record in coverage.get("records", [])}

    snapshots: Dict[str, str] = {}
    all_rows: List[Dict[str, Any]] = []
    for pipeline, path in STORE_PATHS.items():
        store, entries = _load_entries(path)
        snapshots[pipeline] = str(store.get("updated_at") or store.get("scraped_at") or "")
        for entry in entries:
            all_rows.append(normalize_row(entry, pipeline, now, referrals, review, coverage_by_key))

    candidates = [row for row in all_rows if visible_candidate(row)]
    current = [row for row in candidates if str(row.get("review_status") or "").lower() not in INACTIVE_STATUSES]
    completed = _sort_rows(row for row in candidates if str(row.get("review_status") or "").lower() in INACTIVE_STATUSES)
    fresh = _sort_rows(row for row in current if row["freshness"]["fresh_activity"])
    rolling = _sort_rows(row for row in current if row["freshness"]["rolling_activity"])
    older = _sort_rows(
        row for row in current
        if row["freshness"]["discovered"]["age_hours"] is not None
        and 72 < row["freshness"]["discovered"]["age_hours"] <= 168
    )
    referral_rows = _sort_rows(
        row for row in current
        if row.get("referral")
        and row["freshness"]["discovered"]["age_hours"] is not None
        and row["freshness"]["discovered"]["age_hours"] <= 168
    )

    def counts(rows: Iterable[Dict[str, Any]]) -> Dict[str, int]:
        result = Counter(row["pipeline"] for row in rows)
        return {pipeline: result.get(pipeline, 0) for pipeline in STORE_PATHS}

    return {
        "generated_at": now.isoformat(),
        "updated_pt": now.astimezone(PACIFIC).strftime("%Y-%m-%d %H:%M %Z"),
        "pages_url": PAGES_URL,
        "repository": REPO_URL,
        "snapshots": snapshots,
        "report_links": {key: f"{REPO_URL}/blob/main/{path}" for key, path in REPORT_PATHS.items()},
        "referral_file": f"{REPO_URL}/blob/main/source/target_companies.json",
        "coverage_report": f"{REPO_URL}/blob/main/output/cross_pipeline/coverage.md",
        "counts_24h": counts(fresh),
        "counts_3d": counts(rolling),
        "fresh_24h": fresh[:500],
        "rolling_3d": rolling[:1000],
        "referrals": referral_rows[:500],
        "older_review": older[:500],
        "completed": completed[:500],
        "coverage": coverage,
        "official_searches": official_search_catalog(),
    }


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Daniel's Job Board</title>
<style>
:root{--bg:#f4f6f1;--card:#fff;--ink:#152018;--muted:#687269;--line:#dce2da;--green:#176b45;--gold:#ad6c00;--blue:#275fa8;--red:#9d3b31}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.wrap{max-width:1440px;margin:auto;padding:28px}header{display:flex;justify-content:space-between;gap:20px;align-items:flex-end;margin-bottom:20px}h1{font-size:30px;letter-spacing:-.03em;margin:0}h2{font-size:20px;margin:0 0 12px}p{margin:5px 0;color:var(--muted)}a{color:var(--blue)}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:20px 0}.card,.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:0 2px 10px #1b2a1d0a}.card{padding:16px}.card b{display:block;font-size:24px}.panel{padding:18px;margin:16px 0;overflow:hidden}.tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}.tab{border:1px solid var(--line);background:#fff;border-radius:999px;padding:7px 12px;cursor:pointer}.tab.on{background:var(--ink);color:#fff}.tablewrap{overflow:auto;max-height:620px}table{border-collapse:collapse;width:100%;min-width:930px}th,td{text-align:left;padding:9px 10px;border-bottom:1px solid #edf0ec;vertical-align:top}th{position:sticky;top:0;background:#fafbf9;color:#59645c;font-size:12px;text-transform:uppercase;letter-spacing:.04em}.pill{display:inline-block;padding:2px 7px;border-radius:999px;background:#edf2ee;font-size:12px;white-space:nowrap}.confirmed{color:var(--green);background:#e8f4ed}.discovered{color:var(--gold);background:#fff3d8}.gap{color:var(--red);background:#fbeae7}.duplicate{color:var(--green);background:#e8f4ed}.referral{color:#744a00;background:#fff0c8}.empty{padding:24px;color:var(--muted);text-align:center}.small{font-size:12px;color:var(--muted)}details{margin:10px 0;color:var(--muted)}summary{cursor:pointer;color:var(--blue)}.links{display:flex;gap:8px;flex-wrap:wrap}.active{color:var(--green)}.manual{color:var(--gold)}@media(max-width:760px){.wrap{padding:16px}.cards{grid-template-columns:1fr}header{display:block}}
</style></head><body><div class="wrap">
<header><div><h1>Job visibility dashboard</h1><p id="updated"></p></div><div><a id="repo">Repository</a> · <a id="coverageLink">Coverage audit</a></div></header>
<div class="cards" id="summary"></div>
<section class="panel"><h2>Fresh — newly found in the last 24 hours</h2><p>A/B jobs first discovered by the latest pipeline runs. Employer posting dates do not control this section.</p><div class="tabs" data-target="fresh"></div><div id="fresh"></div></section>
<section class="panel"><h2>Rolling — newly found in the last 3 days</h2><p>Current A/B (or Syncareer kept) candidates, ranked Tier A first, then score and discovery time.</p><div class="tabs" data-target="rolling"></div><div id="rolling"></div></section>
<section class="panel"><h2>Referral opportunities</h2><p>Aliases come only from <a id="referralFile">source/target_companies.json</a>.</p><div id="referrals"></div></section>
<section class="panel"><h2>Older / review later — discovered 3–7 days ago</h2><p>Status is read-only here and is committed in profile/review_state.json.</p><div id="older"></div></section>
<section class="panel"><h2>Completed / dismissed</h2><p>These jobs are removed from active sections so they do not repeatedly appear.</p><div id="completed"></div></section>
<section class="panel"><h2>Official coverage</h2><p>Coverage asks whether an ATS/LinkedIn/Syncareer discovery is also present in a dedicated official-company scrape. It is not match quality or application status.</p><details><summary>Coverage labels</summary><p><b>Official source</b>: canonical official listing. <b>Exact match — unvalidated</b>: found in official results, but company coverage still needs manual approval. <b>Official duplicate</b>: exact match for a validated company. <b>Official gap</b>: expected official match is missing. <b>Pending refresh</b>: external discovery is newer than the official snapshot. <b>No dedicated scraper</b>: company is outside the official registry. <b>Unsupported</b>: official adapter is not automated yet.</p></details><div id="coverage"></div></section>
<section class="panel"><h2>Official company search links</h2><p>Quick official searches for manual checks and future adapters. “Automated” entries already have a scraper; “link only” entries are intentionally not reverse-engineered yet.</p><div id="officialSearches"></div></section>
</div><script id="payload" type="application/json">__PAYLOAD__</script><script>
const D=JSON.parse(document.getElementById('payload').textContent); document.getElementById('updated').textContent=`Updated ${D.updated_pt} · snapshot ${D.generated_at}`; document.getElementById('repo').href=D.repository;document.getElementById('coverageLink').href=D.coverage_report;document.getElementById('referralFile').href=D.referral_file;
const names={official:'Big Company Official',board:'ATS / LinkedIn',syncareer:'Syncareer'};
document.getElementById('summary').innerHTML=Object.keys(names).map(k=>`<div class="card"><span>${names[k]}</span><b>${D.counts_24h[k]}</b><p>last 24h · ${D.counts_3d[k]} in 3 days</p><a href="${D.report_links[k]}">open report</a></div>`).join('');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const coverageNames={official_canonical:'Official source',covered_unvalidated:'Exact match — unvalidated',official_duplicate:'Official duplicate',official_gap:'Official gap',pending_official_refresh:'Pending refresh',not_dedicated:'No dedicated scraper',official_unsupported:'Unsupported',not_reconciled:'Not reconciled'};
const bucketNames={lt3h:'<3h', '3to24h':'3–24h', '1to3d':'1–3d', '3to7d':'3–7d', gt7d:'>7d', unknown:'unknown'};
function discoveryText(r){const d=r.freshness.discovered||{};return d.age_hours===null||d.age_hours===undefined?'Discovery unknown':`Found ${bucketNames[d.bucket]||d.bucket} ago`}
function postingText(r){const p=r.freshness.posted||{};if(!p.trusted)return r.posted_date?`Posted ${esc(r.posted_date)} · low confidence`:'Posting date unknown';return p.date_only?`Posted ${esc(r.posted_date)} · day precision`:`Posted ${bucketNames[p.bucket]||p.bucket} ago`}
function jobs(rows){if(!rows.length)return '<div class="empty">No qualifying jobs in this window.</div>';return `<div class="tablewrap"><table><thead><tr><th>Tier</th><th>Company / Title</th><th>Location</th><th>Discovered / Posted</th><th>Referral</th><th>Coverage</th><th>Status</th><th>Source</th></tr></thead><tbody>${rows.map(r=>`<tr><td><b>${esc(r.tier)}</b>${r.score!==''?`<div class="small">${esc(r.score)}</div>`:''}</td><td><b>${esc(r.company)}</b><br><a href="${esc(r.url)}">${esc(r.title)}</a></td><td>${esc(r.location)}</td><td><span class="pill discovered">${discoveryText(r)}</span><div class="small">${postingText(r)}</div></td><td>${r.referral?`<span class="pill referral">${esc(r.referral)}</span>`:'-'}</td><td><span class="pill ${r.coverage_status.includes('gap')?'gap':r.coverage_status.includes('duplicate')||r.coverage_status==='official_canonical'?'duplicate':''}">${esc(coverageNames[r.coverage_status]||r.coverage_status)}</span></td><td>${esc(r.review_status)}</td><td>${esc(names[r.pipeline]||r.pipeline)}</td></tr>`).join('')}</tbody></table></div>`}
function tabs(elId,rows){const tab=document.querySelector(`[data-target="${elId}"]`);const box=document.getElementById(elId);let active='all';const draw=()=>{tab.innerHTML=['all',...Object.keys(names)].map(k=>`<button class="tab ${k===active?'on':''}" data-k="${k}">${k==='all'?'All':names[k]} (${k==='all'?rows.length:rows.filter(r=>r.pipeline===k).length})</button>`).join('');box.innerHTML=jobs(active==='all'?rows:rows.filter(r=>r.pipeline===active));tab.querySelectorAll('button').forEach(b=>b.onclick=()=>{active=b.dataset.k;draw()})};draw()}
tabs('fresh',D.fresh_24h);tabs('rolling',D.rolling_3d);document.getElementById('referrals').innerHTML=jobs(D.referrals);document.getElementById('older').innerHTML=jobs(D.older_review);document.getElementById('completed').innerHTML=jobs(D.completed||[]);
const companies=D.coverage.companies||[];document.getElementById('coverage').innerHTML=`<div class="tablewrap"><table><thead><tr><th>Company</th><th>Manual state</th><th>In scope</th><th>Exact</th><th>Gaps</th><th>Pending</th><th>Coverage</th></tr></thead><tbody>${companies.map(c=>`<tr><td>${esc(c.name)}</td><td>${esc(c.manual_status)}</td><td>${c.in_scope}</td><td>${c.exact_covered}</td><td>${c.official_gaps}</td><td>${c.pending_refresh}</td><td>${c.coverage_ratio===null?'-':Math.round(c.coverage_ratio*100)+'%'}</td></tr>`).join('')}</tbody></table></div>`;
document.getElementById('officialSearches').innerHTML=`<div class="tablewrap"><table><thead><tr><th>Company</th><th>Automation</th><th>Official searches</th><th>Note</th></tr></thead><tbody>${(D.official_searches||[]).map(c=>`<tr><td><b>${esc(c.name)}</b></td><td class="${c.automation==='active'?'active':'manual'}">${c.automation==='active'?'Automated':'Link only'}</td><td><div class="links">${c.search_links.length?c.search_links.map(l=>`<a href="${esc(l.url)}">${esc(l.label||'Search')}</a>`).join(''):'-'}</div></td><td class="small">${esc(c.note)}</td></tr>`).join('')}</tbody></table></div>`;
</script></body></html>'''


def write_dashboard(payload: Dict[str, Any]) -> None:
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    DASHBOARD_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    DASHBOARD_HTML.write_text(HTML_TEMPLATE.replace("__PAYLOAD__", serialized), encoding="utf-8")
    (PUBLIC_DIR / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate GitHub Pages job dashboard")
    parser.add_argument("--json", action="store_true", help="Print compact counts")
    args = parser.parse_args()
    payload = build_payload()
    coverage_reconcile.write_coverage_outputs(payload["coverage"])
    write_dashboard(payload)
    if args.json:
        print(json.dumps({"counts_24h": payload["counts_24h"], "counts_3d": payload["counts_3d"]}, indent=2))
    else:
        print(f"Wrote {DASHBOARD_HTML} and {DASHBOARD_JSON}")


if __name__ == "__main__":
    main()
