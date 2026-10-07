#!/usr/bin/env python3
"""
Adds the Oct 6 2026 reviewed books to data/library.csv and data/conjuring-arts.csv.

- Backs up both CSVs first.
- Skips any title already in the file (matched by slug), so duplicates never get in.
- Fills only columns that exist in each file.
- Places each book after the last row of its section/subsection, else at the end.

    cd ~/Sites/zibalion && python3 add-books-oct6.py
"""
import csv, os, re, shutil, sys, time, unicodedata

SITE = os.path.expanduser("~/Sites/zibalion")
LIB  = os.path.join(SITE, "data", "library.csv")
MAG  = os.path.join(SITE, "data", "conjuring-arts.csv")

# (section, subsection, title, author, edition)
LIBRARY = [
    ("Technology and Computing", "Systems and CS", "Computer Systems: A Programmer's Perspective", "Randal E. Bryant & David R. O'Hallaron", ""),
    ("Technology and Computing", "Systems and CS", "Understanding Distributed Systems", "Roberto Vitillo", "2nd ed."),
    ("Technology and Computing", "Math and statistics", "An Introduction to Statistical Learning", "Gareth James, Daniela Witten, Trevor Hastie & Robert Tibshirani", ""),
    ("Technology and Computing", "SQL and data", "Software Engineering for Data Scientists", "Catherine Nelson", ""),
    ("Technology and Computing", "SQL and data", "Data Quality Fundamentals", "Barr Moses, Lior Gavish & Molly Vorwerck", ""),
    ("Technology and Computing", "SQL and data", "Trustworthy Online Controlled Experiments", "Ron Kohavi, Diane Tang & Ya Xu", ""),
    ("Technology and Computing", "Security", "The Developer's Playbook for Large Language Model Security", "Steve Wilson", ""),
    ("Technology and Computing", "Web", "Don't Make Me Think, Revisited", "Steve Krug", ""),
    ("Business and Economics", "Marketing", "The Anatomy of the Swipe", "Ahmed Siddiqui", ""),
    ("Philosophy", "Spiritual", "Power vs. Force", "David R. Hawkins", ""),
    ("Philosophy", "Spiritual", "The Untethered Soul", "Michael A. Singer", ""),
    ("Psychology", "Habits and focus", "Atomic Habits", "James Clear", ""),
    ("Psychology", "Habits and focus", "The Atomic Habits Workbook", "", ""),
    ("Psychology", "Habits and focus", "Deep Work", "Cal Newport", ""),
    ("Psychology", "Habits and focus", "Flow", "Mihaly Csikszentmihalyi", ""),
    ("Psychology", "Habits and focus", "The Now Habit", "Neil Fiore", ""),
    ("Psychology", "Habits and focus", "12 Rules for Life", "Jordan B. Peterson", ""),
    ("Psychology", "Habits and focus", "The Artist's Way", "Julia Cameron", ""),
    ("Psychology", "Learning and memory", "Make It Stick", "Peter C. Brown, Henry L. Roediger III & Mark A. McDaniel", ""),
    ("Psychology", "Learning and memory", "The Study Skills Handbook", "Stella Cottrell", ""),
    ("Psychology", "Learning and memory", "Moonwalking with Einstein", "Joshua Foer", ""),
    ("Psychology", "Learning and memory", "Unlimited Memory", "Kevin Horsley", ""),
    ("Psychology", "Learning and memory", "How to Develop a Brilliant Memory", "Dominic O'Brien", ""),
    ("Psychology", "Learning and memory", "Learn to Remember", "Dominic O'Brien", ""),
    ("Psychology", "Learning and memory", "Quantum Memory Power", "Dominic O'Brien", ""),
    ("Other", "Chess", "The Art of Attack in Chess", "Vladimir Vukovic", ""),
    ("Other", "Building", "The Visual Handbook of Building and Remodeling", "Charlie Wing", ""),
    ("Other", "Spiritual", "Opening to Channel", "Sanaya Roman & Duane Packer", ""),
]

MAGIC = [
    ("Conjuring Arts", "Cards", "Expert Card Technique", "Jean Hugard & Frederick Braue", ""),
    ("Conjuring Arts", "Cards", "Revolutionary Card Technique", "Ed Marlo", ""),
    ("Conjuring Arts", "Cards", "The Inner Secrets of Card Magic", "Dai Vernon & Lewis Ganson", ""),
    ("Conjuring Arts", "Cards", "The Phantom of the Card Table", "Eddie McGuire", "Critical Edition"),
    ("Conjuring Arts", "Cards", "Card Zones", "Jerry Sadowitz & Peter Duffie", ""),
    ("Conjuring Arts", "Cards", "Ahead of the Pack", "Jack Avis & Lewis Jones", ""),
    ("Conjuring Arts", "Cards", "Cardivances", "Alejandro Guillier", ""),
    ("Conjuring Arts", "Cards", "Classic Fantastic", "Paul Vigil", ""),
    ("Conjuring Arts", "Cards", "The Legendary Hierophant", "Jon Racherbaumer", ""),
    ("Conjuring Arts", "Cards", "Geoff Latta: The Long Goodbye", "Stephen Minch & Stephen Hobbs", ""),
    ("Conjuring Arts", "Cards", "The Book of Secrets", "John Carney", ""),
    ("Conjuring Arts", "Cards", "The Books of Wonder", "Tommy Wonder & Stephen Minch", "2 vols"),
    ("Conjuring Arts", "Cards", "Fred Kaps: Master Magician", "Michel van Zeist", ""),
    ("Conjuring Arts", "Cards", "Al Schneider Magic", "Al Schneider", ""),
    ("Conjuring Arts", "Coins", "Modern Coin Magic", "J. B. Bobo", ""),
    ("Conjuring Arts", "Coins", "Coin Magic", "Jean Hugard", ""),
    ("Conjuring Arts", "Coins", "David Roth's Expert Coin Magic", "Richard Kaufman", ""),
    ("Conjuring Arts", "Coins", "CoinMagic", "Richard Kaufman", ""),
    ("Conjuring Arts", "Coins", "Coin Classics Volume 1", "Chris Kenner", ""),
    ("Conjuring Arts", "Coins", "Rubinstein Coin Magic", "Michael Rubinstein", ""),
    ("Conjuring Arts", "Coins", "Coin and Money Magic", "William G. Stickland", ""),
    ("Conjuring Arts", "Coins", "Coin Snatch", "Paul Diamond", ""),
    ("Conjuring Arts", "Coins", "Giacomo Bertini's System for Amazing Coin Magic", "Giacomo Bertini", ""),
    ("Conjuring Arts", "Coins", "La Magia de las Monedas", "Joaquin Matas", ""),
    ("Conjuring Arts", "Mentalism and general", "Stunners!", "Larry Becker", ""),
    ("Conjuring Arts", "Mentalism and general", "The Compleat Magick", "Bascom Jones", "5 vols"),
    ("Conjuring Arts", "Mentalism and general", "Quick Readings with Numerology", "Richard Webster", ""),
]


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"^(the|a|an)\s+", "", t.strip().lower())
    t = re.sub(r"[^\w\s-]", "", t)
    return re.sub(r"[\s_-]+", "-", t)


def merge(path, books, label):
    if not os.path.exists(path):
        print(f"[{label}] SKIPPED: {path} not found")
        return
    shutil.copy(path, path + ".bak-" + time.strftime("%Y%m%d-%H%M%S"))
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    cols = list(rows[0].keys())
    have = {slug(r.get("title", "")) for r in rows}
    ids = [int(r["id"]) for r in rows if r.get("id", "").isdigit()]
    nid = (max(ids) + 1) if ids else 1
    added, dupes = [], []
    for sec, sub, title, author, ed in books:
        if slug(title) in have:
            dupes.append(title); continue
        r = {c: "" for c in cols}
        for k, v in dict(id=str(nid), section=sec, subsection=sub, title=title,
                         author=author, edition=ed).items():
            if k in r: r[k] = v
        nid += 1; have.add(slug(title))
        pos = None
        for i, x in enumerate(rows):
            if x.get("section") == sec and x.get("subsection") == sub: pos = i + 1
        if pos is None:
            for i, x in enumerate(rows):
                if x.get("section") == sec: pos = i + 1
        rows.insert(pos if pos is not None else len(rows), r)
        added.append(title)
    w = csv.DictWriter(open(path, "w", encoding="utf-8", newline=""), fieldnames=cols)
    w.writeheader(); w.writerows(rows)
    print(f"[{label}] added {len(added)}, skipped {len(dupes)} already there")
    for t in dupes: print(f"    already had: {t}")


if __name__ == "__main__":
    merge(LIB, LIBRARY, "library.csv")
    merge(MAG, MAGIC, "conjuring-arts.csv")
    print("\nDone. Rebuild the pages, then push.")
