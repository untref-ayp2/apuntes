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

---

## Comandos de Build, Lint y Test

### Instalación y formateo

```bash
make install          # pip install --requirement requirements.txt
make fmt              # formatea MD (mdformat)
```

Comandos individuales:

- `mdformat --number contenidos/**/*.md` - Markdown
- `jupyter-book build contenidos` - Compila el libro

### Build y desarrollo

```bash
make build    # compila el libro
make server   # servidor de desarrollo
make clean    # elimina archivos generados
```

---

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

---

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

| Elemento      | Convención   | Ejemplo          |
|---------------|--------------|------------------|
| Paquetes      | lowercase    | `stack`, `queue` |
| Funciones     | PascalCase   | `Push`, `Pop`    |
| Variables     | camelCase    | `nodeValue`      |
| Constantes    | Mayúsculas   | `MAX_SIZE`       |
| Interfaces    | er suffix    | `Reader`, `Stack`|

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

---

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

---

## Code Style Guidelines

### Markdown Content

- Escribir en español
- Usar ATX-style headers (`#`, `##`, `###`)
- Usar fenced code blocks con especificadores de lenguaje: ```go, ```python, etc.
- Habilitar números de línea en bloques de código cuando se demuestre ejecución paso a paso
- Usar admonitions para tips, advertencias y notas:
  ```markdown
  > [!TIP]
  > Tu contenido aquí
  ```

### Markdown Linting

El proyecto usa markdownlint y mdformat con estas reglas (`.markdownlint.json`):

- `default: true` - habilitar todas las reglas por defecto
- `line-length: false` - permitir líneas largas
- `no-inline-html: false` - permitir HTML inline
- `no-duplicate-heading.siblings_only: true` - permitir headings duplicados en diferentes secciones

### File Naming

- Archivos Markdown: `kebab-case` matching el número de sección, ej: `2-3-arreglos-slices.md`
- Paquetes Go: lowercase, ej: `stack`, `binarytree`
- Imágenes: nombres descriptivos en `contenidos/_images/`

### Directory Structure

```
/
├── AGENTS.md
├── Makefile
├── requirements.txt
├── README.md
├── .github/workflows/deploy.yml
├── contenidos/
│   ├── _config.yml          # Jupyter Book configuration
│   ├── _toc.yml             # Table of contents
│   ├── _static/             # Static files (code examples)
│   │   └── code/
│   │       └── go.mod       # Go module for examples
│   ├── _images/             # Diagrams and images
│   ├── _build/              # Generated HTML output
│   └── [chapters]/          # Markdown content files
```

### Git Conventions

- Commit messages en español
- Crear feature branches para cambios significativos
- PRs deben pasar el build antes de merge (CI corre `jupyter-book build`)

---

## Tareas Comunes

### Agregar un Nuevo Capítulo

1. Crear el archivo markdown en `contenidos/`
2. Agregar entrada a `contenidos/_toc.yml` bajo la sección apropiada
3. Agregar imágenes a `contenidos/_images/`
4. Build para verificar: `make build`

### Agregar Ejemplos de Código

1. Agregar archivos Go a `contenidos/_static/code/`
2. Usar fenced code blocks en markdown con ````go` o ````go:line-numbers`
3. Testear el código: `go test ./...` en ese directorio
