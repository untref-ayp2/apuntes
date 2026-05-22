# Sesión — 22/05/2026 — Listas: animaciones SVG interactivas

## Estado actual

- `contenidos/3-estructuras-de-datos/3-3-listas.md` reescrito completo, con pseudocódigo,
  figuras estáticas, y links a animaciones SVG interactivas.
- `data-structures/list/` creado: `list.go` (interface), `node.go`, 4 esqueletos
  (`singly_linked`, `doubly_linked`, `doubly_linked_sentinel`, `circular_doubly_linked`),
  `list_test.go` (18 tests que fallan).
- `data-structures/stack/stack_list.go` + `queue/queue_list.go` con tests.
- `taller-tad/03-listas/ejercicios/01-ejercicios/` con 5 funciones de uso + StackList/QueueList.
- 4 pares SVG estáticos nuevos: Doble InsertBefore, Circular RemoveFirst, Centinelas Clear y Remove.
- 2 SVG animados interactivos (prototipo Find):
  - `contenidos/_static/figures/ListaEnlazadaSimpleFind_anim_light.svg`
  - `contenidos/_static/figures/ListaEnlazadaSimpleFind_anim_dark.svg`

## Pendiente para retomar

1. **Probar prototipo Find**: abrir SVG en navegador, verificar funcionamiento paso a paso.
2. **Generar animaciones para otras operaciones**: InsertAfter, Remove, Prepend, Append,
   RemoveFirst, RemoveLast (Lista Simple).
3. **Animaciones para Doble**: InsertBefore, RemoveLast.
4. **Animaciones para Circular**: RemoveFirst.
5. **Animaciones para Centinelas**: Remove, Clear.
6. **Reemplazar figuras estáticas** por links a las animadas en el markdown.
7. **Comparar `taller-tad` con los contratos de `data-structures/list/`**:
   asegurar consistencia entre las interfaces que ejercita el taller y las que
   definen los contratos.

## Detalles técnicos de las animaciones SVG

- Formato: SVG + JavaScript puro.
- Cada paso es un `<g id="step-N" display="none">` que se activa con `display="inline"`.
- Código panel sincronizado: highlight de línea activa con `class="code-line-active"`.
- Status bar y step counter se actualizan desde array JS.
- No se puede embeber inline en MyST (Typst ignora `<script>`).
  Solución: link directo al `.svg` con `target=_blank`.
- Coordenadas de nodos base: efectivas tras `translate(-67.69, -0.23)` sobre rects
  en x=80, 200, 320, 440.
- Flechas de traversión (azul, stroke-width=2) van de borde derecho de un nodo a
  borde izquierdo del siguiente.

## Archivos relevantes

| Archivo | Propósito |
|---|---|
| `.opencode/Plan-Migracion.md` | Plan general (3-3 en 🔄 En preparación) |
| `.opencode/sesion-2026-05-22-listas.md` | Esta sesión |
| `contenidos/3-estructuras-de-datos/3-3-listas.md` | Contenido del capítulo |
| `contenidos/_static/figures/*Find_anim_*.svg` | Animaciones prototipo Find |
| `contenidos/_static/figures/ListaEnlazadaSimple_*.svg` | Base visual del diagrama simple |
| `contenidos/_static/figures/ListaEnlazadaDoble*_*.svg` | Figuras estáticas Doble |
| `contenidos/_static/figures/ListaEnlazadaCircular*_*.svg` | Figuras estáticas Circular |
| `contenidos/_static/figures/ListaConCentinelas*_*.svg` | Figuras estáticas Centinelas |
