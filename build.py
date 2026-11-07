import os, time
from diagrams import pipeline, skilltest, roles, consolidate, landing, investigation, org, journey, boundary, ladder, teeup, modes
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
</div><script src="{r}js/gate.js?v={V}"></script><script src="{r}js/slides.js?v={V}"></script><script src="{r}js/video.js?v={V}"></script><script src="{r}js/tiles.js?v={V}"></script></body></html>'''

def img(src, cap=""):
    return f'<figure><img src="{src}" alt="">{"<figcaption>"+cap+"</figcaption>" if cap else ""}</figure>'
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
    if not left: cls=(cls+" textonly").strip()
    return f'<div class="row {cls}"><div class="col-img">{left}</div><div class="col-text">{right}</div></div>\n'

def case(title, lede, year, hero, rows, prev, nxt, herocap=""):
    head=f'<h1>{title}</h1>'+(lede if lede.lstrip().startswith("<") else f'<p class="lede">{lede}</p><p class="year">{year}</p>')
    body='<article class="case wrap">'+row("", head, "head")
    for left,right in rows: body+=row(left,right,"" if right else "gallery")
    body+=f'<div class="next"><a href="{prev[0]}">&larr; {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} &rarr;</a></div></article>\n'
    return body

pages={}
tiles=[("oracle","Oracle Health","oracle"),("amazon","Amazon","amazon"),("ebay","eBay","ebay"),("earlier","Earlier Work","earlier-2")]
pages["index.html"]=shell("Kevin Ellis, Design Leadership",'<div class="wrap"><div class="tiles">'+"".join(
    f'<a class="tile" href="work/{k}.html"><img src="img/tiles/{f}.jpg" alt="{t}"><span>{t}</span></a>' for k,t,f in tiles)+'</div></div>',"work",dark=True)

pages["work/oracle.html"]=shell("Oracle Health",case("Oracle Health",
'''<ul class="facts">
<li><b>Role</b> Director, User Experience Design. 2024 to present.</li>
<li><b>Team</b> Experience Core, the platform design team I formed. Nine designers. One design standard across the product organizations and dozens of clinician-facing applications.</li>
<li><b>Work</b> The core task-management experience for an AI-native EHR. Platform patterns, components, design system, research practice, and the team's AI workflow. Named inventor on eight AI-centric patent applications filed by Oracle.</li>
</ul>
<p>I joined Oracle Health to lead the design of the core task-management experience for an AI-native EHR. It started with ambulatory clinical workflows and grew into taking dozens of one-off legacy experiences and combining them into one universal pattern for every role across the whole product: ambulatory, acute, reimbursement, patient administration.</p>
<p>Out of that work I formed Experience Core, our platform design team. We set one design standard across the product organizations for shared components and interaction patterns, with tight integration into engineering so what we design is what ships. I also built the team's AI workflows with engineering, which took concept-to-testable-prototype from weeks to days. That work produced eight AI patent applications I am a named inventor on.</p>
<p class="caveat">Three cases follow. Most of the work is unreleased and stays inside Oracle, so each is told through method, diagrams, and outcomes: no product screens, no internal names, no customers.</p>''',
 "2024 to present","oracle",[
 # ------------------------------------------------------------ case 1
 (fig(consolidate(),"Dozens of lists, one per team and role, became one pattern configured per role."),
  '''<p class="case-label">Case 1</p><h2 class="part">One worklist for every role</h2>
<h3>The problem</h3>
<p>Clinicians got their work from dozens of places: an inbox for messages, a results queue, orders waiting for a signature, requests from other roles, reminders from the system. Each had been built once, by one team, for one role, and each behaved differently. A physician learned one set of habits, a nurse another, the front desk a third, and the same item could show up in three of them.</p>
<p>The ask was to start with ambulatory clinical workflows. It grew into taking the one-off legacy experiences across the product and combining them into one universal pattern for every role.</p>
<h3>Constraints</h3>
<p>Safety first: anything the system interprets or suggests is teed up for a clinician to review, never committed on its own. Several product organizations, each with its own release train. A legal rule on certain words that shaped the naming. And legacy surfaces that had to keep working while the new pattern replaced them one at a time.</p>'''),
 (fig(landing(),"What lands in the list, and how three roles see it."),
  '''<h3>The approach</h3>
<p>I designed the pattern first as a clinician inbox, and it was elevated to the platform worklist, the Action List. The rule underneath it is simple: work lands in one place, and the list knows what to do with each kind of work. A message is work until it is answered. A result is work until it is acknowledged. An order is work until it is signed. Messaging stopped being a separate application and became a kind of item in the list, answered in place and handed to the right role when the question belongs to someone else.</p>
<p>Roles configure the list; they do not fork it. The physician sees fewer items, weighted to decisions. The nurse sees more, weighted to execution and follow-up. The front desk sees scheduling and paperwork and nothing clinical. One pattern, three experiences, because the configuration knows what each role is there to do.</p>'''),
 (fig(investigation(),"The investigation: three prongs, internal analysis first, one finding."),
  '''<h3>What changed</h3>
<p>The Action List shipped in 2025 and is in customers' hands. When leadership relayed that customers were unhappy with it, with no specifics, I ran an investigation instead of reacting: product feedback gathered and reread, a diff of the design against the released build, usability testing, and a rule that no customer was contacted until the internal analysis was done. The finding was a taxonomy failure in our own feedback data. The same surface had four names across the company, and most of the feedback was filed under other components where nobody could find it. The team got a corrected reference set, and the fixes had evidence behind them.</p>'''),
 (fig(skilltest(),"Same prompt, six runs. Without the skill, three answers. With it, one."),
  '''<h3>My role</h3>
<p>I designed the original pattern, wrote the skill that carries its rules, when it applies, what it holds, how it is configured, and led the investigation. The skill and a three-role demo became the reference example senior engineering leadership pointed to.</p>
<h3>What I would do differently</h3>
<p>Put the released build in front of the design team from the first sprint. The diff analysis found drift between what we designed and what shipped that a live reference build would have caught months earlier.</p>
<p class="demo"><b>Clickthrough demo</b> <span class="pending">link to come</span></p>'''),
 # ------------------------------------------------------------ case 2
 (fig(org(),"One platform team between the product organizations and engineering."),
  '''<p class="case-label">Case 2</p><h2 class="part">Experience Core, and the AI workflow behind it</h2>
<h3>The problem</h3>
<p>Every product organization designed its own version of the same things: lists, panels, notifications, search, page layouts. There was no platform design function, so there was no one standard, and engineering rebuilt the same component in several shapes. The worklist work made the gap obvious: a universal pattern needs a universal owner.</p>
<h3>Constraints</h3>
<p>The team did not exist. I had to make the case for it, staff it, and prove it, while a parallel AI effort ran its own track that leadership had not yet reconciled with ours. Clinician-facing software also carries accessibility and regulatory obligations that a pattern library has to satisfy once, for everyone.</p>'''),
 (fig(journey(),"Thirty-four patterns, six stages, ownership by stretch of journey."),
  '''<h3>Forming the team</h3>
<p>I proposed Experience Core as the platform design team: shared components, interaction patterns, the design system, and the research practice, with one standard across the product organizations and tight integration into engineering so what we design is what ships. We inherited thirty-four patterns and no structure. I grouped them by the clinician's journey, access, triage, interpret, execute, collaborate, follow up, and assigned ownership by pattern, so every designer owned a stretch of journey rather than a pile of components. Alignment went in sequence: eight engineering and product pillar leads first, then SVP peers, then the top.</p>'''),
 (fig(pipeline(),"Intent in, prototype out, customers in the loop. What took weeks takes days."),
  '''<h3>The AI workflow</h3>
<p>With engineering I rebuilt how the team produces. The comp stopped being the deliverable; the rules did. Components get guidelines, reference a person or a model can look up. Layouts and patterns get skills, which carry the judgment of when, when not, and how. A skill selects and configures. It does not code. I wrote the first skills myself, then gave each designer a pattern and its skill. Around that sits a prototyping pipeline, custom tooling, and a shared skill library in the team repo. An intent goes in, a brief, a frame, a data file, and a working prototype comes out.</p>'''),
 (img("../img/oracle/layout-validation.jpg","Three stages, three gates, one definition of done for every layout."),
  '''<h3>What changed</h3>
<p>Concept to testable prototype went from weeks to days, and the team validates more concepts per cycle with customers, because a prototype is now cheap enough to be wrong. One design standard holds across the product organizations and dozens of clinician-facing applications, with WCAG 2.1 AA as a gate rather than a hope. A written definition of done, three gates and a release approval, ended the misalignment that had kept layouts from landing. The work produced eight AI patent applications I am a named inventor on.</p>'''),
 (img("../img/oracle/codex-learning-day.jpg","Learning day. Every designer shipped a working prototype in one session. None of it is product; all of it is the new muscle."),
  '''<h3>My role</h3>
<p>I proposed the team, built it, and lead it. I wrote the first skills and ran the learning day where every designer shipped a working prototype in one session, none of it product, all of it the new muscle.</p>
<h3>What I would do differently</h3>
<p>Write the definition of done before the first layout, not after the first misalignment. The gates were cheap to write and expensive to be without.</p>'''),
 # ------------------------------------------------------------ case 3
 (fig(boundary(),"Three patterns, one boundary."),
  '''<p class="case-label">Case 3</p><h2 class="part">AI-native UX: where the system speaks, and where it stops</h2>
<h3>The problem</h3>
<p>In an AI-native EHR the system has something to say on nearly every screen: a result came back, a guideline applies, a draft is ready, a set of tasks could be bundled. Left to each product team, that becomes a different voice on every surface, and a clinician who cannot tell a fact from a suggestion from a to-do. I led the design for how and when the system surfaces AI output to clinicians across the clinical workflows.</p>
<h3>Constraints</h3>
<p>Nothing the system interprets or suggests commits without a clinician's review. That is a regulatory line as well as a design one. Alarm fatigue is a patient-safety risk, so every interruption has to earn its place. A legal constraint ruled out a word the whole industry uses, which forced better naming. And all of it has to be accessible.</p>'''),
 (fig(ladder(),"The interruption ladder: five rungs, from ambient to a person."),
  '''<h3>Three patterns, one boundary</h3>
<p>I drew the line between three things teams kept blurring. The notification pattern asserts facts: the state of the world changed. Guidance proposes decisions. The worklist holds work. A fact can lead to a proposal, and an accepted proposal becomes work, but each lives in its own pattern with its own rules. I authored the notification pattern for the whole product: one notification object model, a five-class severity taxonomy, and an interruption ladder with five rungs, ambient, passive, active, disruptive, and escalation to a person. The system interrupts only as much as the situation needs, and the rules say which situations need what.</p>'''),
 (fig(teeup(),"Teed up, never auto-added. The system drafts; the clinician decides."),
  '''<h3>Teed up, never auto-added</h3>
<p>For AI output the rule is the same everywhere: the system drafts, the clinician decides. When an agent parses a spoken list of problems, medications, and orders, it tees them up in one review space where the clinician edits, removes, and signs once, and the system commits in the right order underneath, diagnoses before the orders that depend on them. Accept, edit, reject, escalate: those four verbs are the whole interaction, on every AI surface. Clinical leadership validated the direction.</p>
<p>Guided workflows got a point of view too: one pattern with two orchestration modes, structured and generative. The difference is who authors the sequence and when, not whether the screen adapts.</p>'''),
 (fig(modes(),"Guided workflow: one pattern, two modes."),
  '''<h3>What changed</h3>
<p>The patterns gave product teams anchors to build on instead of inventing their own, and gave engineering one set of behaviors to implement. The thinking here underlies several of the eight AI patent applications I am named on. The filings are confidential, so this page describes the reasoning, not the claims.</p>
<h3>My role</h3>
<p>Program owner for the notification pattern and its specification. Author of the guided-workflow point of view. Design lead for AI output across the clinical workflows, with the multi-add direction validated by clinical leadership.</p>
<h3>What I would do differently</h3>
<p>Name the modes earlier. "AI mode" lived as a label for too long before it was renamed for what it does, and every week it survived, teams designed to the label.</p>'''),
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
 (img("../img/ebay/sprint-journey.jpg","One step of one persona's journey from the sprint. The seller's words set the target; the concept answers them."),
  '''<h2>The mobile seller sprint</h2>
<p>Small businesses, 6 percent of sellers and 42 percent of revenue, lived on phones, where eBay trailed. I ran one of three Lighthouse sprints with Product, Marketing, and Engineering: three personas, journeys overlaid to find shared territory, concepts that graduate a seller from novice to pro. The vision was one flexible system, because a business grows. The concepts stay internal. The method is the point.</p>
<p>I got design into Product's six-month planning cycle, shaping roadmaps before they were set.</p>'''),
 ],("amazon.html","Amazon"),("earlier.html","Earlier Work")),"work",1)

pages["work/earlier.html"]=shell("Earlier Work",case("Earlier Work",
'''<ul class="facts">
<li><b>Role</b> Partner and VP of Product Design, THANK YOU Studio, 2012 to 2015. Senior Director of UX Design, Nokia, 2009 to 2012. Creative Director, Adobe, 2006 to 2009.</li>
<li><b>Team</b> Studios in San Francisco and Copenhagen. At Nokia, about 35 people across five cities.</li>
<li><b>Work</b> Kindle Fire launch and Fire Phone design system for Amazon. Toyota in-car navigation. MeeGo OS design system and third-party app guidelines. Adobe.com redesign.</li>
</ul>''',
 "2006 to 2015","earlier",[
 (video("../img/earlier/firephone-reel.mp4","../img/earlier/firephone-reel-poster-2.jpg","Fire Phone for Amazon. THANK YOU Studio reel, sound on.",loop=False),""),
 (slides([f"../img/earlier/fire-{i}.jpg" for i in range(1,13)],"Kindle Fire HD launch site for Amazon. THANK YOU Studio, 2012."),""),
 (img("../img/earlier/toyota.jpg","Design exploration of Toyota's native in-car navigation system. THANK YOU Studio."),""),
 (img("../img/earlier/nokia.jpg","My team owned comms apps for the Symbian OS, as well as the 3rd-party app reference designs for the N9 and the debut of the innovative MeeGo OS."),""),
 ],("ebay.html","eBay"),("../leadership.html","Leadership"),herocap="Design exploration of Toyota's native in-car navigation system."),"work",1)

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
<p class="lede">Design leader and inventor. Named on eight AI-centric patent applications filed by Oracle.</p>
<p>I grew up in Alaska drawing and painting. I studied graphic design at California College of the Arts in San Francisco, then human-computer interaction and electronic communication design at Emily Carr University in Vancouver. My first digital work was for an agency in Reykjav&iacute;k, then Copenhagen, then back to San Francisco for design leadership roles at Adobe, Yahoo, Nokia, and eventually my own agency with partners in Copenhagen.</p>
<p>The agency built proof-of-concept work that large clients turned into real products. I missed the client side and joined the biggest of them, Amazon, in 2015. Seven years there, then eBay, now Oracle Health, where I built the platform design organization for the clinical products.</p>
<p>I have 15+ years building and running product design and research organizations across marketplace, commerce, and enterprise software. I design for human needs, whether the person is a customer or an employee using the company's own tools. I owned the seller experience end to end at eBay, where my team shipped eBay's first generative AI feature; led consumer product design at Amazon; and now run a platform design org at Oracle Health. I build teams, set the operating model, and ship measurable outcomes with Product and Engineering as equal partners.</p>
<p class="meta">Seattle, WA</p>''',"head about")+'</article>',"about")

pages["contact.html"]=shell("Contact",'<article class="case wrap">'+row('',
 '''<h1>Contact</h1>
<p><a href="mailto:kevinellis@gmail.com">kevinellis@gmail.com</a></p>
<p>(415) 606-1720</p>
<p><a href="https://www.linkedin.com/in/kevinellisdesign" rel="noopener">linkedin.com/in/kevinellisdesign</a></p>''',"head")+'</article>',"contact")

for path,html in pages.items():
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True); open(path,"w").write(html)
print(len(pages),"pages")
