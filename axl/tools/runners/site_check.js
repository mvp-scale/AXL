// usage: node site_check.js <url> -> JSON of what the site gate asserts (Verb Studio: two pickers, walk, board)
const { chromium } = require('playwright');
const { AxeBuilder } = require('@axe-core/playwright');
const { CHROME } = require('./common');
(async () => {
  const url = process.argv[2], out = { runs: [] };
  const b = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
  for (const [width, height] of [[390, 844], [1440, 900]]) for (const scheme of ['light', 'dark']) {
    const ctx = await b.newContext({ viewport: { width, height }, colorScheme: scheme }); const p = await ctx.newPage(); const errs = [], ext = [];
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); }); p.on('pageerror', e => errs.push(String(e)));
    p.on('request', r => { const u = r.url(); if (!/^(data|blob|about|file):/.test(u) && !u.startsWith(url.split('/').slice(0, 3).join('/'))) ext.push(u); });
    await p.goto(url); await p.waitForFunction('window.axlReady');
    const r = { width, scheme, console_errors: errs, external: ext };
    const s0 = await p.evaluate("document.getElementById('stateTxt').textContent"); await p.waitForTimeout(3100);
    const s1 = await p.evaluate("document.getElementById('stateTxt').textContent");
    r.walks_without_input = s0 !== s1;
    // first visit: the why-AXL modal is shown (with real numbers) and closes with Esc
    r.why_shown = await p.evaluate(() => !document.getElementById('why').hidden && /\d/.test(document.getElementById('whyN').textContent));
    await p.keyboard.press('Escape'); r.why_closes = await p.evaluate(() => document.getElementById('why').hidden);
    r.lit_during_walk = await p.evaluate("document.querySelectorAll('#board .er.lit').length");
    r.preview_visible = await p.evaluate(() => { const f = document.getElementById('frame').getBoundingClientRect(); return f.top < innerHeight * 0.45 && f.height > 200; });
    r.words_above_preview = await p.evaluate(() => document.querySelector('.bar').innerText.trim().split(/\s+/).length);
    await p.keyboard.down('Shift'); r.peek = await p.evaluate("document.getElementById('frame').classList.contains('peeking') && document.getElementById('stateTxt').textContent === 'Original'"); await p.keyboard.up('Shift');
    r.unpeek = await p.evaluate("!document.getElementById('frame').classList.contains('peeking')");
    // pickers: same component twice; multi-select works
    await p.click('#pickW .pbtn'); r.word_tiles = await p.evaluate("document.querySelectorAll('#pickW .tile').length");
    await p.locator('#pickW .tile', { hasText: 'bolder' }).first().click(); await p.click('#pickW .done');
    r.multi_words = await p.evaluate("document.querySelector('#pickW .lab').textContent");
    await p.click('#pickS .pbtn'); r.source_tiles = await p.evaluate("document.querySelectorAll('#pickS .tile').length"); await p.click('#pickS .done');
    await p.click('#pickW .play'); await p.waitForTimeout(3100); r.word_walk = await p.evaluate("document.getElementById('stateTxt').textContent"); await p.click('#pickW .play');
    // one tap on the board builds your word; save gives a file and a command
    await p.locator('#board .erh').first().click(); await p.locator('#board .er.open .tw').first().click(); await p.locator('#board .more .add').click(); r.after_one_tap = await p.evaluate(() => ({ mine: document.querySelectorAll('#board .tw[aria-pressed=true]').length, state: document.getElementById('stateTxt').textContent }));
    await p.locator('#board .er.open .tw').nth(1).click(); await p.locator('#board .more .add').click(); await p.click('#save'); await p.waitForTimeout(300);
    const prompt = await p.evaluate("document.getElementById('out').textContent"); await p.click('.tabs button[data-t=script]');
    // the one-file checker is large; the gate parses the real downloaded file, not the on-screen preview
    const [dl] = await Promise.all([p.waitForEvent('download'), p.click('#dl')]); const script = require('fs').readFileSync(await dl.path(), 'utf8');
    // one kit: rules (plain words + code + quote IDs) and the definition block the CLI reads
    r.saved = (() => { const m = prompt.match(/```axl\n([\s\S]*?)```/); return /## Rules/.test(prompt) && !!m && (m[1].match(/^  - /gm) || []).length === 2 && /DevTools/.test(script); })();
    try { new Function(script); r.script_parses = true; } catch (e) { r.script_parses = String(e); }
    await p.keyboard.press('Escape'); r.sheet_closed = await p.evaluate("!document.getElementById('sheet').classList.contains('open')");
    r.chips = await p.evaluate("document.querySelectorAll('#board .tw').length");
    r.overflow = await p.evaluate('document.scrollingElement.scrollWidth - innerWidth');
    const axe = await new AxeBuilder({ page: p }).exclude('iframe').withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze();
    r.axe = axe.violations.filter(v => ['serious', 'critical'].includes(v.impact)).map(v => ({ id: v.id, n: v.nodes.length, s: v.nodes[0].target.join(' ') }));
    out.runs.push(r); await ctx.close();
  }
  await b.close(); console.log(JSON.stringify(out));
})();
