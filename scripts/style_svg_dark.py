import re

filepath = "/home/martin/AyP2/apuntes/contenidos/_static/figures/MapaDeMemoria_dark.svg"
try:
    with open(filepath, "r") as f:
        content = f.read()
except FileNotFoundError:
    print("MapaDeMemoria_dark.svg not found")
    exit(0)

# 1. Remove light-dark style wrapping
content = re.sub(r'style="[^"]*light-dark[^"]*"', "", content)

# 2. Font family to UI sans
content = content.replace('font-family="Hack"', 'font-family="ui-sans-serif, system-ui, sans-serif"')
content = content.replace('font-family="Jetbrains Mono"', 'font-family="ui-sans-serif, system-ui, sans-serif"')
content = content.replace('font-family="&quot;Hack&quot;"', 'font-family="ui-sans-serif, system-ui, sans-serif"')
content = content.replace(
    'font-family="&quot;Jetbrains Mono&quot;"', 'font-family="ui-sans-serif, system-ui, sans-serif"'
)

# Make text white-ish like dark mode guidelines
content = re.sub(r'fill="#333333"', 'fill="#e0e0e0"', content)
content = re.sub(r'stroke="#333333"', 'stroke="#e0e0e0"', content)

# 3. Heap background: remove fill
content = re.sub(r'(<g data-cell-id="156">.*?)fill="#[a-zA-Z0-9]+"(.*?/>)', r'\1fill="none"\2', content)
content = re.sub(r'(<g data-cell-id="156">.*?)stroke="#[a-zA-Z0-9]+"(.*?/>)', r'\1stroke="none"\2', content)


def replace_node_style(content, node_id, new_fill, new_stroke):
    pattern = rf'(<g data-cell-id="{node_id}">\s*<g>\s*<rect[^>]*?)fill="[^"]*"(.*?)stroke="[^"]*"(.*?/>)'
    replacement = rf'\1fill="{new_fill}"\2stroke="{new_stroke}" stroke-width="2"\3'
    pattern2 = rf'(<g data-cell-id="{node_id}">\s*<g>\s*<rect[^>]*?)stroke="[^"]*"(.*?)fill="[^"]*"(.*?/>)'
    replacement2 = rf'\1stroke="{new_stroke}" stroke-width="2"\2fill="{new_fill}"\3'

    new_content = re.sub(pattern, replacement, content)
    if new_content == content:
        new_content = re.sub(pattern2, replacement2, content)
    return new_content


# Blue objects -> Dark Mode equivalent: #2d3748 fill, #63b3ed stroke
for nid in [142, 122, 126, 132, 140, 135]:
    content = replace_node_style(content, nid, "#2d3748", "#63b3ed")

# Red object (147) and Stack (157) -> Dark Mode equivalent: #4a5568 fill, #fc8181 stroke
content = replace_node_style(content, 147, "#4a5568", "#fc8181")
content = replace_node_style(content, 157, "#4a5568", "#fc8181")

# Left side small pointer variables (75, 89, 93, 97, 102, 106)
for nid in [75, 89, 93, 97, 102, 106]:
    # Use dark grey for them
    content = replace_node_style(content, nid, "#1a202c", "#e0e0e0")

content = re.sub(r'(<g data-cell-id="149">.*?stroke=)"#[a-zA-Z0-9]+"', r'\1"#fc8181"', content)

with open(filepath, "w") as f:
    f.write(content)
