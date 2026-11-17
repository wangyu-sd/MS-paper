/* Export editable SVG geometry through Chromium to a vector PDF. */
const fs = require("node:fs/promises");
const path = require("node:path");
const { chromium } = require("playwright");

async function main() {
  const stem = path.join(__dirname, "orbit_ms_nmi_framework");
  const svg = await fs.readFile(stem + ".svg", "utf8");
  const executablePath = process.env.CHROME_PATH || undefined;
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage();
    await page.setContent(`<!doctype html><meta charset="utf-8">
      <style>
        @page {size: 180mm 101.25mm; margin: 0}
        html,body {margin: 0; padding: 0}
        body > svg {display: block}
      </style>${svg}`);
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({ path: stem + ".pdf", preferCSSPageSize: true, printBackground: true });
  } finally {
    await browser.close();
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
