---
label: arboles-balanceados
---

# Árboles Binarios de Búsqueda Balanceados

Una de las propiedades fundamentales de los árboles binarios de búsqueda es que preservan el orden de los elementos, y por lo tanto se pueden usar como contenedores de datos para implementar estructuras más complejas que requieran mantener el orden de los elementos, como por ejemplo diccionarios, listas ordenadas, etc.

La eficiencia de las operaciones de búsqueda, inserción y eliminación en un árbol binario de búsqueda depende en gran medida de su altura. En el peor de los casos, las operaciones pueden ser de orden lineal $O(n)$. Para evitar esto, se utilizan árboles binarios de búsqueda balanceados, que mantienen la altura del árbol en un nivel logarítmico $O(\log n)$ al garantizar que la diferencia entre las alturas de los subárboles izquierdo y derecho sea mínima.

Existen diferentes tipos de árboles binarios de búsqueda balanceados, como los árboles AVL y los árboles rojo y negro. Estos árboles implementan diferentes algoritmos de balanceo para garantizar que la altura del árbol se mantenga equilibrada después de cada operación de inserción o eliminación.

## Árboles AVL

En 1962, dos científicos soviéticos, _**Georgy Adelson-Velsky**_ y _**Evgenii Landis**_, publicaron un artículo titulado _**"An algorithm for the organization of information"**_ {cite}`adelson1962` (Un algoritmo para la organización de la información). En este trabajo, introdujeron la primera estructura de datos de árbol binario de búsqueda autobalanceado conocido como **árbol AVL**.

El nombre "AVL" proviene de las iniciales de sus inventores. Su principal innovación fue definir una condición de balanceo estricta que debía mantenerse en cada nodo del árbol:

> La diferencia en la altura entre los subárboles izquierdo y derecho de cualquier nodo no puede ser mayor que uno.

Formalmente:

````{admonition} Definición de Árbol AVL
---
class: hint
---
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

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVL-FB_light.svg
---
class: only-light-mode
name: AVL-FB
---
Factores de balanceo de cada nodo de un ABB
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVL-FB_dark.svg
---
class: only-dark-mode
name: AVL-FB
---
Factores de balanceo de cada nodo de un ABB
```

Los árboles AVL son árboles autobalanceados, es decir que se ajustan automáticamente después de cada operación de inserción o eliminación para mantener la propiedad de balanceo. Esto se logra mediante rotaciones, que son operaciones que cambian la estructura del árbol sin afectar el orden de los elementos. Las rotaciones son de orden $O(1)$ y por lo tanto no afectan la complejidad de las operaciones de búsqueda, inserción y eliminación, que siguen siendo $O(\log n)$.

## Rotaciones

Las rotaciones pueden ser simples o dobles. Las rotaciones simples son suficientes para corregir la mayoría de los desbalances, pero en algunos casos se requieren rotaciones dobles.

Partimos del siguiente árbol AVL balanceado:

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVL_light.svg
---
class: only-light-mode
name: AVL
---
Árbol AVL balanceado
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVL_dark.svg
---
class: only-dark-mode
name: AVL
---
Árbol AVL balanceado
```

Sobre este árbol vamos a realizar cuatro inserciones, cada una en una rama distinta, para observar los cuatro tipos de desbalance y sus rotaciones correspondientes.

### Rotación simple a derecha

Supongamos que en el árbol de la {ref}`AVL` insertamos el (5) como hijo izquierdo del (10). Esto provoca un desbalance de tipo **Izquierda-Izquierda**. El primer nodo que queda desbalanceado en el camino de subida es el (20), ya que su subárbol izquierdo queda dos niveles más alto que el derecho ($fb = +2$). El nodo (15) se mantiene dentro del rango permitido ($fb = +1$).

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQIZQ_light.svg
---
class: only-light-mode
name: AVLIZQIZQ
---
Desbalanceo Izquierda-Izquierda: fb(20) = +2
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQIZQ_dark.svg
---
class: only-dark-mode
name: AVLIZQIZQ
---
Desbalanceo Izquierda-Izquierda: fb(20) = +2
```

Para restaurar el equilibrio se debe realizar una **rotación simple a la derecha** del nodo (20). Los nodos involucrados son el (20), el (15), el (10) y el recién insertado (5). El (15) asciende a la posición del (20), y el (20) pasa a ser su hijo derecho. El nodo (17), que originalmente era hijo derecho del (15), pasa a ser hijo izquierdo del (20).

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRotacionSimpleDerecha_light.svg
---
class: only-light-mode
name: AVLRSD
---
Rotación simple a derecha del nodo (20)
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRotacionSimpleDerecha_dark.svg
---
class: only-dark-mode
name: AVLRSD
---
Rotación simple a derecha del nodo (20)
```

Como se ve en la figura a continuación, la rotación solo afecta a algunos pocos nodos del árbol, es decir, siempre son operaciones **locales**.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRestauradoRSD_light.svg
---
class: only-light-mode
name: AVLRestauradoRSD
---
AVL restaurado luego de la rotación simple a derecha
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRestauradoRSD_dark.svg
---
class: only-dark-mode
name: AVLRestauradoRSD
---
AVL restaurado luego de la rotación simple a derecha
```

### Rotación simple a izquierda

Análogamente, cuando la inserción se produce a la derecha del hijo derecho de un nodo, el desbalance es **Derecha-Derecha** y se resuelve con una **rotación simple a la izquierda**.

Partiendo del árbol original, insertamos el (67) como hijo derecho del (66). Esto provoca un desbalance en el nodo (60), cuyo subárbol derecho queda dos niveles más alto que el izquierdo ($fb = -2$).

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERDER_light.svg
---
class: only-light-mode
name: AVLDERDER
---
Desbalanceo Derecha-Derecha: fb(60) = -2
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERDER_dark.svg
---
class: only-dark-mode
name: AVLDERDER
---
Desbalanceo Derecha-Derecha: fb(60) = -2
```

Para corregirlo se realiza una rotación simple a la izquierda del nodo (60). El (65) asciende y el (60) pasa a ser su hijo izquierdo. El (64), que originalmente era hijo izquierdo del (65), pasa a ser hijo derecho del (60).

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRotacionSimpleIzquierda_light.svg
---
class: only-light-mode
name: AVLRSI
---
Rotación simple a izquierda del nodo (60)
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRotacionSimpleIzquierda_dark.svg
---
class: only-dark-mode
name: AVLRSI
---
Rotación simple a izquierda del nodo (60)
```

Luego de la rotación el árbol vuelve a estar balanceado:

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRestauradoRSI_light.svg
---
class: only-light-mode
name: AVLRestauradoRSI
---
AVL restaurado luego de la rotación simple a izquierda
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLRestauradoRSI_dark.svg
---
class: only-dark-mode
name: AVLRestauradoRSI
---
AVL restaurado luego de la rotación simple a izquierda
```

### Rotación doble izquierda-derecha

Cuando el desbalance se produce al insertar un elemento a la *derecha* del hijo *izquierdo* de un nodo, una rotación simple no alcanza: se necesita una **rotación doble izquierda-derecha**. Esta rotación combina una rotación simple a la izquierda del hijo del nodo desbalanceado, seguida de una rotación simple a la derecha del nodo desbalanceado.

Partiendo del árbol original, insertamos el (18) como hijo derecho del (17). Esto provoca que el nodo (20) quede desbalanceado ($fb = +2$). El hijo izquierdo del (20) es el (15), que tiene $fb = -1$ (está cargado a la derecha), indicando que el desbalance es de tipo **Izquierda-Derecha**.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER_light.svg
---
class: only-light-mode
name: AVLIZQDER
---
Desbalanceo Izquierda-Derecha: fb(20) = +2, fb(15) = -1
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER_dark.svg
---
class: only-dark-mode
name: AVLIZQDER
---
Desbalanceo Izquierda-Derecha: fb(20) = +2, fb(15) = -1
```

La solución consiste en dos pasos:

1. **Rotar a la izquierda** el hijo izquierdo del nodo desbalanceado, es decir el (15). Aunque el (15) está dentro del rango permitido, esta rotación alinea los nodos para que el desbalance pase a ser del tipo Izquierda-Izquierda.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-1_light.svg
---
class: only-light-mode
name: AVLIZQDER-1
---
Rotación simple a izquierda del (15)
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-1_dark.svg
---
class: only-dark-mode
name: AVLIZQDER-1
---
Rotación simple a izquierda del (15)
```

Luego de esta primera rotación, el árbol queda con el (17) en la posición que antes ocupaba el (15), y el desbalance ahora es de tipo Izquierda-Izquierda en el (20):

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-2_light.svg
---
class: only-light-mode
name: AVLIZQDER-2
---
Árbol luego de la rotación a izquierda del (15): fb(20) = +2
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-2_dark.svg
---
class: only-dark-mode
name: AVLIZQDER-2
---
Árbol luego de la rotación a izquierda del (15): fb(20) = +2
```

2. **Rotar a la derecha** el nodo desbalanceado (20). El (17) asciende, el (20) pasa a ser su hijo derecho, y el subárbol derecho del (17) (que antes era el (18)) se reubica como hijo izquierdo del (20).

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-3_light.svg
---
class: only-light-mode
name: AVLIZQDER-3
---
Rotación simple a derecha del (20)
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-3_dark.svg
---
class: only-dark-mode
name: AVLIZQDER-3
---
Rotación simple a derecha del (20)
```

Finalmente, el árbol recupera el equilibrio:

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-4_light.svg
---
class: only-light-mode
name: AVLIZQDER-4
---
Árbol rebalanceado luego de la rotación doble izquierda-derecha
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLIZQDER-4_dark.svg
---
class: only-dark-mode
name: AVLIZQDER-4
---
Árbol rebalanceado luego de la rotación doble izquierda-derecha
```

### Rotación doble derecha-izquierda

El caso simétrico se da cuando la inserción ocurre a la *izquierda* del hijo *derecho* de un nodo. Se requiere una **rotación doble derecha-izquierda**.

Partiendo del árbol original, insertamos el (82) como hijo izquierdo del (83). Esto desbalancea el nodo (80) ($fb = -2$). Su hijo derecho es el (85), que tiene $fb = +1$ (cargado a la izquierda), indicando un desbalance **Derecha-Izquierda**.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERIZQ_light.svg
---
class: only-light-mode
name: AVLDERIZQ
---
Desbalanceo Derecha-Izquierda: fb(80) = -2, fb(85) = +1
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERIZQ_dark.svg
---
class: only-dark-mode
name: AVLDERIZQ
---
Desbalanceo Derecha-Izquierda: fb(80) = -2, fb(85) = +1
```

Para restablecer el balance se podría rotar el (85) a la derecha y luego el (80) a la izquierda, pero también puede pensarse a la rotación doble como un único movimiento: se "tira" del (83) hacia arriba para que sea la nueva raíz del subárbol.

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERIZQ-1_light.svg
---
class: only-light-mode
name: AVLDERIZQ-1
---
Rotación doble derecha-izquierda en un solo paso: el (83) asciende
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERIZQ-1_dark.svg
---
class: only-dark-mode
name: AVLDERIZQ-1
---
Rotación doble derecha-izquierda en un solo paso: el (83) asciende
```

Al ascender el (83):

- El (80), que antes era la raíz, pasa a ser su hijo izquierdo (80 < 83).
- El (85) que antes era el padre del (83) pasa a ser su hijo derecho (85 > 83).
- El subárbol izquierdo del (83), el (82), se reubica como hijo derecho del (80), porque 82 > 80.
- El subárbol izquierdo del (80), el (75), se mantiene como su hijo izquierdo.
- El subárbol derecho del (85), el (90), se mantiene como su hijo derecho.

A continuación se muestra el árbol balanceado luego de la rotación doble:

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERIZQ-2_light.svg
---
class: only-light-mode
name: AVLDERIZQ-2
---
Árbol rebalanceado luego de la rotación doble derecha-izquierda
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-10-arboles-balanceados/AVLDERIZQ-2_dark.svg
---
class: only-dark-mode
name: AVLDERIZQ-2
---
Árbol rebalanceado luego de la rotación doble derecha-izquierda
```

```{admonition} Importante
---
class: important
---
Las rotaciones son operaciones locales que solo afectan a un pequeño número de nodos. Cuando se inserta un nuevo nodo, se asciende por el camino desde la inserción hasta la raíz verificando el balanceo de cada nodo. Ante el primer nodo desbalanceado se realiza la rotación correspondiente, lo que restaura la altura del subárbol a su valor anterior a la inserción. Esto garantiza que los nodos superiores recuperen automáticamente el equilibrio.
```

<div class="only-html">

### Visualizador de árbol AVL interactivo

Ingresar uno o más valores separados por coma y presionar Insertar. Usar "Paso a paso" para avanzar una operación a la vez, o "Reproducir" para ver la secuencia completa automáticamente. Las flechas del teclado adelantan/retroceden paso a paso, y la barra espaciadora inicia/pausa la reproducción.

<div class="only-light-mode">
<iframe src="/applets/3-estructuras-de-datos/3-10-arboles-balanceados/avl-visualizer_light.html" width="100%" height="520px"></iframe>
</div>
<div class="only-dark-mode">
<iframe src="/applets/3-estructuras-de-datos/3-10-arboles-balanceados/avl-visualizer_dark.html" width="100%" height="520px"></iframe>
</div>

</div>

## Implementación

### Estructura del nodo AVL

A diferencia de un ABB, donde los nodos solo almacenan valor y referencias a sus hijos, un nodo AVL necesita información adicional para determinar si el subárbol está balanceado. La estrategia más común es guardar la **altura** de cada nodo, y a partir de ella calcular el factor de balanceo como la diferencia entre las alturas de sus hijos derecho e izquierdo.

```go
type AVLNode[T any] struct {
    value  T
    left   *AVLNode[T]
    right  *AVLNode[T]
    height int
}
```

El factor de balanceo se define como:

```text
fb(n) = altura(hijo_izquierdo) - altura(hijo_derecho)
```

Cuando |fb(n)| > 1, el nodo está desbalanceado y se debe aplicar la rotación correspondiente.

### Actualización de alturas

Cada vez que se modifica la estructura del subárbol (inserción o eliminación), se debe actualizar la altura del nodo. La altura de un nodo vacío (`nil`) es $-1$, y la de un nodo hoja recién creado es $0$, consistente con la definición de altura del capítulo {ref}`arboles`.

```text
altura(n) = 1 + max(altura(hijo_izquierdo), altura(hijo_derecho))
```

Esta actualización debe ocurrir después de cada operación recursiva y después de cada rotación, ya que las rotaciones modifican la estructura del subárbol y por lo tanto las alturas de los nodos involucrados.

### Rotaciones

Las rotaciones simple derecha y simple izquierda son operaciones locales que reestructuran el subárbol manteniendo la propiedad de BST. Ambas deben actualizar las alturas de los nodos que modifican.

Una rotación doble (derecha-izquierda o izquierda-derecha) puede implementarse como la composición de dos rotaciones simples, o como un único movimiento como se explicó en la sección anterior.

### Estrategia de inserción y eliminación

Tanto la inserción como la eliminación siguen el mismo patrón recursivo:

1. Realizar la operación como en un ABB (buscar la posición, insertar o eliminar).
2. Actualizar la altura del nodo actual.
3. Calcular el factor de balanceo.
4. Si está desbalanceado, aplicar la rotación correspondiente.

La estructura del árbol AVL es similar a la del ABB:

```go
type AVLTree[T any] struct {
    root *AVLNode[T]
    size int
    cmp  func(T, T) int
}
```

La función de comparación `cmp` permite trabajar con cualquier tipo de dato. Los métodos públicos delegan en funciones auxiliares recursivas que recorren el árbol desde la raíz.

## Ejercicios

Implementar un árbol AVL en el repositorio
[`data-structures`](https://github.com/untref-ayp2/data-structures),
paquete `avltree/`. El árbol debe mantener la altura en cada nodo y
rebalancearse automáticamente después de cada inserción y eliminación
mediante rotaciones simples y dobles.

La implementación de la eliminación ya está completa; las rotaciones
(`rotateRight`, `rotateLeft`) y la inserción quedan a cargo del estudiante.
