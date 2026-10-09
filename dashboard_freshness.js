// Warn about an old compiled page without changing the recorded Health results.
(() => {
  const payload = document.getElementById('payload');
  const generatedAt = payload ? JSON.parse(payload.textContent).generated_at : document.body.dataset.generatedAt;
  const stamp = Date.parse(generatedAt || '');
  const banner = document.getElementById('publicationFreshness');
  function refresh() {
    const stale = Number.isFinite(stamp) && Date.now() - stamp > 24 * 60 * 60 * 1000;
    banner.hidden = !stale;
    banner.textContent = stale ? 'Dashboard has not been rebuilt in over 24 hours. Displayed data may be out of date.' : '';
    banner.style.color = '#795309';
  }
  refresh();
  setInterval(refresh, 60000);
})();
