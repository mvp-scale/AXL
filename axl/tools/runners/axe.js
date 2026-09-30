// usage: node axe.js <html> [width]  -> JSON on stdout. Exit 1 if any violation.
const { AxeBuilder } = require('@axe-core/playwright');
const { withPage } = require('./common');
(async () => {
  const file = process.argv[2], width = +(process.argv[3] || 1440);
  const res = await withPage(file, width, p => new AxeBuilder({ page: p }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze());
  const findings = res.violations.map(v => ({ rule_id: v.id, result: 'fail', impact: v.impact, nodes: v.nodes.length, location: v.nodes[0].target.join(' ') }))
    .sort((a, b) => a.rule_id.localeCompare(b.rule_id));
  const passes = res.passes.map(v => v.id).sort();
  console.log(JSON.stringify({ tool: 'axe-core', engine: res.testEngine.version, width, violations: findings.length, findings, passed_rules: passes.length, passed_ids: passes }));
  process.exit(findings.length ? 1 : 0);
})();
