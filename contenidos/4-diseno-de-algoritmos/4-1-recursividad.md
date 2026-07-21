---
label: recursividad
---

# Recursividad y División y Conquista

## Recursividad

En programación, la recursividad es una técnica donde **una función se llama a sí misma** dentro de su propia definición. Es como si la función se estuviera "descomponiendo" en versiones más pequeñas del mismo problema, hasta llegar a un **caso tan simple que se puede resolver directamente**.

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-1-recursividad/Recursion.svg
---
width: 70%
---
Matryoshka.
```

Para que la recursión funcione, hay que prestar atención a dos aspectos importantes en el diseño de la función recursiva:

Caso base
: Es el caso más simple y trivial que se puede resolver directamente sin necesidad de llamarse a sí misma nuevamente. La recursión debe llegar a este caso para poder terminar. Si no hay un caso base que corte la recursión, la función se llamará a sí misma indefinidamente y se producirá un error de desbordamiento de pila (_stack overflow_).

Caso recursivo
: Es el punto de la función donde se vuelve a llamar a sí misma, pero siempre con una versión más pequeña del problema original. La recursión debe acercarse al caso base en cada llamada recursiva, si no se producirá un error de desbordamiento de pila.

Como ejemplo podemos escribir una función recursiva para calcular el factorial de un número. Recordemos que el factorial de un número entero positivo `n` se define como:

```{math}
f(n) =
\begin{cases}
n \; (n-1) \; (n-2) \; \cdots \; 1 & \text{si } n > 0 \\
1 & \text{si } n = 0
\end{cases}
```

La definición de factorial es claramente recursiva y se puede implementar en Go de la siguiente manera:

```{code-block} go
---
linenos:
---
emphasize-lines: 6,9
package main

import "fmt"

func factorial(n int) int {
    if n == 0 { // Caso base
        return 1
    }
    return n * factorial(n-1) // Caso recursivo
}

func main() {
    fmt.Println(factorial(4))
}
```

```output
24
```

En la línea 6 se define el caso base, donde el factorial de 0 es 1. En la línea 9 se encuentra la llamada recursiva, donde el factorial de `n` es `n` multiplicado por el factorial de `n-1`. La función se llama a sí misma con un valor más pequeño.

Para entender como funciona la recursión tenemos que observar la pila de ejecución. Si ejecutamos el código anterior, la pila de ejecución se verá de la siguiente manera:

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-1-recursividad/RecursionFactorial_light.svg
---
class: only-light-mode
width: 90%
---
Pila de Ejecución - factorial(4).
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-1-recursividad/RecursionFactorial_dark.svg
---
class: only-dark-mode
width: 90%
---
Pila de Ejecución - factorial(4).
```

La primera llamada que se hace a factorial recibe el valor de `n = 4`. Como `n != 0`, se llama a la función factorial con `n = 3`. Luego se llama a la función con `n = 2`, `n = 1` y finalmente `n = 0`. Cuando la función se llama a sí misma queda bloqueada su ejecución en ese punto, esperando el resultado de la llamada recursiva para continuar. Cuando se llega al caso base y se retorna `1` se retoma la ejecución de la llamada anterior y sucesivamente se van desapilando las llamadas recursivas y se van multiplicando los valores de `n` en cada nivel de la pila. Finalmente se obtiene el resultado de `24`.

### Tipos de recursión

La recursividad, de acuerdo a como las funciones se llaman a sí mismas, se puede clasificar en dos tipos:

Recursión directa
: Es la forma más común de recursión, donde una función se llama a sí misma directamente.

Recursión indirecta
: En este caso, dos o más funciones se llaman entre sí de forma cíclica. Es decir, la función A llama a la función B, que a su vez llama a la función A. Este tipo de recursión es menos común y puede ser difícil de entender y depurar. Incluso puede haber más de dos funciones que se llaman mutuamente.

El ejemplo del cálculo del factorial es un ejemplo de recursión directa, ya que la función `factorial` se llama a sí misma directamente.

A continuación se muestra un ejemplo de recursión indirecta, donde dos funciones se llaman entre sí de forma cíclica. Las funciones son capaces de determinar si el entero dado es par o impar, sin usar divisiones, resto de la división o multiplicaciones. Simplemente llegan hasta el caso base cuando `n == 0` y retornan el valor correspondiente. (Es un ejemplo didáctico, no es la forma más eficiente de determinar si un número es par o impar)

```{code-block} go
---
linenos:
---
emphasize-lines: 5,12
func esPar(n int) bool {
    if n == 0 { // El 0 es par
        return true
    }
    return esImpar(n - 1)
}

func esImpar(n int) bool {
    if n == 0 { // El 0 no es impar
        return false
    }
    return esPar(n - 1)
}
```

En este caso en la línea 5 se llama a la función `esImpar` y en la línea 12 a la función `esPar`. Cada llamada recursiva se realiza siempre con un número menor, de forma tal de acercarse al caso base cuando `n == 0`. De acuerdo si llego al caso base por la primera o la segunda función el valor de retorno será `true` o `false`.

### Cálculo de la complejidad de las funciones recursivas

Para calcular el orden de las funciones recursivas se debe escribir la ecuación de recurrencia que describe el tiempo de ejecución de la función. En el caso de factorial por ejemplo tenemos que:

```{math}
T(n) = T(n-1) + O(k)
```

Donde $T(n)$ es el tiempo de ejecución de la función factorial para un valor $n$. La función `factorial` se llama a sí misma con un valor más pequeño, $n-1$, por lo que aparece el término $T(n-1)$, el resto de las operaciones son constantes y se representant con el término $O(k)$.

Aplicando la ecuación de recurrencia podemos calcular $T(n-1)$

```{math}
T(n-1) = T(n-2) + O(k)
```

Si sustituimos la ecuación anterior en la ecuación original obtenemos:

```{math}
T(n) = T(n-2) + 2 \; O(k)
```

Por lo tanto, en el paso $i$-ésimo tendremos que:

```{math}
T(n) = T(n-i) + i \; O(k)
```

Finalmente en la última llamada tendremos:

```{math}
T(n) = T(0) + n \; O(k)
```

como $T(0) = O(1)$, porque no se realiza ninguna llamada recursiva, sino que se resuelve por el caso base, entonces la complejidad de la función factorial es:

```{math}
T(n) = n \; O(k) + O(1) = O(n)
```

## División y Conquista

División y conquista, también conocida como divide y vencerás, es una técnica de diseño de algoritmos, muy vinculada a la recursividad, que se utiliza para resolver problemas que generalmente manipulan una gran cantidad de datos y que consiste aplicar tres pasos:

Dividir
: El problema original se divide en subproblemas más pequeños y manejables. Los subproblemas deben ser de la misma naturaleza que el problema original, pero de menor tamaño. Todos los subproblemas deben tener aproximadamente el mismo tamaño.

Conquistar
: Los subproblemas se resuelven por separados, generalmente de forma recursiva.

Combinar
: Las soluciones de los subproblemas deben combinarse para obtener la solución del problema original.

No todos los problemas se pueden resolver de esta manera, pero aquellos que sí, suelen ser más fáciles de entender y de implementar.

A modo de ejemplo vamos a implementar el algoritmo de búsqueda binaria, que es un algoritmo de búsqueda eficiente para encontrar un elemento específico en un arreglo ordenado. La búsqueda binaria divide el arreglo en mitades y compara el valor buscado con el elemento en el índice medio del arreglo. Si el valor buscado es menor que el elemento en el medio, la búsqueda se realiza en la mitad izquierda del arreglo. Si el valor buscado es mayor, la búsqueda se realiza en la mitad derecha del arreglo. Este proceso se repite hasta que el valor buscado se encuentre o el rango de búsqueda se reduzca a cero.

```{admonition} Importante
---
class: important
---
Las partes en la que se subdivide la entrada de datos original deben ser aproximadamente iguales. En el caso de la búsqueda binaria, si el tamaño del arreglo original era impar, entonces una mitad tendrá un elemento más que la otra, lo cual no afecta a la aplicación de esta técnica.

Esta técnica permite reducir drásticamente el tiempo de ejecución, es decir el orden de la función.
```

```{code-block} go
---
linenos:
---
emphasize-lines: 2,6,9,13
func busquedaBinaria(array []int, inicio int, fin int, x int) int {
    if inicio > fin {
        return -1
    }

    medio := (inicio + fin) / 2

    if array[medio] > x {
        return busquedaBinaria(array, inicio, medio-1, x)
    }

    if array[medio] < x {
        return busquedaBinaria(array, medio+1, fin, x)
    }

    return medio
}
```

Dividir
: En la linea 6 se calcula el medio que parte al arreglo de tamaño $n$ en dos mitades de aproximadamente el mismo tamaño.

Conquistar
: Si el valor buscado se encuentra en la mitad inferior se realiza la llamada recursiva de la línea 9, en cambio si es mayor se realiza la llamada recursiva de la línea 13. Se realiza sólo una de las llamadas, no ambas.

Combinar
: En este ejemplo donde se busca un valor, la construcción del resultado final es trivial, ya que si en alguna de las llamadas recursivas se encuentra el elemento buscado, se devuelve el índice que se propaga debido a los `return` que acompañan a las llamadas recursivas en las líneas 9 y 13.

Caso base
: Como toda función recursiva debe tener un caso base para impedir que la recursión se desborde. En la búsqueda binaria podemos pensar el caso base como aquel en el que no se encuentra el número buscado y se reduce a 0 el espacio de búsqueda. Se puede ver en la línea 2 cuando `inicio > fin`.

### Teorema maestro

El cálculo del orden de las funciones recursivas, en particular de las funciones que aplican la técnica de división y conquista, puede ser complicado de realizar. Por suerte el **Teorema maestro** permite agilizar el cálculo a partir de la siguiente observación:

La ecuación de recurrencia de una función recursiva que aplica la técnica de división y conquista será:

```{math}
T(n) = a \; T \left( \frac{n}{b} \right) + O(n^c)
```

Donde

$b$
: Cantidad de partes iguales en la que se subdivide el problema original.

$a$
: Cuantos de los subproblemas se resuelven efectivamente.

$c$
: $O(n^c)$ es el costo de partir o subdividir el problema original más el costo de combinar las soluciones parciales.

El Teorema maestro establece que la solución a la ecuación de recurrencia es:

```{math}
---
label: teorema-maestro
---
T(n) =
\begin{cases}
O(n^c) & \text{si } \log_b(a) < c \\
O(n^c \; \log_b(n)) & \text{si } \log_b(a) = c \\
O(n^{log_b(a)}) & \text{si } \log_b(a) > c
\end{cases}
```

En el caso de la búsqueda binaria tenemos que:

```{math}
a = 1 \\
b = 2 \\
c = 0
```

por lo tanto, como $\log_2{1}=0$ estamos en el segundo caso

```{math}
T(n) = O(\log_2{n})
```

## Ejercicios

Los ejercicios de este capítulo están en el directorio
`01-recursividad/ejercicios/`
del repositorio
`taller-algoritmos`.
Cada ejercicio tiene un esqueleto con `// TODO` y su correspondiente batería de tests.
Para resolverlos, clonar el repositorio, completar las funciones y ejecutar `go test ./...`.
