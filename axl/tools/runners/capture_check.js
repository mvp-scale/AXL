// Loads the AXL Capture extension into Chromium, records pages on a real site, exports the zip, and compares the offline copy
// with the live page at desktop, tablet and mobile widths (share of pixels that differ).
// usage: node capture_check.js <outdir> <url> [<url> ...]     (first URL starts recording; the rest are visited in order)
const fs = require('fs'), path = require('path'), os = require('os'), { execFileSync } = require('child_process');
const { chromium } = require('playwright'); const { CHROME } = require('./common');
const EXT = path.resolve(__dirname, '../../extension');
(async () => {
  const [out, ...urls] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
  // test copy: host access granted up front (the real extension asks per site)
  const ext = fs.mkdtempSync(path.join(os.tmpdir(), 'axl-ext-')); fs.cpSync(EXT, ext, { recursive: true });
  const m = JSON.parse(fs.readFileSync(path.join(ext, 'manifest.json'))); m.host_permissions = ['<all_urls>']; fs.writeFileSync(path.join(ext, 'manifest.json'), JSON.stringify(m));
  const ctx = await chromium.launchPersistentContext(fs.mkdtempSync(path.join(os.tmpdir(), 'axl-prof-')), { executablePath: CHROME, headless: true, ignoreHTTPSErrors: true,
    viewport: { width: 1280, height: 860 }, args: ['--no-sandbox', `--disable-extensions-except=${ext}`, `--load-extension=${ext}`, '--ignore-certificate-errors'] });
  let sw = ctx.serviceWorkers()[0] || await ctx.waitForEvent('serviceworker'); const id = sw.url().split('/')[2];
  const page = ctx.pages()[0] || await ctx.newPage(); const errors = []; page.on('pageerror', e => errors.push(String(e)));
  await page.goto(urls[0], { waitUntil: 'load', timeout: 60000 });
  const tabId = await sw.evaluate(async u => (await chrome.tabs.query({})).find(t => t.url && t.url.startsWith(u.split('#')[0].slice(0, 30))).id, urls[0]);
  const t0 = Date.now(); const r0 = await sw.evaluate(async ([tabId, origin]) => self.axl.start({ tabId, origin }), [tabId, new URL(urls[0]).origin]);
  console.log('start + first capture', r0, Math.round((Date.now() - t0) / 1000) + 's');
  for (const u of urls.slice(1)) {   // recording: just browse
    const before = (await sw.evaluate(() => self.axl.state())).pages.length;
    await page.goto(u, { waitUntil: 'load', timeout: 60000 });
    for (let i = 0; i < 60; i++) { await page.waitForTimeout(1000); const s = await sw.evaluate(() => self.axl.state()); if (s.pages.length > before && !s.busy) break; }
  }
  const st = await sw.evaluate(() => self.axl.state());
  console.log('recorded pages:', st.pages.map(p => p.title), 'files saved:', st.files, 'missing:', st.missing.length, st.missing.slice(0, 3));
  // the extension's own screens
  const pop = await ctx.newPage(); await pop.setViewportSize({ width: 360, height: 620 }); await pop.goto(`chrome-extension://${id}/popup.html`); await pop.waitForTimeout(800);
  await pop.screenshot({ path: path.join(out, 'popup.png'), fullPage: true });
  const rev = await ctx.newPage(); await rev.goto(`chrome-extension://${id}/review.html`); await rev.waitForTimeout(1200);
  await rev.screenshot({ path: path.join(out, 'review.png'), fullPage: false });
  // export (same code as the Export button) and unzip
  const b64 = await rev.evaluate(async () => { const { all } = await import('./store.js'); const { build } = await import('./export.js');
    const { blob, filename } = await build(await all('pages'), await all('assets'), 'test'); const buf = new Uint8Array(await blob.arrayBuffer());
    let s = ''; for (let i = 0; i < buf.length; i += 32768) s += String.fromCharCode(...buf.subarray(i, i + 32768)); return { filename, data: btoa(s) }; });
  const zipPath = path.join(out, b64.filename); fs.writeFileSync(zipPath, Buffer.from(b64.data, 'base64'));
  const dir = path.join(out, 'unzipped'); fs.rmSync(dir, { recursive: true, force: true }); execFileSync('python3', ['-m', 'zipfile', '-e', zipPath, dir]);
  const man = JSON.parse(fs.readFileSync(path.join(dir, 'manifest.json')));
  console.log('zip:', b64.filename, (fs.statSync(zipPath).size / 1048576).toFixed(1) + ' MB', 'pages:', man.pages.length, 'assets saved:', man.assets.saved, 'missing:', man.assets.missing.length);
  // fidelity: live vs offline copy, same viewport; offline browser has no network at all
  const off = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
  const diff = await off.newPage();
  const W = { desktop: [1280, 860], tablet: [820, 1180], mobile: [390, 844] }, rows = [];
  for (const p of man.pages) for (const [dev, [w, h]] of Object.entries(W)) {
    const live = await ctx.newPage(); await live.setViewportSize({ width: w, height: h }); await live.goto(p.url, { waitUntil: 'load', timeout: 60000 }); await live.waitForTimeout(800);
    const a = await live.screenshot(); await live.close();
    const oc = await off.newContext({ viewport: { width: w, height: h }, offline: true }); const o = await oc.newPage(); let blocked = 0;
    await o.route('**/*', r => { if (r.request().url().startsWith('file:')) r.continue(); else { blocked++; r.abort(); } });
    await o.goto('file://' + path.join(dir, p.file)); await o.waitForTimeout(800); const bshot = await o.screenshot(); await oc.close();
    fs.writeFileSync(path.join(out, `${path.basename(p.file, '.html')}-${dev}-live.png`), a); fs.writeFileSync(path.join(out, `${path.basename(p.file, '.html')}-${dev}-offline.png`), bshot);
    const pct = await diff.evaluate(async ([x, y]) => { const load = s => new Promise(r => { const i = new Image(); i.onload = () => r(i); i.src = 'data:image/png;base64,' + s; });
      const [A, B] = await Promise.all([load(x), load(y)]); const c = new OffscreenCanvas(A.width, A.height), g = c.getContext('2d');
      g.drawImage(A, 0, 0); const da = g.getImageData(0, 0, A.width, A.height).data; g.clearRect(0, 0, A.width, A.height); g.drawImage(B, 0, 0); const db = g.getImageData(0, 0, A.width, A.height).data;
      let n = 0; for (let i = 0; i < da.length; i += 4) if (Math.abs(da[i] - db[i]) + Math.abs(da[i + 1] - db[i + 1]) + Math.abs(da[i + 2] - db[i + 2]) > 48) n++; return 100 * n / (da.length / 4); }, [a.toString('base64'), bshot.toString('base64')]);
    rows.push({ page: p.title.slice(0, 40), dev, differs: pct.toFixed(1) + '%', live_requests_blocked: blocked });
  }
  // the real Export button: downloads the zip, then clears the staged copy
  await rev.bringToFront(); await rev.click('#export');
  await rev.waitForFunction(() => /Saved|failed|interrupted/.test(document.getElementById('msg').textContent), null, { timeout: 60000 }).catch(() => {});
  const after = await sw.evaluate(() => self.axl.state());
  console.log('export button:', await rev.textContent('#msg'), '| staged pages after export:', after.pages.length);
  console.table(rows); fs.writeFileSync(path.join(out, 'fidelity.json'), JSON.stringify({ rows, manifest: man, errors }, null, 1));
  await off.close(); await ctx.close();
})().catch(e => { console.error(e); process.exit(1); });
