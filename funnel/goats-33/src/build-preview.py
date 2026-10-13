"""Stitches the GHL blocks into preview pages, the way GHL will stack them.
The form in the waitlist row is a stand-in for GHL's native form element."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
PHOTO = "../images/smitty-hero.jpg"
def blk(folder, n):
    return next((root / folder).glob(f"{n}-*.html")).read_text().replace("SMITTY_PHOTO_URL", PHOTO).replace("SMITTY_WHY_PHOTO_URL", PHOTO)
reg = lambda n: blk("registration", n)
ty = lambda n: blk("thank-you", n)
FORM = """<form class="mock-form" onsubmit="return false">
  <p class="mock-note">Preview only: GHL's native form goes here</p>
  <label>First name<input placeholder="First name" autocomplete="given-name"></label>
  <label>Email<input type="email" placeholder="you@example.com" autocomplete="email"></label>
  <label>Phone (optional)<input type="tel" placeholder="(312) 555-0133" autocomplete="tel"></label>
  <button class="wf__btn" style="width:100%;font-family:Poppins,sans-serif">I'm In For 33 →</button>
</form>"""
CSS = """<style>
body{margin:0;background:#fff}
.mock-hero{background:#FFF5F5 url(../backgrounds/hero-section.jpg) center top/cover no-repeat}
.mock-row{background:#fff;padding:0 16px 80px}
.mock-row__in{max-width:1000px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}
@media (max-width:760px){.mock-row__in{grid-template-columns:1fr}}
.mock-form{background:#fff;border:1px solid #ECE4E4;border-radius:16px;padding:24px;display:grid;gap:14px;color:#111;font-family:Inter,sans-serif;box-shadow:0 24px 50px -30px rgba(0,0,0,.4)}
.mock-form label{display:grid;gap:6px;font-size:14px;font-weight:600}
.mock-form input{height:52px;border:1px solid #E3D6D7;border-radius:10px;padding:0 14px;font:16px Inter,sans-serif;background:#FBF8F8}
.mock-note{margin:0;font-size:12px;color:#C20017;text-align:center;text-transform:uppercase;letter-spacing:.08em;font-weight:700}
</style>"""
def page(title, body):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<style>{(root / "registration" / "00-global-styles.css").read_text()}</style>{CSS}</head><body>
{body}
</body></html>"""
(root / "preview" / "registration.html").write_text(page("Goat's 33 preview", "\n".join([
    reg("01"), f'<div class="mock-hero">{reg("02")}</div>', reg("03"), reg("04"), reg("05"),
    f'<div class="mock-row"><div class="mock-row__in"><div>{reg("06")}</div>{FORM}</div></div>',
    reg("07"), reg("08"), reg("09")])))
(root / "preview" / "thank-you.html").write_text(page("Goat's 33 thank-you preview", "\n".join([
    ty("01"), f'<div class="mock-hero">{ty("02")}</div>', ty("03"), ty("04"), reg("09")])))
print("wrote preview/registration.html, preview/thank-you.html")
