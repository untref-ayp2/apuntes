---
label: conjuntos
---

# Conjuntos

Los conjuntos son estructuras de datos que permiten almacenar elementos de forma
**desordenada** y **sin repetición**. Son similares a los conjuntos matemáticos:
dos conjuntos son iguales si tienen los mismos elementos, sin importar el orden
en que se encuentren.

```{figure} ../_static/figures/3-estructuras-de-datos/3-6-conjuntos/diagrama-venn_light.svg
---
class: only-light-mode
---
Diagrama de Venn: dos conjuntos con intersección no vacía
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-6-conjuntos/diagrama-venn_dark.svg
---
class: only-dark-mode
---
Diagrama de Venn: dos conjuntos con intersección no vacía
```

Las operaciones básicas que se pueden realizar con conjuntos se dividen en dos
categorías: operaciones sobre los elementos y operaciones entre conjuntos.

## Operaciones sobre los elementos

`Contains(e T) bool`
: Verifica si el elemento `e` pertenece al conjunto. Debe ser $O(1)$ promedio.

`Add(e T)`
: Agrega el elemento `e` al conjunto. Si ya existe, no tiene efecto. Debe ser
$O(1)$ promedio.

`Remove(e T)`
: Elimina el elemento `e` del conjunto. Si no existe, no tiene efecto. Debe ser
$O(1)$ promedio.

`Size() int`
: Devuelve la cantidad de elementos del conjunto. Debe ser $O(1)$.

`Values() []T`
: Devuelve un slice con todos los elementos del conjunto, sin un orden definido.
Debe ser $O(n)$.

`String() string`
: Devuelve una representación textual del conjunto, por ejemplo `{1, 2, 3}`.
Debe ser $O(n)$.

## Operaciones entre conjuntos

`Union(other Set[T]) Set[T]`
: Devuelve un nuevo conjunto con los elementos de ambos conjuntos. Debe ser
$O(n + m)$.

`Intersection(other Set[T]) Set[T]`
: Devuelve un nuevo conjunto con los elementos comunes a ambos conjuntos. Debe
ser $O(\min(n, m))$.

`Difference(other Set[T]) Set[T]`
: Devuelve un nuevo conjunto con los elementos que están en el receptor pero no
en `other`. Debe ser $O(n)$.

`SymmetricDifference(other Set[T]) Set[T]`
: Devuelve un nuevo conjunto con los elementos que están en uno de los conjuntos
pero no en ambos. Debe ser $O(n + m)$.

`Subset(other Set[T]) bool`
: Verifica si el receptor es subconjunto de `other`. Debe ser $O(n)$.

`Superset(other Set[T]) bool`
: Verifica si el receptor es superconjunto de `other`, es decir, si `other` es
subconjunto del receptor. Debe ser $O(m)$.

## Interfaz

Todas estas operaciones definen la interfaz del TAD Conjunto:

```{code-block} go
---
linenos:
---
type Set[T comparable] interface {
    // Operaciones sobre elementos
    Contains(element T) bool
    Add(element T)
    Remove(element T)
    Size() int
    Values() []T
    String() string

    // Operaciones entre conjuntos
    Union(other Set[T]) Set[T]
    Intersection(other Set[T]) Set[T]
    Difference(other Set[T]) Set[T]
    SymmetricDifference(other Set[T]) Set[T]
    Subset(other Set[T]) bool
    Superset(other Set[T]) bool
}
```

## Estrategias de implementación

No existe un tipo nativo `Set` en Go, pero existen varias formas de
implementarlo. La elección depende del balance entre eficiencia y simplicidad.

### Sobre `map[T]struct{}`

La forma más directa es usar un `map` nativo de Go con valores de tipo
`struct{}`. Como las claves del mapa son únicas y `struct{}` no ocupa memoria
adicional (es un tipo de tamaño cero), esta combinación es el *idiom*
recomendado en Go para representar conjuntos:

```{code-block} go
---
linenos:
---
type setMap[T comparable] struct {
    elements map[T]struct{}
}
```

Las operaciones básicas se traducen naturalmente:

- **Agregar**: `s.elements[elem] = struct{}{}`
- **Pertenencia**: `_, ok := s.elements[elem]`
- **Eliminar**: `delete(s.elements, elem)`
- **Cantidad**: `len(s.elements)`

Todas estas operaciones son $O(1)$ promedio gracias a la tabla de *hash* interna
de `map`. Las operaciones que recorren todos los elementos (`Values`, `String`,
`Union`, etc.) son $O(n)$.

Esta implementación es la más simple y eficiente para la mayoría de los casos,
pero tiene una limitación: el tipo `T` debe ser `comparable` (como exige Go
para las claves de un mapa).

### Sobre una tabla de *hash*

Un conjunto puede verse como una tabla de *hash* donde solo importan las claves
y el valor asociado es irrelevante. El repositorio
[`data-structures`](https://github.com/untref-ayp2/data-structures) provee una
implementación genérica de `HashTable[K comparable, V any]` que puede usarse
como base:

```{code-block} go
---
linenos:
---
type setHash[T comparable] struct {
    table hashtable.HashTable[T, struct{}]
}
```

El comportamiento es análogo al de `map[T]struct{}` con la misma complejidad
$O(1)$ promedio para las operaciones básicas. La ventaja es que al implementar
la tabla de *hash* uno controla la función de *hash*, la política de colisiones y
el redimensionamiento, lo que permite adaptar el comportamiento a necesidades
específicas.

### Otras alternativas

También es posible implementar un conjunto sobre un arreglo dinámico (*slice*)
o sobre una lista enlazada. En estos casos las operaciones de búsqueda pasan a
ser $O(n)$, lo que hace que `Contains`, `Add` (que debe verificar si el
elemento ya existe) y `Remove` sean lineales. Solo conviene usarlas para
conjuntos muy pequeños o cuando la eficiencia no es crítica.

## Conjuntos ordenados

Un conjunto ordenado es una variante del TAD Conjunto que, además de no
permitir duplicados, mantiene los elementos organizados según un criterio de
orden. Esto habilita operaciones que la versión con _hash_ no puede realizar
de forma eficiente.

### Para qué se usan

Los conjuntos ordenados son útiles cuando se necesita:

- **Obtener el mínimo o el máximo** elemento del conjunto.
- **Recorrer los elementos en orden** ascendente o descendente.
- **Buscar por rango**, por ejemplo obtener todos los elementos entre dos
  valores dados.
- **Combinar conjuntos ordenados** mediante un _merge_ en tiempo $O(n + m)$,
  más eficiente que la alternativa con tablas de _hash_.

Algunos ejemplos concretos: mantener una lista de palabras en orden
alfabético, un ranking de puntajes ordenados, o un calendario de eventos
donde se necesita consultar el próximo evento después de una fecha dada.

### Estrategias de implementación

**Lista enlazada ordenada**: es la implementación más sencilla. La lista se
mantiene ordenada en todo momento: al agregar un elemento se recorre hasta
encontrar la posición correcta según el criterio de orden. Esto hace que
`Add`, `Remove` y `Contains` sean $O(n)$, ya que en el peor caso hay que
recorrer toda la lista. La `List` del repositorio `data-structures` puede
usarse como base.

**Arreglo ordenado (_slice_)**: los elementos se mantienen en un slice
ordenado. `Contains` puede usar búsqueda binaria ($O(\log n)$), pero
`Add` y `Remove` requieren desplazar elementos ($O(n)$). Es adecuado
cuando el conjunto es mayormente estático (muchas consultas, pocas
modificaciones).

**Árbol binario de búsqueda balanceado**: es la opción más eficiente pero
también la más compleja. Un árbol AVL (que se estudia en el capítulo
{ref}`arboles-balanceados`) mantiene los elementos ordenados y ofrece
$O(\log n)$ en inserción, eliminación y búsqueda.

### Orden de las operaciones

La siguiente tabla compara las complejidades del conjunto ordenado según
la estructura subyacente. Se incluye también el conjunto con _hash_ como
referencia:

| Operación      | Conjunto con _hash_ | Lista enlazada | Slice ordenado | Árbol AVL   |
| -------------- | ------------------- | -------------- | -------------- | ----------- |
| `Add`          | $O(1)$ prom.        | $O(n)$         | $O(n)$         | $O(\log n)$ |
| `Remove`       | $O(1)$ prom.        | $O(n)$         | $O(n)$         | $O(\log n)$ |
| `Contains`     | $O(1)$ prom.        | $O(n)$         | $O(\log n)$    | $O(\log n)$ |
| `Size`         | $O(1)$              | $O(1)$         | $O(1)$         | $O(1)$      |
| `Values`       | $O(n)$              | $O(n)$         | $O(n)$         | $O(n)$      |
| `Union`        | $O(n + m)$          | $O(n + m)$     | $O(n + m)$     | $O(n + m)$  |
| `Intersection` | $O(\min(n, m))$     | $O(n + m)$     | $O(n + m)$     | $O(n + m)$  |

Las operaciones binarias (`Union`, `Intersection`, etc.) se benefician del
orden: pueden resolverse recorriendo ambas estructuras en simultáneo
(_merge_), lo que da $O(n + m)$ independientemente de la implementación
interna. En el conjunto con _hash_, en cambio, `Intersection` puede
aprovechar la búsqueda $O(1)$ del conjunto más chico para lograr
$O(\min(n, m))$.

La elección de la estructura depende del uso. Para los ejercicios de este
capítulo se trabajará con listas enlazadas, que son la opción más simple
de implementar y permiten concentrarse en la lógica de las operaciones
entre conjuntos ordenados.

### Implementación con listas enlazadas

Para que la lista se mantenga ordenada es necesario poder comparar
elementos. En Go, los tipos nativos ordenados (enteros, flotantes,
strings) pueden usar el constraint `cmp.Ordered` (disponible desde
Go 1.21):

```{code-block} go
---
linenos:
---
import "cmp"

type SortedSetList[T cmp.Ordered] struct {
    list list.LinkedList[T]
}
```

Para tipos que no implementan `cmp.Ordered` se pasa una función de
comparación:

```{code-block} go
---
linenos:
---
type SortedSetListFunc[T any] struct {
    list list.LinkedList[T]
    less func(a, b T) bool
}
```

```{admonition} Invariante de representación
---
class: hint
---
Como se vio en el capítulo {ref}`tad`, todo TAD debe cumplir un **invariante
de representación**. En el `SortedSetList` el invariante tiene dos partes:

1. La lista interna está **ordenada** según el criterio definido por la
   función `less`.
2. La lista **no contiene elementos repetidos**.

Ambas condiciones deben cumplirse siempre, antes y después de cada operación,
y son responsabilidad de las primitivas del TAD mantenerlas.
```

**`Add`**: recorre la lista hasta encontrar la posición donde el nuevo
elemento es menor o igual al actual. Si ya existe un elemento igual, no
se agrega. Si se llega al final, se agrega al final.

**`Contains`**: recorre la lista comparando cada elemento. Si se pasa
de la posición donde debería estar (el elemento actual es mayor que el
buscado), se puede detener la búsqueda: el elemento no está.

**`Remove`**: recorre la lista hasta encontrar el elemento y lo elimina.

**`Union`**: recorre ambas listas en simultáneo. En cada paso se toma
el menor de los dos elementos actuales, se agrega al resultado y se
avanza en la lista correspondiente. Si son iguales, se agrega uno solo
y se avanza en ambas.

**`Intersection`**: similar al _merge_ pero solo se agregan los
elementos que aparecen en ambas listas.

**`Difference`**: recorre ambas listas; los elementos que están en la
primera pero no en la segunda se agregan al resultado.

Este patrón de _merge_ es posible únicamente cuando ambas colecciones
están ordenadas, y es la razón principal por la que los conjuntos
ordenados son útiles.

## Ejercicios

Los ejercicios de este capítulo están en `06-conjuntos/ejercicios/` del
repositorio [taller-tad](https://github.com/untref-ayp2/taller-tad).

Antes de comenzar, implementá las interfaces necesarias en tu fork de
[data-structures](https://github.com/untref-ayp2/data-structures).
