# Isometric line illustrations for the Oracle cases. 600x300 viewBox.
# Language: white tops over pale sides, 1px grey lines, dashed ghosts for what is absent,
# one solid-ink object per drawing, few words. The caption carries the sentence.
from diagrams import _t
CX, CY = 300, 150
C30, S30 = 0.866, 0.5

def P(x, y, z, ox=CX, oy=CY):
    return (round(ox + (x - y) * C30, 1), round(oy + (x + y) * S30 - z, 1))

def _poly(pts, cls):
    return '<path class="%s" d="M%s Z"/>' % (cls, " L".join("%s %s" % p for p in pts))

def box(x, y, z, w, d, h, ink=False, ghost=False, ox=CX, oy=CY):
    p = lambda a, b, c: P(a, b, c, ox, oy)
    top = [p(x, y, z + h), p(x + w, y, z + h), p(x + w, y + d, z + h), p(x, y + d, z + h)]
    right = [p(x + w, y, z), p(x + w, y + d, z), p(x + w, y + d, z + h), p(x + w, y, z + h)]
    left = [p(x, y + d, z), p(x + w, y + d, z), p(x + w, y + d, z + h), p(x, y + d, z + h)]
    if ghost:
        return _poly(left, "ghost") + _poly(right, "ghost") + _poly(top, "ghost")
    return _poly(left, "side") + _poly(right, "side") + _poly(top, "ink" if ink else "top")

def tile(x, y, z, w, d, ink=False, ghost=False, ox=CX, oy=CY):
    return box(x, y, z, w, d, 5, ink, ghost, ox, oy)

def node(x, y, z, ox=CX, oy=CY):
    a, b = P(x, y, z, ox, oy)
    return f'<circle class="node" cx="{a}" cy="{b}" r="3.2"/>'

def dash(pts, ox=CX, oy=CY):
    q = [P(*p, ox, oy) if len(p) == 3 else p for p in pts]
    return '<path class="dash" d="M%s"/>' % " L".join("%s %s" % p for p in q)

def line(pts, ox=CX, oy=CY):
    q = [P(*p, ox, oy) for p in pts]
    return '<path class="ln" d="M%s"/>' % " L".join("%s %s" % p for p in q)

def plate(x, y, w, d, ox=CX, oy=CY):
    return box(x, y, -4, w, d, 4, ox=ox, oy=oy)

def svg(body, label, h=300):
    return f'<svg class="dg iso" viewBox="0 0 600 {h}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def lab(x, y, s, cls="mu sm"):
    return _t(x, y, s, cls)

# ---------------------------------------------------------------- case 1
def consolidate():
    # left: loose one-off tiles at odd heights; right: one stacked worklist, ink cap
    b = ""
    import random
    r = random.Random(7)
    ox, oy = 165, 120
    items = []
    for i in range(4):
        for j in range(4):
            items.append((i * 34, j * 34, r.choice([0, 0, 6, 12])))
    for x, y, z in sorted(items, key=lambda t: t[0] + t[1]):
        b += tile(x, y, z, 24, 24, ghost=(x + y) % 102 == 68, ox=ox, oy=oy)
    b += dash([(262, 150), (326, 150)]) + '<circle class="node" cx="330" cy="150" r="3.2"/>'
    ox2, oy2 = 455, 160
    for k in range(5):
        b += tile(0, 0, k * 9, 80, 80, ink=(k == 4), ox=ox2, oy=oy2)
    b += lab(190, 272, "dozens of one-off lists") + lab(455, 272, "one pattern, every role")
    return svg(b, "Dozens of one-off lists becoming one stacked worklist.")

def landing():
    # six kinds of work drop onto the back of one plate; three role stacks stand at the front
    b = ""
    ox, oy = 300, 150
    b += plate(-130, -60, 290, 130, ox=ox, oy=oy)
    for i in range(6):
        x = -120 + i * 40
        b += dash([(x + 10, -45, 60), (x + 10, -45, 20)], ox=ox, oy=oy) + node(x + 10, -45, 60, ox=ox, oy=oy)
        b += box(x, -55, 0, 20, 20, 16, ox=ox, oy=oy)
    for i, (n, ink, name) in enumerate([(2, False, "physician"), (5, True, "nurse"), (3, False, "front desk")]):
        x = -118 + i * 92
        for k in range(n):
            b += tile(x, 18, k * 8, 60, 40, ink=(ink and k == n - 1), ox=ox, oy=oy)
        b += lab(P(x + 30, 38, 0, ox, oy)[0], 282, name)
    return svg(b, "Kinds of work landing at the back of one plate; three role stacks at the front.")

def investigation():
    # three prongs on a plate; dashed drops meet under it and lead to one ink finding; a ghost cube waits apart
    b = ""
    ox, oy = 270, 110
    b += plate(-130, -30, 260, 60, ox=ox, oy=oy)
    for i in range(3):
        x = -115 + i * 90
        b += box(x, -20, 0, 50, 40, 30, ox=ox, oy=oy)
        b += dash([(x + 25, 30, 0), (x + 25, 30, -40)], ox=ox, oy=oy)
    b += dash([(-90, 30, -40), (90, 30, -40)], ox=ox, oy=oy) + dash([(0, 30, -40), (0, 30, -62)], ox=ox, oy=oy)
    b += node(0, 30, -62, ox=ox, oy=oy)
    b += box(-25, 40, -104, 50, 40, 30, ink=True, ox=ox, oy=oy)
    gx, gy = 190, 20
    b += box(gx, gy, 0, 44, 34, 26, ghost=True, ox=ox, oy=oy)
    b += lab(P(gx + 22, gy + 17, 0, ox, oy)[0], 282, "customers, not yet")
    b += lab(P(0, 60, 0, ox, oy)[0], 282, "one finding")
    return svg(b, "Three prongs converging on one finding; the customer call waits as a ghost.")

def skilltest():
    # one prompt node; left: three different ghost answers; right: three identical tiles, one ink
    b = ""
    b += '<circle class="node" cx="300" cy="34" r="3.2"/>'
    b += dash([(300, 38), (300, 60), (150, 60), (150, 80)]) + dash([(300, 60), (450, 60), (450, 80)])
    ox, oy = 150, 190
    b += box(-50, -40, 0, 70, 50, 18, ghost=True, ox=ox, oy=oy)
    b += box(-10, 10, 0, 40, 70, 30, ghost=True, ox=ox, oy=oy)
    b += box(30, -50, 0, 50, 40, 8, ghost=True, ox=ox, oy=oy)
    ox, oy = 450, 180
    for k in range(3):
        b += tile(-35, -35, k * 22, 70, 70, ink=(k == 2), ox=ox, oy=oy)
    b += lab(150, 276, "without the skill, three answers") + lab(450, 276, "with it, one")
    return svg(b, "One prompt: three different ghost answers without the skill, one repeated answer with it.")

# ---------------------------------------------------------------- case 2
def org():
    # engineering plate, one long ink beam across it (Experience Core), five product-org cubes on top
    b = ""
    ox, oy = 300, 150
    b += plate(-150, -40, 300, 80, ox=ox, oy=oy)
    b += box(-140, 0, 0, 280, 26, 14, ink=True, ox=ox, oy=oy)
    for i in range(5):
        x = -135 + i * 56
        b += box(x, -34, 0, 34, 28, 22 + (8 if i == 2 else 0), ox=ox, oy=oy)
    b += lab(300, 262, "product organizations above, engineering below") + lab(300, 280, "one platform team between them")
    return svg(b, "Five product organizations on top, engineering as the plate, one platform beam between.")

def journey():
    # six stages along one plate; a stretch of two owned by one designer, in ink; a node on each stage
    b = ""
    ox, oy = 300, 150
    b += plate(-170, -22, 340, 44, ox=ox, oy=oy)
    for i in range(6):
        x = -160 + i * 56
        b += box(x, -12, 0, 36, 24, 20, ink=i in (2, 3), ox=ox, oy=oy)
        b += dash([(x + 18, 0, 20), (x + 18, 0, 36)], ox=ox, oy=oy) + node(x + 18, 0, 36, ox=ox, oy=oy)
    b += lab(300, 262, "six stages of the clinician's journey") + lab(300, 280, "one designer owns a stretch")
    return svg(b, "Six stages in a row; one designer's stretch in ink.")

def pipeline():
    # intent node -> skill stack -> prototype slab -> customers; a tight loop back; weeks become days
    b = ""
    ox, oy = 300, 112
    b += node(-180, 0, 0, ox=ox, oy=oy) + dash([(-176, 0, 0), (-112, 0, 0)], ox=ox, oy=oy)
    for k in range(4):
        b += tile(-110, -28, k * 8, 56, 56, ox=ox, oy=oy)
    b += dash([(-52, 0, 16), (6, 0, 16)], ox=ox, oy=oy)
    b += box(8, -28, 0, 64, 56, 34, ink=True, ox=ox, oy=oy)
    b += dash([(74, 0, 17), (124, 0, 17)], ox=ox, oy=oy)
    for j in range(3):
        b += box(130 + j * 22, -24 + j * 12, 0, 14, 14, 12, ox=ox, oy=oy)
    b += dash([(170, 20, 0), (170, 44, 0), (-180, 44, 0), (-180, 4, 0)], ox=ox, oy=oy)
    b += '<rect x="130" y="222" width="340" height="7" rx="3.5" class="bar"/>'
    b += '<rect x="130" y="246" width="78" height="7" rx="3.5" class="inkbar"/>'
    b += _t(118, 226, "weeks", "mu sm", anchor="end") + _t(118, 250, "days", "mu sm", anchor="end")
    b += lab(300, 282, "intent in, prototype out, customers in the loop")
    return svg(b, "Intent, skill stack, prototype, customers, looping; weeks become days.")

def gates():
    # three rising steps with dashed gate uprights and nodes; the last step in ink
    b = ""
    ox, oy = 300, 150
    b += plate(-160, -36, 320, 72, ox=ox, oy=oy)
    for i in range(3):
        x = -150 + i * 100
        b += box(x, -26, 0, 90, 52, 18 + i * 18, ink=(i == 2), ox=ox, oy=oy)
    for i in range(3):
        gx = -60 + i * 100 if i < 2 else 140
        b += dash([(gx, 26, 0), (gx, 26, 90)], ox=ox, oy=oy) + node(gx, 26, 90, ox=ox, oy=oy)
    b += lab(300, 262, "rules, skill check, foundation") + lab(300, 280, "a gate after each")
    return svg(b, "Three rising steps, a gate after each, the last in ink.")

# ---------------------------------------------------------------- case 3
def boundary():
    # one plate, three objects: a cube with a node (a fact), a cube with its ghost twin (a proposal), a stack (work)
    b = ""
    ox, oy = 300, 150
    b += plate(-190, -40, 380, 90, ox=ox, oy=oy)
    b += box(-170, -20, 0, 50, 50, 50, ox=ox, oy=oy)
    b += dash([(-145, 5, 50), (-145, 5, 72)], ox=ox, oy=oy) + node(-145, 5, 72, ox=ox, oy=oy)
    b += box(-30, -20, 0, 50, 50, 50, ox=ox, oy=oy) + box(0, -50, 0, 50, 50, 50, ghost=True, ox=ox, oy=oy)
    for k in range(4):
        b += tile(120, -20, k * 12, 60, 60, ink=(k == 3), ox=ox, oy=oy)
    for x, name in [(-145, "facts"), (-5, "proposals"), (150, "work")]:
        b += lab(P(x, 5, 0, ox, oy)[0], 282, name)
    return svg(b, "Three objects on one plate: a fact, a proposal with its ghost, and a stack of work.")

def ladder():
    # five steps rising from a flat tile to a tall ink block
    b = ""
    ox, oy = 300, 160
    b += plate(-160, -30, 320, 60, ox=ox, oy=oy)
    for i in range(5):
        x = -150 + i * 62
        b += box(x, -20, 0, 50, 40, 6 + i * 22, ink=(i == 4), ox=ox, oy=oy)
    b += lab(96, 270, "ambient") + lab(520, 270, "a person")
    return svg(b, "Five rising steps from ambient to a person.")

def teeup():
    # ghost items arrive along a dashed arc onto a review plate; one ink cube signs; a committed stack follows
    b = ""
    ox, oy = 300, 150
    for i in range(3):
        b += box(-210 + i * 30, -10 + i * 14, 0, 24, 24, 20, ghost=True, ox=ox, oy=oy)
    b += dash([(-160, 10, 24), (-110, 0, 70), (-40, -10, 30)], ox=ox, oy=oy) + node(-110, 0, 70, ox=ox, oy=oy)
    b += plate(-50, -40, 110, 80, ox=ox, oy=oy)
    for i in range(3):
        b += box(-40 + i * 34, -30 + (i % 2) * 30, 0, 24, 24, 20, ox=ox, oy=oy)
    b += box(90, -20, 0, 40, 40, 36, ink=True, ox=ox, oy=oy)
    for k in range(3):
        b += tile(150, -30, k * 10, 50, 50, ox=ox, oy=oy)
    for x, y, name in [(-170, 10, "parsed"), (5, 0, "reviewed, signed once"), (175, -5, "committed in order")]:
        b += lab(P(x, y, 0, ox, oy)[0], 282, name)
    return svg(b, "Ghost items arriving on a review plate, one ink sign-off, then a committed stack.")

def modes():
    # two plates: four cubes joined by solid line (structured), four cubes joined by dashed with nodes (generative)
    b = ""
    for n, (ox, oy, dashed) in enumerate([(160, 150, False), (440, 150, True)]):
        b += plate(-80, -30, 160, 60, ox=ox, oy=oy)
        for i in range(4):
            x = -72 + i * 40
            b += box(x, -16, 0, 26, 32, 18, ink=(dashed and i == 3), ox=ox, oy=oy)
        pts = [(-59 + i * 40, 0, 28) for i in range(4)]
        b += dash(pts, ox=ox, oy=oy) if dashed else line(pts, ox=ox, oy=oy)
        if dashed:
            for p in pts: b += node(*p, ox=ox, oy=oy)
    b += lab(160, 272, "structured: sequence authored ahead") + lab(440, 272, "generative: sequence authored at run time")
    return svg(b, "Two plates: a fixed sequence and a sequence assembled at run time.")
