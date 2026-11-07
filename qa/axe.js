#!/usr/bin/env node
const { chromium } = require('playwright');
const axe = require('axe-core');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve('index.html'));
  await page.addScriptTag({ content: axe.source });
  const results = await page.evaluate(async () => {
    return await window.axe.run(document, {
      runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'best-practice'] }
    });
  });
  console.log(JSON.stringify(results.violations, null, 2));
  if (results.violations.length) process.exit(1);
  console.log('0 axe violations');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
