---
name: applet-javascript
description: Crea applets HTML/JS autocontenidos para visualización interactiva en el apunte AyP2
license: CC-BY-SA-4.0
compatibility: opencode
---

<role>
Sos un desarrollador de applets HTML/CSS/JS autocontenidos para el apunte "Algoritmos y Programación 2" de la UNTREF.
Creás applets interactivos (recorridos de árbol, estructuras, algoritmos) que se renderizan sin scrollbars
y se integran vía `{iframe}` de MyST tanto en HTML como en PDF (con placeholder).
</role>

<context>
Los applets son archivos HTML únicos (sin dependencias externas) ubicados en `contenidos/_static/applets/`.
Se embeben en el apunte con el directive `{iframe}` de MyST.
Para el PDF se necesita una imagen placeholder PNG.
La carpeta `_static/applets/` debe estar declarada en `myst.yml` como `project.static_files`.
</context>

## Estructura del HTML

### Documento

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Título Descriptivo</title>
<style>
  /* Todo el CSS inline */
</style>
</head>
<body>
  <!-- Layout: applet → header + main(tree + sidebar) + info -->
  <script>
    // Todo el JavaScript inline
  </script>
</body>
</html>
```

### Layout base (ocupar todo el viewport sin scroll)

```css
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--fg);font-family:system-ui,-apple-system,sans-serif;font-size:14px;line-height:1.5;height:100vh;overflow:hidden;display:flex;flex-direction:column}

.applet{display:flex;flex-direction:column;padding:8px;gap:6px;width:100%;max-width:100%;margin:0 auto;flex:1;min-height:0;overflow:hidden}

.header{font-size:14px;font-weight:700;text-align:center;padding:4px 12px;background:var(--btn-bg);border-radius:6px;border:1px solid var(--border);width:100%;flex-shrink:0}

.main{display:flex;flex:1;min-height:0;gap:8px;width:100%;overflow:hidden}

.sidebar{display:flex;flex-direction:column;gap:8px;flex-shrink:0;width:auto;min-width:120px;justify-content:center}

.info{padding:6px 10px;border:1px solid var(--border);border-radius:6px;width:100%;display:flex;flex-wrap:wrap;gap:3px 12px;align-items:baseline;font-size:12px;flex-shrink:0}
.info .seq{flex:1 1 100%;font-family:'Courier New',monospace;font-size:13px;min-height:1.3em;word-break:break-all}
.info .meta{display:flex;gap:12px;flex-wrap:wrap}
.info .meta span{white-space:nowrap}
```

## Distribución (Tree a la izquierda, Controles a la derecha)

El layout horizontal evita scrollbars porque el árbol ocupa el espacio sobrante vertical:

```
+--------------------------------------------------+
|                    Header                          |
+----------------------------------+----------------+
|                                  | ⏮ ◀ ▶ ▶▶    |
|           Tree SVG               | Vel: [===]    |
|          (flex: 1)               |                |
|                                  | ● No visitado  |
|                                  | ● En proceso   |
|                                  | ● Procesado    |
+----------------------------------+----------------+
|           Info (secuencia + paso)                 |
+--------------------------------------------------+
```

### HTML del layout

```html
<div class="applet" id="app">
  <div class="header" id="header">Título del Recorrido</div>
  <div class="main">
    <div class="tree-wrap"><svg id="tree" viewBox="0 0 W H" xmlns="http://www.w3.org/2000/svg"></svg></div>
    <div class="sidebar">
      <div class="controls">
        <button id="btnStart" title="Ir al inicio">⏮</button>
        <button id="btnPrev" title="Paso anterior">◀</button>
        <button id="btnNext" title="Paso siguiente">▶</button>
        <button id="btnPlay" title="Reproducción automática">▶▶</button>
        <div class="speed-wrap">
          <label for="speed">Vel:</label>
          <input type="range" id="speed" min="400" max="3000" value="1500" step="100">
          <span id="speedLabel">1.5s</span>
        </div>
      </div>
      <div class="legend">
        <div class="legend-item"><span class="legend-dot idle"></span> No visitado</div>
        <div class="legend-item"><span class="legend-dot enter"></span> En proceso</div>
        <div class="legend-item"><span class="legend-dot done"></span> Procesado</div>
      </div>
    </div>
  </div>
  <div class="info">
    <div class="seq" id="seq"><span class="pending">[ ]</span></div>
    <div class="meta">
      <span id="stepLabel">Paso 0 / 0</span>
      <span id="actionLabel">—</span>
    </div>
  </div>
</div>
```

## Altura del iframe

Medir la altura total del applet sumando:

```
body: 100vh (igual al height del iframe)
.applet padding: 8px top + 8px bottom = 16px
gap (header–main) + gap (main–info) = 12px (2 × 6px)
header: ~30px
info: ~32px
total fijo: ~90px
main (tree + sidebar): iframe_height - 90
```

El SVG se escala automáticamente al espacio disponible vía `flex: 1`.
Usar `:height: 560px` en el `{iframe}` como valor base, ajustable ±30px.

## SVG del árbol

### ViewBox y escalado

```css
.tree-wrap{flex:1;min-width:0;display:flex;justify-content:center;align-items:center;overflow:hidden}
.tree-wrap svg{width:100%;height:100%}
```

El SVG usa `preserveAspectRatio="xMidYMid meet"` (default). El `viewBox` debe coincidir con las coordenadas de nodos y aristas. Ejemplo para árbol de 7 nodos:

```js
const tree = {
  id:'+', val:'+', type:'op',
  x:260, y:50,
  left:{ id:'a', val:'a', type:'num', x:100, y:140, left:null, right:null },
  right:{
    id:'*', val:'*', type:'op', x:400, y:140,
    left:{
      id:'-', val:'−', type:'op', x:280, y:230,
      left:{ id:'b', val:'b', type:'num', x:210, y:320, left:null, right:null },
      right:{ id:'c', val:'c', type:'num', x:350, y:320, left:null, right:null }
    },
    right:{ id:'d', val:'d', type:'num', x:460, y:230, left:null, right:null }
  }
};

const edges = [
  {x1:260,y1:50,x2:100,y2:140},
  {x1:260,y1:50,x2:400,y2:140},
  {x1:400,y1:140,x2:280,y2:230},
  {x1:400,y1:140,x2:460,y2:230},
  {x1:280,y1:230,x2:210,y2:320},
  {x1:280,y1:230,x2:350,y2:320}
];
```

Coordenadas para `viewBox="0 0 520 380"` con radio `R=28`.

### Nodos SVG

```js
const R = 28;

edges.forEach(e => {
  const line = document.createElementNS(SVG_NS, 'line');
  line.setAttribute('x1', e.x1); line.setAttribute('y1', e.y1);
  line.setAttribute('x2', e.x2); line.setAttribute('y2', e.y2);
  line.classList.add('tree-edge');
  svg.appendChild(line);
});

allNodes.forEach(n => {
  const g = document.createElementNS(SVG_NS, 'g');
  g.id = 'node-' + n.id;
  const circle = document.createElementNS(SVG_NS, 'circle');
  circle.setAttribute('cx', n.x);
  circle.setAttribute('cy', n.y);
  circle.setAttribute('r', R);
  circle.classList.add('node-circle', n.type === 'op' ? 'op' : 'num');
  g.appendChild(circle);
  const text = document.createElementNS(SVG_NS, 'text');
  text.setAttribute('x', n.x);
  text.setAttribute('y', n.y);
  text.classList.add('node-text');
  text.textContent = n.val;
  g.appendChild(text);
  svg.appendChild(g);
});
```

### CSS de nodos SVG

```css
.tree-edge{stroke:var(--border);stroke-width:2}

.node-text{fill:var(--fg);font-family:monospace;font-size:16px;font-weight:700;text-anchor:middle;dominant-baseline:central;pointer-events:none}

.node-circle.num{fill:var(--node-num-fill);stroke:var(--node-num-stroke);stroke-width:2.5}
.node-circle.op{fill:var(--node-op-fill);stroke:var(--node-op-stroke);stroke-width:2.5}
.node-circle.enter{fill:var(--node-enter-bg);stroke:var(--node-enter-stroke)}
.node-circle.done{fill:var(--node-done-bg);stroke:var(--node-done-stroke)}
```

### Colores de nodos por tipo y estado

| Estado         | Light fill  | Light stroke | Dark fill | Dark stroke |
|----------------|------------|--------------|-----------|-------------|
| Num (idle)     | `#ffe1e1`  | `#e9967a`    | `#4a5568` | `#fc8181`   |
| Op  (idle)     | `#e1f5ff`  | `#4682b4`    | `#2d3748` | `#63b3ed`   |
| Enter (activo) | `#fff3cd`  | `#ffc107`    | `#5a4a00` | `#ffc107`   |
| Done (procesado)| `#d4edda` | `#28a745`    | `#1e3a2f` | `#48c774`   |

## Controles

### Botones

```css
.controls{display:flex;flex-direction:row;gap:4px;flex-wrap:wrap;justify-content:center}
.controls button{width:38px;height:32px;border:1px solid var(--border);border-radius:6px;background:var(--btn-bg);color:var(--btn-text);font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background 0.15s;padding:0}
.controls button:hover:not(:disabled){background:var(--btn-hover)}
.controls button:active:not(:disabled){background:var(--btn-active)}
.controls button:disabled{opacity:0.4;cursor:default}
```

### Velocidad

```css
.speed-wrap{display:flex;align-items:center;gap:3px;font-size:11px;flex:1 1 100%;justify-content:center;white-space:nowrap}
.speed-wrap input[type=range]{width:48px;height:4px;accent-color:var(--highlight)}
```

### Leyenda

```css
.legend{display:flex;flex-direction:column;gap:3px;font-size:11px;align-items:flex-start}
.legend-item{display:flex;align-items:center;gap:4px}
.legend-dot{width:12px;height:12px;border-radius:50%;border:2px solid;flex-shrink:0}
```

## Generación de pasos (recorridos)

Función generadora para preorden/inorden/postorden:

```js
function* genSteps(node, type) {
  if (!node) return;
  yield {action:'enter', node};
  if (type === 'preorder') yield {action:'process', node};
  yield* genSteps(node.left, type);
  if (type === 'inorder') {
    yield {action:'enter', node};
    yield {action:'process', node};
  }
  yield* genSteps(node.right, type);
  if (type === 'postorder') {
    yield {action:'enter', node};
    yield {action:'process', node};
  }
}
```

Construir arreglo de pasos agregando estado:

```js
function buildSteps(root, type) {
  const raw = [];
  for (const s of genSteps(root, type)) raw.push(s);
  const steps = [];
  const processed = new Set();
  const seq = [];
  let currentId = null;
  for (const s of raw) {
    if (s.action === 'enter') currentId = s.node.id;
    else if (s.action === 'process') {
      processed.add(s.node.id);
      seq.push(s.node.val);
      currentId = s.node.id;
    }
    steps.push({
      currentNode: currentId,
      processed: new Set(processed),
      seq: [...seq],
      node: s.node,
      action: s.action
    });
  }
  steps.push({currentNode:null, processed:new Set(processed), seq:[...seq], node:null, action:'done'});
  return steps;
}
```

### Estados de nodo

- `enter` (amarillo): se llamó a la función con ese nodo
- `process` (verde): se procesó/visitó el nodo
- El retroceso es implícito (no se renderiza)

## Dispatcher por archivo separado

Cada variante del applet es un archivo independiente con el tipo hardcodeado.
No se usa query string ni regex sobre el filename.

```js
const TRAVERSALS = {
  preorden: {
    label: 'Preorden (Raíz → Izquierda → Derecha)',
    order: ['+', 'a', '*', '-', 'b', 'c', 'd']
  },
  inorden: {
    label: 'Inorden (Izquierda → Raíz → Derecha)',
    order: ['a', '+', 'b', '-', 'c', '*', 'd']
  },
  postorden: {
    label: 'Postorden (Izquierda → Derecha → Raíz)',
    order: ['a', 'b', 'c', '-', 'd', '*', '+']
  }
};

const tipo = 'preorden';  // hardcodeado según el archivo
```

Archivos generados:

```
recorridos-arbol-preorden_light.html   → const tipo = 'preorden';
recorridos-arbol-preorden_dark.html    → const tipo = 'preorden';
recorridos-arbol-inorden_light.html    → const tipo = 'inorden';
recorridos-arbol-inorden_dark.html     → const tipo = 'inorden';
recorridos-arbol-postorden_light.html  → const tipo = 'postorden';
recorridos-arbol-postorden_dark.html   → const tipo = 'postorden';
```

## Atajos de teclado

```js
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT') return;
  if (e.key === 'ArrowRight') { e.preventDefault(); next(); }
  if (e.key === 'ArrowLeft') { e.preventDefault(); prev(); }
  if (e.key === ' ') { e.preventDefault(); togglePlay(); }
  if (e.key === 'Home') { e.preventDefault(); start(); }
});
```

## Modo oscuro

La página usa `data-theme="dark"` o clase `.dark` en `<html>` para cambiar a modo oscuro
(no usa `prefers-color-scheme`). Como los iframes no heredan esto, se necesitan
versiones `-dark.html` separadas.

### Crear versión dark

1. Copiar el archivo light a `*_dark.html`
2. Reemplazar los colores de `:root` con los valores dark (desde `@media (prefers-color-scheme:dark)`)
3. Eliminar el bloque `@media (prefers-color-scheme:dark)` por completo

### Archivos generados

```
applets/X-tema/X-Y-tema/
├── mi-applet-preorden_light.html        (light)
├── mi-applet-preorden_dark.html         (dark, colores oscuros forzados)
├── mi-applet-inorden_light.html         (light)
├── mi-applet-inorden_dark.html          (dark)
└── ...
```

El sufijo `_light` o `_dark` va al final, antes de la extensión, siguiendo la
convención de las figuras SVG (`Arbol_light.svg`, `Arbol_dark.svg`).

```css
:root {
  --bg: #ffffff;
  --fg: #1a1a2e;
  --border: #d1d5db;
  --btn-bg: #f3f4f6;
  --btn-hover: #e5e7eb;
  --btn-active: #d1d5db;
  --btn-disabled: #e5e7eb;
  --btn-text: #374151;
  --highlight: #1d4ed8;
  --seq-done: #059669;
  --seq-pending: #9ca3af;
  /* colores de nodos en sección correspondiente */
}
@media (prefers-color-scheme:dark) {
:root {
  --bg: #1a1b2e;
  --fg: #e0e0e0;
  --border: #374151;
  --btn-bg: #2d3748;
  --btn-hover: #374151;
  --btn-active: #4a5568;
  --btn-disabled: #1f2937;
  --btn-text: #e0e0e0;
  --highlight: #60a5fa;
  --seq-done: #48c774;
  --seq-pending: #6b7280;
}
}
```

## Organización de archivos

Los applets se ubican en `contenidos/_static/applets/`, con subdirectorio por capítulo
siguiendo el mismo patrón que las figuras:

```
contenidos/_static/applets/
├── 3-estructuras-de-datos/
│   └── 3-8-arboles/
│       ├── recorridos-arbol-preorden_light.html
│       ├── recorridos-arbol-preorden_dark.html
│       ├── recorridos-arbol-inorden_light.html
│       ├── recorridos-arbol-inorden_dark.html
│       ├── recorridos-arbol-postorden_light.html
│       └── recorridos-arbol-postorden_dark.html
├── 4-diseno-de-algoritmos/
│   └── (futuros applets)
└── ...
```

## Integración con MyST

### myst.yml

```yaml
project:
  static_files:
    - _static/applets
```

`static_files` copia recursivamente todo el árbol. No hace falta listar cada subdirectorio.
Cada vez que se modifiquen los static_files, borrar `contenidos/_build/` antes de
`myst start` o `myst build` para forzar reprocesamiento.

### Iframe en markdown (con soporte dark)

No usar `:placeholder:` — los PNG se ven mal en PDF. El applet solo funciona en HTML;
en PDF se omite (el texto circundante y las fórmulas LaTeX alcanzan).

```markdown
:::{iframe} /applets/3-estructuras-de-datos/3-8-arboles/recorridos-arbol-preorden_light.html
:width: 100%
:height: 560px
:class: only-light-mode
:::

:::{iframe} /applets/3-estructuras-de-datos/3-8-arboles/recorridos-arbol-preorden_dark.html
:width: 100%
:height: 560px
:class: only-dark-mode
:::
```

La ruta del `{iframe}` es absoluta desde la raíz del sitio (`/applets/X-tema/X-Y-tema/...`).
**Importante**: no usar query strings para parametrizar el applet, porque el browser cachea
el contenido del iframe y todas las instancias muestran el mismo valor.
En su lugar, crear un archivo separado por cada variante con el tipo hardcodeado
y el sufijo `_light`/`_dark` en el nombre:

```
recorridos-arbol-preorden_light.html   → const tipo = 'preorden';
recorridos-arbol-preorden_dark.html    → const tipo = 'preorden';
recorridos-arbol-inorden_light.html    → const tipo = 'inorden';
recorridos-arbol-inorden_dark.html     → const tipo = 'inorden';
recorridos-arbol-postorden_light.html  → const tipo = 'postorden';
recorridos-arbol-postorden_dark.html   → const tipo = 'postorden';
```
La ruta del placeholder es relativa al archivo `.md`.
El `:height:` controla el viewport del applet (el applet usa `height: 100vh` para llenarlo).

### Placeholder para PDF

Generar con Python PIL un PNG estático del tamaño del iframe (~520×560) con el título del applet y un mensaje "Applet interactivo — disponible en versión HTML":

```python
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (W, H), '#f8f9fa')
draw = ImageDraw.Draw(img)
draw.text((W//2, H//2-20), 'Applet interactivo', fill='#333', anchor='mt', font=font)
draw.text((W//2, H//2+20), 'Disponible en versión HTML', fill='#666', anchor='mt', font=font_small)
img.save('placeholder.png')
```

## Control de estados (render)

```js
function render(idx) {
  const data = (idx >= 0 && idx < steps.length) ? steps[idx] : null;
  const seqArr = data ? data.seq : [];
  const processed = data ? data.processed : new Set();
  const currId = data ? data.currentNode : null;

  // Actualizar colores de nodos SVG
  allNodes.forEach(n => {
    const g = document.getElementById('node-' + n.id);
    const circle = g.querySelector('circle');
    if (processed.has(n.id)) {
      circle.classList.add('done');
      circle.classList.remove('enter', 'idle');
    } else if (n.id === currId) {
      circle.classList.add('enter');
      circle.classList.remove('done', 'idle');
    } else {
      circle.classList.add('idle');
      circle.classList.remove('enter', 'done');
    }
  });

  // Actualizar secuencia
  if (seqArr.length === 0) {
    seqEl.innerHTML = '<span class="pending">[ ]</span>';
  } else {
    const total = TRAVERSALS[tipo].order;
    let html = '';
    total.forEach((v, i) => {
      html += `<span class="${i < seqArr.length ? 'done' : 'pending'}">${v}</span>`;
      if (i < total.length - 1) html += ' ';
    });
    seqEl.innerHTML = `[ ${html} ]`;
  }

  // Actualizar metadatos
  if (data && data.action === 'done') {
    stepLabel.textContent = `Paso ${idx+1} / ${steps.length}`;
    actionLabel.textContent = '✓ Recorrido completo';
  } else if (data) {
    stepLabel.textContent = `Paso ${idx+1} / ${steps.length}`;
    actionLabel.textContent = data.action === 'enter'
      ? `Entrar a ${data.node.val}`
      : `Procesar ${data.node.val}`;
  }

  // Estado botones
  btnStart.disabled = (idx <= 0);
  btnPrev.disabled = (idx <= 0);
  btnNext.disabled = (idx >= steps.length - 1);
}
```

## Variables globales y helpers

```js
let steps = [];
let currentStep = -1;
let playing = false;
let timer = null;
let speed = 1500;

function goTo(n) {
  if (n < 0) n = 0;
  if (n >= steps.length) n = steps.length - 1;
  currentStep = n;
  render(currentStep);
}

function next() { if (currentStep < steps.length - 1) goTo(currentStep + 1); }
function prev() { if (currentStep > 0) goTo(currentStep - 1); }
function start() { goTo(0); }

function play() {
  if (playing) return;
  if (currentStep >= steps.length - 1) goTo(0);
  playing = true;
  btnPlay.textContent = '⏸';
  function tick() {
    if (!playing) return;
    if (currentStep < steps.length - 1) { next(); timer = setTimeout(tick, speed); }
    else { stop(); }
  }
  timer = setTimeout(tick, speed);
}

function stop() {
  playing = false;
  btnPlay.textContent = '▶▶';
  if (timer) { clearTimeout(timer); timer = null; }
}

function togglePlay() { if (playing) stop(); else play(); }
```

## Verificación

- [ ] El applet ocupa todo el viewport del iframe sin scrollbars
- [ ] Layout: header + main(tree + sidebar) + info
- [ ] El árbol usa `flex: 1` para ocupar espacio sobrante
- [ ] Controles a la derecha en la sidebar (⏮ ◀ ▶ ▶▶, Vel, leyenda)
- [ ] La info (secuencia + paso) queda abajo del todo
- [ ] SVG con `viewBox` que coincide con coordenadas de nodos/aristas
- [ ] `R >= 28` para nodos visibles
- [ ] Tres recorridos vía `?tipo=preorden|inorden|postorden`
- [ ] `enter` (amarillo) → `process` (verde), retroceso implícito
- [ ] Play automático con slider de velocidad (400–3000ms)
- [ ] Atajos de teclado: ← → paso, Space play/pausa, Home inicio
- [ ] Modo claro/oscuro vía `prefers-color-scheme`
- [ ] `myst.yml` incluye `project.static_files: [_static/applets]`
- [ ] `{iframe}` usa ruta absoluta `/applets/...` y `:height:` fijo
- [ ] Placeholder PNG generado para PDF
- [ ] Borrar `_build/` al cambiar static_files
- [ ] Archivo html único sin dependencias externas
