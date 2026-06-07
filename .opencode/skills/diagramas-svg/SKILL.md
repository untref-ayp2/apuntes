---
name: diagramas-svg
description: Crea y mantiene diagramas SVG con estilos consistentes para el proyecto UNTREF AyP2
license: CC-BY-SA-4.0
compatibility: opencode
---

<role>
Sos un diseñador de diagramas SVG para el apunte "Algoritmos y Programación 2" de la UNTREF.
Creás y mantenés diagramas en pares light/dark que se renderizan correctamente tanto en HTML como en PDF.
Tus diagramas deben seguir estándares de clases CSS consistentes con el resto del proyecto.
</role>

<context>
Este apunte se compila a HTML (MyST) y PDF (Typst). Los SVG se renderizan con:
- **Versión light** incluida en HTML (modo claro) y en el PDF
- **Versión dark** incluida solo en HTML (modo oscuro)
- Cada diagrama necesita su par `_light.svg` y `_dark.svg`
- Las clases CSS estandarizadas permiten mantener consistencia visual entre cientos de diagramas
</context>

## Estilos Obligatorios

### Estructura con Clases CSS

Usar clases CSS en `<defs><style>` para mantener consistencia y facilitar mantenimiento:

**Light:**

```xml
<defs>
  <style>
    .title { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 20px; text-anchor: middle; fill: #333333; }
    .code-example { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 18px; fill: #333333; text-anchor: start; }
    .code { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 16px; fill: #333333; text-anchor: middle; }
    .variable-node { fill: #e1f5ff; stroke: #4682b4; stroke-width: 2; }
    .value-node { fill: #ffe1e1; stroke: #e9967a; stroke-width: 2; }
    .arrow { stroke: #333333; stroke-width: 2; marker-end: url(#arrowhead); }
    .note { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 14px; fill: #666666; text-anchor: middle; font-style: italic; }
  </style>
  <marker id="arrowhead" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto">
    <polygon points="0 0, 6 2.5, 0 5" fill="#333333" />
  </marker>
</defs>
```

**Dark:**

```xml
<defs>
  <style>
    .title { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 20px; text-anchor: middle; fill: #e0e0e0; }
    .code-example { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 18px; fill: #e0e0e0; text-anchor: start; }
    .code { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 16px; fill: #e0e0e0; text-anchor: middle; }
    .variable-node { fill: #2d3748; stroke: #63b3ed; stroke-width: 2; }
    .value-node { fill: #4a5568; stroke: #fc8181; stroke-width: 2; }
    .arrow { stroke: #e0e0e0; stroke-width: 2; marker-end: url(#arrowhead); }
    .note { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 14px; fill: #a0aec0; text-anchor: middle; font-style: italic; }
  </style>
  <marker id="arrowhead" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto">
    <polygon points="0 0, 6 2.5, 0 5" fill="#e0e0e0" />
  </marker>
</defs>
```

### Clases Semánticas

| Clase            | Descripción                                  | text-anchor |
| ---------------- | -------------------------------------------- | ----------- |
| `.title`         | Título principal del diagrama                | middle      |
| `.code`          | Texto dentro de nodos (16px)                 | middle      |
| `.code-example`  | Ejemplos de código fuera de nodos (18px)     | start       |
| `.variable-node` | Nodos que representan variables (azul)       | -           |
| `.value-node`    | Nodos que representan valores/strings (rojo) | -           |
| `.arrow`         | Flechas/aristas entre nodos                  | -           |
| `.note`          | Notas explicativas en cursiva (14px)         | middle      |

### Fuentes

- **Título** (`.title`): `ui-sans-serif, system-ui, sans-serif`
- **Código** (`.code`, `.code-example`): `menlo, consola, 'DejaVu Sans Mono'`

**Regla**: Si el texto representa código Go o valores de datos, usar fuente monospaciada. Para títulos, usar fuente por defecto.

### Colores - Theme Light (Tonos Pasteles Claros)

| Elemento                 | Fill      | Stroke    |
| ------------------------ | --------- | --------- |
| Fondo principal          | `#f0f2f5` | -         |
| Nodos azules (variables) | `#e1f5ff` | `#4682b4` |
| Nodos verdes             | `#e1ffe1` | `#2e8b57` |
| Nodos rojos (valores)    | `#ffe1e1` | `#e9967a` |
| Nodos naranjas           | `#fff4e1` | `#f6ad55` |
| Nodos morados            | `#f5e1ff` | `#9f7aea` |
| Texto y líneas           | -         | `#333333` |

### Colores - Theme Dark (Tonos Pasteles Oscuros)

| Elemento                   | Fill      | Stroke    |
| -------------------------- | --------- | --------- |
| Fondo principal            | `#1e1e1e` | -         |
| Contenedores               | `#2d3748` | -         |
| Nodos internos (variables) | `#2d3748` | `#63b3ed` |
| Nodos hoja (valores)       | `#4a5568` | `#fc8181` |
| Nodos verdes               | `#285e61` | `#68d391` |
| Nodos naranjas             | `#744210` | `#f6ad55` |
| Nodos morados              | `#44337a` | `#b794f4` |
| Texto y líneas             | -         | `#e0e0e0` |

### Tamaños de Fuente

- **16px**: Texto en nodos (`.code`)
- **18px**: Ejemplos de código (`.code-example`)
- **20px**: Título principal (`.title`)

### Grosores de Línea

- **1px**: Bordes punteados (`stroke-dasharray="5,5"`)
- **2px**: Bordes de nodos, aristas

### Otros Estilos

- Bordes redondeados: `rx="5"` para nodos
- Flechas: marker tipo triángulo
- Alineación de texto: `text-anchor="middle"` o `text-anchor="left"`
- Ruteo de líneas: usar estilo Manhattan

---

## Diagramas de Árboles

Para diagramas de árboles binarios y expresiones, usar estas clases adicionales.
Los colores coinciden con la paleta de los applets interactivos del capítulo 3-8.

### Clases para árboles

| Clase               | Descripción                                           | Ámbito              |
| ------------------- | ----------------------------------------------------- | ------------------- |
| `.edge`             | Arista entre nodos del árbol                          | ArbolBinario        |
| `.tree-edge`        | Arista gruesa entre nodos (árbol genérico)            | Arbol               |
| `.tree-arrowhead`   | Punta de flecha en aristas del árbol genérico         | Arbol               |
| `.op-node`          | Nodo de operación (+, −, *, etc.)                     | ArbolBinario        |
| `.num-node`         | Nodo de número o valor                                | ArbolBinario        |
| `.node-circle`      | Círculo de nodo en árbol genérico                     | Arbol               |
| `.node-text`        | Texto dentro de nodos (monospace, bold)               | Arbol / ArbolBinario |
| `.annotation-text`  | Anotaciones externas (profundidad, nivel, etc.)       | Arbol               |
| `.pointer-line`     | Línea de puntero desde una anotación                  | Arbol               |
| `.pointer-arrowhead`| Punta de flecha del puntero                           | Arbol               |
| `.dashed-line`      | Línea punteada para marcar niveles/profundidad        | Arbol               |

### Colores para árboles — Light

| Elemento                  | Fill         | Stroke       | Stroke-width |
| ------------------------- | ------------ | ------------ | ------------ |
| Nodos operación (`op-node`) | `#e1f5ff`  | `#4682b4`    | 2.5          |
| Nodos número (`num-node`) | `#ffe1e1`    | `#e9967a`    | 2.5          |
| Nodo genérico (`node-circle`) | `#ffe1e1` | `#e9967a`    | 20*          |
| Arista (`edge`)           | —            | `#333333`    | 2            |
| Arista género (`tree-edge`) | —          | `#333333`    | 18*          |
| Flecha arista             | `#333333`    | `#333333`    | 8*           |
| Línea puntero             | —            | `#87cfff`    | 14*          |
| Flecha puntero            | `#e1f5ff`    | `#87cfff`    | 8*           |
| Línea punteada            | —            | `#333333`    | 14*          |
| Texto en nodos            | `#333333`    | —            | —            |
| Anotaciones               | `#333333`    | —            | —            |

\* *Valores para viewBox `0 0 4801 3535` (Arbol). Ajustar proporcionalmente según el viewBox.*

### Colores para árboles — Dark

| Elemento                  | Fill         | Stroke       | Stroke-width |
| ------------------------- | ------------ | ------------ | ------------ |
| Nodos operación (`op-node`) | `#2d3748` | `#63b3ed`    | 2.5          |
| Nodos número (`num-node`) | `#4a5568`    | `#fc8181`    | 2.5          |
| Nodo genérico (`node-circle`) | `#4a5568` | `#fc8181`    | 20*          |
| Arista (`edge`)           | —            | `#e0e0e0`    | 2            |
| Arista género (`tree-edge`) | —          | `#e0e0e0`    | 18*          |
| Flecha arista             | `#e0e0e0`    | `#e0e0e0`    | 8*           |
| Línea puntero             | —            | `#87cfff`    | 14*          |
| Flecha puntero            | `#2d3748`    | `#87cfff`    | 8*           |
| Línea punteada            | —            | `#e0e0e0`    | 14*          |
| Texto en nodos            | `#e0e0e0`    | —            | —            |
| Anotaciones               | `#e0e0e0`    | —            | —            |

\* *Valores para viewBox `0 0 4801 3535` (Arbol). Ajustar proporcionalmente según el viewBox.*

### Ejemplo de árbol binario (light)

```xml
<defs>
  <style>
    .edge { stroke: #333333; stroke-width: 2; fill: none; }
    .op-node { fill: #e1f5ff; stroke: #4682b4; stroke-width: 2.5; }
    .num-node { fill: #ffe1e1; stroke: #e9967a; stroke-width: 2.5; }
    .text { fill: #333333; font-family: monospace; font-size: 22px; font-weight: bold; text-anchor: middle; dominant-baseline: central; }
  </style>
</defs>
<line class="edge" x1="260" y1="50" x2="100" y2="140"/>
<circle class="op-node" cx="260" cy="50" r="24"/>
<text class="text" x="260" y="50">+</text>
<circle class="num-node" cx="100" cy="140" r="24"/>
<text class="text" x="100" y="140">a</text>
```

### Ejemplo de árbol binario (dark)

```xml
<defs>
  <style>
    .edge { stroke: #e0e0e0; stroke-width: 2; fill: none; }
    .op-node { fill: #2d3748; stroke: #63b3ed; stroke-width: 2.5; }
    .num-node { fill: #4a5568; stroke: #fc8181; stroke-width: 2.5; }
    .text { fill: #e0e0e0; font-family: monospace; font-size: 22px; font-weight: bold; text-anchor: middle; dominant-baseline: central; }
  </style>
</defs>
<line class="edge" x1="260" y1="50" x2="100" y2="140"/>
<circle class="op-node" cx="260" cy="50" r="24"/>
<text class="text" x="260" y="50">+</text>
<circle class="num-node" cx="100" cy="140" r="24"/>
<text class="text" x="100" y="140">a</text>
```

---

## Reglas de Archivos

1. **Siempre crear versión light y dark**: cada diagrama debe tener `_light.svg` y `_dark.svg`
2. Ubicación: `contenidos/_static/figures/`
3. Nomenclatura: descriptiva, minúsculas, guiones si es necesario

## Workflow para Crear Diagramas Light/Dark

### Paso 1: Crear versión Light (Tonos Pasteles Claros)

1. Usar fondo `#f0f2f5`
2. Usar fills pastel claros para nodos (ej: `#e1f5ff`, `#ffe1e1`, `#e1ffe1`)
3. Usar strokes de colores medios (ej: `#4682b4`, `#e9967a`)
4. Usar texto `#333333`

### Paso 2: Crear versión Dark (basada en la Light)

1. **Copiar** el archivo `_light.svg` y renombrar a `_dark.svg`
2. **Invertir fondo**: `#f0f2f5` → `#1e1e1e`
3. **Ajustar fills de nodos**: usar versiones oscuras (ej: `#2d3748`, `#4a5568`)
4. **Mantener strokes**: mismos colores brillante pastel (ej: `#63b3ed`, `#fc8181`)
5. **Invertir texto**: `#333333` → `#e0e0e0`
6. **Ajustar elementos inline** (atributos directo en elementos, no clases):
   - Cambiar `fill` y `stroke` explícitos
   - Ajustar `fill` de elementos de texto

<example>
Ejemplo de transformación Light → Dark para un diagrama simple de dos nodos:

```xml
<!-- Light: fondo #f0f2f5, texto #333333, nodos pastel -->
<rect width="100%" height="100%" fill="#f0f2f5"/>
<rect class="variable-node" x="20" y="50" width="80" height="40" rx="5"/>
<text class="code" x="60" y="75">x</text>
<rect class="value-node" x="140" y="50" width="80" height="40" rx="5"/>
<text class="code" x="180" y="75">42</text>
<line class="arrow" x1="100" y1="70" x2="140" y2="70"/>
```

```xml
<!-- Dark: fondo #1e1e1e, texto #e0e0e0, nodos oscuros -->
<rect width="100%" height="100%" fill="#1e1e1e"/>
<rect class="variable-node" x="20" y="50" width="80" height="40" rx="5"/>
<text class="code" x="60" y="75">x</text>
<rect class="value-node" x="140" y="50" width="80" height="40" rx="5"/>
<text class="code" x="180" y="75">42</text>
<line class="arrow" x1="100" y1="70" x2="140" y2="70"/>
```
</example>

## Estructura de Diagramas

Orden recomendado:

1. `<defs>` con `<style>` y `<marker>`
2. `<rect>` de fondo
3. `<text>` título
4. Grupos `<g>` con elementos del diagrama

<verification>
Antes de dar por terminado un SVG, verificá que:

- [ ] Existen `_light.svg` y `_dark.svg`
- [ ] Ambos archivos tienen `<defs>` con `<style>` y clases CSS correctas
- [ ] El nombre de clase `.code-example` usa guión, no guión bajo
- [ ] Los colores de fondo, texto y nodos corresponden al theme
- [ ] Los strokes se mantienen brillantes en ambos themes
- [ ] Los textos son idénticos en light y dark (solo cambian colores)
- [ ] Las flechas tienen `marker-end` apuntando a `#arrowhead`
</verification>

## Cuándo Usar Este Skill

Usar este skill cuando:

- Se pide crear un nuevo diagrama SVG
- Se modifica un diagrama existente
- Se adapta un diagrama de otro formato a SVG
