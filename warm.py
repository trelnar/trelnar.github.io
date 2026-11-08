# Warm, hand-set illustrations in the spirit of the Action List drawing: pastel, rounded, no words.
Y="#e6d78a"; G="#9fb79a"; P="#8a6fa8"; B="#7f9aa6"; O="#b26f4a"; PALE="#e9ead9"; PALE2="#d6d7c6"; CREAM="#f6f1dc"

def listing():
    s=[]
    a=s.append
    a('<svg class="dg warm" viewBox="0 0 800 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Seller inputs flowing into a listing that fills itself in" style="width:100%;height:auto;display:block">')
    # flowing lines from inputs to the card (drawn first, under everything)
    a(f'<path d="M225 150 C 330 150, 360 180, 470 180" fill="none" stroke="{Y}" stroke-width="7" stroke-linecap="round" opacity=".9"/>')
    a(f'<path d="M300 236 C 370 236, 390 190, 470 186" fill="none" stroke="{P}" stroke-width="7" stroke-linecap="round" opacity=".85"/>')
    a(f'<path d="M165 300 C 300 300, 380 210, 470 192" fill="none" stroke="{B}" stroke-width="7" stroke-linecap="round" opacity=".85"/>')
    # photo tile, tilted
    a(f'<g transform="rotate(-7 135 140)"><rect x="60" y="65" width="150" height="150" rx="18" fill="{Y}"/>'
      f'<rect x="78" y="83" width="114" height="92" rx="10" fill="{CREAM}"/>'
      f'<circle cx="160" cy="110" r="14" fill="{O}" opacity=".9"/>'
      f'<path d="M78 175 L 112 132 L 134 156 L 150 142 L 192 175 Z" fill="{G}"/></g>')
    # title pill, tilted the other way
    a(f'<g transform="rotate(4 210 236)"><rect x="110" y="216" width="200" height="40" rx="20" fill="{P}"/>'
      f'<rect x="128" y="231" width="110" height="10" rx="5" fill="{CREAM}" opacity=".9"/>'
      f'<rect x="246" y="231" width="40" height="10" rx="5" fill="{CREAM}" opacity=".6"/></g>')
    # barcode tile
    a(f'<g transform="rotate(-3 105 300)"><rect x="50" y="268" width="112" height="64" rx="12" fill="{B}"/>')
    x=64
    for w in (4,7,3,6,4,8,3,5,7,4):
        a(f'<rect x="{x}" y="282" width="{w}" height="36" rx="1.5" fill="{CREAM}" opacity=".9"/>'); x+=w+5
    a('</g>')
    # the listing card
    a(f'<rect x="478" y="28" width="300" height="304" rx="22" fill="{PALE}"/>')
    a(f'<rect x="504" y="54" width="70" height="70" rx="14" fill="{Y}"/>')
    a(f'<path d="M512 118 L 532 96 L 546 110 L 556 101 L 568 118 Z" fill="{G}"/><circle cx="556" cy="72" r="7" fill="{O}" opacity=".9"/>')
    a(f'<rect x="590" y="62" width="162" height="16" rx="8" fill="{P}"/>')
    a(f'<rect x="590" y="88" width="112" height="12" rx="6" fill="{P}" opacity=".45"/>')
    rows=[(G,.5,228),(B,.5,228),(O,.5,228),(P,0,120),(Y,0,228)]
    y=152
    for i,(c,op,w) in enumerate(rows):
        a(f'<circle cx="516" cy="{y+9}" r="10" fill="{c}"/>')
        a(f'<rect x="536" y="{y}" width="{w}" height="18" rx="9" fill="{PALE2}"/>')
        if op: a(f'<rect x="536" y="{y}" width="{w}" height="18" rx="9" fill="{c}" opacity="{op}"/>')
        if i==3:
            a(f'<g><path d="M672 {y-6} h 56 a12 12 0 0 1 12 12 v 8 a12 12 0 0 1 -12 12 h -36 l -12 11 v -11 h -8 a12 12 0 0 1 -12 -12 v -8 a12 12 0 0 1 12 -12 z" fill="{P}"/>'
              f'<text x="700" y="{y+18}" font-family="-apple-system,Helvetica,Arial,sans-serif" font-size="20" font-weight="700" fill="{CREAM}" text-anchor="middle">?</text></g>')
        y+=36
    a('</svg>')
    return "".join(s)
