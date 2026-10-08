// Run with: node tests/test_dashboard_freshness.js
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync('dashboard_freshness.js', 'utf8');

function page(generatedAt, dashboard = false) {
  let now = Date.parse('2026-10-08T19:00:00Z');
  const overall = {textContent: 'Healthy', className: 'state state-healthy', dataset: {}};
  const badge = {textContent: 'Healthy', className: 'state state-healthy', dataset: {}};
  const banner = {textContent: '', style: {}};
  const heading = {textContent: 'Today'};
  const events = {}, documentEvents = {}, timers = [];
  const body = {dataset: {generatedAt}};
  const context = vm.createContext({
    Date: class extends Date {static now() {return now;}}, Intl,
    window: {addEventListener(name, fn) {events[name] = fn;}},
    document: {body, addEventListener(name, fn) {documentEvents[name] = fn;},
      getElementById(id) {return ({payload: dashboard ? {textContent: JSON.stringify({generated_at: generatedAt})} : null,
        publicationFreshness: banner, healthIndicator: dashboard ? overall : null, healthOverall: overall})[id];},
      querySelectorAll(selector) {return selector === 'h2' ? [heading] : [overall, badge];}},
    setInterval(fn, ms) {timers.push({fn, ms});},
  });
  vm.runInContext(source, context);
  return {overall, badge, banner, heading, body, events, documentEvents, timers,
    ageTo(value) {now = Date.parse(value);timers[0].fn();}};
}

for (const dashboard of [false, true]) {
  const fresh = page('2026-10-08T18:00:00Z', dashboard);
  assert.equal(fresh.overall.textContent, 'Healthy');
  assert.equal(fresh.body.dataset.publicationStale, 'false');
  assert.match(fresh.banner.textContent, /60 minutes old/);
  assert.equal(fresh.timers[0].ms, 60000);
  assert.equal(typeof fresh.events.focus, 'function');
  assert.equal(typeof fresh.documentEvents.visibilitychange, 'function');
  fresh.ageTo('2026-10-08T22:00:00Z');
  assert.equal(fresh.overall.textContent, 'Healthy'); // Exactly four hours.
  fresh.ageTo('2026-10-08T22:01:00Z');
  assert.match(fresh.overall.textContent, /Stale publication/);
  assert.equal(fresh.badge.textContent, 'Snapshot: Healthy');
  assert.ok(!fresh.badge.className.includes('state-healthy'));
  fresh.events.focus();
  assert.equal(fresh.badge.textContent, 'Snapshot: Healthy'); // Never double-prefix.
  for (const stamp of ['', 'invalid', '2026-10-09T19:00:00Z', '2026-10-05T19:00:00Z']) {
    const stale = page(stamp, dashboard);
    assert.match(stale.overall.textContent, /Stale publication/);
    assert.match(stale.banner.textContent, /Current scraper health is unverified/);
    assert.equal(stale.body.dataset.publicationStale, 'true');
  }
}
const yesterday = page('2026-10-08T06:30:00Z');
assert.match(yesterday.heading.textContent, /^Snapshot day/);
console.log('Dashboard and Health freshness checks passed.');
