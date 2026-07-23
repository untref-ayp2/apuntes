# Ejercicios inline 1-2 y 1-3 — Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reemplazar las referencias rotas a `taller-go/02-memoria/ejercicios/` y
`taller-go/03-analisis-de-algoritmos/ejercicios/` por listas numeradas de
ejercicios inline en cada capítulo.

**Architecture:** Edición quirúrgica de dos archivos `.md`. Cada tarea reemplaza
la sección `## Ejercicios` (últimas líneas del archivo) por contenido inline.
Los ejercicios de 1-3 usan pseudocódigo según convención de `ESTILOS.md`.

**Tech Stack:** Markdown (MyST), pseudocódigo en `{code-block} text`.

## Global Constraints

- Idioma: español rioplatense
- Tono: moderadamente formal
- Pseudocódigo: mayúsculas sostenidas, `←` para asignación, `FUNCION`/`FIN FUNCION`,
  `SI`/`ENTONCES`/`SINO`/`FIN SI`, `MIENTRAS`/`HACER`/`FIN MIENTRAS`,
  `PARA`/`HASTA`/`HACER`/`FIN PARA`, `RETORNAR`
- Ejercicios en lista numerada simple (no `{exercise}`, no admonition)
- No tocar nada más del archivo que la sección `## Ejercicios`

---

### Task 1: Ejercicios inline para 1-2-memoria.md

**Files:**
- Modify: `apuntes/contenidos/1-presentacion/1-2-memoria.md` (líneas 242-245)

**Interfaces:**
- Consumes: el archivo existente con sección `## Ejercicios` al final
- Produces: misma sección con 5 ejercicios inline en lista numerada

- [ ] **Step 1: Reemplazar la sección Ejercicios**

Reemplazar desde la línea 242 (`## Ejercicios`) hasta el final del archivo
por el siguiente contenido:

```markdown
## Ejercicios

1. **Mapa de memoria.** Dado el siguiente código, dibujá un esquema de la
   memoria indicando en qué segmento (datos, stack o heap) se almacena cada
   variable y su contenido:

   ```{code-block} go
   :linenos:

   var global int = 42

   type Punto struct {
       X, Y int
   }

   func main() {
       a := 10
       b := &a
       c := Punto{X: 3, Y: 7}
       d := "hola"
   }
   ```

2. **Escape analysis.** Para cada una de las siguientes funciones, indicá si
   la variable creada escapa al heap o se queda en el stack. Justificá:

   ```{code-block} go
   :linenos:

   func f1() int {
       x := 5
       return x
   }

   func f2() *int {
       x := 5
       return &x
   }

   func f3() {
       s := make([]int, 10)
       s[0] = 1
       fmt.Println(s[0])
   }
   ```

3. **Strings en heap.** Explicá por qué el contenido de un `string` en Go
   siempre se almacena en el heap, incluso cuando la variable que lo contiene
   es local. ¿Qué parte de la variable queda en el stack?

4. **Stack frames.** Dada la secuencia de llamadas `main()` → `calcular()` →
   `sumar(a, b int)`, describí el contenido del stack en cada paso. Indicá
   qué datos contiene cada stack frame (parámetros, variables locales,
   dirección de retorno).

5. **Garbage collector.** Explicá brevemente:
   - Qué problema resuelve el garbage collector concurrente de Go.
   - Qué significa *stop-the-world* y por qué las pausas son del orden de
     microsegundos en Go.
   - Qué ventaja tiene un GC concurrente frente a uno no concurrente.
```

- [ ] **Step 2: Verificar el cambio**

```bash
cd /home/martin/AyP2/apuntes && git diff contenidos/1-presentacion/1-2-memoria.md
```

Esperado: la sección `## Ejercicios` ahora contiene 5 ejercicios numerados
con bloques de código Go.

---

### Task 2: Ejercicios inline para 1-3-analisis-de-algoritmos.md

**Files:**
- Modify: `apuntes/contenidos/1-presentacion/1-3-analisis-de-algoritmos.md` (líneas 444-447)

**Interfaces:**
- Consumes: el archivo existente con sección `## Ejercicios` al final
- Produces: misma sección con 4 ejercicios inline (el 4.º con 7 fragmentos)

- [ ] **Step 1: Reemplazar la sección Ejercicios**

Reemplazar desde la línea 444 (`## Ejercicios`) hasta el final del archivo
por el siguiente contenido:

```markdown
## Ejercicios

1. **Máximo entre dos números.** Dado el siguiente pseudocódigo, calculá la
   cantidad de operaciones elementales que ejecuta y determiná su O grande:

   ```{code-block} text
   ---
   caption: Algoritmo máximo
   linenos: true
   ---
   FUNCION maximo(x, y)
       SI x >= y ENTONCES
           RETORNAR x
       SINO
           RETORNAR y
       FIN SI
   FIN FUNCION
   ```

2. **Potencia.** Dado el siguiente pseudocódigo, calculá la cantidad de
   operaciones elementales y determiná su O grande:

   ```{code-block} text
   ---
   caption: Algoritmo potencia
   linenos: true
   ---
   FUNCION potencia(x, n)
       resultado ← 1.0
       PARA i ← 0 HASTA n-1 HACER
           resultado ← resultado * x
       FIN PARA
       RETORNAR resultado
   FIN FUNCION
   ```

3. **Recorrer un arreglo.** Dado el siguiente pseudocódigo, calculá la
   cantidad de operaciones elementales y determiná su O grande:

   ```{code-block} text
   ---
   caption: Algoritmo listar alumnos
   linenos: true
   ---
   FUNCION listarAlumnos(a)
       i ← 0
       MIENTRAS i < LONGITUD(a) HACER
           ESCRIBIR a[i].nombre + " " + a[i].apellido
           i ← i + 1
       FIN MIENTRAS
       RETORNAR
   FIN FUNCION
   ```

4. **Fragmentos de código.** Para cada uno de los siguientes fragmentos,
   determiná el tiempo de ejecución en notación O grande:

   ```{code-block} text
   ---
   caption: Fragmento 1
   linenos: true
   ---
   PARA i ← 0 HASTA n-1 HACER
       sum ← sum + 1
   FIN PARA
   ```

   ```{code-block} text
   ---
   caption: Fragmento 2
   linenos: true
   ---
   PARA i ← 0 HASTA n-1 PASO 2 HACER
       sum ← sum + 1
   FIN PARA
   ```

   ```{code-block} text
   ---
   caption: Fragmento 3
   linenos: true
   ---
   PARA i ← 0 HASTA n-1 HACER
       PARA j ← 0 HASTA n-1 HACER
           sum ← sum + 1
       FIN PARA
   FIN PARA
   ```

   ```{code-block} text
   ---
   caption: Fragmento 4
   linenos: true
   ---
   PARA i ← 0 HASTA n-1 HACER
       sum ← sum + 1
   FIN PARA
   PARA j ← 0 HASTA n-1 HACER
       sum ← sum + 1
   FIN PARA
   ```

   ```{code-block} text
   ---
   caption: Fragmento 5
   linenos: true
   ---
   PARA i ← 0 HASTA n-1 HACER
       PARA j ← 0 HASTA n*n-1 HACER
           sum ← sum + 1
       FIN PARA
   FIN PARA
   ```

   ```{code-block} text
   ---
   caption: Fragmento 6
   linenos: true
   ---
   PARA i ← 0 HASTA n-1 HACER
       PARA j ← 0 HASTA i-1 HACER
           sum ← sum + 1
       FIN PARA
   FIN PARA
   ```

   ```{code-block} text
   ---
   caption: Fragmento 7
   linenos: true
   ---
   PARA i ← 0 HASTA n-1 HACER
       PARA j ← 0 HASTA n*n-1 HACER
           PARA k ← 0 HASTA j-1 HACER
               sum ← sum + 1
           FIN PARA
       FIN PARA
   FIN PARA
   ```

- [ ] **Step 2: Verificar el cambio**

```bash
cd /home/martin/AyP2/apuntes && git diff contenidos/1-presentacion/1-3-analisis-de-algoritmos.md
```

Esperado: la sección `## Ejercicios` ahora contiene 4 ejercicios numerados
con bloques de pseudocódigo.
```

- [ ] **Step 3: Build de verificación (opcional)**

```bash
cd /home/martin/AyP2/apuntes && make build 2>&1 | tail -20
```

Esperado: build exitoso sin errores de sintaxis MyST.
