---
name: revisor-contenido
description: >
  Revisa ortografía, gramática, conceptos e imágenes SVG en capítulos del
  apunte AyP2. Activarlo cuando el usuario pida revisar un capítulo con
  frases como "revisá", "revisa", "revisión", "revisar" seguidas del número
  o nombre del capítulo (ej: "revisá 1-3", "revisa analisis-de-algoritmos").
license: CC-BY-SA-4.0
compatibility: opencode
metadata:
  audience: docentes
  workflow: revision-contenido
---

# Revisor de Contenido — Apunte AyP2

Skill para revisar capítulos del apunte de Algoritmos y Programación II (UNTREF).
**Siempre en modo plan:** solo mostrar sugerencias, NUNCA modificar archivos ni ejecutar builds.

## Resolución del archivo a revisar

El usuario puede referirse al capítulo de varias formas. Buscar el match en esta
tabla priorizando coincidencia por el número de sección:

| Si dice...                  | Archivo correspondiente                          |
| --------------------------- | ------------------------------------------------ |
| `intro` o `introduccion`    | `contenidos/introduccion.md`                     |
| `1-1` o `1-1-intro`         | `contenidos/1-presentacion/1-1-introduccion.md`  |
| `1-2` o `1-2-memoria`       | `contenidos/1-presentacion/1-2-memoria.md`       |
| `1-3` o `1-3-analisis`      | `contenidos/1-presentacion/1-3-analisis-de-algoritmos.md` |
| `2-1` o `2-1-intro-go`      | `contenidos/2-taller-de-go/2-1-introduccion-go.md` |
| `2-2` o `2-2-paquetes`      | `contenidos/2-taller-de-go/2-2-paquetes-y-modulos.md` |
| `2-3` o `2-3-arreglos`      | `contenidos/2-taller-de-go/2-3-arreglos-slices.md` |
| `2-4` o `2-4-maps`          | `contenidos/2-taller-de-go/2-4-maps.md`         |
| `2-5` o `2-5-funciones`     | `contenidos/2-taller-de-go/2-5-funciones.md`    |
| `2-6` o `2-6-punteros`      | `contenidos/2-taller-de-go/2-6-punteros.md`     |
| `2-7` o `2-7-errores`       | `contenidos/2-taller-de-go/2-7-errores.md`      |
| `2-8` o `2-8-structs`       | `contenidos/2-taller-de-go/2-8-structs-interfaces.md` |
| `2-9` o `2-9-exportado`     | `contenidos/2-taller-de-go/2-9-exportado-no-exportado.md` |
| `2-10` o `2-10-oop`         | `contenidos/2-taller-de-go/2-10-oop.md`         |
| `3-1` o `3-1-tad`           | `contenidos/3-estructuras-de-datos/3-1-tad.md`  |
| `3-2` o `3-2-pilas`         | `contenidos/3-estructuras-de-datos/3-2-pilas-colas.md` |
| `3-3` o `3-3-listas`        | `contenidos/3-estructuras-de-datos/3-3-listas.md` |
| `3-4` o `3-4-conjuntos`     | `contenidos/3-estructuras-de-datos/3-4-conjuntos.md` |
| `3-5` o `3-5-mapa-bits`     | `contenidos/3-estructuras-de-datos/3-5-mapa-de-bits.md` |
| `3-6` o `3-6-hashing`       | `contenidos/3-estructuras-de-datos/3-6-tablas-de-hashing.md` |
| `3-7` o `3-7-diccionarios`  | `contenidos/3-estructuras-de-datos/3-7-diccionarios.md` |
| `3-8` o `3-8-arboles`       | `contenidos/3-estructuras-de-datos/3-8-arboles.md` |
| `3-9` o `3-9-abb`           | `contenidos/3-estructuras-de-datos/3-9-abb.md`  |
| `3-10` o `3-10-balanceados` | `contenidos/3-estructuras-de-datos/3-10-arboles-balanceados.md` |
| `3-11` o `3-11-heap`        | `contenidos/3-estructuras-de-datos/3-11-monticulo-binario.md` |
| `3-12` o `3-12-iteradores`  | `contenidos/3-estructuras-de-datos/3-12-iteradores-abb.md` |
| `4-1` o `4-1-recursividad`  | `contenidos/4-diseno-de-algoritmos/4-1-recursividad.md` |
| `4-2` o `4-2-patrones`      | `contenidos/4-diseno-de-algoritmos/4-2-patrones-de-diseno.md` |
| `4-3` o `4-3-avidos`        | `contenidos/4-diseno-de-algoritmos/4-3-algoritmos-avidos.md` |
| `4-4` o `4-4-backtracking`  | `contenidos/4-diseno-de-algoritmos/4-4-backtracking.md` |
| `4-5` o `4-5-programacion-dinamica` | `contenidos/4-diseno-de-algoritmos/4-5-programacion-dinamica.md` |
| `4-6` o `4-6-ordenamientos-rec` | `contenidos/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos.md` |
| `4-7` o `4-7-ordenamientos-lineales` | `contenidos/4-diseno-de-algoritmos/4-7-ordenamientos-lineales.md` |
| `5-1` o `5-1-git`           | `contenidos/5-taller-de-git/5-1-introduccion-git.md` |
| `biblio` o `bibliografia`   | `contenidos/bibliografia.md`                    |

Si no hay match exacto, buscar con glob `contenidos/**/*${termino}*.md` para
encontrar archivos que contengan el término en el nombre.

## Proceso de revisión

### 1. Leer el archivo completo

Leer el archivo markdown de principio a fin para entender su estructura y contenido.

### 2. Revisión ortográfica y gramatical

Identificar y reportar:

- **Tildes faltantes o incorrectas** (ej: "esta" vs "está", "solo" vs "sólo")
- **Puntuación**: comas, puntos, puntos y coma mal usados
- **Concordancia**: género y número entre sujeto y predicado
- **Errores tipográficos**: palabras mal escritas, espacios duplicados
- **Extranjerismos**: verificar que estén en cursiva (`*extranjerismo*`) cuando corresponde
- **Mayúsculas/minúsculas**: títulos, nombres propios, siglas
- **Artículo "el" ante "heap" y "stack"**: usar siempre "el *heap*", "el *stack*" (masculino, en cursiva)
- **Reglas de español rioplatense**: uso de "vos" / "tuteo", evitar "ustedes" para singular

### 3. Revisión conceptual

Verificar la corrección técnica de:

- **Definiciones**: que sean precisas y estén actualizadas (ej: stack dinámico en Go, escape analysis, GC concurrente)
- **Ejemplos de código**: que el código Go compile y haga lo que se describe, que los nombres de variables sigan las convenciones del proyecto
- **Diagramas**: que el texto y valores en el diagrama coincidan con el código de ejemplo
- **Ejercicios**: que el enunciado sea claro, que las soluciones propuestas sean correctas
- **Citas y referencias**: que estén en formato `{cite}` MyST y existan en `references.bib`
- **Consistencia**: que no haya contradicciones entre secciones del mismo capítulo o con otros capítulos ya revisados

### 4. Revisión de formato MyST

- **Admonitions**: verificar que usen el formato unificado `{admonition}` con `class:`. No usar directivos shorthand (`{note}`, `{important}`, `{tip}`, etc.). Clases disponibles: `note`, `hint`, `important`, `warning`, `tip`, `caution`, `dropdown`. El título debe ser conciso y aportar valor.
- **Figures**: verificar que usen los bloques ```` ```{figure} ```` con los campos `name:`, `class:` y `width:` cuando corresponda. Las figuras con `only-light-mode` deben tener su contraparte `only-dark-mode`.
- **Code blocks**: verificar que usen `{code-block}` o `{code-file}` con `:language:` correcto y `:linenos:` cuando sea útil.
- **Labels**: verificar que los ejercicios tengan labels con formato `ej-{seccion}-{numero}`.
- **Frontmatter**: que el archivo tenga frontmatter YAML válido (mínimo `label:`).

### 5. Revisión de imágenes SVG

Para cada imagen referenciada en el capítulo:

1. **Abrir el archivo SVG** referenciado (tanto `_light.svg` como `_dark.svg` si existen)
2. **Verificar contenido**: que el SVG represente correctamente lo que el texto describe, que los valores y etiquetas coincidan con ejemplos
3. **Verificar clases CSS**: que use las clases estándar (`.title`, `.code`, `.variable-node`, `.value-node`, `.arrow`) según el skill `diagramas-svg`
4. **Pares light/dark**: si la figura se muestra como `only-light-mode`, verificar que exista el archivo `*_dark.svg` correspondiente con los colores del tema oscuro. Si falta, reportarlo.

### 6. Reporte estructurado

Devolver un reporte con esta estructura:

```markdown
## Reporte de revisión: <nombre-del-archivo>

### 🔤 Ortografía y gramática
- `archivo.md:XX` — descripción del issue → sugerencia

### 🧠 Conceptos
- `archivo.md:XX` — descripción del issue → sugerencia

### 🖼️ Imágenes SVG
- `ruta/al/svg.svg` — descripción del issue → sugerencia

### 📋 Admonitions y formato
- `archivo.md:XX` — descripción del issue → sugerencia

### 📊 Estado de pares light/dark
- `figura.svg` — ✅ Tiene par light/dark
- `figura.svg` — ❌ Falta versión `_dark.svg`
```

## Reglas estrictas

1. **NUNCA** modificar archivos directamente.
2. **NUNCA** ejecutar `make build`, `myst build`, `typst compile` ni ningún comando de build.
3. **NUNCA** hacer commits ni cambios en el repositorio.
4. **NO** corregir errores sobre la marcha — solo señalarlos y sugerir la corrección.
5. Si hay dudas sobre un concepto, preguntar al usuario en vez de asumir.

## Notas de estilo (actualizadas por revisión)

- **Ejercicios**: Los ejercicios numerados como listas planas son aceptables y preferibles cuando no tienen soluciones asociadas. No es necesario convertirlos a `{exercise}` directives a menos que tengan una `{solution}` correspondiente.
- **Crecimiento de `append`**: La estrategia de crecimiento de `append` no es exactamente 2x en todas las versiones de Go. Desde Go 1.18, la tasa de crecimiento es variable (~2x para capacidades < 256, reduciéndose gradualmente hasta ~1.25x). Usar "aproximadamente el doble" en vez de afirmaciones absolutas.
- **Nombres de variables en adaptaciones**: Al adaptar ejemplos de libros (ej: Donovan & Kernighan), verificar que el nombre de la variable se mantenga consistente entre el texto explicativo y el bloque de código. Si se traduce el nombre (ej: `months` → `meses`), actualizar ambas ocurrencias.
- **Referencias a figuras numeradas**: No usar "Figura X.Y" a menos que la figura tenga un label numerado explícito con `{ref}`. Preferir "la siguiente figura" o usar referencias cruzadas con `{ref}`.

## Referencias útiles

- Skill `diagramas-svg` para estándares de figuras light/dark
- `Plan-Migracion.md` para estado de revisión de cada archivo
- `AGENTS.md` para convenciones del proyecto
- `contenidos/myst.yml` para estructura del TOC
