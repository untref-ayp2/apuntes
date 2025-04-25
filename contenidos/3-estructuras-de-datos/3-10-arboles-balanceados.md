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


- **Rotación simple a la izquierda**: Se utiliza cuando el subárbol derecho de un nodo está desbalanceado y su subárbol derecho también está desbalanceado. En este caso, se realiza una rotación simple a la izquierda para equilibrar el árbol.

- **Rotación doble a la derecha**: Se utiliza cuando el subárbol izquierdo de un nodo está desbalanceado y su subárbol derecho está desbalanceado. En este caso, se realiza una rotación doble a la derecha para equilibrar el árbol.

- **Rotación doble a la izquierda**: Se utiliza cuando el subárbol derecho de un nodo está desbalanceado y su subárbol izquierdo está desbalanceado. En este caso, se realiza una rotación doble a la izquierda para equilibrar el árbol.