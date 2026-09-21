#!/usr/bin/env python3
"""
Looks up each book in data/conjuring-arts.csv against Open Library and fills in
cover_url, isbn, publisher and year where a confident match is found.

Nothing is downloaded. Open Library asks that covers be hotlinked from
covers.openlibrary.org rather than rehosted, so the CSV stores the URL and the
page links straight to them.

Existing values are never overwritten. Run it, look at the hit rate, fix
anything wrong by hand, run it again if you like.

    python3 fetch-covers.py           # live
    python3 fetch-covers.py --dry     # show matches without writing
"""

import csv, json, os, ssl, sys, time, urllib.parse, urllib.request

# macOS python installs often ship without root certificates
try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    CTX = ssl.create_default_context()

SITE = os.path.expanduser("~/Sites/zibalion")
CSV  = os.path.join(SITE, "data", "conjuring-arts.csv")
UA   = "zibalion.com book catalogue (contact: rodney@zibalion.com)"
DRY  = "--dry" in sys.argv

SEARCH = "https://openlibrary.org/search.json"


def query(title, author):
    params = {"title": title, "limit": 5,
              "fields": "title,author_name,first_publish_year,publisher,isbn,cover_i"}
    if author:
        params["author"] = author
    url = SEARCH + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
            return json.load(r).get("docs", [])
    except Exception as e:
        print(f"    lookup failed: {e}")
        return []


def norm(s):
    return "".join(c for c in (s or "").lower() if c.isalnum())


def surname(author):
    a = author.split("/")[0].split("&")[0].strip()
    parts = [p for p in a.replace(".", " ").split() if len(p) > 2]
    return norm(parts[-1]) if parts else ""


def pick(docs, title, author):
    """Exact title match only. If we know the author, they must appear too.

    Prefix matching was letting through 'Apocalypse delayed' for 'Apocalypse',
    so it is gone. A miss is cheap. A wrong book on your own catalogue is not.
    """
    t = norm(title)
    sn = surname(author)
    for d in docs:
        if norm(d.get("title", "")) != t:
            continue
        if sn:
            names = norm(" ".join(d.get("author_name", []) or []))
            if sn not in names:
                continue
        return d
    return None


def main():
    if not os.path.exists(CSV):
        sys.exit(f"No CSV at {CSV}")

    with open(CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        cols = list(rows[0].keys())

    if "cover_url" not in cols:
        cols.append("cover_url")
        for r in rows:
            r["cover_url"] = ""

    hits = 0
    for i, r in enumerate(rows, 1):
        title = (r.get("title") or "").strip()
        author = (r.get("author") or "").strip()
        if not title:
            continue
        if (r.get("cover_url") or "").strip():
            hits += 1
            continue

        # strip the "/ Stephen Minch" style co-credits for the lookup
        a = author.split("/")[0].split("&")[0].strip()

        print(f"[{i}/{len(rows)}] {title}")
        d = pick(query(title, a), title, author)
        if not d and a:
            d = pick(query(title, ""), title, author)

        if not d:
            print("    no match")
            time.sleep(0.6)
            continue

        found = []
        if d.get("cover_i"):
            r["cover_url"] = f"https://covers.openlibrary.org/b/id/{d['cover_i']}-L.jpg"
            found.append("cover")
        if d.get("isbn") and not (r.get("isbn") or "").strip():
            r["isbn"] = d["isbn"][0]
            found.append("isbn")
        if d.get("publisher") and not (r.get("publisher") or "").strip():
            r["publisher"] = d["publisher"][0]
            found.append("publisher")
        if d.get("first_publish_year") and not (r.get("year") or "").strip():
            r["year"] = str(d["first_publish_year"])
            found.append("year")

        if found:
            hits += 1
            flag = "" if surname(author) else "   [no author to verify against - check this one]"
            print(f"    matched \"{d.get('title')}\" -> {', '.join(found)}{flag}")
        else:
            print("    matched but nothing useful attached")
        time.sleep(0.6)

    print(f"\n{hits} of {len(rows)} rows now have something from Open Library.")

    if DRY:
        print("Dry run, nothing written.")
        return

    with open(CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})
    print(f"Wrote {CSV}")
    print("Check it before rebuilding. Wrong matches are easier to fix now than later.")


if __name__ == "__main__":
    main()
