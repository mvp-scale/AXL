// usage: node site_check.js <url>  -> JSON of everything the site gate asserts (single-file story page)
const { chromium } = require('playwright');
const { AxeBuilder } = require('@axe-core/playwright');
const { CHROME } = require('./common');
(async () => {
  const url = process.argv[2], out = { runs: [] };
  const b = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
  for (const [width, height] of [[375, 812], [1440, 800]]) for (const scheme of ['light', 'dark']) {
    const ctx = await b.newContext({ viewport: { width, height }, colorScheme: scheme }); const p = await ctx.newPage(); const errs = [], ext = [];
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); }); p.on('pageerror', e => errs.push(String(e)));
    p.on('request', r => { const u = r.url(); if (!u.startsWith('data:') && !u.startsWith('blob:') && !u.startsWith('about:') && !u.startsWith(url.split('/').slice(0, 3).join('/')) && !u.startsWith('file:')) ext.push(u); });
    await p.goto(url); await p.waitForFunction('window.axlReady');
    const run = { width, scheme, console_errors: errs, external: ext };
    // first screen: words on screen, an obvious control inside the viewport, movement inside 1.2 s
    await p.waitForTimeout(1200);
    run.split_by_1200ms = await p.evaluate("document.getElementById('s1').classList.contains('split')");
    run.first_screen_words = await p.evaluate(() => { const vh = innerHeight; let n = 0; const w = document.createTreeWalker(document.getElementById('s1'), NodeFilter.SHOW_TEXT);
      while (w.nextNode()) { const t = w.currentNode, el = t.parentElement; if (!t.textContent.trim() || el.closest('.sr,[hidden]') || el.closest('svg')) continue; const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); if (r.width && r.top < vh && r.bottom > 0 && cs.visibility !== 'hidden' && parseFloat(cs.opacity) > 0.05) n += t.textContent.trim().split(/\s+/).length; } return n; });
    run.control_in_first_screen = await p.evaluate(() => { const c = document.getElementById('cta').getBoundingClientRect(); return c.top >= 0 && c.bottom <= innerHeight; });
    await p.click('.mean[data-i="1"]'); run.meaning_quote = await p.evaluate("document.getElementById('said').textContent.length");
    await p.keyboard.press('Tab');
    // scene 2: sweep, counter to zero, five pins, each lens shows command + source
    await p.evaluate("document.getElementById('s2').scrollIntoView({behavior:'instant'})"); await p.waitForTimeout(3400);
    run.counter = await p.evaluate("document.getElementById('cnt').textContent"); run.pins_on = await p.evaluate("document.querySelectorAll('.pin.on').length");
    run.lens = [];
    for (let i = 1; i <= 5; i++) { await p.evaluate(i => document.querySelectorAll('.pin')[i - 1].click(), i); await p.waitForTimeout(200); await p.click('#bHow'); const how = await p.evaluate("document.getElementById('pHow').innerText"); await p.click('#bWho'); const who = await p.evaluate("document.getElementById('pWho').innerText + document.getElementById('pWho').innerHTML");
      run.lens.push({ i, big: await p.evaluate("document.getElementById('big').innerText"), cmd: /node axl\/tools\/runners/.test(how), src: /https?:\/\//.test(who) && who.length > 60, imgs: await p.evaluate("document.getElementById('imgA').naturalWidth > 0 && document.getElementById('imgB').naturalWidth > 0") }); await p.keyboard.press('Escape'); await p.waitForTimeout(150); }
    run.lens_closed = await p.evaluate("!document.getElementById('lens').classList.contains('open')");
    // scene 3: every tile answers
    await p.evaluate("document.getElementById('s3').scrollIntoView({behavior:'instant'})"); await p.waitForTimeout(2600);
    run.lit = await p.evaluate("document.getElementById('lit').textContent"); const n = await p.evaluate("document.querySelectorAll('.tile').length"); run.tiles = n; run.tile_bad = [];
    for (let i = 0; i < n; i++) { const r = await p.evaluate(i => { document.querySelectorAll('.tile')[i].click(); const c = document.getElementById('tilecard'); return { txt: c.innerText.length, cmd: /python3|node/.test(c.innerText), lit: document.querySelectorAll('.tile')[i].classList.contains('lit'), link: !!c.querySelector('a[href^="http"]') }; }, i); if (!r.txt || (r.lit && !r.cmd)) run.tile_bad.push(i); }
    // scene 4
    await p.evaluate("document.getElementById('s4').scrollIntoView({behavior:'instant'})"); await p.waitForTimeout(2000);
    run.echo_dots = await p.evaluate("document.querySelectorAll('#echo .n').length"); await p.evaluate("document.querySelector('#echo .n').dispatchEvent(new MouseEvent('click',{bubbles:true}))"); run.echo_info = await p.evaluate("document.getElementById('echoinfo').textContent.length");
    // scene 5
    await p.evaluate("document.getElementById('s5').scrollIntoView({behavior:'instant'})"); run.command_shown = await p.evaluate("document.getElementById('term').innerText.includes('evaluate.py')");
    run.overflow = await p.evaluate('document.scrollingElement.scrollWidth - innerWidth');
    const axe = await new AxeBuilder({ page: p }).exclude('iframe').withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze();
    run.axe = axe.violations.filter(v => ['serious', 'critical'].includes(v.impact)).map(v => ({ id: v.id, nodes: v.nodes.length, sample: v.nodes[0].target.join(' ') }));
    out.runs.push(run); await ctx.close();
  }
  // reduced motion: the end states are there without any animation
  const ctx = await b.newContext({ viewport: { width: 1440, height: 800 }, reducedMotion: 'reduce' }); const p = await ctx.newPage(); await p.goto(url); await p.waitForFunction('window.axlReady'); await p.evaluate("document.getElementById('s2').scrollIntoView({behavior:'instant'})"); await p.waitForTimeout(600);
  out.reduced = { split: await p.evaluate("document.getElementById('s1').classList.contains('split')"), counter: await p.evaluate("document.getElementById('cnt').textContent"), pins: await p.evaluate("document.querySelectorAll('.pin.on').length") };
  await b.close(); console.log(JSON.stringify(out));
})();
