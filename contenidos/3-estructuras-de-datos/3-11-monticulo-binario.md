---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Colas de Prioridad y Montículos Binarios

## Colas de Prioridad

Una cola de prioridad, se comporta de forma similar a una cola, pero cada elemento que ingresa en la cola tiene asignada una prioridad, y los elementos con mayor prioridad son los primeros en salir de la cola.

Si todos los elementos tienen la misma prioridad, la cola se comporta como una cola común, es decir el primero que llega es el primero que sale de la cola.

Por ejemplo, si se tiene una cola de prioridad con los siguientes elementos y prioridades, y la posición en la tabla corresponde al orden de llegada de los elementos, es decir se insertaron en orden alfabético y además suponemos que la prioridad 1 es la mayor, luego la 2 y así sucesivamente.

:::{table} Cola de Prioridad
:width: 40%
:align: center

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

:::

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

Las operaciones que se pueden realizar en una cola de prioridad son:

- Agregar un nuevo elemento, con una prioridad dada.
- Obtener el elemento con mayor prioridad de la cola.
- Extraer el elemento con mayor prioridad de la cola.

Para implementar una cola de prioridad se puede usar un **montículo binario**, ya que optimiza las operaciones de inserción y eliminación de los elementos.

## Montículos Binarios

Los montículos o _heaps_ en inglés, son estructuras de datos que permiten acceder al elemento que se encuentra en la "cima" muy eficientemente. Esta posición privilegiada se utiliza para mantener el mayor elemento del montículo o el menor. En el caso de que se mantenga el mayor elemento en la cima se le llama **Montículo de Máximos** y si se mantiene el menor se le llama **Montículo de Mínimos**.

Existen diferentes tipos de montículos (binario, fibonacci, suave (_soft_), etc.), pero todos comparten la propiedad de que el elemento que se encuentra en la cima es el mayor o el menor de toda la estructura. En nuestro curso nos enfocaremos en los montículos binarios.

```{figure} ../assets/images/HeapRopa.svg
---
width: 300px
name: Monticulo
---
Montículo
```

Un **Montículo Binario** consiste en un árbol binario que cumple con dos propiedades fundamentales.

Propiedad de Forma
: Es un árbol binario **completo** (o casi completo) e **izquierdista**, es decir que se va llenando de izquierda a derecha. Lo que implica que todos los niveles del árbol están llenos, excepto el último nivel que puede estar incompleto.

Propiedad de Orden
: En un montículo de mínimos, cada nodo es menor que todos sus descendientes. Analogamente si es un montículo de máximos, cada nodo es mayor que todos sus descendientes. En otras palabras, en un montículo binario de mínimos, el menor elemento de toda la estructura se encuentra en la raíz y recursivamente podemos pensar a los hijos de la raíz como otros montículos de mínimos

En la siguiente figura se puede ver un heap de mínimos donde se cumplen ambas propiedades. El elemento $A$ es el menor de toda la estructura y se encuentra en la raíz. Analogamente el menor de sus descendientes por la izquierda es el elemento $D$ y se encuentra en la raíz del subárbol izquierdo y por el lado derecho el elemento $M$ es el menor del subárbol derecho.

```{figure} ../assets/images/HeapMinimos.svg
---
width: 300px
name: Heap de Mínimos
---
Montículo Binario de Mínimos
```

### Representación

Como un montículo binario es un árbol binario completo, o casi completo, podemos aprovechar esta propiedad y usar un arreglo para representarlo. Usar un arreglo para representar un árbol binario completo es una técnica muy común en computación y se conoce como **representación por niveles** y tiene ventajas en términos de espacio y tiempo y facilita la implementación de las operaciones.

```{note}
Cómo es un árbol **completo e izquierdista** entonces el arreglo que se usa como contenedor de datos tendrá elementos en todas sus posiciones, es decir no habrá "huecos" y la raíz siempre se econtrará en la posición 0. Además con algunas cuentas simples se puede determinar donde están los hijos o el padre de cualquier nodo.
```

En la siguiente figura se observa como se puede usar un arreglo para mantener un montículo binario. La raíz se encuentra en la posición 0, el hijo izquierdo de la raíz en la posición 1, el hijo derecho de la raíz en la posición 2 y así sucesivamente.

```{figure} ../assets/images/HeapMinimosRepresentacion.svg
---
width: 300px
name: Heap Representacion
---
Representación con arreglos de un Montículo Binario de Mínimos
```

Con las siguientes fórmulas se puede calcular la posición en el arreglo de cualquier hijo o padre de un nodo dado.

:::{card} Fórmulas
$$H_{izq}(i) = 2 \; i + 1$$

$$H_{der}(i) = 2 \; i + 2$$

$$Padre(i) = \left\lfloor \frac{i-1}{2} \right\rfloor$$

Donde el símbolo $\lfloor \; \rfloor$ indica el piso, es decir la parte entera del cociente.

+++
Las fórmulas pueden variar si la primera posición del arreglo es 1 en lugar de 0. ¿Cómo serían las fórmulas?
:::

Por ejemplo en la posición 3 del arreglo se encuentra el elemento $H$, su hijo izquierdo se encuentra en la posición $2 \cdot 3 + 1 = 7$ y su hijo derecho en $2 \cdot 3 + 2 = 8$. A su vez el padre se encuentra en $\left\lfloor\frac{3-1}{2}\right\rfloor = 1$

### Operaciones

Las operaciones básicas que se pueden realizar en un montículo son:

Top
: Devuelve el elemento que se encuentra en la cima del montículo, es decir el máximo o el mínimo de toda la estructura, pero no lo elimina.

Size
: Devuelve la cantidad de elementos que se encuentran en el montículo.

Insert
: Inserta un nuevo elemento en el montículo.

Remove
: Elimina el elemento que se encuentra en la cima del montículo y lo devuelve.

#### Insertar

En la figura {ref}`Heap Insercion`, se representa la inserción del elemento $9$ dentro de un Heap de Máximos.

Para preservar la propiedad de forma, es preciso insertar el elemento en la posición 9 del arreglo, es decir como hijo izquierdo de la posición 4. De esta forma nos aseguramos de mantener siempre un árbol completo e izquierdista.

Al insertar el elemento $9$ en la posición 9 vemos que se perdió la propiedad de orden, ya que el 9 es mayor que su padre, el elemento $5$.

Para reestrablecer la propiedad de orden se realiza la operación `upHeap` desde la hoja recién insertada. Esta operación consiste en comparar el elemento actual con su padre y si no se cumple la propiedad de orden intercambiarlos, luego compara el padre que acaba de intercambiar con su padre, hasta encontrar la posición correcta del elemento recién insertado dentro del montículo.

En el ejemplo de la figura primero intercambia el 9 con el 5. Es decir en el arreglo que representa el heap intercambia los elementos y luego compara la posición 4 con su padre que se encuentra en la posición 1. Cómo el $9$ es mayor que el $7$ los intercambia nuevamente. Finalmente compara la posición 1 con su padre, la raíz en la posición 0, y cómo $10$ es mayor que $9$ termina la operación `upHeap`.

```{figure} ../assets/images/HeapInsercion.svg
---
name: Heap Insercion
---
Inserción en un Heap de Máximos
```

````{prf:algorithm} Insertar
:label: Insertar

Inserta un elemento dentro del Montículo

**Entrada**

- `elemento`: elemento a insertar

```{code-block} go
:linenos:
pos = cantidadDeElementos - 1
A[pos] = elemento
upHeap(pos)
```
````

````{prf:algorithm} upHeap
:label: upHeap

Reestablece la Propiedad de Orden en un montículo de máximos, luego de insertar un elemento

**Entrada**

- `i`: posición dentro del heap donde empieza la operación. Inicialmente la última hoja recién insertada.

```{code-block} go
:linenos:
padre = (i-1) / 2
for A[i] < A[padre] {
    Intercambiar(A, i, padre)
    i = padre
    padre = (i-1) / 2
}
```
````

#### Remover

En la cima del montículo siempre está el máximo o el mínimo de todo el conjunto. Ver el máximo o el mínimo consiste en consultar la posición 0 del arreglo.

Eliminar el máximo o el mínimo implica siempre eliminar la raíz del árbol, por lo que habrá que reordenar los elementos para preservar el montículo.

Para preservar la propiedad de forma, es decir mantener todo el arreglo contiguo y sin posiciones vacías se elimina la última hoja, en la práctica se disminuye el tamaño del arreglo en 1 y el elemento que se encontraba en esa hoja se lo guarda en la raíz.

Esta operación hace que se pierda la propiedad de orden, para reestablecerla se realiza la operación `downHeap`, que consiste en comparar la raíz con sus dos hijos y si la raíz es menor que los hijos (en un heap de máximos) se intercambia con el mayor de los hijos. Nuevamente se realiza la operación sobre el hijo hasta que se encuentra la posición correcta del elemento.

En la figura a continuación, se observa el proceso de eliminación de la raíz en un montículo de máximos

```{figure} ../assets/images/HeapEliminacion.svg
---
name: Heap Eliminacion
---
Eliminación en un Heap de Máximos
```

````{prf:algorithm} Eliminar
:label: Eliminar

Elimina la cima del heap y devuelve el elemento correspondiente

```{code-block}
:linenos:
elemento = A[0]
ultimo = cantidadDeElementos - 1
Intercambiar(A, 0, ultimo)
// Decrementar tamaño del Heap en 1
A = A[:len(A)-1]
downHeap(0)
return elemento
```
````

````{prf:algorithm} downHeap
:label: downHeap

Reestablece la Propiedad de Orden en un montículo de máximos, luego de eliminar la raíz

**Entrada**

- `i`: posición dentro del heap donde empieza la operación. Inicialmente la raíz en la posición 0.

```{code-block}
:linenos:
candidato = Elegir menor de los hijos
Mientras A[i] < A[candidato]:
    Intercambiar(A, i, candidato)
    i = candidato
    candidato = Elegir menor de los hijos
```
````

#### Orden de las operaciones

:::{table} Orden de las Operaciones
:width: 40%
:align: center

| Operación |   Orden    |
| :-------: | :--------: |
|    Top    |   $O(1)$   |
|   Size    |   $O(1)$   |
|  Insert   | $O(log_n)$ |
|  Remove   | $O(log_n)$ |

:::

Insertar y Remover tienen un orden garantizado de $O(log N)$ porque en el peor caso se debe recorrer la altura del árbol para reestablecer la propiedad de orden y el árbol siempre está balanceado.

## Ejercicios

1. Implementar un montículo binario de máximos que soporte números enteros.
2. Dadas la siguiente definición:

   ```{code-block} go
   :linenos:
   type Heap[T any] struct {
       // contenedor de datos
       elements []T
       // Función de comparación. Para un heap de mínimo,
       // devuelve -1 si a < b, 0 si a == b, 1 si a > b
       // Para un heap de máximo, devuelve 1 si a < b, 0 si a == b, -1 si a > b
       compare func(a T, b T) int
   }
   ```

   Completar el código a continuación, para obtener un montículo genérico, cuyos elementos puede ser cualquier cosa que pueda compararse entre sí, por ejemplo enteros, flotantes, cadenas o estructuras más complejas, como {nombre, edad}, etc. y que soporte montículos de máximos y mínimos.

   ```{code-block} go
   // NewGenericHeap crea un nuevo heap binario con una función de comparación personalizada.
   //
   // Uso:
   //
   //     heap := heap.NewGenericHeap[int](func(a int, b int) int {
   //         if a < b {
   //             return -1
   //         }
   //         if a > b {
   //             return 1
   //         }
   //         return 0
   //     })
   //
   // Parámetros:
   //   - `comp` función de comparación personalizada.
   //
   // Retorna:
   //   - un puntero a un heap binario con una función de comparación personalizada.
   func NewGenericHeap[T any](comp func(a T, b T) int) *Heap[T] {
       // ...
   }

   // Size retorna la cantidad de elementos en el heap.
   //
   // Uso:
   //
   //     size := heap.Size()
   //
   // Retorna:
   // - la cantidad de elementos en el heap.
   func (m *Heap[T]) Size() int {
       // ...
   }

   // Insert agrega un elemento al heap.
   //
   // Uso:
   //
   //     heap := heap.NewMinHeap[int]()
   //     heap.Insert(5)
   //
   // Parámetros:
   //   - `element`: elemento a agregar al heap.
   func (m *Heap[T]) Insert(element T) {
       // ...
   }

   // Remove elimina y retorna el elemento en la cima del heap.
   //
   // Uso:
   //
   //     heap := heap.NewMinHeap[int]()
   //     heap.Insert(5)
   //     element, _ := heap.Remove()
   //
   // Retorna:
   //   - el elemento en la cima del heap.
   //   - un error si el heap está vacío.
   func (m *Heap[T]) Remove() (T, error) {
       // ...
   }

   // Top retorna el elemento en la cima del heap.
   //
   // Uso:
   //
   //     heap := heap.NewMinHeap[int]()
   //     heap.Insert(5)
   //     element, _ := heap.Top()
   //
   // Retorna:
   //   - el elemento en la cima del heap.
   //   - un error si el heap está vacío.
   func (m *Heap[T]) Top() (T, error) {
       // ...
   }

   ```

3. Escribir casos de prueba para verificar que el montículo binario del punto anterior funciona correctamente. Usar `Persona` dado a continuación como elementos del montículo.

   ```{code-block} go
   type Persona struct {
       nombre string
       edad   int
   }

   func personasDeMayorAMenorEdad(a Persona, b Persona) int {
       if a.edad < b.edad {
           return 1
       } else if a.edad > b.edad {
           return -1
       }

       return 0
   }

   func personasDeMenorAMayorEdad(a Persona, b Persona) int {
       if a.edad < b.edad {
           return -1
       } else if a.edad > b.edad {
           return 1
       }

       return 0
   }
   ```

4. Crear una Cola de Prioridad de Personas que permita agregar Personas y atenderlas por Orden de prioridad y Orden de llegada. La prioridad se define por la edad de la persona, es decir la persona con mayor edad tiene mayor prioridad.
