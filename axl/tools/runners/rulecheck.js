// Generic rule checker: runs AXL rules (element property test) against any page.
// usage: node rulecheck.js <rules.json> <page.html|https://url> [--lighthouse]
//   rules.json = [{"rule": "text:body font-size >= 16px"}, ...] (axl.py extracts them from a kit's ```axl block)
// Prints JSON: [{rule, status: PASS|FAIL|ASK|UNSUPPORTED|INVALID, detail, fix, elements:[{sel, value}]}]
// How a rule is checked is decided by its property, never by the rule text:
//   CSS property -> the browser's computed value on every matching element, compared with the test
//   wcag:<SC>    -> axe-core rules tagged with that success criterion
//   lighthouse:<audit> -> the Lighthouse audit (only with --lighthouse; slow)
//   axl:<measure> -> a measure implemented below (others report UNSUPPORTED, never a guess)
//   ask          -> listed as a question for a person or agent
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const { CHROME } = require('./common');
const V = JSON.parse(fs.readFileSync(path.join(__dirname, '../../data/vocab.json'), 'utf8'));
const EL = Object.fromEntries(V.elements.map(e => [e.id, e]));
const CSSP = (() => { const j = JSON.parse(fs.readFileSync(path.join(__dirname, '../../data/standards/css_properties.json'), 'utf8')); return new Set([...j.properties, ...(j.shorthands || [])]); })();
const SC_RULES = Object.fromEntries(require('axe-core').getRules().filter(r => r.tags.some(t => /^wcag\d{3,4}$/.test(t))).map(r => [r.ruleId, { enabled: true }]));
const OPS = ['>=', '<=', '==', 'between', 'contains', '!contains', 'pass'];

function parse(line) {
  const m = line.match(/^(\S+)\s+ask\s+"(.+)"$/); if (m) return { el: m[1], prop: 'ask', q: m[2], ctx: [] };
  const ctx = [...line.matchAll(/@(\S+)/g)].map(x => x[1]); const p = line.replace(/\s*@\S+/g, '').trim().split(/\s+/);
  return { el: p[0], prop: p[1], op: p[2], args: p.slice(3), ctx };
}
function invalid(r) {
  if (!EL[r.el]) return `unknown element ${r.el}`;
  if (r.prop === 'ask') return null;
  if (!OPS.includes(r.op)) return `unknown test ${r.op}`;
  if (!(CSSP.has(r.prop) || /^(wcag|lighthouse|axl):/.test(r.prop))) return `unknown property ${r.prop}`;
  for (const c of r.ctx) if (!EL[c]) return `unknown context ${c}`;
  return null;
}

// the in-page checks live in ../engine/axl-engine.js (the same file the one-file console checker uses)
const ENGINE = fs.readFileSync(path.join(__dirname, '../engine/axl-engine.js'), 'utf8');
const AXE = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const SLIM = JSON.stringify(Object.fromEntries(V.elements.map(e => [e.id, [e.name, e.css || '']])));
async function inject(p) { if (await p.evaluate(() => !!window.AXL)) return; await p.addScriptTag({ content: AXE }); await p.addScriptTag({ content: `window.AXL_VOCAB=${SLIM};\n${ENGINE}` }); }

function lighthouse(target) {
  const http = require('http'), os = require('os'), { spawn } = require('child_process');
  return new Promise(done => {
    const go = url => {
      const out = path.join(os.tmpdir(), `axl-lh-${process.pid}.json`);
      const lh = spawn(path.join(__dirname, '..', 'node_modules', '.bin', 'lighthouse'), [url, '--output=json', `--output-path=${out}`, '--quiet', '--form-factor=desktop', '--screenEmulation.disabled', '--throttling-method=provided', '--chrome-flags=--headless=new --no-sandbox' + (process.argv.includes('--insecure') ? ' --ignore-certificate-errors' : '')],
        { stdio: 'ignore', env: { ...process.env, CHROME_PATH: CHROME } });
      const timer = setTimeout(() => lh.kill('SIGKILL'), 180000);
      lh.on('exit', () => { clearTimeout(timer); if (srv) srv.close(); try { done(JSON.parse(fs.readFileSync(out, 'utf8'))); } catch (e) { done({ audits: {}, error: 'Lighthouse did not finish' }); } });
    };
    let srv = null;
    if (/^https?:/.test(target)) return go(target);
    const file = path.resolve(target), dir = path.dirname(file);
    srv = http.createServer((q, s) => { const f = path.join(dir, decodeURIComponent(q.url.split('?')[0])); const p_ = q.url === '/' ? file : f; try { s.end(fs.readFileSync(p_)); } catch (e) { s.statusCode = 404; s.end(); } });
    srv.listen(0, '127.0.0.1', () => go(`http://127.0.0.1:${srv.address().port}/`));
  });
}

(async () => {
  const rules = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')).map(x => ({ line: x.rule, ...parse(x.rule) }));
  const target = process.argv[3]; const url = /^https?:/.test(target) ? target : 'file://' + path.resolve(target);
  let LH = null;
  if (rules.some(r => (r.prop || '').startsWith('lighthouse:')) && !process.argv.includes('--quick')) LH = await lighthouse(target);
  const b = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
  const results = []; let axeCache = {};
  const contextOf = r => ({ width: r.ctx.includes('media:narrow') ? 390 : 1440, dark: r.ctx.includes('media:dark') || r.el === 'media:dark', reduce: r.ctx.includes('media:reduced-motion'), print: r.ctx.includes('media:print') });
  const pages = {};
  async function pageFor(c) {
    const k = JSON.stringify(c); if (pages[k]) return pages[k];
    const ctx = await b.newContext({ ignoreHTTPSErrors: process.argv.includes('--insecure'), viewport: { width: c.width, height: 900 }, colorScheme: c.dark ? 'dark' : 'light', reducedMotion: c.reduce ? 'reduce' : 'no-preference' });
    const p = await ctx.newPage(); try { await p.goto(url, { waitUntil: 'load', timeout: 60000 }); } catch (e) { console.log(JSON.stringify([{ rule: '(page)', status: 'INVALID', detail: 'could not open the page: ' + String(e.message || e).split('\n')[0] }])); process.exit(0); } if (c.print) await p.emulateMedia({ media: 'print' });
    await p.waitForTimeout(300); return (pages[k] = p);
  }
  for (const r of rules) {
    const bad = invalid(r);
    if (bad) { results.push({ rule: r.line, status: 'INVALID', detail: bad }); continue; }
    const c = contextOf(r), p = await pageFor(c);
    try {
      if ((r.prop || '').startsWith('lighthouse:')) {
        const id = r.prop.slice(11);
        if (!LH) { results.push({ rule: r.line, status: 'UNSUPPORTED', detail: 'Lighthouse skipped (--quick)' }); continue; }
        const au = LH.audits && LH.audits[id];
        if (!au) { results.push({ rule: r.line, status: 'UNSUPPORTED', detail: `Lighthouse did not report audit ${id}` + (LH.error ? ` (${LH.error})` : '') }); continue; }
        results.push(au.score === null || au.score >= 0.9 ? { rule: r.line, status: 'PASS', detail: `Lighthouse ${id}: ${au.score === null ? 'not applicable' : 'score ' + au.score}${au.displayValue ? ' · ' + au.displayValue : ''}` }
          : { rule: r.line, status: 'FAIL', detail: `Lighthouse ${id}: score ${au.score}${au.displayValue ? ' · ' + au.displayValue : ''}`, fix: au.title, elements: ((au.details && au.details.items) || []).slice(0, 5).map(i => ({ sel: (i.node && (i.node.selector || i.node.snippet)) || i.url || '', value: i.node ? (i.node.snippet || '') : '' })) });
        continue;
      }
      const st = r.el.startsWith('state:') ? r.el : r.ctx.find(x => x.startsWith('state:'));
      if (st === 'state:hover' && r.prop !== 'ask') {   // the one thing a page can't do to itself: hover; check each target in that state
        await inject(p); const hs = (await p.$$(EL['state:hover'].css)).slice(0, 25); const found = { n: 0, bad: [] };
        for (const h of hs) {
          if (!(await h.isVisible())) continue;
          await h.hover({ timeout: 1000 }).catch(() => {});
          const o = await h.evaluate((e, r) => { const v = getComputedStyle(e).getPropertyValue(r.prop).trim(), want = r.args.join(' ').toLowerCase();
            const ok = r.op === 'contains' ? v.toLowerCase().includes(want) : r.op === '!contains' ? !v.toLowerCase().includes(want) : r.op === '==' && isNaN(parseFloat(r.args[0])) ? v.toLowerCase() === want
              : (x => r.op === '>=' ? x >= parseFloat(r.args[0]) : r.op === '<=' ? x <= parseFloat(r.args[0]) : Math.abs(x - parseFloat(r.args[0])) < 0.01)(parseFloat(v) * (/ms$/.test(v) ? 1 : /s$/.test(v) ? 1000 : 1));
            return { ok, v, sel: e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : '') }; }, { prop: r.prop, op: r.op, args: r.args });
          found.n++; if (!o.ok) found.bad.push({ sel: o.sel, value: o.v });
        }
        results.push(found.bad.length ? { rule: r.line, status: 'FAIL', detail: `${found.bad.length} of ${found.n} hover states fail`, fix: `Set ${r.prop} ${r.op} ${r.args.join(' ')} in the hover state`, elements: found.bad.slice(0, 8) }
          : { rule: r.line, status: 'PASS', detail: found.n ? `${found.n} hover states checked` : 'nothing to hover' });
        continue;
      }
      await inject(p);
      const [x] = await p.evaluate(line => AXL.check([line]), r.line);
      results.push(x);
    } catch (e) { results.push({ rule: r.line, status: 'UNSUPPORTED', detail: 'check error: ' + String(e).slice(0, 120) }); }
  }
  console.log(JSON.stringify(results)); await b.close();
})();
