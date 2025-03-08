---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Montículo

Los montículos o heaps son estructuras de datos que permiten acceder al elemento que se encuentra en la cima muy eficientemente. Esta posición privilegiada se utiliza para mantener el mayor elemento del montículo o el menor.

```{figure} ../assets/images/HeapRopa.svg
---
width: 300px
name: Monticulo
---
Montículo
```

Una forma muy usada de Montículos es el **Montículo Binario** que consiste en un árbol binario que cumple con dos propiedades fundamentales.

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

## Representación

Como un montículo binario es un árbol binario completo, o casi completo, podemos aprovechar esta propiedad y usar un arreglo para representarlo.

```{note}
Cómo es un árbol **completo e izquierdista** entonces el arreglo que se usa como contenedor de datos tendrá elementos en todas sus posiciones, es decir no habrá "huecos" y la raíz siempre se econtrará en la posición 0. Además con algunas cuentas simples se puede determinar donde están los hijos o el padre de cualquier nodo.
```

En la siguiente figura se observa como se usar un arreglo para mantener un montículo. La raíz se encuentra en la posición 0, el hijo izquierdo de la raíz en la posición 1, el hijo derecho de la raíz en la posición 2 y así sucesivamente.

```{figure} ../assets/images/HeapMinimosRepresentacion.svg
---
width: 300px
name: Heap Representacion
---
Representación con Arreglos de un Montículo Binario de Mínimos
```

:::{admonition} Fórmulas
$ H_{izq}(i) = 2 \times i + 1$

$H_{der}(i) = 2 \times i + 2$

$Padre(i) = \lfloor \frac{i-1} {2} \rfloor$ Donde el símbolo $\lfloor$ $\rfloor$ indica el piso, es decir la parte entera del cociente
:::

```{margin}
Las fórmulas pueden variar si la primera posición del arreglo es 1 en lugar de 0. ¿Cómo serían las fórmulas?
```

Por ejemplo en la posición 3 del arreglo se encuentra el elemento $H$, su hijo izquierdo se encuentra en la posición $2 \times 3 + 1 = 7$ y su hijo derecho en $2 \times 3 + 2 = 8$. A su vez el padre se encuentra en $\lfloor \frac{3-1} {2} \rfloor = 1$

## Inserción

En la figura a continuación, {ref}`Heap Insercion`, se representa la inserción del elemento $9$ dentro de un heap de máximos.
Para preservar la propiedad de forma es preciso insertar el elemento en la posición 9 del arreglo, es decir como hijo izquierdo de la posición 4. De esta forma nos aseguramos de mantener siempre un árbol completo e izquierdista.

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

**Entrada** $elemento$: Elemento a insertar

```{code-block}
:linenos:
pos = cantidad de elementos - 1
A[pos] = elemento
upHeap(pos)
```
````

````{prf:algorithm} upHeap
:label: upHeap

Reestablece la Propiedad de Orden en un montículo de máximos, luego de insertar un elemento

**Entrada** $i$: Posición dentro del heap donde empieza la operación. Inicialmente la última hoja recién insertada.

```{code-block}
:linenos:
padre = (i-1) div 2
Mientras A[i] < A[padre]:
    Intercambiar(A, i, padre)
    i = padre
    padre = (i-1) div 2
```
````

## Eliminar Tope

En la cima del montículo siempre está el máximo o el mínimo de todo el conjunto. Ver el máximo o el mínimo consiste en consultar la posición 0 del arreglo.

Eliminar el máximo o el mínimo implica siempre eliminar la raíz del árbol, por lo que habrá que reordenar los elementos para preservar el montículo.

Para preservar la propiedad de forma, es decir mantener todo el arreglo contiguo y sin posiciones vacías se elimina la última hoja, en la práctica se disminuy el tamaño del arreglo en 1 y el elemento que se encontraba en esa hoja se lo guarda en la raíz.

Esta operación hace que se pierda la propiedad de orden, para reestablecerla se realiza la operación `downHeap`, que consiste en comparar la raíz con sus dos hijos y si la raíz es menor que los hijos (en un heap de máximos) se intercambia con el mayor de los hijos. Nuevamente se realiza la operación sobre el hijo hasta que se encuentra la posición correcta del elemento.

En la figura {ref}`Heap Eliminacion`, se observa el proceso de eliminación de la raíz en un montículo de máximos

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
ultimo = cantidad de elementos - 1
Intercambiar(A, 0, ultimo)
Decrementar tamaño del Heap en 1
downHeap(0)
retornar elemento
```
````

````{prf:algorithm} downHeap
:label: downHeap

Reestablece la Propiedad de Orden en un montículo de máximos, luego de eliminar la raíz

**Entrada** $i$: Posición dentro del heap donde empieza la operación. Inicialmente la raíz en la posición 0.

```{code-block}
:linenos:
candidato = Elegir menor de los hijos
Mientras A[i] < A[candidato]:
    Intercambiar(A, i, candidato)
    i = candidato
    candidato = Elegir menor de los hijos
```
````

Los montículos o heaps son estructuras de datos que por lo general se utilizan para implementar colas de prioridad. Una cola de prioridad debe permitir realizar las siguientes operaciones lo más eficientemente posible:

- Agregar un nuevo elemento, con una prioridad dada.
- Obtener el elemento con mayor prioridad de la cola.
- Extraer el elemento con mayor prioridad de la cola.
