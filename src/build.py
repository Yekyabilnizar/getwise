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

import re

from articles import ARTICLES, CHARTS
from content import CALCS, CATS, PAGES
from photos import photo

ROOT = Path(__file__).resolve().parent
DIST = ROOT.parent / "dist"

CONFIG = dict(
    name1="Get", name2="Wise",
    base=os.environ.get("SITE_BASE", "https://getwise.id").rstrip("/"),   # ganti dengan domain Anda
    adsense=os.environ.get("ADSENSE", ""),        # contoh: ca-pub-7815801753925125
    ga=os.environ.get("GA_ID", ""),
    gsc=os.environ.get("GSC_VERIFY", ""),           # kode verifikasi Google Search Console (meta tag)               # contoh: G-XXXXXXXXXX
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
    ARTICLES_RAW = {a["slug"]: list(a["body"]) for a in ARTICLES}
    # siapkan artikel: kategori, waktu baca, grafik
    for a in ARTICLES:
        a["cat"] = byid[a["calc"]]["cat"]
        a["cat_name"] = catmap[a["cat"]]["short"]
        a["body"] = [(h, re.sub(r"\[\[(CH_\w+)\]\]", lambda m: CHARTS[m.group(1)], b)) for h, b in a["body"]]
        words = len(re.sub(r"<[^>]+>", " ", " ".join(b for _, b in a["body"])).split())
        a["minutes"] = max(3, round(words / 200))
        a["chart"] = next((CHARTS[k] for _, b in ARTICLES_RAW[a["slug"]] for k in re.findall(r"\[\[(CH_\w+)\]\]", b)), "")
    guide_of, guides_of = {}, {}
    for a in ARTICLES:
        guide_of.setdefault(a["calc"], a)
        guides_of.setdefault(a["calc"], []).append(a)
    for c in CALCS:
        c["photo"] = photo(c["id"])
    for a in ARTICLES:
        a["photo"] = photo(a.get("photo", "a-" + a["calc"])) if isinstance(a.get("photo", ""), str) else a["photo"]
    search = json.dumps([dict(t=c["short"], k=c["title"] + " " + c["desc"], d=c["card"], u=f"/{c['slug']}/") for c in CALCS]
                        + [dict(t=a["h1"], k=a["title"] + " " + a["desc"] + " panduan tips", d="Panduan · " + a["cat_name"], u=f"/panduan/{a['slug']}/") for a in ARTICLES], ensure_ascii=False)
    common = dict(cfg=CONFIG, cats=CATS, v=v, rules_updated=RULES_UPDATED, search=search, all_calcs=CALCS, all_articles=ARTICLES, foot_articles=ARTICLES[::-1][:6])
    org = {"@context": "https://schema.org", "@type": "WebSite", "name": CONFIG["name1"] + CONFIG["name2"], "url": CONFIG["base"] + "/", "inLanguage": "id-ID"}
    urls = []

    def write(path, html):
        out = DIST / path.strip("/") / "index.html" if path != "/" else DIST / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        urls.append(path)

    write("/", env.get_template("index.html").render(
        **common, calcs=CALCS, articles=ARTICLES[::-1][:8], n_articles=len(ARTICLES), p=photo("home"), city=photo("city"), path="/", page_cat=None, jsonld=[json.dumps(org, ensure_ascii=False)],
        title="GetWise – Kalkulator & Panduan PPh 21, Gaji Bersih, BPJS, KPR, Investasi 2026",
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
            **common, c=c, cat=cat, related=[byid[r] for r in c["related"] if r in byid], guide=guide_of.get(c["id"]), guides=guides_of.get(c["id"], []), p=c["photo"], chart=guide_of.get(c["id"], {}).get("chart", ""), path=path, page_cat=c["cat"],
            title=c["title"], description=c["desc"], jsonld=[json.dumps(x, ensure_ascii=False) for x in (ld_app, ld_faq, ld_bc)]))

    name = CONFIG["name1"] + CONFIG["name2"]
    write("/panduan/", env.get_template("guides.html").render(
        **common, articles=ARTICLES, p=photo("panduan"), path="/panduan/", page_cat="panduan", jsonld=[], title=f"Panduan & Tips Keuangan – {name}",
        description="Panduan keuangan berbahasa Indonesia: PPh 21 dan TER, slip gaji, THR, BPJS, KPR, kredit kendaraan, deposito, dan investasi rutin."))
    for a in ARTICLES:
        path = f"/panduan/{a['slug']}/"
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"], "inLanguage": "id-ID",
              "image": CONFIG["base"] + "/static/img/og.png", "dateModified": "2026-11-27", "author": {"@type": "Organization", "name": name},
              "publisher": {"@type": "Organization", "name": name, "logo": {"@type": "ImageObject", "url": CONFIG["base"] + "/static/img/icon-512.png"}},
              "mainEntityOfPage": CONFIG["base"] + path}
        write(path, env.get_template("article.html").render(
            **common, a=a, p=a["photo"], calc=byid[a["calc"]], others=([x for x in ARTICLES if x is not a and x["cat"] == a["cat"]] + [x for x in ARTICLES if x is not a and x["cat"] != a["cat"]])[:5], path=path, page_cat="panduan",
            title=a["title"], description=a["desc"], jsonld=[json.dumps(ld, ensure_ascii=False)]))
    for slug, (h1, body) in PAGES.items():
        path = f"/{slug}/"
        write(path, env.get_template("page.html").render(
            **common, p=photo("city"), path=path, page_cat=None, jsonld=[], h1=h1, title=f"{h1} – {name}", description=f"{h1} {name}, kalkulator keuangan Indonesia.",
            body=body.format(name=name, email=CONFIG["email"], updated=RULES_UPDATED)))

    write("/masukan/", env.get_template("masukan.html").render(
        **common, p=photo("panduan"), path="/masukan/", page_cat=None, jsonld=[], title=f"Kirim Masukan – {name}",
        description=f"Kirim saran, laporan kesalahan hitung, atau usulan kalkulator baru untuk {name}."))

    # 404
    html = env.get_template("page.html").render(**common, p=photo("city"), path="/404.html", page_cat=None, jsonld=[], h1="Halaman tidak ditemukan", title=f"Halaman tidak ditemukan – {name}",
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
