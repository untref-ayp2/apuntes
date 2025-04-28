---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Conjuntos

Los conjuntos son estructuras de datos que permiten almacenar elementos de forma **desordenada** y **sin repetición**. Son similares a los conjuntos matemáticos. Los conjuntos se pueden comparar, por igual o distinto.

Por definición dos conjuntos son iguales si tienen los mismos elementos, sin importar el orden en que se encuentren. Por otro lado, dos conjuntos son distintos si tienen al menos un elemento diferente.

```{figure} ../assets/images/conjuntos/diagrama-venn.drawio.svg
---
name: Conjuntos
class: dark-light
---
Conjuntos
```

Las operaciones básicas que se pueden realizar con conjuntos se pueden dividir en dos categorías: operaciones sobre los elementos y operaciones entre conjuntos.

## Operaciones sobre los elementos

`Contains`
: Verificar si un elemento está en el conjunto.

`Add`
: Agregar un elemento al conjunto.

`Remove`
: Eliminar un elemento del conjunto.

`Size`
: Obtener el número de elementos del conjunto.

`Values`
: Obtener los elementos del conjunto.

## Operaciones entre conjuntos

`Union`
: Crear un nuevo conjunto con los elementos de dos conjuntos.

`Intersection`
: Crear un nuevo conjunto con los elementos comunes de dos conjuntos.

`Difference`
: Crear un nuevo conjunto con los elementos que están en el primer conjunto pero no en el segundo.

`Subset`
: Verificar si un conjunto es subconjunto de otro.

`SimeetricDifference`
: Crear un nuevo conjunto con los elementos que están en uno de los conjuntos pero no en ambos.

`Superset`
: Verificar si un conjunto es superconjunto de otro.

## Implementación

En Go no existe un tipo de dato nativo para conjuntos. Existen muchas formas de implementarlos, sobre arreglos, listas enlazadas, o mapas.

A modo de ejemplo se muestra una implementación sobre un mapa de tipo `map[int]bool` para representar un conjunto de enteros

```go
package main

import "fmt"

type Set struct {
    elements map[int]bool
}

func NewSet() *Set {
    return &Set{elements: make(map[int]bool)}
}

func (s *Set) Add(element int) {
    s.elements[element] = true
}

func (s *Set) Remove(element int) {
    delete(s.elements, element)
}

func (s *Set) Contains(element int) bool {
    return s.elements[element]
}

func (s *Set) Size() int {
    return len(s.elements)
}

func (s *Set) Values() []int {
    values := make([]int, 0, s.Size())
    for k := range s.elements {
        values = append(values, k)
    }
    return values
}

func main() {
    s := NewSet()
    s.Add(1)
    s.Add(2)
    s.Add(3)
    fmt.Println(s.Contains(2)) // true
    fmt.Println(s.Contains(4)) // false
    fmt.Println(s.Size())      // 3
    fmt.Println(s.Values())    // [1 2 3]
    s.Remove(2)
    fmt.Println(s.Contains(2)) // false
    fmt.Println(s.Size())      // 2
    fmt.Println(s.Values())    // [1 3]
}
```

## Orden de las operaciones

Las operaciones sobre conjuntos tienen un costo asociado. Por ejemplo, en la implementación anterior, las operaciones `Add`, `Remove` y `Contains` tienen un costo de tiempo constante $O(1)$. Por otro lado, las operaciones `Size` y `Values` tienen un costo de tiempo lineal $O(n)$. El orden de las operaciones depende de la implementación del conjunto.

## Ejercicios

1. Implementar la operaciones `Union`, `Intersection`, `Difference`, `Subset`, `SymmetricDifference` y `Superset` para el conjunto de enteros dado como ejemplo.
2. Implementar un conjunto genérico que permita almacenar cualquier tipo de dato.
3. Implementar un conjunto basado en arreglos (que no use maps ni tablas de hashing). Implementar tantos las operaciones sobre elementos como las operaciones entre conjuntos.
4. Implementar un conjunto basado en listas enlazadas. Implementar tantos las operaciones sobre elementos como las operaciones entre conjuntos.
5. Comparar el orden de las operaciones entre las implementaciones de arreglos y listas enlazadas.
