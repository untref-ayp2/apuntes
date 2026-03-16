---
description: Estandariza archivos SVG según el skill diagramas-svg
---

Estandariza los archivos SVG recibidos según las reglas del skill `diagramas-svg`.

Para cada archivo SVG:

1. Lee el archivo
2. Aplica los cambios según el skill:

### Estructura Obligatoria

### Theme Light

Agregar `<defs>` con `<style>` conteniendo las clases CSS:

```xml
<defs>
  <style>
    .title { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 20px; text-anchor: middle; fill: #333333; }
    .code { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 16px; fill: #333333; text-anchor: middle; }
    .code-example { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 18px; fill: #333333; text-anchor: start; }
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

- Fondo: `#f0f2f5`
- `.title` fill: `#333333`
- `.variable-node` fill: `#e1f5ff`, stroke: `#4682b4`
- `.value-node` fill: `#ffe1e1`, stroke: `#e9967a`

### Theme Dark

Agregar `<defs>` con `<style>` conteniendo las clases CSS:

```xml
<defs>
  <style>
    .title { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 20px; text-anchor: middle; fill: #e0e0e0; }
    .code { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 16px; fill: #e0e0e0; text-anchor: middle; }
    .code-example { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 18px; fill: #e0e0e0; text-anchor: start; }
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

- Fondo: `#1e1e1e`
- `.title` fill: `#e0e0e0`
- `.code` fill: `#e0e0e0`
- `.variable-node` fill: `#2d3748`, stroke: `#63b3ed`
- `.value-node` fill: `#4a5568`, stroke: `#fc8181`

### Tamaños de Fuente (obligatorios)

- `.title`: **20px**
- `.code_example`: **18px**
- `.code`: **16px**

Guarda los cambios en los archivos.

Los archivos a procesar son: @\{archivos}
