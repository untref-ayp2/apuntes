# Directivas para Agentes de IA

## Regla crítica

**NUNCA hacer commit ni push sin autorización explícita del usuario.**
No abrir PRs sin autorización. Commits directamente a la rama de trabajo.

## Lineamientos generales

1. **Idioma**: español rioplatense
2. **Tono**: moderadamente formal, amigable pero serio
3. **Sintaxis**: MyST (Mark-up Your Structured Text)
4. **Contenido**: en `contenidos/` — archivos `X-Y-tema.md`
5. **Dependencias**: solo librerías de `requirements.txt`
6. **Estáticos**: imágenes en `contenidos/_static/figures`
7. **Citas**: agregar a `contenidos/references.bib`

## Comandos

```
make install   # pip install --requirement requirements.txt
make fmt       # mdformat --number + black --line-length 120
make build     # HTML + PDF (limpia y reconstruye)
make pdf       # PDF vía scripts/build_pdf.py
make start     # servidor de desarrollo MyST
make clean     # elimina build artifacts
```

## Build PDF

`scripts/build_pdf.py`:

1. Copia `contenidos/` a directorio temporal
2. Pre-procesa .md (elimina `only-dark-mode`, convierte `dropdown` a texto, `admonition` a `note`)
3. Genera Typst con `myst build --execute --typst`
4. Post-procesa `.typ` (reemplaza `arrow.r` por `->`, etc.)
5. Compila con `typst compile`
6. Mueve PDF a `contenidos/exports/apunte-ayp2.pdf`

**Importante:** `contenidos/exports/apunte-ayp2.pdf` se incluye siempre en los commits (no es un artifact descartable).

## MyST y contenido

### Frontmatter

```yaml
---
file: ruta/al/archivo.md
---
```

### Citas

```markdown
{cite}`referencia_bibtex`
```

### Bloques de código

````markdown
```{code-block} go
:linenos:

func ejemplo() error {
    return nil
}
```
````

Siempre que sea posible incluir `func main()` y la salida esperada en ```` ```output ````.

### Ejercicios y soluciones

Labels con formato `ej-{seccion}-{numero}`. Ejercicios numerados como listas planas son aceptables si no tienen solución asociada.

```{exercise}
---
label: ej-pilas-1
---
Enunciado aquí.
```

```{solution}
---
label: sol-ej-pilas-1
---
func respuesta() error {
    return nil
}
```

### Imágenes modo claro/oscuro

Dos archivos: `_light.svg` y `_dark.svg`. Ver skill `diagramas-svg` en `.opencode/skills/diagramas-svg/SKILL.md`.

```{figure} ../_static/figures/mi-diagrama_light.svg
---
class: only-light-mode
---
Mi Diagrama
```

```{figure} ../_static/figures/mi-diagrama_dark.svg
---
class: only-dark-mode
---
Mi Diagrama
```

### Admonitions

```{admonition} Título
---
class: note
---
Tu contenido aquí
```

Clases: `note`, `hint`, `important`, `warning`, `tip`, `caution`, `dropdown`.

### `{code-file}` no disponible

`{code-file}` era de Sphinx (JBv1). En mystmd **no funciona**. Usar `{code-block}` inline con link al archivo en GitHub.

### Referencias cruzadas entre capítulos

Usar `{ref}` (por el título) en lugar de `{numref}` (por el número), para que las referencias no se rompan si se reordenan los capítulos:

```markdown
{ref}`arboles`
{ref}`arboles-binarios-de-busqueda`
```

El `label` de cada capítulo está en su frontmatter (archivo `X-Y-tema.md` línea 2).

## Convenciones

### Ortografía

- Extranjerismos (*struct*, *slice*, *interface*) en cursiva con `*palabra*`
- "Go" va en mayúscula sin cursiva
- Tildes correctas, concordancia género/número

### Estilo Go

- Docstrings en español, formato Go estándar
- Line length: 100 caracteres
- Encoding: UTF-8

### Markdown

- ATX-style headers (`#`, `##`, `###`)
- Fenced code blocks con especificador de lenguaje
- Líneas de código en `{code-block}`: máximo 80 columnas
- `mdformat --number` habilita numeración de líneas

### File naming

- Markdown: `kebab-case` con número de sección, ej: `2-3-arreglos-slices.md`
- Paquetes Go: lowercase (`stack`, `queue`)
- Imágenes: nombres descriptivos en `contenidos/_static/figures/`

## Arquitectura de repositorios de apoyo

Los capítulos 3-x y 4-x usan dos tipos de repositorios en `github.com/untref-ayp2`:

| Tipo      | Ejemplo                       | Uso del alumno                            |
| --------- | ----------------------------- | ----------------------------------------- |
| Contratos | `data-structures`             | Forkea, implementa interfaces localmente  |
| Talleres  | `taller-*` (ej: `taller-tad`) | Clona o fork, contiene esqueletos + tests |

### `go.mod replace`

```go
require github.com/untref-ayp2/data-structures v0.0.0
replace github.com/untref-ayp2/data-structures => ../data-structures
```

### Repositorios como fuente única de ejercicios

Los enunciados **NO** van inline en el apunte. Solo referenciar al repo:

```
Los ejercicios de este capítulo están en `XX-tema/ejercicios/`
del repositorio [taller-*](https://github.com/untref-ayp2/taller-*).
```
