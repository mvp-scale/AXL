// usage: node contrast.js "<fg>,<bg>,<min>" ...  WCAG 2.x relative-luminance ratio; fails when ratio < min.
const lum = h => { const c = h.replace('#', ''); const v = [0, 2, 4].map(i => parseInt(c.substr(i, 2), 16) / 255).map(x => x <= 0.03928 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4); return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]; };
const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };
const findings = process.argv.slice(2).map(p => { const [fg, bg, min] = p.split(','); const r = ratio(fg, bg); return { rule_id: 'wcag-1.4.3', result: r >= +min ? 'pass' : 'fail', evidence: `${fg} on ${bg} = ${r.toFixed(2)}:1 (min ${min}:1)`, location: `${fg} on ${bg}` }; });
console.log(JSON.stringify({ tool: 'wcag-contrast (relative luminance, WCAG 2.x)', findings }));
process.exit(findings.some(f => f.result === 'fail') ? 1 : 0);
