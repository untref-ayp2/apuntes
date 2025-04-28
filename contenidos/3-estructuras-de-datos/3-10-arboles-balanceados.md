---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Árboles Binarios de Búsqueda Balanceados

Una de las propiedades fundamentales de los árboles binarios de búsqueda es que preservan al orden de los elementos, y por lo tanto se pueden usar como contenedores de datos para implementar estructuras más complejas que requieran mantener el orden de los elementos, como por ejemplo diccionarios, listas ordenadas, etc.

La eficiencia de las operaciones de búsqueda, inserción y eliminación en un árbol binario de búsqueda depende en gran medida de su altura. En el peor de los casos, las operaciones pueden ser de orden lineal $O(n)$. Para evitar esto, se utilizan árboles binarios de búsqueda balanceados, que mantienen la altura del árbol en un nivel logarítmico $O(log (n))$ al garantizar que la diferencia entre las alturas de los subárboles izquierdo y derecho sea mínima.

Existen diferentes tipos de árboles binarios de búsqueda balanceados, como los árboles AVL y los árboles rojo y negro. Estos árboles implementan diferentes algoritmos de balanceo para garantizar que la altura del árbol se mantenga equilibrada después de cada operación de inserción o eliminación.

## Árboles AVL

En 1962, dos científicos soviéticos, _**Georgy Adelson-Velsky**_ y _**Evgenii Landis**_, publicaron un artículo titulado _**"An algorithm for the organization of information"**_ (Un algoritmo para la organización de la información). En este trabajo, introdujeron la primera estructura de datos de árbol binario de búsqueda auto-balanceado conocido como **árbol AVL**.

El nombre "AVL" proviene de las iniciales de sus inventores. Su principal innovación fue definir una condición de balanceo estricta que debía mantenerse en cada nodo del árbol:

> La diferencia en la altura entre los subárboles izquierdo y derecho de cualquier nodo no puede ser mayor que uno.

Formalmente: 

:::{admonition} Definición de Árbol AVL
```{math}
\text{AVL } \text{si}
\begin{cases}
\text{ ABB nulo} \\
\text{}\\
\text{ABB no nulo} 
\begin{cases}
|h_{izq} - h_{der}| \leq 1 \\
\text{subárbol izquierdo} \text{ es AVL} \\
\text{subárbol derecho} \text{ es AVL} \\
\end{cases}
\end{cases}
```
:::

En esta definición aparece el concepto de **factor de balanceo** o **factor de equilibrio** de un nodo, que se define como la diferencia entre las alturas de los subárboles izquierdo y derecho:

```{math}
fb(n) = h_{izq} - h_{der}
```

En la siguiente figura se muestra un árbol binario de búsqueda y los factores de balanceo de cada uno de sus nodos.

Si bien la raíz está balanceada, el árbo no es AVL ya que hay varios nodos que están desbalanceados. En este caso, el nodo 4 tiene un factor de balanceo de -2, lo que significa que su subárbol dereche es dos veces más alto que su subárbol izquierdo. Por lo tanto, el árbol no cumple con la condición de balanceo.

```{figure} ../assets/images/AVL-FB.svg
---
name: AVL-FB
---
Factores de balanceo de cada nodo de un ABB
```

Los árboles AVL son árboles autobalanceados, es decir que se ajustan automáticamente después de cada operación de inserción o eliminación para mantener la propiedad de balanceo. Esto se logra mediante rotaciones, que son operaciones que cambian la estructura del árbol sin afectar el orden de los elementos. Las rotaciones son de orden $O(1)$ y por lo tanto no afectan la complejidad de las operaciones de búsqueda, inserción y eliminación, que siguen siendo $O(log (n))$.

## Rotaciones

Las rotaciones pueden ser simples o dobles. Las rotaciones simples son suficientes para corregir la mayoría de los desbalances, pero en algunos casos se requieren rotaciones dobles.

Supongamos que tenemos un árbol AVL como el de la figura que usaremos para graficar las rotaciones.

```{figure} ../assets/images/AVL.svg
---
name: AVL
---
Árbol AVL balanceado
```

### Rotación simple a derecha

Supongamos que en {AVL} se inserta el (18), lo que desbalancea el nodo (23). Si observamos el (23) se desbalanceo cuando se insertó un elemento a la izquierda de su subárbol izquierdo y este desbalanceo solo es local, ya que tanto el (17) como el (50) permanecen balanceados.

```{figure} ../assets/images/AVLIZQIZQ.svg
---
name: AVLIZQIZQ
---
Desbalanceo Izquierda-Izquierda de un nodo
```

Para restaurar el equilibrio del nodo (23) se debe realizar una rotación simple a la derecha del (23). Esta rotación involucra a tres nodos el (23), el (19) y el recién insertado (18). En la siguiente figura se observa la rotación simple a derecha.


```{figure} ../assets/images/AVLRotacionSimpleDerecha.svg
---
name: AVLRSD
---
Rotación simple a derecha
```

Una vez realizada la rotación, todo el árbol queda restaurado, como se observa en la siguiente figura.

```{figure} ../assets/images/AVLRestauradoRSD.svg
---
name: AVLRestauradoRSD
---
AVL restaurado luego de una rotación simple a derecha
```

### Rotación simple a izquierda

Analogamente cuando en un nodo se produce un desbalance por la inserción de un elemento a la derecha de su hijo derecho, se puede reestablecer el balance con una rotación simple a izquierda.

```{figure} ../assets/images/AVLDERDER.svg
---
name: AVLDERDER
---
Desbalanceo Derecha-Derecha de un nodo
```

En la figura al insertar el nodo (70) de desbalancea el nodo (54), que se puede volver a balancear con una rotación a la izquierda del nodo (54)


```{figure} ../assets/images/AVLRotacionSimpleIzquierda.svg
---
name: AVLRSI
---
Rotación simple a izquierda
```

```{figure} ../assets/images/AVLRestauradoRSI.svg
---
name: AVLRestauradoRSI
---
AVL restaurado luego de una rotación simple a izquierda
```
### Rotación doble izquierda-derecha

Cuando el desbalance se produce al insertar un elemento a la izquierda del hijo derecho de un nodo se debe realizar una rotación doble. Las rotaciones doble se componen de dos rotaciones simples, en este caso de una rotación simple a la izquierda seguida de una rotación simple a la derecha.

En la siguiente figura al insertar el (16), se desbalanceó el (17). Parados en el (17) el desbalance se produce al insertar un elemento a la derecha de su hijo izquierdo.

```{figure} ../assets/images/AVLIZQDER.svg
---
name: AVLIZQDER
---
Desbalanceo Derecha-Izquierda de un nodo
```

Para restaurar el balance se preciso realizar dos rotaciones simples, la primera es rotar el hijo izquierdo del nodo desbalanceado, es decir el (12) a la izquierda (aunque el (12) se encuentre balanceado) y luego rotar el nodo desbalanceado originalmente a la derecha.

```{figure} ../assets/images/AVLIZQDER-1.svg
---
name: AVLIZQDER-1
---
Desbalanceo Derecha-Izquierda, rotación a izquierda del hijo del nodo desbalanceado
```

Luego de la primera rotación a izquierda queda:

```{figure} ../assets/images/AVLIZQDER-2.svg
---
name: AVLIZQDER-2
---
Desbalanceo Derecha-Izquierdda, luego de la rotación a izquierda.
```

Luego se rota el (17) a derecha. Se observa que el (14) que pasará a ocupar la posición actual del (17) ya tiene un hijo derecho (16) que deberá reacomodarse como hijo izquierdo del (17)


```{figure} ../assets/images/AVLIZQDER-3.svg
---
name: AVLIZQDER-3
---
Desbalanceo Derecha-Izquierda, rotación a derecha del nodo desbalanceado
```

Finalmente el árbol rebalanceado queda como en la siguiente figura


```{figure} ../assets/images/AVLIZQDER-4.svg
---
name: AVLIZQDER-4
---
Desbalanceo Derecha-Izquierda, árbol rebalanceado
```

### Rotación doble derecha-izquierda

En la siguiente figura se observa que al insertar el (70) se desbalancea el nodo (72). El (70) se insertó bajando una vez a la izquierda y dos veces a la derecha desde el (72), es decir la inserción fue izquierda-derecha, por lo que para reestablecer el balance se deberá realizar una rotación doble derecha-izquierda del (72)

```{figure} ../assets/images/AVLDERIZQ.svg
---
name: AVLDERIZQ
---
Desbalanceo Izquierda-Derecha de un nodo
```

En la siguiente figura se observa los nodos involucrados en la rotación doble, que se puede realizar como dos rotaciones simples como en el ejemplo anterior o directamente en un único paso, donde el (67) pasará a ocupar la posición del (72). 

```{figure} ../assets/images/AVLDERIZQ-1.svg
---
name: AVLDERIZQ-1
---
Desbalanceo Izquierda-Derecha, nodos involucrados en la rotación derecha-izquierda
```

Como (67) tiene un hijo derecho, el nodo (70) recién agregado, entonces deberá ir al subárbol derecho del (67) para mantener la propiedad de búsqueda del ABB, y la única ubicación posible es como hijo izquierdo del (72), como se observa en la siguiente figura.

```{figure} ../assets/images/AVLDERIZQ-2.svg
---
name: AVLDERIZQ-2
---
Desbalanceo Izquierda-Derecha, árbol rebalanceado luego de la rotación doble Derecha-Izquierda
```