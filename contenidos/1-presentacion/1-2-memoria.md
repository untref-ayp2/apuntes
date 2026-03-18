---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Gestión de memoria

En general la memoria de una computadora se puede clasificar en:

Memoria central o primaria
: Constituida por memoria volátil, más rápida y costosa que otros medios de almacenamiento. Es la memoria de trabajo del procesador, la RAM (*Random Access Memory*) de acceso rápido, donde se encuentran los programas en ejecución y sus datos. La información que almacena la RAM se pierde al interrumpirse el suministro de corriente eléctrica.

Memoria secundaria
: Conformada por el conjunto de memorias no volátiles. Es la memoria de persistencia de información. Ejemplos: discos rígidos, discos ópticos, memorias USB, etc. Conserva la información almacenada al interrumpirse el suministro de corriente eléctrica. Es más lenta y barata que la RAM.

## Organización de la Memoria central o primaria

Tanto los programas como el resto de la información que guarda la computadora se encuentran almacenados en la **memoria secundaria**.

Al lanzar la ejecución de un programa, las instrucciones y los datos iniciales se copian a la **memoria primaria**. Un programa en ejecución se denomina **proceso**.

En tiempo de ejecución, un proceso está asociado a una porción de la memoria primaria que se divide lógicamente en 4 segmentos:

Segmento de Código (*code segment*)
: Es la porción donde se localizarán las instrucciones que componen nuestro programa. Su tamaño se determina al comenzar la ejecución. Asociado a este segmento se encuentra un **puntero** que indica la próxima instrucción a ejecutar.

Segmento de Datos (*data segment*)
: Almacena las variables globales y estáticas. Su tamaño también queda determinado al comenzar la ejecución.

Pila (*stack segment*)
: Almacenará el contenido de las variables locales en cada invocación de una función. Cada entrada en la pila constituye un **marco de datos** (*stack frame*) que representa el contexto de una función en ejecución e incluye variables locales, parámetros y valores de retorno. Se va asignando en bloques de memoria dinámica y contigua. En Go, el tamaño inicial es pequeño (generalmente 2KB) y crece o decrece según sea necesario.

Memoria dinámica (*heap*)
: Es el espacio de memoria que se utiliza para la asignación dinámica de memoria. Su tamaño no está determinado al comenzar la ejecución y se va ajustando a medida que el programa solicita más memoria para almacenar datos. No es asignada en bloques de memoria contigua.

## Ejecución de programas

Para poder ejecutar un programa se deben seguir los siguientes pasos:

1\. Compilación y almacenamiento
: Los programas se almacenan inicialmente en la memoria secundaria (por ejemplo, en un disco duro o SSD). En el caso de Go como se trata de un lenguaje compilado, los archivos fuentes se compilan y se genera un archivo ejecutable que se almacena en el disco.

2\. Asignación de memoria central
: Al iniciar la ejecución, el **sistema operativo** carga el programa en la memoria central (RAM). Esto incluye las instrucciones del programa y los datos iniciales necesarios para su ejecución. La memoria asignada al programa se divide en segmentos específicos para el código, los datos, el *stack* y el *heap*. El programa en ejecución se denomina **proceso**.

3\. Ejecución del programa
: El procesador ejecuta una a una las instrucciones del programa desde el **segmento de código**. Cada vez que ejecuta una instrucción, avanza el puntero de instrucción al siguiente. Cuando ejecuta una llamada a una función, se crea un nuevo **marco de pila** (*frame*) en el ***stack*** para almacenar las variables locales y los parámetros de la función. Eventualmente, cuando la función termina, el marco de pila se elimina y el valor de retorno se transfiere al marco anterior desde donde se llamó a la función. Si durante la ejecución de una función se solicita memoria dinámica, se asigna en el ***heap***. En Go, durante la ejecución del programa, el recolector de basura (*garbage collector*) se encarga de liberar la memoria no utilizada en el heap, evitando así las fugas de memoria (*memory leaks*).

4\. Interacción con el sistema operativo
: El sistema operativo supervisa y gestiona la memoria asignada al programa. Si el programa necesita más memoria, puede solicitarla al sistema operativo, que ajustará el tamaño del ***heap*** o el ***stack*** según sea necesario.

5\. Liberación de memoria
: Al finalizar la ejecución, el sistema operativo libera toda la memoria asignada al programa, incluyendo los segmentos de código, datos, pila y heap.

En la figura a continuación, se muestra un esquema de la memoria de un proceso en ejecución. Cada segmento de memoria tiene un tamaño y una función específica en el programa. La figura es solo a modo didáctico y no representa la organización real de la memoria en Go, que es más compleja.

En el diagrama el ***stack*** se ubica en la parte superior de la memoria y crece hacia abajo; cuando no puede crecer más se produce un error de desbordamiento de pila (*stack overflow*). El ***heap*** se ubica en la parte inferior de la memoria, sobre los segmentos de código y datos y crece hacia arriba.

```{figure} ../_static/figures/MemoriaSegmentos_light.svg
---
width: 50%
class: only-light-mode
---
Segmentos de Memoria de un Proceso en Ejecución
```

```{figure} ../_static/figures/MemoriaSegmentos_dark.svg
---
width: 50%
class: only-dark-mode
---
Segmentos de Memoria de un Proceso en Ejecución
```

## Gestión de Memoria Dinámica en Go

La gestión de memoria es un aspecto clave en cualquier lenguaje de programación, ya que impacta en el rendimiento, la eficiencia y la estabilidad del software.

En Go, las variables se almacenan en el ***stack*** o en el ***heap*** dependiendo de su alcance, duración y cómo se utilizan.

El compilador de Go decide automáticamente si una variable debe almacenarse en el ***stack*** o en el ***heap***. Esto se conoce como ***Escape Analysis***. Si una variable **"escapa"** del alcance de la función, se almacena en el ***heap*** en lugar del ***stack***.

Consideraciones de Rendimiento
: El acceso a las variables que se encuentran en el ***stack*** es más directo y más rápido, mientras que el acceso a los datos en el ***heap*** es más lento ya que se deben referenciar desde el ***stack***, pero permite estructuras de datos más grandes y persistentes.

Veamos un ejemplo, dado el siguiente fragmento de código:

```{code-block} go
---
linenos: true
---
type Direccion struct {
    calle, ciudad, provincia string
    numero                   uint
}

type Persona struct {
    nombre, apellido string
    edad             uint
    direccion        Direccion
}

var num int = 5
var p1 Persona

func main() {
    p1.nombre = "Marcelo"
    p1.edad = 27

    p2 := Persona{nombre: "Pepe", edad: 23}
    p3 := Persona{"Juan", "Gonzalez", 34, Direccion{"Valentín Gomez",
                  "Caseros", "Buenos Aires", 742}}
    p4 := &p2

    dir:= Direccion{"Av. Corrientes", "CABA", "Buenos Aires", 1050}

    p4.apellido = "Martinez"
    p4.direccion = dir
}
```

El **Stack**, el **Heap** y el **Segmento de Datos** presentarán el siguiente estado:

```{figure} ../_static/figures/MapaDeMemoria_light.svg
---
name: mapa-memoria-Santi
class: only-light-mode
---
Mapa de Memoria
```

```{figure} ../_static/figures/MapaDeMemoria_dark.svg
---
name: mapa-memoria-Santi
class: only-dark-mode
---
Mapa de Memoria
```

Vamos a analizar cada variable en el código y justificar dónde se almacena:

- **`num`**

  ```go
  var num int = 5
  ```

  - **Almacenamiento:** **Segmento de Datos**
  - **Justificación:** `num` es una variable global (declarada a nivel de paquete). Al no ser una variable local, no se ubica en el *stack* de ninguna función, sino en el segmento de datos estáticos definido al inicio del proceso.

  ______________________________________________________________________

- **`p1`**

  ```go
  var p1 Persona
  p1.nombre = "Marcelo"
  p1.edad = 27
  ```

  - **Almacenamiento:** **Segmento de Datos** (estructura) y **Heap** (cadenas)
  - **Justificación:** `p1` es una variable de tipo `Persona` declarada como global. Su almacenamiento inicial será en el segmento de datos, ocupando el espacio fijo para la estructura. Sin embargo, los valores de los campos de tipo `string` se almacenan en el ***heap***, ya que en Go los *strings* son cabeceras que apuntan a una secuencia de bytes en memoria dinámica.

______________________________________________________________________

- **`p2`**

  ```go
  p2 := Persona{nombre: "Pepe", edad: 23}
  ```

  - **Almacenamiento:** **Stack** (estructura) y **Heap** (cadenas)
  - **Justificación:** `p2` es una variable local definida dentro de `main`, por lo que se crea en el marco de pila (*stack frame*) de dicha función. Al igual que con `p1`, el contenido de los campos de tipo `string` ("Pepe") se almacena en el ***heap***.

  ______________________________________________________________________

- **`p3`**

  ```go
  p3 := Persona{"Juan", "Gonzalez", 34, Direccion{"Valentín Gomez",
                "Caseros", "Buenos Aires", 742}}
  ```

  - **Almacenamiento:** **Stack** (estructura) y **Heap** (cadenas)
  - **Justificación:** La variable `p3` se almacena en el ***stack*** porque es una variable local. Sin embargo, los valores de tipo `string` como `"Juan"`, `"Gonzalez"`, `"Valentín Gomez"`, etc., se almacenan en el ***heap***, ya que las cadenas en Go son referencias a datos en memoria dinámica.

  ______________________________________________________________________

- **`p4`**

  ```go
  p4 := &p2
  ```

  - **Almacenamiento:** **Stack**
  - **Justificación:** `p4` es un puntero a `p2`. Como es una variable local en `main` que almacena una dirección de memoria, se ubica en el ***stack***. En este caso no ocurre un "escape" al *heap* porque `p2` no necesita persistir fuera del alcance de `main`. `p4` y `p2` permiten acceder a la misma ubicación de memoria de la estructura `Persona`.

  ______________________________________________________________________

- **`dir`**

  ```go
  dir := Direccion{"Av. Corrientes", "CABA", "Buenos Aires", 1050}
  ```

  - **Almacenamiento:** **Stack** (estructura) y **Heap** (cadenas)
  - **Justificación:** La variable `dir` se almacena en el ***stack*** porque es una variable local. Sin embargo, los valores de tipo `string` como `"Av. Corrientes"`, `"CABA"`, etc., se almacenan en el ***heap***.

  ______________________________________________________________________

**Resumen general:**

| Variable | Ubicación                               | Justificación                                     |
| -------- | --------------------------------------- | ------------------------------------------------- |
| `num`    | Segmento de Datos                       | Variable global simple.                           |
| `p1`     | Segmento de Datos (header) / Heap (str) | Estructura global, contenido de cadenas en heap.  |
| `p2`     | Stack (estructura) / Heap (cadenas)     | Variable local, contenido de cadenas en heap.     |
| `p3`     | Stack (estructura) / Heap (cadenas)     | Variable local, contenido de cadenas en heap.     |
| `p4`     | Stack                                   | Puntero local a una variable del stack (`p2`).    |
| `dir`    | Stack (estructura) / Heap (cadenas)     | Variable local, contenido de cadenas en heap.     |

En Go, el **compilador y el recolector de basura (GC)** optimizan el uso del stack y el heap. Las estructuras simples y de corta duración suelen estar en el stack, mientras que los datos más complejos o de mayor duración (como cadenas) se almacenan en el heap.

Go utiliza un **recolector de basura concurrente** para liberar memoria automáticamente. Es concurrente porque la mayor parte del trabajo de limpieza ocurre en paralelo con la ejecución del programa. Esto permite que el programador no tenga que liberar la memoria manualmente, evitando errores comunes como el acceso a memoria inválida.

Cuando existen datos en la memoria dinámica que ya no son accesibles (no están referenciados desde la pila ni el segmento de datos), el GC los marca para su eliminación y eventual liberación.

Para coordinar ciertos pasos del proceso de limpieza, el GC realiza pausas extremadamente breves denominadas ***stop-the-world*** (generalmente menores a un milisegundo). Go se destaca por optimizar estas pausas para que no interfieran con el rendimiento percibido del sistema:

- Minimiza las pausas para optimizar la latencia.
- Usa múltiples núcleos de CPU para ejecutar la recolección en paralelo.
- La mayor parte del marcado de objetos ocurre mientras el programa sigue corriendo.
- Detecta y elimina referencias a objetos no utilizados de forma eficiente.

```{admonition} Importante
---
class: Important
---
Un GC concurrente mejora el rendimiento y la experiencia del usuario, ya que evita grandes pausas en la ejecución del programa. Esto es fundamental en servidores y sistemas en tiempo real, donde una pausa larga podría afectar la respuesta del sistema.
```

## Ejercicio

Dado el siguiente fragmento de código:

```{code-block} go
---
linenos: true
---
package main

import "fmt"

// Variable global
var globalVar int = 42

func main() {
  // Variables locales
  localVar := 10
  localStr := "Hola, mundo"

  // Asignación dinámica
  dynamicSlice := make([]int, 3)
  dynamicSlice[0] = 1
  dynamicSlice[1] = 2
  dynamicSlice[2] = 3
}
```

Momentos a graficar:

1. Antes de la ejecución de la función `main`.
2. Durante la ejecución de la función `main`, después de la asignación de `localVar` y `localStr`.
3. Durante la ejecución de la función `main`, después de la asignación de `dynamicSlice`.

En el gráfico, identificar claramente qué variables están en el ***Stack*** y cuáles están en el ***Heap***, así como las referencias entre ellas.
