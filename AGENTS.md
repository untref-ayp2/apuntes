# Directivas para Agentes de IA

## Regla crítica

**NUNCA hacer commit ni push sin autorización explícita del usuario.**
No abrir PRs sin autorización. Commits directamente a la rama de trabajo.
Siempre incluir todos los cambios en el commit, salvo indicación expresa.

## Guía de estilo

**Consultar `ESTILOS.md`** para todas las convenciones de formato MyST, figuras SVG,
admonitions, bloques de código, pseudocódigo, ejercicios, referencias cruzadas, citas y applets.
Es la fuente canónica. Lo que sigue es un resumen mínimo.

## Lineamientos generales

1. **Idioma**: español rioplatense
2. **Tono**: moderadamente formal, amigable pero serio
3. **Contenido**: en `contenidos/` — archivos `X-Y-tema.md`
4. **Dependencias**: solo librerías de `requirements.txt`
5. **Estáticos**: imágenes en `contenidos/_static/figures`, applets en `contenidos/_static/applets`
6. **Citas**: agregar a `contenidos/references.bib`

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
2. Pre-procesa .md (elimina `only-dark-mode` y `<div class="only-html">`, convierte `admonition` a `note`, `dropdown` a texto)
3. Genera Typst con `myst build --execute --typst`
4. Post-procesa `.typ` (reemplaza `arrow.r` por `->`, etc.)
5. Compila con `typst compile`
6. Mueve PDF a `contenidos/exports/apunte-ayp2.pdf`

**Importante:** `contenidos/exports/apunte-ayp2.pdf` se incluye siempre en los commits.

## Classroom50

Usamos [Classroom50](https://classroom50.org) (de la Fifty Foundation) para
gestionar asignaciones y entregas. Es una alternativa open-source a GitHub Classroom.

### Instalación

```bash
gh extension install foundation50/gh-teacher
gh extension install foundation50/gh-student
```

### Extensiones CLI

| Comando | Rol |
|---|---|
| `gh teacher` | Docente: init, classroom, roster, assignment, download |
| `gh student` | Alumno: accept, submit |

### Organizaciones (sedes)

| Sede | Org maestra (templates) | Org estudiantes |
|---|---|---|
| UNTREF | `untref-ayp2` | `untref-ayp2-estudiantes` |
| CUDI | `untref-ayp2` (compartida) | `cudi-ayp2-estudiantes` |

Flujo típico por sede:

```bash
gh teacher classroom add <org-estudiantes> <short-name> --name "<nombre>"
gh teacher roster add <org-estudiantes> <classroom> <username>
gh teacher assignment add <org-estudiantes> <classroom> <slug> --template untref-ayp2/<repo>
gh teacher download <org-estudiantes> <classroom> <slug>
```

Referencia completa en el [wiki de classroom50](https://github.com/foundation50/classroom50/wiki).

### Script de actualización

`scripts/actualizar_repos.fish` — fetch + pull de todos los repos del monorepo
(sirve tanto para UNTREF como para CUDI).

## Arquitectura de repositorios de apoyo

Los capítulos 3-x y 4-x usan un único repositorio en `github.com/untref-ayp2`,
`taller-tad`, que contiene tanto las implementaciones de estructuras como los
ejercicios de aplicación:

| Subdirectorio                | Uso del alumno                                      |
| ---------------------------- | --------------------------------------------------- |
| `data-structures/`           | Implementa las estructuras localmente               |
| `XX-tema/ejercicios/`        | Contiene esqueletos + tests                         |

### `go.mod replace`

```go
require github.com/untref-ayp2/data-structures v0.0.0
replace github.com/untref-ayp2/data-structures => ./data-structures
```

### Repositorios como fuente única de ejercicios

Los enunciados **NO** van inline en el apunte. Solo referenciar al repo:

```
Los ejercicios de este capítulo están en `XX-tema/ejercicios/`
del repositorio [taller-*](https://github.com/untref-ayp2/taller-*).
```

## Revisión de contenido

**Uso:** `/revisar-contenido @<archivo>`

Busca el archivo con `contenidos/**/*<archivo>*.md` y ejecuta la revisión
completa: ortografía, conceptos, formato MyST, recursos externos e imágenes.

### Capítulos comunes

| Parámetro | Archivo |
|---|---|
| `@intro` | `contenidos/introduccion.md` |
| `@1-3-analisis` | `contenidos/1-presentacion/1-3-analisis-de-algoritmos.md` |
| `@2-7-punteros` | `contenidos/2-taller-de-go/2-7-punteros.md` |
| `@3-9-abb` | `contenidos/3-estructuras-de-datos/3-9-abb.md` |
| `@4-4-backtracking` | `contenidos/4-diseno-de-algoritmos/4-4-backtracking.md` |
| `@5-1-git` | `contenidos/5-anexos/5-1-introduccion-git.md` |

Sin match exacto, el agente busca con glob `contenidos/**/*${archivo}*.md`.

### Formato del reporte

```markdown
## Reporte de revisión: <archivo>

### 🔤 Ortografía y gramática
### 🧠 Conceptos
### 📋 Formato MyST
### 🌐 Recursos externos
### 🖼️ Imágenes SVG
```

### Checklist de revisión

1. **Ortografía y gramática**: tildes, puntuación, concordancia, extranjerismos en cursiva, artículo "el" ante "*heap*"/"*stack*"
2. **Conceptos**: código Go compila, diagramas coherentes, consistencia interna
3. **Formato MyST**: `{admonition}` con `:class:`, `{code-block}`, pseudocódigo en mayúsculas con `←`, pares light/dark, `{ref}` no `{numref}`, `{cite}`, frontmatter con `label:`, applets en `<div class="only-html">`
4. **Recursos externos** (capítulos 3-x y 4-x): solo referencia a repos, verificar existencia en `github.com/untref-ayp2` o `github.com/cudi-ayp2`
5. **Imágenes SVG**: pares `_light.svg`/`_dark.svg`, clases CSS estándar, colores del theme
