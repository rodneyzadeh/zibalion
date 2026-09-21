# id: dict(t=title, a=author, e=edition, y=first published, p=publisher, d=description)
D = {
1: dict(y="2016", d="Severance's introduction to programming, built from his University of Michigan course and given away free online. It teaches Python through working with real data rather than abstract exercises, which makes it one of the gentler ways in."),
2: dict(p="No Starch Press", y="2015", d="A fast, project-driven introduction. The first half covers the language; the second builds three real things: a game, a data visualization and a web application."),
3: dict(p="No Starch Press", y="2015", d="Python for people who want to get something done: renaming files, filling spreadsheets, scraping pages, sending email. Sweigart teaches the language through the chores it can take off your hands, and the workbook adds practice for each chapter."),
4: dict(p="O'Reilly", y="2015", d="For programmers who already know Python and want to write it the way the language intends. Ramalho works through the data model, iterators, generators and concurrency, explaining the design decisions underneath the features."),
5: dict(d="An intermediate book on the patterns experienced Python developers lean on: generators, decorators, higher-order functions and test-driven development."),
6: dict(t="Python Cookbook", p="O'Reilly", d="Recipes for specific problems, each worked through with an explanation of why the solution works. Less a book to read in order than one to open when you are stuck."),
7: dict(t="High Performance Python", a="Micha Gorelick & Ian Ozsvald", p="O'Reilly", y="2014", d="How to find out why Python code is slow and what to do about it: profiling, NumPy, compiled extensions, concurrency and clusters. Measurement first, optimization second."),
8: dict(p="Pragmatic Bookshelf", y="2017", d="A practical guide to pytest, the testing framework most Python projects now use. Fixtures, parametrization and plugins, explained through a small working project."),
9: dict(p="No Starch Press", y="2012", d="Not a language book but a problem-solving one. Spraul argues that the hard part of programming is breaking a problem down, and teaches that skill directly."),
10: dict(t="Django for Beginners", e="5th edition", y="2018", d="A step-by-step introduction to Django that builds several complete projects, from a single page to a newspaper site with user accounts, and deploys each one."),
11: dict(t="Django for APIs", e="5th edition", y="2018", d="The companion volume, focused on building web APIs with Django REST Framework: serialization, permissions, authentication and documentation."),
12: dict(p="Packt", y="2024", d="A project-based tour of Django, building a blog, a social site, an online shop and an e-learning platform, each introducing more of the framework."),
13: dict(a="Daniel and Audrey Feldroy", y="2013", d="A book of best practices rather than a tutorial: how experienced Django developers structure projects, settings, models and deployments, and the mistakes they learned to avoid."),
14: dict(p="O'Reilly", y="2001", d="A ground-up introduction to building websites with HTML, CSS, JavaScript and web graphics, written for people with no background. Clear enough to be the first book in many courses."),
15: dict(t="Web Scraping with Python", a="Ryan Mitchell", p="O'Reilly", y="2015", d="How to collect data from the web programmatically, from parsing HTML to handling forms, logins and JavaScript-heavy sites, along with the legal and ethical questions that come with it."),
16: dict(a="Anish Chapagain"),
18: dict(t="Learning SQL", a="Alan Beaulieu", p="O'Reilly", y="2005", d="A clear introduction to SQL that goes beyond basic queries into joins, subqueries, grouping and transactions, with attention to how databases actually process what you write."),
19: dict(t="SQL Cookbook", a="Anthony Molinaro", p="O'Reilly", y="2005", d="Solutions to the queries people actually struggle with, shown side by side across several database systems. Useful for seeing that one problem can be solved more than one way."),
20: dict(p="O'Reilly", y="2012", d="Written by the creator of pandas, the working manual for cleaning, reshaping and analyzing data in Python, with NumPy and Jupyter alongside."),
21: dict(p="Wiley", y="2015", d="On making charts people understand. Knaflic, who taught data visualization at Google, shows how to cut clutter, direct attention and build a narrative around a number."),
22: dict(a="Foster Provost & Tom Fawcett", p="O'Reilly", y="2013", d="The concepts behind data science explained for people who make decisions with it: what the methods can and cannot tell you, and how to treat data as a business asset."),
23: dict(p="O'Reilly", y="2017", d="The book engineers pass around for understanding how data systems really work: replication, partitioning, transactions, consistency and the trade-offs between them. Dense, careful and widely regarded as the best of its kind."),
24: dict(t="Fundamentals of Data Engineering", a="Joe Reis & Matt Housley", p="O'Reilly", y="2022", d="An overview of the data engineering lifecycle, from ingestion to serving, written to outlast any particular tool."),
25: dict(a="Wayne Winston", p="Microsoft Press", y="2004", d="A practical course in using Excel for real analysis: forecasting, optimization, simulation and financial modeling, taught through business problems."),
26: dict(p="W. W. Norton", y="2013", d="Statistics explained without the formulas getting in the way. Wheelan focuses on intuition: what a number is really saying, and the ways it can mislead."),
27: dict(t="The Manga Guide to Statistics", a="Shin Takahashi", p="No Starch Press", y="2008", d="Statistics taught through a comic-book story. An unlikely format that makes the core ideas easier to hold on to."),
28: dict(a="Shin Takahashi & Iroha Inoue", p="No Starch Press", y="2012", d="Vectors, matrices and transformations through a manga narrative, with worked problems behind the story."),
29: dict(a="Hiroyuki Kojima", p="No Starch Press", y="2009", d="Derivatives and integrals introduced through a story, grounding each idea in a practical situation before the notation arrives."),
30: dict(t="Essential Math for Data Science", a="Thomas Nield", p="O'Reilly", y="2022", d="The mathematics underneath data science and machine learning, from probability and statistics to linear algebra and calculus, explained for working programmers."),
31: dict(t="Mathematics for Machine Learning", a="Marc Peter Deisenroth, A. Aldo Faisal & Cheng Soon Ong", p="Cambridge University Press", y="2020", d="A rigorous bridge between undergraduate mathematics and machine learning: linear algebra, geometry, probability and optimization, then the models built on them."),
32: dict(t="Practical Statistics for Data Scientists", a="Peter Bruce, Andrew Bruce & Peter Gedeck", p="O'Reilly", y="2017", d="The statistical concepts that matter most in data science, with a clear eye on which classical methods still earn their place and which do not."),
33: dict(p="Manning", y="2020", d="Mathematics taught through code: vectors, calculus and machine learning built up in Python rather than on paper."),
34: dict(p="O'Reilly", y="2015", d="Grus builds the tools of data science himself in plain Python, from statistics to neural networks, so the reader sees what the libraries are actually doing."),
35: dict(p="O'Reilly", y="2017", d="The standard practical guide to machine learning in Python, moving from classical methods with Scikit-Learn to deep learning with Keras and TensorFlow."),
36: dict(d="Starmer's visual, step-by-step explanation of how neural networks work, in the same friendly style as his StatQuest videos."),
38: dict(a="Lewis Tunstall, Leandro von Werra & Thomas Wolf", p="O'Reilly", y="2022", d="Written by engineers at Hugging Face, a practical guide to transformer models for classification, generation, summarization and question answering."),
39: dict(p="Manning", y="2024", d="Raschka builds a GPT-style language model step by step in PyTorch, from tokenization and attention to pretraining and fine-tuning."),
40: dict(p="O'Reilly", d="How to build applications on foundation models: evaluation, prompt engineering, retrieval, fine-tuning and the systems around them."),
41: dict(a="Valliappa Lakshmanan & Hannes Hapke", p="O'Reilly", y="2025", d="A catalogue of recurring solutions for building with generative AI, in the tradition of design patterns books for software."),
42: dict(a="Andrei Gheorghiu", p="Packt", y="2024", d="A guide to retrieval-augmented generation with LlamaIndex, connecting language models to your own documents and data."),
43: dict(a="Steven Bird, Ewan Klein & Edward Loper", p="O'Reilly", y="2009", d="The book behind NLTK, introducing natural language processing through hands-on work with real text."),
44: dict(a="Emmanuel Ameisen", p="O'Reilly", y="2020", d="The whole path from product idea to deployed machine learning model, with as much attention on iteration and debugging as on the models themselves."),
45: dict(p="Prentice Hall", y="2008", d="Martin's argument that code is read far more often than it is written, and his rules for making it readable. Influential, and argued with as much as followed."),
46: dict(a="Andrew Hunt & David Thomas", p="Addison-Wesley", y="1999", d="Advice on the craft of software development, from debugging to working habits. Its phrases, like DRY and tracer bullets, entered the everyday vocabulary of the field."),
47: dict(p="Yaknyam Press", y="2018", d="Ousterhout's case that the central problem in software is complexity, and that good design means deep modules behind simple interfaces. A short book that takes issue with some popular advice."),
48: dict(p="Addison-Wesley", y="2021", d="Farley argues for treating software development as a genuine engineering discipline, built on learning and managing complexity rather than following fashion."),
49: dict(a="Harry Percival & Bob Gregory", p="O'Reilly", y="2020", d="Domain-driven design, event-driven architecture and related patterns, translated into idiomatic Python."),
50: dict(a="Erich Gamma, Richard Helm, Ralph Johnson & John Vlissides", p="Addison-Wesley", y="1994", d="The catalogue of twenty-three object-oriented design patterns that gave the field a shared vocabulary. Known everywhere as the Gang of Four book."),
51: dict(a="Mark Richards & Neal Ford", p="O'Reilly", y="2020", d="A broad introduction to the architect's job: architectural styles, the characteristics they trade off, and the soft skills the role demands."),
52: dict(a="Neal Ford, Mark Richards, Pramod Sadalage & Zhamak Dehghani", p="O'Reilly", y="2021", d="Follows a fictional team through the hardest decisions in distributed architecture, where every choice is a trade-off and there is rarely a best answer."),
53: dict(p="O'Reilly", y="2015", d="The standard reference on designing, deploying and running systems built from small independent services, including when not to."),
54: dict(t="System Design Interview", e="Volumes 1 and 2", y="2020", d="Worked walkthroughs of designing large systems, from rate limiters to chat services. Written for interview preparation, but a good tour of how real systems are built."),
55: dict(a="Ali Aminian & Hao Sheng", d="The same approach applied to generative AI: how to design and reason about products built on large models."),
56: dict(a="Robert Sedgewick & Kevin Wayne", p="Addison-Wesley", y="2016", d="Princeton's introductory computer science course in book form, covering programming, algorithms, the theory of computation and machine architecture."),
57: dict(p="Springer", y="1997", d="Half textbook, half catalogue of algorithmic problems, with Skiena's war stories about applying them. A practitioner's book rather than a theorist's."),
58: dict(p="Manning", y="2016", d="An illustrated introduction to common algorithms, drawn rather than proved, for readers who find the standard textbooks hard going."),
59: dict(y="2008", d="The standard preparation book for technical interviews: programming questions with worked solutions and a guide to how the process works from the inside."),
60: dict(p="Addison-Wesley", y="2002", d="A collection of bit manipulation tricks and low-level arithmetic techniques, the kind of cleverness that lives inside compilers and hardware."),
61: dict(p="Addison-Wesley", y="1968", d="Knuth's multivolume analysis of algorithms, begun in the 1960s and still in progress. The foundational work of the field, and famously demanding."),
62: dict(p="No Starch Press", y="2014", d="Python for offensive security: writing your own network tools and exploits to understand how attacks actually work."),
63: dict(p="No Starch Press", y="2003", d="Exploitation taught from first principles: C, assembly, memory, networking and how vulnerabilities arise. Comes with an environment to practice in."),
64: dict(p="No Starch Press", y="2014", d="A hands-on introduction to penetration testing, built around a lab the reader sets up to practice the full process safely."),
65: dict(a="Dafydd Stuttard & Marcus Pinto", p="Wiley", y="2007", d="A thorough manual of how web applications are attacked, by the creator of Burp Suite. For years the standard reference for web security testing."),
66: dict(t="The Hacker Playbook", e="Books 2 and 3", d="Kim's field manuals for penetration testing, organized like a sports playbook around the phases of a real engagement."),
67: dict(a="Scott Chacon & Ben Straub", p="Apress", y="2009", d="The comprehensive guide to Git, free to read online, covering daily use and the internals underneath."),
68: dict(p="No Starch Press", y="2012", d="A complete introduction to the shell, from first commands to writing scripts. Patient enough to take someone from nervous to fluent."),
69: dict(p="Pragmatic Bookshelf", y="2012", d="Organized as tips rather than a tutorial, each one a small lesson in thinking the way Vim wants you to."),
70: dict(a="Ruslan Osipov", p="Packt", y="2018", d="Building an efficient Vim setup: navigation, plugins, configuration and customization for serious daily use."),
71: dict(p="Manning", y="2019", d="Building cross-platform mobile apps with React Native, from the fundamentals of the framework to navigation, animation and platform APIs."),
72: dict(a="Thomas Bailey & Alessandro Biessek", p="Packt", d="An introduction to Flutter and Dart for building mobile apps from a single codebase."),
73: dict(a="Alberto Miola", d="A detailed reference to Dart and Flutter, covering the language in depth before moving to the framework."),
74: dict(p="Microsoft Press", y="1999", d="How computers work, built up from flashlights and telegraph relays to logic gates, memory and a working processor. One of the best explanations of the machine ever written for a general reader."),
75: dict(p="Wiley", y="2008", d="Turing's 1936 paper on computable numbers, reproduced in full and explained line by line, with the mathematics and history needed to follow it."),
76: dict(p="MIT Press", y="2016", d="A readable account of Turing's 1936 paper and the ideas it opened up: computability, decidability and the limits of what machines can do."),
77: dict(p="Simon & Schuster", y="2014", d="A history of the digital revolution told through the people who built it, from Ada Lovelace to the founders of the internet, with an emphasis on collaboration over lone genius."),
78: dict(p="Simon & Schuster", y="2017", d="A biography built largely from Leonardo's notebooks, portraying a man driven by curiosity across art, engineering and anatomy."),
79: dict(a="Gerhard Hoernes & Melvin Heilweil", d="A programmed-instruction text that teaches Boolean algebra and logic design one small step at a time, with the reader answering as they go."),
80: dict(y="1977", d="A long-running textbook on digital electronics: number systems, logic gates, combinational and sequential circuits, and the building blocks of computers."),
81: dict(p="Dover", y="1961", d="A short, clear introduction to Boolean algebra and its use in switching circuits and logic, kept in print for decades."),
82: dict(t="Digital Computer Electronics", e="3rd edition", p="McGraw-Hill", y="1977", d="Malvino builds a simple computer in stages, the SAP series, to show how digital circuits combine into a working machine. Many engineers first understood computers this way."),
83: dict(p="Maker Media", y="2009", d="Learning electronics by doing it: a series of experiments with real components, each explaining what happened and why."),
84: dict(p="Maker Media", y="2014", d="The follow-up, moving into chips, sensors and more ambitious projects."),
85: dict(p="Maker Media", y="2012", d="A reference to what components are, how they work and how they fail, organized for looking things up at the bench."),
86: dict(t="Practical Electronics for Inventors", e="4th edition", p="McGraw-Hill", y="2000", d="A large, practical reference covering theory, components and circuit design, written for people who build things."),
87: dict(a="Dan O'Sullivan & Tom Igoe", y="2004", d="Using microcontrollers to connect computers to the physical world through sensors and motors. A foundational text of the maker movement."),
88: dict(p="Maker Media", y="2007", d="Projects that get devices communicating with each other and with the internet."),
89: dict(t="Ingenious Mechanisms for Designers and Inventors", a="Franklin D. Jones (ed.)", e="Four-volume set", p="Industrial Press", y="1930", d="A catalogue of mechanical devices drawn from industry, from cams and linkages to feeding and ejecting mechanisms. Solutions engineers have returned to for decades."),
90: dict(t="Product Design and Development", a="Karl Ulrich & Steven Eppinger", e="3rd edition", p="McGraw-Hill", y="1995", d="The standard textbook on how products move from concept to production, treating design as a process that can be managed."),
91: dict(p="Productivity Press", d="How to design products so they can be built well and cheaply, making manufacturing a design constraint from the start."),
92: dict(p="Wiley", y="2009", d="An insider's account of manufacturing in southern China, and of how quality quietly erodes when a factory holds the advantage over its client."),
93: dict(p="North River Press", y="1984", d="A business novel about a failing factory that introduces the theory of constraints: find the bottleneck, because everything else is secondary to it."),
94: dict(a="Andrew \"bunnie\" Huang", p="No Starch Press", y="2017", d="Essays from a hardware engineer on manufacturing in Shenzhen, reverse engineering and open hardware."),
95: dict(a="Renee DiResta, Brady Forrest & Ryan Vinyard", p="O'Reilly", y="2015", d="A guide to taking a physical product from prototype to market: funding, manufacturing and distribution."),
96: dict(p="W. H. Freeman", y="1976", d="Weizenbaum built ELIZA, then watched people confide in it. This is his argument that some decisions should never be handed to computers, however capable they become."),
97: dict(a="Joseph Weizenbaum & Gunna Wendt", d="A late conversation with Weizenbaum, looking back on computing and society after decades of arguing against its excesses."),
98: dict(y="2003", d="A broad anthology of the philosophy of technology, from the ancient Greeks through Heidegger to contemporary debates."),
99: dict(y="1977", d="Heidegger's essays arguing that modern technology is not just a set of tools but a way of revealing the world, one that turns everything, people included, into resources on standby."),
100: dict(p="Feral House", y="2010", d="Kaczynski's collected writings on why he considered industrial technology incompatible with human freedom. Read as the document of an argument and of the violence it was used to justify."),
101: dict(p="Dutton", y="2021", d="A reported history of the researchers behind the deep learning revolution and the companies that competed to hire them."),
102: dict(p="Viking", y="1985", d="Postman's argument that television turned public discourse into entertainment, and that a culture can be undone by what it loves rather than what it fears."),
103: dict(p="PublicAffairs", y="2019", d="Zuboff's account of an economic order built on extracting and predicting human behavior, and what it costs in autonomy."),
104: dict(p="MIT Press", y="1972", d="Dreyfus's philosophical critique of symbolic AI, drawing on Heidegger and Merleau-Ponty to argue that human intelligence depends on embodied, situated know-how."),
105: dict(p="Basic Books", y="1979", d="Hofstadter weaves Gödel's incompleteness, Escher's drawings and Bach's canons into an inquiry into how meaning and self-reference arise from formal systems. It won the Pulitzer Prize."),
106: dict(p="MIT Press", y="1969", d="Simon's lectures on the design of artificial systems, from economies and organizations to minds, and the idea of bounded rationality."),
107: dict(t="I and Thou", e="Scribner, translated by Walter Kaufmann", y="1923", d="Buber's short, dense work distinguishing two ways of meeting the world: as an It to be used, or as a Thou to be encountered."),
109: dict(t="Existentialism Is a Humanism", e="Yale University Press, translated by Carol Macomber", y="1946", d="Sartre's 1945 lecture defending existentialism to a general audience, and the source of the claim that existence precedes essence."),
110: dict(t="Being and Time", e="Translated by John Macquarrie and Edward Robinson", y="1927", d="Heidegger's unfinished masterwork on the question of what it means to be, approached through human existence. Macquarrie and Robinson's is the long-standard English version."),
111: dict(t="The Myth of Sisyphus", e="Vintage International", y="1942", d="Camus's essay on the absurd and on whether life is worth living without ultimate meaning. It ends by imagining Sisyphus happy at his rock."),
112: dict(y="1946", d="Frankl's account of surviving the Nazi camps, followed by an outline of logotherapy, built on the claim that meaning can be found even in suffering."),
113: dict(t="The Denial of Death", e="50th anniversary edition", y="1973", d="Becker's Pulitzer-winning argument that much of human culture is a defense against the knowledge that we will die."),
114: dict(t="Discourses, Fragments, Handbook", e="Oxford World's Classics, translated by Robin Hard", d="The teachings of a former slave turned Stoic teacher, recorded by his student Arrian. The Handbook distills them into a manual for separating what is in our power from what is not."),
115: dict(t="Letters from a Stoic", e="Penguin Classics", d="Seneca's letters to Lucilius: practical reflections on time, friendship, wealth and death. The most personal and readable of the Roman Stoics."),
116: dict(d="Private notes an emperor wrote to himself, never meant for publication. A record of someone trying, daily, to live by Stoic principles under enormous pressure."),
117: dict(p="Hoover Institution", y="1993", d="Stockdale's lecture on how Epictetus helped him endure seven and a half years as a prisoner of war in Vietnam."),
118: dict(t="Cyropaedia", e="Cornell University Press, translated by Wayne Ambler", d="Xenophon's idealized account of the education and rule of Cyrus the Great, part biography and part treatise on leadership. Machiavelli read it closely."),
119: dict(t="Elements", e="Green Lion Press", d="Geometry built from a handful of definitions and axioms into a complete system. For over two thousand years the model of what rigorous reasoning looks like."),
120: dict(t="The Prince", a="Niccolò Machiavelli", e="Penguin Classics, translated by George Bull", y="1532", d="A short treatise on acquiring and keeping power, written in 1513 and published after Machiavelli's death. Its reputation is darker than its argument, which is about how politics works rather than how it ought to."),
121: dict(t="The Art of War", e="Illustrated edition, James Trapp", d="The ancient Chinese treatise on strategy, built on the idea that the best victory is the one won without fighting."),
122: dict(t="The Complete Musashi", a="Miyamoto Musashi", e="Translated by Alexander Bennett", d="Musashi's writings, including The Book of Five Rings, on strategy, swordsmanship and the discipline of a warrior's path."),
123: dict(t="Hagakure", a="Yamamoto Tsunetomo", e="Translated by Alexander Bennett", d="Reflections of an eighteenth-century samurai retainer on duty, death and loyalty, recorded by a younger listener. Famous and often misread."),
124: dict(t="On War", a="Carl von Clausewitz", e="Princeton University Press, translated by Michael Howard and Peter Paret", y="1832", d="Clausewitz's unfinished study of war as the continuation of politics, full of friction, chance and fog. The Howard and Paret translation is the standard."),
125: dict(t="The Strategy of Conflict", e="Harvard University Press", y="1960", d="Schelling applies game theory to bargaining, deterrence and conflict, showing how commitment and focal points shape outcomes. Part of the work that won him a Nobel prize."),
126: dict(y="1954", d="Liddell Hart's survey of military history arguing for the indirect approach: winning by dislocating the opponent rather than meeting strength with strength."),
127: dict(p="Little, Brown", y="2002", d="A biography of John Boyd, the fighter pilot and strategist behind the OODA loop, and of the institutions he fought as fiercely as any opponent."),
128: dict(t="The Art of Worldly Wisdom", e="Doubleday, translated by Christopher Maurer", y="1647", d="Three hundred aphorisms from a seventeenth-century Jesuit on prudence, reputation and dealing with people. Sharp, worldly and still quoted."),
129: dict(y="2012", d="A reference to more than three hundred logical fallacies, each defined and illustrated with examples."),
130: dict(y="2004", d="A short, plain guide to reasoning well: clear thinking, the structure of arguments and how they go wrong."),
131: dict(y="2013", d="Common fallacies explained through illustrated animal scenes. Brief, charming and surprisingly precise."),
132: dict(e="Translation with commentary", p="W. W. Norton", y="2018", d="Alter's translation of the entire Hebrew Bible with commentary, completed over more than two decades and aiming to keep the literary force of the original."),
133: dict(a="Jewish Publication Society", y="1985", d="The Jewish Publication Society translation of the Hebrew Bible, the standard English version in many Jewish communities."),
134: dict(p="Schocken Books", y="1947", d="Buber's retelling of the stories of the Hasidic masters, gathered and shaped over many years."),
135: dict(t="Tales of the Dervishes", e="Arkana / Penguin", y="1967", d="Teaching stories from the Sufi tradition, meant to be read more than once and to work on the reader over time."),
136: dict(y="1951", d="Heschel's meditation on the Sabbath as a sanctuary in time rather than space. Short, lyrical and one of the defining works of twentieth-century Jewish thought."),
137: dict(y="1995", d="Miles reads God as the protagonist of the Hebrew Bible, following the character through the text as a literary critic would. It won the Pulitzer Prize."),
138: dict(p="Stanford University Press", y="2003", d="A study of Isaac Luria and the circle of kabbalists around him in sixteenth-century Safed."),
139: dict(t="Sha'ar HaGilgulim", a="Chaim Vital", e="Vol. 1, digital edition, translated by Winston", d="The Gate of Reincarnations, a central text of Lurianic kabbalah as recorded by Luria's disciple Chaim Vital."),
140: dict(t="The Jewish Annotated New Testament", a="Amy-Jill Levine & Marc Zvi Brettler (eds.)", e="Oxford University Press, 2nd edition", y="2011", d="The New Testament annotated by Jewish scholars, reading the texts in the context of the Judaism they came from."),
141: dict(p="Stanford University Press", y="2009", d="A study of the Zohar as living mystical experience rather than doctrine alone, attending to its language and its circle of companions."),
142: dict(y="1949", d="Campbell's comparative study of myth and the pattern he called the monomyth, the hero's journey. Enormously influential on storytelling well beyond scholarship."),
143: dict(d="World history told through maps, from the earliest humans to the present."),
144: dict(a="J. M. Roberts & Odd Arne Westad", y="1976", d="A single-volume world history, revised and extended by Westad. Wide in scope and unusually readable for its size."),
145: dict(t="Sapiens", e="10th anniversary edition", y="2011", d="Harari's sweeping account of how Homo sapiens came to dominate the planet through cognitive, agricultural and scientific revolutions. Widely read and widely argued with."),
146: dict(y="1968", d="A short distillation of the Durants' decades on The Story of Civilization, asking what history teaches about human nature, government and war."),
147: dict(a="David Graeber & David Wengrow", y="2021", d="An anthropologist and an archaeologist challenge the standard story of social evolution, arguing that early societies experimented with far more political arrangements than we assume."),
148: dict(p="W. W. Norton", y="2018", d="A single-volume history of the United States, organized around whether the country has lived up to its founding claims."),
149: dict(y="2019", d="A narrative history of the United States, written for students and general readers as a counterweight to more critical accounts."),
150: dict(y="2004", d="An early PayPal employee's account of the company's fights with eBay, regulators and fraudsters, and of the team that later scattered across Silicon Valley."),
152: dict(y="2003", d="A narrative history of the fall of the Roman Republic, from its expansion to the civil wars that ended it, told with a novelist's pace."),
153: dict(t="Lives", e="Vol. 1, Modern Library, Dryden translation", d="Plutarch's paired biographies of Greek and Roman statesmen, written to examine character rather than events. Shakespeare drew on them heavily."),
154: dict(t="Selected Works", e="Penguin Classics, translated by Michael Grant", d="Cicero's speeches, letters and philosophical writing in one volume: the orator, the politician and the thinker together."),
155: dict(t="Selected Political Speeches", e="Penguin Classics, translated by Michael Grant", d="Cicero at his most public, in speeches from the prosecutions and political crises of the late Republic."),
156: dict(y="2015", d="Beard's history of Rome's first thousand years, skeptical of legend and attentive to how the Romans told their own story."),
157: dict(d="The Jewish revolts against Rome, from the Great Revolt to Bar Kokhba, and their long consequences."),
158: dict(t="Shahnameh", e="Penguin Classics, translated by Dick Davis", d="The Persian Book of Kings, Ferdowsi's epic of Iran's mythical and historical past, completed around 1010. Davis renders it in a mix of prose and verse."),
159: dict(y="2007", d="A history of Iran from antiquity to the present, arguing that Iranian identity has persisted through culture and ideas more than through borders."),
160: dict(d="A classic Persian history of the two centuries after the Arab conquest of Iran, and of how Persian language and identity survived them."),
161: dict(t="Esther's Children: A Portrait of Iranian Jews", e="Hardcover", y="2002", d="A richly illustrated portrait of the Jews of Iran and their history, culture and communities across more than two and a half millennia."),
162: dict(y="1991", d="A history, with primary documents, of Jewish communities across the Arab world in the nineteenth and twentieth centuries."),
163: dict(y="1984", d="Lewis's study of Jewish life under Muslim rule from the beginnings of Islam to modern times."),
164: dict(y="2004", d="A memoir of growing up Jewish in Tehran through the Iranian revolution."),
165: dict(y="1959", d="Shackleton's Antarctic expedition, in which the ship was crushed by ice and every man survived. Built from interviews and diaries."),
166: dict(t="Missing 411", e="Six-book slipcase set", y="2011", d="Paulides's series collecting unexplained disappearances in national parks and wilderness areas."),
167: dict(p="W. W. Norton", y="2009", d="Jung's private record of the visions he explored from 1913, illustrated in his own hand and unpublished until 2009."),
168: dict(y="1964", d="The one book Jung made for a general audience, with collaborators, explaining dreams, symbols and the unconscious."),
169: dict(y="1933", d="Essays on dream analysis, the stages of life and the spiritual problem of modern people."),
170: dict(t="Synchronicity", e="Princeton / Bollingen", y="1952", d="Jung's essay on meaningful coincidences with no causal connection, developed partly in conversation with the physicist Wolfgang Pauli."),
171: dict(y="1983", d="Storr's selection of Jung's writings, arranged to trace the development of his ideas."),
172: dict(t="The Freud/Jung Letters", a="William McGuire (ed.)", e="Princeton / Bollingen", y="1974", d="The complete correspondence between Freud and Jung, from their close alliance to the break that ended it."),
173: dict(y="1989", d="A single-volume selection of Freud's writings, edited by his biographer, covering the full range of his work."),
174: dict(a="Robert Moore & Douglas Gillette", y="1990", d="A Jungian account of four archetypes of mature masculinity and the immature forms they take."),
175: dict(y="1973", d="Fromm's study of human aggression, distinguishing defensive aggression from cruelty and destructiveness."),
176: dict(y="2014", d="A psychiatrist's account of how trauma reshapes the body and brain, and of the treatments that help."),
177: dict(y="1980", d="The book that brought cognitive behavioral therapy to general readers, teaching how to identify and challenge distorted thinking."),
178: dict(y="1984", d="Cialdini's study of the principles behind persuasion, such as reciprocity, social proof and scarcity, and how they are used on us."),
179: dict(y="2018", d="A former professional poker player on deciding under uncertainty, and on separating the quality of a decision from the luck of its outcome."),
180: dict(t="The Worldly Philosophers", e="7th edition", y="1953", d="The lives and ideas of the great economists, from Adam Smith to Keynes and Schumpeter. For decades the book that drew people into economics."),
181: dict(t="The Wealth of Nations", e="Glasgow edition, Liberty Fund", y="1776", d="Smith's inquiry into what makes nations prosperous: the division of labor, markets and the limits of government. The founding text of modern economics."),
182: dict(t="Basic Economics", e="5th edition", y="2000", d="Economics without graphs or equations, focused on incentives and consequences, especially the ones nobody intended."),
183: dict(y="1987", d="Sowell's argument that political disagreements trace back to two underlying views of human nature, which he calls the constrained and the unconstrained."),
184: dict(y="2005", d="Essays on cultural history, including Sowell's argument about the origins of certain cultural patterns in the American South."),
185: dict(t="Discrimination and Disparities", e="Revised edition", y="2018", d="Sowell examines why outcomes differ between groups and argues that discrimination is only one of many causes."),
186: dict(y="2013", d="Piketty's historical study of wealth and inequality, arguing that when returns on capital outpace growth, inequality tends to rise."),
187: dict(y="1962", d="Friedman's case that economic freedom is a precondition for political freedom, with proposals that have shaped policy debates ever since."),
188: dict(t="Capitalism, Socialism and Democracy", e="3rd edition", y="1942", d="Schumpeter's study of capitalism's dynamics and future, and the source of the idea of creative destruction."),
189: dict(t="Principles of Economics", e="3rd edition", y="1998", d="Mankiw's widely used introductory textbook, organized around ten principles of economics."),
190: dict(y="1980", d="Porter's framework for analyzing industries and competitors, including the five forces. A foundation of business strategy."),
191: dict(y="2011", d="Rumelt's argument that most of what passes for strategy is goals and slogans, and that real strategy starts with a diagnosis of the problem."),
192: dict(a="Al Ries & Jack Trout", y="1981", d="The classic case that marketing is a battle for a place in the customer's mind, not over product features."),
193: dict(y="2019", d="A practical method for product positioning, especially for products whose value customers do not immediately understand."),
194: dict(y="2003", d="Godin's argument that in a crowded market only the remarkable gets noticed."),
195: dict(a="Al Ramadan, Dave Peterson, Christopher Lochhead & Kevin Maney", y="2016", d="On category design: the idea that the most successful companies create and define new markets rather than compete in existing ones."),
196: dict(t="Crossing the Chasm", e="3rd edition", y="1991", d="Moore's account of the gap between early adopters and the mainstream market, and how technology companies get across it."),
197: dict(y="2013", d="How to talk to customers without being misled by politeness: ask about their lives and past behavior, not about your idea."),
198: dict(t="Running Lean", e="3rd edition", y="2010", d="A step-by-step method for testing a business model before building too much of it."),
199: dict(a="Steve Blank & Bob Dorf", y="2012", d="A detailed guide to customer development, the process of finding a repeatable business model by getting out of the building."),
200: dict(y="2023", d="Walling's guide to building a software business without venture capital, drawn from years of founding and investing in small SaaS companies."),
201: dict(y="2024", d="The founder of Tiny on building a holding company of internet businesses, and a candid account of what ambition cost him."),
202: dict(a="Jason Fried & David Heinemeier Hansson", y="2010", d="The founders of Basecamp argue against much conventional business wisdom: growth for its own sake, long plans and workaholism."),
203: dict(a="Alistair Croll & Benjamin Yoskovitz", p="O'Reilly", y="2013", d="Which metrics matter at each stage of a startup, and how to use data to decide what to build next."),
204: dict(a="Gabriel Weinberg & Justin Mares", y="2014", d="A framework for testing the channels through which a startup can find customers, with the argument that distribution deserves as much attention as product."),
205: dict(a="Étienne Garbugli", y="2014", d="Customer development adapted to selling to businesses, where buyers, users and decision makers are rarely the same person."),
206: dict(y="2018", d="The founder of Zuora on the shift from selling products to selling ongoing relationships, and what it demands of a company."),
207: dict(y="2015", d="Subscription business models and why recurring revenue makes a company more valuable."),
209: dict(y="2020", d="Sales seen from the buyer's side, using jobs to be done to understand the struggle that makes someone ready to buy."),
210: dict(a="Madhavan Ramanujam & Georg Tacke", y="2016", d="The case for designing a product around what customers will pay, starting the pricing conversation before the product is built."),
211: dict(y="2014", d="Eyal's model of habit-forming products: trigger, action, variable reward, investment. Useful to builders, and a clear account of what the attention economy does to users."),
212: dict(a="Sean Ellis & Morgan Brown", y="2017", d="A method for rapid experimentation across a product and its marketing, from the person who coined the term growth hacking."),
213: dict(t="The Art of SEO", a="Eric Enge, Stephan Spencer & Jessie Stricchiola", p="O'Reilly", y="2009", d="A comprehensive reference to search engine optimization, from how search engines work to technical, content and link strategy."),
214: dict(a="John Jantsch & Phil Singleton", y="2016", d="SEO explained for marketers and business owners, tying search strategy to content and business goals."),
215: dict(y="2021", d="Schwartz's argument that SEO should be built around products and user needs rather than keywords and tactics."),
217: dict(a="Simon Kingsnorth", p="Kogan Page", y="2016", d="An integrated approach to planning digital marketing, covering the channels, the measurement and how they fit together."),
218: dict(y="1949", d="Graham's guide to value investing and to the temperament of the defensive investor. Warren Buffett has called it the best book on investing ever written."),
219: dict(a="Karen Berman & Joe Knight", p="Harvard Business Press", y="2008", d="How to read financial statements and understand what the numbers say about a business, written for founders rather than accountants."),
220: dict(a="Susanne Chishti et al. (eds.)", p="Wiley", y="2019", d="Essays from practitioners on the technology reshaping payments."),
221: dict(a="Jeffrey Slater", d="A textbook on the mathematics of business: percentages, interest, discounts, payroll and financial statements."),
222: dict(y="2023", d="Short essays on the things that do not change: human behavior around risk, greed, fear and opportunity."),
223: dict(t="Poor Charlie's Almanack", a="Charles Munger", e="Edited by Peter Kaufman", y="2005", d="Munger's talks and thinking, including his latticework of mental models and his speech on the psychology of human misjudgment."),
224: dict(t="The Great Mental Models", e="Vol. 1", y="2019", d="The first volume of Farnam Street's series on general thinking tools such as first principles, inversion and second-order thinking."),
225: dict(a="Gabriel Weinberg & Lauren McCann", y="2019", d="A large catalogue of mental models from across disciplines, organized for practical use."),
226: dict(y="2010", d="A self-education in business fundamentals, distilled from hundreds of books into a set of core concepts."),
227: dict(t="Notes from Underground", a="Fyodor Dostoevsky", e="Vintage, translated by Richard Pevear and Larissa Volokhonsky", y="1864", d="A bitter, self-lacerating narrator rejects the idea that reason and self-interest can explain human beings. The book that opens the door to existentialism."),
228: dict(t="Crime and Punishment", a="Fyodor Dostoevsky", e="Vintage, translated by Richard Pevear and Larissa Volokhonsky", y="1866", d="A poor student murders a pawnbroker to prove a theory about extraordinary men, then cannot live with it. Dostoevsky's great novel of guilt and redemption."),
229: dict(t="The Idiot", a="Fyodor Dostoevsky", e="Vintage, translated by Richard Pevear and Larissa Volokhonsky", y="1869", d="Dostoevsky's attempt to portray a truly good man, Prince Myshkin, and what happens when goodness meets the society around it."),
230: dict(t="Demons", a="Fyodor Dostoevsky", e="Vintage, translated by Richard Pevear and Larissa Volokhonsky", y="1872", d="A provincial town is torn apart by a radical cell, based on a real political murder. A warning about ideas that consume the people who hold them."),
231: dict(t="The Brothers Karamazov", a="Fyodor Dostoevsky", e="Vintage, translated by Richard Pevear and Larissa Volokhonsky", y="1880", d="Three brothers, a murdered father and the question of whether everything is permitted if there is no God. Dostoevsky's last and largest novel."),
232: dict(t="Short Fiction", a="Leo Tolstoy", e="Norton Critical Edition, edited by Michael R. Katz, 2nd edition", d="Tolstoy's shorter works, including The Death of Ivan Ilyich, with contextual and critical material."),
233: dict(t="Hadji Murad", a="Leo Tolstoy", e="Modern Library, translated by Aylmer Maude, introduction by Azar Nafisi", y="1912", d="Tolstoy's late short novel about a Chechen warrior caught between the Russian empire and his own leader, published after Tolstoy's death."),
234: dict(t="Cancer Ward", a="Aleksandr Solzhenitsyn", e="FSG Classics", y="1968", d="Patients in a Soviet cancer ward in the 1950s, among them a former labor camp prisoner, confront illness and the system that shaped their lives."),
235: dict(t="Dead Souls", a="Nikolai Gogol", e="NYRB Classics, translated by Donald Rayfield", y="1842", d="A swindler travels provincial Russia buying up dead serfs who still exist on paper. Gogol's comic, unfinished masterpiece."),
236: dict(t="Les Misérables", e="Penguin Classics Deluxe, translated by Norman Denny", y="1862", d="Hugo's vast novel of Jean Valjean, a convict pursued by the law across decades of French history, and of mercy set against justice."),
237: dict(t="The Stranger", e="Vintage International, translated by Matthew Ward", y="1942", d="Meursault kills a man on a beach and is condemned less for the crime than for his indifference. Camus's first novel of the absurd."),
238: dict(t="The Plague", e="Vintage International", y="1947", d="An epidemic seals off an Algerian city, and its people respond with courage, denial and solidarity. Often read as an allegory of occupation and of any shared catastrophe."),
239: dict(t="Candide", e="Penguin Classics, translated by Theo Cuffe, and the Norton Critical Edition", y="1759", d="Voltaire's satire of philosophical optimism, following a naive young man through disaster after disaster. It ends in the advice to cultivate our garden."),
240: dict(t="The Magic Mountain", e="Oxford World's Classics, translated by Simon Pare", y="1924", d="A young man visits a sanatorium in the Swiss Alps for three weeks and stays seven years. Mann's novel of time, illness and European ideas before the First World War."),
241: dict(y="1919", d="A young man's awakening under the influence of a mysterious friend, and his break from the respectable world he was raised in."),
242: dict(t="The World of Yesterday", e="Translated by Anthea Bell", y="1942", d="Zweig's memoir of the cultured, secure Europe he grew up in and its destruction, finished shortly before his death in exile."),
243: dict(t="The Metamorphosis", e="Norton, translated by Susan Bernofsky", y="1915", d="Gregor Samsa wakes to find himself transformed into a monstrous insect, and his family's response becomes the real subject."),
244: dict(t="Satantango", e="New Directions, translated by George Szirtes", y="1985", d="A decaying Hungarian collective farm awaits the return of a man thought dead, in long, spiraling sentences. Krasznahorkai's first novel."),
245: dict(t="Lolita", e="Vintage", y="1955", d="Narrated by Humbert Humbert, an eloquent and self-justifying abuser. A study of how beautiful language can be used to disguise monstrous acts."),
246: dict(t="For Whom the Bell Tolls", e="Scribner", y="1940", d="An American volunteer is sent to blow up a bridge during the Spanish Civil War. Hemingway's longest novel, about three days and a whole life."),
247: dict(y="1952", d="An aging Cuban fisherman hooks a great marlin and fights it for days. Short, spare and central to Hemingway's Nobel Prize."),
248: dict(t="The Complete Short Stories", e="Finca Vigía edition", y="1987", d="The collected stories, including previously unpublished work, where Hemingway's compression is at its sharpest."),
249: dict(t="The Road", e="Vintage International", y="2006", d="A father and son walk across a burned America toward the coast. McCarthy's bleakest landscape and his most tender book. It won the Pulitzer Prize."),
250: dict(t="Sabbath's Theater", e="Vintage International", y="1995", d="A disgraced puppeteer spirals through grief and appetite. Roth's most outrageous novel and, for many readers, his best. It won the National Book Award."),
251: dict(t="A Little Life", e="Anchor", y="2015", d="Four friends in New York across several decades, centered on one man whose past will not let him go. A long, harrowing novel about friendship and suffering."),
252: dict(y="2013", d="A boy survives a museum bombing that kills his mother and keeps a small Dutch painting that shapes the rest of his life. It won the Pulitzer Prize."),
253: dict(y="2000", d="A house that is larger on the inside than the outside, told through footnotes, found documents and typography that becomes part of the story."),
254: dict(t="Middlemarch", e="Penguin Classics Deluxe", y="1871", d="The lives of an English provincial town, above all Dorothea Brooke's. Often called the greatest English novel for its moral intelligence and range."),
255: dict(t="Wuthering Heights", e="Penguin Classics", y="1847", d="The passion between Heathcliff and Catherine and the damage it does across two generations on the Yorkshire moors."),
256: dict(t="The Picture of Dorian Gray", e="Belknap Press of Harvard University Press, edited by Nicholas Frankel", y="1890", d="A young man stays beautiful while his portrait ages and corrupts. This edition restores the uncensored text Wilde first submitted, with Frankel's annotations."),
257: dict(y="1878", d="Passion and restlessness on Egdon Heath, a landscape Hardy makes into a character of its own."),
258: dict(t="The Divine Comedy", a="Dante Alighieri", e="Translated by Robert and Jean Hollander, three volumes", d="Dante's journey through Hell, Purgatory and Paradise. The Hollander translation carries extensive commentary drawn from centuries of scholarship."),
259: dict(t="Paradise Lost", a="John Milton", e="Penguin Classics, edited by John Leonard", y="1667", d="Milton's epic of the fall of Satan and of humankind, written to justify the ways of God to men. Satan is its most memorable figure."),
260: dict(t="The Iliad and The Odyssey", e="Translated by Robert Fagles", d="The two foundational epics of the West: the wrath of Achilles at Troy and Odysseus's long voyage home."),
261: dict(t="The Aeneid", e="Penguin Classics Deluxe, translated by Robert Fagles", d="Virgil's epic of Aeneas fleeing Troy to found the people who would become Rome, written under Augustus."),
262: dict(t="The Riverside Shakespeare", a="G. Blakemore Evans (ed.)", e="2nd edition", y="1974", d="The complete works in a single scholarly volume, with introductions and textual notes. A standard edition for decades."),
263: dict(d="Some two hundred and fifty myths of transformation, linked from the creation of the world to the deification of Julius Caesar. A source for Western art and literature ever since."),
264: dict(t="Rhetoric", e="Penguin Classics, translated by Hugh Lawson-Tancred", d="Aristotle's analysis of persuasion through character, emotion and argument. Still the foundation of how rhetoric is taught."),
265: dict(t="Collected Fictions", e="Penguin, translated by Andrew Hurley", y="1998", d="All of Borges's fiction in one volume: labyrinths, infinite libraries, imaginary books and mirrors."),
266: dict(t="Selected Non-Fictions", e="Penguin, edited by Eliot Weinberger", y="1999", d="Borges's essays, reviews and lectures, as strange and brilliant as his stories."),
267: dict(t="In the Woods", e="Penguin", y="2007", d="A Dublin detective investigates a child's murder in the woods where, as a boy, he survived something he cannot remember. French's first novel."),
268: dict(y="2009", d="A financier's death investigated backward through three narratives across Europe and decades, in a novel about money, espionage and secrets."),
269: dict(y="2022", d="A mother watches her son commit a murder, then wakes each day further back in time, working backward to find what led to it."),
270: dict(y="2001", d="A novel about Charles Carter, a stage magician in 1920s America, drawn into a mystery when a president dies suddenly after attending his show."),
271: dict(t="The Culture novels", y="1987", d="Banks's series about the Culture, a post-scarcity civilization run by benevolent artificial minds, told mostly through the people at its edges."),
}


import csv, os, re, shutil, sys, time, unicodedata

SITE = os.path.expanduser("~/Sites/zibalion")
CSV  = os.path.join(SITE, "data", "library.csv")
PAGE = os.path.join(SITE, "process", "index.html")
LIBD = os.path.join(SITE, "library")
BUILD = os.path.join(SITE, "build-library.py")


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)


def main():
    for p in (CSV, PAGE, BUILD):
        if not os.path.exists(p):
            sys.exit(f"ABORT: missing {p}")

    stamp = time.strftime("%Y%m%d-%H%M%S")
    shutil.copy(CSV, CSV + ".bak-" + stamp)
    shutil.copy(PAGE, PAGE + ".bak-" + stamp)

    with open(CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        cols = list(rows[0].keys())

    remap = {}
    for r in rows:
        old = slugify(r["title"])

        # Open Library's text fields were pulled from random editions. Clear them.
        for k in ("publisher", "imprint", "year", "isbn", "edition"):
            r[k] = ""

        v = D.get(int(r["id"]), {})
        if "t" in v: r["title"] = v["t"]
        if "a" in v: r["author"] = v["a"]
        if "e" in v: r["edition"] = v["e"]
        if "y" in v: r["year"] = v["y"]
        if "p" in v: r["publisher"] = v["p"]
        if "d" in v: r["about"] = v["d"]

        new = slugify(r["title"])
        if new != old:
            remap[old] = new

    # guard against two books landing on the same URL
    seen = {}
    for r in rows:
        s = slugify(r["title"])
        if s in seen:
            sys.exit(f"ABORT: slug collision '{s}' between rows {seen[s]} and {r['id']}. Nothing written.")
        seen[s] = r["id"]

    with open(CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})

    # point the shelf list at the new URLs
    src = open(PAGE, encoding="utf-8").read()
    n = 0
    for old, new in remap.items():
        a, b = f'href="/library/{old}/"', f'href="/library/{new}/"'
        if a in src:
            src = src.replace(a, b)
            n += 1
    open(PAGE, "w", encoding="utf-8").write(src)

    # the year shown is first publication, so say so
    b = open(BUILD, encoding="utf-8").read()
    b = b.replace('("year", "Year")', '("year", "First published")')
    open(BUILD, "w", encoding="utf-8").write(b)

    # rebuild from clean so no stale pages survive at old URLs
    if os.path.isdir(LIBD):
        shutil.rmtree(LIBD)

    described = sum(1 for r in rows if r.get("about", "").strip())
    print(f"Updated {len(rows)} rows, {described} with descriptions.")
    print(f"Cleaned {len(remap)} titles, relinked {n} shelf entries to the new URLs.")


if __name__ == "__main__":
    main()
