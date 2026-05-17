---
description: Revisa ortografía, gramática, conceptos, imágenes SVG y recursos externos de GitHub de un capítulo del apunte AyP2
---

# /revisar-contenido

Revisa un capítulo del apunte AyP2 en **modo plan**: solo muestra sugerencias, NUNCA modifica archivos ni ejecuta builds.

**Uso:** `/revisar-contenido [capítulo]` donde `[capítulo]` puede ser el número de sección (ej: `1-3`, `2-6`), un nombre corto (ej: `punteros`, `abb`) o el nombre del archivo. Si se omite el argumento, se detecta automáticamente el próximo capítulo pendiente.

## Detección automática del próximo capítulo

Si no se pasa argumento, determinar el archivo a revisar así:

1. Leer `.opencode/Plan-Migracion.md`
2. Ubicar la tabla "Prioridad Alta — Revisión de Contenido"
3. Buscar el primer capítulo con estado `⬜ Pendiente`
4. Usar ese archivo como objetivo de la revisión
5. Si todos están revisados, informar que no hay pendientes y terminar

## Resolución del capítulo

Usar esta tabla para determinar el archivo a revisar según el argumento (si se especificó):

| Si dice... | Archivo |
|---|---|
| `intro` o `introduccion` | `contenidos/introduccion.md` |
| `1-1` o `1-1-intro` | `contenidos/1-presentacion/1-1-introduccion.md` |
| `1-2` o `1-2-memoria` | `contenidos/1-presentacion/1-2-memoria.md` |
| `1-3` o `1-3-analisis` | `contenidos/1-presentacion/1-3-analisis-de-algoritmos.md` |
| `2-1` o `2-1-intro-go` | `contenidos/2-taller-de-go/2-1-introduccion-go.md` |
| `2-2` o `2-2-paquetes` | `contenidos/2-taller-de-go/2-2-paquetes-y-modulos.md` |
| `2-3` o `2-3-elementos` | `contenidos/2-taller-de-go/2-3-elementos-basicos.md` |
| `2-4` o `2-4-funciones` | `contenidos/2-taller-de-go/2-4-funciones.md` |
| `2-5` o `2-5-arreglos` | `contenidos/2-taller-de-go/2-5-arreglos-slices.md` |
| `2-6` o `2-6-maps` | `contenidos/2-taller-de-go/2-6-maps.md` |
| `2-7` o `2-7-punteros` | `contenidos/2-taller-de-go/2-7-punteros.md` |
| `2-8` o `2-8-structs` | `contenidos/2-taller-de-go/2-8-structs-interfaces.md` |
| `2-9` o `2-9-archivos` | `contenidos/2-taller-de-go/2-9-archivos.md` |
| `2-10` o `2-10-errores` | `contenidos/2-taller-de-go/2-10-errores.md` |
| `2-11` o `2-11-oop` | `contenidos/2-taller-de-go/2-11-oop.md` |
| `3-1` o `3-1-tad` | `contenidos/3-estructuras-de-datos/3-1-tad.md` |
| `3-2` o `3-2-pilas` | `contenidos/3-estructuras-de-datos/3-2-pilas-colas.md` |
| `3-3` o `3-3-listas` | `contenidos/3-estructuras-de-datos/3-3-listas.md` |
| `3-4` o `3-4-conjuntos` | `contenidos/3-estructuras-de-datos/3-4-conjuntos.md` |
| `3-5` o `3-5-mapa-bits` | `contenidos/3-estructuras-de-datos/3-5-mapa-de-bits.md` |
| `3-6` o `3-6-hashing` | `contenidos/3-estructuras-de-datos/3-6-tablas-de-hashing.md` |
| `3-7` o `3-7-diccionarios` | `contenidos/3-estructuras-de-datos/3-7-diccionarios.md` |
| `3-8` o `3-8-arboles` | `contenidos/3-estructuras-de-datos/3-8-arboles.md` |
| `3-9` o `3-9-abb` | `contenidos/3-estructuras-de-datos/3-9-abb.md` |
| `3-10` o `3-10-balanceados` | `contenidos/3-estructuras-de-datos/3-10-arboles-balanceados.md` |
| `3-11` o `3-11-heap` | `contenidos/3-estructuras-de-datos/3-11-monticulo-binario.md` |
| `3-12` o `3-12-iteradores` | `contenidos/3-estructuras-de-datos/3-12-iteradores-abb.md` |
| `4-1` o `4-1-recursividad` | `contenidos/4-diseno-de-algoritmos/4-1-recursividad.md` |
| `4-2` o `4-2-patrones` | `contenidos/4-diseno-de-algoritmos/4-2-patrones-de-diseno.md` |
| `4-3` o `4-3-avidos` | `contenidos/4-diseno-de-algoritmos/4-3-algoritmos-avidos.md` |
| `4-4` o `4-4-backtracking` | `contenidos/4-diseno-de-algoritmos/4-4-backtracking.md` |
| `4-5` o `4-5-programacion-dinamica` | `contenidos/4-diseno-de-algoritmos/4-5-programacion-dinamica.md` |
| `4-6` o `4-6-ordenamientos-rec` | `contenidos/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos.md` |
| `4-7` o `4-7-ordenamientos-lineales` | `contenidos/4-diseno-de-algoritmos/4-7-ordenamientos-lineales.md` |
| `5-1` o `5-1-git` | `contenidos/5-taller-de-git/5-1-introduccion-git.md` |
| `biblio` o `bibliografia` | `contenidos/bibliografia.md` |

Sin match exacto, buscar con `contenidos/**/*${termino}*.md`.

## Proceso de revisión

### 1. Leer el archivo completo

### 2. Revisión ortográfica y gramatical

- Tildes faltantes o incorrectas
- Puntuación mal usada
- Concordancia género/número
- Errores tipográficos, espacios duplicados
- Extranjerismos sin cursiva (`*extranjerismo*`)
- Mayúsculas/minúsculas en títulos, nombres propios, siglas
- Artículo "el" ante "heap" y "stack": usar "el *heap*", "el *stack*"
- Español rioplatense: "vos"/"tuteo", evitar "ustedes" singular

### 3. Revisión conceptual

- Definiciones precisas y actualizadas
- Código Go: que compile y sea correcto
- Diagramas: texto y valores coinciden con ejemplos
- Ejercicios: enunciados claros, soluciones correctas
- Citas/referencias: formato `{cite}`, existen en `references.bib`
- Consistencia entre secciones del capítulo

### 4. Revisión de formato MyST

- Admonitions: formato unificado `{admonition}` con `class:`. No usar shorthand (`{note}`, `{important}`, etc.)
- Figures: ` ```{figure} ``, campos `name:`, `class:`, `width:`. Pares light/dark completos
- Code blocks: solo `{code-block}` con `linenos: true` y `language:`. `{code-file}` **NO es soportado** en mystmd (era de JBv1/Sphinx)
- Labels de ejercicios: `ej-{seccion}-{numero}`
- Frontmatter YAML: mínimo `label:`

### 5. Búsqueda de recursos externos en GitHub

Solo para capítulos 3-x y 4-x (Estructuras de Datos o Diseño de Algoritmos).

### Arquitectura de repositorios

Se usan dos tipos de repositorios:

- **`data-structures`**: forkear, implementar interfaces, correr tests. Template en
  `github.com/untref-ayp2/data-structures`. Contiene solo interfaces y tests, sin
  implementaciones concretas.
- **`taller-*`** (ej: `taller-tad`, `taller-pilas-colas`): clonar o forkear. Contiene
  ejemplos resueltos y ejercicios con esqueletos que usan o complementan
  `data-structures`.

Los alumnos apuntan su fork de `data-structures` desde `taller-*` mediante `replace`
en `go.mod`.

Archivado: `data-structures-old` (reemplazado por el nuevo `data-structures`).

### Revisión de contenido de apoyo

1. Consultar `github.com/untref-ayp2` para encontrar repositorios relevantes al tema:
   - `data-structures` — interfaces y tests de estructuras de datos
   - `taller-*` — ejercicios y ejemplos del capítulo
   - `taller-go` — ejercicios del Taller de Go
   - Archivados: `examples`, `snippets`, `examenes`, `guia-*` (referencia histórica)
2. Usar la sección "Vinculación con Repositorios Externos" de `Plan-Migracion.md`
   para identificar qué repos corresponden al capítulo.
3. Para cada repo encontrado, revisar su `README.md` y estructura de directorios
   para identificar:
   - Esqueletos/tests para ejercicios que podrían citarse en el apunte
   - Código de ejemplo que complemente la teoría del capítulo
4. Presentar los hallazgos como tabla de sugerencias.
5. Preguntar al usuario antes de incorporar cualquier recurso:
   "¿Querés que explore el repo `X` en detalle para buscar contenido para incluir?"
   - Si el usuario dice que sí, explorar el repo y listar archivos concretos.
   - Si el usuario dice que no, saltar ese repo.
6. NO modificar ningún archivo del apunte durante este paso.

### 6. Revisión de imágenes SVG

Para cada SVG referenciado:
1. Abrir el SVG (tanto `_light` como `_dark`)
2. Verificar que represente lo que el texto describe
3. Verificar clases CSS estándar (`.title`, `.code`, `.variable-node`, `.value-node`, `.arrow`)
4. Verificar pares light/dark completos

### 7. Reporte

```markdown
## Reporte de revisión: <archivo>

### 🔤 Ortografía y gramática
- `archivo.md:XX` — descripción → sugerencia

### 🧠 Conceptos
- `archivo.md:XX` — descripción → sugerencia

### 🌐 Recursos externos
- `untref-ayp2/repo` — descripción → sugerencia de inclusión

### 🖼️ Imágenes SVG
- `ruta/al/svg.svg` — descripción → sugerencia

### 📋 Admonitions y formato
- `archivo.md:XX` — descripción → sugerencia

### 📊 Pares light/dark
- `figura.svg` — ✅ Completo
- `figura.svg` — ❌ Falta `_dark.svg`
```

## Reglas estrictas

1. NUNCA modificar archivos directamente.
2. NUNCA ejecutar `make build`, `myst build`, `typst compile` ni comandos de build.
3. NUNCA hacer commits ni cambios en el repositorio.
4. NO corregir errores sobre la marcha — solo señalarlos.
5. Dudas conceptuales → preguntar al usuario.
6. Para capítulos 3-x y 4-x, sugerir recursos externos de `github.com/untref-ayp2` (guías de ejercicios, código de ejemplo) según el paso 5. Para el resto de los capítulos, NO sugerir ampliación de contenido — solo señalar errores existentes.

## Notas de estilo

- Ejercicios como listas planas son aceptables si no tienen solución asociada
- Crecimiento de `append`: ~2x para capacidades < 256, hasta ~1.25x (Go 1.18+)
- Nombres de variables consistentes entre texto y código (ej: traducir ambos si se traduce)
- Referencias a figuras: preferir "la siguiente figura" o `{ref}` sobre "Figura X.Y"

## Referencias

- Skill `diagramas-svg` para estándares de figuras light/dark
- `Plan-Migracion.md` para estado de revisión y tabla de vinculación con repos
- `AGENTS.md` para convenciones del proyecto
- `contenidos/myst.yml` para estructura del TOC
- `github.com/untref-ayp2` para guías de ejercicios y código de ejemplo
