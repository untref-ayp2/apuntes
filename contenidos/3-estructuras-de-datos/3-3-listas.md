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
linenos:
---
type node[T any] struct {
    data T
    next *node[T]
}
```

```{code-block} go
---
linenos:
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
linenos:
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
linenos:
---
type node[T any] struct {
    data T
    next *node[T]
    prev *node[T]
}
```

```{code-block} go
---
linenos:
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
linenos:
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
linenos:
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

::::{tab-set}
:::{tab-item} Simple

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

:::
:::{tab-item} Doble

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

:::
:::{tab-item} Circular

```{code-block} text
---
caption: find — Lista Circular
---
find(buscado):
    si IsEmpty():
        retornar nil
    actual := head
    para i := 0; i < tamaño; i++:
        si actual.dato == buscado:
            retornar actual
        actual = actual.siguiente
    retornar nil
```

:::
::::

### Consulta

Size()
: Devuelve la cantidad de nodos de la lista.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: Size — Lista Simple
---
Size():
    retornar size
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: Size — Lista Doble
---
Size():
    retornar size
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: Size — Lista Circular
---
Size():
    retornar size
```

:::
::::

IsEmpty()
: Devuelve `true` si la lista no tiene elementos.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: IsEmpty — Lista Simple
---
IsEmpty():
    retornar size == 0
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: IsEmpty — Lista Doble
---
IsEmpty():
    retornar size == 0
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: IsEmpty — Lista Circular
---
IsEmpty():
    retornar size == 0
```

:::
::::

Contains(data T)
: Devuelve `true` si el elemento está presente (solo la primera ocurrencia).

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: Contains — Lista Simple
---
Contains(buscado):
    retornar find(buscado) != nil
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: Contains — Lista Doble
---
Contains(buscado):
    retornar find(buscado) != nil
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: Contains — Lista Circular
---
Contains(buscado):
    retornar find(buscado) != nil
```

:::
::::

Head()
: Devuelve el dato del primer nodo. Si la lista está vacía devuelve el valor cero y `false`.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: Head — Lista Simple
---
Head():
    si IsEmpty():
        retornar zero, falso
    retornar head.dato, verdadero
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: Head — Lista Doble
---
Head():
    si IsEmpty():
        retornar zero, falso
    retornar head.dato, verdadero
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: Head — Lista Circular
---
Head():
    si IsEmpty():
        retornar zero, falso
    retornar head.dato, verdadero
```

:::
::::

Tail()
: Devuelve el dato del último nodo. En la lista circular se obtiene desde `head.prev`.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: Tail — Lista Simple
---
Tail():
    si IsEmpty():
        retornar zero, falso
    retornar tail.dato, verdadero
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: Tail — Lista Doble
---
Tail():
    si IsEmpty():
        retornar zero, falso
    retornar tail.dato, verdadero
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: Tail — Lista Circular
---
Tail():
    si IsEmpty():
        retornar zero, falso
    retornar head.prev.dato, verdadero
```

:::
::::

### Inserción

Prepend(data T)
: Agrega un nodo con el dato al inicio de la lista.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: Prepend — Lista Simple
---
Prepend(dato):
    nuevo := NuevoNodo(dato)
    nuevo.siguiente = head
    head = nuevo
    si tail == nil:
        tail = nuevo
    tamaño++
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: Prepend — Lista Doble
---
Prepend(dato):
    nuevo := NuevoNodo(dato)
    nuevo.siguiente = head
    si head != nil:
        head.prev = nuevo
    head = nuevo
    si tail == nil:
        tail = nuevo
    tamaño++
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: Prepend — Lista Circular
---
Prepend(dato):
    nuevo := NuevoNodo(dato)
    si IsEmpty():
        nuevo.siguiente = nuevo
        nuevo.prev = nuevo
    sino:
        cola := head.prev
        nuevo.siguiente = head
        nuevo.prev = cola
        head.prev = nuevo
        cola.siguiente = nuevo
    head = nuevo
    tamaño++
```

:::
::::

La lista simple solo actualiza `head` y `tail` en caso de lista vacía.
La doble además debe enlazar `prev` del `head` anterior.
La circular requiere mantener el ciclo, enlazando el nuevo nodo con `head` y con la cola (`head.prev`).

Append(data T)
: Agrega un nodo con el dato al final de la lista.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: Append — Lista Simple
---
Append(dato):
    nuevo := NuevoNodo(dato)
    si tail != nil:
        tail.siguiente = nuevo
    tail = nuevo
    si head == nil:
        head = nuevo
    tamaño++
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: Append — Lista Doble
---
Append(dato):
    nuevo := NuevoNodo(dato)
    nuevo.prev = tail
    si tail != nil:
        tail.siguiente = nuevo
    tail = nuevo
    si head == nil:
        head = nuevo
    tamaño++
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: Append — Lista Circular
---
Append(dato):
    si IsEmpty():
        Prepend(dato)
        retornar
    cola := head.prev
    nuevo := NuevoNodo(dato)
    nuevo.prev = cola
    nuevo.siguiente = head
    cola.siguiente = nuevo
    head.prev = nuevo
    tamaño++
```

:::
::::

InsertAfter(target, data T)
: Busca `target` e inserta un nodo con `data` a continuación. Devuelve `false` si no encuentra `target`.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: InsertAfter — Lista Simple
---
InsertAfter(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso
    nuevo := NuevoNodo(dato)
    nuevo.siguiente = actual.siguiente
    actual.siguiente = nuevo
    si actual == tail:
        tail = nuevo
    tamaño++
    retornar verdadero
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: InsertAfter — Lista Doble
---
InsertAfter(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso
    nuevo := NuevoNodo(dato)
    nuevo.siguiente = actual.siguiente
    nuevo.prev = actual
    actual.siguiente = nuevo
    si nuevo.siguiente != nil:
        nuevo.siguiente.prev = nuevo
    sino:
        tail = nuevo
    tamaño++
    retornar verdadero
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: InsertAfter — Lista Circular
---
InsertAfter(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso
    nuevo := NuevoNodo(dato)
    nuevo.siguiente = actual.siguiente
    nuevo.prev = actual
    actual.siguiente.prev = nuevo
    actual.siguiente = nuevo
    tamaño++
    retornar verdadero
```

:::
::::

InsertBefore(target, data T)
: Busca `target` e inserta un nodo con `data` antes. Devuelve `false` si no encuentra `target`.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: InsertBefore — Lista Simple
---
InsertBefore(buscado, dato):
    si head == nil:
        retornar falso
    si head.dato == buscado:
        Prepend(dato)
        retornar verdadero
    actual := head
    mientras actual.siguiente != nil:
        si actual.siguiente.dato == buscado:
            nuevo := NuevoNodo(dato)
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            tamaño++
            retornar verdadero
        actual = actual.siguiente
    retornar falso
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: InsertBefore — Lista Doble
---
InsertBefore(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso
    nuevo := NuevoNodo(dato)
    nuevo.prev = actual.prev
    nuevo.siguiente = actual
    actual.prev = nuevo
    si nuevo.prev != nil:
        nuevo.prev.siguiente = nuevo
    sino:
        head = nuevo
    tamaño++
    retornar verdadero
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: InsertBefore — Lista Circular
---
InsertBefore(buscado, dato):
    actual := find(buscado)
    si actual == nil:
        retornar falso
    nuevo := NuevoNodo(dato)
    nuevo.prev = actual.prev
    nuevo.siguiente = actual
    actual.prev.siguiente = nuevo
    actual.prev = nuevo
    si actual == head:
        head = nuevo
    tamaño++
    retornar verdadero
```

:::
::::

En la lista simple `InsertBefore` requiere recorrer la lista buscando al predecesor porque no hay puntero `prev`.
En la lista doble y circular, una vez encontrado el nodo, el reenlace es $O(1)$ gracias al puntero `prev`.

### Eliminación

RemoveFirst()
: Elimina el primer nodo. Devuelve `false` si la lista está vacía.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: RemoveFirst — Lista Simple
---
RemoveFirst():
    si IsEmpty():
        retornar falso
    head = head.siguiente
    si head == nil:
        tail = nil
    tamaño--
    retornar verdadero
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: RemoveFirst — Lista Doble
---
RemoveFirst():
    si IsEmpty():
        retornar falso
    head = head.siguiente
    si head != nil:
        head.prev = nil
    sino:
        tail = nil
    tamaño--
    retornar verdadero
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: RemoveFirst — Lista Circular
---
RemoveFirst():
    si IsEmpty():
        retornar falso
    si tamaño == 1:
        head = nil
    sino:
        cola := head.prev
        head = head.siguiente
        head.prev = cola
        cola.siguiente = head
    tamaño--
    retornar verdadero
```

:::
::::

RemoveLast()
: Elimina el último nodo. Devuelve `false` si la lista está vacía.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: RemoveLast — Lista Simple
---
RemoveLast():
    si IsEmpty():
        retornar falso
    si head == tail:
        head = nil
        tail = nil
        tamaño = 0
        retornar verdadero
    actual := head
    mientras actual.siguiente != tail:
        actual = actual.siguiente
    actual.siguiente = nil
    tail = actual
    tamaño--
    retornar verdadero
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: RemoveLast — Lista Doble
---
RemoveLast():
    si IsEmpty():
        retornar falso
    tail = tail.prev
    si tail != nil:
        tail.siguiente = nil
    sino:
        head = nil
    tamaño--
    retornar verdadero
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: RemoveLast — Lista Circular
---
RemoveLast():
    si IsEmpty():
        retornar falso
    si tamaño == 1:
        head = nil
    sino:
        cola := head.prev
        anteultimo := cola.prev
        anteultimo.siguiente = head
        head.prev = anteultimo
    tamaño--
    retornar verdadero
```

:::
::::

`RemoveLast` es $O(n)$ en la lista simple porque debe recorrer hasta el anteúltimo nodo, mientras que en doble y circular es $O(1)$ gracias al puntero `prev`.

Remove(data T)
: Busca y elimina la **primera** ocurrencia del elemento. Si hay elementos duplicados, solo se elimina el primero que se encuentra. Devuelve `false` si no lo encuentra.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: Remove — Lista Simple
---
Remove(dato):
    si IsEmpty():
        retornar falso
    si head.dato == dato:
        RemoveFirst()
        retornar verdadero
    actual := head
    mientras actual.siguiente != nil:
        si actual.siguiente.dato == dato:
            actual.siguiente = actual.siguiente.siguiente
            si actual.siguiente == nil:
                tail = actual
            tamaño--
            retornar verdadero
        actual = actual.siguiente
    retornar falso
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: Remove — Lista Doble
---
Remove(dato):
    actual := find(dato)
    si actual == nil:
        retornar falso
    si actual.prev != nil:
        actual.prev.siguiente = actual.siguiente
    sino:
        head = actual.siguiente
    si actual.siguiente != nil:
        actual.siguiente.prev = actual.prev
    sino:
        tail = actual.prev
    tamaño--
    retornar verdadero
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: Remove — Lista Circular
---
Remove(dato):
    si IsEmpty():
        retornar falso
    actual := head
    para i := 0; i < tamaño; i++:
        si actual.dato == dato:
            actual.prev.siguiente = actual.siguiente
            actual.siguiente.prev = actual.prev
            si actual == head:
                head = actual.siguiente
            tamaño--
            retornar verdadero
        actual = actual.siguiente
    retornar falso
```

:::
::::

La lista simple debe tratar como caso especial la eliminación de la cabeza (no hay predecesor) y la actualización de `tail`. En doble y circular, el puntero `prev` permite reenlazar simétricamente, aunque en doble aún se verifican extremos.

### Recorrido

Values()
: Devuelve un slice con los datos en el orden de la lista.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: Values — Lista Simple
---
Values():
    resultado := []
    actual := head
    mientras actual != nil:
        resultado.agregar(actual.dato)
        actual = actual.siguiente
    retornar resultado
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: Values — Lista Doble
---
Values():
    resultado := []
    actual := head
    mientras actual != nil:
        resultado.agregar(actual.dato)
        actual = actual.siguiente
    retornar resultado
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: Values — Lista Circular
---
Values():
    si IsEmpty():
        retornar []
    resultado := []
    actual := head
    para i := 0; i < tamaño; i++:
        resultado.agregar(actual.dato)
        actual = actual.siguiente
    retornar resultado
```

:::
::::

### Utilidad

Clear()
: Elimina todos los nodos y deja la lista vacía.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: Clear — Lista Simple
---
Clear():
    head = nil
    tail = nil
    tamaño = 0
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: Clear — Lista Doble
---
Clear():
    head = nil
    tail = nil
    tamaño = 0
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: Clear — Lista Circular
---
Clear():
    head = nil
    tamaño = 0
```

:::
::::

String()
: Devuelve una representación textual de la lista.

::::{tab-set}
:::{tab-item} Simple

```{code-block} text
---
caption: String — Lista Simple
---
String():
    elementos := Values()
    retornar "[" + elementos.join(", ") + "]"
```

:::
:::{tab-item} Doble

```{code-block} text
---
caption: String — Lista Doble
---
String():
    elementos := Values()
    retornar "[" + elementos.join(", ") + "]"
```

:::
:::{tab-item} Circular

```{code-block} text
---
caption: String — Lista Circular
---
String():
    elementos := Values()
    retornar "[" + elementos.join(", ") + "]"
```

:::
::::

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
linenos:
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

IsEmpty
: La lista vacía se detecta cuando `size ==0` o los centinelas se apuntan entre sí.

```{code-block} text
---
caption: IsEmpty — Lista con Centinelas
---
IsEmpty():
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
        retornar zero, falso
    retornar head.siguiente.dato, verdadero

Tail():
    si IsEmpty():
        retornar zero, falso
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
        retornar falso
    nuevo := NuevoNodo(dato)
    nuevo.prev = actual.prev
    nuevo.siguiente = actual
    actual.prev.siguiente = nuevo
    actual.prev = nuevo
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
        retornar falso
    nuevo := NuevoNodo(dato)
    nuevo.siguiente = actual.siguiente
    nuevo.prev = actual
    actual.siguiente.prev = nuevo
    actual.siguiente = nuevo
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
    nuevo := NuevoNodo(dato)
    nuevo.siguiente = head.siguiente
    nuevo.prev = head
    head.siguiente.prev = nuevo
    head.siguiente = nuevo
    tamaño++
```

Append
: Inserta entre el último nodo real y el centinela `tail`.

```{code-block} text
---
caption: Append — Lista con Centinelas
---
Append(dato):
    nuevo := NuevoNodo(dato)
    nuevo.siguiente = tail
    nuevo.prev = tail.prev
    tail.prev.siguiente = nuevo
    tail.prev = nuevo
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
        retornar falso
    actual.prev.siguiente = actual.siguiente
    actual.siguiente.prev = actual.prev
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
        retornar falso
    head.siguiente = head.siguiente.siguiente
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
        retornar falso
    tail.prev = tail.prev.prev
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
    head.siguiente = tail
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
