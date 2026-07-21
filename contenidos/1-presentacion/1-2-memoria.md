---
label: memoria
---

# Gestión de memoria

En general la memoria de una computadora se puede clasificar en:

Memoria central o primaria
: Constituida por memoria volátil, más rápida y costosa que otros medios de almacenamiento. Es la memoria de trabajo del procesador, la RAM (*Random Access Memory*) de acceso rápido, donde se encuentran los programas en ejecución y sus datos. La información que almacena la RAM se pierde al interrumpirse el suministro eléctrico.

Memoria secundaria
: Conformada por el conjunto de memorias no volátiles. Es la memoria de persistencia de información. Ejemplos: discos rígidos, discos ópticos, memorias USB, etc. Conserva la información almacenada al interrumpirse el suministro de corriente eléctrica. Es más lenta y barata que la RAM.

## Organización de la Memoria central o primaria

Tanto los programas como el resto de la información que guarda la computadora se encuentran almacenados en la **memoria secundaria**.

Al lanzar la ejecución de un programa, las instrucciones y los datos iniciales se copian a la **memoria primaria**. Un programa en ejecución se denomina **proceso**.

En tiempo de ejecución, un proceso está asociado a una porción de la memoria primaria que se divide lógicamente en 4 segmentos:

Segmento de Código (*code segment*)
: Es la porción donde se localizan las instrucciones que componen nuestro programa. Su tamaño se determina al comenzar la ejecución. Asociado a este segmento se encuentra un **puntero** que indica la próxima instrucción a ejecutar.

Segmento de Datos (*data segment*)
: Almacena las variables globales y estáticas. Su tamaño también queda determinado al comenzar la ejecución.

Pila (*stack segment*)
: Almacenará el contenido de las variables locales en cada invocación de una función. Cada entrada en la pila constituye un **marco de datos** (*stack frame*) que representa el contexto de una función en ejecución e incluye variables locales, parámetros y valores de retorno. Se asigna como un bloque de memoria contigua. En Go, el tamaño inicial del *stack* es pequeño (generalmente 2KB) pero no es de tamaño fijo como en C, sino que tiene tamaño dinámico (el runtime lo agranda si hace falta).

Memoria dinámica (*heap*)
: Es el espacio de memoria que se utiliza para la asignación dinámica de memoria. Su tamaño no está determinado al comenzar la ejecución y se va ajustando a medida que el programa solicita más memoria para almacenar datos. No se asigna como un único bloque contiguo, sino que puede fragmentarse.

## Ejecución de programas

Para poder ejecutar un programa se deben seguir los siguientes pasos:

1\. Compilación y almacenamiento.
: Los programas se almacenan inicialmente en la memoria secundaria (por ejemplo, en un disco duro o SSD). En el caso de Go como se trata de un lenguaje compilado, los archivos fuentes se compilan y se genera un archivo ejecutable que se almacena en el disco.

2\. Asignación de memoria central
: Al iniciar la ejecución, el **sistema operativo** carga el programa en la memoria central (RAM). Esto incluye las instrucciones del programa y los datos iniciales necesarios para su ejecución. La memoria asignada al programa se divide en segmentos específicos para el código, los datos, el *stack* y el *heap*. El programa en ejecución se denomina **proceso**.

3\. Ejecución del programa
: El procesador ejecuta una a una las instrucciones del programa desde el **segmento de código**. Cada vez que ejecuta una instrucción, avanza el puntero de instrucción a la siguiente instrucción. Cuando ejecuta una llamada a una función, se crea un nuevo **marco de pila** (*frame*) en el *stack* para almacenar las variables locales y los parámetros de la función. Al terminar la función, el marco de pila se elimina y el valor de retorno se transfiere al marco anterior desde donde se llamó a la función. Si durante la ejecución de una función se solicita memoria dinámica, se asigna en el *heap*. En Go, durante la ejecución del programa, el recolector de basura (*garbage collector*) se encarga de liberar la memoria no utilizada en el heap, evitando así las fugas de memoria (*memory leaks*).

4\. Interacción con el sistema operativo
: El sistema operativo supervisa y gestiona la memoria asignada al programa. Si el programa necesita más memoria, puede solicitarla al sistema operativo, que ajustará el tamaño del *heap* o el *stack* según sea necesario.

5\. Liberación de memoria
: Al finalizar la ejecución, el sistema operativo libera toda la memoria asignada al programa, incluyendo los segmentos de código, datos, pila y heap.

En la figura a continuación, se muestra un esquema de la memoria de un proceso en ejecución. Cada segmento de memoria tiene un tamaño y una función específica en el programa. La figura es solo a modo didáctico y no representa la organización real de la memoria en Go, que es más compleja.

En el diagrama el *stack* se ubica en la parte superior de la memoria y crece hacia abajo; cuando no puede crecer más se produce un error de desbordamiento de pila (*stack overflow*). El *heap* se ubica en la parte inferior de la memoria, sobre los segmentos de código y datos y crece hacia arriba.

```{figure} ../_static/figures/1-presentacion/1-2-memoria/MemoriaSegmentos_light.svg
---
class: only-light-mode
width: 50%
---
Segmentos de Memoria de un Proceso en Ejecución
```

```{figure} ../_static/figures/1-presentacion/1-2-memoria/MemoriaSegmentos_dark.svg
---
class: only-dark-mode
width: 50%
---
Segmentos de Memoria de un Proceso en Ejecución
```

## Gestión de Memoria Dinámica en Go

La gestión de memoria es un aspecto clave en cualquier lenguaje de programación, ya que impacta en el rendimiento, la eficiencia y la estabilidad del software.

En Go, las variables se almacenan en el *stack* o en el *heap* dependiendo de su alcance, duración y cómo se utilizan.

El compilador de Go decide automáticamente si una variable debe almacenarse en el *stack* o en el *heap*. Esto se conoce como *Escape Analysis*. Si una variable **"escapa"** del alcance de la función, se almacena en el *heap* en lugar del *stack*.

```{admonition} Consideraciones de Rendimiento
---
class: note
---
El acceso a las variables que se encuentran en el *stack* es más directo y más rápido, mientras que el acceso a los datos en el *heap* es más lento ya que se deben referenciar desde el *stack*, pero permite estructuras de datos más grandes y persistentes.
```

Veamos un ejemplo, dado el siguiente fragmento de código:

```{code-block} go
---
linenos:
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
var p1 = Persona{"Marcelo", "Díaz", 27, Direccion{"Mariano Acosta",
                  "Gonzalez Catán", "Buenos Aires", 6420}}
func main() {
    p2 := Persona{nombre: "Pepe", edad: 23}
    p3 := &p2
    p4 := Persona{"Juan", "Gonzalez", 34, Direccion{"Valentín Gómez",
                  "Caseros", "Buenos Aires", 742}}

    p3.direccion := Direccion{"Av. Corrientes", "CABA", "Buenos Aires", 1050}
    p3.apellido = "Martinez"
    p4.direccion = Direccion{"Mariano Acosta", "Gonzalez Catán",
                             "Buenos Aires", 6420}
}
```

El **Stack**, el **Heap** y el **Segmento de Datos** presentarán el siguiente estado:

```{figure} ../_static/figures/1-presentacion/1-2-memoria/MapaDeMemoria_light.svg
---
class: only-light-mode
---
Mapa de Memoria
```

```{figure} ../_static/figures/1-presentacion/1-2-memoria/MapaDeMemoria_dark.svg
---
class: only-dark-mode
---
Mapa de Memoria
```

Vamos a analizar cada variable en el código y justificar dónde se almacena:

- **`num`**

  ```{code-block} go
  ---
  linenos:
  ---
  var num int = 5
  ```

  - **Almacenamiento:** **Segmento de Datos**
  - **Justificación:** `num` es una variable global (declarada a nivel de paquete). Al no ser una variable local, no se ubica en el *stack* de ninguna función, sino en el segmento de datos estáticos definido al inicio del proceso.

  ______________________________________________________________________

- **`p1`**

  ```{code-block} go
  ---
  linenos:
  ---
  var p1 = Persona{"Marcelo", "Díaz", 27, Direccion{"Mariano Acosta",
                  "Gonzalez Catán", "Buenos Aires", 6420}}
  ```

  - **Almacenamiento:** **Segmento de Datos** (estructura) y **Heap** (cadenas)
  - **Justificación:** `p1` es una variable global, que se encuentra en el segmento de datos, es de tipo `Persona` y ocupa un espacio de tamaño fijo para almacenar toda la estructura. Sin embargo, los valores de los campos de tipo `string` se almacenan en el *heap*, ya que en Go los *strings* son cabeceras que apuntan a una secuencia de bytes en memoria dinámica, mientras que `edad`, que es del tipo `uint` se almacena también en el **Segmento de Datos**.

______________________________________________________________________

- **`p2`**

  ```{code-block} go
  ---
  linenos:
  ---
  p2 := Persona{nombre: "Pepe", edad: 23}
  ```

  - **Almacenamiento:** **Stack** (estructura) y **Heap** (cadenas)
  - **Justificación:** `p2` es una variable local definida dentro de `main`, por lo que se crea en el marco de pila (*stack frame*) de dicha función. Al igual que con `p1`, el contenido de los campos de tipo `string` ("Pepe") se almacena en el *heap*.

  ______________________________________________________________________

- **`p3`**

  ```{code-block} go
  ---
  linenos:
  ---
  p3 := &p2
  ```

  - **Almacenamiento:** **Stack**
  - **Justificación:** `p3` es un puntero a `p2`, definido como variable local en `main`. Se almacena en el *stack* y apunta a la misma estructura `Persona` que `p2`. A través de `p3` se modifican `p2.apellido` a `"Martinez"` y `p2.direccion` a `Direccion{"Av. Corrientes", "CABA", "Buenos Aires", 1050}`.

  ______________________________________________________________________

- **`p4`**

  ```{code-block} go
  ---
  linenos:
  ---
  p4 := Persona{"Juan", "Gonzalez", 34, Direccion{"Valentín Gómez",
                "Caseros", "Buenos Aires", 742}}
  ```

  - **Almacenamiento:** **Stack** (estructura) y **Heap** (cadenas)
  - **Justificación:** `p4` es una variable local de tipo `Persona` que se almacena en el *stack*. Los valores de tipo `string` (`"Juan"`, `"Gonzalez"`, etc.) se almacenan en el *heap*. Posteriormente, se reasigna su campo `direccion` con `Direccion{"Mariano Acosta", "Gonzalez Catán", "Buenos Aires", 6420}`.

  ______________________________________________________________________

**Resumen general:**

| Variable | Ubicación                                 | Justificación                                    |
| -------- | ----------------------------------------- | ------------------------------------------------ |
| `num`    | Segmento de Datos                         | Variable global simple.                          |
| `p1`     | Segmento de Datos (header) / *Heap* (str) | Estructura global, contenido de cadenas en heap. |
| `p2`     | *Stack* (estructura) / *Heap* (cadenas)   | Variable local, contenido de cadenas en heap.    |
| `p3`     | *Stack*                                   | Puntero local a `p2`.                            |
| `p4`     | *Stack* (estructura) / *Heap* (cadenas)   | Variable local, contenido de cadenas en heap.    |

En Go, el **compilador y el recolector de basura (GC)** optimizan el uso del *stack* y el *heap*. Las estructuras simples y de corta duración suelen estar en el stack, mientras que los datos más complejos o de mayor duración (como cadenas) se almacenan en el heap.

Go utiliza un **recolector de basura concurrente** para liberar memoria automáticamente. Es concurrente porque la mayor parte del trabajo de limpieza ocurre en paralelo con la ejecución del programa. Esto permite que el programador no tenga que liberar la memoria manualmente, evitando errores comunes como el acceso a memoria inválida.

Cuando existen datos en la memoria dinámica que ya no son accesibles (no están referenciados desde la pila ni el segmento de datos), el GC los marca para su eliminación y eventual liberación.

Para coordinar ciertos pasos del proceso de limpieza, el GC realiza pausas extremadamente breves denominadas *stop-the-world* (generalmente menores a un milisegundo). Go se destaca por optimizar estas pausas para que no interfieran con el rendimiento percibido del sistema:

- Minimiza las pausas para optimizar la latencia.
- Usa múltiples núcleos de CPU para ejecutar la recolección en paralelo.
- La mayor parte del marcado de objetos ocurre mientras el programa sigue corriendo.
- Detecta y elimina referencias a objetos no utilizados de forma eficiente.

```{admonition} Importante
---
class: important
---
Un GC concurrente mejora el rendimiento y la experiencia del usuario, ya que evita grandes pausas en la ejecución del programa. Esto es fundamental en servidores y sistemas en tiempo real, donde una pausa larga podría afectar la respuesta del sistema.
```

## Ejercicios

Los ejercicios de este capítulo están en `02-memoria/ejercicios/`
del repositorio taller-go.
