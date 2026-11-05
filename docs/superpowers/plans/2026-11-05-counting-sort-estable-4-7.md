# Counting Sort estable en 4-7 — Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reescribir la sección «Ordenamiento por Conteo» del capítulo 4-7 para separar
la variante básica (no estable) de la variante con sumas prefijo (estable), y rehacer el
applet para que permita animar las dos.

**Architecture:** Tres piezas independientes que se referencian entre sí: (1) una figura
SVG light/dark que muestra el pasaje de frecuencias a posiciones finales, (2) la reescritura
de la sección en el capítulo, con dos bloques de pseudocódigo, tablas de ejemplo y el nuevo
texto de presentación del applet, (3) el applet `counting-sort` con selector de variante
Inestable/Estable y etiquetas de origen en cada celda.

**Tech Stack:** Markdown (MyST 1.9.0), pseudocódigo en `{code-block} text`, SVG con clases
CSS light/dark, HTML/CSS/JS autocontenido (ES5, sin dependencias).

**Spec:** cambio acotado, sin documento de spec aparte. El diseño acordado en la
conversación está resumido en «Diseño» (abajo) y detallado en las tareas.

**Rama:** `correcciones-2027` en `~/AyP2/apuntes` (ya creada).

## Diseño

1. **Versión básica**: se conserva el pseudocódigo actual (contar y reconstruir), se marca
   explícitamente como **no estable** y se documenta que la salida se puede escribir sobre
   el arreglo de entrada o en un arreglo nuevo.
2. **Versión estable**: se introduce el conteo con sumas prefijo, se explica el pasaje de
   cuentas a posiciones finales (`conteo[v]` = posición final del último `v`, en 1-based),
   se muestra con tablas y una figura, y se explica que la estabilidad se consigue
   recorriendo el arreglo original **de derecha a izquierda**. La reconstrucción escribe en
   un arreglo de salida nuevo (no puede pisar la entrada).
3. **Applet**: dos botones, **Inestable** (conteo básico) y **Estable** (sumas prefijo +
   recorrido de derecha a izquierda). Cada elemento se muestra con una letra de origen
   (`a`, `b`, `c`, …) para que se vea el orden relativo de los valores repetidos. El modo
   inestable escribe los repetidos empezando por el último contado, con un texto que aclara
   que el algoritmo básico no define ese orden: la identidad se pierde al contar.

## Global Constraints

- Idioma: español rioplatense; voz verbal en infinitivo o «se puede + infinitivo»
  (nunca imperativo ni voseo) — `ESTILOS.md` §9.
- Pseudocódigo: mayúsculas sostenidas, `←`, `FUNCION`/`FIN FUNCION`,
  `SI`/`ENTONCES`/`SINO`/`FIN SI`, `MIENTRAS`/`HACER`/`FIN MIENTRAS`,
  `PARA`/`HASTA`/`HACER`/`FIN PARA`, `RETORNAR`; indentación de 4 espacios;
  comentarios `//` que expliquen el porqué.
- Admonitions: siempre `{admonition}` con `:class:` (nunca `{note}` suelto).
- Referencias cruzadas con `{ref}`, nunca `{numref}`.
- Figuras: par `_light.svg` / `_dark.svg`, clases `only-light-mode` / `only-dark-mode`,
  paleta de `ESTILOS.md` §4.
- Applets: par `_light.html` / `_dark.html` autocontenido, `<iframe>` HTML crudo envuelto
  en `<div class="only-html">`, ruta absoluta `/applets/...`, sin `@media`.
- Extranjerismos en cursiva (`*bucket*`, *count*), «Go» sin cursiva.
- **No hacer commit ni push sin autorización explícita del usuario.**
- Contexto para redactar: los ejercicios ya usan esta terminología
  (`taller-algoritmos/07-ordenamientos-lineales/ejercicios/04-counting-sort-estable`:
  «frecuencias → sumas prefijo → recorrer de derecha a izquierda»). El apunte debe
  coincidir con esos nombres.

---

### Task 1: Figura SVG del pasaje de cuentas a posiciones

**Files:**
- Create: `contenidos/_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort-prefijos_light.svg`
- Create: `contenidos/_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort-prefijos_dark.svg`

**Interfaces:**
- Consumes: nada (archivo nuevo).
- Produces: dos SVG con el mismo contenido textual; el capítulo los referencia desde
  Task 2 con las rutas de arriba.

**Contenido exacto de la figura** (idéntico en light y dark; solo cambian colores):

- Título (clase `.title`, 20px): `Counting Sort estable: de cuentas a posiciones finales`
- Fila 1 — etiqueta izquierda `arreglo original`, arriba de cada celda el índice `0`…`6`,
  celdas: `4 2 2 8 3 3 1`
- Fila 2 — etiqueta `conteo: frecuencias`, índices `0`…`8`, celdas: `0 1 2 2 1 0 0 0 1`
- Fila 3 — etiqueta `conteo: sumas prefijo`, índices `0`…`8`, celdas: `0 1 3 5 6 6 6 6 7`
- Fila 4 — etiqueta `salida`, arriba de cada celda el índice de origen, celdas y orígenes:
  `1`(6) `2`(1) `2`(2) `3`(4) `3`(5) `4`(0) `8`(3)
- Flechas verticales `arrow` entre filas 1→2 (`contar`), 2→3 (`sumas prefijo`) y
  3→4 (`colocar de derecha a izquierda`), con la etiqueta a la derecha de la flecha
  (clase `.note`, 14px, cursiva).
- Nota al pie (clase `.note`):
  `conteo[v] = cantidad de elementos <= v = posición final del último v (desde 1)`
- Nota al pie 2 (clase `.note`):
  `los repetidos quedan con sus índices de origen en orden creciente: 1,2 y 4,5`

**Layout:** `viewBox="0 0 760 470"`. Celda de 40×40 con separación 6 (paso 46), primera
celda en `x=150`. Centros verticales de las filas: 95, 200, 305, 410. Etiquetas de fila en
`x=20` con `text-anchor: start` y `dominant-baseline: middle`. Flechas en `x=600` apuntando
hacia abajo, longitud 55px, con el texto a `x=612`. Las dos notas al pie van en `y=448`
(centradas) — si no entran, subir el `viewBox` a 490 y repartirlas en `y=440` y `y=465`.

- [x] **Step 1: Crear la versión light**

Seguir `ESTILOS.md` §4 y `.opencode/skills/diagramas-svg/SKILL.md`. Estructura obligatoria:
`<defs><style>` con las clases `.title`, `.code`, `.note`, `.arrow`, `.variable-node`
(celdas de arreglos de entrada/conteo), `.value-node` (celdas de la salida) y `<marker
id="arrowhead">`; luego `<rect>` de fondo `#f0f2f5` con `rx="8"`; luego el título; luego
cuatro grupos `<g>` (uno por fila).

Colores light: fondo `#f0f2f5`, celdas de arreglo `fill:#e1f5ff; stroke:#4682b4`, celdas de
salida `fill:#ffe1e1; stroke:#e9967a`, texto `#333333`, flechas `#333333`, `stroke-width: 2`.

- [x] **Step 2: Crear la versión dark**

Copiar la light y reemplazar: fondo `#1e1e1e`, celdas de arreglo
`fill:#2d3748; stroke:#63b3ed`, celdas de salida `fill:#4a5568; stroke:#fc8181`, texto
`#e0e0e0`, flechas `#e0e0e0` (incluido el `fill` del `<polygon>` del marker). Los textos
deben quedar **idénticos** a la versión light.

- [x] **Step 3: Verificar el par**

```bash
cd /home/martin/AyP2/apuntes && ls -l contenidos/_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/
diff <(sed 's/#[0-9a-fA-F]\{6\}//g' contenidos/_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort-prefijos_light.svg) \
     <(sed 's/#[0-9a-fA-F]\{6\}//g' contenidos/_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort-prefijos_dark.svg)
```

Esperado: los dos archivos existen y el `diff` (ignorando colores) no muestra diferencias
de texto.

---

### Task 2: Reescribir la sección «Ordenamiento por Conteo»

**Files:**
- Modify: `contenidos/4-diseno-de-algoritmos/4-7-ordenamientos-lineales.md:13-67`

**Interfaces:**
- Consumes: las dos figuras de Task 1 (rutas relativas
  `../_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort-prefijos_light.svg`
  y `..._dark.svg`).
- Produces: el texto y los nombres (`CountingSort`, `CountingSortEstable`) que usan el
  applet (Task 4) y la tabla comparativa (Task 3).

- [x] **Step 1: Reemplazar la sección completa**

Reemplazar desde el encabezado `## Ordenamiento por Conteo (_Counting Sort_)` (línea 13)
hasta la línea `- **_In Place_**: no, requiere espacio adicional $O(k)$ para el arreglo de
conteo.` (línea 67), inclusive, por:

````markdown
## Ordenamiento por Conteo (_Counting Sort_)

El **Ordenamiento por Conteo** ordena elementos enteros dentro de un rango conocido $[0, k]$. En lugar de comparar elementos, cuenta cuántas veces aparece cada valor y luego reconstruye el arreglo ordenado a partir de esas cuentas.

Hay dos variantes del algoritmo y conviene distinguirlas desde el principio:

- La **versión básica** cuenta las apariciones y reconstruye el arreglo recorriendo el arreglo de conteo. Es la más simple, pero **no es estable**.
- La **versión con sumas prefijo** convierte las cuentas en posiciones finales dentro del arreglo ordenado y coloca cada elemento en su lugar. **Es estable**, y por eso es la que se usa como subrutina de Radix Sort.

Las dos comparten la misma idea: el valor del elemento se usa como **índice** de un arreglo auxiliar. Por eso el algoritmo necesita conocer el rango de valores de antemano.

### Versión básica: contar y reconstruir

El algoritmo sigue estos pasos:

1. **Inicialización**: crear un arreglo de conteo de tamaño $k+1$ e inicializarlo en cero.
2. **Conteo**: recorrer el arreglo original y, para cada elemento, incrementar la posición correspondiente del arreglo de conteo.
3. **Reconstrucción**: recorrer el arreglo de conteo en orden creciente y escribir cada valor tantas veces como se contó.

```{code-block} text
---
caption: Counting Sort básico (contar y reconstruir)
linenos: true
---
FUNCION CountingSort(arreglo, k)
    conteo ← arreglo de tamaño k+1 inicializado en 0
    n ← longitud(arreglo)

    PARA i ← 0 HASTA n-1 HACER
        conteo[arreglo[i]] ← conteo[arreglo[i]] + 1
    FIN PARA

    // la reconstrucción lee solo el arreglo de conteo, por eso se puede
    // escribir la salida sobre el mismo arreglo de entrada
    indice ← 0
    PARA valor ← 0 HASTA k HACER
        PARA repeticiones ← 1 HASTA conteo[valor] HACER
            arreglo[indice] ← valor
            indice ← indice + 1
        FIN PARA
    FIN PARA

    RETORNAR arreglo
FIN FUNCION
```

```{admonition} Pisar el arreglo original o devolver uno nuevo
:class: note

La reconstrucción lee únicamente el arreglo de conteo, así que escribir la salida sobre el mismo arreglo de entrada es seguro: no se pisa ningún dato que todavía haga falta. Esa es la versión del pseudocódigo anterior, y tiene la ventaja de no pedir espacio adicional para la salida (más allá del arreglo de conteo, $O(k)$).

La otra opción es reservar un arreglo nuevo de $n$ posiciones y escribir ahí, dejando la entrada intacta. Cuesta $O(n)$ de espacio extra, pero conserva el arreglo original: es lo que se necesita cuando no se puede modificar la entrada o cuando cada elemento tiene información asociada que hay que mantener.
```

```{admonition} La versión básica no es estable
:class: important

Contar y reconstruir alcanza para ordenar, pero no para preservar el orden relativo de los elementos iguales. Si los datos llevan información asociada —una edad con su nombre, un pedido con su fecha, una palabra con su frecuencia—, esa información queda desordenada dentro de cada grupo de valores iguales.
```

#### ¿Por qué no es estable?

Al contar, el algoritmo **descarta la identidad** de cada elemento: solo conserva cuántas veces aparece cada valor. Cuando dos elementos tienen el mismo valor, la reconstrucción los escribe uno detrás del otro sin ninguna información sobre cuál apareció primero. Con enteros sueltos no se nota —dos `3` son indistinguibles—, pero con datos compuestos importa.

No se trata de un descuido de la implementación sino de una consecuencia del diseño: en ningún momento hay una estructura que recuerde el orden de aparición. Y como el algoritmo no compara elementos, tampoco puede desempatar mirando el dato asociado.

Recordar la definición de estabilidad de {ref}`ordenamientos-por-comparacion`: un algoritmo es estable si mantiene el orden relativo de los elementos que tienen la misma clave.

### Versión estable: de cuentas a posiciones

Para que el ordenamiento sea estable hay que responder otra pregunta: no *cuántas veces* aparece cada valor, sino **en qué posición del arreglo ordenado termina cada elemento**. Las sumas prefijo dan esa información a partir de las cuentas.

Si `conteo[v]` guarda la frecuencia de `v`, acumular hacia la derecha da la cantidad de elementos menores o iguales a `v`:

$$\text{conteo}[v] \leftarrow \text{conteo}[v] + \text{conteo}[v-1]$$

Después de ese recorrido, `conteo[v]` es la cantidad de elementos $\leq v$; en otras palabras, la **posición final** (contando desde 1) del último elemento que vale `v`. En un arreglo indexado desde 0, ese último elemento va en el índice `conteo[v] - 1`, y los elementos anteriores de ese mismo valor van en los índices inmediatamente anteriores. El arreglo de conteo deja de guardar cuentas y pasa a guardar **posiciones**.

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort-prefijos_light.svg
---
class: only-light-mode
width: 100%
---
De cuentas a posiciones finales: las sumas prefijo indican dónde termina el bloque de cada valor y el recorrido de derecha a izquierda preserva el orden de los repetidos.
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort-prefijos_dark.svg
---
class: only-dark-mode
width: 100%
---
De cuentas a posiciones finales: las sumas prefijo indican dónde termina el bloque de cada valor y el recorrido de derecha a izquierda preserva el orden de los repetidos.
```

Por ejemplo, con el arreglo `[4, 2, 2, 8, 3, 3, 1]` y $k = 8$:

```{table} De frecuencias a posiciones finales
| valor                  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--------------------- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| conteo (frecuencias)   | 0 | 1 | 2 | 2 | 1 | 0 | 0 | 0 | 1 |
| conteo (sumas prefijo) | 0 | 1 | 3 | 5 | 6 | 6 | 6 | 6 | 7 |
```

Leer la segunda fila: `conteo[3] = 5` indica que hay 5 elementos $\leq 3$, así que el **último** `3` ocupa el índice `5 - 1 = 4`. Los elementos anteriores de ese bloque van en los índices previos. Notar que `conteo[5] = conteo[6] = conteo[7] = 6` porque no hay elementos con esos valores: el bloque de cada valor que no aparece es vacío.

**Cómo se reconstruye el arreglo ordenado.** Ya no hace falta recorrer el arreglo de conteo: se recorre el **arreglo original** y, para cada elemento, se calcula su posición con `conteo[valor] - 1`. Después de colocarlo se decrementa `conteo[valor]`, para que el siguiente elemento con el mismo valor use la posición libre anterior.

```{table} Colocación recorriendo el arreglo original de derecha a izquierda
| i | arreglo[i] | conteo[arreglo[i]] | posición | salida parcial |
| :-: | :-: | :-: | :-: | :--- |
| 6 | 1 | 1 | 0 | `[1, _, _, _, _, _, _]` |
| 5 | 3 | 5 | 4 | `[1, _, _, _, 3, _, _]` |
| 4 | 3 | 4 | 3 | `[1, _, _, 3, 3, _, _]` |
| 3 | 8 | 7 | 6 | `[1, _, _, 3, 3, _, 8]` |
| 2 | 2 | 3 | 2 | `[1, _, 2, 3, 3, _, 8]` |
| 1 | 2 | 2 | 1 | `[1, 2, 2, 3, 3, _, 8]` |
| 0 | 4 | 6 | 5 | `[1, 2, 2, 3, 3, 4, 8]` |
```

Observar los dos `3`: se colocan de atrás hacia adelante (primero el de `i = 5` en el índice 4, después el de `i = 4` en el índice 3), así que el que estaba antes en la entrada queda antes en la salida. Eso es lo que se llama estabilidad.

**Por qué se recorre de atrás hacia adelante.** Con `conteo[valor] - 1` se toma siempre la **última** posición libre del bloque de ese valor. Recorriendo la entrada desde el final, el último elemento de cada grupo es el primero en colocarse (en la última posición del bloque) y los anteriores se ubican en las posiciones previas, preservando el orden de aparición. Si se recorriera de izquierda a derecha con la misma fórmula, los elementos iguales quedarían en orden inverso: el arreglo seguiría ordenado, pero dejaría de ser estable.

```{code-block} text
---
caption: Counting Sort estable (sumas prefijo)
linenos: true
---
FUNCION CountingSortEstable(arreglo, k)
    n ← longitud(arreglo)
    salida ← arreglo de tamaño n
    conteo ← arreglo de tamaño k+1 inicializado en 0

    // 1. Contar apariciones
    PARA i ← 0 HASTA n-1 HACER
        conteo[arreglo[i]] ← conteo[arreglo[i]] + 1
    FIN PARA

    // 2. Sumas prefijo: conteo[v] pasa a ser la cantidad de elementos <= v,
    //    o sea la posición final (desde 1) del último elemento de valor v
    PARA v ← 1 HASTA k HACER
        conteo[v] ← conteo[v] + conteo[v-1]
    FIN PARA

    // 3. Colocar de derecha a izquierda: cada elemento entra al final de su
    //    bloque y el contador retrocede para el siguiente elemento igual
    PARA i ← n-1 HASTA 0 PASO -1 HACER
        valor ← arreglo[i]
        salida[conteo[valor] - 1] ← arreglo[i]
        conteo[valor] ← conteo[valor] - 1
    FIN PARA

    RETORNAR salida
FIN FUNCION
```

```{admonition} La versión estable no puede escribir sobre la entrada
:class: note

La colocación lee `arreglo[i]` mientras escribe en `salida`, así que necesita un arreglo de salida propio: no se puede reutilizar la entrada como en la versión básica. El espacio extra es $O(n)$ para la salida más $O(k)$ para el arreglo de conteo.
```

<div class="only-html">

A continuación se puede visualizar paso a paso el funcionamiento de Counting Sort con sus dos variantes. Los botones **Inestable** y **Estable** permiten elegir cuál animar; cada elemento se muestra con una letra que identifica su posición de origen, de modo que se pueda ver qué ocurre con los valores repetidos. Se puede ingresar un arreglo de hasta 10 enteros no negativos separados por coma, o generar uno aleatorio con el botón **Aleatorio**. Los botones ◀ ▶ permiten avanzar paso a paso, y >> reproduce la animación automáticamente. La vista muestra el arreglo original, el arreglo de conteo y el arreglo ordenado.

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort_light.html" width="100%" height="560px" class="only-light-mode"></iframe>

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort_dark.html" width="100%" height="560px" class="only-dark-mode"></iframe>

</div>

### Complejidad

Las dos variantes son $O(n + k)$: se recorre el arreglo una vez para contar, se recorre el arreglo de conteo una vez para acumular las sumas prefijo (solo en la variante estable) y se recorre el arreglo una vez más para reconstruir o colocar. Es eficiente cuando $k$ es del orden de $n$ o menor. Si $k$ es mucho mayor que $n$, el arreglo de conteo se vuelve impracticable.

- **Estable**: la variante con sumas prefijo, sí; la básica, no.
- **_In Place_**: no. El arreglo de conteo requiere $O(k)$ en ambas variantes. La versión básica puede escribir la salida sobre la entrada y no suma espacio; la versión estable necesita un arreglo de salida de $O(n)$ porque lee la entrada mientras coloca.
````

- [x] **Step 2: Verificar que la sección quedó bien delimitada**

```bash
cd /home/martin/AyP2/apuntes && sed -n '1,60p' contenidos/4-diseno-de-algoritmos/4-7-ordenamientos-lineales.md
grep -n "^##\|^###\|^####" contenidos/4-diseno-de-algoritmos/4-7-ordenamientos-lineales.md
```

Esperado: la sección termina en `### Complejidad` y le sigue `## Ordenamiento por Urnas (_Bucket Sort_)`, sin restos de la versión anterior (`indice ← 0` aparece una sola vez, dentro del pseudocódigo básico).

- [x] **Step 3: Compilar el HTML para validar la sintaxis MyST**

```bash
cd /home/martin/AyP2/apuntes/contenidos && myst build --html 2>&1 | tail -15
```

Esperado: build exitoso; sin advertencias de figura faltante ni de `{ref}` inexistente.

---

### Task 3: Tabla comparativa y referencia desde Radix Sort

**Files:**
- Modify: `contenidos/4-diseno-de-algoritmos/4-7-ordenamientos-lineales.md` (sección `## Comparación`, tabla y notas al pie; y primer párrafo de `## Radix Sort`)

**Interfaces:**
- Consumes: los nombres y variantes definidos en Task 2.
- Produces: nada que consuman otras tareas.

- [x] **Step 1: Separar Counting Sort en dos filas de la tabla**

Reemplazar el bloque `{table} Algoritmos de Ordenamiento Lineal` completo (tabla + las dos
notas al pie `\*` y `\*\*`) por:

````markdown
```{table} Algoritmos de Ordenamiento Lineal
| Algoritmo                    | Complejidad       | Estable | In Place | Requisito                          |
| :--------------------------- | :---------------: | :-----: | :------: | :--------------------------------- |
| Counting Sort (básico)       | $O(n + k)$        | No      | No*      | Rango acotado $[0, k]$             |
| Counting Sort (con prefijos) | $O(n + k)$        | Sí      | No       | Rango acotado $[0, k]$             |
| Bucket Sort                  | $O(n + k)$        | Sí**    | No       | Distribución uniforme              |
| Radix Sort                   | $O(n \times d)$   | Sí      | No       | Valores descomponibles en dígitos  |
```

\* La versión básica puede escribir la salida sobre el arreglo de entrada, pero igual necesita $O(k)$ para el arreglo de conteo.
\*\* Si el algoritmo intra-bucket es estable.
````

- [x] **Step 2: Ajustar el primer párrafo de Radix Sort**

En el párrafo que empieza con «El **Radix Sort** ordena elementos procesándolos dígito por
dígito…», reemplazar la oración «Utiliza un algoritmo de ordenamiento **estable** (como
Counting Sort o Bucket Sort) como subrutina para ordenar por cada dígito.» por:

````markdown
Utiliza un algoritmo de ordenamiento **estable** (como Counting Sort o Bucket Sort) como subrutina para ordenar por cada dígito. En la práctica se usa la variante estable de Counting Sort de la sección anterior: la que convierte las cuentas en posiciones con sumas prefijo y coloca recorriendo la entrada de derecha a izquierda.
````

- [x] **Step 3: Verificar**

```bash
cd /home/martin/AyP2/apuntes && grep -n "Counting Sort" contenidos/4-diseno-de-algoritmos/4-7-ordenamientos-lineales.md | tail -8
cd /home/martin/AyP2/apuntes/contenidos && myst build --html 2>&1 | tail -8
```

Esperado: la tabla tiene cuatro filas de algoritmos (dos de Counting Sort) y el build pasa.

---

### Task 4: Applet con variante Inestable / Estable

**Files:**
- Modify: `contenidos/_static/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort_light.html`
- Modify: `contenidos/_static/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort_dark.html`

**Interfaces:**
- Consumes: la semántica de Task 2 (conteo básico vs sumas prefijo + recorrido de derecha a
  izquierda).
- Produces: los archivos que referencia el `<iframe>` de Task 2 (mismas rutas, mismos
  nombres).

**Cambios en el HTML**

1. Agregar `id="countLabel"` al `div.section-label` que dice `Arreglo de conteo`.
2. Agregar el selector de variante en el sidebar, arriba del botón **Aleatorio**:

```html
<div class="variants" id="varSelector">
  <button class="var-btn active" data-mode="unstable">Inestable</button>
  <button class="var-btn" data-mode="stable">Estable</button>
</div>
```

**CSS a agregar** (después de `.btn-gen.primary:hover`):

```css
.variants{display:flex;gap:2px}
.variants .var-btn{flex:1;padding:4px 6px;border:1px solid var(--border);border-radius:4px;background:var(--btn-bg);color:var(--btn-text);font-size:11px;cursor:pointer;font-weight:600;transition:background .15s}
.variants .var-btn.active{background:var(--mode-active-bg);color:var(--mode-active-text);border-color:var(--mode-active-bg)}
.variants .var-btn:hover:not(.active){background:var(--btn-hover)}
.cell{position:relative}
.cell .tag{position:absolute;top:1px;right:3px;font-size:9px;font-weight:600;line-height:1;opacity:.65;font-family:system-ui,sans-serif}
```

Y agregar a `:root`: `--mode-active-bg` y `--mode-active-text`
(light: `#1d4ed8` / `#ffffff`; dark: `#60a5fa` / `#1a1b2e`).

**JS: estado y modos**

Reemplazar `var k=9;` y las declaraciones siguientes por:

```js
var k=9;
var original=[];
var steps=[];
var currentStep=-1;
var isPlaying=false;
var playTimer=null;
var speedVal=1500;
var currentMode='unstable';
var letters='abcdefghij';
```

Agregar el handler del selector (después del handler de `btnRandom`):

```js
var varBtns=document.querySelectorAll('#varSelector button');
varBtns.forEach(function(b){
  b.addEventListener('click',function(){
    stopPlay();
    varBtns.forEach(function(x){x.classList.remove('active');});
    b.classList.add('active');
    currentMode=b.dataset.mode;
    regenFromCurrent();
  });
});
```

**JS: generación de pasos** — reemplazar `buildSteps` por las tres funciones siguientes:

```js
function buildSteps(arr){
  if(currentMode==='stable')buildStepsStable(arr);
  else buildStepsUnstable(arr);
}

function buildStepsUnstable(arr){
  original=arr.slice();
  var n=arr.length;
  var count=new Array(k+1).fill(0);
  var sorted=new Array(n).fill(null);
  var sortedTags=new Array(n).fill('');
  var ocurrencias=[];
  for(var v=0;v<=k;v++)ocurrencias.push([]);
  steps=[];

  steps.push({
    desc:'Estado inicial, versión inestable. Arreglo original con '+n+' elementos, k='+k+'.',
    origHL:-1,countHL:-1,sortedHL:-1,countVals:count.slice(),
    sortedVals:sorted.slice(),sortedTags:sortedTags.slice(),phase:'init'
  });

  for(var i=0;i<n;i++){
    var val=arr[i];
    count[val]++;
    ocurrencias[val].push(i);
    steps.push({
      desc:'Contando: arr['+i+'] = '+val+' ('+letters[i]+'). conteo['+val+'] → '+count[val]+'.',
      origHL:i,countHL:val,countVals:count.slice(),
      sortedVals:sorted.slice(),sortedTags:sortedTags.slice(),phase:'count'
    });
  }

  // Reconstrucción: cada bloque se llena tomando las ocurrencias desde el
  // final de la lista, para mostrar que el orden de origen no se conserva
  var si=0;
  for(var v=0;v<=k;v++){
    while(ocurrencias[v].length>0){
      var origen=ocurrencias[v].pop();
      sorted[si]=v;
      sortedTags[si]=letters[origen];
      steps.push({
        desc:'Reconstruyendo: el bloque del '+v+' empieza en la posición '+si+'. Se escribe '+letters[origen]+' en ordenado['+si+']; el algoritmo básico no distingue el orden de origen.',
        origHL:-1,countHL:v,countVals:count.slice(),
        sortedVals:sorted.slice(),sortedTags:sortedTags.slice(),sortedHL:si,phase:'reconstruct'
      });
      count[v]--;
      si++;
    }
  }

  steps.push({
    desc:'¡Ordenado! Pero no es estable: los valores repetidos no conservan su orden de origen.',
    origHL:-1,countHL:-1,countVals:count.slice(),
    sortedVals:sorted.slice(),sortedTags:sortedTags.slice(),phase:'done'
  });

  render(0);
}

function buildStepsStable(arr){
  original=arr.slice();
  var n=arr.length;
  var count=new Array(k+1).fill(0);
  var sorted=new Array(n).fill(null);
  var sortedTags=new Array(n).fill('');
  steps=[];

  steps.push({
    desc:'Estado inicial, versión estable. Arreglo original con '+n+' elementos, k='+k+'.',
    origHL:-1,countHL:-1,sortedHL:-1,countVals:count.slice(),
    sortedVals:sorted.slice(),sortedTags:sortedTags.slice(),phase:'init'
  });

  for(var i=0;i<n;i++){
    var val=arr[i];
    count[val]++;
    steps.push({
      desc:'Contando: arr['+i+'] = '+val+' ('+letters[i]+'). conteo['+val+'] → '+count[val]+'.',
      origHL:i,countHL:val,countVals:count.slice(),
      sortedVals:sorted.slice(),sortedTags:sortedTags.slice(),phase:'count'
    });
  }

  // Sumas prefijo: las cuentas se convierten en posiciones finales
  for(var v=1;v<=k;v++){
    var previo=count[v-1];
    var antes=count[v];
    count[v]=antes+previo;
    steps.push({
      desc:'Sumas prefijo: conteo['+v+'] = '+antes+' + '+previo+' = '+count[v]+'. Ahora indica la posición final del último '+v+'.',
      origHL:-1,countHL:v,countVals:count.slice(),
      sortedVals:sorted.slice(),sortedTags:sortedTags.slice(),phase:'prefix'
    });
  }

  // Colocación de derecha a izquierda: así se conserva el orden de los iguales
  for(var i=n-1;i>=0;i--){
    var valor=arr[i];
    var pos=count[valor]-1;
    sorted[pos]=valor;
    sortedTags[pos]=letters[i];
    steps.push({
      desc:'Colocando de derecha a izquierda: arr['+i+'] = '+valor+' ('+letters[i]+') → ordenado['+pos+']. Queda detrás de sus iguales.',
      origHL:i,countHL:valor,countVals:count.slice(),
      sortedVals:sorted.slice(),sortedTags:sortedTags.slice(),sortedHL:pos,phase:'place'
    });
    count[valor]--;
  }

  steps.push({
    desc:'¡Ordenado y estable! Los valores repetidos conservan su orden relativo.',
    origHL:-1,countHL:-1,countVals:count.slice(),
    sortedVals:sorted.slice(),sortedTags:sortedTags.slice(),phase:'done'
  });

  render(0);
}
```

**JS: `render`** — reemplazar la función `render` por:

```js
function render(idx){
  currentStep=idx;
  var s=steps[idx];
  countLabel.textContent=currentMode==='stable'?'Arreglo de conteo (posiciones finales)':'Arreglo de conteo (frecuencias)';
  origRow.innerHTML='';
  countIdxRow.innerHTML='';
  countRow.innerHTML='';
  sortedRow.innerHTML='';

  for(var i=0;i<original.length;i++){
    var c=document.createElement('div');
    c.className='cell arr'+(i===s.origHL?' active':'');
    c.appendChild(document.createTextNode(String(original[i])));
    var t=document.createElement('span');
    t.className='tag';
    t.textContent=letters[i];
    c.appendChild(t);
    origRow.appendChild(c);
  }

  for(var i=0;i<=k;i++){
    var c=document.createElement('div');
    c.className='cell idx';
    c.textContent=i;
    countIdxRow.appendChild(c);
  }

  for(var i=0;i<=k;i++){
    var c=document.createElement('div');
    var cls='cell count';
    if(i===s.countHL)cls+=' active';
    if(s.countVals[i]===0&&i<s.countHL&&(s.phase==='reconstruct'||s.phase==='place'))cls+=' done';
    c.className=cls;
    c.textContent=s.countVals[i];
    countRow.appendChild(c);
  }

  for(var i=0;i<original.length;i++){
    var lleno=s.sortedVals[i]!==null;
    var c=document.createElement('div');
    c.className='cell sorted'+(lleno?' built':' empty')+(i===s.sortedHL?' active':'');
    c.appendChild(document.createTextNode(lleno?String(s.sortedVals[i]):''));
    if(lleno){
      var t=document.createElement('span');
      t.className='tag';
      t.textContent=s.sortedTags[i];
      c.appendChild(t);
    }
    sortedRow.appendChild(c);
  }

  descEl.textContent=s.desc;
  stepCounterEl.textContent='Paso '+(idx+1)+' / '+steps.length;
  arrInfoEl.textContent=original.length+' elem'+(original.length!==1?'s':'')+' · '+(currentMode==='stable'?'estable':'inestable');

  updateBtns();
}
```

**JS: limpiar** — en el handler de `btnClear`, reemplazar el `steps=[{...}]` por:

```js
steps=[{desc:'Applet limpiado. Ingresar valores o generar aleatorios.',origHL:-1,countHL:-1,sortedHL:-1,countVals:new Array(k+1).fill(0),sortedVals:[],sortedTags:[],phase:'init'}];
```

**JS: generador aleatorio** — para que la estabilidad se vea casi siempre, limitar el rango
de los valores aleatorios:

```js
function generateRandom(){
  var n=4+Math.floor(Math.random()*4);
  var maxV=Math.min(k,5);
  var arr=[];
  for(var i=0;i<n;i++)arr.push(Math.floor(Math.random()*(maxV+1)));
  valInput.value=arr.join(',');
  buildSteps(arr);
}
```

**JS: referencia al label** — agregar junto a las demás declaraciones:

```js
var countLabel=document.getElementById('countLabel');
```

Mantener sin cambios: parseo de entrada (2 a 10 enteros en `[0, k]`), slider de `k`,
controles de navegación, velocidad, atajos de teclado y el ejemplo inicial
`buildSteps([4,2,2,8,3,3,1]);`.

- [x] **Step 1: Aplicar los cambios en `counting-sort_light.html`**

Seguir las indicaciones anteriores en el orden en que aparecen (HTML, CSS, JS).

- [x] **Step 2: Generar la versión dark**

```bash
cd /home/martin/AyP2/apuntes/contenidos/_static/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales
cp counting-sort_light.html counting-sort_dark.html
```

Y reaplicar la paleta oscura en `counting-sort_dark.html` (solo CSS): bloque `:root`
completo con los valores dark, `body{background:#1a1b2e;color:#e0e0e0;...}`, los tres
`box-shadow` con `rgba(96,165,250,.3)`, `--mode-active-bg:#60a5fa`,
`--mode-active-text:#1a1b2e`, `.btn-gen.primary{...color:#1a1b2e}` y
`.controls button.playing{...color:#1a1b2e}`. El `<body>` y el `<script>` deben quedar
idénticos a la versión light.

- [x] **Step 3: Verificar que solo cambia el CSS**

```bash
cd /home/martin/AyP2/apuntes/contenidos/_static/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales
diff counting-sort_light.html counting-sort_dark.html | grep -c '^[<>]'
diff <(sed -n '/<body>/,$p' counting-sort_light.html) <(sed -n '/<body>/,$p' counting-sort_dark.html)
```

Esperado: el segundo `diff` sale vacío (body y script idénticos); el primero solo muestra
diferencias de colores.

- [x] **Step 4: Probar el applet en el navegador (modo light)**

```bash
cd /home/martin/AyP2/apuntes/contenidos/_static && python3 -m http.server 8765
```

Con la skill `webapp-testing` (Playwright) navegar a
`http://localhost:8765/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort_light.html`
y comprobar:

1. Carga con el ejemplo `4,2,2,8,3,3,1` en modo **Inestable**; las celdas del arreglo
   original muestran las letras `a`…`g`.
2. Recorrer todos los pasos con ▶ hasta el final: la fila *Arreglo ordenado* queda
   `[1, 2, 2, 3, 3, 4, 8]` y las etiquetas de los `2` y de los `3` aparecen invertidas
   respecto del origen.
3. Cambiar a **Estable**: vuelve al paso 1, aparece la fase de sumas prefijo (los valores
   del arreglo de conteo llegan a `0 1 3 5 6 6 6 6 7`) y al final las etiquetas de los
   repetidos quedan en orden de origen (`b` antes que `c`, `e` antes que `f`).
4. No hay scrollbars verticales ni horizontales dentro del iframe de 560px.
5. `>>` reproduce y `⏸` pausa; el slider de velocidad cambia el ritmo.

- [x] **Step 5: Probar la versión dark**

Navegar a `..._dark.html` y repetir los puntos 1 a 3. Verificar que el fondo es
`#1a1b2e` y que las letras de origen se leen sobre las celdas oscuras.

- [x] **Step 6: Cortar el servidor**

```bash
# Ctrl-C en la terminal donde corre python3 -m http.server
```

---

### Task 5: Verificación integral y regeneración del PDF

**Files:**
- Modify (generados): `contenidos/exports/apunte-ayp2.pdf` (lo produce `make pdf`)

**Interfaces:**
- Consumes: todo lo anterior.
- Produces: build limpio del libro y PDF actualizado.

- [x] **Step 1: Formatear**

```bash
cd /home/martin/AyP2/apuntes && make fmt
git diff --stat
```

Esperado: cambios solo en los archivos tocados (si `mdformat` reescribe alguna tabla, se
acepta el formato resultante).

- [x] **Step 2: Build completo (HTML + PDF)**

```bash
cd /home/martin/AyP2/apuntes && make build 2>&1 | tail -20
```

Esperado: build sin errores. `contenidos/exports/apunte-ayp2.pdf` regenerado.

- [x] **Step 3: Revisar el PDF**

Abrir `contenidos/exports/apunte-ayp2.pdf` en la página de «Ordenamiento por Conteo» y
comprobar: los dos pseudocódigos completos, la figura light incluida (el bloque
`only-html` del applet no aparece), las dos tablas de ejemplo y la tabla comparativa con
las dos filas de Counting Sort.

- [x] **Step 4: Revisar el HTML en el sitio**

```bash
cd /home/martin/AyP2/apuntes && make start
```

Navegar al capítulo 4-7 y comprobar el applet embebido en modo claro y oscuro. Detener el
servidor al terminar.

- [ ] **Step 5: Commit (solo con autorización explícita)**

```bash
cd /home/martin/AyP2/apuntes && git status
```

Esperado: 5 archivos modificados/creados (1 `.md`, 2 `.html`, 2 `.svg`, más el PDF).
**No ejecutar `git commit` ni `git push` hasta que el usuario lo autorice.**

---

## Notas para el ejecutor

- El capítulo usa `{table}` con el caption en la misma línea del directive; respetarlo.
- Las figuras van con bloque YAML (`class:`, `width:`) como en `4-1-recursividad.md`, no con
  `:class:`.
- El build PDF elimina `<div class="only-html">`, así que el texto de presentación del
  applet no debe contener información imprescindible: la sección tiene que entenderse sin
  el applet (por eso la figura y las tablas de ejemplo).
- Si `mdformat` rompe alguna tabla, priorizar la legibilidad de la fuente y volver a correr
  `make build`.
