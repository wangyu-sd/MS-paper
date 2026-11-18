/* Export the editable master through Chromium's native vector PDF pipeline. */
const fs = require("node:fs/promises");
const path = require("node:path");
const { chromium } = require("playwright");
const { spawnSync } = require("node:child_process");

async function main() {
  const root = path.resolve(__dirname, "..");
  const stem = path.join(root, "figures/orbit_ms_nmi_figure1_vector");
  const svg = await fs.readFile(stem + ".svg", "utf8");
  const executablePath = process.env.CHROME_PATH || undefined;
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1670, height: 942 } });
    await page.setContent(`<!doctype html><meta charset="utf-8">
      <style>
        @page {size: 180mm 101.5329341317mm; margin: 0}
        html,body {margin:0; padding:0}
        body > svg {display:block}
      </style>${svg}`);
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({path: stem + ".pdf", preferCSSPageSize: true, printBackground: true});
    // Chromium rounds print page sizes. Retain its vector content and restore the precise source ratio.
    const normalized = spawnSync(
      process.env.PYTHON || "python3",
      [path.join(root, "scripts/draw_orbit_ms_nmi_figure1_vector.py"), "--normalize-pdf-page"],
      {encoding:"utf8"}
    );
    if (normalized.status !== 0) throw new Error(normalized.stderr || "PDF page normalization failed");
    const issues = await page.evaluate(() => {
      const ns = "http://www.w3.org/2000/svg";
      const outer = document.querySelector("body > svg");
      const nodes = Array.from(outer.querySelectorAll("text"));
      return nodes.map(element => {
        const bounds = element.getBoundingClientRect();
        const frame = outer.getBoundingClientRect();
        return {
          text: element.textContent,
          left: (bounds.left-frame.left)*1670/frame.width,
          right: (bounds.right-frame.left)*1670/frame.width,
          top: (bounds.top-frame.top)*942/frame.height,
          bottom: (bounds.bottom-frame.top)*942/frame.height,
          family: getComputedStyle(element).fontFamily,
          panel: element.closest('g[id^="panel-"]')?.id,
        };
      });
    });
    const verification = path.join(root, "figures/orbit_ms_nmi_figure1_sources/verification");
    await fs.mkdir(verification, {recursive:true});
    await fs.writeFile(path.join(verification, "text-bounds.json"), JSON.stringify(issues, null, 2) + "\n");
  } finally {
    await browser.close();
  }
}

main().catch(error => {console.error(error); process.exitCode = 1});
