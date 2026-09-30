// usage: node site_check.js <url> -> JSON of what the site gate asserts (Verb Studio page)
const { chromium } = require('playwright');
const { AxeBuilder } = require('@axe-core/playwright');
const { CHROME } = require('./common');
(async () => {
  const url = process.argv[2], out = { runs: [] };
  const b = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
  for (const [width, height] of [[390, 844], [1440, 860]]) for (const scheme of ['light', 'dark']) {
    const ctx = await b.newContext({ viewport: { width, height }, colorScheme: scheme }); const p = await ctx.newPage(); const errs = [], ext = [];
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); }); p.on('pageerror', e => errs.push(String(e)));
    p.on('request', r => { const u = r.url(); if (!/^(data|blob|about|file):/.test(u) && !u.startsWith(url.split('/').slice(0, 3).join('/'))) ext.push(u); });
    await p.goto(url); await p.waitForFunction('window.axlReady');
    const r = { width, scheme, console_errors: errs, external: ext };
    const v0 = await p.evaluate("document.querySelector('.ver[aria-pressed=true]').textContent");
    await p.waitForTimeout(2100);
    const v1 = await p.evaluate("document.querySelector('.ver[aria-pressed=true]').textContent");
    r.cycles_without_input = v0 !== v1;                                   // the page changes on its own inside ~2 s
    r.preview_visible = await p.evaluate(() => { const f = document.getElementById('frame').getBoundingClientRect(); return f.top < innerHeight * 0.6 && f.height > 150; });
    r.words_above_preview = await p.evaluate(() => (document.getElementById('claim').innerText + ' ' + document.getElementById('wordTxt').textContent).trim().split(/\s+/).length);
    // one tap adds a tweak, the page switches to "yours", the tray answers
    await p.locator('#metro .row').first().click(); r.after_one_tap = await p.evaluate(() => ({ mine: document.querySelectorAll('#metro .row.mine').length, mode: document.querySelector('.ver.mine').getAttribute('aria-pressed'), facts: /nearest named words/.test(document.getElementById('facts').textContent) }));
    await p.locator('#metro .row').nth(4).click(); await p.click('#save'); await p.waitForTimeout(300);
    r.saved = await p.evaluate(() => { try { const d = JSON.parse(document.getElementById('json').textContent); return d.axl_verb === '0.1' && d.tweaks.length === 2 && /axl\.py check/.test(document.getElementById('cmd').textContent); } catch (e) { return false; } });
    await p.keyboard.press('Escape'); r.sheet_closed = await p.evaluate("!document.getElementById('sheet').classList.contains('open')");
    await p.keyboard.down('Shift'); r.peek = await p.evaluate("document.getElementById('frame').classList.contains('peeking')"); await p.keyboard.up('Shift'); r.unpeek = await p.evaluate("!document.getElementById('frame').classList.contains('peeking')");
    r.chips = await p.evaluate("document.querySelectorAll('#allcats .tw').length");
    await p.click('#wordBtn'); r.words = await p.evaluate("document.querySelectorAll('.wp').length"); await p.locator('.wp', { hasText: 'quieter' }).click();
    r.switch_ok = await p.evaluate("document.getElementById('wordTxt').textContent === 'quieter' && document.querySelectorAll('#metro .row').length > 0 && document.getElementById('wordPop').hidden");
    r.overflow = await p.evaluate('document.scrollingElement.scrollWidth - innerWidth');
    const axe = await new AxeBuilder({ page: p }).exclude('iframe').withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze();
    r.axe = axe.violations.filter(v => ['serious', 'critical'].includes(v.impact)).map(v => ({ id: v.id, n: v.nodes.length, s: v.nodes[0].target.join(' ') }));
    out.runs.push(r); await ctx.close();
  }
  await b.close(); console.log(JSON.stringify(out));
})();
