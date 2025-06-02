---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Ordenamientos Recursivos
## Introducción: La Importancia del Orden

El **ordenamiento de datos** es una de las operaciones fundamentales en la informática y la ciencia de datos. Desde organizar una lista de contactos por nombre hasta clasificar resultados de búsqueda por relevancia o procesar grandes volúmenes de datos para análisis estadísticos, la capacidad de ordenar eficientemente la información es crucial. Un conjunto de datos ordenado facilita enormemente la búsqueda, la inserción y la eliminación, mejorando el rendimiento de casi cualquier aplicación que trabaje con colecciones de elementos.

Pensemos en la vida cotidiana: una biblioteca donde los libros están ordenados alfabéticamente por autor, un cajón de herramientas donde los destornilladores están por tamaño, o una lista de precios en un supermercado. En todos estos casos, el orden nos permite encontrar lo que necesitamos de forma rápida y eficiente. En el ámbito computacional, este principio se traduce en algoritmos que, a través de diversas estrategias, transforman una secuencia desordenada en una secuencia ordenada.

Algunas características de los algoritmos de ordenamiento incluyen:

Complejidad temporal
: La cantidad de tiempo que un algoritmo tarda en ordenar un conjunto de datos. Se mide en función del número de elementos a ordenar y se expresa comúnmente en notación O grande (por ejemplo, $O(n \log n)$, $O(n^2)$).

Estabilidad
: Un algoritmo es estable si mantiene el orden relativo de los elementos iguales después del ordenamiento. Esto es importante en situaciones donde los elementos tienen múltiples claves de ordenamiento.  

En el lugar (_In-place_)
: Un algoritmo es "_in-place_" si requiere una cantidad constante de espacio adicional para ordenar los datos, lo que significa que puede ordenar los datos sin necesidad de estructuras auxiliares significativas.

En línea (_Online_)
: Un algoritmo es "online" si puede procesar los datos a medida que llegan, sin necesidad de conocer el conjunto completo de antemano. Esto es útil en aplicaciones donde los datos se generan en tiempo real.

Existen muchos algoritmos de ordenamiento, cada uno con sus propias fortalezas y debilidades. Algunos de los más conocidos, y a menudo los primeros que se estudian, son los **algoritmos de ordenamiento simple**, por nombrarlos de alguna forma:

Ordenamiento por Inserción (_Insertion Sort_)
: Construye la lista final ordenada un elemento a la vez. Es eficiente para pequeñas cantidades de datos o datos casi ordenados. Su idea es similar a ordenar cartas en la mano: se toma una carta nueva y se inserta en su posición correcta entre las ya ordenadas.

Ordenamiento por Selección (_Selection Sort_)
: Encuentra repetidamente el elemento mínimo (o máximo) del resto no ordenado y lo coloca al principio (o al final) de la lista ordenada. Es simple de entender pero no muy eficiente para grandes conjuntos de datos.

Ordenamiento por Burbujeo (_Bubble Sort_)
: Recorre repetidamente la lista, compara elementos adyacentes y los intercambia si están en el orden incorrecto. Las "burbujas" de elementos más grandes (o más pequeños) se mueven hacia el final (o el principio) de la lista. Es un algoritmo muy intuitivo pero extremadamente ineficiente para grandes conjuntos de datos.

```{table} Algoritmos de Ordenamiento Simple
|         Algoritmo          | Complejidad Temporal (Peor) | Estable | _In Place_ | _Online_ |
| :------------------------: | :-------------------------: | :-----: | :--------: | :------: |
| Ordenamiento por Inserción |          $O(n^2)$           |   Sí    |     Sí     |    Sí    |
| Ordenamiento por Selección |          $O(n^2)$           |   No    |     Sí     |    Sí    |
| Ordenamiento por Burbujeo  |          $O(n^2)$           |   Sí    |     Sí     |    Sí    |
```

Estos algoritmos son fáciles de implementar y entender, lo que los hace ideales para introducir conceptos básicos de ordenamiento. Sin embargo, su rendimiento se degrada rápidamente a medida que el número de elementos crece, lo que los limita a conjuntos de datos pequeños o casi ordenados. Por ejemplo, el **ordenamiento por inserción** es eficiente para listas pequeñas o listas que ya están casi ordenadas, mientras que el **ordenamiento por selección** y el **ordenamiento por burbujeo** son más adecuados para fines educativos que para aplicaciones prácticas en grandes volúmenes de datos.

Los tres algoritmos tienen una complejidad computacional de $O(n^2)$, donde $n$ es el número de elementos a ordenar. Esto significa que a medida que $n$ crece, el tiempo de ejecución aumenta cuadráticamente, lo que los hace imprácticos para conjuntos de datos grandes. Para superar esta limitación, se han desarrollado algoritmos de ordenamiento más avanzados, a menudo basados en el paradigma "**divide y vencerás**", que explotan la recursión para lograr eficiencias significativamente mayores. Nos centraremos en tres de los algoritmos de ordenamiento recursivo más populares: **Mergesort, Quicksort y Heapsort**, analizando en detalle su funcionamiento y su complejidad computacional.

## Algoritmos de Ordenamiento Recursivo

Los algoritmos de ordenamiento recursivo que analizaremos aquí —Mergesort, Quicksort y Heapsort— son ejemplos paradigmáticos de cómo el diseño recursivo puede conducir a soluciones eficientes para problemas complejos. A menudo logran una complejidad de tiempo $O(n \log n)$, lo que representa una mejora sustancial sobre los algoritmos de $O(n^2)$ para conjuntos de datos grandes.

## Mergesort (Ordenamiento por Mezcla)

**Mergesort** es un algoritmo **estable**, que requiere espacio adicional proporcional al tamaño del arreglo, es decir no es **_in place_**, basado en el paradigma "divide y vencerás". Fue creado en 1945 por John von Neumann y es uno de los algoritmos de ordenamiento más eficientes y ampliamente utilizados.

### Funcionamiento

Dividir
: El algoritmo divide recursivamente la lista desordenada en dos sublistas de aproximadamente la mitad del tamaño hasta que cada sublista contiene solo un elemento (que por definición está ordenado).

Conquistar
: Cada sublista de un solo elemento se considera ordenada (caso base).

Combinar
: Las sublistas ordenadas se mezclan repetidamente para producir nuevas sublistas ordenadas hasta que solo quede una sublista, que es la lista original pero ahora completamente ordenada. La operación clave aquí es la **mezcla (merge)** de dos listas ordenadas en una sola lista ordenada.

```{code-block}
:linenos:
:name: mergesort
:caption: Mergesort (Ordenamiento por Mezcla)
funcion mergeSort(arreglo)
  si longitud(arreglo) <= 1 entonces // Caso base: si el arreglo tiene 
                                     // 0 o 1 elementos, ya está ordenado
    retornar arreglo
  fin si

  mitad ← longitud(arreglo) / 2
  izquierda ← mergeSort(subarreglo desde 0 hasta mitad-1)
  derecha ← mergeSort(subarreglo desde mitad hasta fin)
  retornar merge(izquierda, derecha)
fin funcion
```

```{code-block}
:linenos:
:name: merge
:emphasize-lines: 2, 7
:caption: Función de Mezcla (Merge)
funcion merge(izquierda, derecha)
  resultado ← arreglo vacío // Arreglo para almacenar la mezcla
  i ← 0 // Índice para la sublista izquierda
  j ← 0 // Índice para la sublista derecha

  mientras i < longitud(izquierda) y j < longitud(derecha) hacer
    si izquierda[i] <= derecha[j] entonces
      agregar izquierda[i] a resultado
      i ← i + 1
    sino
      agregar derecha[j] a resultado
      j ← j + 1
    fin si
  fin mientras

  // Agregar los elementos restantes de izquierda, si los hay
  mientras i < longitud(izquierda) hacer
    agregar izquierda[i] a resultado
    i ← i + 1
  fin mientras

  // Agregar los elementos restantes de derecha, si los hay
  mientras j < longitud(derecha) hacer
    agregar derecha[j] a resultado
    j ← j + 1
  fin mientras

  retornar resultado
fin funcion
```
En la línea 2 de la función `merge`, por cada mezcla que se realiza se crea un nuevo arreglo `resultado` que contendrá los elementos ordenados de las dos sublistas. Esto es necesario porque Mergesort no modifica las listas originales, sino que crea una nueva lista ordenada a partir de ellas.

En la línea 7 de la función `merge` es fundamental que se compare por menor igual (`<=`) para garantizar la estabilidad del algoritmo, es decir, que los elementos iguales mantengan su orden relativo original.

A continuación se puede visualizar paso a paso el funcionamiento de Mergesort:

<iframe src="https://opendsa-server.cs.vt.edu/embed/mergesortAV" height="650" width="100%" scrolling="no"></iframe>

### Análisis de la Complejidad Computacional:

La recurrencia para el tiempo de ejecución de Mergesort se puede expresar como:
$T(n) = 2T(n/2) + O(n)$
Donde:
* $2T(n/2)$ representa el costo de ordenar las dos sublistas de tamaño $n/2$.
* $O(n)$ representa el costo de la operación de mezcla (merge), ya que en el peor caso se recorren todos los elementos de ambas sublistas una vez para fusionarlas.

Aplicando el Teorema Maestro, se obtiene que la complejidad de tiempo es **$O(n \log n)$**, ya que subdivide recursivamente el arreglo en mitades hasta llegar al caso base y luego combina los resultados de manera lineal.

En este algoritmo no hay un caso mejor o peor, ya que la división y la mezcla siempre ocurren de la misma manera, lo que da como resultado una complejidad de tiempo consistente. 

## Quicksort (Ordenamiento Rápido)

**Quicksort**, como **Mergesort**, es un algoritmo de ordenamiento basado en el paradigma "divide y vencerás". Sin embargo, su enfoque es diferente y su eficiencia en la práctica lo ha convertido en uno de los algoritmos de ordenamiento más utilizados. Quicksort **no es un algoritmo de ordenamiento estable** pero si es **in-place** y estrictamente hablando tampoco se puede asegurar que sea de división y conquista, ya que por la forma de partir el arreglo, no se puede asegurar que las sublistas resultantes sean de tamaño similar. A pesar de esto, es ampliamente considerado como uno de los algoritmos más eficientes para ordenar grandes volúmenes de datos.

La idea principal detrás de Quicksort es seleccionar un elemento de la lista, llamado **pivote**, y reorganizar los elementos de tal manera que todos los elementos menores que el pivote queden a su izquierda y todos los elementos mayores queden a su derecha. Luego, se aplica recursivamente el mismo proceso a las sublistas resultantes. Los elementos a la izquierda y derecha del pivote no están necesariamente ordenados, pero el pivote estará en su posición final ordenada después de la partición. 

Esta técnica de paritición es lo que distingue a Quicksort de otros algoritmos de ordenamiento, se conoce como **partición de 3 vías**.

**Quicksort** fue creado y publicado por Tony Hoare en 1961.

### Funcionamiento

Dividir
: Se elige un elemento de la lista llamado **pivote**. Se reorganiza la lista de tal manera que todos los elementos menores que el pivote queden a su izquierda y todos los elementos mayores queden a su derecha. Los elementos iguales al pivote pueden ir a la izquierda o a la derecha del pivote. Después de esta partición, el pivote se encuentra en su posición final ordenada.

Conquistar
: Se ordenan recursivamente las dos sublistas (la de elementos menores al pivote y la de elementos mayores al pivote).

Combinar
: No hay una fase de combinación explícita, ya que la lista se ordena "en el lugar" a medida que las sublistas se ordenan recursivamente. La lista completa queda ordenada una vez que todas las sublistas han sido procesadas.

```{code-block}
:linenos:
:name: quicksort
:caption: Quicksort (Ordenamiento Rápido)
funcion QuickSort(arreglo, inicio, fin)
 si inicio >= fin entonces
    retornar // Caso base: si el subarreglo tiene 0 o 1 elementos, ya está ordenado
  fin si
  // Particionar el arreglo y obtener el índice del pivote
  pivote_indice = Particionar(arreglo, inicio, fin)
  QuickSort(arreglo, inicio, pivote_indice - 1)
  QuickSort(arreglo, pivote_indice + 1, fin)
fin funcion
```
````{code-block}
:linenos:
:name: particionar
:caption: Partición de 3 vías
funcion Particionar(arreglo, inicio, fin)
  // Elegir el elemento del medio como pivote
  medio = (inicio + fin) / 2
  pivote_valor = arreglo[medio]

  // Mover el pivote al final para simplificar la partición
  Intercambiar(arreglo, medio, fin)

  i = inicio
  j = fin - 1

  mientras i <= j hacer
    // Buscar desde la izquierda un elemento mayor que el pivote
    mientras i <= j y arreglo[i] <= pivote_valor hacer
      i = i + 1
    fin mientras

    // Buscar desde la derecha un elemento menor que el pivote
    mientras i <= j y arreglo[j] >= pivote_valor hacer
      j = j - 1
    fin mientras

    // Si ambos índices no se han cruzado, intercambiar los elementos
    si i < j entonces
      Intercambiar(arreglo, i, j)
    fin si
  fin mientras

  // Colocar el pivote en su posición final
  Intercambiar(arreglo, i, fin)

  retornar i // Retorna el índice final del pivote
fin funcion
````

```{code-block}
:linenos:
:name: intercambiar
:caption: Intercambio de elementos
funcion Intercambiar(arreglo, i, j)
  temp = arreglo[i]
  arreglo[i] = arreglo[j]
  arreglo[j] = temp
fin funcion
```

#### Pivote

La elección del pivote es crucial para el rendimiento de Quicksort. Estrategias comunes incluyen: el primer elemento, el último elemento, el elemento central, o un elemento aleatorio.

Si el pivote elegido es justo el mayor elemento del arreglo, o el menor, la partición resultará en una sublista de tamaño $n-1$ y otra de tamaño 0, lo que llevará a un rendimiento cuadrático en el peor caso.

Una técnica común para mitigar esto es elegir el pivote como la "mediana de tres", que toma el primer, el último y el elemento del medio del arreglo y selecciona el que está en el medio de esos tres valores. Esto ayuda a evitar particiones muy desequilibradas.

Por ejemplo, si tenemos un arreglo `[3, 6, 8, 10, 1, 2, 1]` la mediana de tres compara el primer elemento `3`, el último elemento `1` y el del medio `10`, y selecciona `3` como pivote, lo que ayuda a evitar un caso de peor rendimiento.

A continuación se puede visualizar paso a paso el funcionamiento de Quicksort:

<iframe src="https://opendsa-server.cs.vt.edu/embed/quicksortAV" height="450" width="100%" scrolling="no"></iframe>

### Análisis de la Complejidad Computacional:

La complejidad temporal de Quicksort depende de la elección del pivote y de cómo se distribuyen los elementos en el arreglo:

Mejor Caso
: Ocurre cuando el pivote divide el arreglo en dos subarreglos de tamaño aproximadamente igual en cada llamada recursiva. En este caso, la recurrencia es:
  $T(n) = 2T(n/2) + O(n)$. Aplicando el Teorema Maestro, obtenemos una complejidad de tiempo de **$O(n \log n)$**.

Caso Promedio
: En promedio, una buena implemetación de Quicksort también logra una complejidad de tiempo de **$O(n \log n)$**. Es fundamental que la elección del pivote sea aleatoria o que se utilice una estrategia como la mediana de tres para evitar particiones muy desequilibradas.

Peor Caso
: Ocurre cuando el pivote es el elemento más grande o más pequeño en cada llamada recursiva, lo que lleva a una partición muy desequilibrada. En este caso, la recurrencia es $T(n) = T(n-1) + O(n)$, lo que resulta en una complejidad de tiempo de **$O(n^2)$**.

Si bien Quicksort tiene un peor caso de $O(n^2)$, este escenario es raro en la práctica si se elige un buen pivote, por lo que su uso es muy común en aplicaciones reales.

## Heapsort (Ordenamiento por Montículos)

**Heapsort** es un algoritmo que no se basa en el paradigma de "división y conquista", sino que utiliza un _heap_ o montículo como estructura de datos subyacente para ordenar los elementos. 

**Heapsort** no es estable, pero si _in-place_ por lo que no requiere espacio adicional significativo.

Fue desarrollado por J. W. J. Williams en 1964 y es un algoritmo eficiente que garantiza un tiempo de ejecución de $O(n \log n)$ en todos los casos (mejor, promedio y peor).

### Funcionamiento
Heapsort consta de dos fases principales:

Construcción del _Heap_ (_Heapify_)
: Se transforma el arreglo de entrada en un _heap_ de máximos. Esto se hace comenzando desde el último nodo no hoja y "hundiendo (_downHeap_)" cada elemento hacia abajo en el árbol para asegurar que la propiedad de _heap_ se mantenga. Esta fase toma $O(n)$ tiempo.

Extracción de Elementos (Sort)
: Una vez que el arreglo es un heap de máximo, el elemento más grande (la raíz del heap) está en la primera posición. Se intercambia el elemento raíz con el último elemento del heap. Se reduce el tamaño del heap en uno (excluyendo el elemento que acaba de ser colocado en su posición final). Se "hunde" el nuevo elemento raíz (que era el último elemento) para restaurar la propiedad de heap.

```{code-block}
:linenos:
:caption: Heapsort (Ordenamiento por Montículos)
funcion heapsort(arreglo)
  n ← longitud(arreglo)

  // Heapify: Construir el heap de máximo
  // En un heap el útimo nodo que no es hoja es el nodo en la posición n/2 - 1
  // Al hundir cada nodo desde n/2 - 1 hasta 0, se asegura que todos los nodos 
  // cumplen la propiedad de heap
  // y por lo tanto el arreglo se convierte en un heap de máximos
  para i desde n/2 - 1 hasta 0 hacer
    downHeap(arreglo, n, i)

  // Extraer elementos del heap uno por uno
  para i desde n - 1 hasta 1 hacer
    Intercambiar(arreglo,0, i) //Mover el máximo (raíz del heap) al final del arreglo.
    downHeap(arreglo, i, 0) //Restaurar la propiedad de heap en el heap reducido
  fin para
  retornar arreglo // El arreglo ahora está ordenado
fin funcion
```

La función [Intercambiar](#intercambiar) es la misma que en Quicksort.

### Análisis de la Complejidad Computacional:

La complejidad temporal de Heapsort es **$O(n \log n)$** en todos los casos (mejor, promedio y peor). Esto se debe a que la fase de construcción del heap toma $O(n)$ tiempo y cada extracción del elemento máximo (raíz del heap) toma $O(\log n)$ tiempo, ya que se requiere hundir el nuevo elemento raíz para restaurar la propiedad de heap.

La fase de construcción del heap es eficiente porque, aunque parece que se realizan $n$ operaciones de hundimiento, la mayoría de ellas son en nodos que están cerca de las hojas del árbol, lo que reduce el costo promedio por operación.



## Comparación y Resumen de Complejidades

| Algoritmo     | Complejidad Temporal (Mejor) | Complejidad Temporal (Promedio) | Complejidad Temporal (Peor) | Espacio Auxiliar                      | Es Estable? |
| :------------ | :--------------------------- | :------------------------------ | :-------------------------- | :------------------------------------ | :---------- |
| **Mergesort** | $O(n \log n)$                | $O(n \log n)$                   | $O(n \log n)$               | $O(n)$                                | Sí          |
| **Quicksort** | $O(n \log n)$                | $O(n \log n)$                   | $O(n^2)$                    | $O(\log n)$ (promedio), $O(n)$ (peor) | No          |
| **Heapsort**  | $O(n \log n)$                | $O(n \log n)$                   | $O(n \log n)$               | $O(1)$                                | No          |
| *Inserción*   | $O(n)$                       | $O(n^2)$                        | $O(n^2)$                    | $O(1)$                                | Sí          |
| *Selección*   | $O(n^2)$                     | $O(n^2)$                        | $O(n^2)$                    | $O(1)$                                | No          |
| *Burbuja*     | $O(n)$                       | $O(n^2)$                        | $O(n^2)$                    | $O(1)$                                | Sí          |

Como podemos observar, los algoritmos recursivos de "divide y vencerás" (Mergesort, Quicksort) y el basado en estructura de datos eficiente (Heapsort) superan significativamente a los algoritmos simples de $O(n^2)$ para grandes volúmenes de datos, llevando la complejidad a un óptimo $O(n \log n)$. La elección entre ellos dependerá de factores como la disponibilidad de memoria (Mergesort vs. Quicksort/Heapsort), la necesidad de estabilidad, y la garantía de rendimiento en el peor caso.

---

## Conclusión: Más Allá de las Comparaciones por Comparación

Los algoritmos de ordenamiento recursivo como Mergesort, Quicksort y Heapsort representan pilares fundamentales en la algoritmia moderna. Su eficiencia, lograda a través de la estrategia "divide y vencerás" o la manipulación de estructuras de datos optimizadas, los hace indispensables para procesar grandes volúmenes de información en diversas aplicaciones, desde bases de datos hasta sistemas operativos. Hemos visto cómo, aunque todos comparten una complejidad temporal asintótica de $O(n \log n)$ en sus casos promedio, difieren en su uso de espacio y su comportamiento en el peor caso, ofreciendo un abanico de opciones para el desarrollador.

Sin embargo, el mundo de los algoritmos de ordenamiento es vasto y no se detiene aquí. Los algoritmos que hemos analizado son "**algoritmos de comparación**", lo que significa que basan su funcionamiento en comparar pares de elementos para determinar su orden relativo. Existe una clase diferente de algoritmos de ordenamiento que no se basan en comparaciones y que, bajo ciertas condiciones sobre las claves de los elementos a ordenar, pueden superar el límite inferior de $O(n \log n)$ establecido para los algoritmos de comparación.

Para conjuntos de datos donde las claves tienen una distribución conocida o pueden ser representadas de ciertas maneras (por ejemplo, números enteros dentro de un rango específico), surgen algoritmos como:

* **Ordenamiento por Urnas (Bucket Sort):** Este algoritmo distribuye los elementos en un número finito de "urnas" o "cubetas". Cada urna se ordena individualmente (posiblemente usando otro algoritmo de ordenamiento o recursivamente), y luego las urnas se concatenan para obtener la lista final ordenada. Es muy eficiente cuando los elementos están uniformemente distribuidos.
* **Ordenamiento por Radix (Radix Sort):** Este algoritmo ordena números procesando dígitos individuales (o bits) de forma iterativa, ya sea de derecha a izquierda (LSD - Least Significant Digit) o de izquierda a derecha (MSD - Most Significant Digit). No realiza comparaciones directas entre los números, sino que se basa en la distribución de sus dígitos.

Estos algoritmos, que aprovechan información adicional sobre la estructura de las claves, ofrecen una fascinante puerta de entrada a soluciones aún más rápidas en contextos específicos. Su análisis y comprensión serán el objeto de un próximo apunte, donde profundizaremos en cómo explotar la información sobre las claves para lograr un ordenamiento ultra eficiente.