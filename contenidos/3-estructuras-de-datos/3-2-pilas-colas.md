---
label: pilas-colas
---

# Pilas y Colas

Los primeros TAD que vamos a estudiar son **Pilas** y **Colas**.

Pilas y Colas son estructuras de datos **dinámicas** que mantienen el orden de los elementos y donde los elementos que se agregan y remueven tienen una ubicación específica.

```{admonition} TAD dinámico
---
class: important
---
Un TAD dinámico es un TAD que puede modificar su tamaño, es decir, el espacio en memoria que ocupa, en función de la cantidad de datos que almacena.
```

## Pila

Es una estructura del tipo **LIFO** (_Last In First Out_) es decir el último elemento que ingresó en la pila será el primer elemento en salir. Por ejemplo, en una pila de libros, si queremos agregar un nuevo libro debemos colocarlo encima de la pila, sobre el último libro. A su vez el último libro de la pila es el único al que le podemos ver su portada y sacar de la pila. Por lo tanto para sacar el libro de abajo de la pila, primero hay que sacar uno por uno todos los libros que están apilados sobre él.

```{figure} ../_static/figures/3-estructuras-de-datos/3-2-pilas-colas/book-stack_light.svg
---
class: only-light-mode
---
Pila de Libros
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-2-pilas-colas/book-stack_dark.svg
---
class: only-dark-mode
---
Pila de Libros
```

A partir de la descripción del comportamiento de la pila de libros, podemos intuir el comportamiento de la estructura Pila o Stack:

`Push`
: Permite insertar un elemento en la pila (siempre en el tope de la misma)

`Pop`
: Permite extraer un elemento de la pila (siempre el que está en el tope). Si se intenta hacer un Pop de una pila vacía se debe indicar un error

`Top`
: Permite ver el último elemento que ingresó en la pila, sin sacarlo. Si se intenta hacer un Top de una pila vacía se debe indicar un error

`IsEmpty`
: Verifica si la pila está vacía. Devuelve `true` si la pila está vacía o `false` en caso contrario

Todas las operaciones deben ser $O(1)$. Es decir de tiempo constante, independiente del tamaño de la entrada.

Este comportamiento define la **interfaz** del tipo Pila, es decir las operaciones válidas que se pueden realizar sobre la misma. En código:

```{code-block} go
---
linenos: true
---
type Stack[T any] interface {
    Push(val T)
    Pop() (T, error)
    Top() (T, error)
    IsEmpty() bool
}
```

El parámetro de tipo `[T any]` hace que la interfaz sea **genérica**: al crear una pila concreta se elige un tipo fijo (`Stack[int]`, `Stack[string]`, etc.) y esa pila solo aceptará elementos de ese tipo. No se pueden mezclar tipos distintos en una misma pila, como sí se podía con el tipo `any` sin parámetro.

````{admonition} Encapsulamiento
---
class: important
---
Es fundamental ocultar la implementación para que no se pueda manipular el contenedor de datos con operaciones no permitidas. Por ejemplo, la definición:

```{code-block} go
// Forma incorrecta de definir una pila,
// porque no encapsula el contenedor de datos
type Stack[T any] []T
```

deja expuesto el contenedor de datos y se podría manipular con operaciones propias de slices.

```{code-block} go
var p Stack[int]
p = append(p, 1)
p = append(p, 2)
p[0] = 99
```

En este fragmento se agregan elementos a la pila usando la función `append` de Go y luego se modifica un elemento arbitrariamente.
````

El siguiente seudocódigo muestra una implementación del TAD Pila sobre un arreglo dinámico. El contenedor de datos `data` está encapsulado dentro del struct y su tipo depende del parámetro genérico `T`. Las operaciones `Push`, `Pop` y `Top` trabajan siempre sobre el extremo del arreglo, garantizando costo $O(1)$.

```{code-block} text
---
linenos: true
---
TIPO Stack[T] struct
    data ← ARREGLO de T
FIN TIPO

FUNCION NewStack[T]() → *Stack[T]
    RETORNAR &Stack[T]{}
FIN FUNCION

FUNCION (s *Stack[T]) IsEmpty() → bool
    RETORNAR LONGITUD(s.data) = 0
FIN FUNCION

FUNCION (s *Stack[T]) Push(x T)
    s.data ← AGREGAR_AL_FINAL(s.data, x)
FIN FUNCION

FUNCION (s *Stack[T]) Pop() → (T, error)
    SI s.IsEmpty() ENTONCES
        RETORNAR valorCero, error("pila vacía")
    FIN SI
    x ← s.data[LONGITUD(s.data) - 1]
    s.data ← s.data[0 : LONGITUD(s.data) - 1]
    RETORNAR x, nil
FIN FUNCION

FUNCION (s *Stack[T]) Top() → (T, error)
    SI s.IsEmpty() ENTONCES
        RETORNAR valorCero, error("pila vacía")
    FIN SI
    RETORNAR s.data[LONGITUD(s.data) - 1], nil
FIN FUNCION
```

`NewStack`
: Crea una pila vacía. Reserva espacio en memoria para almacenar la pila y devuelve la dirección de memoria correspondiente.

`IsEmpty`
: Verifica si la cantidad de elementos del contenedor de datos es igual a 0.

`Push`
: Agrega el elemento recibido al final del arreglo.

`Pop`
: Si la pila está vacía devuelve el valor cero de `T` y un error. Caso contrario devuelve el elemento del tope y lo elimina de la pila, reduciendo el arreglo en una posición.

`Top`
: Similar a `Pop` pero no elimina el tope. Si la pila está vacía devuelve error.

A continuación un ejemplo de uso con `Stack[int]`:

```{code-block} go
---
linenos: true
---
import "fmt"

func main() {
    // Crear una pila de enteros
    s := NewStack[int]()

    // Agregar elementos
    s.Push(10)
    s.Push(20)
    s.Push(30)

    // Consultar el tope sin extraerlo
    top, _ := s.Top()
    fmt.Println("Tope:", top)

    // Extraer todos los elementos
    for !s.IsEmpty() {
        val, _ := s.Pop()
        fmt.Println(val)
    }
}
```

Y el mismo `Stack[T]` puede usarse con `string`:

```{code-block} go
---
linenos: true
---
func main() {
    pila := NewStack[string]()
    pila.Push("uno")
    pila.Push("dos")
    pila.Push("tres")

    for !pila.IsEmpty() {
        val, _ := pila.Pop()
        fmt.Println(val)
    }
}
```

## Cola

Es una estructura del tipo **FIFO (First In First Out)** es decir el primer elemento en ingresar en la cola es el primero en salir. Un ejemplo clásico del uso de esta estructura es para modelar una cola de personas, por ejemplo en la caja de un supermercado. La última persona que llega se coloca al final de la cola y espera su turno para ser atendida.

```{figure} ../_static/figures/3-estructuras-de-datos/3-2-pilas-colas/people-queue_light.svg
---
class: only-light-mode
width: 80%
---
Cola de Espera
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-2-pilas-colas/people-queue_dark.svg
---
class: only-dark-mode
width: 80%
---
Cola de Espera
```

El comportamiento de la cola queda definido por las siguientes operaciones:

`Enqueue`
: Permite insertar un elemento en la cola (siempre en la última posición)

`Dequeue`
: Permite extraer un elemento de la cola (siempre el primero). Si se intenta hacer un Dequeue de una cola vacía se debe indicar un error

`Front`
: Permite ver el primer elemento de la cola sin extraerlo. Si se intenta hacer un Front de una cola vacía se debe indicar un error

`IsEmpty`
: Verifica si la Cola está vacía. Devuelve `true` si la cola está vacía o `false` en caso contrario

Todas las operaciones deben ser $O(1)$.

Su interfaz en código es:

```{code-block} go
---
linenos: true
---
type Queue[T any] interface {
    Enqueue(val T)
    Dequeue() (T, error)
    Front() (T, error)
    IsEmpty() bool
}
```

El siguiente seudocódigo muestra una implementación sobre un arreglo dinámico:

```{code-block} text
---
linenos: true
---
TIPO Queue[T] struct
    data ← ARREGLO de T
FIN TIPO

FUNCION NewQueue[T]() → *Queue[T]
    RETORNAR &Queue[T]{}
FIN FUNCION

FUNCION (q *Queue[T]) Enqueue(x T)
    q.data ← AGREGAR_AL_FINAL(q.data, x)
FIN FUNCION

FUNCION (q *Queue[T]) Dequeue() → (T, error)
    SI q.IsEmpty() ENTONCES
        RETORNAR valorCero, error("cola vacía")
    FIN SI
    x ← q.data[0]
    q.data ← q.data[1 : LONGITUD(q.data)]
    RETORNAR x, nil
FIN FUNCION

FUNCION (q *Queue[T]) Front() → (T, error)
    SI q.IsEmpty() ENTONCES
        RETORNAR valorCero, error("cola vacía")
    FIN SI
    RETORNAR q.data[0], nil
FIN FUNCION

FUNCION (q *Queue[T]) IsEmpty() → bool
    RETORNAR LONGITUD(q.data) = 0
FIN FUNCION
```

Nótese que `Dequeue` remueve el primer elemento del *slice*, lo cual en Go implica desplazar todos los elementos restantes una posición hacia la izquierda. Esto hace que `Dequeue` sea $O(n)$, no $O(1)$. Más adelante veremos cómo implementar una cola con $O(1)$ en todas sus operaciones.

Ejemplo de uso:

```{code-block} go
---
linenos: true
---
func main() {
    cola := NewQueue[string]()

    cola.Enqueue("primero")
    cola.Enqueue("segundo")
    cola.Enqueue("tercero")

    front, _ := cola.Front()
    fmt.Println(front)  // primero

    for !cola.IsEmpty() {
        val, _ := cola.Dequeue()
        fmt.Println(val)
    }
}
```

## Ejercicios

Los ejercicios de este capítulo están en `02-pilas-colas/ejercicios/` del
repositorio taller-tad.

Antes de resolverlos hay que tener implementados `SliceStack[T]` y `SliceQueue[T]`
en data-structures,
que está dentro del repositorio `taller-tad` y contiene las interfaces y los esqueletos.
Ambas tareas se trabajan en paralelo: primero completás las implementaciones en
`data-structures` y después las usás acá.
