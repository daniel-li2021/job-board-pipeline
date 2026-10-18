// Offline migration rehearsal using the dashboard's actual reader/action functions.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const {execFileSync} = require('node:child_process');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const html = execFileSync('python3', ['-c', 'import dashboard; print(dashboard.HTML_TEMPLATE)'], {encoding:'utf8'});
let base = html.split('</script><script>')[1].split('</script>')[0];
base = base.slice(0, base.indexOf("window.addEventListener('online'"));
let extension = fs.readFileSync('dashboard_applied_history.js','utf8');
extension = extension.slice(0, extension.indexOf('  // Wait for the initial shared load')) + 'globalThis.prepareHistoryIndex=indexAppliedHistory;globalThis.clearHistoryIndex=()=>{appliedHistoryByCompany=null};})();';
async function run(groups) {
  const writes=[], cache={};
  const payload={snapshots:{},fresh_24h:[],rolling_3d:[],referrals:[],workflow_rows:input.rows,
    history_details:input.history,review_alias_groups:groups,supabase:{}};
  const fixedDate=class extends Date {constructor(...args){super(...(args.length?args:['2026-10-18T14:00:00Z']))} static now(){return 1792332000000}};
  const context=vm.createContext({console,Date:fixedDate,URL,setTimeout:()=>{},window:{addEventListener(){}},
    localStorage:{getItem:k=>cache[k],setItem:(k,v)=>cache[k]=v},
    document:{addEventListener(){},getElementById:()=>({textContent:JSON.stringify(payload),classList:{add(){}},href:''})}});
  vm.runInContext(base,context); vm.runInContext(extension,context);
  context.remote=JSON.parse(JSON.stringify(input.remote)); context.writes=writes;
  vm.runInContext(`renderAll=()=>{};renderReviewMessage=()=>{};
    supabase={from(){return {select(){return {order(){return {range:async(a,b)=>({data:remote.slice(a,b+1),error:null})}}}},upsert(payload){writes.push(payload);return Promise.resolve({error:null})}}}};`,context);
  await vm.runInContext('loadSharedStates()',context);
  const loadedWrites=writes.map(r=>[r.canonical_job_key,r.status,r.deleted]).sort();
  const states=JSON.parse(vm.runInContext('JSON.stringify(reviewStates)',context));
  const before=JSON.stringify(states);
  const keyChecks=vm.runInContext('Object.keys(reviewStates).every(k=>reviewState(k)?.status===reviewStates[k].status&&Boolean(reviewState(k)?.deleted)===Boolean(reviewStates[k].deleted))',context);
  context.samples=input.rows.slice(0,100);
  const started=performance.now();
  const originalBadges=vm.runInContext('samples.map(applicationHistoryBadges).join()',context);
  const historyBadge100Ms=Number((performance.now()-started).toFixed(3));
  const indexedStart=performance.now();
  vm.runInContext('prepareHistoryIndex()',context);
  assert.equal(vm.runInContext('samples.map(applicationHistoryBadges).join()',context),originalBadges);
  const indexedHistoryBadge100Ms=Number((performance.now()-indexedStart).toFixed(3));
  vm.runInContext('clearHistoryIndex()',context);
  let actionWrites=0;
  if(groups.length) {
    context.alias=groups.find(g=>g.some(k=>states[k]));
    if(context.alias) {
      const selected=context.alias[0], prior=vm.runInContext('reviewState(alias[0])?.canonical_job_key',context);
      context.selected=selected;
      vm.runInContext(`pushState=async()=>{};saveStates([selected],{deleted:true});`,context);
      const changed=JSON.parse(vm.runInContext('JSON.stringify(reviewStates)',context));
      const touched=Object.keys(changed).filter(k=>JSON.stringify(changed[k])!==JSON.stringify(states[k]));
      assert.equal(touched.length,1); assert.equal(touched[0],prior);
      actionWrites=touched.length;
      assert.equal(vm.runInContext('isDeleted({canonical_job_key:alias[alias.length-1]})',context),true);
    }
  }
  return {loadedWrites,keyChecks,historyBadge100Ms,indexedHistoryBadge100Ms,directStates:Object.keys(states).length,actionWrites,viewSha:require('node:crypto').createHash('sha256').update(before).digest('hex')};
}
(async()=>{
  const baseline=await run([]),compat=await run(input.groups);
  assert.deepEqual(compat.loadedWrites,baseline.loadedWrites,'Alias reads must not add/change automatic archive writes');
  assert.equal(compat.viewSha,baseline.viewSha,'Alias reads must retain every original expanded status');
  assert.equal(compat.keyChecks,true,'Current backup has conflicting alias statuses');
  console.log(JSON.stringify({actual_runtime_reader_exercised:true,expanded_status_rows:compat.directStates,
    original_state_projection_preserved:true,alias_statuses_agree:true,history_badges_100_rows_ms:compat.historyBadge100Ms,index_and_history_badges_100_rows_ms:compat.indexedHistoryBadge100Ms,
    preexisting_archive_backfills:baseline.loadedWrites.length,new_automatic_writes:0,
    simulated_explicit_delete_updates_existing_key:compat.actionWrites,network_requests:0}));
})().catch(error=>{console.error(error);process.exitCode=1});
