---
label: abb
---

# Árboles Binarios de Búsqueda

```{admonition} Definición de Árbol Binario de Búsqueda
---
class: hint
---
Un árbol binario de búsqueda es un árbol binario que cumple con las siguientes propiedades para cada nodo N:

- Todos los nodos en el subárbol izquierdo de N tienen valores menores que el valor de N.
- Todos los nodos en el subárbol derecho de N tienen valores mayores que el valor de N.
- Ambos subárboles (izquierdo y derecho) deben ser también árboles binarios de búsqueda.
```

En la siguiente figura se muestran dos árboles binarios. El de la izquierda es un ABB válido: su raíz es (7), el hijo izquierdo es (3) y el derecho es (9). A su vez, (3) tiene como hijos a (2) y (5), mientras que (9) tiene a (8) y (10). En todos los nodos se cumple que los valores del subárbol izquierdo son menores que la raíz y los del derecho son mayores.

El árbol de la derecha, en cambio, no es un ABB. Su raíz también es (7), con subárbol izquierdo de raíz (2) y subárbol derecho de raíz (9). El subárbol con raíz (2) tiene como hijos a (1) y (8), y el de raíz (9) tiene a (10) como hijo derecho. Si bien los subárboles izquierdo (con raíz 2) y derecho (con raíz 9) son ABB válidos, el árbol completo no lo es: el nodo (8) —marcado en rojo— está en el subárbol izquierdo de la raíz (7) pero (8) es mayor que (7), violando la propiedad fundamental del ABB.

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABB_light.svg
---
name: abb
class: only-light-mode
---
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABB_dark.svg
---
class: only-dark-mode
---
```

El recorrido inorden de un árbol binario de búsqueda produce una secuencia ordenada de los valores almacenados en el árbol. Esto se debe a que, al visitar el subárbol izquierdo, el nodo raíz y luego el subárbol derecho, se garantiza que los nodos se procesen en orden ascendente.

Por ejemplo, en la siguiente figura se muestran dos árboles binarios de búsqueda que tienen el mismo recorrido inorden: 1, 2, 3, 5, 7, 9. Los árboles son diferentes porque los elementos se insertaron en diferente orden; sin embargo, al ser un ABB, el recorrido inorden es el mismo.

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBInorden_light.svg
---
name: abbinorden
class: only-light-mode
---
Dos árboles binarios de búsqueda con el mismo recorrido inorden
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBInorden_dark.svg
---
class: only-dark-mode
---
Dos árboles binarios de búsqueda con el mismo recorrido inorden
```

## Operaciones en un árbol binario de búsqueda

Las operaciones más comunes en un árbol binario de búsqueda son:

- **Inserción**: Agregar un nuevo nodo al árbol manteniendo la propiedad de ABB.
- **Búsqueda**: Encontrar un nodo en el árbol.
- **Eliminación**: Quitar un nodo del árbol manteniendo la propiedad de ABB.

### Inserción

La inserción en un árbol binario de búsqueda se realiza de manera recursiva. Se compara el valor a insertar con el valor del nodo actual y se decide si ir al subárbol izquierdo o derecho. Si el subárbol correspondiente está vacío, se inserta el nuevo nodo.

Para insertar un nuevo nodo en un árbol binario de búsqueda, se sigue el siguiente algoritmo:

```{code-block}
---
caption: Algoritmo de inserción en un árbol binario de búsqueda
linenos: true
language: text
---
FUNCION InsertarABB(raiz, valor)
    SI raiz ES nula ENTONCES
        raiz ← CrearNodo(valor)
    SINO SI valor < raiz.valor ENTONCES
        raiz.izquierdo ← InsertarABB(raiz.izquierdo, valor)
    SINO SI valor > raiz.valor ENTONCES
        raiz.derecho ← InsertarABB(raiz.derecho, valor)
    FIN SI
    RETORNAR raiz
FIN FUNCION
```

1. Se compara el valor a insertar con la raíz. Si es menor se desciende al subárbol izquierdo; si es mayor, al derecho.
2. Se repite el proceso recursivamente hasta encontrar un subárbol vacío donde insertar el nuevo nodo.
3. Una vez encontrada la posición, se inserta el nodo como hoja del árbol.

```{admonition} Importante
---
class: important
---
La inserción no permite valores duplicados. Si se requiere contar los elementos repetidos en el árbol, se puede modificar el algoritmo para que en lugar de insertar un nuevo nodo, se incremente un contador en el nodo existente.

La inserción de un nuevo nodo siempre se realiza en una hoja del árbol, es decir, un nodo que no tiene hijos. Esto asegura que la estructura del árbol se mantenga y que la propiedad de ABB se respete.
```

### Búsqueda

La búsqueda en un árbol binario de búsqueda también se realiza de manera recursiva. Se compara el valor buscado con el valor del nodo actual y se decide si ir al subárbol izquierdo o derecho. Si el valor es igual al del nodo actual, se ha encontrado el nodo, si en cambio se llega a un nodo nulo, el valor no está en el árbol.

```{code-block}
---
caption: Algoritmo de búsqueda en un árbol binario de búsqueda
linenos: true
language: text
---
FUNCION BuscarABB(raiz, valor)
    SI raiz ES nula ENTONCES
        RETORNAR nula
    SINO SI raiz.valor = valor ENTONCES
        RETORNAR raiz
    SINO SI valor < raiz.valor ENTONCES
        RETORNAR BuscarABB(raiz.izquierdo, valor)
    SINO
        RETORNAR BuscarABB(raiz.derecho, valor)
    FIN SI
FIN FUNCION
```

### Eliminación

La eliminación de un nodo en un árbol binario de búsqueda es un poco más compleja que la inserción y la búsqueda. Existen tres casos a considerar:

El nodo a eliminar es una hoja (no tiene hijos)
: En este caso, simplemente se elimina el nodo. En el ejemplo se elimina la hoja (6).

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBEliminacion-1_light.svg
---
class: only-light-mode
name: eliminacion1
width: 50%
---
Eliminación de un nodo hoja
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBEliminacion-1_dark.svg
---
class: only-dark-mode
width: 50%
---
Eliminación de un nodo hoja
```

El nodo a eliminar tiene un solo hijo
: En este caso, se reemplaza el nodo a eliminar por su hijo. Esto se hace actualizando el puntero del padre del nodo a eliminar para que apunte al hijo del nodo a eliminar. En el ejemplo se elimina el nodo (5) que tiene sólo un hijo izquierdo (3) y se reemplaza por su hijo.

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBEliminacion-2_light.svg
---
class: only-light-mode
name: eliminacion2
width: 80%
---
Eliminación de un nodo con un solo hijo
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBEliminacion-2_dark.svg
---
class: only-dark-mode
width: 80%
---
Eliminación de un nodo con un solo hijo
```

El nodo a eliminar tiene dos hijos
: En este caso, se busca el nodo más pequeño en el subárbol derecho del nodo a eliminar (sucesor) o el nodo más grande en el subárbol izquierdo (predecesor). Luego, se reemplaza el valor del nodo a eliminar por el valor del sucesor o predecesor y se elimina el sucesor o predecesor (que siempre va a ser una hoja o a lo sumo va a tener un solo hijo).

En la siguiente figura se observa la eliminación de la raíz del árbol, el nodo (7).

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBEliminacion-3_light.svg
---
class: only-light-mode
name: eliminacion3
width: 80%
---
Eliminación de un nodo con dos hijos
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBEliminacion-3_dark.svg
---
class: only-dark-mode
width: 80%
---
Eliminación de un nodo con dos hijos
```

Para ubicar al predecesor (es decir, el mayor elemento del subárbol izquierdo), se debe bajar al subárbol izquierdo y luego seguir bajando por las ramas derechas hasta llegar a un nodo que no tenga hijo derecho. En este caso el predecesor es (6).

En cambio, para ubicar al sucesor (es decir, el menor elemento del subárbol derecho), se debe bajar al subárbol derecho y luego seguir bajando por las ramas izquierdas hasta llegar a un nodo que no tenga hijo izquierdo. En este caso el sucesor es (9).

En el ejemplo se eligió reemplazar la raíz con el predecesor y eliminar el nodo (6).

```{admonition} Importante
---
class: important
---
Cuando se elimina un nodo con dos hijos, el nodo no se elimina directamente, sino que se reemplaza por su predecesor o sucesor. Esto asegura mantener la estructura del ABB.
```

A continuación se presenta el algoritmo de eliminación de un nodo en un árbol binario de búsqueda:

```{code-block}
---
caption: Algoritmo de eliminación en un árbol binario de búsqueda
linenos: true
language: text
---
FUNCION EliminarABB(raiz, valor)
    SI raiz ES nula ENTONCES
        RETORNAR nula
    // Buscar el nodo a eliminar
    SINO SI valor < raiz.valor ENTONCES
        raiz.izquierdo ← EliminarABB(raiz.izquierdo, valor)
    SINO SI valor > raiz.valor ENTONCES
        raiz.derecho ← EliminarABB(raiz.derecho, valor)
    SINO // Nodo encontrado
        // Caso 1: Nodo a eliminar es una hoja
        SI raiz.izquierdo ES nula Y raiz.derecho ES nula ENTONCES
            RETORNAR nula
        // Caso 2: Nodo a eliminar tiene un solo hijo
        SINO SI raiz.izquierdo ES nula ENTONCES
            RETORNAR raiz.derecho
        SINO SI raiz.derecho ES nula ENTONCES
            RETORNAR raiz.izquierdo
        // Caso 3: Nodo a eliminar tiene dos hijos
        SINO
            predecesor ← BuscarMaximo(raiz.izquierdo) // busca el mayor del subárbol izquierdo
            raiz.valor ← predecesor.valor
            raiz.izquierdo ← EliminarABB(raiz.izquierdo, predecesor.valor) // elimina el predecesor
        FIN SI
    FIN SI
    RETORNAR raiz
FIN FUNCION
```

```{code-block}
---
caption: Algoritmo de búsqueda del nodo máximo en un árbol binario de búsqueda
linenos: true
language: text
---
FUNCION BuscarMaximo(raiz)
    SI raiz.derecho ES nula ENTONCES
        RETORNAR raiz
    SINO
        RETORNAR BuscarMaximo(raiz.derecho)
    FIN SI
FIN FUNCION
```

<div class="only-html">

### Árbol binario de búsqueda interactivo

Ingresá un valor y presioná Enter para ejecutar la operación seleccionada (insertar, buscar o eliminar). La animación avanza automáticamente paso a paso. Usá el control de velocidad para ajustar la rapidez de la animación.

<div class="only-light-mode">
<iframe src="/applets/3-estructuras-de-datos/3-9-abb/operaciones-abb_light.html" width="100%" height="520px"></iframe>
</div>
<div class="only-dark-mode">
<iframe src="/applets/3-estructuras-de-datos/3-9-abb/operaciones-abb_dark.html" width="100%" height="520px"></iframe>
</div>

</div>

### Orden de las operaciones

En un árbol binario de búsqueda, las operaciones de inserción, búsqueda y eliminación tienen un tiempo de ejecución que depende de la altura del árbol. Por lo tanto, es importante tratar de mantener el árbol equilibrado para que la altura no crezca demasiado.

Un árbol binario de búsqueda equilibrado tiene una altura aproximada de $O(log (n))$, donde $n$ es el número de nodos en el árbol. En este caso, las operaciones de inserción, búsqueda y eliminación tienen un tiempo de ejecución promedio de $O(log (n))$.

Formalmente la altura $h$ de un árbol binario de búsqueda se define como:

```{math}
h =
\begin{cases}
0 & \text{si solo tiene raíz} \\
1 + \max(h_{izq}, h_{der}) & \text{si tiene más de un nodo}
\end{cases}
```

En la siguiente figura se observa un árbol binario de búsqueda completo (con todos los nodos en todos los niveles) y perfectamente balanceado, donde cada nodo tiene dos hijos y la altura del árbol es mínima. En este caso, el árbol tiene una altura de 3 y contiene 15 nodos.

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBBalanceado_light.svg
---
class: only-light-mode
name: arbolbalanceado
---
Árbol binario de búsqueda equilibrado
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBBalanceado_dark.svg
---
class: only-dark-mode
---
Árbol binario de búsqueda equilibrado
```

La altura $h$ de un árbol binario completo y balanceado se puede calcular como:

```{math}
\begin{aligned}
&h = log_2 (n+1)-1 \\
&h = O(log(n))
\end{aligned}
```

Por otro lado, en el peor de los casos, un árbol binario de búsqueda puede degenerar en una lista enlazada, lo que resulta en una altura de $O(n)$ y un tiempo de ejecución de $O(n)$ para las operaciones. Esto ocurre cuando los nodos se insertan en orden ascendente o descendente, lo que provoca que el árbol se convierta en una estructura lineal. En la siguiente figura se observa un árbol binario que degeneró en una lista.

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBDegenerado_light.svg
---
class: only-light-mode
name: ABBDegenerado
width: 70%
---
Árbol binario de búsqueda degenerado
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-9-abb/ABBDegenerado_dark.svg
---
class: only-dark-mode
width: 70%
---
Árbol binario de búsqueda degenerado
```

La altura $h$ de un árbol binario degenerado en una lista se puede calcular como:

```{math}
\begin{aligned}
&h = n-1 \\
&h = O(n)
\end{aligned}
```

## Implementación de un árbol binario de búsqueda

Existen dos enfoques principales para implementar un ABB: construir la estructura desde cero, definiendo explícitamente los nodos, o aprovechar una implementación de árbol binario genérica existente mediante composición. A continuación se analizan ambas alternativas.

En los ejemplos se utiliza una función de comparación `func(T, T) int` que permite trabajar con cualquier tipo de dato, sin restringir a `cmp.Ordered`. Esta función debe devolver un valor negativo si el primer argumento es menor, cero si son iguales, y positivo si es mayor.

```{admonition} Nota
---
class: note
---
La función de comparación sigue la misma convención que `cmp.Compare` de la biblioteca estándar. Para tipos nativos como `int` o `string` puede usarse directamente `cmp.Compare[T]`.
```

### Implementación desde cero

Este enfoque consiste en definir un nodo binario que contenga el valor, el hijo izquierdo y el hijo derecho, y luego construir el ABB alrededor de ese nodo. Es la implementación más directa y no depende de ninguna otra estructura.

```{code-block} go
---
linenos: true
---
package binarysearchtree

// BinaryNode representa un nodo del árbol binario de búsqueda.
type BinaryNode[T any] struct {
    Value T
    Left  *BinaryNode[T]
    Right *BinaryNode[T]
}
```

```{code-block} go
---
linenos: true
---
package binarysearchtree

// BinarySearchTree representa un árbol binario de búsqueda.
type BinarySearchTree[T any] struct {
    Root *BinaryNode[T]
    cmp  func(T, T) int
}

// NewBinarySearchTree crea un ABB vacío con la función de comparación dada.
func NewBinarySearchTree[T any](cmp func(T, T) int) *BinarySearchTree[T] {
    return &BinarySearchTree[T]{cmp: cmp}
}
```

El árbol posee una raíz que apunta al primer nodo. Las operaciones de inserción, búsqueda y eliminación se implementan como métodos recursivos que navegan por los nodos comparando valores. La lógica de ordenamiento está intrínsecamente ligada a la estructura del nodo.

**Ventajas:**

- Control total sobre la representación interna de los datos.
- Sin dependencias externas.
- Ideal para aprendizaje y comprensión del algoritmo.

**Desventajas:**

- Duplica lógica estructural que podría reutilizarse (recorridos, altura, etc.).
- Acopla la validación de la propiedad de orden con la estructura del árbol.
- Menor abstracción: cualquier cambio en la estructura del nodo impacta directamente en las operaciones del ABB.

#### Delegación de operaciones

En la implementación anterior las operaciones se manejan desde el árbol (`bst.Insert`, `bst.Search`, etc.), que delega en métodos privados recursivos. Una alternativa es delegar la lógica en los propios nodos:

```{code-block} go
---
linenos: true
---
func (n *BinaryNode[T]) Insert(value T, cmp func(T, T) int) *BinaryNode[T] {
    if n == nil {
        return &BinaryNode[T]{Value: value}
    }
    if cmp(value, n.Value) < 0 {
        n.Left = n.Left.Insert(value, cmp)
    } else if cmp(value, n.Value) > 0 {
        n.Right = n.Right.Insert(value, cmp)
    }
    return n
}
```

Delegar en los nodos hace que el árbol actúe solo como un envoltorio (`bst.Root = bst.Root.Insert(value, bst.cmp)`). La función de comparación se pasa como parámetro para que el nodo pueda decidir hacia dónde navegar. Esto acerca la implementación al paradigma de objetos donde cada nodo es responsable de su propia manipulación, pero puede dificultar el control de errores y la trazabilidad.

### Implementación por composición

El segundo enfoque consiste en construir el ABB a partir de una implementación genérica de árbol binario existente, como la que se encuentra en el paquete `tree` del repositorio `data-structures`. La idea es que el ABB **contenga** un árbol binario y le agregue la semántica de orden.

```{code-block} go
---
linenos: true
---
package binarysearchtree

import "github.com/untref-ayp2/data-structures/tree"

// BinarySearchTree representa un árbol binario de búsqueda
// construido sobre un árbol binario genérico.
type BinarySearchTree[T any] struct {
    binaryTree *tree.BinaryTree[T]
    cmp        func(T, T) int
}

// NewBinarySearchTree crea un ABB vacío con la función de comparación dada.
func NewBinarySearchTree[T any](cmp func(T, T) int) *BinarySearchTree[T] {
    return &BinarySearchTree[T]{
        binaryTree: tree.NewBinaryTree[T](),
        cmp:        cmp,
    }
}
```

En esta variante, el árbol binario subyacente provee las operaciones estructurales (insertar nodo, recorrer, calcular altura), mientras que el ABB se encarga únicamente de **dónde** insertar según el orden de los valores. La lógica de recorridos se hereda del árbol binario y no necesita reimplementarse.

**Ventajas:**

- Reutilización de código: los recorridos y la gestión estructural del árbol binario ya están implementados.
- Separación de responsabilidades: el árbol binario maneja *cómo* se almacenan los nodos; el ABB maneja *dónde* van según el orden.
- Menor cantidad de código que mantener y testear.
- Mayor abstracción: si cambia la implementación interna del árbol binario, el ABB no se ve afectado.

**Desventajas:**

- Dependencia de una biblioteca externa.
- Menor control sobre la representación interna.
- Curva de aprendizaje adicional si no se conoce la API del árbol binario subyacente.
- Puede introducir overhead si la interfaz genérica no se ajusta perfectamente a las necesidades del ABB.

### Comparación

| Aspecto              | Desde cero                          | Por composición                                        |
| -------------------- | ----------------------------------- | ------------------------------------------------------ |
| Dependencias         | Ninguna                             | `data-structures/tree`                                 |
| Control interno      | Total                               | Limitado por la API del árbol genérico                 |
| Cantidad de código   | Mayor                               | Menor                                                  |
| Reutilización        | Baja                                | Alta (recorridos, altura, etc.)                        |
| Curva de aprendizaje | Directa                             | Requiere conocer la API del árbol binario              |
| Acoplamiento         | Fuerte entre nodo y ABB             | Débil: el ABB solo añade semántica de orden            |
| Mantenimiento        | Mayor (cada cambio impacta en todo) | Menor (los cambios se encapsulan en el árbol genérico) |
| Flexibilidad         | Máxima                              | Limitada por la interfaz del árbol genérico            |
| Ideal para           | Aprendizaje y experimentación       | Proyectos que priorizan la reutilización               |

## Ejercicios

1. **Implementar ABB por composición** — Completar el esqueleto de `BinarySearchTree[T]` en el repositorio
   [`data-structures`](https://github.com/untref-ayp2/data-structures),
   paquete `binarysearchtree/`. La implementación debe componer un `tree.BinaryTree[T]`
   existente y agregar la semántica de orden. El ABB debe implementar inserción, búsqueda,
   eliminación y reutilizar los recorridos y altura del árbol binario subyacente.

2. **Resolver los ejercicios de aplicación** — Los ejercicios de este capítulo están en
   [`09-abb/ejercicios/`](https://github.com/untref-ayp2/taller-tad/tree/main/09-abb/ejercicios)
   del repositorio [`taller-tad`](https://github.com/untref-ayp2/taller-tad).
