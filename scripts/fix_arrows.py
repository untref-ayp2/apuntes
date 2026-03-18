import re

files = [
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/MapaDeMemoria_light.svg",
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/MapaDeMemoria_dark.svg",
]

pattern = r'd="M ([\d\.-]+) ([\d\.-]+) L ([\d\.-]+) ([\d\.-]+) L ([\d\.-]+) ([\d\.-]+) L ([\d\.-]+) ([\d\.-]+) Z"'
replacement = r'd="M \1 \2 L \3 \4 L \7 \8 Z"'

for fp in files:
    with open(fp, "r") as f:
        content = f.read()

    # modify SVG mathematical paths for visual appearance
    content = re.sub(pattern, replacement, content)

    # modify draw.io styling logic for future editability
    content = content.replace("endArrow=classic", "endArrow=block")

    with open(fp, "w") as f:
        f.write(content)

print("Arrows updated to triangles!")
