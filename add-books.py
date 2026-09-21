#!/usr/bin/env python3
"""
Adds confirmed books to data/library.csv and to the shelf list on the process
page, in the right groups, then looks up covers for the new rows only.
Backs up both files first. Safe to re-run: books already present are skipped.
"""
import csv, html, json, os, re, shutil, ssl, sys, time, unicodedata, urllib.parse, urllib.request

SITE = os.path.expanduser("~/Sites/zibalion")
CSV  = os.path.join(SITE, "data", "library.csv")
PAGE = os.path.join(SITE, "process", "index.html")
CONJ_MARK = "<!-- ==== ZB-CONJURING START ==== -->"

NEW = [
 ("Literature","The Russians","War and Peace","Leo Tolstoy","","1869",
  "Tolstoy's panorama of Russian society through the Napoleonic wars, following families through love, battle and the search for how to live. History and private life on one enormous canvas."),
 ("Literature","The Russians","Anna Karenina","Leo Tolstoy","Norton Critical Edition","1878",
  "Anna's love affair and its destruction, set against Levin's search for meaning on his estate. Often called the greatest novel ever written, and one of the most psychologically exact."),
 ("Literature","The Russians","The Master and Margarita","Mikhail Bulgakov","","1967",
  "The Devil arrives in Stalin's Moscow with a talking cat, while a parallel story retells Pilate and Jesus. Satire, theology and farce, written in secret and published long after Bulgakov's death."),
 ("Literature","French","The Count of Monte Cristo","Alexandre Dumas","","1844",
  "Edmond Dantès is betrayed, imprisoned for fourteen years, escapes with a fortune and returns for revenge. Written for serial publication, and one of the most satisfying plots ever built."),
 ("Literature","French","Swann's Way","Marcel Proust","","1913",
  "The first volume of In Search of Lost Time, in which the taste of a madeleine releases a flood of memory. Proust's long sentences are the point: they move the way memory does."),
 ("Literature","English and American","East of Eden","John Steinbeck","","1952",
  "Two families in California's Salinas Valley re-enact the story of Cain and Abel across generations. Steinbeck considered it his most important book, turning on one word: timshel, thou mayest."),
 ("Literature","English and American","A Confederacy of Dunces","John Kennedy Toole","","1980",
  "Ignatius J. Reilly, a monumentally self-regarding misfit, rages against the modern world in New Orleans. Published eleven years after Toole's death, and awarded the Pulitzer Prize."),
 ("Literature","English and American","The Little Friend","Donna Tartt","","2002",
  "A twelve-year-old girl in Mississippi sets out to find who killed her brother years before. Slow, atmospheric Southern gothic."),
 ("Literature","English and American","Moby-Dick","Herman Melville","","1851",
  "Ahab's hunt for the white whale, interrupted by chapters of whaling lore, philosophy and sermon. Ignored in Melville's lifetime and now central to American literature."),
 ("Literature","Latin American","One Hundred Years of Solitude","Gabriel García Márquez","","1967",
  "Seven generations of the Buendía family in the town of Macondo, where the miraculous is reported as plainly as the weather. The defining novel of magical realism."),
 ("Literature","Scandinavian","My Struggle: Book 1","Karl Ove Knausgaard","","2009",
  "The first of Knausgaard's six autobiographical novels, moving from adolescence to his father's death with a close, unhurried attention that makes the ordinary feel enormous."),
 ("Literature","Crime, mystery, and the propulsive shelf","The Passage","Justin Cronin","","2010",
  "A government experiment unleashes a viral catastrophe, and a girl named Amy becomes the hinge of everything after. The first book of an apocalyptic trilogy."),
 ("Literature","Crime, mystery, and the propulsive shelf","Carrion Comfort","Dan Simmons","","1989",
  "A handful of people who can take over other minds play deadly games across the twentieth century, hunted by a Holocaust survivor who has seen what they do."),
 ("Philosophy","Logic and argument","How to Read a Book","Mortimer J. Adler & Charles Van Doren","","1940",
  "Adler's guide to active reading, from inspection through analytical reading to syntopical reading: several books read against each other on one question."),
 ("Philosophy","Esoteric","Reality Transurfing","Vadim Zeland","","2004",
  "Zeland's system, widely read in Russia since the 2000s, describing reality as a field of possible variations and teaching how to move through it by intention rather than struggle."),
 ("Science","Foundations","On the Origin of Species","Charles Darwin","Harvard University Press, facsimile of the 1859 first edition","1859",
  "Darwin's argument for evolution by natural selection, reproduced as it first appeared. The book that reorganized biology and much else."),
 ("Science","Foundations","Principia","Isaac Newton","Translated by I. Bernard Cohen and Anne Whitman","1687",
  "Newton's laws of motion and universal gravitation, in the translation that brought the full text into modern English. The foundation of classical physics."),
 ("Science","Foundations","Relativity: The Special and the General Theory","Albert Einstein","","1916",
  "Einstein's own explanation of special and general relativity, written for readers without advanced mathematics."),
]


def slugify(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"[\s_]+", "-", t)


try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    CTX = ssl.create_default_context()


def norm(s):
    return "".join(c for c in (s or "").lower() if c.isalnum())


def cover_for(title, author):
    """Cover only. Exact title, author surname must match. Nothing else is taken."""
    sn = [p for p in author.split("&")[0].replace(".", " ").split() if len(p) > 2]
    sn = norm(sn[-1]) if sn else ""
    q = urllib.parse.urlencode({"title": title, "author": author.split("&")[0].strip(),
                                "limit": 5, "fields": "title,author_name,cover_i"})
    req = urllib.request.Request("https://openlibrary.org/search.json?" + q,
                                 headers={"User-Agent": "zibalion.com catalogue"})
    try:
        with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
            docs = json.load(r).get("docs", [])
    except Exception:
        return ""
    for d in docs:
        if norm(d.get("title")) != norm(title):
            continue
        if sn and sn not in norm(" ".join(d.get("author_name") or [])):
            continue
        if d.get("cover_i"):
            return f"https://covers.openlibrary.org/b/id/{d['cover_i']}-L.jpg"
    return ""


def main():
    for p in (CSV, PAGE):
        if not os.path.exists(p):
            sys.exit(f"ABORT: missing {p}")
    stamp = time.strftime("%Y%m%d-%H%M%S")
    shutil.copy(CSV, CSV + ".bak-" + stamp)
    shutil.copy(PAGE, PAGE + ".bak-" + stamp)

    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    cols = list(rows[0].keys())
    have = {slugify(r["title"]) for r in rows}
    nextid = max(int(r["id"]) for r in rows) + 1

    added = []
    for sec, sub, title, author, ed, yr, about in NEW:
        s = slugify(title)
        if s in have:
            continue
        r = {c: "" for c in cols}
        r.update(id=str(nextid), section=sec, subsection=sub, title=title,
                 author=author, edition=ed, year=yr, about=about)
        nextid += 1
        have.add(s)

        # place it after the last row of its subsection, else its section, else the end
        pos = None
        for i, x in enumerate(rows):
            if x["section"] == sec and x["subsection"] == sub:
                pos = i + 1
        if pos is None:
            for i, x in enumerate(rows):
                if x["section"] == sec:
                    pos = i + 1
        rows.insert(pos if pos is not None else len(rows), r)
        added.append(r)

    if not added:
        print("Nothing new to add.")
        return

    print(f"Looking up covers for {len(added)} new books...")
    got = 0
    for r in added:
        r["cover_url"] = cover_for(r["title"], r["author"])
        got += bool(r["cover_url"])
        time.sleep(0.6)

    with open(CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})

    # ---- shelf list on the process page ----
    src = open(PAGE, encoding="utf-8").read()

    def li(r):
        label = html.escape(r["author"]) + " \u2014 " + html.escape(r["title"])
        return f'<li><a href="/library/{slugify(r["title"])}/">{label}</a></li>'

    def find_group(src, sec):
        for m in re.finditer(r'<details class="pr-shelfgroup">(.*?)</details>', src, re.S):
            s = re.search(r"<summary>(.*?)<span", m.group(1), re.S)
            if s and html.unescape(s.group(1)).strip() == sec:
                return m
        return None

    for r in added:
        sec, sub = r["section"], r["subsection"]
        g = find_group(src, sec)
        if g is None:
            block = (f'<details class="pr-shelfgroup">\n<summary>{html.escape(sec)}'
                     f'<span class="pr-count">0</span></summary>\n'
                     f'<div class="pr-sub"><h4>{html.escape(sub)}</h4><ul>\n{li(r)}\n</ul></div>\n</details>\n')
            at = src.find(CONJ_MARK)
            if at < 0:
                at = src.rfind("</details>") + len("</details>\n")
            src = src[:at] + block + src[at:]
            continue

        body = g.group(0)
        hm = re.search(r'<div class="pr-sub"><h4>' + re.escape(html.escape(sub)) +
                       r'</h4>\s*<ul>(.*?)</ul>', body, re.S)
        if hm:
            new_body = body[:hm.end(1)] + li(r) + "\n" + body[hm.end(1):]
        else:
            add = f'<div class="pr-sub"><h4>{html.escape(sub)}</h4><ul>\n{li(r)}\n</ul></div>\n'
            new_body = body[:-len("</details>")] + add + "</details>"
        src = src[:g.start()] + new_body + src[g.end():]

    # recount every library group from the data
    counts = {}
    for r in rows:
        counts[r["section"]] = counts.get(r["section"], 0) + 1

    def fix(m):
        name = html.unescape(re.sub(r"<span.*$", "", m.group(1), flags=re.S)).strip()
        return (f'<summary>{html.escape(name)}<span class="pr-count">{counts[name]}</span></summary>'
                if name in counts else m.group(0))

    src = re.sub(r"<summary>(.*?)</summary>", fix, src, flags=re.S)
    open(PAGE, "w", encoding="utf-8").write(src)

    print(f"Added {len(added)} books, {got} with covers.")
    print("Counts: " + ", ".join(f"{k} {v}" for k, v in counts.items()))


if __name__ == "__main__":
    main()
