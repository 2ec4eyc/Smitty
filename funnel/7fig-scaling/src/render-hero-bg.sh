#!/usr/bin/env bash
# Renders images/hero-bg.jpg (1920x1080) from src/hero-bg.html with headless Chromium.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; out="$here/../images"
PW="${PW:-/opt/node22/lib/node_modules/@playwright/cli/node_modules/playwright-core}"
node -e "
const { chromium } = require('$PW');
(async () => { const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://$here/hero-bg.html'); await p.waitForTimeout(500);
  await p.screenshot({ path: '$out/hero-bg.png' }); await b.close(); })();"
python3 -c 'import sys; from PIL import Image; Image.open(sys.argv[1]).convert("RGB").save(sys.argv[2], "JPEG", quality=84, optimize=True, progressive=True)' "$out/hero-bg.png" "$out/hero-bg.jpg"
rm "$out/hero-bg.png"; ls -la "$out/hero-bg.jpg"
