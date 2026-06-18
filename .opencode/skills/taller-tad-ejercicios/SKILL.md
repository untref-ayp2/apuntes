---
name: taller-tad-ejercicios
description: Crea y mantiene ejercicios del repositorio taller-tad. Documenta la estructura de directorios, convenciones de README y el flujo para agregar nuevos capítulos.
license: CC-BY-SA-4.0
compatibility: opencode
---

<role>
Sos un asistente especializado en la creación y mantenimiento de ejercicios prácticos para el repositorio `taller-tad` de la materia Algoritmos y Programación II (UNTREF).
</role>

<context>
Cada capítulo del apunte `contenidos/3-estructuras-de-datos/3-N-tema.md` tiene su contraparte `NN-tema/` en taller-tad.

**Consultar `ESTILOS.md` §5 para convenciones de ejercicios en el apunte (labels, referencias a repos).**
</context>

## Arquitectura de un capítulo

```
NN-tema/
└── ejercicios/
    ├── NN-ejercicio/       # esqueleto .go + _test.go
    ├── NN-otro-ejercicio/
    └── README.md           # enunciados de TODOS los ejercicios
```

- **No** hay `README.md` en la raíz del capítulo.
- **No** hay `README.md` dentro de cada subdirectorio de ejercicio.
- `ejercicios/README.md` es la **única fuente de verdad** para los enunciados.

## Formato del README de ejercicios

```markdown
# Ejercicios: <Nombre del Capítulo>

Antes de comenzar, implementá `<TAD>` en tu repositorio data-structures.

---

## N. Nombre del Ejercicio

Descripción breve.

**Valores**: descripción de los datos que modela el TAD.

**Operaciones**:

- `Nombre(params) Retorno` — descripción de la operación

**Invariante**:

- Condición que debe cumplirse siempre

**Preguntas**:

- Pregunta reflexiva sobre el diseño

→ `NN-ejercicio/`
```

Reglas:
- Usar `##` para cada ejercicio (no `###`).
- Separar ejercicios con `---`.
- Usar `-` para bullets (no `*`).
- **Valores**, **Operaciones**, **Invariante**, **Preguntas** en ese orden.
- Referencia `→ NN-ejercicio/` al final indica el directorio del esqueleto.

## Flujo para agregar un nuevo capítulo

1. Crear estructura en el mirror del apunte:
   ```bash
   mkdir -p ~/AyP2/apuntes/taller-tad/07-diccionarios/ejercicios/01-ejercicio
   ```
2. Crear estructura en el repo:
   ```bash
   mkdir -p ~/AyP2/taller-tad/07-diccionarios/ejercicios/01-ejercicio
   ```
3. Escribir esqueletos `.go` y `_test.go`
4. Escribir `ejercicios/README.md` con los enunciados
5. Actualizar `README.md` raíz de taller-tad:
   - `## Estructura`: agregar directorio al árbol
   - `## Dependencias`: agregar capítulo si depende de data-structures

## Verificación

- `ls 0*/README.md` no debe mostrar archivos
- `ls 0*/ejercicios/*/README.md` no debe mostrar archivos
- `ls 0*/ejercicios/README.md` debe mostrar 1 README por capítulo
- `go test ./NN-tema/...` debe pasar

## Reglas generales

1. **No crear READMEs en raíz de capítulo.**
2. **No crear READMEs por ejercicio.**
3. **No duplicar información** — URLs, setup y go.mod replace solo en README raíz.
4. **Mantener sincronizados** mirror (`apuntes/taller-tad/`) y repo (`~/AyP2/taller-tad/`).
5. **Numeración consistente**: capítulo 3-N del apunte → directorio `NN-tema` en taller-tad.
