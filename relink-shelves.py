#!/usr/bin/env python3
"""
Rewrites the shelf lists in process/index.html:

  * every Goodreads link becomes a link to that book's own page under /library/
  * the counts in each <summary> are recomputed from the data
  * a Conjuring Arts group is added, built from data/conjuring-arts.csv

Backs up first. Safe to run repeatedly: already-rewritten links are left alone
and the Conjuring Arts block is replaced rather than duplicated.

    python3 relink-shelves.py
"""

import csv, html, os, re, shutil, sys, time, unicodedata

SITE = os.path.expanduser("~/Sites/zibalion")
PAGE = os.path.join(SITE, "process", "index.html")
LIB  = os.path.join(SITE, "data", "library.csv")
CONJ = os.path.join(SITE, "data", "conjuring-arts.csv")

MARK_START = "<!-- ==== ZB-CONJURING START ==== -->"
MARK_END   = "<!-- ==== ZB-CONJURING END ==== -->"


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)


def load(path):
    if not os.path.exists(path):
        sys.exit(f"No {path}")
    with open(path, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if (r.get("title") or "").strip()]


def main():
    if not os.path.exists(PAGE):
        sys.exit(f"No {PAGE}")

    lib = load(LIB)
    conj = load(CONJ)

    # title -> slug, matched on the label text in the page
    by_title = {}
    for r in lib:
        by_title[re.sub(r"\s+", " ", r["title"]).strip().lower()] = slugify(r["title"])

    src = open(PAGE, encoding="utf-8").read()
    shutil.copy(PAGE, PAGE + ".bak-" + time.strftime("%Y%m%d-%H%M%S"))

    relinked = [0]
    missed = []

    def swap(m):
        attrs, label = m.group(1), m.group(2)
        if "goodreads.com" not in attrs:
            return m.group(0)

        text = html.unescape(re.sub(r"<[^>]+>", "", label)).strip()
        text = re.sub(r"\s+", " ", text)

        title = text
        for dash in ("\u2014", "\u2013", " - "):
            if dash in text:
                title = text.split(dash, 1)[1].strip()
                break

        slug = by_title.get(title.lower())
        if not slug:
            missed.append(title)
            return m.group(0)

        relinked[0] += 1
        return f'<li><a href="/library/{slug}/">{label}</a></li>'

    src = re.sub(r"<li>\s*<a([^>]*)>(.*?)</a>\s*</li>", swap, src, flags=re.S)

    # recompute the counts in each summary
    counts = {}
    for r in lib:
        counts[r["section"]] = counts.get(r["section"], 0) + 1

    def fixcount(m):
        name = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        n = counts.get(name)
        if n is None:
            return m.group(0)
        return f'<summary>{html.escape(name)}<span class="pr-count">{n}</span></summary>'

    src = re.sub(r"<summary>(.*?)</summary>", fixcount, src, flags=re.S)

    # build the Conjuring Arts group
    groups = []
    for r in conj:
        sec = (r.get("section") or "Other").strip()
        if not groups or groups[-1][0] != sec:
            groups.append((sec, []))
        groups[-1][1].append(r)

    block = [MARK_START, '<details class="pr-shelfgroup">',
             f'<summary>Conjuring Arts<span class="pr-count">{len(conj)}</span></summary>']
    for sec, books in groups:
        block.append(f'<div class="pr-sub"><h4>{html.escape(sec)}</h4><ul>')
        for b in books:
            label = html.escape(b["title"])
            if (b.get("author") or "").strip():
                label = html.escape(b["author"]) + " \u2014 " + label
            block.append(f'<li><a href="/conjuring-arts/{slugify(b["title"])}/">{label}</a></li>')
        block.append("</ul></div>")
    block.append("</details>")
    block.append(MARK_END)
    blocktext = "\n".join(block)

    if MARK_START in src:
        src = re.sub(re.escape(MARK_START) + r".*?" + re.escape(MARK_END),
                     blocktext, src, flags=re.S)
        placed = "replaced"
    else:
        # after the last shelfgroup, inside the shelves div
        last = None
        for m in re.finditer(r"</details>", src):
            last = m
        if not last:
            sys.exit("No </details> found. Nothing written beyond the link swap.")
        src = src[:last.end()] + "\n" + blocktext + src[last.end():]
        placed = "added"

    open(PAGE, "w", encoding="utf-8").write(src)

    print(f"Relinked {relinked[0]} books to their own pages.")
    print(f"Conjuring Arts group {placed}: {len(conj)} titles.")
    print("Counts recomputed: " + ", ".join(f"{k} {v}" for k, v in counts.items()))
    if missed:
        print(f"\n{len(missed)} labels had no matching row and were left pointing at Goodreads:")
        for t in missed[:12]:
            print("  " + t)


if __name__ == "__main__":
    main()
