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

## Distribución (Árbol a la izquierda, Controles a la derecha)

El layout horizontal evita scrollbars porque el árbol ocupa el espacio sobrante vertical:

```
+--------------------------------------------------+
|                    Header                          |
+----------------------------------+----------------+
|                                  | [Insertar]     |
|                                  | [Buscar  ]     |
|          Árbol                   | Valor: [___] ↵ |
|         (flex: 1)                | [Vaciar árbol] |
|                                  | ────────────── |
|                                  | ⏮ ◀ ▶ >>     |
|                                  | Vel: [===] p/s |
|                                  | ────────────── |
|                                  | ● No visitado  |
|                                  | ● Comparando   |
|                                  | : etc.         |
+----------------------------------+----------------+
|           Info (descripción + paso)               |
+--------------------------------------------------+
```

### HTML del layout (estándar para applets con inserción/búsqueda)

```html
<div class="applet">
  <div class="header">Título del Applet</div>
  <div class="main">
    <div class="tree-wrap"><canvas id="treeCanvas"></canvas></div>
    <div class="sidebar">
      <div class="modes" id="modeSelector">
        <button class="mode-btn active" data-mode="insert">Insertar</button>
        <button class="mode-btn" data-mode="search">Buscar</button>
      </div>
      <div class="input-group">
        <label for="valInput">Valor:</label>
        <div class="input-row">
          <input type="text" id="valInput" placeholder="Ej: 10,20,30" autofocus>
          <span class="enter-hint">↵</span>
        </div>
        <button id="btnClear" class="clear-btn">Vaciar árbol</button>
      </div>
      <div class="separator"></div>
      <div class="controls">
        <button id="btnFirst" title="Ir al inicio">⏮</button>
        <button id="btnPrev" title="Paso anterior">◀</button>
        <button id="btnNext" title="Paso siguiente">▶</button>
        <button id="btnSkip" title="Reproducir automático">>></button>
      </div>
      <div class="speed-wrap">
        <label for="speedSlider">Vel:</label>
        <input type="range" id="speedSlider" min="400" max="3000" value="1500" step="100">
        <span id="speedLabel">0.5 p/s</span>
      </div>
      <div class="separator"></div>
      <div class="legend">
        <div class="legend-item"><span class="legend-dot idle"></span> No visitado</div>
        <div class="legend-item"><span class="legend-dot highlight"></span> Comparando</div>
        <div class="legend-item"><span class="legend-dot inserted"></span> Insertado</div>
        <div class="legend-item"><span class="legend-dot error"></span> Desbalance</div>
        <div class="legend-item"><span class="legend-dot rot"></span> Rotando</div>
      </div>
    </div>
  </div>
  <div class="info">
    <div class="path" id="desc">Mensaje de estado inicial.</div>
    <div class="meta">
      <span id="stepCounter">Paso — / —</span>
      <span id="treeInfo">—</span>
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

## Interfaz de control estándar

Todos los applets deben seguir esta interfaz de control unificada para mantener consistencia visual y funcional.

### Modos de operación

Selector de modo como botones (no radio buttons). El activo se pinta con `--mode-active-bg` (azul).

```css
.modes{display:flex;gap:2px}
.modes button{flex:1;padding:4px 6px;border:1px solid var(--border);border-radius:4px;background:var(--btn-bg);color:var(--btn-text);font-size:11px;cursor:pointer;font-weight:600;transition:background .15s}
.modes button.active{background:var(--mode-active-bg);color:var(--mode-active-text);border-color:var(--mode-active-bg)}
.modes button:hover:not(.active){background:var(--btn-hover)}
```

```js
var modeBtns=document.querySelectorAll('#modeSelector button');
modeBtns.forEach(function(b){
  b.addEventListener('click',function(){
    if(isPlaying)return;
    modeBtns.forEach(function(x){x.classList.remove('active');});
    b.classList.add('active');
    currentMode=b.dataset.mode;
  });
});
```

### Input de valores

Acepta valores separados por coma. Muestra ↵ como hint visual.

```css
.input-group{display:flex;flex-direction:column;gap:4px;font-size:12px}
.input-row{display:flex;align-items:center;gap:4px}
.input-row input{flex:1;padding:4px 6px;border:1px solid var(--border);border-radius:4px;background:var(--bg);color:var(--fg);font-size:14px;width:100%}
.enter-hint{font-size:14px;color:var(--slot-stroke);flex-shrink:0}
.clear-btn{width:100%;padding:4px 8px;border:1px solid var(--error-stroke);border-radius:4px;background:transparent;color:var(--error-stroke);font-size:11px;cursor:pointer;font-weight:600;transition:background .15s}
.clear-btn:hover{background:var(--error-fill)}
```

### Separador

```css
.separator{height:1px;background:var(--border);margin:2px 0}
```

### Navegación

Botones: ⏮ (ir al inicio), ◀ (paso anterior), ▶ (paso siguiente), >> (reproducción automática).
El botón >> cambia a ⏸ mientras reproduce.

```css
.controls{display:flex;flex-direction:row;gap:4px;flex-wrap:wrap;justify-content:center}
.controls button{width:36px;height:30px;border:1px solid var(--border);border-radius:6px;background:var(--btn-bg);color:var(--btn-text);font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .15s;padding:0}
.controls button:hover:not(:disabled){background:var(--btn-hover)}
.controls button:active:not(:disabled){background:var(--btn-active)}
.controls button:disabled{opacity:.4;cursor:default}
.controls button.playing{background:var(--error-stroke);color:#fff;border-color:var(--error-stroke)}
.controls button.playing:hover{filter:brightness(1.1)}
```

```js
function updateBtns(){
  var atS=currentStep<=0,atE=currentStep>=steps.length-1,hasS=steps.length>0;
  btnFirst.disabled=atS||!hasS||isPlaying;
  btnPrev.disabled=atS||!hasS||isPlaying;
  btnNext.disabled=(!hasS&&pendingValues.length===0)||(atE&&pendingValues.length===0)||isPlaying;
  btnSkip.disabled=pendingValues.length===0&&atE;
}
```

### Velocidad (pasos por segundo)

Slider invertido: `speedVal = 3400 - slider.value`. A izquierda = lento (0.3 p/s), a derecha = rápido (2.5 p/s).
Solo afecta a la reproducción automática (>>).

```css
.speed-wrap{display:flex;align-items:center;gap:3px;font-size:11px;flex:1 1 100%;justify-content:center;white-space:nowrap}
.speed-wrap input[type=range]{width:48px;height:4px;accent-color:var(--highlight)}
```

```js
var speedVal=1900;
speedSlider.addEventListener('input',function(){
  speedVal=3400-parseInt(this.value);
  speedLabel.textContent=(1000/speedVal).toFixed(1)+' p/s';
  if(isPlaying){stopPlay();startPlay();}
});
```

### Cola de operaciones

Cuando el usuario ingresa varios valores separados por coma, se encolan y se procesan uno por uno al presionar ▶ o >>.

```js
var pendingValues=[];

function parseAndEnq(inp){
  var nums=inp.split(',').map(function(s){return s.trim()}).filter(function(s){return s.length>0}).map(function(s){return parseInt(s,10)}).filter(function(n){return Number.isInteger(n)&&n>0});
  if(nums.length===0){descEl.textContent='⚠ Ingresá números enteros positivos separados por coma.';return;}
  pendingValues.push.apply(pendingValues,nums);
  valInput.value='';
  descEl.textContent=nums.length+' valor'+(nums.length!==1?'es':'')+' encolado'+(nums.length!==1?'s':'')+'. Usá ▶ o >> para procesar'+(nums.length!==1?'los':'lo')+'.';
  updateBtns();
}
```

### Auto‑play (>>)

```js
var isPlaying=false;
var playTimer=null;

function tick(){
  if(!isPlaying)return;
  if(currentStep>=steps.length-1){
    if(pendingValues.length>0){var val=pendingValues.shift();procIns(val);}
    else{stopPlay();return;}
  }
  if(currentStep<steps.length-1){goNext();playTimer=setTimeout(tick,speedVal);}
  else stopPlay();
}
function startPlay(){
  if(currentStep>=steps.length-1&&pendingValues.length===0)return;
  isPlaying=true;
  btnSkip.textContent='⏸';btnSkip.classList.add('playing');
  updateBtns();
  playTimer=setTimeout(tick,speedVal);
}
function stopPlay(){
  isPlaying=false;
  if(playTimer){clearTimeout(playTimer);playTimer=null;}
  btnSkip.textContent='>>';btnSkip.classList.remove('playing');
  updateBtns();
}
function hdlSkip(){
  if(isPlaying){stopPlay();return;}
  if(currentStep>=steps.length-1&&pendingValues.length===0)return;
  startPlay();
}
```

### Atajos de teclado

```js
document.addEventListener('keydown',function(e){
  if(e.target.tagName==='INPUT')return;
  if(e.key==='ArrowRight'){e.preventDefault();hdlNext();}
  if(e.key==='ArrowLeft'){e.preventDefault();goPrev();}
  if(e.key==='Home'){e.preventDefault();goFirst();}
  if(e.key===' '||e.key==='End'){e.preventDefault();hdlSkip();}
});
```

### Info (barra inferior)

```css
.info{padding:6px 10px;border:1px solid var(--border);border-radius:6px;width:100%;display:flex;flex-wrap:wrap;gap:3px 12px;align-items:baseline;font-size:12px;flex-shrink:0}
.info .path{flex:1 1 100%;font-family:'Courier New',monospace;font-size:13px;min-height:1.3em;word-break:break-all}
.info .meta{display:flex;gap:12px;flex-wrap:wrap}
.info .meta span{white-space:nowrap}
```

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

## Dibujo dinámico con Canvas

Para applets donde la estructura crece/modifica dinámicamente (inserción AVL, ABB, etc.),
se usa `<canvas>` en lugar de SVG. En cada paso se recalcula el layout del árbol completo
para que los nodos se redistribuyan según el tamaño actual del canvas.

### Canvas con HiDPI

```css
.tree-wrap canvas{width:100%;height:100%}
```

```js
var canvas=document.getElementById('treeCanvas');
var ctx=canvas.getContext('2d');

function resizeCanvas(){
  var rect=canvas.parentElement.getBoundingClientRect();
  var dpr=window.devicePixelRatio||1;
  canvas.width=rect.width*dpr;canvas.height=rect.height*dpr;
  canvas.style.width=rect.width+'px';canvas.style.height=rect.height+'px';
  canvas._w=rect.width;canvas._h=rect.height;
  ctx.setTransform(dpr,0,0,dpr,0,0);
}
window.addEventListener('resize',resizeCanvas);
```

### Layout dinámico (in-order)

Cada nodo guarda `px`, `py` (posición calculada). El layout se recalcula desde cero
en cada `drawTree()` usando un recorrido in-order para distribuir horizontalmente
y la profundidad para la vertical:

```js
var NODE_R=18;     // radio del nodo
var LEVEL_H=65;    // separación vertical entre niveles

function countN(n){return n?1+countN(n.left)+countN(n.right):0}

function layL(n,d,p){
  if(!n)return;
  layL(n.left,d+1,p);
  n._in=p.c++;   // orden in-order
  n._dep=d;       // profundidad
  layL(n.right,d+1,p);
}

function layT(tree,w,h){
  if(!tree)return;
  var total=countN(tree);if(!total)return;
  layL(tree,0,{c:0});
  var mx=30,my=30,xR=w-2*mx;                         // márgenes
  var mD=function md(n){return n?1+Math.max(md(n.left),md(n.right)):0}(tree);
  var sY=Math.min(LEVEL_H,(h-2*my)/Math.max(mD,1));  // separación vertical
  (function pn(n){
    if(!n)return;
    n.px=mx+(total>1?(n._in/(total-1))*xR:w/2-mx);  // posición X según orden
    n.py=my+n._dep*sY;                                 // posición Y según profundidad
    pn(n.left);pn(n.right);
  })(tree);
}
```

Esto asegura que el árbol siempre ocupe el espacio disponible sin solapamientos,
adaptándose a cualquier cantidad de nodos.

### Dibujar el árbol (aristas + nodos + balanceo)

```js
var cssVar=function(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim()};

function drawTree(tree,highlights,bfArr){
  var w=canvas._w,h=canvas._h;
  ctx.clearRect(0,0,w,h);
  if(!tree)return;
  layT(tree,w,h);  // recalcula layout

  // Mapa de highlights y factores de balanceo
  var hlM={};if(highlights)highlights.forEach(function(h){hlM[h.id]=h.t});
  var bfM={};if(bfArr)bfArr.forEach(function(b){bfM[b.id]=b.fb});

  // 1. Aristas
  (function drE(n){
    if(!n)return;
    if(n.left){
      ctx.beginPath();ctx.moveTo(n.px,n.py);ctx.lineTo(n.left.px,n.left.py);
      ctx.strokeStyle=cssVar('--border');ctx.lineWidth=2;ctx.stroke();
      drE(n.left);
    }
    if(n.right){
      ctx.beginPath();ctx.moveTo(n.px,n.py);ctx.lineTo(n.right.px,n.right.py);
      ctx.strokeStyle=cssVar('--border');ctx.lineWidth=2;ctx.stroke();
      drE(n.right);
    }
  })(tree);

  // 2. Nodos con colores según estado
  var clr={
    idle:{fill:cssVar('--node-fill'),stroke:cssVar('--node-stroke')},
    cmp:{fill:cssVar('--highlight-fill'),stroke:cssVar('--highlight-stroke')},
    ins:{fill:cssVar('--insert-fill'),stroke:cssVar('--insert-stroke')},
    bal:{fill:cssVar('--bal-fill'),stroke:cssVar('--bal-stroke')},
    unb:{fill:cssVar('--error-fill'),stroke:cssVar('--error-stroke')},
    rot:{fill:cssVar('--rot-fill'),stroke:cssVar('--rot-stroke')},
    don:{fill:cssVar('--don-fill'),stroke:cssVar('--don-stroke')}
  };

  (function drN(n){
    if(!n)return;
    var t=hlM[n.id]||'idle',c=clr[t]||clr.idle;
    ctx.beginPath();ctx.arc(n.px,n.py,NODE_R,0,Math.PI*2);
    ctx.fillStyle=c.fill;ctx.fill();
    ctx.strokeStyle=c.stroke;ctx.lineWidth=t==='idle'?2:3;ctx.stroke();
    ctx.fillStyle=cssVar('--node-text');
    ctx.font='bold 14px monospace';
    ctx.textAlign='center';ctx.textBaseline='middle';
    ctx.fillText(n.val,n.px,n.py);
    // Factor de balanceo (opcional, para árboles balanceados)
    var fb=bfM[n.id];
    if(fb!==undefined){
      ctx.font='11px system-ui,sans-serif';
      ctx.fillStyle=Math.abs(fb)>1?cssVar('--fb-bad'):cssVar('--fb-ok');
      ctx.textAlign='left';ctx.textBaseline='bottom';
      ctx.fillText('fb='+(fb>0?'+':'')+fb,n.px+NODE_R+4,n.py-NODE_R+14);
    }
    drN(n.left);drN(n.right);
  })(tree);
}
```

Todos los colores se resuelven con `cssVar()` para que el cambio entre light/dark
sea automático al abrir el archivo correspondiente.

### Paso a paso con snapshot

Cada paso contiene un snapshot del árbol (clonado) más metadatos:

```js
var steps=[];
var currentStep=-1;

// Cada paso
{desc:'Descripción textual',tree:cloneT(arbol),hl:[{id:nodeId,t:'cmp'}],bf:[{id:nodeId,fb:1}],done:false}
```

El `tree` se clona con `cloneT()` para que cada paso sea independiente:

```js
function cloneT(n){
  if(!n)return null;
  var c=new Node(n.val);c.height=n.height;c.id=n.id;
  c.left=cloneT(n.left);c.right=cloneT(n.right);
  return c;
}
```

### Renderizar un paso

```js
function renderStep(idx){
  if(idx<0||idx>=steps.length){
    if(idx===-1&&steps.length===0){
      ctx.clearRect(0,0,canvas._w||400,canvas._h||300);
      descEl.textContent='Árbol vacío.';
      stepCounterEl.textContent='Paso — / —';
      treeInfoEl.textContent='—';
    }
    updateBtns();return;
  }
  var s=steps[idx];
  drawTree(s.tree,s.hl,s.bf);
  descEl.textContent=s.desc;
  stepCounterEl.textContent='Paso '+(idx+1)+' / '+steps.length;
  var total=s.tree?countN(s.tree):0;
  treeInfoEl.textContent=total+' nodo'+(total!==1?'s':'')+(s.tree?', altura '+s.tree.height:'');
  updateBtns();
}
```

## Controles (applets sin inserción/búsqueda)

Para applets de solo visualización (recorridos, ordenamientos, etc.) que no necesitan
modo insertar/buscar, se puede usar una versión simplificada:

```html
<div class="controls">
  <button id="btnFirst" title="Ir al inicio">⏮</button>
  <button id="btnPrev" title="Paso anterior">◀</button>
  <button id="btnNext" title="Paso siguiente">▶</button>
  <button id="btnSkip" title="Reproducir automático">>></button>
</div>
<div class="speed-wrap">
  <label for="speedSlider">Vel:</label>
  <input type="range" id="speedSlider" min="400" max="3000" value="1500" step="100">
  <span id="speedLabel">0.5 p/s</span>
</div>
```

La lógica de navegación, auto‑play y atajos de teclado es la misma que en la
[interfaz estándar](#interfaz-de-control-estándar).

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

Los atajos de teclado se definen en la [interfaz estándar](#interfaz-de-control-estándar).

## Modo oscuro

Los iframes no heredan el tema del sitio padre, por lo que se necesitan
archivos separados `_light.html` y `_dark.html` con colores fijos (sin `@media`).

### Crear versión dark

1. Copiar el archivo light a `*_dark.html`
2. Reemplazar los colores de `:root` con los valores dark de la tabla de colores

### Archivos generados

```
applets/X-tema/X-Y-tema/
├── mi-applet_light.html         (light)
├── mi-applet_dark.html          (dark, colores oscuros forzados)
└── ...
```

El sufijo `_light` o `_dark` va al final, antes de la extensión, siguiendo la
convención de las figuras SVG (`Arbol_light.svg`, `Arbol_dark.svg`).

### Paleta de colores

| Variable | Light | Dark |
|---|---|---|
| `--bg` | `#ffffff` | `#1a1b2e` |
| `--fg` | `#1a1a2e` | `#e0e0e0` |
| `--border` | `#d1d5db` | `#374151` |
| `--btn-bg` | `#f3f4f6` | `#2d3748` |
| `--btn-hover` | `#e5e7eb` | `#374151` |
| `--btn-active` | `#d1d5db` | `#4a5568` |
| `--btn-disabled` | `#e5e7eb` | `#1f2937` |
| `--btn-text` | `#374151` | `#e0e0e0` |
| `--highlight` | `#1d4ed8` | `#60a5fa` |
| `--node-fill` | `#e1f5ff` | `#2d3748` |
| `--node-stroke` | `#4682b4` | `#63b3ed` |
| `--insert-fill` | `#d4edda` | `#1e3a2f` |
| `--insert-stroke` | `#28a745` | `#48c774` |
| `--highlight-fill` | `#fff3cd` | `#5a4a00` |
| `--highlight-stroke` | `#ffc107` | `#ffc107` |
| `--error-fill` | `#ffe1e1` | `#4a5568` |
| `--error-stroke` | `#e9967a` | `#fc8181` |
| `--found-fill` | `#d4edda` | `#1e3a2f` |
| `--found-stroke` | `#28a745` | `#48c774` |
| `--mode-active-bg` | `#1d4ed8` | `#60a5fa` |
| `--mode-active-text` | `#ffffff` | `#1a1b2e` |
| `--cmp-done` | `#059669` | `#48c774` |
| `--slot-stroke` | `#9ca3af` | `#6b7280` |
| `--bal-fill` | `#f3f4f6` | `#2d3748` |
| `--bal-stroke` | `#9ca3af` | `#9ca3af` |
| `--rot-fill` | `#fff3cd` | `#5a4a00` |
| `--rot-stroke` | `#fd7e14` | `#fd7e14` |
| `--don-fill` | `#d4edda` | `#1e3a2f` |
| `--don-stroke` | `#28a745` | `#48c774` |
| `--node-text` | `#1a1a2e` | `#e0e0e0` |
| `--fb-ok` | `#059669` | `#48c774` |
| `--fb-bad` | `#dc2626` | `#fc8181` |
| `--btn-primary` | `#1d4ed8` | `#60a5fa` |
| `--btn-primary-hover` | `#1e40af` | `#3b82f6` |

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
  btnFirst.disabled = (idx <= 0);
  btnPrev.disabled = (idx <= 0);
  btnNext.disabled = (idx >= steps.length - 1);
}
```

## Variables globales y helpers (recorridos)

Para applets de solo visualización (sin cola de pendientes), se usa una versión simplificada:

```js
let steps = [];
let currentStep = -1;
let isPlaying = false;
let playTimer = null;
let speedVal = 1900;

function goTo(n) {
  if (n < 0) n = 0;
  if (n >= steps.length) n = steps.length - 1;
  currentStep = n;
  render(currentStep);
}

function goNext() { if (currentStep < steps.length - 1) goTo(currentStep + 1); }
function goPrev() { if (currentStep > 0) goTo(currentStep - 1); }
function goFirst() { goTo(0); }

function tick() {
  if (!isPlaying) return;
  if (currentStep < steps.length - 1) { goNext(); playTimer = setTimeout(tick, speedVal); }
  else stopPlay();
}
function startPlay() {
  if (currentStep >= steps.length - 1) return;
  isPlaying = true;
  btnSkip.textContent = '⏸'; btnSkip.classList.add('playing');
  playTimer = setTimeout(tick, speedVal);
}
function stopPlay() {
  isPlaying = false;
  if (playTimer) { clearTimeout(playTimer); playTimer = null; }
  btnSkip.textContent = '>>'; btnSkip.classList.remove('playing');
}
function hdlSkip() {
  if (isPlaying) { stopPlay(); return; }
  if (currentStep >= steps.length - 1) return;
  startPlay();
}
```

Para applets con cola de pendientes (inserción de valores), ver la [interfaz estándar](#interfaz-de-control-estándar).

## Verificación

- [ ] El applet ocupa todo el viewport del iframe sin scrollbars
- [ ] Layout: header + main(tree + sidebar) + info
- [ ] El árbol usa `flex: 1` para ocupar espacio sobrante
- [ ] Controles a la derecha en la sidebar siguiendo la interfaz estándar
- [ ] Modo selector como botones (Insertar/Buscar), activo en azul
- [ ] Input acepta valores separados por coma con ↵ hint
- [ ] Botón "Vaciar árbol" para reiniciar
- [ ] Separadores entre secciones de la sidebar
- [ ] Navegación: ⏮ ◀ ▶ >> (>> cambia a ⏸ al reproducir)
- [ ] Speed slider con etiqueta en p/s, solo afecta a >>
- [ ] Cola de pendientes: se ingresan varios valores, se procesan uno por uno
- [ ] La info (descripción + paso) queda abajo del todo
- [ ] SVG con `viewBox` que coincide con coordenadas de nodos/aristas (si usa SVG)
- [ ] Canvas con `cssVar()` para resolución de colores (si usa Canvas)
- [ ] Play automático con slider de velocidad (400–3000ms, invertido 3400-valor)
- [ ] Atajos de teclado: ← → paso, Space/End play/pausa, Home inicio
- [ ] Archivos `_light.html` y `_dark.html` separados sin `@media`
- [ ] `myst.yml` incluye `project.static_files: [_static/applets]`
- [ ] `{iframe}` usa ruta absoluta `/applets/...` y `:height:` fijo
- [ ] Placeholder PNG generado para PDF
- [ ] Borrar `_build/` al cambiar static_files
- [ ] Archivo html único sin dependencias externas
