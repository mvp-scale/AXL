const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: '.', snapshotPathTemplate: '{testDir}/__snap__/{arg}{ext}', reporter: [['json']],
  expect: { toHaveScreenshot: { maxDiffPixelRatio: 0 } },
  use: { launchOptions: { executablePath: process.env.CHROME_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] }, viewport: { width: 1440, height: 900 }, colorScheme: 'light' },
});
