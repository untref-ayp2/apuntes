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
: Constituida por memoria volátil, más rápida y costosa que otros medios de almacenamiento. Es la memoria de trabajo del procesador, la RAM (_Random Access Memory_) de acceso rápido, donde se almacenan los programas en ejecución y los datos. La información que almacena la RAM se pierde al interrumpirse el suministro de corriente eléctrica.

Memoria secundaria
: Conformada por el conjunto de memorias no volátiles. Es la memoria de persistencia de información. Ejemplos: discos rígidos, discos ópticos, memorias USB, etc. Conserva la información almacenada al interrumpirse el suministro de corriente eléctrica. Es más lenta y barata que la RAM.

## Organización de la Memoria central o primaria

Tanto los programas como el resto de información que guarda la computadora están almacenados en la **memoria secundaria**.

Al lanzar la ejecución de un programa, las instrucciones y los datos iniciales se copian a la **memoria primaria**. Un programa en ejecución se denomina **proceso**.

En tiempo de ejecución, un proceso está asociado a una porción de la memoria primaria que se divide lógicamente en 4 segmentos:

Segmento de Código (_code segment_)
: Es la porción donde se localizarán las instrucciones que componen nuestro programa. Su tamaño se determina al comenzar la ejecución. Asociado a este segmento se encuentra un **puntero** que indica la próxima instrucción a ejecutar.

Segmento de Datos (_data segment_)
: Almacena las variables globales y estáticas. Su tamaño también queda determinado al comenzar la ejecución.

Pila (_stack segment_)
: Almacenará el contenido de las variables locales en cada invocación de una función. Su tamaño se determina al comenzar la ejecución del programa. Cada entrada en el stack constituye el contexto de un método en ejecución y contiene variables locales, parámetros y valores de retorno. Se va asignando en bloques de memoria contigua.

Memoria dinámica (_heap_)
: Es el espacio de memoria que se utiliza para la asignación dinámica de memoria. Su tamaño no está determinado al comenzar la ejecución y se va ajustando a medida que el programa solicita más memoria para almacenar datos. No es asignada en bloques de memoria contigua.

## Ejecución de programas

Para poder ejecutar un programa se deben seguir los siguientes pasos:

1\. Compilación y almacenamiento
: Los programas se almacenan inicialmente en la memoria secundaria (por ejemplo, en un disco duro o SSD). En el caso de Go como se trata de un lenguaje compilado, los archivos fuentes se compilan y se genera un archivo ejecutable que se almacena en el disco.

2\. Asignación de memoria central
: Al iniciar la ejecución, el **sistema operativo** carga el programa en la memoria central (RAM). Esto incluye las instrucciones del programa y los datos iniciales necesarios para su ejecución. La memoria asignada al programa se divide en segmentos específicos para el código, los datos, el _stack_ y el _heap_. El programa en ejecución se denomina **proceso**.

3\. Ejecución del programa
: El procesador ejecuta una a una las instrucciones del programa desde el **segmento de código**. Cada vez que ejecuta una instrucción avanza el puntero de instrucción al siguiente. Cuando ejecuta una llamada a una función, se crea un nuevo marco (_frame_) de pila en el _**stack**_ para almacenar las variables locales y los parámetros de la función. Eventualmente cuando la función termina, el marco de pila se elimina y el valor de retorno se transfiere al marco de pila anterior desde donde se llamó a la función. Si durante la ejecución de una función se solicita memoria dinámica, se asigna en el _**heap**_. En Go, durante la ejecución del programa, el recolector de basura (_garbage collector_) se encarga de liberar la memoria no utilizada, para evitar que se produzcan fugas de memoria.

4\. Interacción con el sistema operativo
: El sistema operativo supervisa y gestiona la memoria asignada al programa. Si el programa necesita más memoria, puede solicitarla al sistema operativo, que ajustará el tamaño del _**heap**_ o el _**stack**_ según sea necesario.

5\. Liberación de memoria
: Al finalizar la ejecución, el sistema operativo libera toda la memoria asignada al programa, incluyendo los segmentos de código, datos, pila y heap.

En la figura {ref}`esquema-memoria` se muestra un esquema de la memoria de un proceso en ejecución. Cada segmento de memoria tiene un tamaño y una función específica en el programa. La figura es solo a modo didáctico y no representa la organización real de la memoria en Go, que es más compleja.

En el diagrama el _**stack**_ se ubica en la parte superior de la memoria y crece hacia abajo, cuando no puede crecer más se produce un error de desbordamiento de pila (_stack overflow_). El _**heap**_ se ubica en la parte inferior de la memoria, sobre los segmentos de código y datos y crece hacia arriba.

```{figure} ../assets/images/MemoriaSegmentos.svg
---
width: 500px
name: esquema-memoria
---
Segmentos de Memoria de un Proceso en Ejecución
```

## Gestión de Memoria Dinámica en Go

La gestión de memoria es un aspecto clave en cualquier lenguaje de programación, ya que impacta en el rendimiento, la eficiencia y la estabilidad del software.

En Go, las variables se almacenan en el _**stack**_ o en el _**heap**_ dependiendo de su alcance, duración y cómo se utilizan.

_Escape analysis_ (Análisis de Escape)
: El compilador de Go decide automáticamente si una variable debe almacenarse en el _**stack**_ o en el _**heap**_. Esto se conoce como _**Escape Analysis**_. Si una variable **"escapa"** del alcance de la función, se almacena en el _**heap**_ en lugar del _**stack**_.

Consideraciones de Rendimiento
: El acceso a las variables que se encuentran en el _**stack**_ es más directo y más rápido, mientras que el acceso a los datos en el _**heap**_ es más lento ya que se deben referenciar desde el _**stack**_, pero permite estructuras de datos más grandes y persistentes.

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

El **Stack** y el **Heap** presentaran el siguiente estado:

```{figure} ../assets/images/MapaDeMemoria.dio.svg
---
name: mapa-memoria-Santi
---
Mapa de Memoria
```

Vamos a analizar cada variable en el código y justificar dónde se almacena:

- **`num`**

  ```go
  var num int = 5
  ```

  - **Almacenamiento:** **Stack**
  - **Justificación:** `num` es una variable global, pero en Go, las variables simples como enteros suelen almacenarse en el _**stack**_ si no se necesita que persistan más allá del alcance de la función principal. Sin embargo, si el compilador detecta que se necesita más tiempo de vida, podría moverla al _**heap**_. En este caso, es probable que esté en el _**stack**_.

  ______________________________________________________________________

- **`p1`**

  ```go
  var p1 Persona
  p1.nombre = "Marcelo"
  p1.edad = 27
  ```

  - **Almacenamiento:** **Stack**
  - **Justificación:** `p1` es una variable de tipo `Persona` declarada como global. Su almacenamiento inicial será en el _**stack**_, donde solo tendremos una referencia para acceder a los datos que almacenará la estructura en el _**heap**_ . Los valores de los campos como `nombre` (`"Marcelo"`) se almacenan en el _**heap**_.

______________________________________________________________________

- **`p2`**

  ```go
  p2 := Persona{nombre: "Pepe", edad: 23}
  ```

  - **Almacenamiento:** **Stack**
  - **Justificación:** `p2` es una variable local inicializada en el _**stack**_. Sin embargo, el valor del campo `nombre` ("Pepe") se almacena en el _**heap**_, ya que las cadenas en Go son referencias.

  ______________________________________________________________________

- **`p3`**

  ```go
  p3 := Persona{"Juan", "Gonzalez", 34, Direccion{"Valentín Gomez",
                "Caseros", "Buenos Aires", 742}}
  ```

  - **Almacenamiento:** **Stack** (estructura) y **Heap** (cadenas)
  - **Justificación:** La variable `p3` se almacena en el _**stack**_ porque es una variable local. Sin embargo, los valores de tipo `string` como `"Juan"`, `"Gonzalez"`, `"Valentín Gomez"`, etc., se almacenan en el _**heap**_, ya que las cadenas en Go son referencias a datos en memoria dinámica.

  ______________________________________________________________________

- **`p4`**

  ```go
  p4 := &p2
  ```

  - **Almacenamiento:** **Stack**
  - **Justificación:** `p4` es una copia de la dirección de memoria de `p2`. Dicho de otro modo es una copia de la referencia de `p2`. Se almacena en el _**stack**_. `p4` y `p2` apuntan a la misma ubicación en el _**heap**_.

  ______________________________________________________________________

- **`dir`**

  ```go
  dir := Direccion{"Av. Corrientes", "CABA", "Buenos Aires", 1050}
  ```

  - **Almacenamiento:** **Stack** (estructura) y **Heap** (cadenas)
  - **Justificación:** La variable `dir` se almacena en el _**stack**_ porque es una variable local. Sin embargo, los valores de tipo `string` como `"Av. Corrientes"`, `"CABA"`, etc., se almacenan en el _**heap**_.

  ______________________________________________________________________

**Resumen general:**

| Variable | Stack / Heap                        | Justificación                                 |
| -------- | ----------------------------------- | --------------------------------------------- |
| `num`    | Stack                               | Variable global simple.                       |
| `p1`     | Stack (estructura) / Heap (cadenas) | Estructura en stack, cadenas en heap.         |
| `p2`     | Stack (estructura) / Heap (cadenas) | Igual que `p1`.                               |
| `p3`     | Stack (estructura) / Heap (cadenas) | Igual que `p1`.                               |
| `p4`     | Stack                               | Copia de `p2`, referencias a cadenas en heap. |
| `dir`    | Stack (estructura) / Heap (cadenas) | Igual que `p1`.                               |

En Go, el **compilador y el recolector de basura (GC)** optimizan el uso del stack y el heap. Las estructuras simples y de corta duración suelen estar en el stack, mientras que los datos más complejos o de mayor duración (como cadenas) se almacenan en el heap.

## Garbage Collector (GC) en Go

Go utiliza un **GC concurrente** para liberar memoria automáticamente. Es concurrente porque se ejecuta en paralelo y de forma transparente a los procesos de usuario. Esto es una gran ventaja para el programador que no se debe ocupar de liberar la memoria para evitar que su programa se quede sin espacio para los datos.

Cuando hay datos en la memoria dinámica que ya no se utilizan, es decir que no están referenciados desde la pila o el segmento de datos, entonces el GC los elimina.

Para poder ejecutar el GC, se debe detener completamente la ejecución del programa, lo que se denomina _**stop-the-world**_ , lo que puede ocasionar retrasos en la ejecución entre otros inconvenientes. Go tiene algunas características optimizadas para lidiar con la recolección de basura:

- Minimiza las pausas para mejorar el rendimiento.
- Usa múltiples núcleos de CPU para ejecutar la recolección en paralelo.
- Detecta y elimina referencias a objetos no utilizados.
- Go minimiza los _**stop-the-world**_.
- La mayoría del trabajo del GC ocurre en paralelo con la ejecución del código, evitando así los _**stop the world**_.

```{important}
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

En el gráfico, identificar claramente qué variables están en el _**Stack**_ y cuáles están en el _**Heap**_, así como las referencias entre ellas.
