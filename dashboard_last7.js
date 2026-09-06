// Last-7-days dashboard view: mirrors Fresh/Rolling active-job behavior.
// Loaded after dashboard_applied_history.js.
(() => {
  let recentSource = 'all';
  let recentCompany = 'all';
  let recentQuery = '';

  const recentCompanies = ['all', 'Google', 'Microsoft', 'Apple', 'Amazon', 'Meta', 'TikTok'];
  const tierRank = { A: 0, '1': 0, B: 1, '2': 1, '-': 2 };

  const recentSearchTerms = () => recentQuery.trim().toLowerCase().split(/\s+/).filter(Boolean);
  const matchesRecentSearch = row => {
    const terms = recentSearchTerms();
    if (!terms.length) return true;
    const haystack = `${row?.title || ''} ${row?.company || ''}`.toLowerCase();
    return terms.every(term => haystack.includes(term));
  };
  const recentAge = row => {
    const value = row?.freshness?.discovered?.age_hours;
    return Number.isFinite(value) ? value : 999999;
  };
  const recentScore = row => {
    const value = Number(row?.score);
    return Number.isFinite(value) ? value : -Infinity;
  };
  const sortRecent = rows => [...rows].sort((a, b) =>
    (tierRank[String(a?.tier || '-')] ?? 3) - (tierRank[String(b?.tier || '-')] ?? 3)
    || recentAge(a) - recentAge(b)
    || recentScore(b) - recentScore(a)
    || String(a?.company || '').localeCompare(String(b?.company || ''))
  );

  function recentBaseRows(rows = uniqueRows()) {
    return sortRecent(normalRows(rows).filter(row => {
      if (!['official', 'syncareer'].includes(row?.pipeline)) return false;
      const age = row?.freshness?.discovered?.age_hours;
      return Number.isFinite(age) && age <= 168;
    }));
  }

  function ensureEnhancedLastSevenDaysPanel() {
    let panel = document.getElementById('lastSevenDaysPanel');
    const deletedPanel = document.getElementById('deleted')?.closest('.panel');
    if (!panel && deletedPanel?.parentNode) {
      panel = document.createElement('section');
      panel.className = 'panel';
      panel.id = 'lastSevenDaysPanel';
      deletedPanel.parentNode.insertBefore(panel, deletedPanel);
    }
    if (!panel) return null;

    if (!panel.querySelector('#lastSevenDaysSearch')) {
      panel.innerHTML = `
        <h2>Last 7 Days</h2>
        <p>Unreviewed jobs discovered in the last seven days from Big Company Official and Syncareer. In Progress, Applied/Completed, deleted, and hidden-company jobs stay out of this view.</p>
        <div class="job-search">
          <input id="lastSevenDaysSearch" type="search" autocomplete="off" placeholder="Search title or company" aria-label="Search last seven days jobs by title or company">
          <button id="clearLastSevenDaysSearch" type="button" hidden>Clear</button>
          <span id="lastSevenDaysSearchCount" class="small" aria-live="polite"></span>
        </div>
        <div id="lastSevenDaysTabs" class="tabs"></div>
        <div id="lastSevenDaysCompanyTabs" class="tabs company-tabs"></div>
        <div id="lastSevenDays"></div>`;

      const input = panel.querySelector('#lastSevenDaysSearch');
      const clear = panel.querySelector('#clearLastSevenDaysSearch');
      input.value = recentQuery;
      input.oninput = () => {
        recentQuery = input.value;
        renderEnhancedLastSevenDays(uniqueRows());
      };
      input.onkeydown = event => {
        if (event.key === 'Escape' && input.value) {
          event.preventDefault();
          input.value = '';
          recentQuery = '';
          renderEnhancedLastSevenDays(uniqueRows());
        }
      };
      clear.onclick = () => {
        input.value = '';
        recentQuery = '';
        renderEnhancedLastSevenDays(uniqueRows());
        input.focus({ preventScroll: true });
      };
      panel.querySelector('#lastSevenDaysTabs').onclick = event => {
        const button = event.target.closest('[data-recent-source]');
        if (!button) return;
        recentSource = button.dataset.recentSource || 'all';
        if (recentSource !== 'official') recentCompany = 'all';
        renderEnhancedLastSevenDays(uniqueRows());
      };
      panel.querySelector('#lastSevenDaysCompanyTabs').onclick = event => {
        const button = event.target.closest('[data-recent-company]');
        if (!button) return;
        recentCompany = button.dataset.recentCompany || 'all';
        renderEnhancedLastSevenDays(uniqueRows());
      };
    }
    return panel;
  }

  function renderEnhancedLastSevenDays(rows = uniqueRows()) {
    const panel = ensureEnhancedLastSevenDaysPanel();
    if (!panel) return;

    const base = recentBaseRows(rows);
    const searched = base.filter(matchesRecentSearch);
    const officialCount = searched.filter(row => row.pipeline === 'official').length;
    const syncareerCount = searched.filter(row => row.pipeline === 'syncareer').length;
    const sourceChoices = [
      ['all', 'All', searched.length],
      ['official', 'Big Company Official', officialCount],
      ['syncareer', 'Syncareer', syncareerCount],
    ];

    panel.querySelector('#lastSevenDaysTabs').innerHTML = sourceChoices.map(([key, label, count]) =>
      `<button class="tab ${recentSource === key ? 'on' : ''}" type="button" data-recent-source="${key}">${label} (${count})</button>`
    ).join('');

    const companyTabs = panel.querySelector('#lastSevenDaysCompanyTabs');
    const officialRows = searched.filter(row => row.pipeline === 'official');
    if (recentSource === 'official') {
      companyTabs.style.display = 'flex';
      companyTabs.innerHTML = recentCompanies.map(company => {
        const count = company === 'all'
          ? officialRows.length
          : officialRows.filter(row => String(row.company || '').toLowerCase().includes(company.toLowerCase())).length;
        return `<button class="tab ${recentCompany === company ? 'on' : ''}" type="button" data-recent-company="${company}">${company === 'all' ? 'All' : company} (${count})</button>`;
      }).join('');
    } else {
      companyTabs.style.display = 'none';
      companyTabs.innerHTML = '';
    }

    let selected = searched;
    if (recentSource !== 'all') selected = selected.filter(row => row.pipeline === recentSource);
    if (recentSource === 'official' && recentCompany !== 'all') {
      selected = selected.filter(row => String(row.company || '').toLowerCase().includes(recentCompany.toLowerCase()));
    }
    selected = sortRecent(selected);

    const clear = panel.querySelector('#clearLastSevenDaysSearch');
    const count = panel.querySelector('#lastSevenDaysSearchCount');
    clear.hidden = !recentQuery.trim();
    count.textContent = recentQuery.trim()
      ? `${selected.length} match${selected.length === 1 ? '' : 'es'} in this view`
      : '';

    renderBox('lastSevenDays', selected);
  }

  const previousRenderAll = renderAll;
  renderAll = function() {
    previousRenderAll();
    renderEnhancedLastSevenDays(uniqueRows());
  };

  renderEnhancedLastSevenDays(uniqueRows());
})();
