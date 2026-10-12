"""Stitches registration/*.html into preview/registration.html, the way GHL will stack them.
The form between the hero and the perks is a stand-in for GHL's native form element."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
blk = lambda n: next((root / "registration").glob(f"{n}-*.html")).read_text()
FORM = """<div class="wf wf--dark" style="padding:0 16px"><form class="mock-form" onsubmit="return false">
  <p class="mock-note">Preview only: GHL's native form goes here</p>
  <label>First name<input placeholder="First name" autocomplete="given-name"></label>
  <label>Email<input type="email" placeholder="you@example.com" autocomplete="email"></label>
  <label>Phone (optional)<input type="tel" placeholder="(312) 555-0133" autocomplete="tel"></label>
  <button class="wf__btn" style="width:100%">I'm In For 33 →</button>
</form></div>"""
CSS = """<style>
body{margin:0;background:#0A0606}
.sec{background-size:cover;background-position:center}
.sec--hero{background-image:url(../backgrounds/hero-desktop.jpg)}
@media (max-width:767px){.sec--hero{background-image:url(../backgrounds/hero-mobile.jpg)}}
.sec--dark{background-image:url(../backgrounds/dark-section.jpg)}
.sec--light{background-image:url(../backgrounds/light-section.jpg)}
.mock-form{max-width:520px;margin:16px auto 0;background:#fff;border-radius:14px;padding:24px;display:grid;gap:14px;color:#121212;box-shadow:0 30px 60px -20px rgba(0,0,0,.7)}
.mock-form label{display:grid;gap:6px;font-size:14px;font-weight:600}
.mock-form input{height:52px;border:1px solid #E3D6D7;border-radius:10px;padding:0 14px;font:16px Inter,sans-serif;background:#FBF8F8}
.mock-note{margin:0!important;font-size:12px;color:#B80018;text-align:center;text-transform:uppercase;letter-spacing:.08em;font-weight:700}
</style>"""
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Goat's 33 preview</title>
<style>{(root / "registration" / "00-global-styles.css").read_text()}</style>{CSS}</head><body>
{blk("01")}
<section class="sec sec--hero">{blk("02")}{FORM}{blk("03")}</section>
<section class="sec sec--light">{blk("04")}</section>
<section class="sec sec--dark">{blk("05")}</section>
{blk("06")}
</body></html>"""
(root / "preview" / "registration.html").write_text(page)
print("wrote preview/registration.html")
