#!/usr/bin/env python3
"""
Builds /art/ from data/art.csv, borrowing the site's real head, nav and footer
from process/index.html so it always matches the rest of the site.

An image shows for a work whenever a file named after its slug exists in
assets/img/art/. Otherwise it renders as a text entry.

    python3 build-art.py
"""
import csv, html, os, re, sys, unicodedata, urllib.parse

SITE    = os.path.expanduser("~/Sites/zibalion")
CSV     = os.path.join(SITE, "data", "art.csv")
SOURCE  = os.path.join(SITE, "process", "index.html")
OUT     = os.path.join(SITE, "art")
IMGDIR  = os.path.join(SITE, "assets", "img", "art")
IMGWEB  = "/assets/img/art"
CSSHREF = "/assets/css/art.css"
BASE    = "https://zibalion.com/art"
TITLE   = "Art"
LEDE    = "Paintings I keep coming back to."
EXTS    = (".jpg", ".jpeg", ".png", ".webp")


def slugify(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"[\s_]+", "-", t)


def esc(v):
    return html.escape((v or "").strip())


def image_for(slug):
    for e in EXTS:
        if os.path.exists(os.path.join(IMGDIR, slug + e)):
            return f"{IMGWEB}/{slug}{e}"
    return None


def chrome():
    src = open(SOURCE, encoding="utf-8").read()
    a, b = src.find("</header>"), src.find("<footer")
    if a < 0 or b < 0:
        sys.exit("Could not find </header> and <footer> in the donor page.")
    return src[:a + len("</header>")], src[b:]


def head_for(head, title, desc, canon, ogtype="website", ogimg=None):
    h = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title)}</title>", head, flags=re.S)
    for p in (r'(<meta name="description" content=")[^"]*(")',
              r'(<meta property="og:description" content=")[^"]*(")',
              r'(<meta name="twitter:description" content=")[^"]*(")'):
        h = re.sub(p, lambda m: m.group(1) + html.escape(desc) + m.group(2), h)
    for p in (r'(<meta property="og:title" content=")[^"]*(")',
              r'(<meta name="twitter:title" content=")[^"]*(")'):
        h = re.sub(p, lambda m: m.group(1) + html.escape(title) + m.group(2), h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + canon + m.group(2), h)
    h = re.sub(r'(<meta property="og:type" content=")[^"]*(")', lambda m: m.group(1) + ogtype + m.group(2), h)
    if ogimg:
        full = "https://zibalion.com" + ogimg
        h = re.sub(r'(<meta property="og:image" content=")[^"]*(")', lambda m: m.group(1) + full + m.group(2), h)
        h = re.sub(r'(<meta name="twitter:image" content=")[^"]*(")', lambda m: m.group(1) + full + m.group(2), h)
    h = re.sub(r'(<link rel="stylesheet" href=")/assets/css/process\.css[^"]*(")',
               lambda m: m.group(1) + CSSHREF + m.group(2), h)
    return h


def byline(r):
    bits = [esc(r["artist"])]
    if (r.get("year") or "").strip():
        bits.append(esc(r["year"]))
    return ", ".join(bits)


def credit(r):
    pd = (r.get("public_domain") or "").strip().lower() == "y"
    f = (r.get("commons_file") or "").strip()
    if pd and f:
        link = "https://commons.wikimedia.org/wiki/File:" + urllib.parse.quote(f.replace(" ", "_"))
        return f'Image: <a href="{link}" rel="nofollow">Wikimedia Commons</a>, public domain.'
    if pd:
        return "Public domain."
    return "&copy; The artist or the artist&rsquo;s estate."


def build_index(rows, head, tail):
    groups = []
    for r in rows:
        g = (r.get("group") or "Other").strip()
        if not groups or groups[-1][0] != g:
            groups.append((g, []))
        groups[-1][1].append(r)

    out = [head_for(head, f"{TITLE} — Zibalion", LEDE, BASE + "/"),
           '\n<main class="art-wrap">\n',
           f'  <h1>{TITLE}</h1>\n  <p class="art-lede">{html.escape(LEDE)}</p>\n']

    for g, works in groups:
        out.append(f'  <section class="art-group">\n    <h2>{esc(g)}</h2>\n    <div class="art-grid">\n')
        for r in works:
            href = f'/art/{r["slug"]}/'
            if r["img"]:
                out.append(f'      <a class="art-card" href="{href}">'
                           f'<img src="{r["img"]}" alt="{esc(r["title"])}, {esc(r["artist"])}" loading="lazy">'
                           f'<span class="art-t">{esc(r["title"])}</span>'
                           f'<span class="art-b">{byline(r)}</span></a>\n')
            else:
                out.append(f'      <a class="art-card art-text" href="{href}">'
                           f'<span class="art-t">{esc(r["title"])}</span>'
                           f'<span class="art-b">{byline(r)}</span></a>\n')
        out.append("    </div>\n  </section>\n")

    out.append("</main>\n\n")
    out.append(tail)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write("".join(out))


def build_page(r, head, tail):
    d = os.path.join(OUT, r["slug"])
    os.makedirs(d, exist_ok=True)
    about = (r.get("about") or "").strip()
    desc = re.sub(r"\s+", " ", about or f'{r["title"]} by {r["artist"]}.')[:300]
    title = f'{r["title"]}, {r["artist"]} — Zibalion'

    out = [head_for(head, title, desc, f'{BASE}/{r["slug"]}/', "article", r["img"]),
           '\n<main class="art-wrap art-work">\n']
    if r["img"]:
        out.append(f'  <figure class="art-plate"><img src="{r["img"]}" '
                   f'alt="{esc(r["title"])}, {esc(r["artist"])}"></figure>\n')
    out.append(f'  <h1>{esc(r["title"])}</h1>\n  <p class="art-by">{byline(r)}</p>\n')
    if (r.get("location") or "").strip():
        out.append(f'  <p class="art-where">{esc(r["location"])}</p>\n')
    if about:
        out.append(f'  <div class="art-body"><p>{html.escape(about)}</p></div>\n')

    note = (r.get("note") or "").strip()
    if note:
        out.append('  <div class="art-note">\n    <h2>Why it stays with me</h2>\n')
        for p in [p for p in note.split("\n\n") if p.strip()]:
            out.append(f"    <p>{html.escape(p.strip())}</p>\n")
        out.append("  </div>\n")

    q = urllib.parse.quote_plus(f'{r["title"]} {r["artist"]}')
    out.append(f'  <p class="art-more"><a href="https://en.wikipedia.org/wiki/Special:Search?search={q}" '
               f'rel="nofollow noopener" target="_blank">Read more about this work</a></p>\n')
    if r["img"]:
        out.append(f'  <p class="art-credit">{credit(r)}</p>\n')
    out.append(f'  <a class="art-back" href="/art/">Back to {TITLE}</a>\n</main>\n\n')
    out.append(tail)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write("".join(out))


def main():
    if not os.path.exists(CSV):
        sys.exit(f"No {CSV}")
    head, tail = chrome()
    rows = [r for r in csv.DictReader(open(CSV, encoding="utf-8")) if (r.get("title") or "").strip()]
    seen = set()
    for r in rows:
        r["slug"] = slugify(r["title"])
        if r["slug"] in seen:
            sys.exit(f'Two works share the slug {r["slug"]}. Rename one.')
        seen.add(r["slug"])
        r["img"] = image_for(r["slug"])
    hidden = [r["title"] for r in rows if not r["img"]]
    rows = [r for r in rows if r["img"]]
    # start clean so pages for hidden works don't linger at old URLs
    import shutil
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    build_index(rows, head, tail)
    for r in rows:
        build_page(r, head, tail)
    n = sum(1 for r in rows if r["img"])
    print(f"Built /art/ with {len(rows)} works.")
    if hidden:
        print(f"{len(hidden)} hidden until they have an image: " + ", ".join(hidden))


if __name__ == "__main__":
    main()
