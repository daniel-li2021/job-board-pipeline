// Run with: node tests/test_dashboard_runtime.js
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const {execFileSync} = require('node:child_process');
const html = execFileSync('python3', ['-c', 'import dashboard; print(dashboard.HTML_TEMPLATE)'], {encoding:'utf8'});
const payload = {snapshots:{}, fresh_24h:[], rolling_3d:[], referrals:[], workflow_rows:[], history_details:{}, supabase:{}};
const cache = {};
let replacedUrl='';
const context = vm.createContext({console, setTimeout, Date, URL, location:{href:'https://example.com/job-board/',replace:url=>{replacedUrl=url}}, window:{addEventListener(){}}, localStorage:{getItem:k=>cache[k],setItem:(k,v)=>cache[k]=v}, document:{lastModified:'Mon, 21 Sep 2026 10:00:00 GMT',visibilityState:'visible',addEventListener(){},getElementById:()=>({textContent:JSON.stringify(payload),classList:{add(){}},href:''})}});
let script = html.split('</script><script>')[1].split('</script>')[0];
script = script.slice(0, script.indexOf("window.addEventListener('online'"));
vm.runInContext(script, context);
const renderSummaryOwner = vm.runInContext('renderSummary', context);
vm.runInContext(`
activeMainView='fresh';
exportViewLabels.fresh='Fresh → Big Company Official → Google';
exportViewRows.fresh=[{_variants:[
  {company:'Google',title:'AI | Engineer',score:91,location:'Seattle, WA',url:'https://example.com/full?job=1',tier:'A',pipeline:'official',sponsorship:'Unknown'},
  {company:'Google',title:'AI | Engineer',score:91,location:'New York, NY',url:'https://example.com/full?job=2',tier:'A',pipeline:'official',sponsorship:'Unknown'},
]}];
exportViewRows.rolling=[{company:'Other',title:'Wrong view',score:1,location:'Elsewhere',url:'https://example.com/wrong'}];
`, context);
const markdown = vm.runInContext('markdownExport()', context);
assert.match(markdown,/^## Fresh → Big Company Official → Google/);
assert.match(markdown,/\| Google \| AI \\\| Engineer \| 91 \| Seattle, WA \| https:\/\/example.com\/full\?job=1 \|/);
assert.match(markdown,/\| Google \| AI \\\| Engineer \| 91 \| New York, NY \| https:\/\/example.com\/full\?job=2 \|/);
assert.ok(!markdown.includes('Wrong view'));
assert.ok(!markdown.includes('Tier'));
assert.ok(!markdown.includes('Source'));
assert.ok(!markdown.includes('Sponsorship'));
vm.runInContext(`
D.fresh_24h=[
  {canonical_job_key:'hi',company:'Acme',title:'Staff Engineer',score:91,location:'Seattle, WA',url:'https://example.com/hi',tier:'A',pipeline:'official',sponsorship:'Sponsor',filter_status:'kept'},
  {canonical_job_key:'mid',company:'Acme',title:'Engineer',score:70,location:'Austin, TX',url:'https://example.com/mid',tier:'B',pipeline:'board',sponsorship:'Sponsor',filter_status:'kept'},
  {canonical_job_key:'visa',company:'Globex',title:'Engineer',score:95,location:'Remote',url:'https://example.com/visa',tier:'A',pipeline:'official',sponsorship:'No sponsor',filter_status:'kept'},
  {canonical_job_key:'blank',company:'Acme',title:'Unknown Score',score:'',location:'Boston, MA',url:'https://example.com/blank',tier:'-',pipeline:'syncareer',sponsorship:'Unknown',filter_status:'kept'}
];
D.rolling_3d=D.fresh_24h.slice();
searchQuery='engineer';
minScore='80';
sponsorshipFilters=new Set(['Sponsor']);
`, context);
const filtered = vm.runInContext('discoveryRows(D.fresh_24h).map(r=>r.canonical_job_key).join(",")', context);
assert.equal(filtered, 'hi');
assert.equal(vm.runInContext('searchedRows(D.fresh_24h).map(r=>r.canonical_job_key).join(",")', context), 'hi,mid,visa');
assert.equal(vm.runInContext('mainViewCounts().fresh', context), 1);
assert.equal(vm.runInContext('mainViewCounts()["in-progress"]', context), 0);
vm.runInContext(`
activeMainView='fresh';
exportViewLabels.fresh='Fresh → All';
exportViewRows.fresh=displayRows(discoveryRows(D.fresh_24h));
`, context);
const filteredMarkdown = vm.runInContext('markdownExport()', context);
assert.match(filteredMarkdown, /Staff Engineer/);
assert.ok(!filteredMarkdown.includes('Unknown Score'));
assert.ok(!filteredMarkdown.includes('https://example.com/mid'));
assert.ok(!filteredMarkdown.includes('https://example.com/visa'));
assert.match(vm.runInContext('jobs([],false,true)', context), /No qualifying jobs in this view/);
assert.equal(vm.runInContext("sponsorshipChoices.includes('No sponsor')", context), true);
assert.equal(vm.runInContext("sponsorshipChoices.includes('Likely')", context), true);
assert.equal(vm.runInContext("sponsorshipChoices.includes('Unlikely')", context), true);
assert.equal(vm.runInContext('jobs([],false)', context), '<div class="empty">No qualifying jobs in this view.</div>');
assert.ok(!vm.runInContext('jobs([],false,true)', context).includes('id="discoveryFilters"'));
vm.runInContext(`searchQuery='';minScore='';sponsorshipFilters=new Set(sponsorshipChoices);`, context);
const extensionSources = ['dashboard_applied_history.js','dashboard_last7.js'].map(file => fs.readFileSync(file,'utf8'));
extensionSources.forEach(source => assert.doesNotMatch(source, /\bfunction\s+renderSummary\b|\brenderSummary\s*=/));
let extension = extensionSources[0];
extension = extension.slice(0, extension.indexOf('  // Existing tracked rows')) + 'globalThis.check={appliedRows,applicationHistorySummary,archiveStorageKey,decodeArchive,backfillTrackedArchives,expandedStates,syncArchiveRows,completeTrackedRow,archiveTrackedJob,getArchive:()=>archive};})();';
vm.runInContext(extension, context);
assert.equal(vm.runInContext('renderSummary', context), renderSummaryOwner);
vm.runInContext(`
renderAll=()=>{};renderReviewMessage=()=>{};
allRows.push(
  {canonical_job_key:'one',pipeline:'official',tier:'A',score:91,company:'X',title:'Engineer',location:'Seattle, WA',url:'https://example.com/one'},
  {canonical_job_key:'two',pipeline:'board',tier:'B',score:0,company:'Y',title:'Developer',location:'Austin, TX',url:'https://example.com/two'}
);
activeMainView='applied';
setStatus(['one','two'],'applied_complete');
`, context);
assert.equal(vm.runInContext("reviewStates.one.status", context),'applied_complete');
assert.equal(vm.runInContext("reviewStates.two.status", context),'applied_complete');
assert.equal(vm.runInContext("reviewStates['one,two']", context),undefined);
assert.equal(vm.runInContext('activeMainView', context),'applied');
let archived=JSON.parse(cache.jobAppliedArchiveCacheV1);
assert.equal(archived.one.tier,'A');assert.equal(archived.one.score,91);assert.equal(archived.two.score,0);
assert.equal(archived.one.company,'X');assert.equal(archived.one.title,'Engineer');
assert.equal(archived.one.location,'Seattle, WA');assert.equal(archived.one.url,'https://example.com/one');
assert.equal(archived.one._applied_at,vm.runInContext('reviewStates.one.updated_at',context));
const roundTrip=vm.runInContext("check.decodeArchive({canonical_job_key:check.archiveStorageKey(check.getArchive().one),updated_at:check.getArchive().one._archive_updated_at})",context);
assert.equal(roundTrip.company,'X');assert.equal(roundTrip.title,'Engineer');assert.equal(roundTrip.location,'Seattle, WA');
assert.equal(roundTrip.tier,'A');assert.equal(roundTrip.score,91);assert.equal(roundTrip.url,'https://example.com/one');
assert.equal(roundTrip._applied_at,archived.one._applied_at);
const longKey=vm.runInContext("check.archiveStorageKey({...check.getArchive().one,url:'https://example.com/'+ 'x'.repeat(2200)})",context);
assert.ok(longKey.length<=2000);
assert.equal(vm.runInContext(`check.decodeArchive({canonical_job_key:${JSON.stringify(longKey)}}).company`,context),'X');
vm.runInContext(`
reviewStates['metlife-applied']={canonical_job_key:'metlife-applied',status:'applied_complete',deleted:false,updated_at:'2026-09-10T12:00:00Z'};
reviewStates['metlife-applied-2']={canonical_job_key:'metlife-applied-2',status:'applied_complete',deleted:false,updated_at:'2026-09-11T12:00:00Z'};
check.getArchive()['metlife-applied']={canonical_job_key:'metlife-applied',company:'MetLife',title:'Junior Software Engineer',_applied_at:'2026-09-10T12:00:00Z',_tracked_status:'applied_complete'};
check.getArchive()['metlife-applied-2']={canonical_job_key:'metlife-applied-2',company:'MetLife',title:'Platform Engineer',_applied_at:'2026-09-11T12:00:00Z',_tracked_status:'applied_complete'};
`,context);
const likelyRow={canonical_job_key:'metlife-new',company:'MetLife',title:'Junior Software Engineer',first_seen:'2026-09-12T12:00:00Z',tier:'B',score:80,url:'https://example.com/metlife-new',pipeline:'board',location:'',sponsorship:'Unknown',referral:'',freshness:{discovered:{},posted:{}}};
assert.deepEqual({...vm.runInContext(`check.applicationHistorySummary(${JSON.stringify(likelyRow)})`,context)},{count:2,likely:true});
assert.match(vm.runInContext(`applicationHistoryBadges(${JSON.stringify(likelyRow)})`,context),/Applied 2×.*Likely applied/);
assert.match(vm.runInContext(`jobRows([${JSON.stringify(likelyRow)}])`,context),/<b>MetLife<\/b><span class="application-badges">/);
assert.equal(vm.runInContext(`check.applicationHistorySummary(${JSON.stringify({...likelyRow,canonical_job_key:'metlife-applied'})}).likely`,context),false);
assert.equal(vm.runInContext(`check.applicationHistorySummary(${JSON.stringify({...likelyRow,company:'Other Co'})}).likely`,context),false);
assert.equal(vm.runInContext(`check.applicationHistorySummary(${JSON.stringify({...likelyRow,first_seen:'2026-09-25T12:00:01Z'})}).likely`,context),false);
assert.equal(vm.runInContext(`check.applicationHistorySummary(${JSON.stringify({...likelyRow,first_seen:'invalid',posted_date:'2026-09-12'})}).likely`,context),true);
assert.equal(vm.runInContext(`check.applicationHistorySummary(${JSON.stringify({...likelyRow,first_seen:'',posted_date:''})}).likely`,context),false);
vm.runInContext(`
reviewStates['vsolvit-applied']={canonical_job_key:'vsolvit-applied',status:'applied_complete',deleted:false,updated_at:'2026-09-10T12:00:00Z'};
check.getArchive()['vsolvit-applied']={canonical_job_key:'vsolvit-applied',company:'VSolvit',title:'SOFTWARE DEVELOPER (FULL STACK)',_applied_at:'2026-09-10T12:00:00Z',_tracked_status:'applied_complete'};
reviewStates['notion-applied']={canonical_job_key:'notion-applied',status:'applied_complete',deleted:false,updated_at:'2026-09-10T12:00:00Z'};
check.getArchive()['notion-applied']={canonical_job_key:'notion-applied',company:'Notion',title:'Software Engineer Early Career',_applied_at:'2026-09-10T12:00:00Z',_tracked_status:'applied_complete'};
`,context);
assert.equal(vm.runInContext("check.applicationHistorySummary({canonical_job_key:'vsolvit-new',company:'VSolvit',title:'FULL STACK SOFTWARE DEVELOPER',first_seen:'2026-09-12T12:00:00Z'}).likely",context),true);
assert.equal(vm.runInContext("check.applicationHistorySummary({canonical_job_key:'notion-new',company:'Notion',title:'Software Engineer Early Career AI',first_seen:'2026-09-12T12:00:00Z'}).likely",context),true);
vm.runInContext(`D.fresh_24h=[allRows.find(row=>row.canonical_job_key==='one'),${JSON.stringify(likelyRow)}]`,context);
assert.equal(vm.runInContext("normalRows(D.fresh_24h).map(row=>row.canonical_job_key).join(',')",context),'metlife-new');
vm.runInContext("check.getArchive().one._applied_at='2024-01-01T00:00:00Z';check.getArchive().one._archive_updated_at='2099-01-01T00:00:00Z';check.getArchive().two._applied_at='2025-01-01T00:00:00Z';check.getArchive().two._archive_updated_at='2020-01-01T00:00:00Z'",context);
assert.equal(vm.runInContext("check.appliedRows(uniqueRows())[0].canonical_job_key",context),'two');
vm.runInContext(`
D.history_details.old=['official','Old Co','Senior Engineer','Boston, MA','https://example.com/old','B',78];
reviewStates.old={canonical_job_key:'old',status:'applied_complete',updated_at:'2026-09-08T00:00:00Z'};
check.backfillTrackedArchives();
`,context);
archived=JSON.parse(cache.jobAppliedArchiveCacheV1);
assert.equal(archived.old.tier,'B');assert.equal(archived.old.score,78);
assert.equal(archived.old.company,'Old Co');assert.equal(archived.old.title,'Senior Engineer');
assert.equal(archived.old.location,'Boston, MA');assert.equal(archived.old.url,'https://example.com/old');
assert.equal(archived.old._applied_at,'');
assert.equal(vm.runInContext("check.appliedRows(uniqueRows()).at(-1).canonical_job_key",context),'old');
vm.runInContext(`
D.history_details.expired=['board','Recovered Co','Recovered Engineer','Austin, TX','https://example.com/expired','B',82];
reviewStates.expired={canonical_job_key:'expired',status:'applied_complete',updated_at:'2026-09-09T00:00:00Z'};
check.getArchive().expired={canonical_job_key:'expired',company:'Archived tracked job',title:'Tracked job (source details expired)',tier:'-',score:'',_tracked_status:'applied_complete',_tracked_archive:true,_applied_archive:true,_archive_updated_at:'2099-01-01T00:00:00Z'};
check.backfillTrackedArchives();
`,context);
archived=JSON.parse(cache.jobAppliedArchiveCacheV1);
assert.equal(archived.expired.company,'Recovered Co');assert.equal(archived.expired.title,'Recovered Engineer');
assert.ok(vm.runInContext("check.appliedRows(uniqueRows()).some(row=>row.canonical_job_key==='expired')",context));
vm.runInContext(`
legacyKey='url::https://jobs.sap.com/job/Palo-Alto-SAP-iXp-Intern-Full-Stack-AI-Developer-CA-94304/1425371233';
reviewStates[legacyKey]={canonical_job_key:legacyKey,status:'in_progress',updated_at:'2026-09-15T00:00:00Z'};
check.getArchive()[legacyKey]={canonical_job_key:legacyKey,company:'Archived tracked job',title:'Tracked job (source details expired)',location:'Palo Alto, CA',url:legacyKey.slice(5),tier:'B',score:95,_tracked_status:'in_progress',_tracked_archive:true,_archive_updated_at:'2099-01-01T00:00:00Z'};
check.backfillTrackedArchives();
`,context);
archived=JSON.parse(cache.jobAppliedArchiveCacheV1);
assert.equal(archived[vm.runInContext('legacyKey',context)].company,'SAP');
vm.runInContext(`
D.history_details['id::indeed::in-af8120c6f81934cd']=['board','','Software Engineer','San Francisco, CA, US','https://www.indeed.com/viewjob?jk=af8120c6f81934cd','A',88];
reviewStates['id::indeed::in-af8120c6f81934cd']={canonical_job_key:'id::indeed::in-af8120c6f81934cd',status:'applied_complete',updated_at:'2026-09-22T12:00:00Z'};
check.getArchive()['id::indeed::in-af8120c6f81934cd']={canonical_job_key:'id::indeed::in-af8120c6f81934cd',company:'Archived tracked job',title:'Software Engineer',_tracked_status:'applied_complete',_archive_updated_at:'2099-01-01T00:00:00Z'};
check.backfillTrackedArchives();
`,context);
assert.equal(vm.runInContext("check.getArchive()['id::indeed::in-af8120c6f81934cd'].company",context),'MintMCP');
vm.runInContext("check.syncArchiveRows();searchQuery='mintmcp'",context);
assert.ok(vm.runInContext("check.appliedRows(uniqueRows()).some(row=>row.company==='MintMCP')",context));
vm.runInContext("searchQuery=''",context);
vm.runInContext("allRows.push({canonical_job_key:'missing-company',company:'',title:'Developer',location:'Herndon, VA',url:'https://example.com/missing',tier:'A',score:88});window.prompt=()=>null;setStatus('missing-company','applied_complete')",context);
assert.equal(vm.runInContext("reviewStates['missing-company']",context),undefined);
vm.runInContext("window.prompt=()=> 'Verified Co';setStatus('missing-company','applied_complete')",context);
assert.equal(vm.runInContext("check.getArchive()['missing-company'].company",context),'Verified Co');
assert.equal(vm.runInContext("check.getArchive()['missing-company'].title",context),'Developer');
vm.runInContext("reviewStates['repair-me']={canonical_job_key:'repair-me',status:'applied_complete',updated_at:'2026-09-22T00:00:00Z'};check.syncArchiveRows()",context);
vm.runInContext('check.backfillTrackedArchives()',context);
assert.equal(vm.runInContext("check.getArchive()['repair-me']",context),undefined);
assert.match(vm.runInContext("applicationHistoryBadges(check.appliedRows(uniqueRows()).find(row=>row.canonical_job_key==='repair-me'))",context),/Add job details/);
vm.runInContext("window.prompt=message=>message.startsWith('Company')?'Repaired Co':'Repaired Engineer';check.archiveTrackedJob('repair-me','applied_complete','',check.completeTrackedRow('repair-me',undefined,true))",context);
assert.equal(vm.runInContext("check.getArchive()['repair-me'].company",context),'Repaired Co');
assert.equal(vm.runInContext("check.getArchive()['repair-me'].title",context),'Repaired Engineer');
vm.runInContext("allRows.push({canonical_job_key:'generic',company:'Archived application',title:'Previously applied job (source details expired)',tier:'-',score:'',_applied_archive:true});reviewStates.generic={canonical_job_key:'generic',status:'applied_complete',updated_at:'2099-01-01T00:00:00Z'}",context);
assert.equal(vm.runInContext("check.appliedRows(uniqueRows()).at(-1).canonical_job_key",context),'generic');
const migrated=vm.runInContext("check.decodeArchive({canonical_job_key:'applied-archive::'+JSON.stringify({k:'migrated',c:'Migrated',t:'Engineer',applied:'2020-01-01T00:00:00Z'}),updated_at:'2026-09-08T00:00:00Z'})",context);
assert.equal(migrated._applied_at,'');
const direct=vm.runInContext("check.decodeArchive({canonical_job_key:'applied-archive::'+JSON.stringify({k:'direct',c:'Direct',t:'Engineer',applied:'2026-09-08T00:00:00Z'}),updated_at:'2026-09-08T00:00:10Z'})",context);
assert.equal(direct._applied_at,'2026-09-08T00:00:00Z');
const expanded=vm.runInContext("check.expandedStates({canonical_job_key:'[\\\"id::one\\\",\\\"id::two\\\"]',status:'applied_complete',deleted:false,updated_at:'2020-01-01T00:00:00Z'},false)",context);
assert.equal(expanded.map(state=>state.canonical_job_key).join(','),'id::one,id::two');
assert.ok(expanded.every(state=>state._applied_at==='2020-01-01T00:00:00Z'));
vm.runInContext(`
allRows.push({canonical_job_key:'progress',pipeline:'official',tier:'B',score:80,company:'Progress Co',title:'Engineer',location:'Remote',url:'https://example.com/progress'});
setStatus('progress','in_progress');
allRows.splice(allRows.findIndex(row=>row.canonical_job_key==='progress'),1);
check.syncArchiveRows();
`,context);
assert.equal(vm.runInContext("uniqueRows().find(row=>row.canonical_job_key==='progress').company",context),'Progress Co');
assert.equal(vm.runInContext("reviewStates.progress.status",context),'in_progress');
const htmlAndExtension = html + extension;
const anchors = [...htmlAndExtension.matchAll(/<a\b[^>]*>/g)].map(match => match[0]);
assert.ok(anchors.filter(tag => !/href="#/.test(tag)).every(
  tag => /target="_blank"/.test(tag) && /rel="noopener noreferrer"/.test(tag),
));
(async()=>{
context.fetch=async()=>({ok:true,headers:{get:()=> 'Mon, 21 Sep 2026 09:00:00 GMT'}});
await vm.runInContext('checkForDashboardUpdate()',context);
assert.equal(replacedUrl,'');
context.fetch=async()=>({ok:true,headers:{get:()=> 'Mon, 21 Sep 2026 11:00:00 GMT'}});
await vm.runInContext('checkForDashboardUpdate()',context);
assert.match(replacedUrl,/\?v=\d+$/);
vm.runInContext("supabase={from(){throw new Error('offline')}}",context);
await vm.runInContext('pushState(reviewStates.one)',context);
assert.equal(vm.runInContext("pendingKeys.size",context),0);
assert.equal(vm.runInContext("reviewStates.one.pending",context),true);
console.log('Dashboard runtime checks passed');
})().catch(error=>{console.error(error);process.exitCode=1});
