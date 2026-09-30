// usage: node site_check.js <port>  -> JSON {results:[...], claims_checked, export_doc}
const { chromium } = require('playwright');
const { AxeBuilder } = require('@axe-core/playwright');
const { CHROME } = require('./common');
(async () => {
  const port = process.argv[2], url = `http://127.0.0.1:${port}/`, out = { results: [] };
  const b = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
  for (const width of [375, 1440]) for (const scheme of ['light', 'dark']) {
    const ctx = await b.newContext({ viewport: { width, height: 900 }, colorScheme: scheme }); const p = await ctx.newPage(); const errs = [];
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); }); p.on('pageerror', e => errs.push(String(e)));
    p.on('requestfailed', r => errs.push('requestfailed ' + r.url()));
    const external = []; p.on('request', r => { if (!r.url().startsWith(url) && !r.url().startsWith('data:') && !r.url().startsWith('blob:')) external.push(r.url()); });
    await p.goto(url); await p.waitForFunction('window.axlReady'); await p.waitForTimeout(600);
    await p.click('#go'); await p.waitForTimeout(400);
    const axe = await new AxeBuilder({ page: p }).exclude('iframe').withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze();
    const bad = axe.violations.filter(v => ['serious', 'critical'].includes(v.impact)).map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, sample: v.nodes[0].target.join(' ') }));
    const overflow = await p.evaluate('document.scrollingElement.scrollWidth - innerWidth');
    // keyboard: tab from the top reaches a control with a visible focus ring
    await p.evaluate('window.scrollTo({top:0,behavior:"instant"})'); await p.keyboard.press('Tab'); await p.keyboard.press('Tab');
    const ring = await p.evaluate(() => { const e = document.activeElement; const s = getComputedStyle(e); return { tag: e.tagName, outline: s.outlineStyle + ' ' + s.outlineWidth }; });
    out.results.push({ width, scheme, console_errors: errs, external_requests: external, axe_serious_critical: bad, horizontal_overflow_px: overflow, focus: ring });
    if (width === 1440 && scheme === 'light') {
      const ids = await p.evaluate('window.axlAllClaimIds()'); let ok = 0; const fails = [];
      for (const id of ids) { const r = await p.evaluate(i => window.axlOpenClaim(i), id); const claim = await p.evaluate(i => window.AXL.claims.find(c => c.id === i), id);
        if (r.open && r.html.includes(claim.source_url.replace(/&/g, '&amp;')) ) ok++; else fails.push(id); await p.evaluate("document.getElementById('drawerClose').click()"); }
      out.claims_checked = ids.length; out.drawer_ok = ok; out.drawer_fail = fails.slice(0, 10);
      out.claims_without_source = await p.evaluate('window.AXL.claims.filter(c => !c.source_id || !c.source_url || !window.AXL.sources.find(s => s.id === c.source_id)).length');
      out.export_doc = await p.evaluate('window.axlBuildDocument(window.AXL.claims.filter(c => c.tier === "enforced" || c.tier === "measurable" || c.tier === "subjective").map(c => c.id).slice(0, 400))');
      // keyboard-only: theme toggle and drawer reachable
      await p.evaluate('window.scrollTo({top:0,behavior:"instant"})'); await p.focus('#srcBtn'); await p.keyboard.press('Enter'); out.drawer_keyboard = await p.evaluate('!document.getElementById("drawer").hidden'); await p.keyboard.press('Escape');
    }
    await ctx.close();
  }
  await b.close(); console.log(JSON.stringify(out));
})();
