---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Ordenamientos en Tiempo Lineal

Los algoritmos de ordenamiento en tiempo lineal son una alternativa eficiente para ordenar datos cuando se cumplen ciertas condiciones sobre los valores de los elementos. A diferencia de los algoritmos de ordenamiento basados en comparaciones, que tienen una cota inferior de $O(n \log n)$, los algoritmos de tiempo lineal pueden lograr una complejidad de $O(n+k)$ o $O(n \times k)$ donde $k$ es un factor relacionado con el rango de los valores o el número de dígitos.

Vamos a profundizar en los algoritmos más conocidos: **Ordenamiento por Conteo (_Counting Sort_)**, **Ordenamiento por Urnas (_Bucket Sort_)** y **Radix Sort**.

## Ordenamiento por Conteo (_Counting Sort_)

El **Ordenamiento por Conteo** es un algoritmo que se utiliza para ordenar elementos enteros dentro de un rango conocido. Funciona contando la cantidad de veces que aparece cada valor y luego reconstruyendo el arreglo ordenado a partir de estas cuentas. Por ejemplo supongamos que tenemos un arreglo de $N$ números enteros pero todos los números son del rango $[0, k]$ donde $k$ es un entero positivo. El algoritmo sigue estos pasos:

1. **Inicialización**: Crear un arreglo de conteo de tamaño $k+1$ (para incluir el valor $k$) e inicializarlo a cero.
2. **Conteo**: Recorrer el arreglo original y para cada elemento incrementar su posición correspondiente en el arreglo de conteo.
3. **Reconstrucción**: Recorrer el arreglo de conteo y reconstruir el arreglo ordenado agregando cada valor tantas veces como se contó.
4. **Resultado**: El arreglo resultante estará ordenado.

### Ejemplo de Ordenamiento por Conteo

Supongamos que tenemos el siguiente arreglo de números enteros:

```text
[4, 2, 2, 8, 3, 3, 1]
```

El proceso de ordenamiento por conteo sería:

1. **Inicialización**: Crear un arreglo de conteo de tamaño $9$ (para los valores del $0$ al $8$):

   ```text
   conteo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ```

2. **Conteo**: Recorrer el arreglo original y actualizar el arreglo de conteo:

   ```text
   conteo = [0, 1, 2, 2, 1, 0, 0, 0, 1]
   ```

3. **Reconstrucción**: Recorrer el arreglo de conteo y reconstruir el arreglo ordenado:

   ```text
   ordenado = [1, 2, 2, 3, 3, 4, 8]
   ```

4. **Resultado**: El arreglo ordenado es:

   ```text
   [1, 2, 2, 3, 3, 4, 8]
   ```

### Complejidad del Ordenamiento por Conteo

La complejidad del **Ordenamiento por Conteo** es $O(n + k)$, donde $n$ es el número de elementos a ordenar y $k$ es el rango de los valores. Este algoritmo es eficiente cuando $k$ es a lo sumo del orden de $n$.

## Ordenamiento por Urnas (_Bucket Sort_)

El **Ordenamiento por Urnas** es un algoritmo que distribuye los elementos en varios "buckets" o cubos, eventualmente ordena cada cubo individualmente y luego concatena los resultados. Es especialmente útil cuando los datos están uniformemente distribuidos. El proceso es el siguiente:

1. **División en Buckets**: Dividir el rango de los datos en $k$ intervalos (buckets).
2. **Distribución**: Colocar cada elemento en el bucket correspondiente según su valor.
3. **Concatenación**: Concatenar los elementos de todos los buckets para obtener el arreglo ordenado.

```{Note}
En algunos casos, cada una de las urnas se pueden ordenar utilizando otro algoritmo de ordenamiento, como el **Ordenamiento por Inserción** o el **Ordenamiento por Conteo**, dependiendo de la naturaleza de los datos en cada urna.
```

### Ejemplo de Ordenamiento por Urnas

Supongamos que tenemos una lista de enteros, pero los enteros están el rango de $[0, 9]$ y queremos ordenarlos utilizando el **Ordenamiento por Urnas**. El proceso sería:

```text
[0 ,3, 4,1, 9, 7, 8 ,8, 1, 3, 7, 2, 5, 6, 4, 9]
```

1. **División en Buckets**: Dividimos el rango de $[0, 9]$ en 10 buckets:

   ```text
   buckets = [[], [], [], [], [], [], [], [], [], []]
   ```

2. **Distribución**: Colocamos cada elemento en el bucket correspondiente:

   ```text
   buckets = [[0], [1, 1], [2], [3, 3], [4, 4], [5], [6], [7, 7], [8, 8], [9, 9]]
   ```

3. **Concatenación**: Concatenamos los elementos de todos los buckets para obtener el arreglo ordenado:

   ```text
   ordenado = [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9]
   ```

### Otro ejemplo de Ordenamiento por Urnas donde hay que ordenar los elementos dentro de cada bucket

Supongamos que tenemos el siguiente arreglo de números reales en el rango de $[0, 1]$:

```text
[0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.82]
```

1. **División en Buckets**: Dividimos el rango de $[0, 1]$ en 5 buckets, donde en cada bucket se almacenarán los números en el rango de $[0, 0.2)$, $[0.2, 0.4)$, $[0.4, 0.6)$, $[0.6, 0.8)$ y $[0.8, 1]$:

   ```text
   buckets = [[], [], [], [], []]
   ```

2. **Distribución**: Colocamos cada elemento en el bucket correspondiente:

   ```text
   buckets = [[0.17], [0.39, 0.26, 0.21], [], [0.78], [0.94, 0.82]]
   ```

3. **Ordenamiento de Buckets**: Ordenamos cada bucket individualmente, por ejemplo, utilizando el **Ordenamiento por Inserción**. En este caso sólo necesitamos ordenar el segundo y el último bucket:

   ```text
   buckets = [[0.17], [0.21, 0.26, 0.39], [], [0.78], [0.82, 0.94]]
   ```

4. **Concatenación**: Concatenamos los elementos de todos los buckets para obtener el arreglo ordenado:

   ```text
   ordenado = [0.17, 0.21, 0.26, 0.39, 0.78, 0.82, 0.94]
   ```

### Complejidad del Ordenamiento por Urnas

La complejidad del **Ordenamiento por Urnas** es $O(n + k)$, donde $n$ es el número de elementos a ordenar y $k$ es el número de buckets. Este algoritmo es eficiente cuando los datos están uniformemente distribuidos y el número de buckets es razonable en comparación con el número de elementos a ordenar.

El **Ordenamiento por Urnas** es un algoritmo **estable**, lo que significa que los elementos con el mismo valor mantienen su orden relativo después del ordenamiento.

## Radix Sort

El **Radix Sort** es un algoritmo de ordenamiento que se basa en ordenar los números dígito por dígito, comenzando desde el dígito menos significativo hasta el más significativo. Es especialmente útil para ordenar números enteros o cadenas de caracteres. El proceso es el siguiente:

1. **Identificación del Dígito Menos Significativo**: Comenzar con el dígito menos significativo (LSD).
2. **Ordenamiento por Conteo**: Utilizar el **Ordenamiento por Conteo** para ordenar los números según el dígito actual.
3. **Repetir para Cada Dígito**: Repetir el proceso para cada dígito, avanzando hacia el dígito más significativo (MSD).

### Ejemplo de Radix Sort

Supongamos que tenemos el siguiente arreglo de cadenas de caracteres:

```text
[ZAB, BCA, ACD, DBE, ZEF, CBA]
```

El proceso de Radix Sort sería:

1. **Identificación del Dígito Menos Significativo**: Comenzamos con el último carácter de cada cadena.

2. **Ordenamiento por Urnas**: Utilizamos el **Ordenamiento por Urnas** para ordenar las cadenas según el último carácter. La primera pasada se ordenan todos los elementos solo por el último carácter:

   ```text
   [BCA, CBA, ZAB, ACD, DBE, ZEF]
   ```

3. **Repetir para Cada Dígito**: Ahora repetimos el proceso para el caracter del centro:

   ```text
   [ZAB, CBA, DBE, BCA, ACD, ZEF]
   ```

4. **Repetir para el Primer Dígito**: Finalmente, ordenamos por el primer carácter:

   ```text
   [ACD, BCA, CBA, DBE, ZAB, ZEF]
   ```

### Complejidad del Radix Sort

La complejidad del **Radix Sort** es $O(n \times k)$, donde $n$ es el número de elementos a ordenar y $k$ es el número de dígitos en el valor más grande. Este algoritmo es eficiente cuando el número de dígitos es pequeño en comparación con el número de elementos a ordenar.

Es importante destacar que el algoritmo que se usa para ordenar los dígitos, en este caso el **Ordenamiento por Urnas**, debe ser un algoritmo estable para que el Radix Sort funcione correctamente. Esto significa que los elementos con el mismo valor deben mantener su orden relativo después de cada paso de ordenamiento.

## Ejercicios

1. Ordenar en lápiz y papel el siguiente arreglo de números enteros utilizando el **Ordenamiento por Conteo**:

   ```text
   [5, 2, 9, 1, 5, 6]
   ```

2. Implementar el **Ordenamiento por Urnas** para ordenar el siguiente arreglo de números reales en el rango de $[0, 1]$ de mayor a menor:

   ```text
   [0.42, 0.32, 0.24, 0.56, 0.78, 0.12]
   ```

3. Utilizar el **Radix Sort** para ordenar el siguiente arreglo de números enteros de mayor a menor:

   ```text
   [170, 45, 75, 90, 802, 24, 2, 66]
   ```

4. Investigar otra variante del **Radix Sort** que empiece a ordenar por el dígito más significativo (MSD) en lugar del menos significativo (LSD) y explicar sus diferencias.
