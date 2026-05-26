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
