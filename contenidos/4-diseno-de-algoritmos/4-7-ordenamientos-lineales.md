---
label: ordenamientos-lineales
---

# Ordenamientos en Tiempo Lineal

Los algoritmos de ordenamiento del capítulo anterior (Mergesort, Quicksort, Heapsort) se basan en **comparaciones** entre elementos para determinar su orden. Se puede demostrar que cualquier algoritmo de ordenamiento basado en comparaciones requiere al menos $\Omega(n \log n)$ operaciones en el peor caso[^omega]. Esto significa que ningún algoritmo de este tipo puede superar esa cota, sin importar cuán ingenioso sea su diseño.

Sin embargo, si explotamos propiedades específicas de los datos —como que los valores pertenecen a un rango acotado, que están uniformemente distribuidos, o que se pueden descomponer en dígitos— podemos diseñar algoritmos que ordenen en **tiempo lineal** $O(n)$, superando la barrera de $\Omega(n \log n)$. La clave está en que estos algoritmos **no comparan** elementos entre sí: usan los valores como índices, los distribuyen en *buckets* o los procesan dígito a dígito.

Vamos a estudiar tres algoritmos de ordenamiento en tiempo lineal: **Ordenamiento por Conteo (_Counting Sort_)**, **Ordenamiento por Urnas (_Bucket Sort_)** y **Radix Sort**.

## Ordenamiento por Conteo (_Counting Sort_)

El **Ordenamiento por Conteo** ordena elementos enteros dentro de un rango conocido $[0, k]$. En lugar de comparar elementos, cuenta cuántas veces aparece cada valor y luego reconstruye el arreglo ordenado a partir de esas cuentas.

Hay dos variantes del algoritmo y conviene distinguirlas desde el principio:

- La **versión básica** cuenta las apariciones y reconstruye el arreglo recorriendo el arreglo de conteo. Es la más simple, pero **no es estable**.
- La **versión con sumas prefijo** convierte las cuentas en posiciones finales dentro del arreglo ordenado y coloca cada elemento en su lugar. **Es estable**, y por eso es la que se usa como subrutina de Radix Sort.

Las dos comparten la misma idea: el valor del elemento se usa como **índice** de un arreglo auxiliar. Por eso el algoritmo necesita conocer el rango de valores de antemano.

### Versión básica: contar y reconstruir

El algoritmo sigue estos pasos:

1. **Inicialización**: crear un arreglo de conteo de tamaño $k+1$ e inicializarlo en cero.
2. **Conteo**: recorrer el arreglo original y, para cada elemento, incrementar la posición correspondiente del arreglo de conteo.
3. **Reconstrucción**: recorrer el arreglo de conteo en orden creciente y escribir cada valor tantas veces como se contó.

```{code-block} text
---
caption: Counting Sort básico (contar y reconstruir)
linenos: true
---
FUNCION CountingSort(arreglo, k)
    conteo ← arreglo de tamaño k+1 inicializado en 0
    n ← longitud(arreglo)

    PARA i ← 0 HASTA n-1 HACER
        conteo[arreglo[i]] ← conteo[arreglo[i]] + 1
    FIN PARA

    // la reconstrucción lee solo el arreglo de conteo, por eso se puede
    // escribir la salida sobre el mismo arreglo de entrada
    indice ← 0
    PARA valor ← 0 HASTA k HACER
        PARA repeticiones ← 1 HASTA conteo[valor] HACER
            arreglo[indice] ← valor
            indice ← indice + 1
        FIN PARA
    FIN PARA

    RETORNAR arreglo
FIN FUNCION
```

```{admonition} Pisar el arreglo original o devolver uno nuevo
---
class: note
---
La reconstrucción lee únicamente el arreglo de conteo, así que escribir la salida sobre el mismo arreglo de entrada es seguro: no se pisa ningún dato que todavía haga falta. Esa es la versión del pseudocódigo anterior, y tiene la ventaja de no pedir espacio adicional para la salida (más allá del arreglo de conteo, $O(k)$).

La otra opción es reservar un arreglo nuevo de $n$ posiciones y escribir ahí, dejando la entrada intacta. Cuesta $O(n)$ de espacio extra, pero conserva el arreglo original: es lo que se necesita cuando no se puede modificar la entrada o cuando cada elemento tiene información asociada que hay que mantener.
```

```{admonition} La versión básica no es estable
---
class: important
---
Contar y reconstruir alcanza para ordenar, pero no para preservar el orden relativo de los elementos iguales. Si los datos llevan información asociada —una edad con su nombre, un pedido con su fecha, una palabra con su frecuencia—, esa información queda desordenada dentro de cada grupo de valores iguales.
```

#### ¿Por qué no es estable?

Al contar, el algoritmo **descarta la identidad** de cada elemento: solo conserva cuántas veces aparece cada valor. Cuando dos elementos tienen el mismo valor, la reconstrucción los escribe uno detrás del otro sin ninguna información sobre cuál apareció primero. Con enteros sueltos no se nota —dos `3` son indistinguibles—, pero con datos compuestos importa.

No se trata de un descuido de la implementación sino de una consecuencia del diseño: en ningún momento hay una estructura que recuerde el orden de aparición. Y como el algoritmo no compara elementos, tampoco puede desempatar mirando el dato asociado.

Recordar la definición de estabilidad de {ref}`ordenamientos-por-comparacion`: un algoritmo es estable si mantiene el orden relativo de los elementos que tienen la misma clave.

### Versión estable: de cuentas a posiciones

Para que el ordenamiento sea estable hay que responder otra pregunta: no *cuántas veces* aparece cada valor, sino **en qué posición del arreglo ordenado termina cada elemento**. Las sumas prefijo dan esa información a partir de las cuentas.

Si `conteo[v]` guarda la frecuencia de `v`, acumular hacia la derecha da la cantidad de elementos menores o iguales a `v`:

$$\text{conteo}[v] \leftarrow \text{conteo}[v] + \text{conteo}[v-1]$$

Después de ese recorrido, `conteo[v]` es la cantidad de elementos $\leq v$; en otras palabras, la **posición final** (contando desde 1) del último elemento que vale `v`. En un arreglo indexado desde 0, ese último elemento va en el índice `conteo[v] - 1`, y los elementos anteriores de ese mismo valor van en los índices inmediatamente anteriores. El arreglo de conteo deja de guardar cuentas y pasa a guardar **posiciones**.

Por ejemplo, con el arreglo `[6, 1, 2, 3, 0, 2, 5, 1, 3, 5]` y $k = 6$:

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort-prefijos_light.svg
---
class: only-light-mode
width: 100%
---
De cuentas a posiciones finales: las sumas prefijo indican dónde termina el bloque de cada valor y el recorrido de derecha a izquierda preserva el orden de los repetidos. La letra de cada celda identifica el elemento de origen: así se ve que los valores repetidos conservan su orden de aparición.
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort-prefijos_dark.svg
---
class: only-dark-mode
width: 100%
---
De cuentas a posiciones finales: las sumas prefijo indican dónde termina el bloque de cada valor y el recorrido de derecha a izquierda preserva el orden de los repetidos. La letra de cada celda identifica el elemento de origen: así se ve que los valores repetidos conservan su orden de aparición.
```

En la fila de sumas prefijo, `conteo[3] = 7` indica que hay 7 elementos $\leq 3$, así que el **último** `3` ocupa el índice `7 - 1 = 6`; los elementos anteriores de ese bloque van en los índices previos. Notar que `conteo[4] = 7` también, porque no hay elementos con ese valor: el bloque del valor `4` es vacío.

**Cómo se reconstruye el arreglo ordenado.** Ya no hace falta recorrer el arreglo de conteo: se recorre el **arreglo original** y, para cada elemento, se calcula su posición con `conteo[valor] - 1`. Después de colocarlo se decrementa `conteo[valor]`, para que el siguiente elemento con el mismo valor use la posición libre anterior.

```{table} Colocación recorriendo el arreglo original de derecha a izquierda
|  i  | arreglo[i] | conteo[arreglo[i]] | posición | salida parcial            |
| :-: | :--------: | :----------------: | :------: | :------------------------ |
|  9  |     5      |         9          |    8     | `[_, _, _, _, _, _, _, _, 5, _]` |
|  8  |     3      |         7          |    6     | `[_, _, _, _, _, _, 3, _, 5, _]` |
|  7  |     1      |         3          |    2     | `[_, _, 1, _, _, _, 3, _, 5, _]` |
|  6  |     5      |         8          |    7     | `[_, _, 1, _, _, _, 3, 5, 5, _]` |
|  5  |     2      |         5          |    4     | `[_, _, 1, _, 2, _, 3, 5, 5, _]` |
|  4  |     0      |         1          |    0     | `[0, _, 1, _, 2, _, 3, 5, 5, _]` |
|  3  |     3      |         6          |    5     | `[0, _, 1, _, 2, 3, 3, 5, 5, _]` |
|  2  |     2      |         4          |    3     | `[0, _, 1, 2, 2, 3, 3, 5, 5, _]` |
|  1  |     1      |         2          |    1     | `[0, 1, 1, 2, 2, 3, 3, 5, 5, _]` |
|  0  |     6      |         10         |    9     | `[0, 1, 1, 2, 2, 3, 3, 5, 5, 6]` |
```

Observar los dos `3`: se colocan de atrás hacia adelante (primero el de `i = 8` en el índice 6, después el de `i = 3` en el índice 5), así que el que estaba antes en la entrada queda antes en la salida. Lo mismo pasa con los `1`, los `2` y los `5`. Eso es lo que se llama estabilidad.

**Por qué se recorre de atrás hacia adelante.** Con `conteo[valor] - 1` se toma siempre la **última** posición libre del bloque de ese valor. Recorriendo la entrada desde el final, el último elemento de cada grupo es el primero en colocarse (en la última posición del bloque) y los anteriores se ubican en las posiciones previas, preservando el orden de aparición. Si se recorriera de izquierda a derecha con la misma fórmula, los elementos iguales quedarían en orden inverso: el arreglo seguiría ordenado, pero dejaría de ser estable.

```{code-block} text
---
caption: Counting Sort estable (sumas prefijo)
linenos: true
---
FUNCION CountingSortEstable(arreglo, k)
    n ← longitud(arreglo)
    salida ← arreglo de tamaño n
    conteo ← arreglo de tamaño k+1 inicializado en 0

    // 1. Contar apariciones
    PARA i ← 0 HASTA n-1 HACER
        conteo[arreglo[i]] ← conteo[arreglo[i]] + 1
    FIN PARA

    // 2. Sumas prefijo: conteo[v] pasa a ser la cantidad de elementos <= v,
    //    o sea la posición final (desde 1) del último elemento de valor v
    PARA v ← 1 HASTA k HACER
        conteo[v] ← conteo[v] + conteo[v-1]
    FIN PARA

    // 3. Colocar de derecha a izquierda: cada elemento entra al final de su
    //    bloque y el contador retrocede para el siguiente elemento igual
    PARA i ← n-1 HASTA 0 PASO -1 HACER
        valor ← arreglo[i]
        salida[conteo[valor] - 1] ← arreglo[i]
        conteo[valor] ← conteo[valor] - 1
    FIN PARA

    RETORNAR salida
FIN FUNCION
```

```{admonition} La versión estable no puede escribir sobre la entrada
---
class: note
---
La colocación lee `arreglo[i]` mientras escribe en `salida`, así que necesita un arreglo de salida propio: no se puede reutilizar la entrada como en la versión básica. El espacio extra es $O(n)$ para la salida más $O(k)$ para el arreglo de conteo.
```

<div class="only-html">

A continuación se puede visualizar paso a paso el funcionamiento de Counting Sort con sus dos variantes. Los botones **Inestable** y **Estable** permiten elegir cuál animar; cada elemento se muestra con una letra que identifica su posición de origen, de modo que se pueda ver qué ocurre con los valores repetidos. En el modo inestable los repetidos terminan en orden inverso al de origen (el algoritmo básico no tiene información para desempatar); en el modo estable conservan el orden de origen. Se puede ingresar un arreglo de hasta 10 enteros no negativos separados por coma, o generar uno aleatorio con el botón **Aleatorio**. Los botones ◀ ▶ permiten avanzar paso a paso, y >> reproduce la animación automáticamente. La vista muestra el arreglo original, el arreglo de conteo y el arreglo ordenado.

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort_light.html" width="100%" height="560px" class="only-light-mode"></iframe>

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort_dark.html" width="100%" height="560px" class="only-dark-mode"></iframe>

</div>

### Complejidad

Las dos variantes son $O(n + k)$: se recorre el arreglo una vez para contar, se recorre el arreglo de conteo una vez para acumular las sumas prefijo (solo en la variante estable) y se recorre el arreglo una vez más para reconstruir o colocar. Es eficiente cuando $k$ es del orden de $n$ o menor. Si $k$ es mucho mayor que $n$, el arreglo de conteo se vuelve impracticable.

- **Estable**: la variante con sumas prefijo, sí; la básica, no.
- **_In Place_**: no. El arreglo de conteo requiere $O(k)$ en ambas variantes. La versión básica puede escribir la salida sobre la entrada y no suma espacio; la versión estable necesita un arreglo de salida de $O(n)$ porque lee la entrada mientras coloca.

## Ordenamiento por Urnas (_Bucket Sort_)

El **Ordenamiento por Urnas** distribuye los elementos en varios *buckets* (urnas o cubos), ordena cada *bucket* individualmente y luego concatena los resultados. Es especialmente útil cuando los datos están uniformemente distribuidos en un rango conocido.

1. **División en *buckets***: Dividir el rango de los datos en $k$ intervalos.
2. **Distribución**: Colocar cada elemento en el *bucket* correspondiente según su valor.
3. **Ordenamiento intra-bucket**: Ordenar cada *bucket* individualmente (típicamente con Inserción o Counting Sort si los datos lo permiten).
4. **Concatenación**: Concatenar los *buckets* en orden para obtener el arreglo ordenado.

```{code-block} text
---
linenos: true
caption: Bucket Sort (Ordenamiento por Urnas)
---
FUNCION BucketSort(arreglo, k)
    buckets ← arreglo de k buckets vacíos
    n ← longitud(arreglo)
    max ← máximo valor en arreglo
    min ← mínimo valor en arreglo
    rango ← (max - min + 1) / k

    PARA i ← 0 HASTA n-1 HACER
        indice ← PISO((arreglo[i] - min) / rango)
        SI indice >= k ENTONCES
            indice ← k - 1
        FIN SI
        agregar arreglo[i] a buckets[indice]
    FIN PARA

    PARA i ← 0 HASTA k-1 HACER
        Ordenar(buckets[i])   // Ej: Inserción
    FIN PARA

    resultado ← arreglo vacío
    PARA i ← 0 HASTA k-1 HACER
        PARA cada elemento en buckets[i] HACER
            agregar elemento a resultado
        FIN PARA
    FIN PARA

    RETORNAR resultado
FIN FUNCION
```

<div class="only-html">

A continuación se puede visualizar paso a paso el funcionamiento de Bucket Sort.
Se puede ingresar un arreglo de hasta 10 números reales en $[0, 1)$ separados por coma, o generar uno
aleatorio. La vista muestra los *buckets* como columnas, el proceso de distribución,
el ordenamiento intra-bucket y la concatenación final.

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/bucket-sort_light.html" width="100%" height="560px" class="only-light-mode"></iframe>

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/bucket-sort_dark.html" width="100%" height="560px" class="only-dark-mode"></iframe>

</div>

### Complejidad

La complejidad del **Ordenamiento por Urnas** es $O(n + k)$ en promedio, donde $n$ es la cantidad de elementos y $k$ la cantidad de *buckets*. En el peor caso, si todos los elementos caen en un mismo *bucket*, la complejidad es la del algoritmo de ordenamiento intra-bucket (típicamente $O(n^2)$ si se usa Inserción).

- **Estable**: sí, si el algoritmo intra-bucket es estable.
- **_In Place_**: no, requiere espacio para los *buckets*.

## Radix Sort

El **Radix Sort** ordena elementos procesándolos dígito por dígito, desde el menos significativo (LSD) hasta el más significativo (MSD). Utiliza un algoritmo de ordenamiento **estable** (como Counting Sort o Bucket Sort) como subrutina para ordenar por cada dígito. En la práctica se usa la variante estable de Counting Sort de la sección anterior: la que convierte las cuentas en posiciones con sumas prefijo y coloca recorriendo la entrada de derecha a izquierda.

1. **Identificación del dígito menos significativo**: Comenzar con la posición de dígito $d = 0$ (unidades).
2. **Ordenamiento estable**: Ordenar los elementos según el dígito en la posición $d$ usando un algoritmo estable.
3. **Repetir**: Incrementar $d$ y repetir hasta procesar todos los dígitos del valor más grande.

```{code-block} text
---
linenos: true
caption: Radix Sort (LSD)
---
FUNCION RadixSort(arreglo)
    max ← máximo valor en arreglo
    exp ← 1

    MIENTRAS max / exp > 0 HACER
        CountingSortPorDigito(arreglo, exp)
        exp ← exp * 10
    FIN MIENTRAS

    RETORNAR arreglo
FIN FUNCION

FUNCION CountingSortPorDigito(arreglo, exp)
    n ← longitud(arreglo)
    salida ← arreglo de tamaño n
    conteo ← arreglo de tamaño 10 inicializado en 0

    PARA i ← 0 HASTA n-1 HACER
        digito ← PISO(arreglo[i] / exp) MOD 10
        conteo[digito] ← conteo[digito] + 1
    FIN PARA

    // Sumas prefijo para hacerlo estable
    PARA i ← 1 HASTA 9 HACER
        conteo[i] ← conteo[i] + conteo[i - 1]
    FIN PARA

    // Recorrer de derecha a izquierda para estabilidad
    PARA i ← n-1 HASTA 0 PASO -1 HACER
        digito ← PISO(arreglo[i] / exp) MOD 10
        salida[conteo[digito] - 1] ← arreglo[i]
        conteo[digito] ← conteo[digito] - 1
    FIN PARA

    // Copiar salida en arreglo original
    PARA i ← 0 HASTA n-1 HACER
        arreglo[i] ← salida[i]
    FIN PARA
FIN FUNCION
```

<div class="only-html">

A continuación se puede visualizar paso a paso el funcionamiento de Radix Sort
sobre cadenas alfanuméricas de 6 caracteres (0-9, A-Z). Se puede ingresar un
arreglo de hasta 10 cadenas separadas por coma, o generar una aleatoria.
La vista resalta la posición actual y muestra el conteo por carácter y la
colocación estable para cada dígito.

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/radix-sort_light.html" width="100%" height="500px" class="only-light-mode"></iframe>

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/radix-sort_dark.html" width="100%" height="500px" class="only-dark-mode"></iframe>

</div>

### Complejidad

La complejidad del **Radix Sort** es $O(n \times d)$, donde $n$ es la cantidad de elementos y $d$ la cantidad de dígitos del valor más grande. Si $d$ es constante (por ejemplo, enteros de 32 bits), la complejidad es $O(n)$.

- **Estable**: sí, porque usa una subrutina estable en cada paso.
- **_In Place_**: no, requiere espacio auxiliar para la subrutina estable.

## Comparación

```{table} Algoritmos de Ordenamiento Lineal
| Algoritmo                    | Complejidad     | Estable | In Place | Requisito                          |
| :--------------------------- | :-------------: | :-----: | :------: | :--------------------------------- |
| Counting Sort (básico)       | $O(n + k)$      | No      | No*      | Rango acotado $[0, k]$             |
| Counting Sort (con prefijos) | $O(n + k)$      | Sí      | No       | Rango acotado $[0, k]$             |
| Bucket Sort                  | $O(n + k)$      | Sí**    | No       | Distribución uniforme              |
| Radix Sort                   | $O(n \times d)$ | Sí      | No       | Valores descomponibles en dígitos  |
```

\* La versión básica puede escribir la salida sobre el arreglo de entrada, pero igual necesita $O(k)$ para el arreglo de conteo.
\*\* Si el algoritmo intra-bucket es estable.

## Ejercicios

Los ejercicios de este capítulo están en el directorio
`07-ordenamientos-lineales/ejercicios/`
del repositorio
`taller-algoritmos`.
Cada ejercicio tiene un esqueleto con `// TODO` y su correspondiente batería de tests.
Para resolverlos, clonar el repositorio, completar las funciones y ejecutar `go test ./...`.

[^omega]: La notación $\Omega$ (Omega grande) es la contraparte de $O$ (O grande) que vimos en el capítulo {ref}`analisis-algoritmos`. Mientras que $O$ establece una **cota superior** ($T(n) \leq c \cdot f(n)$), $\Omega$ establece una **cota inferior** ($T(n) \geq c \cdot g(n)$). Decir que un algoritmo requiere $\Omega(n \log n)$ significa que, para entradas suficientemente grandes, necesita **al menos** del orden de $n \log n$ operaciones; ningún algoritmo basado en comparaciones puede hacerlo mejor en el peor caso.
