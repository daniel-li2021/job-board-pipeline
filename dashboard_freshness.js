// Inline in both pages so freshness checks survive a failed deployment or asset fetch.
(() => {
  const payload = document.getElementById('payload');
  const generatedAt = payload ? JSON.parse(payload.textContent).generated_at : document.body.dataset.generatedAt;
  const stamp = Date.parse(generatedAt || '');
  const banner = document.getElementById('publicationFreshness');
  const overall = document.getElementById('healthIndicator') || document.getElementById('healthOverall');
  const originalOverall = overall.textContent;
  const originalClass = overall.className;
  const maxAge = 4 * 60 * 60 * 1000;
  const pacificDay = value => new Intl.DateTimeFormat('en-CA', {timeZone:'America/Los_Angeles',year:'numeric',month:'2-digit',day:'2-digit'}).format(value);

  function refresh() {
    const age = Date.now() - stamp;
    const valid = Number.isFinite(stamp) && age >= -5 * 60 * 1000;
    const stale = !valid || age > maxAge;
    document.body.dataset.publicationStale = String(stale);
    banner.textContent = stale
      ? `Publication stale: ${valid ? `snapshot is ${Math.floor(age / 3600000)} hours old` : 'snapshot time is unavailable or invalid'}. Current scraper health is unverified. Figures below describe the saved snapshot. Check dashboard publishing in GitHub Actions.`
      : `Published snapshot · ${Math.max(0, Math.floor(age / 60000))} minutes old. Scraper results have their own timestamps.`;
    banner.style.cssText = stale ? 'color:#a22f2b;background:#fff0ce;padding:10px;border-radius:8px;font-weight:700' : '';
    overall.textContent = stale ? 'Health: Stale publication' : originalOverall;
    overall.className = stale ? 'state state-partial health-indicator health-stale' : originalClass;
    document.querySelectorAll('.state-healthy,.health-healthy,[data-snapshot-status]').forEach(badge => {
      if (badge === overall) return;
      if (!badge.dataset.snapshotStatus) {
        badge.dataset.snapshotStatus = badge.textContent;
        badge.dataset.snapshotClass = badge.className;
      }
      badge.textContent = stale ? `Snapshot: ${badge.dataset.snapshotStatus}` : badge.dataset.snapshotStatus;
      badge.className = stale ? 'state state-partial health-partial' : badge.dataset.snapshotClass;
    });
    // A page left open across midnight must not call yesterday's figures "Today".
    if (valid && pacificDay(stamp) !== pacificDay(Date.now())) {
      document.querySelectorAll('h2').forEach(heading => {
        if (heading.textContent === 'Today') heading.textContent = `Snapshot day · ${pacificDay(stamp)}`;
      });
    }
  }
  window.refreshPublicationFreshness = refresh;
  refresh();
  setInterval(refresh, 60000);
  window.addEventListener('focus', refresh);
  document.addEventListener('visibilitychange', refresh);
})();
