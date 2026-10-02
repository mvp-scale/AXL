// Runs inside the page being captured (injected by the background worker). Returns a frozen copy of the page as rendered:
// the DOM after the site's scripts ran, every style rule actually in use, form state, canvas pixels, and absolute URLs for
// everything the copy needs (the background worker fetches those). Scripts are removed, so the copy never changes once saved.
(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const abs = u => { try { return new URL(u, document.baseURI).href; } catch (e) { return u; } };
  const absCss = (css, base) => css.replace(/url\(\s*(['"]?)([^'")]+)\1\s*\)/g, (m, q, u) => /^(data:|#|about:)/i.test(u.trim()) ? m : `url("${new URL(u.trim(), base).href}")`)
    .replace(/@import\s+(['"])([^'"]+)\1/g, (m, q, u) => `@import url("${new URL(u, base).href}")`);

  // 1. let the page finish: scroll through it so lazy images load, then wait for images and fonts
  const y0 = scrollY, H = () => document.documentElement.scrollHeight;
  for (let y = 0; y < H() && y < 40000; y += Math.max(200, innerHeight * 0.8)) { scrollTo(0, y); await sleep(90); }
  scrollTo(0, H()); await sleep(250); scrollTo(0, y0); await sleep(250);
  const pending = [...document.images].filter(i => !i.complete).map(i => new Promise(r => { i.addEventListener('load', r, { once: true }); i.addEventListener('error', r, { once: true }); }));
  await Promise.race([Promise.all(pending), sleep(5000)]);
  try { await Promise.race([document.fonts.ready, sleep(3000)]); } catch (e) {}

  // 2. mark originals so their clones can be found, then clone
  const all = [...document.querySelectorAll('*')]; all.forEach((el, i) => el.setAttribute('data-axl-n', i));
  const doc = document.documentElement.cloneNode(true);
  all.forEach(el => el.removeAttribute('data-axl-n'));
  const idx = new Map(all.map((el, i) => [el, i])), cl = [];
  [doc, ...doc.querySelectorAll('[data-axl-n]')].forEach(e => { const n = e.getAttribute('data-axl-n'); if (n !== null) cl[+n] = e; });
  const twin = el => cl[idx.get(el)];
  const resources = new Set(), notes = [];

  // 3. styles in document order: linked sheets by URL (fetched later), inline sheets from the live CSSOM (catches rules added by script)
  for (const sheet of document.styleSheets) {
    const node = sheet.ownerNode, c = node && twin(node); if (!c) continue;
    if (node.tagName === 'LINK') { const href = abs(node.getAttribute('href')); c.setAttribute('href', href); resources.add(href); continue; }
    let text = node.textContent;
    try { const live = [...sheet.cssRules].map(r => r.cssText).join('\n'); if (live.length > text.length || !text.trim()) text = live; } catch (e) {}
    c.textContent = absCss(text, document.baseURI);
  }
  if (document.adoptedStyleSheets && document.adoptedStyleSheets.length) {
    const s = document.createElement('style'); s.setAttribute('data-axl-adopted', '');
    s.textContent = document.adoptedStyleSheets.map(sh => { try { return [...sh.cssRules].map(r => r.cssText).join('\n'); } catch (e) { return ''; } }).join('\n');
    doc.querySelector('head').appendChild(s);
  }
  doc.querySelectorAll('link').forEach(l => { const rel = (l.getAttribute('rel') || '').toLowerCase();
    if (/(^|\s)(preload|prefetch|modulepreload|preconnect|dns-prefetch|manifest|alternate|canonical)(\s|$)/.test(rel) && !/stylesheet/.test(rel)) l.remove();
    else if (/icon/.test(rel)) { const h = abs(l.getAttribute('href')); l.setAttribute('href', h); resources.add(h); } });

  // 4. images as shown: the source the browser actually picked, no lazy loading
  for (const img of document.images) {
    const c = twin(img); if (!c) continue; const src = img.currentSrc || img.src;
    if (src) { c.setAttribute('src', src); resources.add(src); }
    c.removeAttribute('srcset'); c.removeAttribute('sizes'); c.removeAttribute('loading');
  }
  doc.querySelectorAll('picture source').forEach(s => s.remove());
  doc.querySelectorAll('video').forEach(v => { const p = v.getAttribute('poster'); if (p) { v.setAttribute('poster', abs(p)); resources.add(abs(p)); } v.removeAttribute('src'); v.querySelectorAll('source').forEach(s => s.remove()); v.removeAttribute('autoplay'); });
  doc.querySelectorAll('svg image, svg use').forEach(el => ['href', 'xlink:href'].forEach(a => { const v = el.getAttribute(a); if (v && !v.startsWith('#')) { el.setAttribute(a, abs(v)); resources.add(abs(v)); } }));

  // 5. inline style attributes with url()
  doc.querySelectorAll('[style*="url("]').forEach(el => el.setAttribute('style', absCss(el.getAttribute('style'), document.baseURI)));

  // 6. state the person can see: form values, canvas pixels; embedded frames become labelled placeholders
  for (const el of document.querySelectorAll('input, textarea, select')) {
    const c = twin(el); if (!c) continue;
    if (el.tagName === 'TEXTAREA') c.textContent = el.value;
    else if (el.tagName === 'SELECT') [...el.options].forEach((o, i) => { const co = c.options && c.options[i]; if (co) o.selected ? co.setAttribute('selected', '') : co.removeAttribute('selected'); });
    else if (/checkbox|radio/i.test(el.type)) el.checked ? c.setAttribute('checked', '') : c.removeAttribute('checked');
    else if (!/password|file|hidden/i.test(el.type)) c.setAttribute('value', el.value);
  }
  for (const cv of document.querySelectorAll('canvas')) {   // a still of the drawing; the image keeps the canvas's own size rules (width/height, class, style)
    const c = twin(cv); if (!c) continue;
    try { const im = document.createElement('img'); im.src = cv.toDataURL(); for (const at of c.attributes) if (at.name !== 'src') im.setAttribute(at.name, at.value); c.replaceWith(im); } catch (e) { notes.push('A drawing (canvas) from another site could not be copied.'); }
  }
  for (const fr of document.querySelectorAll('iframe, embed, object')) {
    const c = twin(fr); if (!c) continue; const r = fr.getBoundingClientRect(), cs = getComputedStyle(fr);
    const ph = document.createElement('div'); ph.setAttribute('data-axl-embed', abs(fr.getAttribute('src') || fr.getAttribute('data') || ''));
    ph.setAttribute('style', `display:${cs.display === 'inline' ? 'inline-block' : cs.display};width:${r.width}px;max-width:100%;height:${r.height}px;background:#eceef1;border-radius:${cs.borderRadius};color:#5b5d66;font:13px/1.3 system-ui,sans-serif;display:grid;place-items:center;text-align:center`);
    ph.textContent = r.width > 40 && r.height > 24 ? 'Embedded content (not captured)' : ''; c.replaceWith(ph);
  }
  if ([...document.querySelectorAll('*')].some(el => el.shadowRoot)) notes.push('Some parts of this page are built inside components (shadow DOM) and may be missing from the copy.');

  // 7. links: absolute, so the export can point captured pages at each other
  const links = new Set();
  doc.querySelectorAll('a[href]').forEach(a => { const h = a.getAttribute('href'); if (/^(javascript:|mailto:|tel:|#)/i.test(h)) return; const u = abs(h); a.setAttribute('href', u); try { if (new URL(u).origin === location.origin) links.add(u.split('#')[0]); } catch (e) {} });

  // 8. nothing in the copy may run or reload: drop scripts, CSP/refresh/base tags and event handlers
  doc.querySelectorAll('script, noscript, base, meta[http-equiv], #axl-capture-toast').forEach(n => n.remove());
  doc.removeAttribute('data-axl-n');
  doc.querySelectorAll('*').forEach(el => { el.removeAttribute('data-axl-n'); for (const a of [...el.attributes]) if (/^on/i.test(a.name)) el.removeAttribute(a.name); });
  const html = '<!doctype html>\n' + doc.outerHTML;
  return { url: location.href.split('#')[0], title: document.title || location.pathname, html, resources: [...resources].filter(u => /^https?:/.test(u)), links: [...links],
           width: innerWidth, height: innerHeight, notes, capturedAt: new Date().toISOString() };
})();
