// Turn staged pages + files into one package: pages/ (linked to each other), assets/ (each file once), manifest.json, index.html.
import { zip } from './zip.js';
const EXT = { 'image/png': 'png', 'image/jpeg': 'jpg', 'image/gif': 'gif', 'image/svg+xml': 'svg', 'image/webp': 'webp', 'image/avif': 'avif', 'image/x-icon': 'ico', 'image/vnd.microsoft.icon': 'ico',
  'font/woff2': 'woff2', 'font/woff': 'woff', 'font/ttf': 'ttf', 'font/otf': 'otf', 'application/font-woff2': 'woff2', 'application/font-woff': 'woff', 'text/css': 'css' };
const hex = async s => [...new Uint8Array(await crypto.subtle.digest('SHA-1', new TextEncoder().encode(s)))].map(b => b.toString(16).padStart(2, '0')).join('');
const extOf = a => EXT[(a.type || '').split(';')[0].trim().toLowerCase()] || ((new URL(a.url).pathname.match(/\.([a-z0-9]{2,5})$/i) || [])[1] || 'bin').toLowerCase();
const key = u => { try { const x = new URL(u); x.hash = ''; if (x.pathname.length > 1) x.pathname = x.pathname.replace(/\/+$/, ''); return x.href; } catch (e) { return u; } };
const slug = u => { const p = new URL(u).pathname.replace(/\/+$/, '').split('/').filter(Boolean).pop() || 'home'; return p.replace(/\.[a-z0-9]+$/i, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40) || 'page'; };
const esc = t => String(t).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

export async function build(pages, assets, tool) {
  pages = [...pages].sort((a, b) => a.order - b.order);
  const ok = assets.filter(a => a.ok), name = {};
  for (const a of ok) name[a.url] = (await hex(a.url)).slice(0, 12) + '.' + extOf(a);
  const swapCss = (css, prefix) => css.replace(/url\(\s*(['"]?)([^'")]+)\1\s*\)/g, (m, q, u) => { const [base, frag] = u.split('#'); return name[base] ? `url("${prefix}${name[base]}${frag ? '#' + frag : ''}")` : m; });
  const files = [];
  for (const a of ok) files.push(a.type === 'text/css' ? { name: 'assets/' + name[a.url], data: swapCss(a.text, ''), compress: true } : { name: 'assets/' + name[a.url], data: new Uint8Array(a.data), compress: /svg|json|text|javascript/.test(a.type || '') });
  const file = {}, used = new Set();
  pages.forEach((p, i) => { let f = `${String(i + 1).padStart(2, '0')}-${slug(p.url)}.html`; while (used.has(f)) f = f.replace(/\.html$/, '-x.html'); used.add(f); file[key(p.url)] = f; });
  const manifest = { format: 'axl-capture', version: 1, tool, site: new URL(pages[0].url).origin, exported_at: new Date().toISOString(), start: 'pages/' + file[key(pages[0].url)], pages: [],
    assets: { saved: ok.length, bytes: files.reduce((n, f) => n + (typeof f.data === 'string' ? f.data.length : f.data.byteLength), 0), missing: assets.filter(a => !a.ok).map(a => ({ url: a.url, reason: a.error })) } };
  for (const p of pages) {
    const d = new DOMParser().parseFromString(p.html, 'text/html'), here = file[key(p.url)], links = new Set();
    const swap = (el, attr) => { const v = el.getAttribute(attr); if (!v) return; const [base, frag] = v.split('#'); if (name[base]) el.setAttribute(attr, '../assets/' + name[base] + (frag ? '#' + frag : '')); };
    d.querySelectorAll('link[href]').forEach(el => swap(el, 'href'));
    d.querySelectorAll('img[src]').forEach(el => swap(el, 'src'));
    d.querySelectorAll('video[poster]').forEach(el => swap(el, 'poster'));
    d.querySelectorAll('image, use').forEach(el => { swap(el, 'href'); swap(el, 'xlink:href'); });
    d.querySelectorAll('[style*="url("]').forEach(el => el.setAttribute('style', swapCss(el.getAttribute('style'), '../assets/')));
    d.querySelectorAll('style').forEach(el => { el.textContent = swapCss(el.textContent, '../assets/'); });
    d.querySelectorAll('a[href]').forEach(a => { const h = a.getAttribute('href'); if (!/^https?:/.test(h)) return;
      const f = file[key(h)], frag = h.includes('#') ? '#' + h.split('#')[1] : '';
      if (f) { a.setAttribute('href', f + frag); links.add('pages/' + f); }
      else { a.setAttribute('href', '#not-captured'); a.setAttribute('data-axl-href', h); a.setAttribute('data-axl-not-captured', ''); if (!a.title) a.title = 'Not captured'; } });
    const meta = d.createElement('meta'); meta.name = 'axl-capture'; meta.content = `${p.url} · captured ${p.capturedAt}`; d.head.prepend(meta);
    const cs = d.createElement('meta'); cs.setAttribute('charset', 'utf-8'); d.head.prepend(cs);
    const st = d.createElement('style'); st.setAttribute('data-axl-capture', ''); st.textContent = 'a[data-axl-not-captured]{cursor:not-allowed}'; d.head.appendChild(st);
    files.push({ name: 'pages/' + here, data: '<!doctype html>\n' + d.documentElement.outerHTML, compress: true });
    if (p.thumb) { const b = Uint8Array.from(atob(p.thumb.split(',')[1]), c => c.charCodeAt(0)); files.push({ name: 'thumbs/' + here.replace(/\.html$/, '.jpg'), data: b }); }
    manifest.pages.push({ file: 'pages/' + here, url: p.url, title: p.title, captured_at: p.capturedAt, viewport: { width: p.width, height: p.height }, thumb: p.thumb ? 'thumbs/' + here.replace(/\.html$/, '.jpg') : null, links: [...links], notes: p.notes || [] });
  }
  const host = new URL(manifest.site).host;
  files.push({ name: 'manifest.json', data: JSON.stringify(manifest, null, 1), compress: true });
  files.push({ name: 'index.html', compress: true, data: `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AXL capture · ${esc(host)}</title>
<style>body{margin:0;background:#f7f7f5;color:#131316;font:15px/1.45 "Inter Tight","Helvetica Neue",Arial,system-ui,sans-serif}main{max-width:760px;margin:0 auto;padding:40px 20px}
.k{font:700 .7rem ui-monospace,Menlo,monospace;letter-spacing:.1em;text-transform:uppercase;color:#5b5d66}h1{font-size:2rem;letter-spacing:-.03em;margin:.2em 0}
ol{list-style:none;padding:0;display:grid;gap:10px}a{display:flex;gap:14px;align-items:center;padding:10px;border-radius:14px;background:#fff;box-shadow:0 0 0 1px #dfe0e4;color:inherit;text-decoration:none}a:hover{box-shadow:0 0 0 2px #d1175e}
img{width:120px;height:72px;object-fit:cover;object-position:top;border-radius:8px;background:#eeeff1}small{display:block;color:#5b5d66;font:.78rem ui-monospace,Menlo,monospace}</style></head>
<body><main><span class="k">AXL capture</span><h1>${esc(host)}</h1><p>${pages.length} pages captured ${esc(manifest.exported_at.slice(0, 10))}. Open this package in AXL to try sources and commands on it, or open a page below.</p>
<ol>${manifest.pages.map(p => `<li><a href="${esc(p.file)}">${p.thumb ? `<img src="${esc(p.thumb)}" alt="">` : ''}<span>${esc(p.title)}<small>${esc(new URL(p.url).pathname)}</small></span></a></li>`).join('')}</ol></main></body></html>` });
  return { blob: await zip(files), manifest, filename: `axl-capture-${host}-${manifest.exported_at.slice(0, 10)}.zip` };
}
