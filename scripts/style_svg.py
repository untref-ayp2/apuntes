import re
import sys


def process_svg(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # 1. Remove all style="fill: light-dark(...)" etc to prevent conflicts
    content = re.sub(r'style="[^"]*light-dark[^"]*"', "", content)

    # 2. Font family to UI sans
    content = content.replace('font-family="Hack"', 'font-family="ui-sans-serif, system-ui, sans-serif"')
    content = content.replace('font-family="Jetbrains Mono"', 'font-family="ui-sans-serif, system-ui, sans-serif"')
    content = content.replace('font-family="&quot;Hack&quot;"', 'font-family="ui-sans-serif, system-ui, sans-serif"')
    content = content.replace(
        'font-family="&quot;Jetbrains Mono&quot;"', 'font-family="ui-sans-serif, system-ui, sans-serif"'
    )

    # 3. Stack rect (data-cell-id="157") -> make it pastel blue or none?
    # Actually wait. The task says "Eliminar el relleno del sector de la derecha" (Heap).
    content = re.sub(r'(<g data-cell-id="156">.*?)fill="#fff2cc"(.*?/>)', r'\1fill="none"\2', content)
    content = re.sub(r'(<g data-cell-id="156">.*?)stroke="#d6b656"(.*?/>)', r'\1stroke="none"\2', content)

    # 4. Right side objects (Direccion, Persona):
    # They have fill="#ffffff" stroke="#333333". We want pastel blue: fill="#e1f5ff" stroke="#4682b4"
    # Left side variables also have fill="#ffffff" or fill="none".
    # User says: "En los rectangulos que representan los objetios usar colores pasteles (preferiblmemente en la gama de los celestes)"
    # Rectangles that represent objects: data-cell-id="142" (Direccion), 147 (Direccion, red), 126 (Persona), 140 (Direccion), 135 (Direccion), 122 (Persona), 132 (Persona)
    # Actually, all rects that have fill="#ffffff" stroke="#333333" can be turned to pastel blue, except the variables on the left?
    # "reemplazar los colores de relleno oscuro." -> wait, is there any dark fill? Maybe "#333333" or "#121212"?

    with open(filepath, "w") as f:
        f.write(content)


process_svg("/home/martin/AyP2/apuntes/contenidos/_static/figures/MapaDeMemoria_light.svg")
