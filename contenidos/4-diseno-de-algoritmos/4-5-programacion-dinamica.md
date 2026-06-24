---
label: programacion-dinamica
---

# Programación Dinámica

La programación dinámica es otra técnica de optimización utilizada para resolver problemas complejos mediante la descomposición en subproblemas más pequeños y su solución incremental, con el objetivo de encontrar la solución óptima global.

A diferencia de los algoritmos ávidos, que toman decisiones locales óptimas en cada paso sin reconsiderarlas, la programación dinámica resuelve todos los subproblemas posibles y combina sus soluciones para construir la solución óptima global.

El problema original se subdivide en subproblemas de menor tamaño y se almacenan sus soluciones para evitar cálculos redundantes. Esto se logra mediante la técnica de **memoización**, que almacena los resultados de los subproblemas ya resueltos, y la técnica de **tabulación**, que construye una tabla para almacenar las soluciones de los subproblemas.

```{admonition} Importante
:class: important

La principal característica de la programación dinámica es que los cálculos se realizan una sola vez y se reutilizan en lugar de volver a calcularlos.
```

La programación dinámica es especialmente útil para problemas de optimización, donde se busca maximizar o minimizar una función objetivo. Se utiliza en una amplia variedad de aplicaciones, como la teoría de grafos, la teoría de juegos, la bioinformática y la economía.

Esta técnica fue concebida para resolver problemas con **subestructura óptima** y **subproblemas superpuestos**.

Subestructura óptima
: Un problema tiene subestructura óptima si su solución óptima puede construirse a partir de soluciones óptimas de sus subproblemas.

Subproblemas superpuestos
: Ocurren cuando un problema puede dividirse en subproblemas que se repiten múltiples veces.

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
:linenos:
:emphasize-lines: 5

func Fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return Fibonacci(n-1) + Fibonacci(n-2)
}
```

En la línea 5 se observa que la función `Fibonacci` se llama a sí misma dos veces, lo que provoca que se realicen cálculos redundantes. Por ejemplo, al calcular `Fibonacci(5)`, se realizan las siguientes llamadas:

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-5-programacion-dinamica/fibonacci-recursivo_light.svg
:name: fibonacci-recursivo-light
:class: only-light-mode

Árbol de llamadas recursivas de Fibonacci(5). Los colores indican cuántas veces se repite cada cálculo.
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-5-programacion-dinamica/fibonacci-recursivo_dark.svg
:name: fibonacci-recursivo-dark
:class: only-dark-mode

Árbol de llamadas recursivas de Fibonacci(5). Los colores indican cuántas veces se repite cada cálculo.
```

Se puede observar que `Fibonacci(5)` y `Fibonacci(4)` se calcularon 1 vez, `Fibonacci(3)` se calculó 2 veces, `Fibonacci(2)` y `Fibonacci(0)` se calcularon 3 veces cada uno, y `Fibonacci(1)` se calculó 5 veces. Esto significa que el tiempo de ejecución del algoritmo es exponencial, lo que lo hace ineficiente para valores grandes de `n`.

A continuación se muestra cómo se construyen los valores utilizando una tabla para almacenar los resultados de los subproblemas:

```{table}
:align: center

| Paso | Valor calculado | Cómo se obtiene              |
| :--: | :------------- | :--------------------------- |
|  0   | `f(0) = 0`     | Caso base: se inicializa la tabla |
|  1   | `f(1) = 1`     | Caso base: se inicializa la tabla |
|  2   | `f(2) = 1`     | `f(1) + f(0) = 1 + 0` (reutiliza valores) |
|  3   | `f(3) = 2`     | `f(2) + f(1) = 1 + 1` (reutiliza valores) |
|  4   | `f(4) = 3`     | `f(3) + f(2) = 2 + 1` (reutiliza valores) |
|  5   | `f(5) = 5`     | `f(4) + f(3) = 3 + 2` (reutiliza valores) |
```

Observar que los valores de `f(0)` y `f(1)` se usan directamente (no hace falta recalcularlos), y cada paso reutiliza los valores ya almacenados en la tabla.

Esta forma de implementar algoritmos por programación dinámica usando una tabla para almacenar los valores se conoce como **tabulación**, en inglés _**Bottom-Up**_.

Se pueden distinguir dos etapas en la tabulación:

Inicialización de la tabla
: Se inicializa una tabla con los valores base de la serie de Fibonacci. Estos valores iniciales son necesarios para calcular los valores posteriores de la serie.

Llenado iterativo de la tabla
: Se van completando los valores de la tabla de forma iterativa, utilizando los valores previamente calculados. En cada iteración, se calcula el valor de `Fibonacci(n)` sumando los dos valores anteriores en la tabla, es decir, `Fibonacci(n-1)` y `Fibonacci(n-2)`. El proceso se repite hasta que se alcanza el valor deseado de `n`.

El resultado final se encuentra en la última celda de la tabla, que contiene el valor de Fibonacci(n). Este enfoque evita la recursión y los cálculos redundantes, lo que mejora significativamente la eficiencia del algoritmo.

En el siguiente fragmento de código se muestra la implementación de la serie de Fibonacci utilizando tabulación:

```{code-block} go
:linenos:

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
- Complejidad espacial: $O(n)$, ya que se utiliza una tabla de tamaño `n+1` para almacenar los resultados de los subproblemas.

## Problema de la mochila (_Knapsack Problem_)

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-5-programacion-dinamica/mochila-problema_light.svg
:name: mochila-light
:class: only-light-mode
:width: 600px

Problema de la mochila
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-5-programacion-dinamica/mochila-problema_dark.svg
:name: mochila-dark
:class: only-dark-mode
:width: 600px

Problema de la mochila
```

El problema de la mochila es un clásico en programación dinámica y se puede enunciar como:

> Dado un conjunto de objetos, cada uno con un peso y un valor, el objetivo es determinar qué objetos se deben incluir en una mochila de capacidad limitada para maximizar el valor total.

Supongamos que tenemos una mochila de capacidad 5 y los siguientes objetos:

```{table}
:align: center
:width: 30%

| Objeto | Peso | Valor |
| :----: | :--: | :---: |
|   1    |  3   |   2   |
|   2    |  4   |   3   |
|   3    |  1   |   4   |
|   4    |  2   |   2   |
|   5    |  5   |   5   |
```

La solución se puede encontrar utilizando nuevamente tabulación. Para ello se construye una tabla con las siguientes características:

- **Cada columna** representa una capacidad posible de la mochila, desde $0$ hasta la capacidad máxima ($w = 5$ en este ejemplo).
- **Cada fila** representa los objetos que se van incorporando de a uno. La fila $i$ corresponde a tener disponibles los primeros $i$ objetos.
- **Cada celda** $(i, w)$ almacena el máximo valor total que se puede obtener usando los $i$ primeros objetos con una mochila de capacidad $w$.

Inicialización de la tabla
: Para poder inicializar la tabla se debe considerar que si no hay objetos o la capacidad de la mochila es 0, el valor máximo que se puede obtener es 0. Por lo tanto, se inicializan la primera fila y la primera columna de la tabla con 0.

La ecuación de recurrencia que determina el valor de cada celda es:

$$
V(i, w) = \begin{cases}
0 & \text{si } i = 0 \text{ o } w = 0 \\
V(i-1, w) & \text{si } p_i \gt w \\
\max(V(i-1, w), v_i + V(i-1, w - p_i)) & \text{si } p_i \leq w
\end{cases}
$$

Donde $p_i$ y $v_i$ son el peso y valor del objeto $i$, $w$ es la capacidad considerada en esa columna, y $V(i, w)$ es el valor máximo alcanzable con los primeros $i$ objetos y capacidad $w$.

La implementación de esta estrategia utilizando tabulación es la siguiente:

```{code-block} go
:linenos:

type Item struct {
    peso  int
    valor int
}

func Mochila(obj []Item, capacidad int) int {
    n := len(obj)
    // Inicialización de la tabla
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, capacidad+1)
    }
    // Llenado iterativo de la tabla
    for i := 1; i <= n; i++ {
        for w := 1; w <= capacidad; w++ {
            if obj[i-1].peso > w {
                dp[i][w] = dp[i-1][w]
            } else {
                sin := dp[i-1][w]
                con := obj[i-1].valor + dp[i-1][w-obj[i-1].peso]
                if con > sin {
                    dp[i][w] = con
                } else {
                    dp[i][w] = sin
                }
            }
        }
    }
    return dp[n][capacidad]
}
```

Como en el caso de Fibonacci, la tabla se inicializa con ceros y se recorre de forma iterativa. En cada celda se aplica la ecuación de recurrencia: si el objeto no entra se hereda el valor de la fila anterior, y si entra se elige el máximo entre no incluirlo e incluirlo.

<div class="only-html">

En el siguiente applet interactivo se muestra cómo se llena la tabla paso a paso. Cada celda $(i, w)$ almacena un par (peso total, valor total) e indica qué celdas previas se utilizaron para calcularlo. Para avanzar, usar los botones ◀ ▶ o las flechas del teclado. Hacer clic en >> para reproducción automática.

<div class="only-light-mode">
<iframe src="/applets/4-diseno-de-algoritmos/4-5-programacion-dinamica/mochila-dp_light.html" width="100%" height="560px"></iframe>
</div>
<div class="only-dark-mode">
<iframe src="/applets/4-diseno-de-algoritmos/4-5-programacion-dinamica/mochila-dp_dark.html" width="100%" height="560px"></iframe>
</div>

</div>

La complejidad temporal y espacial del algoritmo es:

Complejidad temporal
: $O(n \times w)$, donde $n$ es el número de objetos y $w$ es la capacidad de la mochila. Esto se debe a que se recorre la tabla de tamaño $n$ por $w$.

Complejidad espacial
: $O(n \times w)$, ya que se utiliza una tabla de tamaño $n$ por $w$ para almacenar los resultados de los subproblemas.

## Tabulación (_Bottom-Up_) vs. Memoización (_Top-Down_)

La **tabulación** y la **memoización** son dos enfoques diferentes para implementar la programación dinámica, y cada uno tiene sus propias ventajas y desventajas.

### Tabulación (_Bottom-Up_)

Como vimos, la **tabulación** es un enfoque iterativo que construye una tabla y la recorre en orden sistemático. Para el problema de la mochila, se recorre fila por fila y columna por columna, resolviendo todos los subproblemas posibles. El código de la sección anterior sigue exactamente esta estrategia: inicializa `dp[n+1][capacidad+1]` con ceros y los recorre con dos `for` anidados.

### Memoización (_Top-Down_)

La **memoización** ataca el mismo problema desde el otro extremo: en lugar de llenar toda la tabla de abajo hacia arriba, arranca desde el problema original y baja recursivamente hasta los casos base, almacenando los resultados intermedios en una estructura de datos. Si un subproblema ya fue resuelto, se recupera del caché en lugar de recalcularlo.

Aplicada al problema de la mochila, la versión memoizada usa una matriz `memo` inicializada con `-1` para indicar «no calculado aún». La primera llamada es `Mochila(obj, n, capacidad, memo)` y a partir de ahí la recursión desciende hasta `i == 0` o `w == 0`:

```{code-block} go
:linenos:

func Mochila(obj []Item, i int, w int, memo [][]int) int {
    if i == 0 || w == 0 {
        return 0
    }
    if memo[i][w] != -1 {
        return memo[i][w]
    }
    if obj[i-1].peso > w {
        memo[i][w] = Mochila(obj, i-1, w, memo)
    } else {
        sin := Mochila(obj, i-1, w, memo)
        con := obj[i-1].valor + Mochila(obj, i-1, w-obj[i-1].peso, memo)
        if con > sin {
            memo[i][w] = con
        } else {
            memo[i][w] = sin
        }
    }
    return memo[i][w]
}
```

En este caso se utiliza una matriz `memo` inicializada en `-1` para detectar si un subproblema ya fue calculado. Cuando `memo[i][w] != -1` se devuelve el valor cacheado sin expandir la recursión, evitando así repetir cálculos.

En el siguiente applet se puede visualizar el árbol de llamadas recursivas con memoización. Cada nodo representa un subproblema $(i, w)$ donde $i$ es el índice del objeto que se está evaluando y $w$ la capacidad disponible. Los colores indican el estado de cada nodo:

- **Amarillo**: la recursión descendió a este subproblema. El nodo muestra el par $(i, w)$ indicando qué objeto y capacidad se están evaluando. El resultado todavía no se conoce.
- **Verde**: el subproblema ya fue resuelto. El nodo muestra el par (peso total, valor total) óptimo para esa rama.
- **Celeste**: el subproblema ya había sido calculado previamente (cache hit). Se recupera del caché sin expandir la recursión.

<div class="only-html">

<div class="only-light-mode">
<iframe src="/applets/4-diseno-de-algoritmos/4-5-programacion-dinamica/mochila-memo_light.html" width="100%" height="560px"></iframe>
</div>
<div class="only-dark-mode">
<iframe src="/applets/4-diseno-de-algoritmos/4-5-programacion-dinamica/mochila-memo_dark.html" width="100%" height="560px"></iframe>
</div>

</div>

La complejidad de ambas versiones aplicadas al mismo problema es idéntica:

Complejidad temporal
: $O(n \times w)$, tanto para tabulación como para memoización. En tabulación se recorren todas las celdas; en memoización cada celda se calcula una sola vez (la primera que se necesita) y luego se recupera del caché.

Complejidad espacial
: $O(n \times w)$, ya que ambas versiones almacenan la tabla completa de tamaño $(n+1) \times (w+1)$.

### Comparación

Aunque las complejidades coinciden, los enfoques difieren en aspectos prácticos:

```{table}
:align: center

| Característica             | Tabulación (_Bottom-Up_) | Memoización (_Top-Down_) |
| -------------------------- | ------------------------ | ------------------------- |
| Enfoque                    | Iterativo                | Recursivo                 |
| Orden de llenado           | Por filas, sistemático   | Por demanda, recursivo    |
| Subproblemas calculados    | Todos                    | Solo los necesarios       |
| Complejidad temporal       | $O(n \times w)$          | $O(n \times w)$           |
| Complejidad espacial       | $O(n \times w)$          | $O(n \times w)$           |
```

## Ejercicios

Los ejercicios de este capítulo están en el directorio
[`05-programacion-dinamica/ejercicios/`](https://github.com/untref-ayp2/taller-algoritmos/tree/main/05-programacion-dinamica/ejercicios)
del repositorio
[`taller-algoritmos`](https://github.com/untref-ayp2/taller-algoritmos).
Cada ejercicio tiene un esqueleto con `// TODO` y su correspondiente batería de tests.
Para resolverlos, clonar el repositorio, completar las funciones y ejecutar `go test ./...`.
