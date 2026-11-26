"""Bangun situs statis GetWise ke folder dist/.

Pemakaian:  python src/build.py
Ubah CONFIG di bawah (domain, ID AdSense, GA, email) sebelum deploy.
"""
import json
import os
import shutil
import time
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from content import CALCS, CATS, PAGES

ROOT = Path(__file__).resolve().parent
DIST = ROOT.parent / "dist"

CONFIG = dict(
    name1="Get", name2="Wise",
    base=os.environ.get("SITE_BASE", "https://getwise.id").rstrip("/"),   # ganti dengan domain Anda
    adsense=os.environ.get("ADSENSE", ""),        # contoh: ca-pub-7815801753925125
    ga=os.environ.get("GA_ID", ""),               # contoh: G-XXXXXXXXXX
    email=os.environ.get("CONTACT_EMAIL", "halo@getwise.id"),
)
RULES_UPDATED = "27 November 2026"


def main():
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True)
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "static", DIST / "static")
    shutil.copy(ROOT / "static/img/favicon.ico", DIST / "favicon.ico")
    v = str(int(time.time()))
    byid = {c["id"]: c for c in CALCS}
    catmap = {c["id"]: c for c in CATS}
    search = json.dumps([dict(t=c["short"], k=c["title"] + " " + c["desc"], d=c["card"], u=f"/{c['slug']}/") for c in CALCS], ensure_ascii=False)
    common = dict(cfg=CONFIG, cats=CATS, v=v, rules_updated=RULES_UPDATED, search=search)
    org = {"@context": "https://schema.org", "@type": "WebSite", "name": CONFIG["name1"] + CONFIG["name2"], "url": CONFIG["base"] + "/", "inLanguage": "id-ID"}
    urls = []

    def write(path, html):
        out = DIST / path.strip("/") / "index.html" if path != "/" else DIST / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        urls.append(path)

    write("/", env.get_template("index.html").render(
        **common, calcs=CALCS, path="/", page_cat=None, jsonld=[json.dumps(org, ensure_ascii=False)],
        title="GetWise – Kalkulator PPh 21, Gaji Bersih, BPJS, KPR & Investasi 2026",
        description="Kalkulator keuangan Indonesia gratis: PPh 21 metode TER, gaji bersih, THR, iuran BPJS, simulasi KPR, kredit kendaraan, deposito, dan investasi. Aturan terbaru 2026."))

    for c in CALCS:
        path = f"/{c['slug']}/"
        cat = catmap[c["cat"]]
        ld_app = {"@context": "https://schema.org", "@type": "WebApplication", "name": c["h1"], "url": CONFIG["base"] + path, "applicationCategory": "FinanceApplication",
                  "operatingSystem": "Any", "inLanguage": "id-ID", "description": c["desc"], "offers": {"@type": "Offer", "price": "0", "priceCurrency": "IDR"}}
        ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]}
        ld_bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Beranda", "item": CONFIG["base"] + "/"},
            {"@type": "ListItem", "position": 2, "name": cat["name"], "item": CONFIG["base"] + "/#" + cat["id"]},
            {"@type": "ListItem", "position": 3, "name": c["short"], "item": CONFIG["base"] + path}]}
        write(path, env.get_template("calc.html").render(
            **common, c=c, cat=cat, related=[byid[r] for r in c["related"] if r in byid], path=path, page_cat=c["cat"],
            title=c["title"], description=c["desc"], jsonld=[json.dumps(x, ensure_ascii=False) for x in (ld_app, ld_faq, ld_bc)]))

    name = CONFIG["name1"] + CONFIG["name2"]
    for slug, (h1, body) in PAGES.items():
        path = f"/{slug}/"
        write(path, env.get_template("page.html").render(
            **common, path=path, page_cat=None, jsonld=[], h1=h1, title=f"{h1} – {name}", description=f"{h1} {name}, kalkulator keuangan Indonesia.",
            body=body.format(name=name, email=CONFIG["email"], updated=RULES_UPDATED)))

    # 404
    html = env.get_template("page.html").render(**common, path="/404.html", page_cat=None, jsonld=[], h1="Halaman tidak ditemukan", title=f"Halaman tidak ditemukan – {name}",
                                                 description="Halaman tidak ditemukan.", body='<p>Maaf, halaman yang Anda cari tidak ada. Kembali ke <a href="/">beranda</a> untuk melihat semua kalkulator.</p>')
    (DIST / "404.html").write_text(html, encoding="utf-8")

    today = time.strftime("%Y-%m-%d")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"<url><loc>{CONFIG['base']}{u}</loc><lastmod>{today}</lastmod></url>" for u in urls]
    sm.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {CONFIG['base']}/sitemap.xml\n", encoding="utf-8")
    if CONFIG["adsense"]:
        pub = CONFIG["adsense"].replace("ca-", "")
        (DIST / "ads.txt").write_text(f"google.com, {pub}, DIRECT, f08c47fec0942fa0\n", encoding="utf-8")
    # header cache untuk Cloudflare Pages
    (DIST / "_headers").write_text("/static/*\n  Cache-Control: public, max-age=604800\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n", encoding="utf-8")
    print(f"OK: {len(urls)} halaman -> {DIST}")


if __name__ == "__main__":
    main()
