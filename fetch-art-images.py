#!/usr/bin/env python3
"""
Finds and downloads images for the public-domain works in data/art.csv.

Order of preference for each work:
  1. a file already in assets/img/art/<slug>.jpg  (yours always wins)
  2. the commons_file column, if filled in
  3. Wikidata: a painting item whose title matches and whose creator matches
     the artist, using that item's official image
  4. a Commons file search on title + artist surname (flagged: check it)

Copyrighted works (public_domain = n) are never fetched. Drop your own file
in assets/img/art/ named after the slug if you want one to show.

    python3 fetch-art-images.py
"""
import csv, json, os, re, ssl, sys, time, unicodedata, urllib.parse, urllib.request

SITE   = os.path.expanduser("~/Sites/zibalion")
CSV    = os.path.join(SITE, "data", "art.csv")
IMGDIR = os.path.join(SITE, "assets", "img", "art")
UA     = "zibalion.com art page (rodney@zibalion.com)"
EXTS   = (".jpg", ".jpeg", ".png", ".webp")

try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    CTX = ssl.create_default_context()


def slugify(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"[\s_]+", "-", t)


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    return "".join(c for c in s.lower() if c.isalnum())


def key_name(artist):
    toks = [t for t in re.split(r"[\s\-.]+", artist) if len(t) > 3
            and t.lower() not in ("younger", "elder", "school", "english")]
    return norm(max(toks, key=len)) if toks else ""


def get(url, params=None, raw=False):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        return r.read() if raw else json.load(r)


def label(entity, lang="en"):
    return (entity.get("labels", {}).get(lang) or {}).get("value", "")


def from_wikidata(title, artist):
    key = key_name(artist)
    res = get("https://www.wikidata.org/w/api.php", {
        "action": "wbsearchentities", "search": title, "language": "en",
        "type": "item", "limit": 8, "format": "json"})
    ids = [x["id"] for x in res.get("search", [])]
    if not ids:
        return None
    ents = get("https://www.wikidata.org/w/api.php", {
        "action": "wbgetentities", "ids": "|".join(ids),
        "props": "claims|labels", "languages": "en", "format": "json"}).get("entities", {})
    for qid in ids:
        e = ents.get(qid, {})
        cl = e.get("claims", {})
        if "P18" not in cl:
            continue
        creators = [c["mainsnak"].get("datavalue", {}).get("value", {}).get("id")
                    for c in cl.get("P170", [])]
        creators = [c for c in creators if c]
        ok = not key  # anonymous works match on title alone
        if creators and key:
            ce = get("https://www.wikidata.org/w/api.php", {
                "action": "wbgetentities", "ids": "|".join(creators[:5]),
                "props": "labels", "languages": "en", "format": "json"}).get("entities", {})
            ok = any(key in norm(label(x)) for x in ce.values())
        if ok:
            return cl["P18"][0]["mainsnak"]["datavalue"]["value"]
    return None


def from_commons_search(title, artist):
    q = f'"{title}" {key_name(artist)}'.strip()
    res = get("https://commons.wikimedia.org/w/api.php", {
        "action": "query", "list": "search", "srsearch": q, "srnamespace": 6,
        "srlimit": 5, "format": "json"})
    for hit in res.get("query", {}).get("search", []):
        name = hit["title"].split(":", 1)[1]
        if name.lower().endswith((".jpg", ".jpeg", ".png", ".tif", ".tiff")):
            return name
    return None


def download(filename, dest_base):
    url = ("https://commons.wikimedia.org/wiki/Special:FilePath/"
           + urllib.parse.quote(filename.replace(" ", "_")) + "?width=1400")
    data = get(url, raw=True)
    ext = ".png" if data[:8] == b"\x89PNG\r\n\x1a\n" else ".jpg"
    with open(dest_base + ext, "wb") as f:
        f.write(data)
    return dest_base + ext


def main():
    if not os.path.exists(CSV):
        sys.exit(f"No {CSV}")
    os.makedirs(IMGDIR, exist_ok=True)
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    cols = list(rows[0].keys())
    if "image_source" not in cols:
        cols.append("image_source")

    got, check, miss = [], [], []
    for r in rows:
        title, artist = r["title"], r["artist"]
        slug = slugify(title)
        base = os.path.join(IMGDIR, slug)
        if any(os.path.exists(base + e) for e in EXTS):
            continue
        if r.get("public_domain", "").strip().lower() != "y":
            continue

        print(f"{title}  ({artist})")
        try:
            fname, how = (r.get("commons_file") or "").strip(), "given"
            if not fname:
                fname, how = from_wikidata(title, artist), "wikidata"
            if not fname:
                fname, how = from_commons_search(title, artist), "search"
            if not fname:
                print("    no image found")
                miss.append(title)
                continue
            download(fname, base)
            r["commons_file"] = fname
            r["image_source"] = "Wikimedia Commons"
            print(f"    {how}: {fname}")
            (check if how == "search" else got).append(title)
        except Exception as e:
            print(f"    failed: {e}")
            miss.append(title)
        time.sleep(0.7)

    w = csv.DictWriter(open(CSV, "w", newline="", encoding="utf-8"), fieldnames=cols)
    w.writeheader()
    for r in rows:
        w.writerow({c: r.get(c, "") for c in cols})

    print(f"\n{len(got)} images matched, {len(check)} from a looser search, {len(miss)} not found.")
    if check:
        print("\nLooser matches, check these look right:")
        for t in check: print("  " + t)
    if miss:
        print("\nNo image found (add a commons_file value or drop a file in assets/img/art/):")
        for t in miss: print("  " + t)


if __name__ == "__main__":
    main()
