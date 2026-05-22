---
label: listas
---

# Listas Enlazadas

Las listas enlazadas son estructuras de datos que permiten almacenar una colección de elementos, en posiciones de memoria **no necesariamente contiguas**. Cada elemento de una lista se almacena en un nodo que contiene un campo de dato y uno o dos punteros a otros nodos.

Los nodos están enlazados entre sí para formar la lista. Son estructuras de datos **dinámicas**, que pueden crecer a medida que se le agregan datos y reducirse cuando se eliminan.

Algunos usos de las listas enlazadas pueden ser:

Algoritmos de manipulación de texto
: Las listas enlazadas son útiles en aplicaciones y algoritmos de procesamiento de texto, como editores de texto, donde la inserción y eliminación de caracteres o líneas se realizan con frecuencia.

Undo y redo en aplicaciones
: Las listas enlazadas dobles son útiles para implementar funciones de deshacer y rehacer en aplicaciones de software, ya que permiten navegar hacia adelante y hacia atrás en el historial de acciones realizadas.

Listas de reproducción
: Algunas aplicaciones utilizan listas circulares para implementar las funciones de avanzar y retroceder en listas de reproducción infinitas.

## Interfaz común

Si bien las listas son muy versátiles y su comportamiento se adapta a las necesidades del programador, vamos a definir un conjunto de operaciones, a los fines didácticos, para comprender cual es el comportamiento esperado de este TAD:

### Operaciones de consulta

Size()
: Devuelve la cantidad de nodos de la lista.

IsEmpty()
: Devuelve `true` si la lista no tiene elementos.

Contains(data T)
: Devuelve `true` si el elemento está presente en la lista.

Head()
: Devuelve el dato del primer nodo. Si la lista está vacía devuelve el valor cero y `false`.

Tail()
: Devuelve el dato del último nodo. Si la lista está vacía devuelve el valor cero y `false`.

### Operaciones de inserción

Prepend(data T)
: Agrega un nodo con el dato al inicio de la lista.

Append(data T)
: Agrega un nodo con el dato al final de la lista.

InsertAfter(target, data T)
: Busca `target` e inserta un nodo con `data` a continuación. Devuelve `false` si no encuentra `target`.

InsertBefore(target, data T)
: Busca `target` e inserta un nodo con `data` antes. Devuelve `false` si no encuentra `target`.

### Operaciones de eliminación

RemoveFirst()
: Elimina el primer nodo. Devuelve `false` si la lista está vacía.

RemoveLast()
: Elimina el último nodo. Devuelve `false` si la lista está vacía.

Remove(data T)
: Busca y elimina la primera ocurrencia del elemento. Devuelve `false` si no lo encuentra.

### Operaciones varias

Values()
: Devuelve un slice con los datos en el orden de la lista.

Clear()
: Elimina todos los nodos y deja la lista vacía.

String()
: Devuelve una representación textual de la lista.

Cada variante implementa esta interfaz con distintas estructuras internas y distintas complejidades.

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

## Lista Enlazada Simple

```{admonition} Definición
---
class: hint
---
Una lista enlazada simple es una estructura de datos lineal donde cada nodo de la lista tiene un sucesor, salvo el último. Por definición la lista vacía es la que no contiene datos y su tamaño es 0.

El nodo de una lista enlazada simple tiene dos campos:

Dato
: El valor que se almacena en el nodo.

Puntero (o enlace)
: Una referencia a la dirección de memoria del siguiente nodo en la secuencia.
```

En su implementación más común se mantienen punteros a la cabeza y a la cola, y un contador de tamaño. Esto permite que las operaciones sobre los extremos sean $O(1)$.

```{figure} ../_static/figures/ListaEnlazadaSimpleImplementacion_light.svg
---
width: 100%
class: only-light-mode
name: ssl-implementacion
---
Implementación de una Lista Enlazada Simple, con punteros a la cabeza y la cola
```

```{figure} ../_static/figures/ListaEnlazadaSimpleImplementacion_dark.svg
---
width: 100%
class: only-dark-mode
name: ssl-implementacion
---
Implementación de una Lista Enlazada Simple, con punteros a la cabeza y la cola
```

### Búsqueda

Para buscar un elemento se recorre la lista desde la cabeza hasta encontrar el elemento o llegar al final.

```{code-block}
---
linenos: true
---
Find(buscado):
    actual := Head()
    mientras actual != nulo:
        si actual.dato == buscado:
            retornar actual
        actual = actual.siguiente
    retornar nulo
```

### Inserción después de un elemento

InsertAfter enlaza el nuevo nodo corrigiendo primero su `siguiente` y luego el del nodo actual.

```{figure} ../_static/figures/ListaEnlazadaSimpleInsercion_light.svg
---
width: 100%
class: only-light-mode
name: ssl-insercion
---
Inserción en una Lista Enlazada Simple
```

```{figure} ../_static/figures/ListaEnlazadaSimpleInsercion_dark.svg
---
width: 100%
class: only-dark-mode
name: ssl-insercion
---
Inserción en una Lista Enlazada Simple
```

```{code-block}
---
linenos: true
---
InsertAfter(buscado, elemento):
    nuevo := NuevoNodo(elemento)
    actual := Find(buscado)
    si actual != nulo:
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        tamaño++
        retornar true
    retornar false
```

### Eliminación

Para eliminar un elemento se debe encontrar su predecesor y actualizar su enlace `siguiente`. `RemoveLast` es $O(n)$ porque incluso con puntero a la cola necesita encontrar el anteúltimo nodo.

```{figure} ../_static/figures/ListaEnlazadaSimpleEliminacion_light.svg
---
width: 100%
class: only-light-mode
name: ssl-eliminacion
---
Eliminación de un elemento en una Lista Enlazada Simple
```

```{figure} ../_static/figures/ListaEnlazadaSimpleEliminacion_dark.svg
---
width: 100%
class: only-dark-mode
name: ssl-eliminacion
---
Eliminación de un elemento en una Lista Enlazada Simple
```

```{code-block}
---
linenos: true
---
Remove(buscado):
    si IsEmpty():
        retornar false
    si Head().dato == buscado:
        RemoveFirst()
        retornar true
    actual := Head()
    mientras actual.siguiente != nulo:
        si actual.siguiente.dato == buscado:
            actual.siguiente = actual.siguiente.siguiente
            si actual.siguiente == nulo:
                Tail() = actual
            tamaño--
            retornar true
        actual = actual.siguiente
    retornar false
```

### Clear

Clear solo requiere liberar los nodos y reiniciar los punteros. Como en simple solo se necesita descartar la cabeza, su complejidad es $O(1)$.

```{code-block}
---
linenos: true
---
Clear():
    head = nulo
    tail = nulo
    tamaño = 0
```

```{table} Orden de las Operaciones — Lista Simple
---
width: 40%
align: center
---
|      Operación       | Orden  |
| :------------------: | :----: |
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
```

Las operaciones que requieren recorrer la lista son $O(n)$. En particular, `RemoveLast` es $O(n)$ incluso con puntero a la cola, porque necesita encontrar el anteúltimo nodo.

## Lista Enlazada Doble

```{admonition} Definición
---
class: hint
---
Una lista enlazada doble es una estructura de datos lineal donde cada nodo tiene un sucesor y un predecesor, salvo el primero y el último.

El nodo de una lista enlazada doble tiene tres campos:

Dato
: El valor que se almacena en el nodo.

Puntero al sucesor
: Una referencia a la dirección de memoria del siguiente nodo en la secuencia.

Puntero al predecesor
: Una referencia a la dirección de memoria del nodo anterior en la secuencia.
```

En la lista doble, cada nodo mantiene dos punteros: uno al sucesor y otro al predecesor. Esto permite avanzar y retroceder en tiempo constante $O(1)$.

```{figure} ../_static/figures/ListaEnlazadaDoble_light.svg
---
width: 100%
class: only-light-mode
name: lista-doble
---
Lista Enlazada Doble
```

```{figure} ../_static/figures/ListaEnlazadaDoble_dark.svg
---
width: 100%
class: only-dark-mode
name: lista-doble
---
Lista Enlazada Doble
```

Al tener acceso directo al predecesor, operaciones como `RemoveLast` e `InsertBefore` se vuelven $O(1)$.

### Inserción antes de un elemento

InsertBefore en una lista doble no necesita recorrer desde la cabeza porque el nodo apunta a su predecesor.

```{figure} ../_static/figures/ListaEnlazadaDobleInsercionBefore_light.svg
---
width: 100%
class: only-light-mode
name: dll-insercion-before
---
Inserción antes de un elemento en una Lista Enlazada Doble
```

```{figure} ../_static/figures/ListaEnlazadaDobleInsercionBefore_dark.svg
---
width: 100%
class: only-dark-mode
name: dll-insercion-before
---
Inserción antes de un elemento en una Lista Enlazada Doble
```

```{code-block}
---
linenos: true
---
InsertBefore(buscado, elemento):
    actual := Find(buscado)
    si actual != nulo:
        nuevo := NuevoNodo(elemento)
        nuevo.siguiente = actual
        nuevo.prev = actual.prev
        si actual.prev != nulo:
            actual.prev.siguiente = nuevo
        sino:
            head = nuevo
        actual.prev = nuevo
        tamaño++
        retornar true
    retornar false
```

### RemoveLast

RemoveLast accede directamente al anteúltimo nodo mediante `tail.prev`, eliminando la necesidad de recorrer la lista.

```{code-block}
---
linenos: true
---
RemoveLast():
    si IsEmpty():
        retornar false
    si tamaño == 1:
        RemoveFirst()
        retornar true
    anteultimo := tail.prev
    anteultimo.siguiente = nulo
    tail = anteultimo
    tamaño--
    retornar true
```

```{table} Orden de las Operaciones — Lista Doble
---
width: 40%
align: center
---
|      Operación       | Orden  |
| :------------------: | :----: |
|     `Head`     | $O(1)$ |
|     `Tail`     | $O(1)$ |
|     `Size`     | $O(1)$ |
|   `IsEmpty`    | $O(1)$ |
|   `Prepend`    | $O(1)$ |
|    `Append`    | $O(1)$ |
| `InsertAfter`  | $O(n)$ |
| `InsertBefore` | $O(n)$ |
| `RemoveFirst`  | $O(1)$ |
|  `RemoveLast`  | $O(1)$ |
|    `Remove`    | $O(n)$ |
|     `Find`     | $O(n)$ |
|    `Clear`     | $O(1)$ |
```

Si bien `InsertBefore` y `RemoveLast` mejoran respecto de la lista simple, las operaciones que requieren buscar un elemento (`Find`, `InsertAfter`, `InsertBefore`, `Remove`) siguen siendo $O(n)$ porque necesitan recorrer la lista.

## Lista Enlazada Circular

```{admonition} Definición
---
class: hint
---
Una lista enlazada circular es una estructura de datos donde el último nodo se enlaza al primero, formando un ciclo. Puede implementarse con enlaces simples o dobles.

En una lista circular doble, el sucesor del último nodo es el primero, y el predecesor del primero es el último. Esto permite recorridos continuos sin necesidad de un marcador de fin.
```

En una lista circular el último nodo se enlaza al primero, formando un ciclo. Se utiliza para modelar colas, gestión de procesos de un sistema operativo y juegos, entre otras aplicaciones. Las listas circulares se pueden implementar con enlaces simples o dobles.

```{figure} ../_static/figures/ListaEnlazadaCircularDoble_light.svg
---
width: 100%
class: only-light-mode
name: lista-circular-doble
---
Lista Enlazada Circular Doble
```

```{figure} ../_static/figures/ListaEnlazadaCircularDoble_dark.svg
---
width: 100%
class: only-dark-mode
name: lista-circular-doble
---
Lista Enlazada Circular Doble
```

Al ser cíclica, basta con mantener un puntero a la cabeza; la cola se obtiene como el predecesor de la cabeza.

### Eliminación del primer elemento

RemoveFirst en una lista circular doble requiere actualizar la cabeza y mantener el ciclo entre el nuevo primer nodo y el último.

```{figure} ../_static/figures/ListaEnlazadaCircularEliminacionFirst_light.svg
---
width: 100%
class: only-light-mode
name: cdll-remove-first
---
Eliminación del primer elemento en una Lista Circular Doble
```

```{figure} ../_static/figures/ListaEnlazadaCircularEliminacionFirst_dark.svg
---
width: 100%
class: only-dark-mode
name: cdll-remove-first
---
Eliminación del primer elemento en una Lista Circular Doble
```

```{code-block}
---
linenos: true
---
RemoveFirst():
    si IsEmpty():
        retornar false
    si size == 1:
        head = nulo
    sino:
        cola := head.prev
        head = head.siguiente
        head.prev = cola
        cola.siguiente = head
    tamaño--
    retornar true
```

## Implementaciones con Centinelas

```{admonition} Definición
---
class: hint
---
Los centinelas son nodos ficticios que se colocan al principio y al final de la lista. No contienen datos útiles y su propósito es eliminar los casos especiales en las operaciones de inserción y eliminación.

En una lista con centinelas:

- La cabeza real es el sucesor del centinela inicial.
- La cola real es el predecesor del centinela final.
- Una lista vacía tiene los dos centinelas apuntándose entre sí.
```

Los centinelas son nodos ficticios que no contienen datos y se agregan al principio y al final de la lista. Su propósito es estandarizar las operaciones eliminando los casos especiales de lista vacía, cabeza y cola.

```{figure} ../_static/figures/ListaConCentinelas_light.svg
---
width: 100%
class: only-light-mode
name: lista-centinelas
---
Lista Enlazada Doble con Centinelas
```

```{figure} ../_static/figures/ListaConCentinelas_dark.svg
---
width: 100%
class: only-dark-mode
name: lista-centinelas
---
Lista Enlazada Doble con Centinelas
```

En una lista vacía con centinelas, los dos nodos ficticios se apuntan entre sí:

```{figure} ../_static/figures/ListaVaciaCentinelas_light.svg
---
width: 100%
class: only-light-mode
name: lista-vacia-centinelas
---
Lista Vacía con Centinelas
```

```{figure} ../_static/figures/ListaVaciaCentinelas_dark.svg
---
width: 100%
class: only-dark-mode
name: lista-vacia-centinelas
---
Lista Vacía con Centinelas
```

### Remove con centinelas

Al tener centinelas, `Remove` no necesita verificar si el nodo a eliminar es la cabeza o la cola. La presencia de los nodos ficticios garantiza que siempre hay un nodo anterior y un nodo siguiente.

```{code-block}
---
linenos: true
---
Remove(buscado):
    actual := Find(buscado)
    si actual != nulo:
        actual.prev.siguiente = actual.siguiente
        actual.siguiente.prev = actual.prev
        tamaño--
        retornar true
    retornar false
```

### Clear con centinelas

Clear solo debe re-enlazar los centinelas entre sí, sin necesidad de liberar cada nodo.

```{code-block}
---
linenos: true
---
Clear():
    head.siguiente = tail
    tail.prev = head
    tamaño = 0
```

Esta técnica simplifica el código porque operaciones como `InsertBefore` o `Remove` ya no necesitan verificar si el nodo es la cabeza o la cola: los centinelas garantizan que siempre hay un nodo anterior y un nodo siguiente.

## Cuándo usar cada tipo

| Criterio | Simple | Doble | Circular | Centinelas |
|----------|--------|-------|----------|------------|
| Memoria por nodo | 1 puntero | 2 punteros | 1 o 2 punteros | 2 + 2 nodos fijos |
| Recorrido | solo hacia adelante | ambas direcciones | continuo | ambas direcciones |
| `RemoveLast` eficiente | no | sí | depende | sí |
| `InsertBefore` eficiente | no | sí | sí (doble) | sí |
| Código sin casos borde | no | no | no | sí |
| Ideal para | memoria limitada, solo forward | navegación bidireccional | rondas, turnos, playlists | implementar Stack/Queue |

## Ejercicios

Los ejercicios de este capítulo están en `03-listas/ejercicios/` del repositorio [taller-tad](https://github.com/untref-ayp2/taller-tad).

[▶ Animación: Find interactivo (abrir en nueva pestaña)](../_static/figures/ListaEnlazadaSimpleFind_anim_light.svg){.only-light-mode target=_blank}

[▶ Animación: Find interactivo (abrir en nueva pestaña)](../_static/figures/ListaEnlazadaSimpleFind_anim_dark.svg){.only-dark-mode target=_blank}
