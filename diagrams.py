# Inline SVG diagrams for the Oracle page. Abstract by design: no product UI,
# no internal names. They inherit site type and color via css/site.css (.dg).

def _svg(vb, body, cls="dg", label=""):
    return f'<svg class="{cls}" viewBox="0 0 {vb[0]} {vb[1]}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def _marker(i):
    return (f'<defs><marker id="ar{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10z" class="arf"/></marker></defs>')

def _box(x, y, w, h, title, sub="", cls="bx", r=6):
    t = f'<text x="{x+w/2}" y="{y+h/2+(0 if not sub else -6)}" text-anchor="middle" class="b" dominant-baseline="middle">{title}</text>'
    s = f'<text x="{x+w/2}" y="{y+h/2+15}" text-anchor="middle" class="mu sm" dominant-baseline="middle">{sub}</text>' if sub else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" class="{cls}"/>{t}{s}'

# ---------------------------------------------------------------- A. pipeline
def pipeline():
    b = _marker(1)
    boxes = [("Intent", "brief, frame, data"), ("Skill library", "guidelines, skills"),
             ("Prototype", "working, testable"), ("Customers", "validate, iterate")]
    xs = [6, 154, 302, 450]; y, w, h = 44, 132, 70
    # tooling group behind boxes 2 and 3
    b += f'<rect x="146" y="30" width="296" height="98" rx="10" class="grp"/>'
    b += f'<text x="294" y="20" text-anchor="middle" class="mu sm">custom tooling, in the team repo</text>'
    for (t, s), x in zip(boxes, xs):
        b += _box(x, y, w, h, t, s)
    for x in xs[:-1]:
        b += f'<path d="M{x+w+1} {y+h/2}H{x+w+20}" class="ln" marker-end="url(#ar1)"/>'
    # loop back
    b += f'<path d="M516 {y+h} V156 H72 V{y+h+2}" class="ln dash" marker-end="url(#ar1)"/>'
    b += f'<text x="294" y="170" text-anchor="middle" class="mu sm">next cycle</text>'
    # before / after
    b += '<text x="20" y="238" class="mu sm">Before</text>'
    b += '<rect x="90" y="226" width="410" height="14" rx="3" class="bar"/>'
    b += '<text x="510" y="238" class="b" dominant-baseline="middle">weeks</text>'
    for lab, x in [("comp", 90), ("review", 172), ("handoff", 254), ("build", 336), ("test", 418)]:
        b += f'<path d="M{x} 226v14" class="tick"/><text x="{x+6}" y="258" class="mu sm">{lab}</text>'
    b += '<text x="20" y="318" class="mu sm">After</text>'
    b += '<rect x="90" y="306" width="96" height="14" rx="3" class="acf"/>'
    b += '<text x="196" y="318" class="b" dominant-baseline="middle">days</text>'
    for lab, x in [("intent", 90), ("prototype", 122), ("test", 162)]:
        b += f'<path d="M{x} 306v14" class="tick"/>'
    b += '<text x="96" y="342" class="mu sm">intent, prototype, test</text>'
    return _svg((600, 356), b, label="The prototyping pipeline: intent in, prototype out, customers in the loop. Weeks became days.")

# ------------------------------------------------------------ B. skill test
def _card(x, y, kind, cls="wire"):
    """Abstract 120x70 wireframe. kind: 'a','b','c' differ; 's' is the skilled layout."""
    w, h = 120, 70
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" class="{cls}"/>'
    L = lambda x1, y1, x2, y2: f'<path d="M{x1} {y1}H{x2}" class="{cls}"/>' if y1 == y2 else f'<path d="M{x1} {y1}V{y2}" class="{cls}"/>'
    R = lambda rx, ry, rw, rh, c=cls: f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" class="{c}"/>'
    if kind == "a":   # list left, detail right
        o += L(x+40, y, x+40, y+h)
        for i in range(4): o += L(x+8, y+12+i*14, x+32, y+12+i*14)
        o += R(x+48, y+10, 64, 50)
    elif kind == "b": # top tabs, 2x2 grid
        o += L(x, y+16, x+w, y+16)
        for i in range(3): o += L(x+8+i*26, y+8, x+26+i*26, y+8)
        for r in range(2):
            for c in range(2): o += R(x+10+c*52, y+24+r*22, 48, 16)
    elif kind == "c": # single column of rows
        for i in range(5): o += L(x+10, y+10+i*13, x+110, y+10+i*13)
    else:             # 's': header, filter row, rows with checkbox, right rail
        o += L(x, y+14, x+w, y+14)
        o += L(x+6, y+7, x+40, y+7)
        o += L(x+6, y+22, x+70, y+22)
        for i in range(4):
            yy = y+32+i*10
            o += R(x+8, yy-3, 6, 6, "wire") + L(x+18, yy, x+78, yy)
        o += L(x+88, y+14, x+88, y+h)
        o += L(x+94, y+26, x+112, y+26) + L(x+94, y+36, x+112, y+36)
    return o

def skilltest():
    b = _marker(2)
    b += _box(240, 14, 120, 40, "One prompt")
    b += '<path d="M300 54V72H150V96" class="ln" marker-end="url(#ar2)"/><path d="M300 72H450V96" class="ln" marker-end="url(#ar2)"/>'
    b += '<text x="150" y="116" text-anchor="middle" class="b">Without the skill</text>'
    b += '<text x="450" y="116" text-anchor="middle" class="b">With the skill</text>'
    for i, k in enumerate("abc"):
        b += _card(90, 134+i*84, k)
        b += _card(390, 134+i*84, "s", "wire ac")
    b += '<text x="150" y="400" text-anchor="middle" class="mu sm">three layouts, three behaviors</text>'
    b += '<text x="450" y="400" text-anchor="middle" class="mu sm">three matches, and they match</text>'
    b += '<text x="450" y="418" text-anchor="middle" class="mu sm">the shipped design</text>'
    return _svg((600, 436), b, label="Three agents given the same prompt without the skill produced three different layouts; with the skill, three matching prototypes that match the shipped design.")

# -------------------------------------------------------------- C. roles
def roles():
    b = _marker(3)
    b += _box(180, 14, 240, 58, "One patient panel")
    for i in range(10):
        b += f'<circle cx="{215+i*19}" cy="60" r="4" class="dot"/>'
    b += '<path d="M300 72V92" class="ln" marker-end="url(#ar3)"/>'
    b += _box(205, 100, 190, 36, "one pattern, one skill", cls="bx ac")
    b += '<path d="M300 136V150H110V166" class="ln" marker-end="url(#ar3)"/><path d="M300 150V166" class="ln" marker-end="url(#ar3)"/><path d="M300 150H490V166" class="ln" marker-end="url(#ar3)"/>'
    cols = [(110, "Physician", 3, "dec", ["fewer tasks,", "weighted to decisions"]),
            (300, "Nurse", 6, "exe", ["more tasks, weighted", "to execution and follow-up"]),
            (490, "Front desk", 4, "adm", ["scheduling and paperwork,", "nothing clinical"])]
    for cx, name, n, kind, sub in cols:
        b += f'<text x="{cx}" y="188" text-anchor="middle" class="b">{name}</text>'
        x = cx-75
        for i in range(n):
            y = 200+i*22
            b += f'<rect x="{x}" y="{y}" width="150" height="16" rx="3" class="rowbx"/>'
            if kind == "dec":
                b += f'<rect x="{x+6}" y="{y+4}" width="8" height="8" class="acf"/><path d="M{x+22} {y+8}H{x+100}" class="wire"/>'
            elif kind == "exe":
                b += f'<rect x="{x+6}" y="{y+4}" width="8" height="8" class="wire"/><path d="M{x+22} {y+8}H{x+80}" class="wire"/><path d="M{x+120} {y+8}H{x+140}" class="wire"/>'
            else:
                b += f'<rect x="{x+6}" y="{y+3}" width="10" height="10" rx="1" class="wire"/><path d="M{x+6} {y+6}H{x+16}" class="wire"/><path d="M{x+22} {y+8}H{x+90}" class="wire"/>'
        b += f'<text x="{cx}" y="352" text-anchor="middle" class="mu sm">{sub[0]}</text><text x="{cx}" y="369" text-anchor="middle" class="mu sm">{sub[1]}</text>'
    return _svg((600, 386), b, label="The same patient panel seen by a physician, a nurse, and front desk staff: one pattern and one skill produce three different worklists.")

# ====================================================================== 11/6
def _t(x, y, s, cls="", anchor="middle", base="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" dominant-baseline="{base}" class="{cls}">{s}</text>'
def _arrow(d, i, cls="ln"):
    return f'<path d="{d}" class="{cls}" marker-end="url(#ar{i})"/>'

# D1. dozens of one-off lists -> one pattern, every role
def consolidate():
    import random
    b = _marker(11); rnd = random.Random(7)
    roles = ["physician", "nurse", "front desk", "billing"]
    for r, role in enumerate(roles):
        y = 28 + r * 64
        for c in range(4 + (r % 2)):
            x = 14 + c * 52 + (6 if r % 2 else 0); h = 36 + rnd.choice([0, 6, -6]); w = 46
            b += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" class="wire"/>'
            for i in range(3): b += f'<path d="M{x+6} {y+9+i*9}H{x+w-6-rnd.choice([0,8,16])}" class="wire"/>'
        b += _t(14, y + 52, role, "mu sm", anchor="start")
    b += _t(150, 302, "dozens of one-off lists,", "mu sm") + _t(150, 320, "one per team and role", "mu sm")
    b += _arrow("M292 160H326", 11)
    x, y, w, h = 334, 28, 256, 252
    b += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="bx"/>'
    b += _t(x + 14, y + 20, "Worklist", "b sm", anchor="start") + _t(x + w - 14, y + 20, "every role", "mu sm", anchor="end")
    b += f'<path d="M{x} {y+38}H{x+w}" class="wire"/>'
    for i in range(8):
        yy = y + 58 + i * 24
        b += f'<rect x="{x+14}" y="{yy-5}" width="10" height="10" rx="2" class="wire"/>'
        b += f'<path d="M{x+32} {yy}H{x+w-74-(i%3)*20}" class="wire"/><path d="M{x+w-52} {yy}H{x+w-14}" class="wire"/>'
    b += _t(462, 302, "one pattern,", "mu sm") + _t(462, 320, "configured per role", "mu sm")
    b += _t(300, 350, "ambulatory, acute, reimbursement, patient administration", "sm")
    return _svg((600, 366), b, label="Dozens of one-off worklists, one per team and role, consolidated into one pattern configured for every role across ambulatory, acute, reimbursement, and patient administration.")

# D2. what lands in the list, and three role views
def landing():
    b = _marker(12)
    for i, s_ in enumerate(["messages", "results", "orders", "requests", "reminders", "AI drafts"]):
        x = 8 + i * 98
        b += f'<rect x="{x}" y="14" width="90" height="34" rx="5" class="bx"/>' + _t(x + 45, 31, s_, "sm") + _arrow(f"M{x+45} 48V66", 12)
    b += f'<rect x="150" y="68" width="300" height="40" rx="6" class="bx ac"/>' + _t(300, 88, "one worklist, one set of rules", "b")
    b += _t(300, 124, "work until answered, acknowledged, or signed", "mu sm")
    b += _arrow("M300 108V134H110V150", 12) + _arrow("M300 134V150", 12) + _arrow("M300 134H490V150", 12)
    cols = [(110, "Physician", 3, "dec", ["fewer items,", "weighted to decisions"]), (300, "Nurse", 6, "exe", ["more items,", "execution and follow-up"]), (490, "Front desk", 4, "adm", ["scheduling and", "paperwork, nothing clinical"])]
    for cx, name, n, kind, sub in cols:
        b += _t(cx, 168, name, "b"); x = cx - 75
        for i in range(n):
            y = 182 + i * 20
            b += f'<rect x="{x}" y="{y}" width="150" height="14" rx="3" class="rowbx"/>'
            if kind == "dec": b += f'<rect x="{x+6}" y="{y+3}" width="8" height="8" class="acf"/><path d="M{x+22} {y+7}H{x+100}" class="wire"/>'
            elif kind == "exe": b += f'<rect x="{x+6}" y="{y+3}" width="8" height="8" class="wire"/><path d="M{x+22} {y+7}H{x+80}" class="wire"/><path d="M{x+120} {y+7}H{x+140}" class="wire"/>'
            else: b += f'<rect x="{x+6}" y="{y+2}" width="10" height="10" rx="1" class="wire"/><path d="M{x+6} {y+5}H{x+16}" class="wire"/><path d="M{x+22} {y+7}H{x+90}" class="wire"/>'
        b += _t(cx, 318, sub[0], "mu sm") + _t(cx, 336, sub[1], "mu sm")
    return _svg((600, 352), b, label="Messages, results, orders, requests, reminders, and AI drafts land in one worklist with one set of rules, shown three ways for physician, nurse, and front desk.")

# D3. the investigation
def investigation():
    b = _marker(13)
    b += f'<rect x="170" y="12" width="260" height="36" rx="5" class="bx"/>' + _t(300, 30, "“Customers aren’t happy with it”", "sm")
    b += _t(300, 60, "no specifics", "mu sm")
    for i, (t, s_) in enumerate([("Product feedback", "gathered and reread"), ("Design vs. build", "diff against the release"), ("Usability testing", "with clinicians")]):
        x = 20 + i * 190
        b += _arrow(f"M300 48V70H{x+90}V82", 13) if i != 1 else _arrow("M300 48V82", 13)
        b += f'<rect x="{x}" y="84" width="180" height="50" rx="5" class="bx"/>' + _t(x + 90, 101, t, "b sm") + _t(x + 90, 121, s_, "mu sm")
        b += _arrow(f"M{x+90} 134V156", 13)
    b += f'<rect x="20" y="158" width="560" height="30" rx="5" class="grp"/>' + _t(300, 173, "internal analysis first; no customer contacted until it was done", "mu sm")
    b += _arrow("M300 188V206", 13)
    b += f'<rect x="60" y="208" width="480" height="60" rx="6" class="bx ac"/>'
    b += _t(300, 228, "Finding: a taxonomy failure in our own data", "b sm") + _t(300, 250, "one surface, four names; feedback filed where nobody looked", "mu sm")
    b += _arrow("M300 268V286", 13)
    b += _t(300, 300, "a corrected reference set, and fixes with evidence behind them", "sm")
    return _svg((600, 318), b, label="A three-pronged investigation, internal analysis before any customer contact, found that the surface had four names and its feedback was filed where nobody looked.")

# D5. Experience Core in the org
def org():
    b = _marker(15)
    for i, o in enumerate(["Ambulatory", "Acute", "Reimbursement", "Patient admin", "..."]):
        x = 6 + i * 118
        b += f'<rect x="{x}" y="14" width="112" height="40" rx="5" class="bx"/>' + _t(x + 56, 34, o, "sm") + _arrow(f"M{x+56} 110V56", 15)
    b += _t(300, 76, "product organizations, dozens of clinician-facing applications", "mu sm")
    b += f'<rect x="70" y="112" width="460" height="70" rx="6" class="bx ac"/>' + _t(300, 136, "Experience Core", "b") + _t(300, 160, "patterns, components, design system, research: one standard", "mu sm")
    b += f'<rect x="70" y="206" width="460" height="40" rx="6" class="bx"/>' + _t(300, 226, "Engineering: what we design is what ships", "sm")
    b += f'<path d="M300 182V206" class="ln"/><path d="M292 194H308" class="ln"/>'
    b += _t(300, 272, "the team did not exist until I made the case for it", "mu sm")
    return _svg((600, 288), b, label="Experience Core sits between the product organizations and engineering, setting one standard for patterns, components, the design system, and research.")

# D6. the journey and ownership
def journey():
    b = ""
    for i, s_ in enumerate(["access", "triage", "interpret", "execute", "collaborate", "follow up"]):
        x = 8 + i * 97
        b += f'<path d="M{x} 20H{x+82}L{x+96} 44L{x+82} 68H{x}L{x+14} 44Z" class="bx{" ac" if i==2 else ""}"/>' + _t(x + 48, 44, s_, "sm b" if i == 2 else "sm")
    b += _t(300, 92, "thirty-four patterns, grouped by where they sit in the clinician’s journey", "mu sm")
    b += f'<path d="M250 108V124" class="ln ac"/>'
    b += f'<rect x="150" y="126" width="200" height="34" rx="5" class="bx ac"/>' + _t(250, 143, "one designer, one stretch", "sm")
    b += _t(300, 184, "ownership by pattern, not by component pile", "mu sm")
    return _svg((600, 200), b, label="Six journey stages, access through follow up; thirty-four patterns grouped by stage; each designer owns a stretch of the journey.")

# D7. three patterns, one boundary
def boundary():
    b = _marker(17)
    for i, (t, s_, q) in enumerate([("Notifications", "assert facts", "the world changed"), ("Guidance", "proposes decisions", "what you could do"), ("The worklist", "holds work", "what you have to do")]):
        x = 10 + i * 196
        b += f'<rect x="{x}" y="16" width="184" height="86" rx="6" class="bx{" ac" if i==2 else ""}"/>' + _t(x + 92, 40, t, "b") + _t(x + 92, 62, s_, "sm") + _t(x + 92, 84, q, "mu sm")
    b += _arrow("M194 59H206", 17) + _arrow("M390 59H402", 17)
    b += _t(200, 126, "may lead to a proposal", "mu sm") + _t(400, 126, "accepted, becomes work", "mu sm")
    b += _t(300, 160, "each lives in its own pattern, with its own rules", "sm")
    return _svg((600, 176), b, label="Three patterns with one boundary: notifications assert facts, guidance proposes decisions, the worklist holds work.")

# D8. the interruption ladder
def ladder():
    b = ""
    for i, (t, s_) in enumerate([("Ambient", "visible when you look"), ("Passive", "noted, no interruption"), ("Active", "asks for a glance"), ("Disruptive", "stops the task"), ("Escalation", "reaches a person")]):
        y = 196 - i * 42; w = 260 + i * 50; x = 40
        b += f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="4" class="{"bx ac" if i>=3 else "bx"}"/>'
        b += _t(x + 12, y + 17, t, "b sm", anchor="start") + _t(x + w - 12, y + 17, s_, "mu sm", anchor="end")
    b += f'<path d="M560 230V30" class="ln dash"/><path d="M555 36L560 28L565 36" class="ln"/>' + _t(590, 246, "more interruption", "mu sm", anchor="end")
    b += _t(300, 270, "interrupt only as much as the situation needs", "mu sm")
    return _svg((600, 286), b, label="A five-rung interruption ladder from ambient to escalation to a person. The system interrupts only as much as the situation needs.")

# D9. teed up, never auto-added
def teeup():
    b = _marker(19)
    steps = [("Spoken list", "problems,", "meds, orders"), ("Parsed", "by an agent,", "teed up"), ("Reviewed", "edit, remove,", "confirm"), ("Signed once", "the clinician", "decides"), ("Committed", "diagnoses,", "then orders")]
    for i, (t, s1, s2) in enumerate(steps):
        x = 6 + i * 119
        b += f'<rect x="{x}" y="24" width="110" height="74" rx="6" class="bx{" ac" if i==3 else ""}"/>' + _t(x + 55, 44, t, "b sm") + _t(x + 55, 64, s1, "mu sm") + _t(x + 55, 82, s2, "mu sm")
        if i < 4: b += _arrow(f"M{x+111} 61H{x+118}", 19)
    b += f'<rect x="6" y="116" width="588" height="30" rx="5" class="grp"/>' + _t(300, 131, "nothing commits without a clinician; the system drafts, the clinician decides", "mu sm")
    b += _t(300, 172, "accept, edit, reject, escalate: the four verbs on every AI surface", "sm")
    return _svg((600, 190), b, label="AI output is teed up for review, never auto-added: a spoken list is parsed, reviewed in one place, signed once, and committed in order.")

# D10. guided workflow, two orchestration modes
def modes():
    b = _marker(20)
    for i, (t, s_, q) in enumerate([("Structured", "sequence authored ahead of time", "by the protocol owner"), ("Generative", "sequence authored at run time", "by the system, from context")]):
        x = 20 + i * 300
        b += f'<rect x="{x}" y="16" width="260" height="74" rx="6" class="bx"/>' + _t(x + 130, 38, t, "b") + _t(x + 130, 58, s_, "sm") + _t(x + 130, 76, q, "mu sm")
        for j in range(4):
            sx = x + 40 + j * 56
            b += f'<rect x="{sx}" y="100" width="40" height="18" rx="3" class="{"wire" if i==0 else "wire ac"}"/>'
            if j < 3: b += _arrow(f"M{sx+41} 109H{sx+54}", 20, "ln" if i == 0 else "ln dash")
    b += _t(300, 146, "one pattern, two modes", "b sm")
    b += _t(300, 166, "the discriminator is who authors the sequence and when,", "mu sm") + _t(300, 184, "not whether the screen adapts", "mu sm")
    return _svg((600, 200), b, label="Guided workflow as one pattern with two orchestration modes, structured and generative; the difference is who authors the sequence and when.")
