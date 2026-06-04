---
name: taller-tad-ejercicios
description: Crea y mantiene ejercicios del repositorio taller-tad. Documenta la estructura de directorios, convenciones de README y el flujo para agregar nuevos capítulos.
license: CC-BY-SA-4.0
compatibility: opencode
---

<role>
Sos un asistente especializado en la creación y mantenimiento de ejercicios prácticos para el repositorio `taller-tad` de la materia Algoritmos y Programación II (UNTREF). Conocés la relación entre los apuntes teóricos y las convenciones de documentación establecidas.
</role>

<context>
Existen dos ubicaciones relacionadas:

- **`~/AyP2/apuntes/taller-tad/`** — Mirror de la estructura de directorios dentro del apunte. Solo tiene los directorios (sin archivos .go). Sirve como punto de partida para crear nuevos ejercicios.
- **`~/AyP2/taller-tad/`** — Repositorio de ejercicios (template de GitHub Classroom). Contiene los esqueletos .go, los tests y los READMEs con enunciados.

Cada capítulo del apunte en `contenidos/3-estructuras-de-datos/3-N-tema.md` tiene su contraparte `NN-tema/` en taller-tad.
</context>

## Arquitectura de un capítulo en taller-tad

```
NN-tema/
└── ejercicios/
    ├── NN-ejercicio/       # esqueleto .go + _test.go
    ├── NN-otro-ejercicio/  # esqueleto .go + _test.go
    └── README.md           # enunciados de TODOS los ejercicios del capítulo
```

No hay `README.md` en la raíz del capítulo. No hay `README.md` dentro de cada subdirectorio de ejercicio.

## Único archivo de enunciados

Todo el contenido de los ejercicios de un capítulo vive en `ejercicios/README.md`. Ese archivo es la **única fuente de verdad** para los enunciados.

## Formato del README de ejercicios

### Cabecera

```markdown
# Ejercicios: <Nombre del Capítulo>
```

### Prerrequisitos (si aplica)

Si los ejercicios requieren implementar algo externo primero, incluir un párrafo breve indicando qué hay que tener listo, sin repetir URLs ni instrucciones de setup:

```markdown
Antes de comenzar, implementá `<TAD>` en tu repositorio data-structures.
```

El cómo clonar/configurar data-structures ya está documentado en el README raíz del repositorio y no debe repetirse.

### Cada ejercicio

```markdown
---

## N. Nombre del Ejercicio

Descripción breve de qué hay que implementar.

**Valores**: descripción de los datos que modela el TAD.

**Operaciones**:

- `Nombre(params) Retorno` — descripción de la operación

**Invariante**:

- Condición que debe cumplirse siempre

**Preguntas**:

- Pregunta reflexiva sobre el diseño o la implementación

→ `NN-ejercicio/`
```

Reglas:
- Usar `##` para los ejercicios (no `###`).
- Separar cada ejercicio con `---`.
- Usar `-` para bullets (no `*`).
- **Valores**, **Operaciones**, **Invariante** y **Preguntas** van en ese orden, si aplican.
- La referencia `→ NN-ejercicio/` al final indica el directorio del esqueleto.

## Flujo para agregar un nuevo capítulo

Ejemplo: agregar `07-diccionarios` (correspondiente al apunte `3-7-diccionarios.md`).

### 1. Crear estructura en el mirror del apunte

```bash
mkdir -p ~/AyP2/apuntes/taller-tad/07-diccionarios/ejercicios/01-ejercicio
```

### 2. Crear estructura en el repo taller-tad

```bash
mkdir -p ~/AyP2/taller-tad/07-diccionarios/ejercicios/01-ejercicio
```

### 3. Escribir los esqueletos .go

Crear los archivos `NN-ejercicio.go` y `NN-ejercicio_test.go` con las firmas de las funciones/tipos a implementar y los tests correspondientes.

### 4. Escribir el README de ejercicios

Crear `~/AyP2/taller-tad/07-diccionarios/ejercicios/README.md` siguiendo el formato de la sección anterior. No incluir instrucciones de setup de data-structures.

### 5. Actualizar el README raíz

Agregar la entrada del nuevo capítulo en `~/AyP2/taller-tad/README.md`:

- En la sección `## Estructura`, agregar el directorio al árbol:

```
07-diccionarios/                # ← capítulo 3-7
└── ejercicios/
    └── 01-ejercicio/           # descripción breve
```

- En la sección `## Dependencias`, agregar `07-diccionarios/` a la lista si depende de data-structures.

### 6. Verificar

- `ls 0*/README.md` no debe mostrar archivos (no debe haber READMEs en raíces de capítulo)
- `ls 0*/ejercicios/*/README.md` no debe mostrar archivos (no debe haber READMEs por ejercicio)
- `ls 0*/ejercicios/README.md` debe mostrar exactamente 1 README por capítulo existente
- `go test ./NN-tema/...` debe pasar desde `~/AyP2/taller-tad/`

## Reglas generales

1. **No crear READMEs en la raíz del capítulo** — la información de estructura y dependencias ya está en el README raíz del repositorio.
2. **No crear READMEs por ejercicio** — todos los enunciados van en `ejercicios/README.md`.
3. **No duplicar información** — las URLs, instrucciones de setup y reemplazos de go.mod se documentan solo en el README raíz.
4. **Mantener sincronizados** `~/AyP2/apuntes/taller-tad/` y `~/AyP2/taller-tad/` en estructura de directorios.
5. **Numeración consistente**: capítulo 3-N del apunte → directorio NN-tema en taller-tad.
