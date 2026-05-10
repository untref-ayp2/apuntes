"""
Fix MapaDeMemoria SVG layout:
1. Move "Stack" title up (y=19.5 -> y=10)
2. Move "Segmento de Datos" title (y=249.5 -> y=238)
3. Reorganize heap into 3 clean rows
4. Rewrite arrow paths to eliminate crossings
"""

import os, re

BASE = "/home/martin/AyP2/apuntes/contenidos/_static/figures"

# =====================================================
# Transformations for ALL heap boxes (rect coordinates)
# =====================================================
# Format: (old_x, old_y, old_w, old_h) -> (new_x, new_y)
# Only the first two numbers (x,y) change; width/height stay same.

HEAP_RECT_MOVES = [
    # --- Row 1 (y=30): Persona(p2) + Direccion(empty) + Direccion(Av.Corrientes) ---
    # Persona(p2) box
    ('x="380" y="50" width="220" height="60"', 'x="300" y="30" width="220" height="60"'),
    # Persona(p2) label
    ('x="300" y="50" width="80" height="20"', 'x="220" y="30" width="80" height="20"'),
    
    # Direccion(empty, red) box
    ('x="760" y="30" width="200" height="60"', 'x="700" y="30" width="200" height="60"'),
    # Direccion(empty, red) label
    ('x="680" y="30" width="80" height="20"', 'x="620" y="30" width="80" height="20"'),

    # Direccion(Av.Corrientes) box
    ('x="510" y="190" width="280" height="60"', 'x="930" y="30" width="280" height="60"'),
    # Direccion(Av.Corrientes) label
    ('x="430" y="190" width="80" height="20"', 'x="850" y="30" width="80" height="20"'),

    # --- Row 2 (y=140): Persona(p3) + Direccion(p3) ---
    # Persona(p3) box
    ('x="360" y="110" width="220" height="60"', 'x="300" y="140" width="220" height="60"'),
    # Persona(p3) label
    ('x="280" y="110" width="80" height="20"', 'x="220" y="140" width="80" height="20"'),
    
    # Direccion(p3) box [Valentín Gomez]
    ('x="700" y="90" width="280" height="60"', 'x="580" y="140" width="280" height="60"'),
    # Direccion(p3) label
    ('x="620" y="90" width="80" height="20"', 'x="500" y="140" width="80" height="20"'),

    # --- Row 3 (y=280): Persona(p1) + Direccion(p1) ---
    # Persona(p1) box
    ('x="340" y="290" width="200" height="60"', 'x="300" y="280" width="200" height="60"'),
    # Persona(p1) label
    ('x="260" y="290" width="80" height="20"', 'x="220" y="280" width="80" height="20"'),
    
    # Direccion(p1) empty box
    ('x="700" y="270" width="200" height="60"', 'x="560" y="280" width="200" height="60"'),
    # Direccion(p1) label
    ('x="620" y="270" width="80" height="20"', 'x="480" y="280" width="80" height="20"'),
]

# =====================================================
# Text coordinate transformations
# =====================================================
# For each heap text element, map old string -> new string
# Based on UNIQUE text content identification

NBSP = '\xa0'

TEXT_MOVES = [
    # === Row 1: Persona(p2): old (380,50) -> new (300,30) => dx=-80, dy=-20 ===
    ('x="384.5" y="63">nombre string = "Pepe"', 'x="304.5" y="43">nombre string = "Pepe"'),
    ('x="384.5" y="77">apellido string = "Martinez"', 'x="304.5" y="57">apellido string = "Martinez"'),
    ('x="384.5" y="51">edad uint = 23', 'x="304.5" y="31">edad uint = 23'),
    ('x="384.5" y="185.5">direccion Direccion = *', 'x="304.5" y="165.5">direccion Direccion = *'),
    ('x="374.5" y="64">Persona', 'x="294.5" y="44">Persona'),

    # === Row 1: Direccion(empty, red): old (760,30) -> new (700,30) => dx=-60, dy=0 ===
    (f'x="764.5" y="43">calle{NBSP}string = ""', f'x="704.5" y="43">calle{NBSP}string = ""'),
    (f'x="764.5" y="57">direccion{NBSP}string = ""', f'x="704.5" y="57">direccion{NBSP}string = ""'),
    (f'x="764.5" y="71">provincia{NBSP}string = ""', f'x="704.5" y="71">provincia{NBSP}string = ""'),
    ('x="764.5" y="45">numero uint = 0', 'x="704.5" y="45">numero uint = 0'),
    ('x="754.5" y="44">Direccion', 'x="694.5" y="44">Direccion'),

    # === Row 1: Direccion(Av.Corrientes): old (510,190) -> new (930,30) => dx=420, dy=-160 ===
    (f'x="514.5" y="203">calle{NBSP}string = "Av. Corrientes"', f'x="934.5" y="43">calle{NBSP}string = "Av. Corrientes"'),
    ('x="514.5" y="217">ciudad string = "CABA"', 'x="934.5" y="57">ciudad string = "CABA"'),
    (f'x="514.5" y="231">provincia{NBSP}string = "Buenos Aires"', f'x="934.5" y="71">provincia{NBSP}string = "Buenos Aires"'),
    ('x="514.5" y="365.5">numero uint = 1050', 'x="934.5" y="45">numero uint = 1050'),
    ('x="504.5" y="204">Direccion', 'x="924.5" y="44">Direccion'),

    # === Row 2: Persona(p3): old (360,110) -> new (300,140) => dx=-60, dy=30 ===
    ('x="364.5" y="123">nombre string = "Juan"', 'x="304.5" y="153">nombre string = "Juan"'),
    ('x="364.5" y="137">apellido string = "Gonzalez"', 'x="304.5" y="167">apellido string = "Gonzalez"'),
    ('x="364.5" y="111">edad uint = 34', 'x="304.5" y="141">edad uint = 34'),
    ('x="364.5" y="275.5">direccion Direccion = *', 'x="304.5" y="305.5">direccion Direccion = *'),
    ('x="354.5" y="124">Persona', 'x="294.5" y="154">Persona'),

    # === Row 2: Direccion(p3): old (700,90) -> new (580,140) => dx=-120, dy=50 ===
    (f'x="704.5" y="103">calle{NBSP}string = "Valentín Gomez"', f'x="584.5" y="153">calle{NBSP}string = "Valentín Gomez"'),
    ('x="704.5" y="117">ciudad string = "Caseros"', 'x="584.5" y="167">ciudad string = "Caseros"'),
    (f'x="704.5" y="131">provincia{NBSP}string = "Buenos Aires"', f'x="584.5" y="181">provincia{NBSP}string = "Buenos Aires"'),
    ('x="704.5" y="105">numero uint = 742', 'x="584.5" y="155">numero uint = 742'),
    ('x="694.5" y="104">Direccion', 'x="574.5" y="154">Direccion'),

    # === Row 3: Persona(p1): old (340,290) -> new (300,280) => dx=-40, dy=-10 ===
    ('x="344.5" y="303">nombre string = "Marcelo"', 'x="304.5" y="293">nombre string = "Marcelo"'),
    ('x="344.5" y="317">apellido string = ""', 'x="304.5" y="307">apellido string = ""'),
    ('x="344.5" y="291">edad uint = 27', 'x="304.5" y="281">edad uint = 27'),
    ('x="344.5" y="95.5">direccion Direccion = *', 'x="304.5" y="85.5">direccion Direccion = *'),
    ('x="334.5" y="304">Persona', 'x="294.5" y="294">Persona'),

    # === Row 3: Direccion(p1) empty: old (700,270) -> new (560,280) => dx=-140, dy=10 ===
    (f'x="704.5" y="283">calle{NBSP}string = ""', f'x="564.5" y="293">calle{NBSP}string = ""'),
    (f'x="704.5" y="297">direccion{NBSP}string = ""', f'x="564.5" y="307">direccion{NBSP}string = ""'),
    (f'x="704.5" y="311">provincia{NBSP}string = ""', f'x="564.5" y="321">provincia{NBSP}string = ""'),
    ('x="704.5" y="285">numero uint = 0', 'x="564.5" y="295">numero uint = 0'),
    ('x="694.5" y="284">Direccion', 'x="554.5" y="294">Direccion'),
]

# =====================================================
# Arrow path replacements
# =====================================================
# Format: (old_d_attribute, new_d_attribute)

ARROW_REPLACEMENTS = [
    # Arrow 1: p2 (180,20) -> Persona(p2) at (300,30..90, center ~50)
    # Was: M 180 20 Q 210 10 240 17 Q 270 25 300 25 Q 330 25 373.9 11
    # New: straight curve right and slightly down
    ('M 180 20 Q 210 10 240 17 Q 270 25 300 25 Q 330 25 373.9 11',
     'M 180 20 Q 200 20 240 50 Q 260 50 293.63 50'),
    ('M 378.93 80 L 373.23 45 L 371.22 78 Z',
     'M 298.88 50 L 291.88 47 L 291.88 53 Z'),

    # Arrow 2: p3 (180,80) -> Persona(p3) at (300,140..200, center ~170)
    # Was: M 180 80 Q 230 250 353.63 250
    ('M 180 80 Q 230 250 353.63 250',
     'M 180 80 Q 200 80 240 170 Q 260 170 293.63 170'),
    ('M 238 140 L 231 143 L 231 136 Z',
     'M 298.88 170 L 291.88 167 L 291.88 173 Z'),

    # Arrow 3: p4 (180,140) -> Persona(p2) at (300,30..90, center ~50)
    # p4 points to p2, so same target as Arrow 1 but enters at y=70
    # Was: M 180 140 Q 250 270 265 235 Q 280 200 315 200 Q 350 200 375.11 179.08
    ('M 180 140 Q 250 270 265 235 Q 280 200 315 200 Q 350 200 375.11 179.08',
     'M 180 140 Q 200 140 240 70 Q 260 70 293.63 70'),
    ('M 379.14 55 L 376 62 L 371.52 57 Z',
     'M 298.88 70 L 291.88 67 L 291.88 73 Z'),

    # Arrow 4: dir (180,200) -> Direccion(Av.Corrientes) at (930,30..90, center ~45)
    # Route: go right from dir, curve up to y=45 (inside target box), across
    ('M 180 200 Q 240 330 315 200 Q 390 370 503.82 191',
     'M 180 200 Q 220 200 220 45 Q 220 45 923.63 45'),
    ('M 508.92 220 L 502.97 225 L 501.28 218 Z',
     'M 928.88 45 L 921.88 42 L 921.88 48 Z'),

    # Arrow 5: p1 (180,310) -> Persona(p1) at (300,280..340, center ~310)
    # Was: M 180 310 Q 200 310 240 90 Q 280 70 333.63 70 ← this went up to y=70, wrong!
    ('M 180 310 Q 200 310 240 90 Q 280 70 333.63 70',
     'M 180 310 Q 220 310 293.63 310'),
    ('M 218 320 L 211 323 L 211 316 Z',
     'M 298.88 310 L 291.88 307 L 291.88 313 Z'),

    # Arrow 6: Persona(p2) -> Direccion(empty, red) at (700,30..90, center ~60)
    # From Persona(p2) right side at y=60 (dashed, original direccion)
    ('M 554 60 Q 660 60 753.63 60',
     'M 514 60 Q 600 60 693.63 60'),
    ('M 758.88 60 L 751.88 63 L 751.88 56 Z',
     'M 698.88 60 L 691.88 63 L 691.88 57 Z'),

    # Arrow 7: Persona(p2) -> Direccion(Av.Corrientes) at (930,30..90, center ~45)
    # From Persona(p2) right side. Route slightly above the dashed arrow (at y=50 vs y=60)
    ('M 554 60 Q 600 60 620 110 Q 640 110 648.75 303.76',
     'M 514 50 Q 700 50 923.63 50'),
    ('M 649.78 308.9 L 644.98 302.73 L 651.84 301.35 Z',
     'M 928.88 50 L 921.88 47 L 921.88 53 Z'),

    # Arrow 8: Persona(p3) -> Direccion(p3) at (580,140..200, center ~170)
    # From Persona(p3) right side at x~514
    # Was: M 535 120 Q 600 120 625 140 Q 650 120 693.63 120
    ('M 535 120 Q 600 120 625 140 Q 650 120 693.63 120',
     'M 514 170 Q 540 170 573.63 170'),
    ('M 698.88 120 L 691.88 123 L 691.88 116 Z',
     'M 578.88 170 L 571.88 173 L 571.88 167 Z'),

    # Arrow 9: Persona(p1) -> Direccion(p1) at (560,280..340, center ~310)
    # From Persona(p1) right side at x~494
    # Was: M 514 300 Q 570 300 605 320 Q 640 300 693.63 300
    ('M 514 300 Q 570 300 605 320 Q 640 300 693.63 300',
     'M 494 310 Q 520 310 553.63 310'),
    ('M 698.88 300 L 691.88 303 L 691.88 296 Z',
     'M 558.88 310 L 551.88 313 L 551.88 307 Z'),
]


def fix_titles(svg):
    svg = re.sub(
        r'(y="19\.5"[^>]*font-weight="bold"[^>]*>Stack<)',
        lambda m: m.group(0).replace('y="19.5"', 'y="12"'),
        svg
    )
    svg = re.sub(
        r'(y="249\.5"[^>]*font-weight="bold"[^>]*>Segmento de Datos<)',
        lambda m: m.group(0).replace('y="249.5"', 'y="238"'),
        svg
    )
    return svg


def process(variant):
    fname = f"MapaDeMemoria_{variant}.svg"
    path = os.path.join(BASE, fname)
    
    with open(path) as f:
        svg = f.read()
    
    # 1. Titles
    svg = fix_titles(svg)
    
    # 2. Heap rects
    for old, new in HEAP_RECT_MOVES:
        if old in svg:
            svg = svg.replace(old, new)
        else:
            print(f"  [WARN] rect not found: {old}")
    
    # 3. Text
    for old, new in TEXT_MOVES:
        if old in svg:
            svg = svg.replace(old, new)
        else:
            print(f"  [WARN] text not found: {old[:60]}")
    
    # 4. Arrows
    for old, new in ARROW_REPLACEMENTS:
        if old in svg:
            svg = svg.replace(old, new)
        else:
            print(f"  [WARN] arrow not found: {old[:60]}")
    
    # Backup
    bak = path + ".bak2"
    if not os.path.exists(bak):
        with open(bak, 'w') as f:
            f.write(open(path).read())
        print(f"  Backup: {fname}.bak2")
    
    with open(path, 'w') as f:
        f.write(svg)
    print(f"  Written: {fname}")


if __name__ == "__main__":
    for v in ['light', 'dark']:
        print(f"--- {v} ---")
        process(v)
