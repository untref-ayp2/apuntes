import re


def process_svg(filepath, mode):
    with open(filepath, "r") as f:
        text = f.read()

    # 1. Fonts
    text = re.sub(r'font-family="[^"]*"', 'font-family="ui-sans-serif, system-ui, sans-serif"', text)
    text = re.sub(r"font-family:[^;]*;", "font-family: ui-sans-serif, system-ui, sans-serif;", text)

    # 2. General replaces
    if mode == "light":
        text = text.replace('stroke="rgb(0,0,0)"', 'stroke="#333333"')
        text = text.replace('stroke="rgb(37,37,37)"', 'stroke="#333333"')
        text = text.replace('fill="rgb(0,0,0)"', 'fill="#333333"')
        text = text.replace('fill="rgb(37,37,37)"', 'fill="#333333"')

        text = text.replace('stroke="rgb(255,0,0)"', 'stroke="#e9967a"')
        text = text.replace('fill="rgb(255,0,0)"', 'fill="#ffe1e1"')

        text = text.replace('stroke="rgb(0,100,0)"', 'stroke="#8fbc8f"')
        text = text.replace('fill="rgb(0,100,0)"', 'fill="#e6f4ea"')

        text = text.replace('stroke="rgb(0,0,255)"', 'stroke="#4682b4"')
        text = text.replace('fill="rgb(0,0,255)"', 'fill="#e1f5ff"')

        text = text.replace('fill="#ffffff"', 'fill="none"')
        text = text.replace('fill="rgb(255,255,255)"', 'fill="none"')
        text = text.replace('stroke="rgb(255,255,255)"', 'stroke="none"')

    elif mode == "dark":
        text = text.replace('stroke="rgb(0,0,0)"', 'stroke="#e0e0e0"')
        text = text.replace('stroke="rgb(37,37,37)"', 'stroke="#e0e0e0"')
        text = text.replace('fill="rgb(0,0,0)"', 'fill="#e0e0e0"')
        text = text.replace('fill="rgb(37,37,37)"', 'fill="#e0e0e0"')

        text = text.replace('stroke="rgb(255,0,0)"', 'stroke="#fc8181"')
        text = text.replace('fill="rgb(255,0,0)"', 'fill="#fc8181"')

        text = text.replace('stroke="rgb(0,100,0)"', 'stroke="#68d391"')
        text = text.replace('fill="rgb(0,100,0)"', 'fill="#68d391"')

        text = text.replace('stroke="rgb(0,0,255)"', 'stroke="#63b3ed"')
        text = text.replace('fill="rgb(0,0,255)"', 'fill="#63b3ed"')

        text = text.replace('fill="#ffffff"', 'fill="none"')
        text = text.replace('fill="rgb(255,255,255)"', 'fill="none"')
        text = text.replace('stroke="rgb(255,255,255)"', 'stroke="none"')
        text = text.replace('stroke="rgb(192,192,192)"', 'stroke="#4a5568"')

    with open(filepath, "w") as f:
        f.write(text)


files_light = [
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/funcion_acotada_light.svg",
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/comparacion_funciones_light.svg",
]
files_dark = [
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/funcion_acotada_dark.svg",
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/comparacion_funciones_dark.svg",
]

for fp in files_light:
    process_svg(fp, "light")

for fp in files_dark:
    process_svg(fp, "dark")

print("Styling applied!")
