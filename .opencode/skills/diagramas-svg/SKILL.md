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
| `.node-circle`      | Círculo de nodo en árbol binario                      | Arbol               |
| `.node-text`        | Texto dentro de nodos (monospace, 14px, bold)         | Arbol / ArbolBinario |
| `.fb-label`         | Etiqueta de factor de balanceo (sans-serif, 12px)     | AVL                 |
| `.fb-bal`           | Color verde para nodos balanceados                    | AVL                 |
| `.fb-unbal`         | Color rojo para nodos desbalanceados                  | AVL                 |
| `.annotation-text`  | Anotaciones externas (profundidad, nivel, etc.)       | Arbol               |
| `.pointer-line`     | Línea de puntero desde una anotación                  | Arbol               |
| `.pointer-arrowhead`| Punta de flecha del puntero                           | Arbol               |
| `.dashed-line`      | Línea punteada para marcar niveles/profundidad        | Arbol               |

### Colores para árboles — Light

| Elemento                         | Fill         | Stroke       | Stroke-width |
| -------------------------------- | ------------ | ------------ | ------------ |
| Nodo ABB/AVL (`node-circle`)     | `#e1f5ff`    | `#4682b4`    | 2.5          |
| Nodo operación (`op-node`)       | `#e1f5ff`    | `#4682b4`    | 2.5          |
| Nodo número (`num-node`)         | `#ffe1e1`    | `#e9967a`    | 2.5          |
| Nodo árbol genérico (`node-circle`) | `#ffe1e1`| `#e9967a`    | 20*          |
| Arista (`edge`)                  | —            | `#333333`    | 2            |
| Arista género (`tree-edge`)      | —            | `#333333`    | 18*          |
| Flecha arista                    | `#333333`    | `#333333`    | 8*           |
| Línea puntero                    | —            | `#87cfff`    | 14*          |
| Flecha puntero                   | `#e1f5ff`    | `#87cfff`    | 8*           |
| Línea punteada                   | —            | `#333333`    | 14*          |
| Texto en nodos (`node-text`)     | `#333333`    | —            | —            |
| Etiqueta fb balanceado (`fb-bal`)| `#2e8b57`    | —            | —            |
| Etiqueta fb desbalanceado (`fb-unbal`)| `#c53030`| —            | —            |
| Anotaciones                      | `#333333`    | —            | —            |

\* *Valores para viewBox `0 0 4801 3535` (Arbol). Ajustar proporcionalmente según el viewBox.*

### Colores para árboles — Dark

| Elemento                         | Fill         | Stroke       | Stroke-width |
| -------------------------------- | ------------ | ------------ | ------------ |
| Nodo ABB/AVL (`node-circle`)     | `#2d3748`    | `#63b3ed`    | 2.5          |
| Nodo operación (`op-node`)       | `#2d3748`    | `#63b3ed`    | 2.5          |
| Nodo número (`num-node`)         | `#4a5568`    | `#fc8181`    | 2.5          |
| Nodo árbol genérico (`node-circle`) | `#4a5568`| `#fc8181`    | 20*          |
| Arista (`edge`)                  | —            | `#e0e0e0`    | 2            |
| Arista género (`tree-edge`)      | —            | `#e0e0e0`    | 18*          |
| Flecha arista                    | `#e0e0e0`    | `#e0e0e0`    | 8*           |
| Línea puntero                    | —            | `#87cfff`    | 14*          |
| Flecha puntero                   | `#2d3748`    | `#87cfff`    | 8*           |
| Línea punteada                   | —            | `#e0e0e0`    | 14*          |
| Texto en nodos (`node-text`)     | `#e0e0e0`    | —            | —            |
| Etiqueta fb balanceado (`fb-bal`)| `#68d391`    | —            | —            |
| Etiqueta fb desbalanceado (`fb-unbal`)| `#fc8181`| —            | —            |
| Anotaciones                      | `#e0e0e0`    | —            | —            |

\* *Valores para viewBox `0 0 4801 3535` (Arbol). Ajustar proporcionalmente según el viewBox.*

> **Nota sobre `node-circle`**: Para árboles de búsqueda (ABB/AVL) usar la fila azul (como `op-node`). La fila roja es para árboles genéricos sin relación de orden.

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

### Convenciones para árboles binarios de búsqueda (ABB/AVL)

Los diagramas de ABB y AVL siguen convenciones específicas para que todos los árboles del apunte tengan el mismo estilo visual.

#### Estilo de nodos

| Propiedad          | Light                       | Dark                        |
| ------------------ | --------------------------- | --------------------------- |
| Fill               | `#e1f5ff`                   | `#2d3748`                   |
| Stroke             | `#4682b4` (ancho 2.5)       | `#63b3ed` (ancho 2.5)       |
| Forma              | Círculo, `r="18"`           | Círculo, `r="18"`           |
| Texto interior     | Monospace 14px bold         | Monospace 14px bold         |
| Color texto        | `#333333`                   | `#e0e0e0`                   |

Usar clases `.node-circle` y `.node-text`.

#### Etiquetas de factor de balanceo (AVL)

Colocar la etiqueta `fb = X` junto a cada nodo:

| Etiqueta        | Clase      | Light     | Dark      |
| --------------- | ---------- | --------- | --------- |
| Balanceado      | `fb-bal`   | `#2e8b57` | `#68d391` |
| Desbalanceado   | `fb-unbal` | `#c53030` | `#fc8181` |

Posicionamiento:
- **Derecha del nodo**: `x="cx + r + 6"` con `text-anchor: start` (default)
- **Izquierda del nodo**: `x="cx - r - 6"` con `style="text-anchor: end"` (cuando la etiqueta derecha se superpone con otro nodo)

Usar fuente `sans-serif` 12px bold con clase `.fb-label`.

#### ViewBox por defecto

Usar **`0 0 700 360`** como viewBox base para diagramas de árboles binarios de 5 niveles (ABB/AVL). Para árboles más pequeños (3-4 niveles) se puede reducir la altura a `300` o `280`, pero **mantener el ancho en `700`** para que la escala sea consistente con el resto del capítulo.

**Importante**: si el viewBox es demasiado pequeño (ej. `400×220`), el árbol se ve desproporcionadamente grande al renderizarse sin `width` fijo. Usar `700` de ancho da el mismo factor de escala que los AVL del capítulo 3-10, que no usan `width` explícito.

#### Disposición de niveles

Para que el árbol sea legible y muestre claramente la relación padre-hijo izquierdo/derecho:

1. **Los hijos deben desplazarse diagonalmente** del padre, nunca alineados verticalmente
2. **Separación vertical decreciente** a medida que se baja de nivel (ej: 70→65→60→55px entre niveles 0→1→2→3→4)
3. **Ocupar todo el ancho** del viewBox, espaciando los nodos para que no se superpongan
4. **El árbol debe ser un BST válido**: cada nodo debe estar en la posición correcta según su valor y el orden del árbol

Ejemplo de separaciones para 5 niveles (viewBox `0 0 700 360`):
```
Nivel 0 → Nivel 1: Δy = 70px
Nivel 1 → Nivel 2: Δy = 65px
Nivel 2 → Nivel 3: Δy = 60px
Nivel 3 → Nivel 4: Δy = 55px
```

Desplazamiento horizontal (restar para hijo izquierdo, sumar para hijo derecho):
```
Nivel 0 → Nivel 1: ±130-150px
Nivel 1 → Nivel 2: ±75-90px
Nivel 2 → Nivel 3: ±45-55px
Nivel 3 → Nivel 4: ±25-30px
```

Ajustar según la cantidad de nodos y el viewBox.

#### Ejemplo completo: AVL-FB

Estructura del árbol:
```
        50
      /    \
    17      76
   /  \    /
  9   23  54
   \  /    \
   14 19    72
  /        /
 12       67
```

**Light:**

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 360">
  <defs>
    <style>
      .bg { fill: #f0f2f5; }
      .edge { stroke: #333333; stroke-width: 2; fill: none; }
      .node-circle { fill: #e1f5ff; stroke: #4682b4; stroke-width: 2.5; }
      .node-text { fill: #333333; font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 14px; font-weight: bold; text-anchor: middle; dominant-baseline: central; }
      .fb-label { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; font-weight: bold; text-anchor: start; dominant-baseline: central; }
      .fb-bal { fill: #2e8b57; }
      .fb-unbal { fill: #c53030; }
    </style>
  </defs>

  <rect class="bg" width="700" height="360" rx="8"/>

  <line class="edge" x1="350" y1="45" x2="200" y2="115"/>
  <line class="edge" x1="350" y1="45" x2="500" y2="115"/>
  <line class="edge" x1="200" y1="115" x2="110" y2="180"/>
  <line class="edge" x1="200" y1="115" x2="290" y2="180"/>
  <line class="edge" x1="500" y1="115" x2="410" y2="180"/>
  <line class="edge" x1="110" y1="180" x2="165" y2="240"/>
  <line class="edge" x1="290" y1="180" x2="235" y2="240"/>
  <line class="edge" x1="410" y1="180" x2="465" y2="240"/>
  <line class="edge" x1="165" y1="240" x2="135" y2="295"/>
  <line class="edge" x1="465" y1="240" x2="435" y2="295"/>

  <circle class="node-circle" cx="350" cy="45" r="18"/><text class="node-text" x="350" y="45">50</text>
  <text class="fb-label fb-bal" x="376" y="41">fb = 0</text>

  <circle class="node-circle" cx="200" cy="115" r="18"/><text class="node-text" x="200" y="115">17</text>
  <text class="fb-label fb-bal" x="226" y="111">fb = +1</text>

  <circle class="node-circle" cx="500" cy="115" r="18"/><text class="node-text" x="500" y="115">76</text>
  <text class="fb-label fb-unbal" x="526" y="111">fb = +3</text>

  <circle class="node-circle" cx="110" cy="180" r="18"/><text class="node-text" x="110" y="180">9</text>
  <text class="fb-label fb-unbal" x="136" y="176">fb = -2</text>

  <circle class="node-circle" cx="290" cy="180" r="18"/><text class="node-text" x="290" y="180">23</text>
  <text class="fb-label fb-bal" x="316" y="176">fb = +1</text>

  <circle class="node-circle" cx="410" cy="180" r="18"/><text class="node-text" x="410" y="180">54</text>
  <text class="fb-label fb-unbal" x="436" y="176">fb = -2</text>

  <circle class="node-circle" cx="165" cy="240" r="18"/><text class="node-text" x="165" y="240">14</text>
  <text class="fb-label fb-bal" x="141" y="236" style="text-anchor: end;">fb = +1</text>

  <circle class="node-circle" cx="235" cy="240" r="18"/><text class="node-text" x="235" y="240">19</text>
  <text class="fb-label fb-bal" x="261" y="236">fb = 0</text>

  <circle class="node-circle" cx="465" cy="240" r="18"/><text class="node-text" x="465" y="240">72</text>
  <text class="fb-label fb-bal" x="491" y="236">fb = +1</text>

  <circle class="node-circle" cx="135" cy="295" r="18"/><text class="node-text" x="135" y="295">12</text>
  <text class="fb-label fb-bal" x="161" y="291">fb = 0</text>

  <circle class="node-circle" cx="435" cy="295" r="18"/><text class="node-text" x="435" y="295">67</text>
  <text class="fb-label fb-bal" x="461" y="291">fb = 0</text>
</svg>
```

**Dark:** mismas coordenadas, cambiar colores según tabla Dark de árboles.

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
