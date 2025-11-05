---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Pilas y Colas

Los primeros TAD que vamos a estudiar son **Pilas** y **Colas**.

Pilas y Colas son estructuras de datos **dinámicas** que mantienen el orden de los elementos y donde los elementos que se agregan y remueven tienen una ubicación específica.

```{important}
Un TAD dinámico es un TAD que puede modificar su tamaño, es decir, el espacio en memoria que ocupa, en función de la cantidad de datos que almacena.
```

## Pila

Es una estructura del tipo **LIFO** (_Last In First Out_) es decir el último elemento que ingresó en la pila será el primer elemento en salir. Por ejemplo, en una {ref}`pila-libros` si queremos agregar un nuevo libro debemos colocarlo encima de la pila, sobre el último libro. A su vez el último libro de la pila es el único al que le podemos ver su portada y sacar de la pila. Por lo tanto para sacar el libro de abajo de la pila, primero hay que sacar uno por uno todos los libros que están apilados sobre él.

```{figure} ../assets/images/book-stack.svg
---
width: 300px
name: pila-libros
---
Pila de Libros
```

A partir de la descripción del comportamiento de la pila de libros, podemos intuir el comportamiento de la estructura Pila o Stack:

`Push`{l=go}
: Permite insertar un elemento en la pila (siempre en el tope de la misma)

`Pop`{l=go}
: Permite extraer un elemento de la pila (siempre el que está en el tope). Si se intenta hacer un Pop de una pila vacía se debe indicar un error

`Top`{l=go}
: Permite ver el último elemento que ingresó en la pila, sin sacarlo. Si se intenta hacer un Top de una pila vacía se debe indicar un error

`IsEmpty`{l=go}
: Verifica si la pila está vacía. Devuelve `true`{l=go} si la pila está vacía o `false`{l=go} en caso contrario

Todas las operaciones deben ser $O(1)$. Es decir de tiempo constante, independiente del tamaño de la entrada

Este comportamiento define la **interfaz** del tipo Pila, es decir las operaciones válidas que se pueden realizar sobre la misma. Falta definir la implementación, es decir la estructura de datos interna que utilizaremos para almacenar nuestros datos. A continuación se muestra una implementación de una pila sobre slices de Go, es decir sobre arreglos dinámicos capaces de aumentar su tamaño a medida que se necesita almacenar más elementos.

En la definición de la pila no hay ninguna restricción sobre el tipo de elementos que se almacenan, por ejemplo podríamos apilar, libros, revistas, cajas, en una única pila. El tamaño de la pila debe ser un entero entre 0 y N (invariante de representación)

Para poder tener una pila genérica, es decir, donde no hay restricciones sobre el tipo de datos que se almacena se puede usar el tipo de datos `Any`{l=go}.

````{important}
Como ya se mencionó es fundamental ocultar la implementación para que no se pueda manipular el contenedor de datos con operaciones no permitidas. por ejemplo, la definición:

```go
// Forma incorrecta de definir un pila,
// porque no encapsula el contenedor de datos
type Stack []any
```

deja expuesto el contenedor de datos y se podría manipular con operaciones propias de slices.

```go
p := Stack
p = append(p, "hola")
p = append(p, 2)
p[0] = "chau"
```

En este fragmento se agregan elementos a la pila, usando la función `append`{l=go} de Go y luego se modifica el primer elemento de la pila
````

A continuación se define el TAD Stack, que internamente estará implementado sobre un arreglo dinámico o slice de Go.

```go
import "errors"

type Stack struct {
    data []any
}
```

El contenedor de datos `data`{l=go} está encapsulado dentro del `struct`{l=go}.

```go
func NewStack() *Stack {
    var pila Stack
    return &pila
}
```

`NewStack`{l=go} es una especie de constructor, que nos devuelve una pila vacía cada vez que se llama. Reserva espacio en memoria para almacenar la pila y devuelve la dirección de memoria correspondiente.

```go
func (s *Stack) IsEmpty() bool {
    return len(s.data) == 0
}
```

`IsEmpty`{l=go} chequea si la cantidad de elementos del contenedor de datos es igual a 0

```go
func (s *Stack) Push(x any) {
    s.data = append(s.data, x)
}
```

`Push`{l=go} agrega siempre al final del arreglo el elemento que recibe

```go
func (s *Stack) Pop() (any, error) {
    var x any
    if s.IsEmpty() {
        return x, errors.New("pila vacía")
    }
    x = s.data[len(s.data)-1]
    s.data = s.data[:len(s.data)-1]

    return x, nil
}
```

`Pop`{l=go} chequea si la pila está vacía, en ese caso devuelve el par `(nil, error)`{l=go}. Caso contrario devuelve el par `(x, nil)`{l=go} y elimina el tope de la pila. Siempre devuelve un par de valores.

```go
func (s *Stack) Top() (any, error) {
    var x any
    if s.IsEmpty() {
        return x, errors.New("pila vacía")
    }
    x = s.data[len(s.data)-1]

    return x, nil
}
```

`Top`{l=go} es similar a `Pop`{l=go} pero no elimina el tope

```go
import "fmt"

func main() {
    // Crear una nueva pila de enteros
    s := NewStack()

    // Agregar elementos a la pila
    s.Push(1)
    s.Push("cadena")
    s.Push(3.52)

    // Verificar si la pila está vacía
    if s.IsEmpty() {
        fmt.Println("La pila está vacía")
    } else {
        fmt.Println("La pila no está vacía")
    }

    // Consultar el elemento en la cima de la pila
    topElement, _ := s.Top()
    fmt.Println("Elemento en la cima de la pila:", topElement)

    // Extraer elementos de la pila
    for !s.IsEmpty() {
        poppedElement, _ := s.Pop()
        fmt.Println("Elemento extraído de la pila:", poppedElement)
    }

    // Verificar si la pila está vacía
    if s.IsEmpty() {
        fmt.Println("La pila está vacía")
    } else {
        fmt.Println("La pila no está vacía")
    }
}

main()
```

## Cola

Es una estructura del tipo **FIFO (First In First Out)** es decir el primer elemento en ingresar en la cola es el primero en salir. Un ejemplo clásico del uso de esta estructura es para modelar una {ref}`cola-personas`, por ejemplo en la caja de un supermercado. La última persona que llega se coloca al final de la cola y espera su turno para hacer atendido

```{figure} ../assets/images/people-queue.png
---
width: 500px
name: cola-personas
---
Cola de Espera
```

El comportamiento de la cola queda definido por los siguientes métodos:

`Enqueue`{l=go}
: Permite insertar un elemento en la cola (siempre en la última posición)

`Dequeue`{l=go}
: Permite extraer un elemento de la cola (siempre el primero). Si se intenta hacer un Dequeue de una cola vacía se debe indicar un error

`Front`{l=go}
: Permite ver el primer elemento de la cola. Si se intenta hacer un Front de una cola vacía se debe indicar un error

`IsEmpty`{l=go}
: Verifica si la Coa está vacía. Devuelve `true`{l=go} si la cola está vacía o `false`{l=go} en caso contrario

Todas las operaciones deben ser $O(1)$. Es decir de tiempo constante, independiente del tamaño de la entrada

## Ejercicios

1. Implementar una cola genérica, similar a la pila dada.
2. Verificar que todas las operaciones de pila y cola sean $O(1)$
3. Escribir casos de pruebas para las operaciones de pila y cola[^1].

[^1]: Los casos deben cubrir todas las operaciones
