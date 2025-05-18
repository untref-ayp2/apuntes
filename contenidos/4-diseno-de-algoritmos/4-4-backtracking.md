---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Backtracking (Vuelta Atrás)

Backtracking es una técnica algorítmica para resolver problemas donde la solución se construye probando posibilidades paso a paso y descartando caminos inviables. Siempre que el problema tenga solución con esta técnica la podemos encontrar, ya que explora todas las posibilidades hasta encontrarla, al costo de no ser la más eficiente.

Se utiliza comúnmente en problemas de decisión, combinatoria y optimización donde la solución se puede construir de manera incremental.

La idea es agregar un nuevo elemento a la solución parcial y verificar si es una solución válida. Si no lo es, se descarta y se prueba con otro elemento. Este proceso se repite hasta encontrar la solución o encontrar que no hay más opciones disponibles y por lo tanto no hay solución.

Con esta técnica también se pueden encontrar todas las soluciones posibles a un problema, no solo una. Para ello, se debe modificar el algoritmo para que no termine al encontrar la primera solución, sino que continúe buscando.

## Ejemplo: Problema de las N Reinas

El problema de las N reinas consiste en colocar N reinas en un tablero de ajedrez de N x N de tal manera que ninguna reina ataque a otra. Esto significa que no pueden estar en la misma fila, columna o diagonal. En la siguente figura se muestra una solución para el caso de tableros de 8 x 8 donde se colocan 8 reinas.

```{figure} ../assets/images/NReinasSolucion.svg
---
width: 60%
name: sol.n.reinas
---
Solución al problema de las N reinas para N=8
```

Para encontrar una solución posible, la idea es ir colocando una reina en cada fila del tablero, comenzando desde la primera fila. En cada fila se va probando con las distintas columnas, verificando si la posición es válida (no hay otra reina en la misma columna o diagonal). Si se encuentra una posición válida, se coloca la reina y se pasa a la siguiente fila. Si no se encuentra ninguna posición válida en una fila, se vuelve atrás (backtracking) y se prueba con otra columna en la fila anterior.

En la siguiente animación se muestra el proceso de búsqueda de una solución al problema de las N reinas para N=4. En este caso, se puede ver cómo se van colocando las reinas y cómo se vuelve atrás cuando no hay más opciones disponibles.

<!-- markdownlint-disable MD033 -->
<p class="align-center">
  <video src="../_static/videos/NReinas-20250516.mp4" width="100%"controls autoplay></video>
</p>
<!-- markdownlint-enable MD033 -->

## Algoritmo de Backtracking

A continuación se muestra la estructura general de este esquema:

```{code-block}
:linenos:
funcion backtracking(solución_parcial, ...)
    si es_solución(solución_parcial) entonces
        mostrar(solución_parcial)
        terminar // o continuar buscando si se desea encontrar todas las soluciones
    sino
        para cada opción posible de extender solución_parcial hacer
            si es_factible(opción) entonces
                registrar(solución_parcial, opción) // agregar opción a la solución parcial
                backtracking(solución_parcial, ...) // llamada recursiva
                borrar(opción, solución_parcial)    // vuelta atrás
```

### Como proceder para resolver un problema con Backtracking

Para resolver un problema con backtracking, se deben identificar y definir los siguientes elementos:

solución_parcial
: Determinar una estructura de datos adecuada para representar la solución parcial. Puede ser un vector, una lista, etc. **solución_parcial** debe permitir agregar nuevas opciones y verificar si es una solución válida.

es_solución
: Definir una función que verifique si **solución_parcial** es una solución completa.

extender
: Definir una función que tome una **solución parcial** y devuelva una a una todas las opciones posibles para extenderla. Esta función debe generar todas las combinaciones posibles de extender **solución_parcial**.

es_factible
: Definir una función que verifique si una opción es válida para extender **solución_parcial**. Esta función debe verificar si la opción no viola ninguna restricción del problema.

registrar
: Definir una función que registre la opción generada con **extender** en la **solución parcial**. Eventualmente puede ser necesario registrar información adicional de la opción generada.

borrar
: Definir una función que borre la última opción registrada en **solución_parcial**. Es decir es el paso opuesto al de **registrar**. Si es necesario también debe restaurar cualquier información extra o de contexto registrada anteriormente.

## Implementación de la solución al problema de las N reinas

solucion_parcial
: puede ser un arreglo de tamaño N donde las posiciones del arreglo representan las filas y los valores alamacenados en cada posición del arreglo representan las columnas. Por ejemplo, para el caso de N=4, una solución parcial podría ser [2, 0, 3, 1], lo que significa que hay una reina en la fila 0 en la columna 2, una reina en la fila 1 en la columna 0, etc.

es_solución
: es una función que verifica si la **solución_parcial** tiene N reinas. En este caso, se verifica si la longitud del arreglo **solucion_parcial** es igual a N.

extender
: con un solo ciclo entre $[0, N)$, podemos generar todas las posibles columnas en la que se puede colocar una reina en la fila i.

es_factible
: es una función que debe chequear si en la misma columna o en las diagonales hay otras reinas que entren en conflicto con la nueva reina que intentamos agregar al tablero. Para chequear si hay ya una reina en la misma columna basta con revisar los valores del arreglo **solución_parcial** para asegurarse que la columna candidata no está atacada por otra reina, es decir no puede haber dos valores iguales en el arreglo y para chequear si hay una reina en alguna de las dos diagonales que se pueden generar en cualquier posición del tablero, se puede usar la propiedad de que en todas las diagonales directas, por nombrarlas de alguna forma, las de color azul, $fila - columna = constante$. Mientras que para las diagonales inversas, las de color rojo, se cumple que $fila + columna = constante$. Ver la figura a continuación.

```{figure} ../assets/images/NReinasDiagonal.svg
---
width: 70%
name: sol.n.reinas.diagonal
---
Reinas en la misma diagonal
```

A continuación se muestra una implementación en Go.

```{code-block} go
:linenos:
package reinas

// Función que implementa la solución al problema de las N reinas
// Recibe como parámetro el número de reinas a colocar
// Retorna un arreglo con la solución
func NReinas(n int) []int {
    var reinas []int //solución_parcial
    var solucion []int //variable para almacenar la solución encontrada
    backtracking(n, 0, reinas, &solucion)
    return solucion
}

// Verifica si una reina puede ser colocada en (fila, columna)
// dada una configuración de reinas ya colocadas
func es_factible(fila int, columna int, reinas []int) bool {
    for i := 0; i < len(reinas); i++ {
        if reinas[i] == columna || fila+columna == i+reinas[i] || fila-columna == i-reinas[i] {
            return false
        }
    }
    return true
}

// Función recursiva que realiza el backtracking
// Parámetros: el número de reinas a colocar, la fila actual,
// la configuración de reinas ya colocadas.
// Retorna la solución encontrada
func backtracking(n int, fila int, reinas []int, solucion *[]int) {
    if fila == n { //Colocamos n reinas en el tablero
        //*solucion = reinas
        *solucion = make([]int, len(reinas))
        copy(*solucion, reinas) // Copiamos la solución encontrada a la variable
                                // solucion que se pasó por referencia

        return
    }
    //Extender
    for columna := 0; columna < n; columna++ {
        if es_factible(fila, columna, reinas) {
            nuevaSolucion := append(reinas, columna) //Registrar
            backtracking(n, fila+1, nuevaSolucion, solucion)
            //Borrar está implícito en la forma en que se maneja la variable
			// nuevaSolucion, ya que en cada ciclo se crea una nueva copia de
			// nuevaSolucion
        }
    }
}
```

## Análisis de la complejidad computacional

La complejidad computacional de un algoritmo de backtracking depende del número de soluciones posibles y del tiempo que toma verificar si una solución es válida. En el caso del problema de las N reinas, la complejidad es $O(N!)$, ya que en el peor de los casos se deben probar todas las combinaciones posibles de colocar las reinas en el tablero.

Como caso general se puede pensar que la complejidad es $O(N^M)$, donde $N$ es el número de opciones posibles en cada paso y $M$ es la profundidad máxima del árbol de búsqueda.

En la figura a continuación se muestra un árbol de búsqueda para el caso de $N=3$ y $M=3$. En este caso, se puede ver que el árbol tiene una profundidad de 3 y en cada nivel hay 3 opciones posibles.

```{figure} ../assets/images/BacktrackingOrden.svg
---
width: 70%
name: BacktrackingOrden
---
Árbol de búsqueda para el caso de N=3 y M=3
```

Un orden de complejidad exponencial o factorial no es aceptable para la mayoría de los problemas, pero en algunos casos se puede reducir el tiempo de ejecución utilizando técnicas como la poda (pruning) o alguna heurística. La poda consiste en eliminar ramas del árbol de búsqueda que no pueden llevar a una solución válida, mientras que la heurística consiste en utilizar información adicional para guiar la búsqueda hacia soluciones más prometedoras.

## Conclusiones

Backtracking es una técnica algorítmica poderosa para resolver problemas de decisión, combinatoria y optimización. Aunque su complejidad computacional puede ser alta, en muchos casos es la única forma de encontrar una solución. La clave para implementar un algoritmo de backtracking eficiente es definir correctamente los elementos que componen el algoritmo y utilizar técnicas como la poda o heurísticas para reducir el tiempo de ejecución.

La implementación de backtracking puede ser sencilla y elegante, como se ha visto en el ejemplo del problema de las N reinas. Sin embargo, es importante tener en cuenta que no siempre es la mejor opción para resolver un problema, ya que en algunos casos puede ser más eficiente utilizar otras técnicas algorítmicas como la programación dinámica, algoritmos ávidos o soluciones aproximadas.

## Ejercicios

1. Modificar la implementación de las N reinas para que devuelva un arreglo de soluciones, con todas las soluciones encontradas.

2. Implementar una solución para el problema del cambio de monedas usando backtracking. El problema consiste en entregar la menor cantidad de monedas posibles para un monto dado.

3. Escribir un programa para resolver sudokus usando backtracking. El sudoku es un rompecabezas de lógica que consiste en llenar una cuadrícula de 9x9 con números del 1 al 9, de tal manera que cada fila, cada columna y cada una de las nueve subcuadrículas de 3x3 contengan todos los dígitos del 1 al 9 sin repetir. En general se inicia de un tablero parcialmente lleno, como el que se muestra a continuación.

```{figure} ../assets/images/Sudoku.svg
---
width: 100%
name: Sudoku
---
```
