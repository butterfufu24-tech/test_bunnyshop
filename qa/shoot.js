#!/usr/bin/env node
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve('index.html'));
  await page.screenshot({ path: 'qa/out/desktop.png', fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: 'qa/out/mobile.png', fullPage: true });
  console.log('screenshots written');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
