---
name: applet-javascript
description: Crea applets HTML/JS autocontenidos para visualización interactiva en el apunte AyP2
license: CC-BY-SA-4.0
compatibility: opencode
---

<role>
Sos un desarrollador de applets HTML/CSS/JS autocontenidos para el apunte "Algoritmos y Programación 2" de la UNTREF.
Creás applets interactivos que se renderizan sin scrollbars y se integran vía `{iframe}` de MyST.
</role>

<context>
Los applets son archivos HTML únicos (sin dependencias externas) en `contenidos/_static/applets/`.
Se embeben en el apunte con `{iframe}` envuelto en `<div class="only-html">`.
La carpeta `_static/applets/` debe declararse en `myst.yml` como `project.static_files`.

**Consultar `ESTILOS.md` §8 para incrustación en markdown, estructura de archivos, `myst.yml` y restricciones del build PDF.**
</context>

## Layout base (ocupar todo el viewport sin scroll)

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

## Distribución (árbol a la izquierda, controles a la derecha)

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
+----------------------------------+----------------+
|           Info (descripción + paso)               |
+--------------------------------------------------+
```

### HTML del layout estándar

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
      <div class="legend" id="legend"></div>
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

## Interfaz de control estándar

### Modos de operación

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

### Navegación y auto-play

```css
.controls{display:flex;flex-direction:row;gap:4px;flex-wrap:wrap;justify-content:center}
.controls button{width:36px;height:30px;border:1px solid var(--border);border-radius:6px;background:var(--btn-bg);color:var(--btn-text);font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .15s;padding:0}
.controls button:hover:not(:disabled){background:var(--btn-hover)}
.controls button:disabled{opacity:.4;cursor:default}
.controls button.playing{background:var(--error-stroke);color:#fff;border-color:var(--error-stroke)}
```

```js
var isPlaying=false;
var playTimer=null;
var steps=[];
var currentStep=-1;
var pendingValues=[];

function updateBtns(){
  var atS=currentStep<=0,atE=currentStep>=steps.length-1,hasS=steps.length>0;
  btnFirst.disabled=atS||!hasS||isPlaying;
  btnPrev.disabled=atS||!hasS||isPlaying;
  btnNext.disabled=(!hasS&&pendingValues.length===0)||(atE&&pendingValues.length===0)||isPlaying;
  btnSkip.disabled=pendingValues.length===0&&atE;
}

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
  isPlaying=true;btnSkip.textContent='⏸';btnSkip.classList.add('playing');
  updateBtns();playTimer=setTimeout(tick,speedVal);
}

function stopPlay(){
  isPlaying=false;
  if(playTimer){clearTimeout(playTimer);playTimer=null;}
  btnSkip.textContent='>>';btnSkip.classList.remove('playing');updateBtns();
}

function hdlSkip(){
  if(isPlaying){stopPlay();return;}
  if(currentStep>=steps.length-1&&pendingValues.length===0)return;
  startPlay();
}
```

### Velocidad (slider invertido)

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

```js
function parseAndEnq(inp){
  var nums=inp.split(',').map(function(s){return s.trim()}).filter(function(s){return s.length>0})
    .map(function(s){return parseInt(s,10)}).filter(function(n){return Number.isInteger(n)&&n>0});
  if(nums.length===0){descEl.textContent='⚠ Ingresá números enteros positivos separados por coma.';return;}
  pendingValues.push.apply(pendingValues,nums);
  valInput.value='';
  descEl.textContent=nums.length+' valor'+(nums.length!==1?'es':'')+' encolado'+(nums.length!==1?'s':'')+'.';
  updateBtns();
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

### Separador

```css
.separator{height:1px;background:var(--border);margin:2px 0}
```

## Dibujo dinámico con Canvas

Para applets donde la estructura crece dinámicamente (inserción AVL, ABB), usar `<canvas>`.

```css
.tree-wrap canvas{width:100%;height:100%}
```

```js
var canvas=document.getElementById('treeCanvas');
var ctx=canvas.getContext('2d');
var NODE_R=18;
var LEVEL_H=65;

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

```js
function countN(n){return n?1+countN(n.left)+countN(n.right):0}

function layL(n,d,p){
  if(!n)return;
  layL(n.left,d+1,p);
  n._in=p.c++;n._dep=d;
  layL(n.right,d+1,p);
}

function layT(tree,w,h){
  if(!tree)return;
  var total=countN(tree);if(!total)return;
  layL(tree,0,{c:0});
  var mx=30,my=30,xR=w-2*mx;
  var mD=function md(n){return n?1+Math.max(md(n.left),md(n.right)):0}(tree);
  var sY=Math.min(LEVEL_H,(h-2*my)/Math.max(mD,1));
  (function pn(n){
    if(!n)return;
    n.px=mx+(total>1?(n._in/(total-1))*xR:w/2-mx);
    n.py=my+n._dep*sY;
    pn(n.left);pn(n.right);
  })(tree);
}
```

### Dibujar el árbol

```js
var cssVar=function(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim()};

function drawTree(tree,highlights,bfArr){
  var w=canvas._w,h=canvas._h;
  ctx.clearRect(0,0,w,h);
  if(!tree)return;
  layT(tree,w,h);
  var hlM={};if(highlights)highlights.forEach(function(h){hlM[h.id]=h.t});
  var bfM={};if(bfArr)bfArr.forEach(function(b){bfM[b.id]=b.fb});

  // Aristas
  (function drE(n){
    if(!n)return;
    if(n.left){ctx.beginPath();ctx.moveTo(n.px,n.py);ctx.lineTo(n.left.px,n.left.py);
      ctx.strokeStyle=cssVar('--border');ctx.lineWidth=2;ctx.stroke();drE(n.left);}
    if(n.right){ctx.beginPath();ctx.moveTo(n.px,n.py);ctx.lineTo(n.right.px,n.right.py);
      ctx.strokeStyle=cssVar('--border');ctx.lineWidth=2;ctx.stroke();drE(n.right);}
  })(tree);

  // Nodos
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
    ctx.fillStyle=c.fill;ctx.fill();ctx.strokeStyle=c.stroke;ctx.lineWidth=t==='idle'?2:3;ctx.stroke();
    ctx.fillStyle=cssVar('--node-text');ctx.font='bold 14px monospace';
    ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(n.val,n.px,n.py);
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

## Paso a paso con snapshot

```js
var steps=[];
var currentStep=-1;

function cloneT(n){
  if(!n)return null;
  var c=new Node(n.val);c.height=n.height;c.id=n.id;
  c.left=cloneT(n.left);c.right=cloneT(n.right);
  return c;
}

function renderStep(idx){
  if(idx<0||idx>=steps.length){
    if(idx===-1&&steps.length===0){
      ctx.clearRect(0,0,canvas._w||400,canvas._h||300);
      descEl.textContent='Árbol vacío.';stepCounterEl.textContent='Paso — / —';treeInfoEl.textContent='—';
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

Cada paso: `{desc:'...', tree:cloneT(arbol), hl:[{id:nodeId,t:'cmp'}], bf:[{id:nodeId,fb:1}], done:false}`

## Applets de solo visualización (recorridos)

Para applets sin inserción, usar versión simplificada: sin cola de pendientes, sin modos.

```js
function goTo(n){n=Math.max(0,Math.min(n,steps.length-1));currentStep=n;render(currentStep);}
function goNext(){if(currentStep<steps.length-1)goTo(currentStep+1);}
function goPrev(){if(currentStep>0)goTo(currentStep-1);}
function goFirst(){goTo(0);}
```

### Generación de pasos para recorridos

```js
function* genSteps(node, type){
  if(!node)return;
  yield{action:'enter',node};
  if(type==='preorder')yield{action:'process',node};
  yield* genSteps(node.left,type);
  if(type==='inorder'){yield{action:'enter',node};yield{action:'process',node};}
  yield* genSteps(node.right,type);
  if(type==='postorder'){yield{action:'enter',node};yield{action:'process',node};}
}
```

### Dispatcher por archivo separado

Cada variante es un archivo independiente con el tipo hardcodeado. No usar query strings.

```js
const tipo = 'preorden';  // hardcodeado según el archivo
```

Archivos generados:
```
recorridos-arbol-preorden_light.html   → const tipo = 'preorden';
recorridos-arbol-inorden_light.html    → const tipo = 'inorden';
recorridos-arbol-postorden_light.html  → const tipo = 'postorden';
```

## Modo oscuro

Los iframes no heredan el tema del sitio padre → archivos `_light.html` y `_dark.html` separados con colores fijos (sin `@media`).

Crear versión dark: copiar light, reemplazar variables CSS `:root` con la paleta dark.

### Paleta de colores

| Variable | Light | Dark |
|---|---|---|
| `--bg` | `#ffffff` | `#1a1b2e` |
| `--fg` | `#1a1a2e` | `#e0e0e0` |
| `--border` | `#d1d5db` | `#374151` |
| `--btn-bg` | `#f3f4f6` | `#2d3748` |
| `--btn-hover` | `#e5e7eb` | `#374151` |
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
| `--cmmp-done` | `#059669` | `#48c774` |
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
└── ...
```

## Verificación

- [ ] Layout: header + main(tree + sidebar) + info
- [ ] Ocupa todo el viewport del iframe sin scrollbars
- [ ] Modo selector como botones, activo en azul
- [ ] Input acepta valores separados por coma con ↵ hint
- [ ] Navegación: ⏮ ◀ ▶ >> (>> cambia a ⏸ al reproducir)
- [ ] Speed slider con etiqueta en p/s, solo afecta a >>
- [ ] Cola de pendientes funcional
- [ ] Canvas con `cssVar()` para resolución de colores
- [ ] Play automático con slider invertido (400–3000ms)
- [ ] Atajos de teclado: ← → paso, Space/End play/pausa, Home inicio
- [ ] Archivos `_light.html` y `_dark.html` separados sin `@media`
- [ ] `myst.yml` incluye `project.static_files: [_static/applets]`
- [ ] Incrustación en markdown según `ESTILOS.md` §8
- [ ] Archivo html único sin dependencias externas
