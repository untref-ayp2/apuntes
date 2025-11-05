---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# _Backtracking_ (Vuelta Atrás)

_**Backtracking**_ es una técnica algorítmica para resolver problemas donde la solución se construye probando posibilidades paso a paso y descartando caminos inviables. Siempre que el problema tenga solución, con esta técnica la podemos encontrar, ya que explora todas las posibilidades hasta encontrarla, al costo de no ser la más eficiente.

Se utiliza comúnmente en problemas de decisión, combinatoria y optimización donde la solución se puede construir de manera incremental.

La idea es agregar un nuevo elemento a la solución parcial y verificar si es una solución válida. Si no lo es, se descarta y se prueba con otro elemento. Este proceso se repite hasta encontrar la solución o encontrar que no hay más opciones disponibles y por lo tanto no hay solución.

Con esta técnica también se pueden encontrar todas las soluciones posibles a un problema, no solo una. Para ello, se debe modificar el algoritmo para que no termine al encontrar la primera solución, sino que continúe buscando.

## Ejemplo: Problema de las N Reinas

El problema de las N reinas consiste en colocar $N$ reinas en un tablero de ajedrez de $N \times N$ de tal manera que ninguna reina ataque a otra. Esto significa que no pueden estar en la misma fila, columna o diagonal. En la siguente figura se muestra una solución para el caso de tableros de $8 \times 8$ donde se colocan $8$ reinas.

```{figure} ../assets/images/NReinasSolucion.svg
---
width: 60%
name: sol.n.reinas
---
Solución al problema de las $N$ reinas para $N=8$
```

Para encontrar una solución posible, la idea es ir colocando una reina en cada fila del tablero, comenzando desde la primera fila. En cada fila se va probando con las distintas columnas, verificando si la posición es válida (no hay otra reina en la misma columna o diagonal). Si se encuentra una posición válida, se coloca la reina y se pasa a la siguiente fila. Si no se encuentra ninguna posición válida en una fila, se vuelve atrás (_backtracking_) y se prueba con otra columna en la fila anterior.

En la siguiente animación se muestra el proceso de búsqueda de una solución al problema de las N reinas para N=4. En este caso, se puede ver cómo se van colocando las reinas y cómo se vuelve atrás cuando no hay más opciones disponibles.

<p class="align-center">
  <video src="../_static/videos/NReinas-20250516.mp4" width="100%" controls autoplay loop></video>
</p>

## Algoritmo de _Backtracking_

A continuación se muestra la estructura general de este esquema:

```{code-block} text
---
linenos: true
---
FUNCION backtracking(solucionParcial, ...)
    SI esSolucion(solucionParcial) ENTONCES
        mostrar(solucionParcial)
        TERMINAR // o continuar buscando si se desea encontrar todas las soluciones
    SINO
        PARA CADA opcion posible de extender solucionParcial HACER
            SI esFactible(opcion) ENTONCES
                registrar(solucionParcial, opcion) // agregar opcion a la solución parcial
                backtracking(solucionParcial, ...) // llamada recursiva
                borrar(opcion, solucionParcial)    // vuelta atrás
```

### Como proceder para resolver un problema con _Backtracking_

Para resolver un problema con _backtracking_, se deben identificar y definir los siguientes elementos:

`solucionParcial`{l=go}
: Determinar una estructura de datos adecuada para representar la solución parcial. Puede ser un vector, una lista, etc. `solucionParcial`{l=go} debe permitir agregar nuevas opciones y verificar si es una solución válida.

`esSolucion`{l=go}
: Definir una función que verifique si `solucionParcial`{l=go} es una solución completa.

`extender`{l=go}
: Definir una función que tome una `solucionParcial`{l=go} y devuelva una a una todas las opciones posibles para extenderla. Esta función debe generar todas las combinaciones posibles de extender `solucionParcial`{l=go}.

`esFactible`{l=go}
: Definir una función que verifique si una opción es válida para extender `solucionParcial`{l=go}. Esta función debe verificar si la opción no viola ninguna restricción del problema.

`registrar`{l=go}
: Definir una función que registre la opción generada con `extender`{l=go} en la `solucionParcial`{l=go}. Eventualmente puede ser necesario registrar información adicional de la opción generada.

`borrar`{l=go}
: Definir una función que borre la última opción registrada en `solucionParcial`{l=go}. Es decir es el paso opuesto al de `registrar`{l=go}. Si es necesario también debe restaurar cualquier información extra o de contexto registrada anteriormente.

## Implementación de la solución al problema de las N reinas

`solucionParcial`{l=go}
: puede ser un arreglo de tamaño $N$ donde las posiciones del arreglo representan las filas y los valores alamacenados en cada posición del arreglo representan las columnas. Por ejemplo, para el caso de $N=4$, una solución parcial podría ser $[2, 0, 3, 1]$, lo que significa que hay una reina en la fila $0$ en la columna $2$, una reina en la fila $1$ en la columna $0$, etc.

`esSolucion`{l=go}
: es una función que verifica si la `solucionParcial`{l=go} tiene $N$ reinas. En este caso, se verifica si la longitud del arreglo `solucionParcial`{l=go} es igual a $N$.

`extender`{l=go}
: con un solo ciclo entre $[0, N)$, podemos generar todas las posibles columnas en la que se puede colocar una reina en la fila $i$.

`esFactible`{l=go}
: es una función que debe chequear si en la misma columna o en las diagonales hay otras reinas que entren en conflicto con la nueva reina que intentamos agregar al tablero.

: Para chequear si hay ya una reina en la misma columna basta con revisar los valores del arreglo `solucionParcial`{l=go} para asegurarse que la columna candidata no está atacada por otra reina, es decir no puede haber dos valores iguales en el arreglo y para chequear si hay una reina en alguna de las dos diagonales que se pueden generar en cualquier posición del tablero, se puede usar la propiedad de que en todas las diagonales directas, por nombrarlas de alguna forma, las de color azul, $fila - columna = constante$. Mientras que para las diagonales inversas, las de color rojo, se cumple que $fila + columna = constante$. Ver la figura a continuación.

```{figure} ../assets/images/NReinasDiagonal.svg
---
width: 70%
name: sol.n.reinas.diagonal
---
Reinas en la misma diagonal
```

A continuación se muestra una implementación en Go.

```{code-block} go
---
linenos: true
---
package nreinas

// NReinas es una función que implementa la solución al problema de las N reinas.
//
// Recibe como parámetro el número de reinas a colocar y retorna un slice con la
// primera solución encontrada.
func NReinas(n int) []int {
    var solucionParcial []int
    var solucion []int
    backtracking(n, 0, solucionParcial, &solucion)
    return solucion
}

// esFactible verifica si una reina puede ser colocada en una posición, dada una
// configuración de reinas ya colocadas.
func esFactible(fila int, columna int, solucionParcial []int) bool {
    for i := range solucionParcial {
        if solucionParcial[i] == columna ||
            fila+columna == i+solucionParcial[i] ||
            fila-columna == i-solucionParcial[i] {
            return false
        }
    }
    return true
}

// backtracking es una función recursiva que realiza el backtracking para el
// problema de las N reinas.
//
// Recibe como parámetros el número de reinas a colocar, la fila actual, la
// configuración de reinas ya colocadas y retorna la solución encontrada.
func backtracking(n int, fila int, solucionParcial []int, solucion *[]int) {
    if fila == n {
        // Ya pudimos colocar `n` reinas en el tablero.
        *solucion = make([]int, len(solucionParcial))
        // Copiamos la solución encontrada a la variable `solucion` que se pasó
        // por referencia.
        copy(*solucion, solucionParcial)
        return
    }

    // Extender
    for columna := range n {
        if esFactible(fila, columna, solucionParcial) {
            // Registrar
            nuevaSolucion := append(solucionParcial, columna)
            backtracking(n, fila+1, nuevaSolucion, solucion)
            // Borrar está implícito en la forma en que se maneja la variable
            // `nuevaSolucion`, ya que en cada ciclo se crea una nueva copia de
            // `nuevaSolucion`.
        }
    }
}

```

## Análisis de la complejidad computacional

La complejidad computacional de un algoritmo de _backtracking_ depende del número de soluciones posibles y del tiempo que toma verificar si una solución es válida. En el caso del problema de las N reinas, la complejidad es $O(N!)$, ya que en el peor de los casos se deben probar todas las combinaciones posibles de colocar las reinas en el tablero.

Como caso general se puede pensar que la complejidad es $O(N^M)$, donde $N$ es el número de opciones posibles en cada paso y $M$ es la profundidad máxima del árbol de búsqueda.

En la figura a continuación se muestra un árbol de búsqueda para el caso de $N=3$ y $M=3$. En este caso, se puede ver que el árbol tiene una profundidad de 3 y en cada nivel hay 3 opciones posibles.

```{figure} ../assets/images/BacktrackingOrden.svg
---
width: 70%
name: BacktrackingOrden
---
Árbol de búsqueda para el caso de $N=3$ y $M=3$
```

Un orden de complejidad exponencial o factorial no es aceptable para la mayoría de los problemas, pero en algunos casos se puede reducir el tiempo de ejecución utilizando técnicas como la poda (_pruning_) o alguna heurística. La poda consiste en eliminar ramas del árbol de búsqueda que no pueden llevar a una solución válida, mientras que la heurística consiste en utilizar información adicional para guiar la búsqueda hacia soluciones más prometedoras.

## Conclusiones

_Backtracking_ es una técnica algorítmica poderosa para resolver problemas de decisión, combinatoria y optimización. Aunque su complejidad computacional puede ser alta, en muchos casos es la única forma de encontrar una solución. La clave para implementar un algoritmo de _backtracking_ eficiente es definir correctamente los elementos que componen el algoritmo y utilizar técnicas como la poda o heurísticas para reducir el tiempo de ejecución.

La implementación de _backtracking_ puede ser sencilla y elegante, como se ha visto en el ejemplo del problema de las N reinas. Sin embargo, es importante tener en cuenta que no siempre es la mejor opción para resolver un problema, ya que en algunos casos puede ser más eficiente utilizar otras técnicas algorítmicas como la programación dinámica, algoritmos ávidos o soluciones aproximadas.

## Ejercicios

1. Modificar la implementación de las N reinas para que devuelva un arreglo de soluciones, con todas las soluciones encontradas.

2. Implementar una solución para el problema del cambio de monedas usando _backtracking_. El problema consiste en entregar la menor cantidad de monedas posibles para un monto dado.

3. Escribir un programa para resolver sudokus usando _backtracking_. El sudoku es un rompecabezas de lógica que consiste en llenar una cuadrícula de 9x9 con números del 1 al 9, de tal manera que cada fila, cada columna y cada una de las nueve subcuadrículas de 3x3 contengan todos los dígitos del 1 al 9 sin repetir. En general se inicia de un tablero parcialmente lleno, como el que se muestra a continuación.

```{figure} ../assets/images/Sudoku.svg
---
width: 100%
name: Sudoku
---
```
