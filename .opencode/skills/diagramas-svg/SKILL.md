---
name: diagramas-svg
description: Crea y mantiene diagramas SVG con estilos consistentes para el proyecto UNTREF EDD
license: CC-BY-SA-4.0
compatibility: opencode
---

## Estilos Obligatorios

### Estructura con Clases CSS

Usar clases CSS en `<defs><style>` para mantener consistencia y facilitar mantenimiento:

```xml
<defs>
  <style>
    .title { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 20px; text-anchor: middle; fill: #333333; }
    .code_example { font-family: menlo, consola, 'DejaVu Sans Mono'; font-size: 18px; fill: #333333; text-anchor: start; }
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

### Clases Semánticas

| Clase            | Descripción                                  | text-anchor |
| ---------------- | -------------------------------------------- | ----------- |
| `.title`         | Título principal del diagrama                | middle      |
| `.code`          | Texto dentro de nodos (16px)                 | middle      |
| `.code_example`  | Ejemplos de código fuera de nodos (18px)     | start       |
| `.variable-node` | Nodos que representan variables (azul)       | -           |
| `.value-node`    | Nodos que representan valores/strings (rojo) | -           |
| `.arrow`         | Flechas/aristas entre nodos                  | -           |
| `.note`          | Notas explicativas en cursiva (14px)         | middle      |

### Fuentes

- **Título** (`.title`): `ui-sans-serif, system-ui, sans-serif`
- **Código** (`.code`, `.code_example`): `menlo, consola, 'DejaVu Sans Mono'`

**Regla**: Si el texto representa código Python o valores de datos, usar fuente monospaciada. Para títulos, usar fuente por defecto.

### Colores - Theme Light

| Elemento                 | Fill      | Stroke    |
| ------------------------ | --------- | --------- |
| Fondo principal          | `#f0f2f5` | -         |
| Nodos azules (variables) | `#e1f5ff` | `#4682b4` |
| Nodos verdes             | `#e1ffe1` | `#2e8b57` |
| Nodos rojos (valores)    | `#ffe1e1` | `#e9967a` |
| Nodos naranjas           | `#fff4e1` | `#f6ad55` |
| Nodos morados            | `#f5e1ff` | `#9f7aea` |
| Texto y líneas           | -         | `#333333` |

### Colores - Theme Dark

| Elemento                   | Fill      | Stroke    |
| -------------------------- | --------- | --------- |
| Fondo principal            | `#1e1e1e` | -         |
| Contenedores               | `#2d3748` | -         |
| Nodos internos (variables) | `#2d3748` | `#63b3ed` |
| Nodos hoja (valores)       | `#4a5568` | `#fc8181` |
| Texto y líneas             | -         | `#e0e0e0` |

### Tamaños de Fuente

- **16px**: Texto en nodos (`.code`)
- **18px**: Ejemplos de código (`.code_example`)
- **20px**: Título principal (`.title`)

### Grosores de Línea

- **1px**: Bordes punteados (`stroke-dasharray="5,5"`)
- **2px**: Bordes de nodos, aristas

### Otros Estilos

- Bordes redondeados: `rx="5"` para nodos
- Flechas: marker tipo triángulo
- Alineación de texto: `text-anchor="middle"` o `text-anchor="left"`

## Reglas de Archivos

1. **Siempre crear versión light y dark**: cada diagrama debe tener `_light.svg` y `_dark.svg`
2. Ubicación: `contenidos/_static/figures/`
3. Nomenclatura: descriptiva, minúsculas, guiones si es necesario

## Estructura de Diagramas

Orden recomendado:

1. `<defs>` con `<style>` y `<marker>`
2. `<rect>` de fondo
3. `<text>` título
4. Grupos `<g>` con elementos del diagrama

## Cuándo Usar Este Skill

Usar este skill cuando:

- Se pide crear un nuevo diagrama SVG
- Se modifica un diagrama existente
- Se adapta un diagrama de otro formato a SVG
