"""Builds preview/*.html from the two paste-ready pages.
The real photos and videos live on GHL's CDN, which this build environment can't reach, so the
preview swaps them for labelled stand-in boxes; the GHL form embed becomes a mock form."""
import re
from pathlib import Path
from urllib.parse import quote
root = Path(__file__).resolve().parent.parent
CDN = "https://assets.cdn.filesafe.space/BU5M3MidcixGHbnmd1on/media/"
LABELS = {"6ad5013c989628c77a615ead": ("Kenny photo", 800, 1000), "69ca10ccbe0ea3271a9700f9": ("Inner Circle 1", 216, 298),
          "69ca10ccbe0ea3c5979700f7": ("Inner Circle 2", 266, 356), "69ca10afcfb25f92dbd1e048": ("Inner Circle 3", 239, 292),
          "6aeac231fb31f444f21758bb": ("Testimonial 1", 900, 1300), "6aeac23134f5791473736d8c": ("Testimonial 2", 900, 1000),
          "6aeac231e322309abfaa6955": ("Testimonial 3", 900, 1500)}
def ph(label, w, h, bg="#C9C9CF"):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"><rect width="100%" height="100%" fill="{bg}"/>'
           f'<text x="50%" y="50%" text-anchor="middle" font-family="Arial" font-size="{w//14}" fill="#555">{label} (stand-in)</text></svg>')
    return "data:image/svg+xml," + quote(svg)
FORM = """<form onsubmit="return false" style="display:grid;gap:12px">
<p style="margin:0;font-size:12px;color:#C20017;text-align:center;text-transform:uppercase;letter-spacing:.08em;font-weight:700">Preview only: your GHL form embed goes here</p>
<input placeholder="First name" style="height:50px;border:1px solid #E3D6D7;border-radius:10px;padding:0 14px;font:16px Inter,sans-serif">
<input placeholder="Email" style="height:50px;border:1px solid #E3D6D7;border-radius:10px;padding:0 14px;font:16px Inter,sans-serif">
<input placeholder="Phone" style="height:50px;border:1px solid #E3D6D7;border-radius:10px;padding:0 14px;font:16px Inter,sans-serif">
<button class="ks-btn" style="width:100%;animation:none">Save My Free Seat →</button></form>"""
def fix(html):
    for key, (label, w, h) in LABELS.items():
        html = re.sub(re.escape(CDN + key) + r"\.\w+", ph(label, w, h), html)
    html = re.sub(r'<video ([^>]*)src="[^"]+"', lambda m: f'<video {m.group(1)}poster="{ph("Video", 1280, 720, "#2A2A30")}"', html)
    html = __import__('re').sub(r'<iframe\s+src="https://api.leadconnectorhq.com.*?</script>', FORM, html, flags=__import__('re').S)
    return html.replace("GHL_FORM_EMBED", FORM).replace("CALENDAR_LINK", "#").replace("SMITTY_LOGO_URL", "../images/smitty-logo.png").replace("HERO_BG_URL", "../images/hero-bg.jpg")
for name in ["landing", "thank-you"]:
    body = fix((root / f"{name}.html").read_text())
    (root / "preview" / f"{name}.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{name} preview</title><style>body{{margin:0}}</style></head><body>{body}</body></html>')
print("built preview/landing.html, preview/thank-you.html")
