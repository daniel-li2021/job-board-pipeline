// Dashboard runtime extension: immutable discovery counters + durable applied-job history.
// Loaded after dashboard.py's inline script by the Pages workflow.
(() => {
  const archivePrefix = 'applied-archive::';
  const archiveCacheKey = 'jobAppliedArchiveCacheV1';
  let archive = {};
  try { archive = JSON.parse(localStorage.getItem(archiveCacheKey) || '{}'); } catch (e) { archive = {}; }
  const archivePending = new Set();
  let recentSource = 'all';

  const stateKeys = key => {
    if (!String(key || '').startsWith('[')) return [key];
    try {
      const keys = JSON.parse(key);
      return Array.isArray(keys) && keys.length && keys.every(value => typeof value === 'string') ? keys : [key];
    } catch (e) { return [key]; }
  };
  const expandedStates = (state, pending) => {
    const keys = stateKeys(state.canonical_job_key);
    const grouped = keys.length !== 1 || keys[0] !== state.canonical_job_key;
    return keys.map(key => {
      const snapshot = normalizedState({...state, canonical_job_key: key}, pending);
      snapshot._applied_at = state._applied_at || (
        grouped && normalizeStatus(state.status) === 'applied_complete' ? state.updated_at : ''
      );
      return snapshot;
    });
  };

  const persistAppliedArchive = () => {
    try { localStorage.setItem(archiveCacheKey, JSON.stringify(archive)); } catch (e) {}
  };
  const archiveTime = row => {
    const value = Date.parse(row?._archive_updated_at || '');
    return Number.isFinite(value) ? value : 0;
  };
  const compactSnapshot = row => ({
    v: 2,
    k: String(row?.canonical_job_key || ''),
    p: String(row?.pipeline || ''),
    c: String(row?.company || ''),
    t: String(row?.title || ''),
    l: String(row?.location || ''),
    u: String(row?.url || ''),
    d: String(row?.posted_date || ''),
    tier: row?.tier || '-',
    score: row?.score ?? '',
    applied: row?._applied_at || '',
  });
  const archiveStorageKey = row => {
    const key = archivePrefix + JSON.stringify(compactSnapshot(row));
    return key.length <= 2000 ? key : '';
  };
  const decodeArchive = state => {
    const key = String(state?.canonical_job_key || '');
    if (!key.startsWith(archivePrefix)) return null;
    try {
      const s = JSON.parse(key.slice(archivePrefix.length));
      if (!s?.k) return null;
      const applied = String(s.applied || '');
      const appliedTime = Date.parse(applied), archivedTime = Date.parse(state.updated_at || '');
      const trustedApplied = Number(s.v) >= 2 || (
        Number.isFinite(appliedTime) && Number.isFinite(archivedTime) && Math.abs(appliedTime - archivedTime) <= 60000
      );
      return {
        canonical_job_key: s.k,
        pipeline: s.p || '',
        company: s.c || 'Archived application',
        company_key: '',
        title: s.t || 'Previously applied job',
        location: s.l || '',
        posted_date: s.d || '',
        first_seen: '',
        tier: s.tier || '-',
        score: s.score ?? '',
        _applied_at: trustedApplied ? applied : '',
        sponsorship: 'Unknown',
        referral: '',
        url: s.u || (String(s.k).startsWith('url::') ? String(s.k).slice(5) : ''),
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
  const isCompanyState = key => isPreferenceKey(key) || String(key || '').startsWith(archivePrefix);

  const metadataFields = ['pipeline', 'company', 'title', 'location', 'url', 'tier', 'score'];
  const hasTier = row => row?.tier && row.tier !== '-';
  const hasScore = row => row?.score !== '' && row?.score != null;
  const hasMetadata = (row, field) => {
    if (field === 'tier') return hasTier(row);
    if (field === 'score') return hasScore(row);
    const value = String(row?.[field] || '');
    return Boolean(value) && value !== 'Archived application' && !value.startsWith('Previously applied job');
  };
  const metadataQuality = row => metadataFields.filter(field => hasMetadata(row, field)).length;
  const mergeArchive = (left, right) => {
    if (!left) return right;
    if (!right) return left;
    const newer = archiveTime(right) >= archiveTime(left) ? right : left;
    const merged = {...newer};
    metadataFields.forEach(field => {
      if (!hasMetadata(merged, field)) {
        const source = hasMetadata(right, field) ? right : left;
        if (hasMetadata(source, field)) merged[field] = source[field];
      }
    });
    const applied = [left._applied_at, right._applied_at]
      .filter(value => Number.isFinite(Date.parse(value)))
      .sort((a, b) => Date.parse(b) - Date.parse(a))[0];
    merged._applied_at = applied || '';
    return merged;
  };
  function recoveredRow(key) {
    const matches = [archive[key], ...allRows]
      .filter(row => row?.canonical_job_key === key);
    const details = (D.history_details || {})[key];
    const scores = (D.history_scores || {})[key];
    const historical = details ? {
      canonical_job_key: key, pipeline: details[0], company: details[1], title: details[2],
      location: details[3], url: details[4], tier: details[5], score: details[6],
    } : scores ? {canonical_job_key: key, tier: scores[0], score: scores[1]} : null;
    if (!matches.length && !historical) return null;
    const row = matches.reverse().reduce(mergeArchive, historical || placeholderApplied(key));
    return row;
  }
  const appliedTime = row => Date.parse(row?._applied_at || '') || 0;
  const appliedRows = rows => searchedRows(rows.filter(r => statusOf(r) === 'applied_complete' && !isDeleted(r)))
    .map(row => recoveredRow(row.canonical_job_key) || row)
    .sort((a, b) => appliedTime(b) - appliedTime(a)
      || metadataQuality(b) - metadataQuality(a)
      || String(a.company || '').localeCompare(String(b.company || ''))
      || String(a.title || '').localeCompare(String(b.title || '')));
  const discoveryActivityText = activityText;
  activityText = row => {
    if (!row?._applied_archive && !row?._applied_at) return discoveryActivityText(row);
    const applied = Date.parse(row._applied_at || '');
    if (!Number.isFinite(applied)) return 'Applied date unavailable';
    return `Applied ${new Intl.DateTimeFormat('en-US', {
      timeZone: 'America/Los_Angeles', month: 'short', day: 'numeric', year: 'numeric',
      hour: 'numeric', minute: '2-digit', hour12: true,
    }).format(new Date(applied)).replace(',', '')} PT`;
  };

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
      sharedError = 'Could not sync applied history: archived job metadata exceeds the storage limit';
      renderReviewMessage();
      return;
    }
    archivePending.add(jobKey);
    const updatedAt = snapshot._archive_updated_at || new Date().toISOString();
    const payload = { canonical_job_key: storageKey, status: 'applied_complete', deleted: false, updated_at: updatedAt };
    let error;
    try { ({ error } = await supabase.from('job_review_status').upsert(payload, { onConflict: 'canonical_job_key' })); }
    catch (failure) { error = failure; }
    finally { archivePending.delete(jobKey); }
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

  function archiveAppliedJob(key, appliedAt = archive[key]?._applied_at || '') {
    const row = recoveredRow(key);
    if (!row) return;
    const snapshot = {
      ...row,
      _applied_archive: true,
      _applied_at: appliedAt,
      _archive_updated_at: new Date().toISOString(),
      pending: true,
    };
    archive[key] = snapshot;
    persistAppliedArchive();
    syncArchiveRows();
    pushAppliedArchive(snapshot);
  }

  function backfillAppliedArchives() {
    Object.entries(reviewStates).forEach(([key, state]) => {
      if (isCompanyState(key) || normalizeStatus(state?.status) !== 'applied_complete') return;
      const recovered = recoveredRow(key), saved = archive[key];
      const improves = recovered && metadataFields.some(field => !hasMetadata(saved, field) && hasMetadata(recovered, field));
      if (!saved || improves) archiveAppliedJob(key, state._applied_at || saved?._applied_at || '');
    });
  }

  // Headline cards are discovery metrics, not remaining-action counts.
  renderSummary = function() {
    const fresh = D.counts_24h || {}, rolling = D.counts_3d || {};
    document.getElementById('summary').innerHTML = Object.keys(names).map(k =>
      `<div class="card"><span>${names[k]}</span><div class="countline"><b>${fresh[k] || 0}</b><span>last 24h</span><i>·</i><b>${rolling[k] || 0}</b><span>in 3 days</span></div><a target="_blank" rel="noopener noreferrer" href="${D.report_links[k]}">open report</a></div>`
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
  setStatus = function(keys, value) {
    if (!statusChoices.includes(value)) return;
    keys = Array.isArray(keys) ? keys : [keys];
    saveStates(keys, { status: value, deleted: false });
    if (value === 'applied_complete') keys.forEach(key => archiveAppliedJob(key, reviewState(key).updated_at));
  };

  mainViewCounts = function(rows = uniqueRows()) {
    syncArchiveRows();
    rows = uniqueRows();
    return {
      fresh: searchedRows(normalRows(D.fresh_24h)).length,
      rolling: searchedRows(normalRows(D.rolling_3d)).length,
      'in-progress': searchedRows(rows.filter(r => statusOf(r) === 'in_progress' && !isDeleted(r))).length,
      applied: appliedRows(rows).length,
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
    renderBox('applied', appliedRows(rows));
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
        remoteArchive[snapshot.canonical_job_key] = mergeArchive(previous, snapshot);
        return;
      }
      if (row.canonical_job_key && statusChoices.includes(row.status)) expandedStates(row, false).forEach(snapshot => {
        const key = snapshot.canonical_job_key;
        if (!merged[key] || stateTime(snapshot) >= stateTime(merged[key])) merged[key] = snapshot;
      });
    });

    Object.values(reviewStates).forEach(local => {
      expandedStates(local, Boolean(local.pending)).forEach(snapshot => {
        const key = snapshot.canonical_job_key;
        const remote = merged[key];
        if (!remote || stateTime(snapshot) > stateTime(remote)) merged[key] = snapshot;
      });
    });
    Object.values(archive).forEach(local => {
      const remote = remoteArchive[local.canonical_job_key];
      remoteArchive[local.canonical_job_key] = mergeArchive(remote, local);
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
