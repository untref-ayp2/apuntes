# Guía de Estilo — Apunte AyP2

Este documento es la fuente canónica de convenciones de estilo para el proyecto.
Cualquier agente o colaborador debe consultarlo antes de escribir o modificar contenido.

---

## 1. Estructura de capítulos

Cada capítulo es un archivo `X-Y-tema.md` en `contenidos/`. El frontmatter YAML es **obligatorio**
y debe incluir al menos el campo `label`, que se usa para referencias cruzadas con `{ref}`.

**Formato:**

```yaml
---
label: arreglos-slices
---
```

**Reglas:**

- Encoding: UTF-8
- Headers: ATX-style (`#`, `##`, `###`); no usar setext (`===`, `---`)
- Nombres de archivo: `kebab-case` con número de sección (ej. `2-5-arreglos-slices.md`)
- El `label` debe ser único y descriptivo en minúsculas con guiones (ej. `iteradores-abb`)

---

## 2. Admonitions

Usar **siempre** el formato `{admonition}` con `:class:`. El shorthand (`{note}`, `{warning}`, etc.)
**no funciona en mystmd**.

**Formato obligatorio:**

````markdown
```{admonition} Título
:class: note

Contenido aquí.
```
````

**NO usar** (no funciona en mystmd):

````markdown
```{note}
Contenido aquí.
```
````

**Clases disponibles:**

| Clase        | Uso típico                            |
| ------------ | ------------------------------------- |
| `note`       | Nota informativa o aclaración         |
| `hint`       | Sugerencia o pista                    |
| `important`  | Dato relevante que no debe pasarse    |
| `warning`    | Advertencia o precaución              |
| `tip`        | Consejo práctico                      |
| `caution`    | Peligro o riesgo                      |
| `dropdown`   | Contenido colapsable (solo HTML)      |

**Restricciones del build PDF** (`scripts/build_pdf.py`):

1. `{admonition}` se convierte automáticamente a `{note}` — todas las admonitions se ven iguales en PDF.
2. `{dropdown}` se aplana a texto: el título se vuelve un párrafo en negrita (`**Título**`) seguido del contenido.
3. Los bloques con `:class: only-dark-mode` se **eliminan completamente** del PDF.
4. Los bloques `<div class="only-html">...</div>` se **eliminan completamente** del PDF. Usar este wrapper para contenido que solo funciona en HTML (applets, videos).

---

## 3. Bloques de código

### Código fuente (Go)

Usar `{code-block}` con especificador de lenguaje. Incluir `:linenos:` para numeración.

````markdown
```{code-block} go
:linenos:

func main() {
    fmt.Println("Hola")
}
```
````

Siempre que sea posible, incluir `func main()` y la salida esperada en ```` ```output ````.

**Reglas:**

- `{code-file}` **no existe** en mystmd (era de Sphinx/JBv1). Usar `{code-block}` en su lugar.
- Líneas de código: máximo 80 columnas.
- Docstrings en español, formato Go estándar.

### Pseudocódigo

Usar `{code-block} text` con `:caption:` para pseudocódigo. Seguir este formato:

````markdown
```{code-block} text
:caption: Algoritmo de selección

FUNCION seleccion(arr)
    n ← LONGITUD(arr)
    PARA i ← 0 HASTA n-1 HACER
        minimo ← i
        PARA j ← i+1 HASTA n-1 HACER
            SI arr[j] < arr[minimo] ENTONCES
                minimo ← j
            FIN SI
        FIN PARA
        INTERCAMBIAR arr[i], arr[minimo]
    FIN PARA
    RETORNAR arr
FIN FUNCION
```
````

**Convenciones de pseudocódigo:**

| Elemento       | Sintaxis                                   |
| -------------- | ------------------------------------------ |
| Función        | `FUNCION` / `FIN FUNCION`                  |
| Condicional    | `SI` / `ENTONCES` / `SINO` / `FIN SI`      |
| Bucle mientras | `MIENTRAS` / `HACER` / `FIN MIENTRAS`      |
| Bucle para     | `PARA` / `HASTA` / `HACER` / `FIN PARA`    |
| Retorno        | `RETORNAR`                                 |
| Salida         | `SALIR`                                    |
| Y lógico       | `Y`                                        |
| Asignación     | `←` (U+2190)                               |
| Indentación    | 4 espacios                                 |

---

## 4. Figuras SVG

Cada diagrama requiere **dos archivos**: `_light.svg` y `_dark.svg`.
Ubicación: `contenidos/_static/figures/`.

### Incrustación en markdown

````markdown
```{figure} ../_static/figures/mi-diagrama_light.svg
:name: mi-diagrama-light
:class: only-light-mode

Descripción de la figura.
```

```{figure} ../_static/figures/mi-diagrama_dark.svg
:name: mi-diagrama-dark
:class: only-dark-mode

Descripción de la figura.
```
````

Usar `:class: only-dark-mode` y `:class: only-light-mode` (no `only-dark` ni `only-light`).

### Clases CSS estándar

| Clase            | Descripción                                  | text-anchor |
| ---------------- | -------------------------------------------- | ----------- |
| `.title`         | Título principal del diagrama (20px)         | `middle`    |
| `.code`          | Texto dentro de nodos (16px)                 | `middle`    |
| `.code-example`  | Ejemplos de código fuera de nodos (18px)     | `start`     |
| `.variable-node` | Nodos que representan variables (azul)       | —           |
| `.value-node`    | Nodos que representan valores/strings (rojo) | —           |
| `.arrow`         | Flechas/aristas entre nodos                  | —           |
| `.note`          | Notas explicativas en cursiva (14px)         | `middle`    |

**Clases para árboles:**

| Clase               | Descripción                                       |
| ------------------- | ------------------------------------------------- |
| `.edge`             | Arista entre nodos del árbol                      |
| `.tree-edge`        | Arista gruesa entre nodos (árbol genérico)        |
| `.op-node`          | Nodo de operación (+, −, *, etc.)                 |
| `.num-node`         | Nodo de número o valor                            |
| `.node-circle`      | Círculo de nodo en árbol binario                  |
| `.node-text`        | Texto dentro de nodos (monospace, 14px, bold)     |
| `.fb-label`         | Etiqueta de factor de balanceo (sans-serif, 12px) |
| `.fb-bal`           | Color verde para nodos balanceados (AVL)          |
| `.fb-unbal`         | Color rojo para nodos desbalanceados (AVL)        |

### Fuentes

- **Títulos** (`.title`): `ui-sans-serif, system-ui, sans-serif`
- **Código** (`.code`, `.code-example`, `.node-text`): `menlo, consola, 'DejaVu Sans Mono'`

### Paleta de colores — Light

| Elemento                     | Fill        | Stroke      | Stroke-width |
| ---------------------------- | ----------- | ----------- | ------------ |
| Fondo principal              | `#f0f2f5`   | —           | —            |
| Nodos azules (variables)     | `#e1f5ff`   | `#4682b4`   | 2            |
| Nodos rojos (valores)        | `#ffe1e1`   | `#e9967a`   | 2            |
| Nodos verdes                 | `#e1ffe1`   | `#2e8b57`   | 2            |
| Nodos naranjas               | `#fff4e1`   | `#f6ad55`   | 2            |
| Nodos morados                | `#f5e1ff`   | `#9f7aea`   | 2            |
| Texto y líneas               | —           | `#333333`   | 2            |
| Nodo árbol (ABB/AVL)         | `#e1f5ff`   | `#4682b4`   | 2.5          |
| Arista árbol                 | —           | `#333333`   | 2            |
| FB balanceado                | `#2e8b57`   | —           | —            |
| FB desbalanceado             | `#c53030`   | —           | —            |

### Paleta de colores — Dark

| Elemento                     | Fill        | Stroke      | Stroke-width |
| ---------------------------- | ----------- | ----------- | ------------ |
| Fondo principal              | `#1e1e1e`   | —           | —            |
| Nodos azules (variables)     | `#2d3748`   | `#63b3ed`   | 2            |
| Nodos rojos (valores)        | `#4a5568`   | `#fc8181`   | 2            |
| Nodos verdes                 | `#285e61`   | `#68d391`   | 2            |
| Nodos naranjas               | `#744210`   | `#f6ad55`   | 2            |
| Nodos morados                | `#44337a`   | `#b794f4`   | 2            |
| Texto y líneas               | —           | `#e0e0e0`   | 2            |
| Nodo árbol (ABB/AVL)         | `#2d3748`   | `#63b3ed`   | 2.5          |
| Arista árbol                 | —           | `#e0e0e0`   | 2            |
| FB balanceado                | `#68d391`   | —           | —            |
| FB desbalanceado             | `#fc8181`   | —           | —            |

### Grosores de línea

- **1px**: bordes punteados (`stroke-dasharray="5,5"`)
- **2px**: bordes de nodos estándar, aristas
- **2.5px**: círculos de nodos en árboles (ABB/AVL)

### Convenciones para árboles binarios de búsqueda (ABB/AVL)

- ViewBox por defecto: `0 0 700 360` para árboles de 5 niveles
- Radio de nodo: `r="18"`
- Texto interior: monospace 14px bold, centrado vertical y horizontal
- Separación vertical entre niveles: decreciente (70→65→60→55px)
- Las etiquetas de factor de balanceo van a la derecha del nodo (`x="cx + r + 6"`)
- Si la etiqueta derecha se superpone con otro nodo, va a la izquierda (`x="cx - r - 6"` con `text-anchor: end`)

### Restricción del build PDF

- El build PDF solo incluye los SVG `_light` (los `_dark` se descartan con los bloques `only-dark-mode`).
- El script `build_pdf.py` limpia atributos `font-family` de los SVG para compatibilidad con Typst/resvg.

---

## 5. Ejercicios

Los enunciados **NO** van inline en el apunte. Solo se referencia el directorio del repositorio
correspondiente.

**Formato para capítulos 2-x (taller-go):**

```markdown
## Ejercicios

Los ejercicios de este capítulo están en `05-arreglos-slices/ejercicios/`
del repositorio [taller-go](https://github.com/untref-ayp2/taller-go.git).
```

**Formato para capítulos 3-x y 4-x (taller-tad, data-structures):**

```markdown
## Ejercicios

Los ejercicios de este capítulo están en `03-listas/ejercicios/`
del repositorio [taller-tad](https://github.com/untref-ayp2/taller-tad).
Antes de comenzar, implementá las interfaces necesarias en tu fork de
[data-structures](https://github.com/untref-ayp2/data-structures).
```

**Labels de ejercicios** (cuando se use el directive `{exercise}`):

- Formato: `ej-{seccion}-{numero}`
- Ejemplo: `ej-pilas-1`, `ej-arboles-3`
- Las soluciones usan labels correspondientes: `sol-ej-pilas-1`

**Cuando se usan listas planas** sin `{exercise}`/`{solution}`, los labels no son necesarios.

---

## 6. Referencias cruzadas

Usar **`{ref}`** (por título), **nunca** `{numref}` (por número).
Las referencias por número se rompen si se reordenan los capítulos.

```markdown
{ref}`arboles`
{ref}`arboles-binarios-de-busqueda`
```

El `label` de cada capítulo está en el frontmatter (archivo `X-Y-tema.md`, línea 2).
El texto visible de la referencia es el título del capítulo destino (`# Título`).

---

## 7. Citas

Formato `{cite}` con clave de `contenidos/references.bib`.

```markdown
{cite}`knuth1997`
{cite}`cormen2022`
```

Las entradas se agregan a `contenidos/references.bib` en formato BibTeX estándar.

---

## 8. Applets

Los applets son archivos HTML/JS autocontenidos (sin dependencias externas).
Ubicación: `contenidos/_static/applets/`, con subdirectorio por capítulo.

### Estructura de archivos

```
contenidos/_static/applets/
├── 3-estructuras-de-datos/
│   └── 3-8-arboles/
│       ├── recorridos-arbol-preorden_light.html
│       ├── recorridos-arbol-preorden_dark.html
│       ├── recorridos-arbol-inorden_light.html
│       ├── recorridos-arbol-inorden_dark.html
│       ├── recorridos-arbol-postorden_light.html
│       └── recorridos-arbol-postorden_dark.html
└── ...
```

Cada applet requiere dos archivos: `_light.html` y `_dark.html` con colores fijos (no `@media`).
Los iframes no heredan el tema del sitio padre.

### Incrustación en markdown

Los applets solo se renderizan en HTML, no en PDF. Por eso **todo el bloque de iframes
debe envolverse en `<div class="only-html">`** para que el build PDF lo elimine completamente
(vía `strip_only_html_blocks()`).

````markdown
<div class="only-html">

```{iframe} /applets/3-estructuras-de-datos/3-8-arboles/recorridos-arbol-preorden_light.html
:width: 100%
:height: 560px
:class: only-light-mode
```

```{iframe} /applets/3-estructuras-de-datos/3-8-arboles/recorridos-arbol-preorden_dark.html
:width: 100%
:height: 560px
:class: only-dark-mode
```

</div>
````

La ruta del `{iframe}` es absoluta desde la raíz del sitio (`/applets/...`).
No usar query strings para parametrizar el applet.

### `myst.yml`

```yaml
project:
  static_files:
    - _static/applets
```

### Altura del iframe

Usar `:height: 560px` como valor base, ajustable ±30px según el contenido del applet.

### Restricción del build PDF

- El wrapper `<div class="only-html">` elimina todo el bloque de iframes del PDF.
- No se usa `:placeholder:` — los PNG placeholder se ven mal en PDF. El texto
  circundante y las fórmulas LaTeX deben ser suficientes para entender el concepto
  sin el applet.

---

## 9. Convenciones generales

### Markdown

- ATX-style headers (`#`, `##`, `###`)
- Fenced code blocks con especificador de lenguaje
- `mdformat --number` para formateo automático con numeración de líneas

### Ortografía

- Extranjerismos en cursiva: `*struct*`, `*slice*`, `*interface*`
- "Go" va en mayúscula sin cursiva
- Español rioplatense; tildes correctas, concordancia género/número
- Artículo "el" ante "*heap*" y "*stack*": «el *heap*», «el *stack*»

### File naming

- Markdown: `kebab-case` con número de sección (`2-5-arreglos-slices.md`)
- Paquetes Go: lowercase (`stack`, `queue`)
- Imágenes: nombres descriptivos en `contenidos/_static/figures/`

### Citas y referencias

- `{cite}` para bibliografía (clave de `references.bib`)
- `{ref}` para referencias cruzadas entre capítulos (no `{numref}`)

---

## Referencias rápidas

| Qué                             | Usar                                    | NO usar                             |
| ------------------------------- | --------------------------------------- | ----------------------------------- |
| Admonition                      | `{admonition}` con `:class: note`       | `{note}` (shorthand)                |
| Código fuente                   | `{code-block} go` con `:linenos:`       | `{code-file}`                       |
| Pseudocódigo                    | `{code-block} text` con `:caption:`     | `{prf:algorithm}`                   |
| Figura light/dark               | `{figure}` con `:class: only-light-mode` / `only-dark-mode` | Una sola figura sin par |
| Referencia entre capítulos      | `{ref}``\`label\``                      | `{numref}``\`label\``               |
| Cita bibliográfica              | `{cite}``\`clave\``                     | `[@clave]`                          |
| Label de ejercicio              | `ej-{seccion}-{numero}`                 | Números sueltos sin prefijo         |
| Applet light/dark               | `{iframe}` con `:class: only-light-mode` / `only-dark-mode` envuelto en `<div class="only-html">` | Un solo iframe sin par ni wrapper |
