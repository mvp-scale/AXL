// AXL Capture background worker: records pages as the person browses (or one at a time), fetches the files each page needs,
// and keeps everything staged locally until the review page exports one zip.
import { put, get, del, all, keys, clear } from './store.js';

const session = { get: async () => (await chrome.storage.session.get('s')).s || {}, set: async v => chrome.storage.session.set({ s: Object.assign(await session.get(), v) }) };
const timers = {};
const PINK = '#d1175e', REC = '#c62828';

async function badge() {
  const s = await session.get(), n = (await keys('pages')).length;
  await chrome.action.setBadgeBackgroundColor({ color: s.recording ? REC : PINK });
  await chrome.action.setBadgeText({ text: s.recording ? (n ? String(n) : 'REC') : (n ? String(n) : '') });
}

// fetch every file a page needs; stylesheets are read for the fonts and images they point to (and @import), three levels deep
const isCss = (u, type) => /text\/css/i.test(type || '') || /\.css(\?|$)/i.test(u);
const cssUrls = (css, base) => { const out = []; css.replace(/url\(\s*(['"]?)([^'")]+)\1\s*\)/g, (m, q, u) => { u = u.trim(); if (!/^(data:|#|about:)/i.test(u)) try { out.push(new URL(u, base).href); } catch (e) {} });
  css.replace(/@import\s+(['"])([^'"]+)\1/g, (m, q, u) => { try { out.push(new URL(u, base).href); } catch (e) {} }); return out; };
const absCss = (css, base) => css.replace(/url\(\s*(['"]?)([^'")]+)\1\s*\)/g, (m, q, u) => /^(data:|#|about:)/i.test(u.trim()) ? m : `url("${new URL(u.trim(), base).href}")`)
  .replace(/@import\s+(['"])([^'"]+)\1/g, (m, q, u) => `@import url("${new URL(u, base).href}")`);
async function fetchAll(urls, depth = 0) {
  const todo = [...new Set(urls)].filter(u => /^https?:/.test(u));
  const have = new Set(await keys('assets')); const next = [];
  const queue = todo.filter(u => !have.has(u));
  const work = async u => {
    try {
      const r = await fetch(u, { credentials: 'include' });
      if (!r.ok) throw new Error('HTTP ' + r.status);
      const type = r.headers.get('content-type') || '';
      if (isCss(u, type)) { const text = absCss(await r.text(), u); next.push(...cssUrls(text, u)); await put('assets', { url: u, type: 'text/css', text, ok: true }); }
      else await put('assets', { url: u, type, data: await r.arrayBuffer(), ok: true });
    } catch (e) {
      const permitted = await chrome.permissions.contains({ origins: [new URL(u).origin + '/*'] });
      await put('assets', { url: u, ok: false, error: permitted ? String(e.message || e) : 'no-permission' });
    }
  };
  for (let i = 0; i < queue.length; i += 6) await Promise.all(queue.slice(i, i + 6).map(work));
  if (next.length && depth < 3) await fetchAll(next, depth + 1);
}

async function toast(tabId, text) {
  try { await chrome.scripting.executeScript({ target: { tabId }, args: [text], func: t => {
    const id = 'axl-capture-toast'; document.getElementById(id)?.remove();
    const d = document.createElement('div'); d.id = id; d.textContent = t; d.setAttribute('role', 'status');
    d.style.cssText = 'all:initial;position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:2147483647;background:#131316;color:#fff;font:600 14px/1.3 "Inter Tight","Helvetica Neue",Arial,system-ui,sans-serif;padding:12px 18px 12px 14px;border-radius:99px;box-shadow:0 8px 24px rgba(0,0,0,.3);display:flex;gap:10px;align-items:center;transition:opacity .4s';
    const dot = document.createElement('span'); dot.style.cssText = 'all:initial;width:12px;height:12px;border-radius:3px;background:#d1175e;flex:none'; d.prepend(dot);
    document.documentElement.appendChild(d); setTimeout(() => { d.style.opacity = '0'; setTimeout(() => d.remove(), 450); }, 2200);
  } }); } catch (e) {}
}

async function capture(tabId) {
  const s = await session.get(), tab = await chrome.tabs.get(tabId);
  if (!s.origin || !tab.url || new URL(tab.url).origin !== s.origin) return { skipped: 'This tab is not on ' + (s.origin || 'the site being captured') };
  await session.set({ busy: tab.url });
  await toast(tabId, 'AXL is capturing this page… (it scrolls once to load images)');
  let snap;
  try { [{ result: snap }] = await chrome.scripting.executeScript({ target: { tabId }, files: ['snapshot.js'] }); }
  catch (e) { await session.set({ busy: null }); return { error: String(e.message || e) }; }
  let thumb = null; try { if (tab.active) thumb = await chrome.tabs.captureVisibleTab(tab.windowId, { format: 'jpeg', quality: 55 }); } catch (e) {}
  const prev = await get('pages', snap.url), order = prev ? prev.order : (s.order || 0) + 1;
  await put('pages', Object.assign(snap, { order, thumb }));
  if (!prev) await session.set({ order });
  await fetchAll(snap.resources);
  await session.set({ busy: null }); await badge();
  const n = (await keys('pages')).length;
  await toast(tabId, `AXL saved this page · ${n} page${n === 1 ? '' : 's'} captured`);
  return { ok: true, url: snap.url, pages: n };
}
const schedule = (tabId, ms) => { clearTimeout(timers[tabId]); timers[tabId] = setTimeout(() => capture(tabId), ms); };

chrome.tabs.onUpdated.addListener(async (tabId, info, tab) => {
  const s = await session.get(); if (!s.recording || s.tabId !== tabId) return;
  if (info.status === 'complete') schedule(tabId, 1500);                 // a full page load
  else if (info.url && !info.status) schedule(tabId, 2500);              // an in-page navigation (single-page apps)
});
chrome.tabs.onRemoved.addListener(async tabId => { const s = await session.get(); if (s.tabId === tabId) { await session.set({ recording: false }); await badge(); } });

async function state() {
  const s = await session.get(), pages = (await all('pages')).sort((a, b) => a.order - b.order).map(p => ({ url: p.url, title: p.title, order: p.order }));
  const assets = await all('assets'), missing = assets.filter(a => !a.ok);
  return { origin: s.origin || null, recording: !!s.recording, tabId: s.tabId, busy: s.busy || null, pages, files: assets.length - missing.length, missing: missing.map(a => ({ url: a.url, error: a.error })) };
}

const handlers = {
  state,
  async start({ tabId, origin }) {
    const s = await session.get();
    if (s.origin && s.origin !== origin && (await keys('pages')).length) return { error: `Pages from ${s.origin} are still staged. Export or clear them first.` };
    await session.set({ origin, recording: true, tabId }); await badge(); return capture(tabId);
  },
  async stop() { await session.set({ recording: false }); await badge(); return state(); },
  async captureNow({ tabId, origin }) {
    const s = await session.get();
    if (s.origin && s.origin !== origin && (await keys('pages')).length) return { error: `Pages from ${s.origin} are still staged. Export or clear them first.` };
    await session.set({ origin }); return capture(tabId);
  },
  async remove({ url }) { await del('pages', url); await badge(); return state(); },
  async retry() { const bad = (await all('assets')).filter(a => !a.ok); for (const a of bad) await del('assets', a.url); await fetchAll(bad.map(a => a.url)); return state(); },
  async clear() { await clear(); await chrome.storage.session.set({ s: {} }); await badge(); return state(); },
};
chrome.runtime.onMessage.addListener((m, sender, reply) => { (handlers[m.type] || (async () => ({ error: 'unknown request' })))(m).then(reply, e => reply({ error: String(e.message || e) })); return true; });
chrome.runtime.onStartup?.addListener(badge); chrome.runtime.onInstalled.addListener(badge);
self.axl = handlers;   // for automated tests
