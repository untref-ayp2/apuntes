---
label: ordenamientos-recursivos
---

# Ordenamientos Recursivos

## Introducción: La Importancia del Orden

El **ordenamiento de datos** es una de las operaciones fundamentales en la informática y la ciencia de datos. Desde organizar una lista de contactos por nombre hasta clasificar resultados de búsqueda por relevancia o procesar grandes volúmenes de datos para análisis estadísticos, la capacidad de ordenar eficientemente la información es crucial. Un conjunto de datos ordenado facilita enormemente la búsqueda, la inserción y la eliminación, mejorando el rendimiento de casi cualquier aplicación que trabaje con colecciones de elementos.

Pensemos en la vida cotidiana: una biblioteca donde los libros están ordenados alfabéticamente por autor, un cajón de herramientas donde los destornilladores están por tamaño, o una lista de precios en un supermercado. En todos estos casos, el orden nos permite encontrar lo que necesitamos de forma rápida y eficiente. En el ámbito computacional, este principio se traduce en algoritmos que, a través de diversas estrategias, transforman una secuencia desordenada en una secuencia ordenada.

Algunas características de los algoritmos de ordenamiento incluyen:

Complejidad temporal
: La cantidad de tiempo que un algoritmo tarda en ordenar un conjunto de datos. Se mide en función del número de elementos a ordenar y se expresa comúnmente en notación O grande (por ejemplo, $O(n \log n)$, $O(n^2)$). En los algoritmos de ordenamiento, además de establecer la complejidad temporal para el peor caso, se suele analizar los casos promedio y el mejor caso, teniendo en cuenta cuando se presenta cada escenario.

Peor Caso
: Describe la situación en la que el algoritmo tarda el mayor tiempo posible en completarse. Esto ocurre cuando los datos de entrada están dispuestos de tal manera que el algoritmo se ve obligado a realizar el número máximo de operaciones. El análisis del peor caso nos da una cota superior. Nos permite garantizar que el algoritmo nunca tardará más de un cierto tiempo, sin importar cómo estén los datos de entrada.

Caso Promedio
: Representa el tiempo de ejecución esperado del algoritmo cuando los datos de entrada son aleatorios o no tienen un patrón específico. Calcularlo puede ser más complejo, ya que implica considerar la probabilidad de diferentes configuraciones de entrada. El análisis del caso promedio nos da una idea más realista del rendimiento del algoritmo en situaciones típicas.

Mejor Caso
: Es la situación en la que el algoritmo tarda el menor tiempo posible en completarse. Esto sucede cuando los datos de entrada están dispuestos de una manera ideal para el algoritmo. Aunque no es tan útil como el peor caso o el caso promedio para predecir el rendimiento general, el mejor caso puede ser de utilidad en algoritmos de ordenamiento adaptativos que puedan adaptarse a los datos de entrada.

Estabilidad
: Un algoritmo es estable si mantiene el orden relativo de los elementos iguales después del ordenamiento. Esto es importante en situaciones donde los elementos tienen múltiples claves de ordenamiento. Por ejemplo si una clave de ordenamiento aparece repetida varias veces en una secuencia de datos desordenadas, puede ser interesante mantener el orden relativo (el primero que aparece, luego el segundo, etc.) en la secuencia ordenada.

En el lugar (_In Place_)
: Un algoritmo es "_In Place_" si requiere una cantidad acotada de espacio adicional para ordenar los datos, lo que significa que puede ordenar los datos sin necesidad de estructuras auxiliares del tamaño del arreglo original. En otras palabras, el espacio adicional que se necesita no es proporcional a $n$, la cantidad de elementos a ordenar.

En línea (_Online_)
: Un algoritmo es "_Online_" si puede procesar los datos a medida que llegan, sin necesidad de conocer el conjunto completo de antemano. Esto es útil en aplicaciones donde los datos se generan en tiempo real y se pueden ir ordenando a medida que llegan.

Existen muchos algoritmos de ordenamiento, cada uno con sus propias fortalezas y debilidades. Algunos de los más conocidos, y a menudo los primeros que se estudian, son los **algoritmos de ordenamiento simple**, por nombrarlos de alguna forma.

## Algoritmos de Ordenamiento Simple

Ordenamiento por Inserción (_Insertion Sort_)
: Construye la lista final ordenada un elemento a la vez. Es eficiente para pequeñas cantidades de datos o datos casi ordenados. Su idea es similar a ordenar cartas en la mano: se toma una carta nueva y se inserta en su posición correcta entre las ya ordenadas. Las ventajas de este algoritmo es que es **Estable**, _**In Place**_ y _**Online**_. En el mejor de los casos donde el arreglo está casi ordenado, salvo algunos pocos elementos, se puede estimar que el orden es $O(n)$. En el peor caso y en el caso promedio es $O(n^2)$

Ordenamiento por Selección (_Selection Sort_)
: Encuentra repetidamente el elemento mínimo (o máximo) del resto no ordenado y lo coloca al principio (o al final) de la lista ordenada. Es simple de entender pero no muy eficiente para grandes conjuntos de datos. No es **Estable**, ni _**Online**_, pero si _**In Place**_. Su complejidad temporal es $O(n^2)$ tanto para el peor, el mejor y el caso promedio.

Ordenamiento por Burbujeo (_Bubble Sort_)
: Recorre repetidamente la lista, compara elementos adyacentes y los intercambia si están en el orden incorrecto. Las "burbujas" de elementos más grandes (o más pequeños) se mueven hacia el final (o el principio) de la lista. Es un algoritmo muy intuitivo pero extremadamente ineficiente para grandes conjuntos de datos. Es **Estable** e _**In Place**_, pero no _**Online**_. En el mejor caso cuando los datos están casi ordenados, salvo unos pocos elementos puede presentar una complejidad de $O(n)$. En el peor caso y en el caso promedio es $O(n^2)$.

En la siguiente tabla se resumen las principales características de estos algoritmos:

```{table} Algoritmos de Ordenamiento Simple
|         Algoritmo          | Inserción   | Selección  |  Burbujeo |
| :------------------------- | :---------: | :--------: | :-------: |
| Peor Caso                  | $O(n^2)$    | $O(n^2)$   | $O(n^2)$  |
| Caso Promedio              | $O(n^2)$    | $O(n^2)$   | $O(n^2)$  |
| Mejor Caso                 | $O(n)$      | $O(n^2)$   | $O(n)$    |
| Estable                    | Sí          | No         | Sí        |
| _In Place_                 | Sí          | Sí         | Sí        |
| _Online_                   | Sí          | No         | No        |
```

Estos algoritmos son fáciles de implementar y entender, lo que los hace ideales para introducir conceptos básicos de ordenamiento. Sin embargo, su rendimiento se degrada rápidamente a medida que el número de elementos crece, lo que los limita a conjuntos de datos pequeños o casi ordenados. Por ejemplo, el **ordenamiento por inserción** es eficiente para listas pequeñas o listas que ya están casi ordenadas, mientras que el **ordenamiento por selección** y el **ordenamiento por burbujeo** son más adecuados para fines educativos que para aplicaciones prácticas en grandes volúmenes de datos.

Los tres algoritmos tienen una complejidad computacional de $O(n^2)$, donde $n$ es el número de elementos a ordenar. Esto significa que a medida que $n$ crece, el tiempo de ejecución aumenta cuadráticamente, lo que los hace imprácticos para conjuntos de datos grandes. Para superar esta limitación, se han desarrollado algoritmos de ordenamiento más avanzados, a menudo basados en el paradigma "**divide y vencerás**", que explotan la recursión para lograr eficiencias significativamente mayores. Nos centraremos en tres de los algoritmos de ordenamiento más eficientes: **Mergesort, Quicksort y Heapsort**, analizando en detalle su funcionamiento y su complejidad computacional.

## Algoritmos de Ordenamiento Recursivo

Los algoritmos de ordenamiento recursivo que analizaremos son ejemplos paradigmáticos de cómo el diseño recursivo puede conducir a soluciones eficientes para problemas complejos. A menudo logran una complejidad de tiempo $O(n \log n)$, lo que representa una mejora sustancial sobre los algoritmos de $O(n^2)$ para grandes conjuntos de datos.

### Mergesort (Ordenamiento por Mezcla)

**Mergesort** es un algoritmo **Estable**, que requiere espacio adicional proporcional al tamaño del arreglo, es decir no es **_In Place_**, basado en el paradigma "divide y vencerás". Fue creado en 1945 por John von Neumann y es uno de los algoritmos de ordenamiento más eficientes y ampliamente utilizados.

#### Funcionamiento

Dividir
: El algoritmo divide recursivamente la lista desordenada en dos sublistas de aproximadamente la mitad del tamaño hasta que cada sublista contiene solo un elemento (que por definición está ordenado).

Conquistar
: Cada sublista de un solo elemento se considera ordenada (caso base).

Combinar
: Las sublistas ordenadas se mezclan repetidamente para producir nuevas sublistas ordenadas hasta que solo quede una sublista, que es la lista original pero ahora completamente ordenada. La operación clave aquí es la **mezcla (merge)** de dos listas ordenadas en una sola lista ordenada.

```{code-block} text
---
linenos: true
caption: Mergesort (Ordenamiento por Mezcla)
---
FUNCION Mergesort(arreglo)
    SI longitud(arreglo) <= 1 ENTONCES // Caso base: si el arreglo tiene
                                       // 0 o 1 elementos, ya está ordenado
        RETORNAR arreglo
    FIN SI

    mitad ← longitud(arreglo) / 2
    izquierda ← Mergesort(subarreglo desde 0 hasta mitad-1)
    derecha ← Mergesort(subarreglo desde mitad hasta fin)
    RETORNAR merge(izquierda, derecha)
FIN FUNCION
```

```{code-block} text
---
linenos: true
emphasize-lines: 2, 7
caption: Función de Mezcla (Merge)
---
FUNCION merge(izquierda, derecha)
    resultado ← arreglo vacío // Arreglo para almacenar la mezcla
    i ← 0 // Índice para la sublista izquierda
    j ← 0 // Índice para la sublista derecha

    MIENTRAS i < longitud(izquierda) Y j < longitud(derecha) HACER
        SI izquierda[i] <= derecha[j] ENTONCES
            agregar izquierda[i] a resultado
            i ← i + 1
        SINO
            agregar derecha[j] a resultado
            j ← j + 1
        FIN SI
    FIN MIENTRAS

    // Agregar los elementos restantes de izquierda, si los hay
    MIENTRAS i < longitud(izquierda) HACER
        agregar izquierda[i] a resultado
        i ← i + 1
    FIN MIENTRAS

    // Agregar los elementos restantes de derecha, si los hay
    MIENTRAS j < longitud(derecha) HACER
        agregar derecha[j] a resultado
        j ← j + 1
    FIN MIENTRAS

    RETORNAR resultado
FIN FUNCION
```

En la línea 2 de la función `merge`, por cada mezcla que se realiza se crea un nuevo arreglo `resultado` que contendrá los elementos ordenados de las dos sublistas. Esto es necesario porque Mergesort no modifica las listas originales, sino que crea una nueva lista ordenada a partir de ellas.

En la línea 7 de la función `merge` es fundamental que se compare por menor igual (`<=`) para garantizar la estabilidad del algoritmo, es decir, que los elementos iguales mantengan su orden relativo original.

<div class="only-html">

A continuación se puede visualizar paso a paso el funcionamiento de Mergesort.
Se puede ingresar un arreglo de hasta 10 elementos separados por coma, o generar uno
aleatorio con el botón **Generar**. Luego, usar los botones ◀ ▶ para avanzar
paso a paso, o >> para reproducir la animación de forma automática. Se puede
alternar entre orden ascendente y descendente con los botones **Asc** y **Desc**
del encabezado.

<iframe src="/applets/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos/mergesort-visualizer_light.html" width="100%" height="560px" class="only-light-mode"></iframe>

<iframe src="/applets/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos/mergesort-visualizer_dark.html" width="100%" height="560px" class="only-dark-mode"></iframe>

</div>

#### Análisis de la Complejidad Computacional

La recurrencia para el tiempo de ejecución de Mergesort se puede expresar como:
$T(n) = 2T(n/2) + O(n)$
Donde:

- $2T(n/2)$ representa el costo de ordenar las dos sublistas de tamaño $n/2$.
- $O(n)$ representa el costo de la operación de mezcla (merge), ya que en el peor caso se recorren todos los elementos de ambas sublistas una vez para fusionarlas.

Aplicando el Teorema Maestro, se obtiene que la complejidad de tiempo es **$O(n \log n)$**, ya que subdivide recursivamente el arreglo en mitades hasta llegar al caso base y luego combina los resultados de manera lineal.

En este algoritmo no hay un caso mejor o peor, ya que la división y la mezcla siempre ocurren de la misma manera, lo que da como resultado una complejidad de tiempo consistente.

### Quicksort (Ordenamiento Rápido)

**Quicksort**, como **Mergesort**, es un algoritmo de ordenamiento basado en el paradigma "divide y vencerás". Sin embargo, su enfoque es diferente y su eficiencia en la práctica lo ha convertido en uno de los algoritmos de ordenamiento más utilizados. Quicksort **no es un algoritmo de ordenamiento estable** ni _**Online**_ pero si es _**In Place**_ y estrictamente hablando tampoco se puede asegurar que sea de división y conquista, ya que por la forma de partir el arreglo, no se puede asegurar que las sublistas resultantes sean de tamaño similar. A pesar de esto, es ampliamente considerado como uno de los algoritmos más eficientes para ordenar grandes volúmenes de datos.

La idea principal detrás de Quicksort es seleccionar un elemento de la lista, llamado **pivote**, y reorganizar los elementos de tal manera que todos los elementos menores que el pivote queden a su izquierda y todos los elementos mayores queden a su derecha. Luego, se aplica recursivamente el mismo proceso a las sublistas resultantes. Los elementos a la izquierda y derecha del pivote no están necesariamente ordenados, pero el pivote estará en su posición final ordenada después de la partición.

Esta técnica de partición es lo que distingue a Quicksort de otros algoritmos de ordenamiento, se conoce como **partición de 2 vías**.

**Quicksort** fue creado y publicado por Tony Hoare en 1961.

#### Funcionamiento

Dividir
: Se elige un elemento de la lista llamado **pivote**. Se reorganiza la lista de tal manera que todos los elementos menores que el pivote queden a su izquierda y todos los elementos mayores queden a su derecha. Los elementos iguales al pivote pueden ir a la izquierda o a la derecha del pivote. Después de esta partición, el pivote se encuentra en su posición final ordenada.

Conquistar
: Se ordenan recursivamente las dos sublistas (la de elementos menores al pivote y la de elementos mayores al pivote).

Combinar
: No hay una fase de combinación explícita, ya que la lista se ordena "en el lugar" a medida que las sublistas se ordenan recursivamente. La lista completa queda ordenada una vez que todas las sublistas han sido procesadas.

```{code-block} text
---
linenos: true
caption: Quicksort (Ordenamiento Rápido)
---
FUNCION Quicksort(arreglo, inicio, fin)
    SI inicio >= fin ENTONCES
        RETORNAR // Caso base: si el subarreglo tiene 0 o 1 elementos, ya está ordenado
    FIN SI
    // Particionar el arreglo y obtener el índice del pivote
    pivote_indice ← Particionar(arreglo, inicio, fin)
    Quicksort(arreglo, inicio, pivote_indice - 1)
    Quicksort(arreglo, pivote_indice + 1, fin)
FIN FUNCION
```

```{code-block} text
---
linenos: true
caption: Partición de 2 vías
---
FUNCION Particionar(arreglo, inicio, fin)
    // Elegir el elemento del medio como pivote
    medio ← (inicio + fin) / 2
    pivote_valor ← arreglo[medio]

    // Mover el pivote al final para simplificar la partición
    Intercambiar(arreglo, medio, fin)

    i ← inicio
    j ← fin - 1

    MIENTRAS i <= j HACER
        // Buscar desde la izquierda un elemento mayor que el pivote
        MIENTRAS i <= j Y arreglo[i] <= pivote_valor HACER
            i ← i + 1
        FIN MIENTRAS

        // Buscar desde la derecha un elemento menor que el pivote
        MIENTRAS i <= j Y arreglo[j] >= pivote_valor HACER
            j ← j - 1
        FIN MIENTRAS

        // Si ambos índices no se han cruzado, intercambiar los elementos
        SI i < j ENTONCES
            Intercambiar(arreglo, i, j)
        FIN SI
    FIN MIENTRAS

    // Colocar el pivote en su posición final
    Intercambiar(arreglo, i, fin)

    RETORNAR i // Retorna el índice final del pivote
FIN FUNCION
```

```{code-block} text
---
linenos: true
caption: Intercambio de elementos
---
FUNCION Intercambiar(arreglo, i, j)
    temp ← arreglo[i]
    arreglo[i] ← arreglo[j]
    arreglo[j] ← temp
FIN FUNCION
```

#### Pivote

La elección del pivote es crucial para el rendimiento de Quicksort. Estrategias comunes incluyen elegir el primer elemento, el último elemento, el elemento central, o un elemento aleatorio.

Si el pivote elegido es justo el mayor elemento del arreglo (o el menor), la partición resultará en una sublista de tamaño $n-1$ y otra de tamaño 0, lo que llevará a un rendimiento cuadrático en el peor caso.

Una técnica común para mitigar este comportamiento es elegir el pivote como la **"mediana de tres"**, que toma el primer, el último y el elemento del medio del arreglo y selecciona el que está en el medio de esos tres valores. Esto ayuda a evitar particiones muy desequilibradas.

Por ejemplo, si tenemos un arreglo `{...}[3, 6, 8, 10, 1, 2, 1]` la mediana de tres compara el primer elemento `3`, el último elemento `1` y el del medio `10`, y selecciona `3` como pivote, lo que ayuda a evitar un caso de peor rendimiento.

<div class="only-html">

A continuación se puede visualizar paso a paso el funcionamiento de Quicksort.
Se puede ingresar un arreglo de hasta 10 elementos separados por coma, o generar uno
aleatorio con el botón **Generar**. Luego, usar los botones ◀ ▶ para avanzar
paso a paso, o >> para reproducir la animación de forma automática. Se puede
alternar entre orden ascendente y descendente con los botones **Asc** y **Desc**
del encabezado.

<iframe src="/applets/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos/quicksort-visualizer_light.html" width="100%" height="360px" class="only-light-mode"></iframe>

<iframe src="/applets/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos/quicksort-visualizer_dark.html" width="100%" height="360px" class="only-dark-mode"></iframe>

</div>

### Análisis de la Complejidad Computacional

La complejidad temporal de Quicksort depende de la elección del pivote y de cómo se distribuyen los elementos en el arreglo:

Mejor Caso
: Ocurre cuando el pivote divide el arreglo en dos subarreglos de tamaño aproximadamente igual en cada llamada recursiva. En este caso, la recurrencia es:
$T(n) = 2T(n/2) + O(n)$. Aplicando el Teorema Maestro, obtenemos una complejidad de tiempo de **$O(n \log n)$**.

Caso Promedio
: En promedio, una buena implementación de Quicksort también logra una complejidad de tiempo de **$O(n \log n)$**. Es fundamental que la elección del pivote sea aleatoria o que se utilice una estrategia como la mediana de tres para evitar particiones muy desequilibradas.

Peor Caso
: Ocurre cuando el pivote es el elemento más grande o más pequeño en cada llamada recursiva, lo que lleva a una partición muy desequilibrada. En este caso, la recurrencia es $T(n) = T(n-1) + O(n)$, lo que resulta en una complejidad de tiempo de **$O(n^2)$**.

Si bien Quicksort tiene un peor caso de $O(n^2)$, este escenario es raro en la práctica si se elige un buen pivote, por lo que su uso es muy común en aplicaciones reales. No se debe usar este algoritmo si tenemos que garantizar que el peor caso sea menor $O(n^2)$, por ejemplo en algunas aplicaciones de tiempo real.

### Heapsort (Ordenamiento por Montículos)

**Heapsort** es un algoritmo que no se basa en el paradigma de "división y conquista", sino que utiliza un _heap_ o montículo como estructura de datos subyacente para ordenar los elementos.

**Heapsort no es estable** ni _**Online**_, pero si _**In Place**_ por lo que no requiere espacio adicional significativo.

Fue desarrollado por J. W. J. Williams en 1964 y es un algoritmo eficiente que garantiza un tiempo de ejecución de $O(n \log n)$ en todos los casos (mejor, promedio y peor).

#### Representación del _heap_ en un arreglo

Un _heap_ es un árbol binario completo que se representa de forma implícita en un arreglo, sin necesidad de punteros explícitos. Para un nodo en la posición $i$ del arreglo:

- Su **padre** (si existe) está en la posición $\lfloor (i - 1) / 2 \rfloor$
- Su **hijo izquierdo** (si existe) está en la posición $2i + 1$
- Su **hijo derecho** (si existe) está en la posición $2i + 2$

Esta representación es muy eficiente en términos de espacio: el árbol y el arreglo son la misma estructura vista de dos formas diferentes. Un _max-heap_ cumple la **propiedad de heap**: todo nodo padre es mayor o igual que sus hijos, lo que garantiza que la raíz contiene el máximo.

#### Funcionamiento

Heapsort consta de dos fases principales:

Construcción del _Heap_ (_Heapify_)
: Se transforma el arreglo de entrada en un _heap_ de máximos. Esto se hace comenzando desde el último nodo no hoja (índice $\lfloor n/2 \rfloor - 1$) y aplicando la operación _downHeap_ (hundir) sobre cada nodo hasta llegar a la raíz. _downHeap_ compara un nodo con sus hijos y, si es menor que alguno, lo intercambia con el mayor de ellos, repitiendo el proceso hacia abajo hasta que el nodo quede en posición correcta. Esta fase toma $O(n)$ tiempo.

Extracción de Elementos (_Sort_)
: Una vez construido el _heap_, la raíz contiene el máximo. Se intercambia la raíz con la última posición del _heap_, se reduce el tamaño del _heap_ en uno (el elemento intercambiado queda en su posición final) y se aplica _downHeap_ sobre la nueva raíz para restaurar la propiedad de _heap_. Se repite este proceso hasta que el _heap_ queda con un solo elemento. Esta etapa es similar al algoritmo de **Selección**.

```{admonition} Importante
:class: important

Para ordenar de menor a mayor se construye un _max-heap_ (la raíz es el mayor). Para ordenar de mayor a menor se construye un _min-heap_ (la raíz es el menor).
```

```{code-block} text
---
linenos: true
caption: Heapsort (Ordenamiento por Montículos)
---
FUNCION Heapsort(arreglo)
    n ← longitud(arreglo)

    // Heapify: Construir el _heap_ de máximo
    // En un _heap_ el último nodo que no es hoja es el nodo en la posición n/2 - 1
    // Al hundir cada nodo desde (n/2)-1 hasta 0, se asegura que todos los nodos
    // cumplen la propiedad de heap
    // y por lo tanto el arreglo se convierte en un _heap_ de máximos
    PARA i DESDE (n/2)-1 HASTA 0 HACER
        downHeap(arreglo, n, i)

    // Extraer elementos del _heap_ uno por uno
    PARA i DESDE n - 1 HASTA 1 HACER
        Intercambiar(arreglo, 0, i) // Mover el máximo (raíz del heap) al final del _heap_.
        downHeap(arreglo, i, 0) // Restaurar la propiedad de _heap_ en el _heap_ reducido
    FIN PARA
    RETORNAR arreglo // El arreglo ahora está ordenado
FIN FUNCION
```

<div class="only-html">

A continuación se puede visualizar paso a paso el funcionamiento de Heapsort.
Se puede ingresar un arreglo de hasta 10 elementos separados por coma, o generar uno
aleatorio con el botón **Generar**. Luego, usar los botones ◀ ▶ para avanzar
paso a paso, o >> para reproducir la animación de forma automática. El applet
muestra el arreglo y, debajo, el árbol binario que representa el _heap_. En la
fase de _heapify_ se observa cómo cada nodo se "hunde" intercambiándose con
sus hijos. En la fase de extracción, la última hoja se desconecta del árbol y
la posición correspondiente del arreglo se marca como fuera del _heap_.

<iframe src="/applets/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos/heapsort-visualizer_light.html" width="100%" height="620px" class="only-light-mode"></iframe>

<iframe src="/applets/4-diseno-de-algoritmos/4-6-ordenamientos-recursivos/heapsort-visualizer_dark.html" width="100%" height="620px" class="only-dark-mode"></iframe>

</div>

#### Análisis de la Complejidad Computacional

La complejidad temporal de Heapsort es **$O(n \log n)$** en todos los casos (mejor, promedio y peor). Esto se debe a que la fase de construcción del _heap_ toma $O(n)$ tiempo y la etapa de extracción de elementos toma $O(n \log n)$.

##### Heapify

El proceso de heapify (construir un _heap_ a partir de un arreglo desordenado) se realiza de abajo hacia arriba, comenzando desde el último nodo no hoja (índice $\lfloor n/2 \rfloor - 1$) y subiendo hasta la raíz (índice $0$).

Para cada nodo, se aplica la operación _downHeap_, que asegura que el subárbol con raíz en ese nodo cumpla la propiedad de _heap_. La operación _downHeap_ toma un tiempo proporcional a la altura del subárbol, es decir, $O(h)$.

Aunque la altura máxima de un árbol es $\log_2 (n)$, la mayoría de los nodos en un árbol binario completo se encuentran en los niveles inferiores (cerca de las hojas), donde la altura es pequeña (uno o dos). A medida que subimos en el árbol, hay menos nodos en cada nivel, pero la altura de sus subárboles aumenta.

La complejidad total de construir un _heap_ es la suma de los costos de _downHeap_ para todos los nodos. Matemáticamente, esto se puede expresar como:

$$
\sum_{h=0}^{\lfloor \log_2 n \rfloor} \frac{n}{2^{h+1}} \cdot h
$$

Donde $h$ es la altura del nodo, y $\frac{n}{2^{h+1}}$ es el número aproximado de nodos que hay a esa altura. Esta suma se puede simplificar y se demuestra que es $O(n)$. Es decir, el tiempo requerido para convertir un arreglo desordenado en un _heap_ es lineal con el número de elementos en el arreglo.

En resumen, a pesar de que una sola operación de _downHeap_ puede tomar $O(\log n)$, la suma de todas las operaciones de _downHeap_ en el proceso de construcción del _heap_ resulta en una complejidad de tiempo lineal $O(n)$, lo que lo hace muy eficiente.

##### Etapa de Extracción de Elementos

En esta etapa el algoritmo es similar al algoritmo de selección, en el sentido que ambos algoritmos localizan el mayor elemento del arreglo y lo colocan al final del mismo. La diferencia fundamental es que en Heapsort, el mayor elemento siempre está en la posición 0, es decir, en la raíz del árbol, y por lo tanto solo tiene que intercambiarlo con el último elemento del _heap_ y hacer un _downHeap_ de la nueva raíz, lo que tiene un costo $O(\log n)$. La operación se repite $n$ veces dando como resultado un costo total de $O(n)$ del _heapify_, más $O(n \log n)$ de la etapa de extracción de elementos, quedando $O(n \log n)$.

## Comparación y Resumen de Complejidades

```{table} Algoritmos de Ordenamiento Recursivos
| Algoritmo     |      Mergesort      |      Quicksort      |       Heapsort      |
| :------------ | :-----------------: | :-----------------: | :-----------------: |
| Peor Caso     | $O(n \log n)$       | $O(n^2)$            | $O(n \log n)$       |
| Caso Promedio | $O(n \log n)$       | $O(n \log n)$       | $O(n \log n)$       |
| Mejor Caso    | $O(n \log n)$       | $O(n \log n)$       | $O(n \log n)$       |
| Estable       | Sí                  | No                  | No                  |
| _In Place_    | No                  | Sí                  | Sí                  |
| _Online_      | No                  | No                  | No                  |
```

Como podemos observar, los algoritmos recursivos de "divide y vencerás" (Mergesort, Quicksort) y el basado en estructura de datos eficiente (Heapsort) superan significativamente a los algoritmos simples de $O(n^2)$ para grandes volúmenes de datos, llevando la complejidad a un óptimo $O(n \log n)$. La elección entre ellos dependerá de factores como la disponibilidad de memoria (Mergesort vs. Quicksort/Heapsort), la necesidad de estabilidad, y la garantía de rendimiento en el peor caso.

```{admonition} Importante
:class: important

Los algoritmos de ordenamiento, basados en comparaciones (es decir que deben comparar cada elemento con los restantes) realizan al menos $n \log(n)$ operaciones simples. Es decir no hay forma de obtener un algoritmo con una mejor cota temporal que $O(n \log n)$ para el peor caso o el caso promedio.
```

## Ejercicios

Los ejercicios de este capítulo están en el directorio
[`06-ordenamientos-recursivos/ejercicios/`](https://github.com/untref-ayp2/taller-algoritmos/tree/main/06-ordenamientos-recursivos/ejercicios)
del repositorio
[`taller-algoritmos`](https://github.com/untref-ayp2/taller-algoritmos).
Cada ejercicio tiene un esqueleto con `// TODO` y su correspondiente batería de tests.
Para resolverlos, clonar el repositorio, completar las funciones y ejecutar `go test ./...`.
