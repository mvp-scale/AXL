import { all } from './store.js';
import { build } from './export.js';
const $ = s => document.querySelector(s), ask = (type, extra) => chrome.runtime.sendMessage(Object.assign({ type }, extra));
const esc = t => String(t).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const mb = n => (n / 1048576).toFixed(n > 10485760 ? 0 : 1) + ' MB';
async function paint() {
  const pages = (await all('pages')).sort((a, b) => a.order - b.order), assets = await all('assets');
  const bytes = assets.reduce((n, a) => n + (a.data ? a.data.byteLength : a.text ? a.text.length : 0), 0), bad = assets.filter(a => !a.ok);
  $('#site').textContent = pages.length ? new URL(pages[0].url).host : 'Nothing staged';
  $('#sum').innerHTML = `<div><b>${pages.length}</b><span class="note">pages</span></div><div><b>${assets.length - bad.length}</b><span class="note">files saved</span></div><div><b>${mb(bytes)}</b><span class="note">total</span></div>` + (bad.length ? `<div><b class="warn">${bad.length}</b><span class="note">files missing</span></div>` : '');
  const byOrigin = {}; bad.forEach(a => { const o = new URL(a.url).origin; (byOrigin[o] = byOrigin[o] || []).push(a); });
  const blocked = Object.keys(byOrigin).filter(o => byOrigin[o].some(a => a.error === 'no-permission'));
  $('#missing').hidden = !bad.length;
  $('#missing').innerHTML = bad.length ? `<h2 class="warn">${bad.length} file${bad.length === 1 ? '' : 's'} could not be saved</h2><p class="note">They will be missing offline (the copy still opens; those images or fonts fall back).${blocked.length ? ` Files from ${blocked.map(esc).join(', ')} need permission.` : ''}</p>
    ${blocked.length ? '<button class="btn" id="allow" type="button">Allow and try again</button>' : '<button class="btn" id="retry" type="button">Try again</button>'}<ul>${bad.slice(0, 8).map(a => `<li>${esc(a.url)} · ${esc(a.error === 'no-permission' ? 'needs permission' : a.error)}</li>`).join('')}${bad.length > 8 ? `<li>… and ${bad.length - 8} more</li>` : ''}</ul>` : '';
  $('#pages').innerHTML = pages.map((p, i) => `<article class="card">${p.thumb ? `<img src="${p.thumb}" alt="">` : '<span class="ph"></span>'}<div><span class="n">${i === 0 ? 'START · ' : ''}${String(i + 1).padStart(2, '0')}</span><b>${esc(p.title)}</b><small>${esc(new URL(p.url).pathname)}</small>${(p.notes || []).map(n => `<small class="warn">${esc(n)}</small>`).join('')}</div><button type="button" data-url="${esc(p.url)}">Remove</button></article>`).join('');
  $('#export').disabled = !pages.length; $('#discard').disabled = !pages.length;
  return { pages, assets, blocked };
}
$('#pages').addEventListener('click', async e => { const b = e.target.closest('button[data-url]'); if (b) { await ask('remove', { url: b.dataset.url }); paint(); } });
$('#missing').addEventListener('click', async e => {
  if (e.target.id === 'allow') { const { blocked } = await paint(); await chrome.permissions.request({ origins: blocked.map(o => o + '/*') }).catch(() => false); }
  if (e.target.id === 'allow' || e.target.id === 'retry') { $('#msg').textContent = 'Trying again…'; await ask('retry'); $('#msg').textContent = ''; paint(); }
});
$('#discard').addEventListener('click', async () => { if (confirm('Discard all staged pages?')) { await ask('clear'); paint(); } });
$('#export').addEventListener('click', async () => {
  const { pages, assets } = await paint(); $('#export').disabled = true; $('#msg').textContent = 'Building the zip…';
  try {
    const { blob, filename, manifest } = await build(pages, assets, 'AXL Capture ' + chrome.runtime.getManifest().version);
    const url = URL.createObjectURL(blob);
    const id = await chrome.downloads.download({ url, filename, saveAs: false });
    chrome.downloads.onChanged.addListener(async function done(d) {
      if (d.id !== id || !d.state) return;
      if (d.state.current === 'complete') { chrome.downloads.onChanged.removeListener(done); URL.revokeObjectURL(url); await ask('clear'); await paint();
        $('#site').textContent = 'Exported'; $('#msg').textContent = `Saved ${filename} (${manifest.pages.length} pages, ${mb(blob.size)}) to your Downloads. The staged copy was cleared.`; }
      if (d.state.current === 'interrupted') { chrome.downloads.onChanged.removeListener(done); $('#msg').textContent = 'The download was interrupted. Nothing was cleared; try again.'; $('#export').disabled = false; }
    });
    window.axlLast = { filename, manifest };
  } catch (e) { $('#msg').textContent = 'Export failed: ' + (e.message || e); $('#export').disabled = false; }
});
paint();
