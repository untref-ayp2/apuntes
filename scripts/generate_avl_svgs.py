#!/usr/bin/env python3
"""Generate all AVL tree SVG figures for chapter 3-10.

Positions updated from user's Inkscape edits.
IMPORTANT: The IZQIZQ example is at node 20 (not 15).
When inserting 5 as left child of 10: fb(15)=+1, fb(20)=+2 (first unbalanced).
"""

import os

OUT = "contenidos/_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados"

# ── Base positions (from user's AVL_light.svg Inkscape edit) ────
N = {}
N[50] = (350, 40)
N[30] = (212, 110); N[70] = (494, 110)
N[20] = (142, 175); N[40] = (282, 175); N[60] = (424, 175); N[80] = (564, 175)
N[15] = (97, 235);  N[25] = (187, 235); N[45] = (327, 235)
N[55] = (379, 235); N[65] = (469, 235); N[75] = (519, 235); N[85] = (609, 235)
N[10] = (67, 290);  N[17] = (127, 290)
N[64] = (439, 290); N[66] = (499, 290); N[83] = (579, 290)

# IZQIZQ variant: shifted up 20px to fit 5 at y=320
# (from user's AVLIZQIZQ_light.svg edit)
I = dict(N)
for k in I: I[k] = (I[k][0], I[k][1] - 20)  # shift all up
I[50] = (350, 20)
I[30] = (212, 90); I[70] = (494, 90)
I[20] = (142, 155); I[40] = (282, 155); I[60] = (424, 155); I[80] = (564, 155)
I[15] = (97, 215);  I[25] = (187, 215); I[45] = (327, 215)
I[55] = (379, 215); I[65] = (469, 215); I[75] = (519, 215); I[85] = (609, 215)
I[10] = (67, 270);  I[17] = (127, 270)
I[64] = (439, 270); I[66] = (499, 270); I[83] = (579, 270)
I[5]  = (37, 320)

# FB label preferences: nodes on LEFT side get text-anchor:end
LEFT_SET = {30, 20, 15, 10, 55, 64}
LABEL_OVERRIDE = {
    45: (399, 231, "start"),
    65: (473, 211, "start"),
}

def node(v, fb_val, fb_class="fb-bal", pd=None):
    if pd is None: pd = N
    x, y = pd[v]
    if v in LABEL_OVERRIDE:
        lx, ly, anchor = LABEL_OVERRIDE[v]
        st = ' style="text-anchor:end"' if anchor == "end" else ""
        label = f'  <text class="fb-label {fb_class}" x="{lx}" y="{ly}"{st}>fb = {fb_val}</text>'
    elif v in LEFT_SET:
        label = f'  <text class="fb-label {fb_class}" x="{x-22}" y="{y-4}" style="text-anchor:end">fb = {fb_val}</text>'
    else:
        label = f'  <text class="fb-label {fb_class}" x="{x+22}" y="{y-4}">fb = {fb_val}</text>'
    return (
        f'  <circle class="node-circle" cx="{x}" cy="{y}" r="16"/>\n'
        f'  <text class="node-text" x="{x}" y="{y}">{v}</text>\n'
        + label
    )

def edge(v, w, pd=None):
    if pd is None: pd = N
    x1, y1 = pd[v]; x2, y2 = pd[w]
    return f'  <line class="edge" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'

def full_tree_edges(pd=None):
    if pd is None: pd = N
    return [
        edge(50, 30, pd), edge(50, 70, pd),
        edge(30, 20, pd), edge(30, 40, pd),
        edge(70, 60, pd), edge(70, 80, pd),
        edge(20, 15, pd), edge(20, 25, pd),
        edge(40, 45, pd),
        edge(60, 55, pd), edge(60, 65, pd),
        edge(80, 75, pd), edge(80, 85, pd),
        edge(15, 10, pd), edge(15, 17, pd),
        edge(65, 64, pd), edge(65, 66, pd),
        edge(85, 83, pd),
    ]

def all_nodes(pd=None, extra_nodes=None, overrides=None):
    if pd is None: pd = N
    if extra_nodes is None: extra_nodes = []
    default_fb = {
        50: ("0",), 30: ("+1",), 70: ("0",),
        20: ("+1",), 40: ("-1",), 60: ("-1",), 80: ("-1",),
        15: ("0",), 25: ("0",), 45: ("0",), 55: ("0",), 65: ("0",),
        75: ("0",), 85: ("+1",),
        10: ("0",), 17: ("0",), 64: ("0",), 66: ("0",), 83: ("0",),
    }
    merged = dict(default_fb)
    if overrides: merged.update(overrides)
    result = []
    for v in sorted(merged.keys()):
        fb_val, *rest = merged[v]
        fb_class = rest[0] if rest else "fb-bal"
        result.append(node(v, fb_val, fb_class, pd))
    for v in extra_nodes:
        result.append(node(v, "0", "fb-bal", pd))
    return result

# ── SVG template ─────────────────────────────────────────────────
STYLE_LIGHT = """    .bg { fill: #f0f2f5; }
    .edge { stroke: #333333; stroke-width: 2; fill: none; }
    .node-circle { fill: #e1f5ff; stroke: #4682b4; stroke-width: 2.5; }
    .node-text { fill: #333333; font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 14px; font-weight: bold; text-anchor: middle; dominant-baseline: central; }
    .fb-label { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; font-weight: bold; text-anchor: start; dominant-baseline: central; }
    .fb-bal { fill: #2e8b57; }
    .fb-unbal { fill: #c53030; }
    .arrow-line { stroke: #333333; stroke-width: 2.5; marker-end: url(#arrowhead); }
    .label-sub { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 13px; fill: #333333; font-weight: bold; }"""

STYLE_DARK = """    .bg { fill: #1e1e1e; }
    .edge { stroke: #e0e0e0; stroke-width: 2; fill: none; }
    .node-circle { fill: #2d3748; stroke: #63b3ed; stroke-width: 2.5; }
    .node-text { fill: #e0e0e0; font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 14px; font-weight: bold; text-anchor: middle; dominant-baseline: central; }
    .fb-label { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; font-weight: bold; text-anchor: start; dominant-baseline: central; }
    .fb-bal { fill: #68d391; }
    .fb-unbal { fill: #fc8181; }
    .arrow-line { stroke: #e0e0e0; stroke-width: 2.5; marker-end: url(#arrowhead); }
    .label-sub { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 13px; fill: #e0e0e0; font-weight: bold; }"""

def make_svg(theme, viewbox, elements, height=340):
    style = STYLE_LIGHT if theme == "light" else STYLE_DARK
    arrow_fill = "#333333" if theme == "light" else "#e0e0e0"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}">
  <defs>
    <style>
{style}
    </style>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="8,3 0,6 0,0" fill="{arrow_fill}"/>
    </marker>
  </defs>
  <rect class="bg" width="700" height="{height}" rx="8"/>
{elements}
</svg>'''

def save_pair(name, elements, height=340):
    light = make_svg("light", f"0 0 700 {height}", elements, height)
    dark = make_svg("dark", f"0 0 700 {height}", elements, height)
    with open(os.path.join(OUT, f"{name}_light.svg"), "w") as f: f.write(light)
    with open(os.path.join(OUT, f"{name}_dark.svg"), "w") as f: f.write(dark)
    print(f"  {name}")

# ── 1. AVL ──────────────────────────────────────────────────────
# User-edited in Inkscape. Generate with base positions.

# ── 2. AVLIZQIZQ ────────────────────────────────────────────────
# Insert 5 as left child of 10. fb(20)=+2 (unbal), fb(15)=+1 (bal).
def make_izqizq():
    pd = dict(I)
    pd[5] = (37, 320)
    edges = full_tree_edges(pd) + [edge(10, 5, pd)]
    # Correct FB: 20 is unbalanced, 15 is balanced
    overrides = {20: ("+2", "fb-unbal"), 15: ("+1",), 50: ("+1",), 30: ("+1",)}
    return "\n".join(edges + all_nodes(pd, [5], overrides))

# ── 3. AVLRSD: RSD on 20 (before/after subtree) ────────────────
# Before: 20→15,25→10,17→5   After: 15→10,20→5,17,25
RSD_NODES = """  <text class="label-sub" x="20" y="20">Antes</text>
  <text class="label-sub" x="370" y="20">Después</text>
  <line class="edge" x1="140" y1="65" x2="80" y2="145"/>
  <line class="edge" x1="140" y1="65" x2="200" y2="145"/>
  <line class="edge" x1="80" y1="145" x2="45" y2="215"/>
  <line class="edge" x1="80" y1="145" x2="120" y2="215"/>
  <line class="edge" x1="45" y1="215" x2="25" y2="280"/>
  <circle class="node-circle" cx="140" cy="65" r="16"/><text class="node-text" x="140" y="65">20</text>
  <text class="fb-label fb-unbal" x="116" y="61" style="text-anchor:end">fb = +2</text>
  <circle class="node-circle" cx="80" cy="145" r="16"/><text class="node-text" x="80" y="145">15</text>
  <text class="fb-label fb-bal" x="106" y="141">fb = +1</text>
  <circle class="node-circle" cx="200" cy="145" r="16"/><text class="node-text" x="200" y="145">25</text>
  <text class="fb-label fb-bal" x="226" y="141">fb = 0</text>
  <circle class="node-circle" cx="45" cy="215" r="16"/><text class="node-text" x="45" y="215">10</text>
  <text class="fb-label fb-bal" x="71" y="211">fb = 0</text>
  <circle class="node-circle" cx="120" cy="215" r="16"/><text class="node-text" x="120" y="215">17</text>
  <text class="fb-label fb-bal" x="146" y="211">fb = 0</text>
  <circle class="node-circle" cx="25" cy="280" r="16"/><text class="node-text" x="25" y="280">5</text>
  <text class="fb-label fb-bal" x="51" y="276">fb = 0</text>
  <line class="arrow-line" x1="280" y1="100" x2="340" y2="100"/>
  <line class="edge" x1="450" y1="65" x2="390" y2="145"/>
  <line class="edge" x1="450" y1="65" x2="510" y2="145"/>
  <line class="edge" x1="390" y1="145" x2="360" y2="215"/>
  <line class="edge" x1="510" y1="145" x2="470" y2="215"/>
  <line class="edge" x1="510" y1="145" x2="550" y2="215"/>
  <circle class="node-circle" cx="450" cy="65" r="16"/><text class="node-text" x="450" y="65">15</text>
  <text class="fb-label fb-bal" x="476" y="61">fb = 0</text>
  <circle class="node-circle" cx="390" cy="145" r="16"/><text class="node-text" x="390" y="145">10</text>
  <text class="fb-label fb-bal" x="416" y="141">fb = 0</text>
  <circle class="node-circle" cx="510" cy="145" r="16"/><text class="node-text" x="510" y="145">20</text>
  <text class="fb-label fb-bal" x="536" y="141">fb = 0</text>
  <circle class="node-circle" cx="360" cy="215" r="16"/><text class="node-text" x="360" y="215">5</text>
  <text class="fb-label fb-bal" x="386" y="211">fb = 0</text>
  <circle class="node-circle" cx="470" cy="215" r="16"/><text class="node-text" x="470" y="215">17</text>
  <text class="fb-label fb-bal" x="496" y="211">fb = 0</text>
  <circle class="node-circle" cx="550" cy="215" r="16"/><text class="node-text" x="550" y="215">25</text>
  <text class="fb-label fb-bal" x="576" y="211">fb = 0</text>"""

# ── 4. AVLRestauradoRSD ─────────────────────────────────────────
# After RSD on 20: 15 takes 20's position. 10→5 left of 15. 20→17,25 right of 15.
def make_rest_rsd():
    pd = dict(I)  # use IZQIZQ positions (shifted up)
    # After RSD on 20:
    pd[15] = (142, 155)  # 15 takes 20's position
    pd[10] = (97, 215)   # 10 left of 15
    pd[5]  = (67, 270)   # 5 left of 10
    pd[20] = (187, 215)  # 20 right of 15
    pd[17] = (157, 270)  # 17 left of 20
    pd[25] = (217, 270)  # 25 right of 20
    edges = [
        edge(50, 30, pd), edge(50, 70, pd),
        edge(30, 15, pd), edge(30, 40, pd),  # 30's left is now 15
        edge(70, 60, pd), edge(70, 80, pd),
        edge(15, 10, pd), edge(15, 20, pd),
        edge(40, 45, pd),
        edge(60, 55, pd), edge(60, 65, pd),
        edge(80, 75, pd), edge(80, 85, pd),
        edge(10, 5, pd),
        edge(20, 17, pd), edge(20, 25, pd),
        edge(65, 64, pd), edge(65, 66, pd),
        edge(85, 83, pd),
    ]
    overrides = {50: ("0",), 30: ("0",), 20: ("0",), 15: ("0",)}
    return "\n".join(edges + all_nodes(pd, [5], overrides)), 320

# ── 5. AVLIZQDER ────────────────────────────────────────────────
def make_izqder():
    pd = dict(N); pd[18] = (157, 340)
    edges = full_tree_edges(pd) + [edge(17, 18, pd)]
    overrides = {20: ("+2", "fb-unbal"), 50: ("+1",), 30: ("+1",)}
    return "\n".join(edges + all_nodes(pd, [18], overrides))

# ── 6. AVLIZQDER-1 (subtree before/after) ───────────────────────
IZQDER1_NODES = """  <text class="label-sub" x="20" y="20">Antes</text>
  <text class="label-sub" x="370" y="20">Después</text>
  <line class="edge" x1="130" y1="65" x2="90" y2="155"/>
  <line class="edge" x1="130" y1="65" x2="180" y2="155"/>
  <line class="edge" x1="180" y1="155" x2="215" y2="240"/>
  <circle class="node-circle" cx="130" cy="65" r="16"/><text class="node-text" x="130" y="65">15</text>
  <text class="fb-label fb-bal" x="106" y="61" style="text-anchor:end">fb = -1</text>
  <circle class="node-circle" cx="90" cy="155" r="16"/><text class="node-text" x="90" y="155">10</text>
  <text class="fb-label fb-bal" x="116" y="151">fb = 0</text>
  <circle class="node-circle" cx="180" cy="155" r="16"/><text class="node-text" x="180" y="155">17</text>
  <text class="fb-label fb-bal" x="206" y="151">fb = 0</text>
  <circle class="node-circle" cx="215" cy="240" r="16"/><text class="node-text" x="215" y="240">18</text>
  <text class="fb-label fb-bal" x="241" y="236">fb = 0</text>
  <line class="arrow-line" x1="285" y1="115" x2="345" y2="115"/>
  <line class="edge" x1="460" y1="65" x2="410" y2="155"/>
  <line class="edge" x1="460" y1="65" x2="515" y2="155"/>
  <line class="edge" x1="410" y1="155" x2="370" y2="240"/>
  <circle class="node-circle" cx="460" cy="65" r="16"/><text class="node-text" x="460" y="65">17</text>
  <text class="fb-label fb-bal" x="486" y="61">fb = +1</text>
  <circle class="node-circle" cx="410" cy="155" r="16"/><text class="node-text" x="410" y="155">15</text>
  <text class="fb-label fb-bal" x="436" y="151">fb = 0</text>
  <circle class="node-circle" cx="515" cy="155" r="16"/><text class="node-text" x="515" y="155">18</text>
  <text class="fb-label fb-bal" x="541" y="151">fb = 0</text>
  <circle class="node-circle" cx="370" cy="240" r="16"/><text class="node-text" x="370" y="240">10</text>
  <text class="fb-label fb-bal" x="396" y="236">fb = 0</text>"""

# ── 7. AVLIZQDER-2 ──────────────────────────────────────────────
IZQDER2_NODES = """  <text class="label-sub" x="20" y="20">Antes</text>
  <text class="label-sub" x="370" y="20">Después</text>
  <line class="edge" x1="130" y1="65" x2="80" y2="155"/>
  <line class="edge" x1="130" y1="65" x2="185" y2="155"/>
  <line class="edge" x1="80" y1="155" x2="45" y2="240"/>
  <line class="edge" x1="80" y1="155" x2="120" y2="240"/>
  <circle class="node-circle" cx="130" cy="65" r="16"/><text class="node-text" x="130" y="65">20</text>
  <text class="fb-label fb-unbal" x="106" y="61" style="text-anchor:end">fb = +2</text>
  <circle class="node-circle" cx="80" cy="155" r="16"/><text class="node-text" x="80" y="155">17</text>
  <text class="fb-label fb-bal" x="106" y="151">fb = 0</text>
  <circle class="node-circle" cx="185" cy="155" r="16"/><text class="node-text" x="185" y="155">25</text>
  <text class="fb-label fb-bal" x="211" y="151">fb = 0</text>
  <circle class="node-circle" cx="45" cy="240" r="16"/><text class="node-text" x="45" y="240">15</text>
  <text class="fb-label fb-bal" x="71" y="236">fb = 0</text>
  <circle class="node-circle" cx="120" cy="240" r="16"/><text class="node-text" x="120" y="240">18</text>
  <text class="fb-label fb-bal" x="146" y="236">fb = 0</text>
  <line class="arrow-line" x1="260" y1="100" x2="330" y2="100"/>
  <line class="edge" x1="450" y1="65" x2="390" y2="155"/>
  <line class="edge" x1="450" y1="65" x2="510" y2="155"/>
  <line class="edge" x1="510" y1="155" x2="465" y2="240"/>
  <line class="edge" x1="510" y1="155" x2="555" y2="240"/>
  <circle class="node-circle" cx="450" cy="65" r="16"/><text class="node-text" x="450" y="65">17</text>
  <text class="fb-label fb-bal" x="476" y="61">fb = 0</text>
  <circle class="node-circle" cx="390" cy="155" r="16"/><text class="node-text" x="390" y="155">15</text>
  <text class="fb-label fb-bal" x="416" y="151">fb = 0</text>
  <circle class="node-circle" cx="510" cy="155" r="16"/><text class="node-text" x="510" y="155">20</text>
  <text class="fb-label fb-bal" x="536" y="151">fb = 0</text>
  <circle class="node-circle" cx="465" cy="240" r="16"/><text class="node-text" x="465" y="240">18</text>
  <text class="fb-label fb-bal" x="491" y="236">fb = 0</text>
  <circle class="node-circle" cx="555" cy="240" r="16"/><text class="node-text" x="555" y="240">25</text>
  <text class="fb-label fb-bal" x="581" y="236">fb = 0</text>"""

# ── 8. AVLIZQDER-2: full tree after RSI on 15 ─────────────────
def make_izqder2():
    pd = dict(N)
    # After RSI on 15: 17→15,18. 15 has left=10.
    pd[17] = (142, 175)  # 17 takes 20's spot (lv2)
    pd[20] = (187, 235)  # 20 right of 17 (lv3)
    pd[15] = (97, 235)   # 15 left of 17 (lv3)
    pd[10] = (67, 290)   # 10 left of 15 (lv4)
    pd[18] = (157, 290)  # 18 right of 17 (lv4)
    pd[25] = (217, 290)  # 25 right of 20 (lv4)
    edges = [
        edge(50, 30, pd), edge(50, 70, pd),
        edge(30, 17, pd), edge(30, 40, pd),
        edge(70, 60, pd), edge(70, 80, pd),
        edge(17, 15, pd), edge(17, 20, pd),
        edge(40, 45, pd),
        edge(60, 55, pd), edge(60, 65, pd),
        edge(80, 75, pd), edge(80, 85, pd),
        edge(15, 10, pd),
        edge(20, 18, pd), edge(20, 25, pd),
        edge(65, 64, pd), edge(65, 66, pd),
        edge(85, 83, pd),
    ]
    overrides = {20: ("+2", "fb-unbal"), 50: ("0",), 30: ("+1",), 17: ("0",)}
    return "\n".join(edges + all_nodes(pd, [18, 10], overrides))

# ── 9. AVLIZQDER-4 ──────────────────────────────────────────────
def make_izqder4():
    pd = dict(N)
    pd[17] = (142, 175); pd[20] = (187, 235); pd[15] = (97, 235)
    pd[10] = (67, 290); pd[18] = (157, 290); pd[25] = (217, 290)
    edges = [edge(50, 30, pd), edge(50, 70, pd),
        edge(30, 17, pd), edge(30, 40, pd),
        edge(70, 60, pd), edge(70, 80, pd),
        edge(17, 15, pd), edge(17, 20, pd),
        edge(40, 45, pd),
        edge(60, 55, pd), edge(60, 65, pd),
        edge(80, 75, pd), edge(80, 85, pd),
        edge(15, 10, pd),
        edge(20, 18, pd), edge(20, 25, pd),
        edge(65, 64, pd), edge(65, 66, pd), edge(85, 83, pd)]
    overrides = {50: ("0",), 30: ("0",), 17: ("0",), 20: ("0",)}
    return "\n".join(edges + all_nodes(pd, [18, 10], overrides))

# ── 9. AVLDERDER ────────────────────────────────────────────────
def make_derder():
    pd = dict(N); pd[67] = (529, 340)
    edges = full_tree_edges(pd) + [edge(66, 67, pd)]
    overrides = {60: ("-2", "fb-unbal"), 70: ("+1",), 50: ("0",), 30: ("+1",)}
    return "\n".join(edges + all_nodes(pd, [67], overrides))

# ── 10. AVLRSI (before/after subtree) ───────────────────────────
RSI_NODES = """  <text class="label-sub" x="20" y="20">Antes</text>
  <text class="label-sub" x="370" y="20">Después</text>
  <line class="edge" x1="130" y1="65" x2="80" y2="155"/>
  <line class="edge" x1="130" y1="65" x2="190" y2="155"/>
  <line class="edge" x1="190" y1="155" x2="150" y2="240"/>
  <line class="edge" x1="190" y1="155" x2="230" y2="240"/>
  <line class="edge" x1="230" y1="240" x2="265" y2="310"/>
  <circle class="node-circle" cx="130" cy="65" r="16"/><text class="node-text" x="130" y="65">60</text>
  <text class="fb-label fb-unbal" x="106" y="61" style="text-anchor:end">fb = -2</text>
  <circle class="node-circle" cx="80" cy="155" r="16"/><text class="node-text" x="80" y="155">55</text>
  <text class="fb-label fb-bal" x="106" y="151">fb = 0</text>
  <circle class="node-circle" cx="190" cy="155" r="16"/><text class="node-text" x="190" y="155">65</text>
  <text class="fb-label fb-bal" x="216" y="151">fb = -1</text>
  <circle class="node-circle" cx="150" cy="240" r="16"/><text class="node-text" x="150" y="240">64</text>
  <text class="fb-label fb-bal" x="176" y="236">fb = 0</text>
  <circle class="node-circle" cx="230" cy="240" r="16"/><text class="node-text" x="230" y="240">66</text>
  <text class="fb-label fb-bal" x="256" y="236">fb = 0</text>
  <circle class="node-circle" cx="265" cy="310" r="16"/><text class="node-text" x="265" y="310">67</text>
  <text class="fb-label fb-bal" x="291" y="306">fb = 0</text>
  <line class="arrow-line" x1="330" y1="130" x2="400" y2="130"/>
  <line class="edge" x1="480" y1="65" x2="420" y2="155"/>
  <line class="edge" x1="480" y1="65" x2="540" y2="155"/>
  <line class="edge" x1="420" y1="155" x2="380" y2="240"/>
  <line class="edge" x1="420" y1="155" x2="465" y2="240"/>
  <circle class="node-circle" cx="480" cy="65" r="16"/><text class="node-text" x="480" y="65">65</text>
  <text class="fb-label fb-bal" x="506" y="61">fb = 0</text>
  <circle class="node-circle" cx="420" cy="155" r="16"/><text class="node-text" x="420" y="155">60</text>
  <text class="fb-label fb-bal" x="446" y="151">fb = 0</text>
  <circle class="node-circle" cx="540" cy="155" r="16"/><text class="node-text" x="540" y="155">67</text>
  <text class="fb-label fb-bal" x="566" y="151">fb = 0</text>
  <circle class="node-circle" cx="380" cy="240" r="16"/><text class="node-text" x="380" y="240">55</text>
  <text class="fb-label fb-bal" x="406" y="236">fb = 0</text>
  <circle class="node-circle" cx="465" cy="240" r="16"/><text class="node-text" x="465" y="240">64</text>
  <text class="fb-label fb-bal" x="491" y="236">fb = 0</text>"""

# ── 11. AVLRestauradoRSI ────────────────────────────────────────
def make_rest_rsi():
    pd = dict(N)
    pd[65] = (424, 175); pd[60] = (379, 235)
    pd[55] = (349, 290); pd[64] = (409, 290)
    pd[67] = (469, 235); pd[66] = (499, 290)
    edges = [edge(50, 30, pd), edge(50, 70, pd),
        edge(30, 20, pd), edge(30, 40, pd),
        edge(70, 65, pd), edge(70, 80, pd),
        edge(20, 15, pd), edge(20, 25, pd),
        edge(40, 45, pd),
        edge(65, 60, pd), edge(65, 67, pd),
        edge(80, 75, pd), edge(80, 85, pd),
        edge(15, 10, pd), edge(15, 17, pd),
        edge(60, 55, pd), edge(60, 64, pd),
        edge(67, 66, pd), edge(85, 83, pd)]
    overrides = {50: ("0",), 30: ("+1",), 65: ("0",), 70: ("0",)}
    return "\n".join(edges + all_nodes(pd, [67, 66], overrides)), 340

# ── 12. AVLDERIZQ ───────────────────────────────────────────────
def make_derizq():
    pd = dict(N); pd[82] = (549, 340)
    edges = full_tree_edges(pd) + [edge(83, 82, pd)]
    overrides = {80: ("-2", "fb-unbal"), 85: ("+1",), 70: ("+1",), 50: ("0",), 30: ("+1",)}
    return "\n".join(edges + all_nodes(pd, [82], overrides))

# ── 13. AVLDERIZQ-1 (subtree before/after) ──────────────────────
DERIZQ1_NODES = """  <text class="label-sub" x="20" y="20">Antes</text>
  <text class="label-sub" x="370" y="20">Después</text>
  <line class="edge" x1="130" y1="65" x2="90" y2="155"/>
  <line class="edge" x1="90" y1="155" x2="55" y2="240"/>
  <circle class="node-circle" cx="130" cy="65" r="16"/><text class="node-text" x="130" y="65">85</text>
  <text class="fb-label fb-bal" x="156" y="61">fb = +1</text>
  <circle class="node-circle" cx="90" cy="155" r="16"/><text class="node-text" x="90" y="155">83</text>
  <text class="fb-label fb-bal" x="116" y="151">fb = 0</text>
  <circle class="node-circle" cx="55" cy="240" r="16"/><text class="node-text" x="55" y="240">82</text>
  <text class="fb-label fb-bal" x="81" y="236">fb = 0</text>
  <line class="arrow-line" x1="220" y1="110" x2="300" y2="110"/>
  <line class="edge" x1="430" y1="65" x2="380" y2="155"/>
  <line class="edge" x1="430" y1="65" x2="480" y2="155"/>
  <circle class="node-circle" cx="430" cy="65" r="16"/><text class="node-text" x="430" y="65">83</text>
  <text class="fb-label fb-bal" x="456" y="61">fb = 0</text>
  <circle class="node-circle" cx="380" cy="155" r="16"/><text class="node-text" x="380" y="155">82</text>
  <text class="fb-label fb-bal" x="406" y="151">fb = 0</text>
  <circle class="node-circle" cx="480" cy="155" r="16"/><text class="node-text" x="480" y="155">85</text>
  <text class="fb-label fb-bal" x="506" y="151">fb = 0</text>"""

# ── 14. AVLDERIZQ-2 ─────────────────────────────────────────────
def make_derizq2():
    pd = dict(N)
    pd[83] = (564, 175); pd[80] = (519, 235); pd[85] = (609, 235)
    pd[75] = (489, 290); pd[82] = (549, 290)
    edges = [edge(50, 30, pd), edge(50, 70, pd),
        edge(30, 20, pd), edge(30, 40, pd),
        edge(70, 60, pd), edge(70, 83, pd),
        edge(20, 15, pd), edge(20, 25, pd),
        edge(40, 45, pd),
        edge(60, 55, pd), edge(60, 65, pd),
        edge(83, 80, pd), edge(83, 85, pd),
        edge(80, 75, pd), edge(80, 82, pd),
        edge(15, 10, pd), edge(15, 17, pd),
        edge(65, 64, pd), edge(65, 66, pd)]
    overrides = {50: ("0",), 30: ("+1",), 83: ("0",), 70: ("0",), 80: ("0",), 85: ("0",)}
    return "\n".join(edges + all_nodes(pd, [82], overrides))

# ── Generate ──────────────────────────────────────────────────────
os.makedirs(OUT, exist_ok=True)

save_pair("AVL", "\n".join(full_tree_edges() + all_nodes()))
save_pair("AVLIZQIZQ", make_izqizq())
save_pair("AVLRotacionSimpleDerecha", RSD_NODES, 330)
d, h = make_rest_rsd(); save_pair("AVLRestauradoRSD", d, h)
save_pair("AVLIZQDER", make_izqder())
save_pair("AVLIZQDER-1", IZQDER1_NODES, 290)
save_pair("AVLIZQDER-2", make_izqder2())
save_pair("AVLIZQDER-3", IZQDER2_NODES, 290)
save_pair("AVLIZQDER-4", make_izqder4())
save_pair("AVLDERDER", make_derder())
save_pair("AVLRotacionSimpleIzquierda", RSI_NODES, 360)
d, h = make_rest_rsi(); save_pair("AVLRestauradoRSI", d, h)
save_pair("AVLDERIZQ", make_derizq())
save_pair("AVLDERIZQ-1", DERIZQ1_NODES, 290)
save_pair("AVLDERIZQ-2", make_derizq2())

print("\nDone!")
