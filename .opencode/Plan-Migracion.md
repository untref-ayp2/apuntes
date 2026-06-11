# Plan de Migración — Apunte AyP2 a Jupyter-Book 2 (MyST)

## Diagnóstico General

El repositorio tiene dos ramas principales:

- **`main`**: versión publicada actual con Jupyter Book v1
- **`jb2-martin`** (HEAD): migración a MyST/JBv2 en progreso

### Estado de la migración técnica

| Componente              | Estado                           |
| ----------------------- | -------------------------------- |
| Build system            | ✅ Migrado a `myst build`        |
| Config (`myst.yml`)     | ✅ Creado                        |
| Archivos legacy         | ✅ `_config.yml`/`_toc.yml` quitados |
| Assets a `_static/`     | ✅ Imágenes movidas              |
| CSS light/dark mode     | ✅ Reemplazado con el de EDD     |
| JS sidebar              | ✅ Adaptado a MyST               |
| Script PDF              | ✅ Migrado a Typst               |
| Template PDF            | ✅ `plain_typst_book_ayp2`       |
| Fuente Roboto           | ✅ Instalada en el sistema       |
| Figuras light/dark      | 🔶 ~50/80 imágenes convertidas   |
| Admonitions             | 🔶 ~34 `{admonition}` sin normalizar |
| GitHub Actions          | ✅ Migrado a myst                |
| Dependencias            | 🔶 Tiene restos de JBv1          |

---

## Prioridad Alta — Revisión de Contenido (iniciada 09/05/2026)

Ciclo de revisión completo del contenido: leer cada archivo, verificar formato MyST,
corregir errores, admonitions, figuras, y consistencia general.

| #  | Archivo | Estado | Repos vinculados |
| -- | ------- | ------ | ---------------- |
| 1  | `contenidos/introduccion.md` | ✅ Revisado | — |
| 2  | `contenidos/1-presentacion/1-1-introduccion.md` | ✅ Revisado | — |
| 3  | `contenidos/1-presentacion/1-2-memoria.md` | ✅ Revisado | — |
| 4  | `contenidos/1-presentacion/1-3-analisis-de-algoritmos.md` | ✅ Revisado | — |
| 5  | `contenidos/2-taller-de-go/2-1-introduccion-go.md` | ✅ Revisado | `taller-go`, `taller-resuelto` |
| 6  | `contenidos/2-taller-de-go/2-2-paquetes-y-modulos.md` | ✅ Revisado | `taller-go` |
| 7  | `contenidos/2-taller-de-go/2-3-elementos-basicos.md` | ✅ Revisado | `taller-go` |
| 8  | `contenidos/2-taller-de-go/2-4-funciones.md` | ✅ Revisado | `taller-go` |
| 9  | `contenidos/2-taller-de-go/2-5-arreglos-slices.md` | ✅ Revisado | `taller-go` |
| 10 | `contenidos/2-taller-de-go/2-6-maps.md` | ✅ Revisado | `taller-go` |
| 11 | `contenidos/2-taller-de-go/2-7-punteros.md` | ✅ Revisado | `taller-go` |
| 12 | `contenidos/2-taller-de-go/2-8-structs-interfaces.md` | ✅ Revisado | `taller-go` |
| 13 | `contenidos/2-taller-de-go/2-9-archivos.md` | ✅ Revisado | `taller-go` |
| 14 | `contenidos/2-taller-de-go/2-10-errores.md` | ✅ Revisado | `taller-go` |
| 15 | `contenidos/2-taller-de-go/2-11-oop.md` | ✅ Revisado | `taller-go` |
| 16 | `contenidos/2-taller-de-go/2-12-genericos.md` | ✅ Revisado | `taller-go` |
| 17 | `contenidos/3-estructuras-de-datos/3-1-tad.md` | ✅ Revisado | `data-structures`, `taller-tad` |
| 18 | `contenidos/3-estructuras-de-datos/3-2-pilas-colas.md` | ✅ Revisado | `taller-tad`, `data-structures` |
| 19 | `contenidos/3-estructuras-de-datos/3-3-listas.md` | ✅ Revisado | `data-structures`, `taller-tad` |
| 20 | `contenidos/3-estructuras-de-datos/3-4-mapa-de-bits.md` | ✅ Revisado | `data-structures`, `taller-tad` |
| 21 | `contenidos/3-estructuras-de-datos/3-5-tablas-de-hashing.md` | ✅ Revisado | `data-structures`, `taller-tad` |
| 22 | `contenidos/3-estructuras-de-datos/3-6-conjuntos.md` | ✅ Revisado | `data-structures`, `taller-tad` |
| 23 | `contenidos/3-estructuras-de-datos/3-7-diccionarios.md` | ✅ Revisado | `data-structures`, `taller-tad` |
| 24 | `contenidos/3-estructuras-de-datos/3-8-arboles.md` | ✅ Revisado | `taller-tad`, `data-structures` |
| 25 | `contenidos/3-estructuras-de-datos/3-9-abb.md` | ✅ Revisado | `guia-abb`, `data-structures` |
| 26 | `contenidos/3-estructuras-de-datos/3-10-arboles-balanceados.md` | ✅ Revisado | `data-structures` |
| 27 | `contenidos/3-estructuras-de-datos/3-11-monticulo-binario.md` | ⬜ Pendiente | `guia-monticulos-binarios` |
| 28 | `contenidos/3-estructuras-de-datos/3-12-iteradores-abb.md` | ⬜ Pendiente | `guia-abb` |
| 29 | `contenidos/4-diseno-de-algoritmos/4-1-recursividad.md` | ⬜ Pendiente | `guia-algoritmos`, `examples` |
| 30 | `contenidos/4-diseno-de-algoritmos/4-2-patrones-de-diseno.md` | ⬜ Pendiente | `guia-patrones`, `examples` |
| 31 | `contenidos/4-diseno-de-algoritmos/4-3-algoritmos-avidos.md` | ⬜ Pendiente | `guia-avidos`, `examples` |
| 32 | `contenidos/4-diseno-de-algoritmos/4-4-backtracking.md` | ⬜ Pendiente | `guia-backtracking`, `examples` |
| 33 | `contenidos/4-diseno-de-algoritmos/4-5-programacion-dinamica.md` | ⬜ Pendiente | `guia-algoritmos`, `examples` |
| 34 | `contenidos/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos.md` | ⬜ Pendiente | `guia-ordenamientos-recursivos`, `examples` |
| 35 | `contenidos/4-diseno-de-algoritmos/4-7-ordenamientos-lineales.md` | ⬜ Pendiente | `examples` |
| 36 | `contenidos/5-taller-de-git/5-1-introduccion-git.md` | ⬜ Pendiente | — |
| 37 | `contenidos/bibliografia.md` | ⬜ Pendiente | — |

---

## Vinculación con Repositorios Externos

Cada capítulo de 3-x y 4-x tiene repositorios asociados en `github.com/untref-ayp2`
con guías de ejercicios, código de ejemplo y soluciones. La revisión de cada capítulo
debe buscar recursos en estos repos para referenciar o incluir en el apunte.

| Capítulo | Guías de ejercicios | Código de ejemplo |
|---|---|---|
| 3-1 TAD | `taller-tad` | `data-structures` |
| 3-2 Pilas y Colas | `taller-tad` (ejercicios en `02-pilas-colas/`) | `data-structures` |
| 3-3 Listas | `taller-tad` (`03-listas/`) | `data-structures` (`list/`) |
| 3-4 Mapa de bits | `taller-tad` (`04-mapa-de-bits/`) | `data-structures` (`bitmap/`) |
| 3-5 Tablas de Hashing | `taller-tad` (`05-hashing/`) | `data-structures` (`hashtable/`) |
| 3-6 Conjuntos | `taller-tad` (`06-conjuntos/`) | `data-structures` (`set/`) |
| 3-7 Diccionarios | `taller-tad` (`07-diccionarios/`) | `data-structures` (`dictionary/`) |
| 3-8 Árboles | `guia-arboles-binarios`, `guia-arboles-binarios-resuelta` | `data-structures` |
| 3-9 ABB | `guia-abb`, `guia-abb-resuelta` | `data-structures` |
| 3-10 Árboles Balanceados | `guia-abb-balanceados`, `guia-abb-balanceados-resuelta` | — |
| 3-11 Montículo Binario | `guia-monticulos-binarios`, `guia-monticulos-binarios-resuelta` | — |
| 3-12 Iteradores ABB | `guia-abb`, `guia-abb-resuelta` | — |
| 4-1 Recursividad | `guia-algoritmos` | `examples/recursividad` |
| 4-2 Patrones de Diseño | `guia-patrones`, `guia-patrones-resuelta` | `examples/patrones` |
| 4-3 Algoritmos Ávidos | `guia-avidos`, `guia-avidos-resuelta` | `examples/avidos` |
| 4-4 Backtracking | `guia-backtracking`, `guia-backtracking-resuelta` | `examples/backtracking` |
| 4-5 Programación Dinámica | `guia-algoritmos` | `examples/programacion_dinamica` |
| 4-6 Ordenamientos Recursivos | `guia-ordenamientos-recursivos`, `guia-ordenamientos-recursivos-resuelta` | `examples/ordenam_rec` |
| 4-7 Ordenamientos Lineales | — | `examples` |

Además, hay repositorios transversales útiles para múltiples capítulos:
- `untref-ayp2/examples` (archivado): Código de ejemplo de toda la cursada
- `untref-ayp2/snippets` (archivado): Fragmentos de código varios
- `untref-ayp2/examenes` (archivado): Exámenes anteriores
- `untref-ayp2/tp20252C`, `untref-ayp2/tp20252C-Resuelto`: Trabajos prácticos

---

## Tareas Restantes (compactado)

### CSS Light/Dark Mode
Reemplazar `custom.css` con el de EDD. Incluye reglas `only-light-mode` / `only-dark-mode`.

### Estandarizar Admonitions
- 34 `{admonition}` sin normalizar, 5 `{note}`, 5 `{important}`, 2 con HTML legacy
- Unificar títulos y convertir legacy
- **Definiciones**: usar `{admonition} Definición` con `class: hint`. Ejemplo en `1-3-analisis-de-algoritmos.md:24-29`

### Figuras — Pares Light/Dark
- ✅ MapaDeMemoria: agregado Segmento de Datos
- ✅ Listas (8 figuras): completado 21/05/2026
- Pendiente: ~22 imágenes (ABB, AVL, Patrones, Recursión, Backtracking, Heap, Misc). Usar skill `diagramas-svg`.

### Arquitectura de repos de apoyo (definido 17/05/2026)
- ✅ `data-structures` (nuevo): interfaces + tests, alumnos forkear e implementar
- ✅ `taller-tad` (nuevo): ejercicios y ejemplos del capítulo 3-1
- ✅ `data-structures-old` archivado (renombrado)
- 📝 Poblar `data-structures` con más interfaces a medida que se revisen capítulos 3-x
- 📝 Crear `taller-*` adicionales según se avance en la revisión

### Limpieza
- `requirements.txt`: remover `sphinx-proof`, `sphinx-thebe`, `myst-parser`
- Directorios legacy: `assets/geogebra/`, `assets/xfig/`
- `myst.yml`: apuntar template Typst, agregar descarga PDF, logo, favicon
- `bibliografia.md`: adaptar formato MyST

### CI/CD
- GitHub Actions: agregar paso `make pdf` con instalación de `typst`
- ✅ Target del deploy cambiado a `main` (17/05/2026)

---

## Resumen Visual

```
Estado actual (jb2-martin):

  Infraestructura:
    Build + PDF        ✅ script + template + fuentes
    Deploy target      ✅ main (desactivado jb2-martin)
    CSS light/dark     🔶 pendiente completar

  Revisión de contenido (09/05/2026):
    introduccion.md    ✅
    1-1-introduccion   ✅
    1-2-memoria        ✅
    1-3-analisis       ✅
    2-Taller de Go     ✅ 12 archivos
    3-Estructuras      ✅ 8 / 🔄 0 / ⬜ 4 archivos
    4-Diseño Alg.      ⬜ 7 archivos
    5-Taller Git       ⬜
    bibliografia       ⬜

  Admonitions          🔶 ~34 pendientes
  Figuras l/d          🔶 ~30 pendientes
  Repos apoyo          ✅ data-structures + taller-tad creados + list/
  Dependencias         🔶 con restos JBv1
```
