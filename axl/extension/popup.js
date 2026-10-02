const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const ask = (type, extra) => chrome.runtime.sendMessage(Object.assign({ type }, extra));
let tab, origin, mode = localStorage.getItem('axl-mode') || 'record', assetOrigins = [];
const HOW = {
  record: 'Browse the site normally. Each page you open is captured once it has loaded (AXL scrolls it once so images load). Close cookie banners first. Stop when you have the pages you want.',
  page: 'Go to a page, wait until it looks right (close cookie banners, open anything you want shown), then capture it. Repeat for each page.',
};
const esc = t => String(t).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const path = u => { try { const x = new URL(u); return x.pathname + x.search; } catch (e) { return u; } };
const error = t => { $('#err').hidden = !t; $('#err').textContent = t || ''; };

async function paint() {
  const s = await ask('state');
  const other = !!(origin && s.origin && s.origin !== origin && s.pages.length);
  $('#count').textContent = s.pages.length ? `${s.pages.length} page${s.pages.length === 1 ? '' : 's'}` : '';
  $$('.seg button').forEach(b => b.setAttribute('aria-pressed', b.dataset.mode === mode));
  $('#how').textContent = HOW[mode];
  const go = $('#go'), recHere = s.recording && s.tabId === tab.id;
  go.disabled = !origin || other; go.className = 'btn ' + (recHere ? 'rec' : 'primary');
  go.textContent = mode === 'record' ? (recHere ? 'Stop recording' : 'Start recording') : 'Capture this page';
  const st = $('#status'); st.hidden = !(recHere || s.busy);
  st.innerHTML = s.busy ? '<span class="dot"></span>Capturing this page…' : recHere ? '<span class="dot"></span>Recording. Open the pages you want.' : '';
  $('#pages').innerHTML = s.pages.length ? s.pages.map(p => `<li><span>${esc(p.title)}<small>${esc(path(p.url))}</small></span><button type="button" data-url="${esc(p.url)}" aria-label="Remove ${esc(p.title)}">×</button></li>`).join('')
    : `<li class="empty">No pages yet.</li>`;
  $('#review').disabled = !s.pages.length; $('#clear').disabled = !s.pages.length;
  if (other) error(`Pages from ${s.origin} are still staged. Export or clear them before capturing another site.`);
  else if (s.missing.length) error(`${s.missing.length} file${s.missing.length === 1 ? '' : 's'} couldn't be saved yet. See Review & export.`);
  else error('');
}
(async () => {
  [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  try { const u = new URL(tab.url); if (/^https?:$/.test(u.protocol)) origin = u.origin; } catch (e) {}
  $('#origin').textContent = origin || 'Open a website to capture it';
  if (origin) {
    const ok = await chrome.permissions.contains({ origins: [origin + '/*'] });
    $('#perm').textContent = ok ? 'AXL may read this site.' : 'AXL will ask to read this site when you start.';
    // the other servers this page loads files from (fonts, images): asked for at the same time, so the copy is complete
    try { const [{ result }] = await chrome.scripting.executeScript({ target: { tabId: tab.id }, func: () => [...new Set(performance.getEntriesByType('resource').map(e => { try { return new URL(e.name).origin; } catch (x) { return null; } }).filter(o => o && /^https?:/.test(o) && o !== location.origin))] });
      assetOrigins = result || []; } catch (e) {}
  }
  await paint();
})();

$$('.seg button').forEach(b => b.addEventListener('click', () => { mode = b.dataset.mode; localStorage.setItem('axl-mode', mode); paint(); }));
$('#go').addEventListener('click', async () => {
  const s = await ask('state');
  if (mode === 'record' && s.recording && s.tabId === tab.id) { await ask('stop'); return paint(); }
  const granted = await chrome.permissions.request({ origins: [origin + '/*', ...assetOrigins.map(o => o + '/*')] }).catch(() => false);
  if (!granted && !(await chrome.permissions.contains({ origins: [origin + '/*'] }))) return error('AXL needs permission to read this site to capture it.');
  error(''); const p = ask(mode === 'record' ? 'start' : 'captureNow', { tabId: tab.id, origin });
  setTimeout(paint, 150); const r = await p; if (r && r.error) error(r.error); paint();
});
$('#pages').addEventListener('click', async e => { const b = e.target.closest('button[data-url]'); if (b) { await ask('remove', { url: b.dataset.url }); paint(); } });
$('#review').addEventListener('click', () => chrome.tabs.create({ url: chrome.runtime.getURL('review.html') }));
$('#clear').addEventListener('click', async () => { if (confirm('Remove all staged pages? This cannot be undone.')) { await ask('clear'); paint(); } });
chrome.storage.session.onChanged?.addListener(paint);
