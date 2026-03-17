# Directivas para Agentes de IA

Este documento contiene las directivas para agentes que colaboren en este proyecto.

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
make fmt              # formatea MD (mdformat)
```

Comandos individuales:

- `mdformat --number contenidos/**/*.md` - Markdown
- `jupyter-book build contenidos` - Compila el libro (deprecated, usar myst)

### Build y desarrollo

```bash
make build    # compila el libro (HTML + PDF)
make pdf      # compila solo el PDF
make server   # servidor de desarrollo
make clean    # elimina archivos generados
```

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

````markdown
```{exercise}
:label: ejercicio-1

Enunciado aquí.
```

```{solution}
:label: solucion-1

func respuesta() error {
    return nil
}
```
````

### Imágenes Modo Claro/Oscuro

Para soportar ambos temas, crear dos versiones de cada imagen SVG:

- `_light.svg` para modo claro
- `_dark.svg` para modo oscuro

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

### Markdown Content

- Escribir en español
- Usar ATX-style headers (`#`, `##`, `###`)
- Usar fenced code blocks con especificadores de lenguaje: `go, `python, etc.
- Habilitar números de línea en bloques de código cuando se demuestre ejecución paso a paso
- Usar admonitions para tips, advertencias y notas:
  ````markdown
  ```{note}
  Tu contenido aquí
  ````
  ```

  ```

### Markdown Linting

El proyecto usa markdownlint y mdformat:

- `mdformat --number` - Habilita números de línea
- Permitir líneas largas

### File Naming

- Archivos Markdown: `kebab-case` matching el número de sección, ej: `2-3-arreglos-slices.md`
- Paquetes Go: lowercase, ej: `stack`, `binarytree`
- Imágenes: nombres descriptivos en `contenidos/_static/figures/`

### Directory Structure

```
/
├── AGENTS.md
├── Makefile
├── requirements.txt
├── README.md
├── .github/workflows/deploy.yml
├── scripts/
│   └── build_pdf.py
├── contenidos/
│   ├── myst.yml              # MyST configuration (reemplaza _config.yml y _toc.yml)
│   ├── _static/
│   │   ├── figures/          # Imágenes y diagramas
│   │   ├── code/            # Código fuente Go
│   │   ├── css/custom.css   # Estilos personalizados
│   │   └── js/custom.js     # Scripts personalizados
│   ├── references.bib
│   └── [chapters]/           # Archivos markdown
```

### Git Conventions

- Commit messages en español
- Trabajar en la rama `jb2-martin` para cambios de migración
- PRs deben pasar el build antes de merge

______________________________________________________________________

## Tareas Comunes

### Agregar un Nuevo Capítulo

1. Crear el archivo markdown en `contenidos/`
2. Agregar entrada a `contenidos/myst.yml` bajo la sección `project.toc`
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

______________________________________________________________________

## Normas del Proyecto

- **NO abrir PRs** sin autorización expresa del usuario
- Los commits se hacen directamente a la rama de trabajo
- Solo crear PR cuando el trabajo esté completo y el usuario lo solicite
