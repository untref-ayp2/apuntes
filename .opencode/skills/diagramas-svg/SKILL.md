---
name: diagramas-svg
description: Crea y mantiene diagramas SVG con estilos consistentes para el proyecto UNTREF AyP2
license: CC-BY-SA-4.0
compatibility: opencode
---

<role>
Sos un diseñador de diagramas SVG para el apunte "Algoritmos y Programación 2" de la UNTREF.
Creás y mantenés diagramas en pares light/dark que se renderizan correctamente tanto en HTML como en PDF.
</role>

<context>
Este apunte se compila a HTML (MyST) y PDF (Typst):
- **Versión light** incluida en HTML (modo claro) y en el PDF
- **Versión dark** incluida solo en HTML (modo oscuro)
- Cada diagrama necesita su par `_light.svg` y `_dark.svg`

**Consultar `ESTILOS.md` §4 para paletas de colores, fuentes, grosores y clases CSS estándar.**
</context>

## Estructura del SVG

Usar clases CSS en `<defs><style>` para mantener consistencia. Orden recomendado:

1. `<defs>` con `<style>` y `<marker>`
2. `<rect>` de fondo
3. `<text>` título
4. Grupos `<g>` con elementos del diagrama

### Clases semánticas

Las definiciones de color y fuente están en `ESTILOS.md` §4. Acá solo la semántica:

| Clase            | Uso                                               |
| ---------------- | ------------------------------------------------- |
| `.title`         | Título principal (20px, sans-serif, text-anchor middle) |
| `.code`          | Texto en nodos (16px, monoespaciado, text-anchor middle) |
| `.code-example`  | Código fuera de nodos (18px, monoespaciado, text-anchor start) |
| `.variable-node` | Nodos que representan variables (fill azul)       |
| `.value-node`    | Nodos que representan valores (fill rojo)         |
| `.arrow`         | Flechas/aristas con marker-end `#arrowhead`       |
| `.note`          | Notas en cursiva (14px, sans-serif)               |

### Ejemplo mínimo (light)

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 360">
  <defs>
    <style>
      .title { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 20px; text-anchor: middle; fill: #333333; }
      .code { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 16px; fill: #333333; text-anchor: middle; }
      .variable-node { fill: #e1f5ff; stroke: #4682b4; stroke-width: 2; }
      .value-node { fill: #ffe1e1; stroke: #e9967a; stroke-width: 2; }
      .arrow { stroke: #333333; stroke-width: 2; marker-end: url(#arrowhead); }
    </style>
    <marker id="arrowhead" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <polygon points="0 0, 6 2.5, 0 5" fill="#333333" />
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="#f0f2f5" rx="8"/>
  <!-- elementos del diagrama -->
</svg>
```

## Diagramas de árboles

### Clases para árboles

| Clase            | Uso                                     |
| ---------------- | --------------------------------------- |
| `.edge`          | Arista entre nodos (ABB, AVL)           |
| `.tree-edge`     | Arista gruesa (árbol genérico)          |
| `.op-node`       | Nodo de operación (+, −, *, etc.)       |
| `.num-node`      | Nodo de número o valor                  |
| `.node-circle`   | Círculo de nodo (r=18, stroke-width 2.5) |
| `.node-text`     | Texto interior (monospace 14px bold, centrado) |
| `.fb-label`      | Etiqueta factor de balanceo (sans-serif 12px) |
| `.fb-bal`        | FB balanceado (verde)                   |
| `.fb-unbal`      | FB desbalanceado (rojo)                 |
| `.annotation-text` | Anotaciones externas                 |
| `.pointer-line`  | Línea de puntero desde anotación        |
| `.dashed-line`   | Línea punteada para marcar niveles      |

Los colores de cada clase están en `ESTILOS.md` §4 (tablas "Paleta de colores — Light/Dark").

### ViewBox y layout para ABB/AVL

- ViewBox por defecto: `0 0 700 360` para 5 niveles; reducir altura a `300` o `280` para 3-4 niveles, **mantener ancho 700**.
- Radio de nodo: `r="18"`
- Separación vertical decreciente: 70→65→60→55px entre niveles 0→1→2→3→4
- Desplazamiento horizontal: ±130-150px (nivel 0→1), ±75-90px (1→2), ±45-55px (2→3), ±25-30px (3→4)

### Etiquetas de factor de balanceo (AVL)

- Posición default: derecha del nodo (`x="cx + r + 6"`, `text-anchor: start`)
- Si se superpone con otro nodo: izquierda (`x="cx - r - 6"`, `text-anchor: end`)
- Etiqueta balanceado: clase `fb-bal`; desbalanceado: clase `fb-unbal`

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

## Reglas de archivos

1. **Siempre crear versión light y dark**: `_light.svg` y `_dark.svg`
2. Ubicación: `contenidos/_static/figures/`
3. Nomenclatura: descriptiva, minúsculas, guiones (ej. `slice-append-entangled-1_light.svg`)

## Workflow

### Paso 1: Crear versión Light
1. Fondo `#f0f2f5`
2. Fills pastel claros (ej. `#e1f5ff`, `#ffe1e1`)
3. Strokes medios (ej. `#4682b4`, `#e9967a`)
4. Texto `#333333`

### Paso 2: Crear versión Dark
1. Copiar `_light.svg` → `_dark.svg`
2. Fondo `#f0f2f5` → `#1e1e1e`
3. Fills oscuros (ej. `#2d3748`, `#4a5568`)
4. Mantener strokes brillantes (ej. `#63b3ed`, `#fc8181`)
5. Texto `#333333` → `#e0e0e0`
6. Ajustar atributos inline (no clases) que tengan colores fijos

## Verificación

- [ ] Existen `_light.svg` y `_dark.svg`
- [ ] Ambos tienen `<defs>` con `<style>` y clases CSS
- [ ] Los colores de fondo, texto y nodos corresponden al theme (ver `ESTILOS.md` §4)
- [ ] Los strokes se mantienen brillantes en ambos themes
- [ ] Los textos son idénticos en light y dark (solo cambian colores)
- [ ] Las flechas tienen `marker-end` apuntando a `#arrowhead`
- [ ] El nombre de clase `.code-example` usa guión, no guión bajo

## Cuándo usar este skill

- Se pide crear un nuevo diagrama SVG
- Se modifica un diagrama existente
- Se adapta un diagrama de otro formato a SVG
