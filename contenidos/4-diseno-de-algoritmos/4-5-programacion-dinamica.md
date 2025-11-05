---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Programación Dinámica

La programación dinámica es otra técnica de optimización utilizada para resolver problemas complejos mediante la descomposición en subproblemas más pequeños y su solución incremental, con el objetivo de encontrar la solución óptima global.

A diferencia de los algoritmos ávidos, que toman decisiones locales óptimas en cada paso, la programación dinámica considera todas las soluciones posibles y elige la mejor en cada paso, garantizando así que la solución final sea óptima.

El problema original se subdivide en subproblemas de menor tamaño y se almacenan sus soluciones para evitar cálculos redundantes. Esto se logra mediante la técnica de **memorización**, que almacena los resultados de los subproblemas ya resueltos, y la técnica de **tabulación**, que construye una tabla para almacenar las soluciones de los subproblemas.

```{Important}
La principal característica de la programación dinámica es que los cálculos se realizan una sola vez y se reutilizan en lugar de volver a calcularlos.
```

La programación dinámica es especialmente útil para problemas de optimización, donde se busca maximizar o minimizar una función objetivo. Se utiliza en una amplia variedad de aplicaciones, como la teoría de grafos, la teoría de juegos, la bioinformática y la economía.

Esta técnica fue concebida para resolver problemas con **subestructura óptima** y **subproblemas superpuestos**.

Subestructura óptima
: Un problema tiene subestructura óptima si su solución óptima puede construirse a partir de soluciones óptimas de sus subproblemas.

Subproblemas superpuestos
: Ocurren cuando un problema puede dividirse en subproblemas que se repiten múltiples veces

## Serie de Fibonacci

La serie de Fibonacci puede definirse de la siguiente manera:

$$
F(n) = \begin{cases}
0 & \text{si } n = 0 \\
1 & \text{si } n = 1 \\
F(n-1) + F(n-2) & \text{si } n > 1
\end{cases}
$$

Una posible implementación del cálculo de la serie de Fibonacci utilizando recursión es la siguiente:

```{code-block} go
---
linenos: true
emphasize-lines: 5
---
func Fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return Fibonacci(n-1) + Fibonacci(n-2)
}
```

En la línea 5 se observa que la función `Fibonacci`{l=go} se llama a sí misma dos veces, lo que provoca que se realicen cálculos redundantes. Por ejemplo, al calcular `Fibonacci(5)`{l=go}, se realizan las siguientes llamadas:

```{figure} ../assets/images/programacion-dinamica/fibonacci-recursivo.drawio.svg
---
name: fibonacci-recursivo
class: dark-light
---
Cálculo de la serie de Fibonacci utilizando recursión
```

Se puede observar que `Fibonacci(5)`{l=go} y `Fibonacci(4)`{l=go} se calcularon 1 vez, `Fibonacci(3)`{l=go} se calculó 2 veces, `Fibonacci(2)`{l=go} y `Fibonacci(0)`{l=go} se calcularon 3 veces cada uno, y `Fibonacci(1)`{l=go} se calculó 5 veces. Esto significa que el tiempo de ejecución del algoritmo es exponencial, lo que lo hace ineficiente para valores grandes de `n`{l=go}.

En la siguiente animación se muestra como se pueden reutilizar los resultados utilizando una tabla para almacenar los resultados de los subproblemas:

<p class="align-center">
  <video src="../_static/videos/Fibonacci.mp4" width="100%" controls autoplay loop></video>
</p>

Esta forma de implementar algoritmos por programación dinámica usando una tabla para almacenar los valores se conoce como **tabulación**, en inglés _**Bottom/Up**_.

Se pueden distinguir dos etapas en la tabulación:

Inicialización de la tabla
: Se inicializa una tabla con los valores base de la serie de Fibonacci. Estos valores iniciales son necesarios para calcular los valores posteriores de la serie.

Llenado Iterativo de la tabla
: Se van completando los valores de la tabla de forma iterativa, utilizando los valores previamente calculados. En cada iteración, se calcula el valor de `Fibonacci(n)`{l=go} sumando los dos valores anteriores en la tabla, es decir, `Fibonacci(n-1)`{l=go} y `Fibonacci(n-2)`{l=go}. El proceso se repite hasta que se alcanza el valor deseado de `n`{l=go}.

El resultado final se encuentra en la última celda de la tabla, que contiene el valor de Fibonacci(n). Este enfoque evita la recursión y los cálculos redundantes, lo que mejora significativamente la eficiencia del algoritmo.

En el siguiente fragmento de código se muestra la implementación de la serie de Fibonacci utilizando tabulación:

```{code-block} go
---
linenos: true
---
func Fibonacci(n int) int {
    // Inicialización de la tabla
    fib := make([]int, n+1)
    fib[0] = 0 // no hace falta inicializarlo, pero es una buena práctica
    fib[1] = 1

    // Llenado iterativo de la tabla
    for i := 2; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2]
    }

    return fib[n]
}
```

En este caso donde la tabla es en realidad un arreglo, se puede estimar la complejidad temporal y espacial del algoritmo:

- Complejidad temporal: $O(n)$, ya que se realiza un solo recorrido a través de la tabla.
- Complejidad espacial: $O(n)$, ya que se utiliza una tabla de tamaño `n+1`{l=go} para almacenar los resultados de los subproblemas.

## Problema de la mochila (_Knapsack Problem_)

```{Figura} ../assets/images/Mochila00.svg
---
width: 600px
name: mochila
---
Problema de la mochila
```

El problema de la mochila es un clásico en programación dinámica y se puede enunciar como:

> Dado un conjunto de objetos, cada uno con un peso y un valor, el objetivo es determinar que objetos se deben incluir en una mochila de capacidad limitada para maximizar el valor total.

Supongamos que tenemos una mochila de capacidad 5 y los siguientes objetos:

```{Table}
---
align: center
width: 30%
---
| Objeto | Peso | Valor |
| :----: | :--: | :---: |
|   1    |  3   |   2   |
|   2    |  4   |   3   |
|   3    |  1   |   4   |
|   4    |  2   |   2   |
|   5    |  5   |   5   |
```

La solución se puede encontrar utilizando nuevamente tabulación, donde se construye una tabla que almacena el valor máximo que se puede obtener para cada capacidad de la mochila y cada objeto.

A continuación se presenta la ecuación de recurrencia que se utiliza para llenar la tabla:

$$
V(i, w) = \begin{cases}
0 & \text{si } i = 0 \text{ o } w = 0 \\
V(i-1, w) & \text{si } p_i \gt w \\
\max(V(i-1, w), v_i + V(i-1, w - p_i)) & \text{si } p_i \leq w
\end{cases}
$$

Donde:

$V(i, w)$
: es el valor máximo que se puede obtener con los primeros $i$ objetos y una capacidad de mochila $w$.

$p_i$
: es el peso del objeto $i$.

$v_i$
: es el valor del objeto $i$.

$w$
: es la capacidad de la mochila.

$i$
: es el índice del objeto actual.

$V(i-1, w)$
: es el valor máximo, para una mochila de capacidad $w$, sin incluir el objeto $i$.

$V(i-1, w - p_i)$
: es el valor máximo al incluir el objeto $i$ y restar su peso de la capacidad de la mochila.

La celda $V(i, w)$ representa el valor máximo que se puede obtener con los primeros $i$ objetos y una capacidad de mochila $w$.

Inicialización de la tabla
: Para poder inicializar la tabla se debe considerar que si no hay objetos o la capacidad de la mochila es 0, el valor máximo que se puede obtener es 0. Por lo tanto, se inicializan la primera fila y la primera columna de la tabla con 0.

Llenado iterativo de la tabla
: Se llena la tabla iterativamente considerando que para cada celda se tiene la opción de incluir o no incluir el objeto actual. Si se incluye el objeto, se resta su peso de la capacidad de la mochila y se suma su valor al valor máximo obtenido con los objetos restantes. Si no se incluye el objeto, se mantiene el valor máximo obtenido sin incluirlo.

Cómo se pretende maximizar el valor total, pero restringidos por la capacidad máxima de la mochila, es decir por el peso de los objetos, en cada se pueden almacenar dos valores: el peso máximo que se puede obtener y el valor máximo correspondiente.

En la siguiente animación se muestra cómo se llena la tabla para una capacidad de mochila de 5 y los objetos dados anteriormente. En cada posición de la tabla se almacenan dos valores, el superior corresponde al peso máximo que se puede obtener y el inferior al valor máximo correspondiente.:

<p class="align-center">
  <video src="../_static/videos/Mochila.mp4" width="100%"controls autoplay></video>
</p>

La decisión de incluir o no incluir el objeto se basa en la comparación entre el valor máximo obtenido al incluir el objeto y el valor máximo obtenido sin incluirlo. La celda correspondiente se llena con el valor máximo de ambas opciones.

La complejidad temporal y espacial del algoritmo es:

Complejidad temporal
: $O(n \times w)$, donde $n$ es el número de objetos y $w$ es la capacidad de la mochila. Esto se debe a que se recorre la tabla de tamaño $n$ por $w$.

Complejidad espacial
: $O(n \times w)$, ya que se utiliza una tabla de tamaño $n$ por $w$ para almacenar los resultados de los subproblemas.

## Tabulación (_Bottom_/_Up_) vs. Memorización (_Top_/_Down_)

La **tabulación** y la **memorización** son dos enfoques diferentes para implementar la programación dinámica, y cada uno tiene sus propias ventajas y desventajas.

Como vimos la **tabulación**, es un enfoque más iterativo que utiliza una tabla para almacenar los resultados de todos los subproblemas desde el principio. Esto significa que se resuelven todos los subproblemas de manera sistemática y se almacenan en la tabla.

A diferencia de la **tabulación**, la **memorización** utiliza recursión para resolver el problema y almacena los resultados de los subproblemas en alguna estructura de datos conveniente, por ejemplo un diccionario o una tabla, a medida que se van calculando. Esto significa que se resuelven los subproblemas solo cuando son necesarios, lo que puede ser más eficiente en algunos casos.

La **memorización** es útil cuando el problema tiene una estructura de árbol, donde algunos subproblemas se resuelven varias veces. Por ejemplo en el caso de la serie de Fibonacci, donde se realizan múltiples llamadas recursivas a los mismos subproblemas.

En el siguiente fragmento de código se muestra la implementación de la serie de Fibonacci utilizando memorización:

```{code-block} go
---
linenos: true
---
func Fibonacci(n int, memo map[int]int) int {
    if n <= 1 {
        return n
    }
    if val, ok := memo[n]; ok {
        return val
    }
    memo[n] = Fibonacci(n-1, memo) + Fibonacci(n-2, memo)
    return memo[n]
}
```

En este caso, se utiliza un mapa `memo`{l=go} para almacenar los resultados de los subproblemas a medida que se van calculando. Si el resultado ya está en el mapa, se devuelve directamente sin volver a calcularlo.

La complejidad temporal y espacial del algoritmo es:

Complejidad temporal
: $O(n)$, ya que cada subproblema se resuelve una sola vez y se almacena en el mapa.

Complejidad espacial
: $O(n)$, ya que se utiliza un mapa de tamaño $n$ para almacenar los resultados de los subproblemas.

En la siguiente tabla se resumen las diferencias entre ambos enfoques:

```{Table}
---
align: center
---
| Característica             | Tabulación (_Bottom_/_Up_) | Memorización (_Top_/_Down_) |
| -------------------------- | ------------------------ | ------------------------- |
| Enfoque                    | Iterativo                | Recursivo                 |
| Inicialización             | Tabla                    | Estructura de datos       |
| Almacenamiento             | Tabla                    | Estructura de datos       |
| Resolución de subproblemas | Todos los subproblemas   | Solo los necesarios       |
| Complejidad temporal       | $O(n \times w)$          | $O(n)$                    |
| Complejidad espacial       | $O(n \times w)$          | $O(n)$                    |
```

En algunos casos la **tabulación** puede ser más fácil de implementar y entender, mientras que la **memorización** puede ser más eficiente en términos de tiempo de ejecución. La elección entre ambos enfoques depende del problema específico y de las preferencias del programador.

## Ejercicios

1. Modificar el algoritmo de la serie de Fibonacci por tabulación para que utilice un arreglo de tamaño 2 en lugar de un arreglo de tamaño `n+1`{l=go}. Esto se puede lograr utilizando dos variables para almacenar los dos últimos valores de la serie y actualizarlos en cada iteración.

2. Implementar el problema de la mochila utilizando memorización. Dado un conjunto de objetos con peso y valor, y una capacidad de mochila, el objetivo es determinar el valor máximo que se puede obtener al incluir los objetos en la mochila. Utilizar un mapa para almacenar los resultados de los subproblemas a medida que se van calculando.

   ```{Admonition} Pista
   ---
   class: tip
   ---
   Se puede utilizar una función recursiva que tome como parámetros el índice del objeto actual, la capacidad restante de la mochila y un mapa para almacenar los resultados de los subproblemas. La función debe considerar dos casos: incluir el objeto actual o no incluirlo, y devolver el valor máximo obtenido en ambos casos.
   ```

3. Implementar el problema de la subcadena común más larga (Longest Common Subsequence) utilizando programación dinámica. Dado dos cadenas de caracteres, el objetivo es encontrar la longitud de la subcadena común más larga entre ellas. Por ejemplo, para las cadenas `"AGGTAB"`{l=go} y `"GXTXAYB"`{l=go}, la subcadena común más larga es `"GTAB"`{l=go} y su longitud es 4.

4. Implementar el problema de la suma de subconjuntos (Subset Sum Problem) utilizando programación dinámica. Dado un conjunto de números enteros y un número objetivo, el objetivo es determinar la cantidad de subconjuntos de los números que sume exactamente el número objetivo. Por ejemplo, para el conjunto `{3, 34, 4, 12, 5, 2}` y el número objetivo `9`, hay 2 subconjuntos que suman `9`: `{4, 5}` y `{3, 4, 2}`.
