---
label: arboles-balanceados
---

# Árboles Binarios de Búsqueda Balanceados

Una de las propiedades fundamentales de los árboles binarios de búsqueda es que preservan el orden de los elementos, y por lo tanto se pueden usar como contenedores de datos para implementar estructuras más complejas que requieran mantener el orden de los elementos, como por ejemplo diccionarios, listas ordenadas, etc.

La eficiencia de las operaciones de búsqueda, inserción y eliminación en un árbol binario de búsqueda depende en gran medida de su altura. En el peor de los casos, las operaciones pueden ser de orden lineal $O(n)$. Para evitar esto, se utilizan árboles binarios de búsqueda balanceados, que mantienen la altura del árbol en un nivel logarítmico $O(log (n))$ al garantizar que la diferencia entre las alturas de los subárboles izquierdo y derecho sea mínima.

Existen diferentes tipos de árboles binarios de búsqueda balanceados, como los árboles AVL y los árboles rojo y negro. Estos árboles implementan diferentes algoritmos de balanceo para garantizar que la altura del árbol se mantenga equilibrada después de cada operación de inserción o eliminación.

## Árboles AVL

En 1962, dos científicos soviéticos, _**Georgy Adelson-Velsky**_ y _**Evgenii Landis**_, publicaron un artículo titulado _**"An algorithm for the organization of information"**_ (Un algoritmo para la organización de la información). En este trabajo, introdujeron la primera estructura de datos de árbol binario de búsqueda auto-balanceado conocido como **árbol AVL**.

El nombre "AVL" proviene de las iniciales de sus inventores. Su principal innovación fue definir una condición de balanceo estricta que debía mantenerse en cada nodo del árbol:

> La diferencia en la altura entre los subárboles izquierdo y derecho de cualquier nodo no puede ser mayor que uno.

Formalmente:

````{admonition} Definición de Árbol AVL

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

````

En esta definición aparece el concepto de **factor de balanceo** o **factor de equilibrio** de un nodo, que se define como la diferencia entre las alturas de los subárboles izquierdo y derecho:

```{math}
fb(n) = h_{izq} - h_{der}
```

En la siguiente figura se muestra un árbol binario de búsqueda y los factores de balanceo de cada uno de sus nodos.

Si bien la raíz está balanceada, el árbol no es AVL ya que hay varios nodos que están desbalanceados. En este caso, el nodo 54 tiene un factor de balanceo de -2, lo que significa que su subárbol derecho es dos veces más alto que su subárbol izquierdo. Por lo tanto, el árbol no cumple con la condición de balanceo.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVL-FB.svg
---
name: AVL-FB
---
Factores de balanceo de cada nodo de un ABB
```

Los árboles AVL son árboles autobalanceados, es decir que se ajustan automáticamente después de cada operación de inserción o eliminación para mantener la propiedad de balanceo. Esto se logra mediante rotaciones, que son operaciones que cambian la estructura del árbol sin afectar el orden de los elementos. Las rotaciones son de orden $O(1)$ y por lo tanto no afectan la complejidad de las operaciones de búsqueda, inserción y eliminación, que siguen siendo $O(log (n))$.

## Rotaciones

Las rotaciones pueden ser simples o dobles. Las rotaciones simples son suficientes para corregir la mayoría de los desbalances, pero en algunos casos se requieren rotaciones dobles.

Supongamos que tenemos un árbol AVL como el de la figura que usaremos para graficar las rotaciones.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVL.svg
---
name: AVL
---
Árbol AVL balanceado
```

### Rotación simple a derecha

Supongamos que en {ref}`AVL` se inserta el (18), lo que desbalancea el nodo (23). Si observamos el (23) se desbalanceó cuando se insertó un elemento a la izquierda de su subárbol izquierdo y este desbalanceo solo es local, ya que tanto el (17) como el (50) permanecen balanceados.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQIZQ.svg
---
name: AVLIZQIZQ
---
Desbalanceo Izquierda-Izquierda de un nodo
```

Para restaurar el equilibrio del nodo (23) se debe realizar una rotación simple a la derecha del (23). Esta rotación involucra a tres nodos: el (23), el (19) y el recién insertado (18). En la siguiente figura se observa la rotación simple a derecha.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRotacionSimpleDerecha.svg
---
name: AVLRSD
---
Rotación simple a derecha
```

Una vez realizada la rotación, todo el árbol queda restaurado, como se observa en la siguiente figura.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRestauradoRSD.svg
---
name: AVLRestauradoRSD
---
AVL restaurado luego de una rotación simple a derecha
```

### Rotación simple a izquierda

Análogamente cuando en un nodo se produce un desbalance por la inserción de un elemento a la derecha de su hijo derecho, se puede restablecer el balance con una rotación simple a izquierda.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERDER.svg
---
name: AVLDERDER
---
Desbalanceo Derecha-Derecha de un nodo
```

En la figura al insertar el nodo (70) se desbalancea el nodo (54), que se puede volver a balancear con una rotación a la izquierda del nodo (54)

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRotacionSimpleIzquierda.svg
---
name: AVLRSI
---
Rotación simple a izquierda
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRestauradoRSI.svg
---
name: AVLRestauradoRSI
---
AVL restaurado luego de una rotación simple a izquierda
```

### Rotación doble izquierda-derecha

Cuando el desbalance se produce al insertar un elemento a la derecha del hijo izquierdo de un nodo se debe realizar una rotación doble. Las rotaciones dobles se componen de dos rotaciones simples, en este caso de una rotación simple a la izquierda seguida de una rotación simple a la derecha.

En la siguiente figura al insertar el (16), se desbalanceó el (17). Parados en el (17) el desbalance se produce al insertar un elemento a la derecha de su hijo izquierdo.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER.svg
---
name: AVLIZQDER
---
Desbalanceo Izquierda-Derecha de un nodo
```

Para restaurar el balance se precisó realizar dos rotaciones simples, la primera es rotar el hijo izquierdo del nodo desbalanceado, es decir el (12) a la izquierda (aunque el (12) se encuentre balanceado) y luego rotar el nodo desbalanceado originalmente a la derecha.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-1.svg
---
name: AVLIZQDER-1
---
Desbalanceo Izquierda-Derecha, rotación a izquierda del hijo del nodo desbalanceado
```

Luego de la primera rotación a izquierda queda:

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-2.svg
---
name: AVLIZQDER-2
---
Desbalanceo Izquierda-Derecha, luego de la rotación a izquierda.
```

Luego se rota el (17) a derecha. Se observa que el (14) que pasará a ocupar la posición actual del (17) ya tiene un hijo derecho (16) que deberá reacomodarse como hijo izquierdo del (17)

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-3.svg
---
name: AVLIZQDER-3
---
Desbalanceo Izquierda-Derecha, rotación a derecha del nodo desbalanceado
```

Finalmente el árbol rebalanceado queda como en la siguiente figura

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-4.svg
---
name: AVLIZQDER-4
---
Desbalanceo Izquierda-Derecha, árbol rebalanceado
```

### Rotación doble derecha-izquierda

En la siguiente figura se observa que al insertar el (73) se desbalancea el nodo (72). El (73) se insertó bajando una vez a la derecha y una vez a la izquierda desde el (72), es decir la inserción fue derecha-izquierda, por lo que para reestablecer el balance se deberá realizar una rotación doble derecha-izquierda del (72)

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERIZQ.svg
---
name: AVLDERIZQ
---
Desbalanceo Derecha-Izquierda de un nodo
```

En la siguiente figura se observa los nodos involucrados en la rotación doble; que se puede realizar como dos rotaciones simples como en el ejemplo anterior o directamente en un único paso, donde el (74) pasará a ocupar la posición del (72).

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERIZQ-1.svg
---
name: AVLDERIZQ-1
---
Desbalanceo Derecha-Izquierda, nodos involucrados en la rotación derecha-izquierda
```

Como (74) tiene un hijo izquierdo, el nodo (73) recién agregado, entonces deberá ir al subárbol derecho del (72) para mantener la propiedad de búsqueda del ABB, y la única ubicación posible es como hijo derecho del (72), como se observa en la siguiente figura.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERIZQ-2.svg
---
name: AVLDERIZQ-2
---
Desbalanceo Derecha-Izquierda, árbol rebalanceado
```

```{admonition} Importante
---
class: Important
---
Las rotaciones son operaciones locales que solo afectan a un pequeño número de nodos en el árbol. Cuando se inserta un nuevo nodo, en el camino de regreso a la raíz, se verifica el balanceo de cada nodo y se realizan las rotaciones necesarias. Siempre las rotaciones se realizan en el camino de regreso a la raíz, es decir, desde el nodo recién insertado hasta la raíz del árbol.
```

<div class="only-html">

### Visualizador de árbol AVL interactivo

Ingresá uno o más valores separados por coma y presioná Insertar. Usá "Paso a paso" para avanzar una operación a la vez, o "Reproducir" para ver la secuencia completa automáticamente. Las flechas del teclado adelantan/retroceden paso a paso, y la barra espaciadora inicia/pausa la reproducción.

<div class="only-light-mode">
<iframe src="/applets/3-estructuras-de-datos/3-10-arboles-balanceados/avl-visualizer_light.html" width="100%" height="520px"></iframe>
</div>
<div class="only-dark-mode">
<iframe src="/applets/3-estructuras-de-datos/3-10-arboles-balanceados/avl-visualizer_dark.html" width="100%" height="520px"></iframe>
</div>

</div>

## Ejercicios

Los ejercicios de este capítulo están en la guía de trabajos prácticos [guia-abb-balanceados](https://github.com/untref-ayp2/guia-abb-balanceados).
