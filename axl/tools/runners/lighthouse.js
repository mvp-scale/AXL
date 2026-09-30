// usage: node lighthouse.js <html> -> serves the file on localhost, runs the Lighthouse accessibility category.
// Findings = failed accessibility audits (audit level is stable; the category score is not asserted).
const http = require('http'), fs = require('fs'), path = require('path'), os = require('os'), { spawn } = require('child_process');
const file = path.resolve(process.argv[2]);
const srv = http.createServer((q, s) => { s.setHeader('content-type', 'text/html'); s.end(fs.readFileSync(file)); });
srv.listen(0, '127.0.0.1', () => {
  const url = `http://127.0.0.1:${srv.address().port}/`;
  const out = path.join(os.tmpdir(), `lh-${process.pid}.json`);
  const lh = spawn(path.join(__dirname, '..', 'node_modules', '.bin', 'lighthouse'),
    [url, '--only-categories=accessibility', '--output=json', `--output-path=${out}`, '--quiet', '--form-factor=desktop', '--screenEmulation.disabled', '--chrome-flags=--headless=new --no-sandbox'],
    { stdio: 'ignore', env: { ...process.env, CHROME_PATH: process.env.CHROME_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' } });
  const timer = setTimeout(() => lh.kill('SIGKILL'), 100000);
  lh.on('exit', code => {
    clearTimeout(timer); srv.close();
    try {
      if (code !== 0) throw new Error('lighthouse exited ' + code);
      const r = JSON.parse(fs.readFileSync(out, 'utf8'));
      const refs = r.categories.accessibility.auditRefs.filter(a => a.weight > 0);
      const findings = refs.map(a => r.audits[a.id]).filter(a => a.score === 0).map(a => ({ rule_id: a.id, result: 'fail', evidence: a.title, location: '' })).sort((a, b) => a.rule_id.localeCompare(b.rule_id));
      console.log(JSON.stringify({ tool: 'lighthouse', version: r.lighthouseVersion, checked_audits: refs.length, findings }));
      process.exit(findings.length ? 1 : 0);
    } catch (e) { console.log(JSON.stringify({ tool: 'lighthouse', error: String(e.message).slice(0, 200), findings: [] })); process.exit(2); }
  });
});
