/* AXL rule engine: runs AXL rules (element property test) inside any web page. No dependencies; uses window.axe when present.
   Used two ways, with the same code:
   - by the command line (tools/runners/rulecheck.js injects it, and adds Lighthouse, hover, phone width and dark mode);
   - as one self-contained file (engine + axe-core + a kit's rules) pasted into the browser console on any site.
   window.AXL_VOCAB = { "<element id>": ["<plain name>", "<css selector>"] } must be set first.
   AXL.check(["text:body font-size >= 16px", ...]) -> Promise<[{rule, status: PASS|FAIL|ASK|UNSUPPORTED|INVALID, detail, fix, elements}]> */
(function () {
  const OPS = ['>=', '<=', '==', 'between', 'contains', '!contains', 'pass'];
  const V = () => window.AXL_VOCAB || {};
  const parse = line => {
    const m = line.match(/^(\S+)\s+ask\s+"(.+)"$/); if (m) return { line, el: m[1], prop: 'ask', q: m[2], ctx: [] };
    const ctx = [...line.matchAll(/@(\S+)/g)].map(x => x[1]); const p = line.replace(/\s*@\S+/g, '').trim().split(/\s+/);
    return { line, el: p[0], prop: p[1], op: p[2], args: p.slice(3).map(a => a.replace(/^"|"$/g, '')), ctx };
  };
  const invalid = r => {
    if (!V()[r.el]) return `unknown element ${r.el}`;
    if (r.prop === 'ask') return null;
    if (!OPS.includes(r.op)) return `unknown test ${r.op}`;
    if (!/^(wcag|lighthouse|axl):/.test(r.prop) && !CSS.supports(r.prop, 'initial')) return `unknown CSS property ${r.prop}`;
    for (const c of r.ctx) if (!V()[c]) return `unknown context ${c}`;
    return null;
  };
  // where a rule applies: contexts the page is in right now (the CLI emulates them; in a console, resize or switch theme and re-run)
  const envOk = c => ({ 'media:narrow': innerWidth <= 430, 'media:dark': matchMedia('(prefers-color-scheme: dark)').matches, 'media:reduced-motion': matchMedia('(prefers-reduced-motion: reduce)').matches,
    'media:print': matchMedia('print').matches, 'media:forced-colors': matchMedia('(forced-colors: active)').matches }[c]);
  const path = e => { const s = e.tagName.toLowerCase(); if (e.id) return s + '#' + e.id; const c = typeof e.className === 'string' ? e.className.trim().split(/\s+/)[0] : ''; return s + (c ? '.' + c : ''); };
  const visible = e => { const b = e.getBoundingClientRect(); return b.width > 0 && b.height > 0 && getComputedStyle(e).visibility !== 'hidden'; };
  const ownText = e => [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
  const rootPx = () => parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;
  const chPx = e => { const s = document.createElement('span'); s.style.cssText = 'position:absolute;visibility:hidden;width:1ch'; (e || document.body).appendChild(s); const w = s.getBoundingClientRect().width; s.remove(); return w || 8; };
  const num = (v, e, prop) => {   // a CSS value as a number (px, ms, ratio or unitless)
    if (v == null) return NaN; v = String(v).trim(); if (prop === 'line-height' && v === 'normal') return 1.2;
    const m = v.match(/^(-?[\d.]+)(px|rem|em|ch|ms|s|%)?$/); if (!m) return NaN; let n = parseFloat(m[1]); const u = m[2] || '';
    if (u === 'rem') n *= rootPx(); else if (u === 'em') n *= e ? parseFloat(getComputedStyle(e).fontSize) : rootPx(); else if (u === 's') n *= 1000; else if (u === 'ch') n *= chPx(e);
    return n;
  };
  const cmp = (x, op, a, b) => op === '>=' ? x >= a - 1e-6 : op === '<=' ? x <= a + 1e-6 : op === '==' ? Math.abs(x - a) < 0.01 : op === 'between' ? x >= a - 1e-6 && x <= b + 1e-6 : false;

  // one CSS-property rule on a set of elements
  function cssRule(r, els) {
    const out = { n: 0, bad: [], sample: [] };
    const targets = r.el === 'text:*' ? els.filter(ownText) : els; out.n = targets.length;
    const ratio = r.prop === 'line-height' && !/(px|rem|em)$/.test(r.args[0] || '');
    for (const e of targets) {
      let raw = getComputedStyle(e).getPropertyValue(r.prop).trim(), ok;
      if (['contains', '!contains'].includes(r.op) || (r.op === '==' && isNaN(parseFloat(r.args[0])))) {
        const want = r.args.join(' ').toLowerCase(), have = raw.toLowerCase();
        ok = r.op === '!contains' ? !have.includes(want) : r.op === '==' ? have === want : have.includes(want);
      } else {
        let x = num(raw, e, r.prop); if (ratio && /px$/.test(raw)) { x = x / parseFloat(getComputedStyle(e).fontSize); raw = x.toFixed(2); }
        ok = isNaN(x) ? null : cmp(x, r.op, num(r.args[0], e, r.prop), num(r.args[1], e, r.prop));
      }
      if (ok === false) out.bad.push({ sel: path(e), value: raw }); else if (out.sample.length < 3) out.sample.push({ sel: path(e), value: raw });
    }
    return out;
  }
  // AXL measures (axl/measures.md): computed page properties no standard names
  function measure(r, els) {
    const all = [...document.querySelectorAll('body *')].filter(visible), text = els.map(e => e.innerText || '').join('\n'), bad = [];
    const distinct = f => new Set(all.filter(ownText).map(f)).size, max = a => Math.max(0, ...a);
    const M = {
      'axl:distinct-font-sizes': () => distinct(e => getComputedStyle(e).fontSize),
      'axl:distinct-font-families': () => distinct(e => getComputedStyle(e).fontFamily.split(',')[0].trim().replace(/['"]/g, '').toLowerCase()),
      'axl:distinct-font-weights': () => distinct(e => getComputedStyle(e).fontWeight),
      'axl:chars-per-line': () => Math.round(max(els.filter(ownText).map(e => e.getBoundingClientRect().width / chPx(e)))),
      'axl:spacing-off-scale': () => { const base = parseFloat((r.args.find(a => a.startsWith('base=')) || 'base=4').slice(5)); let n = 0;
        for (const e of all) { const c = getComputedStyle(e); for (const p of ['marginTop', 'marginBottom', 'paddingTop', 'paddingBottom', 'paddingLeft', 'rowGap', 'columnGap']) { const v = parseFloat(c[p]); if (v > 0 && Math.abs(v / base - Math.round(v / base)) > 0.01) { n++; if (bad.length < 8) bad.push({ sel: path(e), value: `${p} ${c[p]}` }); break; } } } return n; },
      'axl:emoji-as-icons': () => els.filter(e => /\p{Extended_Pictographic}/u.test(e.textContent) && e.getBoundingClientRect().width < 64).length,
      'axl:emoji-count': () => (text.match(/\p{Extended_Pictographic}/gu) || []).length,
      'axl:emoji-in-text': () => (text.match(/\p{Extended_Pictographic}/gu) || []).length,
      'axl:exclamation-marks': () => (text.match(/!/g) || []).length,
      'axl:ellipsis-three-dots': () => (text.match(/\.\.\./g) || []).length,
      'axl:dash-double-hyphen': () => (text.match(/(^|[^-])--([^-]|$)/g) || []).length,
      'axl:quotes-typographic': () => { const s = (text.match(/["']/g) || []).length, c = (text.match(/[“”‘’]/g) || []).length; return s + c ? Math.round(100 * c / (s + c)) : 100; },
      'axl:gradient-count': () => all.filter(e => /gradient/.test(getComputedStyle(e).backgroundImage)).length,
      'axl:gradient-stops': () => max(all.map(e => { const m = getComputedStyle(e).backgroundImage.match(/gradient\((.*)\)/); return m ? m[1].split(/,(?![^(]*\))/).length - (/(deg|to |circle|ellipse|at )/.test(m[1].split(',')[0]) ? 1 : 0) : 0; })),
      'axl:distinct-border-radii': () => new Set(all.map(e => getComputedStyle(e).borderTopLeftRadius).filter(v => v !== '0px')).size,
      'axl:distinct-shadow-levels': () => new Set(all.map(e => getComputedStyle(e).boxShadow).filter(v => v !== 'none')).size,
      'axl:box-shadow-layers': () => max(els.map(e => { const v = getComputedStyle(e).boxShadow; return v === 'none' ? 0 : v.split(/,(?![^(]*\))/).length; })),
      'axl:h1-word-count': () => ((document.querySelector('h1') || {}).innerText || '').trim().split(/\s+/).filter(Boolean).length,
      'axl:characters-per-heading': () => max([...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => h.innerText.trim().length)),
      'axl:max-dom-depth': () => { let d = 0; for (const e of document.querySelectorAll('*')) { let k = 0, x = e; while (x) { k++; x = x.parentElement; } d = Math.max(d, k); } return d; },
    };
    if (!M[r.prop]) return null;
    const value = M[r.prop]();
    return { value, bad, pass: cmp(value, r.op, num(r.args[0]), num(r.args[1])) };
  }

  let axeResult = null;
  async function wcag(r) {
    const sc = r.prop.slice(5), tag = 'wcag' + sc.replace(/\./g, '');
    if (!window.axe) return { status: 'UNSUPPORTED', detail: 'axe-core is not loaded' };
    if (!axeResult) { const rules = {}; axe.getRules().filter(x => x.tags.some(t => /^wcag\d{3,4}$/.test(t))).forEach(x => rules[x.ruleId] = { enabled: true }); axeResult = await axe.run(document, { rules }); }
    const has = [...axeResult.violations, ...axeResult.passes, ...axeResult.incomplete].some(v => v.tags.includes(tag));
    if (!has) return { status: 'UNSUPPORTED', detail: `axe has no automated rule for WCAG ${sc} that applies here; review it by hand` };
    // count only violations on this rule's own elements (the whole page for page and text:*)
    const sel = r.el === 'page' || r.el === 'text:*' ? null : V()[r.el][1];
    const mine = n => { if (!sel) return true; try { const e = document.querySelector(n.target[n.target.length - 1]); return !!e && (e.matches(sel) || !!e.closest(sel)); } catch (err) { return false; } };
    const v = axeResult.violations.filter(x => x.tags.includes(tag)).map(x => ({ ...x, nodes: x.nodes.filter(mine) })).filter(x => x.nodes.length);
    return v.length ? { status: 'FAIL', detail: v.map(x => x.help).join('; '), fix: v.map(x => `${x.help}: ${x.nodes.slice(0, 3).map(n => n.target.join(' ')).join(', ')}${x.nodes.length > 3 ? ` +${x.nodes.length - 3} more` : ''} (${x.helpUrl})`).join('; '), elements: v.flatMap(x => x.nodes.slice(0, 5).map(n => ({ sel: n.target.join(' '), value: (n.failureSummary || '').split('\n')[1] || '' }))) }
      : { status: 'PASS', detail: `axe: no WCAG ${sc} violations` };
  }

  async function one(r) {
    const bad = invalid(r); if (bad) return { status: 'INVALID', detail: bad };
    if (r.prop === 'ask') return { status: 'ASK', detail: r.q };
    if (r.el === 'process') return { status: 'ASK', detail: 'Not on the page: check the process.' };
    for (const c of r.ctx.filter(c => c.startsWith('media:'))) if (!envOk(c)) return { status: 'UNSUPPORTED', detail: `applies to ${V()[c][0].toLowerCase()}: re-run in that mode (the command line emulates it)` };
    if (r.el.startsWith('media:') && r.el !== 'media:print' && !envOk(r.el)) return { status: 'UNSUPPORTED', detail: `applies to ${V()[r.el][0].toLowerCase()}: re-run in that mode` };
    if (r.prop.startsWith('lighthouse:')) return { status: 'UNSUPPORTED', detail: 'Lighthouse audits run from the command line' };
    if (r.prop.startsWith('wcag:')) return wcag(r);
    const st = r.el.startsWith('state:') ? r.el : r.ctx.find(c => c.startsWith('state:'));
    if (st === 'state:hover') return { status: 'UNSUPPORTED', detail: 'hover states need the command line (a page cannot hover itself)' };
    const name = V()[r.el][0];
    let els;
    if (st === 'state:focus-visible') {   // focus each control with a visible focus and read it in that state
      const out = { n: 0, bad: [], sample: [] };
      for (const e of [...document.querySelectorAll(V()['state:focus-visible'][1])].filter(visible).slice(0, 30)) {
        e.focus({ focusVisible: true, preventScroll: true }); if (document.activeElement !== e) continue;
        const o = cssRule(r, [e]); out.n += o.n; out.bad.push(...o.bad); if (out.sample.length < 3) out.sample.push(...o.sample);
      }
      document.activeElement && document.activeElement.blur && document.activeElement.blur();
      return out.bad.length ? { status: 'FAIL', detail: `${out.bad.length} of ${out.n} focus states fail`, fix: `Set ${r.prop} ${r.op} ${r.args.join(' ')} in the keyboard focus state`, elements: out.bad.slice(0, 8) }
        : { status: 'PASS', detail: out.n ? `${out.n} focus states checked` : 'nothing focusable' };
    }
    els = [...document.querySelectorAll(V()[r.el][1] || 'html')].filter(visible);
    if (r.prop.startsWith('axl:')) {
      const o = measure(r, els); if (!o) return { status: 'UNSUPPORTED', detail: `measure ${r.prop} is proposed but not implemented yet (axl/measures.md)` };
      const what = r.prop.slice(4).replace(/-/g, ' ');
      return o.pass ? { status: 'PASS', detail: `${what} = ${o.value}` } : { status: 'FAIL', detail: `${what} = ${o.value}, needs ${r.op} ${r.args.join(' ')}`, fix: `Bring ${what} on ${name.toLowerCase()} to ${r.op} ${r.args.join(' ')} (now ${o.value})`, elements: o.bad.slice(0, 8) };
    }
    const o = cssRule(r, els);
    if (!o.n) return { status: 'PASS', detail: `no ${name.toLowerCase()} on the page` };
    return o.bad.length ? { status: 'FAIL', detail: `${o.bad.length} of ${o.n} ${name.toLowerCase()} fail`, fix: `Set ${r.prop} ${r.op} ${r.args.join(' ')} on ${name.toLowerCase()} (${o.bad.slice(0, 3).map(x => `${x.sel} is ${x.value}`).join('; ')})`, elements: o.bad.slice(0, 8) }
      : { status: 'PASS', detail: `${o.n} checked, e.g. ${o.sample.map(x => x.value).slice(0, 2).join(', ')}` };
  }

  async function check(lines) {
    axeResult = null; const res = [];
    for (const line of lines) { let x; try { x = await one(parse(line)); } catch (e) { x = { status: 'UNSUPPORTED', detail: 'check error: ' + String(e).slice(0, 120) }; } res.push({ rule: line, ...x }); }
    return res;
  }
  // console report: a table, the fixes, and a JSON copy for an agent
  async function run(name, lines) {
    const res = await check(lines), n = s => res.filter(x => x.status === s).length;
    console.log(`%c${name} on ${location.href}: ${n('PASS')} pass · ${n('FAIL')} fail · ${n('ASK')} to review · ${n('UNSUPPORTED')} not checkable here`, 'font-weight:bold;font-size:14px');
    console.table(res.map(x => ({ status: x.status, rule: x.rule, detail: x.detail })));
    res.filter(x => x.status === 'FAIL').forEach(x => console.log(`%cFAIL%c ${x.rule}\n  fix: ${x.fix}`, 'color:#c00;font-weight:bold', ''));
    const report = JSON.stringify({ word: name, page: location.href, results: res }, null, 1);
    try { copy(report); console.log('Report copied to the clipboard as JSON: paste it to your agent.'); } catch (e) { window.AXL_REPORT = report; console.log('Report saved in window.AXL_REPORT.'); }
    return res;
  }
  window.AXL = { check, run, parse };
})();
