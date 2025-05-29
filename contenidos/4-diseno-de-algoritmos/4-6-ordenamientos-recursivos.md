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
: Un algoritmo es "in-place" si requiere una cantidad constante de espacio adicional para ordenar los datos, lo que significa que puede ordenar los datos sin necesidad de estructuras auxiliares significativas.

En línea (_Online_)
: Un algoritmo es "online" si puede procesar los datos a medida que llegan, sin necesidad de conocer el conjunto completo de antemano. Esto es útil en aplicaciones donde los datos se generan en tiempo real.

Existen muchos algoritmos de ordenamiento, cada uno con sus propias fortalezas y debilidades. Algunos de los más conocidos, y a menudo los primeros que se estudian, son los **algoritmos de ordenamiento simple**, por nombrarlos de alguna forma:

Ordenamiento por Inserción (Insertion Sort)
: Construye la lista final ordenada un elemento a la vez. Es eficiente para pequeñas cantidades de datos o datos casi ordenados. Su idea es similar a ordenar cartas en la mano: se toma una carta nueva y se inserta en su posición correcta entre las ya ordenadas.

Ordenamiento por Selección (Selection Sort)
: Encuentra repetidamente el elemento mínimo (o máximo) del resto no ordenado y lo coloca al principio (o al final) de la lista ordenada. Es simple de entender pero no muy eficiente para grandes conjuntos de datos.

Ordenamiento por Burbujeo (Bubble Sort)
: Recorre repetidamente la lista, compara elementos adyacentes y los intercambia si están en el orden incorrecto. Las "burbujas" de elementos más grandes (o más pequeños) se mueven hacia el final (o el principio) de la lista. Es un algoritmo muy intuitivo pero extremadamente ineficiente para grandes conjuntos de datos.

```{table} Algoritmos de Ordenamiento Simple
| Algoritmo                  | Complejidad Temporal (Peor) | Estable     | In Place  | Online    |
| :------------------------: | :-------------------------: | :---------: | :-------: | :-------: |
| Ordenamiento por Inserción | $O(n^2)$                    |     Sí      |    Sí     |    Sí     |
| Ordenamiento por Selección | $O(n^2)$                    |     No      |    Sí     |    Sí     |
| Ordenamiento por Burbujeo  | $O(n^2)$                    |     Sí      |    Sí     |    Sí     |
```

Estos algoritmos son fáciles de implementar y entender, lo que los hace ideales para introducir conceptos básicos de ordenamiento. Sin embargo, su rendimiento se degrada rápidamente a medida que el número de elementos crece, lo que los limita a conjuntos de datos pequeños o casi ordenados. Por ejemplo, el **ordenamiento por inserción** es eficiente para listas pequeñas o listas que ya están casi ordenadas, mientras que el **ordenamiento por selección** y el **ordenamiento por burbujeo** son más adecuados para fines educativos que para aplicaciones prácticas en grandes volúmenes de datos.

Estos algoritmos simples tienen una complejidad computacional de $O(n^2)$, donde $n$ es el número de elementos a ordenar. Esto significa que a medida que $n$ crece, el tiempo de ejecución aumenta cuadráticamente, lo que los hace imprácticos para conjuntos de datos grandes. Para superar esta limitación, se han desarrollado algoritmos de ordenamiento más avanzados, a menudo basados en el paradigma "**divide y vencerás**", que explotan la recursión para lograr eficiencias significativamente mayores. Nos centraremos en tres de los algoritmos de ordenamiento recursivo más populares: **Mergesort, Quicksort y Heapsort**, analizando en detalle su funcionamiento y su complejidad computacional.

## Algoritmos de Ordenamiento Recursivo

Los algoritmos de ordenamiento recursivo que analizaremos aquí —Mergesort, Quicksort y Heapsort— son ejemplos paradigmáticos de cómo el diseño recursivo puede conducir a soluciones eficientes para problemas complejos. A menudo logran una complejidad de tiempo $O(n \log n)$, lo que representa una mejora sustancial sobre los algoritmos de $O(n^2)$ para conjuntos de datos grandes.

## Mergesort (Ordenamiento por Mezcla)

**Mergesort** es un algoritmo de ordenamiento basado en el paradigma "divide y vencerás". Es un algoritmo de **ordenamiento estable**. Fue creado en 1945 por John von Neumann y es uno de los algoritmos de ordenamiento más eficientes y ampliamente utilizados.

```{code-block}
:linenos:
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
:emphasize lines: 2, 7
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

### Funcionamiento

Divide
: El algoritmo divide recursivamente la lista desordenada en dos sublistas de aproximadamente la mitad del tamaño hasta que cada sublista contiene solo un elemento (que por definición está ordenado).

Vencerás (Conquistar)
: Cada sublista de un solo elemento se considera ordenada (caso base).

Combina (Mezcla)
: Las sublistas ordenadas se mezclan repetidamente para producir nuevas sublistas ordenadas hasta que solo quede una sublista, que es la lista original pero ahora completamente ordenada. La operación clave aquí es la **mezcla (merge)** de dos listas ordenadas en una sola lista ordenada.

En la siguiente animación se muestra cómo Mergesort ordena la lista `[38, 9, 43, 3, 9, 82, 10]`. Los `9` aparecen coloreados para observar como se mantienen en el mismo orden relativo durante el proceso de ordenamiento, lo que demuestra la estabilidad del algoritmo. 
<!-- markdownlint-disable MD033 -->
<p class="align-center">
  <video src="../_static/videos/Mergesort.mp4" width="80%"controls autoplay></video>
</p>
<!-- markdownlint-enable MD033 -->


### Análisis de la Complejidad Computacional:

#### Tiempo de Ejecución

La recurrencia para el tiempo de ejecución de Mergesort se puede expresar como:
$T(n) = 2T(n/2) + O(n)$
Donde:
* $2T(n/2)$ representa el costo de ordenar las dos sublistas de tamaño $n/2$.
* $O(n)$ representa el costo de la operación de mezcla (merge), ya que en el peor caso se recorren todos los elementos de ambas sublistas una vez para fusionarlas.

Aplicando el Teorema Maestro, se obtiene que la complejidad de tiempo es **$O(n \log n)$**, ya que subdivide recursivamente el arreglo en mitades hasta llegar al caso base y luego combina los resultados de manera lineal.

En este algoritmo no hay un caso mejor o peor, ya que la división y la mezcla siempre ocurren de la misma manera, lo que da como resultado una complejidad de tiempo consistente. 

#### Espacio de Almacenamiento

Mergesort requiere un espacio auxiliar de $O(n)$ para la operación de mezcla. Esto se debe a que se necesita un arreglo temporal para almacenar los elementos mezclados antes de copiarlos de vuelta al arreglo original. Esto lo convierte en un algoritmo que **no es "in-place"** (en el lugar).

## Quicksort (Ordenamiento Rápido)

**Quicksort**, como Mergesort, es un algoritmo de ordenamiento basado en el paradigma "divide y vencerás". Sin embargo, su enfoque es diferente y su eficiencia en la práctica lo ha convertido en uno de los algoritmos de ordenamiento más utilizados. Quicksort **no es un algoritmo de ordenamiento estable** y estrictamente hablando tampoco se puede asegurar que sea de división y conquista, ya que por la forma de partir el arreglo, no se puede asegurar que las sublistas resultantes sean de tamaño similar. A pesar de esto, es ampliamente considerado como uno de los algoritmos más eficientes para ordenar grandes volúmenes de datos.


**Funcionamiento:**

1.  **Divide (Particiona):** Se elige un elemento de la lista llamado **pivote**. Se reorganiza la lista de tal manera que todos los elementos menores que el pivote queden a su izquierda y todos los elementos mayores queden a su derecha. Los elementos iguales al pivote pueden ir a cualquier lado. Después de esta partición, el pivote se encuentra en su posición final ordenada.
2.  **Vencerás (Conquistar):** Se ordenan recursivamente las dos sublistas (la de elementos menores al pivote y la de elementos mayores al pivote).
3.  **Combina:** No hay una fase de combinación explícita, ya que la lista se ordena "en el lugar" a medida que las sublistas se ordenan recursivamente. La lista completa queda ordenada una vez que todas las sublistas han sido procesadas.

La elección del pivote es crucial para el rendimiento de Quicksort. Estrategias comunes incluyen: el primer elemento, el último elemento, el elemento central, o un elemento aleatorio.

**Ejemplo Ilustrativo:**

Supongamos que queremos ordenar la lista: `[10, 80, 30, 90, 40, 50, 70]`
Elegimos el último elemento como pivote: `70`

1.  **Partición (usando 70 como pivote):**
    * Se recorre el arreglo, moviendo elementos menores que 70 a la izquierda y mayores a la derecha.
    * Después de la partición, la lista podría verse así: `[10, 40, 30, 50, | 70 | , 90, 80]` (Los elementos a la izquierda de 70 son menores, los de la derecha son mayores)

2.  **Llamadas Recursivas:**
    * Ordenar la sublista izquierda: `[10, 40, 30, 50]`
    * Ordenar la sublista derecha: `[90, 80]`

    Esto se repite hasta que las sublistas tengan un solo elemento o estén vacías.

**Análisis de la Complejidad Computacional:**

* **Tiempo de Ejecución:**

    * **Mejor Caso y Caso Promedio:** $O(n \log n)$. Esto ocurre cuando la partición del pivote divide la lista en dos sublistas de tamaños aproximadamente iguales. La recurrencia es similar a la de Mergesort: $T(n) = 2T(n/2) + O(n)$.
    * **Peor Caso:** $O(n^2)$. Esto ocurre cuando la elección del pivote resulta en particiones extremadamente desequilibradas, por ejemplo, cuando el pivote es siempre el elemento más pequeño o el más grande de la sublista. En este escenario, una sublista es de tamaño $n-1$ y la otra es de tamaño 0, llevando a una recurrencia $T(n) = T(n-1) + O(n)$, que se resuelve a $O(n^2)$. Un ejemplo de esto es cuando el arreglo ya está ordenado o casi ordenado, y se elige el primer o último elemento como pivote. Para mitigar esto, se suelen usar estrategias como elegir un pivote aleatorio o la "mediana de tres".

* **Espacio de Almacenamiento:**
    * **Mejor Caso y Caso Promedio:** $O(\log n)$ debido a la profundidad de la pila de llamadas recursivas.
    * **Peor Caso:** $O(n)$ si la partición es muy desequilibrada, ya que la profundidad de la recursión puede llegar a $n$.

**Ventajas:**
* Muy rápido en la práctica para grandes conjuntos de datos en el caso promedio.
* Es un algoritmo "**in-place**" (generalmente), lo que significa que requiere muy poco espacio auxiliar (solo para la pila de recursión).

**Desventajas:**
* Rendimiento en el peor caso ($O(n^2)$) es pobre, aunque es raro en la práctica con una buena elección de pivote.
* No es un algoritmo estable.

## Heapsort (Ordenamiento por Montículos)

**Heapsort** es un algoritmo de ordenamiento basado en la estructura de datos llamada "**heap**" (montículo). Un heap es un árbol binario completo que satisface la propiedad de heap: para un heap de máximo, cada nodo padre es mayor o igual que sus nodos hijos; para un heap de mínimo, cada nodo padre es menor o igual que sus nodos hijos. Heapsort típicamente utiliza un heap de máximo.

**Funcionamiento:**

Heapsort consta de dos fases principales:

1.  **Construcción del Heap (Heapify):** Se transforma el arreglo de entrada en un heap de máximo. Esto se hace comenzando desde el último nodo no hoja y "hundiendo" cada elemento hacia abajo en el árbol para asegurar que la propiedad de heap se mantenga. Esta fase toma $O(n)$ tiempo.
2.  **Extracción de Elementos (Sort):** Una vez que el arreglo es un heap de máximo, el elemento más grande (la raíz del heap) está en la primera posición.
    * Se intercambia el elemento raíz con el último elemento del heap.
    * Se reduce el tamaño del heap en uno (excluyendo el elemento que acaba de ser colocado en su posición final).
    * Se "hunde" el nuevo elemento raíz (que era el último elemento) para restaurar la propiedad de heap.
    * Estos pasos se repiten hasta que el tamaño del heap sea 1.

**Ejemplo Ilustrativo:**

Supongamos que queremos ordenar la lista: `[4, 10, 3, 5, 1]`

1.  **Construcción del Heap de Máximo:**
    Transformar `[4, 10, 3, 5, 1]` en un heap de máximo.
    (Visualmente, esto implica reorganizar los nodos para que los padres sean mayores que sus hijos).
    El heap resultante podría ser (representado como un arreglo): `[10, 5, 3, 4, 1]` (donde 10 es la raíz, 5 y 3 son sus hijos, etc.)

2.  **Extracción y Ordenamiento:**
    * **Paso 1:** Intercambiar 10 (raíz) con 1 (último). Arreglo: `[1, 5, 3, 4, | 10]`. El 10 está en su posición final.
        * Restaurar heap en `[1, 5, 3, 4]`. Hundir 1. Heap: `[5, 4, 3, | 1]`.
    * **Paso 2:** Intercambiar 5 (raíz) con 1 (último). Arreglo: `[1, 4, 3, | 5, 10]`. El 5 está en su posición final.
        * Restaurar heap en `[1, 4, 3]`. Hundir 1. Heap: `[4, 3, | 1]`.
    * **Paso 3:** Intercambiar 4 (raíz) con 1 (último). Arreglo: `[1, 3, | 4, 5, 10]`. El 4 está en su posición final.
        * Restaurar heap en `[1, 3]`. Hundir 1. Heap: `[3, | 1]`.
    * **Paso 4:** Intercambiar 3 (raíz) con 1 (último). Arreglo: `[1, | 3, 4, 5, 10]`. El 3 está en su posición final.
        * Heap restante: `[1]` (ordenado).
    La lista final ordenada es: `[1, 3, 4, 5, 10]`

**Análisis de la Complejidad Computacional:**

* **Tiempo de Ejecución:**
    * **Construcción del Heap:** $O(n)$. Aunque `heapify-down` (la operación de hundir un elemento) toma $O(\log n)$ en el peor caso, la suma de los costos de `heapify-down` para todos los nodos en la construcción del heap da como resultado un tiempo total de $O(n)$.
    * **Extracción de Elementos:** Se realizan $n-1$ extracciones. Cada extracción implica un intercambio y una operación de `heapify-down` (que toma $O(\log n)$ tiempo). Por lo tanto, esta fase toma $O(n \log n)$.

    La suma de ambas fases da:
    * **Mejor Caso, Promedio y Peor Caso:** $O(n \log n)$. Heapsort tiene un rendimiento de tiempo de ejecución garantizado de $O(n \log n)$ en todos los casos.

* **Espacio de Almacenamiento:**
    Heapsort es un algoritmo "**in-place**", lo que significa que solo requiere una cantidad constante de espacio auxiliar ($O(1)$) más allá del espacio para el arreglo de entrada.

**Ventajas:**
* Rendimiento garantizado de $O(n \log n)$ en todos los casos (mejor, promedio y peor).
* Es un algoritmo "in-place", lo que lo hace eficiente en el uso de memoria.

**Desventajas:**
* No es un algoritmo estable.
* En la práctica, puede ser un poco más lento que Quicksort en el caso promedio debido a la constante más grande en su tiempo de ejecución, y a que sus operaciones involucran más accesos no secuenciales a memoria.

---

## Comparación y Resumen de Complejidades

| Algoritmo       | Complejidad Temporal (Mejor) | Complejidad Temporal (Promedio) | Complejidad Temporal (Peor) | Espacio Auxiliar | Es Estable? |
| :-------------- | :--------------------------- | :------------------------------ | :-------------------------- | :--------------- | :---------- |
| **Mergesort** | $O(n \log n)$                | $O(n \log n)$                   | $O(n \log n)$               | $O(n)$           | Sí          |
| **Quicksort** | $O(n \log n)$                | $O(n \log n)$                   | $O(n^2)$                    | $O(\log n)$ (promedio), $O(n)$ (peor) | No          |
| **Heapsort** | $O(n \log n)$                | $O(n \log n)$                   | $O(n \log n)$               | $O(1)$           | No          |
| *Inserción* | $O(n)$                       | $O(n^2)$                        | $O(n^2)$                    | $O(1)$           | Sí          |
| *Selección* | $O(n^2)$                     | $O(n^2)$                        | $O(n^2)$                    | $O(1)$           | No          |
| *Burbuja* | $O(n)$                       | $O(n^2)$                        | $O(n^2)$                    | $O(1)$           | Sí          |

Como podemos observar, los algoritmos recursivos de "divide y vencerás" (Mergesort, Quicksort) y el basado en estructura de datos eficiente (Heapsort) superan significativamente a los algoritmos simples de $O(n^2)$ para grandes volúmenes de datos, llevando la complejidad a un óptimo $O(n \log n)$. La elección entre ellos dependerá de factores como la disponibilidad de memoria (Mergesort vs. Quicksort/Heapsort), la necesidad de estabilidad, y la garantía de rendimiento en el peor caso.

---

## Conclusión: Más Allá de las Comparaciones por Comparación

Los algoritmos de ordenamiento recursivo como Mergesort, Quicksort y Heapsort representan pilares fundamentales en la algoritmia moderna. Su eficiencia, lograda a través de la estrategia "divide y vencerás" o la manipulación de estructuras de datos optimizadas, los hace indispensables para procesar grandes volúmenes de información en diversas aplicaciones, desde bases de datos hasta sistemas operativos. Hemos visto cómo, aunque todos comparten una complejidad temporal asintótica de $O(n \log n)$ en sus casos promedio, difieren en su uso de espacio y su comportamiento en el peor caso, ofreciendo un abanico de opciones para el desarrollador.

Sin embargo, el mundo de los algoritmos de ordenamiento es vasto y no se detiene aquí. Los algoritmos que hemos analizado son "**algoritmos de comparación**", lo que significa que basan su funcionamiento en comparar pares de elementos para determinar su orden relativo. Existe una clase diferente de algoritmos de ordenamiento que no se basan en comparaciones y que, bajo ciertas condiciones sobre las claves de los elementos a ordenar, pueden superar el límite inferior de $O(n \log n)$ establecido para los algoritmos de comparación.

Para conjuntos de datos donde las claves tienen una distribución conocida o pueden ser representadas de ciertas maneras (por ejemplo, números enteros dentro de un rango específico), surgen algoritmos como:

* **Ordenamiento por Urnas (Bucket Sort):** Este algoritmo distribuye los elementos en un número finito de "urnas" o "cubetas". Cada urna se ordena individualmente (posiblemente usando otro algoritmo de ordenamiento o recursivamente), y luego las urnas se concatenan para obtener la lista final ordenada. Es muy eficiente cuando los elementos están uniformemente distribuidos.
* **Ordenamiento por Radix (Radix Sort):** Este algoritmo ordena números procesando dígitos individuales (o bits) de forma iterativa, ya sea de derecha a izquierda (LSD - Least Significant Digit) o de izquierda a derecha (MSD - Most Significant Digit). No realiza comparaciones directas entre los números, sino que se basa en la distribución de sus dígitos.

Estos algoritmos, que aprovechan información adicional sobre la estructura de las claves, ofrecen una fascinante puerta de entrada a soluciones aún más rápidas en contextos específicos. Su análisis y comprensión serán el objeto de un próximo apunte, donde profundizaremos en cómo explotar la información sobre las claves para lograr un ordenamiento ultra eficiente.