// Run with: node tests/test_dashboard_freshness.js
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync('dashboard_freshness.js', 'utf8');

function page(generatedAt, dashboard) {
  let now = Date.parse('2026-10-08T19:00:00Z');
  const banner = {hidden: true, textContent: '', style: {}};
  const overall = {textContent: 'Healthy', className: 'state state-healthy'};
  let timer;
  vm.runInNewContext(source, {
    Date: class extends Date {static now() {return now;}},
    document: {body: {dataset: {generatedAt}},
      getElementById(id) {return ({payload: dashboard ? {textContent: JSON.stringify({generated_at: generatedAt})} : null,
        publicationFreshness: banner, healthIndicator: overall, healthOverall: overall})[id];}},
    setInterval(fn, ms) {assert.equal(ms, 60000);timer = fn;},
  });
  return {banner, overall, ageTo(value) {now = Date.parse(value);timer();}};
}
for (const dashboard of [false, true]) {
  const current = page('2026-10-08T15:00:00Z', dashboard);
  assert.equal(current.banner.hidden, true); // Four hours is normal.
  assert.equal(current.banner.textContent, '');
  current.ageTo('2026-10-09T15:00:00Z');
  assert.equal(current.banner.hidden, true); // Exactly 24 hours.
  current.ageTo('2026-10-09T15:01:00Z');
  assert.equal(current.banner.hidden, false);
  assert.match(current.banner.textContent, /has not been rebuilt in over 24 hours/);
  assert.equal(current.overall.textContent, 'Healthy');
  assert.equal(current.overall.className, 'state state-healthy');
  assert.equal(page('2026-10-05T19:00:00Z', dashboard).banner.hidden, false);
  for (const stamp of ['', 'invalid', '2026-10-09T19:00:00Z']) {
    assert.equal(page(stamp, dashboard).banner.hidden, true);
  }
}
console.log('Dashboard rebuild warning checks passed.');
