---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Árboles Binarios de Búsqueda Balanceados

Una de las propiedades fundamentales de los árboles binarios de búsqueda es que preservan al orden de los elementos, y por lo tanto se pueden usar como contenedores de datos para implementar estructuras más complejas que requieran mantener el orden de los elementos, como por ejemplo diccionarios, listas ordenadas, etc.

La eficiencia de las operaciones de búsqueda, inserción y eliminación en un árbol binario de búsqueda depende en gran medida de su altura. En el peor de los casos, un árbol binario de búsqueda puede degenerar en una lista enlazada, lo que resulta en un tiempo de operación lineal O(n). Para evitar esto, se utilizan árboles binarios de búsqueda balanceados, que mantienen la altura del árbol en un nivel logarítmico O(log n) al garantizar que la diferencia entre las alturas de los subárboles izquierdo y derecho sea mínima.

Existen diferentes tipos de árboles binarios de búsqueda balanceados, como los árboles AVL y los árboles rojo y negro. Estos árboles implementan diferentes algoritmos de balanceo para garantizar que la altura del árbol se mantenga equilibrada después de cada operación de inserción o eliminación.

## Árboles AVL

Un árbol AVL es un ABB **autobalanceado** lo que signfica que es capaz de mantenerse equilibrado.


```{admonition} Definición de Árbol Binario de Búsqueda Balanceado
````{math}
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
````
```

