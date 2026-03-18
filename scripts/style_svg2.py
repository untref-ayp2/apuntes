import re

filepath = "/home/martin/AyP2/apuntes/contenidos/_static/figures/MapaDeMemoria_light.svg"
with open(filepath, "r") as f:
    content = f.read()


def replace_node_style(content, node_id, new_fill, new_stroke):
    pattern = rf'(<g data-cell-id="{node_id}">\s*<g>\s*<rect[^>]*?)fill="[^"]*"(.*?)stroke="[^"]*"(.*?/>)'
    replacement = rf'\1fill="{new_fill}"\2stroke="{new_stroke}" stroke-width="2"\3'
    # Try with stroke before fill just in case
    pattern2 = rf'(<g data-cell-id="{node_id}">\s*<g>\s*<rect[^>]*?)stroke="[^"]*"(.*?)fill="[^"]*"(.*?/>)'
    replacement2 = rf'\1stroke="{new_stroke}" stroke-width="2"\2fill="{new_fill}"\3'

    new_content = re.sub(pattern, replacement, content)
    if new_content == content:
        new_content = re.sub(pattern2, replacement2, content)
    return new_content


# Blue objects
for nid in [142, 122, 126, 132, 140, 135]:
    content = replace_node_style(content, nid, "#e1f5ff", "#4682b4")

# Red object (147)
content = replace_node_style(content, 147, "#ffe1e1", "#e9967a")
# Also red arrow 149
content = re.sub(r'(<g data-cell-id="149">.*?stroke=)"#ff6666"', r'\1"#e9967a"', content)
content = re.sub(r'(<g data-cell-id="149">.*?fill=)"#ff6666"', r'\1"#e9967a"', content)

# Stack region 157
content = replace_node_style(content, 157, "#ffe1e1", "#e9967a")

with open(filepath, "w") as f:
    f.write(content)
