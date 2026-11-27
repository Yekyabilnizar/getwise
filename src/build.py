"""Bangun situs statis GetWise (Bahasa Indonesia + English) ke folder dist/.

Pemakaian:  python src/build.py
Ubah CONFIG di bawah (domain, ID AdSense, GA, email) lewat variabel lingkungan saat build.
"""
import copy
import json
import os
import re
import shutil
import time
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from articles import ARTICLES, CHARTS
from articles_en import ART_EN, CHARTS_EN
from articles_more import CLOSE, EXTRA
from articles_more_en import CLOSE_EN, EXTRA_EN
from articles_new import NEW
from articles_new_en import NEW_EN

ARTICLES = ARTICLES + NEW   # artikel gelombang 3
ART_EN.update(NEW_EN)
from content import CALCS, CATS, PAGES
from content_en import CALC_EN, CATS_EN, PAGES_EN
from i18n import CALC_SLUG_EN, GUIDES, LANGS, PAGE_SLUG, PREFIX, T
from photos import photo

ROOT = Path(__file__).resolve().parent
DIST = ROOT.parent / "dist"

CONFIG = dict(
    name1="Get", name2="Wise",
    base=os.environ.get("SITE_BASE", "https://getwise.id").rstrip("/"),   # ganti dengan domain Anda
    adsense=os.environ.get("ADSENSE", ""),          # contoh: ca-pub-7815801753925125
    ga=os.environ.get("GA_ID", ""),                 # contoh: G-XXXXXXXXXX
    gsc=os.environ.get("GSC_VERIFY", ""),           # kode verifikasi Google Search Console (meta tag)
    email=os.environ.get("CONTACT_EMAIL", "halo@getwise.id"),
)
RULES_UPDATED = {"id": "27 November 2026", "en": "27 November 2026"}
CH = re.compile(r"\[\[(CH_\w+)\]\]")


def calc_url(lang, cid, slug_id):
    return f"/{slug_id}/" if lang == "id" else f"/en/{CALC_SLUG_EN[cid]}/"


def art_url(lang, slug_id):
    return f"/panduan/{slug_id}/" if lang == "id" else f"/en/guides/{ART_EN[slug_id]['slug']}/"


def page_url(lang, key):
    return f"/{key}/" if lang == "id" else f"/en/{PAGE_SLUG[key]}/"


def localized(lang):
    """Kembalikan salinan kategori, kalkulator, artikel, dan halaman untuk satu bahasa."""
    cats = copy.deepcopy(CATS)
    calcs = copy.deepcopy(CALCS)
    arts = copy.deepcopy(ARTICLES)
    charts = CHARTS if lang == "id" else CHARTS_EN
    if lang == "en":
        for c in cats:
            c.update(CATS_EN[c["id"]])
        for c in calcs:
            c.update(CALC_EN[c["id"]])
        for a in arts:
            a["id_slug"] = a["slug"]
            a.update({k: v for k, v in ART_EN[a["slug"]].items() if k != "slug"})
    catmap = {c["id"]: c for c in cats}
    byid = {c["id"]: c for c in calcs}
    for c in calcs:
        c["url"] = calc_url(lang, c["id"], CALCS_BY_ID[c["id"]]["slug"])
        c["alt"] = {lg: calc_url(lg, c["id"], CALCS_BY_ID[c["id"]]["slug"]) for lg in LANGS}
        c["photo"] = photo(c["id"])
        if lang == "id":
            c["chip"] = c["short"].replace("Kalkulator ", "").replace("Simulasi ", "")
    extra = EXTRA if lang == "id" else EXTRA_EN
    for a in arts:
        sid = a.get("id_slug", a["slug"])
        add = extra.get(sid, [])
        if add:  # sisipkan bagian tambahan sebelum bagian tips (terakhir)
            a["body"] = list(a["body"][:-1]) + list(add) + [a["body"][-1]]
        close = (CLOSE if lang == "id" else CLOSE_EN).get(sid)
        if close:  # penutup + FAQ tambahan
            a["body"] = list(a["body"]) + [("Kesimpulan" if lang == "id" else "Conclusion", close[0])]
            a["faq"] = list(a.get("faq", [])) + list(close[1])
        a["url"] = art_url(lang, sid)
        a["alt"] = {lg: art_url(lg, sid) for lg in LANGS}
        a["cat"] = byid[a["calc"]]["cat"]
        a["cat_name"] = catmap[a["cat"]]["short"]
        keys = [k for _, b in a["body"] for k in CH.findall(b)]
        a["chart"] = charts[keys[0]] if keys else ""
        a["body"] = [(h, CH.sub(lambda m: charts[m.group(1)], b)) for h, b in a["body"]]
        words = len(re.sub(r"<[^>]+>", " ", " ".join(b for _, b in a["body"])).split())
        a["minutes"] = max(3, round(words / 200))
        key = a.get("photo") if isinstance(a.get("photo"), str) else None
        a["photo"] = photo(key or ("a-" + a["calc"]))
        if lang == "en":
            a["photo"]["credit"] = "Photo"
    if lang == "en":
        for c in calcs:
            c["photo"]["credit"] = "Photo"
    pages = PAGES if lang == "id" else PAGES_EN
    return cats, catmap, calcs, byid, arts, pages


CALCS_BY_ID = {c["id"]: c for c in CALCS}


def main():
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True)
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "static", DIST / "static")
    shutil.copy(ROOT / "static/img/favicon.ico", DIST / "favicon.ico")
    v = str(int(time.time()))
    name = CONFIG["name1"] + CONFIG["name2"]
    urls = []

    def write(path, html):
        out = DIST / path.strip("/") / "index.html" if path != "/" else DIST / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        urls.append(path)

    for lang in LANGS:
        t = T[lang]
        inlang = "id-ID" if lang == "id" else "en"
        cats, catmap, calcs, byid, arts, pages = localized(lang)
        guide_of, guides_of = {}, {}
        for a in arts:
            guide_of.setdefault(a["calc"], a)
            guides_of.setdefault(a["calc"], []).append(a)
        home_url = PREFIX[lang] + "/"
        purl = {k: page_url(lang, k) for k in PAGE_SLUG}
        word = "panduan tips" if lang == "id" else "guide tips"
        search = json.dumps([dict(t=c["short"], k=c["title"] + " " + c["desc"], d=c["card"], u=c["url"]) for c in calcs]
                            + [dict(t=a["h1"], k=a["title"] + " " + a["desc"] + " " + word, d=t["guides"] + " · " + a["cat_name"], u=a["url"]) for a in arts],
                            ensure_ascii=False)
        common = dict(cfg=CONFIG, cats=cats, v=v, rules_updated=RULES_UPDATED[lang], search=search, all_calcs=calcs, all_articles=arts,
                      foot_articles=arts[::-1][:6], t=t, lang=lang, home_url=home_url, guides_url=GUIDES[lang], purl=purl)
        org = {"@context": "https://schema.org", "@type": "WebSite", "name": name, "url": CONFIG["base"] + home_url, "inLanguage": inlang}

        write(home_url, env.get_template("index.html").render(
            **common, calcs=calcs, articles=arts[::-1][:8], n_articles=len(arts), p=photo("home") | ({"credit": "Photo"} if lang == "en" else {}),
            city=photo("city") | ({"credit": "Photo"} if lang == "en" else {}), thp_url=byid["gaji-bersih"]["url"],
            path=home_url, alt={lg: PREFIX[lg] + "/" for lg in LANGS}, page_cat=None, jsonld=[json.dumps(org, ensure_ascii=False)],
            title=t["home_title"], description=t["home_desc"]))

        for c in calcs:
            path, cat = c["url"], catmap[c["cat"]]
            ld_app = {"@context": "https://schema.org", "@type": "WebApplication", "name": c["h1"], "url": CONFIG["base"] + path, "applicationCategory": "FinanceApplication",
                      "operatingSystem": "Any", "inLanguage": inlang, "description": c["desc"], "offers": {"@type": "Offer", "price": "0", "priceCurrency": "IDR"}}
            ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]}
            ld_bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": t["home"], "item": CONFIG["base"] + home_url},
                {"@type": "ListItem", "position": 2, "name": cat["name"], "item": CONFIG["base"] + home_url + "#" + cat["id"]},
                {"@type": "ListItem", "position": 3, "name": c["short"], "item": CONFIG["base"] + path}]}
            g = guide_of.get(c["id"])
            write(path, env.get_template("calc.html").render(
                **common, c=c, cat=cat, related=[byid[r] for r in c["related"] if r in byid], guide=g, guides=guides_of.get(c["id"], []),
                p=c["photo"], chart=g["chart"] if g else "", path=path, alt=c["alt"], page_cat=c["cat"],
                title=c["title"], description=c["desc"], jsonld=[json.dumps(x, ensure_ascii=False) for x in (ld_app, ld_faq, ld_bc)]))

        pg = photo("panduan") | ({"credit": "Photo"} if lang == "en" else {})
        write(GUIDES[lang], env.get_template("guides.html").render(
            **common, articles=arts, p=pg, path=GUIDES[lang], alt=GUIDES, page_cat="panduan", jsonld=[],
            title=f"{t['guides_title']} – {name}", description=t["guides_desc"]))
        for a in arts:
            path = a["url"]
            ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"], "inLanguage": inlang,
                  "image": CONFIG["base"] + "/static/img/og.png", "dateModified": "2026-11-27", "author": {"@type": "Organization", "name": name},
                  "publisher": {"@type": "Organization", "name": name, "logo": {"@type": "ImageObject", "url": CONFIG["base"] + "/static/img/icon-512.png"}},
                  "mainEntityOfPage": CONFIG["base"] + path}
            others = ([x for x in arts if x is not a and x["cat"] == a["cat"]] + [x for x in arts if x is not a and x["cat"] != a["cat"]])[:5]
            write(path, env.get_template("article.html").render(
                **common, a=a, p=a["photo"], calc=byid[a["calc"]], others=others, path=path, alt=a["alt"], page_cat="panduan",
                title=a["title"], description=a["desc"], jsonld=[json.dumps(ld, ensure_ascii=False)]))

        pc = photo("city") | ({"credit": "Photo"} if lang == "en" else {})
        for key, (h1, body) in pages.items():
            path = purl[key]
            desc = f"{h1} – {name}, " + ("kalkulator keuangan Indonesia." if lang == "id" else "Indonesian finance calculators.")
            write(path, env.get_template("page.html").render(
                **common, p=pc, path=path, alt={lg: page_url(lg, key) for lg in LANGS}, page_cat=None, jsonld=[], h1=h1,
                title=f"{h1} – {name}", description=desc,
                body=body.format(name=name, email=CONFIG["email"], updated=RULES_UPDATED[lang], fb=purl["masukan"], home=home_url)))

        path = purl["masukan"]
        write(path, env.get_template("masukan.html").render(
            **common, p=pg, path=path, alt={lg: page_url(lg, "masukan") for lg in LANGS}, page_cat="masukan", jsonld=[],
            title=f"{t['fb_title']} – {name}", description=f"{t['fb_desc']} {name}."))

        html = env.get_template("page.html").render(**common, p=pc, path=PREFIX[lang] + "/404.html", alt={lg: PREFIX[lg] + "/" for lg in LANGS}, page_cat=None,
                                                     jsonld=[], h1=t["nf_h1"], title=f"{t['nf_h1']} – {name}", description=t["nf_h1"], body=t["nf_body"])
        (DIST / PREFIX[lang].strip("/") / "404.html").write_text(html, encoding="utf-8")

    today = time.strftime("%Y-%m-%d")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"<url><loc>{CONFIG['base']}{u}</loc><lastmod>{today}</lastmod></url>" for u in urls]
    sm.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {CONFIG['base']}/sitemap.xml\n", encoding="utf-8")
    if CONFIG["adsense"]:
        pub = CONFIG["adsense"].replace("ca-", "")
        (DIST / "ads.txt").write_text(f"google.com, {pub}, DIRECT, f08c47fec0942fa0\n", encoding="utf-8")
    (DIST / "_headers").write_text("/static/*\n  Cache-Control: public, max-age=604800\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n", encoding="utf-8")
    print(f"OK: {len(urls)} halaman -> {DIST}")


if __name__ == "__main__":
    main()
