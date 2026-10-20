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
