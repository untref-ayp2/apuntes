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

| #  | Archivo | Estado |
| -- | ------- | ------ |
| 1  | `contenidos/introduccion.md` | ✅ Revisado |
| 2  | `contenidos/1-presentacion/1-1-introduccion.md` | ✅ Revisado |
| 3  | `contenidos/1-presentacion/1-2-memoria.md` | ✅ Revisado |
| 4  | `contenidos/1-presentacion/1-3-analisis-de-algoritmos.md` | ⬜ Pendiente |
| 5  | `contenidos/2-taller-de-go/2-1-introduccion-go.md` | ⬜ Pendiente |
| 6  | `contenidos/2-taller-de-go/2-2-paquetes-y-modulos.md` | ⬜ Pendiente |
| 7  | `contenidos/2-taller-de-go/2-3-elementos-basicos.md` | ⬜ Pendiente |
| 8  | `contenidos/2-taller-de-go/2-4-funciones.md` | ⬜ Pendiente |
| 9  | `contenidos/2-taller-de-go/2-5-arreglos-slices.md` | ⬜ Pendiente |
| 10 | `contenidos/2-taller-de-go/2-6-maps.md` | ⬜ Pendiente |
| 11 | `contenidos/2-taller-de-go/2-7-punteros.md` | ⬜ Pendiente |
| 12 | `contenidos/2-taller-de-go/2-8-structs-interfaces.md` | ⬜ Pendiente |
| 13 | `contenidos/2-taller-de-go/2-9-archivos.md` | ⬜ Pendiente |
| 14 | `contenidos/2-taller-de-go/2-10-errores.md` | ⬜ Pendiente |
| 15 | `contenidos/2-taller-de-go/2-11-oop.md` | ⬜ Pendiente |
| 16 | `contenidos/3-estructuras-de-datos/3-1-tad.md` | ⬜ Pendiente |
| 17 | `contenidos/3-estructuras-de-datos/3-2-pilas-colas.md` | ⬜ Pendiente |
| 18 | `contenidos/3-estructuras-de-datos/3-3-listas.md` | ⬜ Pendiente |
| 19 | `contenidos/3-estructuras-de-datos/3-4-conjuntos.md` | ⬜ Pendiente |
| 20 | `contenidos/3-estructuras-de-datos/3-5-mapa-de-bits.md` | ⬜ Pendiente |
| 21 | `contenidos/3-estructuras-de-datos/3-6-tablas-de-hashing.md` | ⬜ Pendiente |
| 22 | `contenidos/3-estructuras-de-datos/3-7-diccionarios.md` | ⬜ Pendiente |
| 23 | `contenidos/3-estructuras-de-datos/3-8-arboles.md` | ⬜ Pendiente |
| 24 | `contenidos/3-estructuras-de-datos/3-9-abb.md` | ⬜ Pendiente |
| 25 | `contenidos/3-estructuras-de-datos/3-10-arboles-balanceados.md` | ⬜ Pendiente |
| 26 | `contenidos/3-estructuras-de-datos/3-11-monticulo-binario.md` | ⬜ Pendiente |
| 27 | `contenidos/3-estructuras-de-datos/3-12-iteradores-abb.md` | ⬜ Pendiente |
| 28 | `contenidos/4-diseno-de-algoritmos/4-1-recursividad.md` | ⬜ Pendiente |
| 29 | `contenidos/4-diseno-de-algoritmos/4-2-patrones-de-diseno.md` | ⬜ Pendiente |
| 30 | `contenidos/4-diseno-de-algoritmos/4-3-algoritmos-avidos.md` | ⬜ Pendiente |
| 31 | `contenidos/4-diseno-de-algoritmos/4-4-backtracking.md` | ⬜ Pendiente |
| 32 | `contenidos/4-diseno-de-algoritmos/4-5-programacion-dinamica.md` | ⬜ Pendiente |
| 33 | `contenidos/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos.md` | ⬜ Pendiente |
| 34 | `contenidos/4-diseno-de-algoritmos/4-7-ordenamientos-lineales.md` | ⬜ Pendiente |
| 35 | `contenidos/5-taller-de-git/5-1-introduccion-git.md` | ⬜ Pendiente |
| 36 | `contenidos/bibliografia.md` | ⬜ Pendiente |

---

## Tareas Restantes (compactado)

### CSS Light/Dark Mode
Reemplazar `custom.css` con el de EDD. Incluye reglas `only-light-mode` / `only-dark-mode`.

### Estandarizar Admonitions
- 34 `{admonition}` sin normalizar, 5 `{note}`, 5 `{important}`, 2 con HTML legacy
- Unificar títulos y convertir legacy

### Figuras — Pares Light/Dark
- ✅ MapaDeMemoria: agregado Segmento de Datos
- Pendiente: ~30 imágenes (ABB, AVL, Listas, Patrones, Recursión, Backtracking, Heap, Misc). Usar skill `diagramas-svg`.

### Limpieza
- `requirements.txt`: remover `sphinx-proof`, `sphinx-thebe`, `myst-parser`
- Directorios legacy: `assets/geogebra/`, `assets/xfig/`
- `myst.yml`: apuntar template Typst, agregar descarga PDF, logo, favicon
- `bibliografia.md`: adaptar formato MyST

### CI/CD
- GitHub Actions: agregar paso `make pdf` con instalación de `typst`
- Cambiar target del deploy a `main` cuando esté listo

---

## Resumen Visual

```
Estado actual (jb2-martin):

  Infraestructura:
    Build + PDF        ✅ script + template + fuentes
    CSS light/dark     🔶 pendiente completar

  Revisión de contenido (09/05/2026):
    introduccion.md    ✅
    1-1-introduccion   ✅
    1-2-memoria        ✅
    1-3-analisis       ⬜
    2-Taller de Go     ⬜ 11 archivos
    3-Estructuras      ⬜ 12 archivos
    4-Diseño Alg.      ⬜ 7 archivos
    5-Taller Git       ⬜
    bibliografia       ⬜

  Admonitions          🔶 ~34 pendientes
  Figuras l/d          🔶 ~30 pendientes
  Dependencias         🔶 con restos JBv1
```
