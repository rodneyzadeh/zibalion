#!/usr/bin/env python3
"""
Builds /library/ from data/library.csv.

Head, nav and footer are lifted from an existing page rather than hardcoded,
so the generated pages inherit whatever chrome the site currently has.

Images: drop a photo at assets/img/conjuring/<slug>.jpg (or .png / .webp)
and the next build picks it up automatically. No CSV edit needed.

    python3 build-conjuring.py
"""

import csv, os, re, html, sys, unicodedata

SITE    = os.path.expanduser("~/Sites/zibalion")
CSV     = os.path.join(SITE, "data", "library.csv")
SOURCE  = os.path.join(SITE, "process", "index.html")
OUTDIR  = os.path.join(SITE, "library")
IMGDIR  = os.path.join(SITE, "assets", "img", "library")
IMGWEB  = "/assets/img/library"
CSSHREF = "/assets/css/conjuring.css"
BASEURL = "https://zibalion.com/library"

SECTION_TITLE = "The library"
LEDE = "Books on the shelves, grouped by subject."

IMG_EXTS = (".jpg", ".jpeg", ".png", ".webp")


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)


def find_image(slug):
    for ext in IMG_EXTS:
        if os.path.exists(os.path.join(IMGDIR, slug + ext)):
            return f"{IMGWEB}/{slug}{ext}"
    return None


def load_chrome():
    with open(SOURCE, encoding="utf-8") as f:
        src = f.read()
    m = re.search(r"</header>", src)
    if not m:
        sys.exit("No </header> in the donor page.")
    m2 = re.search(r"<footer", src)
    if not m2:
        sys.exit("No <footer> in the donor page.")
    return src[:m.end()], src[m2.start():]


def head_for(head, title, description, canonical, ogtype="website"):
    h = head
    h = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title)}</title>",
               h, flags=re.S)
    for pat in (r'(<meta name="description" content=")[^"]*(")',
                r'(<meta property="og:description" content=")[^"]*(")',
                r'(<meta name="twitter:description" content=")[^"]*(")'):
        h = re.sub(pat, lambda m: m.group(1) + html.escape(description) + m.group(2), h)
    for pat in (r'(<meta property="og:title" content=")[^"]*(")',
                r'(<meta name="twitter:title" content=")[^"]*(")'):
        h = re.sub(pat, lambda m: m.group(1) + html.escape(title) + m.group(2), h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*(")',
               lambda m: m.group(1) + canonical + m.group(2), h)
    h = re.sub(r'(<meta property="og:type" content=")[^"]*(")',
               lambda m: m.group(1) + ogtype + m.group(2), h)
    h = re.sub(r'(<link rel="stylesheet" href=")/assets/css/process\.css[^"]*(")',
               lambda m: m.group(1) + CSSHREF + m.group(2), h)
    return h


def read_rows():
    with open(CSV, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if (r.get("title") or "").strip()]
    for r in rows:
        r["slug"] = slugify(r["title"])
        r["img"] = find_image(r["slug"])
    return rows


def esc(v):
    return html.escape((v or "").strip())


def paras(text):
    return [p.strip() for p in text.split("\n\n") if p.strip()]


def build_index(rows, head, tail):
    sections = []
    for r in rows:
        sec = (r.get("section") or "Other").strip()
        if not sections or sections[-1][0] != sec:
            sections.append((sec, []))
        sections[-1][1].append(r)

    out = [head_for(head, f"{SECTION_TITLE} — Zibalion", LEDE, BASEURL + "/"),
           '\n<main class="cj-wrap">\n',
           f"  <h1>{SECTION_TITLE}</h1>\n",
           f'  <p class="cj-lede">{html.escape(LEDE)}</p>\n']

    for sec, books in sections:
        out.append('  <section class="cj-group">\n')
        out.append(f"    <h2>{esc(sec)}</h2>\n")
        out.append('    <div class="cj-rule"></div>\n')
        cur = None
        for b in books:
            sub = (b.get("subsection") or "").strip()
            if sub != cur:
                if cur is not None:
                    out.append("    </ul>\n")
                cur = sub
                if sub:
                    out.append(f'    <h3 class="cj-h3">{esc(sub)}</h3>\n')
                out.append('    <ul class="cj-list">\n')
            line = f'      <li><a href="/library/{b["slug"]}/">{esc(b["title"])}</a>'
            if (b.get("author") or "").strip():
                line += f' <span class="cj-by">{esc(b["author"])}</span>'
            out.append(line + "</li>\n")
        out.append("    </ul>\n  </section>\n")

    out.append("</main>\n\n")
    out.append(tail)

    os.makedirs(OUTDIR, exist_ok=True)
    with open(os.path.join(OUTDIR, "index.html"), "w", encoding="utf-8") as f:
        f.write("".join(out))


def build_book(b, head, tail):
    d = os.path.join(OUTDIR, b["slug"])
    os.makedirs(d, exist_ok=True)

    title = b["title"].strip()
    author = (b.get("author") or "").strip()
    about = (b.get("about") or "").strip()

    desc = about or f"{title}{' by ' + author if author else ''} in the Zibalion conjuring library."
    desc = re.sub(r"\s+", " ", desc)[:300]

    out = [head_for(head, f"{title} — Zibalion", desc,
                    f"{BASEURL}/{b['slug']}/", ogtype="article"),
           '\n<main class="cj-wrap cj-book">\n',
           f"  <h1>{esc(title)}</h1>\n"]

    if author or (b.get("volumes") or "").strip():
        out.append('  <p class="cj-author">')
        if author:
            out.append(esc(author))
        if (b.get("volumes") or "").strip():
            out.append(f'<span class="cj-vol">{esc(b["volumes"])}</span>')
        out.append("</p>\n")

    sub = (b.get("subsection") or "").strip()
    if sub:
        out.append(f'  <p class="cj-sub">{esc(b["section"])} / {esc(sub)}</p>\n')

    # a photo you took wins; otherwise fall back to the Open Library cover
    cover = b.get("img") or (b.get("cover_url") or "").strip()
    if cover:
        alt = f"{title}" + (f", {author}" if author else "")
        out.append('  <figure class="cj-cover">\n')
        out.append(f'    <img src="{cover}" alt="{esc(alt)}" loading="lazy">\n')
        if not b.get("img"):
            isbn = (b.get("isbn") or "").strip()
            link = f"https://openlibrary.org/isbn/{isbn}" if isbn else "https://openlibrary.org/"
            out.append(f'    <figcaption class="cj-credit">Cover via '
                       f'<a href="{link}" rel="nofollow">Open Library</a></figcaption>\n')
        out.append("  </figure>\n")

    if about:
        out.append('  <div class="cj-body">\n')
        for p in paras(about):
            out.append(f"    <p>{html.escape(p)}</p>\n")
        out.append("  </div>\n")

    fields = [("publisher", "Publisher"), ("imprint", "Imprint"),
              ("year", "Year"), ("edition", "Edition"),
              ("pages", "Pages"), ("format", "Format"),
              ("illustrator", "Illustrations"), ("editor", "Editor"),
              ("isbn", "ISBN")]
    have = [(lab, b[k].strip()) for k, lab in fields if (b.get(k) or "").strip()]
    if have:
        out.append('  <div class="cj-pub">\n    <dl>\n')
        for lab, val in have:
            out.append(f"      <dt>{lab}</dt><dd>{esc(val)}</dd>\n")
        out.append("    </dl>\n  </div>\n")

    note = (b.get("note") or "").strip()
    if note:
        out.append('  <div class="cj-note">\n    <h2>My notes</h2>\n')
        for p in paras(note):
            out.append(f"    <p>{html.escape(p)}</p>\n")
        out.append("  </div>\n")

    gr = (b.get("goodreads") or "").strip()
    if gr:
        out.append('  <p class="cj-out"><a href="' + html.escape(gr) +
                   '" target="_blank" rel="nofollow noopener">See it on Goodreads</a></p>\n')

    out.append(f'  <a class="cj-back" href="/library/">Back to {SECTION_TITLE}</a>\n')
    out.append("</main>\n\n")
    out.append(tail)

    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write("".join(out))


def main():
    if not os.path.exists(CSV):
        sys.exit(f"No CSV at {CSV}")
    os.makedirs(IMGDIR, exist_ok=True)

    head, tail = load_chrome()
    rows = read_rows()

    build_index(rows, head, tail)
    for r in rows:
        build_book(r, head, tail)

    imgs = sum(1 for r in rows if r["img"] or (r.get("cover_url") or "").strip())
    pubs = sum(1 for r in rows if (r.get("publisher") or "").strip())
    notes = sum(1 for r in rows if (r.get("note") or "").strip())

    print(f"Built /library/ and {len(rows)} book pages.")
    print(f"  {imgs} have a cover image")
    print(f"  {pubs} have publisher details")
    print(f"  {notes} have your own notes")
    if imgs < len(rows):
        print(f"\nDrop photos in assets/img/conjuring/ named <slug>.jpg to add covers.")
        missing = [r["slug"] for r in rows if not r["img"]][:5]
        print("  e.g. " + ", ".join(s + ".jpg" for s in missing))


if __name__ == "__main__":
    main()
