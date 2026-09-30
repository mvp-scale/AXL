// usage: node designmd.js <DESIGN.md> -> fails on any warning or error
const { execFileSync } = require('child_process');
let out, code = 0;
try { out = execFileSync(require('path').join(__dirname,'..','node_modules','.bin','design.md'), ['lint', process.argv[2], '--format', 'json'], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }); }
catch (e) { out = e.stdout; code = e.status; }
const r = JSON.parse(out);
const findings = r.findings.filter(f => f.severity !== 'info').map(f => ({ rule_id: f.rule, result: 'fail', severity: f.severity, evidence: f.message, location: f.path || '' }));
console.log(JSON.stringify({ tool: 'design.md lint', findings }));
process.exit(findings.length || code ? 1 : 0);
