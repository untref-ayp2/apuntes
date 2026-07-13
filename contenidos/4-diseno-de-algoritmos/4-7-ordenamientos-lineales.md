---
label: ordenamientos-lineales
---

# Ordenamientos en Tiempo Lineal

Los algoritmos de ordenamiento del capítulo anterior (Mergesort, Quicksort, Heapsort) se basan en **comparaciones** entre elementos para determinar su orden. Se puede demostrar que cualquier algoritmo de ordenamiento basado en comparaciones requiere al menos $\Omega(n \log n)$ operaciones en el peor caso[^omega]. Esto significa que ningún algoritmo de este tipo puede superar esa cota, sin importar cuán ingenioso sea su diseño.

Sin embargo, si explotamos propiedades específicas de los datos —como que los valores pertenecen a un rango acotado, que están uniformemente distribuidos, o que se pueden descomponer en dígitos— podemos diseñar algoritmos que ordenen en **tiempo lineal** $O(n)$, superando la barrera de $\Omega(n \log n)$. La clave está en que estos algoritmos **no comparan** elementos entre sí: usan los valores como índices, los distribuyen en *buckets* o los procesan dígito a dígito.

Vamos a estudiar tres algoritmos de ordenamiento en tiempo lineal: **Ordenamiento por Conteo (_Counting Sort_)**, **Ordenamiento por Urnas (_Bucket Sort_)** y **Radix Sort**.

## Ordenamiento por Conteo (_Counting Sort_)

El **Ordenamiento por Conteo** ordena elementos enteros dentro de un rango conocido $[0, k]$. En lugar de comparar elementos, cuenta cuántas veces aparece cada valor y luego reconstruye el arreglo ordenado a partir de esas cuentas. El algoritmo sigue estos pasos:

1. **Inicialización**: Crear un arreglo de conteo de tamaño $k+1$ e inicializarlo a cero.
2. **Conteo**: Recorrer el arreglo original y para cada elemento incrementar su posición correspondiente en el arreglo de conteo.
3. **Reconstrucción**: Recorrer el arreglo de conteo y escribir cada valor tantas veces como se contó.

```{code-block} text
---
linenos: true
caption: Counting Sort (Ordenamiento por Conteo)
---
FUNCION CountingSort(arreglo, k)
    conteo ← arreglo de tamaño k+1 inicializado en 0
    n ← longitud(arreglo)

    PARA i ← 0 HASTA n-1 HACER
        valor ← arreglo[i]
        conteo[valor] ← conteo[valor] + 1
    FIN PARA

    indice ← 0
    PARA i ← 0 HASTA k HACER
        MIENTRAS conteo[i] > 0 HACER
            arreglo[indice] ← i
            indice ← indice + 1
            conteo[i] ← conteo[i] - 1
        FIN MIENTRAS
    FIN PARA

    RETORNAR arreglo
FIN FUNCION
```

<div class="only-html">

A continuación se puede visualizar paso a paso el funcionamiento de Counting Sort.
Se puede ingresar un arreglo de hasta 10 enteros no negativos separados por coma, o generar uno
aleatorio con el botón **Generar**. Los botones ◀ ▶ permiten avanzar paso a paso,
y >> reproduce la animación automáticamente. La vista muestra el arreglo original,
el arreglo de conteo y la reconstrucción del arreglo ordenado.

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort_light.html" width="100%" height="500px" class="only-light-mode"></iframe>

<iframe src="/applets/4-diseno-de-algoritmos/4-7-ordenamientos-lineales/counting-sort_dark.html" width="100%" height="500px" class="only-dark-mode"></iframe>

</div>

### Complejidad

La complejidad del **Ordenamiento por Conteo** es $O(n + k)$, donde $n$ es la cantidad de elementos y $k$ es el rango de valores. Es eficiente cuando $k$ es del orden de $n$ o menor. Si $k$ es mucho mayor que $n$, el arreglo de conteo se vuelve impracticable.

- **Estable**: sí, si se recorre el arreglo original de derecha a izquierda en la fase de reconstrucción (la versión presentada no es estable; la variante estable acumula sumas prefijo para determinar posiciones finales).
- **_In Place_**: no, requiere espacio adicional $O(k)$ para el arreglo de conteo.

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

El **Radix Sort** ordena elementos procesándolos dígito por dígito, desde el menos significativo (LSD) hasta el más significativo (MSD). Utiliza un algoritmo de ordenamiento **estable** (como Counting Sort o Bucket Sort) como subrutina para ordenar por cada dígito.

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
| Algoritmo      | Complejidad       | Estable | In Place | Requisito                          |
| :------------- | :---------------: | :-----: | :------: | :--------------------------------- |
| Counting Sort  | $O(n + k)$        | Sí*     | No       | Rango acotado $[0, k]$             |
| Bucket Sort    | $O(n + k)$        | Sí**    | No       | Distribución uniforme              |
| Radix Sort     | $O(n \times d)$   | Sí      | No       | Valores descomponibles en dígitos  |
```

\* La variante estable requiere recorrer de derecha a izquierda con sumas prefijo.
\*\* Si el algoritmo intra-bucket es estable.

## Ejercicios

Los ejercicios de este capítulo están en el directorio
[`07-ordenamientos-lineales/ejercicios/`](https://github.com/untref-ayp2/taller-algoritmos/tree/main/07-ordenamientos-lineales/ejercicios)
del repositorio
[`taller-algoritmos`](https://github.com/untref-ayp2/taller-algoritmos).
Cada ejercicio tiene un esqueleto con `// TODO` y su correspondiente batería de tests.
Para resolverlos, clonar el repositorio, completar las funciones y ejecutar `go test ./...`.

[^omega]: La notación $\Omega$ (Omega grande) es la contraparte de $O$ (O grande) que vimos en el capítulo {ref}`analisis-algoritmos`. Mientras que $O$ establece una **cota superior** ($T(n) \leq c \cdot f(n)$), $\Omega$ establece una **cota inferior** ($T(n) \geq c \cdot g(n)$). Decir que un algoritmo requiere $\Omega(n \log n)$ significa que, para entradas suficientemente grandes, necesita **al menos** del orden de $n \log n$ operaciones; ningún algoritmo basado en comparaciones puede hacerlo mejor en el peor caso.
