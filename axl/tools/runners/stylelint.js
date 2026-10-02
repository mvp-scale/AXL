// usage: node stylelint.js <css> -> fails on any violation
const { execFileSync } = require('child_process');
let out, code = 0;
try { out = execFileSync(require('path').join(__dirname,'..','node_modules','.bin','stylelint'), ['--config', 'axl/tools/stylelint.config.json', '--formatter', 'json', process.argv[2]], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }); }
catch (e) { out = e.stderr || e.stdout; code = e.status; }
const r = JSON.parse(out.trim().split('\n').filter(l => l.startsWith('[')).pop() || '[]');
const findings = r.flatMap(f => f.warnings.map(w => ({ rule_id: w.rule, result: 'fail', evidence: w.text.replace(/\s+/g, ' '), location: `line ${w.line}` })))
  .sort((a, b) => a.location.localeCompare(b.location, undefined, { numeric: true }));
console.log(JSON.stringify({ tool: 'stylelint', findings }));
process.exit(findings.length ? 1 : 0);
