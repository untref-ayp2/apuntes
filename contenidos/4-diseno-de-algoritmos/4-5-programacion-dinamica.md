---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Programación Dinámica

La programación dinámica es una otra técnica de optimización utilizada para resolver problemas complejos mediante la descomposición en subproblemas más pequeños y su solución incremental, con el objetivo de encontrar la solución óptima global.

A diferencia de los algoritmos ávidos, que toman decisiones locales óptimas en cada paso, la programación dinámica considera todas las soluciones posibles y elige la mejor en cada paso, garantizando así que la solución final sea óptima.

La programación dinámica divide el problema general en subproblemas más simples y almacena sus soluciones para evitar cálculos redundantes. Esto se logra mediante la técnica de **memorización**, que almacena los resultados de los subproblemas ya resueltos, y la técnica de **tabulación**, que construye una tabla para almacenar las soluciones de los subproblemas.

Esta técnica es especialmente útil para problemas con **subestructura óptima** y **subproblemas superpuestos**.

Subestructura óptima 
: Un problema tiene subestructura óptima si su solución óptima puede construirse a partir de soluciones óptimas de sus subproblemas. 

Subproblemas superpuestos
: Ocurren cuando un problema puede dividirse en subproblemas que se repiten múltiples veces

##  Problema de la mochila (_Knapsack Problem_)

El problema de la mochila es un clásico en programación dinámica y se puede enunciar como:

> Dado un conjunto de objetos, cada uno con un peso y un valor, el objetivo es determinar la cantidad de cada objeto a incluir en una mochila de capacidad limitada para maximizar el valor total.

La mochila tiene un límite de peso que puede cargar debido a su capacidad y lo que se pretende es encontrar la combinación de objetos a incluir en la mochila con el fin de maximizar el valor total de los objetos que se pueden llevar.

Supongamos que tenemos una mochila de capacidad 5 y los siguientes objetos:

:::{Table}
:align: center
:width: 30%

| Objeto | Peso | Valor |
|:------:|:----:|:-----:|
| 1      | 3    | 2     |
| 2      | 4    | 3     |
| 3      | 1    | 4     |
| 4      | 2    | 2     |
| 5      | 5    | 5     |
:::

La solución se puede encontrar utilizando un enfoque de programación dinámica, donde se construye una tabla que almacena el valor máximo que se puede obtener para cada capacidad de la mochila y cada objeto.

A continuación se presenta la ecuación de recurrencia que se utiliza para llenar la tabla:

```{math}
V(i, w) = \begin{cases}
0 & \text{si } i = 0 \text{ o } w = 0 \\
V(i-1, w) & \text{si } p_i > w \\
\max(V(i-1, w), v_i + V(i-1, w - p_i)) & \text{si } p_i \leq w
\end{cases}
```
Donde:
- $V(i, w)$ es el valor máximo que se puede obtener con los primeros $i$ objetos y una capacidad de mochila $w$.
- $p_i$ es el peso del objeto $i$.
- $v_i$ es el valor del objeto $i$.
- $w$ es la capacidad de la mochila.
- $i$ es el índice del objeto actual.
- $V(i-1, w)$ es el valor máximo sin incluir el objeto $i$.
- $V(i-1, w - p_i)$ es el valor máximo al incluir el objeto $i$ y restar su peso de la capacidad de la mochila.
- $\max$ es la función que devuelve el valor máximo entre dos opciones.
La celda $V(i, w)$ representa el valor máximo que se puede obtener con los primeros $i$ objetos y una capacidad de mochila $w$.

En el siguiente video se muestra cómo se llena la tabla para el problema de la mochila:

<!-- markdownlint-disable MD033 -->
<p class="align-center">
  <video src="../_static/videos/Mochila.mp4" width="100%"controls autoplay></video>
</p>
<!-- markdownlint-enable MD033 -->
Las columnas representan la capacidad de la mochila, que va desde 0 hasta la capacidad máxima de la mochila, y las filas representan los objetos disponibles.

La primera fila y la primera columna de la tabla se inicializan con 0, ya que si no hay objetos o la capacidad de la mochila es 0, el valor máximo que se puede obtener es 0. Esta inicialización se realiza para facilitar el llenado de la tabla ya que se pueden calcular independientemente de los objetos y de la capacidad de la mochila, por lo que sirven como una iniaciliazación de la tabla.

El resto de la tabla se llena iterativamente considerando que para cada celda se tiene la opción de incluir o no incluir el objeto actual. Si se incluye el objeto, se resta su peso de la capacidad de la mochila y se suma su valor al valor máximo obtenido con los objetos restantes. Si no se incluye el objeto, se mantiene el valor máximo obtenido sin incluirlo.

En cada posición de la tabla se almacenan dos valores, el superior corresponde al peso máximo que se puede obtener y el inferior al valor máximo correspondiente.

La decisión de incluir o no incluir el objeto se basa en la comparación entre el valor máximo obtenido al incluir el objeto y el valor máximo obtenido sin incluirlo. La celda correspondiente se llena con el valor máximo de ambas opciones.
