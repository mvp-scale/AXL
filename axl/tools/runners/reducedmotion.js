// usage: node reducedmotion.js <html> -> emulates prefers-reduced-motion: reduce; fails if any element still has a non-zero transition/animation duration.
const { chromium } = require('playwright');
const path = require('path');
const { CHROME } = require('./common');
(async () => {
  const b = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
  const ctx = await b.newContext({ reducedMotion: 'reduce', viewport: { width: 1440, height: 900 } });
  const p = await ctx.newPage(); await p.goto('file://' + path.resolve(process.argv[2]));
  const bad = await p.evaluate(() => {
    const ms = v => Math.max(0, ...v.split(',').map(x => x.trim().endsWith('ms') ? parseFloat(x) : parseFloat(x) * 1000 || 0));
    const seen = {};
    for (const el of document.querySelectorAll('*')) { const c = getComputedStyle(el); const t = ms(c.transitionDuration), a = ms(c.animationDuration);
      if (t > 1 || (a > 1 && c.animationName !== 'none')) { const k = el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : ''); seen[k] = { t, a }; } }
    return seen; });
  await b.close();
  const findings = Object.entries(bad).sort().map(([k, v]) => ({ rule_id: 'reduced-motion', result: 'fail', evidence: `transition ${v.t}ms / animation ${v.a}ms under prefers-reduced-motion: reduce`, location: k }));
  console.log(JSON.stringify({ tool: 'playwright emulateMedia(reducedMotion)', findings })); process.exit(findings.length ? 1 : 0);
})();
