// Dashboard runtime extension: immutable discovery counters + durable applied-job history.
// Loaded after dashboard.py's inline script by the Pages workflow.
(() => {
  const archivePrefix = 'applied-archive::';
  const archiveCacheKey = 'jobAppliedArchiveCacheV1';
  let archive = {};
  try { archive = JSON.parse(localStorage.getItem(archiveCacheKey) || '{}'); } catch (e) { archive = {}; }
  const archivePending = new Set();
  let recentSource = 'all';

  const persistAppliedArchive = () => {
    try { localStorage.setItem(archiveCacheKey, JSON.stringify(archive)); } catch (e) {}
  };
  const archiveTime = row => {
    const value = Date.parse(row?._archive_updated_at || '');
    return Number.isFinite(value) ? value : 0;
  };
  const compactSnapshot = row => ({
    k: String(row?.canonical_job_key || ''),
    p: String(row?.pipeline || ''),
    c: String(row?.company || ''),
    t: String(row?.title || ''),
    l: String(row?.location || ''),
    u: String(row?.url || ''),
    d: String(row?.posted_date || ''),
  });
  const archiveStorageKey = row => {
    const snapshot = compactSnapshot(row);
    const build = () => archivePrefix + JSON.stringify(snapshot);
    let key = build();
    if (key.length <= 2000) return key;
    snapshot.u = '';
    key = build();
    if (key.length <= 2000) return key;
    snapshot.t = snapshot.t.slice(0, 160);
    snapshot.l = snapshot.l.slice(0, 120);
    snapshot.c = snapshot.c.slice(0, 80);
    key = build();
    return key.length <= 2000 ? key : '';
  };
  const decodeArchive = state => {
    const key = String(state?.canonical_job_key || '');
    if (!key.startsWith(archivePrefix)) return null;
    try {
      const s = JSON.parse(key.slice(archivePrefix.length));
      if (!s?.k) return null;
      return {
        canonical_job_key: s.k,
        pipeline: s.p || '',
        company: s.c || 'Archived application',
        company_key: '',
        title: s.t || 'Previously applied job',
        location: s.l || '',
        posted_date: s.d || '',
        first_seen: '',
        tier: '-',
        score: '',
        sponsorship: 'Unknown',
        referral: '',
        url: s.u || '',
        freshness: { discovered: { age_hours: null }, posted: { trusted: false } },
        _applied_archive: true,
        _archive_updated_at: state.updated_at || '',
        pending: false,
      };
    } catch (e) { return null; }
  };
  const placeholderApplied = key => ({
    canonical_job_key: key,
    pipeline: '',
    company: 'Archived application',
    company_key: '',
    title: 'Previously applied job (source details expired)',
    location: '',
    posted_date: '',
    first_seen: '',
    tier: '-',
    score: '',
    sponsorship: 'Unknown',
    referral: '',
    url: String(key).startsWith('url::') ? String(key).slice(5) : '',
    freshness: { discovered: { age_hours: null }, posted: { trusted: false } },
    _applied_archive: true,
  });
  const isCompanyState = key => String(key || '').startsWith(companyStatePrefix);
  const currentSourceRow = key => [...allRows].reverse().find(row =>
    row?.canonical_job_key === key && !row?._applied_archive
  ) || null;

  function syncArchiveRows() {
    for (let i = allRows.length - 1; i >= 0; i--) {
      if (allRows[i]?._applied_archive) allRows.splice(i, 1);
    }
    const archived = Object.values(archive);
    const placeholders = Object.entries(reviewStates)
      .filter(([key, state]) => !isCompanyState(key) && normalizeStatus(state?.status) === 'applied_complete' && !archive[key])
      .map(([key]) => placeholderApplied(key));
    allRows.unshift(...archived, ...placeholders);
  }

  async function pushAppliedArchive(snapshot) {
    const jobKey = snapshot?.canonical_job_key;
    if (!supabase || !jobKey || archivePending.has(jobKey)) return;
    const storageKey = archiveStorageKey(snapshot);
    if (!storageKey) {
      if (archive[jobKey]) { archive[jobKey].pending = false; persistAppliedArchive(); }
      return;
    }
    archivePending.add(jobKey);
    const updatedAt = snapshot._archive_updated_at || new Date().toISOString();
    const payload = { canonical_job_key: storageKey, status: 'applied_complete', deleted: false, updated_at: updatedAt };
    const { error } = await supabase.from('job_review_status').upsert(payload, { onConflict: 'canonical_job_key' });
    archivePending.delete(jobKey);
    const current = archive[jobKey];
    if (error) {
      sharedError = `Could not sync applied history: ${error.message}`;
    } else if (current && archiveTime(current) <= Date.parse(updatedAt)) {
      current.pending = false;
      current._archive_updated_at = updatedAt;
      sharedError = '';
      persistAppliedArchive();
    }
    renderReviewMessage();
    renderAll();
  }

  function archiveAppliedJob(key) {
    const row = currentSourceRow(key) || archive[key];
    if (!row) return;
    const snapshot = decodeArchive({
      canonical_job_key: archiveStorageKey(row),
      updated_at: new Date().toISOString(),
    });
    if (!snapshot) return;
    snapshot.pending = true;
    archive[key] = snapshot;
    persistAppliedArchive();
    syncArchiveRows();
    pushAppliedArchive(snapshot);
  }

  function backfillAppliedArchives() {
    Object.entries(reviewStates).forEach(([key, state]) => {
      if (isCompanyState(key) || normalizeStatus(state?.status) !== 'applied_complete' || archive[key]) return;
      if (currentSourceRow(key)) archiveAppliedJob(key);
    });
  }

  // Headline cards are discovery metrics, not remaining-action counts.
  renderSummary = function() {
    const fresh = D.counts_24h || {}, rolling = D.counts_3d || {};
    document.getElementById('summary').innerHTML = Object.keys(names).map(k =>
      `<div class="card"><span>${names[k]}</span><div class="countline"><b>${fresh[k] || 0}</b><span>last 24h</span><i>·</i><b>${rolling[k] || 0}</b><span>in 3 days</span></div><a href="${D.report_links[k]}">open report</a></div>`
    ).join('');
  };

  function ensureLastSevenDaysPanel() {
    let panel = document.getElementById('lastSevenDaysPanel');
    if (panel) return panel;
    const deletedPanel = document.getElementById('deleted')?.closest('.panel');
    if (!deletedPanel?.parentNode) return null;
    panel = document.createElement('section');
    panel.className = 'panel';
    panel.id = 'lastSevenDaysPanel';
    panel.innerHTML = '<h2>Last 7 Days</h2><p>Jobs discovered in the last seven days from Big Company Official and Syncareer. Discovery time is based on when the pipeline first found the job, not the employer posting date.</p><div id="lastSevenDaysTabs" class="tabs"></div><div id="lastSevenDays"></div>';
    deletedPanel.parentNode.insertBefore(panel, deletedPanel);
    panel.querySelector('#lastSevenDaysTabs').onclick = event => {
      const button = event.target.closest('[data-recent-source]');
      if (!button) return;
      recentSource = button.dataset.recentSource || 'all';
      renderLastSevenDays(uniqueRows());
    };
    return panel;
  }

  function renderLastSevenDays(rows = uniqueRows()) {
    const panel = ensureLastSevenDaysPanel();
    if (!panel) return;
    const sourceChoices = [
      ['all', 'All'],
      ['official', 'Big Company Official'],
      ['syncareer', 'Syncareer'],
    ];
    panel.querySelector('#lastSevenDaysTabs').innerHTML = sourceChoices.map(([key, label]) =>
      `<button class="tab ${recentSource === key ? 'on' : ''}" type="button" data-recent-source="${key}">${label}</button>`
    ).join('');
    const recent = searchedRows(rows.filter(row => {
      if (!['official', 'syncareer'].includes(row?.pipeline)) return false;
      if (recentSource !== 'all' && row.pipeline !== recentSource) return false;
      if (isDeleted(row) || isCompanyHidden(row)) return false;
      const age = row?.freshness?.discovered?.age_hours;
      return Number.isFinite(age) && age <= 168;
    }));
    renderBox('lastSevenDays', recent);
  }

  // Archive metadata before the source row can age out of its 7-day store.
  setStatus = function(key, value) {
    if (!statusChoices.includes(value)) return;
    if (value === 'applied_complete') archiveAppliedJob(key);
    saveState(key, { status: value, deleted: false });
  };

  mainViewCounts = function(rows = uniqueRows()) {
    syncArchiveRows();
    rows = uniqueRows();
    return {
      fresh: searchedRows(normalRows(D.fresh_24h)).length,
      rolling: searchedRows(normalRows(D.rolling_3d)).length,
      'in-progress': searchedRows(rows.filter(r => statusOf(r) === 'in_progress' && !isDeleted(r))).length,
      applied: searchedRows(rows.filter(r => statusOf(r) === 'applied_complete')).length,
    };
  };

  renderAll = function() {
    syncArchiveRows();
    const rows = uniqueRows();
    renderSummary();
    tabs('fresh', D.fresh_24h);
    tabs('rolling', D.rolling_3d);
    renderBox('referrals', normalRows(D.referrals));
    renderBox('inProgress', searchedRows(rows.filter(r => statusOf(r) === 'in_progress' && !isDeleted(r))));
    renderBox('applied', searchedRows(rows.filter(r => statusOf(r) === 'applied_complete')));
    renderLastSevenDays(rows);
    const box = document.getElementById('deleted');
    box.innerHTML = jobs(rows.filter(isDeleted), true);
    bindStatus(box);
    renderHiddenCompanies(rows);
    renderMainViewTabs(rows);
    renderSearchState(rows);
  };

  syncPending = async function() {
    await Promise.all([
      ...Object.values(reviewStates).filter(state => state?.pending).map(state => pushState(state)),
      ...Object.values(archive).filter(row => row?.pending).map(row => pushAppliedArchive(row)),
    ]);
  };

  loadSharedStates = async function() {
    const rows = [];
    for (let from = 0; ; from += 1000) {
      const { data, error } = await supabase.from('job_review_status')
        .select('canonical_job_key,status,deleted,updated_at')
        .order('canonical_job_key', { ascending: true })
        .range(from, from + 999);
      if (error) throw error;
      const page = data || [];
      rows.push(...page);
      if (page.length < 1000) break;
    }

    const merged = {}, remoteArchive = {};
    rows.forEach(row => {
      const snapshot = decodeArchive(row);
      if (snapshot) {
        const previous = remoteArchive[snapshot.canonical_job_key];
        if (!previous || archiveTime(snapshot) >= archiveTime(previous)) remoteArchive[snapshot.canonical_job_key] = snapshot;
        return;
      }
      if (row.canonical_job_key && statusChoices.includes(row.status)) merged[row.canonical_job_key] = normalizedState(row, false);
    });

    Object.values(reviewStates).filter(state => state?.pending).forEach(local => {
      const remote = merged[local.canonical_job_key];
      if (!remote || stateTime(local) > stateTime(remote)) merged[local.canonical_job_key] = normalizedState(local, true);
    });
    Object.values(archive).filter(row => row?.pending).forEach(local => {
      const remote = remoteArchive[local.canonical_job_key];
      if (!remote || archiveTime(local) > archiveTime(remote)) remoteArchive[local.canonical_job_key] = local;
    });

    reviewStates = merged;
    archive = remoteArchive;
    persist();
    persistAppliedArchive();
    sharedLoaded = true;
    sharedError = '';
    syncArchiveRows();
    backfillAppliedArchives();
    renderReviewMessage();
    renderAll();
    await syncPending();
  };

  // Existing applied rows are immediately retained; old rows with already-pruned
  // metadata remain visible as placeholders instead of silently disappearing.
  syncArchiveRows();
  backfillAppliedArchives();
  renderAll();
})();
