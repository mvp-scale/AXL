(function () {
  'use strict';
  const A = window.AXL, $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const esc = t => String(t == null ? '' : t).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const claimById = Object.fromEntries(A.claims.map(c => [c.id, c])), srcById = Object.fromEntries(A.sources.map(s => [s.id, s]));
  const defByVerb = Object.fromEntries(A.definitions.map(d => [d.verb, d])), verbRow = Object.fromEntries(A.verbs.map(v => [v.verb, v]));
  const st = { verb: 'polish', applied: new Set(), viewport: 'desktop', phase: 'ready', claim: null, picked: new Set(), extraCss: null };
  const save = (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} }, load = k => { try { return localStorage.getItem(k); } catch (e) { return null; } };
  const pct = x => Math.round(x * 100);

  /* theme */
  const root = document.documentElement, saved = load('axl-theme'); if (saved) root.dataset.theme = saved;
  $('#theme').addEventListener('click', () => { const dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; root.dataset.theme = dark ? 'light' : 'dark'; save('axl-theme', root.dataset.theme); });

  /* headline meter: system vs luck */
  (function meter() {
    const g = A.metrics.guidance_audited, t = g.by_tier, n = g.claims, seg = [['enforced', 'var(--pass)'], ['measurable', 'var(--warn)'], ['subjective', 'var(--fail)']];
    const bar = seg.map(([k, col]) => `<i style="width:${Math.max((t[k] || 0) / n * 100, t[k] ? 1.5 : 0)}%;background:${col}" title="${k}: ${t[k] || 0}"></i>`).join('');
    $('#meter').innerHTML = `<div class="bar" aria-hidden="true">${bar}</div><div class="txt"><b>${pct(g.luck_share)}%</b> of ${n} audited design-guidance statements have no measurable definition. <b>${pct(g.system_share)}%</b> do, ${t.enforced || 0} with a re-runnable check.</div>`;
  })();

  /* verb chips */
  (function chips() {
    const html = A.definitions.map(d => `<button type="button" data-verb="${d.verb}" aria-pressed="${d.verb === st.verb}">${d.verb}</button>`).join('');
    const undef = A.verbs.filter(v => v.resolution === 'undefined').length;
    $('#verbs').innerHTML = html + `<a class="more" href="#dictionary">+ ${undef} words with no measurable meaning yet</a>`;
    $('#verbs').addEventListener('click', e => { const b = e.target.closest('button[data-verb]'); if (!b) return; st.verb = b.dataset.verb; st.applied = new Set(); st.extraCss = null; $$('#verbs button').forEach(x => x.setAttribute('aria-pressed', x === b)); renderDefn(); applyPane(); });
  })();

  /* stage panes */
  const frames = { L: $('#frameL iframe'), R: $('#frameR iframe') }, wraps = { L: $('#frameL'), R: $('#frameR') };
  function sizeFrames() {
    for (const k of ['L', 'R']) {
      const w = wraps[k], f = frames[k], avail = w.clientWidth || 300;
      const fw = st.viewport === 'phone' ? 375 : 1100, fh = st.viewport === 'phone' ? 720 : 760, sc = Math.min(1, avail / fw);
      f.style.width = fw + 'px'; f.style.height = fh + 'px'; f.style.transform = `scale(${sc})`; w.style.height = Math.round(fh * sc) + 'px';
    }
  }
  const post = (f, msg) => { try { f.contentWindow.postMessage(msg, '*'); } catch (e) {} };
  function currentCss() { if (st.extraCss) return st.extraCss; return [...st.applied].map(id => A.css[id]).filter(Boolean).join('\n'); }
  function applyPane() {
    const css = currentCss();
    post(frames.R, { type: 'lab-recipe', css, highlight: '' });
    post(frames.L, { type: 'lab-sync-state', state: { phase: st.phase } }); post(frames.R, { type: 'lab-sync-state', state: { phase: st.phase } });
    $('#rightLabel').textContent = st.extraCss ? 'With the selected claim' : st.applied.size ? `With ${st.applied.size} check${st.applied.size > 1 ? 's' : ''} applied` : 'Nothing applied yet';
    renderScores();
  }
  for (const k of ['L', 'R']) frames[k].addEventListener('load', () => { sizeFrames(); applyPane(); });
  addEventListener('resize', sizeFrames);
  $('#viewport').addEventListener('click', e => { const b = e.target.closest('button'); if (!b) return; st.viewport = b.dataset.v; $$('#viewport button').forEach(x => x.setAttribute('aria-pressed', x === b)); sizeFrames(); });
  $('#phase').addEventListener('change', e => { st.phase = e.target.value; applyPane(); });

  /* receipts helpers */
  const rcs = ids => (ids || []).map(i => A.receipts[i]).filter(Boolean);
  function renderScores() {
    const ids = [...st.applied].flatMap(id => { for (const d of A.definitions) for (const p of d.patterns) if (p.id === id) return p.receipts.map(r => r.id); return []; });
    const rs = rcs([...new Set(ids)]), b = rs.filter(r => r.role === 'before'), a = rs.filter(r => r.role === 'after');
    const sum = xs => xs.reduce((n, r) => n + r.fails, 0);
    const L = $('#scoreL'), R = $('#scoreR');
    if (!b.length) { L.textContent = 'apply a check'; L.className = 'chip'; R.textContent = ''; R.className = 'chip'; return; }
    L.textContent = `${sum(b)} findings`; L.className = 'chip ' + (sum(b) ? 'bad' : 'good');
    R.textContent = `${sum(a)} findings`; R.className = 'chip ' + (sum(a) ? 'bad' : 'good');
  }

  /* definition panel */
  const tag = (k, v) => `<span class="tag ${esc(v)}" title="${k}">${esc(v)}</span>`;
  function receiptTable(rs) {
    if (!rs.length) return '<p class="small">No tool run yet.</p>';
    return `<table class="rc"><thead><tr><th scope="col">Run</th><th scope="col">Result</th><th scope="col">Findings</th></tr></thead><tbody>${rs.map(r => `<tr><td class="f">${esc(r.id)}</td><td>${r.exit_code === 0 ? 'pass' : 'fail'}</td><td>${r.fails}</td></tr>`).join('')}</tbody></table>`;
  }
  function renderDefn() {
    const d = defByVerb[st.verb], v = verbRow[st.verb];
    const pats = d.patterns.map(p => {
      const on = st.applied.has(p.id), has = !!A.css[p.id], c = claimById[p.claim_id];
      const discr = p.discriminates === false ? ' <span class="small">(the check passes on the original too)</span>' : '';
      return `<li class="pat${on ? ' on' : ''}" data-p="${p.id}"><header><h3>${esc(p.name)}</h3>${tag('tier', p.tier)}${tag('status', p.status)}</header><p>${esc(p.plain)}${discr}</p>
        <div class="row">${has ? `<button type="button" data-apply="${p.id}" aria-pressed="${on}">${on ? 'Applied' : 'Apply to the right pane'}</button>` : '<span class="small">Nothing to change on this page: it already passes.</span>'}<button type="button" data-open="${p.claim_id}">Sources</button></div></li>`;
    }).join('');
    const sel = [...st.applied].map(id => d.patterns.find(p => p.id === id)).filter(Boolean);
    const shown = sel.length ? sel[sel.length - 1] : null;
    let rec = '<p class="small">Apply a check to see its command and result.</p>';
    if (shown) rec = `<div class="receipt"><strong>${esc(shown.name)}</strong><span class="cmd" id="cmdText" tabindex="0" role="region" aria-label="Command to run">${esc(shown.check.command)}</span><button type="button" data-copy="${esc(shown.check.command)}">Copy command</button>
      <p class="small">Passes when: ${esc(shown.check.pass_criteria)}.<br>Parameter: ${esc(shown.parameter_origin || 'source')}. Coverage: ${esc(shown.coverage || '')}.</p>${shown.disagreement ? `<p class="small"><b>Where sources disagree:</b> ${esc(shown.disagreement)}</p>` : ''}${receiptTable(rcs(shown.receipts.map(r => r.id)))}
      <p class="small">Syntax example, not the explanation: <code>${esc(shown.example || '')}</code></p></div>`;
    $('#defn').innerHTML = `<h2>${esc(d.verb)}</h2><p class="plain">${esc(d.plain)}</p><p class="never"><b>Stays subjective:</b> ${esc(d.stays_subjective)}</p>
      <p class="small">${d.patterns.length} measurable patterns. ${v.resolution === 'tool-backed' ? 'At least one is enforced by a tool with a receipt.' : ''}</p><ul class="patterns">${pats}</ul>
      <button type="button" class="primary" data-all="1">Apply every check for “${esc(d.verb)}”</button>${rec}`;
    st.claim = shown ? shown.claim_id : (d.patterns[0] && d.patterns[0].claim_id) || st.claim; pinText();
  }
  $('#defn').addEventListener('click', e => {
    const a = e.target.closest('[data-apply]'), o = e.target.closest('[data-open]'), c = e.target.closest('[data-copy]'), all = e.target.closest('[data-all]');
    if (a) { const id = a.dataset.apply; st.extraCss = null; st.applied.has(id) ? st.applied.delete(id) : st.applied.add(id); renderDefn(); applyPane(); }
    if (all) { st.extraCss = null; defByVerb[st.verb].patterns.forEach(p => { if (A.css[p.id]) st.applied.add(p.id); }); renderDefn(); applyPane(); }
    if (o) openDrawer(o.dataset.open);
    if (c) { copy(c.dataset.copy, c); }
  });
  function copy(text, btn) { const done = () => { if (btn) { const t = btn.textContent; btn.textContent = 'Copied'; setTimeout(() => btn.textContent = t, 1200); } }; if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, done); else done(); }

  /* dictionary */
  (function dict() {
    const rows = A.verbs.slice().sort((a, b) => (a.resolution === 'undefined') - (b.resolution === 'undefined') || a.verb.localeCompare(b.verb));
    const n = { 'tool-backed': 0, measurable: 0, undefined: 0 }; rows.forEach(v => n[v.resolution]++);
    $('#dictSub').textContent = `${rows.length} words checked against ${A.sources.filter(s => s.fetch_status === 'ok').length} fetched sources. ${n['tool-backed']} are backed by a tool, ${n.measurable} are measurable, ${n.undefined} have no measurable definition anywhere we looked.`;
    $('#dictTable tbody').innerHTML = rows.map(v => {
      const d = defByVerb[v.verb];
      const meaning = d ? d.patterns.map(p => esc(p.name)).join('; ') : (v.shared_deltas.length ? v.shared_deltas.map(x => esc(x.property + ' ' + x.after)).join('; ') : 'No measurable definition in any source. It cannot ship as a skill.');
      return `<tr class="${v.resolution === 'undefined' ? 'undef' : ''}"><td>${esc(v.verb)}</td><td>${tag('resolution', v.resolution === 'undefined' ? 'subjective' : v.resolution === 'tool-backed' ? 'enforced' : 'measurable').replace(/>[^<]*</, `>${esc(v.resolution)}<`)}</td><td>${meaning}</td><td>${v.definitions.length} source${v.definitions.length === 1 ? '' : 's'}</td></tr>`;
    }).join('');
  })();

  /* evidence: rail */
  const groups = {}; A.claims.forEach(c => (groups[c.verb] = groups[c.verb] || []).push(c));
  (function srcFilter() { const ids = [...new Set(A.claims.map(c => c.source_id))].sort(); $('#fSource').innerHTML += ids.map(i => `<option value="${esc(i)}">${esc(srcById[i] ? srcById[i].publisher + ' · ' + srcById[i].url.replace(/^https?:\/\/(www\.)?/, '').slice(0, 36) : i)}</option>`).join(''); })();
  const filt = () => ({ tier: $('#fTier').value, status: $('#fStatus').value, surface: $('#fSurface').value, source: $('#fSource').value });
  function renderRail() {
    const f = filt(); let n = 0;
    const html = Object.keys(groups).sort().map(v => {
      const items = groups[v].filter(c => (!f.tier || c.tier === f.tier) && (!f.status || c.status === f.status) && (!f.surface || c.surface.includes(f.surface)) && (!f.source || c.source_id === f.source || c.supports.some(s => s.source_id === f.source)));
      if (!items.length) return ''; n += items.length;
      return `<details class="grp"${(f.tier || f.status || f.source || f.surface) ? ' open' : ''}><summary>${esc(v)}<span>${items.length}</span></summary>${items.map(c => {
        const can = c.tier === 'enforced' || c.tier === 'measurable';
        return `<div class="item">${can ? `<input type="checkbox" data-pick="${c.id}" aria-label="Include in export: ${esc(c.text.slice(0, 60))}"${st.picked.has(c.id) ? ' checked' : ''}>` : '<span style="width:20px;flex:none"></span>'}<button type="button" data-claim="${c.id}" aria-current="${st.claim === c.id}">${tag('tier', c.tier)}${esc(c.text.length > 130 ? c.text.slice(0, 127) + '…' : c.text)}</button></div>`;
      }).join('')}</details>`;
    }).join('');
    $('#catalog').innerHTML = html || '<p class="small">No claims match these filters.</p>'; $('#railCount').textContent = `${n} of ${A.claims.length} claims`;
  }
  ['fTier', 'fStatus', 'fSurface', 'fSource'].forEach(i => $('#' + i).addEventListener('change', renderRail));
  $('#catalog').addEventListener('click', e => { const b = e.target.closest('[data-claim]'); if (b) selectClaim(b.dataset.claim); });
  $('#catalog').addEventListener('change', e => { const p = e.target.closest('[data-pick]'); if (p) { p.checked ? st.picked.add(p.dataset.pick) : st.picked.delete(p.dataset.pick); } });

  /* independence explanation */
  function independence(c) {
    const roots = c.independent_roots || [], sup = c.supports || [];
    if (!c.quote) return 'No verified quote, so no root is counted.';
    const names = roots.map(r => (srcById[r] ? srcById[r].publisher : r));
    const how = `Roots come from the lineage graph: ${roots.length} distinct root${roots.length === 1 ? '' : 's'} (${names.join(', ') || 'none'}). A source that derives from another shares its root and counts once; a page that summarises several sources adds no root.`;
    return `${how} Status ${c.status}: ` + (c.status === 'verified' ? 'two or more independent roots state it.' : c.status === 'single-source' ? 'one root states it.' : 'the quote could not be matched.');
  }
  function claimDetail(c) {
    const can = c.tier === 'enforced' || c.tier === 'measurable';
    const dl = c.delta ? `<dl class="kv"><dt>Selector</dt><dd>${esc(c.delta.selector)}</dd><dt>Property</dt><dd>${esc(c.delta.property)}</dd><dt>Before</dt><dd>${esc(c.delta.before == null ? 'not stated by the source' : c.delta.before)}</dd><dt>After</dt><dd>${esc(c.delta.after)}</dd></dl>` : '';
    const enf = c.enforcement ? `<p><strong>Command that was run</strong></p><span class="cmd" tabindex="0" role="region" aria-label="Command that was run">${esc(c.enforcement.command)}</span><p class="small">Passes when: ${esc(c.enforcement.pass_criteria)}</p>${receiptTable(rcs(c.receipts))}` : '';
    return `<h3>${tag('tier', c.tier)} ${tag('status', c.status)} <span class="small">${esc(c.verb)}</span></h3><p>${esc(c.text)}</p>
      ${c.quote ? `<blockquote>${esc(c.quote)}</blockquote>` : '<p class="small">No verbatim quote found in the saved source; this entry is a paraphrase from the legacy catalog and is marked unverified.</p>'}
      ${can ? dl + enf : '<div class="nodef">No measurable definition. This claim is kept in the catalog but cannot be applied, exported as a correction, or shipped as a skill.</div>'}
      <div class="row"><button type="button" data-open="${c.id}" class="primary">Sources</button>${c.css ? `<button type="button" data-try="${c.id}">Apply to the demo</button>` : ''}</div>`;
  }
  function selectClaim(id) { st.claim = id; const c = claimById[id]; $('#detail').innerHTML = claimDetail(c); $$('#catalog [data-claim]').forEach(b => b.setAttribute('aria-current', b.dataset.claim === id)); pinText(); highlight(c); }
  $('#detail').addEventListener('click', e => { const o = e.target.closest('[data-open]'), t = e.target.closest('[data-try]'); if (o) openDrawer(o.dataset.open); if (t) { st.extraCss = claimById[t.dataset.try].css; st.applied = new Set(); applyPane(); $('#stage').scrollIntoView(); } });
  function pinText() { const c = claimById[st.claim]; $('#pinText').textContent = c ? `${c.tier} · ${c.status} · ${c.text.slice(0, 90)}` : 'Pick a claim to see its sources'; }

  /* lineage map */
  const cited = A.sources.filter(s => s.cited || s.derives_from.length || A.sources.some(o => o.derives_from.includes(s.id)));
  const rootList = [...new Set(cited.map(s => s.root))];
  const palette = ['#0a6b5e', '#a3301c', '#7d5200', '#1f5fa8', '#7a3d8f', '#4d5a66', '#8a6d00', '#00786a'];
  const rootColor = r => palette[rootList.indexOf(r) % palette.length];
  const pos = {}, labels = [];
  (function layout() {
    const byRoot = {}; cited.forEach(s => (byRoot[s.root] = byRoot[s.root] || []).push(s));
    const multi = Object.keys(byRoot).filter(r => byRoot[r].length > 1).sort((a, b) => byRoot[b].length - byRoot[a].length), single = Object.keys(byRoot).filter(r => byRoot[r].length === 1);
    let y = 8;
    for (let i = 0; i < multi.length; i += 2) {
      const row = multi.slice(i, i + 2), rad = Math.max(...row.map(r => Math.min(58, 16 + byRoot[r].length * 3)));
      row.forEach((r, k) => { const cx = row.length === 1 ? 140 : 70 + k * 140, cy = y + rad + 6, m = byRoot[r], rootNode = m.find(s => s.id === r) || m[0], kids = m.filter(s => s !== rootNode);
        pos[rootNode.id] = { x: cx, y: cy }; kids.forEach((s, n) => { const ang = (n / Math.max(kids.length, 1)) * Math.PI * 2 - Math.PI / 2; const rr = kids.length > 6 ? rad * (n % 2 ? .95 : .62) : rad * .8; pos[s.id] = { x: cx + Math.cos(ang) * rr, y: cy + Math.sin(ang) * rr }; });
        labels.push({ x: cx, y: cy + rad + 20, t: `${(srcById[r] ? srcById[r].publisher : r).slice(0, 22)} ×${m.length}` }); });
      y += rad * 2 + 34;
    }
    y += 12;
    single.forEach((r, i) => { pos[byRoot[r][0].id] = { x: 12 + (i % 10) * 26, y: y + 8 + Math.floor(i / 10) * 24 }; });
    labels.push({ x: 140, y: y - 4, t: `single voices (${single.length})` });
    $('#lineage').dataset.h = y + Math.ceil(single.length / 10) * 24 + 16;
  })();
  function drawLineage(active) {
    const h = +$('#lineage').dataset.h, act = new Set(active || []);
    const edges = A.lineage.edges.filter(e => pos[e.from] && pos[e.to] && A.lineage.roots[e.from] === A.lineage.roots[e.to]).map(e => `<line x1="${pos[e.from].x}" y1="${pos[e.from].y}" x2="${pos[e.to].x}" y2="${pos[e.to].y}" stroke="${rootColor(A.lineage.roots[e.from].split('+')[0])}" stroke-width="1.5" opacity="${act.size && !(act.has(e.from) || act.has(e.to)) ? .15 : .7}"/>`).join('');
    const nodes = cited.map(s => { const p = pos[s.id], on = !act.size || act.has(s.id); return `<g class="node" tabindex="0" role="button" data-src="${esc(s.id)}" aria-label="${esc(s.publisher)}, ${s.kind}, root ${esc(srcById[s.root] ? srcById[s.root].publisher : s.root)}"><circle cx="${p.x}" cy="${p.y}" r="${s.kind === 'primary' ? 7 : 5}" fill="${rootColor(s.root.split('+')[0])}" opacity="${on ? 1 : .2}" stroke="${act.has(s.id) ? 'var(--ink)' : 'none'}" stroke-width="2.5"/><title>${esc(s.publisher)} (${s.kind})</title></g>`; }).join('');
    const lab = labels.map(l => `<text x="${l.x}" y="${l.y}" text-anchor="middle">${esc(l.t)}</text>`).join('');
    $('#lineage').innerHTML = `<svg viewBox="0 0 280 ${h}" role="group" aria-label="Source lineage map, one focusable dot per source">${edges}${lab}${nodes}</svg>`;
  }
  function highlight(c) { drawLineage(c ? [c.source_id, ...(c.supports || []).map(s => s.source_id), ...(c.independent_roots || [])] : []); }
  $('#lineage').addEventListener('click', e => { const n = e.target.closest('[data-src]'); if (n) openDrawer(null, n.dataset.src); });
  $('#lineage').addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { const n = e.target.closest('[data-src]'); if (n) { e.preventDefault(); openDrawer(null, n.dataset.src); } } });

  /* sources drawer */
  const drawer = $('#drawer'); let lastFocus = null;
  function chainHtml(s) { return `<ul class="chain">${s.chain.map((id, i) => `<li>${i ? 'derives from ' : ''}${esc(srcById[id].publisher)} <span class="small">(${srcById[id].kind})</span></li>`).join('')}</ul>`; }
  function srcCard(id, quote, note) {
    const s = srcById[id]; if (!s) return `<p>${esc(id)}</p>`;
    return `<div><h3>${esc(s.publisher)} ${tag('kind', s.kind === 'primary' ? 'process' : 'subjective').replace(/>[^<]*</, `>${s.kind}<`)}</h3>${quote ? `<blockquote>${esc(quote)}</blockquote>` : ''}${note ? `<p class="small">${esc(note)}</p>` : ''}
      <dl class="kv"><dt>URL</dt><dd><a href="${esc(s.url)}" rel="noopener noreferrer" target="_blank">${esc(s.url)}</a></dd><dt>Retrieved</dt><dd>${esc(s.retrieved_at || 'not fetched')}</dd><dt>Licence</dt><dd>${esc(s.license)}</dd><dt>Content hash</dt><dd>${esc((s.content_hash || 'n/a').slice(0, 16))}</dd></dl>${chainHtml(s)}${s.lineage_note ? `<p class="small">${esc(s.lineage_note)}</p>` : ''}</div>`;
  }
  function openDrawer(claimId, srcId) {
    lastFocus = document.activeElement; const c = claimById[claimId || st.claim];
    if (c && !srcId) { st.claim = c.id; pinText(); highlight(c); }
    let h = '';
    if (srcId) h = srcCard(srcId, null, 'Selected from the lineage map.');
    else if (c) {
      h = `<p><b>Claim:</b> ${esc(c.text)}</p><p>${tag('tier', c.tier)} ${tag('status', c.status)}</p>` + srcCard(c.source_id, c.quote, c.quote ? 'Verbatim from the fetched page.' : 'No verbatim quote could be matched in the fetched page.') +
        (c.supports || []).map(s => '<hr>' + srcCard(s.source_id, s.quote, 'Second source.')).join('') +
        `<h3>Independence: ${(c.independent_roots || []).length} root${(c.independent_roots || []).length === 1 ? '' : 's'}</h3><p>${esc(independence(c))}</p>
        <div class="howto"><h3>How to re-check</h3><ol><li>Run <code>python3 axl/scripts/refetch_sources.py</code>; it re-downloads the page and flags a changed hash.</li><li>Search the saved text in <code>axl/receipts/sources/</code> for the quote above.</li>${c.enforcement ? `<li>Run the command: <code>${esc(c.enforcement.command)}</code></li>` : '<li>No tool command exists for this claim; it cannot be checked mechanically.</li>'}</ol></div>`;
    } else h = '<p>Pick a claim first.</p>';
    $('#paneClaim').innerHTML = h; drawer.hidden = false; $('#tabClaim').click(); $('#drawerClose').focus();
  }
  function closeDrawer() { drawer.hidden = true; if (lastFocus) lastFocus.focus(); }
  $('#srcBtn').addEventListener('click', () => openDrawer());
  $('#drawerClose').addEventListener('click', closeDrawer);
  drawer.addEventListener('click', e => { if (e.target === drawer) closeDrawer(); });
  drawer.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeDrawer();
    if (e.key === 'Tab') { const f = $$('button,a[href]', drawer).filter(x => x.offsetParent !== null); if (!f.length) return; const a = f[0], z = f[f.length - 1]; if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); } else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); } }
  });
  function tab(which) { const all = which === 'all'; $('#tabAll').setAttribute('aria-selected', all); $('#tabClaim').setAttribute('aria-selected', !all); $('#paneAll').hidden = !all; $('#paneClaim').hidden = all;
    if (all && !$('#paneAll').dataset.done) { $('#paneAll').dataset.done = 1; $('#paneAll').innerHTML = `<div class="table-wrap" tabindex="0" role="region" aria-label="All sources"><table class="rc"><thead><tr><th scope="col">Source</th><th scope="col">Kind</th><th scope="col">Root</th><th scope="col">Fetch</th><th scope="col">Licence</th></tr></thead><tbody>${A.sources.map(s => `<tr><td><a href="${esc(s.url)}" rel="noopener noreferrer" target="_blank">${esc(s.publisher)}</a></td><td>${s.kind}</td><td>${esc(srcById[s.root] ? srcById[s.root].publisher : s.root)}</td><td>${esc(s.fetch_status.slice(0, 28))}</td><td>${esc(s.license.slice(0, 20))}</td></tr>`).join('')}</tbody></table></div>`; } }
  $('#tabClaim').addEventListener('click', () => tab('claim')); $('#tabAll').addEventListener('click', () => tab('all'));

  /* export: an AXL document from the selected claims */
  function ops(c) {
    const out = []; if (!c.css) return out;
    for (const m of c.css.matchAll(/([^{}@]+)\{([^{}]+)\}/g)) for (const d of m[2].split(';')) { const i = d.indexOf(':'); if (i < 1) continue; out.push({ op: 'set', target: m[1].trim(), property: d.slice(0, i).trim(), value: d.slice(i + 1).replace(/!important/, '').trim(), reason: c.text.slice(0, 120), claim_id: c.id }); }
    return out;
  }
  window.axlBuildDocument = function (ids) {
    const chosen = ids.map(i => claimById[i]).filter(Boolean), skipped = chosen.filter(c => c.tier !== 'enforced' && c.tier !== 'measurable');
    const use = chosen.filter(c => c.tier === 'enforced' || c.tier === 'measurable');
    const rules = use.map(c => { const r = { id: c.id + '-' + c.verb, tier: c.tier, check: c.text.slice(0, 160), pass_criteria: c.enforcement ? c.enforcement.pass_criteria : (c.delta ? `${c.delta.property}: ${c.delta.after}` : 'see claim'), claim_ids: [c.id] }; if (c.enforcement) { r.tool = c.enforcement.tool; r.command = c.enforcement.command; } return r; });
    const cops = use.flatMap(ops).slice(0, 400);
    return { axl: '0.1', describe: { name: 'Northstar demo (web)', surface: 'web', states: ['ready', 'loading', 'empty', 'error', 'success'], viewports: ['1440x900', '375x812'] }, evaluate: { rules }, correct: { ops: cops, notes: skipped.map(c => `Skipped ${c.id}: ${c.tier}, no measurable definition.`).concat(use.filter(c => !c.css).map(c => `No mechanical patch for ${c.id}; it is checked, not applied.`)) } };
  };
  function exportIds() { const ids = new Set(st.picked); st.applied.forEach(id => { for (const d of A.definitions) for (const p of d.patterns) if (p.id === id) ids.add(p.claim_id); }); return [...ids]; }
  let lastDoc = '';
  $('#doExport').addEventListener('click', () => { const ids = exportIds(); if (!ids.length) { $('#exportMsg').textContent = 'Tick claims in the catalog or apply a check first.'; return; } const d = window.axlBuildDocument(ids); lastDoc = JSON.stringify(d, null, 2); $('#exportOut').textContent = lastDoc; $('#exportMsg').textContent = `${d.evaluate.rules.length} rules, ${d.correct.ops.length} patch operations.`; });
  $('#copyDoc').addEventListener('click', e => { if (lastDoc) copy(lastDoc, e.currentTarget); });
  $('#dlDoc').addEventListener('click', () => { if (!lastDoc) return; const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([lastDoc], { type: 'application/json' })); a.download = 'axl-document.json'; a.click(); });

  /* footer + boot */
  const m = A.metrics; $('#footNote').textContent = `${m.public_claims} public claims from ${m.sources_total} sources (${m.sources_fetched} fetched); ${A.excluded.private_kit} private-kit claims excluded; ${m.receipts} receipts, each with the exact command to re-run. Quotes are copied verbatim from pages fetched on the dates shown in the Sources drawer. No vendor endorsement is implied.`;
  renderDefn(); renderRail(); drawLineage([]); selectClaim(A.definitions[0].patterns[0].claim_id); sizeFrames();
  window.axlOpenClaim = id => { selectClaim(id); openDrawer(id); return { open: !drawer.hidden, html: $('#paneClaim').innerHTML }; };
  window.axlAllClaimIds = () => A.claims.map(c => c.id);
  window.axlReady = true;
})();
