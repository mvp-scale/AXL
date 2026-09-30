// Measure whether each tweak preview visibly changes the Northstar demo.
// usage: node preview_check.js previews.json [demo.html]  -> prints JSON {id: {changed, sample}} ; previews.json = [{id, css, patch, view, state}]
// patch = [{sel, text|attr|before|after|prepend|append}] content edits, applied by the demo's axlPatch()
const { chromium } = require('playwright'); const fs = require('fs'); const { CHROME } = require('./common');
const PROPS = ['color', 'background-color', 'background-image', 'font-size', 'font-weight', 'font-family', 'font-style', 'letter-spacing', 'line-height', 'text-align', 'text-transform',
  'font-variant-numeric', 'text-wrap', 'text-decoration-line', 'text-underline-offset', 'padding-top', 'padding-left', 'padding-bottom', 'margin-top', 'margin-bottom', 'border-top-width', 'border-top-color',
  'border-left-width', 'border-radius', 'box-shadow', 'max-width', 'width', 'height', 'min-height', 'display', 'row-gap', 'column-gap', 'grid-template-columns', 'filter', 'opacity', 'outline-style', 'outline-width',
  'outline-offset', 'transform', 'transition-duration', 'animation-name', 'animation-duration', 'cursor', 'hyphens', 'quotes', 'overflow-x', 'white-space', 'text-overflow', 'position', 'z-index', 'backdrop-filter',
  'font-feature-settings', 'accent-color', 'caret-color', 'scroll-behavior', 'overscroll-behavior-y', 'touch-action', 'resize', 'object-fit', 'aspect-ratio', 'visibility', 'justify-content', 'align-items', 'flex-direction', 'text-shadow', '-webkit-font-smoothing', 'text-rendering', 'hanging-punctuation', 'font-optical-sizing', 'color-scheme', 'content-visibility', 'contain', 'will-change', 'text-indent', 'word-spacing', 'list-style-type', 'vertical-align', 'mix-blend-mode'];
(async () => {
  const items = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')); const demo = process.argv[3] || `${__dirname}/../../demo/northstar.html`;
  const b = await chromium.launch({ executablePath: CHROME }); const p = await b.newPage({ viewport: { width: 980, height: 760 } });
  await p.goto('file://' + require('path').resolve(demo)); await p.addStyleTag({ content: '*,*::before,*::after{animation-play-state:paused!important;caret-color:auto}' });
  const out = {};
  for (const it of items) {
    if (!it.css && !it.patch) continue;
    try {
      out[it.id] = await p.evaluate(async ({ it, PROPS }) => {
        document.activeElement && document.activeElement.blur && document.activeElement.blur(); const base = { view: 'overview', modal: null, phase: 'ready', menu: false, drawer: false, streaming: true, siErr: '', editorTab: 'details', toast: '', feedback: '' };
        st = { ...st, ...base, view: it.view || 'overview', ...(it.state || {}) }; draw(); await new Promise(r => setTimeout(r, 30)); 
        const snap1 = el => { const c = getComputedStyle(el), a = getComputedStyle(el, '::before'), z = getComputedStyle(el, '::after');
          return PROPS.map(k => c.getPropertyValue(k)).join('|') + '#' + a.content + a.color + a.backgroundColor + '#' + z.content + z.color + z.backgroundColor; };
        const rs = document.querySelector('#recipe-style'); rs.textContent = ''; axlPatch([]);
        const s0 = new Map([...document.querySelectorAll('body [data-k]')].map(el => [el.dataset.k, [snap1(el), el.getClientRects().length > 0, el.textContent]]));
        rs.textContent = it.css || ''; axlPatch(it.patch || []);
        let vis = 0; const sample = [], note = el => { vis++; if (sample.length < 3) sample.push(el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className ? '.' + el.className.split(' ')[0] : '')); };
        // count elements on screen whose style or own text changed, plus inserted/edited elements (by stable data-k stamps, so inserts don't shift the comparison)
        document.querySelectorAll('body *').forEach(el => { const o = el.dataset.k != null && s0.get(el.dataset.k);
          if (!o) { if (el.hasAttribute('data-axl-ins') && el.getClientRects().length) note(el); return; }
          if ((o[1] || el.getClientRects().length) && el.hasAttribute('data-axl-p') && el.textContent !== o[2]) { note(el); return; }   // words changed (attribute-only edits count only if they change the look)
          if ((o[1] || el.getClientRects().length) && snap1(el) !== o[0]) note(el); });
        rs.textContent = ''; axlPatch([]);
        return { changed: vis, sample };
      }, { it, PROPS });
    } catch (e) { out[it.id] = { changed: -1, error: String(e).slice(0, 120) }; }
  }
  console.log(JSON.stringify(out)); await b.close();
})();
