---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Gestión de memoria

```{code-cell} go
:tags: [remove-cell]
import f "fmt"

type FmtWrapper struct{}

func (fw FmtWrapper) Println(a ...interface{}) {
    _, _ = f.Println(a...)
}

var fmt FmtWrapper = FmtWrapper{}
```

En general la memoria de una computadora se puede clasificar en:

Memoria central o primaria
: Constituida por memoria volátil. Es la memoria de trabajo del procesador, la RAM de acceso rápido, donde se almacenan los programas en ejecución y los datos.

Memoria secundaria
: Conformada por el conjunto de memorias no volátiles. Es la memoria de persistencia de información. Ejemplos: discos rígidos, discos ópticos, memorias USB, etc.

## Organización de la memoria

En tiempo de ejecución, un proceso está asociado a una porción de la memoria central que se divide lógicamente en 4 segmentos:

Segmento de Código (_code segment_)
: Es la porción donde se localizarán las instrucciones que componen nuestro programa. Su tamaño se determina al comenzar la ejecución. Asociado a este segmento se encuentra un puntero que indica la próxima instrucción a ejecutar.

Segmento de Datos (_data segment_)
: Almacena las variables globales y estáticas. Su tamaño también queda determinado al comenzar la ejecución.

Pila (_stack_)
: Almacenará el contenido de las variables locales en cada invocación de una función. Su tamaño se determina al comenzar la ejecución del programa. Cada entrada en el stack constituye el contexto de un método en ejecución y contiene variables locales, parámetros y valores de retorno.

Memoria dinámica (_heap_)
: Es el espacio de memoria que se utiliza para la asignación dinámica de memoria. Su tamaño no está determinado al comenzar la ejecución y se va ajustando a medida que el programa solicita más memoria para almacenar datos.

## Ejecución de programas

Cuando se ejecuta un programa, la memoria se organiza y utiliza de la siguiente manera:

1- Compilación y almacenamiento
: Los programas se almacenan inicialmente en la memoria secundaria (por ejemplo, en un disco duro o SSD). En el caso de GO como se trata de un lenguaje compilado, los arhcivos fuentes se compilan y se genera un archivo ejecutable que se almacena en el disco.

2- Asignación de memoria central
: Al iniciar la ejecución, el sistema operativo carga el programa en la memoria central (RAM). Esto incluye las instrucciones del programa y los datos iniciales necesarios para su ejecución. La memoria asignada al programa se divide en segmentos específicos para el código, los datos, la pila y el heap. El programa en ejecución se denomina **proceso**.

3- Ejecución del programa
: El procesador ejecuta una a una las instrucciones del programa desde el **Segmento de Código**. Cada vez que ejecuta una instrucción avanza el puntero de instrucción al siguiente. Cuando ejecuta una llamada a una función, se crea un nuevo marco (_frame_) de pila en el **Stack** para almacenar las variables locales y los parámetros de la función. Eventualmente cuando la función termina, el marco de pila se elimina y el valor de retorno se transfiere al marco de pila anterior desde donde se llamó a la función. Si durante la ejecución de una función se solicita memoria dinámica, se asigna en el **Heap**. En GO, durante la ejecución del programa, el recolector de basura (_garbage collector_) se encarga de liberar la memoria no utilizada, para evitar que se produzcan fugas de memoria.

4- Interacción con el sistema operativo
: El sistema operativo supervisa y gestiona la memoria asignada al programa. Si el programa necesita más memoria, puede solicitarla al sistema operativo, que ajustará el tamaño del **Heap** o la **Pila** según sea necesario.

5- Liberación de memoria
: Al finalizar la ejecución, el sistema operativo libera toda la memoria asignada al programa, incluyendo los segmentos de código, datos, pila y heap.

En la siguiente imagen se muestra un esquema de la memoria de un proceso en ejecución. Cada segmento de memoria tiene un tamaño y una función específica en el programa. La figura es solo a modo didáctico para comprender y no representa la organización real de la memoria en GO, que es más compleja.

En el diagrama la pila se ubica en la parte superior de la memoria y crece hacia abajo, cuando no puede crecer más se produce un error de desbordamiento de pila (_stack overflow_). La memoria dinámica se ubica en la parte inferior de la memoria, sobre los segmentos de código y datos y crece hacia arriba.


```{figure} ../assets/images/MemoriaSegmentos.svg
---
width: 500px
name: esquema-memoria
---
Segmentos de Memoria de un Proceso en Ejecución
```

## Gestión de Memoria Dinámica en GO
La gestión de memoria es un aspecto clave en cualquier lenguaje de programación, ya que impacta en el rendimiento, la eficiencia y la estabilidad del software. 

Algunos lenguajes como C requieren una administración manual de la memoria, mientras que otros como Java y Python utilizan un **Recolector de Basura** o _**Garbage Collector (GC)**_ para automatizar la liberación de memoria.

GO combina lo mejor de ambos mundos, un **GC concurrente y eficiente**, con pausas reducidas y un modelo de asignación de memoria optimizado con **Stack, Heap y Escape Analysis**.

A continuación un ejemplo para observar donde se encuentran los identificadores y los valores de las variables en la memoria.

```{code-block} go
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
p1.nombre = "Marcelo"
p1.edad = 27

p2 := Persona{nombre: "Pepe", edad: 23}
p3 := Persona{"Juan", "Gonzalez", 34, Direccion{"Valentín Gomez",
              "Caseros", "Buenos Aires", 742}}
p4 := p2

dir:= Direccion{"Av. Corrientes", "CABA", "Buenos Aires", 1050}

p4.apellido = "Martinez"
p4.apellido = "Martinez"
p4.direccion = dir
```

```{figure} ../assets/images/mapaDeMemoria.svg
---
name: mapa-memoria
---
Mapa de Memoria
```

### Asignación de Memoria Dinámica: ```new()``` vs ```make()```

GO proporciona dos formas principales de asignar memoria:

```new()```
: Reserva memoria pero no la inicializa. Devuelve un puntero al tipo de dato especificado.

```{code-cell} go
import "fmt"
p := new(int)     // p es un puntero a un entero, inicialmente vale 0

fmt.Println(*p)   //valor guardado en la direccion de memoria de a la que apunta p
fmt.Println(p)    //direccion de memoria a la que apunta p
*p = 42          //asigna 42 al valor de la direccion de memoria a la que apunta p    
fmt.Println(*p)
fmt.Println(p)
```

```make()```
: Se usa para inicializar **slices, maps y channels**. Asigna y prepara estructuras para su uso.

```{code-cell} go
import "fmt"
s := make([]int, 5) // Slice con capacidad y longitud 5
print(s)
```

Diferencia clave: `new()` solo asigna memoria, `make()` inicializa estructuras internas.

## Garbage Collector (GC) en GO

GO utiliza un **GC concurrente** para liberar memoria automáticamente.

Cuando se dice que el Garbage Collector (GC) de GO es concurrente, significa que puede ejecutar la recolección de basura mientras el programa sigue en ejecución.

Algunas características clave:

- Minimiza las pausas para mejorar el rendimiento.
- Usa múltiples núcleos de CPU para ejecutar la recolección en paralelo.
- Detecta y elimina referencias a objetos no utilizados.

## ¿Cómo logra esto el GC de GO?

### 1. Algoritmo Tricolor Mark-Sweep

 * Divide los objetos en:
   * **blancos** (no alcanzados, serán eliminados)
   * **grises** (en proceso de análisis)
   * **negros** (alcanzados y ya analizados)
 * Marca y rastrea los objetos accesibles sin detener completamente la ejecución del programa.

### Pausas muy cortas (low-pause GC)

 * GO minimiza los "stop-the-world" (momentos en los que detiene completamente la ejecución para limpiar memoria).
 * La mayoría del trabajo del GC ocurre en paralelo con la ejecución del código.

### Ejecución en múltiples hilos

- El GC usa múltiples núcleos de la CPU para hacer la recolección de basura sin bloquear las goroutines activas.

### Beneficio principal

Un GC concurrente mejora el rendimiento y la experiencia del usuario, ya que evita grandes pausas en la ejecución del programa. Esto es fundamental en servidores y sistemas en tiempo real, donde una pausa larga podría afectar la respuesta del sistema.

## Escape Analysis: Stack vs. Heap

El compilador de GO decide automáticamente si una variable debe almacenarse en el **Stack** o en el **Heap**. Esto se conoce como **Escape Analysis**.

Si una variable "escapa" del alcance de la función, se almacena en el Heap en lugar del Stack.
Si una variable "escapa" del alcance de la función, se almacena en el Heap en lugar del Stack.

**Ejemplo:**
```{code-cell} go
func stack() {
    x := 10 // Se asigna en el Stack
}

func heap() *int {
    p := new(int) // Se asigna en el Heap porque se devuelve un puntero
    return p      //retorna el puntero
}

```

## Optimización de Memoria en GO

Algunas estrategias para mejorar el uso de memoria:

- Preasignar capacidad en slices con `make()`.
- Evitar fugas de memoria eliminando referencias innecesarias.
- Minimizar uso de punteros si no son necesarios.

:::{prf:example} Optimización: preasignación en slices

**Mala práctica**: crecimiento descontrolado de slices

```{code-cell} go
var data []int
for i := 0; i < 1000000; i++ {
    data = append(data, i) // Reasignaciones y consumo extra de memoria
}
```

**Buena práctica**: prealocar capacidad

```{code-cell} go
data := make([]int, 1000000) // Mejor que ir agregando con append
for i := 0; i < 1000000; i++ {
    data[i] = i
}
```

:::

Esta optimización reduce el número de **realocaciones de memoria**, mejorando el rendimiento.

## Conclusión

* GO proporciona un modelo de memoria eficiente con Stack, Heap y Escape Analysis.

* Su GC concurrente optimiza la recolección de basura con el algoritmo Tricolor Mark-Sweep.

* Prestar atención al uso de memoria puede mejorar el rendimiento de los programas en GO.


