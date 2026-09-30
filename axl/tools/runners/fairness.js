// Fairness audit: does applying a definition's previews make the Northstar page objectively worse?
// usage: node fairness.js <jobs.json> -> JSON [{key, view, device, base:{...}, after:{...}, worse:[...]}]
// jobs.json = [{key, view, css, patch}]; each job runs on desktop 1280x800, tablet 820x1180, mobile 390x844.
// Harm = more of any of: horizontal overflow, elements off-screen, overlapping text, clipped text, text under 11px, contrast failures (axe).
const fs = require('fs'), path = require('path'); const { chromium } = require('playwright'); const { CHROME } = require('./common');
const AXE = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const DEV = { desktop: [1280, 800], tablet: [820, 1180], mobile: [390, 844] };
const MEASURE = async () => {
  const panel = [...document.querySelectorAll('.panel')].find(p => !p.hidden) || document.body, W = innerWidth;
  const vis = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && e.checkVisibility({ contentVisibilityAuto: true, opacityProperty: true, visibilityProperty: true }); };
  const overlay = e => { for (let a = e; a && a !== document.body; a = a.parentElement) if (/(fixed|sticky)/.test(getComputedStyle(a).position)) return true; return false; };   // banners and toasts sit over content by design
  const els = [...panel.querySelectorAll('*')].filter(vis);
  const ownText = e => !(e.tagName === 'DETAILS' && !e.open) && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());   // a closed disclosure's own text is hidden
  const texts = els.filter(e => ownText(e) && !overlay(e));
  // the visible part of each text box: clipped by any scrolling/clipping ancestor (content scrolled out of view doesn't count)
  const clip = (e, r) => { let x = { l: r.left, t: r.top, r: r.right, b: r.bottom }; for (let a = e.parentElement; a && a !== document.body; a = a.parentElement) { const c = getComputedStyle(a); if (/(hidden|auto|scroll|clip)/.test(c.overflowX + c.overflowY)) { const q = a.getBoundingClientRect(); x = { l: Math.max(x.l, q.left), t: Math.max(x.t, q.top), r: Math.min(x.r, q.right), b: Math.min(x.b, q.bottom) }; } } return x; };
  let overlap = 0; const boxes = texts.map(e => { const rg = document.createRange(); rg.selectNodeContents(e); const q = clip(e, rg.getBoundingClientRect()); return { e, r: { left: q.l, top: q.t, right: q.r, bottom: q.b, width: q.r - q.l, height: q.b - q.t } }; }).filter(b => b.r.width > 2 && b.r.height > 2);
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
    const a = boxes[i], b = boxes[j]; if (a.e.contains(b.e) || b.e.contains(a.e)) continue;
    const x = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left), y = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
    if (x > 3 && y > 3) overlap++;
  }
  const clipped = texts.filter(e => { const c = getComputedStyle(e); return (/(hidden|clip)/.test(c.overflowX + c.overflowY) || c.textOverflow === 'ellipsis') && (e.scrollWidth > e.clientWidth + 2 || e.scrollHeight > e.clientHeight + 2); }).length;
  const offscreen = els.filter(e => { const q = clip(e, e.getBoundingClientRect()); return q.r > q.l && (q.r > W + 2 || q.l < -2); }).filter(e => !e.closest('[aria-hidden=true]')).length;
  const tiny = texts.filter(e => parseFloat(getComputedStyle(e).fontSize) < 11).length;
  let contrast = 0; try { const r = await axe.run(panel, { runOnly: ['color-contrast'] }); contrast = r.violations.reduce((n, v) => n + v.nodes.length, 0); } catch (e) {}
  return { hscroll: document.documentElement.scrollWidth > W + 1 ? 1 : 0, offscreen, overlap, clipped, tiny, contrast };
};
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')); const demo = 'file://' + path.resolve(__dirname, '../../demo/northstar.html');
  const b = await chromium.launch({ executablePath: CHROME }); const out = []; const base = {};
  for (const [dev, [w, h]] of Object.entries(DEV)) {
    const p = await (await b.newContext({ viewport: { width: w, height: h } })).newPage(); await p.goto(demo); await p.addScriptTag({ content: AXE });
    await p.addStyleTag({ content: '*,*::before,*::after{animation:none!important;transition:none!important}' });
    const run = async (view, css, patch) => p.evaluate(async ({ view, css, patch, M }) => {
      st = { ...st, view, modal: null, phase: 'ready', menu: false, drawer: false, siErr: '' }; draw();
      document.querySelector('#recipe-style').textContent = css || ''; axlPatch(patch || []); await new Promise(r => setTimeout(r, 30));
      const m = await (new Function('return (' + M + ')'))()(); document.querySelector('#recipe-style').textContent = ''; axlPatch([]); return m;
    }, { view, css, patch, M: MEASURE.toString() });
    for (const j of jobs) {
      if (j.device && j.device !== dev) continue;
      const k = j.view + dev; if (!base[k]) base[k] = await run(j.view, '', []);
      const a = await run(j.view, j.css, j.patch);
      const worse = Object.keys(a).filter(m => a[m] > base[k][m]);
      out.push({ key: j.key, view: j.view, device: dev, base: base[k], after: a, worse });
    }
  }
  console.log(JSON.stringify(out)); await b.close();
})();
