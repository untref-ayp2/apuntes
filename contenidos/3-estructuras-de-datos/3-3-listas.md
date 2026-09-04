---
label: listas
---

# Listas Enlazadas

Las listas enlazadas son estructuras de datos que permiten almacenar una colección de elementos en posiciones de memoria **no necesariamente contiguas**. Cada elemento se guarda en un nodo que contiene un campo de dato y uno o dos punteros a otros nodos. Los nodos se enlazan entre sí para formar la secuencia.

Son estructuras **dinámicas**: pueden crecer a medida que se agregan datos y reducirse cuando se eliminan. A diferencia de los arreglos, no requieren bloques contiguos de memoria ni reasignaciones costosas al cambiar de tamaño.

Algunos usos frecuentes:

Algoritmos de manipulación de texto
: Las listas enlazadas son útiles en procesamiento de texto, donde la inserción y eliminación de caracteres o líneas se realizan con frecuencia. Cada línea del documento puede ser un nodo; insertar o borrar una línea solo requiere reenlazar punteros, sin desplazar el resto del contenido.

Undo y redo en aplicaciones
: Las listas enlazadas dobles permiten navegar hacia adelante y atrás en el historial de acciones. Cada acción es un nodo; la doble vinculación permite moverse en ambas direcciones en tiempo constante.

Listas de reproducción
: Una lista circular permite reproducir canciones en ciclo infinito. Al llegar al final, se vuelve al principio sin necesidad de reiniciar manualmente. Algunas implementaciones combinan listas dobles (para avanzar/retroceder) con comportamiento circular (para repetición continua).

Existen cuatro variantes principales de listas enlazadas, que se diferencian en la cantidad de punteros por nodo, cómo se marcan los extremos y cómo se recorren. Cada variante tiene fortalezas y debilidades según la operación que se quiera optimizar.

## Lista Enlazada Simple

```{admonition} Definición
---
class: hint
---
Una lista enlazada simple es una estructura lineal donde cada nodo tiene un **sucesor**, salvo el último cuyo puntero es `nil`. La lista vacía no contiene nodos y su tamaño es 0.

El nodo almacena:
- **Dato**: el valor del elemento.
- **Siguiente**: puntero al próximo nodo de la secuencia.
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-3-listas/ListaEnlazadaSimple_light.svg
---
name: ssl-estructura
class: only-light-mode
---
Lista Enlazada Simple
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-3-listas/ListaEnlazadaSimple_dark.svg
---
class: only-dark-mode
---
Lista Enlazada Simple
```

```{code-block} go
---
linenos: true
---
type node[T any] struct {
    data T
    next *node[T]
}
```

```{code-block} go
---
linenos: true
---
type List[T comparable] struct {
    head *node[T]
    tail *node[T]
    size int
}
```

Notar que el nodo se parametriza con `[T any]` porque solo almacena y enlaza datos, sin necesidad de compararlos. La lista, en cambio, usa `[T comparable]`, ya que, como veremos a continuación, algunas operaciones necesitan comparar elementos con `==` para encontrar un dato buscado.

Cuando una operación como `Head()` o `Tail()` se ejecuta sobre una lista vacía, debe devolver el **valor cero** del tipo `T` (no `nil`, que solo es válido para punteros, *slices*, *maps* y canales). En Go, el valor cero se obtiene con `var zero T`:

```{code-block} go
---
linenos: true
---
var zero T
/*
    0       para int
    0.0     para float
    ""      para string
    false   para bool
    nil     para punteros, slices, maps y canales
*/
```

## Lista Enlazada Doble

```{admonition} Definición
---
class: hint
---
Una lista enlazada doble es una estructura lineal donde cada nodo tiene un **sucesor** y un **predecesor**, salvo el primero (sin predecesor) y el último (sin sucesor).

El nodo almacena:
- **Dato**: el valor del elemento.
- **Siguiente**: puntero al próximo nodo.
- **Previo / Anterior**: puntero al nodo predecesor.
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-3-listas/ListaEnlazadaDoble_light.svg
---
name: dll-estructura
class: only-light-mode
---
Lista Enlazada Doble
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-3-listas/ListaEnlazadaDoble_dark.svg
---
class: only-dark-mode
---
Lista Enlazada Doble
```

```{code-block} go
---
linenos: true
---
type node[T any] struct {
    data T
    next *node[T]
    prev *node[T]
}
```

```{code-block} go
---
linenos: true
---
type List[T comparable] struct {
    head *node[T]
    tail *node[T]
    size int
}
```

## Lista Enlazada Circular

```{admonition} Definición
---
class: hint
---
Una lista enlazada circular es una estructura donde el último nodo se enlaza al primero, formando un ciclo. Puede implementarse con enlaces simples o dobles.

En una lista circular doble:
- El sucesor del último nodo es el primero.
- El predecesor del primero es el último.
- No hay marcador de fin: el recorrido puede continuar indefinidamente.

El nodo es el mismo que el de la lista doble (`node[T]` con `next` y `prev`).
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-3-listas/ListaEnlazadaCircularDoble_light.svg
---
name: cll-estructura
class: only-light-mode
---
Lista Enlazada Circular Doble
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-3-listas/ListaEnlazadaCircularDoble_dark.svg
---
class: only-dark-mode
---
Lista Enlazada Circular Doble
```

Al ser cíclica, basta con mantener un único puntero a la cabeza: la cola se obtiene como `head.prev`. Esto ahorra un campo en la estructura.

```{code-block} go
---
linenos: true
---
type List[T comparable] struct {
    head *node[T]  // único puntero necesario
    size int
}
```

## Interfaz común

Si bien las listas son versátiles y no existe un único comportamiento estándar para todas, vamos a definir una interfaz común para los tipos de lista que veremos a continuación. El objetivo es didáctico: acordar un conjunto de operaciones típicas que nos permita comparar implementaciones.

```{code-block} go
---
linenos: true
---
type List[T comparable] interface {
    // Consulta
    Size() int
    IsEmpty() bool
    Contains(data T) bool
    Head() (T, bool)
    Tail() (T, bool)

    // Inserción
    Prepend(data T)
    Append(data T)
    InsertAfter(target, data T) bool
    InsertBefore(target, data T) bool

    // Eliminación
    RemoveFirst() bool
    RemoveLast() bool
    Remove(data T) bool

    // Recorrido
    Values() []T

    // Utilidad
    Clear()
    String() string
}
```

La mayoría de las operaciones de inserción, eliminación y búsqueda dependen de un método interno `find` que recorre la lista en busca de un elemento. Este método es **privado** (en Go, minúscula inicial) porque devuelve un puntero a un nodo interno, y no debería exponerse fuera de la lista. A continuación se muestra su implementación en cada variante; las operaciones del resto de la sección lo referencian.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: find — Lista Simple
---
find(buscado):
    actual := head
    mientras actual != nil:
        si actual.dato == buscado:
            retornar actual
        actual = actual.siguiente
    retornar nil
```

````
````{tab-item} Doble

```{code-block} text
---
caption: find — Lista Doble
---
find(buscado):
    actual := head
    mientras actual != nil:
        si actual.dato == buscado:
            retornar actual
        actual = actual.siguiente
    retornar nil
```

````
````{tab-item} Circular

```{code-block} text
---
caption: find — Lista Circular
---
find(buscado):
    si IsEmpty():
        retornar nil
    actual := head
    para i := 0; i < Size(); i++:
        si actual.dato == buscado:
            retornar actual
        actual = actual.siguiente
    retornar nil
```

````
`````

### Consulta

Size()
: Devuelve la cantidad de nodos de la lista.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: Size — Lista Simple
---
Size():
    retornar size
```

````
````{tab-item} Doble

```{code-block} text
---
caption: Size — Lista Doble
---
Size():
    retornar size
```

````
````{tab-item} Circular

```{code-block} text
---
caption: Size — Lista Circular
---
Size():
    retornar size
```

````
`````

IsEmpty()
: Devuelve `true` si la lista no tiene elementos.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: IsEmpty — Lista Simple
---
IsEmpty():
    retornar size == 0
```

````
````{tab-item} Doble

```{code-block} text
---
caption: IsEmpty — Lista Doble
---
IsEmpty():
    retornar size == 0
```

````
````{tab-item} Circular

```{code-block} text
---
caption: IsEmpty — Lista Circular
---
IsEmpty():
    retornar size == 0
```

````
`````

Contains(data T)
: Devuelve `true` si el elemento está presente (solo la primera ocurrencia).

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: Contains — Lista Simple
---
Contains(buscado):
    retornar find(buscado) != nil
```

````
````{tab-item} Doble

```{code-block} text
---
caption: Contains — Lista Doble
---
Contains(buscado):
    retornar find(buscado) != nil
```

````
````{tab-item} Circular

```{code-block} text
---
caption: Contains — Lista Circular
---
Contains(buscado):
    retornar find(buscado) != nil
```

````
`````

Head()
: Devuelve el dato del primer nodo. Si la lista está vacía devuelve el valor cero y `false`.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: Head — Lista Simple
---
Head():
    si IsEmpty():
        retornar zero, falso  // lista vacía: no hay primer dato
    retornar head.dato, verdadero
```

````
````{tab-item} Doble

```{code-block} text
---
caption: Head — Lista Doble
---
Head():
    si IsEmpty():
        retornar zero, falso  // lista vacía: no hay primer dato
    retornar head.dato, verdadero
```

````
````{tab-item} Circular

```{code-block} text
---
caption: Head — Lista Circular
---
Head():
    si IsEmpty():
        retornar zero, falso  // lista vacía: no hay primer dato
    retornar head.dato, verdadero
```

````
`````

Tail()
: Devuelve el dato del último nodo. En la lista circular se obtiene desde `head.prev`.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: Tail — Lista Simple
---
Tail():
    si IsEmpty():
        retornar zero, falso  // lista vacía: no hay último dato
    retornar tail.dato, verdadero
```

````
````{tab-item} Doble

```{code-block} text
---
caption: Tail — Lista Doble
---
Tail():
    si IsEmpty():
        retornar zero, falso  // lista vacía: no hay último dato
    retornar tail.dato, verdadero
```

````
````{tab-item} Circular

```{code-block} text
---
caption: Tail — Lista Circular
---
Tail():
    si IsEmpty():
        retornar zero, falso  // lista vacía: no hay último dato
    retornar head.prev.dato, verdadero  // en la circular la cola precede a head
```

````
`````

### Inserción

Prepend(data T)
: Agrega un nodo con el dato al inicio de la lista.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: Prepend — Lista Simple
---
Prepend(dato):
    nuevo := nuevoNodo(dato)
    nuevo.siguiente = head  // apunta al que era el primer nodo
    head = nuevo            // el nuevo pasa a ser el primer nodo
    si IsEmpty():
        tail = nuevo  // si estaba vacía, el nuevo también es la cola
    tamaño++
```

````
````{tab-item} Doble

```{code-block} text
---
caption: Prepend — Lista Doble
---
Prepend(dato):
    nuevo := nuevoNodo(dato)
    nuevo.siguiente = head  // apunta al que era el primer nodo
    si IsEmpty():
        tail = nuevo  // si estaba vacía, el nuevo también es la cola
    sino:
        head.prev = nuevo  // el nodo anterior enlaza su prev al nuevo
    head = nuevo  // el nuevo pasa a ser el primer nodo
    tamaño++
```

````
````{tab-item} Circular

```{code-block} text
---
caption: Prepend — Lista Circular
---
Prepend(dato):
    nuevo := nuevoNodo(dato)
    si IsEmpty():
        nuevo.siguiente = nuevo  // lista de un solo nodo: se apunta a sí mismo
        nuevo.prev = nuevo
    sino:
        cola := head.prev
        nuevo.siguiente = head
        nuevo.prev = cola
        head.prev = nuevo
        cola.siguiente = nuevo  // cierra el ciclo entre cola y el nuevo head
    head = nuevo
    tamaño++
```

````
`````

La lista simple solo actualiza `head` y `tail` en caso de lista vacía.
La doble además debe enlazar `prev` del `head` anterior.
La circular requiere mantener el ciclo, enlazando el nuevo nodo con `head` y con la cola (`head.prev`).

Append(data T)
: Agrega un nodo con el dato al final de la lista.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: Append — Lista Simple
---
Append(dato):
    nuevo := nuevoNodo(dato)
    si IsEmpty():
        head = nuevo  // el primer nodo de la lista
    sino:
        tail.siguiente = nuevo  // se encadena tras la cola actual
    tail = nuevo  // en ambos casos el nuevo pasa a ser la cola
    tamaño++
```

````
````{tab-item} Doble

```{code-block} text
---
caption: Append — Lista Doble
---
Append(dato):
    nuevo := nuevoNodo(dato)
    nuevo.prev = tail  // apunta al que era la cola
    si IsEmpty():
        head = nuevo  // el primer nodo de la lista
    sino:
        tail.siguiente = nuevo  // se encadena tras la cola actual
    tail = nuevo  // en ambos casos el nuevo pasa a ser la cola
    tamaño++
```

````
````{tab-item} Circular

```{code-block} text
---
caption: Append — Lista Circular
---
Append(dato):
    si IsEmpty():
        Prepend(dato)  // reutiliza el caso de lista con un solo nodo
        retornar
    cola := head.prev
    nuevo := nuevoNodo(dato)
    nuevo.prev = cola  // el nuevo va entre la cola y head
    nuevo.siguiente = head
    cola.siguiente = nuevo
    head.prev = nuevo  // queda enlazado en ambos extremos del ciclo
    tamaño++
```

````
`````

InsertAfter(target, data T)
: Busca `target` e inserta un nodo con `data` a continuación. Devuelve `false` si no encuentra `target`.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: InsertAfter — Lista Simple
---
InsertAfter(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso  // target no encontrado
    nuevo := nuevoNodo(dato)
    nuevo.siguiente = actual.siguiente  // el nuevo apunta al sucesor de actual
    actual.siguiente = nuevo  // actual pasa a apuntar al nuevo
    si actual == tail:
        tail = nuevo  // si inserté al final, el nuevo es la nueva cola
    tamaño++
    retornar verdadero
```

````
````{tab-item} Doble

```{code-block} text
---
caption: InsertAfter — Lista Doble
---
InsertAfter(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso  // target no encontrado
    nuevo := nuevoNodo(dato)
    nuevo.siguiente = actual.siguiente
    nuevo.prev = actual
    si actual == tail:
        tail = nuevo  // si inserté al final, el nuevo es la nueva cola
    sino:
        nuevo.siguiente.prev = nuevo  // el sucesor enlaza su prev al nuevo
    actual.siguiente = nuevo  // actual pasa a apuntar al nuevo
    tamaño++
    retornar verdadero
```

````
````{tab-item} Circular

```{code-block} text
---
caption: InsertAfter — Lista Circular
---
InsertAfter(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso  // target no encontrado
    nuevo := nuevoNodo(dato)
    nuevo.siguiente = actual.siguiente
    nuevo.prev = actual
    actual.siguiente.prev = nuevo  // el sucesor enlaza su prev al nuevo
    actual.siguiente = nuevo  // actual pasa a apuntar al nuevo
    tamaño++
    retornar verdadero
```

````
`````

InsertBefore(target, data T)
: Busca `target` e inserta un nodo con `data` antes. Devuelve `false` si no encuentra `target`.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: InsertBefore — Lista Simple
---
InsertBefore(buscado, dato):
    si IsEmpty():
        retornar falso  // no hay nada ante qué insertar
    si head.dato == buscado:
        Prepend(dato)  // insertar antes del primer nodo es un prepend
        retornar verdadero
    actual := head
    mientras actual.siguiente != nil:
        si actual.siguiente.dato == buscado:
            nuevo := nuevoNodo(dato)
            nuevo.siguiente = actual.siguiente  // el nuevo apunta al target
            actual.siguiente = nuevo  // actual pasa a apuntar al nuevo
            tamaño++
            retornar verdadero
        actual = actual.siguiente  // recorre buscando al predecesor del target
    retornar falso
```

````
````{tab-item} Doble

```{code-block} text
---
caption: InsertBefore — Lista Doble
---
InsertBefore(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso  // target no encontrado
    nuevo := nuevoNodo(dato)
    nuevo.prev = actual.prev
    nuevo.siguiente = actual
    si actual == head:
        head = nuevo  // si inserté antes del primer nodo, el nuevo es head
    sino:
        // el predecesor enlaza su siguiente al nuevo
        nuevo.prev.siguiente = nuevo
    actual.prev = nuevo  // target pasa a apuntar al nuevo
    tamaño++
    retornar verdadero
```

````
````{tab-item} Circular

```{code-block} text
---
caption: InsertBefore — Lista Circular
---
InsertBefore(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso  // target no encontrado
    nuevo := nuevoNodo(dato)
    nuevo.prev = actual.prev
    nuevo.siguiente = actual
    actual.prev.siguiente = nuevo  // el predecesor enlaza su siguiente al nuevo
    actual.prev = nuevo  // target pasa a apuntar al nuevo
    si actual == head:
        head = nuevo  // si inserté antes del primer nodo, el nuevo es head
    tamaño++
    retornar verdadero
```

````
`````

En la lista simple `InsertBefore` requiere recorrer la lista buscando al predecesor porque no hay puntero `prev`.
En la lista doble y circular, una vez encontrado el nodo, el reenlace es $O(1)$ gracias al puntero `prev`.

### Eliminación

RemoveFirst()
: Elimina el primer nodo. Devuelve `false` si la lista está vacía.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: RemoveFirst — Lista Simple
---
RemoveFirst():
    si IsEmpty():
        retornar falso  // nada que eliminar
    si Size() == 1:
        Clear()  // el único nodo: se vacía toda la lista
        retornar verdadero
    head = head.siguiente  // salta el primer nodo
    tamaño--
    retornar verdadero
```

````
````{tab-item} Doble

```{code-block} text
---
caption: RemoveFirst — Lista Doble
---
RemoveFirst():
    si IsEmpty():
        retornar falso  // nada que eliminar
    si Size() == 1:
        Clear()  // el único nodo: se vacía toda la lista
        retornar verdadero
    head = head.siguiente  // salta el primer nodo
    head.prev = nil  // el nuevo head ya no tiene predecesor
    tamaño--
    retornar verdadero
```

````
````{tab-item} Circular

```{code-block} text
---
caption: RemoveFirst — Lista Circular
---
RemoveFirst():
    si IsEmpty():
        retornar falso  // nada que eliminar
    si Size() == 1:
        Clear()  // el único nodo: se vacía toda la lista
        retornar verdadero
    cola := head.prev  // guarda la cola antes de mover head
    head = head.siguiente  // salta el primer nodo
    head.prev = cola
    cola.siguiente = head  // vuelve a cerrar el ciclo
    tamaño--
    retornar verdadero
```

````
`````

RemoveLast()
: Elimina el último nodo. Devuelve `false` si la lista está vacía.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: RemoveLast — Lista Simple
---
RemoveLast():
    si IsEmpty():
        retornar falso  // nada que eliminar
    si Size() == 1:
        Clear()  // el único nodo: se vacía toda la lista
        retornar verdadero
    actual := head
    mientras actual.siguiente != tail:
        actual = actual.siguiente  // avanza hasta el anteúltimo nodo
    actual.siguiente = nil  // desconecta el último nodo
    tail = actual  // el anteúltimo pasa a ser la cola
    tamaño--
    retornar verdadero
```

````
````{tab-item} Doble

```{code-block} text
---
caption: RemoveLast — Lista Doble
---
RemoveLast():
    si IsEmpty():
        retornar falso  // nada que eliminar
    si Size() == 1:
        Clear()  // el único nodo: se vacía toda la lista
        retornar verdadero
    tail = tail.prev  // retrocede al anteúltimo nodo
    tail.siguiente = nil  // desconecta el último nodo
    tamaño--
    retornar verdadero
```

````
````{tab-item} Circular

```{code-block} text
---
caption: RemoveLast — Lista Circular
---
RemoveLast():
    si IsEmpty():
        retornar falso  // nada que eliminar
    si Size() == 1:
        Clear()  // el único nodo: se vacía toda la lista
        retornar verdadero
    cola := head.prev  // cola actual
    anteultimo := cola.prev
    anteultimo.siguiente = head  // la nueva cola apunta a head
    head.prev = anteultimo  // head queda enlazado con la nueva cola
    tamaño--
    retornar verdadero
```

````
`````

`RemoveLast` es $O(n)$ en la lista simple porque debe recorrer hasta el anteúltimo nodo, mientras que en doble y circular es $O(1)$ gracias al puntero `prev`.

Remove(data T)
: Busca y elimina la **primera** ocurrencia del elemento. Si hay elementos duplicados, solo se elimina el primero que se encuentra. Devuelve `false` si no lo encuentra.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: Remove — Lista Simple
---
Remove(dato):
    si IsEmpty():
        retornar falso  // nada que eliminar
    si head.dato == dato:
        RemoveFirst()  // el target es la cabeza: reutiliza el caso simple
        retornar verdadero
    actual := head
    mientras actual.siguiente != nil:
        si actual.siguiente.dato == dato:
            // salta el nodo a eliminar
            actual.siguiente = actual.siguiente.siguiente
            si actual.siguiente == nil:
                // si eliminé el último, actual pasa a ser la cola
                tail = actual
            tamaño--
            retornar verdadero
        actual = actual.siguiente
    retornar falso
```

````
````{tab-item} Doble

```{code-block} text
---
caption: Remove — Lista Doble
---
Remove(dato):
    actual := find(dato)
    si actual == nil:
        retornar falso  // dato no encontrado
    si actual == head:
        head = actual.siguiente  // el target era la cabeza
    sino:
        // salta hacia adelante desde el predecesor
        actual.prev.siguiente = actual.siguiente
    si actual == tail:
        tail = actual.prev  // el target era la cola
    sino:
        // salta hacia atrás desde el sucesor
        actual.siguiente.prev = actual.prev
    tamaño--
    retornar verdadero
```

````
````{tab-item} Circular

```{code-block} text
---
caption: Remove — Lista Circular
---
Remove(dato):
    si IsEmpty():
        retornar falso  // nada que eliminar
    si Size() == 1:
        si head.dato == dato:
            Clear()  // era el único nodo
            retornar verdadero
        retornar falso
    actual := head
    para i := 0; i < Size(); i++:
        si actual.dato == dato:
            // salta el nodo en el ciclo
            actual.prev.siguiente = actual.siguiente
            actual.siguiente.prev = actual.prev
            si actual == head:
                head = actual.siguiente  // si eliminé la cabeza, avanza
            tamaño--
            retornar verdadero
        actual = actual.siguiente
    retornar falso
```

````
`````

La lista simple debe tratar como caso especial la eliminación de la cabeza (no hay predecesor) y la actualización de `tail`. En doble y circular, el puntero `prev` permite reenlazar simétricamente, aunque en doble aún se verifican extremos.

### Recorrido

Values()
: Devuelve un slice con los datos en el orden de la lista.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: Values — Lista Simple
---
Values():
    resultado := []
    actual := head
    mientras actual != nil:
        resultado.agregar(actual.dato)
        actual = actual.siguiente  // avanza al siguiente nodo
    retornar resultado
```

````
````{tab-item} Doble

```{code-block} text
---
caption: Values — Lista Doble
---
Values():
    resultado := []
    actual := head
    mientras actual != nil:
        resultado.agregar(actual.dato)
        actual = actual.siguiente  // avanza al siguiente nodo
    retornar resultado
```

````
````{tab-item} Circular

```{code-block} text
---
caption: Values — Lista Circular
---
Values():
    si IsEmpty():
        retornar []  // sin nodos, no hay nada que recorrer
    resultado := []
    actual := head
    // nunca llega a nil: recorre una vuelta completa
    para i := 0; i < Size(); i++:
        resultado.agregar(actual.dato)
        actual = actual.siguiente
    retornar resultado
```

````
`````

### Utilidad

Clear()
: Elimina todos los nodos y deja la lista vacía.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: Clear — Lista Simple
---
Clear():
    head = nil
    tail = nil
    tamaño = 0
```

````
````{tab-item} Doble

```{code-block} text
---
caption: Clear — Lista Doble
---
Clear():
    head = nil
    tail = nil
    tamaño = 0
```

````
````{tab-item} Circular

```{code-block} text
---
caption: Clear — Lista Circular
---
Clear():
    head = nil  // en la circular solo existe head: no hay tail que resetear
    tamaño = 0
```

````
`````

String()
: Devuelve una representación textual de la lista.

`````{tab-set}
````{tab-item} Simple

```{code-block} text
---
caption: String — Lista Simple
---
String():
    elementos := Values()
    retornar "[" + elementos.join(", ") + "]"
```

````
````{tab-item} Doble

```{code-block} text
---
caption: String — Lista Doble
---
String():
    elementos := Values()
    retornar "[" + elementos.join(", ") + "]"
```

````
````{tab-item} Circular

```{code-block} text
---
caption: String — Lista Circular
---
String():
    elementos := Values()
    retornar "[" + elementos.join(", ") + "]"
```

````
`````

## Lista con Centinelas

```{admonition} Definición
---
class: hint
---
Los centinelas son nodos ficticios que se colocan al principio y al final de la lista. No contienen datos útiles y su propósito es eliminar los casos especiales en las operaciones de inserción y eliminación.

En una lista con centinelas:
- La cabeza real es el sucesor del centinela frontal.
- La cola real es el predecesor del centinela trasero.
- Una lista vacía tiene los dos centinelas apuntándose entre sí.
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-3-listas/ListaConCentinelas_light.svg
---
name: lista-centinelas
class: only-light-mode
---
Lista Enlazada Doble con Centinelas
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-3-listas/ListaConCentinelas_dark.svg
---
class: only-dark-mode
---
Lista Enlazada Doble con Centinelas
```

```{code-block} go
---
linenos: true
---
type List[T comparable] struct {
    head *node[T]  // centinela frontal
    tail *node[T]  // centinela trasero
    size int
}
```

Los centinelas eliminan los casos borde de lista vacía, cabeza y cola. Al inicializar la lista, `head.siguiente = tail` y `tail.prev = head`. Como los centinelas nunca son `nil`, toda inserción o eliminación ocurre siempre entre dos nodos reales o ficticios, y las operaciones se vuelven uniformes.

find
: Al no haber `nil`, el recorrido va desde `head.siguiente` hasta llegar al centinela `tail`.

```{code-block} text
---
caption: find — Lista con Centinelas
---
find(buscado):
    // el primer nodo real está tras el centinela frontal
    actual := head.siguiente
    // el centinela trasero marca el fin: nunca se llega a nil
    mientras actual != tail:
        si actual.dato == buscado:
            retornar actual
        actual = actual.siguiente
    retornar nil
```

IsEmpty
: La lista vacía se detecta cuando `size == 0` o los centinelas se apuntan entre sí.

```{code-block} text
---
caption: IsEmpty — Lista con Centinelas
---
IsEmpty():
    // vacía cuando los centinelas se apuntan entre sí
    retornar head.siguiente == tail
```

Head / Tail
: El primer dato está en `head.siguiente` y el último en `tail.prev`.

```{code-block} text
---
caption: Head / Tail — Lista con Centinelas
---
Head():
    si IsEmpty():
        retornar zero, falso  // lista vacía
    // el primer nodo real está tras el centinela frontal
    retornar head.siguiente.dato, verdadero

Tail():
    si IsEmpty():
        retornar zero, falso  // lista vacía
    // el último nodo real está antes del centinela trasero
    retornar tail.prev.dato, verdadero
```

InsertBefore
: No necesita verificar si `actual` es la cabeza real porque el centinela `head` garantiza que `actual.prev` nunca es `nil`.

```{code-block} text
---
caption: InsertBefore — Lista con Centinelas
---
InsertBefore(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso  // buscado no encontrado
    nuevo := nuevoNodo(dato)
    // si actual es el primer nodo real, su prev es el centinela head
    nuevo.prev = actual.prev
    nuevo.siguiente = actual
    actual.prev.siguiente = nuevo  // el predecesor enlaza su siguiente al nuevo
    actual.prev = nuevo  // actual pasa a apuntar al nuevo
    tamaño++
    retornar verdadero
```

InsertAfter
: Como `actual.siguiente` nunca es `nil` (puede ser `tail`), no hay caso especial de cola.

```{code-block} text
---
caption: InsertAfter — Lista con Centinelas
---
InsertAfter(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso  // buscado no encontrado
    nuevo := nuevoNodo(dato)
    // el sucesor puede ser el centinela tail: nunca es nil
    nuevo.siguiente = actual.siguiente
    nuevo.prev = actual
    actual.siguiente.prev = nuevo  // el sucesor enlaza su prev al nuevo
    actual.siguiente = nuevo  // actual pasa a apuntar al nuevo
    tamaño++
    retornar verdadero
```

Prepend
: Inserta entre el centinela `head` y el primer nodo real. No puede delegar en `InsertBefore` porque busca por valor y fallaría con datos duplicados.

```{code-block} text
---
caption: Prepend — Lista con Centinelas
---
Prepend(dato):
    nuevo := nuevoNodo(dato)
    // si la lista está vacía, head.siguiente es tail: igual funciona
    nuevo.siguiente = head.siguiente
    nuevo.prev = head
    // el primer nodo real (o el centinela tail) enlaza su prev al nuevo
    head.siguiente.prev = nuevo
    head.siguiente = nuevo  // el centinela head apunta al nuevo
    tamaño++
```

Append
: Inserta entre el último nodo real y el centinela `tail`.

```{code-block} text
---
caption: Append — Lista con Centinelas
---
Append(dato):
    nuevo := nuevoNodo(dato)
    nuevo.siguiente = tail  // apunta al centinela final
    // si la lista está vacía, tail.prev es head: igual funciona
    nuevo.prev = tail.prev
    // el último nodo real (o el centinela head) enlaza su siguiente al nuevo
    tail.prev.siguiente = nuevo
    tail.prev = nuevo  // el centinela tail apunta al nuevo
    tamaño++
```

Remove
: No necesita verificar si el nodo es `head` o `tail` real. Los centinelas aseguran que `actual.prev` y `actual.siguiente` siempre existen.

```{code-block} text
---
caption: Remove — Lista con Centinelas
---
Remove(dato):
    actual := find(dato)
    si actual == nil:
        retornar falso  // dato no encontrado
    // sin casos de cabeza o cola: si actual es el primer o último nodo real,
    // el vecino del otro lado es un centinela y se reenlaza igual
    actual.prev.siguiente = actual.siguiente  // el predecesor salta al sucesor
    actual.siguiente.prev = actual.prev  // el sucesor salta al predecesor
    tamaño--
    retornar verdadero
```

RemoveFirst
: Reenlaza el centinela `head` con el segundo nodo real. No puede delegar en `Remove` por el mismo problema de los duplicados.

```{code-block} text
---
caption: RemoveFirst — Lista con Centinelas
---
RemoveFirst():
    si IsEmpty():
        retornar falso  // nada que eliminar
    head.siguiente = head.siguiente.siguiente  // salta el primer nodo real
    // el nuevo head.siguiente apunta al centinela
    // (puede ser tail si era el único nodo)
    head.siguiente.prev = head
    tamaño--
    retornar verdadero
```

RemoveLast
: Reenlaza el centinela `tail` con el anteúltimo nodo real.

```{code-block} text
---
caption: RemoveLast — Lista con Centinelas
---
RemoveLast():
    si IsEmpty():
        retornar falso  // nada que eliminar
    tail.prev = tail.prev.prev  // retrocede al anteúltimo nodo real
    // el nuevo tail.prev apunta al centinela
    // (puede ser head si era el único nodo)
    tail.prev.siguiente = tail
    tamaño--
    retornar verdadero
```

Clear
: Solo reenlaza los centinelas entre sí.

```{code-block} text
---
caption: Clear — Lista con Centinelas
---
Clear():
    head.siguiente = tail  // reenlaza los centinelas entre sí
    tail.prev = head
    tamaño = 0
```

**Ventajas frente a las versiones sin centinelas:**

- `InsertBefore` e `InsertAfter` sin verificar extremos.
- `Prepend` y `Append` con código simétrico, sin casos de lista vacía.
- `Remove` sin verificar `head`/`tail`.
- `RemoveFirst` y `RemoveLast` con código simétrico.
- `Clear` solo reenlaza los centinelas.
- `IsEmpty` es simplemente comparar punteros.

La principal desventaja es el costo de memoria de dos nodos adicionales, que es despreciable en la mayoría de los escenarios.

```{table} Comparación de algunas de las operaciones según la variante
---
align: center
---
| Operación        | Simple     | Doble      | Circular   | Centinelas |
| :--------------- | :--------: | :--------: | :--------: | :--------: |
| `Head`           | $O(1)$     | $O(1)$     | $O(1)$     | $O(1)$     |
| `Tail`           | $O(1)$     | $O(1)$     | $O(1)$     | $O(1)$     |
| `Prepend`        | $O(1)$     | $O(1)$     | $O(1)$     | $O(1)$     |
| `Append`         | $O(1)$     | $O(1)$     | $O(1)$     | $O(1)$     |
| `InsertAfter`    | $O(n)$     | $O(n)$     | $O(n)$     | $O(n)$     |
| `InsertBefore`   | $O(n)$     | $O(n)$     | $O(n)$     | $O(n)$     |
| `RemoveFirst`    | $O(1)$     | $O(1)$     | $O(1)$     | $O(1)$     |
| `RemoveLast`     | $O(n)$     | $O(1)$     | $O(1)$     | $O(1)$     |
| `Remove`         | $O(n)$     | $O(n)$     | $O(n)$     | $O(n)$     |
| `find`           | $O(n)$     | $O(n)$     | $O(n)$     | $O(n)$     |
| `Clear`          | $O(1)$     | $O(1)$     | $O(1)$     | $O(1)$     |
```

La complejidad asintótica de las operaciones que requieren búsqueda es $O(n)$ en todas las variantes. La diferencia está en las constantes y en la cantidad de casos especiales que debe manejar el código: la lista simple requiere verificaciones constantes de `nil` en los extremos, mientras que los centinelas las eliminan por completo.

## Ejercicios

Los ejercicios de este capítulo están en `03-listas/ejercicios/` del
repositorio taller-tad.

Antes de comenzar, asegurate de tener implementadas las estructuras necesarias en
data-structures,
que está dentro del repositorio `taller-tad`.
Ambas tareas se trabajan en paralelo: primero completás las implementaciones
en `data-structures` y después las usás acá.
