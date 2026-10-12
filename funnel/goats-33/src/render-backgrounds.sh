#!/usr/bin/env bash
# Renders the background JPGs from bg.html with headless Chromium via Playwright.
# Usage: src/render-backgrounds.sh   (needs node, playwright-core, python3 with Pillow)
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; out="$here/../backgrounds"
PW="${PW:-/opt/node22/lib/node_modules/@playwright/cli/node_modules/playwright-core}"
node - "$here" "$out" "$PW" <<'JS'
const [here, out, pw] = process.argv.slice(2);
const { chromium } = require(pw);
const jobs = [['hero-desktop','hero',1920,1680],['hero-mobile','hero',1080,5270],['dark-section','dark',1920,1080],['light-section','light',1920,1080]];
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium' });
  for (const [name, v, w, h] of jobs) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto(`file://${here}/bg.html?v=${v}`); await p.waitForTimeout(1500);
    await p.screenshot({ path: `${out}/${name}.png` }); await p.close();
  }
  await b.close();
})();
JS
for f in "$out"/*.png; do
  python3 -c 'import sys; from PIL import Image; Image.open(sys.argv[1]).convert("RGB").save(sys.argv[2], "JPEG", quality=80, optimize=True, progressive=True)' "$f" "${f%.png}.jpg"
  rm "$f"
done
ls -la "$out"
