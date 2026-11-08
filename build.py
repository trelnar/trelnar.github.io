import os, time
from iso import pipeline, skilltest, consolidate, landing, investigation, org, journey, boundary, ladder, teeup, modes, gates
V=str(int(time.time()))
NAV=[("work","index.html","Work"),("lead","leadership.html","Leadership"),("about","about.html","About"),("contact","contact.html","Contact")]
def shell(title, body, on, depth=0, dark=False):
    r="../" if depth else ""; ON=' class="on"'
    nav="".join(f'<li><a href="{r}{h}"{ON if k==on else ""}>{t}</a></li>' for k,h,t in NAV)
    brand='<span class="brand">Kevin Ellis</span>' if (on=="work" and not depth) else f'<a class="brand" href="{r}index.html">Kevin Ellis</a>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{title}</title>
<link rel="stylesheet" href="{r}css/site.css?v={V}"></head>
<body class="locked{' dark' if dark else ''}"><div id="site">
<div class="wrap"><header class="top">{brand}<nav><ul>{nav}</ul></nav></header></div>
{body}
<footer>Kevin Ellis, 2026. Employer and client work is shown at the level of method and outcomes; unreleased designs, customer names, and internal data are excluded.</footer>
</div><script src="{r}js/gate.js?v={V}"></script><script src="{r}js/slides.js?v={V}"></script><script src="{r}js/video.js?v={V}"></script><script src="{r}js/tiles.js?v={V}"></script></body></html>'''

def img(src, cap="", href=None):
    im=f'<img src="{src}" alt="">'
    if href: im=f'<a href="{href}" target="_blank" rel="noopener" title="Open full size">{im}</a>'
    return f'<figure>{im}{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
def fig(svg, cap=""):
    return f'<figure>{svg}{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
def slot(label, cap=""):
    return f'<figure><div class="slot">{label}</div>{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
def slides(srcs, cap=""):
    ON=' class="on"'
    imgs="".join(f'<img src="{x}" alt=""{ON if i==0 else ""}>' for i,x in enumerate(srcs))
    return f'<figure><div class="slides" style="aspect-ratio:1024/668">{imgs}</div>{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
def video(src, poster, cap="", controls=False, loop=True, maxw=None):
    st = f' style="max-width:{maxw}px;margin-left:auto"' if maxw else ""
    if loop:
        attrs = "autoplay muted loop playsinline" + (" controls" if controls else "")
        return f'<figure{st}><video src="{src}" poster="{poster}" {attrs}></video>{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
    return f'<figure{st}><div class="vid"><video src="{src}" poster="{poster}" playsinline preload="metadata"></video><button class="play" aria-label="Play"></button></div>{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
def row(left, right, cls=""):
    if not left: cls=(cls+(" chapter" if '<h2 class="part">' in right else " textonly")).strip()
    return f'<div class="row {cls}"><div class="col-img">{left}</div><div class="col-text">{right}</div></div>\n'

def case(title, lede, year, hero, rows, prev, nxt, herocap=""):
    head=f'<h1>{title}</h1>'+(lede if lede.lstrip().startswith("<") else f'<p class="lede">{lede}</p><p class="year">{year}</p>')
    body='<article class="case wrap">'+row("", head, "head")
    for left,right in rows: body+=row(left,right,"" if right else "gallery")
    body+=f'<div class="next"><a href="{prev[0]}">&larr; {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} &rarr;</a></div></article>\n'
    return body

pages={}
tiles=[("oracle","Oracle Health","oracle"),("amazon","Amazon","amazon"),("ebay","eBay","ebay"),("earlier","Earlier Work","earlier-3")]
pages["index.html"]=shell("Kevin Ellis, Design Leadership",'<div class="wrap"><div class="tiles">'+"".join(
    f'<a class="tile" href="work/{k}.html"><img src="img/tiles/{f}.jpg" alt="{t}"><span>{t}</span></a>' for k,t,f in tiles)+'</div></div>',"work",dark=True)

pages["work/oracle.html"]=shell("Oracle Health",case("Oracle Health",
'''<p class="lede">Director, User Experience Design, 2024 to present.</p>
<p>I joined Oracle Health to lead the design of the core task-management experience for an AI-native EHR. It started with ambulatory clinical workflows and grew into one universal pattern for every role across the whole product. Out of that work I formed Experience Core, our platform design team, and built its AI workflows with engineering, which took concept-to-testable-prototype from weeks to days. This work has resulted in <mark>nine AI patent applications I am a named inventor on.</mark></p>
<p class="caveat">Most of this is unreleased, so the cases are told through method and diagrams.</p>''',
 "2024 to present","oracle",[
 # ------------------------------------------------------------ case 1
 (img("../img/oracle/action-list.png","From many disparate views, into one."),
  '''<h2>From Inbox to Action List</h2>
<p>What started as a fix for the clinician inbox is now Oracle Health’s universal work list pattern across the entire EHR platform: every role, every workflow, from ambulatory, acute, patient administration, rev cycle and reimbursements. One place to see the work and do it, instead of a different queue in every corner of the product.</p>
<p><em>Public release of this experience is set for Oracle Health Summit, Q1 2027.</em></p>'''),
 # ------------------------------------------------------------ case 2
 (video("../img/oracle/journey.mp4","../img/oracle/journey-poster.jpg","Thirty-four patterns, grouped by where they sit in the clinician’s journey. The team is organized the same way."),
  '''<h2>Experience Core</h2>
<p>Oracle Health already had a patterns team and a shared goal of one design language. What it lacked was structure: thirty-four patterns, several managers, no single thread of ownership.</p>
<p>I rebuilt the team around the clinician’s journey instead of the pattern list. Six segments, each with a lead designer and research partner who own their segment, end to end. We called ourselves Experience Core.</p>
<p>The team runs on six habits. Concepts, components, and guidelines define what we make. Cadence, governance, and evangelism define how we work. Guidance lives where the work lives, not in redlines, but in a living, coded reference app.</p>'''),
 # ------------------------------------------------------------ case 3
 (img("../img/oracle/ai-ux-platform.png","The platform, end to end: intent in, guidelines and context pulled from the design system, a spec and a working prototype out, triaged to the right team. Click to enlarge.",href="../img/oracle/ai-ux-platform.png"),
  '''<h2>From intent to working code</h2>
<p>Instead of handing off Figma comps, specs and guidelines to our partners, we’ve reimagined our design process around a shared platform. The design system’s components, layouts, guidelines, and guardrails live in one place that designers and the AI tooling both read from. A designer states an intent, the platform pulls in the right context, and the result is a spec and a working prototype in the same pass, routed to the right team.</p>
<p>Going from concept to testable prototype has gone from weeks to days, and every team now works from the same source of truth.</p>'''),
 (img("../img/oracle/learning-day.jpg","Learning day. Every designer left with a working prototype. Click to enlarge.",href="../img/oracle/learning-day.jpg"),
  '''<p>AI talk in tech has come rapid-fire, and for most people it has been overwhelming. The way through is always together, and it’s even better when it’s fun. We gather everyone for regular team collaborations with no product work, no clinical constraints, a made-up brief for each team, and one rule: ship a working prototype by day’s end. Be silly, be free, be together.</p>'''),
 ],("../index.html","Work"),("amazon.html","Amazon")),"work",1)

pages["work/amazon.html"]=shell("Amazon",case("Amazon",
'''<ul class="facts">
<li><b>Role</b> Head of Design and Research. Amazon Fashion, 2015 to 2019. Amazon Photos, 2019 to 2022.</li>
<li><b>Team</b> Fashion: 5 designers and 2 researchers to 20, adding program management, design technology, and managers. Photos: 8 to 19.</li>
<li><b>Work</b> Prime Wardrobe, concept to launch. Luxury Stores. Project Cooper, the Photos rebuild: CSAT 61% to 78% in six months. Mobile, web, desktop, Echo Show, Fire TV.</li>
</ul>''',
 "2015 to 2022","amazon",[
 (video("../img/amazon/cooper-launch-2.mp4","../img/amazon/cooper-launch-2-poster.jpg","The launch video. Sound on.",loop=False,maxw=402),
  '''<h2 class="part">Amazon Photos</h2>
<p>Photos began as cloud storage that happened to hold photos; years of additions by different teams left it trailing native apps. Six million monthly active customers, and underperforming for a Prime-bundled service.</p>
<h3>Project Cooper</h3>
<p>Leadership green-lit a teardown and rebuild. Research set the order. The whole list: show me my photos, help me find them fast, let me share them easily, surprise me with memories, show me my account. The home screen took the first two; the rest followed.</p>
<p>We set tenets with Dev and PM first, so three orgs made decisions from one set of criteria. The design direction shaped the rebrand that shipped alongside. Most features carried over unchanged; the gain was making them usable and findable.</p>
<h3>Shipped</h3>
<p><span class="stat"><b>61% to 78%</b>CSAT within six months of launch</span></p>'''),
 ('<div class="pair">'+video("../img/amazon/cooper-process-1.mp4","../img/amazon/cooper-process-1-poster.jpg","Cooper: the process, in my words. Sound on.",loop=False)+video("../img/amazon/cooper-prototypes.mp4","../img/amazon/cooper-prototypes-poster.jpg","Cooper prototypes, built and tested with customers before the rebuild.")+'</div>',""),
 (img("../img/amazon/wardrobe-screens.jpg","Prime Wardrobe, then Prime Try Before You Buy: fill a box from the app.")+img("../img/amazon/wardrobe-box.jpg","It came in a resealable, postage-paid box for hassle-free returns after try-on.")+img("../img/amazon/wardrobe-stylist.jpg","Prime Stylist concept: a digital version of the customer for a virtual try-on."),
  '''<h2 class="part">Amazon Fashion</h2>
<p>In 2015 the US spent roughly $300 billion on clothing and shoes, under a tenth of it online. Prime Wardrobe, born Prime Try Before You Buy, took aim at the weak point: judging a garment from a detail page.</p>
<h3>Prime Wardrobe</h3>
<p>Fill a box, shipped free, seven days to try, pay only for what you keep. I pitched and resourced the design with the product owner and executive leadership, and saw it through to launch. Prime Stylist, a curated box, followed.</p>'''),
 (video("../img/amazon/luxury-walkthrough.mp4","../img/amazon/luxury-walkthrough-poster.jpg","The early prototype that pitched Amazon Luxury, placeholder name X. Approved by executive leadership, it became the reference for the final experience. Click to play.",loop=False,maxw=320)+img("../img/amazon/luxury.jpg","Early concept work for Amazon Luxury."),
  '''<h2>Luxury Stores</h2>
<p>My last project there was the luxury brands exploration: a walled garden in Amazon's app, only the most exclusive fashion brands, minimal store presence, content carrying the experience. No legacy to design around. It launched more than two years after we designed it, remarkably like the original.</p>'''),
 (img("../img/amazon/fashion-detail-page.jpg","Rethinking the product detail page for a more content-led, fashion-centric interaction."),
  '''<h2>The detail page, as a lesson</h2>
<p>Four years on the fashion detail page, where every change had to win for all Amazon customers and pass web labs. Glacially incremental, and it taught me how to move a shared platform: negotiate, test, pick the changes that help everyone. Shared tenets later pulled my team, marketing design, and Shopbop design into one fashion experience across Amazon.</p>'''),
 ],("oracle.html","Oracle Health"),("ebay.html","eBay")),"work",1)

pages["work/ebay.html"]=shell("eBay",case("eBay",
'''<ul class="facts">
<li><b>Role</b> Director of Product Design, Seller Experience. 2022 to 2024.</li>
<li><b>Team</b> 25 designers, 2 researchers, 2 design program managers.</li>
<li><b>Work</b> Seller experience end to end, web and mobile, consumer to enterprise, on a marketplace of roughly $73 billion annual GMV and 132 million active buyers. eBay's first generative AI feature.</li>
</ul>''',
 "2022 to 2024","ebay",[
 (video("../img/ebay/magical-listing.mp4","../img/ebay/magical-listing-poster.jpg","The Magical Listing Tool, as launched. eBay's video, sound on.",loop=False),
  '''<h2>eBay's first generative AI feature</h2>
<p>Most listings had no description. Between two similar items, buyers almost always chose the one that did. My team designed and shipped the Magical Listing Tool with eBay's AI team, concept to launch, September 2023. It drafts title, description, and item specifics. The first of a set of tools that take the effort out of listing: a photo, or a video with voice-over, and the rest follows.</p>
<p><span class="stat"><b>30%</b>of daily US app sellers tried it in the first weeks</span> <span class="stat"><b>95%+</b>of those kept the AI draft, with or without edits</span> <span class="stat"><b>80%+</b>CSAT</span></p>
<p class="meta">Figures from <a href="https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/" rel="noopener">eBay's launch post</a>. Named Best Overall Generative AI Solution in the <a href="https://innovation.ebayinc.com/stories/ebays-magical-listing-tool-wins-ai-breakthrough-award-for-best-overall-generative-ai-solution/" rel="noopener">AI Breakthrough Awards</a>.</p>'''),
 (img("../img/ebay/quicklist.jpg","Start with a photo or a barcode, and the listing fills itself in."),
  '''<h2>The future of listing</h2>
<p>Listing was the hardest thing we asked sellers to do, and a decade of fixes produced a dozen different flows. The strategy we set in 2023 reduced it to two questions: What am I selling? and How am I selling it? Get the answer from whatever the seller has, a photo, a title, a number on a box, and fill in the rest.</p>
<p>Three rules carried the design: always listen, simply ask, be invisible. We proved the model in a test harness before anyone built a screen, and ran discovery alongside to validate.</p>'''),
 (img("../img/ebay/sprint-journey.jpg","One step of one persona's journey from the sprint. The seller's words set the target; the concept answers them."),
  '''<h2>The mobile seller sprint</h2>
<p>Small businesses, 6 percent of sellers and 42 percent of revenue, lived on phones, where eBay trailed. I ran one of three Lighthouse sprints with Product, Marketing, and Engineering: three personas, journeys overlaid to find shared territory, concepts that graduate a seller from novice to pro. The vision was one flexible system, because a business grows. The concepts stay internal. The method is the point.</p>
<p>I got design into Product's six-month planning cycle, shaping roadmaps before they were set.</p>'''),
 ],("amazon.html","Amazon"),("earlier.html","Earlier Work")),"work",1)

pages["work/earlier.html"]=shell("Earlier Work",case("Earlier Work",
'''<ul class="facts">
<li><b>Roles</b> Partner and VP of Product Design, THANK YOU Studio, 2012 to 2015. Senior Director of UX Design, Nokia, 2009 to 2012. Creative Director, Adobe, 2006 to 2009.</li>
<li><b>Team</b> Studios in San Francisco and Copenhagen. At Nokia, about 35 people across five cities.</li>
<li><b>Work</b> Kindle Fire launch and Fire Phone design system for Amazon. Toyota in-car navigation. MeeGo OS design system and third-party app guidelines. Adobe.com redesign.</li>
</ul>''',
 "2006 to 2015","earlier",[
 (video("../img/earlier/firephone-reel.mp4","../img/earlier/firephone-reel-poster-2.jpg","At THANK YOU, we conceived a unique design system for Amazon’s Fire Phone. It took advantage of the device’s 3D interface where depth offered real advantages, and used the best of flat design everywhere else, so the 3D moments stood out. Reel, sound on.",loop=False),""),
 (slides([f"../img/earlier/fire-{i}.jpg" for i in range(1,13)],"Three sizes of Kindle Fire HD, one launch site built to show the hardware and the differences between them. Minimal copy let the devices and the Kindle graphics shine, and our rigged and lit 3D scenes let Amazon re-shoot every size for any format. THANK YOU Studio, 2012."),""),
 (img("../img/earlier/toyota.jpg","Design explorations for Toyota's native in-car navigation system. THANK YOU Studio."),""),
 (img("../img/earlier/nokia.jpg","At Nokia, one focus of my team was the creation of 3rd-party app reference designs for the N9 in the debut of the innovative MeeGo OS. (pictured: Associated Press, Qik, AccuWeather, and Facebook)"),""),
 (img("../img/earlier/adobe-cs3.jpg","Creative Suite 3 was a merger of Macromedia and Adobe brands under one roof, so the site underwent a radical transformation to showcase the new look, and provide more content space to celebrate the creative expression of the tools."),""),
 (img("../img/earlier/adobe-cs5.jpg","By CS5, we were pushing beyond the concept of a web page, introducing immersive landing screens with layers, motion and highly interactive UI to allow visitors to play with the tools."),""),
 ],("ebay.html","eBay"),("../leadership.html","Leadership"),herocap="Design explorations for Toyota's native in-car navigation system."),"work",1)

pages["leadership.html"]=shell("How I Lead",'<article class="case wrap">'+row(
 img("img/lead/birthday.jpg","Birthday tradition: everyone dresses as the birthday person.")
 +img("img/lead/ebay-offsite.jpg","Seller experience offsite at eBay.")
 +img("img/lead/fashion-collab-1.jpg","A multi-day collaboration across Amazon Fashion, organized and run by me.")
 +img("img/lead/fashion-collab-2.jpg","Same session: the wall by day three.")
 +img("img/lead/quarterly.jpg","Design Quarterly, volume 11. Amazon Photos."),
 '''<h1>How I Lead</h1><p class="lede">Design is a business capability, and it earns that standing by being legible to the rest of the company.</p>
<h2>Operating habits</h2>
<ul>
<li>A team contract, written down: what I expect from the team and what they can expect from me.</li>
<li>Tenets set with partners at the start, so the hard conversations happen once.</li>
<li>A written definition of done.</li>
<li>Ownership assigned by pattern, so every designer has something that is theirs.</li>
<li>Staying hands-on with the tools, because the toolchain is changing and I want to understand it before I ask the team to.</li>
</ul>
<h2>Building the org</h2>
<p>Amazon Fashion, 5 designers and 2 researchers to 20 total, adding program management, design technology, and managers. Amazon Photos, 8 to 19, adding research, motion, and design technology. eBay, 25 designers with research and design program management. Oracle Health, a platform design team that did not exist before I made the case for it. At Nokia, as a senior director reporting to a VP, I ran about 35 people and managed managers. Across all of it the pattern holds: turn ambiguous direction into a structured, verifiable program, and build the team that can run it without me in the room.</p>
<h2>Design Quarterly</h2>
<p>At Photos the team published a Design Quarterly: our work, our process, new people, wins, open roles. It went to the whole org, to external subscribers, and to Amazon Design. It kept partners aware of what we were doing and it kept the team connected to the larger story their pieces added up to. In the first summer of Covid we put out an issue with no design work in it at all; everyone wrote and designed a spread on what was helping them cope and what gave them hope.</p>''',"head flip")+'</article>',"lead")

pages["about.html"]=shell("About",'<article class="case wrap">'+row('<img class="headshot" src="img/headshot-600.jpg" alt="Kevin Ellis">',
 '''<h1>About</h1>
<p class="lede">Design leader and inventor. Named on nine AI-centric patent applications filed by Oracle.</p>
<p>I grew up in Alaska drawing and painting. I studied graphic design at California College of the Arts in San Francisco, then human-computer interaction and electronic communication design at Emily Carr University in Vancouver. My first digital work was for an agency in Reykjav&iacute;k, then Copenhagen, then back to San Francisco for design leadership roles at Adobe, Yahoo, Nokia, and eventually my own agency with partners in Copenhagen.</p>
<p>The agency built proof-of-concept work that large clients turned into real products. I missed the client side and joined the biggest of them, Amazon, in 2015. Seven years there, then eBay, now Oracle Health, where I built the platform design organization for the clinical products.</p>
<p>I have 15+ years building and running product design and research organizations across marketplace, commerce, and enterprise software. I design for human needs, whether the person is a customer or an employee using the company's own tools. I owned the seller experience end to end at eBay, where my team shipped eBay's first generative AI feature; led consumer product design at Amazon; and now run a platform design org at Oracle Health. I build teams, set the operating model, and ship outcomes with Product and Engineering as equal partners.</p>
<p class="meta">Seattle, WA</p>''',"head about")+'</article>',"about")

pages["contact.html"]=shell("Contact",'<article class="case wrap">'+row('',
 '''<h1>Contact</h1>
<p><a href="mailto:kevinellis@gmail.com">kevinellis@gmail.com</a></p>
<p>(415) 606-1720</p>
<p><a href="https://www.linkedin.com/in/kevinellisdesign" rel="noopener">linkedin.com/in/kevinellisdesign</a></p>''',"head")+'</article>',"contact")

for path,html in pages.items():
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True); open(path,"w").write(html)
print(len(pages),"pages")
