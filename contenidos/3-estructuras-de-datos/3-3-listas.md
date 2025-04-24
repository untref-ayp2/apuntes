---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Listas Enlazadas

Las listas enlazadas son estructuras de datos que permiten almacenar una colección de elementos, en posiciones de memoria **no necesariamente contiguas**. Cada elemento de una lista se almacena en un nodo que contiene un campo de dato y uno o dos punteros a otros nodos.

Los nodos están enlazados entre sí para formar la lista. Son estructuras de datos **dinámicas**, que pueden crecer a medida que se le agregan datos y decrecer cuando se eliminan.

Las listas enlazadas generalmente se usan como contenedores para definir estructuras de datos más complejas. Existen varios tipos de listas enlazadas, que se utilizan para distintas aplicaciones.

Algunos usos de las listas enlazadas pueden ser:

Algoritmos de manipulación de texto
: Las listas enlazadas son útiles en aplicaciones y algoritmos de procesamiento de texto, como editores de texto, donde la inserción y eliminación de caracteres o líneas se realizan con frecuencia.

Undo y redo en aplicaciones
: Las listas enlazadas dobles son útiles para implementar funciones de deshacer y rehacer en aplicaciones de software, ya que permiten navegar hacia adelante y hacia atrás en el historial de acciones realizadas.

Listas de reproducción
: Algunas aplicaciones utilizan listas circulares para implementar las funciones de avanzar y retroceder en listas de reproducción infinitas.

Las listas que estudiaremos son:

- Lista Enlazada Simple (Simple Linked List)
- Lista Enlazada Doble (Double Linked List)
- Lista Circular (Circular List)

Las listas enlazadas son muy versátiles y su comportamiento se puede adaptar a medida de las necesidades. Algunas de las operaciones típicas que soporta una lista enlazada son:

`Head`
: Devuelve un puntero al primer elemento de la lista.

`Tail`
: Devuelve un puntero al último elemento de la lista.

`Size`
: Devuelve el tamaño de la lista (cantidad de nodos que tiene la lista).

`IsEmpty`
: Devuelve **Verdadero** si la lista está vacía o **Falso** en caso contrario.

`Prepend`
: Insertar un elemento en la cabeza de la lista.

`Append`
: Insertar un elemento en la cola de la lista.

`InsertAfter`
: Inserta un elemento a continuación de un elemento dado.

`InsertBefore`
: Inserta un elemento antes de un elemento dado.

`RemoveFirst`
: Elimina el primer elemento de la lista.

`RemoveLast`
: Elimina el último elemento de la lista.

`Remove`
: Elimina la primera aparición del elemento dado.

`Find`
: Devuelve un puntero a la primera aparición de un elemento buscado.

`Clear`
: Elimina todos los elementos de la lista

## Lista Enlazada Simple

```{Admonition} Definición

Una lista enlazada simple es una estructura de datos lineal donde cada nodo de la lista tiene un sucesor, salvo el último. Por definición la lista vacía es la que no contiene datos y su tamaño es 0.

El nodo de una lista enlazada simple tiene dos campos:

Dato
: El valor que se almacena en el nodo.

Puntero (o enlace)
: Una referencia a la dirección de memoria del siguiente nodo en la secuencia.
```

```{figure} ../assets/images/ListaEnlazadaSimple.svg
---
width: 500px
name: lista-simple
---
Lista Enlazada Simple
```

### Búsqueda

Para buscar un elemento no queda otra alternativa que recorrer toda la lista desde la cabeza de la misma hasta encontrar el elemento o llegar al final de la lista y determinar que no se encuentra. Si encuentra el elemento devuelve un puntero al nodo correspondiente o nulo en caso contrario

```{code-block}
:linenos:
Find(buscado):
    actual := self.Head()
    mientras actual != nulo:
        si actual.Data() == buscado:
            retornar actual
        actual = actual.Next()
    retornar nulo
```

### Inserción después de un elemento dado

Supongamos que dada la lista de la figura {ref}`lista-simple`, se quiere insertar un elemento nuevo después de un elemento dado. Para poder lograrlo primero hay que crear un nuevo nodo con el elemento a insertar, buscar el elemento después del cual se quiere insertar y finalmente actualizar los campos siguientes de los nodos:

```{code-block}
:linenos:
InsertAfter(buscado, elemento):
    nuevo := NuevoNodo(elemento)
    actual := self.Find(buscado)
    si actual != nulo:
        nuevo.SetNext(actual.Next()) // Primero hay que enlazar el nuevo nodo a la lista
        actual.SetNext(nuevo) // Después corregir al siguiente del nodo actual
```

De esta forma se garantiza la integridad de la lista. Ver figura {ref}`ssl-insercion`

```{figure} ../assets/images/ListaEnlazadaSimpleInsercion.svg
---
width: 500px
name: ssl-insercion
---
Inserción en una Lista Enlazada Simple
```

### Eliminación

Supongamos que dada la lista de la figura {ref}`lista-simple`, se quiere eliminar el elemento **E3**, para no perder la integridad de la lista se deben seguir los pasos a continuación:

```{code-block}
:linenos:
Remove(buscado):
    si
    actual := self.Find(buscado)
    si actual != nulo:
        si actual == self.Head():
            self.RemoveFirst()
            return
        previo := self.Head()
        mientras previo.Next().Data()

```

Eventualmente el recolector de basura liberará la memoria que ocupa el nodo **E3**, ya no es alcanzable (no hay ningún puntero que nos permita llegar a **E3**). Ver figura {ref}`ssl-eliminacion`

```{figure} ../assets/images/ListaEnlazadaSimpleEliminacion.svg
---
width: 500px
name: ssl-eliminacion
---
Eliminación de un elemento en una Lista Enlazada Simple
```

### Orden de las operaciones

En la siguiente tabla se muestra el orden que deberían tener las operaciones básicas sobre una lista enlazada simple

:::{table} Orden de las Operaciones
:width: 40%
:align: center

|   Operación    | Orden  |
| :------------: | :----: |
|     `Head`     | $O(1)$ |
|     `Tail`     | $O(1)$ |
|     `Size`     | $O(1)$ |
|   `IsEmpty`    | $O(1)$ |
|   `Prepend`    | $O(1)$ |
|    `Append`    | $O(1)$ |
| `InsertAfter`  | $O(n)$ |
| `InsertBefore` | $O(n)$ |
| `RemoveFirst`  | $O(1)$ |
|  `RemoveLast`  | $O(n)$ |
|    `Remove`    | $O(n)$ |
|     `Find`     | $O(n)$ |
|    `Clear`     | $O(1)$ |

:::

Las operaciones que requieren recorrer la lista son $O(n)$. En particular buscar un elemento, insertar o eliminar un elemento en una posición arbitraria requieren recorrer uno a uno cada nodo hasta posicionarse en el nodo adecuado.

Encontrar el predecesor de un elemento dado también es $O(n)$ ya que hay ingresar a la lista desde la cabeza y comparar si el siguiente de cada nodo es el nodo actual para poder encontrar su predecesor.

### Implementación de la lista enlazada simple

Existen distintas alternativas para implementar una lista. Una alternativa se muestra en la figura {ref}`ssl-implementacion`. Para lograr que las operaciones de insertar y eliminar un elemento de la cola de la lista sean $O(1)$ se guarda un puntero a la cola de la lista, para poder acceder en tiempo constante al último elemento de la lista. En esta implementación la lista vacía se representa cuando los punteros a la cabeza y la cola son nulos y el tamaño es 0

```{figure} ../assets/images/ListaEnlazadaSimpleImplementacion.svg
---
width: 500px
name: ssl-implementacion
---
Implementación de una Lista Enlazada Simple, con punteros a la cabeza y la cola
```

### Implementación en Go

A continuación una implementación de una lista enlazada simple, donde se definen dos tipos `LinkedNode` como un node de lista que contiene un dato y un puntero al siguiente y el tipo `LinkedList`. Los datos de la lista son genéricos, pero se piden que sean Comparables entre sí

```{code-block} go
:linenos:
package list

// LinkedNode representa un nodo de una lista enlazada simple.
type LinkedNode[T comparable] struct {
    data T
    next *LinkedNode[T]
}

// NewLinkedListNode crea un nuevo nodo de lista enlazada con el dato especificado.
//
// Uso:
//
// node := list.NewLinkedListNode(10) // Crea un nuevo nodo con el dato 10.
//
// Parámetros:
//   - `data`: el dato a almacenar en el nodo.
func NewLinkedListNode[T comparable](data T) *LinkedNode[T] {
    return &LinkedNode[T]{data: data}
}

// SetData establece el dato almacenado en el nodo.
//
// Uso:
//
// node.SetData(20) // Establece el dato del nodo a 20.
//
// Parámetros:
//   - `data`: el dato a almacenar en el nodo.
func (n *LinkedNode[T]) SetData(data T) {
    n.data = data
}

// Data devuelve el dato almacenado en el nodo.
//
// Uso:
//
// data := node.Data() // Obtiene el dato almacenado en el nodo.
//
// Retorna:
//   - el dato almacenado en el nodo.
func (n *LinkedNode[T]) Data() T {
    return n.data
}

// SetNext establece el nodo siguiente al nodo actual.
//
// Uso:
//
// node.SetNext(newNode) // Establece el nodo siguiente al nodo actual.
//
// Parámetros:
//   - `newNext`: el nodo siguiente al nodo actual.
func (n *LinkedNode[T]) SetNext(newNext *LinkedNode[T]) {
    n.next = newNext
}

// Next devuelve el nodo siguiente al nodo actual.
//
// Uso:
//
// nextNode := node.Next() // Obtiene el nodo siguiente al nodo actual.
func (n *LinkedNode[T]) Next() *LinkedNode[T] {
    return n.next
}

// HasNext evalúa si el nodo actual tiene asignado un nodo siguiente.
//
// Uso:
//
// if node.HasNext() {
//  fmt.Println("El nodo tiene un nodo siguiente.")
// }
//
// Retorna:
//   - `true` si el nodo tiene un nodo siguiente; `false` en caso contrario.
func (n *LinkedNode[T]) HasNext() bool {
    return n.next != nil
}
```

```{code-block} go
:linenos:
package list

import "fmt"

// LinkedList se implementa con un nodo que contiene un dato y un puntero al siguiente nodo.
// Los elementos deben ser de un tipo comparable.
type LinkedList[T comparable] struct {
    head *LinkedNode[T]
    tail *LinkedNode[T]
    size int
}

// NewLinkedList crea una nueva lista vacía.
//
// Uso:
//
// list := list.NewLinkedList[int]() // Crea una nueva lista vacía.
func NewLinkedList[T comparable]() *LinkedList[T] {
    return &LinkedList[T]{}
}

// Head devuelve el primer nodo de la lista.
//
// Uso:
//
// head := list.Head() // Obtiene el primer nodo de la lista.
//
// Retorna:
//   - el primer nodo de la lista.
func (l *LinkedList[T]) Head() *LinkedNode[T] {
    return l.head
}

// Tail devuelve el último nodo de la lista.
//
// Uso:
//
// tail := list.Tail() // Obtiene el último nodo de la lista.
//
// Retorna:
//   - el último nodo de la lista.
func (l *LinkedList[T]) Tail() *LinkedNode[T] {
    return l.tail
}

// Size devuelve el tamaño de la lista.
//
// Uso:
//
// size := list.Size() // Obtiene el tamaño de la lista.
//
// Retorna:
//   - el tamaño de la lista.
func (l *LinkedList[T]) Size() int {
    return l.size
}

// IsEmpty evalúa si la lista está vacía.
//
// Uso:
//
// empty := list.IsEmpty() // Verifica si la lista está vacía.
//
// Retorna:
//   - `true` si la lista está vacía; `false` en caso contrario.
func (l *LinkedList[T]) IsEmpty() bool {
    return l.size == 0
}

// Clear elimina todos los nodos de la lista.
//
// Uso:
//
// list.Clear() // Elimina todos los nodos de la lista.
func (l *LinkedList[T]) Clear() {
    l.head = nil
    l.tail = nil
    l.size = 0
}

// Prepend inserta un dato al inicio de la lista.
//
// Uso:
//
// list.Prepend(10) // Inserta el dato 10 al inicio de la lista.
//
// Parámetros:
//   - `data`: el dato a insertar en la lista.
func (l *LinkedList[T]) Prepend(data T) {
    newNode := NewLinkedListNode(data)
    if l.IsEmpty() {
        l.tail = newNode
    } else {
        newNode.SetNext(l.head)
    }
    l.head = newNode
    l.size++
}

// Append inserta un dato al final de la lista.
//
// Uso:
//
// list.Append(10) // Inserta el dato 10 al final de la lista.
//
// Parámetros:
//   - `data`: el dato a insertar en la lista.
func (l *LinkedList[T]) Append(data T) {
    newNode := NewLinkedListNode(data)
    if l.IsEmpty() {
        l.head = newNode
    } else {
        l.tail.SetNext(newNode)
    }
    l.tail = newNode
    l.size++
}

// Find busca un dato en la lista, si lo encuentra devuelve el nodo
// correspondiente, si no lo encuentra devuelve nil
//
// Uso:
//
// node := list.Find(10) // Busca el dato 10 en la lista.
//
// Parámetros:
//   - `data`: el dato a buscar en la lista.
//
// Retorna:
//   - el nodo que contiene el dato; `nil` si el dato no se encuentra.
func (l *LinkedList[T]) Find(data T) *LinkedNode[T] {
    for current := l.head; current != nil; current = current.Next() {
        if current.Data() == data {
            return current
        }
    }

    return nil
}

// RemoveFirst elimina el primer nodo de la lista.
//
// Uso:
//
// list.RemoveFirst() // Elimina el primer nodo de la lista.
func (l *LinkedList[T]) RemoveFirst() {
    if l.IsEmpty() {
        return
    }

    l.head = l.head.Next()

    if l.head == nil {
        l.tail = nil
    }

    l.size--
}

// RemoveLast elimina el último nodo de la lista.
//
// Uso:
//
// list.RemoveLast() // Elimina el último nodo de la lista.
func (l *LinkedList[T]) RemoveLast() {
    if l.IsEmpty() {
        return
    }

    if l.Size() == 1 {
        l.head = nil
        l.tail = nil
    } else {
        current := l.head
        for current.Next() != l.tail {
            current = current.Next()
        }
        current.SetNext(nil)
        l.tail = current
    }
    l.size--
}

// Remove elimina un la primera aparición de un dato en la lista.
//
// Uso:
//
// list.Remove(10) // Elimina la primera aparición del dato 10 en la lista.
//
// Parámetros:
//   - `data`: el dato a eliminar de la lista.
func (l *LinkedList[T]) Remove(data T) {
    node := l.Find(data)

    if node == nil {
        return
    }

    if node == l.head {
        l.RemoveFirst()
        return
    }

    current := l.Head()

    for current.Next() != node {
        current = current.Next()
    }

    current.SetNext(node.Next())

    if node == l.tail {
        l.tail = current
    }
    l.size--
}

// String devuelve una representación en cadena de la lista.
//
// Uso:
//
// fmt.Println(list) // Imprime la representación en cadena de la lista.
//
// Retorna:
//   - una representación en cadena de la lista.
func (l *LinkedList[T]) String() string {
    if l.IsEmpty() {
        return "LinkedList: []"
    }

    result := "LinkedList: "

    current := l.Head()
    for {
        result += fmt.Sprintf("[%v]", current.Data())
        if !current.HasNext() {
            break
        }
        result += " → "
        current = current.Next()
    }

    return result
}
```

## Lista Enlazada Doble

En la lista doble, en cada nodo se mantienen dos punteros, uno al sucesor y otro al predecesor. Esta lista permite avanzar y retroceder una posición en la lista en tiempo constante $O(1)$. Su principal uso es en aplicaciones que requieran avanzar y retroceder desde cualquier posición como editores de texto o gestores de historiales de navegación. En la siguiente figura se puede ver una representación gráfica.

```{figure} ../assets/images/ListaEnlazadaDoble.svg
---
width: 500px
name: lista-doble
---
Implementación de una Lista Enlazada Doble, con punteros a la cabeza y la cola
```

## Lista Enlazada Circular

En una lista circular el último nodo se enlaza al primero para poder recorrer en forma continua la lista, se utiliza para modelar colas, gestión de procesos de un sistema operativo y juegos entre otras aplicaciones. En la siguiente figura se puede ver una implementación de una lista circular doble. Las listas circulares se pueden implementar con enlaces dobles o simples. Como el último y el primer elemento de la lista están enlazados solo es necesario mantener un puntero a la cabeza de la lista.

```{figure} ../assets/images/ListaEnlazadaCircularDoble.svg
---
width: 500px
name: lista-circular-doble
---
Implementación de una Lista Enlazada Circular Doble, con puntero a la cabeza
```

## Implementaciones con Centinelas

Los centinelas son nodos ficticios que no contienen datos, y se agrega uno al principio y otro al final de la lista.

El propósito de estos centinelas es de alguna forma estandarizar las operaciones primitivas de las listas sin tener que contemplar casos especiales como si la lista está vacía (y por lo tanto no hay ningún nodo) o si estoy parado sobre el último elemento, etc.

```{figure} ../assets/images/ListaConCentinelas.svg
---
width: 500px
name: lista-centinelas
---
Implementación de una Lista Enlazada Doble con centinelas
```

Hay que prestar especial atención a que ahora la lista vacía contendrá al menos dos nodos que se apuntan entre si y no contienen datos como se observa en la siguiente figura

```{figure} ../assets/images/ListaVaciaCentinelas.svg
---
width: 500px
name: lista-vacia-centinelas
---
Representación de una Lista Enlazada Doble, vacía, con centinelas
```

## Ejercicios

1. Implementar una lista circular simple, similar a la lista simple dada.
2. Implementar una lista enlazada doble, similar a la lista simple dada.
3. Implementar una lista enlazada doble con centinelas.
4. Analizar pros y contra de cada una de las implementaciones de lista enlazada doble con y sin centinelas.
