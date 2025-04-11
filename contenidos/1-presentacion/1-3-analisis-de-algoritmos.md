---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Análisis de Algoritmos

Como ya mencionamos antes, podemos entender a un algoritmo como un método para
resolver un problema dado en una computadora. Un algoritmo describe los pasos
que se deben seguir para alcanzar el resultado buscado.

Para un problema cualquiera, puede existir más de un algoritmo que lo resuelva.
Un algoritmo puede consumir más o menos recursos que otro que resuelve el mismo
problema, por lo tanto una de las principales variable de análisis generalmente
es la **eficiencia** en el uso de los recursos.

:::{note}
Los recursos que consumen un algoritmo son tiempo y espacio (memoria). El mismo
problema se puede resolver, en la misma computadora, en minutos o en años, de
acuerdo al algoritmo que se implemente.
:::

Otro aspecto a tener en cuenta al analizar algoritmos es la **simplicidad**. Un
algoritmo simple es más fácil de entender, adaptar y mantener, por eso a veces
prima la simplicidad a la hora de elegir un algoritmo.

La **simplicidad** y la **eficiencia** no son conceptos antagónicos. Es decir un
algoritmo puede ser simple y eficiente a la vez. Estas métricas sirven
principalmente para comparar algoritmos entre sí y así poder elegir el más
adecuado para una situación concreta.

## Complejidad

:::{admonition} Definición
La **complejidad** es una propiedad de un algoritmo que nos indica como escala
la cantidad de recursos que se necesitan a medida que aumenta el volumen de los
datos.
:::

En esta definición de **complejidad** entra en juego una variable más, la
cantidad o el tamaño de los datos, por ejemplo si tenemos que ordenar pocos
datos, y rara vez se agregan nuevos datos o se modifican los existentes, quizás
prime la simplicidad del algoritmo a la hora de elegir alguno de los algoritmos
de ordenamiento, pero si tenemos que ordenar millones de datos, donde además se
agregan cientos o miles de datos y se modifican otros muy frecuentemente, es
probable que nos interese analizar cuanto tiempo va a demorar y cuanta memoria o
espacio en disco vamos a necesitar y más aún, cuánto más necesitaremos a medida
que aumente el volumen de datos, es decir es probable que prime la
**eficiencia** a la hora de elegir.

Informalmente hablando, cuanto mayor sea la **complejidad** de un algoritmo,
será menos **eficiente** en el uso de los recuros.

La **complejidad** es independiente del hardware o la máquina donde se ejecuta
el algoritmo. No debemos confundir **complejidad** con **rendimiento**.

:::{note}
El **rendimiento** es la capacidad de una computadora para realizar una
determinada tarea en un tiempo dado
:::

El **rendimiento** si depende del hardware. Por ejemplo en la medida que aumenta
la velocidad del procesador, se necesitará menos tiempo para completar una tarea
dada. En cambio la **complejidad** nos indica cuanto más tiempo o memoria va a
requerir el algoritmo en función del tamaño de los datos.

:::{admonition} El mito de la computadora todopoderosa
Muchas veces se cae en la tentación de pensar que a medida que aumente la
capacidad de procesamiento de las computadoras se podrá completar cualquier
tarea en un tiempo aceptable. Esta afirmación es una falacia. Existen problemas
muy bien conocidos que resultan intratables para las computadoras, es decir, que
no importa que tanto aumente la capacidad de procesamiento, una pequeño aumento
en el tamaño de los datos implica que el tiempo de ejecución aumente
desmesuradamente, hasta el punto de hacer inviable el cálculo.
:::

En esta primera aproximación al estudio del análisis de algoritmos, nos vamos a
enfocar en la **complejidad temporal**. Como la complejidad temporal es una
métrica independiente del hardware donde se ejecuta el programa, normalmente se
estima contando la cantidad de operaciones elementales que realiza el algoritmo
bajo análisis para completar el cálculo, teniendo en cuenta que cada unidad
elemental requiere una cantidad fija de tiempo, que por simplicidad se asume
como una unidad de tiempo.

Como la cantidad de operaciones elementales que debe realizar depende de los
datos, se toma siempre el peor caso, para poder obtener una cota confiable. Por
ejemplo si hay que buscar un elemento en un arreglo desdordenado, no queda otra
que buscar el elemento en todas las posiciones del arreglo. En el peor caso se
deberá recorrer todo el arreglo para encontrar el elemento en la última
posición escrutada o poder concluir que el elemento no se encuentra, es
probable que si ejecutamos nuestro algoritmo muchas veces, algunas veces lo
encuentre antes de recorrer todo el arreglo, pero como buscamos una cota, **se
toma siempre el peor caso.**

## Cota Superior Asintótica (O grande)

La cota superior asintótica, O grande o _Big-O_ en inglés, es parte de la
familia de notaciones asintóticas, también conocidas como notaciones de
Bachmann-Landau. En ciencias de la computación, la O grande, permite clasificar
a los algoritmos de acuerdo a como aumenta la cantidad de recursos que necesita
en la medida que aumenta el tamaño de la entrada, es decir nos permite
clasificar algoritmos en el límite, cuando el tamaño de la entrada tiende a
infinito. Sea $T(n)$ la función que indica cuanto tiempo va a tardar un
algoritmo en función del tamaño de la entrada $n$, donde $n$ es un número
natural, entonces:

:::{admonition} Definición
$$
T(n) = O(f(n)) \; \textrm{si} \; \exists \; c, \; n_0 \; \textrm{tal que} \; T(n) \leq c \cdot f(n), \; \forall n > n_0
$$

donde $c$ es una constante positiva y $n_0$ un número natural.
:::

Esto quiere decir que la tasa de crecimiento de $T(n)$ es menor o igual a la
tasa de crecimiento de $f(n)$. Es decir la tasa de crecimiento de $T(n)$ está
acotada por arriba por $f(n), \; \forall n > n_0$.

Por ejemplo, si tenemos la función $T(n) = 4 n + 1$, se verifica que es de la
familia de $O(n)$, es decir la tasa de crecimiento de $T(n)$ está acotada por
$f(n) = n$, ya que:

$\exists \; c = 5, \; n_0 = 1$

tal que:

$5 n \ge 4 n + 1, \; \forall n \ge 1$

:::{figure} ../assets/images/funcion_acotada.svg
---

name: funcion-acotada
---

Función Acotada: $T(n) \subset O(n)$
:::

A continuación se muestran algunas tasas de crecimiento de las
funciones que comunmente se encuentran al calcular la O grande.

:::{figure} ../assets/images/comparacion_funciones.svg
---

name: tasa-crecimiento
---

Comparación de tasas de crecimiento
:::

En la siguiente tabla se muestran algunas de las funciones más comunes y sus
nombres

| Orden | Nombre |
| :---: | :---: |
| $O(1)$ | constante |
| $O(log_2(n))$ | logaritmica |
| $O(n)$ | lineal |
| $O(n \cdot log_2(n))$ | casi lineal |
| $O(n^2)$ | cuadrática |
| $O(n^n)$ | exponencial |

### Propieadades de la O grande

:::{prf:property} Propiedad transitiva
Si,

$$T(n) = O(f(n)) \quad \land \quad f(n) = O(g(n))$$

entonces:

$$T(n) = O(g(n))$$
:::

:::{prf:property}
Si,

$$T(n) = O(f(n)) \quad \land \quad k \ne 0$$

entonces:

$$O(k \, T(n)) = k \cdot O(T(n)) = O(f(n))$$
:::

:::{prf:property} Propiedad de la suma
Si,

$$T_1(n) = O(f(n)) \quad \land \quad T_2(n) = O(g(n))$$

entonces:

$$T_1(n) + T_2(n) = \max(O(f(n)), O(g(n)))$$
:::

:::{prf:property} Propiedad del producto
Si,

$$T_1(n) = O(f(n)) \quad \land \quad T_2(n) = O(g(n))$$

entonces:

$$T_1(n) \cdot T_2(n) = O(f(n) \cdot g(n))$$
:::

:::{prf:property} Propiedad de los polinomios
Si,

$$T(n) = c_k \, n^k + c_{k-1} \, n^{k-1} + \dots + c_1 \, n + c_0$$

es decir $T(n)$ es un polinomio de grado $k$, entonces:

$$T(n) = O(n^k)$$
:::

:::{prf:example} Aplicación de las propiedades de la O grande
$T_1(n)=5 n^2 + 3 = O(n^2)$

$T_2(n)=4 n + 1 = O(n)$

$O(T_1(n) + T_2(n)) = \max(O(n^2), O(n)) = O(n^2)$

$O(T_1(n) \cdot T_2(n)) = O(n^2 \cdot n) = O(n^3)$
:::

## Cálculo de la O grande

Como ya se mencionó, para poder calcular el orden de un algoritmo se necesita
contar cuantas operaciones elementales realiza.

### Operaciones elementales (OE)

:::{note}
Un valor simple, es un valor que se puede representar en un registro de la
computadora y por lo tanto se puede leer y escribir en una única operación, por
ejemplo un número entero de una longitud finita, un número en punto flotante, un
bit, etc. No son valores simples los enteros de longitud indefinida o valores
compuestos, por ejemplo un objeto compuestos por otros otros objetos.
:::

Las operaciones elementales son lo que tienen un costo de 1 es decir cuyo tiempo
de ejecución es 1 (una unidad genérica de tiempo).

Las siguientes son OE:

- Asignación o consulta de una variable simple.
- Operaciones aritméticas elementales de valores simples(suma, resta,
multiplicación, división y resto).
- Comparaciones (mayor, mayor igual, igual, distinto, menor y menor igual).
- Operaciones lógicas (_and_, _or_ y _not_).
- Acceso indexado a un elemento simple de un arreglo.
- Desreferenciar un puntero.

### Operaciones complejas

Por operaciones complejas entendemos a los condicionales, los ciclos y la
ejecución de funciones. Estas operaciones en general pueden anidar otras
operaciones.

:::{card} Condicionales
$$\texttt{if} \; \langle C \rangle \; \texttt{then} \; \langle S_1 \rangle \; \texttt{else} \; \langle S_2 \rangle$$

entonces:

$$T(n) = T(C) + \max(T(S_1), T(S_2))$$
+++
El tiempo de ejecución de un condicional se calcula como el tiempo para evaluar
la condición $C$ más el máximo entre el cuerpo del $\texttt{then}$ y el
$\texttt{else}$, considerando el peor caso de ejecución.
:::

:::{card} Ciclos
$$\texttt{for} \; \langle C \rangle \; \{ \; \langle S \rangle \; \}$$

entonces:

$$T(n) = T(C) + \langle iteraciones \rangle \cdot (T(C) + T(S))$$
+++
El tiempo de ejecución de un ciclo se calcula como el tiempo de evaluar la
condición por primera vez, para ver si se ejecuta el ciclo, mas la cantidad de
iteraciones multiplicado por la suma de evaluar nuevamente la condición en cada
iteración más el tiempo de todas las sentencias del cuerpo del ciclo.
:::

:::{card} Ejecución de Funciones
$$F(P_1, P_2, P_3, \dots, P_n) \; \{ \; \langle S \rangle \; \}$$

entonces:

$$T(n) = 1 + T(P_1) + T(P_2) + T(P_3) + \dots +T(P_n) + T(S)$$
+++
El tiempo de ejecución de una función se calcula como 1 (operación elemental de
llamar a la función) más el tiempo de evaluar cada uno de los parámetros, más el
tiempo de ejecutar todas las instrucciones en el cuerpo de la función.
:::

### Ejemplos de cálculo

:::::{prf:example} Cálculo de O en la búsqueda lineal
> Dado un arreglo de elementos (por simplicidad solo números enteros) y un
elemento a buscar, se debe recorrer todo el arreglo desde la primera posición
hasta la última, hasta encontrar el elemento buscado o determinar que no se
encuentra. Si el elemento se ecuentra en el arreglo, se devuelve la posición del
elemento o -1 en caso contrario.

::::{prf:algorithm} Búsqueda Lineal
**Entrada**

- `lista [n]int`: arreglo de enteros.
- `n int`: longitud del arreglo.
- `elemento int`: número entero a buscar.

**Salida**

- La posición del elemento buscado dentro del arreglo o `-1` si no se encuentra.

:::{code-block} go
:linenos:
pos := 0
for pos < n:
    if lista[pos] == elemento:
        return pos
    pos = pos + 1
return -1
:::
::::

Para calcular el tiempo de ejecución de un algoritmo, conviene empezar por las
operaciones elementales que se encuentran más anidadas. En este ejemplo la línea
4 dentro del condicional es $O(1)$.

Evaluar la condición `pos < n` también es $O(1)$ ya que se trata de accesos a
valores y una comparación, por lo tanto:

$$T(\langle condicional \rangle) = O(1)$$

Entonces dentro del ciclo **mientras** (`for`) tenemos un condicional de $O(1)$
y la instrucción de la línea 5 que son operaciones simples y por lo tanto es
$O(1)$. Podemos concluir que todo el cuerpo del ciclo es $O(1)$.

$$T(\langle ciclo \rangle) = O(1) + n \, O(1) = O(n)$$

ya que evaluar la condición del ciclo, `pos < n`, también es $O(1)$

Las líneas 1 y 6 también son $O(1)$.

$$T(n) = O(1) + O(n) + O(1) = O(n)$$
:::::

:::::{prf:example} Ejemplo del cálculo de O en la búsqueda binaria
> Dado un arreglo de elementos (por simplicidad solo números enteros) que están
**ordenados** y un elemento a buscar, se compara el elemento buscado con el
elemento que se encuentra el medio del arreglo. Si el elemento del medio del
arreglo es menor que elemento buscado, se descarta la primera mitad del arreglo,
en cambio si el elemento del medio es mayor que el elemento buscado, se descarta
la mitad superior del arreglo. Si no es menor ni mayor, entonces es igual y
encontramos el elemento.
>
> La operación se repite hasta que se encuentra el elemento o ya no se puede
seguir partiendo al medio y por lo tanto no se encuentra.

::::{prf:algorithm} Búsqueda Binaria
**Entrada**

- `lista [n]int`: arreglo ordenado de enteros.
- `n int`: longitud del arreglo.
- `elemento int`: número entero a buscar.

**Salida**

- La posición del elemento buscado dentro del arreglo o `-1` si no se encuentra.

:::{code-block} go
:linenos:
L := 0 // primera posición del arregloa
R := n-1 // última posición del arreglo
for L <= R:
    M := (L + R) / 2 // índice del medio del arreglo
    if lista[M] < elemento: // el elemento buscado no puede estar en la primera mitad del arreglo
        L = M + 1
        continue // reinicia el ciclo mientras
    if lista[M] > elemento: // el elemento buscado no puede estar en la mitad superior del arreglo
        R = M - 1
        continue // reinicia el ciclo mientras
    return m // se encontró el elemento buscado
return -1 // no se encontró el elemento
:::
::::

Para analizar la búsqueda binaria, la primera observación que podemos realizar
es que los condicionales son $O(1)$. Siguiendo el mismo razonamiento, todas las
instrucciones que se realizan afuera del ciclo Mientras también son OE. Por lo
tanto podemos plantear la siguiente ecuación de recurrencia:

$$T(n) = T(\frac{n}{2}) + c$$

Donde $T(\frac{n}{2})$ representa que en cada vuelta del ciclo mientras se
descarta la mitad del arreglo. La constante $c$ representa todas las operaciones
$O(1)$ que se realizan en cada vuelta del ciclo. Para resolverla podemos suponer
que `n` es una potencia de 2. Es decir:

$$n = 2^k$$

Reemplazando obtenemos:

Primera vuelta del ciclo
: $$T(n) = T(\frac{2^k}{2}) + c = T(2^{k-1}) + c$$

Segunda vuelta del ciclo
: $$T(n) = T(2^{k-2}) + 2 \, c$$

$$\dots$$

Vuelta $i$ del ciclo
: $$T(n) = T(2^{k-i}) + i \, c$$

entonces para $i = k$

Vuelta $k$ del ciclo
: $$T(n) = T(1) + k \, c$$

$T(0)$ es cuanto cuesta si el arreglo tiene tamaño 0, es dedir `L > R`, y por lo
tanto solo devuelve el -1 de la línea 12. Entonces $T(0) = O(1)$

podemos despejar $k$ de la ecuación $n = 2^k$ y nos queda que $k = log_2(n)$.
Finalmente queda:

$$T(n) = O(1) + c \; log_2(n)$$

$$T(n) = O(log_2(n))$$

Es decir al tener el arreglo ordenado, la búsqueda binaria necesita realizar
mucho menos operaciones que la búsqueda lineal para encontrar el valor buscado o
determinar que no existe. La clave está en descartar la mitad del arreglo en
cada vuelta del ciclo **mientras**.
:::::
