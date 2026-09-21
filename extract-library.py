#!/usr/bin/env python3
"""
Reads the shelf lists out of process/index.html and writes data/library.csv.

Nothing is modified. Run it once to create the CSV, then the CSV is the
source of truth and this script is only needed if you add books to the old
lists by hand.

    python3 extract-library.py
"""

import csv, html, os, re, sys, unicodedata

SITE = os.path.expanduser("~/Sites/zibalion")
SRC  = os.path.join(SITE, "process", "index.html")
OUT  = os.path.join(SITE, "data", "library.csv")

COLS = ["id", "section", "subsection", "title", "author", "goodreads",
        "publisher", "imprint", "year", "edition", "pages", "format",
        "illustrator", "editor", "isbn", "cover_url", "about", "note"]


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)


def main():
    if not os.path.exists(SRC):
        sys.exit(f"No {SRC}")
    if os.path.exists(OUT):
        sys.exit(f"{OUT} already exists. Delete it first if you really want to "
                 f"regenerate, but you will lose anything you have typed into it.")

    src = open(SRC, encoding="utf-8").read()

    rows = []
    # each <details class="pr-shelfgroup"> ... </details> is a top-level subject
    for grp in re.finditer(
            r'<details class="pr-shelfgroup">(.*?)</details>', src, re.S):
        body = grp.group(1)

        m = re.search(r"<summary>(.*?)(?:<span[^>]*>.*?</span>)?</summary>", body, re.S)
        section = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else "Other"

        # each <div class="pr-sub"><h4>Name</h4><ul> ... </ul></div>
        for sub in re.finditer(
                r'<div class="pr-sub"><h4>(.*?)</h4>\s*<ul>(.*?)</ul>', body, re.S):
            subsection = html.unescape(sub.group(1)).strip()
            for li in re.finditer(r"<li>\s*<a([^>]*)>(.*?)</a>\s*</li>",
                                  sub.group(2), re.S):
                attrs, label = li.group(1), li.group(2)

                href = ""
                h = re.search(r'href="([^"]*)"', attrs)
                if h:
                    href = html.unescape(h.group(1))

                text = html.unescape(re.sub(r"<[^>]+>", "", label)).strip()
                text = re.sub(r"\s+", " ", text)

                # "Author — Title" where the dash is present
                author, title = "", text
                for dash in ("\u2014", "\u2013", " - "):
                    if dash in text:
                        a, t = text.split(dash, 1)
                        author, title = a.strip(), t.strip()
                        break

                if not title:
                    continue

                rows.append({
                    "section": section, "subsection": subsection,
                    "title": title, "author": author, "goodreads": href,
                })

    if not rows:
        sys.exit("Parsed nothing. The markup may differ from what was expected.")

    # unique slugs so no page overwrites another
    seen = {}
    for i, r in enumerate(rows, 1):
        r["id"] = i
        s = slugify(r["title"])
        seen[s] = seen.get(s, 0) + 1
        if seen[s] > 1:
            r["_dupe"] = f"{s} ({seen[s]})"

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in COLS})

    sections = {}
    for r in rows:
        sections[r["section"]] = sections.get(r["section"], 0) + 1

    print(f"Wrote {OUT} with {len(rows)} books.\n")
    for s, n in sections.items():
        print(f"  {n:>4}  {s}")

    dupes = [r["_dupe"] for r in rows if "_dupe" in r]
    if dupes:
        print(f"\n{len(dupes)} duplicate titles. They will need distinct slugs:")
        for d in dupes[:10]:
            print("  " + d)
    noauth = sum(1 for r in rows if not r["author"])
    if noauth:
        print(f"\n{noauth} rows have no author (no dash in the original label).")


if __name__ == "__main__":
    main()
