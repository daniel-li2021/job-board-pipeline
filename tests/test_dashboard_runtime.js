// Run with: node tests/test_dashboard_runtime.js
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const {execFileSync} = require('node:child_process');
const html = execFileSync('python3', ['-c', 'import dashboard; print(dashboard.HTML_TEMPLATE)'], {encoding:'utf8'});
const payload = {snapshots:{}, fresh_24h:[], rolling_3d:[], referrals:[], workflow_rows:[], history_scores:{}, supabase:{}};
const cache = {};
const context = vm.createContext({console, setTimeout, Date, localStorage:{getItem:k=>cache[k],setItem:(k,v)=>cache[k]=v}, document:{getElementById:()=>({textContent:JSON.stringify(payload)})}});
let script = html.split('</script><script>')[1].split('</script>')[0];
script = script.slice(0, script.indexOf("window.addEventListener('online'"));
vm.runInContext(script, context);
let extension = fs.readFileSync('dashboard_applied_history.js','utf8');
extension = extension.slice(0, extension.indexOf('  // Existing applied rows')) + 'globalThis.check={appliedRows,archiveStorageKey,decodeArchive,backfillAppliedArchives};})();';
vm.runInContext(extension, context);
vm.runInContext(`
renderAll=()=>{};renderReviewMessage=()=>{};
allRows.push({canonical_job_key:'one',tier:'A',score:91,company:'X',title:'Engineer'}, {canonical_job_key:'two',tier:'B',score:0,company:'X',title:'Engineer'});
activeMainView='applied';
setStatus(['one','two'],'applied_complete');
`, context);
assert.equal(vm.runInContext("reviewStates.one.status", context),'applied_complete');
assert.equal(vm.runInContext("reviewStates.two.status", context),'applied_complete');
assert.equal(vm.runInContext("reviewStates['one,two']", context),undefined);
assert.equal(vm.runInContext('activeMainView', context),'applied');
let archived=JSON.parse(cache.jobAppliedArchiveCacheV1);
assert.equal(archived.one.tier,'A');assert.equal(archived.one.score,91);assert.equal(archived.two.score,0);
vm.runInContext(`
D.history_scores.old=['B',78];
reviewStates.old={canonical_job_key:'old',status:'applied_complete',updated_at:'2020-01-01T00:00:00Z'};
check.backfillAppliedArchives();
`,context);
archived=JSON.parse(cache.jobAppliedArchiveCacheV1);
assert.equal(archived.old.tier,'B');assert.equal(archived.old.score,78);assert.equal(archived.old._applied_at,'2020-01-01T00:00:00Z');
assert.equal(vm.runInContext("check.appliedRows(uniqueRows()).at(-1).canonical_job_key",context),'old');
assert.ok(!/<a (?!target="_blank" rel="noopener noreferrer")/.test(html+extension));
(async()=>{
vm.runInContext("supabase={from(){throw new Error('offline')}}",context);
await vm.runInContext('pushState(reviewStates.one)',context);
assert.equal(vm.runInContext("pendingKeys.size",context),0);
assert.equal(vm.runInContext("reviewStates.one.pending",context),true);
console.log('Dashboard runtime checks passed');
})().catch(error=>{console.error(error);process.exitCode=1});
