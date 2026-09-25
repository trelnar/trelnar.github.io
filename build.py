import os, time
V=str(int(time.time()))
NAV=[("work","index.html","Work"),("lead","leadership.html","Leadership"),("about","about.html","About"),("contact","contact.html","Contact")]
def shell(title, body, on, depth=0, dark=False):
    r="../" if depth else ""; ON=' class="on"'
    nav="".join(f'<li><a href="{r}{h}"{ON if k==on else ""}>{t}</a></li>' for k,h,t in NAV)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{title}</title>
<link rel="stylesheet" href="{r}css/site.css?v={V}"></head>
<body class="locked{' dark' if dark else ''}"><div id="site">
<div class="wrap"><header class="top"><a class="brand" href="{r}index.html">Kevin Ellis</a><nav><ul>{nav}</ul></nav></header></div>
{body}
<footer>Kevin Ellis, 2026. Oracle Health work is described at the level of method and structure; unreleased designs, customer names, and internal data are excluded.</footer>
</div><script src="{r}js/gate.js?v={V}"></script><script src="{r}js/slides.js?v={V}"></script><script src="{r}js/video.js?v={V}"></script></body></html>'''

def img(src, cap=""):
    return f'<figure><img src="{src}" alt="">{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
def slot(label, cap=""):
    return f'<figure><div class="slot">{label}</div>{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
def slides(srcs, cap=""):
    ON=' class="on"'
    imgs="".join(f'<img src="{x}" alt=""{ON if i==0 else ""}>' for i,x in enumerate(srcs))
    return f'<figure><div class="slides" style="aspect-ratio:1024/668">{imgs}</div>{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
def video(src, poster, cap="", controls=False, loop=True, maxw=None):
    st = f' style="max-width:{maxw}px"' if maxw else ""
    if loop:
        attrs = "autoplay muted loop playsinline" + (" controls" if controls else "")
        return f'<figure{st}><video src="{src}" poster="{poster}" {attrs}></video>{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
    return f'<figure{st}><div class="vid"><video src="{src}" poster="{poster}" playsinline preload="metadata"></video><button class="play" aria-label="Play"></button></div>{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
def row(left, right, cls=""):
    if not left: cls=(cls+" textonly").strip()
    return f'<div class="row {cls}"><div class="col-img">{left}</div><div class="col-text">{right}</div></div>\n'

def case(title, lede, year, hero, rows, prev, nxt, herocap=""):
    head=f'<h1>{title}</h1><p class="lede">{lede}</p><p class="year">{year}</p>'
    body='<article class="case wrap">'+row(img(f"../img/tiles/{hero}.jpg",herocap), head, "head")
    for left,right in rows: body+=row(left,right,"" if right else "gallery")
    body+=f'<div class="next"><a href="{prev[0]}">&larr; {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} &rarr;</a></div></article>\n'
    return body

pages={}
tiles=[("oracle","Oracle Health"),("amazon","Amazon"),("ebay","eBay"),("earlier","Earlier Work")]
pages["index.html"]=shell("Kevin Ellis, Design Leadership",'<div class="wrap"><div class="tiles">'+"".join(
    f'<a class="tile" href="work/{k}.html"><img src="img/tiles/{k}.jpg" alt="{t}"><span>{t}</span></a>' for k,t in tiles)+'</div></div>',"work",dark=True)

pages["work/oracle.html"]=shell("Oracle Health",case("Oracle Health",
 "Director, User Experience Design. I established Experience Core, the platform design team that owns the interaction patterns, components, design system, and research practice across Oracle Health's clinical products. Experience Core sets the design standard for five product teams and dozens of clinician-facing applications. Most of the work is unreleased and stays inside Oracle. What I can show is the operating model, because the operating model is the work. I am a named inventor on eight patent applications filed by Oracle during this period.",
 "2024 to present","oracle",[
 (video("../img/oracle/journey.mp4","../img/oracle/journey-poster.jpg","Thirty-four patterns, grouped by where they sit in the clinician's journey. The team is organized the same way."),
  '''<h2>Organize around the journey</h2>
<p>Experience Core inherited thirty-four patterns with no structure. I grouped them by the stage of the clinician's journey they serve: access, triage, interpret, execute, collaborate, follow up. Each stage has a job the user is trying to do, in their words. Pattern ownership, and then the team itself, was organized the same way, so a designer owns a stretch of the journey rather than a pile of components.</p>'''),
 (img("../img/oracle/tooling-spec.jpg","The tooling pipeline: intent in, guidelines and skills pulled from the design system, output triaged into specs and prototypes. Every design team works from the same library."),
  '''<h2>From comps to rules</h2>
<p>We've stopped shipping Figma comps. I treated it as an operating-model shift rather than a tooling swap. We split the output in two. Components get guidelines, which are reference material a person or a model can look up. Layouts and patterns get skills, which carry the judgment about when to use something, when not to, and how to configure it. The deliverable became the rules, not the pictures. A skill selects and configures; it does not code.</p>
<p>I wrote the first skills myself so I understood what the toolchain actually needed, then gave each designer ownership of a pattern and its skill. We built an internal prototyping pipeline, custom tooling, and a shared skill library in a team repo. Concept to testable prototype went from weeks to days, and the team validated considerably more concepts per cycle, internally and with customers.</p>'''),
 (img("../img/oracle/codex-learning-day.jpg","Codex learning day. Every designer shipped a working prototype in one session. None of it is product; all of it is the new muscle."),
  '''<h2>Upskilling the team</h2>
<p>A new toolchain is a leadership problem before it is a tooling problem. I ran a learning day: no product work, no clinical constraints, a made-up brief per designer, and one rule, ship a working prototype by the end of the day. Everyone did. Some of it was silly on purpose. That was the point; the fear of the tool went away in an afternoon.</p>
<p>From there each designer took ownership of a pattern and its skill, so the learning had somewhere to land. The prototyping pipeline, the custom tooling, and the shared skill library in the team repo all came out of designers building for themselves, not out of a mandate. Concept to testable prototype went from weeks to days.</p>'''),
 (img("../img/oracle/layout-validation.jpg","Three stages, three gates, one scale for every layout."),
  '''<h2>Three gates and a definition of done</h2>
<p>Layouts kept getting misaligned because nobody shared a definition of done. I wrote one, as three gates. Release approval by the platform leads with Dev and Product follows the third.</p>
<p>Landing it meant sequencing alignment deliberately: eight Dev and PM pillar leads first, then SVP peers, then the top. The Action List skill and a three-role human-factors demo became the reference example senior engineering leadership pointed to.</p>'''),
 ],("../index.html","Work"),("amazon.html","Amazon")),"work",1)

pages["work/amazon.html"]=shell("Amazon",case("Amazon",
 "One company, two businesses. Head of Design and Research for Amazon Fashion, 2015 to 2019, growing the org from 5 designers and 2 researchers to 20. Concept-to-launch of Prime Wardrobe. Then Head of Design and Research for Amazon Photos, across mobile, web, desktop, Echo Show, and Fire TV.",
 "2015 to 2022","amazon",[
 (video("../img/amazon/cooper-launch-2.mp4","../img/amazon/cooper-launch-2-poster.jpg","The launch video. Sound on.",loop=False,maxw=402)+video("../img/amazon/cooper-process-1.mp4","../img/amazon/cooper-process-1-poster.jpg","Cooper: the process, in my words. Sound on.",loop=False)+video("../img/amazon/cooper-prototypes.mp4","../img/amazon/cooper-prototypes-poster.jpg","Cooper prototypes, built and tested with customers before the rebuild."),
  '''<h2 class="part">Amazon Photos</h2>
<p>Photos began as a cloud storage service that happened to hold photos, and years of feature additions by different teams had accumulated into an experience that didn't compete with the native photo apps on anyone's phone. At six million monthly active customers it was underperforming for a Prime-bundled service. Leadership was committed to fixing it.</p>
<h3>Project Cooper</h3>
<p>That case got the green light for a full teardown and rebuild. Research settled what customers actually wanted, in order: show me my photos, help me find them fast, let me share them easily, surprise me with memories, show me my account. That's the whole list. The home screen was rebuilt to meet the first two immediately, and the rest of the model followed: my memories, quick-find tools, what I've shared and with whom, my account.</p>
<p>We set shared design and product tenets with Dev and PM partners at the start, so three orgs argued from one set of decision criteria instead of relitigating tradeoffs at every review. The design direction shaped the rebrand that shipped alongside the rebuild. Most of the feature set carried over unchanged, so the gains came from making it usable and findable.</p>
<h3>Shipped</h3>
<p><span class="stat"><b>61% to 78%</b>CSAT within six months of launch</span> <span class="stat"><b>8 to 15</b>designers, adding research, motion, and design technology</span></p>'''),
 (img("../img/amazon/wardrobe-screens.jpg","Prime Wardrobe, then Prime Try Before You Buy: fill a box from the app.")+img("../img/amazon/wardrobe-box.jpg","It came in a resealable, postage-paid box for hassle-free returns after try-on.")+img("../img/amazon/wardrobe-stylist.jpg","Prime Stylist concept: a digital version of the customer for a virtual try-on."),
  '''<h2 class="part">Amazon Fashion</h2>
<p>In 2015 less than a tenth of the roughly $300 billion spent on clothing and shoes in the US was spent online, and Amazon was investing heavily to change that. Search and discovery were strong; evaluating a garment on a detail page was the weak point. Prime Wardrobe, then called Prime Try Before You Buy, took aim at it.</p>
<h3>Prime Wardrobe</h3>
<p>Shop for clothing and shoes, fill a box, have it shipped free, try everything for seven days, send back what you don't want in the same self-sealing prepaid box, pay only for what you keep. It was complex even for Amazon, touching every part of the retail supply chain, digital and physical. I worked directly with the product owner and executive leadership to pitch and resource the design, and saw it through to launch. Prime Stylist followed, a curated-box model for customers who wanted guidance.</p>'''),
 (img("../img/amazon/luxury.jpg","Early concept work for Amazon Luxury."),
  '''<h2>Luxury Stores</h2>
<p>The last project I led there was the luxury brands exploration: a walled garden inside the Amazon app where only the most exclusive fashion brands could be bought, with minimal store presence and the content carrying the experience. No legacy to design around. It launched more than two years after we designed it, and looked remarkably like the original work.</p>
'''),
 (img("../img/amazon/fashion-detail-page.jpg","Rethinking the product detail page for a more content-led, fashion-centric interaction."),
  '''<h2>The detail page, as a lesson</h2>
<p>For four years, improving the product detail page for fashion customers was constant work, and every change had to win for all Amazon customers and pass web labs before it shipped. It was glacially incremental and it taught me how to move a shared platform: negotiate, test, and pick the changes that help everyone. I later aligned my team, marketing design, and the Shopbop design team on shared tenets so the fashion experience read as one thing across Amazon.</p>'''),
 ],("oracle.html","Oracle Health"),("ebay.html","eBay")),"work",1)

pages["work/ebay.html"]=shell("eBay",case("eBay",
 "Director of Product Design, Seller Experience. I owned the seller experience end to end, web and mobile, across consumer, small business, and enterprise sellers on a marketplace running roughly $73 billion in annual GMV with 132 million active buyers. Relative to the buyer side, selling had been neglected for years, which meant the opportunity was large and the organizational habits were set.",
 "2022 to 2024","ebay",[
 (video("../img/ebay/magical-listing.mp4","../img/ebay/magical-listing-poster.jpg","The Magical Listing Tool, as launched. eBay's video, sound on.",loop=False),
  '''<h2>eBay's first generative AI feature</h2>
<p>Most listings on eBay had no description, and when buyers compared two similar items they almost always chose the one with a description. My team designed and shipped the Magical Listing Tool, which drafts title, description, and item specifics for sellers, end to end with eBay's AI team from concept to launch in September 2023. It was the first of a set of tools aimed at removing the effort from listing: start from a photo, or a video with voice-over, and let the system do the rest.</p>
<p><span class="stat"><b>30%</b>of daily US app sellers tried it in the first weeks</span> <span class="stat"><b>95%+</b>of those kept the AI draft, with or without edits</span> <span class="stat"><b>80%+</b>CSAT</span></p>
<p class="meta">Figures from <a href="https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/" rel="noopener">eBay's launch post</a>. Named Best Overall Generative AI Solution in the <a href="https://innovation.ebayinc.com/stories/ebays-magical-listing-tool-wins-ai-breakthrough-award-for-best-overall-generative-ai-solution/" rel="noopener">AI Breakthrough Awards</a>.</p>'''),
 (img("../img/ebay/sprint-journey.jpg","One step of one persona's journey from the sprint. The seller's words set the target; the concept answers them."),
  '''<h2>The mobile seller sprint</h2>
<p>Small-business sellers were running their businesses on phones, and eBay's mobile selling features trailed competitors by a wide margin. SMBs were 6 percent of sellers and 42 percent of revenue. I ran one of three Lighthouse design sprints on this: cross-disciplinary teams from Product, Marketing, and Engineering through a structured discovery track, three personas plotted against their emotional and functional journeys, overlaid to find the shared territories, then concepts for each territory that graduate a seller from novice to pro. The vision was one flexible system rather than a fixed feature set, because a seller's needs change as the business grows. The concepts themselves stay internal; the method is the point.</p>
<p>The other change that mattered: I got Product to commit design into their six-month planning cycle, so the team shaped roadmaps before they were set instead of receiving them finished.</p>'''),
 ],("amazon.html","Amazon"),("earlier.html","Earlier Work")),"work",1)

pages["work/earlier.html"]=shell("Earlier Work",case("Earlier Work",
 "Adobe, Nokia, and THANK YOU Studio. Agency and in-house, San Francisco and Copenhagen, before Amazon.",
 "2006 to 2015","earlier",[
 (video("../img/earlier/firephone.mp4","../img/earlier/firephone-poster.jpg","Fire Phone design system. THANK YOU Studio for Amazon."),""),
 (slides([f"../img/earlier/fire-{i}.jpg" for i in range(1,13)],"Kindle Fire HD launch site for Amazon. THANK YOU Studio, 2012."),""),
 (img("../img/earlier/nokia.jpg","Nokia N9, MeeGo. Our team focused on the MeeGo OS design system, as well as 3rd-party app guidelines."),""),
 ],("ebay.html","eBay"),("../leadership.html","Leadership"),herocap="Design exploration of Toyota's native in-car navigation system."),"work",1)

pages["leadership.html"]=shell("How I Lead",'''<article class="case wrap">'''+row(
 "",
 '''<h1>How I Lead</h1><p class="lede">Design is a business capability, and it earns that standing by being legible to the rest of the company.</p>
<h2>Design Quarterly</h2>
<p>At Photos the team published a Design Quarterly: our work, our process, new people, wins, open roles. It went to the whole org, to external subscribers, and to Amazon Design. It kept partners aware of what we were doing and it kept the team connected to the larger story their pieces added up to. In the first summer of Covid we put out an issue with no design work in it at all; everyone wrote and designed a spread on what was helping them cope and what gave them hope.</p>''',"head")+row('',
 '''<h2>Operating habits</h2>
<ul>
<li>Tenets set with partners at the start, so the argument happens once.</li>
<li>A written definition of done.</li>
<li>A weekly written note that ends up read beyond its intended audience.</li>
<li>Ownership assigned by pattern, so every designer has something that is theirs.</li>
<li>Staying hands-on with the tools, because the toolchain is changing and I want to understand it before I ask the team to.</li>
</ul>
<h2>Building the org</h2>
<p>Amazon Fashion, 5 designers and 2 researchers to 20. Amazon Photos, 8 to 15, adding research, motion, and design technology. eBay, 25 designers with research and design program management. Oracle Health, a platform design team that did not exist before I made the case for it. Across all of it the pattern holds: turn ambiguous direction into a structured, verifiable program, and build the team that can run it without me in the room.</p>''')+'</article>',"lead")

pages["about.html"]=shell("About",'<article class="case wrap">'+row('<img class="headshot" src="img/headshot-600.jpg" alt="Kevin Ellis">',
 '''<h1>About</h1>
<p>I grew up in Alaska drawing and painting. I studied graphic design at California College of the Arts in San Francisco, then human-computer interaction and electronic communication design at Emily Carr University in Vancouver. My first digital work was for an agency in Reykjav&iacute;k, then Copenhagen, then back to San Francisco for design leadership roles at Adobe, Yahoo, Nokia, and eventually my own agency with partners in Copenhagen.</p>
<p>The agency built proof-of-concept work that large clients turned into real products. I missed the client side and joined the biggest of them, Amazon, in 2015. Seven years there, then eBay, then Oracle Health, where I built the platform design organization for the clinical products.</p>
<p>Twenty years of leading design teams. I build design organizations, the operating models they run on, and the AI-native tooling that changes how they work.</p>
<p class="meta">Seattle, WA</p>''',"head about")+'</article>',"about")

pages["contact.html"]=shell("Contact",'<article class="case wrap">'+row('',
 '''<h1>Contact</h1>
<p><a href="mailto:kevinellis@gmail.com">kevinellis@gmail.com</a></p>
<p>(415) 606-1720</p>
<p><a href="https://www.linkedin.com/in/kevinellisdesign" rel="noopener">linkedin.com/in/kevinellisdesign</a></p>''',"head")+'</article>',"contact")

for path,html in pages.items():
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True); open(path,"w").write(html)
print(len(pages),"pages")
