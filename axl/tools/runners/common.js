const path = require('path');
const { chromium } = require('playwright');
const CHROME = process.env.CHROME_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
async function withPage(file, width, fn, state) {
  const b = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
  const ctx = await b.newContext({ viewport: { width, height: 900 } });
  const p = await ctx.newPage();
  await p.goto('file://' + path.resolve(file));
  try { return await fn(p); } finally { await b.close(); }
}
module.exports = { withPage, CHROME };
