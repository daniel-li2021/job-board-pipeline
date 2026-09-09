// Run with: node tests/test_dashboard_runtime.js
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const {execFileSync} = require('node:child_process');
const html = execFileSync('python3', ['-c', 'import dashboard; print(dashboard.HTML_TEMPLATE)'], {encoding:'utf8'});
const payload = {snapshots:{}, fresh_24h:[], rolling_3d:[], referrals:[], workflow_rows:[], history_details:{}, supabase:{}};
const cache = {};
const context = vm.createContext({console, setTimeout, Date, localStorage:{getItem:k=>cache[k],setItem:(k,v)=>cache[k]=v}, document:{getElementById:()=>({textContent:JSON.stringify(payload)})}});
let script = html.split('</script><script>')[1].split('</script>')[0];
script = script.slice(0, script.indexOf("window.addEventListener('online'"));
vm.runInContext(script, context);
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
let extension = fs.readFileSync('dashboard_applied_history.js','utf8');
extension = extension.slice(0, extension.indexOf('  // Existing applied rows')) + 'globalThis.check={appliedRows,archiveStorageKey,decodeArchive,backfillAppliedArchives,expandedStates,getArchive:()=>archive};})();';
vm.runInContext(extension, context);
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
vm.runInContext("check.getArchive().one._applied_at='2024-01-01T00:00:00Z';check.getArchive().one._archive_updated_at='2099-01-01T00:00:00Z';check.getArchive().two._applied_at='2025-01-01T00:00:00Z';check.getArchive().two._archive_updated_at='2020-01-01T00:00:00Z'",context);
assert.equal(vm.runInContext("check.appliedRows(uniqueRows())[0].canonical_job_key",context),'two');
vm.runInContext(`
D.history_details.old=['official','Old Co','Senior Engineer','Boston, MA','https://example.com/old','B',78];
reviewStates.old={canonical_job_key:'old',status:'applied_complete',updated_at:'2026-09-08T00:00:00Z'};
check.backfillAppliedArchives();
`,context);
archived=JSON.parse(cache.jobAppliedArchiveCacheV1);
assert.equal(archived.old.tier,'B');assert.equal(archived.old.score,78);
assert.equal(archived.old.company,'Old Co');assert.equal(archived.old.title,'Senior Engineer');
assert.equal(archived.old.location,'Boston, MA');assert.equal(archived.old.url,'https://example.com/old');
assert.equal(archived.old._applied_at,'');
assert.equal(vm.runInContext("check.appliedRows(uniqueRows()).at(-1).canonical_job_key",context),'old');
vm.runInContext("allRows.push({canonical_job_key:'generic',company:'Archived application',title:'Previously applied job (source details expired)',tier:'-',score:'',_applied_archive:true});reviewStates.generic={canonical_job_key:'generic',status:'applied_complete',updated_at:'2099-01-01T00:00:00Z'}",context);
assert.equal(vm.runInContext("check.appliedRows(uniqueRows()).at(-1).canonical_job_key",context),'generic');
const migrated=vm.runInContext("check.decodeArchive({canonical_job_key:'applied-archive::'+JSON.stringify({k:'migrated',c:'Migrated',t:'Engineer',applied:'2020-01-01T00:00:00Z'}),updated_at:'2026-09-08T00:00:00Z'})",context);
assert.equal(migrated._applied_at,'');
const direct=vm.runInContext("check.decodeArchive({canonical_job_key:'applied-archive::'+JSON.stringify({k:'direct',c:'Direct',t:'Engineer',applied:'2026-09-08T00:00:00Z'}),updated_at:'2026-09-08T00:00:10Z'})",context);
assert.equal(direct._applied_at,'2026-09-08T00:00:00Z');
const expanded=vm.runInContext("check.expandedStates({canonical_job_key:'[\\\"id::one\\\",\\\"id::two\\\"]',status:'applied_complete',deleted:false,updated_at:'2020-01-01T00:00:00Z'},false)",context);
assert.equal(expanded.map(state=>state.canonical_job_key).join(','),'id::one,id::two');
assert.ok(expanded.every(state=>state._applied_at==='2020-01-01T00:00:00Z'));
assert.ok(!/<a (?!target="_blank" rel="noopener noreferrer")/.test(html+extension));
(async()=>{
vm.runInContext("supabase={from(){throw new Error('offline')}}",context);
await vm.runInContext('pushState(reviewStates.one)',context);
assert.equal(vm.runInContext("pendingKeys.size",context),0);
assert.equal(vm.runInContext("reviewStates.one.pending",context),true);
console.log('Dashboard runtime checks passed');
})().catch(error=>{console.error(error);process.exitCode=1});
