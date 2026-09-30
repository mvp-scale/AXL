// usage: node pins.js <outdir>  -> writes <outdir>/pins.json and before/after element crops (PNG) for the site's annotated stage.
// Every number is measured from the rendered pages (computed style / bounding box), never typed.
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const { CHROME } = require('./common');
const out = path.resolve(process.argv[2]); fs.mkdirSync(out, { recursive: true });
const DEMO = path.resolve(__dirname, '../../demo');
const SPECS = [
  { id: 'contrast', pattern: 'readable-contrast', title: 'Faint text made readable', sel: 'thead th', measure: 'contrast', unit: ':1' },
  { id: 'targets', pattern: 'reachable-targets', title: 'Buttons big enough to tap', sel: 'button.row-action', measure: 'size', unit: 'px' },
  { id: 'spacing', pattern: 'on-grid-spacing', title: 'Gaps snapped to a 4px scale', sel: 'nav.app-nav', measure: 'css:rowGap', unit: 'px' },
  { id: 'type', pattern: 'text-size-floor', title: 'Small print no smaller than 14px', sel: '.activity li', measure: 'css:fontSize', unit: 'px' },
  { id: 'focus', pattern: 'visible-focus', title: 'Keyboard focus you can see', sel: 'button.primary', measure: 'focus', unit: '' },
];
const lum = (r, g, b) => { const v = [r, g, b].map(x => x / 255).map(x => x <= 0.03928 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4); return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]; };
const rgb = s => s.match(/[\d.]+/g).slice(0, 3).map(Number);
const ratio = (a, b) => { const [x, y] = [lum(...a), lum(...b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };
async function bgOf(el) { return el.evaluate(e => { let n = e; while (n) { const c = getComputedStyle(n).backgroundColor; if (c && !/rgba\(0, 0, 0, 0\)|transparent/.test(c)) return c; n = n.parentElement; } return 'rgb(255,255,255)'; }); }
async function measure(page, spec) {
  const el = page.locator(spec.sel).first(); await el.scrollIntoViewIfNeeded();
  const box = await el.boundingBox();
  let value;
  if (spec.measure === 'contrast') { const fg = await el.evaluate(e => getComputedStyle(e).color); value = ratio(rgb(fg), rgb(await bgOf(el))).toFixed(2); }
  else if (spec.measure === 'size') value = Math.round(box.width) + '×' + Math.round(box.height);
  else if (spec.measure.startsWith('css:')) value = parseFloat(await el.evaluate((e, p) => getComputedStyle(e)[p], spec.measure.slice(4))).toString();
  else if (spec.measure === 'focus') { await page.keyboard.press('Tab'); await page.locator(spec.sel).first().focus(); await page.keyboard.press('Shift+Tab'); await page.keyboard.press('Tab'); value = await el.evaluate(e => { const s = getComputedStyle(e); return s.outlineStyle === 'none' || parseFloat(s.outlineWidth) === 0 ? 'none' : parseFloat(s.outlineWidth) + 'px ring'; }); }
  return { value, box };
}
(async () => {
  const b = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
  const pins = [];
  const shots = {};
  for (const variant of ['before', 'polished']) {
    const ctx = await b.newContext({ viewport: { width: 980, height: 660 }, deviceScaleFactor: 2 }); const page = await ctx.newPage();
    await page.goto('file://' + path.join(DEMO, variant + '.html')); await page.waitForTimeout(300);
    for (const s of SPECS) {
      const m = await measure(page, s); (shots[s.id] = shots[s.id] || {})[variant] = m;
      const el = page.locator(s.sel).first(); const pad = s.id === 'spacing' ? 0 : 14; const bx = m.box;
      const clip = s.id === 'spacing' ? { x: 0, y: Math.max(0, bx.y), width: Math.min(bx.width + 40, 220), height: Math.min(bx.height, 300) } : { x: Math.max(0, bx.x - pad), y: Math.max(0, bx.y - pad), width: Math.min(bx.width + pad * 2, 520), height: Math.min(bx.height + pad * 2, 160) };
      await page.screenshot({ path: path.join(out, `pin-${s.id}-${variant === 'before' ? 'before' : 'after'}.png`), clip, animations: 'disabled' });
    }
    await ctx.close();
  }
  for (const s of SPECS) { const a = shots[s.id]; pins.push({ id: s.id, pattern: s.pattern, title: s.title, unit: s.unit, before: a.before.value, after: a.polished.value, rect: a.before.box, rectAfter: a.polished.box }); }
  await b.close();
  fs.writeFileSync(path.join(out, 'pins.json'), JSON.stringify({ frame: { width: 980, height: 660 }, pins }, null, 1));
  console.log(JSON.stringify(pins.map(p => [p.id, p.before, p.after])));
})();
