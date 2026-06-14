---
label: monticulo-binario
---

# Colas de Prioridad y Montículos Binarios

## Colas de Prioridad

Una cola de prioridad se comporta de forma similar a una cola, pero cada elemento que ingresa tiene asignada una prioridad y los elementos con mayor prioridad son los primeros en salir de la cola.

Si todos los elementos tienen la misma prioridad, la cola se comporta como una cola común, es decir, el primero que llega es el primero que sale de la cola.

Por ejemplo, si se tiene una cola de prioridad con los siguientes elementos y prioridades, y la posición en la tabla corresponde al orden de llegada de los elementos, es decir, se insertaron en orden alfabético y además suponemos que la prioridad 1 es la mayor, luego la 2 y así sucesivamente.

```{table} Cola de Prioridad
---
width: 40%
align: center
---
| Elemento | Prioridad |
| :------: | :-------: |
|    A     |     3     |
|    B     |     1     |
|    C     |     2     |
|    D     |     1     |
|    E     |     3     |
|    F     |     2     |
|    G     |     1     |
|    H     |     3     |
|    I     |     2     |

```

La cola de prioridad se comportará de la siguiente forma:

1. Se extrae el elemento B
2. Se extrae el elemento D
3. Se extrae el elemento G
4. Se extrae el elemento C
5. Se extrae el elemento F
6. Se extrae el elemento I
7. Se extrae el elemento A
8. Se extrae el elemento E
9. Se extrae el elemento H

En este ejemplo se puede observar que el orden de extracción combina la prioridad con el orden de llegada: a igual prioridad, los elementos se extraen en el mismo orden en que fueron insertados.

Las operaciones que definen una cola de prioridad son:

- `Enqueue`: agregar un nuevo elemento con una prioridad asociada.
- `Dequeue`: eliminar y devolver el elemento con mayor prioridad.
- `Peek`: obtener el elemento con mayor prioridad sin eliminarlo.
- `IsEmpty`: consultar si la cola está vacía.
- `Size`: obtener la cantidad de elementos.

### Interfaz

En Go, definimos una interfaz que capture este comportamiento:

```{code-block} go
---
linenos: true
---
type PriorityQueue[T any] interface {
	// Enqueue agrega un nuevo elemento a la cola.
	Enqueue(element T)
	// Dequeue elimina y devuelve el elemento con mayor prioridad.
	// Error si la cola está vacía.
	Dequeue() (T, error)
	// Peek devuelve el elemento con mayor prioridad sin eliminarlo.
	// Error si la cola está vacía.
	Peek() (T, error)
	// IsEmpty devuelve true si la cola no tiene elementos.
	IsEmpty() bool
	// Size devuelve la cantidad de elementos en la cola.
	Size() int
}
```

### Estrategia de comparación

Para determinar qué elemento tiene mayor prioridad, la cola necesita una forma de comparar elementos. Go no tiene una interfaz `Ordered` nativa como otros lenguajes, así que la estrategia habitual es pasar una **función de comparación** al constructor de la implementación.

La convención es usar una función del tipo `func(a, b T) int` que devuelva:

- un número **negativo** si `a` tiene prioridad sobre `b`,
- **cero** si son equivalentes,
- un número **positivo** si `b` tiene prioridad sobre `a`.

Por ejemplo, para enteros con orden ascendente (menor valor, mayor prioridad):

```go
compare := func(a, b int) int {
    return a - b
}
```

Para orden descendente (mayor valor, mayor prioridad):

```go
compare := func(a, b int) int {
    return b - a
}
```

Para un `struct` con un campo `edad`:

```go
compare := func(a, b Persona) int {
    return a.edad - b.edad
}
```

Esta misma estrategia se utiliza en la biblioteca estándar de Go (`sort.Slice` recibe una función `less` similar, y `container/heap` requiere implementar `Less`).

Para implementar una cola de prioridad se puede usar un **montículo binario**, ya que optimiza las operaciones de inserción y eliminación de los elementos.

## Montículos Binarios

Los montículos o _heaps_ en inglés son estructuras de datos que permiten acceder al elemento que se encuentra en la "cima" muy eficientemente. Esta posición privilegiada se utiliza para mantener el mayor elemento del montículo o el menor. En el caso de que se mantenga el mayor elemento en la cima se le llama **Montículo de Máximos** y si se mantiene el menor se le llama **Montículo de Mínimos**.

Existen diferentes tipos de montículos (binario, fibonacci, suave (_soft_), etc.), pero todos comparten la propiedad de que el elemento que se encuentra en la cima es el mayor o el menor de toda la estructura. En nuestro curso nos enfocaremos en los montículos binarios.

```{figure} ../_static/figures/3-estructuras-de-datos/3-11-monticulo-binario/heap-boxes_light.svg
---
width: 350px
name: piramide-de-cajas
class: only-light-mode
---
Pirámide de Cajas
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-11-monticulo-binario/heap-boxes_dark.svg
---
width: 350px
name: piramide-de-cajas
class: only-dark-mode
---
Pirámide de Cajas
```

Un **Montículo Binario** consiste en un árbol binario que cumple con dos propiedades fundamentales.

Propiedad de Forma
: Es un árbol binario **completo** (o casi completo) e **izquierdista**, es decir que se va llenando de izquierda a derecha. Lo que implica que todos los niveles del árbol están llenos, excepto el último nivel que puede estar incompleto.

Propiedad de Orden
: En un montículo de mínimos, cada nodo es menor que todos sus descendientes. Análogamente si es un montículo de máximos, cada nodo es mayor que todos sus descendientes. En otras palabras, en un montículo binario de mínimos, el menor elemento de toda la estructura se encuentra en la raíz y recursivamente podemos pensar a los hijos de la raíz como otros montículos de mínimos

En la siguiente figura se puede ver un heap de mínimos donde se cumplen ambas propiedades. El elemento $10$ es el menor de toda la estructura y se encuentra en la raíz. Análogamente el menor de sus descendientes por la izquierda es el elemento $20$ y se encuentra en la raíz del subárbol izquierdo y por el lado derecho el elemento $30$ es el menor del subárbol derecho.

```{figure} ../_static/figures/3-estructuras-de-datos/3-11-monticulo-binario/HeapMinimos_light.svg
---
class: only-light-mode
name: heap-de-minimos
---
Montículo Binario de Mínimos
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-11-monticulo-binario/HeapMinimos_dark.svg
---
class: only-dark-mode
name: heap-de-minimos
---
Montículo Binario de Mínimos
```

### Representación

Como un montículo binario es un árbol binario completo, o casi completo, podemos aprovechar esta propiedad y usar un arreglo para representarlo. Usar un arreglo para representar un árbol binario completo es una técnica muy común en computación y se conoce como **representación por niveles** y tiene ventajas en términos de espacio y tiempo y facilita la implementación de las operaciones.

```{note}
Cómo es un árbol **completo e izquierdista** entonces el arreglo que se usa como contenedor de datos tendrá elementos en todas sus posiciones, es decir, no habrá "huecos" y la raíz siempre se encontrará en la posición 0. Además con algunas cuentas simples se puede determinar donde están los hijos o el padre de cualquier nodo.
```

En la siguiente figura se observa como se puede usar un arreglo para mantener un montículo binario. La raíz se encuentra en la posición 0, el hijo izquierdo de la raíz en la posición 1, el hijo derecho de la raíz en la posición 2 y así sucesivamente.

```{figure} ../_static/figures/3-estructuras-de-datos/3-11-monticulo-binario/HeapMinimosRepresentacion_light.svg
---
width: 100%
name: heap-representacion
class: only-light-mode
---
Representación con arreglos de un Montículo Binario de Mínimos
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-11-monticulo-binario/HeapMinimosRepresentacion_dark.svg
---
width: 100%
name: heap-representacion
class: only-dark-mode
---
Representación con arreglos de un Montículo Binario de Mínimos
```

Con las siguientes fórmulas se puede calcular la posición en el arreglo de cualquier hijo o padre de un nodo dado.

```{card} Fórmulas
$\displaystyle H_{izq}(i) = 2 \; i + 1$

$\displaystyle H_{der}(i) = 2 \; i + 2$

$\displaystyle Padre(i) = \left\lfloor \frac{i-1}{2} \right\rfloor$

Donde el símbolo $\lfloor \; \rfloor$ indica el piso, es decir la parte entera del cociente.

+++

Las fórmulas pueden variar si la primera posición del arreglo es 1 en lugar de 0. ¿Cómo serían las fórmulas?
```

Por ejemplo en la posición 3 del arreglo se encuentra el elemento $40$, su hijo izquierdo se encuentra en la posición $2 \cdot 3 + 1 = 7$ y su hijo derecho en $2 \cdot 3 + 2 = 8$. A su vez el padre se encuentra en $\left\lfloor\frac{3-1}{2}\right\rfloor = 1$.

### Operaciones

Las operaciones básicas que se pueden realizar en un montículo son:

`Top`
: Devuelve el elemento que se encuentra en la cima del montículo, es decir el máximo o el mínimo de toda la estructura, pero no lo elimina.

`Size`
: Devuelve la cantidad de elementos que se encuentran en el montículo.

`Insert`
: Inserta un nuevo elemento en el montículo.

`Remove`
: Elimina el elemento que se encuentra en la cima del montículo y lo devuelve.

#### Insertar

Para preservar la propiedad de forma, se inserta el nuevo elemento al final del arreglo (como última hoja del árbol), manteniendo así la estructura de árbol completo e izquierdista.

Al insertar un elemento en la última posición, se pierde la propiedad de orden, ya que el nuevo elemento podría ser mayor (en un heap de máximos) que su padre. Para restaurarla se ejecuta `upHeap` desde la hoja recién insertada. Esta operación compara el elemento con su padre y, si no se cumple la propiedad de orden, los intercambia, repitiendo el proceso hacia arriba hasta que el elemento encuentra su lugar.

```{code-block}
---
caption: Algoritmo de inserción en un montículo de máximos
linenos: true
language: text
---
FUNCION Insertar(elemento)
    pos ← n                 // n es la cantidad actual de elementos
    A[pos] ← elemento
    n ← n + 1
    upHeap(pos)
FIN FUNCION
```

Con la siguiente función auxiliar se restablece la propiedad de orden, intercambiando el elemento con su padre hasta que cumple la condición del montículo. El padre de la posición $i$ se calcula como $\lfloor (i-1) / 2 \rfloor$.

```{code-block}
---
caption: Algoritmo upHeap
linenos: true
language: text
---
FUNCION upHeap(i)
    MIENTRAS i > 0 Y A[i] > A[padre(i)] HACER
        intercambiar(A[i], A[padre(i)])
        i ← padre(i)
    FIN MIENTRAS
FIN FUNCION
```

`upHeap` recorre en el peor caso toda la altura del árbol. Como el montículo binario es un árbol completo, su altura es $O(\log n)$, por lo tanto **Insertar** tiene orden $O(\log n)$.

#### Remover

La cima del montículo (el máximo o el mínimo) se encuentra siempre en la posición $0$ del arreglo, por lo que consultarla cuesta $O(1)$.

Para eliminar la cima se debe preservar la propiedad de forma: se reemplaza la raíz por la última hoja del árbol (decrementando el tamaño) y luego se ejecuta `downHeap` desde la raíz para restaurar la propiedad de orden. `downHeap` compara el nodo actual con sus dos hijos; en un heap de máximos, si el nodo es menor que alguno de sus hijos, se intercambia con el **mayor** de ellos, repitiendo el proceso hacia abajo hasta encontrar la posición correcta.

```{code-block}
---
caption: Algoritmo de eliminación de la cima de un montículo de máximos
linenos: true
language: text
---
FUNCION Eliminar()
    cima ← A[0]            // guardar la raíz
    n ← n - 1
    A[0] ← A[n]            // mover la última hoja a la raíz
    downHeap(0)
    RETORNAR cima
FIN FUNCION
```

La siguiente función auxiliar busca entre los dos hijos del nodo actual cuál es el mayor. Si el nodo actual es menor que ese hijo, los intercambia y continúa hacia abajo.

```{code-block}
---
caption: Algoritmo downHeap
linenos: true
language: text
---
FUNCION downHeap(i)
    MIENTRAS verdadero HACER
        candidato ← i
        izq ← 2 * i + 1
        der ← 2 * i + 2
        SI izq < n Y A[izq] > A[candidato] ENTONCES
            candidato ← izq
        FIN SI
        SI der < n Y A[der] > A[candidato] ENTONCES
            candidato ← der
        FIN SI
        SI candidato = i ENTONCES
            SALIR
        FIN SI
        intercambiar(A[i], A[candidato])
        i ← candidato
    FIN MIENTRAS
FIN FUNCION
```

`downHeap` también recorre en el peor caso la altura del árbol, $O(\log n)$, por lo tanto **Remover** tiene orden $O(\log n)$.

#### Orden de las operaciones

```{table} Orden de las Operaciones
---
width: 40%
align: center
---
|    Operación    |   Orden    |
| :-------------: | :--------: |
|   `Top`   |   $O(1)$   |
|  `Size`   |   $O(1)$   |
| `Insert`  | $O(\log n)$ |
| `Remove`  | $O(\log n)$ |

```

**Top** y **Size** son $O(1)$ porque solo acceden a la posición $0$ del arreglo o devuelven el tamaño almacenado, sin recorrer la estructura. **Insertar** y **Remover** son $O(\log n)$ porque en el peor caso deben recorrer la altura del árbol (que siempre es $O(\log n)$ por tratarse de un árbol completo) para reestablecer la propiedad de orden mediante `upHeap` o `downHeap`.

### Visualizador de montículo binario interactivo

Seleccioná el tipo de montículo (mínimo o máximo), ingresá uno o más enteros separados por coma y presioná Enter para encolarlos. Usá **>** para procesar una operación, **>>** para procesar todas las pendientes, o **Remover cima** para eliminar la raíz. Las teclas **<** y **>** navegan entre pasos, **<<** deshace la última inserción, y Espacio inicia/pausa la reproducción automática. Solo se admiten enteros de hasta 3 cifras (±999).

:::{iframe} /applets/3-estructuras-de-datos/3-11-monticulo-binario/heap-visualizer_light.html
:width: 100%
:height: 680px
:class: only-light-mode
:::

:::{iframe} /applets/3-estructuras-de-datos/3-11-monticulo-binario/heap-visualizer_dark.html
:width: 100%
:height: 680px
:class: only-dark-mode
:::

## Ejercicios

Los ejercicios de este capítulo se encuentran en el repositorio
[taller-tad](https://github.com/untref-ayp2/taller-tad) y en el repositorio
[data-structures](https://github.com/untref-ayp2/data-structures).

### En data-structures

1. **Implementar un montículo binario genérico** (`heap/`). Crear las
   implementaciones `SliceHeap[T]` con constructores `NewMinHeap` y
   `NewMaxHeap` que reciben una función de comparación `func(T, T) int`.
   El montículo debe soportar las operaciones `Insert`, `Remove`, `Top`,
   `Size` e `IsEmpty`.

2. **Implementar una cola de prioridad genérica** (`priorityqueue/`). Crear
   `PriorityQueue[T]` que recibe un `Heap[T]` por constructor (inyección de
   dependencia). Operaciones: `Enqueue`, `Dequeue`, `Front`, `Size`, `IsEmpty`.

### En taller-tad

Los ejercicios de aplicación están en
[`10-monticulo-binario/ejercicios/`](https://github.com/untref-ayp2/taller-tad/tree/main/10-monticulo-binario/ejercicios):

- **01-merge-listas**: fusionar K listas ordenadas en una sola usando una
  cola de prioridad.
- **02-triage**: sistema de atención hospitalaria que ordena pacientes por
  gravedad y orden de llegada.
