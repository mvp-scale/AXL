// usage: node visual.js [--update]  -> runs toHaveScreenshot tests; findings = failed tests
const { spawnSync } = require('child_process');
const args = ['test', '-c', 'axl/tools/visual/playwright.config.js'].concat(process.argv[2] === '--update' ? ['--update-snapshots', '-g', 'before matches'] : []);
const r = spawnSync(require('path').join(__dirname,'..','node_modules','.bin','playwright'), args, { encoding: 'utf8' });
let j; try { j = JSON.parse(r.stdout); } catch (e) { console.log(JSON.stringify({ tool: 'playwright toHaveScreenshot', error: (r.stderr || r.stdout).slice(0, 200), findings: [] })); process.exit(2); }
const specs = j.suites.flatMap(s => s.specs);
const findings = specs.map(s => ({ rule_id: s.title, result: s.ok ? 'pass' : 'fail', evidence: s.ok ? 'ok' : 'screenshot assertion failed', location: 'demo' }));
console.log(JSON.stringify({ tool: 'playwright toHaveScreenshot', findings }));
process.exit(findings.some(f => f.result === 'fail') ? 1 : 0);
