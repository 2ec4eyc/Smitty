#!/usr/bin/env bash
# Renders backgrounds/hero-section.jpg from src/hero-section-bg.html with headless Chromium via Playwright.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; out="$here/../backgrounds"; mkdir -p "$out"
PW="${PW:-/opt/node22/lib/node_modules/@playwright/cli/node_modules/playwright-core}"
node - "$here" "$out" "$PW" <<'JS'
const [here, out, pw] = process.argv.slice(2);
const { chromium } = require(pw);
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1920, height: 1400 } });
  await p.goto(`file://${here}/hero-section-bg.html`); await p.waitForTimeout(500);
  await p.screenshot({ path: `${out}/hero-section.png` }); await b.close();
})();
JS
python3 -c 'import sys; from PIL import Image; Image.open(sys.argv[1]).convert("RGB").save(sys.argv[2], "JPEG", quality=85, optimize=True, progressive=True)' "$out/hero-section.png" "$out/hero-section.jpg"
rm "$out/hero-section.png"; ls -la "$out"
