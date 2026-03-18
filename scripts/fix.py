import re

files = [
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/funcion_acotada_light.svg",
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/funcion_acotada_dark.svg",
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/comparacion_funciones_light.svg",
    "/home/martin/AyP2/apuntes/contenidos/_static/figures/comparacion_funciones_dark.svg",
]

for fp in files:
    try:
        with open(fp, "r") as f:
            text = f.read()

        # Draw.io buggy export sometimes adds fill="rgb(xxx)" right after fill="#xxx"
        text = re.sub(r'(fill="[^"]*"\s*)fill="rgb\([^)]+\)"', r"\1", text)

        with open(fp, "w") as f:
            f.write(text)
        print("Fixed", fp)
    except Exception as e:
        print("Error reading", fp, e)
