# Render favicon & og.png dari logo.svg (butuh playwright)
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
img = Path(__file__).resolve().parent.parent / "src/static/img"
svg = (img / "logo.svg").read_text()
og = f"""<html><body style="margin:0"><div style="width:1200px;height:630px;box-sizing:border-box;padding:80px;color:#fff;font-family:Arial,Helvetica,sans-serif;
background:radial-gradient(700px 400px at 95% -10%,rgba(232,169,12,.35),transparent 60%),linear-gradient(135deg,#0B2E26,#0E5A49 70%,#0E7C66);display:flex;flex-direction:column;justify-content:center">
<div style="display:flex;align-items:center;gap:22px;font-size:58px;font-weight:800"><div style="width:96px;height:96px">{svg}</div><span>Get<span style="color:#E8A90C">Wise</span></span></div>
<div style="font-size:50px;font-weight:800;margin-top:40px;line-height:1.2">Kalkulator PPh 21, Gaji Bersih,<br>BPJS, KPR &amp; Investasi</div>
<div style="font-size:30px;color:#D5EDE5;margin-top:24px">Aturan terbaru 2026 · Gratis · Data tetap di perangkat Anda</div></div></body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for size, name in [(48, "favicon-48.png"), (180, "apple-touch-icon.png"), (512, "icon-512.png")]:
        pg.set_viewport_size({"width": size, "height": size})
        pg.set_content(f'<html><body style="margin:0;background:transparent"><div style="width:{size}px;height:{size}px">{svg}</div></body></html>')
        pg.screenshot(path=str(img / name), omit_background=True)
    pg.set_viewport_size({"width": 1200, "height": 630}); pg.set_content(og); pg.screenshot(path=str(img / "og.png"))
    b.close()
print("ok")
