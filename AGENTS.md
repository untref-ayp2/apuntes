# Directivas para Agentes de IA

Este documento contiene las directivas para agentes que colaboren en este proyecto.

## Regla Crítica

**NUNCA hacer commit ni push sin autorización explícita del usuario.**
Esperar a que el usuario diga "commiteá", "hacé commit" o "pusheá".

## Lineamientos Generales

1. **Idioma**: Español rioplatense
2. **Tono**: Moderadamente formal, amigable pero serio
3. **Sintaxis**: MyST (Mark-up Your Structured Text)
4. **Estructura**: Contenido en `contenidos/`, archivos con formato `X-Y-tema.md`
5. **Dependencias**: Solo librerías de `requirements.txt`
6. **Estáticos**: Imágenes en `contenidos/_static/figures`
7. **Citas**: Agregar a `contenidos/references.bib` y usar sintaxis MyST

______________________________________________________________________

## Comandos de Build, Lint y Test

### Instalación y formateo

```bash
make install          # pip install --requirement requirements.txt
make fmt              # formatea MD y Python (mdformat + black)
```

Comandos individuales:

- `mdformat --number contenidos/**/*.md` - Markdown
- `black --line-length 120 .` - Python

### Build y desarrollo

```bash
make build    # compila el libro (HTML + PDF)
make pdf      # genera PDF con pre-procesamiento (scripts/build_pdf.py)
make start    # inicia servidor de desarrollo
make clean    # elimina archivos generados por compilación
```

### Build PDF

El PDF se genera mediante `scripts/build_pdf.py` que:

1. Copia `contenidos/` a un directorio temporal
2. Pre-procesa los archivos .md (elimina bloques `only-dark-mode`, convierte `dropdown` a texto, `admonition` a `note`)
3. Genera Typst con `myst build --execute --typst`
4. Post-procesa los `.typ` (reemplaza `arrow.r` por `->`, etc.)
5. Compila con `typst compile`
6. Mueve el PDF a `contenidos/exports/apunte-ayp2.pdf`

______________________________________________________________________

## Testing

Este proyecto contiene código Go embebido con archivos de test en `contenidos/_static/code/`. Para ejecutar los tests de Go:

```sh
# Run all tests in a directory
cd contenidos/_static/code && go test ./...

# Run a single test file
go test -v -run TestFunctionName ./package/path
```

### Ejemplo de un Test

```sh
go test -v -run TestStackPush ./stack
```

### Cobertura

```sh
# Cobertura global
go test -cover ./...

# Cobertura con perfil detallado
go test -v -coverprofile=coverage.out ./package/path
go tool cover -html=coverage.out
```

______________________________________________________________________

## Convenciones de Código Go

### Estilo General

- **Line length**: 100 caracteres
- **Docstrings**: En español, formato estándar de Go
- **Encoding**: UTF-8

### Imports (ordenar con líneas en blanco)

```go
import (
    "fmt"
    "errors"

    "golang.org/x/example/stringutil"
)
```

### Convenciones de Nombres

| Elemento   | Convención | Ejemplo           |
| ---------- | ---------- | ----------------- |
| Paquetes   | lowercase  | `stack`, `queue`  |
| Funciones  | PascalCase | `Push`, `Pop`     |
| Variables  | camelCase  | `nodeValue`       |
| Constantes | Mayúsculas | `MAX_SIZE`        |
| Interfaces | er suffix  | `Reader`, `Stack` |

### Manejo de Errores

- Retornar errores explícitos (`error`)
- Mensajes en español, claros y concisos

```go
// Correcto
if s.isEmpty() {
    return "", errors.New("pop from empty stack")
}
```

### Métodos

Incluir siempre `String()` para debugging cuando sea necesario.

```go
func (s Stack) String() string {
    return fmt.Sprintf("Stack(%v)", s.items)
}
```

### Estructura de Archivos

1. Package declaration
2. Imports
3. Constantes
4. Tipos
5. Funciones exportadas (con docstrings)
6. Funciones no exportadas

______________________________________________________________________

## MyST y Contenido

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

### Bloques de Código

````markdown
```{code-block} go
:linenos:

func ejemplo() error {
    return nil
}
```
````

Siempre que sea posible, los bloques de código deben incluir un `func main()` y la salida esperada debe mostrarse en un bloque ` ```output ` inmediatamente después del bloque de código.

````markdown
```go
func main() {
    fmt.Println("hola")
}
```
```output
hola
```
````

### Inclusion de archivos de código

Para incluir archivos de código fuente:

````markdown
```{code-file} ../_static/code/mipackage/mifile.go
:language: go
:linenos: true
:lineno-match: true
```
````

### Ejercicios y Soluciones

Usar labels con formato `ej-{seccion}-{numero}` (ej. `ej-pilas-1`, `ej-abb-orden`).

Los ejercicios numerados como **listas planas** son aceptables y preferibles cuando no tienen soluciones asociadas. No es necesario convertirlos a `{exercise}` directives a menos que tengan una `{solution}` correspondiente.

````markdown
```{exercise}
:label: ej-pilas-1

Enunciado aquí.
```

```{solution}
:label: sol-ej-pilas-1

func respuesta() error {
    return nil
}
```
````

### Imágenes Modo Claro/Oscuro

Para soportar ambos temas, crear dos versiones de cada imagen SVG:

- `_light.svg` para modo claro
- `_dark.svg` para modo oscuro

Para las guías detalladas de estilo (colores, tipografía, flechas, grosores),
consultar el skill `diagramas-svg` en `.opencode/skills/diagramas-svg/SKILL.md`.

Y usarlas así:

````markdown
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
````

______________________________________________________________________

## Code Style Guidelines

### Ortografía y gramática

- Extranjerismos (palabras en inglés como *struct*, *slice*, *interface*) deben ir en cursiva con `*palabra*`
- Excepción: "Go" va en mayúscula sin cursiva
- Tildes correctas, puntuación adecuada, concordancia género/número
- Español rioplatense

### Markdown Content

- Escribir en español
- Usar ATX-style headers (`#`, `##`, `###`)
- Usar fenced code blocks con especificadores de lenguaje: `go`, `python`, etc.
- Habilitar números de línea en bloques de código cuando se demuestre ejecución paso a paso
- Líneas de código en `{code-block}` y `{code-file}`: máximo 80 columnas
- Usar admonitions con el formato unificado `{admonition}` + `class:`:
  ```markdown
  ```{admonition} Título
  ---
  class: note
  ---
  Tu contenido aquí
  ```
  ```
  Clases disponibles: `note`, `hint`, `important`, `warning`, `tip`, `caution`, `dropdown`.

### Markdown Linting

El proyecto usa markdownlint y mdformat:

- `mdformat --number` - Habilita números de línea
- Permitir líneas largas
- `black --line-length 120` - Python

### File Naming

- Archivos Markdown: `kebab-case` matching el número de sección, ej: `2-3-arreglos-slices.md`
- Paquetes Go: lowercase, ej: `stack`, `binarytree`
- Imágenes: nombres descriptivos en `contenidos/_static/figures/`

### Directory Structure

```text
/
├── AGENTS.md
├── Makefile
├── requirements.txt
├── README.md
├── .github/workflows/deploy.yml
├── .opencode/
│   └── skills/
│       └── diagramas-svg/SKILL.md
├── scripts/
│   └── build_pdf.py            # Generación de PDF con pre-procesamiento
├── contenidos/
│   ├── myst.yml                # Configuración MyST
│   ├── _static/
│   │   ├── figures/            # Imágenes y diagramas
│   │   ├── code/               # Código fuente Go
│   │   ├── css/custom.css      # Estilos personalizados
│   │   └── js/custom.js        # Scripts personalizados
│   ├── references.bib
│   └── [capítulos]/            # Archivos markdown
```

### Git Conventions

- **Commits**: Mensajes en español, idealmente con prefijos semánticos
  (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`)
- **Ramas**: Trabajar en `jb2-martin` para cambios de migración
- **PRs**: Apuntar a `main` y deben pasar el build antes de merge
- **Licencia**: `CC-BY-SA-4.0`

______________________________________________________________________

## Tareas Comunes

### Agregar un Nuevo Capítulo

1. Crear el archivo `X-Y-tema.md` en `contenidos/` (numeración coherente con existentes)
2. Agregar entrada a `contenidos/myst.yml` bajo `project.toc` respetando el orden
3. Agregar imágenes a `contenidos/_static/figures/`
4. Build para verificar: `make build`

### Agregar Ejemplos de Código

1. Agregar archivos Go a `contenidos/_static/code/`
2. Usar fenced code blocks en markdown con \`\`\`\`go`o`code-file\` para incluir archivos
3. Testear el código: `go test ./...` en ese directorio

______________________________________________________________________

## Build System

Este proyecto usa **MyST** (mystmd) en lugar de Jupyter Book v1.

### Diferencias principales con Jupyter Book v1

| Aspecto  | JBv1                       | MyST (JBv2)          |
| -------- | -------------------------- | -------------------- |
| Config   | `_config.yml` + `_toc.yml` | `myst.yml`           |
| Build    | `jupyter-book build`       | `myst build`         |
| PDF      | LaTeX                      | Typst                |
| Imágenes | Una versión                | Versiones light/dark |

### Dependencias

- `mystmd` - Build system
- `typst` - Compilador PDF
- `mdformat` - Formateador Markdown
- `templates/plain_latex_book` - Template PDF (definido en `myst.yml`)

______________________________________________________________________

## Arquitectura de Repositorios de Apoyo (definido 2026-05-17)

Los capítulos 3-x y 4-x usan dos tipos de repositorios en `github.com/untref-ayp2`:

| Tipo | Repositorio | Uso del alumno | Contenido |
|---|---|---|---|
| Contratos | `data-structures` | Forkea, implementa interfaces localmente | Interfaces + tests. Sin implementaciones. |
| Talleres | `taller-*` (ej: `taller-tad`) | Clona o fork | `NN-tema/ejemplos/` y `NN-tema/ejercicios/` con esqueletos y tests. |

### Mecanismo de dependencia

El `go.mod` de cada `taller-*` declara un `replace` para apuntar al fork local de
`data-structures`:

```go
require github.com/untref-ayp2/data-structures v0.0.0

replace github.com/untref-ayp2/data-structures => ../data-structures
```
Esto permite que el alumno implemente las interfaces en su fork y los ejercicios del
taller consuman su propia implementación.

### Repositorios como fuente única de ejercicios

Los enunciados y detalles de los ejercicios **NO** deben ir inline en el apunte.
El apunte solo debe contener:

```markdown
## Ejercicios

Los ejercicios de este capítulo están en `XX-tema/ejercicios/`
del repositorio [taller-*](https://github.com/untref-ayp2/taller-*).
Cada directorio contiene un `README.md` con el enunciado y los esqueletos
para resolverlo.
```

Sin tablas, sin listas de ejercicios, sin descripciones. Todo va en el `README.md`
del repo. Así se puede agregar, modificar o sacar ejercicios sin tocar el apunte.

### `{code-file}` no soportado

`{code-file}` era una directiva de Sphinx (JBv1). En mystmd **no está disponible**.
Para incluir código de repos externos en el apunte, usar `{code-block}` inline y
agregar una admonition con link al archivo en GitHub.

### Repositorios archivados

- `data-structures-old` — anterior repo de estructuras, archivado
- `examples`, `snippets`, `guia-*` — históricos, solo como referencia

______________________________________________________________________

## Normas del Proyecto

- **NO abrir PRs** sin autorización expresa del usuario
- **NO commitear ni pushear** sin autorización expresa del usuario. Esperar a que el usuario indique explícitamente "commiteá", "hacé commit" o "pusheá".
- Los commits se hacen directamente a la rama de trabajo
- Solo crear PR cuando el trabajo esté completo y el usuario lo solicite
