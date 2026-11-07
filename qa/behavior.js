#!/usr/bin/env node
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve('index.html'));
  // basic smoke
  await page.waitForSelector('header');
  console.log('header present');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
