const { test, expect } = require('@playwright/test');
const path = require('path');
const url = f => 'file://' + path.resolve(__dirname, '../../demo', f);
test('before matches its own baseline', async ({ page }) => { await page.goto(url('before.html')); await expect(page).toHaveScreenshot('before-1440.png', { animations: 'disabled' }); });
test('after differs from the before baseline', async ({ page }) => { await page.goto(url('after.html')); await expect(page).not.toHaveScreenshot('before-1440.png', { animations: 'disabled' }); });
