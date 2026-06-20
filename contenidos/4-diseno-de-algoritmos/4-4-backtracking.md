---
label: backtracking
---

# _Backtracking_ (Vuelta Atrás)

_**Backtracking**_ es una técnica algorítmica para resolver problemas donde la solución se construye probando posibilidades paso a paso y descartando caminos inviables. Siempre que el problema tenga solución, con esta técnica la podemos encontrar, ya que explora todas las posibilidades hasta encontrarla, al costo de no ser la más eficiente.

Se utiliza comúnmente en problemas de decisión, combinatoria y optimización donde la solución se puede construir de manera incremental.

La idea es agregar un nuevo elemento a la solución parcial y verificar si es una solución válida. Si no lo es, se descarta y se prueba con otro elemento. Este proceso se repite hasta encontrar la solución o encontrar que no hay más opciones disponibles y por lo tanto no hay solución.

Con esta técnica también se pueden encontrar todas las soluciones posibles a un problema, no solo una. Para ello, se debe modificar el algoritmo para que no termine al encontrar la primera solución, sino que continúe buscando.

## Ejemplo: Problema de las N Reinas

El problema de las N reinas consiste en colocar $N$ reinas en un tablero de ajedrez de $N \times N$ de tal manera que ninguna reina ataque a otra. Esto significa que no pueden estar en la misma fila, columna o diagonal. En la siguiente figura se muestra una solución para el caso de tableros de $8 \times 8$ donde se colocan $8$ reinas.

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-4-backtracking/NReinasSolucion_light.svg
---
width: 60%
name: sol.n.reinas
class: only-light-mode
---
Solución al problema de las $N$ reinas para $N=8$
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-4-backtracking/NReinasSolucion_dark.svg
---
width: 60%
name: sol.n.reinas-dark
class: only-dark-mode
---
Solución al problema de las $N$ reinas para $N=8$
```

Para encontrar una solución posible, la idea es ir colocando una reina en cada fila del tablero, comenzando desde la primera fila. En cada fila se va probando con las distintas columnas, verificando si la posición es válida (no hay otra reina en la misma columna o diagonal). Si se encuentra una posición válida, se coloca la reina y se pasa a la siguiente fila. Si no se encuentra ninguna posición válida en una fila, se vuelve atrás (_backtracking_) y se prueba con otra columna en la fila anterior.

## Algoritmo de _Backtracking_

A continuación se muestra la estructura general de este esquema:

```{code-block} text
---
linenos: true
---
FUNCION backtracking(solucionParcial, ...)
    SI esSolucion(solucionParcial) ENTONCES
        mostrar(solucionParcial)
        SALIR // o continuar buscando si se desea encontrar todas las soluciones
    SINO
        PARA CADA opcion posible de extender solucionParcial HACER
            SI esFactible(opcion) ENTONCES
                registrar(solucionParcial, opcion) // agregar opcion a la solución parcial
                backtracking(solucionParcial, ...) // llamada recursiva
                borrar(opcion, solucionParcial)    // vuelta atrás
            FIN SI
        FIN PARA
    FIN SI
FIN FUNCION
```

<div class="only-html">

El siguiente applet muestra el algoritmo de _backtracking_ resolviendo el problema de las 4 reinas. A la izquierda se ve el tablero con las reinas que se van colocando, y a la derecha el árbol de búsqueda que se expande con cada llamada recursiva. El nodo activo se resalta en amarillo; en rojo se marcan los conflictos y los retrocesos. Usar los botones ◀ ▶ para avanzar paso a paso, o ▶▶ para reproducir la animación automáticamente.

<div class="only-light-mode">
<iframe src="/applets/4-diseno-de-algoritmos/4-4-backtracking/nreinas-backtracking_light.html" width="100%" height="1000px"></iframe>
</div>
<div class="only-dark-mode">
<iframe src="/applets/4-diseno-de-algoritmos/4-4-backtracking/nreinas-backtracking_dark.html" width="100%" height="1000px"></iframe>
</div>

</div>

### Cómo proceder para resolver un problema con _Backtracking_

Para resolver un problema con _backtracking_, se deben identificar y definir los siguientes elementos:

`solucionParcial`
: Determinar una estructura de datos adecuada para representar la solución parcial. Puede ser un vector, una lista, etc. `solucionParcial` debe permitir agregar nuevas opciones y verificar si es una solución válida.

`esSolucion`
: Definir una función que verifique si `solucionParcial` es una solución completa.

`extender`
: Definir una función que tome un `solucionParcial` y devuelva una a una todas las opciones posibles para extenderla. Esta función debe generar todas las combinaciones posibles de extender `solucionParcial`.

`esFactible`
: Definir una función que verifique si una opción es válida para extender `solucionParcial`. Esta función debe verificar si la opción no viola ninguna restricción del problema.

`registrar`
: Definir una función que registre la opción generada con `extender` en la `solucionParcial`. Eventualmente puede ser necesario registrar información adicional de la opción generada.

`borrar`
: Definir una función que borre la última opción registrada en `solucionParcial`. Es decir es el paso opuesto al de `registrar`. Si es necesario también debe restaurar cualquier información extra o de contexto registrada anteriormente.

## Implementación de la solución al problema de las N reinas

`solucionParcial`
: puede ser un arreglo de tamaño $N$ donde las posiciones del arreglo representan las filas y los valores almacenados en cada posición del arreglo representan las columnas. Por ejemplo, para el caso de $N=4$, una solución parcial podría ser $[2, 0, 3, 1]$, lo que significa que hay una reina en la fila $0$ en la columna $2$, una reina en la fila $1$ en la columna $0$, etc.

`esSolucion`
: es una función que verifica si la `solucionParcial` tiene $N$ reinas. En este caso, se verifica si la longitud del arreglo `solucionParcial` es igual a $N$.

`extender`
: con un solo ciclo entre $[0, N)$, podemos generar todas las posibles columnas en la que se puede colocar una reina en la fila $i$.

`esFactible`
: es una función que debe chequear si en la misma columna o en las diagonales hay otras reinas que entren en conflicto con la nueva reina que intentamos agregar al tablero.

: Para chequear si hay ya una reina en la misma columna basta con revisar los valores del arreglo `solucionParcial` para asegurarse que la columna candidata no está atacada por otra reina, es decir no puede haber dos valores iguales en el arreglo y para chequear si hay una reina en alguna de las dos diagonales que se pueden generar en cualquier posición del tablero, se puede usar la propiedad de que en todas las diagonales directas, por nombrarlas de alguna forma, las de color azul, $fila - columna = constante$. Mientras que para las diagonales inversas, las de color rojo, se cumple que $fila + columna = constante$. Ver la figura a continuación.

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-4-backtracking/NReinasDiagonal_light.svg
---
width: 70%
name: sol.n.reinas.diagonal
class: only-light-mode
---
Reinas en la misma diagonal
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-4-backtracking/NReinasDiagonal_dark.svg
---
width: 70%
name: sol.n.reinas.diagonal-dark
class: only-dark-mode
---
Reinas en la misma diagonal
```

El código completo de esta implementación está disponible en el repositorio
[`taller-algoritmos`](https://github.com/untref-ayp2/taller-algoritmos), en el directorio
[`04-backtracking/ejemplos/nreinas/`](https://github.com/untref-ayp2/taller-algoritmos/tree/main/04-backtracking/ejemplos/nreinas).
Allí se puede ejecutar con `go run ./04-backtracking/ejemplos/nreinas/`.

## Análisis de la complejidad computacional

Para entender cuánto tarda un algoritmo de _backtracking_, pensemos en el problema de las N reinas:

- En la primera fila podemos poner una reina en cualquiera de las $N$ columnas → $N$ opciones.
- En la segunda fila, como no puede repetir columna, nos quedan $N-1$ opciones.
- En la tercera fila, $N-2$ opciones, y así sucesivamente.

Por eso, en el peor de los casos el algoritmo prueba $N \times (N-1) \times (N-2) \times \dots \times 1 = N!$ combinaciones. Decimos que su complejidad es $O(N!)$ (orden factorial).

**Pensemos con números concretos:** para $N = 8$, $N! = 40320$ combinaciones. La computadora lo resuelve rápido. Pero para $N = 20$, $N! \approx 2.4 \times 10^{18}$, una cantidad tan enorme que el algoritmo tardaría siglos.

### Vista general: el árbol de búsqueda

Podemos pensar el _backtracking_ como un árbol donde:

- Cada **nivel** del árbol representa un paso en la construcción de la solución (por ejemplo, colocar una reina en una fila).
- De cada nodo salen **ramas** que representan las opciones disponibles en ese paso.

En la figura siguiente, el árbol tiene $d = 3$ niveles (profundidad) y de cada nodo salen $b = 3$ ramas (factor de ramificación):

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-4-backtracking/BacktrackingOrden_light.svg
---
width: 70%
name: BacktrackingOrden
class: only-light-mode
---
Árbol de búsqueda para el caso de $b=3$ y $d=3$
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-4-backtracking/BacktrackingOrden_dark.svg
---
width: 70%
name: BacktrackingOrden-dark
class: only-dark-mode
---
Árbol de búsqueda para el caso de $b=3$ y $d=3$
```

La cantidad de nodos en un árbol así es $b^d$ (en este ejemplo $3^3 = 27$). Como el algoritmo podría tener que recorrer todo el árbol, su complejidad general es $O(b^d)$.

**¿Qué significa esto en la práctica?** Si $b$ y $d$ son grandes, $b^d$ crece muy rápido. Por ejemplo, con $b=10$ y $d=10$ tendríamos $10^{10} = 10000$ millones de nodos, demasiados para recorrerlos todos.

### Cómo mejorar la eficiencia

Un orden de complejidad factorial ($N!$) o exponencial ($b^d$) no es aceptable para problemas grandes. Para mejorar el tiempo de ejecución se usan dos técnicas principales:

**Poda (_pruning_):** consiste en cortar ramas del árbol que no pueden llevar a una solución válida, evitando recorrerlas. Por ejemplo, en el problema de las N reinas, si ya colocamos dos reinas en la misma columna, no tiene sentido seguir probando opciones en esa rama: la cortamos.

**Heurística:** usar información del problema para decidir qué rama explorar primero, con suerte encontrando la solución más rápido. Por ejemplo, podríamos empezar probando las columnas del centro del tablero porque estadísticamente dan más soluciones.

Estas técnicas no cambian la complejidad en el peor caso, pero en la práctica reducen mucho el tiempo de ejecución.

## Conclusiones

_Backtracking_ es una técnica algorítmica poderosa para resolver problemas de decisión, combinatoria y optimización. Aunque su complejidad computacional puede ser alta, en muchos casos es la única forma de encontrar una solución. La clave para implementar un algoritmo de _backtracking_ eficiente es definir correctamente los elementos que componen el algoritmo y utilizar técnicas como la poda o heurísticas para reducir el tiempo de ejecución.

La implementación de _backtracking_ puede ser sencilla y elegante, como se ha visto en el ejemplo del problema de las N reinas. Sin embargo, es importante tener en cuenta que no siempre es la mejor opción para resolver un problema, ya que en algunos casos puede ser más eficiente utilizar otras técnicas algorítmicas como la programación dinámica, algoritmos ávidos o soluciones aproximadas.

## Ejercicios

Los ejercicios de este capítulo están en el directorio
[`04-backtracking/ejercicios/`](https://github.com/untref-ayp2/taller-algoritmos/tree/main/04-backtracking/ejercicios)
del repositorio
[`taller-algoritmos`](https://github.com/untref-ayp2/taller-algoritmos).
Cada ejercicio tiene un esqueleto con `// TODO` y su correspondiente batería de tests.
Para resolverlos, clonar el repositorio, completar las funciones y ejecutar `go test ./...`.
